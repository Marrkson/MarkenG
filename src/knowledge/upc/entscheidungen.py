# -*- coding: utf-8 -*-
"""Entscheidungskorpus des EPG (alle Entscheidungen und Anordnungen aus data/upc_decisions.json).

Wird nicht als Graphknoten je Entscheidung eingebunden (1.900 Knoten würden die Apps aufblähen),
sondern als eigene Datenbank docs/upc_entscheidungen.json ausgeliefert und in IPelico nachgeladen
(Ansicht „EPG-Rechtsprechung“, Zitierlisten an jedem Artikel und jeder Regel). Hier: Laden,
Kompaktieren, Zitierzähler je Norm.
"""
import json
import re
from collections import Counter
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data" / "upc_decisions.json"

_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
ENTSCHEIDUNGEN = _JSON["entscheidungen"]

DIVISION_KURZ = {
    "Luxembourg (LU)": "Berufungsgericht",
    "Paris (FR) Central Division - Seat": "Zentralkammer Paris",
    "Munich (DE) Central Division - Section": "Zentralkammer München",
    "Milan (IT) Central Division- Section": "Zentralkammer Mailand",
    "Nordic Baltic Regional Division": "Regionalkammer Nordisch-Baltisch",
    "Stockholm (SE) - Seat of the Regional Division": "Regionalkammer Nordisch-Baltisch",
}


def division_kurz(div):
    if div in DIVISION_KURZ:
        return DIVISION_KURZ[div]
    m = re.match(r"^(.+?) \([A-Z]{2}\) Local Division$", div or "")
    if m:
        ort = {"Munich": "München", "The Hague": "Den Haag", "Milan": "Mailand", "Brussels": "Brüssel", "Vienna": "Wien", "Lisbon": "Lissabon", "Copenhagen": "Kopenhagen"}.get(m.group(1), m.group(1))
        return "Lokalkammer " + ort
    return div or "–"


def zitierungen():
    """{'eunorm:upca:33': n, 'eunorm:rop:19': n} – Zahl der Entscheidungen, die die Norm nennen."""
    c = Counter()
    for e in ENTSCHEIDUNGEN:
        for nr in e["upca"]:
            c[f"eunorm:upca:{nr}"] += 1
        for nr in e["rop"]:
            c[f"eunorm:rop:{nr}"] += 1
    return dict(c)


def kompakt():
    """Für docs/upc_entscheidungen.json: nur was die App braucht."""
    out = []
    for e in ENTSCHEIDUNGEN:
        out.append(dict(
            az=e["docket"], datum=e["date"], typ=e["typ"], kammer=division_kurz(e["division"]), sprache=e["lang"],
            parteien=(e["claimant"][:80] + (" ./. " + e["respondent"][:80] if e["respondent"] else "")).strip(),
            patent=e["patent"], url=e["url"], leitsatz=e["headnote"][:900], schlagworte=e["keywords"][:300],
            upca=sorted(e["upca"], key=int), rop=sorted(e["rop"], key=lambda x: (int(re.match(r"\d+", x).group()), x)),
        ))
    return dict(meta=dict(quelle=META["quelle"], anzahl=len(out), zeitraum=META["zeitraum"], hinweis=META["hinweis"]), entscheidungen=out)
