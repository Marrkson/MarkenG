# -*- coding: utf-8 -*-
"""Rechtsgebiete: die Ebene über den Kursen (Kurs -> Kapitel -> Einheit).

Jeder Kurs trägt `gebiet=<id>`; `kurse/__init__.py` prüft, dass die ID hier registriert ist.
`geplant=True` markiert Gebiete ohne Kurse; die App zeigt sie unter „In Vorbereitung“.
Reihenfolge = Reihenfolge in der App.
"""
GEBIETE = [
    dict(id="markeng", kurz="MarkenG", titel="Markengesetz", farbe="#1482e3",
         beschreibung="Materielles deutsches Markenrecht: Schutzfähigkeit, Verletzung, Schranken, Löschung, Kennzeichen, Rechtsfolgen."),
    dict(id="eu", kurz="EU-Recht", titel="EU- und internationales Markenrecht", farbe="#2b3fb4",
         beschreibung="Unionsmarke, IR-Marke, Markenrechtsrichtlinie und Durchsetzungsrichtlinie."),
    dict(id="verfahren", kurz="Verfahren", titel="Verfahren und Klausur", farbe="#4a6d3a",
         beschreibung="Zulässigkeit und Wirksamkeit nach Verfahrensart sowie Training an echten NS-Klausuren der Patentanwaltsprüfung."),
    dict(id="patg", kurz="PatG", titel="Patentgesetz", farbe="#5c5f66", geplant=True),
    dict(id="epue", kurz="EPÜ", titel="Europäisches Patentübereinkommen (EPC)", farbe="#5c5f66", geplant=True),
    dict(id="upc", kurz="EPG", titel="Einheitliches Patentgericht (EPGÜ, VerfO)", farbe="#7a3e9d",
         beschreibung="Aufbau und Zuständigkeit des EPG, Verletzungs- und Nichtigkeitsverfahren, einstweilige Maßnahmen, Beweis, Rechtsfolgen, Berufung – mit der Rechtsprechung des Berufungsgerichts und der Brücke zur Durchsetzungsrichtlinie."),
    dict(id="designg", kurz="DesignG", titel="Designrecht", farbe="#5c5f66", geplant=True),
    dict(id="arbnerfg", kurz="ArbnErfG", titel="Arbeitnehmererfindungsrecht", farbe="#5c5f66", geplant=True),
    dict(id="bgb", kurz="BGB", titel="Bürgerliches Recht", farbe="#5c5f66", geplant=True),
    dict(id="uwg", kurz="UWG", titel="Lauterkeitsrecht (UWG)", farbe="#5c5f66", geplant=True),
]
GEBIET_IDS = {g["id"] for g in GEBIETE}
