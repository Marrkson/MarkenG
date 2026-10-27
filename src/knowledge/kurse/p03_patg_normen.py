# -*- coding: utf-8 -*-
"""Normkurs Patentrecht im Jurafuchs-Format: ein Kapitel je Vorschrift (Anspruchsgrundlage, Tatbestand, Verfahrensnorm),
Unterkapitel (`abschnitt`) je Absatz oder Tatbestandsmerkmal, darin kurze Fallketten mit Abwandlungen.

Auswahl und Reihenfolge der Vorschriften folgen der Rangliste data/norm_ranking.json (tools/norm_ranking.py: Zahl der
BGH-/BPatG-Entscheidungen, die die Vorschrift auslegen) und den Anspruchsgrundlagen der Verletzungsklage. Die Kapitel stehen in
zwei Modulen (_p03_rechtsbestand: Patentfähigkeit, Erteilung, Rechtsbestand, Verfahren; _p03_verletzung: Schutzbereich,
Benutzung, Ansprüche) und werden hier in Gesetzesreihenfolge (`order`) zusammengeführt.
"""
from . import _p03_rechtsbestand, _p03_verletzung

KURS = dict(
    id="p03", gebiet="patent", kompakt=True,
    titel="PatG und GebrMG nach Vorschriften",
    untertitel="Von § 1 PatG bis § 141 PatG: jede Vorschrift mit den Fällen, in denen BGH und BPatG sie ausgelegt haben",
    farbe="#2f6b4f", icon="norm",
    beschreibung="Ein Kapitel je Vorschrift, sortiert nach dem Gesetz: Patentfähigkeit (§§ 1 bis 4 PatG), Anmeldung und Widerruf, Einspruch, "
                 "Beschwerde, Nichtigkeit, Wiedereinsetzung, Schutzbereich und Benutzung (§§ 9 bis 14 PatG), die Anspruchsgrundlagen der "
                 "Verletzungsklage (§ 139 PatG, §§ 140a bis 141 PatG) und das Gebrauchsmuster. Jeder Fall ist ein kurzer Sachverhalt mit mehreren "
                 "Fragen, Prüfungspunkt für Prüfungspunkt, oft mit Abwandlung.",
    kapitel=sorted(_p03_rechtsbestand.KAPITEL + _p03_verletzung.KAPITEL, key=lambda k: k.pop("order")),
)
