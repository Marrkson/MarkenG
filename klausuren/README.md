# Klausuren Patentanwaltsprüfung – Nichttechnische Schutzrechte (NS)

Quelle: [kandidatentreff.de – Patentanwaltsprüfung (schriftlich)](https://kandidatentreff.de/2018/03/patentanwaltspruefung-schriftlich/).
Die PDFs (Aufgaben `PAP-<Jahr>-<Termin>-NS.pdf`, Lösungshinweise `L-PAP-…-NS.pdf`) liegen unter `ns/`,
die Textextrakte unter `ns/txt/`; beide sind nicht versioniert (`.gitignore`), die Liste der URLs
steht in `ns/urls.txt` und lässt sich mit `curl` erneut laden. Stand des Downloads: 8. September 2026.

Auf dieser Grundlage sind entstanden:

- der Kurs **„Klausurtraining NS“** (`src/knowledge/kurse/k12_klausurtraining.py`) mit 56 Kurzfällen,
- der Kurs **„Wirksamkeit und Zulässigkeit“** (`src/knowledge/kurse/k13_zulaessigkeit.py`) mit 59 Einheiten in acht
  Kapiteln: die drei Ebenen, die vier Fähigkeiten, Gebühren, Widerspruch, Rechtsbehelfe, Wiedereinsetzung,
  Klagen vor dem Landgericht und ein Kapitel nur mit Tenorvorschlägen,
- die Navigator-Sektion **„Klausur NS“** (`src/knowledge/klausur.py`) mit Format, Zulässigkeitsraster,
  Fristen, Gebühren, Tenorformeln und dieser Klausurliste,
- die Prüfungsschemata `schema_klausur_ns`, `schema_zulaessigkeit_widerspruch`,
  `schema_zulaessigkeit_beschwerde` und `schema_wiedereinsetzung` sowie 15 Verfahrensbegriffe
  in `src/knowledge/concepts.py`,
- die Beschlüsse in `src/knowledge/cases.py` (Tag „Klausur NS“).

## Zuordnung Klausur → Entscheidung

Die Prüfung erfolgte durch Vergleich von Registernummern, Waren-/Dienstleistungsverzeichnissen,
Daten und Verfahrensgang mit dem Volltext des jeweiligen Beschlusses (Entscheidungsdatenbank des
BPatG, dejure.org, rewis.io, Lösungshinweise von kandidatentreff.de). „Sicher“ bedeutet: Sachverhalt
und Rechtsfragen stimmen bis auf ausgetauschte Namen und Daten überein.

| Klausur | Thema | Lösungshinweis | Zugrunde liegender Beschluss | Prüfergebnis |
|---|---|---|---|---|
| NS II/2018 | „Fassbrause“-Widersprüche; „Wuppertaler Flönz“ (g.g.A.) | ja (Lösungsskizze) | Teil 1: kein einzelner Beschluss, Lösungsskizze zitiert BGH „Culinaria/Villa Culinaria“; Teil 2: BGH 12.04.2018, I ZR 253/16 „Deutscher Balsamico“ (im Lösungshinweis abgedruckt), EuGH 04.12.2019, C-432/18; „Flönz“ ist seit 29.07.2016 g.g.A. | Lehrfall, Teil 2 an reale g.g.A. angelehnt |
| NS III/2018 | villa rocca / ROCA: Abholfach-Zustellung, Einrede im Beschwerdeverfahren, Wellenlinie | nein | kein veröffentlichter Beschluss gefunden (Volltextsuche BPatG „rocca“, „Abholfach“) | Lehrfall |
| NS I/2019 | MICHEL LEON / JEAN LEON: Beschwerdefrist, Beschwerdegebühr, Vor-/Nachname | nein | kein veröffentlichter Beschluss gefunden | Lehrfall |
| NS II/2019 | Øresundsbron: Marke des Ticket-Wiederverkäufers, Bösgläubigkeit | nein | BPatG 06.09.2024, 26 W (pat) 2/20 (Nichtigkeitsverfahren gegen DE 30 2013 000 930, Widerspruch 26 W (pat) 556/16 zurückgenommen; DPMA-Beschluss 22.10.2019) | **sicher**: Klassen 35/39, Registernummer (Jahr getauscht), Vorgeschichte identisch |
| NS III/2019 | sportnord / NordSport: Widerspruch nach MaMoG, Benutzungszeitraum, Silbenrotation | nein | BPatG 22.05.2019, 29 W (pat) 47/16 | **sicher**: Marken, Klassen, Daten identisch |
| NS I/2020 | ACRIGLAS: Gattungsbezeichnung, Rechtsnachfolge, IR-Marke | nein | kein Beschluss gefunden (Vorbild offenbar „PLEXIGLAS“; Suche „Acryl“, „Plexiglas“ ohne Treffer) | Lehrfall |
| NS II/2020 | Balidrom: Pächterin meldet Bezeichnung des Bades an | ja (BGH-Beschluss abgedruckt) | BPatG 17.04.2014, 30 W (pat) 32/12 „LIQUIDROM“; BGH 15.10.2015, I ZB 44/14 „LIQUIDROM“ | **sicher**: Pachtvertrag, Ausschreibung, Anmeldung identisch |
| NS III/2020 | gelbfunk / Gelbe Seiten: Beschwerde per E-Mail, Rechtsnachfolge | nein | kein Beschluss gefunden (Volltextsuche „Gelbe“ nur ältere Löschungsverfahren 27 W (pat) 211/09) | Lehrfall |
| NS I/2021 | rahi / RAMI, „Kumas“: Beratungsfall | nein | kein Beschluss (Beratungsklausur) | Lehrfall |
| NS II/2021 | Black Panther / PANTHER: Wiedereinsetzung („Amtsliste“), Benutzung | nein | kein Beschluss gefunden | Lehrfall |
| NS III/2021 | vita+lebenskraft / VITA: Serienzeichen, Fristen | nein | BPatG 13.06.2019, 25 W (pat) 11/18 | **sicher**: Marken, Waren, Gutachten, Markenserie identisch |
| NS I/2022 | Silberpferd / POWER HORSE: Wiedereinsetzung, Einrede durch Prokuristen, Verwechslungsgefahr | ja (BPatG-Beschluss abgedruckt) | BPatG 26.07.2022, 26 W (pat) 38/17 „SILVER HORSE/POWER HORSE“; Rechtsbeschwerde BGH 01.06.2023, I ZB 65/22 | **sicher**: IR 1 037 284, Waren, Argumente identisch; Wiedereinsetzungsteil vom Prüfer hinzugefügt |
| NS II/2022 | EMOTION rims: Verletzung einer Unionsmarke, Beratungsschreiben | nein | kein Beschluss (Beratungsklausur) | Lehrfall |
| NS III/2022 | Dunes Berlin: zwei Widersprüche, Teilrechtskraft, Inlandsvertreter | nein | kein Beschluss gefunden | Lehrfall |
| NS I/2023 | gelbe Kaffeemühlen: Benutzungsmarke, Beratung | nein | kein Beschluss (Beratungsklausur) | Lehrfall |
| NS II/2023 | LOUIS HOTEL / Louis C. Jacob: öffentliche Zustellung, Benutzung auf Hotelutensilien | nein | kein Beschluss gefunden | Lehrfall |
| NS III/2023 | MEGACAPS: Widerspruch gegen Verfallsantrag vor Fristbeginn | ja (BPatG-Beschluss abgedruckt) | BPatG 08.02.2023, 29 W (pat) 30/22 „AUTOMATOR“ (IR 343 815) | **sicher**: Verfahrensgang und Daten identisch |
| NS I/2024 | KuKa S.p.A. / KreuzKamp: Aussetzung, Nichtigkeitsantrag gegen Unionsmarke | ja (BPatG-Beschluss abgedruckt) | BPatG 07.03.2022, 29 W (pat) 522/20 | **sicher**: Verzeichnisse, Aussetzungsantrag, Argumente identisch (Daten um zwei Jahre verschoben) |
| NS II/2024 | SofTax Esro.Med / EsroMedi: negative Feststellungsklage, Anwaltshaftung | nein | kein Beschluss (Verletzungs-/Haftungsfall vor dem LG) | Lehrfall |
| NS III/2024 | Dream A Job UG: Beschwerde einer gelöschten UG, Kosten bei Rücknahme | nein | Kernfrage nach BPatG 01.02.2024, 30 W (pat) 61/23 „BLIZZARD“; Löschungsdatum 4.7.2022 aus 25 W (pat) 52/21 übernommen | Vorbild, kein 1:1-Fall |
| NS I/2025 | NITREDA / INTREDA: Zuordnung der Widerspruchsgebühr | ja (BPatG-Beschluss abgedruckt) | BPatG 18.07.2022, 26 W (pat) 30/20 „Silberweide“ | **sicher**: Daten und Verfahrensgang identisch |
| NS II/2025 | Gold-Bärger / Stadtbäckerei Goldenberger: Widerspruch aus regionalem Unternehmenskennzeichen, Bösgläubigkeit | nein | BPatG 24.10.2022, 25 W (pat) 52/21 „Engelbrecht/Stadtbäckerei Engelbrecht GmbH“ | **sicher**: Verzeichnisse, Anträge, Beschwerdebegründung wörtlich übereinstimmend |
| NS III/2025 | Lurkis / Luki's u. a.: mehrere Widersprüche, Fristen, Erbfolge, Besetzung | nein | kein Beschluss (zusammengesetzter Lehrfall) | Lehrfall |

Nicht als Beschluss ermittelte Klausuren sind im Kurs dennoch enthalten; die Lösungen stützen sich dort auf
Gesetz, ständige Rechtsprechung und, soweit vorhanden, die Lösungshinweise.

## Erneut herunterladen

```bash
cd klausuren/ns && while read u; do curl -sL -A "Mozilla/5.0" -O "$u"; done < urls.txt
for f in *.pdf; do pdftotext -layout "$f" "txt/${f%.pdf}.txt"; done
```

# Klausuren Patentanwaltsprüfung – Technische Schutzrechte (TS)

Quelle: dieselbe Seite von kandidatentreff.de. Die PDFs (Aufgaben `PAP-<Jahr>-<Termin>-TS.pdf`, Lösungsskizzen
`L-PAP-2018-II-TS.pdf`, `L-PAP-2018-II-TS_2.pdf`, `L-PAP-2018-III-TS.pdf`) liegen unter `ts/`, die Textextrakte unter
`ts/txt/`; beide sind nicht versioniert, die URLs stehen in `ts/urls.txt`. Stand des Downloads: 24. September 2026.

Daraus entstand der Kurs **„Klausurtraining TS“** (`src/knowledge/kurse/p01_klausurtraining_ts.py`, Rechtsgebiet
`verfahren`, neben dem NS-Training) mit 61 Einheiten in neun Kapiteln (Aufbau, Anmeldung, Priorität/Teilung/Abzweigung, Neuheit und Vorbenutzung,
Einspruch Zulässigkeit, Einspruch Widerrufsgründe, Nichtigkeitsklage, Beschwerde und Wiedereinsetzung, Verletzung und
Entnahme). Die Einheiten verweisen auf die Begriffe, Schemata, Abgrenzungen und Leitentscheidungen des Patentpakets
(`src/knowledge/patent/`).

## Klausuren und Themen

Anders als die NS-Klausuren sind die TS-Klausuren durchweg konstruierte Lehrfälle ohne einen zugrunde liegenden
Beschluss (Namen wie „Flintenschuß KG“, Aktenzeichen wie „DE 111“). Eine Zuordnung zu Entscheidungen entfällt; wo eine
Leitentscheidung die Rechtsfrage trägt, ist sie in der Einheit verlinkt. Lösungsskizzen von kandidatentreff.de gibt es
nur für II/2018 und III/2018; sie decken sich mit den Lösungen im Kurs (Einspruch vor Veröffentlichung unzulässig,
Erledigung bei Verzicht, Abzweigung mit Gebrauchsmuster-Schonfrist).

| Klausur | Themen | Lösungsskizze | Einheiten |
|---|---|---|---|
| TS II/2018 | Fünf Einsprüche (vor Veröffentlichung, unsubstantiierte Vorbenutzung, PIZ, gemeinsame Gebühr, Erweiterung aus Zeichnung); Messevorführung und Gebrauchsmuster-Schonfrist | ja | p01d-1, p01d-6, p01e-1, p01e-2 |
| TS III/2018 | Nichtigkeit eines EP (Technizität Haustierfutter-Verfahren), WO-Anmeldung als Stand der Technik, Priorität bei vier US-Erfindern | ja | p01c-2, p01g-7 |
| TS I/2019 | Rechtskraft der Klageabweisung, Popularklage, Streitwert, Vergleich vor Zustellung an Verkündungs Statt | nein | p01g-1, p01g-2, p01g-3 |
| TS II/2019 | Englische Anmeldung ohne Übersetzung, Priorität eines Mitanmelders, Einspruch mit Vorbenutzung, vier Abzweigungen, Löschungsverfahren | nein | p01b-3, p01c-2, p01c-5, p01e-4 |
| TS III/2019 | Gebührenfreie Voranmeldung, Prioritätsintervall, § 83-Hinweis und verspäteter Hilfsantrag, Nichtangriff, Lizenzrückzahlung | nein | p01c-1, p01d-4, p01g-6 |
| TS I/2020 | Erloschenes Patent, Jahresgebühren-Dienstleister, Entschädigung § 33, Teilanmeldung, Priorität aus Figuren | nein | p01h-6, p01i-2, p01i-3 |
| TS II/2020 | Einspruchsschriftsatz mit sechs Druckschriften, verspätete Entgegenhaltung, Gebrauchsmuster für Verfahren, Kauf des Wettbewerbers | nein | p01f-3, p01e-7 |
| TS III/2020 | PIZ-Eingang, Übersetzung, Anhörungspflicht, Hilfsanträge aus Figuren, Anträge, Beschwerdefrist, Teilung | nein | p01b-4, p01c-4, p01f-7, p01h-4 |
| TS I/2021 | Teilung um 23:30 Uhr, sieben Vorbenutzungen, Ausstellungsschutz, Gebrauchsmuster, italienisches Handbuch | nein | p01c-3, p01d-2 |
| TS II/2021 | Beschwerde zweier Inhaberinnen, Beteiligtenstellung, Verschlechterungsverbot, einschränkendes nicht offenbartes Merkmal, Aliud | nein | p01f-4, p01h-2 |
| TS III/2021 | Berechtigungsanfrage, Vorbenutzungsrecht, Widerrufsgründe, Insolvenz, Nachanmeldung, Miterfinder, Klagesperre | nein | p01c-6, p01c-7, p01d-3, p01f-1, p01g-4, p01i-1, p01i-5 |
| TS I/2022 | Formmängel, drei Einsprüche (falsche Gebührennummer, Angestellte, geschwärzte Beweise), Verteidigung, Verletzung | nein | p01e-3 |
| TS II/2022 | Offene Bereichsangabe, PCT-Schrift als ältere Anmeldung, Beschwerdefrist, Vorbenutzung Las Vegas, Entnahme, Ausführbarkeit von Amts wegen | nein | p01d-5, p01f-5, p01h-1 |
| TS III/2022 | GbR als Anmelderin, Gebühren, Prüfungsantragsfrist, PCT-Nachanmeldung eines Miterfinders, Blogeintrag | nein | p01b-1, p01b-7, p01g-4 |
| TS I/2023 | Drei Einsprüche (PIZ Hamburg, Teilgebühr, Wiedereinsetzung), Beitritt, generische Formel, Rechtsbeschwerde | nein | p01d-5, p01d-7, p01e-2, p01e-6 |
| TS II/2023 | Doppelpatentierung DE/EP, Einspruch mit eigener älterer Anmeldung, Sprache, neue Beweismittel in der Beschwerde, Klageschrift | nein | p01f-2, p01g-5 |
| TS III/2023 | Mehrfachpriorität, Teilpriorität, Übersetzungsfehler, Rücknahme in der Anhörung | nein | p01c-8, p01h-7 |
| TS I/2024 | Widerrechtliche Entnahme (Konstruktionszeichnung), Einspruch, SEPA-Mandat, Hilfsantrag der Freundin, Inlandsvertreter | nein | p01f-6, p01h-3 |
| TS II/2024 | Elf Ansprüche mit 60 EUR, Priorität, Zurückweisung nach Fristablauf, Weiterbehandlung, Rache-Fachartikel, Miterfinder | nein | p01b-2, p01h-7, p01i-6 |
| TS III/2024 | Anmeldetag und nachgereichte Figuren, Anhörung in Abwesenheit, rechtliches Gehör, ausgeschlossener Richter | nein | p01b-6, p01h-5 |
| TS I/2025 | Gleiche Merkmale, anderes Substrat; Vorbenutzung; Miterfinderin; US-Priorität; Entnahme im Nichtigkeitsverfahren | nein | p01i-7 |
| TS II/2025 | Fehlgeschlagenes Fax am Prioritätstag, erfinderische Tätigkeit, vier Einsprüche (Vorbenutzung, Gebühren), Beschwerde | nein | p01b-5, p01e-2, p01e-5 |
| TS III/2025 | Geschäftsführer als Miterfinder, Priorität, Einspruch einer Kanzlei, Lizenz, Foreign Filing License, Rechtsnachfolge | nein | p01i-4 |

## Erneut herunterladen

```bash
cd klausuren/ts && while read u; do curl -sL -A "Mozilla/5.0" -O "$u"; done < urls.txt
mkdir -p txt && for f in *.pdf; do pdftotext -layout "$f" "txt/${f%.pdf}.txt"; done
```
