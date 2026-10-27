# -*- coding: utf-8 -*-
"""Normkurs Arbeitnehmererfinderrecht im Jurafuchs-Format: ein Kapitel je Vorschrift des ArbnErfG (oder eng verbundener Gruppe),
Unterkapitel (`abschnitt`) je Absatz, darin kurze Fallketten.

Grundlage ist der Kommentar zum ArbnErfG (patent/arbnerfg_kommentar): Jede Frage nimmt eine Randnummer auf, also eine Auslegung,
die die Schiedsstelle beim DPMA oder der BGH der Vorschrift gegeben hat. Auswahl und Gewicht der Kapitel folgen der Zahl der
Entscheidungen, die die Vorschrift auslegen (data/arbnerfg_decisions.json: § 9 vor § 12, § 6, § 5, § 16, § 13, § 23 …).
Die Kapitel stehen in fünf Modulen parallel zu den Kommentarteilen und werden hier nach `order` (Paragraph × 100) zusammengeführt.
"""
from . import _p04_a, _p04_b, _p04_c, _p04_d, _p04_e

KURS = dict(
    id="p04", gebiet="patent", kompakt=True,
    titel="ArbnErfG nach Vorschriften",
    untertitel="Arbeitnehmererfindungen von der Meldung bis zur Schiedsstelle: wie Schiedsstelle und BGH das Gesetz auslegen",
    farbe="#2f6b4f", icon="norm",
    beschreibung="Ein Kapitel je Vorschrift des Gesetzes über Arbeitnehmererfindungen: Diensterfindung und freie Erfindung, Meldung, "
                 "Inanspruchnahme und Freigabe, Vergütung mit Erfindungswert und Anteilsfaktor nach den Vergütungsrichtlinien, Festsetzung "
                 "und Anpassung, Schutzrechtsanmeldung und Aufgabe, Verbesserungsvorschläge, Unbilligkeit, Schiedsverfahren und Klage, "
                 "Hochschulerfindungen. Jeder Fall ist ein kurzer Sachverhalt mit mehreren Fragen nach Einigungsvorschlägen der Schiedsstelle "
                 "und Urteilen des BGH.",
    kapitel=sorted(_p04_a.KAPITEL + _p04_b.KAPITEL + _p04_c.KAPITEL + _p04_d.KAPITEL + _p04_e.KAPITEL, key=lambda k: k.pop("order")),
)
