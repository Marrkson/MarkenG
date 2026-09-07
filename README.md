# Markenrecht – Wissensgraph, Karteikarten und Lernnavigator

Lernmaterial zum deutschen Markenrecht (MarkenG), aufgebaut auf einem Wissensgraphen aus
Gesetzestext, Begriffen, Prüfungsschemata, Abgrenzungen, IPWiki-Verweisen und BGH-/EuGH-Leitentscheidungen.

## Was ist drin?

| Pfad | Inhalt |
|---|---|
| `docs/kurse/index.html` | **Fallkurs** im Jurafuchs-Format: 10 Kurse, 125 Lerneinheiten (Fälle mit Ja/Nein, Wissensfragen, Prüfungsschemata, Einführungen), sofortiges Feedback, Wiederholung, Streak und Punkte; Fortschritt per Cookie |
| `docs/didaktik.md` | Analyse des Jurafuchs-Formats und Kursaufbau |
| `docs/index.html` | **Lernnavigator** (eigenständige HTML-Datei, offline nutzbar): Prüfungsschemata zum Durchklicken mit Definitionen, Normtext und Entscheidungen inline; Begriffe; Abgrenzungen; Rechtsprechung; Gesetz; Karteikarten-Modus; Graph-Explorer |
| `graph/markenrecht_graph.json` | **Wissensgraph** (820 Knoten, ca. 2.600 Kanten) |
| `flashcards/karteikarten.csv` | **Karteikarten** für Anki (Tab-getrennt: Vorderseite, Rückseite, Tags) |
| `flashcards/karteikarten.md` / `.json` | dieselben Karten als Markdown bzw. JSON |
| `data/markeng.md` / `.json` | Gesetzestext des MarkenG (Markdown-Original und geparste Fassung) |
| `src/knowledge/markenrl.py` | Markenrechtsrichtlinie (EU) 2015/2436: alle 57 Artikel als Paraphrase je Absatz, Erwägungsgründe, Umsetzungstabelle zum MarkenG |
| `src/knowledge/` | kuratiertes Fachwissen (Begriffe, Schemata, Abgrenzungen, Entscheidungen, IPWiki-Index) |
| `src/knowledge/kurse/` | die zehn Fallkurse (`data/kurse.json` ist der Export) |
| `src/*.py`, `build.py` | Build-Pipeline |

## Fallkurs starten

`docs/kurse/index.html` im Browser öffnen, am besten über einen kleinen Webserver (`python3 -m http.server` im Ordner `docs`), damit der Fortschritt in Cookies gespeichert wird. Als lokale Datei geöffnet, nutzt die App automatisch den Browserspeicher.

- **Kurse → Kapitel → Einheiten**: Sachverhalt, Frage, Ja/Nein oder Auswahl, sofortiges Feedback, Lösung im Gutachtenstil, Merksatz; Begriffe, Normen und Entscheidungen inline aufklappbar.
- **Wiederholen**: falsch beantwortete Fälle und fällige Wiederholungen (Intervalle 1, 3, 7, 14, 30, 60 Tage).
- **Profil**: Streak, Punkte, Fortschritt je Kurs, Fortschritt löschen.
- Tastatur: `J`/`N`, `1`–`4`, `Enter`.

## Lernnavigator starten

`docs/index.html` im Browser öffnen. Keine Installation, keine externen Ressourcen.

- **Markenrechtsrichtlinie**: alle 57 Artikel der RL (EU) 2015/2436 mit Kapitelgliederung, je Artikel die umsetzenden MarkenG-Normen, Hinweise zu den Änderungen durch das MaMoG 2019 und die zugehörigen EuGH-Entscheidungen; Umsetzungstabelle als Abgrenzung; Schema „Markenrechtsrichtlinie anwenden“.
- **Prüfungsschemata**: Gutachtenaufbau z.B. für die Markenverletzung ([§ 14](https://www.gesetze-im-internet.de/markeng/__14.html)), die Verwechslungsgefahr,
  den Bekanntheitsschutz, die Eintragungsfähigkeit (§§ [3](https://www.gesetze-im-internet.de/markeng/__3.html), [8](https://www.gesetze-im-internet.de/markeng/__8.html)), §§ [23](https://www.gesetze-im-internet.de/markeng/__23.html)/[24](https://www.gesetze-im-internet.de/markeng/__24.html), Benutzungszwang, §§ [5](https://www.gesetze-im-internet.de/markeng/__5.html)/[15](https://www.gesetze-im-internet.de/markeng/__15.html),
  Widerspruch und Löschung, die relativen Schutzhindernisse im Register ([§ 9 Abs. 1 Nr. 1](https://www.gesetze-im-internet.de/markeng/__9.html)-3) sowie
  das Vorgehen aus einer Unionsmarke (UMV, [§ 125b](https://www.gesetze-im-internet.de/markeng/__125b.html) ff.) und aus einer IR-Marke (PMMA, §§ [112](https://www.gesetze-im-internet.de/markeng/__112.html)-[125](https://www.gesetze-im-internet.de/markeng/__125.html)). Jeder Prüfungspunkt lässt sich aufklappen; Begriffe (rot), Normen (blau)
  und Entscheidungen (violett) öffnen sich als Karte direkt an Ort und Stelle – auch verschachtelt.
- **Karteikarten**: 500 Karten (Definitionen, Umkehrkarten, Schemata, Prüfungspunkte, Abgrenzungen,
  Entscheidungen, Normen). Filter nach Typ und Thema, Karten pro Schema, Tastatursteuerung,
  Fortschritt „gewusst / nicht gewusst“ im Browser (localStorage).
- **Abgrenzungen**: Vergleichstabellen, z.B. Kennzeichnungskraft vs. Unterscheidungskraft,
  Verkehrsgeltung vs. Verkehrsdurchsetzung vs. Bekanntheit, Prägetheorie vs. selbständig
  kennzeichnende Stellung, Verfall vs. Nichtigkeit.
- **Graph-Explorer**: Nachbarschaft eines Knotens als Kräftegraph, Klick wechselt das Zentrum.
- **Suche** (Taste `/`): Begriffe, Paragraphen (z.B. `23`), Entscheidungen (Name oder Aktenzeichen).

## Graph-Modell

Knotentypen: `norm` (Paragraph mit Absätzen), `eunorm` (Artikel der MarkenRL, Paraphrase), `concept` (Definition + Erläuterung), `schema`,
`step` (Prüfungspunkt, baumförmig), `case` (Entscheidung mit Kernaussage, Aktenzeichen, Fundstelle,
dejure-Link), `distinction` (Vergleichstabelle), `source` (IPWiki-Artikel), `course`, `chapter`, `unit`
(Fallkurs; Einheiten verweisen mit `trains`, `cites`, `applies`, `covers` auf Begriffe, Entscheidungen, Normen und Prüfungspunkte).

Kanten: `defined_in`, `related_to`, `illustrated_by`, `documented_in`, `interprets`, `implements` (MarkenG-Norm setzt MarkenRL-Artikel um), `has_step`,
`next_step`, `uses_concept`, `cites`, `applies`, `contrasts`.

## Karteikarten in Anki importieren

`flashcards/karteikarten.csv` → Anki „Datei › Importieren“, Feldtrenner Tab, HTML in Feldern erlauben,
drittes Feld als Tags.

## Neu bauen

```bash
python3 build.py
```

Die Pipeline parst `data/markeng.md`, baut den Graphen aus `src/knowledge/` (inklusive Kursen), erzeugt die Karten und
rendert beide Apps aus `src/templates/app.html` und `src/templates/kurs.html`. Inhalte werden ausschließlich in `src/knowledge/`
gepflegt.

## Deployment auf GitHub Pages

Der Workflow `.github/workflows/pages.yml` läuft bei jedem Push auf `main` (und manuell über
„Run workflow“). Er baut Graph, Karteikarten und beide Apps neu und veröffentlicht:

| URL | Inhalt |
|---|---|
| `https://<owner>.github.io/MarkenG/` | Fallkurs (Jurafuchs-Format) |
| `https://<owner>.github.io/MarkenG/navigator/` | Lernnavigator |

Beim ersten Lauf aktiviert der Workflow GitHub Pages selbst (Quelle „GitHub Actions“). Falls das
an fehlenden Rechten scheitert: Settings → Pages → Source „GitHub Actions“ wählen und den Workflow
erneut starten. Der Lernfortschritt liegt in Cookies, die auf den Pfad `/MarkenG/` begrenzt sind.

## Gesetzeszitate

Jedes Zitat einer deutschen Vorschrift wird automatisch auf
[gesetze-im-internet.de](https://www.gesetze-im-internet.de/) verlinkt: in beiden Web-Apps
(Fragen, Lösungen, Definitionen, Entscheidungen, Vergleichstabellen, Gesetzestext) sowie in
`flashcards/karteikarten.md` (Markdown-Links) und `flashcards/karteikarten.csv` (HTML-Links
für Anki).

Die Regeln stehen nur an einer Stelle, in `src/knowledge/gesetze.py`; die JavaScript-Fassung
für die HTML-Apps wird daraus erzeugt (`js_source`), damit beide identisch verlinken:

- Ohne Gesetzesangabe gilt das MarkenG: `§ 14 Abs. 2 Nr. 2` führt zu `markeng/__14.html`.
- Andere deutsche Gesetze werden an ihrer Abkürzung erkannt (BGB, UWG, ZPO, GG, UrhG, PatG,
  HGB, TMG, GKG und weitere; Tabelle `LAWS` im Modul).
- Ketten werden je Vorschrift einzeln verlinkt: `§§ 9 bis 13`, `§§ 3, 7, 8`, `§§ 23/24`,
  `§§ 112-125`.
- Unionsrecht (MarkenRL, UMV, AEUV) steht nicht auf gesetze-im-internet.de; Zitate führen deshalb auf
  das Dokument bei EUR-Lex. Internationale Abkommen (PMMA, PVÜ) bleiben unverlinkt.
- Normen-Chips tragen zusätzlich ein ↗ direkt zur amtlichen Fassung.

Erkennung prüfen: `python3 src/knowledge/gesetze.py` gibt Beispielzitate mit Links aus.

## Quellen und Hinweise

- **Markenrechtsrichtlinie (EU) 2015/2436**: EUR-Lex war aus der Build-Umgebung nicht erreichbar.
  Die Artikel in `src/knowledge/markenrl.py` sind deshalb inhaltlich vollständige **Paraphrasen**
  je Absatz, kein amtlicher Wortlaut. Für Zitate den Text auf
  [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2436) prüfen; beide
  Apps und die Karteikarten weisen darauf hin.

- **Gesetzestext**: gesetze-im-internet.de, bezogen über den Spiegel
  [bundestag/gesetze](https://github.com/bundestag/gesetze) (Stand im Repo: Änderungen bis 2021
  berücksichtigt; Metadaten in `data/markeng.json`).
- **IPWiki** (www.ipwiki.de): Die Artikel konnten aus der Build-Umgebung nicht direkt geladen werden
  (Netzwerk-Sperre). `src/knowledge/ipwiki.py` enthält den per Websuche ermittelten Artikelindex mit
  Kurzinhalt und Link; die Begriffe verweisen darauf.
- **Rechtsprechung**: 101 Entscheidungen (75 BGH, 26 EuGH), per Websuche recherchiert und mit
  Aktenzeichen/Datum gegen dejure.org, bundesgerichtshof.de und Fachveröffentlichungen abgeglichen.
  Die Kernaussagen sind Paraphrasen für Lernzwecke – für Zitate den Volltext prüfen
  (Link „dejure ↗“ in jeder Entscheidung).
- Die Definitionen und Schemata folgen der ständigen Rechtsprechung von BGH und EuGH sowie der
  gängigen Lehrbuchsystematik; sie ersetzen kein Lehrbuch und keine Rechtsberatung.
