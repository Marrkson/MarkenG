# -*- coding: utf-8 -*-
"""Kapitel des Normkurses p04 (siehe p04_arbnerfg.py), Teil e: §§ 27 bis 42 ArbnErfG. Jedes Kapitel trägt `order` (Paragraph × 100)."""
from ._helpers import intro, frage, fallkette  # noqa: F401

KAPITEL = [
    # ================================================================== § 42 ArbnErfG
    dict(id="p04n42", order=4200, titel="§ 42 ArbnErfG: Erfindungen an Hochschulen", einheiten=[
        intro("p04n42-0", "Sonderrecht der Hochschulerfinder",
              "§ 42 ArbnErfG passt das Gesetz an die Wissenschaftsfreiheit an. Der Erfinder darf seine Diensterfindung nach Anzeige veröffentlichen "
              "(Nr. 1), muss sie nicht melden, wenn er die Offenbarung ablehnt (Nr. 2), und behält ein Benutzungsrecht für Lehre und Forschung "
              "(Nr. 3). Die Vergütung ist pauschal: 30 % der durch die Verwertung erzielten Einnahmen (Nr. 4).",
              norms=["§ 42 ArbnErfG"], concepts=["arb_hochschulerfindung"], abschnitt="Überblick"),
        *fallkette("p04n42-1", "Die Sterilisationsschleuse",
            "Medizintechniker M, angestellt am Universitätsklinikum U, entwickelt eine Schleuse, die die Sterilisation von OP-Besteck "
            "verkürzt. U nutzt sie selbst und spart jährlich 200.000 Euro. M verlangt eine Vergütung.",
            [frage("Gilt für M die Sonderregel für Hochschulerfinder, obwohl U ein Klinikum in eigener Rechtsform ist und M kein Wissenschaftler?", True,
                   ["**Ja!** Ein Universitätsklinikum ist wegen der Verzahnung von Forschung, Lehre und Krankenversorgung Hochschule im Sinne "
                    "des § 42 ArbnErfG, gleich in welcher Rechtsform. Beschäftigte sind alle, auch nichtwissenschaftliches Personal "
                    "(Schiedsstelle Hochschulklinikum)."],
                   merke="Uniklinikum = Hochschule; jeder Beschäftigte = Hochschulerfinder.", titel="Hochschule und Beschäftigte", level=1),
             frage("Berechnet sich die Vergütung nach Erfindungswert und Anteilsfaktor?", False,
                   ["**Nein!** Für Hochschulbeschäftigte gilt ausnahmslos § 42 Nr. 4 ArbnErfG: **30 % der Einnahmen** aus der Verwertung, "
                    "ohne Erfindungswert und Anteilsfaktor nach § 9 Abs. 2 ArbnErfG (Schiedsstelle Hochschulklinikum)."],
                   merke="Hochschule: 30 % der Einnahmen statt Erfindungswert × Anteilsfaktor.", titel="Bemessung", level=1,
                   norms=["§ 42 ArbnErfG", "§ 9 Abs. 2 ArbnErfG"]),
             frage("Darf U die Ersparnis vor Anwendung der 30 % mit einem Umrechnungsfaktor (Lizenzsatz) kürzen?", False,
                   ["**Nein!** Einnahmen sind alle geldwerten Vorteile aus der Verwertung, auch ein ersparter betrieblicher Nutzen. Ein "
                    "Umrechnungsfaktor bildet den Lizenzsatz der Lizenzanalogie nach und gehört zu § 9 Abs. 2 ArbnErfG; bei § 42 Nr. 4 ArbnErfG "
                    "ist er systemwidrig (Schiedsstelle Hochschulklinikum)."],
                   merke="Ersparnis zählt voll als Einnahme.", titel="Einnahmen", level=2),
             ],
            abschnitt="Nr. 4: Vergütung", level=1, concepts=["arb_hochschulerfindung"], norms=["§ 42 ArbnErfG"],
            cases=["arb_sst_hochschulklinikum"]),
    ]),
]
