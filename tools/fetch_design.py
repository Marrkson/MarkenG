#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quellen für das Wissenspaket Designrecht beschaffen (Netz + Postgres) und als JSON unter data/ ablegen.

Erzeugt (alle mitversioniert, damit `build.py` ohne Netz und ohne Datenbank läuft):
  data/designg.json            Designgesetz (DesignG), alle Paragraphen mit Abschnittsgliederung und Absätzen (gesetze-im-internet.de, XML)
  data/designv.json            Designverordnung (DesignV)
  data/designrl.json           Richtlinie 98/71/EG über den rechtlichen Schutz von Mustern und Modellen (Cellar, PDF des Amtsblatts,
                               zweispaltig; Spalten werden je Seite getrennt), amtlicher Wortlaut mit Erwägungsgründen
  data/designrl2024.json       Richtlinie (EU) 2024/2823 über den rechtlichen Schutz von Designs (Neufassung; Cellar, XHTML)
  data/ggv.json                Verordnung (EG) Nr. 6/2002 über Unionsgeschmacksmuster in der konsolidierten Fassung vom 1.7.2026
                               (Cellar, XHTML; Änderungsmarken ►M2 … ◄ entfernt)
  data/design_decisions.json   Entscheidungen des BPatG (Design-Beschwerde- und Nichtigkeitssachen des 10. und 30. Senats) und des BGH
                               (I. Zivilsenat: Designsachen und Entscheidungen mit DesignG-/GeschmMG-Zitaten) aus der RheinIP-Datenbank

Die Verordnung (EU) 2024/2822 wird nicht als eigene Datei geführt: ihre Änderungen stecken in der konsolidierten GGV.

Aufruf:  python3 tools/fetch_design.py [--no-net] [--no-db]
Zwischenstände (XML-Zips, PDF, XHTML) liegen in ~/.cache/ipelico/design/. Postgres-Zugang: POSTGRES_LOGIN aus ~/github/RheinIP/.env.
"""
import collections
import html as htmlmod
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_patent as fp  # noqa: E402  (XML-Parser für gesetze-im-internet.de und Datenbankzugang)

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path.home() / ".cache" / "ipelico" / "design"
fp.CACHE = CACHE
UA = {"User-Agent": "Mozilla/5.0 (IPelico fetch_design)"}

GESETZE = [
    dict(key="designg", slug="geschmmg_2004", kurz="DesignG", datei="designg.json"),
    dict(key="designv", slug="designv", kurz="DesignV", datei="designv.json"),
]
CELLAR = "https://publications.europa.eu/resource/celex/"
EU = [
    dict(key="designrl", datei="designrl.json", kurz="DesignRL", art="pdf",
         url="http://publications.europa.eu/resource/cellar/399f8f58-0b0e-4252-a0a8-8c8600f55c5e.0004.02/DOC_1",
         gesetz="Richtlinie 98/71/EG des Europäischen Parlaments und des Rates vom 13. Oktober 1998 über den rechtlichen Schutz von Mustern und Modellen",
         quelle="https://eur-lex.europa.eu/eli/dir/1998/71/oj/deu", quelle_pdf="https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:31998L0071",
         stand="ABl. L 289 vom 28.10.1998, S. 28; wird mit Wirkung vom 9.12.2027 durch die Richtlinie (EU) 2024/2823 aufgehoben"),
    dict(key="designrl2024", datei="designrl2024.json", kurz="DesignRL 2024", art="xhtml", celex="32024L2823",
         gesetz="Richtlinie (EU) 2024/2823 des Europäischen Parlaments und des Rates vom 23. Oktober 2024 über den rechtlichen Schutz von Designs (Neufassung)",
         quelle="https://eur-lex.europa.eu/eli/dir/2024/2823/oj/deu", quelle_pdf="https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32024L2823",
         stand="ABl. L, 2024/2823, 18.11.2024; in Kraft seit 8.12.2024, Umsetzungsfrist 9.12.2027"),
    dict(key="ggv", datei="ggv.json", kurz="GGV", art="xhtml", celex="02002R0006-20260701",
         gesetz="Verordnung (EG) Nr. 6/2002 des Rates vom 12. Dezember 2001 über Unionsgeschmacksmuster (konsolidierte Fassung)",
         quelle="https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02002R0006-20260701", quelle_pdf="https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:02002R0006-20260701",
         stand="Konsolidierte Fassung vom 1.7.2026 (geändert durch die Verordnung (EU) 2024/2822; Titel seit 1.5.2025 „Unionsgeschmacksmuster“)"),
]


def fetch(url, target, net, headers=None):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 1000:
        return target.read_bytes()
    if not net:
        raise SystemExit("fehlt im Cache und --no-net gesetzt: %s" % target.name)
    data = urllib.request.urlopen(urllib.request.Request(url, headers={**UA, **(headers or {})}), timeout=120).read()
    target.write_bytes(data)
    return data


# ---------------------------------------------------------------- XHTML (Cellar) -> Artikel
_TAG = re.compile(r"<[^>]+>")
_MARK = re.compile(r"[►▼◄]\s*[MBC]?\d*\s*")


def _text(html):
    html = re.sub(r"\s+", " ", html)                                       # Quellformatierung (Einrückung) ist keine Zeilenstruktur
    html = re.sub(r"<span class=\"superscript\">.*?</span>", "", html)
    html = re.sub(r"<a\b[^>]*>.*?</a>", "", html)                          # ►M2-Verweise auf den Änderungsrechtsakt, Fußnotenanker
    html = re.sub(r"<td\b[^>]*>(.*?)</td>", lambda m: _TAG.sub("", m.group(1)) + " ", html)   # Listenzellen „a)“ + Text in einer Zeile
    html = re.sub(r"<div class=\"list grid-list-column-1\">(.*?)</div>", lambda m: _TAG.sub("", m.group(1)) + " ", html)
    html = re.sub(r"</(?:p|div|tr|li|table)>", "\n", html)
    html = re.sub(r"<br\s*/?>", "\n", html)
    s = htmlmod.unescape(_TAG.sub("", html)).replace("\xa0", " ")
    s = _MARK.sub("", s)
    s = re.sub(r"\(\s*\)", "", s)                                         # Reste entfernter Fußnotenanker
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in s.split("\n")]
    return [ln for ln in lines if ln]


_ABS = re.compile(r"^\((\d+[a-z]?)\)\s*")


def _absaetze(lines):
    absaetze, cur = [], None
    for t in lines:
        m = _ABS.match(t)
        if m:
            if cur:
                absaetze.append(cur)
            cur = dict(nr=m.group(1), text=t[m.end():])
        elif cur:
            cur["text"] += "\n" + t
        else:
            cur = dict(nr=None, text=t)
    if cur:
        absaetze.append(cur)
    return absaetze


_HEAD = re.compile(r"<p[^>]*class=\"(oj-ti-section-[12]|title-division-[12])\"[^>]*>(.*?)</p>|<div class=\"eli-subdivision\" id=\"(art_\w+|rct_\d+)\">", re.S)
_GLIED = re.compile(r"^(TITEL|KAPITEL|Abschnitt|\d+\. Abschnitt)\b", re.I)


def parse_xhtml(html):
    body = html[html.find("<body"):]
    heads = list(_HEAD.finditer(body))
    artikel, erw = [], []
    teil = abschnitt = None
    pending = None
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        if m.group(1):
            t = " ".join(_text(m.group(2)))
            if not t:
                continue
            if pending:
                lvl, lab = pending
                pending = None
                if lvl == 1:
                    teil, abschnitt = lab + " – " + t, None
                else:
                    abschnitt = lab + " – " + t
            elif _GLIED.match(t):
                pending = (1 if t.upper().startswith(("TITEL", "KAPITEL")) else 2, t)
            continue
        ident = m.group(3)
        chunk = body[m.end():end]
        # Artikel enden vor dem nächsten Abschnitt oder Artikel; Anhänge werden nicht erfasst
        if ident.startswith("rct_"):
            lines = _text(chunk)
            if lines:
                mm = _ABS.match(lines[0])
                erw.append(dict(nr=mm.group(1) if mm else str(len(erw) + 1), text=(lines[0][mm.end():] if mm else lines[0]) + ("\n" + "\n".join(lines[1:]) if lines[1:] else "")))
            continue
        nr = ident[4:]
        tm = re.search(r"<p class=\"(?:oj-sti-art|stitle-article-norm)\">(.*?)</p>", chunk, re.S)
        titel = " ".join(_text(tm.group(1))) if tm else ""
        rest = chunk[tm.end():] if tm else chunk
        rest = re.sub(r"<p[^>]*class=\"(?:oj-ti-art|title-article-norm)\"[^>]*>.*?</p>", "", rest, flags=re.S)
        absaetze = _absaetze(_text(rest))
        if not absaetze:
            continue
        artikel.append(dict(nr=nr, titel=titel, kapitel=teil or "Allgemeines", abschnitt=abschnitt, absaetze=absaetze))
    return artikel, erw


# ---------------------------------------------------------------- PDF (zweispaltiges Amtsblatt 1998) -> Artikel
def _pages(pdf):
    """Zweispaltiges Amtsblatt: jede Seite wird links und rechts der Seitenmitte getrennt extrahiert (pdftotext -x/-W)."""
    info = subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    w, h = (float(x) for x in re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
    mid = int(w / 2)
    lines = []
    for p in range(1, pages + 1):
        for x, width in ((0, mid), (mid, int(w) - mid)):
            txt = subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), "-x", str(x), "-y", "0", "-W", str(width), "-H", str(int(h)), str(pdf), "-"],
                                 check=True, capture_output=True, text=True).stdout
            lines.extend(ln.strip() for ln in txt.split("\n"))
    return lines


_ART = re.compile(r"^Artikel (\d+)$")


def parse_pdf(pdf):
    lines = _pages(pdf)
    kopf = re.compile(r"^(L 289/\d+|\d+\. \d+\. \d+)\s+DE\s+Amtsblatt|Gemeinschaften\s+(L 289/\d+|\d+\. \d+\. \d+)$|^(L 289/\d+|\d+\. \d+\. \d+|DE)$")
    lines = [ln for ln in lines if ln and not kopf.search(ln)]
    # Erwägungsgründe: von „in Erwägung nachstehender Gründe“ bis „HABEN FOLGENDE RICHTLINIE ERLASSEN“
    try:
        a = next(i for i, ln in enumerate(lines) if ln.startswith("in Erwägung nachstehender Gründe"))
        b = next(i for i, ln in enumerate(lines) if ln.startswith("HABEN FOLGENDE RICHTLINIE ERLASSEN"))
    except StopIteration:
        raise SystemExit("Erwägungsgründe nicht gefunden")
    erw_lines, skip = [], False   # Fußnoten (Fundstellen im ABl.) stehen am Fuß der Spalte und beginnen mit „(1) ABl.“ / „(3) Stellungnahme“
    for ln in lines[a + 1:b]:
        if re.match(r"^\(\d\) (ABl\.|Stellungnahme)", ln):
            skip = True
        elif skip and re.match(r"^\(\d+\)\s+[A-ZÄÖÜ]", ln):
            skip = False
        if not skip:
            erw_lines.append(ln)
    erw = _absaetze(_join_hyphen(erw_lines))
    erw = [e for e in erw if e["nr"]]
    # Artikel in Dokumentreihenfolge: Kopfzeile „Artikel n“ allein, gefolgt von einer Titelzeile
    body = lines[b + 1:]
    idx = [i for i, ln in enumerate(body) if _ART.match(ln) and i + 1 < len(body) and body[i + 1][:1].isupper()]
    artikel = []
    for k, i in enumerate(idx):
        end = idx[k + 1] if k + 1 < len(idx) else len(body)
        nr = _ART.match(body[i]).group(1)
        block = body[i + 1:end]
        # Titel: erste Zeile; Folgezeilen gehören zum Titel, wenn sie klein beginnen („und Muster von …“, „gegen die guten Sitten …“)
        titel, j = [block[0]], 1
        while j < len(block) and block[j][:1].islower() and not _ABS.match(block[j]):
            titel.append(block[j])
            j += 1
        text = _join_hyphen(block[j:])
        text = [ln for ln in text if not ln.startswith("Im Namen des") and not re.match(r"^Geschehen zu|^Der Präsident|^[A-Z]\. [A-Z]+$", ln)]
        absaetze = _absaetze(text)
        if absaetze:
            artikel.append(dict(nr=nr, titel=" ".join(titel), kapitel="Richtlinie 98/71/EG", abschnitt=None, absaetze=absaetze))
    artikel.sort(key=lambda a: int(a["nr"]))
    return artikel, erw


def _join_hyphen(lines):
    """Zeilenumbrüche innerhalb eines Absatzes zusammenführen (Absätze beginnen mit „(n)“, Buchstabenlisten mit „a)“)."""
    out = []
    for ln in lines:
        if out and not _ABS.match(ln) and not re.match(r"^[a-z]\) ", ln):
            prev = out[-1]
            if prev.endswith("-") and ln[:1].islower():
                out[-1] = prev[:-1] + ln
            else:
                out[-1] = prev + " " + ln
        else:
            out.append(ln)
    return out


# ---------------------------------------------------------------- Rechtsprechung (Postgres)
LAW_KEYS = {"DesignG": "designg", "GeschmMG": "geschmmg", "UrhG": "urhg", "UWG": "uwg", "MarkenG": "markeng", "PatKostG": "patkostg"}
SENAT_KURZ = {"Juristischer-Beschwerdesenat": "Juristischer Beschwerdesenat", "Marken- und Design-Beschwerdesenat": "Marken- und Design-Beschwerdesenat"}


def _verfahren(az, typ, gericht):
    if gericht == "BGH":
        return "Rechtsbeschwerde" if " ZB " in az else "Revision/Berufung" if " ZR " in az else "Sonstiges"
    if re.search(r"nichtigkeit", typ or "", re.I):
        return "Nichtigkeitsbeschwerde"
    if " ZA " in az:
        return "Kosten/Erinnerung"
    return "Beschwerde"


def build_decisions():
    cur = fp._db_cursor()
    cur.execute('select "decisionId", law, paragraph, bool_or(interpreted), sum(mentions) from "DeCourtNorm" where law = any(%s) group by 1, 2, 3', (list(LAW_KEYS),))
    raw = collections.defaultdict(list)
    for did, law, par, interp, ment in cur.fetchall():
        if par:
            raw[did].append((law, par, bool(interp), int(ment or 0)))

    def zitate(did, datum):
        z = collections.defaultdict(dict)
        for law, par, interp, ment in raw.get(did, []):
            key = LAW_KEYS[law]
            # Das GeschmMG 2004 ist das heutige DesignG mit gleicher Paragraphenzählung (Umbenennung 1.1.2014); ältere Zitate bleiben getrennt
            if law == "GeschmMG":
                key = "designg" if datum and datum >= "2004-06-01" else "geschmmg_alt"
            old = z[key].get(par)
            z[key][par] = dict(i=(old["i"] if old else False) or interp, m=(old["m"] if old else 0) + ment)
        return dict(z)

    out = []
    cur.execute('select id, url, "fileNumber", ecli, senate, "senateType", category, "decisionType", "caseType", "caseName", norms, "decisionDate", headnote '
                'from "BpatgDecision" where category = \'design\' order by "decisionDate", "fileNumber"')
    for did, url, az, ecli, senat, styp, cat, dtyp, ctyp, name, norms, date, head in cur.fetchall():
        datum = date.date().isoformat() if date else None
        out.append(dict(id=did, gericht="BPatG", az=fp._ws(az), ecli=ecli or "", senat=fp._ws(senat), senat_typ=SENAT_KURZ.get(styp or "", styp or "–"),
                        typ=dtyp or "", verfahren=_verfahren(az, ctyp, "BPatG"), sache=fp._ws(ctyp)[:160], name=fp._name(name), gebiet=cat,
                        datum=datum, leitsatz=fp._leitsatz(head), normen_text=fp._ws("; ".join(norms or []))[:300], url=url, zitate=zitate(did, datum)))
    cur.execute('select d.id, d.url, d."fileNumber", d.ecli, d.senate, d.category, d."decisionType", d."caseType", d."caseName", d.norms, d."decisionDate", d.headnote '
                'from "BghDecision" d where d.category = \'design\' or exists (select 1 from "DeCourtNorm" n where n."decisionId" = d.id and n.law in (\'DesignG\', \'GeschmMG\')) '
                'order by d."decisionDate", d."fileNumber"')
    for did, url, az, ecli, senat, cat, dtyp, ctyp, name, norms, date, head in cur.fetchall():
        datum = date.date().isoformat() if date else None
        out.append(dict(id=did, gericht="BGH", az=fp._ws(az), ecli=ecli or "", senat=fp._ws(senat), senat_typ=fp._ws(senat),
                        typ=dtyp or "", verfahren=_verfahren(az, ctyp, "BGH"), sache=fp._ws(ctyp)[:160], name=fp._name(name), gebiet=cat,
                        datum=datum, leitsatz=fp._leitsatz(head), normen_text=fp._ws("; ".join(norms or []))[:300], url=url, zitate=zitate(did, datum)))
    out.sort(key=lambda e: (e["datum"] or "", e["az"]))
    stat = collections.Counter(e["gericht"] for e in out)
    daten = sorted(e["datum"] for e in out if e["datum"])
    meta = dict(quelle="RheinIP-Datenbank, Tabellen BpatgDecision und BghDecision (Designsachen), Normzitate aus DeCourtNorm",
                anzahl=len(out), bpatg=stat["BPatG"], bgh=stat["BGH"], mit_leitsatz=sum(1 for e in out if e["leitsatz"]),
                zeitraum=[daten[0], daten[-1]] if daten else None,
                hinweis="BPatG: Beschwerden in Design- und Geschmacksmustersachen (Juristischer Beschwerdesenat, seit 2014 auch Nichtigkeitsbeschwerden zum "
                        "30. Senat); BGH: I. Zivilsenat. Normzitate sind maschinell aus dem Volltext erkannt (i = die Entscheidung legt die Norm aus); "
                        "Zitate des GeschmMG in Entscheidungen ab dem 1.6.2004 werden dem DesignG zugeordnet (gleiche Paragraphenzählung), ältere bleiben getrennt.")
    return dict(meta=meta, entscheidungen=out)


def main():
    net = "--no-net" not in sys.argv
    for g in GESETZE:
        d = fp.parse_gesetz(g, net)
        (DATA / g["datei"]).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print("%s: %d Vorschriften; %s" % (g["datei"], len(d["paragraphen"]), "; ".join(d["meta"]["stand"])[:100]))
    for e in EU:
        if e["art"] == "pdf":
            pdf = CACHE / (e["key"] + ".pdf")
            fetch(e["url"], pdf, net, {"Accept": "application/pdf"})
            artikel, erw = parse_pdf(pdf)
        else:
            x = CACHE / (e["key"] + ".xhtml")
            html = fetch(CELLAR + e["celex"], x, net, {"Accept": "application/xhtml+xml", "Accept-Language": "deu"}).decode("utf-8")
            artikel, erw = parse_xhtml(html)
        d = dict(gesetz=e["gesetz"], kurz=e["kurz"], meta=dict(stand=e["stand"], quelle=e["quelle"], quelle_pdf=e["quelle_pdf"]), artikel=artikel, erwaegungsgruende=erw)
        (DATA / e["datei"]).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print("%s: %d Artikel, %d Erwägungsgründe" % (e["datei"], len(artikel), len(erw)))
    if "--no-db" not in sys.argv:
        d = build_decisions()
        (DATA / "design_decisions.json").write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")
        print("design_decisions.json:", {k: v for k, v in d["meta"].items() if k != "hinweis"})
    else:
        print("design_decisions.json unverändert (--no-db)")


if __name__ == "__main__":
    main()
