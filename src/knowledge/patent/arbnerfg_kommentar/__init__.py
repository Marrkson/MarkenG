# -*- coding: utf-8 -*-
"""Kommentar zum ArbnErfG aus der Rechtsprechung: je Paragraph Randnummern mit der Auslegung durch die Schiedsstelle beim DPMA und
den BGH, jede mit Belegen aus data/arbnerfg_decisions.json. Entstehung: Für jeden Paragraphen wurden die Textstellen aller
Entscheidungen gesammelt, die ihn zitieren (tools/fetch_arbnerfg.py -> ~/.cache/ipelico/arbnerfg/passagen.json), nach Absätzen
geordnet und zu Randnummern verdichtet; die Leitsätze der Entscheidungen, die die Vorschrift in ihrer Normenkette führen, gehen vor.

Module nach Gesetzesteilen (je `KOMMENTAR = {"9": [rn(…), …]}` und `CASES = [ea(…), …]`):
  a_erfindung    §§ 1 bis 8, 43   Anwendungsbereich, Erfindung, Diensterfindung, Meldung, Inanspruchnahme, Freigabe, Übergangsrecht
  b_verguetung   §§ 9 bis 11      Vergütungsanspruch, Erfindungswert, Anteilsfaktor, Vergütungsrichtlinien
  c_festsetzung  §§ 12, 22 bis 26 Feststellung und Festsetzung, Anpassung, Unabdingbarkeit, Unbilligkeit, Arbeitsverhältnis
  d_schutzrechte §§ 13 bis 21     Anmeldung im In- und Ausland, Aufgabe, Betriebsgeheimnis, freie Erfindungen, Verbesserungsvorschläge
  e_verfahren    §§ 27 bis 42     Insolvenz, Schiedsverfahren, gerichtliches Verfahren, öffentlicher Dienst, Hochschulen
"""
from . import a_erfindung, b_verguetung, c_festsetzung, d_schutzrechte, e_verfahren

_MODULE = (a_erfindung, b_verguetung, c_festsetzung, d_schutzrechte, e_verfahren)
KOMMENTAR = {}
CASES = []
for _m in _MODULE:
    for _nr, _rns in _m.KOMMENTAR.items():
        if _nr in KOMMENTAR:
            raise ValueError(f"Kommentar zu § {_nr} ArbnErfG doppelt ({_m.__name__})")
        KOMMENTAR[_nr] = [dict(rn=i + 1, **r) for i, r in enumerate(_rns)]
    CASES += _m.CASES
