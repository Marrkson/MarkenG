# IPelico – Gestaltungsrichtlinie

Verbindlich für die Kursapp (`src/templates/kurs.html`, Assets in `src/templates/ipelico/`). Der
Lernnavigator (`src/templates/app.html`) übernimmt vorerst nur den Namen, nicht die Optik.
Abgestimmt am 10.09.2026 anhand der Konzeptseite (Glas-Probe, Logo-Runden, Icon-Stile).

## 1. Leitidee: Fallakte statt Spielwiese

Ein Lernwerkzeug, das aussieht wie ein gutes juristisches Arbeitsmittel: ruhig, strukturiert, in
Rhein-IP-Blau. Die Inhalte sind gegliedert wie bei AMBOSS (Akte, Wissensboxen, Chips), die
Oberflächen folgen dem Glas-Stil (weiche Lichtflecken im Hintergrund, halbtransparente Karten mit
großen Radien, Verlaufs-Hero, schwarze Pill-Buttons). Kein Maskottchen, keine Illustrationen. Das
Zeichen ist ein abstrahierter Pelikankopf; die Icons sprechen dieselbe Formensprache.

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

Seite: eine Spalte bis 720 px, 16 px Rand, 96 px Platz unten für die Tableiste. Tap-Ziele ≥ 44 px.

## 5. Typografie

IBM Plex Sans (400, 600, 700) und IBM Plex Mono (500), als woff2 in die HTML-Datei eingebettet
(`__FONTS__`, Dateien in `src/templates/ipelico/fonts/`), Rückfall Systemschrift. Plex Mono für
Aktenzeichen, Zähler, Einheiten-IDs und Kursnummern.

Skala 12 (Labels, Versalien, 0,08 em), 13 (Meta), 14 (Chips, Untertitel), 15 (Fließtext Karten),
16 (Fließtext, 1.55), 17 (Sachverhalt), 19 (Frage, 700), 20 (h2, 600), 28 (h1, 700, 1.15,
`text-wrap:balance`), 44 (Score). Gewichte nur 400, 600, 700. Zahlen tabellarisch.

## 6. Zeichen

Datei `src/templates/ipelico/logo/ipelico-mark.svg` (100×100): Ring (Kopf, r 17), gerader Strich
(Schnabel), Bogen (Beutel), Strich 8/100, runde Enden, um 30° nach unten gedreht, damit das Zeichen
quadratisch steht. Farbe über `currentColor`. Badge `ipelico-badge.svg`: blaue Kachel, Radius 24,
Zeichen in Weiß (Favicon, App-Icon). Wortmarke: Zeichen 1,3 em hoch + „IPelico“ in Plex Sans 700.
Kein Auge, keine Füllung, keine Verläufe im Zeichen. Schutzraum: halbe Ringbreite rundum.

## 7. Icons

Stil T1: dicke Linie wie das Zeichen (Strich ≈ 1/10 der Höhe), runde Enden, Kreise, Striche, Bögen,
keine Füllungen außer Punkten, einfarbig über `currentColor` (Tabbar aktiv Blau, inaktiv `--muted`,
in Boxen die Boxfarbe). Hybrid: die fünf Icons `tab-kurse`, `tab-wdh`, `tab-profil`, `tab-konzept`,
`feier` enthalten den Pelikan; alle übrigen sind reine Motive. Erzeugung: `tools/gen_assets.py`
(Gemini → potrace → `icons/ic-*.svg`, viewBox 24). Symbol-IDs `ic-<name>`, im Template `ic('name')`.
Größen: 24 (Tabbar, Buttons), 20 (Listen, Boxen), 16 (Chips, Pills).

## 8. Komponenten

| Klasse | Beschreibung |
|---|---|
| `.topbar` | sticky Glas, Zeichen + Wortmarke oder Zurück + Titel, rechts Streak- und XP-Pills |
| `.hero` | `--brand-grad`, r-xl, Weiß-Text, weißer Button; Fortschrittsring |
| `.glass` | Glaskarte (siehe 3) |
| `.box` | Wissensbox: 4-px-Balken links, getönter Grund, Label in Versalien mit Icon; Typen `merke`, `def`, `tip`, `ok`, `bad`, `sv` (Sachverhalt) |
| `.btn.primary` | schwarze Pill (`--ink` auf `--paper`), im Dunkelmodus invertiert; `.btn.light` weiße Pill auf Verlauf; `.btn.ghost` transparent mit Rahmen |
| `.tag` | Pastell-Pill 13/600 mit 16-px-Icon; Varianten `brand ok bad tip` |
| `.chip` | Kategorie-Pill mit 16-px-Icon, öffnet Inline-Karte; `.open` invertiert |
| `.row` | Listenzeile: Nummern-Kachel (Plex Mono) oder Typ-Icon, Titel, Untertitel, Balken, Chevron |
| `.ans` | Antwortkarte: deckend, 2-px-Rahmen, Zustände `sel right wrong` |
| `.tabbar` | schwebende Glas-Pille, 4 Tabs mit Pelikan-Icons |
| `.notice` | schwebende Glaskarte über der Tableiste |
| `.inline` | Inline-Karte (Begriff, Norm, Entscheidung, Schema) mit Linksbalken in Typfarbe |

## 9. Bewegung

`--dur:160ms`, `--ease:cubic-bezier(.2,.7,.2,1)`. Buttons `:active{transform:scale(.98)}`.
Ergebnis-Panel: Einblenden und 8 px Anheben in 220 ms. Balken 400 ms. Unter
`prefers-reduced-motion` alles aus. Kein Blur-Übergang (teuer).

## 10. Barrierefreiheit

Fokusring `3px solid var(--brand-deep)`, Offset 2 px. Klickbare Karten sind `<a href>` oder
`<button>`. `[hidden]{display:none!important}` bleibt. Kontraste: siehe 2. `color-scheme` und
`<meta name="theme-color">` folgen dem Theme (hell `#f3f5f9`, dunkel `#0f1420`).
