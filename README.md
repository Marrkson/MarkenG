# IPelico – Markenrecht in Fällen: Fallkurs, Wissensgraph, Karteikarten, Lernnavigator

Lernmaterial zum deutschen Markenrecht (MarkenG), aufgebaut auf einem Wissensgraphen aus
Gesetzestext, Begriffen, Prüfungsschemata, Abgrenzungen, IPWiki-Verweisen und BGH-/EuGH-Leitentscheidungen.

## Was ist drin?

| Pfad | Inhalt |
|---|---|
| `docs/index.html` | **IPelico**, der Fallkurs: 24 Kurse in zwei Rechtsgebieten (Markenrecht, Einheitliches Patentgericht), 74 Kapitel, 409 Lerneinheiten (261 Fälle mit Ja/Nein, 81 Wissensfragen, 31 Prüfungsschemata, 36 Einführungen), sofortiges Feedback, Wiederholung, Streak und Punkte; Fortschritt per Cookie; Gestaltung nach `DESIGN.md` |
| `docs/didaktik.md` | Didaktisches Konzept von IPelico und Kursaufbau |
| `DESIGN.md`, `src/templates/ipelico/` | Gestaltungsrichtlinie (Glas-Stil, Rhein-IP-Blau, Zeichen, Icons, Schriften) und die Assets dazu; `tools/gen_assets.py` erzeugt die Icons |
| `docs/navigator/index.html` | **Lernnavigator** (eigenständige HTML-Datei, offline nutzbar): Prüfungsschemata zum Durchklicken mit Definitionen, Normtext und Entscheidungen inline; Begriffe; Abgrenzungen; Rechtsprechung; Gesetz; Karteikarten-Modus; Graph-Explorer |
| `graph/markenrecht_graph.json` | **Wissensgraph** (2.180 Knoten, ca. 7.500 Kanten; Markenrecht und EPG in einem Graphen) |
| `flashcards/karteikarten.csv` | **Karteikarten** für Anki (Tab-getrennt: Vorderseite, Rückseite, Tags) |
| `flashcards/karteikarten.md` / `.json` | dieselben Karten als Markdown bzw. JSON |
| `data/markeng.md` / `.json` | Gesetzestext des MarkenG (Markdown-Original und geparste Fassung) |
| `src/knowledge/markenrl.py` | Markenrechtsrichtlinie (EU) 2015/2436: alle 57 Artikel als Paraphrase je Absatz, Erwägungsgründe, Umsetzungstabelle zum MarkenG |
| `src/knowledge/durchsetzungsrl.py` | Durchsetzungsrichtlinie 2004/48/EG: alle 22 Artikel im amtlichen Wortlaut (berichtigte Fassung ABl. L 195/16), Erwägungsgründe, je Artikel die Umsetzung in MarkenG, PatG, GebrMG, DesignG, UrhG, HalblSchG, SortSchG und im allgemeinen Recht; Umsetzungstabelle über alle Gesetze |
| `src/knowledge/` | kuratiertes Fachwissen (Begriffe, Schemata, Abgrenzungen, Entscheidungen, IPWiki-Index) |
| `src/knowledge/klausur.py` | Klausurwissen zur Aufsichtsarbeit „Nichttechnische Schutzrechte“: Aufgabentypen, Zeitplan, Fristen- und Gebührentabellen, Tenorformeln, typische Fehler, alle 23 Klausuren (Export: `data/klausur.json`) |
| `src/knowledge/kurse/` | die vierzehn Fallkurse (`data/kurse.json` ist der Export); Kurs 14 „Die Durchsetzungsrichtlinie 2004/48/EG“ erklärt Auskunft, Vorlage, Sicherung, Eilrechtsschutz, Mittelspersonen und Kosten anhand der EuGH-Rechtsprechung und zeigt die Umsetzungstabelle für alle Schutzrechtsgesetze; Kurs 12 „Klausurtraining NS“ folgt den Klausuren der Patentanwaltsprüfung, Kurs 13 „Wirksamkeit und Zulässigkeit“ übt das Verfahrensrecht nach Verfahrensart mit den Anschlussnormen aus BGB, HGB, GmbHG, ZPO, GVG und InsO |
| `klausuren/` | NS-Klausuren 2018–2025 (kandidatentreff.de) und die Zuordnung zu den zugrunde liegenden BPatG-/BGH-Beschlüssen (`klausuren/README.md`) |
| `src/*.py`, `build.py` | Build-Pipeline |

## IPelico starten

`docs/index.html` im Browser öffnen, am besten über einen kleinen Webserver (`python3 -m http.server` im Ordner `docs`), damit der Fortschritt in Cookies gespeichert wird. Als lokale Datei geöffnet, nutzt die App automatisch den Browserspeicher.

- **Kurse → Kapitel → Einheiten**: Sachverhalt, Frage, Ja/Nein oder Auswahl, sofortiges Feedback, Lösung im Gutachtenstil, Merksatz; Begriffe, Normen und Entscheidungen inline aufklappbar.
- **Wiederholen**: falsch beantwortete Fälle und fällige Wiederholungen (Intervalle 1, 3, 7, 14, 30, 60 Tage).
- **Profil**: Streak, Punkte, Fortschritt je Kurs, Fortschritt löschen.
- Tastatur: `J`/`N`, `1`–`4`, `Enter`.

## Lernnavigator starten

`docs/navigator/index.html` im Browser öffnen. Keine Installation, keine externen Ressourcen.

- **Klausur NS**: eigene Sektion zur Aufsichtsarbeit „Nichttechnische Schutzrechte“ der Patentanwaltsprüfung.
  Aufgabentypen mit Häufigkeit und Aufgabenformeln, Zeitplan für vier Stunden, das Zulässigkeitsraster als
  klickbare Prüfungsschemata (Widerspruch, Beschwerde, Wiedereinsetzung), Fristen- und Gebührentabellen
  mit Zahlungstag nach der PatKostZV, zwölf Tenorformeln aus veröffentlichten Beschlüssen, Textbausteine,
  typische Fehler und alle 23 Klausuren 2018 bis 2025 mit Schwerpunkten und zugeordnetem Beschluss.
- **Markenrechtsrichtlinie**: alle 57 Artikel der RL (EU) 2015/2436 mit Kapitelgliederung, je Artikel die umsetzenden MarkenG-Normen, Hinweise zu den Änderungen durch das MaMoG 2019 und die zugehörigen EuGH-Entscheidungen; Umsetzungstabelle als Abgrenzung; Schema „Markenrechtsrichtlinie anwenden“.
- **Durchsetzungsrichtlinie**: alle 22 Artikel der RL 2004/48/EG im Wortlaut, je Artikel die Umsetzung in allen sieben Schutzrechtsgesetzen und in ZPO/BGB (Tabelle „Artikel → Gesetz“), Schema „Durchsetzung einer Markenverletzung“, Abgrenzung §§ 19/19a/19b und 16 EuGH-/BGH-Entscheidungen (Coty, Constantin Film, L'Oréal/eBay, Tommy Hilfiger, NovaText, Koch Media, …).
- **Prüfungsschemata**: Gutachtenaufbau z.B. für die Markenverletzung ([§ 14](https://www.gesetze-im-internet.de/markeng/__14.html)), die Verwechslungsgefahr,
  den Bekanntheitsschutz, die Eintragungsfähigkeit (§§ [3](https://www.gesetze-im-internet.de/markeng/__3.html), [8](https://www.gesetze-im-internet.de/markeng/__8.html)), §§ [23](https://www.gesetze-im-internet.de/markeng/__23.html)/[24](https://www.gesetze-im-internet.de/markeng/__24.html), Benutzungszwang, §§ [5](https://www.gesetze-im-internet.de/markeng/__5.html)/[15](https://www.gesetze-im-internet.de/markeng/__15.html),
  Widerspruch und Löschung, die relativen Schutzhindernisse im Register ([§ 9 Abs. 1 Nr. 1](https://www.gesetze-im-internet.de/markeng/__9.html)-3) sowie
  das Vorgehen aus einer Unionsmarke (UMV, [§ 125b](https://www.gesetze-im-internet.de/markeng/__125b.html) ff.) und aus einer IR-Marke (PMMA, §§ [112](https://www.gesetze-im-internet.de/markeng/__112.html)-[125](https://www.gesetze-im-internet.de/markeng/__125.html)). Jeder Prüfungspunkt lässt sich aufklappen; Begriffe (rot), Normen (blau)
  und Entscheidungen (violett) öffnen sich als Karte direkt an Ort und Stelle – auch verschachtelt.
- **Karteikarten**: 1.248 Karten (Definitionen, Umkehrkarten, Schemata, Prüfungspunkte, Abgrenzungen,
  Entscheidungen, Normen). Filter nach Typ und Thema, Karten pro Schema, Tastatursteuerung,
  Fortschritt „gewusst / nicht gewusst“ im Browser (localStorage).
- **Abgrenzungen**: Vergleichstabellen, z.B. Kennzeichnungskraft vs. Unterscheidungskraft,
  Verkehrsgeltung vs. Verkehrsdurchsetzung vs. Bekanntheit, Prägetheorie vs. selbständig
  kennzeichnende Stellung, Verfall vs. Nichtigkeit.
- **Graph-Explorer**: Nachbarschaft eines Knotens als Kräftegraph, Klick wechselt das Zentrum.
- **Suche** (Taste `/`): Begriffe, Paragraphen (z.B. `23`), Entscheidungen (Name oder Aktenzeichen).

## Einheitliches Patentgericht (EPGÜ, VerfO, EPG-Rechtsprechung)

Seit September 2026 enthält der Graph ein zweites Wissenspaket zum Verfahren vor dem Einheitlichen Patentgericht
(`src/knowledge/upc/`), im selben Graphen wie das Markenrecht und über die Durchsetzungsrichtlinie 2004/48/EG mit ihm
verbunden (Art. 59 bis 69 und 80 EPGÜ tragen `entspricht`-Kanten zu den Richtlinienartikeln, die Tabelle
„Durchsetzungsrichtlinie: Umsetzung im EPGÜ, in der VerfO und im deutschen Recht“ stellt EPGÜ, VerfO, MarkenG und PatG nebeneinander).

- **EPGÜ**: alle 89 Artikel im amtlichen deutschen Wortlaut (englischer Titel und Wortlaut je Artikel verlinkt), gegliedert nach
  Teilen und Kapiteln, mit Lern- und Klausurhinweisen zu den Kernnormen (Art. 25 bis 34, 47 bis 49, 56 bis 69, 73 bis 83).
- **Verfahrensordnung**: alle 303 Regeln der konsolidierten deutschen Fassung (Änderungen vom 4.11.2025, in Kraft seit 1.1.2026)
  mit Präambel, englischen Regeltiteln und der Kante „Bezug zum Übereinkommen“ (`konkretisiert`) zu den EPGÜ-Artikeln.
- **EPG-Rechtsprechung**: alle Entscheidungen und Anordnungen des EPG seit dem 1. Juni 2023 aus der RheinIP-Datenbank
  (`data/upc_decisions.json`, Volltexte bleiben in der Datenbank) mit Leitsätzen, Schlagworten und den zitierten Artikeln und
  Regeln; in IPelico als Datenbank `#/epg` mit Suche und Filtern (Kammer, Verfahrensart, nur mit Leitsatz), je Artikel und Regel
  unter `#/epg/norm/…` und als Abschnitt auf jeder EPGÜ-/VerfO-Lernkarte; jeder Norm-Knoten trägt die Zahl der zitierenden Entscheidungen.
- **Kuratiert**: 80 Begriffe, 65 Leitentscheidungen (überwiegend Berufungsgericht, Kernaussage auf Deutsch), 8 Prüfungsschemata
  (Zuständigkeit, Verletzungsklage, einstweilige Maßnahmen, Beweissicherung, Nichtigkeit, Berufung, Kosten, Vertraulichkeit),
  8 Abgrenzungen (u.a. Lokal- vs. Zentralkammer, Einspruch vs. Klageerwiderung, R. 262 vs. R. 262A, EPG vs. deutsches Verfahren).
- **Kurse 15 bis 24** (Rechtsgebiet „EPG“): Grundlagen, Zuständigkeit, Verletzungsverfahren, Verletzung und Auslegung, einstweilige
  Maßnahmen und Beweis, Nichtigkeit, Rechtsfolgen und Vollstreckung, Kosten, Berufung, EPGÜ und Durchsetzungsrichtlinie.
- **Zitierweise** in Texten und `norms`-Feldern: `Art. 33 Abs. 1 EPGÜ`, `R. 19.1 VerfO`, `R. 262A VerfO` (auch `UPCA`, `RoP`);
  `Art. … EPGÜ` verlinkt auf EUR-Lex, `R. … VerfO` auf das VerfO-PDF.

Aktualisieren: `python3 tools/fetch_upc.py` (Postgres-Zugang aus `~/github/RheinIP/.env`; `--no-net` nutzt nur die Datenbank und
den lokalen Cache der Normtexte), danach `python3 build.py`. Vorgehen und Datenmodell: `PLAYBOOK.md` Abschnitt 11.

## Graph-Modell

Knotentypen: `norm` (Paragraph mit Absätzen), `eunorm` (Artikel der MarkenRL als Paraphrase, der DurchsetzungsRL und des EPGÜ im Wortlaut sowie die Regeln der VerfO; Feld `rl` unterscheidet sie (`markenrl`, `durchsetzungsrl`, `upca`, `rop`), `zitat` die Zitierform (`Art.`/`R.`), `umsetzung_weitere` nennt die Parallelnormen der anderen Gesetze, `zitiert` die Zahl der EPG-Entscheidungen), `concept` (Definition + Erläuterung), `schema`,
`step` (Prüfungspunkt, baumförmig), `case` (Entscheidung mit Kernaussage, Aktenzeichen, Fundstelle,
dejure-Link), `distinction` (Vergleichstabelle), `source` (IPWiki-Artikel), `course`, `chapter`, `unit`
(Fallkurs; Einheiten verweisen mit `trains`, `cites`, `applies`, `covers` auf Begriffe, Entscheidungen, Normen, Prüfungspunkte und Abgrenzungstabellen).

Kanten: `defined_in`, `related_to`, `illustrated_by`, `documented_in`, `interprets`, `implements` (MarkenG-Norm setzt einen Richtlinienartikel um), `entspricht` (EPGÜ-Artikel setzt einen Artikel der DurchsetzungsRL für das EPG um), `konkretisiert` (VerfO-Regel → EPGÜ-Artikel), `has_step`,
`next_step`, `uses_concept`, `cites`, `applies`, `contrasts`.

## Karteikarten in Anki importieren

`flashcards/karteikarten.csv` → Anki „Datei › Importieren“, Feldtrenner Tab, HTML in Feldern erlauben,
drittes Feld als Tags.

## Neu bauen

```bash
python3 build.py
```

Die Pipeline parst `data/markeng.md`, baut den Graphen aus `src/knowledge/` (inklusive Kursen), erzeugt die Karten und
rendert beide Apps aus `src/templates/app.html` und `src/templates/kurs.html`; in IPelico werden dabei das SVG-Sprite
(Icons, Zeichen) und die Plex-Schriften aus `src/templates/ipelico/` eingebettet. Inhalte werden ausschließlich in `src/knowledge/`
gepflegt.

## Deployment auf GitHub Pages

Der Ordner `docs/` ist die fertige Website; er wird mitversioniert. Zwei Wege, beide brauchen
einmalig einen Klick in den Repo-Settings:

**A. GitHub Actions (empfohlen, baut bei jedem Push aus den Quellen):**
Settings → Pages → Source „GitHub Actions“ wählen. Danach läuft `.github/workflows/pages.yml`
bei jedem Push auf `main` (und manuell über „Run workflow“): `python3 build.py`, dann Upload von
`docs/`. Änderungen in `src/knowledge/` erscheinen so auch dann, wenn man vergisst, lokal zu bauen.

**B. Direkt aus dem Branch (kein Workflow nötig):**
Settings → Pages → Source „Deploy from a branch“, Branch `main`, Ordner `/docs`. GitHub
veröffentlicht dann die eingecheckten HTML-Dateien bei jedem Push. Vor dem Push `python3 build.py`
ausführen, damit `docs/` aktuell ist. Bei diesem Weg die Datei `.github/workflows/pages.yml`
löschen, sonst läuft der Workflow leer mit.

| URL | Inhalt |
|---|---|
| `https://<owner>.github.io/MarkenG/` | IPelico (Fallkurs) |
| `https://<owner>.github.io/MarkenG/navigator/` | Lernnavigator |

Der Lernfortschritt liegt in Cookies, die auf den Pfad der Seite begrenzt sind.

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
  GebrMG, DesignG, HalblSchG, SortSchG, HGB, GKG und weitere; Tabelle `LAWS` im Modul).
- Tabellen mit einer Spalte je Gesetz: `qualify(text, law)` hängt Zitaten ohne Gesetzesangabe das
  Gesetz der Spalte an („§ 140b“ → „§ 140b PatG“), damit sie nicht auf das MarkenG verlinken.
- Ketten werden je Vorschrift einzeln verlinkt: `§§ 9 bis 13`, `§§ 3, 7, 8`, `§§ 23/24`,
  `§§ 112-125`.
- Unionsrecht (MarkenRL, DurchsetzungsRL, UMV, AEUV) steht nicht auf gesetze-im-internet.de; Zitate führen deshalb auf
  das Dokument bei EUR-Lex. Internationale Abkommen (PMMA, PVÜ) bleiben unverlinkt.
- Normen-Chips tragen zusätzlich ein ↗ direkt zur amtlichen Fassung.

Erkennung prüfen: `python3 src/knowledge/gesetze.py` gibt Beispielzitate mit Links aus.

## Quellen und Hinweise

- **Markenrechtsrichtlinie (EU) 2015/2436**: EUR-Lex war aus der Build-Umgebung nicht erreichbar.
  Die Artikel in `src/knowledge/markenrl.py` sind deshalb inhaltlich vollständige **Paraphrasen**
  je Absatz, kein amtlicher Wortlaut. Für Zitate den Text auf
  [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2436) prüfen; beide
  Apps und die Karteikarten weisen darauf hin.
- **Durchsetzungsrichtlinie 2004/48/EG**: Der amtliche deutsche Wortlaut (berichtigte Fassung,
  ABl. L 195 vom 2.6.2004, S. 16) wurde über den EU-Cellar geladen; `src/knowledge/durchsetzungsrl.py`
  gibt ihn je Absatz wieder (Buchstabenaufzählungen eingerückt, Fußnoten weggelassen). Die Parallelnormen
  in PatG, GebrMG, DesignG, UrhG, HalblSchG und SortSchG sind am XML von gesetze-im-internet.de geprüft.

- **Gesetzestext**: gesetze-im-internet.de, bezogen über den Spiegel
  [bundestag/gesetze](https://github.com/bundestag/gesetze) (Stand im Repo: Änderungen bis 2021
  berücksichtigt; Metadaten in `data/markeng.json`).
- **IPWiki** (www.ipwiki.de): Die Artikel konnten aus der Build-Umgebung nicht direkt geladen werden
  (Netzwerk-Sperre). `src/knowledge/ipwiki.py` enthält den per Websuche ermittelten Artikelindex mit
  Kurzinhalt und Link; die Begriffe verweisen darauf.
- **Rechtsprechung**: 131 Entscheidungen zum Markenrecht (81 BGH, 40 EuGH, 10 BPatG), per Websuche recherchiert und mit
  Aktenzeichen/Datum gegen dejure.org, bundesgerichtshof.de und Fachveröffentlichungen abgeglichen.
  Die Kernaussagen sind Paraphrasen für Lernzwecke – für Zitate den Volltext prüfen
  (Link „dejure ↗“ in jeder Entscheidung).
- Die Definitionen und Schemata folgen der ständigen Rechtsprechung von BGH und EuGH sowie der
  gängigen Lehrbuchsystematik; sie ersetzen kein Lehrbuch und keine Rechtsberatung.
