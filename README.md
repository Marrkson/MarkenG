# Markenrecht – Wissensgraph, Karteikarten und Lernnavigator

Lernmaterial zum deutschen Markenrecht (MarkenG), aufgebaut auf einem Wissensgraphen aus
Gesetzestext, Begriffen, Prüfungsschemata, Abgrenzungen, IPWiki-Verweisen und BGH-/EuGH-Leitentscheidungen.

## Was ist drin?

| Pfad | Inhalt |
|---|---|
| `docs/index.html` | **Lernapp** (eigenständige HTML-Datei, offline nutzbar): Prüfungsschemata zum Durchklicken mit Definitionen, Normtext und Entscheidungen inline; Begriffe; Abgrenzungen; Rechtsprechung; Gesetz; Karteikarten-Modus; Graph-Explorer |
| `graph/markenrecht_graph.json` | **Wissensgraph** (600 Knoten, ca. 1.500 Kanten) |
| `flashcards/karteikarten.csv` | **Karteikarten** für Anki (Tab-getrennt: Vorderseite, Rückseite, Tags) |
| `flashcards/karteikarten.md` / `.json` | dieselben Karten als Markdown bzw. JSON |
| `data/markeng.md` / `.json` | Gesetzestext des MarkenG (Markdown-Original und geparste Fassung) |
| `src/knowledge/` | kuratiertes Fachwissen (Begriffe, Schemata, Abgrenzungen, Entscheidungen, IPWiki-Index) |
| `src/*.py`, `build.py` | Build-Pipeline |

## Lernapp starten

`docs/index.html` im Browser öffnen. Keine Installation, keine externen Ressourcen.

- **Prüfungsschemata**: Gutachtenaufbau z.B. für die Markenverletzung (§ 14), die Verwechslungsgefahr,
  den Bekanntheitsschutz, die Eintragungsfähigkeit (§§ 3, 8), §§ 23/24, Benutzungszwang, §§ 5/15,
  Widerspruch und Löschung. Jeder Prüfungspunkt lässt sich aufklappen; Begriffe (rot), Normen (blau)
  und Entscheidungen (violett) öffnen sich als Karte direkt an Ort und Stelle – auch verschachtelt.
- **Karteikarten**: 448 Karten (Definitionen, Umkehrkarten, Schemata, Prüfungspunkte, Abgrenzungen,
  Entscheidungen, Normen). Filter nach Typ und Thema, Karten pro Schema, Tastatursteuerung,
  Fortschritt „gewusst / nicht gewusst“ im Browser (localStorage).
- **Abgrenzungen**: Vergleichstabellen, z.B. Kennzeichnungskraft vs. Unterscheidungskraft,
  Verkehrsgeltung vs. Verkehrsdurchsetzung vs. Bekanntheit, Prägetheorie vs. selbständig
  kennzeichnende Stellung, Verfall vs. Nichtigkeit.
- **Graph-Explorer**: Nachbarschaft eines Knotens als Kräftegraph, Klick wechselt das Zentrum.
- **Suche** (Taste `/`): Begriffe, Paragraphen (z.B. `23`), Entscheidungen (Name oder Aktenzeichen).

## Graph-Modell

Knotentypen: `norm` (Paragraph mit Absätzen), `concept` (Definition + Erläuterung), `schema`,
`step` (Prüfungspunkt, baumförmig), `case` (Entscheidung mit Kernaussage, Aktenzeichen, Fundstelle,
dejure-Link), `distinction` (Vergleichstabelle), `source` (IPWiki-Artikel).

Kanten: `defined_in`, `related_to`, `illustrated_by`, `documented_in`, `interprets`, `has_step`,
`next_step`, `uses_concept`, `cites`, `applies`, `contrasts`.

## Karteikarten in Anki importieren

`flashcards/karteikarten.csv` → Anki „Datei › Importieren“, Feldtrenner Tab, HTML in Feldern erlauben,
drittes Feld als Tags.

## Neu bauen

```bash
python3 build.py
```

Die Pipeline parst `data/markeng.md`, baut den Graphen aus `src/knowledge/`, erzeugt die Karten und
rendert die HTML-App aus `src/templates/app.html`. Inhalte werden ausschließlich in `src/knowledge/`
gepflegt.

## Quellen und Hinweise

- **Gesetzestext**: gesetze-im-internet.de, bezogen über den Spiegel
  [bundestag/gesetze](https://github.com/bundestag/gesetze) (Stand im Repo: Änderungen bis 2021
  berücksichtigt; Metadaten in `data/markeng.json`).
- **IPWiki** (www.ipwiki.de): Die Artikel konnten aus der Build-Umgebung nicht direkt geladen werden
  (Netzwerk-Sperre). `src/knowledge/ipwiki.py` enthält den per Websuche ermittelten Artikelindex mit
  Kurzinhalt und Link; die Begriffe verweisen darauf.
- **Rechtsprechung**: 96 Entscheidungen (75 BGH, 21 EuGH), per Websuche recherchiert und mit
  Aktenzeichen/Datum gegen dejure.org, bundesgerichtshof.de und Fachveröffentlichungen abgeglichen.
  Die Kernaussagen sind Paraphrasen für Lernzwecke – für Zitate den Volltext prüfen
  (Link „dejure ↗“ in jeder Entscheidung).
- Die Definitionen und Schemata folgen der ständigen Rechtsprechung von BGH und EuGH sowie der
  gängigen Lehrbuchsystematik; sie ersetzen kein Lehrbuch und keine Rechtsberatung.
