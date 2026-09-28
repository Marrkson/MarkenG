"""Holt den amtlichen Text des MarkenG (gesetze-im-internet.de, XML-Fassung `markeng/xml.zip`) und legt ihn
strukturiert unter data/markeng.json ab (mitversioniert; `build.py` läuft ohne Netz).

Ausgabe: Liste aller Paragraphen mit Gliederung (Teil / Abschnitt), Überschrift, Absätzen und Volltext.
Der XML-Parser ist derselbe wie für PatG, PatV, IntPatÜG und PatKostG (tools/fetch_patent.py).
Bis September 2026 kam der Text aus dem Markdown-Spiegel bundestag/gesetze (Stand 2018/2019); der war nach der
Neunummerierung (Unionsmarken §§ 119 bis 125a statt §§ 125b bis 125i, IR-Marken §§ 107 bis 118) veraltet.

Aufruf:  python3 src/parse_markeng.py      (XML-Zip im Cache ~/.cache/ipelico/patent/markeng.zip, sonst aus dem Netz)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "markeng.json"
sys.path.insert(0, str(ROOT / "tools"))

import fetch_patent  # noqa: E402


def _gliederung(s):
    """„Teil 3 Verfahren in Markenangelegenheiten“ -> „Teil 3 - Verfahren in Markenangelegenheiten“ (bisherige Schreibweise)."""
    return re.sub(r"^((?:Teil|Abschnitt) \d+[a-z]?) ", r"\1 - ", s) if s else s


def parse(net=True):
    d = fetch_patent.parse_gesetz(dict(key="markeng", slug="markeng", kurz="MarkenG", datei="markeng.json"), net)
    paragraphen = []
    for p in d["paragraphen"]:
        if not re.fullmatch(r"\d+[a-z]?", p["nr"]):   # „§§ 161 bis 163 (weggefallen)“
            continue
        paragraphen.append({
            "id": f"§ {p['nr']}",
            "nummer": p["nr"],
            "titel": re.sub(r"\s+", " ", p["titel"]),
            "teil": _gliederung(p["teil"]),
            "abschnitt": _gliederung(p["abschnitt"]),
            "absaetze": p["absaetze"],
            "text": p["text"],
        })
    meta = d["meta"]
    out = {
        "gesetz": "Gesetz über den Schutz von Marken und sonstigen Kennzeichen (Markengesetz - MarkenG)",
        "quelle": meta["quelle"] + " (XML: " + meta["quelle_xml"] + ")",
        "meta": {"Ausfertigungsdatum": meta["ausfertigung"], "Stand": "; ".join(meta["stand"]), "builddate": meta["builddate"]},
        "paragraphen": paragraphen,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(paragraphen)} Paragraphen -> {OUT.relative_to(ROOT)} ({out['meta']['Stand']})")
    return out


if __name__ == "__main__":
    parse(net="--no-net" not in sys.argv)
