# IPelico-Assets

Alle Dateien hier werden von `src/build_kurs.py` zu einem `<symbol>`-Sprite zusammengefasst und an der
Stelle `__SPRITE__` in `src/templates/kurs.html` eingebettet. Dateiname = Symbol-ID.

| Ordner | Präfix | Format | Regeln (siehe `DESIGN.md`) |
|---|---|---|---|
| `icons/` | `ic-` | 24×24, Strich 1.75, `currentColor` | gefüllte Variante mit Suffix `-f` |
| `motifs/` | `m-` | 24×24 wie Icons | Bausteine der Kapitel-Vignetten |
| `logo/` | – | 100×100 | Zeichen `ipelico-mark`, Badge `ipelico-badge`, gerenderte App-Icons (`tools/render_icons.py`) |
| `kurse/` | `ks-` | 160×120 | eine Szene je Kurs, Kursfarbe über `var(--c)` |
| `kapitel/` | `vg-` | 64×64 | optionale Hand-Overrides; sonst erzeugt `vignettes.py` die Vignetten |

Neues Kapitel: Eintrag in `vignettes.py` (`CHAPTERS`) ergänzen, sonst warnt der Build und nimmt ein
Motiv nach Stichwort. Neuer Kurs: `kurse/ks-<kursid>.svg` anlegen und `icon` in `k*.py` auf ein
vorhandenes `ic-<name>` setzen; der Build bricht sonst ab.

Farben nie fest eintragen; nur `currentColor` oder `style="fill:var(--x)"`. Keine `<style>`-Blöcke,
keine externen Referenzen. Interne IDs (Verläufe, Masken) werden vom Build mit der Symbol-ID präfixiert.
