# Hinweise für Agenten

- Inhalte werden ausschließlich in `src/knowledge/` gepflegt; `docs/`, `graph/`, `flashcards/` und
  `data/*.json` sind generiert (`python3 build.py`) und werden mitversioniert.
- Vorgehen für neue Rechtsgebiete, Datenmodell, Konventionen und Prüfschritte: `PLAYBOOK.md`.
- Gesetzeszitate im Text so schreiben, dass `src/knowledge/gesetze.py` sie erkennt
  (`§ 14 Abs. 2 Nr. 2`, `§ 242 BGB`, `Art. 10 MarkenRL`); sie werden automatisch verlinkt.
- Gestaltung der Kursapp IPelico: `DESIGN.md` ist verbindlich (Glas-Stil, Rhein-IP-Blau, Zeichen, Icons);
  Assets liegen in `src/templates/ipelico/` und werden als SVG-Sprite (`__SPRITE__`) und Schriften
  (`__FONTS__`) eingebettet. Icons erzeugt `tools/gen_assets.py` (Gemini + potrace).
- Vor jedem Push: `python3 build.py` fehlerfrei, `python3 tools/smoke_test.py` über lokalen HTTP-Server
  (siehe `PLAYBOOK.md` Abschnitt 7).
- Aktenzeichen und Daten von Entscheidungen nie ungeprüft übernehmen; per WebSearch verifizieren.
- Klausur-PDFs unter `klausuren/` sind nicht versioniert; Zuordnung Klausur → Beschluss steht in
  `klausuren/README.md` und ist bei neuen Klausuren fortzuschreiben (Vorgehen: `PLAYBOOK.md` 5a).
- Zweites Wissenspaket EPG (`src/knowledge/upc/`): Normtexte und Entscheidungen kommen aus `data/upca.json`,
  `data/upc_rop.json`, `data/upc_decisions.json` (erzeugt von `tools/fetch_upc.py` aus der RheinIP-Postgres-Datenbank
  und den amtlichen Texten; Vorgehen `PLAYBOOK.md` Abschnitt 11). Zitierform `Art. 33 Abs. 1 EPGÜ`, `R. 19.1 VerfO`.
  Einheitspatent (`src/knowledge/upc/einheitspatent.py`): `data/up_epatvo.json`, `data/up_epatuevo.json`,
  `data/up_doeps.json`, `data/up_gebeps.json`, `data/up_richtlinien.json` (aus der Tabelle `UPLegaltext` der
  RheinIP-Datenbank); Zitierform `Art. 3 EPatVO`, `Art. 6 EPatÜVO`, `R. 6 Abs. 1 DOEPS`, `Art. 2 GebOEPS`; UP-Richtlinien
  und EPA-Informationsseiten als `source`-Knoten (`quellen=["uprl:2.4", "upinfo:cost"]`).
- Drittes Wissenspaket Patentrecht (`src/knowledge/patent/`): Normtexte `data/patg.json`, `patv.json`, `intpatueg.json`, `patkostg.json`
  (XML von gesetze-im-internet.de) und Korpus `data/patent_decisions.json` (BPatG-Nichtigkeits- und Beschwerdesenate, BGH-Patentsachen aus
  den Tabellen BpatgDecision/BghDecision/DeCourtNorm der RheinIP-Datenbank), beides aus `tools/fetch_patent.py` (PLAYBOOK Abschnitt 12).
  Zitierform `§ 3 Abs. 1 PatG`, `§ 9 PatV`, `Art. II § 6 Abs. 1 Nr. 3 IntPatÜG`, `§ 6 PatKostG`, `Anlage PatKostG`. Leitentscheidungen in
  `patent/cases.py` werden beim Import gegen den Korpus geprüft (Aktenzeichen + Datum); unbekannte Entscheidungen brechen den Build ab.
- Viertes Wissenspaket Designrecht (`src/knowledge/design/`): Normtexte `data/designg.json`, `designv.json` (XML von gesetze-im-internet.de),
  `designrl.json` (Richtlinie 98/71/EG, Cellar-PDF), `designrl2024.json` (Richtlinie (EU) 2024/2823, Cellar-XHTML), `ggv.json` (VO (EG) Nr. 6/2002
  über Unionsgeschmacksmuster, konsolidiert 1.7.2026, Cellar-XHTML) und Korpus `data/design_decisions.json` (BPatG-Designsachen, BGH I. ZS aus der
  RheinIP-Datenbank), alles aus `tools/fetch_design.py` (PLAYBOOK Abschnitt 13). Zitierform `§ 2 Abs. 3 DesignG`, `§ 7 DesignV`, `Art. 5 DesignRL`,
  `Art. 19 DesignRL 2024`, `Art. 20a GGV`. BGH-/BPatG-Leitentscheidungen in `design/cases.py` werden gegen den Korpus geprüft; EuGH/EuG-Fälle
  per WebSearch verifizieren. Kurs `kurse/d01_designrecht.py`; Anspruchsgrundlagentabelle `d_des_anspruchsgrundlagen_eu` (MarkenG, PatG, GebrMG,
  DesignG, UrhG, UMV/GGV, EPGÜ mit VerfO-Regeln).
