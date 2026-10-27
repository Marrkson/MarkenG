# -*- coding: utf-8 -*-
"""Entscheidungskorpus Arbeitnehmererfinderrecht: Einigungsvorschläge, Beschlüsse und Zwischenbescheide der Schiedsstelle nach
dem ArbEG beim DPMA (seit 2000) und die Entscheidungen des BGH und des BPatG, die das ArbEG zitieren, aus
data/arbnerfg_decisions.json (erzeugt von tools/fetch_arbnerfg.py aus der RheinIP-Datenbank).

Wie der Patentkorpus keine Graphknoten, sondern docs/arbnerfg_entscheidungen.json neben der App (Ansicht „Schiedsstelle und BGH“,
Zitierlisten an jedem Paragraphen des ArbnErfG). Hier: Laden, Zitierzähler je Norm, Verifikation der Kommentarbelege und der
kuratierten Leitentscheidungen (cases_arb.py), Kompaktfassung für die App.
"""
import json
from collections import Counter
from pathlib import Path

from .entscheidungen import _parkey

_DATA = Path(__file__).resolve().parents[3] / "data" / "arbnerfg_decisions.json"

_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
ENTSCHEIDUNGEN = _JSON["entscheidungen"]
GESETZ_KURZ = {"arbnerfg": "ArbnErfG"}

_BY_AZ = {}
for _e in ENTSCHEIDUNGEN:
    _BY_AZ.setdefault(_e["az"], []).append(_e)


def zitierungen():
    """{'eunorm:arbnerfg:9': n, …} – Zahl der Entscheidungen, die die Vorschrift nennen."""
    c = Counter()
    for e in ENTSCHEIDUNGEN:
        for par in e["zitate"].get("arbnerfg", {}):
            c[f"eunorm:arbnerfg:{par}"] += 1
    return dict(c)


def by_az(az, datum=None):
    """Entscheidung zu einem Aktenzeichen („Arb.Erf. 12/23“, „X ZR 104/09“), bei Mehrdeutigkeit mit Datum, oder None."""
    hits = _BY_AZ.get(az, [])
    if datum:
        hits = [h for h in hits if h["datum"] == datum]
    return hits[0] if len(hits) == 1 or datum else None


def beleg(az, datum=None):
    """Kommentar-/Kursbeleg: Entscheidung aus dem Korpus oder Abbruch (Aktenzeichen und Datum nie ungeprüft übernehmen)."""
    rec = by_az(az, datum)
    if rec is None:
        n = len(_BY_AZ.get(az, []))
        raise ValueError(f"Entscheidung {az}" + (f" vom {datum}" if datum else "") + (" mehrdeutig, Datum angeben" if n > 1 and not datum else
                         " nicht im Korpus data/arbnerfg_decisions.json"))
    return dict(az=rec["az"], datum=rec["datum"], g=rec["gericht"], typ=rec["typ"], name=rec["name"], url=rec["url"])


def kompakt():
    """Für docs/arbnerfg_entscheidungen.json: Kurzschlüssel wie docs/patent_entscheidungen.json, dazu Schlagworte (sw)."""
    out = []
    for e in ENTSCHEIDUNGEN:
        z = e["zitate"].get("arbnerfg", {})
        out.append(dict(az=e["az"], datum=e["datum"], g=e["gericht"], s=e["senat_typ"], typ=e["typ"], v=e["verfahren"],
                        name=e["name"], ls=e["leitsatz"][:1200], nt=e["normen_text"], sw=e["schlagworte"], url=e["url"],
                        n={"arbnerfg": sorted(z, key=_parkey)} if z else {},
                        ni={"arbnerfg": sorted((p for p, m in z.items() if m["i"]), key=_parkey)} if any(m["i"] for m in z.values()) else {}))
    return dict(meta=dict(quelle=META["quelle"], anzahl=len(out), schiedsstelle=META["schiedsstelle"], bgh=META["bgh"], bpatg=META["bpatg"],
                          mit_leitsatz=META["mit_leitsatz"], zeitraum=META["zeitraum"], hinweis=META["hinweis"], gesetze=GESETZ_KURZ),
                entscheidungen=out)
