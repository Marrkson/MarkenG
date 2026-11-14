# Klausurrelevante Normen, Anspruchsgrundlagen und Definitionen

Stand: 14. November 2026. Grundlage sind die Klausurlösungen in Lösungssprache unter `klausuren/loesungen/` (nicht versioniert):
17 TS-Lösungen (II/2018 bis III/2023) sowie je eine Lösung NS II/2019, RP1 II/2019 und RP2 I/2019. Für Marken, Design und
ArbnErfG gibt es also bisher nur eine Lösung je Bereich; dort sind die Listen aus den Aufgabentexten aller 17 Klausuren je Art
(`klausuren/json/`) und den bestehenden Kursen (k12, k13, d01, d02) ergänzt (Klausur-IDs in Klammern = nur aus dem Aufgabentext
erkennbar). Jede Frist, Gebühr und Voraussetzung ist am geltenden Normtext geprüft (MarkenG 2026, GGV konsolidiert 01.07.2026).

Zu jedem Bereich gibt es einen Kurs in IPelico („Anspruchsgrundlagen für die Klausur“): ein Kapitel je Anspruchsgrundlage mit
Prüfungsschema in Lösungssprache, Definitionen, Drill zu Normenketten und Fristen und Klausurfällen.

| Bereich | Kurs | Kapitel | Einheiten |
|---|---|---|---|
| Patent | p05 Anspruchsgrundlagen Patent | 14 | 242 |
| Gebrauchsmuster | p06 Anspruchsgrundlagen Gebrauchsmuster | 7 | 107 |
| Marken | k15 Anspruchsgrundlagen Marken | 11 | 134 |
| Design | d03 Anspruchsgrundlagen Design | 8 | 108 |
| ArbnErfG | p07 Anspruchsgrundlagen ArbnErfG | 8 | 118 |

## Häufigkeit in den TS-Lösungen

Wie viele der 17 TS-Klausuren die Anspruchsgrundlage prüfen:

| AGL | TS-Klausuren |
|---|---|
| Einspruch (§ 59 PatG) | 11 |
| Widerruf und beschränkte Aufrechterhaltung (§ 21 PatG, § 61 PatG) | 10 |
| Nichtigkeitsklage (§ 81 PatG, § 22 PatG, Art. II § 6 IntPatÜG) | 8 |
| Beschwerde (§ 73 PatG) | 8 |
| Prüfungs- und Erteilungsverfahren (§§ 42 bis 49 PatG) | 8 |
| Abzweigung (§ 5 GebrMG) | 7 |
| Priorität (§ 40 PatG, § 41 PatG, Art. 4 PVÜ, Art. 87 EPÜ, § 6 GebrMG) | 6 |
| Wiedereinsetzung (§ 123 PatG) | 5 |
| Teilung (§ 39 PatG), Änderungen (§ 38 PatG), Verletzung (§ 139 PatG, § 24 GebrMG), GebrM-Löschung (§ 15 GebrMG) | je 4 |
| Weiterbehandlung (§ 123a PatG), Gebühren und Rücknahmefiktion (§ 6 PatKostG, § 35a PatG) | je 3 |

Meistzitierte Einzelnormen (Zahl der Klausuren): § 6 Abs. 1 PatKostG (18), § 4 PatG (15), § 59 Abs. 1 PatG, § 21 Abs. 1 PatG,
§ 3 Abs. 1 PatG, § 6 Abs. 2 PatKostG (je 14), § 193 BGB (13), § 3 Abs. 2 PatG (12), § 5 Abs. 1 GebrMG (11), § 61 Abs. 1 PatG,
§ 21 Abs. 2 PatG, § 188 Abs. 2 BGB (je 10), § 73 PatG, § 123 Abs. 1 PatG, § 3 Abs. 1 GebrMG, § 187 Abs. 1 BGB, § 3 Abs. 1 PatKostG (je 9).

## Allgemein: Fristen immer mit drei Normen

| Stelle | Frist | Berechnung | Verschiebung |
|---|---|---|---|
| DPMA | Fachnorm (z. B. § 59 Abs. 1 S. 1 PatG) | § 187 Abs. 1 BGB, § 188 Abs. 2, 3 BGB | § 193 BGB (Feiertag am Erklärungsort: München, Jena, Berlin) |
| BPatG | Fachnorm (z. B. § 73 Abs. 2 S. 1 PatG) | § 99 Abs. 1 PatG bzw. § 82 Abs. 1 MarkenG i.V.m. § 222 Abs. 1 ZPO | § 222 Abs. 2 ZPO |
| EPA | Fachnorm | R. 131 EPÜ | R. 134 EPÜ |
| Priorität | Art. 4 C Abs. 1 PVÜ | Art. 4 C Abs. 2 PVÜ | Art. 4 C Abs. 3 PVÜ |
| Gebühren | § 6 Abs. 1 PatKostG (Fälligkeit § 3 Abs. 1 PatKostG) | wie Handlungsfrist | Zahlungstag § 2 PatKostZV; Folge § 6 Abs. 2 PatKostG |

## Patent (Teil A: Rechtsbestand und Rechtsbehelfe)

Grundlage: Lösungen der 17 TS-Klausuren II/2018 bis III/2023 (`klausuren/loesungen/ts`) und RP2 I/2019; Kurs p05, Kapitel p05a bis p05g
(`src/knowledge/kurse/_p05_a.py`). Normtexte geprüft an `data/patg.json`, `data/patkostg.json` (Anlage), `data/intpatueg.json`,
`data/upca.json`, BGB/ZPO/PatKostZV/VwZG aus dem Gesetze-Cache. Klausur-IDs ohne Klammer: in den Lösungen geprüft; die übrigen
Aufgabentexte (NS, RP1, RP2) enthalten keine weiteren Fragen zu diesen Rechtsbehelfen.

### Anspruchsgrundlagen und Rechtsbehelfe

| AGL | Normenkette (V1 … Vn mit Norm) | Rechtsfolge | Klausuren |
|---|---|---|---|
| Patentfähigkeit (Vorfrage zu § 21 Abs. 1 Nr. 1, § 22 Abs. 1, § 48 S. 1, § 49 Abs. 1 PatG; Art. II § 6 Abs. 1 Nr. 1 IntPatÜG) | V0 Auslegung, Merkmalsgliederung (§ 14 PatG) · V1 Zeitrang: Anmeldetag (§ 35 Abs. 1 PatG), Priorität (§ 40 Abs. 1, 3 PatG; § 41 Abs. 1 PatG i.V.m. Art. 4 PVÜ; Art. 87 bis 89 EPÜ), Teilpriorität · V2 technische Lehre (§ 1 Abs. 1 PatG) · V3 kein Ausschluss (§ 1 Abs. 3, 4 PatG, §§ 1a, 2, 2a PatG) · V4 Stand der Technik (§ 3 Abs. 1 S. 2 PatG), ältere Anmeldungen (§ 3 Abs. 2 S. 1 Nr. 1 bis 3, S. 2 PatG; PCT erst nach nationaler Phase, Art. III § 8 Abs. 3 IntPatÜG) · V5 keine unschädliche Offenbarung (§ 3 Abs. 5 PatG) · V6 Neuheit: Einzelvergleich (§ 3 Abs. 1 S. 1 PatG; Indikation § 3 Abs. 3, 4 PatG) · V7 erfinderische Tätigkeit (§ 4 S. 1 PatG; ältere Anmeldungen außer Betracht, § 4 S. 2 PatG) · V8 gewerbliche Anwendbarkeit (§ 5 PatG) | Erteilung / Aufrechterhaltung bzw. Zurückweisung (§ 48 S. 1 PatG), Widerruf (§ 21 Abs. 1 Nr. 1 PatG), Nichtigerklärung (§ 22 Abs. 1 PatG), je Anspruch und Hilfsantrag | TS II/2018, TS III/2018, TS I/2019, TS II/2019, TS III/2019, TS I/2020, TS II/2020, TS III/2020, TS I/2021, TS II/2021, TS III/2021, TS I/2022, TS II/2022, TS III/2022, TS I/2023, TS II/2023, TS III/2023 |
| Einspruch, § 59 Abs. 1 S. 1 PatG i.V.m. § 21 Abs. 1 PatG | V1 Statthaftigkeit: erteiltes Patent, Veröffentlichung der Erteilung (§ 59 Abs. 1 S. 1 PatG, § 58 Abs. 1 PatG); verfrühter Einspruch unzulässig · V2 Einsprechender: jeder, Entnahme nur der Verletzte (§ 59 Abs. 1 S. 1 PatG) · V3 Frist neun Monate, Eingang beim DPMA (nicht PIZ, § 34 Abs. 2 S. 1 PatG), keine Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 1 PatG) · V4 Form: schriftlich (§ 59 Abs. 1 S. 2 PatG, § 125a Abs. 1 PatG), deutsch (§ 126 PatG), Vertretung (§ 15 DPMAV, § 25 Abs. 1 PatG) · V5 Gebühr 200 EUR je Einsprechendem (Nr. 313 600 Anlage PatKostG, § 6 Abs. 1 S. 1, Abs. 2 PatKostG) · V6 Widerrufsgrund des § 21 PatG behauptet (§ 59 Abs. 1 S. 3 PatG) · V7 Tatsachen im Einzelnen bis Fristende (§ 59 Abs. 1 S. 4, 5 PatG) · B: Widerrufsgrund (§ 21 Abs. 1 Nr. 1 bis 4 PatG) | Verwerfung des unzulässigen Einspruchs; auf zulässigen Einspruch Aufrechterhaltung, beschränkte Aufrechterhaltung oder Widerruf durch Beschluss (§ 61 Abs. 1 S. 1, 2 PatG); Rücknahme: Fortsetzung von Amts wegen (§ 61 Abs. 1 S. 3, 4 PatG); Kosten § 62 Abs. 1 PatG | TS II/2018, TS III/2018, TS II/2019, TS II/2020, TS I/2021, TS III/2021, TS I/2022, TS II/2022, TS III/2022, TS I/2023, TS II/2023 |
| Widerruf und beschränkte Aufrechterhaltung, § 61 Abs. 1 S. 2 PatG i.V.m. § 21 Abs. 1, 2 PatG | V1 mindestens ein zulässiger Einspruch (§ 61 Abs. 1 S. 2 PatG) · V2 Verfahren nicht beendet (§ 61 Abs. 1 S. 4, 5 PatG) · V3 Amtsermittlung, Hinweise Dritter (§ 59 Abs. 5 PatG i.V.m. § 46 Abs. 1 S. 1, § 43 Abs. 3 S. 2 PatG); weitere Gründe von Amts wegen außer Entnahme · V4 Gehör (§ 59 Abs. 3 PatG) · V5 bis V8 Widerrufsgrund Nr. 1 bis 4 (§ 21 Abs. 1 PatG); Nr. 4: einschränkendes nicht offenbartes Merkmal bleibt (BGH Winkelmesseinrichtung), Aliud führt zum Widerruf · V9 beschränkte Fassung nur auf Antrag des Inhabers (§ 21 Abs. 2 PatG) · V10 keine Erweiterung (§ 21 Abs. 1 Nr. 4 PatG, Rechtsgedanke § 22 Abs. 1 PatG) | Widerruf oder beschränkte Aufrechterhaltung ex tunc (§ 21 Abs. 3 PatG), Veröffentlichung (§ 61 Abs. 3, 4 PatG); Erledigung nach Verzicht: Feststellungsbeschluss (§ 61 Abs. 1 S. 5 PatG) | TS II/2018, TS II/2019, TS II/2020, TS I/2021, TS II/2021, TS III/2021, TS I/2022, TS II/2022, TS III/2022, TS I/2023, TS II/2023 |
| Beschwerde, § 73 Abs. 1 PatG | V1 Beschluss der Prüfungsstelle oder Patentabteilung (§ 73 Abs. 1 PatG; nicht Bescheid § 45 PatG) · V2 Beteiligter (§ 74 Abs. 1 PatG) · V3 Beschwer · V4 schriftlich beim DPMA (§ 73 Abs. 2 S. 1 PatG) · V5 ein Monat nach Zustellung, Lauf nur mit Belehrung (§ 47 Abs. 2 S. 2, 3 PatG), Verkündung genügt nicht (§ 47 Abs. 1 S. 3 PatG) · V6 Gebühr 500 EUR (Nr. 401 100) oder 200 EUR (Nr. 401 300 Anlage PatKostG) in der Frist (§ 6 Abs. 1 S. 1, Abs. 2 PatKostG), gemeinsame Beschwerde gemeinschaftlicher Inhaber/Anmelder = eine Gebühr seit 18.08.2021 · V7 Abhilfe nur einseitig (§ 73 Abs. 3, 4 PatG) · V9 Beteiligte, Anschlussbeschwerde (§ 99 Abs. 1 PatG i.V.m. § 62, § 567 Abs. 3 ZPO) · V10 Prüfungsrahmen: § 87 Abs. 1 PatG, neue Widerrufsgründe nur auf Antrag des Einsprechenden (BGH Ventileinrichtung), Verschlechterungsverbot | Beschluss (§ 79 Abs. 1 PatG): Verwerfung (§ 79 Abs. 2 PatG), Zurückweisung, Sachentscheidung oder Zurückverweisung (§ 79 Abs. 3 PatG); Kosten § 80 PatG | TS III/2020, TS I/2021, TS II/2021, TS II/2022, TS III/2022, TS I/2023, TS II/2023, TS III/2023 |
| Nichtigkeitsklage, § 81 Abs. 1 S. 1 PatG i.V.m. § 22 Abs. 1 PatG; EP: Art. II § 6 Abs. 1 IntPatÜG | V1 BPatG (§ 65 Abs. 1, § 81 Abs. 4 S. 1 PatG); EP nur bei fortbestehender deutscher Zuständigkeit (Art. 83 Abs. 1, 3 EPGÜ) · V2 keine Klagesperre (§ 81 Abs. 2 S. 1 PatG, auch EPA-Einspruch) · V3 Beklagter = eingetragener Inhaber (§ 81 Abs. 1 S. 2 PatG); Kläger jeder, Entnahme nur Verletzter (§ 81 Abs. 3 PatG), Art. II § 6 Abs. 4 IntPatÜG · V4 Form, Inhalt (§ 81 Abs. 4, 5 PatG) · V5 Gebühr 4,5 nach Streitwert (§ 2 Abs. 2 PatKostG, Nr. 402 100 Anlage PatKostG, § 3 Abs. 1 S. 2 Nr. 4, § 6 Abs. 1 S. 2, Abs. 2 PatKostG) · V6 Sicherheit (§ 81 Abs. 6 PatG) · V7 Rechtsschutzbedürfnis nach Erlöschen · V8 keine Rechtskraft (§ 99 Abs. 1 PatG i.V.m. § 325 Abs. 1 ZPO), kein Strohmann, keine Nichtangriffsabrede · V9 Nichtigkeitsgrund (§ 22 Abs. 1 PatG; Art. II § 6 Abs. 1 Nr. 1 bis 5 IntPatÜG; Art. 139 Abs. 2 EPÜ) · Verfahren: § 82, § 83 PatG | Urteil (§ 84 Abs. 1 PatG): Nichtigerklärung ganz oder teilweise ex tunc (§ 22 Abs. 2 PatG i.V.m. § 21 Abs. 3 PatG; Art. II § 6 Abs. 1 S. 2, Abs. 2 IntPatÜG), Kosten § 84 Abs. 2 PatG | TS III/2018, TS I/2019, TS III/2019, TS I/2020, TS III/2021, TS III/2022, TS II/2023 |
| Nichtigkeitsklage vor dem EPG, Art. 32 Abs. 1 lit. d EPGÜ | Zentralkammer (Art. 33 Abs. 4 EPGÜ), kein Opt-out (Art. 83 Abs. 3 EPGÜ), kein vorheriger EPA-Einspruch nötig (Art. 33 Abs. 8 EPGÜ), Aussetzung möglich (Art. 33 Abs. 10 EPGÜ) | Nichtigerklärung für alle EPG-Staaten | TS III/2021, TS II/2023 |
| Klagerücknahme und Vergleich, § 99 Abs. 1 PatG i.V.m. § 269 ZPO, § 278 Abs. 6 ZPO | Rücknahme ohne Einwilligung, auch nach mündlicher Verhandlung (BGH Sitzgelenk); Gebührenermäßigung auf 1,5 nur vor Schluss der mündlichen Verhandlung bzw. Vergleich ohne vorausgegangenes Urteil (Nr. 402 110 Anlage PatKostG); Streitwert: gemeiner Wert + Schadensersatz, Verletzungsstreitwert + ein Viertel (§ 2 Abs. 2 S. 4 PatKostG i.V.m. § 51 Abs. 1 GKG; BGH Nichtigkeitsstreitwert) | Verfahren gilt als nicht anhängig (§ 269 Abs. 3 S. 1 ZPO), Kosten beim Kläger (§ 269 Abs. 3 S. 2 ZPO); Vergleich beendet Verfahren, nicht Patent | TS I/2019 |
| Beitritt, § 59 Abs. 2 PatG | Einspruch anhängig · Dritter · Verletzungsklage (auch Verfügungsantrag, BGH Ratschenschlüssel) oder negative Feststellungsklage nach Abmahnung · nach Ablauf der Einspruchsfrist, binnen drei Monaten nach Klageerhebung · Begründung in der Frist (§ 59 Abs. 2 S. 3, 4 PatG) · Gebühr Nr. 313 600 Anlage PatKostG (§ 3 Abs. 1 S. 2 Nr. 3 PatKostG) | Stellung eines Einsprechenden, eigene Widerrufsgründe | TS I/2023 |
| Rechtsbeschwerde, § 100 Abs. 1 PatG bzw. § 100 Abs. 3 PatG | V1 Beschluss über Beschwerde nach § 73 PatG oder nach § 61 Abs. 2 PatG · V2 Zulassung (§ 100 Abs. 2 Nr. 1, 2 PatG) oder Mangel nach § 100 Abs. 3 Nr. 1 bis 6 PatG; keine Nichtzulassungsbeschwerde (§ 99 Abs. 2 PatG) · V3 Beteiligter (§ 101 Abs. 1 PatG) · V4 ein Monat beim BGH (§ 102 Abs. 1 PatG) · V5 Begründung ein Monat ab Einlegung (§ 102 Abs. 3, 4 PatG) · V6 BGH-Anwalt (§ 102 Abs. 5 PatG) · V7 Rechtsverletzung (§ 101 Abs. 2 PatG), Bindung an Tatsachen (§ 107 Abs. 2 PatG) | Beschluss (§ 107 Abs. 1 PatG); Aufhebung und Zurückverweisung mit Bindung (§ 108 PatG) | TS I/2023 (TS III/2021: Abschluss des Einspruchsverfahrens) |
| Berufung zum BGH, § 110 Abs. 1 PatG | ein Monat ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung (§ 110 Abs. 3 PatG) · Begründung drei Monate (§ 112 Abs. 2 PatG) · Vertretung Rechts- oder Patentanwalt (§ 113 PatG) | Urteil des BGH | TS III/2019 |
| Doppelschutz, Art. II § 8 Abs. 1 IntPatÜG | deutsches und europäisches Patent · derselbe Erfinder oder Rechtsnachfolger · dieselbe Erfindung · dieselbe Priorität · EP wegen Opt-out nicht beim EPG (seit 01.06.2023) · Zeitpunkt nach Art. II § 8 Abs. 1 Nr. 1 bis 4 IntPatÜG | DE-Patent verliert endgültig seine Wirkung (Art. II § 8 Abs. 2 IntPatÜG); sonst Einrede Art. II § 18 IntPatÜG; Einspruch bleibt zulässig (BGH Kornfeinung) | TS II/2023 |

### Definitionen

| Begriff | Definition | Quelle |
|---|---|---|
| Einspruch | Rechtsbehelf jedes Dritten (bei Entnahme nur des Verletzten), mit dem binnen neun Monaten nach Veröffentlichung der Erteilung der Widerruf aus Gründen des § 21 PatG verlangt wird | § 59 Abs. 1 S. 1, 3 PatG |
| Tatsachen im Einzelnen (Substantiierung) | Begründung, aus der Patentinhaber und Patentabteilung ohne eigene Ermittlungen abschließende Folgerungen für das Vorliegen eines Widerrufsgrunds ziehen können; Richtigkeit ist Frage der Begründetheit | § 59 Abs. 1 S. 4 PatG; st. Rspr., BGH Leistungshalbleiterbauelement |
| Substantiierte Vorbenutzung | Angabe von Gegenstand (Merkmalszuordnung), Zeitpunkt vor dem Zeitrang, Ort, Person und Umständen der Öffentlichkeit mit Beweismitteln | Rspr. des BPatG; Lösungen TS II/2019, TS I/2021 |
| Beitritt | Eintritt des Verletzungsbeklagten oder negativen Feststellungsklägers als Einsprechender in ein anhängiges Einspruchsverfahren | § 59 Abs. 2 PatG |
| Widerrechtliche Entnahme | wesentlicher Inhalt des Patents den Beschreibungen, Zeichnungen, Modellen, Gerätschaften, Einrichtungen oder dem Verfahren eines anderen ohne dessen Einwilligung entnommen | Legaldefinition § 21 Abs. 1 Nr. 3 PatG |
| Unzulässige Erweiterung | Gegenstand geht über die ursprünglich eingereichte Fassung hinaus; liegt vor, wenn er sich erst aus eigenen, vom Fachwissen getragenen Überlegungen des Fachmanns ergibt | § 21 Abs. 1 Nr. 4 PatG; BGH Hubgliedertor I |
| Einschränkendes nicht offenbartes Merkmal | konkretisiert eine ursprünglich als zur Erfindung gehörend offenbarte Anweisung, Streichung würde den Schutzbereich erweitern: bleibt im Anspruch, stützt die Patentfähigkeit nicht | BGH Winkelmesseinrichtung; BGH Wundbehandlungsvorrichtung |
| Aliud | hinzugefügtes Merkmal betrifft einen technischen Aspekt, der den ursprünglichen Unterlagen weder konkret noch abstrakt zu entnehmen ist: Widerruf | Lösungen TS II/2021, TS I/2023 (nach BGH-Rspr.) |
| Ausführbarkeit | Patent offenbart die Erfindung so deutlich und vollständig, dass ein Fachmann sie ohne unzumutbaren Aufwand ausführen kann | § 21 Abs. 1 Nr. 2 PatG, § 34 Abs. 4 PatG |
| Beschränkte Aufrechterhaltung | Teilwiderruf durch Änderung von Ansprüchen, Beschreibung oder Zeichnungen, wenn die Gründe nur einen Teil betreffen; nur auf Antrag des Inhabers | § 21 Abs. 2 PatG |
| Erledigung der Hauptsache | Patent erloschen, kein Einsprechender hat ein eigenes Interesse am rückwirkenden Widerruf | § 61 Abs. 1 S. 5 PatG |
| Technik | Lehre zum planmäßigen Handeln unter Einsatz beherrschbarer Naturkräfte zur unmittelbaren Herbeiführung eines kausal übersehbaren Erfolgs | st. Rspr. des BGH; § 1 Abs. 1 PatG |
| Neu | Erfindung gehört nicht zum Stand der Technik | Legaldefinition § 3 Abs. 1 S. 1 PatG |
| Stand der Technik | alle Kenntnisse, die vor dem für den Zeitrang maßgeblichen Tag durch schriftliche oder mündliche Beschreibung, Benutzung oder sonst der Öffentlichkeit zugänglich gemacht worden sind | Legaldefinition § 3 Abs. 1 S. 2 PatG |
| Öffentlich zugänglich (Vorbenutzung) | nicht nur entfernte Möglichkeit, dass beliebige Dritte zuverlässige Kenntnis erhalten, angeknüpft an einen feststehenden Kommunikationsakt (Angebot, Lieferung); Entwicklung und Erprobung mit Geheimhaltungsinteresse regelmäßig nicht | BGH Presszange; BGH Oberflächenbeschichtung |
| Neuheitsschädlich offenbart | was der Fachmann dem Gesamtinhalt einer Entgegenhaltung unmittelbar und eindeutig entnimmt, einschließlich des Selbstverständlichen | BGH Olanzapin |
| Ältere Anmeldung | Patentanmeldung mit älterem Zeitrang, veröffentlicht an oder nach dem Zeitrangtag (national, EP mit DE-Benennungsgebühr, PCT mit DPMA als Bestimmungsamt nach nationaler Phase); nur Neuheit | § 3 Abs. 2 PatG, § 4 S. 2 PatG, Art. III § 8 Abs. 3 IntPatÜG |
| Erfinderische Tätigkeit | Erfindung ergibt sich für den Fachmann nicht in naheliegender Weise aus dem Stand der Technik | Legaldefinition § 4 S. 1 PatG |
| Fachmann | Durchschnittsfachmann des Gebiets, das sich nach dem technischen Problem bestimmt (Konstrukteur, nicht Anwender); ggf. Team | BGH Fischbissanzeiger |
| Gewerblich anwendbar | Gegenstand kann auf irgendeinem gewerblichen Gebiet einschließlich der Landwirtschaft hergestellt oder benutzt werden | Legaldefinition § 5 PatG |
| Unschädliche Offenbarung | höchstens sechs Monate vor Einreichung, beruhend auf offensichtlichem Missbrauch oder Zurschaustellung auf amtlich anerkannter Ausstellung (Angabe, Bescheinigung binnen vier Monaten) | § 3 Abs. 5 PatG |
| Popularklage | jeder klagebefugt ohne eigenes Interesse, solange das Patent in Kraft ist; nach Erlöschen eigenes Interesse nötig | § 81 Abs. 1 PatG; BGH Leistungsüberwachungsgerät |
| Subsidiarität (Klagesperre) | Nichtigkeitsklage ausgeschlossen, solange Einspruch möglich oder anhängig, auch beim EPA und bei Stützung nur auf ältere nationale Rechte | § 81 Abs. 2 S. 1 PatG; BGH Strahlungssteuerung, BGH Mautberechnung |
| Erweiterung des Schutzbereichs | nach der Erteilung geänderte Fassung schützt mehr als die erteilte; nur Nichtigkeitsgrund | § 22 Abs. 1 Alt. 2 PatG, Art. II § 6 Abs. 1 Nr. 4 IntPatÜG |
| Strohmann | Kläger ohne eigenes Interesse für einen gebundenen Hintermann; ebenso ausgeschlossen | BGH Ziehmaschinenzugeinheit II |
| Nichtigkeitsstreitwert | gemeiner Wert des Patents bei Klageerhebung zuzüglich bis dahin entstandener Schadensersatzforderungen; Anhalt Verletzungsstreitwert plus ein Viertel | BGH Nichtigkeitsstreitwert |
| Qualifizierter Hinweis | frühzeitiger Hinweis auf entscheidungserhebliche Gesichtspunkte, möglichst binnen sechs Monaten nach Zustellung der Klage | § 83 Abs. 1 PatG |
| Beschluss (DPMA) | Entscheidung, die das Verfahren ganz oder teilweise regelt; zu begründen, zuzustellen, mit Belehrung; ein Prüfungsbescheid ist keiner | § 47 Abs. 1, 2 PatG |
| Beschwer (formell) | Entscheidung bleibt hinter dem Antrag des Beschwerdeführers zurück | allg. Rechtsmittelrecht |
| Abhilfe | Änderung des eigenen Beschlusses durch die erlassende Stelle bei begründeter Beschwerde; nur einseitiges Verfahren | § 73 Abs. 3 S. 1, Abs. 4 PatG |
| Unselbständige Anschlussbeschwerde | Antrag des Beschwerdegegners auch nach Fristablauf; verliert Wirkung mit Rücknahme oder Verwerfung der Hauptbeschwerde | § 99 Abs. 1 PatG i.V.m. § 567 Abs. 3 ZPO |
| Verschlechterungsverbot | ohne Rechtsmittel des Gegners keine Änderung zum Nachteil des Beschwerdeführers | Rechtsgedanke § 528 S. 2 ZPO i.V.m. § 99 Abs. 1 PatG |
| Grundsätzliche Bedeutung | entscheidungserhebliche, klärungsbedürftige Rechtsfrage, die sich in einer unbestimmten Vielzahl von Fällen stellen kann | § 100 Abs. 2 Nr. 1 PatG; Begriff der ZPO-Zulassungsgründe |
| Versagung rechtlichen Gehörs | erheblicher Vortrag übergangen oder Entscheidung auf einen Gesichtspunkt gestützt, zu dem keine Äußerung möglich war | Art. 103 Abs. 1 GG, § 100 Abs. 3 Nr. 3 PatG |
| Nicht mit Gründen versehen | Gründe fehlen oder sind unverständlich; sachlich falsche Gründe genügen nicht | § 100 Abs. 3 Nr. 6 PatG |

### Fristen

| Frist | Norm | Berechnung | Verschiebung | Gebühr |
|---|---|---|---|---|
| Einspruch: neun Monate nach Veröffentlichung der Erteilung | § 59 Abs. 1 S. 1 PatG; keine Wiedereinsetzung § 123 Abs. 1 S. 2 Nr. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB (§ 188 Abs. 3 BGB) | § 193 BGB | 200 EUR je Einsprechendem, Nr. 313 600 Anlage PatKostG, in der Frist (§ 6 Abs. 1 S. 1 PatKostG), sonst nicht erhoben (§ 6 Abs. 2 PatKostG); Zahlungstag § 2 PatKostZV |
| Substantiierung: bis Ablauf der Einspruchsfrist | § 59 Abs. 1 S. 5 PatG | wie Einspruch | § 193 BGB | – |
| Beitritt: drei Monate nach Erhebung der Verletzungsklage, Begründung in derselben Frist | § 59 Abs. 2 S. 1, 3 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 200 EUR, Nr. 313 600, fällig mit der Erklärung (§ 3 Abs. 1 S. 2 Nr. 3 PatKostG) |
| Antrag auf Entscheidung durch das BPatG: Widerspruch binnen zwei Monaten (Nr. 1) oder nach 15 Monaten (Nr. 2); Sperre bei Ladung/Entscheidung binnen drei Monaten | § 61 Abs. 2 PatG | BGB | § 193 BGB | 300 EUR, Nr. 400 000 Anlage PatKostG, zusätzlich |
| Nachanmeldung nach Entnahme-Einspruch: ein Monat nach amtlicher Mitteilung | § 7 Abs. 2 PatG; keine Wiedereinsetzung § 123 Abs. 1 S. 2 Nr. 3 PatG | BGB | § 193 BGB | Anmeldegebühren |
| Beschwerde: ein Monat nach Zustellung; ohne Belehrung ein Jahr | § 73 Abs. 2 S. 1 PatG, § 47 Abs. 2 S. 2, 3 PatG; Einsprechender gegen Aufrechterhaltung keine Wiedereinsetzung § 123 Abs. 1 S. 2 Nr. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB; Zustellung § 127 Abs. 1 PatG, § 5 Abs. 4 VwZG, § 4 Abs. 2 S. 2 VwZG | § 193 BGB | 500 EUR Nr. 401 100 (Einspruch) / 200 EUR Nr. 401 300 / 50 EUR Nr. 401 200 (Kostenfestsetzung) Anlage PatKostG, in der Frist, sonst nicht eingelegt (§ 6 Abs. 2 PatKostG) |
| Beschwerde gegen Kostenfestsetzungsbeschluss: zwei Wochen | § 62 Abs. 2 S. 4 PatG | BGB | § 193 BGB | 50 EUR, Nr. 401 200 |
| Vorlage nach Nichtabhilfe: ein Monat | § 73 Abs. 3 S. 3 PatG | – | – | – |
| Anschlussbeschwerde: bis Schluss der mündlichen Verhandlung | § 99 Abs. 1 PatG i.V.m. § 567 Abs. 3 ZPO, § 91 Abs. 3 PatG | – | – | kein Gebührentatbestand (unsicher) |
| Rechtsbeschwerde: ein Monat nach Zustellung, beim BGH | § 102 Abs. 1 PatG | § 106 Abs. 1 S. 1 PatG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | Gerichtskosten nach GKG |
| Rechtsbeschwerdebegründung: ein Monat ab Einlegung, verlängerbar | § 102 Abs. 3 PatG | wie oben | § 222 Abs. 2 ZPO | – |
| Nichtigkeitsklage: keine Klagefrist; Sperre § 81 Abs. 2 S. 1 PatG | – | – | – | 4,5 Gebühren nach Streitwert, Nr. 402 100 Anlage PatKostG, fällig mit Klage (§ 3 Abs. 1 S. 2 Nr. 4 PatKostG), drei Monate (§ 6 Abs. 1 S. 2 PatKostG), sonst Rücknahmefiktion (§ 6 Abs. 2 PatKostG); Ermäßigung 1,5 Nr. 402 110 |
| Widerspruch des Nichtigkeitsbeklagten: ein Monat nach Zustellung; Begründung zwei Monate nach Zustellung der Klage (+ ein Monat) | § 82 Abs. 1 PatG, § 82 Abs. 3 S. 2, 3 PatG | § 99 Abs. 1 PatG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | – |
| Qualifizierter Hinweis: soll binnen sechs Monaten nach Zustellung der Klage | § 83 Abs. 1 S. 2 PatG | – | – | – |
| Sicherheitsleistung: vom Gericht bestimmte Frist | § 81 Abs. 6 S. 2, 3 PatG | – | – | Versäumung: Klage gilt als zurückgenommen |
| Berufung: ein Monat ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung | § 110 Abs. 3 PatG | § 222 Abs. 1 ZPO (entsprechend), § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | Gerichtskosten nach GKG |
| Berufungsbegründung: drei Monate ab Zustellung, spätestens ab fünf Monaten nach Verkündung | § 112 Abs. 2 PatG | wie oben | § 222 Abs. 2 ZPO | – |
| EPA-Einspruch (Klagesperre für den DE-Teil): neun Monate nach Hinweis auf die Erteilung | Art. 99 Abs. 1 EPÜ | R. 131 Abs. 2, 4 EPÜ | R. 134 Abs. 1 EPÜ | EPA-Einspruchsgebühr |
| Ausstellungsschutz: Bescheinigung binnen vier Monaten nach Einreichung; Offenbarung höchstens sechs Monate vor Einreichung | § 3 Abs. 5 S. 1, 2 PatG | BGB | § 193 BGB | – |

### Weitere Hilfsnormen

- Fristberechnung: § 186 BGB, § 187 Abs. 1 BGB, § 188 Abs. 2, 3 BGB, § 193 BGB (DPMA); § 99 Abs. 1 PatG i.V.m. § 222 ZPO (BPatG); § 106 Abs. 1 S. 1 PatG (Rechtsbeschwerde).
- Zustellung: § 127 Abs. 1 PatG i.V.m. VwZG (Empfangsbekenntnis § 5 Abs. 4 VwZG; Einschreiben vierter Tag, § 4 Abs. 2 S. 2 VwZG); Verkündung und Zustellung von Beschlüssen § 47 Abs. 1 PatG, Belehrung § 47 Abs. 2 PatG.
- Gebühren: § 2 Abs. 1, 2 PatKostG (Gebührenverzeichnis, Streitwertgebühren), § 3 Abs. 1 PatKostG (Fälligkeit), § 5 Abs. 1 S. 3 PatKostG (Zustellung der Klage nach Zahlung), § 6 PatKostG (Frist, Fiktion), § 10 PatKostG (Erstattung), Vorbemerkung Teil A Abs. 2 und Teil B Abs. 1 Anlage PatKostG (je Antragsteller; gemeinsame Beschwerde gemeinschaftlicher Inhaber/Anmelder seit 18.08.2021), § 1 Abs. 1, § 2 PatKostZV (Zahlungswege, Zahlungstag).
- Verfahren DPMA: § 59 Abs. 3 bis 5 PatG (Anhörung, Ordnung, Verweis auf § 43 Abs. 3 S. 2, §§ 46, 47 PatG), § 62 PatG (Kosten), § 64 PatG (Beschränkung/Widerruf auf Antrag des Inhabers, Nr. 313 700), § 20 Abs. 1 Nr. 1 PatG (Verzicht ex nunc), § 25 PatG (Inlandsvertreter), § 126 PatG (Sprache), § 125a PatG (elektronische Form), § 15 DPMAV (Vollmacht).
- Verfahren BPatG: § 65 PatG, § 67 PatG (Besetzung), § 69 PatG (Öffentlichkeit), § 75 PatG (aufschiebende Wirkung), § 78 PatG (mündliche Verhandlung), § 79 PatG, § 80 PatG, § 84 PatG, § 86 PatG (Ausschließung), § 87 PatG (Untersuchungsgrundsatz), § 91 Abs. 3 PatG (Schluss der Verhandlung), § 94 Abs. 1 PatG (Verkündung/Zustellung des Urteils), § 97 PatG (Vertretung), § 99 PatG (ZPO entsprechend; Anfechtung nur nach PatG).
- BGH: § 101 PatG bis § 108 PatG (Rechtsbeschwerde), § 110 PatG bis § 121 PatG (Berufung, Vertretung § 113 PatG, Anschließung § 115 PatG, Prüfungsumfang § 116, § 117 PatG).
- ZPO entsprechend: § 50 ZPO (Parteifähigkeit), § 62 ZPO (notwendige Streitgenossen), § 253 Abs. 1 ZPO (Klageerhebung), § 269 ZPO (Rücknahme), § 278 Abs. 6 ZPO (Vergleich), § 322 ZPO, § 325 ZPO (Rechtskraft), § 528 S. 2 ZPO (Verschlechterungsverbot), § 567 Abs. 3 ZPO (Anschlussbeschwerde), § 240 ZPO (Unterbrechung bei Insolvenz).
- Europäische Bezüge: Art. II § 6, § 8, § 18 IntPatÜG; Art. III § 4, § 8 IntPatÜG; Art. 54, 56, 87 bis 89, 99, 138, 139 EPÜ; Art. 32, 33, 83 EPGÜ.
- Streitwert: § 2 Abs. 2 S. 4 PatKostG i.V.m. § 51 Abs. 1 GKG, § 63 Abs. 2 GKG; Herabsetzung § 144 PatG.

## Patent (Teil B: Erteilung, Fristen, Verletzung, Recht auf das Patent)

Grundlage: Lösungen TS II/2018 bis TS III/2023 und RP2 I/2019 (`klausuren/loesungen/`), Normtexte `data/patg.json`,
`data/patkostg.json` (Anlage zu § 2 Abs. 1 PatKostG), `data/intpatueg.json`. Kurs p05, Kapitel p05h bis p05n.

### Anspruchsgrundlagen und Rechtsbehelfe

| AGL | Normenkette (V1 … Vn mit Norm) | Rechtsfolge | Klausuren |
|---|---|---|---|
| Erteilung / Zurückweisung im Prüfungsverfahren, § 49 Abs. 1 PatG / § 48 S. 1 PatG | V1 Anmeldetag § 35 Abs. 1 PatG · V2 Prüfungsantrag § 44 Abs. 1, 2 PatG · V3 Erfordernisse § 34 PatG, § 37 PatG, § 38 PatG (Rüge § 45 Abs. 1 PatG) · V4 Patentfähigkeit §§ 1 bis 5 PatG (Bescheid § 45 Abs. 2 PatG) · V5 Gehör § 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG, Anhörung § 46 Abs. 1 S. 3, 4 PatG · V6 beantragte Fassung, einheitliche Entscheidung über Haupt- und Hilfsanträge | Erteilungsbeschluss, Wirkung ab Veröffentlichung (§ 58 Abs. 1 S. 3 PatG); sonst Zurückweisung → Beschwerde § 73 PatG, Weiterbehandlung § 123a PatG | TS II/2018, TS III/2020, TS I/2021, TS I/2022, TS II/2022, TS III/2022, TS III/2023 |
| Prioritätsrecht: innere § 40 Abs. 1 PatG; Auslandspriorität Art. 4 A Abs. 1 PVÜ i.V.m. § 41 Abs. 1 PatG; EP Art. 87 Abs. 1 EPÜ; PCT Art. 8 PCT i.V.m. Art. III § 4 IntPatÜG | V1 prioritätsbegründende (erste, vorschriftsmäßige) Voranmeldung, kein Kettenprioritätsfall § 40 Abs. 1 Hs. 2 PatG · V2 Berechtigung (Anmelder oder Rechtsnachfolger vor Nachanmeldung) · V3 dieselbe Erfindung § 40 Abs. 3 PatG, Art. 4 H PVÜ · V4 zwölf Monate § 40 Abs. 1 PatG, Art. 4 C Abs. 1 PVÜ · V5 Erklärung § 40 Abs. 4 PatG (zwei Monate) bzw. § 41 Abs. 1 PatG (16 Monate) | Zeitrang des Prioritätstags (§ 3 Abs. 1 S. 2 PatG); Rücknahmefiktion der früheren Patentanmeldung § 40 Abs. 5 S. 1 PatG (nicht GebrM, § 40 Abs. 5 S. 2 PatG; PCT: Art. III § 4 Abs. 4 IntPatÜG) | TS II/2018, TS III/2018, TS III/2020, TS III/2021, TS II/2022, TS III/2022, TS III/2023 |
| Wiedereinsetzung § 123 Abs. 1 S. 1 PatG | V1 gesetzliche Frist gegenüber DPMA/BPatG mit Rechtsnachteil, kein Ausschluss § 123 Abs. 1 S. 2 Nr. 1–3 PatG · V2 schriftlicher Antrag § 123 Abs. 2 S. 1 PatG · V3 zwei Monate nach Wegfall des Hindernisses · V4 Tatsachen, Glaubhaftmachung § 123 Abs. 2 S. 2 PatG, § 294 ZPO · V5 Nachholung § 123 Abs. 2 S. 3 PatG · V6 Jahresfrist § 123 Abs. 2 S. 4 PatG · V7 ohne Verschulden, Vertreter § 85 Abs. 2 ZPO | Handlung gilt als rechtzeitig; unanfechtbar § 123 Abs. 4 PatG; Weiterbenutzungsrecht § 123 Abs. 5 bis 7 PatG | TS II/2019, TS I/2020, TS I/2021, TS III/2022, TS I/2023 (TS II/2018: Rechtsunkenntnis) |
| Änderungen § 38 S. 1 PatG | V1 bis Erteilungsbeschluss, vor Prüfungsantrag eingeschränkt · V2 deutsche Fassung § 126 PatG · V3 keine Erweiterung gegenüber der ursprünglich eingereichten Fassung (nicht Prioritätsunterlage) · V4 beantragte Fassung | zulässig: Prüfung der neuen Fassung (neuer Bescheid); unzulässig: keine Rechte § 38 S. 2 PatG, Rüge, Zurückweisung § 48 S. 1 PatG; nach Erteilung § 21 Abs. 1 Nr. 4 PatG | TS II/2018, TS III/2020, TS I/2021, TS II/2022, TS III/2023 |
| Verletzungsansprüche § 139 Abs. 1, 2 PatG, § 140a PatG, § 140b PatG, § 242 BGB | V1 Zuständigkeit § 143 Abs. 1 PatG · V2 Patent in Kraft § 58 Abs. 1 S. 3 PatG · V3 Aktivlegitimation · V4 Benutzung § 9 S. 2 Nr. 1–3 PatG, § 10 PatG · V5 Schutzbereich § 14 PatG (wortsinngemäß, äquivalent) · V6 keine Einwendung (§ 11 PatG, § 12 PatG, § 123 Abs. 5 PatG, Erschöpfung) · V7 Wiederholungs-/Erstbegehungsgefahr § 139 Abs. 1 S. 1, 2 PatG · V8 Verschulden § 139 Abs. 2 PatG · V9 Verjährung § 141 PatG | Unterlassung; Schadensersatz (konkret, Verletzergewinn § 139 Abs. 2 S. 2 PatG, Lizenzanalogie § 139 Abs. 2 S. 3 PatG); Vernichtung, Rückruf; Auskunft; Rechnungslegung | TS III/2019, TS I/2020, TS III/2021, TS I/2022 (TS II/2020: § 9 S. 2 Nr. 3 PatG) |
| Teilung § 39 Abs. 1 S. 1 PatG | V1 anhängige Anmeldung (bis Ablauf der Beschwerdefrist) · V2 schriftliche Erklärung § 39 Abs. 1 S. 2 PatG, § 125a PatG · V3 Unterlagen binnen drei Monaten § 39 Abs. 3 PatG · V4 Gebühren § 39 Abs. 2 PatG binnen drei Monaten | Teilanmeldung mit AT und Priorität der Stammanmeldung § 39 Abs. 1 S. 4 PatG, Prüfungsantrag gilt als gestellt § 39 Abs. 1 S. 3 PatG; sonst Erklärung gilt als nicht abgegeben | TS III/2020, TS I/2021, TS II/2022, TS III/2023 (TS I/2020: Teilanmeldung DE2) |
| Weiterbehandlung § 123a Abs. 1 PatG | V1 Zurückweisung nach Versäumung einer Amtsfrist · V2 Antrag ein Monat nach Zustellung § 123a Abs. 2 S. 1 PatG · V3 Nachholung § 123a Abs. 2 S. 2 PatG · V4 Gebühr 100 EUR Nr. 313 000 GV PatKostG | Zurückweisungsbeschluss wird wirkungslos; keine Wiedereinsetzung § 123a Abs. 3 PatG | TS II/2019, TS I/2021, TS III/2022, TS III/2023 |
| Anmeldetag, Übersetzung, Gebühren, Offensichtlichkeitsprüfung: § 35 PatG, § 35a PatG, § 6 PatKostG, § 42 PatG | V1 Name, Antrag, Beschreibung dem Anschein nach § 35 Abs. 1 PatG · V2 Übersetzung § 35a PatG · V3 Anmelde-/Recherchegebühr drei Monate § 6 Abs. 1 S. 2 PatKostG · V4 offensichtliche Mängel § 42 Abs. 1 PatG · V5 offensichtlicher Ausschluss § 42 Abs. 2 PatG | Rücknahmefiktion § 35a Abs. 1 S. 2 PatG, § 6 Abs. 2 PatKostG; Zurückweisung § 42 Abs. 3 PatG | TS II/2019, TS III/2022, TS III/2023 |
| Vorbenutzungsrecht § 12 Abs. 1 S. 1 PatG (Einwendung) | V1 Erfindungsbesitz · V2 Benutzung oder Veranstaltungen im Inland · V3 Stichtag Anmelde-/Prioritätstag § 12 Abs. 2 PatG, Fortbestand · V4 kein Ausschluss § 12 Abs. 1 S. 4 PatG | Wirkung des Patents tritt nicht ein; Nutzung für den eigenen Betrieb, nur mit dem Betrieb übertragbar | TS I/2020, TS III/2021, TS I/2022 |
| Entschädigung § 33 Abs. 1 PatG | V1 Hinweis § 32 Abs. 5 PatG · V2 Benutzung des Gegenstands der Anmeldung · V3 wusste oder musste wissen · V4 kein Ausschluss § 33 Abs. 2 PatG · V5 kein Wegfall § 58 Abs. 2 PatG, § 21 Abs. 3 PatG · V6 Verjährung § 33 Abs. 3 PatG | angemessene Entschädigung, weitergehende Ansprüche ausgeschlossen | TS I/2020, TS III/2021 |
| Vindikation § 8 S. 1, 2 PatG; Art. II § 5 Abs. 1 IntPatÜG | V1 Berechtigter § 6 PatG (Rechtsnachfolge, auch § 7 Abs. 1 ArbnErfG) · V2 Anmeldung eines Nichtberechtigten / Entnahme · V3 Übereinstimmung der Lehren (sonst Mitberechtigung) · V4 Frist § 8 S. 3–5 PatG bzw. Art. II § 5 Abs. 2 IntPatÜG · V5 LG § 143 PatG | Abtretung des Erteilungsanspruchs, Übertragung des Patents oder Einräumung der Mitberechtigung | TS III/2021, RP2 I/2019 (TS II/2022: Alternative zum Entnahme-Einspruch) |
| Berichtigung der Erfindernennung § 63 Abs. 2 S. 1 PatG | V1 Nennung unrichtig oder unterblieben · V2 Anspruchsteller Erfinder (schöpferischer Beitrag) · V3 Gegner: Patentsucher/-inhaber und zu Unrecht Benannter | Zustimmung gegenüber dem DPMA, unwiderruflich § 63 Abs. 2 S. 2 PatG; keine Berichtigung veröffentlichter Schriften § 63 Abs. 3 PatG | TS III/2021, RP2 I/2019 |
| Einspruch wegen widerrechtlicher Entnahme § 59 Abs. 1 S. 1 PatG i.V.m. § 21 Abs. 1 Nr. 3 PatG | V1 nur der Verletzte, neun Monate · V2 Gebühr 200 EUR Nr. 313 600 GV PatKostG · V3 Entnahme ohne Einwilligung | Widerruf; Nachanmelderecht ein Monat § 7 Abs. 2 PatG (keine Wiedereinsetzung) | TS III/2021, TS II/2022 |
| Einstweilige Verfügung § 935 ZPO, § 940 ZPO | V1 Verfügungsanspruch § 139 Abs. 1 PatG · V2 Verfügungsgrund: Dringlichkeit, gesicherter Rechtsbestand · V3 Glaubhaftmachung § 920 Abs. 2 ZPO, § 294 ZPO | Unterlassungsverfügung | TS I/2022 (TS II/2019: Androhung) |
| Berechtigungsanfrage statt Schutzrechtsverwarnung (§ 823 Abs. 1 BGB, § 256 Abs. 1 ZPO) | V1 kein Unterlassungsverlangen · V2 kein Haftungsrisiko · V3 Information über Gegenrechte · V4 Kenntnis für § 139 Abs. 2 PatG, § 33 Abs. 1 PatG | keine Haftung aus § 823 Abs. 1 BGB | TS III/2021 |
| Rücknahme der Anmeldung in der Anhörung (§ 46 Abs. 2 PatG) | V1 Erklärung gegenüber dem DPMA, formfrei · V2 Niederschrift § 46 Abs. 2 PatG i.V.m. § 162 ZPO · V3 Vertretungsmacht · V4 unbedingt, unwiderruflich | Anmeldung erledigt; keine Beschwerde, keine Teilung; Abzweigung § 5 Abs. 1 S. 3 GebrMG | TS III/2023 |

### Definitionen

| Begriff | Definition | Quelle |
|---|---|---|
| Anmeldetag | Tag des Eingangs von Name, Erteilungsantrag und Angaben, die dem Anschein nach Beschreibung sind, beim DPMA oder PIZ | § 35 Abs. 1 PatG (Legaldefinition) |
| Ausführbare Offenbarung | Fachmann kann die Erfindung mit Fachwissen und Fachkönnen erfolgreich ausführen; ein gangbarer Weg genügt | § 34 Abs. 4 PatG; BGH Klammernahtgerät, BGH Taxol |
| Einheitlichkeit | eine Erfindung oder Gruppe mit einer einzigen allgemeinen erfinderischen Idee | § 34 Abs. 5 PatG |
| Zusammenfassung | dient ausschließlich der technischen Unterrichtung | § 36 Abs. 2 PatG |
| Rücknahmefiktion | kraft Gesetzes eintretender Wegfall ohne Beschluss | § 35a Abs. 1 S. 2 PatG, § 58 Abs. 3 PatG, § 6 Abs. 2 PatKostG |
| Zahlungstag | Gutschrift, Bareinzahlung, Eingang des SEPA-Mandats | § 2 PatKostZV |
| Unzulässige Erweiterung | Gegenstand geht über das hinaus, was der Fachmann den ursprünglichen Unterlagen unmittelbar und eindeutig als zur Erfindung gehörend entnimmt | § 38 S. 1 PatG; BGH Hubgliedertor I, BGH Fälschungssicheres Dokument |
| Zwischenverallgemeinerung | Aufnahme eines Merkmals ohne die mit ihm offenbarten Merkmale; zulässig nur, wenn die Kombination als Ausgestaltung offenbart ist | EPA-Praxis; BGH Schleifprodukt |
| Uneigentliche Erweiterung | nicht offenbartes, nur beschränkendes Merkmal bleibt im Anspruch, zählt aber nicht für die Patentfähigkeit | BGH Winkelmesseinrichtung |
| Teilung | einseitige schriftliche Erklärung, mit der aus der anhängigen Anmeldung eine selbständige Teilanmeldung abgetrennt wird | § 39 Abs. 1 S. 1, 2 PatG |
| Teilanmeldung | eigenständiger Verfahrensgegenstand mit Zeitrang der Stammanmeldung, im Verfahrensstand der Stammanmeldung fortgeführt | § 39 Abs. 1 S. 4 PatG; BPatG 20 W (pat) 28/09 |
| Dieselbe Erfindung (Priorität) | Gegenstand des Anspruchs ist der Voranmeldung als Ganzes unmittelbar und eindeutig zu entnehmen; Gesamtheit der Merkmale deutlich offenbart | § 40 Abs. 3 PatG; EPA G 2/98; BGH UV-unempfindliche Druckplatte |
| Vorschriftsmäßige Hinterlegung | jede Hinterlegung, die zur Festlegung des Anmeldetags genügt, ohne Rücksicht auf das spätere Schicksal | Art. 4 A Abs. 3 PVÜ, Art. 87 Abs. 3 EPÜ |
| Teilpriorität | Priorität für die in der Voranmeldung offenbarten Alternativen eines generischen Anspruchs | EPA G 1/15 |
| Kettenpriorität | Voranmeldung beansprucht selbst eine Priorität; keine innere Priorität | § 40 Abs. 1 Hs. 2 PatG |
| Wiedereinsetzung | Beseitigung der Folgen einer schuldlos versäumten gesetzlichen Frist auf Antrag | § 123 Abs. 1 S. 1 PatG |
| Verschulden | Außerachtlassen der im Verkehr erforderlichen Sorgfalt; jede Fahrlässigkeit schadet | § 276 Abs. 2 BGB |
| Wegfall des Hindernisses | Kenntnis oder fahrlässige Unkenntnis der Säumnis beim Säumigen oder Vertreter | Rechtsprechung zu § 123 Abs. 2 PatG |
| Glaubhaftmachung | alle Beweismittel einschließlich eidesstattlicher Versicherung, überwiegende Wahrscheinlichkeit | § 294 Abs. 1 ZPO |
| Weiterbehandlung | verschuldensunabhängiger Rechtsbehelf gegen die Zurückweisung nach Versäumung einer Amtsfrist | § 123a Abs. 1 PatG |
| Anbieten | Bereitstellen des Erzeugnisses zum Erwerb; Werbeprospekt genügt | § 9 S. 2 Nr. 1 PatG; BGH Kupplung für optische Geräte |
| Wesentliches Element | Merkmal, das zur Verwirklichung der geschützten Lehre beiträgt | § 10 Abs. 1 PatG; BGH Pipettensystem |
| Äquivalenz | Gleichwirkung, Auffindbarkeit ohne erfinderisches Bemühen, Orientierung am Sinngehalt des Anspruchs | § 14 PatG; BGH Schneidmesser I |
| Wiederholungsgefahr | ernsthafte Besorgnis weiterer Verletzungen, durch die begangene Verletzung indiziert | § 139 Abs. 1 S. 1 PatG; Rechtsprechung |
| Erstbegehungsgefahr | ernsthafte und greifbare Anhaltspunkte für eine bevorstehende Verletzung | § 139 Abs. 1 S. 2 PatG; Rechtsprechung |
| Erfindungsbesitz | Lehre objektiv fertig und subjektiv als ausführbar erkannt | § 12 Abs. 1 PatG; BGH Desmopressin |
| Erschöpfung | Rechte am konkreten, mit Zustimmung im EWR in Verkehr gebrachten Erzeugnis verbraucht; nicht bei Neuherstellung | ungeschriebener Grundsatz; BGH Scheibenbremse II |
| Schutzrechtsverwarnung | ernsthaftes und endgültiges Unterlassungsverlangen (anders: Berechtigungsanfrage) | Rechtsprechung |
| Recht auf das Patent | Recht des Erfinders oder Rechtsnachfolgers | § 6 S. 1 PatG |
| Miterfinder | wer einen schöpferischen Beitrag zur Erfindung geleistet hat | BGH Verkranzungsverfahren, BGH Atemgasdrucksteuerung |
| Bruchteilsgemeinschaft | Rechtsverhältnis der Miterfinder ohne abweichende Vereinbarung | §§ 741 ff. BGB; BGH Rollenantriebseinheit |
| Doppelerfindung | unabhängig voneinander gemacht; Recht des Erstanmelders | § 6 S. 3 PatG |
| Widerrechtliche Entnahme | wesentlicher Inhalt des Patents den Unterlagen oder dem Verfahren eines anderen ohne Einwilligung entnommen | § 21 Abs. 1 Nr. 3 PatG (Legaldefinition) |
| Diensterfindung | während des Arbeitsverhältnisses, aus der obliegenden Tätigkeit oder maßgeblich auf Erfahrungen des Betriebs beruhend | § 4 Abs. 2 ArbnErfG |

### Fristen

| Frist | Norm | Berechnung | Verschiebung | Gebühr |
|---|---|---|---|---|
| Übersetzung: drei Monate; Englisch/Französisch zwölf Monate, höchstens 15 ab Prioritätstag | § 35a Abs. 1 S. 1, Abs. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB (Feiertag am Erklärungsort) | – |
| Fehlende Zeichnungen/Beschreibungsteile: ein Monat nach Aufforderung | § 35 Abs. 2, 3 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Anmelde- und Recherchegebühr: drei Monate ab Fälligkeit (Einreichung) | § 3 Abs. 1 S. 1 PatKostG, § 6 Abs. 1 S. 2 PatKostG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB; Zahlungstag § 2 PatKostZV | § 193 BGB | 40 EUR bis zehn Ansprüche, je weiterer 20 EUR, Papier 1,5fach (Nr. 311 000, 311 050, 311 100 GV PatKostG); Recherche 300 EUR (Nr. 311 200) |
| Zusammenfassung: 15 Monate ab Anmelde-/Prioritätstag | § 36 Abs. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Erfinderbenennung: 15 Monate ab Anmelde-/Prioritätstag | § 37 Abs. 1 S. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Prüfungsantrag: sieben Jahre nach Einreichung; Gebühr drei Monate ab Fälligkeit, spätestens sieben Jahre | § 44 Abs. 2 S. 1–3 PatG; Folge § 58 Abs. 3 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 350 EUR, nach Rechercheantrag 150 EUR (Nr. 311 400, 311 300 GV PatKostG) |
| Teilung: Unterlagen und Gebühren drei Monate nach Eingang der Teilungserklärung | § 39 Abs. 3 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Gebühren der Stammanmeldung bis zur Teilung (§ 39 Abs. 2 PatG) |
| Teilung nach Beschluss: bis Ablauf der Beschwerdefrist (ein Monat nach Zustellung) | § 39 Abs. 1 S. 1 PatG, § 73 Abs. 2 S. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Priorität: zwölf Monate | § 40 Abs. 1 PatG; Art. 4 C Abs. 1 PVÜ; Art. 87 Abs. 1 EPÜ | Art. 4 C Abs. 2 PVÜ, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB (EPA R. 131 Abs. 2, 4 EPÜ) | Art. 4 C Abs. 3 PVÜ, § 193 BGB (EPA R. 134 Abs. 1 EPÜ) | – |
| Erklärung innere Priorität: zwei Monate nach AT der Nachanmeldung | § 40 Abs. 4 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Angaben Auslandspriorität: bis Ablauf des 16. Monats nach Prioritätstag | § 41 Abs. 1 S. 1 PatG | § 188 Abs. 2 BGB | § 193 BGB | – |
| Nationale Phase PCT: 31 Monate ab Anmelde-/Prioritätstag | Art. III § 4 Abs. 2 S. 1 IntPatÜG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Anmeldegebühr PCT 60 EUR bis zehn Ansprüche, je weiterer 30 EUR (Nr. 311 150, 311 160 GV PatKostG) |
| Wiedereinsetzung: zwei Monate nach Wegfall des Hindernisses, Ausschlussfrist ein Jahr nach Ablauf der versäumten Frist | § 123 Abs. 2 S. 1, 4 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine Gebühr im GV PatKostG |
| Weiterbehandlung: ein Monat nach Zustellung der Zurückweisung | § 123a Abs. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 100 EUR (Nr. 313 000 GV PatKostG), § 6 Abs. 1 S. 1 PatKostG |
| Jahresgebühr: fällig letzter Tag des Anmeldemonats; zahlbar bis Ablauf des zweiten Monats, mit Zuschlag bis Ablauf des sechsten Monats | § 3 Abs. 2 S. 1 PatKostG, § 7 Abs. 1 PatKostG; Folge § 58 Abs. 3 PatG, § 20 Abs. 1 Nr. 2 PatG | § 188 Abs. 2 BGB | § 193 BGB | z. B. 3. Jahr 70 EUR, Zuschlag 50 EUR (Nr. 312 030, 312 032 GV PatKostG) |
| Vindikation: zwei Jahre nach Veröffentlichung der Erteilung; ein Jahr nach Abschluss des Entnahme-Einspruchs; bösgläubig unbefristet | § 8 S. 3–5 PatG; EP: Art. II § 5 Abs. 2 IntPatÜG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Gerichtskosten nach GKG |
| Nachanmeldung nach Entnahme-Widerruf: ein Monat nach amtlicher Mitteilung | § 7 Abs. 2 PatG (keine Wiedereinsetzung § 123 Abs. 1 S. 2 Nr. 3 PatG) | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Anmeldegebühr wie oben |
| Einspruch wegen Entnahme: neun Monate nach Veröffentlichung der Erteilung | § 59 Abs. 1 S. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 200 EUR (Nr. 313 600 GV PatKostG) |
| Entschädigung: Verjährung frühestens ein Jahr nach Erteilung | § 33 Abs. 3 S. 1 PatG, § 195 BGB, § 199 Abs. 1 BGB | § 199 Abs. 1 BGB (Jahresende) | – | – |
| Verletzungsansprüche: drei Jahre ab Jahresende der Entstehung und Kenntnis | § 141 S. 1 PatG, § 195 BGB, § 199 Abs. 1 BGB | § 199 Abs. 1 BGB | – | – |
| Gebrauchsmusterabzweigung: bis zwei Monate nach Ende des Monats der Erledigung, höchstens zehn Jahre | § 5 Abs. 1 S. 3 GebrMG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |

### Weitere Hilfsnormen

- Gehör vor Zurückweisung: § 42 Abs. 3 S. 2 PatG (über § 48 S. 2 PatG); Anhörung § 46 Abs. 1 S. 3–5 PatG; Niederschrift § 46 Abs. 2 PatG i.V.m. § 162 ZPO.
- Erteilungsbeschluss aussetzen: § 49 Abs. 2 PatG (bis 15 Monate). Wirkung: § 58 Abs. 1 S. 3 PatG; Wegfall der Entschädigung § 58 Abs. 2 PatG.
- Verfahrenssprache deutsch: § 126 PatG; elektronische Schriftform: § 125a Abs. 1 PatG i.V.m. § 130a ZPO.
- Gebühren: Fälligkeit § 3 Abs. 1 PatKostG, Bearbeitung erst nach Zahlung § 5 Abs. 1 PatKostG, Wegfall/Erstattung § 10 Abs. 2 PatKostG.
- Akteneinsicht in die Voranmeldung bei innerer Priorität: § 40 Abs. 6 PatG, § 31 Abs. 2 S. 1 Nr. 2 PatG.
- Weiterbenutzungsrecht nach Wiedereinsetzung: § 123 Abs. 5 bis 7 PatG.
- Aussetzung des Verletzungsprozesses: § 148 Abs. 1 ZPO; Abmahnung und Kosten § 93 ZPO; negative Feststellungsklage § 256 Abs. 1 ZPO.
- Mitberechtigte: § 744 Abs. 2 BGB (Erhaltungsmaßnahmen), § 747 S. 1 BGB (Verfügung über den Anteil); Vertreterverschulden § 85 Abs. 2 ZPO.
- Arbeitnehmererfindung als Rechtsnachfolge: § 6 ArbnErfG, § 7 Abs. 1 ArbnErfG; Zuständigkeit § 39 Abs. 1 ArbnErfG.

## Gebrauchsmuster

GebrMG in der Fassung nach dem 2. PatModG (2021); Gebühren nach der Anlage zu § 2 Abs. 1 PatKostG. Kurs: p06 „Anspruchsgrundlagen Gebrauchsmuster“.

### Anspruchsgrundlagen und Rechtsbehelfe

| AGL | Normenkette (V1 … Vn mit Norm) | Rechtsfolge | Klausuren |
|---|---|---|---|
| Abzweigung (§ 5 Abs. 1 S. 1 GebrMG) | V1 frühere Patentanmeldung mit Wirkung für DE (DE, EP mit Benennung DE Art. 66 EPÜ, PCT mit Bestimmung DE Art. 11 Abs. 3 PCT) · V2 derselbe Anmelder oder Rechtsnachfolger (nicht der Entnahme-Verletzte ohne Rechtsübergang, BGH Angussvorrichtung für Spritzgießwerkzeuge II) · V3 dieselbe Erfindung (Erweiterung: keine Rechte, BGH Momentanpol; § 15 Abs. 1 Nr. 3 GebrMG) · V4 Erklärung mit der GebrM-Anmeldung, Angaben und Abschrift auf Aufforderung (§ 5 Abs. 2 GebrMG) · V5 Frist § 5 Abs. 1 S. 3 GebrMG · V6 Anmeldeerfordernisse § 4, § 4a, § 4b GebrMG, kein Verfahren § 2 Nr. 3 GebrMG, Gebühr Nr. 321 000 Anlage PatKostG | Anmeldetag der Patentanmeldung, deren Priorität bleibt (§ 5 Abs. 1 S. 2 GebrMG); Schutzdauer ab diesem Anmeldetag (§ 23 Abs. 1 GebrMG); Wirkung erst ab Eintragung (§ 11 Abs. 1 GebrMG); verspätet: kein Anmeldetag, Zurückweisung (BGH Sintervorrichtung) | TS II/2018, TS II/2019, TS III/2019, TS II/2020, TS I/2021, TS III/2021, TS I/2022, TS II/2022, TS III/2022, TS II/2023, TS III/2023 |
| Schutzfähigkeit (§ 1 Abs. 1 GebrMG; Vorfrage zu § 8, § 13 Abs. 1, § 15 Abs. 1 Nr. 1 GebrMG) | V1 Erfindung, kein Ausschluss als solcher (§ 1 Abs. 2, 3 GebrMG) · V2 kein Ausschluss § 2 Nr. 1 bis 3 GebrMG (Verfahren), biotechnologische Erfindungen § 1 Abs. 2 Nr. 5 GebrMG · V3 Zeitrangtag (§ 4a, § 5, § 6, § 6a GebrMG) · V4 SdT: schriftliche Beschreibung weltweit, Benutzung im Inland (§ 3 Abs. 1 S. 2 GebrMG) · V5 keine Schonfrist (§ 3 Abs. 1 S. 3 GebrMG) · V6 nicht neuheitsschädlich offenbart · V7 erfinderischer Schritt (§ 1 Abs. 1 GebrMG; BGH Demonstrationsschrank) · V8 gewerbliche Anwendbarkeit (§ 3 Abs. 2 GebrMG) | schutzfähig; sonst Löschungsanspruch und kein Schutz (§ 13 Abs. 1 GebrMG); V1/V2 schon bei Eintragung geprüft (BGH Feldmausbekämpfung) | TS II/2018, TS II/2020, TS I/2021, TS III/2021, TS I/2022, TS II/2022, TS III/2022, TS III/2023 (TS II/2019) |
| Löschungsantrag (§ 15 Abs. 1 GebrMG i.V.m. § 16 GebrMG) | A Zulässigkeit: V1 eingetragenes GBM (nach Erlöschen Feststellung mit besonderem Rechtsschutzinteresse) · V2 jedermann, bei Entnahme nur der Verletzte (§ 15 Abs. 2 GebrMG) · V3 schriftlich beim DPMA mit Tatsachen (§ 16 S. 1, 2 GebrMG), § 81 Abs. 6 PatG, § 125 PatG (§ 16 S. 3 GebrMG) · V4 Gebühr 300 EUR je Antragsteller (Nr. 323 100 Anlage PatKostG) · B Begründetheit: V5 Löschungsgrund § 15 Abs. 1 Nr. 1 GebrMG (§§ 1 bis 3 GebrMG), Nr. 2 (Doppelschutz, BGH Formkörper mit Durchtrittsöffnungen), Nr. 3 (Erweiterung, BGH Tintenstrahldrucker) GebrMG; § 15 Abs. 2 GebrMG mit § 13 Abs. 2 GebrMG · C Verfahren: V6 Widerspruch binnen eines Monats (§ 17 Abs. 1 GebrMG) | Löschung, Teillöschung auch durch Änderung der Schutzansprüche (§ 15 Abs. 3 GebrMG; BGH Tischgrill); ohne Widerspruch Löschung ohne Sachprüfung (§ 17 Abs. 1 S. 2 GebrMG); Beschluss der Gebrauchsmusterabteilung (§ 17 Abs. 3 GebrMG, § 10 Abs. 3 GebrMG) | TS II/2019, TS I/2021, TS III/2021, TS III/2022, TS III/2023 (TS II/2022, TS II/2023) |
| Kosten des Löschungsverfahrens (§ 17 Abs. 4 GebrMG) | V1 Beschluss nach § 17 Abs. 3 S. 1 GebrMG oder Kostenantrag binnen eines Monats (§ 17 Abs. 4 S. 2, 3 GebrMG) · V2 Maßstab § 84 Abs. 2 S. 2 PatG mit § 91 ZPO · V3 § 93 ZPO: Nichtwiderspruch = sofortiges Anerkenntnis (BGH Dynamisches Mikrofon), aber Veranlassung durch Verwarnung oder Schweigen auf Verzichtsaufforderung (BGH Druckdatenübertragungsverfahren) · V4 erstattungsfähig § 62 Abs. 2 PatG | Kostenquote; ohne Entscheidung trägt jeder seine Kosten (§ 17 Abs. 4 S. 5 GebrMG) | TS II/2019 |
| Innere Priorität (§ 6 Abs. 1 GebrMG i.V.m. § 40 PatG) | V1 frühere Patent- oder GebrM-Anmeldung beim DPMA · V2 keine Kettenpriorität · V3 dieselbe Erfindung, deutlich offenbart (§ 40 Abs. 3 PatG) · V4 zwölf Monate (§ 6 Abs. 1 S. 1 GebrMG) · V5 Erklärung binnen zwei Monaten mit Aktenzeichen (§ 40 Abs. 4 PatG) | Zeitrang des Prioritätstags; frühere Patentanmeldung gilt nicht als zurückgenommen (§ 6 Abs. 1 S. 2 GebrMG), frühere anhängige GebrM-Anmeldung schon (§ 40 Abs. 5 S. 1 PatG); Schutzdauer ab eigenem Anmeldetag | TS II/2018, TS I/2021, TS III/2021 (TS III/2022: Patent mit Priorität aus GBM, § 40 Abs. 5 S. 2 PatG) |
| Verletzungsansprüche (§ 24 Abs. 1, 2 GebrMG, § 24a, § 24b GebrMG) | V1 eingetragenes GBM in Kraft (§ 11 Abs. 1 GebrMG, § 23 GebrMG) · V2 Verletzter (Inhaber, ausschließlicher Lizenznehmer § 22 Abs. 2 GebrMG) · V3 Benutzung (§ 11 Abs. 1 S. 2, Abs. 2 GebrMG; Schutzbereich § 12a GebrMG) · V4 Schutzfähigkeit als Einwand (§ 13 Abs. 1 GebrMG) · V5 keine Schranke (§ 12 GebrMG), kein Vorbenutzungsrecht (§ 13 Abs. 3 GebrMG i.V.m. § 12 PatG) · V6a Wiederholungs-/Erstbegehungsgefahr, Verhältnismäßigkeit (§ 24 Abs. 1 S. 1 bis 3 GebrMG) · V6b Verschulden (§ 24 Abs. 2 GebrMG) | Unterlassung, Schadensersatz (drei Berechnungsarten), Vernichtung/Rückruf, Auskunft; LG ausschließlich (§ 27 Abs. 1 GebrMG); Aussetzung § 19 GebrMG | TS I/2022 (TS III/2021; RP1 III/2021) |
| Aussetzung des Verletzungsstreits (§ 19 GebrMG) | V1 Löschungsverfahren anhängig · V2 Rechtsstreit hängt vom Bestehen des Schutzes ab · V3 Ermessen (S. 1), zwingend bei für unwirksam gehaltener Eintragung (S. 2) | Aussetzung; Bindung an Zurückweisung nur zwischen denselben Parteien (§ 19 S. 3 GebrMG) | TS III/2021, TS I/2022 (RP1 III/2021) |
| Eintragung (§ 8 Abs. 1 GebrMG) | V1 Anmeldung beim DPMA (§ 4 Abs. 1 GebrMG) · V2 Anmeldetag (§ 4a GebrMG) · V3 Inhalt (§ 4 Abs. 3 GebrMG) · V4 Übersetzung (§ 4b GebrMG) · V5 Gebühr (Nr. 321 000/321 100 Anlage PatKostG) · V6 kein Schutzhindernis § 2 GebrMG | Eintragung ohne Sachprüfung (§ 8 Abs. 1 S. 2 GebrMG); Aussetzung bis 15 Monate (§ 8 Abs. 1 S. 3 GebrMG i.V.m. § 49 Abs. 2 PatG) | TS II/2019, TS I/2021, TS III/2023 (RP1 III/2021) |
| Schutzdauer und Aufrechterhaltung (§ 23 GebrMG) | V1 Anmeldetag (auch abgezweigt) · V2 Aufrechterhaltungsgebühren 4.–6., 7./8., 9./10. Jahr (§ 23 Abs. 2 GebrMG), Fälligkeit § 3 Abs. 2 PatKostG, Zahlung § 7 Abs. 1 PatKostG | Ende zehn Jahre nach Ablauf des Anmeldemonats (§ 23 Abs. 1 GebrMG); Erlöschen § 23 Abs. 3 GebrMG | TS II/2018, TS II/2019, TS II/2020, TS I/2021, TS III/2021, TS I/2022, TS II/2022 |
| Beschwerde (§ 18 Abs. 1 GebrMG) | V1 Beschluss der Gebrauchsmusterstelle oder -abteilung · V2 ein Monat (§ 18 Abs. 2 S. 1 GebrMG i.V.m. § 73 Abs. 2 PatG) · V3 Gebühr 500 EUR (Löschung, Nr. 401 100) bzw. 200 EUR (Nr. 401 300 Anlage PatKostG) in der Frist | Entscheidung des Gebrauchsmuster-Beschwerdesenats; Kosten § 84 Abs. 2 PatG (§ 18 Abs. 2 S. 2 GebrMG); Rechtsbeschwerde nur bei Zulassung (§ 18 Abs. 4 GebrMG) | (TS II/2019) |
| Ausstellungspriorität (§ 6a GebrMG) | V1 bekanntgemachte Ausstellung (§ 6a Abs. 1 bis 3 GebrMG) · V2 Anmeldung binnen sechs Monaten · V3 Angaben und Nachweis vor Ablauf des 16. Monats (§ 6a Abs. 4 GebrMG) | Priorität ab Zurschaustellung; keine Verlängerung der Frist des § 6 Abs. 1 GebrMG (§ 6a Abs. 5 GebrMG) | – |
| Unionspriorität (§ 6 Abs. 2 GebrMG i.V.m. § 41 PatG) | V1 erste Anmeldung in Verbandsstaat, auch Patent → GBM (Art. 4 E Abs. 2 PVÜ) · V2 zwölf Monate (Art. 4 C Abs. 1 PVÜ) · V3 Angaben bis Ablauf des 16. Monats (§ 41 Abs. 1 PatG) | Prioritätsrecht; sonst Verwirkung | (TS III/2023 für das Patent) |
| Gebrauchsmuster statt Patent beim Arbeitgeber (§ 13 Abs. 1 S. 2 ArbnErfG) | V1 gemeldete Diensterfindung · V2 Gebrauchsmusterschutz bei verständiger Würdigung der Verwertbarkeit zweckdienlicher | Anmeldung als Gebrauchsmuster, unverzüglich (§ 13 Abs. 1 S. 3 ArbnErfG) | (RP2 I/2021) |

### Definitionen

| Begriff | Definition | Quelle |
|---|---|---|
| Neu | nicht zum Stand der Technik gehörend | § 3 Abs. 1 S. 1 GebrMG (Legaldefinition) |
| Stand der Technik | alle Kenntnisse, die vor dem für den Zeitrang maßgeblichen Tag durch schriftliche Beschreibung oder durch eine im Inland erfolgte Benutzung der Öffentlichkeit zugänglich gemacht worden sind | § 3 Abs. 1 S. 2 GebrMG (Legaldefinition) |
| Schriftliche Beschreibung | jede verkörperte, reproduzierbare Wiedergabe der Lehre (Druckschrift, Prospekt, Internetseite), gleich wo veröffentlicht | Lehre |
| Neuheitsschonfrist | Beschreibung oder Benutzung binnen sechs Monaten vor dem Zeitrangtag bleibt außer Betracht, wenn sie auf der Ausarbeitung des Anmelders oder seines Rechtsvorgängers beruht; lückenlose Kette der Wissensvermittlung, Anscheinsbeweis möglich | § 3 Abs. 1 S. 3 GebrMG; BPatG Tür- und Fenstersensor (35 W (pat) 424/22) |
| Öffentlich zugänglich (Import) | bei äußerlich nicht erkennbarer Lehre eines importierten Erzeugnisses erst ab Angebot an Endkunden | BPatG Toilettendeckel aus Schichtverbundstoff (35 W (pat) 402/23) |
| Gewerblich anwendbar | auf irgendeinem gewerblichen Gebiet einschließlich der Landwirtschaft herstellbar oder benutzbar | § 3 Abs. 2 GebrMG (Legaldefinition) |
| Erfindung | Lehre zum planmäßigen Handeln unter Einsatz beherrschbarer Naturkräfte zur Erreichung eines kausal übersehbaren Erfolgs | Rechtsprechung zu § 1 PatG |
| Erfinderischer Schritt | qualitatives Kriterium, Ergebnis einer Wertung wie die erfinderische Tätigkeit, gegenüber dem SdT nach § 3 GebrMG | BGH Demonstrationsschrank (X ZB 27/05) |
| Verfahren (§ 2 Nr. 3 GebrMG) | Arbeits- oder Herstellungsverfahren; nicht: Erzeugnis ohne körperliches Substrat (Signalfolge), Verwendungsanspruch mit Sacheigenschaften | BGH Signalfolge (X ZB 9/03); BPatG Lithiumsilikat-Glaskeramik (35 W (pat) 412/16) |
| Abzweigung | Inanspruchnahme des Anmeldetags einer früheren Patentanmeldung mit Wirkung für DE durch Erklärung in der GebrM-Anmeldung | § 5 Abs. 1 S. 1 GebrMG |
| Erledigt (§ 5 Abs. 1 S. 3 GebrMG) | Patentanmeldung nicht mehr anhängig: rechtskräftige Zurückweisung, Rücknahme, Rücknahmefiktion, Erteilung | Lehre; TS III/2023 |
| Innere Priorität | Zeitrang einer früheren DPMA-Anmeldung derselben Erfindung binnen zwölf Monaten | § 6 Abs. 1 S. 1 GebrMG |
| Bereits geschützt (§ 15 Abs. 1 Nr. 2 GebrMG) | Identität der Gegenstände (gleicher Schutzbereich) und entstandener Schutz aus der früheren Anmeldung; mögliche spätere Nichtigerklärung unbeachtlich | BGH Formkörper mit Durchtrittsöffnungen (X ZA 1/11) |
| Unzulässige Erweiterung (§ 15 Abs. 1 Nr. 3 GebrMG) | Gegenstand geht über die ursprünglich eingereichte Fassung hinaus; nicht offenbartes, nur beschränkendes Merkmal ohne Aliud führt nicht zur Löschung | BGH Tintenstrahldrucker (X ZB 2/12) |
| Widerrechtliche Entnahme | wesentlicher Inhalt der Eintragung den Beschreibungen, Zeichnungen, Modellen, Gerätschaften oder Einrichtungen eines anderen ohne dessen Einwilligung entnommen | § 13 Abs. 2 GebrMG (Legaldefinition) |
| Veranlassung zum Antrag (§ 93 ZPO) | Verhalten des Inhabers, das den Antragsteller annehmen lässt, ohne Verfahren nicht zum Ziel zu kommen (Verwarnung, Schweigen auf Verzichtsaufforderung) | BGH Druckdatenübertragungsverfahren (X ZR 73/12); BGH Dynamisches Mikrofon (X ZR 26/00) |
| Schutzbereich | bestimmt durch den Inhalt der Schutzansprüche; Beschreibung und Zeichnungen zur Auslegung | § 12a GebrMG |
| Anbieten | Handlung, die das Erzeugnis der Nachfrage zum Erwerb äußerlich wahrnehmbar zugänglich macht | BGH Kunststoffbügel (X ZR 169/04) |
| Fahrlässigkeit | Außerachtlassen der im Verkehr erforderlichen Sorgfalt | § 276 Abs. 2 BGB (Legaldefinition) |
| Anmeldetag | Eingang von Name, Eintragungsantrag und dem Anschein nach Beschreibung beim DPMA | § 4a Abs. 1 GebrMG (Legaldefinition) |
| Schutzdauer | Anmeldetag bis zehn Jahre nach Ablauf des Anmeldemonats | § 23 Abs. 1 GebrMG |

### Fristen

| Frist | Norm | Berechnung | Verschiebung | Gebühr |
|---|---|---|---|---|
| Abzweigung: zwei Monate nach Ende des Monats der Erledigung bzw. des Abschlusses des Einspruchs, längstens Ablauf des 10. Jahres | § 5 Abs. 1 S. 3 GebrMG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Anmeldegebühr 30 EUR elektronisch / 40 EUR Papier (Nr. 321 000, Nr. 321 100 Anlage PatKostG), fällig § 3 Abs. 1 S. 1 PatKostG, binnen drei Monaten § 6 Abs. 1 S. 2 PatKostG, sonst § 6 Abs. 2 PatKostG |
| Angaben und Abschrift zur Abzweigung: zwei Monate nach Zustellung der Aufforderung | § 5 Abs. 2 S. 1 GebrMG (Folge Verwirkung S. 3) | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB; Zustellung § 21 Abs. 1 GebrMG i.V.m. § 127 PatG | § 193 BGB | – |
| Übersetzung: drei Monate nach Einreichung | § 4b GebrMG (Rücknahmefiktion S. 2) | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Fehlende Zeichnungen/Teile: ein Monat nach Zustellung der Aufforderung | § 4a Abs. 2, 3 GebrMG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Innere Priorität: zwölf Monate ab Anmeldetag der früheren Anmeldung; Erklärung zwei Monate ab Anmeldetag der späteren | § 6 Abs. 1 S. 1 GebrMG; § 6 Abs. 1 S. 2 GebrMG i.V.m. § 40 Abs. 4 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB; keine Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 3 PatG) | – |
| Unionspriorität: zwölf Monate; Angaben bis Ablauf des 16. Monats nach dem Prioritätstag | Art. 4 C Abs. 1 PVÜ; § 6 Abs. 2 GebrMG i.V.m. § 41 Abs. 1 PatG | Art. 4 C Abs. 2 PVÜ | Art. 4 C Abs. 3 PVÜ | – |
| Ausstellungspriorität: Anmeldung sechs Monate seit Zurschaustellung; Angaben vor Ablauf des 16. Monats | § 6a Abs. 1, 4 GebrMG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Neuheitsschonfrist: sechs Monate vor dem Zeitrangtag | § 3 Abs. 1 S. 3 GebrMG | rückwärts, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB entsprechend | – | – |
| Widerspruch gegen Löschungsantrag: ein Monat nach Zustellung der Mitteilung | § 17 Abs. 1 S. 1 GebrMG (Folge Löschung S. 2) | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Löschungsantrag: keine Frist | § 15 GebrMG, § 16 GebrMG | – | – | 300 EUR je Antragsteller (Nr. 323 100 Anlage PatKostG, Vorbemerkung Teil A Abs. 2), binnen drei Monaten ab Fälligkeit (§ 3 Abs. 1 S. 1, § 6 Abs. 1 S. 2 PatKostG), sonst Rücknahmefiktion (§ 6 Abs. 2 PatKostG) |
| Kostenantrag ohne Hauptsacheentscheidung: ein Monat nach Zustellung der Beendigungsmitteilung | § 17 Abs. 4 S. 3 GebrMG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Beschwerde: ein Monat nach Zustellung | § 18 Abs. 2 S. 1 GebrMG i.V.m. § 73 Abs. 2 S. 1 PatG | § 99 Abs. 1 PatG, § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | 500 EUR Löschungssachen (Nr. 401 100), sonst 200 EUR (Nr. 401 300 Anlage PatKostG), in der Frist (§ 6 Abs. 1 S. 1 PatKostG), sonst nicht eingelegt (§ 6 Abs. 2 PatKostG) |
| Aufrechterhaltungsgebühr: fällig letzter Tag des Anmeldemonats vor dem 4., 7., 9. Jahr (bei späterer Eintragung: Ende des Eintragungsmonats); zahlbar zwei Monate, mit Zuschlag sechs Monate | § 23 Abs. 2 GebrMG; § 3 Abs. 2 S. 1, 2 PatKostG; § 7 Abs. 1 PatKostG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 210 / 350 / 530 EUR (Nr. 322 100, 322 200, 322 300 Anlage PatKostG), Zuschlag 50 EUR; sonst Erlöschen § 23 Abs. 3 Nr. 2 GebrMG |
| Aussetzung der Eintragung: bis 15 Monate ab Anmelde- oder Prioritätstag | § 8 Abs. 1 S. 3 GebrMG i.V.m. § 49 Abs. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | – | – |
| Weiterbehandlung: ein Monat nach Zustellung der Zurückweisung | § 21 Abs. 1 GebrMG i.V.m. § 123a Abs. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 100 EUR (Nr. 323 000 Anlage PatKostG), in der Frist (§ 6 Abs. 1 S. 1 PatKostG) |
| Wiedereinsetzung: zwei Monate nach Wegfall des Hindernisses, höchstens ein Jahr | § 21 Abs. 1 GebrMG i.V.m. § 123 Abs. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | – |
| Verjährung der Verletzungsansprüche: drei Jahre ab Jahresende der Kenntnis | § 24f GebrMG i.V.m. § 195 BGB, § 199 Abs. 1 BGB | § 199 Abs. 1 BGB | – | – |
| Schutzdauer: zehn Jahre nach Ablauf des Anmeldemonats | § 23 Abs. 1 GebrMG | Monatsende | keine (§ 193 BGB gilt nicht) | – |

### Weitere Hilfsnormen

- **Wirkung und Schranken:** § 11 GebrMG (unmittelbare und mittelbare Benutzung, nur Erzeugnisse), § 12 GebrMG (privat, Versuche, § 11 Nr. 4 bis 6 PatG), § 12a GebrMG (Schutzbereich), § 13 Abs. 3 GebrMG (§ 6, § 7 Abs. 1, § 8, § 12, § 13 PatG entsprechend), § 14 GebrMG (älteres GBM gegen jüngeres Patent), § 22 GebrMG (Übertragung, Lizenz).
- **Verfahren:** § 4 Abs. 5 GebrMG (Änderungen ohne Erweiterung bis zur Eintragungsverfügung), § 4 Abs. 6 GebrMG (Teilung jederzeit), § 7 GebrMG (Recherche, 250 EUR Nr. 321 200 Anlage PatKostG, jedermann, nur ein Antrag), § 10 GebrMG (Gebrauchsmusterstelle, Gebrauchsmusterabteilung), § 17 Abs. 2 GebrMG (Beweisaufnahme, mündliche Verhandlung auf Antrag), § 18 GebrMG (Beschwerde, Rechtsbeschwerde), § 21 GebrMG (Verweis auf § 123, § 123a, § 126, § 127 PatG; Verfahrenskostenhilfe §§ 129 bis 138 PatG), § 28 GebrMG (Inlandsvertreter).
- **Durchsetzung:** § 24c GebrMG (Vorlage, Besichtigung), § 24d GebrMG (Bank- und Handelsunterlagen), § 24e GebrMG (Urteilsbekanntmachung), § 24g GebrMG (andere Ansprüche), § 25 GebrMG (Strafbarkeit; Aussetzung nach § 25 Abs. 8 GebrMG), § 26 GebrMG (Streitwertbegünstigung), § 27 GebrMG (LG ausschließlich, Patentanwaltskosten), § 30 GebrMG (Auskunft bei Gebrauchsmusterberühmung).
- **Kosten:** § 62 Abs. 2 PatG (erstattungsfähige Kosten, Kostenfestsetzung), § 84 Abs. 2 PatG (ZPO-Kostenrecht mit Billigkeitsvorbehalt), § 91 ZPO, § 93 ZPO; Zahlungstag § 2 PatKostZV.
- **Verhältnis zum Patent:** § 3 Abs. 2 PatG gilt nicht (dafür § 15 Abs. 1 Nr. 2 GebrMG); § 40 Abs. 5 S. 2 PatG (GBM gilt bei Patent mit innerer Priorität nicht als zurückgenommen); § 13 Abs. 1 S. 2 ArbnErfG (GBM statt Patent bei Diensterfindungen).

## Marken

MarkenG in der Fassung 2026 (Unionsmarken §§ 119 bis 125a MarkenG), Gebühren nach der Anlage zu § 2 Abs. 1 PatKostG. Spalte
„Klausuren“: Klausur mit ausgearbeiteter Lösung (`klausuren/loesungen/ns/`) ohne Klammer, aus den Aufgabentexten erkennbare
weitere Klausuren in Klammern. Kurs dazu: `src/knowledge/kurse/k15_agl_marken.py` („Anspruchsgrundlagen Marken“).

### Anspruchsgrundlagen und Rechtsbehelfe

| AGL | Normenkette (V1 … Vn mit Norm) | Rechtsfolge | Klausuren |
|---|---|---|---|
| Widerspruch § 42 Abs. 1 S. 1, Abs. 2 MarkenG | V0 Gebühr 250 € + 50 € je weiteres Kennzeichen (Nr. 331 600, 331 610), in der Frist (§ 64a MarkenG, § 6 Abs. 1 S. 1, Abs. 2 PatKostG) · V1 Statthaftigkeit: eingetragene, veröffentlichte Marke (§ 42 Abs. 1, § 41 Abs. 2 MarkenG; IR § 114 MarkenG) · V2 Beteiligten-/Prozessfähigkeit (§ 7 MarkenG; § 50, § 51 ZPO) · V3 Inlandsvertreter (§ 96 Abs. 1 MarkenG) · V4 Widerspruchsberechtigung (§ 42 Abs. 1, § 6, § 28, § 119 Nr. 1, § 112 Abs. 1 MarkenG) · V5 Frist drei Monate (§ 42 Abs. 1 S. 1 MarkenG; § 114 Abs. 2 MarkenG) · V6 Form (§ 29, § 30 MarkenV; § 42 Abs. 3 MarkenG) · V7 Widerspruchsgrund § 42 Abs. 2 Nr. 1–5 MarkenG (§ 9 MarkenG, § 10 MarkenG, § 11 MarkenG, § 12 MarkenG mit § 4 Nr. 2 MarkenG/§ 5 MarkenG, § 13 MarkenG) · V8 Benutzung auf Einrede (§ 43 Abs. 1 MarkenG) | Löschung ganz/teilweise (§ 43 Abs. 2 S. 1 MarkenG), ex tunc (§ 43 Abs. 4, § 52 Abs. 2 MarkenG); sonst Zurückweisung (§ 43 Abs. 2 S. 2 MarkenG) | NS II/2019 (NS II/2018, III/2018, I/2019, III/2019, III/2020, II/2021, III/2021, I/2022, III/2022, II/2023; I/2024, I/2025, II/2025, III/2025) |
| Relative Schutzhindernisse § 9 Abs. 1 Nr. 1–3 MarkenG (im Widerspruch über § 42 Abs. 2 Nr. 1 MarkenG, in der Nichtigkeit über § 51 Abs. 1 MarkenG) | V1 ältere Marke (§ 9 Abs. 1, 2, § 6 Abs. 2, § 119 Nr. 1 MarkenG) · Nr. 1: Zeichen- und Warenidentität · Nr. 2: V2 Waren-/DL-Ähnlichkeit (§ 9 Abs. 3 MarkenG) · V3 Kennzeichnungskraft · V4 Zeichenähnlichkeit (Klang, Bild, Sinn; Prägung; selbständig kennzeichnende Stellung) · V5 Wechselwirkung · V6 gedankliches Inverbindungbringen (Serienzeichen) · Nr. 3: Bekanntheit (Union: § 119 Nr. 1 MarkenG), Verknüpfung, Ausnutzung/Beeinträchtigung, Unlauterkeit | Löschung (§ 43 Abs. 2 MarkenG) bzw. Nichtigkeit (§ 51 Abs. 1 MarkenG) | NS II/2019 (NS II/2018, III/2018, I/2019, III/2019, III/2020, II/2021, III/2021, I/2022, II/2023) |
| Einrede mangelnder Benutzung § 43 Abs. 1 MarkenG i.V.m. § 26 MarkenG | V1 Widerspruch aus eingetragener Marke · V2 Einrede eindeutig erhoben (jederzeit, auch vor dem BPatG) · V3 Schonfrist am Anmeldetag der jüngeren Marke abgelaufen (§ 43 Abs. 1 S. 1, § 26 Abs. 5 MarkenG; Unionsmarke § 119 Nr. 4 MarkenG, Art. 18 UMV; IR § 116 Abs. 1, § 115 Abs. 2 MarkenG) · V4 Zeitraum fünf Jahre vor Anmelde-/Prioritätstag (Altfälle § 158 Abs. 5 MarkenG) · V5 ernsthaft, als Marke, im Inland (§ 26 Abs. 1 MarkenG) · V6 Zustimmung (§ 26 Abs. 2 MarkenG) · V7 abweichende Form (§ 26 Abs. 3 MarkenG) · V8 berechtigte Gründe · V9 Nachweis, auch eidesstattliche Versicherung (§ 43 Abs. 1 S. 2 MarkenG) | nur benutzte Waren (§ 43 Abs. 1 S. 3 MarkenG); sonst Zurückweisung des Widerspruchs | NS II/2019 (NS II/2018, III/2018, I/2019, III/2019, II/2020, II/2021, III/2021, I/2022, II/2023; I/2024) |
| Beschwerde § 66 Abs. 1 S. 1 MarkenG | V0 Gebühr 200 € (Nr. 401 300), Verfall/Nichtigkeit 500 € (Nr. 401 100), in der Frist (§ 6 Abs. 1 S. 1, Abs. 2 PatKostG) · V1 Beschluss Markenstelle/-abteilung · V2 Beteiligter, Beschwer (§ 66 Abs. 1 S. 2 MarkenG) · V3 Fähigkeiten, Vertretung (§ 82 Abs. 1, § 81, § 96 MarkenG) · V4 schriftlich beim DPMA (§ 66 Abs. 2, § 95a MarkenG) · V5 ein Monat ab Zustellung (§ 66 Abs. 2, § 94 MarkenG) · Abhilfe nur einseitig (§ 66 Abs. 5 MarkenG) | Aufhebung, eigene Entscheidung oder Zurückverweisung (§ 70 Abs. 3 MarkenG); Verwerfung; Feststellung „gilt als nicht eingelegt“ | (NS III/2018, I/2019, III/2019, I/2020, III/2020, II/2021, I/2022, III/2022, II/2023, III/2023; III/2024, III/2025) |
| Nichtigkeit wegen absoluter Schutzhindernisse § 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 MarkenG | V0 Gebühr 400 € (Nr. 333 300; § 6 Abs. 1 S. 2 PatKostG) · V1 Antrag beim DPMA (§ 53 Abs. 1 MarkenG; keine Klage) · V2 jedermann (§ 53 Abs. 2 MarkenG) · V3 Form, Tatsachen, Beweismittel (§ 53 Abs. 1 S. 1, 2 MarkenG) · V4 keine Rechtskraft (§ 53 Abs. 1 S. 4 MarkenG) · V5 Frist nur für Nr. 1–3: zehn Jahre (§ 50 Abs. 2 S. 3 MarkenG); Amtsverfahren zwei Jahre (§ 50 Abs. 3 MarkenG) · V6 Eintragung entgegen § 3, § 7, § 8 MarkenG · V7 Fortbestehen (§ 50 Abs. 2 S. 1 MarkenG, nicht Nr. 14) · V8 keine Verkehrsdurchsetzung bis Antrag (§ 50 Abs. 2 S. 2 MarkenG) · Verfahren § 53 Abs. 4, 5 MarkenG | Nichtigerklärung, Löschung, ganz/teilweise (§ 50 Abs. 1, 4 MarkenG), ex tunc (§ 52 Abs. 2 MarkenG) | NS II/2019 (NS II/2018, I/2020, II/2020, I/2021; II/2025) |
| Nichtigkeit wegen älterer Rechte § 51 Abs. 1 MarkenG mit § 53 MarkenG (DPMA, seit 01.05.2020) oder § 55 MarkenG (LG) | V0 Gebühr 400 € + 100 € je weiteres Recht (Nr. 333 300, 333 350) · V1 Wahl DPMA/LG, kein Doppelverfahren (§ 53 Abs. 1 S. 4, 5, § 55 Abs. 1 S. 2 MarkenG) · V2 nur Inhaber des Rechts (§ 53 Abs. 3, § 55 Abs. 2 Nr. 2 MarkenG) · V3 Gegner: eingetragener Inhaber (§ 55 Abs. 1 MarkenG) · V4 Form (§ 53 Abs. 1 MarkenG; Klage § 78 ZPO) · V5 älteres Recht §§ 9 bis 13 MarkenG (§ 12: bundesweit) · V6 Kollision · V7 kein Ausschluss (§ 51 Abs. 2–4 MarkenG) · V8 Benutzung auf Einrede (§ 53 Abs. 6, § 55 Abs. 3, § 119 Nr. 5, § 116 Abs. 2 MarkenG) | Nichtigerklärung, Löschung (§ 51 Abs. 1, 5 MarkenG), ex tunc (§ 52 Abs. 2 MarkenG) | NS II/2019 (NS III/2019 Frage 4, II/2020, I/2021; I/2024) |
| Kosten § 63 Abs. 1 MarkenG (DPMA), § 71 Abs. 1 MarkenG (BPatG), § 90 MarkenG (BGH); Kennzeichenstreitsache § 91 ZPO, § 140 Abs. 4 MarkenG | V1 mehrseitiges Verfahren · V2 Billigkeit (Grundsatz § 63 Abs. 1 S. 3, § 71 Abs. 1 S. 2 MarkenG) · V3 auch bei Rücknahme (§ 63 Abs. 1 S. 2, § 71 Abs. 4 MarkenG) · V4 notwendige Kosten, Gegenstandswert, Festsetzung (§ 63 Abs. 2, 4, § 71 Abs. 5 MarkenG) · Rückzahlung von Gebühren (§ 63 Abs. 3, § 64 Abs. 5, § 66 Abs. 5 S. 3, § 71 Abs. 3 MarkenG) · Patentanwaltskosten nur bei Notwendigkeit (§ 140 Abs. 4 MarkenG) | Kostenauferlegung oder Kostentragung jedes Beteiligten | NS II/2019 (NS I/2020, III/2021, III/2023; III/2024, I/2025, II/2025) |
| Wiedereinsetzung § 91 Abs. 1 S. 1 MarkenG | V1 Fristversäumnis mit Rechtsnachteil; nicht Widerspruchsfrist/-gebühr (§ 91 Abs. 1 S. 2 MarkenG), nicht Weiterbehandlung (§ 91a Abs. 3 MarkenG) · V2 Antrag (§ 91 Abs. 1, Abs. 4 S. 2 MarkenG) · V3 zwei Monate ab Wegfall, ein Jahr Höchstfrist (§ 91 Abs. 2, 5 MarkenG) · V4 Nachholung (§ 91 Abs. 4 S. 1 MarkenG) · V5 Tatsachen, Glaubhaftmachung (§ 91 Abs. 3 MarkenG, § 294 ZPO) · V6 ohne Verschulden (§ 85 Abs. 2 ZPO) | versäumte Handlung gilt als rechtzeitig; Entscheidung § 91 Abs. 6 MarkenG, unanfechtbar § 91 Abs. 7 MarkenG, Weiterbenutzungsrecht § 91 Abs. 8 MarkenG | (NS III/2020, II/2021, I/2022, II/2023) |
| Verfall § 49 Abs. 1, 2 MarkenG mit § 53 MarkenG (DPMA) oder § 55 MarkenG (LG) | V0 Gebühr 100 € (Nr. 333 400) · V1 Antrag DPMA oder Klage; IR: Schutzentziehung (§ 115 Abs. 1 MarkenG) · V2 jedermann (§ 53 Abs. 2, § 55 Abs. 2 Nr. 1 MarkenG) · V3 Form (§ 53 Abs. 1 MarkenG) · V4 Mitteilung mit Zweimonatsfrist (§ 53 Abs. 4 MarkenG) · V5 Widerspruch des Inhabers (§ 53 Abs. 5 S. 1 MarkenG) · V6 Weiterverfolgungsgebühr 300 € binnen eines Monats (§ 53 Abs. 5 S. 4, 5 MarkenG, Nr. 333 450) oder Klage (§ 49 Abs. 1 S. 4 MarkenG) · V7 Schonfrist (§ 49 Abs. 1 S. 1, § 26 Abs. 5, § 115 Abs. 2 MarkenG) · V8 fünf Jahre keine Benutzung nach § 26 MarkenG · V9 keine Heilung (§ 49 Abs. 1 S. 2, 3 MarkenG) · Abs. 2 Nr. 1–3 | Verfall, Löschung, ganz/teilweise (§ 49 Abs. 1, 3 MarkenG), Wirkung ab Antrag (§ 52 Abs. 1 MarkenG); ohne Widerspruch ohne Sachprüfung (§ 53 Abs. 5 S. 1 MarkenG) | (NS I/2020, III/2021 Frage 3, III/2023) |
| Unterlassung, Schadensersatz, Vernichtung, Auskunft § 14 Abs. 5, 6, § 18, § 19 MarkenG; § 15 Abs. 2, 4, 5 MarkenG; Unionsmarke Art. 9 UMV, § 119 Nr. 2 MarkenG | V1 LG ausschließlich (§ 140 Abs. 1 MarkenG; Unionsmarke § 122 MarkenG) · V2 Marke nach § 4 MarkenG, Aktivlegitimation (§ 28 Abs. 1, § 30 Abs. 3 MarkenG) · V3 geschäftlicher Verkehr · V4 ohne Zustimmung · V5 markenmäßige Benutzung für Waren/DL (§ 14 Abs. 2, 3 MarkenG) · V6 § 14 Abs. 2 S. 1 Nr. 1–3 MarkenG · V7 keine Schranke (§ 20 MarkenG bis § 25 MarkenG) · V8 Wiederholungs-/Erstbegehungsgefahr; Verschulden; Verhältnismäßigkeit (§ 18 Abs. 3 MarkenG) | Unterlassung, Schadensersatz (dreifache Berechnung § 14 Abs. 6 S. 2, 3 MarkenG), Vernichtung/Rückruf, Auskunft; einstweilige Verfügung § 140 Abs. 3 MarkenG | (NS I/2020, I/2021, II/2022, I/2023; II/2024) |
| Erinnerung § 64 Abs. 1 MarkenG | V0 Gebühr 150 € (Nr. 333 000) · V1 Beschluss des gehobenen Dienstes (§ 64 Abs. 1 MarkenG) · V2 Beteiligter, Beschwer · V3 ein Monat ab Zustellung beim DPMA (§ 64 Abs. 2 MarkenG) · Abhilfe (§ 64 Abs. 3 MarkenG); wahlweise Beschwerde (§ 64 Abs. 6 MarkenG); Durchgriffsbeschwerde (§ 66 Abs. 3 MarkenG) | Entscheidung durch ein Mitglied des DPMA (§ 64 Abs. 4 MarkenG) | (III/2025) |
| Rechtsbeschwerde § 83 MarkenG | V1 Beschwerdebeschluss des BPatG · V2 Zulassung (§ 83 Abs. 1, 2 MarkenG) oder Rüge nach § 83 Abs. 3 Nr. 1–6 MarkenG · V3 ein Monat beim BGH, Begründung ein Monat (§ 85 Abs. 1, 3 MarkenG) · V4 BGH-Anwalt (§ 85 Abs. 5 MarkenG) | Aufhebung und Zurückverweisung oder Zurückweisung; Kosten § 90 Abs. 2 MarkenG | (NS I/2022: BGH I ZB 65/22) |
| Weiterbehandlung § 91a MarkenG | V1 Zurückweisung der Anmeldung nach Versäumung einer Amtsfrist · V2 Antrag und Nachholung binnen eines Monats (§ 91a Abs. 2 MarkenG) · V3 Gebühr 100 € (Nr. 333 050) | Zurückweisung wird wirkungslos (§ 91a Abs. 1 MarkenG); keine Wiedereinsetzung (§ 91a Abs. 3 MarkenG) | (NS I/2023: Anmeldung „Mahlefix“) |

### Definitionen

| Begriff | Definition | Quelle |
|---|---|---|
| Widerspruchskennzeichen | jede Marke, geschäftliche Bezeichnung, g.U. oder g.g.A., wegen der Widerspruch erhoben wird | § 29 Abs. 1 S. 1 MarkenV |
| Zeitrang | Anmelde- oder Prioritätstag; bei Benutzungsrechten Zeitpunkt des Erwerbs | § 6 Abs. 2, 3 MarkenG |
| Unternehmenskennzeichen | Zeichen, die im geschäftlichen Verkehr als Name, Firma oder besondere Bezeichnung eines Geschäftsbetriebs oder Unternehmens benutzt werden | § 5 Abs. 2 S. 1 MarkenG |
| Bundesweite Untersagungsbefugnis | nicht eingetragenes Recht berechtigt, die Benutzung der jüngeren Marke im gesamten Bundesgebiet zu untersagen | § 12, § 13 Abs. 1 MarkenG; BPatG Engelbrecht |
| Agent oder Vertreter | wer aufgrund eines Vertragsverhältnisses die geschäftlichen Interessen des Markeninhabers wahrzunehmen hat | § 11 MarkenG, Rechtsprechung (weite Auslegung) |
| Inlandsvertreter | Rechts- oder Patentanwalt, den bestellen muss, wer im Inland weder Wohnsitz, Sitz noch Niederlassung hat | § 96 Abs. 1 MarkenG |
| Verwechslungsgefahr | Gefahr, dass das Publikum annimmt, die Waren/DL stammen aus demselben oder wirtschaftlich verbundenen Unternehmen | EuGH Canon (C-39/97), SABEL/Puma (C-251/95) |
| Wechselwirkung | geringere Waren-/DL-Ähnlichkeit kann durch höhere Zeichenähnlichkeit oder Kennzeichnungskraft ausgeglichen werden und umgekehrt | EuGH Canon |
| Waren-/DL-Ähnlichkeit | Art, Verwendungszweck, Nutzung, Wettbewerbs- oder Ergänzungsverhältnis, ferner Herstellungsstätte und Vertriebswege; Klasse unerheblich | EuGH Canon; § 9 Abs. 3 MarkenG |
| Kennzeichnungskraft | Eignung, die Waren als von einem Unternehmen stammend zu kennzeichnen; fünf Grade | EuGH Lloyd (C-342/97); BGH Culinaria (I ZR 85/11) |
| Durchschnittsverbraucher | durchschnittlich informiert, aufmerksam, verständig; unvollkommenes Erinnerungsbild | EuGH Lloyd |
| Prägung | ein Bestandteil prägt, wenn die übrigen für den Verkehr weitgehend zurücktreten | BGH Culinaria |
| Selbständig kennzeichnende Stellung | ältere Marke behält im jüngeren Kombinationszeichen eine eigenständige Stellung, ohne es zu dominieren | EuGH THOMSON LIFE (C-120/04); BGH Culinaria |
| Serienzeichen | Verkehr sieht im übereinstimmenden, hinweiskräftigen Stamm den Hinweis auf eine Zeichenserie desselben Unternehmens; i.d.R. Benutzung mehrerer Stammzeichen | Rechtsprechung; BPatG vita+lebenskraft/VITA |
| Bekannte Marke | einem bedeutenden Teil des betroffenen Publikums bekannt; keine festen Prozentsätze | EuGH General Motors (C-375/97) |
| Zeichenidentität | Wiedergabe aller Elemente ohne Änderung oder Hinzufügung, oder so geringe Abweichungen, dass sie dem Durchschnittsverbraucher entgehen | st. Rspr. des EuGH |
| Ernsthafte Benutzung | Benutzung entsprechend der Hauptfunktion, um einen Absatzmarkt zu erschließen oder zu sichern; nicht symbolisch | EuGH Ansul (C-40/01) |
| Benutzung als Marke | Verwendung als Herkunftshinweis für die eingetragenen Waren/DL; Firmenbezeichnung allein genügt nicht | § 26 Abs. 1 MarkenG; EuGH Céline (C-17/06) |
| Benutzungsschonfrist | fünf Jahre ab dem Tag, ab dem kein Widerspruch mehr möglich ist (bei Widerspruch: Rechtskraft/Rücknahme) | § 26 Abs. 5, § 49 Abs. 1 S. 1 MarkenG; IR § 115 Abs. 2 MarkenG |
| Abweichende Form | Abweichung, die den kennzeichnenden Charakter nicht verändert | § 26 Abs. 3 MarkenG |
| Benutzung der Unionsmarke | ernsthafte Benutzung in der Union; Grenzen der Mitgliedstaaten außer Betracht | Art. 18 UMV; EuGH Leno Merken (C-149/11) |
| Bösgläubige Anmeldung | rechtsmissbräuchliche oder sittenwidrige Anmeldung, insbesondere als Mittel des Wettbewerbskampfes (Sperrmarke) oder zur Störung eines schutzwürdigen Besitzstands; Zeitpunkt der Anmeldung | § 8 Abs. 2 Nr. 14 MarkenG; BGH GLÜCKSPILZ (I ZB 69/14), BGH LIQUIDROM (I ZB 44/14) |
| Unterscheidungskraft | konkrete Eignung, vom Verkehr als Unterscheidungsmittel für die Waren eines Unternehmens aufgefasst zu werden | § 8 Abs. 2 Nr. 1 MarkenG; st. Rspr. des BGH |
| Beschreibende Angabe | Zeichen, die zur Bezeichnung von Merkmalen der Waren dienen können, auch künftig vernünftigerweise zu erwarten | § 8 Abs. 2 Nr. 2 MarkenG; EuGH Windsurfing Chiemsee (C-108/97) |
| Üblich gewordene Bezeichnung | im allgemeinen Sprachgebrauch oder in den redlichen und ständigen Verkehrsgepflogenheiten zur Bezeichnung der Waren üblich geworden | § 8 Abs. 2 Nr. 3 MarkenG |
| Verkehrsdurchsetzung | erheblicher Teil der beteiligten Verkehrskreise ordnet die Waren aufgrund der Marke einem Unternehmen zu | § 8 Abs. 3, § 50 Abs. 2 S. 2 MarkenG; EuGH Windsurfing Chiemsee |
| Verkehrsgeltung | Zeichen wird innerhalb beteiligter Verkehrskreise als Herkunftshinweis verstanden; Schutz ohne Eintragung | § 4 Nr. 2 MarkenG |
| Duldung | Hinnahme der Benutzung der eingetragenen jüngeren Marke fünf aufeinanderfolgende Jahre in Kenntnis; nicht bei Bösgläubigkeit | § 51 Abs. 2 S. 1, § 21 Abs. 1 MarkenG |
| Sonstige ältere Rechte | Namensrechte, Recht an der eigenen Abbildung, Urheberrechte, Sortenbezeichnungen, geografische Herkunftsangaben, sonstige gewerbliche Schutzrechte | § 13 Abs. 2 MarkenG |
| Verfall | Löschung wegen nachträglich eingetretener Gründe, Wirkung ab Antrag/Klage | § 49, § 52 Abs. 1 MarkenG |
| Nichtigkeit | Löschung, weil die Marke nicht hätte eingetragen werden dürfen; Wirkung von Anfang an | § 50, § 51, § 52 Abs. 2 MarkenG |
| Kennzeichenstreitsache | Klage, durch die ein Anspruch aus einem im MarkenG geregelten Rechtsverhältnis geltend gemacht wird | § 140 Abs. 1 MarkenG |
| Benutzung im geschäftlichen Verkehr | im Zusammenhang mit einer auf wirtschaftlichen Vorteil gerichteten kommerziellen Tätigkeit, nicht privat | EuGH Arsenal (C-206/01) |
| Markenmäßige Benutzung | Benutzung, die die Funktionen der Marke, insbesondere die Herkunftsfunktion, beeinträchtigen kann | EuGH Arsenal; EuGH Céline |
| Wiederholungsgefahr / Erstbegehungsgefahr | durch Verletzung vermutet, entfällt i.d.R. nur durch strafbewehrte Unterlassungserklärung / ernsthafte, greifbare Anhaltspunkte für drohende Erstverletzung | § 14 Abs. 5 S. 1, 2 MarkenG; Rechtsprechung |
| Dreifache Schadensberechnung | konkreter Schaden, Verletzergewinn, Lizenzanalogie | § 14 Abs. 6 S. 1–3 MarkenG |
| Erschöpfung | kein Verbot für Waren, die vom Inhaber oder mit Zustimmung im EWR in Verkehr gebracht wurden, außer berechtigte Gründe | § 24 Abs. 1, 2 MarkenG |
| Beschwer | angefochtene Entscheidung bleibt hinter dem Antrag zurück | Rechtsprechung |
| Abhilfe | Aufhebung durch die Ausgangsstelle selbst, nur ohne Gegenbeteiligten | § 64 Abs. 3, § 66 Abs. 5 MarkenG |
| Verschulden (§ 91 MarkenG) | Außerachtlassen der von einem gewissenhaften Beteiligten bzw. Anwalt zu erwartenden Sorgfalt; leichte Fahrlässigkeit schadet | Rechtsprechung |
| Wegfall des Hindernisses | Kenntnis oder Kennenmüssen der Säumnis | Rechtsprechung |
| Vertreterverschulden | Verschulden des Bevollmächtigten steht dem der Partei gleich; Büroversehen bei ordnungsgemäßer Organisation nicht | § 85 Abs. 2 ZPO; Rechtsprechung |
| Glaubhaftmachung | überwiegende Wahrscheinlichkeit; alle Beweismittel, auch eidesstattliche Versicherung | § 294 Abs. 1 ZPO |
| Billigkeit (Kosten) | besondere Umstände, etwa Verfahren in aussichtsloser Lage; Unterliegen allein genügt nicht | § 63 Abs. 1, § 71 Abs. 1 MarkenG; BPatG Engelbrecht (25 W (pat) 52/21) |

### Fristen

| Frist | Norm | Berechnung | Verschiebung | Gebühr |
|---|---|---|---|---|
| Widerspruch: drei Monate nach Veröffentlichung der Eintragung | § 42 Abs. 1 S. 1 MarkenG (IR: Beginn erster Tag des Folgemonats, § 114 Abs. 2 MarkenG); keine Wiedereinsetzung § 91 Abs. 1 S. 2 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB (IR: § 187 Abs. 2 BGB) | § 193 BGB (Feiertag am Erklärungsort) | 250 € Nr. 331 600 + 50 € je weiteres Kennzeichen Nr. 331 610; in der Frist (§ 6 Abs. 1 S. 1 PatKostG), sonst nicht erhoben (§ 6 Abs. 2 PatKostG); Zahlungstag § 2 PatKostZV |
| Einigungsfrist (cooling off): mindestens zwei Monate auf beiderseitigen Antrag | § 42 Abs. 4 MarkenG | — | — | — |
| Erinnerung: ein Monat nach Zustellung | § 64 Abs. 2 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 150 € Nr. 333 000 |
| Beschwerde: ein Monat nach Zustellung, beim DPMA | § 66 Abs. 2 MarkenG; Zustellung § 94 Abs. 1 MarkenG, § 4 Abs. 2 S. 2 VwZG (vierter Tag), § 94 Abs. 1 Nr. 3 MarkenG (Abholfach dritter Tag) | § 82 Abs. 1 MarkenG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | 200 € Nr. 401 300; Verfall/Nichtigkeit 500 € Nr. 401 100; in der Frist (§ 6 Abs. 1 S. 1, Abs. 2 PatKostG) |
| Beschwerde gegen Kostenfestsetzungsbeschluss: zwei Wochen | § 63 Abs. 4 S. 4 MarkenG | § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | 50 € Nr. 401 200 |
| Rechtsbeschwerde: ein Monat nach Zustellung, beim BGH; Begründung ein Monat ab Einlegung | § 85 Abs. 1, 3 MarkenG | § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | — (keine Gebühr nach PatKostG) |
| Widerspruch des Inhabers gegen Verfalls-/Nichtigkeitsantrag: zwei Monate nach Zustellung der Mitteilung | § 53 Abs. 4, 5 S. 1 MarkenG (ohne Fristsetzung kein Fristbeginn, BPatG AUTOMATOR) | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | — |
| Weiterverfolgung des Verfallsantrags: ein Monat nach Zustellung des Widerspruchs | § 53 Abs. 5 S. 4, 5 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 300 € Nr. 333 450; sonst Verfahren abgeschlossen |
| Klage nach Verfallsantrag mit Wahrung des Antragstags: drei Monate nach Zustellung der Mitteilung | § 49 Abs. 1 S. 4 MarkenG | § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | Gerichtskosten nach GKG |
| Verfalls-/Nichtigkeitsantrag: keine Antragsfrist; § 8 Abs. 2 Nr. 1–3 MarkenG: zehn Jahre seit Eintragung | § 50 Abs. 2 S. 3 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Verfall 100 € Nr. 333 400; Nichtigkeit 400 € Nr. 333 300 + 100 € je weiteres Recht Nr. 333 350; drei Monate ab Fälligkeit (§ 3 Abs. 1, § 6 Abs. 1 S. 2 PatKostG) |
| Nichtigkeit von Amts wegen (§ 8 Abs. 2 Nr. 4–14 MarkenG): Einleitung binnen zwei Jahren seit Eintragung | § 50 Abs. 3 Nr. 1 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | — |
| Wiedereinsetzung: zwei Monate nach Wegfall des Hindernisses; höchstens ein Jahr nach Ablauf der versäumten Frist | § 91 Abs. 2, 5 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB (BPatG: § 222 Abs. 2 ZPO) | Gebühr der nachgeholten Handlung |
| Weiterbehandlung: ein Monat nach Zustellung der Zurückweisung | § 91a Abs. 2 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | 100 € Nr. 333 050 |
| Eintragungsbewilligungsklage: sechs Monate nach Unanfechtbarkeit der Löschung | § 44 Abs. 2 MarkenG | § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | Gerichtskosten nach GKG |
| Benutzungszeitraum im Widerspruch: fünf Jahre vor Anmelde-/Prioritätstag der angegriffenen Marke (Zeitraum) | § 43 Abs. 1 S. 1 MarkenG (Altfälle § 158 Abs. 5 MarkenG) | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | keine (Zeitraum) | — |
| Benutzungsschonfrist: fünf Jahre (Zeitraum) | § 26 Abs. 5, § 49 Abs. 1 S. 1 MarkenG; IR § 115 Abs. 2 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | keine (Zeitraum) | — |
| Duldung/Verwirkung: fünf aufeinanderfolgende Jahre in Kenntnis | § 51 Abs. 2, § 21 Abs. 1 MarkenG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | keine (Zeitraum) | — |
| Verjährung der Verletzungsansprüche: drei Jahre ab Jahresende der Kenntnis | § 20 MarkenG i.V.m. § 195, § 199 Abs. 1 BGB | § 199 Abs. 1 BGB | — | — |

### Weitere Hilfsnormen

- **Wirksamkeit und Zahlung:** § 64a MarkenG (PatKostG gilt vor dem DPMA), § 3 Abs. 1 PatKostG (Fälligkeit), § 6 PatKostG (Zahlungsfrist, Fiktion), § 10 Abs. 2 PatKostG (Wegfall/Erstattung), § 2 PatKostZV (Zahlungstag: Gutschrift, Einzahlung, Eingang des SEPA-Mandats), § 3 Abs. 1 S. 5 PatKostG und § 6 Abs. 4 PatKostG (Erinnerung und Beschwerde nach § 64 Abs. 6 MarkenG).
- **Beteiligte:** § 7 MarkenG (Inhaberschaft), § 28 MarkenG (Vermutung, Rechtsnachfolge im Verfahren), § 27 MarkenG (Übertragung), § 53 Abs. 7, § 55 Abs. 4 MarkenG (Rechtsnachfolge im Löschungsverfahren), § 81 MarkenG (Vertretung vor dem BPatG), § 96 MarkenG (Inlandsvertreter), § 15 DPMAV (Vollmacht), § 50, § 51 ZPO; § 105 Abs. 2, § 161 Abs. 2 HGB (Personengesellschaften), § 49 Abs. 1 HGB (Prokura).
- **Verfahren:** § 56 MarkenG (Markenstelle/Markenabteilung, gehobener Dienst), § 59 MarkenG (Amtsermittlung, rechtliches Gehör), § 78 MarkenG (Beweiswürdigung, Gehör vor dem BPatG), § 82 Abs. 1 MarkenG (GVG/ZPO entsprechend; § 148 ZPO Aussetzung), § 94 MarkenG (Zustellung, VwZG), § 95a MarkenG (elektronische Einreichung, § 130a ZPO), § 70 MarkenG (Entscheidung, Zurückverweisung), § 43 Abs. 3 MarkenG (Aussetzung weiterer Widersprüche), § 44 MarkenG (Eintragungsbewilligungsklage), § 52 MarkenG (Wirkung von Verfall und Nichtigkeit).
- **Unionsmarke und IR-Marke:** § 119 Nr. 1–6 MarkenG, § 122 MarkenG (Unionsmarkengerichte), Art. 9, Art. 18, Art. 63, Art. 128 UMV; § 107 MarkenG, § 112 MarkenG, § 114 MarkenG bis § 117 MarkenG; Art. 5 Abs. 2a PMMA.
- **Übergangsrecht MaMoG:** § 158 Abs. 2–6, 8 MarkenG (Anmeldungen, Widersprüche und Anträge vor dem 14.01.2019). Das DPMA-Nichtigkeitsverfahren wegen älterer Rechte (§ 51, § 53 MarkenG) gilt seit 01.05.2020 (gestaffeltes Inkrafttreten des MaMoG).
- **Verletzung:** § 14 Abs. 3, 4, 7 MarkenG, § 14a MarkenG, § 19a MarkenG bis § 19c MarkenG, § 140 Abs. 3, 4 MarkenG; Abmahnkosten über § 677, § 683 S. 1, § 670 BGB oder als Schadensersatz.

## Design

Grundlage: Lösung RP1 II/2019 (`loesungen/rp1/PAP-2019-II-RP1.json`) und die Aufgabentexte aller 17 RP1-Klausuren II/2018 bis III/2023.
GGV in der konsolidierten Fassung vom 1.7.2026 (Nachahmungsschutz Art. 19 Abs. 4 GGV, früher Abs. 2; Aufschiebung Art. 19 Abs. 5 GGV,
früher Abs. 3; Art. 89 GGV ohne Buchstaben). Kurs: `src/knowledge/kurse/d03_agl_design.py`.

### Anspruchsgrundlagen und Rechtsbehelfe

| AGL | Normenkette (V1 … Vn mit Norm) | Rechtsfolge | Klausuren |
|---|---|---|---|
| Unterlassung/Beseitigung aus dem deutschen Design: § 42 Abs. 1 DesignG i.V.m. § 38 Abs. 1 S. 1 DesignG | V1 Anspruchsteller § 1 Nr. 5, § 8 DesignG (Lizenznehmer § 31 Abs. 3 DesignG) · V2 Schutzrecht in Kraft § 27, § 28 DesignG, Vermutung § 39 DesignG · V3 Benutzung § 38 Abs. 1 S. 2 DesignG · V4 kein anderer Gesamteindruck § 38 Abs. 2 DesignG · V5 ohne Zustimmung; während Aufschiebung nur Nachahmung § 38 Abs. 3 DesignG · V6 keine Schranke § 40, § 40a, § 41, § 48 DesignG · V7 Nichtigkeit nur per Widerklage/Antrag § 52a DesignG · V8 Wiederholungs-/Erstbegehungsgefahr § 42 Abs. 1 S. 1, 2 DesignG | Unterlassung, Beseitigung; Verjährung § 49 S. 1 DesignG i.V.m. § 195, § 199 Abs. 1 BGB | RP1 II/2019 (DE1, DE2) (III/2019, I/2019, I/2020, I/2022, III/2023) |
| Unterlassung aus dem Unionsgeschmacksmuster: Art. 19 Abs. 1 GGV i.V.m. Art. 89 Abs. 1 GGV | V1 Inhaber Art. 17 GGV, nicht eingetragen Art. 14 GGV · V2 Schutzrecht: eingetragen Art. 12 GGV, Vermutung Art. 85 Abs. 1 GGV; nicht eingetragen Art. 11 GGV + Angabe der Eigenart Art. 85 Abs. 2 GGV · V3 Benutzung Art. 19 Abs. 2 GGV · V4 Schutzumfang Art. 10 GGV · V5 nicht eingetragen/Aufschiebung nur Nachahmung Art. 19 Abs. 4, 5 GGV · V6 Schranken Art. 20, 20a, 21, 22 GGV · V7 Nichtigkeit nur per Widerklage Art. 85 Abs. 1 S. 2 GGV · V8 Verletzung oder drohende Verletzung Art. 89 Abs. 1 GGV | Verbot, unionsweit bei Zuständigkeit nach Art. 82 Abs. 1 bis 4 GGV (Art. 83 Abs. 1 GGV) | RP1 II/2019 (EU1) (II/2018, III/2018, II/2020, II/2021, III/2021, III/2022, II/2023) |
| Schadensersatz: § 42 Abs. 2 DesignG; Unionsmuster Art. 89 Abs. 2, Art. 88 Abs. 2 GGV, Art. 8 Abs. 2 Rom-II-VO i.V.m. § 62a Nr. 1 DesignG, § 42 Abs. 2 DesignG | V1 Verletzung wie oben · V2 Vorsatz/Fahrlässigkeit § 42 Abs. 2 S. 1 DesignG · V3 Berechnung: konkreter Schaden, Verletzergewinn, Lizenzanalogie § 42 Abs. 2 S. 2, 3 DesignG · V4 anwendbares Recht: Ort der ursprünglichen Verletzungshandlung (EuGH Nintendo) | Ersatz des Schadens; Lizenznehmer eigener Schaden Art. 32 Abs. 3, 4 GGV | RP1 II/2019 (DE2) (II/2021, III/2021) |
| Vernichtung, Rückruf, Auskunft: § 43, § 46 DesignG (Unionsmuster über § 62a Nr. 1 DesignG) | V1 Verletzung · V2 Erzeugnisse im Besitz/Eigentum des Verletzers § 43 Abs. 1 DesignG · V3 Verhältnismäßigkeit § 43 Abs. 4, § 46 Abs. 4 DesignG · V4 Auskunftsinhalt § 46 Abs. 3 DesignG; im Eilverfahren nur bei offensichtlicher Verletzung § 46 Abs. 7 DesignG | Vernichtung, Rückruf, Überlassung, Auskunft | RP1 II/2019 (III/2018) |
| Nichtigkeitsantrag beim DPMA: § 34a Abs. 1 DesignG i.V.m. § 33 DesignG; Widerklage § 52b DesignG | V1 eingetragenes Design, auch nach Erlöschen § 33 Abs. 5 DesignG · V2 DPMA, Designabteilung § 23 Abs. 2 DesignG · V3 Antragsbefugnis § 34 S. 1 DesignG (jedermann), § 34 S. 2 DesignG (Inhaber) DesignG · V4 schriftlich, Tatsachen, Beweismittel § 34a Abs. 1 S. 1, 2 DesignG · V5 Gebühr 300 EUR Nr. 346 100, § 3 Abs. 1, § 6 Abs. 1 S. 2, § 6 Abs. 2 PatKostG · V6 keine Rechtskraft § 34a Abs. 1 S. 4 DesignG · V7 Widerspruch binnen eines Monats § 34a Abs. 2 DesignG · V8 Gründe § 33 Abs. 1 Nr. 1–3, Abs. 2 Nr. 1–3 DesignG | Feststellung/Erklärung der Nichtigkeit, ex tunc mit Unanfechtbarkeit § 33 Abs. 4 DesignG; Löschung § 36 Abs. 1 Nr. 5 DesignG; Beschwerde § 23 Abs. 4 DesignG | RP1 II/2019 (DISC) (I/2019, I/2020, I/2021) |
| Nichtigkeit des Unionsmusters: Antrag EUIPO Art. 24 Abs. 1, Art. 52 GGV i.V.m. Art. 25 GGV; Widerklage Art. 81 lit. d, Art. 84 GGV; nicht eingetragen nur vor Gericht Art. 24 Abs. 3, Art. 81 lit. c GGV | V1 Antragsbefugnis Art. 25 Abs. 2 GGV (lit. a, b jedermann), Abs. 3, Abs. 4 (lit. d–f Inhaber) GGV · V2 schriftlich, begründet, Gebühr Art. 52 Abs. 2 GGV · V3 keine Rechtskraft Art. 52 Abs. 3 GGV · V4 Gründe Art. 25 Abs. 1 lit. a–g GGV · V5 Erwerber erst nach Umschreibung Art. 28 Abs. 6 GGV | Nichtigerklärung, Wirkung ex tunc Art. 26 GGV; Aussetzung des Verletzungsprozesses Art. 91 GGV | RP1 II/2019 (UGM DISC) (III/2018, II/2020, III/2020, I/2021, III/2021, II/2022, III/2022) |
| Zuständigkeit für Klagen aus dem Unionsmuster: Art. 80 bis 83 GGV, § 63, § 63b DesignG | V1 Streitsache Art. 81 GGV · V2 international Art. 82 Abs. 1 GGV (Beklagter), Art. 82 Abs. 2 GGV (Kläger), Abs. 3 (Spanien), Abs. 4 (Vereinbarung, Einlassung), Abs. 5 (Verletzungsort) GGV; Art. 79 Abs. 2 lit. a GGV, Art. 8 Nr. 1 Brüssel-Ia-VO · V3 Reichweite Art. 83 Abs. 1, 2 GGV · V4 örtlich § 63b DesignG, § 12, § 17, § 32 ZPO · V5 sachlich LG § 63 Abs. 1, 2 DesignG | Klage am Beklagtensitz: unionsweit; am Verletzungsort: nur Gerichtsstaat | RP1 II/2019 (II/2018, II/2020, II/2021, III/2022, II/2023) |
| Zuständigkeit für Klagen aus dem deutschen Design: Brüssel-Ia-VO, § 52 DesignG | V1 Art. 4 Abs. 1, Art. 7 Nr. 2 Brüssel-Ia-VO; Drittstaat § 32 ZPO · V2 Gültigkeit Art. 24 Nr. 4 Brüssel-Ia-VO · V3 LG ausschließlich § 52 Abs. 1, 2 DesignG | Klage in Deutschland für Verletzungen im Inland | RP1 II/2019 |
| Einstweilige Verfügung: § 935, § 940 ZPO i.V.m. § 42 Abs. 1 DesignG bzw. Art. 89 Abs. 1, Art. 90 Abs. 1 GGV | V1 Gericht der Hauptsache § 937 Abs. 1 ZPO; Art. 90 Abs. 1, 3 GGV · V2 Antrag, Glaubhaftmachung § 920, § 294, § 936 ZPO · V3 Verfügungsanspruch (Unterlassung, Sequestration § 938 Abs. 2 ZPO, Auskunft § 46 Abs. 7 DesignG) · V4 Dringlichkeit · V5 Nichtigkeitseinwand § 52a S. 2 DesignG, Art. 90 Abs. 2 GGV · V6 Abmahnung § 93 ZPO · V7 Vollziehung § 929 Abs. 2, § 922 Abs. 2, § 936 ZPO · V8 Risiko § 945 ZPO | Unterlassungsgebot mit Ordnungsmittelandrohung § 890 ZPO, Sequestration | RP1 II/2019 (III/2021, III/2022, II/2023) |
| Grenzbeschlagnahme: Art. 17, Art. 23 VO (EU) Nr. 608/2013 i.V.m. § 57a DesignG; national § 55 DesignG | V1 Drittlandsware Art. 1 Abs. 1 VO (EU) Nr. 608/2013 · V2 Unionsantrag nur Unionsrecht Art. 4 VO (EU) Nr. 608/2013 · V3 Antrag bei der Generalzolldirektion § 57 Abs. 1 S. 1, § 57a DesignG · V4 Entscheidung binnen 30 Arbeitstagen · V5 Aussetzung Art. 17 VO (EU) Nr. 608/2013 · V6 Vernichtung binnen zehn Arbeitstagen Art. 23 Abs. 1 VO (EU) Nr. 608/2013, sonst Verfahren Art. 23 Abs. 3 VO (EU) Nr. 608/2013 · V7 Haftung Art. 28 VO (EU) Nr. 608/2013, § 56 Abs. 5 DesignG; national subsidiär, offensichtliche Verletzung, Sicherheit § 55 Abs. 1 DesignG | Aussetzung, Vernichtung, Namen von Absender und Empfänger | RP1 II/2019 |
| Klage des Lizenznehmers: § 31 Abs. 3 DesignG, Art. 32 Abs. 3 GGV | V1 wirksame Lizenz § 31 Abs. 1 DesignG, Art. 32 Abs. 1 GGV · V2 Zustimmung (auch im Vertrag) § 31 Abs. 3 S. 1 DesignG, Art. 32 Abs. 3 S. 1 GGV · V3 ausschließlicher Lizenznehmer nach Aufforderung § 31 Abs. 3 S. 2 DesignG, Art. 32 Abs. 3 S. 2 GGV · V4 Eintragung nicht nötig (Art. 33 Abs. 1 GGV; EuGH Thomas Philipps) · V5 Verletzung | Unterlassung, eigener Schaden; Beitritt § 31 Abs. 4 DesignG, Art. 32 Abs. 4 GGV | (II/2021, II/2023) |
| Rechtsübergang Unionsmuster: Art. 27, Art. 28 GGV | V1 Recht des Registersitzes Art. 27 Abs. 1, 2 GGV · V2 Schriftform und Unterschrift beider Parteien Art. 28 Abs. 1 GGV · V3 Eintragung auf Antrag Art. 28 Abs. 2 GGV · V4 Rechte erst nach Eintragung Art. 28 Abs. 6 GGV | Übergang; Wirkung gegenüber Dritten Art. 33 Abs. 1 GGV | (II/2022) |
| Anmeldung und Eintragung: § 11, § 16, § 18, § 19 DesignG; Art. 35, 36, 38, 45, 47, 48 GGV | V1 Berechtigung § 7, § 8 DesignG, Art. 14 GGV · V2 Mindestinhalt § 11 Abs. 2 DesignG, Art. 36 Abs. 1 GGV; Anmeldetag § 13 DesignG, Art. 38 GGV · V3 Erzeugnisangabe § 11 Abs. 3, 6 DesignG · V4 Sammelanmeldung § 12 DesignG (100), Art. 37 GGV (50) · V5 Gebühr § 3 Abs. 1, § 6 PatKostG · V6 Priorität § 13 Abs. 2, § 14, § 15 DesignG, Art. 41, 44 GGV · V7 Prüfung § 16, § 18 DesignG, Art. 45, 47 GGV · V8 Aufschiebung § 21 DesignG, Art. 50 GGV | Eintragung; Schutz ab Eintragung § 27 Abs. 1 DesignG, Art. 12 Abs. 1 GGV | (II/2018, I/2019, III/2019, I/2020, III/2021, II/2023, III/2023) |
| Vindikation: § 9 DesignG, Art. 15 GGV | V1 Eintragung auf Nichtberechtigten · V2 Berechtigung nach § 7 DesignG, Art. 14 GGV · V3 Klage binnen drei Jahren ab Bekanntmachung § 9 Abs. 2 DesignG, Art. 15 Abs. 3 GGV (nicht bei Bösgläubigkeit) | Übertragung, Einwilligung in die Löschung, Mitinhaberschaft | (I/2021, III/2021, II/2023) |

### Definitionen

| Begriff | Definition | Quelle |
|---|---|---|
| Design | Zwei- oder dreidimensionale Erscheinungsform eines ganzen Erzeugnisses oder eines Teils, insbesondere aus Linien, Konturen, Farben, Gestalt, Oberflächenstruktur, Werkstoffen | Legaldefinition § 1 Nr. 1 DesignG; Art. 3 Nr. 1 GGV |
| Erzeugnis | Industrieller oder handwerklicher Gegenstand einschließlich Verpackung, Ausstattung, grafischer Symbole, Schriftzeichen, Einzelteile; kein Computerprogramm | Legaldefinition § 1 Nr. 2 DesignG; Art. 3 Nr. 2 GGV |
| Komplexes Erzeugnis | Erzeugnis aus mehreren ersetzbaren Bauelementen, auseinander- und wieder zusammenbaubar | Legaldefinition § 1 Nr. 3 DesignG |
| Bestimmungsgemäße Verwendung | Verwendung durch den Endbenutzer ohne Instandhaltung, Wartung, Reparatur; Sicht von Endbenutzer und außenstehendem Beobachter | Legaldefinition § 1 Nr. 4 DesignG; EuGH Monz |
| Neuheit | Vor dem Anmeldetag kein identisches Design offenbart; identisch bei Unterschieden nur in unwesentlichen Einzelheiten | Legaldefinition § 2 Abs. 2 DesignG; Art. 5 GGV |
| Eigenart | Gesamteindruck beim informierten Benutzer unterscheidet sich von dem jedes älteren offenbarten Designs; Gestaltungsfreiheit berücksichtigen; Einzelvergleich | Legaldefinition § 2 Abs. 3 DesignG; Art. 6 GGV; EuGH Karen Millen |
| Informierter Benutzer | Kennt Designs des Sektors und übliche Gestaltungselemente, vergleichsweise aufmerksam, möglichst direkter Vergleich; zwischen Verbraucher und Fachmann | EuGH PepsiCo |
| Gestaltungsfreiheit | Spielraum nach technischen/rechtlichen Vorgaben und Musterdichte; großer Spielraum verlangt großen Abstand und gibt weiten Schutz | § 2 Abs. 3 S. 2, § 38 Abs. 2 S. 2 DesignG; BGH Untersetzer |
| Offenbarung | Bekannt gemacht, ausgestellt, im Verkehr verwendet oder sonst zugänglich, außer wenn die Fachkreise der Union es nicht kennen konnten; nicht bei Vertraulichkeit | Legaldefinition § 5 DesignG; Art. 7 Abs. 1 GGV; EuGH Gautzsch |
| Neuheitsschonfrist | Offenbarung durch Entwerfer, Rechtsnachfolger, Dritte als Folge ihrer Informationen oder durch Missbrauch in den zwölf Monaten vor dem Anmeldetag bleibt unberücksichtigt | § 6 DesignG; Art. 7 Abs. 2, 3 GGV |
| Ausschließlich technisch bedingt | Technische Funktion war der einzige Faktor, ästhetische Erwägungen spielten keine Rolle; objektiv nach allen Umständen, Merkmal für Merkmal | § 3 Abs. 1 Nr. 1 DesignG, Art. 8 Abs. 1 GGV; EuGH DOCERAM; BGH Tellerschleifgerät |
| Nachahmung | Angegriffene Gestaltung beruht auf Kenntnis des Musters; nicht bei unabhängiger Gestaltung eines Entwerfers ohne Kenntnis | Art. 19 Abs. 4 GGV |
| Benutzung | Herstellung, Anbieten, Inverkehrbringen, Einfuhr, Ausfuhr, Gebrauch, Besitz zu diesen Zwecken | § 38 Abs. 1 S. 2 DesignG; Art. 19 Abs. 2 GGV |
| Schutzumfang | Jedes Design ohne anderen Gesamteindruck beim informierten Benutzer; Wahrnehmung bei bestimmungsgemäßer Verwendung | § 38 Abs. 2 DesignG; Art. 10 GGV; BGH Armbanduhr |
| Erstbegehungsgefahr | Ernsthafte, greifbare Anhaltspunkte für eine unmittelbar bevorstehende Verletzung | § 42 Abs. 1 S. 2 DesignG; Rechtsprechung |
| Verletzer | Wer entgegen § 38 Abs. 1 S. 1 DesignG ein eingetragenes Design benutzt | Legaldefinition § 42 Abs. 1 S. 1 DesignG |
| Erschöpfung | Keine Rechte an Erzeugnissen, die der Inhaber oder mit seiner Zustimmung im EWR in Verkehr gebracht wurden | § 48 DesignG; Art. 21 GGV |
| Vorbenutzungsrecht | DE: identisches, unabhängig entwickeltes Design, gutgläubig im Inland benutzt oder ernsthafte Anstalten vor dem Anmeldetag; GGV: nicht nachgeahmtes Muster im Schutzumfang, in der Union | § 41 DesignG, BGH Bettgestell; Art. 22 GGV |
| Reparaturklausel | Kein Schutz für Bauelement, das allein zur Reparatur verwendet wird, um das ursprüngliche Erscheinungsbild wiederherzustellen, bei Ursprungshinweis; GGV nur formgebundene Teile | § 40a DesignG; Art. 20a GGV |
| Feststellung / Erklärung der Nichtigkeit | Feststellung bei absoluten Gründen (§ 33 Abs. 1 DesignG), Erklärung bei relativen Gründen nur auf Antrag des Inhabers (§ 33 Abs. 2 DesignG) | § 33, § 34 DesignG |
| Älterer Zeitrang | Früherer Anmelde-/Prioritätstag; älteres eingetragenes Design wirkt auch bei späterer Offenbarung | § 13, § 33 Abs. 2 Nr. 2 DesignG; Art. 25 Abs. 1 lit. d GGV |
| Designstreitsache | Klage, mit der ein Anspruch aus einem im DesignG geregelten Rechtsverhältnis geltend gemacht wird | Legaldefinition § 52 Abs. 1 DesignG |
| Unionsgeschmacksmustergericht | Vom Mitgliedstaat benanntes nationales Gericht erster oder zweiter Instanz; in Deutschland die Landgerichte | Art. 80 Abs. 1 GGV; § 63 Abs. 1 DesignG |
| Sammelanmeldung | Mehrere Designs in einer Anmeldung, DPMA bis 100, EUIPO bis 50 | Legaldefinition § 12 Abs. 1 DesignG; Art. 37 Abs. 1 GGV |
| Aufschiebung der Bekanntmachung | Bekanntmachung nur der Eintragung ohne Wiedergabe für 30 Monate; Schutz nur gegen Nachahmung | § 21 Abs. 1, § 38 Abs. 3 DesignG; Art. 50, Art. 19 Abs. 5 GGV |

### Fristen

| Frist | Norm | Berechnung | Verschiebung | Gebühr |
|---|---|---|---|---|
| Neuheitsschonfrist 12 Monate vor AT/PT | § 6 S. 1 DesignG; Art. 7 Abs. 2 lit. b GGV | Rückrechnung entsprechend § 187 Abs. 1, § 188 Abs. 2 BGB (§ 186 BGB) | keine (Rückwärtsfrist ohne Handlungspflicht) | – |
| Priorität 6 Monate | Art. 4 C PVÜ, § 14 DesignG; Art. 41 Abs. 1 GGV | § 187 Abs. 1, § 188 Abs. 2 BGB | § 193 BGB | – |
| Ausstellungspriorität 6 Monate ab Zurschaustellung | § 15 Abs. 1 DesignG; Art. 44 GGV | § 187 Abs. 1, § 188 Abs. 2 BGB | § 193 BGB | – |
| Prioritätsangaben bis Ablauf 16. Monat | § 14 Abs. 1 S. 1, § 15 Abs. 4 DesignG | § 187 Abs. 1, § 188 Abs. 2 BGB | § 193 BGB | – |
| Anmeldegebühr DPMA 3 Monate | § 3 Abs. 1, § 6 Abs. 1 S. 2 PatKostG | § 187 Abs. 1, § 188 Abs. 2 BGB; Zahlungstag § 2 PatKostZV | § 193 BGB | 60 EUR elektronisch, 70 EUR Papier (Nr. 341 000, 341 100); Folge § 6 Abs. 2 PatKostG |
| Anmeldegebühr EUIPO 1 Monat | Art. 38 GGV | Art. 66e Abs. 1 GGV | nach Durchführungsrecht | sonst kein Anmeldetag |
| Mängelbeseitigung EUIPO 2 Monate | Art. 45 Abs. 3 GGV | Art. 66e Abs. 1 GGV | nach Durchführungsrecht | – |
| Aufschiebung 30 Monate ab AT/PT | § 21 Abs. 1 S. 1 DesignG; Art. 50 Abs. 1 GGV | § 187 Abs. 1, § 188 Abs. 2 BGB | – | Aufschiebung 30 EUR (Nr. 341 400) |
| Erstreckungsgebühr innerhalb der Aufschiebungsfrist | § 21 Abs. 2 DesignG, § 7 Abs. 2 PatKostG | wie Aufschiebungsfrist | – | 40 EUR (Nr. 341 600); sonst Schutzende § 21 Abs. 4 DesignG |
| Aufrechterhaltung je 5 Jahre ab 6. Jahr | § 28 Abs. 1 DesignG; Fälligkeit § 3 Abs. 2 PatKostG | zahlbar bis Ablauf 2. Monat, mit Zuschlag bis Ablauf 6. Monat nach Fälligkeit (§ 7 Abs. 1 PatKostG) | § 193 BGB | 90/120/150/180 EUR (Nr. 342 100–342 400), Zuschlag 50 EUR |
| Erneuerung Unionsmuster | Art. 12 Abs. 2, Art. 50d Abs. 3 GGV | 6 Monate vor Ablauf, Nachfrist 6 Monate mit Zuschlag | – | Erneuerungsgebühr EUIPO |
| Nicht eingetragenes Unionsmuster 3 Jahre | Art. 11 Abs. 1 GGV | ab Tag der ersten Offenbarung in der Union | – (Schutzdauer) | – |
| Widerspruch im Nichtigkeitsverfahren 1 Monat | § 34a Abs. 2 S. 1 DesignG | ab Zustellung; § 187 Abs. 1, § 188 Abs. 2 BGB | § 193 BGB | Nichtigkeitsantrag 300 EUR je Design (Nr. 346 100), § 3 Abs. 1, § 6 Abs. 1 S. 2, § 6 Abs. 2 PatKostG |
| Kostenantrag 1 Monat | § 34a Abs. 5 S. 3 DesignG | ab Unanfechtbarkeit bzw. Zustellung des Einstellungsbeschlusses | § 193 BGB | – |
| Beitritt zum Nichtigkeitsverfahren 3 Monate | § 34c Abs. 1 S. 2 DesignG | ab Klageerhebung oder Zugang der Unterlassungsaufforderung | § 193 BGB | wie Antrag (§ 34c Abs. 2 DesignG) |
| Beschwerde BPatG 1 Monat | § 23 Abs. 4 S. 4 DesignG i.V.m. § 73 Abs. 2 S. 1 PatG | ab Zustellung; § 187 Abs. 1, § 188 Abs. 2 BGB | § 193 BGB | 500 EUR Nichtigkeit (Nr. 401 100 Nr. 6), sonst 200 EUR (Nr. 401 300), innerhalb der Frist § 6 Abs. 1 S. 1 PatKostG |
| Weiterbehandlung 1 Monat | § 17 Abs. 2 DesignG | ab Zustellung der Zurückweisung | § 193 BGB | 100 EUR (Nr. 346 000); keine Wiedereinsetzung § 17 Abs. 3 DesignG |
| Vindikation 3 Jahre (Ausschlussfrist) | § 9 Abs. 2 DesignG; Art. 15 Abs. 3 GGV | ab Bekanntmachung (GGV: bzw. Offenbarung) | – | – |
| Verjährung 3 Jahre | § 49 S. 1 DesignG i.V.m. § 195 BGB | ab Schluss des Jahres der Kenntnis § 199 Abs. 1 BGB | § 193 BGB | – |
| Vollziehung der Beschlussverfügung 1 Monat | § 929 Abs. 2 ZPO i.V.m. § 936 ZPO | ab Zustellung an den Antragsteller; § 222 Abs. 1 ZPO i.V.m. § 187 Abs. 1, § 188 Abs. 2 BGB | § 222 Abs. 2 ZPO | Gerichtskosten nach GKG |
| Zoll: Entscheidung über den Antrag 30 Arbeitstage | VO (EU) Nr. 608/2013 (Lösung II/2019: Art. 9 Abs. 1 VO (EU) Nr. 608/2013) | Arbeitstage, VO (EWG, Euratom) Nr. 1182/71 | Art. 3 Abs. 4 VO Nr. 1182/71 | gebührenfrei |
| Zoll: Bestätigung und Zustimmung zur Vernichtung 10 Arbeitstage | Art. 23 Abs. 1, 3 VO (EU) Nr. 608/2013 | ab Mitteilung der Aussetzung | Verlängerung um bis zu 10 Arbeitstage (Art. 23 Abs. 4 VO (EU) Nr. 608/2013) | – |
| Nationale Beschlagnahme: Widerspruch 2 Wochen; gerichtliche Entscheidung 2 Wochen | § 56 Abs. 1, Abs. 4 DesignG | ab Zustellung der Mitteilung | § 193 BGB | Kosten nach § 178 AO (§ 57 Abs. 1 S. 2 DesignG) |
| Urteilsbekanntmachung 3 Monate | § 47 S. 3 DesignG | ab Rechtskraft | – | – |

### Weitere Hilfsnormen

- Vermutung der Rechtsgültigkeit: § 39 DesignG, § 52a DesignG; Art. 85 GGV; im Eilverfahren § 52a S. 2 DesignG, Art. 90 Abs. 2 GGV.
- Schutzgegenstand: § 37 DesignG, Art. 18a GGV; Erzeugnisangabe ohne Einfluss § 11 Abs. 6 DesignG; Einzeldesign mit Varianten nichtig (BGH Sporthelm).
- Prioritätstag statt Anmeldetag: § 13 Abs. 2 DesignG.
- Teilweise Aufrechterhaltung: § 35 DesignG; Einwilligung in die Löschung § 33 Abs. 6 DesignG; Kosten bei sofortiger Einwilligung (BPatG Kühlergitter-Emblemhalterung).
- Aussetzung: Art. 91 GGV (BGH Kinderwagen I), § 34b DesignG, § 52b Abs. 3 DesignG.
- Anwendbares Recht: Art. 88 GGV, Art. 8 Abs. 1, 2 Rom-II-VO (EuGH Nintendo, Acacia/BMW), § 62a DesignG (verweist noch auf Art. 89 Abs. 1 lit. a bis c GGV a.F.).
- Haftung des Unternehmensinhabers § 44 DesignG; Entschädigung § 45 DesignG; Vorlage, Besichtigung, Sicherung § 46a, § 46b DesignG.
- Patentanwaltskosten im Prozess § 52 Abs. 4, § 63 Abs. 4 DesignG; Abmahnkosten § 677, § 683 S. 1, § 670 BGB.
- Arbeitnehmerdesign § 7 Abs. 2 DesignG, Art. 14 Abs. 3 GGV; Auftragsentwurf (EuGH FEIA).
- Reform 2024: Einreichung der Unionsmusteranmeldung nur beim EUIPO (Art. 35 Abs. 1 GGV; früher auch DPMA, § 62 DesignG); Richtlinie (EU) 2024/2823 bis 9.12.2027 umzusetzen.

## Arbeitnehmererfinderrecht (ArbnErfG)

Grundlage: Lösung RP2 I/2019 (`klausuren/loesungen/rp2/PAP-2019-I-RP2.json`) und die Aufgabentexte RP2 II/2018 bis III/2023.
Klausuren ohne Klammer: aus der Lösung; in Klammern: aus dem Aufgabentext erkennbar. Normtexte: `data/arbnerfg.json` (geltende
Fassung), `data/patg.json`, Vergütungsrichtlinien `data/arbnerfg_vergrl.json`. Altfälle (Meldung vor dem 1.10.2009): ArbnErfG a.F.
(§ 43 Abs. 3 S. 1 ArbnErfG). Kurs: `src/knowledge/kurse/p07_agl_arbnerfg.py`.

### Anspruchsgrundlagen und Rechtsbehelfe

| AGL | Normenkette (V1 … Vn mit Norm) | Rechtsfolge | Klausuren |
|---|---|---|---|
| Vergütung, § 9 Abs. 1 ArbnErfG | V1 Arbeitnehmer (§ 1 ArbnErfG; nicht GmbH-Geschäftsführer, Arb.Erf. 58/16; Leiharbeitnehmer gegen Entleiher, Arb.Erf. 24/23) · V2 Diensterfindung (§ 4 Abs. 2 ArbnErfG) · V3 Inanspruchnahme (§ 6 ArbnErfG) · V4 kein wirksamer Ausschluss (§ 22 S. 1 ArbnErfG; Vereinbarung nach Meldung § 22 S. 2 ArbnErfG) · V5 Erfindungswert (§ 9 Abs. 2 ArbnErfG; RL Nr. 3 bis RL Nr. 29) · V6 Anteilsfaktor (RL Nr. 30 bis RL Nr. 37) · V7 Miterfinderanteil (§ 12 Abs. 2 ArbnErfG) | V = E × A (RL Nr. 39), Lizenzanalogie V = B × L × A; laufend oder Gesamtabfindung (RL Nr. 40, RL Nr. 41) | (RP2 II/2018, III/2018, II/2019, II/2020, III/2020, II/2021, III/2021, I/2022, II/2022, III/2022, I/2023, II/2023) |
| Vergütung bei Lizenzvergabe, § 9 Abs. 1 ArbnErfG i.V.m. RL Nr. 14, RL Nr. 15 | V1–V4 wie oben · V5 Nettolizenzeinnahme (RL Nr. 14), vereinfacht 20–50 % der Bruttolizenzeinnahme (RL Nr. 15) · Know-how-Entgelt abziehen (RL Nr. 14) · Export eines inländischen Lizenznehmers zählt (RL Nr. 26) | V = E × A × Anteil | (RP2 II/2018, II/2019, II/2020, II/2021, III/2021, III/2022) |
| Vergütung bei Verkauf, § 9 Abs. 1 ArbnErfG i.V.m. RL Nr. 16 | V1–V4 wie oben · V5 Nettoertrag (RL Nr. 16) · Schuldner bleibt Arbeitgeber (Arb.Erf. 23/21 vom 14.06.2023), anders § 613a Abs. 1 BGB und Umwandlung (Arb.Erf. 23/21 vom 14.11.2023) | Vergütung aus dem Kaufpreis, Erwerber schuldet nichts | (RP2 I/2023, III/2022) |
| Auskunft und Rechnungslegung, § 242 BGB i.V.m. § 9 Abs. 1 ArbnErfG | V1 Vergütungsanspruch dem Grunde nach · V2 Erfinder braucht die Angaben zur Berechnung · V3 Arbeitgeber kann sie zumutbar geben · Umfang nach Methode (BGH Abwasserbehandlung), nicht Gewinn (BGH Türinnenverstärkung) | Auskunft, ggf. Stufenklage mit § 38 ArbnErfG | (RP2 III/2018, III/2019, II/2021, II/2022) |
| Unwirksamkeit wegen Unbilligkeit, § 23 Abs. 1 ArbnErfG | V1 nach dem Gesetz zulässige Vereinbarung (§ 22 S. 2 ArbnErfG) oder Festsetzung (§ 12 Abs. 4 ArbnErfG) · V2 erhebliche Unbilligkeit im Zeitpunkt des Abschlusses (Faktor 2, BGH Chemische Verbrauchsmaterialien zur Überzahlung; Pauschale Faktor 3, Arb.Erf. 03/09) · V3 Geltendmachung in Textform bis sechs Monate nach Ende des Arbeitsverhältnisses (§ 23 Abs. 2 ArbnErfG) | Vereinbarung/Festsetzung unwirksam, gesetzliche Vergütung | (RP2 II/2018, II/2019, II/2020, II/2021, III/2021, I/2022) |
| Anpassung, § 12 Abs. 6 S. 1 ArbnErfG | V1 Feststellung oder Festsetzung · V2 wesentliche Änderung der maßgebenden Umstände nach Abschluss (Pauschale: etwa dreifache Nutzung, Arb.Erf. 52/13) · V3 Festhalten unzumutbar (Arb.Erf. 29/20) | Einwilligung in andere Regelung; keine Rückforderung (§ 12 Abs. 6 S. 2 ArbnErfG) | (RP2 III/2019, I/2021, II/2021, I/2022) |
| Festsetzung und Widerspruch, § 12 Abs. 3, 4 ArbnErfG | V1 keine Vereinbarung in angemessener Frist · V2 begründete Erklärung in Textform, spätestens drei Monate nach Erteilung (§ 12 Abs. 3 ArbnErfG) · V3 Widerspruch in Textform binnen zwei Monaten (§ 12 Abs. 4 S. 1 ArbnErfG); Miterfinder § 12 Abs. 5 ArbnErfG | ohne Widerspruch verbindlich (§ 12 Abs. 4 S. 2 ArbnErfG) | (RP2 II/2018, II/2020, III/2022) |
| Rechtsübergang durch Inanspruchnahme, § 7 Abs. 1 ArbnErfG i.V.m. § 6 ArbnErfG | V1 Diensterfindung (§ 4 Abs. 2 ArbnErfG) · V2 anwendbares Recht (§ 43 Abs. 3 ArbnErfG) · V3a Erklärung (§ 6 Abs. 1 ArbnErfG; ohne Meldung keine Frist, Arb.Erf. 21/09) oder V3b Fiktion vier Monate nach ordnungsgemäßer Meldung (§ 6 Abs. 2 ArbnErfG; § 5 Abs. 1, 3 ArbnErfG) · V4 keine Freigabe (§ 8 S. 1 ArbnErfG) · V5 keine Sperre (§ 18 Abs. 2 ArbnErfG) | alle vermögenswerten Rechte beim Arbeitgeber; frühere Verfügungen relativ unwirksam (§ 7 Abs. 2 ArbnErfG) | RP2 I/2019 (RP2 III/2019, III/2020, II/2021, I/2022, I/2023, III/2023) |
| Vindikation, § 8 S. 2 PatG (vor Erteilung § 8 S. 1 PatG) | V1 Berechtigter (§ 6 S. 1 PatG; § 7 Abs. 1 ArbnErfG bzw. § 8 S. 1 ArbnErfG) · V2 Anmeldung durch Nichtberechtigten (§ 7 Abs. 2 ArbnErfG, § 24 Abs. 2 ArbnErfG) · V3 Identität der Erfindung; Patentfähigkeit unerheblich (BGH Schleppfahrzeug) · V4 Klage binnen zwei Jahren nach Veröffentlichung der Erteilung (§ 8 S. 3, 4 PatG; § 58 Abs. 1 PatG), unbefristet bei Bösgläubigkeit (§ 8 S. 5 PatG) · Einwendung Verwirkung (§ 242 BGB) | Übertragung des Patents bzw. Mitberechtigung (§ 6 S. 2 PatG); EP: Art. II § 5 IntPatÜG | RP2 I/2019 (RP2 II/2021, III/2021, III/2022, III/2023) |
| Berichtigung der Erfindernennung, § 63 Abs. 2 S. 1 PatG | V1 Nennung unrichtig (§ 63 Abs. 1 S. 1 PatG) · V2 Anspruchsteller ist Erfinder der patentierten Lehre: schöpferischer Beitrag, Schutzfähigkeit unerheblich (BGH Atemgasdrucksteuerung); keine Doppelerfindung mit früherer Anmeldung (§ 6 S. 3 PatG; BGH Schleppfahrzeug); Recht des Anmelders stammt vom Anspruchsteller (§ 37 Abs. 1 S. 2 PatG, § 7 Abs. 1 ArbnErfG) · V3 Gegner: Inhaber und zu Unrecht Benannter · Durchsetzung Patentstreitkammer, keine Schiedsstelle (§ 143 Abs. 1 PatG, § 37 Abs. 1 ArbnErfG, Arb.Erf. 45/11) | Zustimmung gegenüber dem DPMA, unwiderruflich (§ 63 Abs. 2 S. 2 PatG); keine Berichtigung veröffentlichter Druckschriften (§ 63 Abs. 3 PatG) | RP2 I/2019 (RP2 III/2018, III/2019, I/2020, II/2020, III/2023) |
| Anmeldepflicht und Ersatzvornahme, § 13 Abs. 1, 3 ArbnErfG | V1 gemeldete Diensterfindung · V2 Inanspruchnahme · V3 keine Ausnahme (§ 13 Abs. 2 Nr. 1–3 ArbnErfG) · V4 unverzüglich, Patent statt Gebrauchsmuster (§ 13 Abs. 1 S. 2, 3 ArbnErfG; Arb.Erf. 27/20) · V5 angemessene Nachfrist fruchtlos | Anmeldung durch den Arbeitnehmer auf Namen und Kosten des Arbeitgebers; Schadensersatz § 823 Abs. 2 BGB i.V.m. § 13 Abs. 1 ArbnErfG | RP2 I/2019 (§ 13 Abs. 1 S. 1 ArbnErfG als Vorfrage) (RP2 I/2021, II/2023) |
| Betriebsgeheimnis, § 17 ArbnErfG | V1 berechtigte Belange (kein Wahlrecht, Arb.Erf. 23/11 vom 17.01.2013) · V2 Anerkennung der Schutzfähigkeit (§ 17 Abs. 1 ArbnErfG) oder Anrufung der Schiedsstelle (§ 17 Abs. 2 ArbnErfG) | keine Anmeldepflicht (§ 13 Abs. 2 Nr. 3 ArbnErfG); Vergütung mit Nachteilsausgleich (§ 17 Abs. 3 ArbnErfG, RL Nr. 27) | (RP2 III/2019, I/2021, III/2022, III/2023) |
| Übertragung bei Aufgabe, § 16 Abs. 1 ArbnErfG | V1 Anmeldung oder Schutzrecht · V2 vor Erfüllung des Vergütungsanspruchs · V3 Aufgabeabsicht · V4 Mitteilung · V5 Verlangen binnen drei Monaten (§ 16 Abs. 2 ArbnErfG; BGH Zündlanze) | Übertragung auf Kosten des Arbeitnehmers; Vorbehalt des Benutzungsrechts (§ 16 Abs. 3 ArbnErfG) | (RP2 II/2022, II/2023, III/2022) |
| Auslandsfreigabe, § 14 Abs. 2 ArbnErfG | V1 Inanspruchnahme (§ 14 Abs. 1 ArbnErfG) · V2 Staat ohne Anmeldeabsicht · V3 rechtzeitig für die Prioritätsfrist (§ 14 Abs. 2 S. 2 ArbnErfG) | Freigabe, Vorbehalt Benutzungsrecht (§ 14 Abs. 3 ArbnErfG); schutzrechtsfreies Ausland sonst nicht vergütet (RL Nr. 26) | (RP2 II/2019, II/2023) |
| Freie Erfindung: Mitteilung und Angebot, § 18 ArbnErfG, § 19 ArbnErfG | V1 freie Erfindung während des Arbeitsverhältnisses (§ 4 Abs. 3 ArbnErfG) · V2 Mitteilung in Textform, außer offensichtlich nicht verwendbar (§ 18 Abs. 1, 3 ArbnErfG) · V3 Arbeitsbereich im Zeitpunkt des Angebots (§ 19 Abs. 1 ArbnErfG) | nichtausschließliches Benutzungsrecht; Vorrecht erlischt nach drei Monaten (§ 19 Abs. 2 ArbnErfG); Bestreiten binnen drei Monaten (§ 18 Abs. 2 ArbnErfG) | (RP2 III/2020, III/2023) |
| Vergütung in der Insolvenz, § 27 ArbnErfG | V1 Inanspruchnahme vor Eröffnung · V2 Eröffnung · V3 Nr. 1 Verkauf mit Betrieb (Erwerber ab Eröffnung, Arb.Erf. 51/12, 49/16) / Nr. 2 Verwertung im Unternehmen (Masse) / Nr. 3 sonst Angebot an den Arbeitnehmer (ein Jahr, zwei Monate) / Nr. 4 Insolvenzgläubiger | Erwerber, Masse oder Erlös zahlt | (RP2 III/2022) |
| Hochschulerfindung, § 42 ArbnErfG | Nr. 1 Anzeige zwei Monate vor Offenbarung (verfassungsgemäß, BGH selbststabilisierendes Kniegelenk) · Nr. 2 keine Meldung bei Ablehnung der Offenbarung · Nr. 4 30 % der Einnahmen | Vergütung gegen den Dienstherrn | (RP2 III/2020, II/2022, III/2022) |
| Anrufung der Schiedsstelle, § 28 S. 1 ArbnErfG | V1 Streitfall Arbeitgeber–Arbeitnehmer aus dem ArbnErfG (nicht Erfinderschaft, Arb.Erf. 45/11) · V2 schriftlicher Antrag (§ 31 Abs. 1 ArbnErfG) · V3 Schiedsstelle beim DPMA (§ 29 Abs. 1 ArbnErfG) · Besetzung § 30 ArbnErfG, Erweiterung § 32 ArbnErfG | Einigungsvorschlag (§ 34 Abs. 2 ArbnErfG), angenommen ohne schriftlichen Widerspruch binnen eines Monats (§ 34 Abs. 3 ArbnErfG); kostenfrei (§ 36 ArbnErfG) | RP2 I/2019 (verneint für § 63 PatG) (RP2 I/2020, II/2022, II/2018) |
| Klage, § 37 ArbnErfG, § 38 ArbnErfG, § 39 ArbnErfG | V1 Patentstreitkammer (§ 39 Abs. 1 ArbnErfG, § 143 Abs. 1 PatG; Ausnahme § 39 Abs. 2 ArbnErfG) · V2 Schiedsverfahren vorausgegangen (§ 37 Abs. 1 ArbnErfG) oder Ausnahme (§ 37 Abs. 2 Nr. 1–4, Abs. 3, Abs. 4 ArbnErfG) · V3 unbezifferter Antrag (§ 38 ArbnErfG) | Urteil; Kostenerstattung Patentanwalt (§ 143 Abs. 3 PatG) | RP2 I/2019 (RP2 II/2018, III/2018, II/2019, I/2020, II/2021, II/2022) |

### Definitionen

| Begriff | Definition | Quelle |
|---|---|---|
| Erfindung | nur patent- oder gebrauchsmusterfähige Erfindungen | § 2 ArbnErfG |
| Technischer Verbesserungsvorschlag | Vorschlag für sonstige technische Neuerungen, die nicht patent- oder gebrauchsmusterfähig sind; qualifiziert bei ähnlicher Vorzugsstellung wie ein Schutzrecht | § 3 ArbnErfG, § 20 Abs. 1 ArbnErfG |
| Diensterfindung | während der Dauer des Arbeitsverhältnisses gemacht und aus der obliegenden Tätigkeit entstanden (Nr. 1) oder maßgeblich auf Erfahrungen oder Arbeiten des Betriebs beruhend (Nr. 2) | § 4 Abs. 2 ArbnErfG |
| Freie Erfindung | sonstige Erfindung eines Arbeitnehmers; frei gewordene Diensterfindung | § 4 Abs. 3 ArbnErfG, § 8 ArbnErfG |
| Fertige Erfindung | Lehre für den Fachmann ausführbar | Lösung RP2 I/2019 |
| Unverzüglich | ohne schuldhaftes Zögern | § 121 Abs. 1 S. 1 BGB |
| Gesonderte Meldung | hebt sich in der Fülle des betrieblichen Schriftverkehrs als Erfindungsmeldung ab | BGH Fesoterodinhydrogenfumarat (X ZR 148/17, 17.12.2019) |
| Textform | lesbare Erklärung, Person des Erklärenden genannt, dauerhafter Datenträger | § 126b BGB |
| Schriftform | eigenhändige Namensunterschrift | § 126 Abs. 1 BGB |
| Ordnungsgemäße Meldung | § 5 Abs. 1 ArbnErfG erfüllt, Aufgabe, Lösung, Zustandekommen beschrieben (§ 5 Abs. 2 S. 1 ArbnErfG) oder Mängel nicht binnen zwei Monaten beanstandet | § 5 Abs. 3 S. 1 ArbnErfG; Arb.Erf. 34/06 |
| Gleichwertige Dokumentation | Arbeitgeber dokumentiert nach außen die Kenntnis, die die Meldung verschaffen soll, v. a. eigene Anmeldung mit Erfinderbenennung; nicht Eigenanmeldung des Arbeitnehmers | BGH Haftetikett (X ZR 155/03), Initialidee (X ZR 72/10); Arb.Erf. 58/16 |
| Inanspruchnahme | einseitige, empfangsbedürftige Erklärung gegenüber dem Arbeitnehmer; Fiktion nach vier Monaten | § 6 ArbnErfG |
| Freigabe | Erklärung in Textform, die die Diensterfindung frei macht | § 8 S. 1 ArbnErfG |
| Miterfinder | eigener, bestimmbarer schöpferischer Beitrag, nicht selbst patentfähig, aber wesentlich für die Lösung | Arb.Erf. 46/20 |
| Erfinder i.S.v. § 63 PatG, § 8 PatG | schöpferischer Beitrag zum Gegenstand der unter Schutz gestellten Erfindung einschließlich Zustandekommen; Schutzfähigkeit unerheblich | BGH Atemgasdrucksteuerung (X ZR 53/08, 17.05.2011) |
| Doppelerfindung | unabhängig voneinander gemacht; Recht des Erstanmelders | § 6 S. 3 PatG |
| Widerrechtliche Entnahme | wesentlicher Inhalt den Unterlagen eines anderen ohne dessen Einwilligung entnommen | § 21 Abs. 1 Nr. 3 PatG |
| Erfindungswert | Preis, den der Arbeitgeber einem freien Erfinder zahlen würde | § 9 Abs. 2 ArbnErfG, RL Nr. 3 |
| Lizenzanalogie | E = Bezugsgröße × Lizenzsatz | RL Nr. 6, RL Nr. 7, RL Nr. 39 |
| Bezugsgröße | Umsatz oder Erzeugung, Rechnungswert ab Werk; Verrechnungspreis unter Markt mit Aufschlag | RL Nr. 7, RL Nr. 8; Arb.Erf. 29/12 |
| Nettolizenzeinnahme | Bruttolizenzeinnahme abzüglich Kosten und Know-how-Anteil; vereinfacht 20–50 % brutto | RL Nr. 14, RL Nr. 15 |
| Anteilsfaktor | Prozentsatz des Erfindungswerts für den Arbeitnehmer, aus a + b + c | RL Nr. 30, RL Nr. 37 |
| Wertzahl a | 1 Aufgabe mit Lösungsweg … 6 Aufgabe außerhalb des Aufgabenbereichs selbst gestellt | RL Nr. 31 |
| Wertzahl b | 1 bei beruflich geläufigen Überlegungen, betrieblichen Arbeiten/Kenntnissen und technischen Hilfsmitteln; 6 ohne alle drei | RL Nr. 32 |
| Wertzahl c | 1 Leiter Forschung … 4 Ingenieure/Chemiker in der Entwicklung … 8 Ungelernte | RL Nr. 34 |
| Erhebliche Unbilligkeit | objektives Missverhältnis zwischen vereinbarter und gesetzlicher Vergütung bei Abschluss | § 23 Abs. 1 ArbnErfG; BGH Chemische Verbrauchsmaterialien (X ZR 37/22) |
| Wesentliche Änderung | nachträgliches auffallendes Missverhältnis, Festhalten unzumutbar | § 12 Abs. 6 ArbnErfG; Arb.Erf. 29/20 |
| Benutzung der Diensterfindung | nur, soweit ein Patent einem Wettbewerber das Vorgehen verbieten könnte | Arb.Erf. 46/20 |
| Schutzrechtsfreies Ausland | weder Arbeitgeber noch Arbeitnehmer haben dort Schutz; dortige Herstellung nicht vergütet | RL Nr. 26 |
| Arbeitnehmer | weisungsgebundene, fremdbestimmte Arbeit in persönlicher Abhängigkeit | § 611a Abs. 1 S. 1 BGB |

### Fristen

| Frist | Norm | Berechnung | Verschiebung | Gebühr |
|---|---|---|---|---|
| Meldung unverzüglich | § 5 Abs. 1 S. 1 ArbnErfG | § 121 Abs. 1 S. 1 BGB | – | keine |
| Beanstandung der Meldung, zwei Monate ab Eingang | § 5 Abs. 3 S. 1 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Freigabe, sonst Fiktion, vier Monate ab Eingang (a.F.: schriftliche Inanspruchnahme, § 6 Abs. 2 S. 2 ArbnErfG a.F.) | § 6 Abs. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Bestreiten freier Erfindung, drei Monate ab Zugang | § 18 Abs. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Annahme Benutzungsangebot, drei Monate | § 19 Abs. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Festsetzung spätestens drei Monate nach Erteilung | § 12 Abs. 3 S. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Widerspruch gegen Festsetzung, zwei Monate, Textform | § 12 Abs. 4 S. 1 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Übertragungsverlangen, drei Monate ab Zugang der Mitteilung | § 16 Abs. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Unbilligkeit, bis sechs Monate nach Beendigung, Textform | § 23 Abs. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Insolvenz: Angebot spätestens ein Jahr nach Eröffnung; Annahme zwei Monate | § 27 Nr. 3 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Erweiterungsantrag des Gegners, zwei Wochen nach Zustellung | § 32 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine (§ 36 ArbnErfG) |
| Widerspruch gegen Einigungsvorschlag, ein Monat nach Zustellung, schriftlich | § 34 Abs. 3 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine (§ 36 ArbnErfG) |
| Wiedereinsetzung, ein Monat nach Wegfall des Hindernisses, höchstens ein Jahr | § 34 Abs. 4 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Klage ohne abgeschlossenes Schiedsverfahren, sechs Monate nach Anrufung | § 37 Abs. 2 Nr. 2 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | – | Gerichtskosten der Patentstreitsache |
| Vindikationsklage, zwei Jahre nach Veröffentlichung der Erteilung (nach Einspruch ein Jahr nach Abschluss; bösgläubig unbefristet) | § 8 S. 3 bis 5 PatG, § 58 Abs. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB entsprechend | Gerichtskosten |
| EP-Vindikation, zwei Jahre nach Hinweis auf die Erteilung | Art. II § 5 Abs. 2 IntPatÜG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB entsprechend | Gerichtskosten |
| Einspruch wegen widerrechtlicher Entnahme, neun Monate | § 59 Abs. 1 S. 1 PatG, § 21 Abs. 1 Nr. 3 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Einspruchsgebühr nach Anlage zu § 2 Abs. 1 PatKostG |
| Nachanmeldung nach Widerruf wegen Entnahme, ein Monat | § 7 Abs. 2 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | Anmeldegebühr |
| Erfinderbenennung, 15 Monate ab Anmelde- oder Prioritätstag | § 37 Abs. 1 S. 1 PatG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | § 193 BGB | keine |
| Verjährung Vergütung, drei Jahre ab Jahresschluss; Höchstfrist zehn Jahre | § 195 BGB, § 199 Abs. 1 BGB, § 199 Abs. 4 BGB | Jahresschluss § 199 Abs. 1 BGB | Hemmung § 203 BGB, § 204 Abs. 1 Nr. 4 BGB analog (BGH Profilstrangpressverfahren) | – |
| Hochschule: Anzeige vor Offenbarung, in der Regel zwei Monate | § 42 Nr. 1 ArbnErfG | § 187 Abs. 1 BGB, § 188 Abs. 2 BGB | – | keine |

### Weitere Hilfsnormen

- Anwendungsbereich und Übergang: § 1 ArbnErfG (Arbeitnehmer, Beamte, Soldaten), § 43 Abs. 3 ArbnErfG (Meldung vor dem 1.10.2009 → a.F.; ohne Meldung: Zeitpunkt der Meldepflicht, Arb.Erf. 21/09).
- Zugang und Vertretung: § 130 Abs. 1 S. 1 BGB, § 35 Abs. 1 S. 1 GmbHG; Patentabteilung der Konzernmutter als Empfangsvertreterin (Arb.Erf. 49/16).
- Geheimhaltung: § 24 ArbnErfG; Unterrichtung im Anmeldeverfahren: § 15 ArbnErfG; Unabdingbarkeit: § 22 ArbnErfG (Vorausklausel „durch Gehalt abgegolten“ unwirksam, Arb.Erf. 53/99); Fortgeltung nach Ausscheiden: § 26 ArbnErfG.
- Erben: § 1922 Abs. 1 BGB, Vergütungsanspruch vererblich (Arb.Erf. 14/06); Miterfinder verschiedener Arbeitgeber: eigener Arbeitnehmer wie Alleinerfinder (Arb.Erf. 14/06).
- Mitinhaberschaft: § 6 S. 2 PatG, § 741 BGB, § 743 Abs. 2 BGB, § 745 Abs. 1 BGB (BGH Penetrometer, X ZR 142/18), § 747 BGB; Ausgleich für Nichtnutzung (BGH Zylinderrohr, X ZR 165/04).
- Betriebsübergang und Umwandlung: § 613a Abs. 1 BGB; Arb.Erf. 23/21 (14.06.2023 und 14.11.2023), Arb.Erf. 22/22.
- Patentrecht: § 6 PatG, § 7 Abs. 2 PatG, § 8 PatG, § 21 Abs. 1 Nr. 3 PatG, § 37 Abs. 1 PatG, § 58 Abs. 1 PatG, § 59 Abs. 1 PatG, § 63 PatG, § 143 PatG; EP: Art. II § 5 IntPatÜG.
- Vergütungsrichtlinien: RL Nr. 1 (nur Anhaltspunkte), RL Nr. 2 (kein doppelter Ansatz), RL Nr. 10 (Lizenzsätze), RL Nr. 11 (Abstaffelung), RL Nr. 23 (Prüfungszeit drei bis fünf Jahre), RL Nr. 26 (Ausland), RL Nr. 27 (Betriebsgeheimnis), RL Nr. 38 (Wegfall bei geringem Wert), RL Nr. 40, RL Nr. 41 (Zahlungsweise, Laufdauer sechs Jahre bei Gesamtabfindung), RL Nr. 43 (Vergütung bis zur Nichtigerklärung).
