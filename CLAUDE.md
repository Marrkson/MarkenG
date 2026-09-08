# Hinweise für Agenten

- Inhalte werden ausschließlich in `src/knowledge/` gepflegt; `docs/`, `graph/`, `flashcards/` und
  `data/*.json` sind generiert (`python3 build.py`) und werden mitversioniert.
- Vorgehen für neue Rechtsgebiete, Datenmodell, Konventionen und Prüfschritte: `PLAYBOOK.md`.
- Gesetzeszitate im Text so schreiben, dass `src/knowledge/gesetze.py` sie erkennt
  (`§ 14 Abs. 2 Nr. 2`, `§ 242 BGB`, `Art. 10 MarkenRL`); sie werden automatisch verlinkt.
- Vor jedem Push: `python3 build.py` fehlerfrei, Playwright-Rauchtest über lokalen HTTP-Server
  (siehe `PLAYBOOK.md` Abschnitt 7).
- Aktenzeichen und Daten von Entscheidungen nie ungeprüft übernehmen; per WebSearch verifizieren.
- Klausur-PDFs unter `klausuren/` sind nicht versioniert; Zuordnung Klausur → Beschluss steht in
  `klausuren/README.md` und ist bei neuen Klausuren fortzuschreiben (Vorgehen: `PLAYBOOK.md` 5a).
