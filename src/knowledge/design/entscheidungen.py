# -*- coding: utf-8 -*-
"""Entscheidungskorpus Designrecht: BPatG (Design- und Geschmacksmusterbeschwerden des Juristischen Beschwerdesenats, seit 2014
Nichtigkeitsbeschwerden zum 30. Senat) und BGH (I. Zivilsenat) aus data/design_decisions.json (erzeugt von tools/fetch_design.py
aus der RheinIP-Datenbank).

Wie beim Patentkorpus sind die Entscheidungen keine Graphknoten, sondern liegen als docs/design_entscheidungen.json neben der App
und werden in IPelico nachgeladen (Ansicht #/bpatg/design, Zitierlisten an jedem Paragraphen des DesignG und der DesignV).
Hier: Laden, Kompaktieren, Zitierzähler je Norm und die Verifikation der kuratierten Leitentscheidungen (cases.py).
"""
import json
import re
from collections import Counter
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data" / "design_decisions.json"

_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
ENTSCHEIDUNGEN = _JSON["entscheidungen"]
# Gesetzesschlüssel des Korpus, die als eunorm-Familien im Graphen existieren (Zitierzähler, Ansicht je Norm)
FAMILIEN_KEYS = ("designg", "designv")
GESETZ_KURZ = {"designg": "DesignG", "designv": "DesignV", "geschmmg_alt": "GeschmMG a.F.", "urhg": "UrhG", "uwg": "UWG", "markeng": "MarkenG", "patkostg": "PatKostG"}

_BY_AZ = {}
for _e in ENTSCHEIDUNGEN:
    _BY_AZ.setdefault(_e["az"], []).append(_e)


def zitierungen():
    """{'eunorm:designg:2': n, …} – Zahl der Entscheidungen, die die Norm nennen (Erwähnung oder Auslegung)."""
    c = Counter()
    for e in ENTSCHEIDUNGEN:
        for key, pars in e["zitate"].items():
            if key in FAMILIEN_KEYS:
                for par in pars:
                    c[f"eunorm:{key}:{par}"] += 1
    return dict(c)


def by_az(az, datum=None):
    """Entscheidung zu einem Aktenzeichen (optional mit Datum) oder None."""
    hits = _BY_AZ.get(az, [])
    if datum:
        hits = [h for h in hits if h["datum"] == datum]
    return hits[0] if hits else None


def _parkey(p):
    m = re.search(r"(\d+)([a-z]?)$", p)
    return (int(m.group(1)) if m else 0, m.group(2) if m else p)


def kompakt():
    """Für docs/design_entscheidungen.json: nur was die App braucht (Kurzschlüssel, keine Volltexte)."""
    out = []
    for e in ENTSCHEIDUNGEN:
        n = {k: sorted(v, key=_parkey) for k, v in e["zitate"].items()}
        ni = {k: sorted(p for p, m in v.items() if m["i"]) for k, v in e["zitate"].items()}
        out.append(dict(az=e["az"], datum=e["datum"], g=e["gericht"], s=e["senat_typ"], typ=e["typ"], v=e["verfahren"],
                        name=e["name"], ls=e["leitsatz"][:1200], nt=e["normen_text"], url=e["url"],
                        n=n, ni={k: v for k, v in ni.items() if v}))
    return dict(meta=dict(quelle=META["quelle"], anzahl=len(out), bpatg=META["bpatg"], bgh=META["bgh"], mit_leitsatz=META["mit_leitsatz"],
                          zeitraum=META["zeitraum"], hinweis=META["hinweis"], gesetze=GESETZ_KURZ, korpus="design",
                          titel="Designrecht: BPatG und BGH", beschreibung="Beschwerden in Design- und Geschmacksmustersachen vor dem BPatG (Anmeldung, Nichtigkeit) und die designrechtliche Rechtsprechung des I. Zivilsenats des BGH seit 2000 mit Leitsätzen und den zitierten Vorschriften."),
                entscheidungen=out)
