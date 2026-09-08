# Playbook: Wissensgraph und Lernkurse für ein Rechtsgebiet erstellen

Dieses Dokument beschreibt, wie der Markenrecht-Graph, die Karteikarten, der Lernnavigator und der
Fallkurs entstanden sind, damit derselbe Prozess für weitere Gesetze (PatG, GebrMG, DesignG,
ArbnErfG, PatKostG, IntPatÜG, ERVDPMAV, …) wiederholt werden kann. Es ist als Arbeitsanweisung
für einen Agenten geschrieben. Reihenfolge, Konventionen und Prüfschritte sind verbindlich; die
Inhalte sind das, was den Aufwand ausmacht.

## 0. Ergebnisbild

Ein Rechtsgebiet ist fertig, wenn es Folgendes gibt:

| Artefakt | Pfad | Erzeugt durch |
|---|---|---|
| Gesetzestext (Markdown + JSON) | `data/<gesetz>.md`, `data/<gesetz>.json` | `src/parse_markeng.py` (zu verallgemeinern, s. Abschnitt 8) |
| Kuratiertes Wissen | `src/knowledge/{concepts,schemata,distinctions,cases,ipwiki}.py` | Hand |
| Kurse (Fallformat) | `src/knowledge/kurse/k*.py` | Hand |
| Wissensgraph | `graph/markenrecht_graph.json` | `src/build_graph.py` |
| Karteikarten (JSON, Anki-CSV, Markdown) | `flashcards/` | `src/build_flashcards.py` |
| Fallkurs (Website-Startseite) | `docs/index.html` | `src/build_kurs.py` + `src/templates/kurs.html` |
| Lernnavigator | `docs/navigator/index.html` | `src/build_html.py` + `src/templates/app.html` |

`python3 build.py` erzeugt alles in dieser Reihenfolge. Jede Änderung geschieht **nur** in
`src/knowledge/`; generierte Dateien werden nie von Hand editiert, aber mitversioniert
(GitHub Pages veröffentlicht `docs/`).

## 1. Quellen beschaffen

Die Reihenfolge ist wichtig, weil der Netzwerkzugang aus der Agentenumgebung eingeschränkt ist.

1. **Gesetzestext**: `gesetze-im-internet.de` ist per Egress-Proxy gesperrt (auch per WebFetch).
   Funktioniert hat der Spiegel `github.com/bundestag/gesetze` über den Git-Proxy:
   ```bash
   GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse \
       https://github.com/bundestag/gesetze /home/user/bundestag/gesetze
   git -C /home/user/bundestag/gesetze sparse-checkout set p/patg g/gebrmg   # Slugs wie auf gesetze-im-internet.de
   ```
   Vorhandene Ordner prüfen mit `git ls-tree -d --name-only HEAD p/patg`. Im Spiegel (Stand 2022)
   nachgewiesen: `m/markeng`, `p/patg`, `p/patkostg`, `g/gebrmg`, `a/arbnerfg`, `g/geschmmg_2004`
   (DesignG), `p/patanwo`, `m/markenv_2004`. Nicht gefunden: IntPatÜG, ERVDPMAV, DPMAV; dafür
   WebSearch nach einer erreichbaren Quelle oder den Text vom Nutzer erbitten. Den Stand des
   Textes (Frontmatter „Zuletzt geändert durch“) immer in README und `meta` festhalten.
2. **IPWiki** (`ipwiki.de`): ebenfalls gesperrt. Ersatz: `WebSearch` mit `allowed_domains: ["ipwiki.de"]`
   je Themenblock; die Suche liefert Seitennamen (`patentrecht:...`) und Kurzinhalte. Diese als
   `source`-Knoten mit URL und Zusammenfassung erfassen (`src/knowledge/ipwiki.py`).
3. **Rechtsprechung**: Leitentscheidungen aus eigenem Wissen auflisten, dann **jedes Aktenzeichen
   und Datum per WebSearch verifizieren** (dejure.org-Treffer im Suchergebnis reichen). Beim
   Markenrecht mussten 18 von 95 Fundstellen korrigiert werden; ohne Verifikation ist die
   Fehlerquote zu hoch. Links werden nicht erfunden: Entscheidungen bekommen die stabile
   dejure-Vernetzungs-URL (`build_graph.case_url` aus Gericht, Datum, Aktenzeichen).
4. **EU-/Völkerrecht** (EPÜ, PCT, Richtlinien, Verordnungen): EUR-Lex und Spiegel sind gesperrt.
   Dann wie bei der MarkenRL vorgehen: artikelweise **Paraphrase je Absatz** aus eigenem Wissen,
   in jedem Knoten `paraphrase=True`, deutlicher Hinweis in Apps, Karten und README, Link auf das
   Originaldokument. Für Zitate muss der Nutzer den Wortlaut prüfen; das steht überall dabei.

## 2. Wissensmodell (was in `src/knowledge/` steht)

Alle Dateien sind reine Python-Datenlisten; IDs sind ASCII, snake_case, sprechend.

| Datei | Objekt | Pflichtfelder | Verknüpfungen |
|---|---|---|---|
| `concepts.py` | Begriff | `id, label, kategorie, definition, erlaeuterung` | `norms` (Zitate), `cases` (IDs), `ipwiki` (Seitennamen), `related` (Begriff-IDs) |
| `cases.py` | Entscheidung | `id, name, court, date, az, fundstelle, kern, tags` | `norms`, `concepts` |
| `schemata.py` | Prüfungsschema als Baum | `id, label, kategorie, beschreibung, norms, steps` | Schritt: `label, text, concepts, norms, cases, children, hinweis` |
| `distinctions.py` | Abgrenzungstabelle | `id, label, frage, kriterien, spalten, rows, merksatz, concepts` | `len(rows)==len(kriterien)`, `len(row)==len(spalten)` |
| `ipwiki.py` | Quelle | `page, title, summary` | – |
| `markenrl.py` | EU-Artikel | `nr, titel, kapitel, abschnitt, absaetze, umsetzung, concepts, cases, hinweis` | `umsetzung` = nationale Normzitate |
| `kurse/k*.py` | Kurs → Kapitel → Einheiten | s. Abschnitt 5 | `concepts, norms, cases, step` |
| `gesetze.py` | Verlinkungsregeln | `LAWS` (Slug + Zitierweise), `EU_LAWS`, `UNLINKED` | erzeugt auch das JavaScript |

**Definition** = ein bis drei Sätze, klausurtauglich, mit Normzitat. **Erläuterung** = Prüfungs-
hinweise, Fallgruppen, Abgrenzungen, Leitentscheidungen in Klammern. **Kern** einer Entscheidung =
der Rechtssatz in eigenen Worten, nicht der Sachverhalt.

Normzitate im Text folgen einem festen Muster, weil `gesetze.py` sie erkennt und verlinkt:
`§ 14 Abs. 2 Nr. 2` (Standardgesetz des Projekts, hier MarkenG), `§ 242 BGB`, `Art. 5 Abs. 3 GG`,
`Art. 10 MarkenRL`, Ketten `§§ 9 bis 13`, `§§ 3, 7, 8`, `§§ 23/24`. Für ein neues Gesetz:
Abkürzung und Slug in `LAWS` eintragen (Slug = Pfad auf gesetze-im-internet.de), das
Standardgesetz in `DEFAULT_LAW` setzen (bei mehreren Gesetzen s. Abschnitt 8).

## 3. Graph bauen (`src/build_graph.py`)

Knotentypen: `norm` (Paragraph mit Absätzen), `eunorm` (EU-Artikel), `concept`, `schema`, `step`,
`case`, `distinction`, `source`, `course`, `chapter`, `unit`.
Kanten: `defined_in`, `related_to`, `illustrated_by`, `documented_in`, `interprets`, `implements`,
`has_step` (mit `order`), `next_step`, `uses_concept`, `cites`, `applies`, `contrasts`,
`has_chapter`, `has_unit`, `trains`, `covers`.

Der Builder **bricht ab**, wenn ein Zitat auf eine unbekannte Norm, ein Begriff auf einen
unbekannten Fall oder eine Einheit auf einen unbekannten Prüfungspunkt zeigt. Das ist beabsichtigt:
Erst wenn `python3 src/build_graph.py` ohne Fehler läuft, ist die Wissensbasis konsistent.
Zusätzlich vor dem Build ein kleines Skript laufen lassen, das Querverweise prüft (Vorlage: die
Prüfblöcke, die während der Erstellung in Bash ausgeführt wurden; sie prüfen `related`, `cases`,
`ipwiki`, Tabellenmaße, MC-Indizes).

## 4. Prüfungsschemata und Abgrenzungen

- Ein Schema pro Anspruch oder Verfahren, Gutachtenreihenfolge, Tiefe zwei bis drei Ebenen.
  Jeder Schritt trägt die Begriffe, Normen und Entscheidungen, die man an dieser Stelle braucht;
  die App blendet sie dort inline ein.
- Abgrenzungen für die Paare, die Studierende erfahrungsgemäß verwechseln (beim Markenrecht:
  Kennzeichnungskraft/Unterscheidungskraft, Verfall/Nichtigkeit, § 23/§ 24, Prägetheorie/
  selbständig kennzeichnende Stellung). Fünf bis acht Kriterien, ein Merksatz.
- Bei EU-Grundlage eine Umsetzungstabelle (Artikel, nationale Norm, letzte Änderung).

## 5. Kurse im Fallformat (Jurafuchs-Prinzip)

Didaktik: kleinste Einheit = ein Prüfungspunkt; kurzer Lebenssachverhalt mit Namen; eine Frage
(Ja/Nein oder vier Optionen); sofortiges Feedback; Lösung im Gutachtenstil (Antwortsatz fett,
Definition, Subsumtion, Ergebnis, ein bis drei Absätze); ein Merksatz; Stufe 1 bis 3.
Kapitel beginnen mit `intro` (Systematik) oder `schema` (Prüfungsschema aus dem Graphen).

Einheitentypen (`kurse/_helpers.py`): `intro`, `schema`, `fall` (Ja/Nein), `mc` (Index der
richtigen Option). Jede Einheit verweist auf `concepts`, `norms`, `cases` und, wenn passend, den
Prüfungspunkt `step:<schema>.<n>.<m>`. IDs: `k07b-3` = Kurs 7, Kapitel b, Einheit 3.

Richtwerte aus dem Markenrecht: 10 bis 12 Kurse, je 2 bis 3 Kapitel, je 3 bis 8 Einheiten,
insgesamt 120 bis 150; etwa 70 % Ja/Nein-Fälle, 15 % MC, 15 % Intro/Schema. Fälle an
Leitentscheidungen anlehnen (der Fall im Kurs ist der Fall des BGH in drei Sätzen), dann trägt
die Verlinkung auf die Entscheidung den Lernstoff.

### 5a. Kurse aus Prüfungsklausuren

Für Kurs 12 wurden die NS-Klausuren der Patentanwaltsprüfung (kandidatentreff.de) heruntergeladen,
mit `pdftotext -layout` extrahiert und jede Klausur dem zugrunde liegenden Beschluss zugeordnet.
Was funktioniert hat: Volltextsuche der BPatG-Entscheidungsdatenbank per `curl`
(`Entscheidungen_Formular.html?templateQueryString=<Wort>&cl2LanguageEnts_Themenbereich=marke`)
nach Markenwörtern, Registernummern oder ungewöhnlichen Verfahrensbegriffen („Abholfach“, „Amtsliste“);
die PDFs unter `SharedDocs/Entscheidungen/DE/<Jahr>/…` lassen sich direkt laden. rewis.io und lexika.de
liefern Volltexte, wenn ein Aktenzeichen bekannt ist; dejure.org bestätigt Datum und Aktenzeichen.
Ein Treffer gilt erst als sicher, wenn Waren-/Dienstleistungsverzeichnis, Daten und Verfahrensgang mit
der Klausur übereinstimmen (Prüfer tauschen Namen und verschieben Jahre). Etwa die Hälfte der
Klausuren sind reine Lehrfälle ohne Beschluss; diese Einheiten stützen sich auf Lösungshinweise und
Standardrechtsprechung und sind im Kurs entsprechend gekennzeichnet. Zuordnungstabelle: `klausuren/README.md`.

Aus derselben Auswertung entstand die Navigator-Sektion „Klausur NS“ (`src/knowledge/klausur.py`,
View `vKlausur` in `src/templates/app.html`). Das Muster lässt sich auf andere Prüfungen übertragen:
Aufgabenstellungen aller Klausuren extrahieren (`grep -E "Aufgabe|Bearbeitervermerk|Nehmen Sie"`),
daraus die Aufgabentypen mit Häufigkeit ableiten, das Prüfungsraster als eigene Schemata in
`schemata.py` modellieren (dann landen sie automatisch im Graphen und in den Karteikarten) und den
Rest – Format, Zeitplan, Fristen, Gebühren, Tenorformeln, Fehlerliste – als reine Datenlisten in ein
eigenes Modul legen, das `build_html.py` als `__KLAUSUR__` einbettet. Gebührennummern und Beträge
immer am Gebührenverzeichnis (Anlage zu § 2 Abs. 1 PatKostG) prüfen, Zahlungstage an § 2 PatKostZV;
beides ändert sich und wird in Klausuren gezielt abgefragt. Achtung: In `norms`-Feldern dürfen nur
Normen des Standardgesetzes und MarkenRL-Artikel stehen, weil `build_graph` sonst abbricht;
Fremdgesetze gehören in den Fließtext, wo `gesetze.py` sie verlinkt.

## 6. Apps, Karten, Links

- Templates sind eigenständige HTML-Dateien ohne externe Ressourcen; Daten werden als JSON
  eingebettet (`__DATA__`, `__CARDS__`, `__KURSE__`, `__GRAPH__`), das Verlinkungs-JavaScript
  wird aus `gesetze.py` erzeugt (`__LAWJS__`). Für ein neues Gesetz sind an den Templates in der
  Regel keine Änderungen nötig, außer Ansichten für neue Knotentypen (Vorbild: `vRichtlinie`).
- Karteikarten entstehen automatisch aus dem Graphen (`build_flashcards.generate`): Definition,
  Umkehrkarte, Schema, Prüfungspunkt, Abgrenzung, Entscheidung (beide Richtungen), Norm, EU-Artikel.
- Fortschritt des Fallkurses liegt in zwei Cookies (`mgk_p`, `mgk_m`), Pfad = Seitenpfad,
  Fallback localStorage bei `file://`.

## 7. Qualitätssicherung vor jedem Push

1. `python3 build.py` ohne Fehler.
2. Playwright-Rauchtest über einen lokalen HTTP-Server (Cookies brauchen http):
   ```bash
   (cd docs && setsid nohup python3 -m http.server 8791 >/dev/null 2>&1 < /dev/null &)
   node test.js   # require('/opt/node22/lib/node_modules/playwright'); Chromium ist installiert
   ```
   Prüfen: keine `pageerror`, alle Einheiten durchklicken (Antwort geben, Chips vorhanden, keine
   leeren `.chips`), Gesetzeslinks mit gültigem `href`, Inline-Karten öffnen sich, Cookie gesetzt.
   Nicht `pkill -f http.server` verwenden; das Muster trifft die eigene Shell.
3. Stichprobe von fünf Lösungen fachlich gegenlesen (Antwortsatz, Norm, Entscheidung passen zusammen).
4. README-Zahlen (Knoten, Karten, Einheiten) aktualisieren.

## 8. Ein zweites Gesetz aufnehmen: empfohlene Verallgemeinerung

Der Code ist auf ein Gesetz ausgelegt (Norm-IDs `norm:§14`, `DEFAULT_LAW = "MarkenG"`,
`parse_markeng.py`). Vor dem zweiten Gesetz diese vier Schritte, in dieser Reihenfolge:

1. **Parser verallgemeinern**: `parse_markeng.py` → `parse_gesetz.py <slug> <abkuerzung>`,
   Ausgabe `data/<abk>.json`; Frontmatter-Metadaten wie bisher.
2. **IDs namensräumen**: `norm:<Abk>:§14`, `concept:<gebiet>:…` nur, wo Begriffe gesetzesspezifisch
   sind (viele sind es nicht: Verwechslungsgefahr bleibt eindeutig, „Neuheit“ gibt es in PatG,
   GebrMG und DesignG mit verschiedenen Definitionen → `concept:patg:neuheit`). `norm_id()` in
   `build_graph.py` liest das Gesetz aus dem Zitat (`§ 3 PatG`); Zitate ohne Gesetz gelten für das
   Standardgesetz des jeweiligen Wissenspakets.
3. **Wissenspakete pro Gebiet**: `src/knowledge/markenrecht/`, `src/knowledge/patentrecht/` mit
   identischer Dateistruktur; `build_graph.py` iteriert über alle Pakete in einen Graphen, damit
   gebietsübergreifende Kanten möglich sind (Beispiel: ArbnErfG → PatG § 6; PatKostG → PatG;
   GebrMG § 5 Abzweigung → PatG).
4. **Website**: Startseite mit Auswahl des Rechtsgebiets, Kurs-IDs mit Gebietspräfix (`pat-k03b-2`),
   Cookies nach Gebiet getrennt (`mgk_p_<gebiet>`).

Alternativ, wenn schnelle Ergebnisse wichtiger sind als ein gemeinsamer Graph: das Repo pro Gebiet
kopieren und nur `DEFAULT_LAW`, Parser-Slug und Wissenspaket austauschen. Das kostet später die
gebietsübergreifenden Kanten, die im gewerblichen Rechtsschutz aber wertvoll sind (Neuheit,
Priorität, Erschöpfung, Lizenz, Zwangsvollstreckung tauchen in allen Gesetzen auf).

## 9. Vorschlag für die Reihenfolge der nächsten Gebiete

| Gebiet | Umfang | Besonderheiten |
|---|---|---|
| PatG | groß (147 §§) | EPÜ und PCT als Paraphrase; Leitentscheidungen BGH X. ZS und BPatG; Schemata: Patentfähigkeit, Verletzung (Äquivalenz), Nichtigkeit, Einspruch, Zwangslizenz |
| GebrMG | klein | eng am PatG; Abzweigung, Schutzfähigkeit ohne Prüfung, Löschung |
| ArbnErfG | klein | Meldung, Inanspruchnahme, Vergütung; hängt an PatG § 6 |
| DesignG | mittel | Neuheit/Eigenart, Gesamteindruck, informierter Benutzer; GGV parallel |
| PatKostG, ERVDPMAV, DPMAV | Verfahren | keine Schemata im Gutachtensinn, eher Fristen- und Gebührentabellen; als Abgrenzungen und Normkarten erfassen |
| IntPatÜG | klein | Brücke zu EPÜ und PCT; Übersetzungen, Doppelschutz |

Empfehlung: erst PatG mit GebrMG und ArbnErfG zusammen (ein Wissenspaket „Patentrecht“), dann
DesignG, zuletzt die Verfahrens- und Kostengesetze als Ergänzung der bestehenden Pakete.

## 10. Was beim Markenrecht Zeit gekostet hat (zum Vermeiden)

- Aktenzeichen und Daten aus dem Gedächtnis sind zu etwa 20 % falsch. Immer verifizieren.
- Jeder Zugriff auf gesetze-im-internet, dejure, ipwiki, eur-lex ist gesperrt; nicht wiederholt
  versuchen, sondern Spiegel und WebSearch nutzen und Lücken transparent kennzeichnen.
- Playwright-Tests, die `.$('selector')` auf versteckte Elemente anwenden, laufen in Timeouts;
  vorher `isVisible()` prüfen.
- `[hidden]` in HTML braucht `[hidden]{display:none!important}`, sonst gewinnt eigenes `display:flex`.
- Knoten-IDs mit Sonderzeichen (`norm:§14`) konsequent überall gleich bilden; ein falsch gebauter
  Präfix hat in der Kursapp zeitweise alle Norm-Chips verschluckt, ohne Fehler zu werfen. Deshalb
  beim Rauchtest auf leere Chip-Zeilen prüfen.
- Bei Republish eines Artifacts verlangt der Dienst zuerst `action: read` der Live-Version.
