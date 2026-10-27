# -*- coding: utf-8 -*-
"""Entscheidungskorpus der Beschwerdekammern des EPA (data/epc_decisions.json, tools/fetch_epc.py aus der Tabelle BoaDecision).

Wie beim EPG- und beim Patentkorpus sind die Entscheidungen keine Graphknoten, sondern liegen als docs/boa_entscheidungen.json
neben der App (Ansicht „Beschwerdekammern“, `#/boa`, und Liste an jedem Artikel und jeder Regel). Hier: Laden, Kompaktieren,
Zitierzähler je Vorschrift und die Verifikation der kuratierten Leitentscheidungen (cases.py) gegen den Korpus.
"""
import json
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data" / "epc_decisions.json"
_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
ENTSCHEIDUNGEN = _JSON["entscheidungen"]

_BY_AZ = {}
for _e in ENTSCHEIDUNGEN:
    _BY_AZ.setdefault(_e["az"], []).append(_e)


def by_az(az, datum=None):
    """Entscheidung nach Aktenzeichen ('G 1/15') und, falls mehrdeutig, Datum ('2016-11-29'); None, wenn nicht im Korpus."""
    hits = [e for e in _BY_AZ.get(az, []) if datum is None or e["datum"] == datum]
    if len(hits) > 1 and datum is None:
        hits = [e for e in hits if e["leitsatz"]] or hits
    return hits[0] if hits else None


def zitierungen():
    """{'eunorm:epc:54': n, 'eunorm:epcr:71': n} – Zahl der Entscheidungen (alle Verteiler, EPÜ 2000), die die Vorschrift nennen."""
    out = {}
    for key, n in META["zitiert"].items():
        if key.startswith("a") and key[1:2].isdigit():
            out["eunorm:epc:" + key[1:]] = n
        elif key.startswith("r") and key[1:2].isdigit():
            out["eunorm:epcr:" + key[1:]] = n
    return out


KAMMER = {"G": "Große Beschwerdekammer", "J": "Juristische Beschwerdekammer", "R": "Große Beschwerdekammer (Überprüfung)", "T": "Technische Beschwerdekammer"}


def kompakt():
    """Für docs/boa_entscheidungen.json: kurze Schlüssel (az, d, k = Kammer, v = Verteiler, t = Titel, h = Stichwort, sw = Schlagworte,
    ls = Leitsatz, u = URL, a/r = zitierte Artikel/Regeln, de = {ls, sw, u} deutsche Fassung, falls vorhanden)."""
    out = []
    for e in ENTSCHEIDUNGEN:
        x = dict(az=e["az"], d=e["datum"], k=e["kammer"], v=e["verteiler"], t=e["titel"], h=e["stichwort"], sw=e["schlagworte"][:300],
                 ls=e["leitsatz"][:900], u=e["url"], a=e["a"], r=e["r"])
        if e.get("url_de"):
            x["de"] = dict(ls=e.get("leitsatz_de", "")[:900], sw=e.get("schlagworte_de", "")[:300], u=e["url_de"])
        out.append({k: v for k, v in x.items() if v not in ("", [], None)})
    meta = dict(quelle=META["quelle"], anzahl=len(out), gesamt=META["gesamt"], zeitraum=META["zeitraum"], auswahl=META["auswahl"],
                mit_leitsatz=sum(1 for e in out if e.get("ls")))
    return dict(meta=meta, entscheidungen=out)
