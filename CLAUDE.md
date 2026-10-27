# Hinweise für Agenten

- Inhalte werden ausschließlich in `src/knowledge/` gepflegt; `docs/`, `graph/`, `flashcards/` und
  `data/*.json` sind generiert (`python3 build.py`) und werden mitversioniert.
- Vorgehen für neue Rechtsgebiete, Datenmodell, Konventionen und Prüfschritte: `PLAYBOOK.md`.
- Gesetzeszitate im Text so schreiben, dass `src/knowledge/gesetze.py` sie erkennt
  (`§ 14 Abs. 2 Nr. 2`, `§ 242 BGB`, `Art. 10 MarkenRL`); sie werden automatisch verlinkt. Nacktes `§` nur im Markenpaket
  (= MarkenG); in Patent, Design, EPG jedes Zitat mit Gesetz (`§ 139 PatG`, `Art. 33 EPGÜ`, `R. 19.1 VerfO`). MarkenG in der
  Fassung von 2026 zitieren (Unionsmarken §§ 119 bis 125a, nicht §§ 125b ff.). Prüfung: `python3 tools/check_zitate.py`.
- Gestaltung der Kursapp IPelico: `DESIGN.md` ist verbindlich (Glas-Stil, Rhein-IP-Blau, Zeichen, Icons);
  Assets liegen in `src/templates/ipelico/` und werden als SVG-Sprite (`__SPRITE__`) und Schriften
  (`__FONTS__`) eingebettet. Icons erzeugt `tools/gen_assets.py` (Gemini + potrace).
- Vor jedem Push: `python3 build.py` und `python3 tools/check_zitate.py` fehlerfrei, `python3 tools/smoke_test.py` über lokalen HTTP-Server
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
  Prüfungsrichtlinien des DPMA: `data/dpma_pruefungsrichtlinien.json` (`tools/fetch_pruefungsrichtlinien.py`, PDF P 2796), als
  `source`-Knoten in `patent/richtlinien.py` (`quellen=["prl:2.4.1"]`), Kurs `kurse/p02_pruefungsrichtlinien.py`.
- Viertes Wissenspaket Designrecht (`src/knowledge/design/`): Normtexte `data/designg.json`, `designv.json` (XML von gesetze-im-internet.de),
  `designrl.json` (Richtlinie 98/71/EG, Cellar-PDF), `designrl2024.json` (Richtlinie (EU) 2024/2823, Cellar-XHTML), `ggv.json` (VO (EG) Nr. 6/2002
  über Unionsgeschmacksmuster, konsolidiert 1.7.2026, Cellar-XHTML) und Korpus `data/design_decisions.json` (BPatG-Designsachen, BGH I. ZS aus der
  RheinIP-Datenbank), alles aus `tools/fetch_design.py` (PLAYBOOK Abschnitt 13). Zitierform `§ 2 Abs. 3 DesignG`, `§ 7 DesignV`, `Art. 5 DesignRL`,
  `Art. 19 DesignRL 2024`, `Art. 20a GGV`. BGH-/BPatG-Leitentscheidungen in `design/cases.py` werden gegen den Korpus geprüft; EuGH/EuG-Fälle
  per WebSearch verifizieren. Kurs `kurse/d01_designrecht.py`; Anspruchsgrundlagentabelle `d_des_anspruchsgrundlagen_eu` (MarkenG, PatG, GebrMG,
  DesignG, UrhG, UMV/GGV, EPGÜ mit VerfO-Regeln).
- Arbeitnehmererfinderrecht (Teil des Patentpakets): `data/arbnerfg.json` (XML), `data/arbnerfg_vergrl.json` (Vergütungsrichtlinien 1959,
  PDF dpma.de), `data/arbnerfg_decisions.json` (Tabelle `SchiedsstelleDecision` + BGH/BPatG mit ArbEG-Zitaten) aus `tools/fetch_arbnerfg.py`.
  Kommentar aus der Rechtsprechung in `src/knowledge/patent/arbnerfg_kommentar/` (`rn()` prüft Belege gegen den Korpus), Kurs `kurse/p04_arbnerfg.py`.
  Zitierform `§ 9 Abs. 2 ArbnErfG` (nie „ArbEG“ im eigenen Text), Richtlinien als „RL Nr. 34“ (`source:vrl:34`); Altfälle (Meldung vor
  1.10.2009) nach ArbnErfG a.F. (§ 43 Abs. 3 ArbnErfG). PLAYBOOK Abschnitt 16.
- Spielmechanik und Erinnerung (Tagesziel 100 XP, Streak nur über Zieltage, Service Worker `src/templates/sw.js`, Cloudflare Worker
  `push/` mit `node push/test.mjs`, Worker-URL in `data/push_api.txt`): `PLAYBOOK.md` Abschnitt 14. `data/push_vapid_private.txt` nie versionieren.
- Normkurse und Fallketten (Jurafuchs-Format): Kapitel je Vorschrift nach `data/norm_ranking.json` (`tools/norm_ranking.py`), Fälle als
  `fallkette` mit kurzen Fragen, Längengrenzen `LIMITS` in `kurse/__init__.py` für `kompakt=True`-Kurse: `PLAYBOOK.md` Abschnitt 15.
- Englische App für das EPG (`docs/en/`): Oberfläche `src/knowledge/upc/en/ui.py` (Ersetzungen im Template, jedes Paar muss treffen),
  Inhalte `src/knowledge/upc/en/*.json` (nur Text, Hash `_de` des deutschen Stands). Wer EPG-Inhalte oder Oberflächentext ändert, zieht die
  englische Fassung nach: `python3 tools/i18n_en.py status`, `export … --nur-offen`, `check`. Zitierform englisch `Art. 33(1) UPCA`,
  `R. 19.1 RoP`, `Art. 3(1) UPReg`, `R. 6(1) UPR`, `Art. 8 IPRED`. Normtexte amtlich englisch (VerfO-Wortlaut 2022). PLAYBOOK Abschnitt 17.
- Fünftes Wissenspaket EPÜ (`src/knowledge/epc/`): Artikel und Regeln aus `data/epc.json` (epo.org deutsch/englisch, DB-Kontrolle), Korpus der
  Beschwerdekammern `data/epc_decisions.json` (Tabelle `BoaDecision`), Richtlinien 2026 `data/epc_guidelines.json` und Amtsblatt `data/epc_oj.json`
  (Tabelle `EPOLegaltext`), Paper-D-Rangliste `data/eqe_d1.json`; alles aus `tools/fetch_epc.py`. Zitierform `Art. 54 Abs. 3 EPÜ`, `R. 71 Abs. 3 EPÜ`
  (Familien `epc`/`epcr`), `Art. 14 Abs. 1 GebO`, `Art. 12 Abs. 4 VOBK`, `R. 80.2 PCT` (nur Text). Kurs `kurse/e01_epue_paper_d.py` (Gebiet Patent, auch
  englisch: `src/knowledge/upc/en/e01.json`, `epc_knoten_*.json`), Ansicht `#/boa`. Leitentscheidungen `epc/cases*.py` werden gegen den Korpus geprüft.
  PLAYBOOK Abschnitt 18.
