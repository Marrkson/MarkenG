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
