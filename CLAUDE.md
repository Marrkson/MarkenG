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
