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
