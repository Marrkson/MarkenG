#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Englischer Wortlaut der Durchsetzungsrichtlinie 2004/48/EG (berichtigte Fassung, ABl. L 195 vom 2.6.2004) für die
englische EPG-App (docs/en/, knowledge/upc/en): data/durchsetzungsrl_en.json mit Artikeln wie data/upca.json
(nr, titel_en, absaetze_en, url_en).

Quelle: EU-Cellar per Content-Negotiation (PDF, zweispaltig); jede Seite wird in linke und rechte Spalte geschnitten
(`pdftotext -x/-W`), dann Kopfzeilen entfernt und Artikel und Absätze geparst. Die Absatzzahl jedes Artikels wird mit der
deutschen Fassung (knowledge/durchsetzungsrl.py) verglichen; Abweichungen brechen ab. Cache: ~/.cache/ipelico/eu/.
Aufruf: python3 tools/fetch_durchsetzungsrl_en.py [--no-net]
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from knowledge.durchsetzungsrl import ARTIKEL  # noqa: E402

CELLAR = "https://publications.europa.eu/resource/celex/32004L0048R%2801%29"
URL_EN = "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0048R(01)"
CACHE = Path.home() / ".cache" / "ipelico" / "eu" / "durchsetzungsrl_en.pdf"
OUT = ROOT / "data" / "durchsetzungsrl_en.json"
# Kopfzeile jeder Seite („L 195/22  EN  Official Journal of the European Union  2.6.2004“), an der Spaltengrenze zerschnitten
_HEAD = re.compile(r"^(?:L \d+/\d+|\d{1,2}\.\d{1,2}\.\d{4}|EN|Official Journal of th?e?|(?:t?h?e )?European Union|Official Journal of the European Union)$")


def pdf():
    if "--no-net" not in sys.argv and not CACHE.exists():
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(CELLAR, headers={"Accept": "application/pdf", "Accept-Language": "eng", "User-Agent": "Mozilla/5.0 (IPelico)"})
        CACHE.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return CACHE


def spalten(p):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout).group(1))
    out = []
    for page in range(1, n + 1):
        for x, w in ((0, 298), (298, 300)):
            col = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-x", str(x), "-y", "0", "-W", str(w), "-H", "842", str(p), "-"],
                                 capture_output=True, text=True, check=True).stdout.replace("\f", "").split("\n")
            head = [ln for ln in col[:8] if ln.strip() and not _HEAD.match(ln.strip())]
            out.append("\n".join(head + col[8:]) if len(head) < len([ln for ln in col[:8] if ln.strip()]) else "\n".join(col))
    return "\n".join(out)


def parse(text):
    lines = [ln.strip() for ln in text.split("\n")]
    body = "\n".join(lines)
    # Erwägungsgründe „(1) …“ bis „(32) …“ am Zeilenanfang, fortlaufend gezählt (Fußnoten „(1) OJ C …“ bleiben außen vor)
    rec, want, cuts = body[body.index("Whereas:"):body.index("HAVE ADOPTED THIS DIRECTIVE")], 1, []
    for m in re.finditer(r"(?m)^\((\d+)\)\s+(?!OJ\b)", rec):
        if int(m.group(1)) == want:
            cuts.append(m); want += 1
    erw = []
    for j, m in enumerate(cuts):
        t = rec[m.end():cuts[j + 1].start() if j + 1 < len(cuts) else len(rec)]
        t = re.sub(r"(?m)^\(\d+\)\s+OJ\b.*$", "", t)  # Fußnoten der Seite
        t = re.sub(r"\s*\n\s*", " ", t).strip()
        erw.append(dict(nr=str(j + 1), text=re.sub(r"(\w)- (\w)", r"\1\2", t)))
    body = body[body.index("HAVE ADOPTED THIS DIRECTIVE"):]
    body = body[:body.index("Done at Strasbourg")]
    # Absatzmarken des PDF am Zeilenanfang: „1. Member“, „1. .Member“, „.1 Member“, „3.\n\nThis“; gezählt wird nur die
    # jeweils nächste Nummer des Artikels (Fußnoten, Jahreszahlen, Aufzählungen bleiben Text)
    marke = re.compile(r"(?m)^\.?(\d{1,2})\.?\s*(?:\n\s*)*\.?(?=[A-Z‘“])")
    parts = re.split(r"(?m)^Article (\d+)\n", body)
    arts = []
    for i in range(1, len(parts), 2):
        nr, chunk = int(parts[i]), parts[i + 1].strip()
        titel, rest = (chunk.split("\n", 1) + [""])[:2]
        cuts, want = [], 1
        for m in marke.finditer(rest):
            if int(m.group(1)) == want:
                cuts.append((m.start(), m.end(), want))
                want += 1
        stuecke = [rest[:cuts[0][0]]] if cuts else [rest]
        stuecke = [s for s in stuecke if s.strip()]
        for j, (a, b, n) in enumerate(cuts):
            stuecke.append("%d. " % n + rest[b:cuts[j + 1][0] if j + 1 < len(cuts) else len(rest)])
        absaetze = []
        for s in stuecke:
            s = re.sub(r"\s*\n\s*", " ", s).strip()
            s = re.sub(r"\s+(?:CHAPTER [IVX]+|Section \d+)\b.*$", "", s)  # Überschrift des folgenden Kapitels/Abschnitts
            absaetze.append(re.sub(r"(\w)- (\w)", r"\1\2", s))
        arts.append(dict(nr=nr, titel=titel.strip(), absaetze=absaetze))
    return arts, erw


def main():
    arts, erw = parse(spalten(pdf()))
    from knowledge.durchsetzungsrl import ERWAEGUNGSGRUENDE
    if len(erw) != 32:
        raise SystemExit("Erwägungsgründe: %d statt 32 erkannt" % len(erw))
    erw = [e for e in erw if e["nr"] in {x["nr"] for x in ERWAEGUNGSGRUENDE}]  # dieselbe Auswahl wie die deutsche Fassung
    de = {int(a["nr"]): a for a in ARTIKEL}
    fehler = []
    for a in arts:
        d = de.get(a["nr"])
        if d and len(d["absaetze"]) != len(a["absaetze"]):
            fehler.append("Art. %d: %d Absätze englisch, %d deutsch" % (a["nr"], len(a["absaetze"]), len(d["absaetze"])))
    missing = sorted(set(de) - {a["nr"] for a in arts})
    if fehler or missing:
        raise SystemExit("Parser passt nicht zur deutschen Fassung:\n  " + "\n  ".join(fehler + ["fehlt: Art. %d" % m for m in missing]))
    meta = dict(titel="Directive 2004/48/EC on the enforcement of intellectual property rights (corrigendum, OJ L 195, 2.6.2004)",
                kurz="IPRED", quelle=CELLAR, url_en=URL_EN, hinweis="Official English text (corrected version), EU Cellar.")
    artikel = [dict(nr=a["nr"], titel=a["titel"], titel_en=a["titel"], absaetze_en=a["absaetze"], url_en=URL_EN) for a in arts]
    OUT.write_text(json.dumps(dict(meta=meta, artikel=artikel, erwaegungsgruende_en=erw), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(OUT.relative_to(ROOT), len(artikel), "Artikel")


if __name__ == "__main__":
    main()
