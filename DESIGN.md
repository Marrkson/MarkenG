# IPelico – Gestaltungsrichtlinie

Verbindlich für die Kursapp (`src/templates/kurs.html`, Assets in `src/templates/ipelico/`). Der
Lernnavigator (`src/templates/app.html`) übernimmt vorerst nur den Namen, nicht die Optik.
Abgestimmt am 10.09.2026 anhand der Konzeptseite (Glas-Probe, Logo-Runden, Icon-Stile).

## 1. Leitidee: Fallakte statt Spielwiese

Ein Lernwerkzeug, das aussieht wie ein gutes juristisches Arbeitsmittel: ruhig, strukturiert, in
Rhein-IP-Blau. Die Inhalte sind gegliedert wie bei AMBOSS (Akte, Wissensboxen, Chips), die
Oberflächen folgen dem Glas-Stil (weiche Lichtflecken im Hintergrund, halbtransparente Karten mit
großen Radien, Verlaufs-Hero, schwarze Pill-Buttons). Kein Maskottchen, keine Illustrationen, kein
Tiermotiv. Das Zeichen ist eine Kachel mit ausgespartem „IP“; die Icons sprechen dieselbe runde Formensprache.

## 2. Farbtokens

Brand-Blau ist das Blau des Rhein-IP-Logos (`#1482e3`). Auf Weiß hat es 3,9:1 Kontrast: nur für
Flächen, Linien, Balken und große Schrift (≥ 18,66 px fett). Text in Fließgröße nutzt `--brand-deep`.

### Hell (`:root`)

| Token | Wert | Verwendung |
|---|---|---|
| `--bg` | `#f3f5f9` | Seitengrund (kühles Grau) |
| `--paper` | `#ffffff` | deckende Flächen (Antworten, Innenboxen) |
| `--ink` | `#101828` | Text, schwarze Pill-Buttons |
| `--muted` | `#5b6474` | Sekundärtext (5,8:1) |
| `--line` | `#dde3ec` | Trennlinien |
| `--brand` | `#1482e3` | Flächen, Balken, aktive Icons |
| `--brand-deep` | `#0b5fb0` | Links, blauer Fließtext, Fokusring |
| `--brand-soft` | `#e6f1fc` | Tags, Merke-Box |
| `--brand-grad` | `linear-gradient(135deg,#3b9cf0 0%,#1482e3 55%,#0b5fb0 100%)` | Hero, Profilkarte, Feierkarte |
| `--ok` / `--ok-soft` | `#157f4a` / `#e3f4ea` | richtig |
| `--bad` / `--bad-soft` | `#c43d2f` / `#fce9e6` | falsch, löschen |
| `--tip` / `--tip-soft` | `#b7791f` / `#fdf3df` | Klausurtipp, fällig, Streak |
| `--def` / `--def-soft` | `#4b5563` / `#eef1f6` | Definition, Sachverhalt |
| `--concept` / `-soft` | `#9a3b25` / `#f7e8e3` | Begriff |
| `--norm` / `-soft` | `#0b5fb0` / `#e6f1fc` | Norm, Richtlinie |
| `--case` / `-soft` | `#6a4c93` / `#ece5f5` | Entscheidung |
| `--schema` / `-soft` | `#2f6b4f` / `#e2f0e8` | Schema, Prüfungspunkt |
| `--dist` / `-soft` | `#8a5a00` / `#fbf1d6` | Abgrenzung, Tabelle |

### Glas (hell)

```
--glass: rgba(255,255,255,.42)   Grundfarbe der Glaskarten
--g1: rgba(255,255,255,.58)  --g2: rgba(255,255,255,.22)    Verlauf auf der Karte
--g-top: rgba(255,255,255,.95)  --g-bot: rgba(255,255,255,.35)  --g-bot2: rgba(255,255,255,.7)  --g-side: rgba(255,255,255,.5)
--g-sheen: rgba(255,255,255,.6)   schräges Glanzlicht
--shadow: 0 1px 2px rgba(16,24,40,.04), 0 10px 30px rgba(16,24,40,.08)
--shadow-2: 0 2px 6px rgba(16,24,40,.06), 0 24px 60px rgba(16,24,40,.14)
Hintergrund: --bg plus vier Radialverläufe (Blau .55 oben links, Hellblau .5 rechts, Tiefblau .42 unten, Weiß .7 Mitte)
```

### Dunkel (`:root[data-theme="dark"]`, ein einziger Block)

| Token | Wert |
|---|---|
| `--bg` / `--paper` | `#0f1420` / `#171d2b` |
| `--ink` / `--muted` / `--line` | `#e9edf3` / `#98a2b3` / `#2a3346` |
| `--brand` / `--brand-deep` / `--brand-soft` | `#5aa9f0` / `#8ec5f7` / `#16283f` |
| `--brand-grad` | `linear-gradient(135deg,#2a7fd0,#0f4f8f)` |
| `--ok` / `-soft` | `#5fc48f` / `#173226` |
| `--bad` / `-soft` | `#ef8a7a` / `#3a221d` |
| `--tip` / `-soft` | `#e2b04a` / `#3a3120` |
| `--def` / `-soft` | `#b8c0cc` / `#222a3a` |
| `--concept` `--norm` `--case` `--schema` `--dist` | `#e0866f` `#8ec5f7` `#b89ee0` `#7fc4a0` `#e2b04a` (soft: `#3a2622` `#1b2b3d` `#2c2540` `#1f3329` `#3a3120`) |
| Glas | `--glass: rgba(30,38,56,.45)`, `--g1: rgba(40,50,72,.55)`, `--g2: rgba(24,30,46,.30)`, `--g-top: rgba(255,255,255,.28)`, `--g-bot: rgba(255,255,255,.06)`, `--g-bot2: rgba(255,255,255,.18)`, `--g-side: rgba(255,255,255,.12)`, `--g-sheen: rgba(255,255,255,.16)` |

Das JavaScript setzt `data-theme` immer (gespeicherter Wert `mgk_theme` oder Systemeinstellung, mit
Nachführung bei Systemwechsel), deshalb genügt ein Dark-Block.

### Kursfarben

`farbe` in `src/knowledge/kurse/k*.py` ist dekorativ (Tönung der Kursnummer-Kachel, Tag-Pill). Alles
Interaktive ist Brand-Blau oder Ink. Status nie allein über Farbe (Icon + Text).

## 3. Glas, aber diszipliniert

Die Klasse `.glass` liefert: Verlauf `--g1`→`--g2`, `backdrop-filter: blur(30px) saturate(190%)
brightness(1.05)`, maskierter Verlaufsrahmen (1 px, oben hell, unten schwach), inneres Lichtband
(`inset 0 1px 0 --g-top`), schräges Glanzlicht (`::after`, 112°), Schatten `--shadow` bzw. `--shadow-2`.
Der Weichzeichner sitzt nur auf Hero, Topbar, Tableiste, Hinweiskarte und Karten der ersten Ebene.
Listenzeilen und Innenboxen sind deckend (`--paper`, `--def-soft`). Text steht nie direkt auf dem
Verlauf. Ohne `backdrop-filter` sehen Browser deckende Karten; nichts bricht.

## 4. Radien und Abstände

| Token | Wert | Verwendung |
|---|---|---|
| `--r-xl` | 30px | Hero, Profilkarte, Feierkarte, Phone-Rahmen |
| `--r-lg` | 22px | Glaskarten |
| `--r-md` | 14px | Antworten, Innenboxen, Kursnummer-Kacheln |
| `--r-sm` | 10px | kleine Kacheln |
| `--r-pill` | 999px | Buttons, Tags, Chips, Tableiste |

Seite: eine Spalte bis 720 px, 16 px Rand, unten `104px + env(safe-area-inset-bottom)` Platz für die
Tableiste. Tap-Ziele ≥ 44 px (Tabs 52 px, runde Knöpfe 44/52 px, Schnellzugriff-Pillen 48 px), Abstand
zwischen Tap-Zielen ≥ 8 px. Horizontale Reihen (`.hscroll`, `.quick`) laufen bis an den Rand
(`margin: 0 -16px`), Scroll-Snap, versteckte Scrollleiste, nächste Karte ragt sichtbar an (76 % Breite).
Ab 760 px: Hero mit allen vier Radien, Tableiste als schwebende Pille, Reihen ohne Randüberlauf.

## 5. Typografie

IBM Plex Sans (400, 600, 700) und IBM Plex Mono (500), als woff2 in die HTML-Datei eingebettet
(`__FONTS__`, Dateien in `src/templates/ipelico/fonts/`), Rückfall Systemschrift. Plex Mono für
Aktenzeichen, Zähler, Einheiten-IDs und Kursnummern.

Skala 12 (Labels, Versalien, 0,08 em), 13 (Meta), 14 (Chips, Untertitel), 15 (Fließtext Karten),
16 (Fließtext, 1.55), 17 (Sachverhalt), 19 (Frage, 700), 20 (h2, 600), 28 (h1, 700, 1.15,
`text-wrap:balance`), 44 (Score). Gewichte nur 400, 600, 700. Zahlen tabellarisch.

## 6. Zeichen

Datei `src/templates/ipelico/logo/ipelico-mark.svg` (100×100, gewählt am 10.09.2026 als Konzept 04
„IP-Kachel“, das Pelikan-Zeichen ist verworfen): eine Kachel 84×84 an 8/8, Radius 24, darin „IP“ als
Aussparung (Maske, der Grund scheint durch): I und P-Stamm als Pillen 11×46 an x 27 und 46 (y 27), Bauch
als Bogen r 11 mit runden Enden, Strich 11. Einfarbig, keine Transparenz, keine Verläufe. Farbe über
`currentColor`. Badge `ipelico-badge.svg` (App-Icon, Favicon): blaue Kachel, Radius 24, darin das Zeichen in
Weiß auf 72 % (Kachel in der Kachel); PNGs und `ref/logo-mark.png` rendert `python3 tools/render_icons.py`.
Wortmarke: Zeichen 1,3 em hoch + „IPelico“ in Plex Sans 700. Vor Veröffentlichung: TMview-Bildrecherche (Wiener Klassifikation 26.4, 27.5) und
Namensprüfung gegen „Pelico“ in den Klassen 9, 41 und 42.

## 7. Icons

Stil T1: dicke Linie wie das Zeichen (Strich ≈ 1/10 der Höhe), runde Enden, Kreise, Striche, Bögen,
keine Füllungen außer Punkten, einfarbig über `currentColor` (Tabbar aktiv Blau, inaktiv `--muted`,
in Boxen die Boxfarbe). Tableiste in der Sprache des Zeichens: `tab-kurse` (das Zeichen als Kontur mit IP),
`tab-wdh` (Kreispfeil um eine Kachel), `tab-profil` (Büste in einer Kachel), `tab-konzept` (Doktorhut).
`feier` zeigt noch zwei überlappende Kacheln aus der Vorrunde; alle übrigen sind reine Motive. Erzeugung: `tools/gen_assets.py`
(Gemini → potrace → `icons/ic-*.svg`, viewBox 24). Symbol-IDs `ic-<name>`, im Template `ic('name')`.
Größen: 24 (Tabbar, Buttons), 20 (Listen, Boxen), 16 (Chips, Pills).

## 8. Komponenten

| Klasse | Beschreibung |
|---|---|
| `.topbar` | sticky, ohne Grund; runder Zurück-Knopf (44 px) + Titel 22/700, rechts Pills oder `.seg.ic-seg` (Liste/Raster). Beim Scrollen (`.scrolled`) Hintergrund `--bg` 82 % + Blur. Auf der Startseite ausgeblendet; dort trägt der Hero die Wortmarke |
| `.hero` | Startseite: vollflächig bis unter die Statusleiste (`env(safe-area-inset-top)`), nur untere Radien r-xl, `--brand-grad` + zwei Lichtflecken, zentrierter Gruß (17) und Titel (32/700), darunter `.status`-Pille (Glas auf Verlauf, Zähler-Badge, Chevron; führt zu Wiederholung oder nächster Einheit) |
| `.next` | überlappende Karte unter dem Hero (`margin-top:-52px`, `--paper`, `--shadow-2`): Eyebrow „Weiter mit Kurs“, Titel, Meta mit Icon, Wasserzeichen-Icon; Fußzeile mit Prozentwert und schwarzer Pill „Weiter lernen“ |
| `.quick` / `.qa` | Schnellzugriff: zweizeiliges, horizontal scrollendes Raster aus weißen Pillen (Icon Brand + Label, optional Zähler `.n`) |
| `.hscroll` / `.kcard` | Kurs-Karussell: Hochkant-Karten 76 % Breite in Kursfarbe (`.cthumb`-Verlauf), Pill oben, Wasserzeichen-Icon, Titel/Meta/Balken unten auf Abdunklung |
| `.lcard` | Listenkarte (Glas): Kurskachel 96 px links, Kategorie-Pill, Titel 17/600, Meta mit Icon, Balken; im Raster (`.lgrid`) zweispaltig mit Kachel oben. Ansicht wird in `mgk_view` gemerkt |
| `.detail` | Kursdetail (Glas): große Kurskachel 210 px mit Nummer-Pill, Status-Tag, h1, Beschreibung, `.mrow`-Metazeilen mit Icon, Balken, `.actrow`: schwarze Pill (flex 1) + runde Icon-Knöpfe 52 px |
| `.cthumb` | Kurskachel: Verlauf aus `--c` (heller → Kursfarbe → dunkler), Glanzlicht, weißes Icon mit Schatten |
| `.last` | „Zuletzt gelernt“: Avatar-Kreis mit Typ-Icon, Titel, Tags, darunter `.chk`-Zeilen (Haken/Kreuz/Uhr) |
| `.glass` | Glaskarte (siehe 3) |
| `.box` | Wissensbox: 4-px-Balken links, getönter Grund, Label in Versalien mit Icon; Typen `merke`, `def`, `tip`, `ok`, `bad`, `sv` (Sachverhalt) |
| `.btn.primary` | schwarze Pill (`--ink` auf `--paper`), im Dunkelmodus invertiert; `.btn.light` weiße Pill auf Verlauf; `.btn.ghost` transparent mit Rahmen |
| `.tag` | Pastell-Pill 13/600 mit 16-px-Icon; Varianten `brand ok bad tip` |
| `.chip` | Kategorie-Pill mit 16-px-Icon, öffnet Inline-Karte; `.open` invertiert |
| `.row` | Listenzeile: Nummern-Kachel (Plex Mono) oder Typ-Icon, Titel, Untertitel, Balken, Chevron |
| `.ans` | Antwortkarte: deckend, 2-px-Rahmen, Zustände `sel right wrong` |
| `.tabwrap` / `.tabbar` / `.fab` | wie iOS 26: schwebende Glas-Kapsel mit 4 Tabs (Icon 26 + Label 11, aktiv Icon Brand + Label Ink, `aria-current`) und daneben eine eigene Glas-Kugel (64 px) für Suchen/Nachschlagen; Abstand unten `max(12px, env(safe-area-inset-bottom))` |
| `.notice` | kompakte Glaskarte (13 px, Knopf „OK“ 44 px) direkt über der Tableiste |
| `.sbox` | Suchfeld als Glas-Pille, sticky unter der Kopfzeile, Lupe links, Löschen-Kreis rechts; Eingabe 17 px, `enterkeyhint=search`, Ergebnisse nach 110 ms |
| `.grp` / `.hit` | Treffergruppe (Versalien-Label, Icon, Zähler, „alle zeigen“) und Trefferzeile: Typ-Kreis in Typfarbe, Titel mit `<mark>`, zweizeiliger Auszug, roter Punkt bei Lernradar |
| `.cats` / `.cat` | Stöbern-Kacheln (2 Spalten, Glas): Icon, Kategorie, Zähler in Plex Mono |
| `.toc` | Abschnittsleiste der Lernkarte: sticky, horizontal scrollend, Glas-Pillen mit 16-px-Icon, springt weich zu `.sec` |
| `.sec` | Lernkarten-Abschnitt in fester Reihenfolge: Definition/Kern, Norm, Prüfung, Rechtsprechung, Abgrenzung, Verwandt, Fälle dazu; leere Abschnitte entfallen, die Reihenfolge nie |
| Lernradar | `.chip.weak` (2-px-Unterstrich `--bad` + roter Punkt), `.tree .node.weak` (roter Unterstrich), `.row .rd` / `.hit .rd` (roter Punkt), `.box.bad` „Lernradar“ am Kopf der Lernkarte; bleibt bis zur nächsten richtigen Antwort |
| `.inline` | Inline-Karte (Begriff, Norm, Entscheidung, Schema) mit Linksbalken in Typfarbe |

## 8a. Mobile Struktur (Vorlage: Versicherungs-App, abgestimmt 10.09.2026)

Reihenfolge Startseite: Hero → überlappende Weiter-Karte → Schnellzugriff → Kurs-Karussell mit „Alle
anzeigen“ → Zuletzt gelernt → Kennzahlen. Route `#/kurse` zeigt alle Kurse als Liste oder Raster mit
Umschalter in der Kopfzeile. Kursdetail wie eine Ortskarte: Bild, Kategorie, Titel, Metazeilen,
Aktionszeile. Angewandte Regeln: Primäraktionen in der Daumenzone (Fußzeile der Karte, Aktionszeile,
Tableiste), 3–5 Tabs mit Label, `touch-action: manipulation` und ohne Tap-Highlight, sichtbare
`:active`-Skalierung, horizontale Reihen nur mit angeschnittener Folgekarte als Hinweis, sticky
Kopfzeile ohne weiteren Inhalt, keine `100vh`-Höhen.

## 8b. Nachschlagen (Vorbild AMBOSS, 10.09.2026)

Eine Wissensbasis, zwei Nutzungsweisen: Kurse lernen, Lernkarten schlagen nach. Route `#/suche`
(Such-Kugel in der Tableiste, Taste `/`): leer zeigt sie zuletzt Gesuchtes, den Lernradar-Hinweis und
Stöbern-Kacheln je Knotentyp; ab zwei Zeichen gruppierte Treffer (Begriffe, Prüfungspunkte, Schemata,
Gesetz, Richtlinien, Entscheidungen, Abgrenzungen, Fälle) mit Hervorhebung, maximal fünf je Gruppe plus
„alle zeigen“, Null-Treffer mit Vorschlägen. Route `#/karte/<knoten>`: Lernkarte mit immer gleichem
Aufbau (siehe `.sec`), Zurück per Verlauf. Jede Inline-Karte verlinkt auf ihre Lernkarte; jede Lernkarte
listet die Fälle, die den Punkt trainieren. Lernradar: falsch beantwortete Fälle markieren ihre Begriffe,
Prüfungspunkte, Entscheidungen und Abgrenzungen rot in Chips, Schemata, Lernkarten, Suche und im Tab
Wiederholen; Schalter im Profil (`mgk_radar`). Glas nur auf der Navigationsebene (Kopfzeile, Suchfeld,
Abschnittsleiste, Tableiste) und Karten erster Ebene; Listen und Boxen bleiben deckend.

## 9. Bewegung

`--dur:160ms`, `--ease:cubic-bezier(.2,.7,.2,1)`. Buttons `:active{transform:scale(.98)}`.
Ergebnis-Panel: Einblenden und 8 px Anheben in 220 ms. Balken 400 ms. Unter
`prefers-reduced-motion` alles aus. Kein Blur-Übergang (teuer).

## 10. Barrierefreiheit

Fokusring `3px solid var(--brand-deep)`, Offset 2 px. Klickbare Karten sind `<a href>` oder
`<button>`. `[hidden]{display:none!important}` bleibt. Kontraste: siehe 2. `color-scheme` und
`<meta name="theme-color">` folgen dem Theme (hell `#f3f5f9`, dunkel `#0f1420`).
