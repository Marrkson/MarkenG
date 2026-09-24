# -*- coding: utf-8 -*-
"""Entscheidungskorpus Patentrecht: BPatG (Nichtigkeitssenate, Technische und Juristische Beschwerdesenate,
Gebrauchsmuster-Beschwerdesenat) und BGH (X. und Xa. Zivilsenat sowie weitere Senate mit Patentbezug) aus
data/patent_decisions.json (erzeugt von tools/fetch_patent.py aus der RheinIP-Datenbank).

Wie beim EPG-Korpus sind die Entscheidungen keine Graphknoten (17.500 Knoten würden die Apps aufblähen), sondern
liegen als docs/patent_entscheidungen.json neben der App und werden in IPelico nachgeladen (Ansicht „BPatG/BGH-
Rechtsprechung“, Zitierlisten an jedem Paragraphen). Hier: Laden, Kompaktieren, Zitierzähler je Norm und die
Verifikation der kuratierten Leitentscheidungen (cases.py) gegen die Datenbank.
"""
import json
from collections import Counter
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data" / "patent_decisions.json"

_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
ENTSCHEIDUNGEN = _JSON["entscheidungen"]
# Gesetzesschlüssel des Korpus, die als eunorm-Familien im Graphen existieren (Zitierzähler, Ansicht je Norm)
FAMILIEN_KEYS = ("patg", "patv", "intpatueg", "patkostg")
GESETZ_KURZ = {"patg": "PatG", "patv": "PatV", "intpatueg": "IntPatÜG", "patkostg": "PatKostG", "gebrmg": "GebrMG", "arbnerfg": "ArbnErfG", "epue": "EPÜ"}

_BY_AZ = {}
for _e in ENTSCHEIDUNGEN:
    _BY_AZ.setdefault(_e["az"], []).append(_e)


def _nid(key, par):
    """'patg','3' -> eunorm:patg:3; 'intpatueg','II 6' -> eunorm:intpatueg:II§6 (Knoten-ID wie build_graph)."""
    return f"eunorm:{key}:{par.replace(' ', '§')}"


def zitierungen():
    """{'eunorm:patg:3': n, …} – Zahl der Entscheidungen, die die Norm nennen (Erwähnung oder Auslegung)."""
    c = Counter()
    for e in ENTSCHEIDUNGEN:
        for key, pars in e["zitate"].items():
            if key in FAMILIEN_KEYS:
                for par in pars:
                    c[_nid(key, par)] += 1
    return dict(c)


def by_az(az, datum=None):
    """Entscheidung zu einem Aktenzeichen (optional mit Datum, falls das Aktenzeichen mehrfach vorkommt) oder None."""
    hits = _BY_AZ.get(az, [])
    if datum:
        hits = [h for h in hits if h["datum"] == datum]
    return hits[0] if hits else None


def kompakt():
    """Für docs/patent_entscheidungen.json: nur was die App braucht (Kurzschlüssel, keine Volltexte)."""
    out = []
    for e in ENTSCHEIDUNGEN:
        n = {k: sorted(v, key=_parkey) for k, v in e["zitate"].items()}
        ni = {k: sorted(p for p, m in v.items() if m["i"]) for k, v in e["zitate"].items()}
        out.append(dict(az=e["az"], datum=e["datum"], g=e["gericht"], s=e["senat_typ"], typ=e["typ"], v=e["verfahren"],
                        name=e["name"], ls=e["leitsatz"][:1200], nt=e["normen_text"], url=e["url"],
                        n=n, ni={k: v for k, v in ni.items() if v}))
    return dict(meta=dict(quelle=META["quelle"], anzahl=len(out), bpatg=META["bpatg"], bgh=META["bgh"], mit_leitsatz=META["mit_leitsatz"],
                          zeitraum=META["zeitraum"], hinweis=META["hinweis"], gesetze=GESETZ_KURZ), entscheidungen=out)


def _parkey(p):
    import re
    m = re.search(r"(\d+)([a-z]?)$", p)
    return (p.split(" ")[0] if " " in p else "", int(m.group(1)) if m else 0, m.group(2) if m else p)
