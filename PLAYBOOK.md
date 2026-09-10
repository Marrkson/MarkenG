# Playbook: Wissensgraph und Lernkurse für ein Rechtsgebiet erstellen

Dieses Dokument beschreibt, wie der Markenrecht-Graph, die Karteikarten, der Lernnavigator und der
Fallkurs IPelico entstanden sind, damit derselbe Prozess für weitere Gesetze (PatG, GebrMG, DesignG,
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
| IPelico (Fallkurs, Website-Startseite) | `docs/index.html` | `src/build_kurs.py` + `src/templates/kurs.html` + `src/templates/ipelico/` |
| Gestaltungsrichtlinie | `DESIGN.md` | Hand |
| Icons, Zeichen, Schriften | `src/templates/ipelico/` | `tools/gen_assets.py` (Gemini + potrace), Hand |
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
5. **Vom Rechner des Nutzers aus** (Claude Code lokal statt Sandbox) sind beide Sperren weg, nur die
   Adressen müssen stimmen:
   - EUR-Lex: `legal-content/…` und `LexUriServ/…` liefern eine leere HTML-Hülle (HTTP 202). Der
     **Cellar** liefert das Dokument per Content-Negotiation:
     `curl -H "Accept: application/pdf" -H "Accept-Language: deu" -o rl.pdf "https://publications.europa.eu/resource/celex/32004L0048R(01)"`
     (CELEX-Nummer mit `R(01)` für die Berichtigung; `pdftotext` daraus). So entstand
     `src/knowledge/durchsetzungsrl.py` im amtlichen Wortlaut (`paraphrase=False`).
   - gesetze-im-internet.de: `https://www.gesetze-im-internet.de/<slug>/xml.zip` enthält das Gesetz
     als XML (`<norm>` mit `<enbez>§ 140b</enbez>`, `<titel>`, `<textdaten>`); damit lassen sich
     Paragraphen anderer Gesetze für Umsetzungstabellen prüfen, ohne den Spiegel zu klonen.
   - dejure.org, curia, rewis: per WebSearch erreichbar; EuGH-Aktenzeichen sind dort verlässlich.

## 2. Wissensmodell (was in `src/knowledge/` steht)

Alle Dateien sind reine Python-Datenlisten; IDs sind ASCII, snake_case, sprechend.

| Datei | Objekt | Pflichtfelder | Verknüpfungen |
|---|---|---|---|
| `concepts.py` | Begriff | `id, label, kategorie, definition, erlaeuterung` | `norms` (Zitate), `cases` (IDs), `ipwiki` (Seitennamen), `related` (Begriff-IDs) |
| `cases.py` | Entscheidung | `id, name, court, date, az, fundstelle, kern, tags` | `norms`, `concepts` |
| `schemata.py` | Prüfungsschema als Baum | `id, label, kategorie, beschreibung, norms, steps` | Schritt: `label, text, concepts, norms, cases, children, hinweis` |
| `distinctions.py` | Abgrenzungstabelle | `id, label, frage, kriterien, spalten, rows, merksatz, concepts` | `len(rows)==len(kriterien)`, `len(row)==len(spalten)` |
| `ipwiki.py` | Quelle | `page, title, summary` | – |
| `markenrl.py`, `durchsetzungsrl.py` | EU-Artikel | `nr, titel, kapitel, abschnitt, absaetze, umsetzung, concepts, cases, hinweis` | `umsetzung` = MarkenG-Zitate (Graphkanten); `umsetzung_weitere` = dict Gesetz → Zitate der übrigen Gesetze (nur Text); Richtlinien werden in `build_graph.RICHTLINIEN` registriert (Kürzel, `paraphrase`-Flag), das Zitat `Art. 8 Abs. 3 lit. e DurchsetzungsRL` wird daraus aufgelöst |
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
- Bei EU-Grundlage eine Umsetzungstabelle (Artikel, nationale Norm, letzte Änderung). Betrifft die
  Richtlinie mehrere Gesetze (Durchsetzungs-RL), eine Spalte je Gesetz; Zellen ohne Gesetzesangabe mit
  `gesetze.qualify(text, law)` qualifizieren, sonst verlinkt `linkify` sie auf das Standardgesetz.
  Zitatketten so schreiben, dass der Erkenner sie trennt: `§§ 935 ff. ZPO, § 937 Abs. 2 ZPO`, nicht
  `§§ 935 ff., 937 Abs. 2 ZPO`; Gesetz hinter das Zitat, nicht davor in Klammern.

## 5. Kurse im Fallformat

Ebene über den Kursen: Rechtsgebiete in `kurse/gebiete.py` (MarkenG, EU-Recht, Verfahren; geplant PatG, EPÜ,
UPC, DesignG, ArbnErfG, BGB, UWG). Jeder Kurs trägt `gebiet=<id>`, der Import bricht bei unbekannter ID ab. Die App
gruppiert die Kursliste danach und zeigt geplante Gebiete als „In Vorbereitung“. Neues Gebiet: Eintrag in
`gebiete.py`, dann Kurse mit dieser ID anlegen; `geplant=True` entfernen, sobald der erste Kurs steht.

Didaktik: kleinste Einheit = ein Prüfungspunkt; kurzer Lebenssachverhalt mit Namen; eine Frage
(Ja/Nein oder vier Optionen); sofortiges Feedback; Lösung im Gutachtenstil (Antwortsatz fett,
Definition, Subsumtion, Ergebnis, ein bis drei Absätze); ein Merksatz; Stufe 1 bis 3.
Kapitel beginnen mit `intro` (Systematik) oder `schema` (Prüfungsschema aus dem Graphen).

Einheitentypen (`kurse/_helpers.py`): `intro`, `schema`, `fall` (Ja/Nein), `mc` (Index der
richtigen Option). Jede Einheit verweist auf `concepts`, `norms`, `cases` und, wenn passend, den
Prüfungspunkt `step:<schema>.<n>.<m>`; `distinctions` hängt Abgrenzungstabellen an, die bei
`intro`-Einheiten direkt unter dem Text erscheinen (so steht die Umsetzungstabelle im Kurs 14).
IDs: `k07b-3` = Kurs 7, Kapitel b, Einheit 3.

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
  wird aus `gesetze.py` erzeugt (`__LAWJS__`). IPelico bettet zusätzlich `__SPRITE__` (alle `icons/ic-*.svg` und
  `logo/*.svg` als `<symbol>`), `__FONTS__` (woff2 als data-URI) und `__FAVICON__` ein; `build_kurs.py` bricht ab,
  wenn ein im Template benötigtes Icon fehlt (`REQUIRED_ICONS`).
- App-Icons: `build_kurs.py` kopiert `logo/*.png` und `favicon.ico` (Apple-Touch-Icon 180, 192, 512, maskable 512,
  Favicons 16/32, ICO 16/32/48) und schreibt `docs/manifest.webmanifest`; der Navigator verweist auf dieselben Dateien. Die PNGs werden aus `ipelico-badge.svg` gerendert (`python3 tools/render_icons.py`);
  bei neuem Zeichen neu rendern.
- Gestaltung: `DESIGN.md` ist verbindlich. Neue Icons in `tools/gen_assets.py` eintragen, `gen` und `trace`
  laufen lassen, Ergebnis auf dem Kontaktblatt prüfen (16 px muss lesbar bleiben). Für ein neues Gesetz sind an den Templates in der
  Regel keine Änderungen nötig, außer Ansichten für neue Knotentypen (Vorbild: `vRichtlinie`).
- Karteikarten entstehen automatisch aus dem Graphen (`build_flashcards.generate`): Definition,
  Umkehrkarte, Schema, Prüfungspunkt, Abgrenzung, Entscheidung (beide Richtungen), Norm, EU-Artikel.
- Fortschritt des Fallkurses liegt in zwei Cookies (`mgk_p`, `mgk_m`), Pfad = Seitenpfad,
  Fallback localStorage bei `file://`.

## 7. Qualitätssicherung vor jedem Push

1. `python3 build.py` ohne Fehler.
2. Rauchtest über einen lokalen HTTP-Server (Cookies brauchen http), Python-Playwright ist installiert:
   ```bash
   (cd docs && python3 -m http.server 8791 >/dev/null 2>&1 &)
   python3 tools/smoke_test.py
   ```
   Prüft: keine `pageerror`, alle `<use>`-Symbole vorhanden, keine leeren `.chips`, Gesetzeslinks mit
   `href`, Antwortfluss inkl. Tastatur, Cookie-Altformat, Theme-Umschaltung.
   Nicht `pkill -f http.server` verwenden; das Muster trifft die eigene Shell.
   Sichtprüfung: Screenshots Home, Kurs, Einheit vor und nach Antwort, Ende, Profil in hell und dunkel
   (390×844 und 1280×900).
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

## 11. Zweites Wissenspaket: Einheitliches Patentgericht (EPGÜ, VerfO, EPG-Rechtsprechung)

So wurde das UPC-Paket im September 2026 aufgenommen; das Muster gilt für weitere Pakete (EPÜ, PatG).

**Quellen.** Die Entscheidungen des EPG liegen in der Postgres-Datenbank `patentcost` (RheinIP, Tabelle
`UpcDecision`: 1.886 Entscheidungen und Anordnungen seit 1.6.2023 mit Volltext, Kammer, Verfahrensart, Parteien,
Patent, URL). `tools/fetch_upc.py` zieht daraus `data/upc_decisions.json` (Metadaten, Leitsätze und Schlagworte aus
den Abschnitten LEITSATZ/HEADNOTES und SCHLAGWORTE/KEYWORDS der Entscheidungen, Zählung der zitierten EPGÜ-Artikel
und VerfO-Regeln im Volltext; keine Volltexte). Zugang: `POSTGRES_LOGIN` aus `~/github/RheinIP/.env`, nur lesend.
Die Datenbank enthält den EPGÜ-Text nur unvollständig (`EPOLegaltext`, type `upc-a`: Art. 1 bis 23, englisch) und
die VerfO nur als englische PDF-Seiten von 2022 (`UPCLegaltext`). Deshalb holt das Skript den amtlichen deutschen
und englischen Wortlaut des EPGÜ artikelweise von `epo.org/de/legal/up-upc/2022/upca_<n>.html` und die konsolidierte
deutsche VerfO (Stand 1.1.2026) als PDF von unifiedpatentcourt.org (`pdftotext -layout`, Regeln, Absätze, Präambel
und „Bezug zum Übereinkommen“ werden geparst). Zwischenstände liegen in `~/.cache/ipelico/upc/`;
`--no-net`/`--no-db` bauen aus dem Cache. Alle drei JSON-Dateien sind versioniert, `build.py` braucht weder Netz
noch Datenbank.

**Modell.** `src/knowledge/upc/` hat dieselbe Struktur wie das Markenrecht (`concepts`, `cases`, `schemata`,
`distinctions`), IDs mit Präfix `upc_`/`d_upc_`; `upca.py` und `rop.py` laden die Normtexte und tragen Hinweise,
`entscheidungen.py` liefert den Korpus. EPGÜ und VerfO sind als weitere `eunorm`-Familien in
`build_graph.RICHTLINIEN` registriert (`key=upca`, `kurz=EPGÜ`, Zitat `Art.`; `key=rop`, `kurz=VerfO`, Zitat `R.`).
Zitierformen in `norms`-Feldern: `Art. 33 Abs. 1 EPGÜ`, `R. 19.1 VerfO`, `R. 262A VerfO` (Aliase `UPCA`, `RoP`;
Kürzel und Schlüssel stehen in `gesetze.EU_NORM_KEYS`, die Regel-Zitatköpfe in `gesetze.RULE_HEADS`; der
Zitaterkenner verlinkt `Art. … EPGÜ` auf EUR-Lex und `R. … VerfO` auf das VerfO-PDF). Entscheidungen tragen
`url` (unifiedpatentcourt.org) statt der dejure-URL; Gerichte heißen `EPG-BerG`, `EPG LK <Ort>`, `EPG ZK <Ort>`.

**Kanten zum Markenrecht.** Die Durchsetzungsrichtlinie verbindet beide Pakete: `upca.ENTSPRICHT` erzeugt Kanten
`eunorm:upca:<n> -[entspricht]-> eunorm:durchsetzungsrl:<m>` (Art. 59↔6, 60↔7, 67↔8, 62↔9, 64↔10, 63↔11, 68↔13,
69↔14, 80↔15), die Tabelle `d_upc_entsprechung_durchsetzungsrl` zeigt daneben MarkenG und PatG. Jede VerfO-Regel
zeigt mit `konkretisiert` auf die Artikel aus ihrem „Bezug zum Übereinkommen“. Beide Kanten erscheinen auf den
Lernkarten (IPelico) und Inline-Karten (Navigator).

**Rechtsprechungskorpus.** Die 1.886 Entscheidungen sind keine Graphknoten (das würde die Apps verdoppeln), sondern
liegen als `docs/upc_entscheidungen.json` (1 MB) neben der App und werden in IPelico nachgeladen: Ansicht `#/epg`
(Suche, Kammer, Verfahrensart, nur mit Leitsatz), `#/epg/norm/<knoten-id>` je Artikel/Regel, und als Abschnitt
„EPG-Rechtsprechung“ auf jeder EPGÜ-/VerfO-Lernkarte. Jeder Norm-Knoten trägt `zitiert` (Zahl der Entscheidungen).
Kuratierte Leitentscheidungen (65, überwiegend Berufungsgericht) sind zusätzlich `case`-Knoten mit deutschem `kern`.

**Aktualisieren.** Neue Entscheidungen: `python3 tools/fetch_upc.py --no-net` (nur Datenbank), dann `build.py`.
Neue VerfO-Fassung: Cache-PDF löschen und ohne `--no-net` laufen lassen; das Deckblatt landet in `meta.stand`.
Karteikarten entstehen für EPGÜ/VerfO nur für Vorschriften mit Begriff, Schema, Entscheidung oder Hinweis.
