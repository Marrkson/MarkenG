# -*- coding: utf-8 -*-
"""Normkurs EPÜ im Jurafuchs-Format, ausgerichtet auf die EQE (Paper D, Teil 1 / Modul M2): ein Kapitel je Vorschrift oder
Vorschriftengruppe, Fälle als kurze Fallketten, Prüfungspunkt für Prüfungspunkt.

Auswahl der Vorschriften nach der Häufigkeit in den Musterlösungen der Paper-D-Fragen 2015 bis 2025 (data/eqe_d1.json, Rang in
`EQE_META["rang"]`): Art. 54 EPÜ vor Art. 121, Art. 122, Art. 123 EPÜ, R. 51, R. 131, R. 134, R. 159 EPÜ und Art. 153 EPÜ. Jede Vorschrift
ist im Graphen angereichert mit Beschwerdekammerentscheidungen, Richtlinienabschnitten und Amtsblattfundstellen (knowledge/epc/texte.py).
Die Kapitel stehen in fünf Modulen (_e01_a bis _e01_e) und werden hier in der Reihenfolge des EPÜ (`order`) zusammengeführt.
"""
from . import _e01_a, _e01_b, _e01_c, _e01_d, _e01_e

KURS = dict(
    id="e01", gebiet="patent", reihe="Europäisches Patent (EPÜ)", kompakt=True,
    titel="EPÜ nach Vorschriften (EQE Paper D)",
    untertitel="Die Vorschriften, nach denen Paper D am häufigsten fragt: von Art. 14 EPÜ bis Art. 153 EPÜ, mit Rechtsprechung, Richtlinien und Amtsblatt",
    farbe="#1f5f8b", icon="union",
    beschreibung="Ein Kapitel je Vorschrift, sortiert nach dem EPÜ und ausgewählt nach der Häufigkeit in den Rechtsfragen der EQE (Paper D 2015 bis 2025): "
                 "Sprachen, Recht auf das Patent, Teilanmeldung, Anmeldetag, Jahresgebühren, Priorität, Neuheit, Prüfung und Erteilung, Einspruch, "
                 "Beschränkung, Beschwerde, Fristen, Weiterbehandlung, Wiedereinsetzung, Änderungen, Vertretung, Euro-PCT und die internationale Phase. "
                 "Jeder Fall ist ein kurzer Sachverhalt mit mehreren Fragen; Lernkarten zeigen zu jedem Artikel und jeder Regel die Entscheidungen der "
                 "Beschwerdekammern, die Abschnitte der Richtlinien und die Mitteilungen im Amtsblatt.",
    kapitel=sorted(_e01_a.KAPITEL + _e01_b.KAPITEL + _e01_c.KAPITEL + _e01_d.KAPITEL + _e01_e.KAPITEL, key=lambda k: k.pop("order")),
)
