# -*- coding: utf-8 -*-
"""Rechtsgebiete: die Auswahlebene über den Kursen (Gebiet -> Kurs -> Kapitel -> Einheit).

Die App zeigt zuerst nur diese fünf Gebiete; erst nach der Wahl eines Gebiets erscheinen dessen Kurse.
Jeder Kurs trägt `gebiet=<id>`; `kurse/__init__.py` prüft, dass die ID hier registriert ist.
Optional trägt ein Kurs `reihe="…"`; Kurse mit gleicher Reihe stehen im Gebiet unter einer eigenen
Zwischenüberschrift (z. B. „Verfahren und Klausur“). Reihenfolge = Reihenfolge in der App.
`icon` ist ein Symbolname aus dem Sprite (`src/templates/ipelico/icons/ic-<name>.svg`).
"""
GEBIETE = [
    dict(id="eu", kurz="EU-Recht", titel="EU und internationales Recht", farbe="#2b3fb4", icon="union",
         beschreibung="Unionsmarke, IR-Marke, Markenrechtsrichtlinie und Durchsetzungsrichtlinie."),
    dict(id="marken", kurz="Marken", titel="Marken", farbe="#1482e3", icon="marke",
         beschreibung="Deutsches Markenrecht: Schutzfähigkeit, Verletzung, Schranken, Löschung, Kennzeichen, Rechtsfolgen; dazu Verfahrensrecht und Training an echten NS-Klausuren."),
    dict(id="patent", kurz="Patent", titel="Patent", farbe="#2f6b4f", icon="norm",
         beschreibung="Patent und Gebrauchsmuster: Patentfähigkeit, Anmeldung und Erteilung, Schutzbereich und Verletzung, Einspruch und Nichtigkeit, europäische und internationale Anmeldung; dazu Training an echten TS-Klausuren."),
    dict(id="designg", kurz="DesignG", titel="DesignG", farbe="#b0562b", icon="register",
         beschreibung="Schutzvoraussetzungen, Anmeldung und Nichtigkeitsverfahren beim DPMA, Schutzumfang und Verletzung, Reparaturklausel, Unionsgeschmacksmuster und Designrichtlinien."),
    dict(id="upc", kurz="EPG", titel="Einheitliches Patentgericht (EPGÜ, VerfO)", farbe="#7a3e9d", icon="entscheidung",
         beschreibung="Aufbau und Zuständigkeit des EPG, Verletzungs- und Nichtigkeitsverfahren, einstweilige Maßnahmen, Beweis, Rechtsfolgen, Berufung, Einheitspatent – mit der Rechtsprechung des Berufungsgerichts."),
]
GEBIET_IDS = {g["id"] for g in GEBIETE}
