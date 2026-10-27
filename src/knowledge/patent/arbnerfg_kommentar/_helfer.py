# -*- coding: utf-8 -*-
"""Bausteine des ArbnErfG-Kommentars: Randnummern (`rn`) und Leitentscheidungen (`ea`), beide gegen den Korpus geprüft."""
from .. import arbnerfg_entscheidungen as _k

SST, BGH, BPATG = "Schiedsstelle", "BGH", "BPatG"


def _beleg(b):
    """Beleg als Aktenzeichen („Arb.Erf. 12/23“) oder Paar (Aktenzeichen, Datum ISO); Datum Pflicht, wenn das Aktenzeichen mehrdeutig ist."""
    az, datum = (b, None) if isinstance(b, str) else b
    return _k.beleg(az, datum)


def rn(titel, text, belege=(), absatz=""):
    """Eine Randnummer: `titel` (Stichwort), `text` (Auslegung in eigenen Worten, zwei bis sechs Sätze, Zitate mit Gesetz:
    „§ 6 Abs. 2 ArbnErfG“, Vergütungsrichtlinien als „RL Nr. 34“), `belege` (Entscheidungen des Korpus, wichtigste zuerst),
    `absatz` („Abs. 2“, „Nr. 4“; leer = ganze Vorschrift). Die Nummerierung vergibt das Paket fortlaufend je Paragraph."""
    if not belege:
        raise ValueError(f"Randnummer „{titel}“ ohne Beleg")
    return dict(titel=titel, text=text, absatz=absatz, belege=[_beleg(b) for b in belege])


def ea(id, name, court, date, az, kern, norms=(), concepts=(), tags=()):
    """Leitentscheidung (case-Knoten) aus dem ArbnErfG-Korpus; `name` bei der Schiedsstelle ein Stichwort („Hochschulklinikum“)."""
    rec = _k.by_az(az, date)
    if rec is None:
        raise ValueError(f"Entscheidung {az} vom {date} ({name}) nicht im Korpus data/arbnerfg_decisions.json")
    art = rec["typ"] or "Entscheidung"
    fund = f"{court}, {art} vom {date[8:]}.{date[5:7]}.{date[:4]} – {az}"
    return dict(id=id, name=name, court=court, date=date, az=az, fundstelle=fund, ecli=rec.get("ecli", ""),
                norms=list(norms), concepts=list(concepts), kern=kern, tags=list(tags), url=rec["url"])
