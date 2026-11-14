# -*- coding: utf-8 -*-
"""Kurs p05: Anspruchsgrundlagen Patent für die schriftliche Prüfung (TS, NS, RP1, RP2).

Ein Kapitel je Anspruchsgrundlage oder Rechtsbehelf, jeweils in derselben Folge: Prüfungsschema in Lösungssprache (AGL,
Voraussetzungen V1 … Vn mit Norm, Fristen mit Frist · Berechnung · Verschiebung, Rechtsfolge, Klausurfallen), Definitionen,
Drill-Einheiten zu Definitionen und Normenketten, danach Klausurfälle als Fallketten nach den TS-Klausuren II/2018 bis III/2023.
Teil A (_p05_a: Überblick, Einspruch, Widerruf, Patentfähigkeit, Nichtigkeitsklage, Beschwerde, Rechtsbeschwerde) und
Teil B (_p05_b: Erteilung, Teilung, Priorität, Wiedereinsetzung, Verletzung, Recht auf das Patent).
"""
from . import _p05_a, _p05_b

KURS = dict(
    id="p05", gebiet="patent", reihe="Anspruchsgrundlagen für die Klausur", kompakt="fragen",
    titel="Anspruchsgrundlagen Patent",
    untertitel="Anspruchsgrundlage für Anspruchsgrundlage: Voraussetzungen, Definitionen und Normenketten aus den TS-Klausuren",
    farbe="#2f6b4f", icon="hammer",
    beschreibung="Jede Anspruchsgrundlage und jeder Rechtsbehelf des Patentrechts als Prüfungsschema in Lösungssprache: Einspruch, "
                 "Widerruf und beschränkte Aufrechterhaltung, Patentfähigkeit als Vorfrage, Nichtigkeitsklage, Beschwerde und "
                 "Rechtsbeschwerde, Erteilungsverfahren, Teilung, Priorität, Wiedereinsetzung und Weiterbehandlung, Verletzungsansprüche "
                 "und Recht auf das Patent. Zu jeder Voraussetzung die Norm, zu jeder Frist Berechnung und Verschiebung, dazu die "
                 "Definitionen und Klausurfälle nach den TS-Klausuren 2018 bis 2023.",
    kapitel=_p05_a.KAPITEL + _p05_b.KAPITEL,
)
