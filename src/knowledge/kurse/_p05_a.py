# -*- coding: utf-8 -*-
"""Kurs p05 (siehe p05_agl_patent.py), Teil A: Überblick über alle Anspruchsgrundlagen des Kurses, Rechtsbestand und Rechtsbehelfe
(Einspruch, Widerruf, Patentfähigkeit als Vorfrage, Nichtigkeitsklage, Beschwerde, Rechtsbeschwerde).

Grundlage sind die Lösungen der TS-Klausuren II/2018 bis III/2023 (klausuren/loesungen/ts) und die RP2-Lösung I/2019; jede Frist,
Gebühr und Voraussetzung ist am Normtext geprüft (data/patg.json, data/patkostg.json mit Anlage, data/intpatueg.json, data/upca.json,
BGB/ZPO/PatKostZV aus dem Gesetze-Cache). Entscheidungen stehen nur im Text, wenn sie im Korpus data/patent_decisions.json stehen;
verlinkt (cases=) werden nur die in patent/cases*.py angelegten. Listenteil: klausuren/normenliste_patent_a.md."""
from ._helpers import intro, mc, fall, frage, fallkette  # noqa: F401

_E = "step:pat_schema_einspruch"
_N = "step:pat_schema_nichtigkeitsklage"
_PF = "step:pat_schema_patentfaehigkeit"

KAPITEL = [
    # ================================================================== p05a Überblick
    dict(id="p05a", titel="Überblick: Anspruchsgrundlagen und Fristen", einheiten=[
        intro("p05a-0", "Die Anspruchsgrundlagen im Überblick",
              "Je Zeile: **Ziel des Mandanten → AGL** · Normenkette (Voraussetzungen in Prüfungsreihenfolge) · Rechtsfolge. "
              "Teil A dieses Kurses behandelt Rechtsbestand und Rechtsbehelfe, Teil B Erteilung, Priorität, Fristversäumnis, "
              "Verletzung und Recht auf das Patent.\n\n"
              "**A · Rechtsbestand und Rechtsbehelfe**\n"
              "**Patent eines Dritten beseitigen, Einspruchsfrist läuft → Einspruch** · § 59 Abs. 1 S. 1 PatG i.V.m. § 21 Abs. 1 PatG: "
              "erteiltes Patent, Veröffentlichung der Erteilung (§ 58 Abs. 1 PatG), Frist neun Monate, jeder (Entnahme: nur der Verletzte), "
              "schriftlich und begründet (§ 59 Abs. 1 S. 2 PatG), Widerrufsgrund des § 21 PatG (§ 59 Abs. 1 S. 3 PatG), Tatsachen im "
              "Einzelnen (§ 59 Abs. 1 S. 4, 5 PatG), Gebühr 200 EUR (Nr. 313 600 Anlage PatKostG, § 6 Abs. 1 S. 1 PatKostG) · "
              "Widerruf oder beschränkte Aufrechterhaltung (§ 61 Abs. 1 S. 2 PatG, § 21 Abs. 2 PatG).\n"
              "**Verletzungsbeklagter will in laufendes Einspruchsverfahren → Beitritt** · § 59 Abs. 2 S. 1 PatG: Einspruch anhängig, "
              "Verletzungsklage oder negative Feststellungsklage nach Abmahnung, Erklärung binnen drei Monaten, Begründung (§ 59 Abs. 2 S. 3, 4 PatG), "
              "Gebühr Nr. 313 600 Anlage PatKostG.\n"
              "**Widerruf durch die Patentabteilung** · § 61 Abs. 1 S. 2 PatG i.V.m. § 21 Abs. 1 Nr. 1 bis 4 PatG: zulässiger Einspruch, "
              "Widerrufsgrund, Umfang nach den Anträgen des Inhabers (§ 21 Abs. 2 PatG) · Wirkung ex tunc (§ 21 Abs. 3 PatG).\n"
              "**Patentfähigkeit (Vorfrage zu Nr. 1)** · §§ 1 bis 5 PatG: Erfindung auf technischem Gebiet (§ 1 Abs. 1 PatG), kein Ausschluss "
              "(§ 1 Abs. 3, 4 PatG, §§ 1a, 2, 2a PatG), Neuheit (§ 3 PatG), erfinderische Tätigkeit (§ 4 PatG), gewerbliche Anwendbarkeit (§ 5 PatG).\n"
              "**Patent nach Ablauf der Einspruchsfrist beseitigen → Nichtigkeitsklage** · § 81 Abs. 1 S. 1 PatG i.V.m. § 22 Abs. 1 PatG "
              "(europäisches Patent: Art. II § 6 Abs. 1 IntPatÜG): BPatG (§ 65 Abs. 1 PatG), keine Klagesperre (§ 81 Abs. 2 S. 1 PatG), "
              "Klage gegen den eingetragenen Inhaber (§ 81 Abs. 1 S. 2 PatG), Form und Inhalt (§ 81 Abs. 4, 5 PatG), Gebühr Nr. 402 100 "
              "Anlage PatKostG · Nichtigerklärung ganz oder teilweise (§ 22 Abs. 2 PatG). Alternative für europäische Patente: EPG "
              "(Art. 32 Abs. 1 lit. d EPGÜ, Art. 33 Abs. 4 EPGÜ).\n"
              "**Beschluss des DPMA angreifen → Beschwerde** · § 73 Abs. 1 PatG: Beschluss, Beteiligter (§ 74 Abs. 1 PatG), Beschwer, "
              "schriftlich beim DPMA binnen eines Monats (§ 73 Abs. 2 S. 1 PatG), Gebühr Nr. 401 100 oder 401 300 Anlage PatKostG · "
              "Abhilfe (§ 73 Abs. 3 PatG) oder Entscheidung des BPatG (§ 79 PatG).\n"
              "**Beschluss des Beschwerdesenats angreifen → Rechtsbeschwerde** · § 100 Abs. 1 PatG: zugelassen (§ 100 Abs. 2 PatG) oder "
              "Verfahrensmangel nach § 100 Abs. 3 PatG, Frist und Begründung (§ 102 Abs. 1, 3, 4 PatG), BGH-Anwalt (§ 102 Abs. 5 PatG) · "
              "Aufhebung und Zurückverweisung (§ 108 PatG).\n\n"
              "**B · Erteilung, Priorität, Fristen, Verletzung, Berechtigung**\n"
              "**Patent erteilt bekommen → Erteilungsbeschluss** · § 49 Abs. 1 PatG: Anmeldung mit Anmeldetag (§ 34 Abs. 3 PatG, "
              "§ 35 Abs. 1 PatG), Übersetzung (§ 35a PatG), Anmeldegebühr (§ 3 Abs. 1 PatKostG, § 6 Abs. 1 S. 2 PatKostG), "
              "Offensichtlichkeitsprüfung (§ 42 PatG), Prüfungsantrag (§ 44 PatG), Prüfungsbescheid (§ 45 PatG), Anhörung (§ 46 Abs. 1 S. 3 PatG), "
              "Änderungen ohne Erweiterung (§ 38 PatG), sonst Zurückweisung (§ 48 PatG).\n"
              "**Anmeldung aufspalten oder retten → Teilung** · § 39 Abs. 1 PatG: Anmeldung anhängig, schriftliche Erklärung, Zeitrang "
              "bleibt (§ 39 Abs. 1 S. 4 PatG), Unterlagen und Gebühren binnen drei Monaten (§ 39 Abs. 3 PatG).\n"
              "**Früheren Zeitrang sichern → Priorität** · innere Priorität § 40 Abs. 1 PatG (Erklärung § 40 Abs. 4 PatG, Rücknahmefiktion "
              "§ 40 Abs. 5 PatG); ausländische Priorität § 41 Abs. 1 PatG i.V.m. Art. 4 A Abs. 1 PVÜ, Art. 4 C Abs. 1 PVÜ; europäische "
              "Nachanmeldung Art. 87 Abs. 1 EPÜ; PCT-Nachanmeldung zur DE-Voranmeldung Art. III § 4 Abs. 4 IntPatÜG.\n"
              "**Versäumte gesetzliche Frist heilen → Wiedereinsetzung** · § 123 Abs. 1 S. 1 PatG: Frist gegenüber DPMA oder BPatG mit "
              "Rechtsnachteil, kein Ausschluss (§ 123 Abs. 1 S. 2 Nr. 1 bis 3 PatG), ohne Verschulden, Antrag und Nachholung binnen zwei "
              "Monaten, höchstens ein Jahr (§ 123 Abs. 2 PatG).\n"
              "**Zurückweisung nach versäumter Amtsfrist beseitigen → Weiterbehandlung** · § 123a Abs. 1 PatG: Frist des DPMA versäumt, "
              "Zurückweisung, Antrag und Nachholung binnen eines Monats (§ 123a Abs. 2 PatG), Gebühr Nr. 313 000 Anlage PatKostG.\n"
              "**Verletzer in Anspruch nehmen → Unterlassung, Schadensersatz, Vernichtung, Auskunft** · § 139 Abs. 1, 2 PatG, § 140a PatG, "
              "§ 140b PatG: Patent in Kraft, Benutzung im Schutzbereich (§ 14 PatG) durch Handlung nach § 9 PatG (mittelbar § 10 PatG), "
              "ohne Zustimmung, kein Vorbenutzungsrecht (§ 12 PatG); Entschädigung vor Erteilung § 33 Abs. 1 PatG.\n"
              "**Erfindung zurückholen → Vindikation** · § 8 S. 1, 2 PatG: Recht auf das Patent (§ 6 PatG), Anmeldung durch Nichtberechtigten "
              "oder widerrechtliche Entnahme, Klage binnen zwei Jahren nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG); daneben "
              "Erfindernennung (§ 63 Abs. 2 PatG) und Nachanmeldung nach Entnahme-Einspruch (§ 7 Abs. 2 PatG).",
              concepts=["pat_einspruch", "pat_nichtigkeitsklage", "pat_beschwerde", "pat_rechtsbeschwerde", "pat_recht_auf_patent"],
              norms=["§ 59 Abs. 1 PatG", "§ 61 Abs. 1 PatG", "§ 81 Abs. 1 PatG", "§ 73 Abs. 1 PatG", "§ 100 Abs. 1 PatG", "§ 139 Abs. 1 PatG"],
              abschnitt="Überblick"),
        intro("p05a-1", "Fristen und Gebühren",
              "Je Zeile: **Frist** · Norm · Berechnung · Verschiebung · Gebühr. Gesetzliche Fristen vor dem DPMA berechnen sich nach "
              "§ 186 BGB, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB (Tag des Ereignisses zählt nicht; Ende am Tag gleicher Zahl, fehlt er, am "
              "Monatsletzten, § 188 Abs. 3 BGB), Verschiebung auf den nächsten Werktag nach § 193 BGB. Vor dem BPatG gilt die ZPO "
              "(§ 99 Abs. 1 PatG i.V.m. § 222 Abs. 1 ZPO, Verschiebung § 222 Abs. 2 ZPO), vor dem BGH im Rechtsbeschwerdeverfahren über "
              "§ 106 Abs. 1 S. 1 PatG. Gebühren: Fälligkeit § 3 Abs. 1 PatKostG, Zahlungsfrist § 6 Abs. 1 PatKostG (gesetzliche Frist "
              "für die Handlung, sonst drei Monate ab Fälligkeit), Folge § 6 Abs. 2 PatKostG, Zahlungstag § 2 PatKostZV (Überweisung: "
              "Gutschrift, Nr. 1; SEPA-Basislastschriftmandat: Eingang beim DPMA, Nr. 3).\n\n"
              "**Einspruch:** neun Monate nach Veröffentlichung der Erteilung · § 59 Abs. 1 S. 1 PatG · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · "
              "§ 193 BGB · 200 EUR (Nr. 313 600 Anlage PatKostG) in der Einspruchsfrist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt der "
              "Einspruch als nicht erhoben (§ 6 Abs. 2 PatKostG); keine Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 1 PatG).\n"
              "**Beitritt:** drei Monate nach Erhebung der Verletzungsklage · § 59 Abs. 2 S. 1 PatG · wie oben · § 193 BGB · 200 EUR "
              "(Nr. 313 600 Anlage PatKostG), fällig mit der Beitrittserklärung (§ 3 Abs. 1 S. 2 Nr. 3 PatKostG), zahlbar in der Beitrittsfrist.\n"
              "**Antrag auf Entscheidung durch das BPatG:** Widerspruch der übrigen Beteiligten binnen zwei Monaten, sonst 15 Monate nach "
              "Ablauf der Einspruchsfrist · § 61 Abs. 2 S. 1 Nr. 1, 2 PatG · 300 EUR (Nr. 400 000 Anlage PatKostG) zusätzlich zur Einspruchsgebühr.\n"
              "**Beschwerde:** ein Monat nach Zustellung, Lauf nur mit Rechtsmittelbelehrung, sonst ein Jahr · § 73 Abs. 2 S. 1 PatG, "
              "§ 47 Abs. 2 S. 2, 3 PatG · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · 500 EUR gegen Einspruchsentscheidungen "
              "(Nr. 401 100 Anlage PatKostG), sonst 200 EUR (Nr. 401 300 Anlage PatKostG), in der Beschwerdefrist, sonst gilt die Beschwerde "
              "als nicht eingelegt (§ 6 Abs. 2 PatKostG); Einsprechender gegen Aufrechterhaltung: keine Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 2 PatG).\n"
              "**Rechtsbeschwerde:** ein Monat nach Zustellung beim BGH (§ 102 Abs. 1 PatG), Begründung ein Monat ab Einlegung, "
              "verlängerbar (§ 102 Abs. 3 PatG) · § 106 Abs. 1 S. 1 PatG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · "
              "§ 222 Abs. 2 ZPO · Gerichtskosten des BGH nach dem GKG, nicht nach dem PatKostG.\n"
              "**Nichtigkeitsklage:** keine Klagefrist, aber Sperre bis zum Ende der Einspruchsmöglichkeit (§ 81 Abs. 2 S. 1 PatG) · "
              "4,5 Gebühren nach dem Streitwert (§ 2 Abs. 2 PatKostG, Nr. 402 100 Anlage PatKostG), fällig mit der Klage (§ 3 Abs. 1 S. 2 Nr. 4 "
              "PatKostG), zahlbar binnen drei Monaten (§ 6 Abs. 1 S. 2 PatKostG), sonst gilt die Klage als zurückgenommen (§ 6 Abs. 2 PatKostG).\n"
              "**Widerspruch des Nichtigkeitsbeklagten:** ein Monat nach Zustellung (§ 82 Abs. 1 PatG), Begründung zwei Monate nach "
              "Zustellung der Klage (§ 82 Abs. 3 S. 2 PatG) · § 99 Abs. 1 PatG i.V.m. § 222 Abs. 1 ZPO · § 222 Abs. 2 ZPO.\n"
              "**Berufung zum BGH:** ein Monat ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung "
              "(§ 110 Abs. 3 PatG); Begründung drei Monate (§ 112 Abs. 2 PatG).\n\n"
              "**Teil B (Erteilung, Priorität, Fristversäumnis, Berechtigung)**\n"
              "**Anmeldegebühr:** drei Monate ab Einreichung (§ 3 Abs. 1 PatKostG, § 6 Abs. 1 S. 2 PatKostG), sonst gilt die Anmeldung als "
              "zurückgenommen (§ 6 Abs. 2 PatKostG).\n"
              "**Übersetzung:** drei Monate, für Englisch und Französisch zwölf Monate, höchstens 15 Monate ab Priorität (§ 35a Abs. 1, 2 PatG), "
              "sonst Rücknahmefiktion (§ 35a Abs. 1 S. 2 PatG).\n"
              "**Prüfungsantrag:** sieben Jahre ab Einreichung (§ 44 Abs. 2 S. 1 PatG), Prüfungsgebühr drei Monate ab Fälligkeit (§ 44 Abs. 2 S. 2 PatG); "
              "sonst Rücknahmefiktion (§ 58 Abs. 3 PatG).\n"
              "**Priorität:** zwölf Monate (§ 40 Abs. 1 PatG, Art. 4 C Abs. 1 PVÜ, Art. 87 Abs. 1 EPÜ); Erklärung innere Priorität zwei Monate "
              "(§ 40 Abs. 4 PatG), Angaben zur Auslandspriorität 16 Monate (§ 41 Abs. 1 PatG); keine Wiedereinsetzung in die Frist für die "
              "Nachanmeldung (§ 123 Abs. 1 S. 2 Nr. 3 PatG).\n"
              "**Teilung:** Unterlagen und Gebühren drei Monate nach Eingang der Teilungserklärung (§ 39 Abs. 3 PatG).\n"
              "**Wiedereinsetzung:** zwei Monate nach Wegfall des Hindernisses, höchstens ein Jahr nach Fristablauf (§ 123 Abs. 2 S. 1, 4 PatG).\n"
              "**Weiterbehandlung:** ein Monat nach Zustellung der Zurückweisung (§ 123a Abs. 2 PatG), 100 EUR (Nr. 313 000 Anlage PatKostG), "
              "keine Wiedereinsetzung (§ 123a Abs. 3 PatG).\n"
              "**Vindikation:** Klage binnen zwei Jahren nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG), nach Entnahme-Einspruch ein Jahr "
              "nach dessen rechtskräftigem Abschluss (§ 8 S. 4 PatG), keine Frist bei Bösgläubigkeit (§ 8 S. 5 PatG); Nachanmeldung nach "
              "Entnahme-Einspruch ein Monat (§ 7 Abs. 2 PatG).",
              concepts=["pat_fristen", "pat_gebuehren", "pat_zahlungsfristen", "pat_faelligkeit"],
              norms=["§ 59 Abs. 1 PatG", "§ 73 Abs. 2 PatG", "§ 102 Abs. 1 PatG", "§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG", "§ 123 Abs. 1 PatG"],
              abschnitt="Überblick"),
        mc("p05a-2", "Fremdes Patent, Erteilung vor drei Monaten",
           "Das Patent eines Wettbewerbers wurde vor drei Monaten erteilt; die Erteilung ist veröffentlicht. Der Mandant will es mit "
           "einer Druckschrift beseitigen, möglichst günstig. Welche AGL wählen Sie?",
           ["Einspruch, § 59 Abs. 1 S. 1 PatG i.V.m. § 21 Abs. 1 Nr. 1 PatG",
            "Nichtigkeitsklage, § 81 Abs. 1 S. 1 PatG i.V.m. § 22 Abs. 1 PatG",
            "Beschränkungsverfahren, § 64 Abs. 1 PatG",
            "Beschwerde gegen den Erteilungsbeschluss, § 73 Abs. 1 PatG"], 0,
           ["**Einspruch.** Die Neun-Monats-Frist des § 59 Abs. 1 S. 1 PatG läuft noch; die Nichtigkeitsklage ist bis zu ihrem Ablauf "
            "gesperrt (§ 81 Abs. 2 S. 1 PatG). Der Einspruch kostet 200 EUR (Nr. 313 600 Anlage PatKostG), jeder trägt grundsätzlich "
            "seine Kosten (§ 62 Abs. 1 PatG). § 64 PatG steht nur dem Inhaber zu; gegen die Erteilung ist der Dritte nicht beschwerdeberechtigt, "
            "weil er am Erteilungsverfahren nicht beteiligt war (§ 74 Abs. 1 PatG)."],
           merke="Einspruchsfrist läuft: Einspruch (§ 59 PatG); danach Nichtigkeitsklage (§ 81 PatG).", level=1,
           concepts=["pat_einspruch", "pat_nichtigkeitsklage"], norms=["§ 59 Abs. 1 PatG", "§ 81 Abs. 2 PatG", "§ 64 Abs. 1 PatG"],
           abschnitt="Welche AGL?"),
        mc("p05a-3", "Verklagt, Einspruchsfrist vorbei",
           "Der Mandant wurde vor einem Monat aus einem deutschen Patent verklagt. Die Einspruchsfrist ist abgelaufen, der Einspruch "
           "eines Dritten ist noch vor der Patentabteilung anhängig. Wie greift er das Patent am schnellsten an?",
           ["Beitritt zum Einspruchsverfahren, § 59 Abs. 2 S. 1 PatG",
            "Nichtigkeitsklage, § 81 Abs. 1 S. 1 PatG",
            "Eigener Einspruch mit Antrag auf Wiedereinsetzung, § 123 Abs. 1 PatG",
            "Nebenintervention im Einspruchsverfahren nach § 66 ZPO"], 0,
           ["**Beitritt.** Wer nachweist, dass gegen ihn Verletzungsklage erhoben ist, kann dem anhängigen Einspruchsverfahren nach "
            "Ablauf der Einspruchsfrist binnen drei Monaten nach Klageerhebung als Einsprechender beitreten (§ 59 Abs. 2 S. 1 PatG). "
            "Die Nichtigkeitsklage ist gesperrt, solange das Einspruchsverfahren anhängig ist (§ 81 Abs. 2 S. 1 PatG); Wiedereinsetzung in "
            "die Einspruchsfrist ist ausgeschlossen (§ 123 Abs. 1 S. 2 Nr. 1 PatG)."],
           merke="Beitritt: anhängiger Einspruch · Verletzungsklage · drei Monate (§ 59 Abs. 2 PatG) · Gebühr Nr. 313 600 Anlage PatKostG.", level=2,
           concepts=["pat_beitritt"], norms=["§ 59 Abs. 2 PatG", "§ 81 Abs. 2 PatG", "§ 123 Abs. 1 PatG"], cases=["pat_bgh_ratschenschluessel"],
           abschnitt="Welche AGL?"),
        mc("p05a-4", "Übersetzung vergessen",
           "Die englischsprachige Anmeldung des Mandanten gilt als zurückgenommen, weil die deutsche Übersetzung nicht binnen zwölf "
           "Monaten eingereicht wurde. Die Kanzleikraft hatte die Frist trotz zuverlässiger Kontrolle falsch notiert. Welche AGL prüfen Sie?",
           ["Wiedereinsetzung in den vorigen Stand, § 123 Abs. 1 S. 1 PatG",
            "Weiterbehandlung, § 123a Abs. 1 PatG",
            "Beschwerde gegen die Rücknahmefiktion, § 73 Abs. 1 PatG",
            "Teilung der Anmeldung, § 39 Abs. 1 PatG"], 0,
           ["**Wiedereinsetzung.** Die Frist des § 35a Abs. 2 S. 1 PatG ist eine gesetzliche Frist, ihre Versäumung führt kraft Gesetzes "
            "zur Rücknahmefiktion (§ 35a Abs. 1 S. 2 PatG). Weiterbehandlung setzt eine Zurückweisung nach Versäumung einer vom DPMA "
            "bestimmten Frist voraus (§ 123a Abs. 1 PatG). Antrag binnen zwei Monaten nach Wegfall des Hindernisses mit Nachholung der "
            "Übersetzung (§ 123 Abs. 2 PatG)."],
           merke="Gesetzliche Frist: Wiedereinsetzung (§ 123 PatG); Amtsfrist mit Zurückweisung: Weiterbehandlung (§ 123a PatG).", level=2,
           concepts=["pat_wiedereinsetzung", "pat_weiterbehandlung"], norms=["§ 123 Abs. 1 PatG", "§ 123a Abs. 1 PatG", "§ 35a Abs. 1 PatG"],
           abschnitt="Welche AGL?"),
        mc("p05a-5", "Mängelfrist versäumt",
           "Die Prüfungsstelle setzte zur Beseitigung von Formmängeln eine Frist von zwei Monaten. Die Anmelderin antwortete nicht; die "
           "Anmeldung wurde zurückgewiesen, der Beschluss vor zwei Wochen zugestellt. Welcher Weg ist am einfachsten?",
           ["Weiterbehandlung, § 123a Abs. 1 PatG: Antrag und Nachholung binnen eines Monats, 100 EUR",
            "Wiedereinsetzung, § 123 Abs. 1 S. 1 PatG: Antrag binnen zwei Monaten",
            "Beschwerde, § 73 Abs. 1 PatG: nur so wird der Beschluss beseitigt",
            "Neuanmeldung mit innerer Priorität, § 40 Abs. 1 PatG"], 0,
           ["**Weiterbehandlung.** Die Anmeldung wurde nach Versäumung einer vom DPMA bestimmten Frist zurückgewiesen (§ 123a Abs. 1 PatG). "
            "Antrag und Nachholung binnen eines Monats nach Zustellung (§ 123a Abs. 2 PatG), Gebühr 100 EUR (Nr. 313 000 Anlage PatKostG); "
            "der Beschluss wird ohne Aufhebung wirkungslos. Auf Verschulden kommt es nicht an. Gegen die Versäumung der Monatsfrist gibt es "
            "keine Wiedereinsetzung (§ 123a Abs. 3 PatG)."],
           merke="Weiterbehandlung: Amtsfrist · Zurückweisung · ein Monat ab Zustellung (§ 123a Abs. 2 PatG) · 100 EUR · kein Verschulden nötig.", level=2,
           concepts=["pat_weiterbehandlung"], norms=["§ 123a Abs. 1 PatG", "§ 123a Abs. 2 PatG", "§ 123a Abs. 3 PatG"],
           abschnitt="Welche AGL?"),
        mc("p05a-6", "Erfindung entwendet",
           "Ein früherer Mitarbeiter eines Kunden hat die Erfindung des Mandanten selbst angemeldet; das Patent ist seit 14 Monaten "
           "erteilt. Der Mandant will das Patent für sich haben. Welche AGL?",
           ["Vindikation, § 8 S. 2 PatG: Übertragung des Patents, Klage binnen zwei Jahren nach Veröffentlichung der Erteilung",
            "Einspruch wegen widerrechtlicher Entnahme, § 59 Abs. 1 S. 1 PatG i.V.m. § 21 Abs. 1 Nr. 3 PatG",
            "Nichtigkeitsklage wegen widerrechtlicher Entnahme, § 81 Abs. 3 PatG",
            "Berichtigung der Erfindernennung, § 63 Abs. 2 PatG"], 0,
           ["**Vindikation.** Der Berechtigte (§ 6 S. 1 PatG) kann vom Patentinhaber die Übertragung verlangen (§ 8 S. 2 PatG); die Klage "
            "ist binnen zwei Jahren nach Veröffentlichung der Erteilung zu erheben (§ 8 S. 3 PatG), läuft hier also noch. Einspruch und "
            "Nichtigkeitsklage beseitigen das Patent nur; die Einspruchsfrist ist zudem abgelaufen. § 63 Abs. 2 PatG ändert nur die Nennung."],
           merke="Patent haben wollen: § 8 PatG; Patent vernichten: § 59, § 81 PatG; Nennung: § 63 Abs. 2 PatG.", level=2,
           concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG", "§ 6 PatG", "§ 21 Abs. 1 Nr. 3 PatG"], abschnitt="Welche AGL?"),
        mc("p05a-7", "Benutzung vor der Erteilung",
           "Ein Wettbewerber stellt die angemeldete Vorrichtung seit der Veröffentlichung des Offenlegungshinweises her, obwohl er die "
           "Offenlegungsschrift kennt. Das Patent wurde gestern erteilt. Was kann der Mandant für die Zeit vor der Erteilung verlangen?",
           ["Angemessene Entschädigung, § 33 Abs. 1 PatG; weitergehende Ansprüche sind ausgeschlossen",
            "Schadensersatz nach § 139 Abs. 2 PatG für den gesamten Zeitraum",
            "Unterlassung und Vernichtung für die Vergangenheit, § 139 Abs. 1 PatG, § 140a PatG",
            "Nichts, weil vor der Erteilung kein Schutz besteht"], 0,
           ["**§ 33 Abs. 1 PatG.** Von der Veröffentlichung des Hinweises nach § 32 Abs. 5 PatG an schuldet, wer den Gegenstand der "
            "Anmeldung benutzt, obwohl er es wusste oder wissen musste, eine angemessene Entschädigung; weitergehende Ansprüche sind "
            "ausgeschlossen. Die Verletzungsansprüche der § 139 PatG, § 140a PatG, § 140b PatG entstehen erst mit der Veröffentlichung "
            "der Erteilung (§ 58 Abs. 1 S. 3 PatG). Verjährung frühestens ein Jahr nach Erteilung (§ 33 Abs. 3 S. 1 PatG)."],
           merke="Vor Erteilung: Entschädigung § 33 PatG; ab Veröffentlichung der Erteilung: § 139 PatG ff.", level=1,
           concepts=["pat_verletzung", "pat_schadensersatz"], norms=["§ 33 Abs. 1 PatG", "§ 139 Abs. 2 PatG", "§ 58 Abs. 1 PatG"],
           abschnitt="Welche AGL?"),
        *fallkette("p05a-8", "Ein Patent, mehrere Wege (nach TS III/2021)",
            "Die Erfindungen GmbH wird aus dem deutschen Patent DE 456 B1 abgemahnt; die Erteilung wurde vor fünf Monaten veröffentlicht. "
            "Herr Reich, der ohne Arbeitsverhältnis gemeinsam mit dem Geschäftsführer der Inhaberin den Stock entwickelt hat, ist im "
            "Patent nicht als Erfinder genannt.",
            [frage("Welche AGL wählt die Erfindungen GmbH gegen den Rechtsbestand?", 0,
                   ["**Einspruch.** Die Frist des § 59 Abs. 1 S. 1 PatG läuft noch rund vier Monate; „jeder“ ist einspruchsberechtigt, ein "
                    "Rechtsschutzbedürfnis ist nicht darzulegen. Die Nichtigkeitsklage ist bis zum Ende des Einspruchsverfahrens gesperrt "
                    "(§ 81 Abs. 2 S. 1 PatG)."],
                   optionen=["Einspruch, § 59 Abs. 1 PatG i.V.m. § 21 Abs. 1 PatG", "Nichtigkeitsklage, § 81 Abs. 1 PatG",
                             "Beitritt, § 59 Abs. 2 PatG", "Beschränkungsantrag, § 64 Abs. 1 PatG"],
                   merke="Neun Monate ab Veröffentlichung der Erteilung: Einspruch; Nichtigkeitsklage gesperrt (§ 81 Abs. 2 PatG).",
                   titel="Weg gegen den Rechtsbestand", norms=["§ 59 Abs. 1 PatG", "§ 81 Abs. 2 PatG"], step=_E + ".1"),
             frage("Kann Herr Reich Einspruch wegen widerrechtlicher Entnahme erheben?", False,
                   ["**Nein!** Die Entnahme kann nur der Verletzte geltend machen (§ 59 Abs. 1 S. 1 PatG). Wer an der Erfindung selbst "
                    "mitberechtigt ist (§ 6 S. 2 PatG), ist gegenüber dem Mitberechtigten nicht Verletzter; sein Entnahme-Einspruch ist "
                    "unzulässig (BPatG Fondue-Einrichtung)."],
                   merke="Mitberechtigter ist kein Verletzter im Sinne von § 21 Abs. 1 Nr. 3 PatG.", titel="Entnahme durch Miterfinder",
                   level=2, norms=["§ 59 Abs. 1 PatG", "§ 21 Abs. 1 Nr. 3 PatG", "§ 6 PatG"], cases=["pat_bpatg_fondue_einrichtung"]),
             frage("Welcher Anspruch verschafft Herrn Reich seine Beteiligung am Patent?", 1,
                   ["**§ 8 PatG.** Mehreren gemeinsamen Erfindern steht das Recht auf das Patent gemeinschaftlich zu (§ 6 S. 2 PatG). "
                    "Der übergangene Mitberechtigte kann nach § 8 S. 1, 2 PatG die Einräumung einer Mitberechtigung verlangen, binnen zwei "
                    "Jahren nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG). Widerruf oder Nichtigerklärung nähmen ihm das Recht mit."],
                   optionen=["Einspruch und Nachanmeldung mit Priorität, § 7 Abs. 2 PatG", "Einräumung einer Mitberechtigung, § 8 S. 1, 2 PatG",
                             "Schadensersatz, § 139 Abs. 2 PatG", "Nichtigkeitsklage, § 81 Abs. 3 PatG"],
                   merke="Miterfinder: Mitberechtigung über § 8 PatG binnen zwei Jahren (§ 8 S. 3 PatG).", titel="Vindikation des Miterfinders",
                   level=2, norms=["§ 8 PatG", "§ 6 PatG"], concepts=["pat_recht_auf_patent"]),
             frage("Kann Herr Reich zusätzlich verlangen, als Miterfinder genannt zu werden?", True,
                   ["**Ja!** Ist die Person des Erfinders unrichtig angegeben, sind Patentinhaber und zu Unrecht Benannter dem Erfinder "
                    "verpflichtet, der Berichtigung gegenüber dem DPMA zuzustimmen (§ 63 Abs. 2 S. 1 PatG). Bereits veröffentlichte Druckschriften "
                    "werden nicht berichtigt (§ 63 Abs. 3 PatG)."],
                   merke="Erfindernennung: Zustimmung zur Berichtigung, § 63 Abs. 2 S. 1 PatG.", titel="Erfindernennung",
                   norms=["§ 63 Abs. 2 PatG"], concepts=["pat_erfinderbenennung"]),
            ],
            abschnitt="Klausurfall", level=1, concepts=["pat_einspruch", "pat_recht_auf_patent"]),
    ]),
    # ================================================================== p05b § 59 PatG
    dict(id="p05b", titel="§ 59 PatG: Einspruch", einheiten=[
        intro("p05b-0", "Prüfungsschema",
              "**AGL:** § 59 Abs. 1 S. 1 PatG i.V.m. § 21 Abs. 1 PatG (Entscheidung § 61 Abs. 1 S. 2 PatG)\n\n"
              "**A · Zulässigkeit**\n"
              "**V1 Statthaftigkeit** – § 59 Abs. 1 S. 1 PatG: Einspruch „gegen das Patent“, also erteiltes deutsches Patent nach "
              "Veröffentlichung der Erteilung im Patentblatt (§ 58 Abs. 1 S. 1, 3 PatG). Ein vor der Veröffentlichung erhobener Einspruch "
              "ist unzulässig und wird durch die spätere Veröffentlichung nicht geheilt. Erklärung auslegen: „für nichtig erklären“ oder "
              "„vollständiger Widerruf“ eines Dritten ist Einspruch (§ 133 BGB).\n"
              "**V2 Einsprechender** – § 59 Abs. 1 S. 1 PatG: jeder, kein Rechtsschutzbedürfnis (auch nicht nach Wegfall der Wirkung "
              "wegen Doppelschutzes, BGH Kornfeinung); bei widerrechtlicher Entnahme nur der Verletzte; Identität muss bis Fristende "
              "zweifelsfrei feststehen (BPatG Gabelschlüssel). Unzulässig ist der Einspruch des Inhabers selbst.\n"
              "**V3 Frist** – neun Monate nach Veröffentlichung der Erteilung (§ 59 Abs. 1 S. 1 PatG) · Berechnung § 187 Abs. 1 BGB, "
              "§ 188 Abs. 2 BGB · Verschiebung § 193 BGB · maßgeblich ist der Eingang beim DPMA (München, Jena, Berlin); ein "
              "Patentinformationszentrum nimmt nur Anmeldungen entgegen (§ 34 Abs. 2 S. 1 PatG) · keine Wiedereinsetzung "
              "(§ 123 Abs. 1 S. 2 Nr. 1 PatG).\n"
              "**V4 Form** – schriftlich (§ 59 Abs. 1 S. 2 PatG; elektronisch § 125a Abs. 1 PatG), deutsch (§ 126 PatG); Vertretung: "
              "Vollmacht bei Angestellten (§ 15 Abs. 1 DPMAV), bei Anwälten Prüfung nur auf Rüge (§ 15 Abs. 4 DPMAV); Inlandsvertreter nur "
              "ohne Sitz im Inland (§ 25 Abs. 1 PatG).\n"
              "**V5 Gebühr** – 200 EUR für jeden Einsprechenden gesondert (Nr. 313 600 Anlage PatKostG, Vorbemerkung Teil A Abs. 2), "
              "fällig mit Einreichung (§ 3 Abs. 1 S. 1 PatKostG), zahlbar innerhalb der Einspruchsfrist (§ 6 Abs. 1 S. 1 PatKostG); nicht, "
              "nicht vollständig oder nicht rechtzeitig gezahlt: Einspruch gilt als nicht erhoben (§ 6 Abs. 2 PatKostG); Zahlungstag "
              "§ 2 PatKostZV; keine Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 1 PatG).\n"
              "**V6 Widerrufsgrund** – nur die Behauptung eines Grundes des § 21 Abs. 1 PatG (§ 59 Abs. 1 S. 3 PatG); mangelnde Klarheit "
              "oder Uneinheitlichkeit genügen nicht.\n"
              "**V7 Substantiierung** – Tatsachen im Einzelnen (§ 59 Abs. 1 S. 4 PatG), bis Fristende nachzureichen (§ 59 Abs. 1 S. 5 PatG); "
              "ein substantiierter Grund gegen einen Anspruch genügt (BGH Automatisches Fahrzeuggetriebe); ob die Entgegenhaltung "
              "wirklich Stand der Technik ist, betrifft die Begründetheit (BGH Leistungshalbleiterbauelement).\n\n"
              "**B · Begründetheit**\n"
              "**V8 Widerrufsgrund liegt vor** – § 21 Abs. 1 Nr. 1 bis 4 PatG (Kapitel §§ 21, 61 PatG); Prüfung von Amts wegen "
              "(§ 59 Abs. 5 PatG i.V.m. § 46 Abs. 1 S. 1 PatG).\n\n"
              "**C · Sonderformen**\n"
              "**Beitritt** – § 59 Abs. 2 PatG: Einspruch anhängig, Dritter, Verletzungsklage gegen ihn (auch Verfügungsantrag, BGH "
              "Ratschenschlüssel) oder negative Feststellungsklage nach Abmahnung, nach Ablauf der Einspruchsfrist, Erklärung binnen drei "
              "Monaten nach Klageerhebung, Begründung in derselben Frist (§ 59 Abs. 2 S. 3 PatG), § 59 Abs. 1 S. 3 bis 5 PatG entsprechend "
              "(§ 59 Abs. 2 S. 4 PatG), Gebühr Nr. 313 600 Anlage PatKostG (§ 3 Abs. 1 S. 2 Nr. 3 PatKostG).\n"
              "**Gemeinsamer Einspruch** – mehrere Einsprechende in einem Schriftsatz zahlen je 200 EUR; eine Gebühr ist zuzuordnen, "
              "im Zweifel dem zuerst Genannten.\n"
              "**Teileinspruch** – Antrag auf Widerruf nur einzelner Ansprüche; er bestimmt den Umfang des Angriffs.\n\n"
              "**⇒ Rechtsfolge:** Verfahren vor der Patentabteilung (§ 59 Abs. 3 bis 5 PatG: Anhörung auf Antrag, Amtsermittlung), "
              "Entscheidung durch Beschluss (§ 61 Abs. 1 S. 1 PatG): unzulässiger Einspruch wird verworfen; auf einen zulässigen Einspruch "
              "Aufrechterhaltung, beschränkte Aufrechterhaltung oder Widerruf (§ 61 Abs. 1 S. 2 PatG). Rücknahme: Fortsetzung von Amts wegen "
              "(§ 61 Abs. 1 S. 3 PatG), außer beim reinen Entnahme-Einspruch (§ 61 Abs. 1 S. 4 PatG). Kosten: jeder trägt seine, Abweichung "
              "nach Billigkeit (§ 62 Abs. 1 PatG). Auf Antrag entscheidet das BPatG (§ 61 Abs. 2 PatG, 300 EUR Nr. 400 000 Anlage PatKostG).\n\n"
              "**Klausurfallen:** verfrühter Einspruch; Abgabe beim PIZ; Gebühr nur einmal für mehrere Einsprechende; falsche Gebührennummer "
              "(schadet nicht, wenn der Betrag stimmt), falscher Betrag (schadet); Vorbenutzung ohne Zeitpunkt; Bedienungsanleitung nur "
              "mit „© 2019“; Zeugenangebot statt Tatsachenvortrag; Verweis auf „Fachwissen“ ohne Begründung; Entnahme-Einspruch des "
              "Mitberechtigten; Insolvenz oder Rücknahme beenden das Verfahren nicht.\n\n"
              "**In den Klausuren:** TS II/2018 (fünf Einsprüche: verfrüht, Vorbenutzung ohne Datum, gemeinsamer Einspruch mit einer Gebühr), "
              "TS III/2018, TS II/2019 (unsubstantiierte Vorbenutzung), TS II/2020 (Einspruchsschriftsatz), TS I/2021 (sieben Vorbenutzungen), "
              "TS III/2021 (Insolvenz, Entnahme), TS I/2022 (drei Einsprüche: undatierte Anleitung, Gebühr 120 statt 200 EUR, Teileinspruch), "
              "TS II/2022, TS III/2022, TS I/2023 (PIZ, unvollständige Gebühr, Beitritt), TS II/2023 (ältere Anmeldung als Begründung).",
              concepts=["pat_einspruch", "pat_beitritt", "pat_widerrufsgruende", "pat_gebuehren"],
              norms=["§ 59 Abs. 1 PatG", "§ 59 Abs. 2 PatG", "§ 61 Abs. 1 PatG", "§ 21 Abs. 1 PatG", "§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG"],
              cases=["pat_bgh_leistungshalbleiterbauelement", "pat_bgh_automatisches_fahrzeuggetriebe", "pat_bgh_ratschenschluessel",
                     "pat_bgh_kornfeinung", "pat_bpatg_gabelschluessel"],
              abschnitt="Normenkette"),
        intro("p05b-1", "Definitionen",
              "**Einspruch:** Rechtsbehelf, mit dem jeder (bei widerrechtlicher Entnahme nur der Verletzte) binnen neun Monaten nach "
              "Veröffentlichung der Erteilung den Widerruf eines erteilten Patents aus den Gründen des § 21 PatG verlangt "
              "(§ 59 Abs. 1 S. 1, 3 PatG).\n"
              "**Tatsachen im Einzelnen (Substantiierung):** Die Begründung muss die maßgeblichen Umstände so darlegen, dass Patentinhaber "
              "und Patentabteilung daraus ohne eigene Ermittlungen abschließende Folgerungen für das Vorliegen eines Widerrufsgrunds "
              "ziehen können (§ 59 Abs. 1 S. 4 PatG; ständige Rechtsprechung, BGH Leistungshalbleiterbauelement). Ob der Vortrag zutrifft, "
              "ist Frage der Begründetheit.\n"
              "**Substantiierte Vorbenutzung:** Angabe, was (Gegenstand mit Zuordnung zu den Merkmalen), wann (vor dem Zeitrangtag), wo, "
              "durch wen und unter welchen Umständen (Öffentlichkeit) benutzt wurde, mit Beweismitteln (Rechtsprechung des BPatG; "
              "Lösungen TS II/2019, TS I/2021).\n"
              "**Beitritt:** Eintritt eines Dritten, gegen den Verletzungsklage oder nach Abmahnung negative Feststellungsklage erhoben ist, "
              "als Einsprechender in ein anhängiges Einspruchsverfahren nach Ablauf der Einspruchsfrist (§ 59 Abs. 2 PatG).\n"
              "**Verletzter (Entnahme):** derjenige, dessen Beschreibungen, Zeichnungen, Modellen, Gerätschaften, Einrichtungen oder "
              "Verfahren der wesentliche Inhalt des Patents ohne Einwilligung entnommen wurde (§ 21 Abs. 1 Nr. 3 PatG); nicht der "
              "Mitberechtigte gegenüber dem anderen Mitberechtigten (BPatG Fondue-Einrichtung).\n"
              "**Sonstige Handlung (§ 6 PatKostG):** auch der Einspruch; deshalb gilt die Zahlungsfrist des § 6 Abs. 1 S. 1 PatKostG und "
              "die Fiktion des § 6 Abs. 2 PatKostG (BGH Verspätete Zahlung der Einspruchsgebühr).",
              concepts=["pat_einspruch", "pat_beitritt"], norms=["§ 59 Abs. 1 PatG", "§ 59 Abs. 2 PatG", "§ 21 Abs. 1 Nr. 3 PatG"],
              cases=["pat_bgh_leistungshalbleiterbauelement", "pat_bpatg_fondue_einrichtung", "pat_bgh_einspruchsgebuehr_verspaetet"],
              abschnitt="Definitionen"),
        mc("p05b-2", "Einspruchsfrist",
           "Die Erteilung des Patents wurde am Mittwoch, 12.07.2017, im Patentblatt veröffentlicht. Wann endet die Einspruchsfrist?",
           ["Donnerstag, 12.04.2018", "Mittwoch, 11.04.2018", "Montag, 16.04.2018", "Donnerstag, 12.07.2018"], 0,
           ["**Do 12.04.2018.** Die Frist beträgt neun Monate nach der Veröffentlichung der Erteilung (§ 59 Abs. 1 S. 1 PatG). Der Tag "
            "der Veröffentlichung zählt nicht mit (§ 187 Abs. 1 BGB); die Frist endet mit Ablauf des Tages gleicher Zahl im neunten "
            "Monat (§ 188 Abs. 2 BGB). Der 12.04.2018 ist ein Donnerstag, eine Verschiebung nach § 193 BGB entfällt (TS II/2019)."],
           merke="Frist § 59 Abs. 1 S. 1 PatG · Berechnung § 187 Abs. 1, § 188 Abs. 2 BGB · Verschiebung § 193 BGB · keine Wiedereinsetzung.",
           level=1, concepts=["pat_fristen"], norms=["§ 59 Abs. 1 PatG"], step=_E + ".1.1", abschnitt="Definitionen und Normen"),
        mc("p05b-3", "Einspruchsgebühr",
           "Welche Gebühr kostet der Einspruch, bis wann ist sie zu zahlen, und was folgt aus der Nichtzahlung?",
           ["200 EUR (Nr. 313 600 Anlage PatKostG), zahlbar in der Einspruchsfrist; sonst gilt der Einspruch als nicht erhoben, "
            "Wiedereinsetzung ausgeschlossen",
            "200 EUR, zahlbar binnen drei Monaten nach Einreichung des Einspruchs",
            "120 EUR (Nr. 313 700 Anlage PatKostG), zahlbar in der Einspruchsfrist",
            "200 EUR je Schriftsatz, auch wenn mehrere Einsprechende gemeinsam einsprechen"], 0,
           ["**Nr. 313 600, § 6 Abs. 1 S. 1, Abs. 2 PatKostG.** Ist für die Handlung eine gesetzliche Frist bestimmt, ist die Gebühr in "
            "dieser Frist zu zahlen (§ 6 Abs. 1 S. 1 PatKostG); sonst gilt der Einspruch als nicht erhoben (§ 6 Abs. 2 PatKostG). "
            "Wiedereinsetzung ist ausgeschlossen (§ 123 Abs. 1 S. 2 Nr. 1 PatG). Die Gebühr fällt für jeden Einsprechenden gesondert an "
            "(Vorbemerkung Teil A Abs. 2 der Anlage). Nr. 313 700 betrifft das Beschränkungsverfahren nach § 64 PatG."],
           merke="Nr. 313 600 · in der Einspruchsfrist (§ 6 Abs. 1 S. 1 PatKostG) · sonst nicht erhoben (§ 6 Abs. 2 PatKostG) · § 123 Abs. 1 S. 2 Nr. 1 PatG.",
           level=1, concepts=["pat_gebuehren", "pat_zahlungsfristen"], norms=["§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG", "§ 123 Abs. 1 PatG"],
           cases=["pat_bgh_einspruchsgebuehr_verspaetet", "pat_bpatg_einspruchsgebuehren_gemeinsam"], step=_E + ".1.2",
           abschnitt="Definitionen und Normen"),
        fall("p05b-4", "Nur Unklarheit gerügt",
             "Herr Müller erhebt fristgerecht Einspruch, zahlt 200 EUR und begründet ausführlich, Anspruch 2 sei unklar, weil "
             "„einstückig“ und „lösbar verbunden“ einander widersprächen. Weitere Gründe nennt er nicht.",
             "Ist der Einspruch zulässig?", False,
             ["**Nein!** Der Einspruch kann nur auf die Behauptung eines Widerrufsgrundes des § 21 PatG gestützt werden "
              "(§ 59 Abs. 1 S. 3 PatG). Der Katalog ist abschließend; mangelnde Klarheit gehört nicht dazu. Herr Müller muss den "
              "Merkmalswiderspruch als unzulässige Erweiterung (§ 21 Abs. 1 Nr. 4 PatG) oder mangelnde Ausführbarkeit (§ 21 Abs. 1 Nr. 2 PatG) "
              "fassen und bis Fristende mit Tatsachen belegen (§ 59 Abs. 1 S. 5 PatG; TS III/2021)."],
             merke="Nur Gründe des § 21 PatG (§ 59 Abs. 1 S. 3 PatG); Klarheit ist keiner.", level=1,
             concepts=["pat_widerrufsgruende"], norms=["§ 59 Abs. 1 PatG", "§ 21 Abs. 1 PatG"], step=_E + ".1.3",
             abschnitt="Definitionen und Normen"),
        fall("p05b-5", "Ältere Anmeldung gegen die erfinderische Tätigkeit",
             "Die Trausnitz GmbH stützt ihren fristgerechten Einspruch darauf, Anspruch 1 sei gegenüber D1 und der älteren, "
             "nachveröffentlichten europäischen Anmeldung EP 3 nicht erfinderisch; sie ordnet jedes Merkmal einer Fundstelle zu.",
             "Ist der Einspruch unzulässig, weil eine ältere Anmeldung bei der erfinderischen Tätigkeit nicht berücksichtigt wird?", False,
             ["**Nein!** Dass ein auf mangelnde Patentfähigkeit gestützter Einspruch mit einer älteren Anmeldung begründet wird, die nach "
              "§ 4 S. 2 PatG bei der erfinderischen Tätigkeit außer Betracht bleibt, steht der Zulässigkeit nicht entgegen, gleich ob "
              "Neuheit oder erfinderische Tätigkeit gerügt wird (BGH Leistungshalbleiterbauelement). Ob die Begründung trägt, ist eine "
              "Frage der Begründetheit (TS I/2022, TS II/2023)."],
             merke="Zulässigkeit: substantiierter Vortrag; Richtigkeit: Begründetheit.", level=2,
             concepts=["pat_einspruch"], norms=["§ 59 Abs. 1 PatG", "§ 4 PatG", "§ 3 Abs. 2 PatG"], cases=["pat_bgh_leistungshalbleiterbauelement"],
             step=_E + ".1.3", abschnitt="Definitionen und Normen"),
        fall("p05b-6", "Angriff auf einen von zwei Nebenansprüchen",
             "Das Patent hat zwei unabhängige Ansprüche 1 (Vorrichtung) und 6 (Verfahren). Die Einsprechende beantragt den Widerruf "
             "insgesamt, begründet aber nur gegen Anspruch 1, Merkmal für Merkmal.",
             "Ist der Einspruch zulässig?", True,
             ["**Ja!** Die Zulässigkeit erfordert nicht, dass der Einsprechende gegen sämtliche Nebenansprüche Widerrufsgründe vorträgt; "
              "er kann die Patentfähigkeit nur eines Nebenanspruchs angreifen (BGH Automatisches Fahrzeuggetriebe). Ist der Einspruch "
              "zulässig, entscheidet die Patentabteilung, ob und in welchem Umfang das Patent aufrechterhalten wird (§ 61 Abs. 1 S. 2 PatG)."],
             merke="Ein substantiierter Grund gegen einen Anspruch macht den Einspruch zulässig.", level=2,
             concepts=["pat_einspruch"], norms=["§ 59 Abs. 1 PatG", "§ 61 Abs. 1 PatG"], cases=["pat_bgh_automatisches_fahrzeuggetriebe"],
             step=_E + ".1.3", abschnitt="Definitionen und Normen"),
        fall("p05b-7", "Rücknahme und Insolvenz der Einsprechenden",
             "Die einzige Einsprechende stützt ihren Einspruch auf fehlende Patentfähigkeit und unzulässige Erweiterung. Über ihr "
             "Vermögen wird das Insolvenzverfahren eröffnet; der Verwalter nimmt den Einspruch zurück.",
             "Ist das Einspruchsverfahren damit beendet?", False,
             ["**Nein!** Nimmt der Einsprechende den Einspruch zurück, wird das Verfahren von Amts wegen ohne ihn fortgesetzt "
              "(§ 61 Abs. 1 S. 3 PatG); das gilt auch in Beschwerde und Rechtsbeschwerde (BGH Gruppierungssystem). Beendet ist es nur, "
              "wenn der Einspruch allein auf widerrechtliche Entnahme gestützt war (§ 61 Abs. 1 S. 4 PatG). Die Insolvenz kann das Verfahren "
              "allenfalls unterbrechen (§ 240 ZPO entsprechend), nicht beenden (TS III/2021)."],
             merke="Rücknahme: Fortsetzung von Amts wegen (§ 61 Abs. 1 S. 3 PatG); Ende nur beim reinen Entnahme-Einspruch (S. 4).", level=2,
             concepts=["pat_einspruch"], norms=["§ 61 Abs. 1 PatG"], cases=["pat_bgh_gruppierungssystem"], step=_E + ".3",
             abschnitt="Definitionen und Normen"),
        mc("p05b-8", "Entscheidung durch das BPatG",
           "Seit Ablauf der Einspruchsfrist sind 16 Monate vergangen; die Patentabteilung hat weder geladen noch entschieden. Die "
           "Einsprechende will eine gerichtliche Entscheidung. Was gilt?",
           ["Auf ihren Antrag entscheidet der Beschwerdesenat (§ 61 Abs. 2 S. 1 Nr. 2 PatG), Gebühr 300 EUR, außer die "
            "Patentabteilung lädt oder entscheidet binnen drei Monaten",
            "Sie kann Untätigkeitsbeschwerde nach § 73 Abs. 1 PatG einlegen",
            "Sie muss die Zustimmung der Inhaberin einholen; ohne sie bleibt es bei der Patentabteilung",
            "Sie kann jetzt Nichtigkeitsklage erheben, weil die Einspruchsfrist abgelaufen ist"], 0,
           ["**§ 61 Abs. 2 S. 1 Nr. 2 PatG.** Auf Antrag nur eines Beteiligten entscheidet der Beschwerdesenat, wenn mindestens 15 Monate "
            "seit Ablauf der Einspruchsfrist vergangen sind. Das gilt nicht, wenn die Patentabteilung binnen drei Monaten nach Zugang des "
            "Antrags lädt oder entscheidet (§ 61 Abs. 2 S. 2 PatG). Gebühr 300 EUR zusätzlich (Nr. 400 000 Anlage PatKostG). Die "
            "Nichtigkeitsklage bleibt gesperrt (§ 81 Abs. 2 S. 1 PatG)."],
           merke="§ 61 Abs. 2 PatG: Nr. 1 Antrag ohne Widerspruch binnen zwei Monaten, Nr. 2 nach 15 Monaten; 300 EUR.", level=3,
           concepts=["pat_einspruch"], norms=["§ 61 Abs. 2 PatG", "§ 81 Abs. 2 PatG"], step=_E + ".3", abschnitt="Definitionen und Normen"),
        *fallkette("p05b-9", "Fünf Einsprüche (nach TS II/2018)",
            "Die Erteilung des Patents der P (Anmeldetag 19.03.2015) wurde am Do 29.09.2016 veröffentlicht. A erhob am 11.08.2016 "
            "Einspruch, nach dem Erteilungsbeschluss. B stützt sich auf einen Katalog vom Mai 2015 und einen Kauf „einige Monate vor "
            "Herausgabe des Katalogs“. C und D reichen am letzten Tag der Frist einen gemeinsamen Einspruch ein und zahlen einmal 200 EUR.",
            [frage("Ist der Einspruch der A statthaft?", False,
                   ["**Nein!** Einspruch ist „innerhalb von neun Monaten nach der Veröffentlichung der Erteilung“ gegen „das Patent“ zu "
                    "erheben (§ 59 Abs. 1 S. 1 PatG); die Wirkungen des Patents treten erst mit der Veröffentlichung ein (§ 58 Abs. 1 S. 3 PatG). "
                    "Der verfrühte Einspruch ist unzulässig und wird durch die spätere Veröffentlichung nicht geheilt. A hätte bis zum "
                    "Fristende erneut einsprechen müssen."],
                   merke="Einspruch erst nach Veröffentlichung der Erteilung (§ 59 Abs. 1 S. 1, § 58 Abs. 1 PatG).", titel="V1 Statthaftigkeit",
                   norms=["§ 59 Abs. 1 PatG", "§ 58 Abs. 1 PatG"], step=_E + ".1.1"),
             frage("Bis wann konnte Einspruch erhoben werden?", 1,
                   ["**Do 29.06.2017.** Neun Monate nach der Veröffentlichung vom 29.09.2016 (§ 59 Abs. 1 S. 1 PatG); der Tag der "
                    "Veröffentlichung zählt nicht (§ 187 Abs. 1 BGB), Ende am Tag gleicher Zahl (§ 188 Abs. 2 BGB). Der 29.06.2017 ist ein "
                    "Donnerstag, § 193 BGB greift nicht."],
                   optionen=["Mi 28.06.2017", "Do 29.06.2017", "Mo 03.07.2017", "Fr 29.09.2017"],
                   merke="Neun Monate ab Veröffentlichung: § 187 Abs. 1, § 188 Abs. 2 BGB.", titel="V3 Frist", step=_E + ".1.1"),
             frage("Ist der Einspruch der B ausreichend substantiiert?", False,
                   ["**Nein!** Der Katalog erschien nach dem Anmeldetag und ist kein Stand der Technik (§ 3 Abs. 1 S. 2 PatG). Für die "
                    "Vorbenutzung fehlt die Behauptung, dass sie vor dem 19.03.2015 lag („einige Monate vor Mai“ kann März oder April "
                    "2015 sein), ebenso Ort, Abnehmer und Umstände. Nachreichung war nur bis Fristende möglich (§ 59 Abs. 1 S. 4, 5 PatG)."],
                   merke="Vorbenutzung: was, wann (vor dem Zeitrang), wo, wer, wie öffentlich – bis Fristende.", titel="V7 Substantiierung",
                   level=2, norms=["§ 59 Abs. 1 PatG", "§ 3 Abs. 1 PatG"], step=_E + ".1.3"),
             frage("Gilt der Einspruch von C und D für beide als erhoben?", False,
                   ["**Nein!** Die Gebühr Nr. 313 600 wird für jeden Einsprechenden gesondert erhoben, auch bei gemeinsamem Schriftsatz "
                    "(Vorbemerkung Teil A Abs. 2 Anlage PatKostG; BPatG Einspruchsgebühren bei gemeinsamem Einspruch). Die eine Gebühr ist "
                    "zuzuordnen, im Zweifel dem zuerst Genannten (Rechtsgedanke BGH Mehrschichtlager). Für D gilt der Einspruch als nicht "
                    "erhoben (§ 6 Abs. 2 PatKostG)."],
                   merke="Jeder Einsprechende zahlt 200 EUR; eine Zahlung deckt nur einen.", titel="V5 Gebühr bei gemeinsamem Einspruch",
                   level=2, norms=["§ 6 Abs. 2 PatKostG"], cases=["pat_bpatg_einspruchsgebuehren_gemeinsam"], step=_E + ".1.2"),
             frage("Kann D Wiedereinsetzung in die Frist zur Zahlung der Einspruchsgebühr beantragen?", False,
                   ["**Nein!** Wiedereinsetzung ist ausgeschlossen für die Frist zur Erhebung des Einspruchs und zur Zahlung der "
                    "Einspruchsgebühr (§ 123 Abs. 1 S. 2 Nr. 1 PatG; BGH Verspätete Zahlung der Einspruchsgebühr). D ist am Verfahren nicht "
                    "beteiligt; ihr bleibt nach Abschluss des Einspruchsverfahrens die Nichtigkeitsklage (§ 81 Abs. 2 S. 1 PatG)."],
                   merke="§ 123 Abs. 1 S. 2 Nr. 1 PatG: keine Wiedereinsetzung für Einspruchsfrist und Einspruchsgebühr.", titel="Wiedereinsetzung",
                   norms=["§ 123 Abs. 1 PatG"], cases=["pat_bgh_einspruchsgebuehr_verspaetet"]),
            ],
            abschnitt="Klausurfall", level=1, concepts=["pat_einspruch"], norms=["§ 59 Abs. 1 PatG"]),
        *fallkette("p05b-10", "Beitritt nach der Verletzungsklage (nach TS I/2023)",
            "Die Erteilung des Patents P wurde am Mi 12.09.2018 veröffentlicht; der zulässige Einspruch E2 ist anhängig. E3 erhob am "
            "12.06.2019 Einspruch, zahlte aber nur 100 EUR. Im Juli 2019 verklagt die Inhaberin E3 vor dem LG Düsseldorf; eine Woche nach "
            "Klageerhebung erklärt E3 den Beitritt und rügt erstmals eine unzulässige Erweiterung.",
            [frage("Gilt der Einspruch der E3 als erhoben?", False,
                   ["**Nein!** Die Gebühr von 200 EUR (Nr. 313 600 Anlage PatKostG) war bis Fristende am Mi 12.06.2019 vollständig zu zahlen "
                    "(§ 6 Abs. 1 S. 1 PatKostG). Bei nicht vollständiger Zahlung gilt der Einspruch als nicht erhoben (§ 6 Abs. 2 PatKostG); "
                    "Wiedereinsetzung ist ausgeschlossen (§ 123 Abs. 1 S. 2 Nr. 1 PatG)."],
                   merke="Teilzahlung = keine Zahlung (§ 6 Abs. 2 PatKostG).", titel="Unvollständige Gebühr",
                   norms=["§ 6 Abs. 2 PatKostG", "§ 123 Abs. 1 PatG"], step=_E + ".1.2"),
             frage("Kann E3 dem Einspruchsverfahren noch beitreten?", True,
                   ["**Ja!** Gegen das Patent ist Einspruch erhoben (E2), E3 ist Dritte und weist nach, dass gegen sie Verletzungsklage "
                    "erhoben ist; sie erklärt den Beitritt nach Ablauf der Einspruchsfrist und binnen drei Monaten nach Klageerhebung "
                    "(§ 59 Abs. 2 S. 1 PatG; Klage erhoben mit Zustellung, § 253 Abs. 1 ZPO). Ihr gescheiterter Einspruch schadet nicht."],
                   merke="Beitritt: anhängiger Einspruch · Verletzungsklage · drei Monate ab Klageerhebung (§ 59 Abs. 2 S. 1 PatG).",
                   titel="Beitritt", level=2, norms=["§ 59 Abs. 2 PatG"], cases=["pat_bgh_ratschenschluessel"], step=_E + ".1.4"),
             frage("Muss E3 für den Beitritt eine Gebühr zahlen?", True,
                   ["**Ja!** Nr. 313 600 Anlage PatKostG erfasst das Einspruchsverfahren nach § 59 Abs. 1 und Abs. 2 PatG; die Gebühr wird "
                    "mit der Beitrittserklärung fällig (§ 3 Abs. 1 S. 2 Nr. 3 PatKostG) und ist in der Beitrittsfrist zu zahlen "
                    "(§ 6 Abs. 1 S. 1 PatKostG), sonst gilt der Beitritt als nicht erklärt (§ 6 Abs. 2 PatKostG). Die 100 EUR von 2019 "
                    "gehören zum gescheiterten Einspruch."],
                   merke="Beitritt kostet wie der Einspruch 200 EUR, fällig mit der Erklärung (§ 3 Abs. 1 S. 2 Nr. 3 PatKostG).",
                   titel="Beitrittsgebühr", level=2, norms=["§ 3 Abs. 1 PatKostG", "§ 6 Abs. 1 PatKostG"], step=_E + ".1.4"),
             frage("Darf E3 mit dem Beitritt einen Widerrufsgrund geltend machen, den E2 nicht vorgebracht hat?", True,
                   ["**Ja!** Der Beitretende wird Einsprechender; für seine Begründung gilt § 59 Abs. 1 S. 3 bis 5 PatG entsprechend "
                    "(§ 59 Abs. 2 S. 4 PatG). Er kann jeden Widerrufsgrund des § 21 PatG geltend machen, sofern er ihn in der Beitrittsfrist "
                    "begründet (§ 59 Abs. 2 S. 3 PatG). Damit wird § 21 Abs. 1 Nr. 4 PatG Gegenstand des Verfahrens, auch für eine spätere "
                    "Beschwerde (BGH Ventileinrichtung)."],
                   merke="Beitretender = Einsprechender mit eigener Begründung in der Beitrittsfrist (§ 59 Abs. 2 S. 3, 4 PatG).",
                   titel="Neuer Widerrufsgrund", level=3, norms=["§ 59 Abs. 2 PatG", "§ 21 Abs. 1 Nr. 4 PatG"], cases=["pat_bgh_ventileinrichtung"]),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_beitritt", "pat_einspruch"], norms=["§ 59 Abs. 2 PatG"]),
    ]),
    # ================================================================== p05c §§ 21, 61 PatG
    dict(id="p05c", titel="§§ 21, 61 PatG: Widerruf und beschränkte Aufrechterhaltung", einheiten=[
        intro("p05c-0", "Prüfungsschema",
              "**AGL:** § 61 Abs. 1 S. 2 PatG i.V.m. § 21 Abs. 1 Nr. 1 bis 4 PatG (beschränkte Aufrechterhaltung § 21 Abs. 2 PatG)\n\n"
              "**A · Verfahrensvoraussetzungen**\n"
              "**V1 Mindestens ein zulässiger Einspruch** – § 61 Abs. 1 S. 2 PatG: Sachentscheidung nur „auf einen zulässigen Einspruch hin“; "
              "sind alle Einsprüche unzulässig, werden sie verworfen, ohne Sachprüfung. Ein zulässiger Einspruch genügt für die Prüfung des "
              "ganzen Angriffs.\n"
              "**V2 Verfahren nicht beendet** – keine Rücknahme eines allein auf Entnahme gestützten Einspruchs (§ 61 Abs. 1 S. 4 PatG), "
              "keine Erledigung der Hauptsache (§ 61 Abs. 1 S. 5 PatG); sonst Fortsetzung von Amts wegen (§ 61 Abs. 1 S. 3 PatG).\n\n"
              "**B · Prüfungsumfang**\n"
              "**V3 Amtsermittlung** – § 59 Abs. 5 PatG i.V.m. § 46 Abs. 1 S. 1 PatG: Ermittlungen von Amts wegen; Hinweise Dritter zum Stand "
              "der Technik (§ 59 Abs. 5 PatG i.V.m. § 43 Abs. 3 S. 2 PatG), auch aus unzulässigen Einsprüchen. Die Patentabteilung darf "
              "weitere Widerrufsgründe aufgreifen, nicht aber die Entnahme (nur der Verletzte); erst das BPatG ist im Beschwerdeverfahren "
              "gesperrt (BGH Ventileinrichtung). Rahmen: angegriffener Teil des Patents (Teileinspruch).\n"
              "**V4 Rechtliches Gehör** – neuer Grund oder neues Material vor der Entscheidung mitteilen, Anhörung auf Antrag (§ 59 Abs. 3 S. 1 PatG).\n\n"
              "**C · Widerrufsgrund (abschließend)**\n"
              "**V5 Nr. 1 Patentfähigkeit fehlt** – §§ 1 bis 5 PatG (eigenes Kapitel).\n"
              "**V6 Nr. 2 Ausführbarkeit fehlt** – Patent offenbart die Erfindung nicht so deutlich und vollständig, dass ein Fachmann sie "
              "ausführen kann; maßgeblich ist das Patent insgesamt (Ansprüche, Beschreibung, Zeichnungen).\n"
              "**V7 Nr. 3 Widerrechtliche Entnahme** – wesentlicher Inhalt den Beschreibungen, Zeichnungen, Modellen, Gerätschaften, "
              "Einrichtungen oder dem Verfahren eines anderen ohne dessen Einwilligung entnommen; nur auf Einspruch des Verletzten.\n"
              "**V8 Nr. 4 Unzulässige Erweiterung** – Gegenstand geht über die ursprünglich eingereichte Fassung hinaus; bei Teilanmeldung "
              "und Nachanmeldung nach § 7 Abs. 2 PatG auch über die frühere Anmeldung (§ 21 Abs. 1 Nr. 4 Hs. 2 PatG). Rettung: nicht "
              "offenbartes, nur einschränkendes Merkmal bleibt im Anspruch, zählt aber nicht für die Patentfähigkeit (BGH Winkelmesseinrichtung); "
              "Aliud führt zum Widerruf.\n\n"
              "**D · Umfang**\n"
              "**V9 Antrag des Inhabers** – beschränkte Aufrechterhaltung nur, soweit der Inhaber eine beschränkte Fassung verteidigt (Haupt- "
              "und Hilfsanträge in seiner Reihenfolge); Beschränkung durch Änderung der Ansprüche, der Beschreibung oder der Zeichnungen "
              "(§ 21 Abs. 2 S. 2 PatG). Ohne Hilfsantrag wird über die erteilte Fassung insgesamt entschieden; fällt ein Anspruch, fällt das "
              "Patent.\n"
              "**V10 Zulässige Fassung** – keine Erweiterung gegenüber der Anmeldung (§ 21 Abs. 1 Nr. 4 PatG) und des Schutzbereichs "
              "(Rechtsgedanke § 22 Abs. 1 PatG).\n\n"
              "**⇒ Rechtsfolge:** Widerruf, beschränkte Aufrechterhaltung oder Aufrechterhaltung durch Beschluss (§ 61 Abs. 1 S. 1, 2 PatG) mit "
              "Rechtsmittelbelehrung (§ 59 Abs. 5 PatG i.V.m. § 47 Abs. 2 PatG); Wirkungen des Patents und der Anmeldung gelten als von "
              "Anfang an nicht eingetreten, bei Beschränkung entsprechend (§ 21 Abs. 3 PatG); Veröffentlichung im Patentblatt (§ 61 Abs. 3 PatG), "
              "geänderte Patentschrift (§ 61 Abs. 4 PatG); Kosten nach § 62 Abs. 1 PatG. Nach Verzicht (§ 20 Abs. 1 Nr. 1 PatG, nur ex nunc): "
              "Erledigung, Feststellung der Beendigung durch Beschluss (§ 61 Abs. 1 S. 5 PatG), es sei denn, ein Einsprechender hat ein "
              "Rechtsschutzbedürfnis am rückwirkenden Widerruf.\n\n"
              "**Klausurfallen:** Patentabteilung „hält das Patent von sich aus beschränkt aufrecht“ (nein, Antrag nötig); Breitenmerkmal aus "
              "der Zeichnung; Kombination nur alternativ offenbarter Merkmale; Bezugszeichenfehler ist keine Erweiterung; Streichen eines "
              "nicht offenbarten Merkmals erweitert den Schutzbereich; Doppelpatentierung und Unklarheit sind keine Widerrufsgründe; Widerruf "
              "wirkt ex tunc, Verzicht ex nunc; nach Abschluss des Einspruchs: Gebrauchsmusterabzweigung binnen zwei Monaten nach Ende des "
              "Monats (§ 5 Abs. 1 S. 3 GebrMG).\n\n"
              "**In den Klausuren:** TS II/2018 (Amtsermittlung, Erledigung nach Verzicht), TS II/2019, TS II/2020 (Verteidigungsoptionen), "
              "TS I/2021, TS II/2021 (Aliud), TS III/2021, TS I/2022 (Teileinspruch, Hilfsanträge), TS II/2022 (Ausführbarkeit von Amts wegen, "
              "Entnahme), TS III/2022, TS I/2023 (Auswahl aus generischer Formel), TS II/2023.",
              concepts=["pat_widerrufsgruende", "pat_unzulaessige_erweiterung", "pat_ausfuehrbarkeit", "pat_einspruch"],
              norms=["§ 61 Abs. 1 PatG", "§ 21 Abs. 1 PatG", "§ 21 Abs. 2 PatG", "§ 21 Abs. 3 PatG", "§ 59 Abs. 5 PatG", "§ 62 Abs. 1 PatG"],
              cases=["pat_bgh_ventileinrichtung", "pat_bgh_winkelmesseinrichtung"], abschnitt="Normenkette"),
        intro("p05c-1", "Definitionen",
              "**Widerrechtliche Entnahme:** Der wesentliche Inhalt des Patents ist den Beschreibungen, Zeichnungen, Modellen, "
              "Gerätschaften oder Einrichtungen eines anderen oder einem von diesem angewendeten Verfahren ohne dessen Einwilligung "
              "entnommen worden (Legaldefinition § 21 Abs. 1 Nr. 3 PatG).\n"
              "**Unzulässige Erweiterung:** Der Gegenstand des Patents geht über den Inhalt der Anmeldung in der ursprünglich eingereichten "
              "Fassung hinaus (§ 21 Abs. 1 Nr. 4 PatG); das ist der Fall, wenn sich der Gegenstand für den Fachmann erst aufgrund eigener, "
              "von seinem Fachwissen getragener Überlegungen ergibt (BGH Hubgliedertor I). Maßstab ist, was der Fachmann den ursprünglichen "
              "Unterlagen unmittelbar und eindeutig als zur Erfindung gehörend entnimmt.\n"
              "**Einschränkendes (nicht offenbartes) Merkmal:** Merkmal, das eine in den ursprünglichen Unterlagen als zur Erfindung gehörend "
              "offenbarte Anweisung zum technischen Handeln konkretisiert und dessen Streichung den Schutzbereich erweitern würde; es bleibt "
              "im Anspruch (BGH Winkelmesseinrichtung) und darf die Patentfähigkeit nicht stützen (BGH Wundbehandlungsvorrichtung).\n"
              "**Aliud:** hinzugefügtes Merkmal, das einen technischen Aspekt betrifft, der den ursprünglichen Unterlagen weder konkret noch "
              "abstrakt als zur Erfindung gehörend zu entnehmen ist; Folge Widerruf (Lösung TS II/2021, TS I/2023).\n"
              "**Ausführbarkeit:** Das Patent offenbart die Erfindung so deutlich und vollständig, dass ein Fachmann sie ausführen kann "
              "(§ 21 Abs. 1 Nr. 2 PatG); er muss die Lehre mit seinem Fachwissen ohne unzumutbaren Aufwand verwirklichen können.\n"
              "**Beschränkte Aufrechterhaltung:** Teilwiderruf, wenn die Widerrufsgründe nur einen Teil des Patents betreffen, durch Änderung "
              "der Ansprüche, der Beschreibung oder der Zeichnungen (§ 21 Abs. 2 PatG).\n"
              "**Erledigung der Hauptsache:** Das Patent ist erloschen (Verzicht, Nichtzahlung), und kein Einsprechender hat ein eigenes "
              "Rechtsschutzbedürfnis an einem rückwirkenden Widerruf; Feststellung der Beendigung durch Beschluss (§ 61 Abs. 1 S. 5 PatG).",
              concepts=["pat_widerrufsgruende", "pat_unzulaessige_erweiterung", "pat_ausfuehrbarkeit"],
              norms=["§ 21 Abs. 1 Nr. 2 PatG", "§ 21 Abs. 1 Nr. 3 PatG", "§ 21 Abs. 1 Nr. 4 PatG", "§ 21 Abs. 2 PatG", "§ 61 Abs. 1 PatG"],
              cases=["pat_bgh_hubgliedertor_i", "pat_bgh_winkelmesseinrichtung", "pat_bgh_wundbehandlungsvorrichtung"], abschnitt="Definitionen"),
        mc("p05c-2", "Was ist kein Widerrufsgrund?",
           "Welcher der folgenden Einwände kann einen Widerruf nach § 21 Abs. 1 PatG nicht tragen?",
           ["Erweiterung des Schutzbereichs nach der Erteilung",
            "Fehlende erfinderische Tätigkeit des Anspruchs 1",
            "Das Patent ist nicht so deutlich offenbart, dass ein Fachmann es ausführen kann",
            "Das Patent beruht auf einer Teilanmeldung und geht über die Stammanmeldung hinaus"], 0,
           ["**Erweiterung des Schutzbereichs.** Sie ist nur Nichtigkeitsgrund (§ 22 Abs. 1 Alt. 2 PatG), weil sie erst durch "
            "Änderungen nach der Erteilung entstehen kann (Einspruch, Beschränkung). Widerrufsgründe sind abschließend fehlende "
            "Patentfähigkeit (Nr. 1), mangelnde Ausführbarkeit (Nr. 2), Entnahme (Nr. 3) und unzulässige Erweiterung, auch gegenüber der "
            "früheren Anmeldung bei Teilanmeldungen (Nr. 4 Hs. 2)."],
           merke="§ 21 Abs. 1 Nr. 1 bis 4 PatG; § 22 Abs. 1 PatG zusätzlich: Schutzbereichserweiterung.", level=1,
           concepts=["pat_widerrufsgruende", "pat_nichtigkeitsgruende"], norms=["§ 21 Abs. 1 PatG", "§ 22 Abs. 1 PatG"], step=_E + ".2",
           abschnitt="Definitionen und Normen"),
        fall("p05c-3", "Ausführbarkeit von Amts wegen",
             "Zwei zulässige Einsprüche stützen sich auf eine offenkundige Vorbenutzung und auf widerrechtliche Entnahme; beide sind "
             "unbegründet. Die Patentabteilung hält die Erfindung aber für nicht ausführbar.",
             "Darf sie das Patent wegen mangelnder Ausführbarkeit widerrufen?", True,
             ["**Ja!** Auf einen zulässigen Einspruch hin entscheidet die Patentabteilung, ob und in welchem Umfang das Patent "
              "aufrechterhalten wird (§ 61 Abs. 1 S. 2 PatG); sie ermittelt von Amts wegen (§ 59 Abs. 5 PatG i.V.m. § 46 Abs. 1 S. 1 PatG) "
              "und ist an die geltend gemachten Gründe nicht gebunden. Vorher muss sie den neuen Grund mitteilen und Gelegenheit zur "
              "Stellungnahme und zur beschränkten Verteidigung geben (TS II/2022)."],
             merke="Patentabteilung: weitere Widerrufsgründe von Amts wegen; BPatG im Beschwerdeverfahren nicht (Ventileinrichtung).",
             level=2, concepts=["pat_ausfuehrbarkeit", "pat_rechtliches_gehoer"], norms=["§ 61 Abs. 1 PatG", "§ 59 Abs. 5 PatG", "§ 21 Abs. 1 Nr. 2 PatG"],
             cases=["pat_bgh_ventileinrichtung"], step=_E + ".2.2", abschnitt="Definitionen und Normen"),
        fall("p05c-4", "Entnahme von Amts wegen",
             "Im Einspruchsverfahren erfährt die Patentabteilung aus der Akte, dass der Inhaber die Erfindung einem Stuhl entnommen haben "
             "könnte, den Herr Nolte entwickelt hat. Nolte hat keinen Einspruch eingelegt.",
             "Darf die Patentabteilung das Patent wegen widerrechtlicher Entnahme widerrufen?", False,
             ["**Nein!** Im Falle der widerrechtlichen Entnahme kann nur der Verletzte Einspruch erheben (§ 59 Abs. 1 S. 1 PatG). Der Grund "
              "dient dem Schutz des Verletzten, nicht der Allgemeinheit; er steht deshalb nicht zur Prüfung von Amts wegen. Nolte bleiben "
              "der eigene Einspruch in der Frist, danach die Nichtigkeitsklage (§ 81 Abs. 3 PatG) oder die Vindikation (§ 8 PatG)."],
             merke="§ 21 Abs. 1 Nr. 3 PatG nur auf Einspruch des Verletzten (§ 59 Abs. 1 S. 1 PatG).", level=2,
             concepts=["pat_widerrufsgruende"], norms=["§ 21 Abs. 1 Nr. 3 PatG", "§ 59 Abs. 1 PatG", "§ 81 Abs. 3 PatG"], step=_E + ".2.3",
             abschnitt="Definitionen und Normen"),
        mc("p05c-5", "Nicht offenbartes, einschränkendes Merkmal",
           "Anspruch 1 wurde im Erteilungsverfahren um die Breite „1 m bis 1,5 m“ ergänzt, die in den Unterlagen nicht steht; sie "
           "konkretisiert die offenbarte Anweisung „Matte bündig zwischen den Reifen“. Was folgt?",
           ["Das Merkmal bleibt im Anspruch, kein Widerruf nach § 21 Abs. 1 Nr. 4 PatG; für die Patentfähigkeit zählt es nicht",
            "Widerruf nach § 21 Abs. 1 Nr. 4 PatG, weil jedes nicht offenbarte Merkmal unzulässig ist",
            "Das Merkmal wird gestrichen und das Patent im Übrigen aufrechterhalten",
            "Das Merkmal bleibt und begründet die erfinderische Tätigkeit"], 0,
           ["**Winkelmesseinrichtung.** Ein nicht offenbartes Merkmal, dessen Streichung den Schutzbereich erweitern würde, kann im Anspruch "
            "bleiben, wenn es eine ursprünglich als zur Erfindung gehörend offenbarte Anweisung konkretisiert (BGH Winkelmesseinrichtung). "
            "Es darf aber die Patentfähigkeit nicht stützen (BGH Wundbehandlungsvorrichtung). Streichen scheidet aus, weil es den Schutzbereich "
            "erweitert (TS II/2018)."],
           merke="Einschränkung: bleibt, zählt nicht; Aliud: Widerruf; Streichen: Schutzbereichserweiterung.", level=2,
           concepts=["pat_unzulaessige_erweiterung"], norms=["§ 21 Abs. 1 Nr. 4 PatG", "§ 21 Abs. 2 PatG"],
           cases=["pat_bgh_winkelmesseinrichtung", "pat_bgh_wundbehandlungsvorrichtung"], step=_E + ".2.4", abschnitt="Definitionen und Normen"),
        fall("p05c-6", "Teileinspruch ohne Hilfsantrag",
             "Die zulässige Einsprechende greift nur die Ansprüche 1, 2, 5 und 6 an; die Ansprüche 3 und 4 hält auch die Prüfungsstelle "
             "für patentfähig. Die Inhaberin äußert sich nicht. Die Ansprüche 1 und 6 sind nicht erfinderisch.",
             "Hält die Patentabteilung das Patent mit den Ansprüchen 3 und 4 aufrecht?", False,
             ["**Nein!** Eine beschränkte Aufrechterhaltung (§ 21 Abs. 2 PatG) setzt voraus, dass die Inhaberin eine beschränkte Fassung "
              "verteidigt; die Patentabteilung darf ihr keine Fassung aufdrängen. Verteidigt sie nur den erteilten Anspruchssatz und ist "
              "ein Anspruch nicht rechtsbeständig, wird das Patent insgesamt widerrufen (§ 61 Abs. 1 S. 2 PatG; TS I/2022). Rettung: "
              "Hilfsanträge, etwa Anspruch 1 mit den Merkmalen der Ansprüche 3 und 4."],
             merke="Ohne Hilfsantrag fällt das ganze Patent; beschränkte Aufrechterhaltung nur auf Antrag des Inhabers.", level=2,
             concepts=["pat_beschraenkte_verteidigung"], norms=["§ 21 Abs. 2 PatG", "§ 61 Abs. 1 PatG"], step=_E + ".3",
             abschnitt="Definitionen und Normen"),
        mc("p05c-7", "Widerruf oder Verzicht",
           "Wie unterscheiden sich Widerruf (§ 61 Abs. 1 S. 2 PatG) und Verzicht (§ 20 Abs. 1 Nr. 1 PatG) in der Wirkung?",
           ["Widerruf wirkt von Anfang an (§ 21 Abs. 3 PatG), Verzicht nur für die Zukunft",
            "Beide wirken von Anfang an",
            "Beide wirken nur für die Zukunft",
            "Verzicht wirkt von Anfang an, Widerruf ab Rechtskraft des Beschlusses"], 0,
           ["**§ 21 Abs. 3 PatG.** Mit dem Widerruf gelten die Wirkungen des Patents und der Anmeldung als von Anfang an nicht eingetreten; "
            "bei beschränkter Aufrechterhaltung entsprechend. Der Verzicht lässt das Patent nur erlöschen (§ 20 Abs. 1 Nr. 1 PatG). "
            "Deshalb erledigt ein Verzicht das Einspruchsverfahren nur, wenn kein Einsprechender ein Interesse am rückwirkenden Widerruf hat, "
            "etwa weil er für die Vergangenheit in Anspruch genommen wird."],
           merke="Widerruf ex tunc (§ 21 Abs. 3 PatG), Verzicht ex nunc (§ 20 Abs. 1 Nr. 1 PatG).", level=1,
           concepts=["pat_widerrufsgruende"], norms=["§ 21 Abs. 3 PatG", "§ 20 Abs. 1 PatG"], step=_E + ".3", abschnitt="Definitionen und Normen"),
        fall("p05c-8", "Verzicht im Einspruchsverfahren",
             "Nach dem Hinweis der Patentabteilung verzichtet die Inhaberin auf das Patent und zusätzlich auf alle Rechte aus dem Patent "
             "für die Vergangenheit. Keine Einsprechende verlangt die Fortsetzung.",
             "Ist das Verfahren durch Feststellungsbeschluss zu beenden?", True,
             ["**Ja!** Das Patent erlischt (§ 20 Abs. 1 Nr. 1 PatG); wegen des Verzichts auch für die Vergangenheit droht keine "
              "Inanspruchnahme, ein Rechtsschutzbedürfnis am rückwirkenden Widerruf fehlt. Das Verfahren ist in der Hauptsache erledigt; die "
              "Beendigung wird durch Beschluss festgestellt (§ 61 Abs. 1 S. 5 PatG). § 61 Abs. 1 S. 3 PatG greift nicht, weil niemand "
              "zurückgenommen hat; Kosten nach Billigkeit (§ 62 Abs. 1 S. 2 PatG; TS II/2018)."],
             merke="Erledigung: Feststellung der Beendigung durch Beschluss (§ 61 Abs. 1 S. 5 PatG).", level=2,
             concepts=["pat_einspruch"], norms=["§ 61 Abs. 1 PatG", "§ 20 Abs. 1 PatG", "§ 62 Abs. 1 PatG"], step=_E + ".3",
             abschnitt="Definitionen und Normen"),
        *fallkette("p05c-9", "Breitenmerkmal und Amtsermittlung (nach TS II/2018)",
            "Von fünf Einsprüchen ist nur der Einspruch der E zulässig; er rügt nur das nicht offenbarte Breitenmerkmal (§ 21 Abs. 1 Nr. 4 "
            "PatG). In der Akte liegt die Druckschrift E(1) aus dem unzulässigen, verfrühten Einspruch der A; sie zeigt sämtliche Merkmale "
            "des einzigen Anspruchs. Die Inhaberin beantragt nur, die Einsprüche zurückzuweisen.",
            [frage("Darf die Patentabteilung in der Sache entscheiden?", True,
                   ["**Ja!** Die Sachentscheidung setzt nur einen zulässigen Einspruch voraus (§ 61 Abs. 1 S. 2 PatG); das ist der Einspruch "
                    "der E. Die unzulässigen Einsprüche werden im selben Beschluss als unzulässig verworfen."],
                   merke="Ein zulässiger Einspruch eröffnet die Sachprüfung (§ 61 Abs. 1 S. 2 PatG).", titel="V1 Zulässiger Einspruch",
                   norms=["§ 61 Abs. 1 PatG"], step=_E + ".3"),
             frage("Führt der Einspruch der E zum Widerruf?", False,
                   ["**Nein!** Die Breite „1 m bis 1,5 m“ ist nicht offenbart, konkretisiert aber die offenbarte Lehre „bündig zwischen den "
                    "Reifen“; ihre Streichung würde den Schutzbereich erweitern. Das Merkmal bleibt im Anspruch und zählt für die "
                    "Patentfähigkeit nicht (BGH Winkelmesseinrichtung). Nr. 4 trägt den Widerruf nicht."],
                   merke="Konkretisierung bleibt im Anspruch, zählt aber nicht.", titel="V8 Nr. 4", level=2,
                   norms=["§ 21 Abs. 1 Nr. 4 PatG"], cases=["pat_bgh_winkelmesseinrichtung"], step=_E + ".2.4"),
             frage("Darf die Patentabteilung E(1) verwerten, obwohl sie aus einem unzulässigen Einspruch stammt?", True,
                   ["**Ja!** Die Patentabteilung ermittelt von Amts wegen (§ 59 Abs. 5 PatG i.V.m. § 46 Abs. 1 S. 1 PatG); jedermann kann "
                    "Hinweise zum Stand der Technik geben (§ 59 Abs. 5 PatG i.V.m. § 43 Abs. 3 S. 2 PatG). Was in der Akte liegt, ist zu "
                    "berücksichtigen; ein Patent, das § 3 PatG widerspricht, ist nicht aufrechtzuerhalten."],
                   merke="Amtsermittlung: Material aus unzulässigen Einsprüchen bleibt verwertbar.", titel="V3 Amtsermittlung",
                   norms=["§ 59 Abs. 5 PatG"], step=_E + ".2.1"),
             frage("Darf sie das Patent wegen fehlender Neuheit widerrufen, obwohl E nur Nr. 4 geltend gemacht hat?", True,
                   ["**Ja!** Die Patentabteilung ist an die geltend gemachten Gründe nicht gebunden; gesperrt ist erst das BPatG im "
                    "Beschwerdeverfahren (BGH Ventileinrichtung). Sie muss der Inhaberin E(1) und den neuen Grund vorher mitteilen und "
                    "Gelegenheit zur Stellungnahme geben (§ 59 Abs. 3 PatG). Dann Widerruf nach § 21 Abs. 1 Nr. 1 PatG i.V.m. § 3 Abs. 1 PatG."],
                   merke="Neuer Widerrufsgrund: vor dem DPMA ja (nach Gehör), vor dem BPatG nicht von Amts wegen.", titel="V5 Nr. 1",
                   level=2, norms=["§ 21 Abs. 1 Nr. 1 PatG", "§ 3 Abs. 1 PatG"], cases=["pat_bgh_ventileinrichtung"], step=_E + ".2.1"),
             frage("Muss die Patentabteilung das Patent beschränkt aufrechterhalten, statt es zu widerrufen?", False,
                   ["**Nein!** Der einzige Anspruch ist nicht neu; eine Beschränkung kommt nur in Betracht, wenn die Inhaberin eine "
                    "beschränkte Fassung verteidigt (§ 21 Abs. 2 PatG). Sie beantragt nur Zurückweisung. Tenor: Widerruf; Wirkung von Anfang "
                    "an (§ 21 Abs. 3 PatG), Veröffentlichung (§ 61 Abs. 3 PatG)."],
                   merke="Kein Hilfsantrag, kein Teilwiderruf.", titel="V9 Umfang", norms=["§ 21 Abs. 2 PatG", "§ 21 Abs. 3 PatG"], step=_E + ".3"),
            ],
            abschnitt="Klausurfall", level=1, concepts=["pat_widerrufsgruende", "pat_unzulaessige_erweiterung"]),
        *fallkette("p05c-10", "Hilfsanträge der Lederdruck GmbH (nach TS I/2022)",
            "Gegen das Patent der Lederdruck GmbH (Ansprüche 1 bis 6, unabhängig 1 und 6) liegt der zulässige Teileinspruch der Trausnitz "
            "GmbH gegen die Ansprüche 1, 2, 5 und 6 vor. Anspruch 1 enthält das Merkmal „beheizbare Prägewalze“, das nur in der "
            "Schilderung des Standes der Technik steht. Die Ansprüche 3 und 4 sind unangegriffen.",
            [frage("Darf Lederdruck Anspruch 1 mit den Merkmalen der Ansprüche 3 und 4 als Hilfsantrag verteidigen?", True,
                   ["**Ja!** Betreffen die Widerrufsgründe nur einen Teil des Patents, wird es beschränkt aufrechterhalten; die Beschränkung "
                    "kann durch Änderung der Patentansprüche erfolgen (§ 21 Abs. 2 PatG). Die Zusammenfassung erteilter Ansprüche beschränkt "
                    "nur und ist ursprünglich offenbart. Den Verfahrensanspruch 6 muss Lederdruck anpassen oder streichen."],
                   merke="Hilfsantrag: Zusammenfassung erteilter Ansprüche (§ 21 Abs. 2 S. 2 PatG).", titel="V9 Hilfsantrag",
                   norms=["§ 21 Abs. 2 PatG"], concepts=["pat_beschraenkte_verteidigung"], step=_E + ".3"),
             frage("Darf Lederdruck das Merkmal „beheizbar“ streichen, falls es nicht ursprünglich offenbart ist?", False,
                   ["**Nein!** Streichen erweiterte den Schutzbereich; das ist im Einspruch unzulässig (Rechtsgedanke § 22 Abs. 1 PatG). "
                    "Konkretisiert das Merkmal eine offenbarte Lehre, bleibt es im Anspruch und zählt für die Patentfähigkeit nicht "
                    "(BGH Winkelmesseinrichtung); andernfalls ist es Aliud und führt zum Widerruf."],
                   merke="Nicht offenbartes Merkmal: nicht streichen, sondern als Einschränkung halten.", titel="V10 Fassung", level=2,
                   norms=["§ 21 Abs. 1 Nr. 4 PatG", "§ 22 Abs. 1 PatG"], cases=["pat_bgh_winkelmesseinrichtung"], step=_E + ".2.4"),
             frage("Kann Lederdruck statt Hilfsanträgen auf die angegriffenen Ansprüche verzichten?", True,
                   ["**Ja!** Ein Teilverzicht durch schriftliche Erklärung gegenüber dem DPMA ist auch im Einspruchsverfahren möglich "
                    "(§ 20 Abs. 1 Nr. 1 PatG). Er wirkt aber nur für die Zukunft und ist endgültig; der Hilfsantrag hält dagegen die "
                    "erteilte Fassung als Hauptantrag offen (TS I/2022)."],
                   merke="Teilverzicht: endgültig, ex nunc; Hilfsantrag: flexibel.", titel="Teilverzicht", level=2, norms=["§ 20 Abs. 1 PatG"]),
             frage("Wirkt die beschränkte Aufrechterhaltung auf den Anmeldetag zurück?", True,
                   ["**Ja!** Bei beschränkter Aufrechterhaltung gelten die Wirkungen des Patents insoweit als von Anfang an nicht eingetreten "
                    "(§ 21 Abs. 3 S. 2 PatG). Die Beschränkung wird im Patentblatt veröffentlicht, die Patentschrift geändert "
                    "(§ 61 Abs. 3, 4 PatG). Gegen den Beschluss: Beschwerde binnen eines Monats, 500 EUR (Nr. 401 100 Anlage PatKostG)."],
                   merke="§ 21 Abs. 3 S. 2 PatG: Beschränkung ex tunc; § 61 Abs. 3, 4 PatG: Veröffentlichung.", titel="Rechtsfolge",
                   norms=["§ 21 Abs. 3 PatG", "§ 61 Abs. 3 PatG"]),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_beschraenkte_verteidigung", "pat_widerrufsgruende"]),
    ]),
    # ================================================================== p05d §§ 1 bis 5 PatG
    dict(id="p05d", titel="§§ 1 bis 5 PatG: Patentfähigkeit als Vorfrage", einheiten=[
        intro("p05d-0", "Prüfungsschema",
              "**AGL:** keine eigene; Vorfrage im Widerrufsgrund § 21 Abs. 1 Nr. 1 PatG, im Nichtigkeitsgrund § 22 Abs. 1 PatG "
              "(europäisches Patent: Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 52 bis 57 EPÜ), in der Zurückweisung § 48 S. 1 PatG und "
              "der Erteilung § 49 Abs. 1 PatG; Normenkette § 1 Abs. 1 PatG i.V.m. § 3, § 4, § 5 PatG.\n\n"
              "**A · Vorbereitung**\n"
              "**V0 Auslegung und Merkmalsgliederung** – Gegenstand nach den Ansprüchen, Beschreibung und Zeichnungen zur Auslegung "
              "(§ 14 PatG); Anspruch in Merkmale M1, M2 … gliedern; Zweckangaben nur als Eignung; Fachmann bestimmen.\n"
              "**V1 Zeitrang** – Anmeldetag (§ 35 Abs. 1 PatG) oder Priorität: innere (§ 40 Abs. 1, 3 PatG), ausländische (§ 41 Abs. 1 PatG "
              "i.V.m. Art. 4 PVÜ), europäische (Art. 87 bis 89 EPÜ); Priorität nur für dieselbe Erfindung, je Merkmal oder Alternative "
              "(Teilpriorität); Teilanmeldung behält den Zeitrang (§ 39 Abs. 1 S. 4 PatG). Für europäische Patente spricht eine widerlegbare "
              "Vermutung der Prioritätsberechtigung (BGH Sorafenib-Tosylat).\n\n"
              "**B · Erfindung**\n"
              "**V2 Lehre auf technischem Gebiet** – § 1 Abs. 1 PatG; bei Datenverarbeitung genügt ein technischer Teilaspekt.\n"
              "**V3 Kein Ausschluss** – § 1 Abs. 3 Nr. 1 bis 4 PatG nur „als solche“ (§ 1 Abs. 4 PatG); §§ 1a, 2 PatG; Pflanzensorten, "
              "Tierrassen, im Wesentlichen biologische Verfahren (§ 2a Abs. 1 Nr. 1 PatG); chirurgische, therapeutische und "
              "Diagnostizierverfahren am Körper (§ 2a Abs. 1 Nr. 2 S. 1 PatG), nicht aber Stoffe für diese Verfahren (§ 2a Abs. 1 Nr. 2 S. 2 PatG).\n\n"
              "**C · Neuheit (§ 3 PatG)**\n"
              "**V4 Stand der Technik** – alle Kenntnisse, die vor dem Zeitrangtag durch schriftliche oder mündliche Beschreibung, durch "
              "Benutzung oder in sonstiger Weise der Öffentlichkeit zugänglich waren (§ 3 Abs. 1 S. 2 PatG), weltweit, ohne Altersgrenze. "
              "Ältere Anmeldungen, veröffentlicht an oder nach dem Zeitrangtag (§ 3 Abs. 2 S. 1 PatG): nationale (Nr. 1), europäische mit "
              "Schutz für Deutschland und gezahlter Benennungsgebühr, Euro-PCT zusätzlich mit den Voraussetzungen des Art. 153 Abs. 5 EPÜ (Nr. 2), "
              "PCT mit DPMA als Bestimmungsamt (Nr. 3), aber erst nach Gebühr und Übersetzung (Art. III § 8 Abs. 3 IntPatÜG i.V.m. "
              "Art. III § 4 Abs. 2 IntPatÜG); bei prioritätsbegründetem älterem Zeitrang nur, soweit die Voranmeldung den Inhalt trägt "
              "(§ 3 Abs. 2 S. 2 PatG). Gebrauchsmusteranmeldungen sind keine älteren Anmeldungen.\n"
              "**V5 Keine unschädliche Offenbarung** – § 3 Abs. 5 PatG: nicht früher als sechs Monate vor Einreichung der Anmeldung "
              "(tatsächlicher Anmeldetag) und zurückgehend auf offensichtlichen Missbrauch (Nr. 1) oder auf die Zurschaustellung durch den "
              "Anmelder auf einer amtlich anerkannten Ausstellung (Nr. 2; Angabe bei Einreichung und Bescheinigung binnen vier Monaten, "
              "§ 3 Abs. 5 S. 2 PatG). Keine allgemeine Neuheitsschonfrist; anders § 3 Abs. 1 S. 3 GebrMG.\n"
              "**V6 Einzelvergleich** – neuheitsschädlich ist nur, was eine einzige Entgegenhaltung mit allen Merkmalen unmittelbar und "
              "eindeutig offenbart, einschließlich des Selbstverständlichen (BGH Olanzapin); medizinische Indikation: § 3 Abs. 3, 4 PatG.\n\n"
              "**D · Erfinderische Tätigkeit (§ 4 PatG)**\n"
              "**V7 Nicht naheliegend** – § 4 S. 1 PatG: Fachmann, Ausgangspunkt (bedarf der Rechtfertigung, BGH Fischbissanzeiger), "
              "Unterschiedsmerkmale, objektive Aufgabe, Anlass zur Lösung; nur technische Anweisungen zählen (BGH Wiedergabe topografischer "
              "Informationen); Aggregation ohne Synergie ist naheliegend. Ältere Anmeldungen bleiben außer Betracht (§ 4 S. 2 PatG).\n\n"
              "**E · Gewerbliche Anwendbarkeit (§ 5 PatG)**\n"
              "**V8** – Gegenstand kann auf irgendeinem gewerblichen Gebiet einschließlich der Landwirtschaft hergestellt oder benutzt werden.\n\n"
              "**⇒ Rechtsfolge:** patentfähig: Erteilung (§ 49 Abs. 1 PatG) bzw. kein Widerruf/keine Nichtigerklärung insoweit; nicht "
              "patentfähig: Zurückweisung (§ 48 S. 1 PatG), Widerruf (§ 21 Abs. 1 Nr. 1 PatG), Nichtigerklärung (§ 22 Abs. 1 PatG), je Anspruch "
              "und Hilfsantrag.\n\n"
              "**Klausurfallen:** Zeitrang zuerst klären (Priorität entscheidet, ob eine Schrift SdT, ältere Anmeldung oder gar nichts ist); "
              "Veröffentlichung am Zeitrangtag selbst ist nicht „vor“ ihm (nur § 3 Abs. 2 PatG); ältere Anmeldung „plus Fachwissen“ gegen "
              "§ 4 PatG; PCT-Anmeldung vor Eintritt in die nationale Phase; eigene Messevorführung ohne anerkannte Ausstellung; Schonfrist ab "
              "Prioritätstag gerechnet (falsch: ab Einreichung); Ästhetik ist kein Kriterium; Entwicklung beim Partner ist nicht öffentlich.\n\n"
              "**In den Klausuren:** in allen 17 TS-Klausuren 2018 bis 2023 als Vorfrage; Schwerpunkte TS I/2021 (sieben Vorbenutzungen), "
              "TS III/2020 und TS II/2022 (§ 4 S. 2 PatG), TS I/2020 und TS III/2019 (Teilpriorität), TS I/2023 (zweite Indikation, D5 am AT), "
              "TS III/2022 (§ 2a PatG, § 3 Abs. 5 PatG), TS II/2020 und TS III/2018 (Technizität, nichttechnische Merkmale).",
              concepts=["pat_neuheit", "pat_erfinderische_taetigkeit", "pat_technizitaet", "pat_gewerbliche_anwendbarkeit", "pat_prioritaet"],
              norms=["§ 1 Abs. 1 PatG", "§ 3 Abs. 1 PatG", "§ 3 Abs. 2 PatG", "§ 3 Abs. 5 PatG", "§ 4 PatG", "§ 5 PatG"],
              cases=["pat_bgh_olanzapin", "pat_bgh_fischbissanzeiger", "pat_bgh_wiedergabe_topografischer_informationen", "pat_bgh_sorafenib_tosylat"],
              abschnitt="Normenkette"),
        intro("p05d-1", "Definitionen",
              "**Technik (Erfindung):** Lehre zum planmäßigen Handeln unter Einsatz beherrschbarer Naturkräfte zur unmittelbaren "
              "Herbeiführung eines kausal übersehbaren Erfolgs (ständige Rechtsprechung des BGH); ausgeschlossen sind die Gegenstände des "
              "§ 1 Abs. 3 PatG nur als solche (§ 1 Abs. 4 PatG).\n"
              "**Neu:** Die Erfindung gehört nicht zum Stand der Technik (Legaldefinition § 3 Abs. 1 S. 1 PatG).\n"
              "**Stand der Technik:** alle Kenntnisse, die vor dem für den Zeitrang der Anmeldung maßgeblichen Tag durch schriftliche oder "
              "mündliche Beschreibung, durch Benutzung oder in sonstiger Weise der Öffentlichkeit zugänglich gemacht worden sind "
              "(Legaldefinition § 3 Abs. 1 S. 2 PatG).\n"
              "**Öffentlich zugänglich (offenkundige Vorbenutzung):** wenn nach der Lebenserfahrung die nicht nur entfernte Möglichkeit "
              "bestand, dass beliebige Dritte und damit auch Fachkundige zuverlässige Kenntnis erhalten; vorausgesetzt ist mindestens ein "
              "feststehender Kommunikationsakt wie Angebot oder Lieferung (BGH Presszange). Gewerbliche Entwicklung und Erprobung mit "
              "Geheimhaltungsinteresse ist im Regelfall nicht öffentlich (BGH Oberflächenbeschichtung).\n"
              "**Neuheitsschädlich offenbart:** was der Fachmann dem Gesamtinhalt einer Entgegenhaltung unmittelbar und eindeutig entnimmt, "
              "einschließlich des für ihn Selbstverständlichen, das er mitliest (BGH Olanzapin); nicht, was er erst mit seinem Fachwissen ergänzt.\n"
              "**Ältere Anmeldung:** Patentanmeldung mit älterem Zeitrang, die erst an oder nach dem Zeitrangtag der jüngeren Anmeldung "
              "öffentlich zugänglich wird; zählt nur für die Neuheit (§ 3 Abs. 2 PatG, § 4 S. 2 PatG).\n"
              "**Erfinderische Tätigkeit:** Die Erfindung ergibt sich für den Fachmann nicht in naheliegender Weise aus dem Stand der Technik "
              "(Legaldefinition § 4 S. 1 PatG).\n"
              "**Fachmann:** fiktive Person mit dem durchschnittlichen Wissen und Können des maßgeblichen Fachgebiets, das sich nach dem "
              "technischen Problem bestimmt, nicht nach dem Anwender (BGH Fischbissanzeiger: Konstrukteur von Angelgeräten, nicht der Angler); "
              "auch ein Team mehrerer Disziplinen.\n"
              "**Gewerblich anwendbar:** Der Gegenstand kann auf irgendeinem gewerblichen Gebiet einschließlich der Landwirtschaft hergestellt "
              "oder benutzt werden (Legaldefinition § 5 PatG).\n"
              "**Unschädliche Offenbarung:** Offenbarung höchstens sechs Monate vor Einreichung, die auf offensichtlichem Missbrauch zum Nachteil "
              "des Anmelders oder auf seiner Zurschaustellung auf einer amtlich anerkannten Ausstellung beruht (§ 3 Abs. 5 PatG).",
              concepts=["pat_technizitaet", "pat_neuheit", "pat_offenbarung", "pat_erfinderische_taetigkeit", "pat_fachmann",
                        "pat_gewerbliche_anwendbarkeit"],
              norms=["§ 1 Abs. 1 PatG", "§ 3 Abs. 1 PatG", "§ 3 Abs. 2 PatG", "§ 3 Abs. 5 PatG", "§ 4 PatG", "§ 5 PatG"],
              cases=["pat_bgh_olanzapin", "pat_bgh_fischbissanzeiger"], abschnitt="Definitionen"),
        mc("p05d-2", "Offenkundige Vorbenutzung",
           "Wann ist eine Benutzung vor dem Zeitrangtag öffentlich zugänglich im Sinne von § 3 Abs. 1 S. 2 PatG?",
           ["Wenn nach der Lebenserfahrung die nicht nur entfernte Möglichkeit bestand, dass beliebige Dritte zuverlässige Kenntnis "
            "erhalten, angeknüpft an einen Kommunikationsakt",
            "Erst wenn ein Dritter die Erfindung tatsächlich zur Kenntnis genommen hat",
            "Nur wenn die Benutzung im Inland stattgefunden hat",
            "Wenn irgendeine Person außerhalb des Erfinderbetriebs von der Benutzung wusste"], 0,
           ["**BGH Presszange.** Es genügt die nicht nur entfernte Möglichkeit, dass beliebige Dritte, damit auch Fachkundige, zuverlässige "
            "Kenntnis erhalten; der Schluss setzt mindestens einen feststehenden Kommunikationsakt wie ein Angebot oder eine Lieferung "
            "voraus. Tatsächliche Kenntnisnahme ist nicht nötig. Der Ort ist gleich (anders § 3 Abs. 1 S. 2 GebrMG: Benutzung im "
            "Geltungsbereich des Gesetzes)."],
           merke="Offenkundig: nicht nur entfernte Möglichkeit der Kenntnis beliebiger Dritter, angeknüpft an einen Kommunikationsakt.", level=1,
           concepts=["pat_neuheit"], norms=["§ 3 Abs. 1 PatG"], step=_PF + ".3.1", abschnitt="Definitionen und Normen"),
        fall("p05d-3", "Angebot in Bozen",
             "Vor dem Anmeldetag bietet die Calfreddo snc in einem allgemein versandten Prospekt Kühlgeräte an, die „ab sofort“ in Bozen "
             "abholbar oder lieferbar sind; die Geräte weisen sämtliche Merkmale des Anspruchs 1 auf. Der Prospekt selbst nennt nur Leistungsdaten.",
             "Gehören die Geräte zum Stand der Technik?", True,
             ["**Ja!** Der Stand der Technik ist weltweit (§ 3 Abs. 1 S. 2 PatG); der Ort der Benutzung ist unerheblich. Ein allgemeines "
              "Angebot fertiger, sofort lieferbarer Geräte macht sie für jedermann erwerbbar und untersuchbar; das Angebot ist der "
              "Kommunikationsakt (BGH Presszange). Dass der Prospekt die Lehre nicht beschreibt, schadet nicht. Beweis: Zeugen, Lieferscheine "
              "(TS I/2021)."],
             merke="Benutzung im Ausland ist Stand der Technik (§ 3 Abs. 1 S. 2 PatG); Angebot = Kommunikationsakt.", level=2,
             concepts=["pat_neuheit"], norms=["§ 3 Abs. 1 PatG"], step=_PF + ".3.1", abschnitt="Definitionen und Normen"),
        fall("p05d-4", "Veröffentlicht am Anmeldetag",
             "Die europäische Anmeldung D5 mit Benennung Deutschlands und älterem Zeitrang wird genau an dem Tag veröffentlicht, an dem "
             "das Streitpatent angemeldet wurde. Die Einsprechende will mit D5 die erfinderische Tätigkeit angreifen.",
             "Kann sie D5 für die erfinderische Tätigkeit heranziehen?", False,
             ["**Nein!** Stand der Technik nach § 3 Abs. 1 S. 2 PatG ist nur, was „vor“ dem Zeitrangtag zugänglich war. Eine Veröffentlichung "
              "„an“ diesem Tag macht D5 allenfalls zur älteren Anmeldung (§ 3 Abs. 2 S. 1 Nr. 2 PatG, Benennungsgebühr gezahlt), die bei der "
              "erfinderischen Tätigkeit außer Betracht bleibt (§ 4 S. 2 PatG). D5 trägt nur einen Neuheitsangriff (TS I/2023)."],
             merke="„Vor“ dem Zeitrangtag: § 3 Abs. 1 PatG; „an oder nach“: § 3 Abs. 2 PatG, nur Neuheit (§ 4 S. 2 PatG).", level=2,
             concepts=["pat_neuheit", "pat_erfinderische_taetigkeit"], norms=["§ 3 Abs. 1 PatG", "§ 3 Abs. 2 PatG", "§ 4 PatG"], step=_PF + ".3.1",
             abschnitt="Definitionen und Normen"),
        mc("p05d-5", "Neuheitsschonfrist",
           "Der Anmelder hat seine Erfindung fünf Monate vor der Anmeldung auf einer Freizeitmesse vorgeführt, die keine amtlich anerkannte "
           "Ausstellung ist. Was gilt für die Patentanmeldung?",
           ["Die Vorführung ist Stand der Technik; § 3 Abs. 5 PatG schützt nur Missbrauch und amtlich anerkannte Ausstellungen",
            "Sie bleibt außer Betracht, weil sie weniger als sechs Monate vor der Anmeldung lag",
            "Sie bleibt außer Betracht, weil eigene Offenbarungen des Anmelders nie schaden",
            "Sie bleibt außer Betracht, wenn der Anmelder binnen vier Monaten eine Bescheinigung einreicht"], 0,
           ["**§ 3 Abs. 5 PatG.** Das PatG kennt keine allgemeine Neuheitsschonfrist. Unschädlich ist eine Offenbarung nur, wenn sie nicht "
            "früher als sechs Monate vor Einreichung erfolgte und auf offensichtlichem Missbrauch (Nr. 1) oder auf der Zurschaustellung auf "
            "einer amtlich anerkannten Ausstellung (Nr. 2, mit Angabe und Bescheinigung nach S. 2) beruht. Das Gebrauchsmuster hätte geholfen "
            "(§ 3 Abs. 1 S. 3 GebrMG; TS II/2018)."],
           merke="§ 3 Abs. 5 PatG: sechs Monate vor Einreichung · Missbrauch oder anerkannte Ausstellung; sonst eigene Offenbarung schädlich.",
           level=1, concepts=["pat_neuheit"], norms=["§ 3 Abs. 5 PatG"], step=_PF + ".3.1", abschnitt="Definitionen und Normen"),
        mc("p05d-6", "Reihenfolge der Prüfung",
           "Gegen das Patent werden eine Druckschrift D1 und eine ältere Anmeldung D2 vorgelegt; das Patent beansprucht eine innere "
           "Priorität. Was prüfen Sie nach der Merkmalsgliederung zuerst?",
           ["Den Zeitrang jedes Anspruchs, also ob die Priorität wirksam ist",
            "Die erfinderische Tätigkeit gegenüber D1 und D2",
            "Die Neuheit gegenüber D2",
            "Die gewerbliche Anwendbarkeit"], 0,
           ["**Zeitrang.** Ob D1 Stand der Technik nach § 3 Abs. 1 PatG, D2 ältere Anmeldung nach § 3 Abs. 2 PatG oder beide unbeachtlich "
            "sind, hängt vom maßgeblichen Tag ab (§ 3 Abs. 1 S. 2 PatG). Er folgt aus dem Anmeldetag oder einer wirksamen Priorität "
            "(§ 40 Abs. 1, 3 PatG), gegebenenfalls nur für Teile des Anspruchs. Danach Erfindung, Neuheit (§ 3 PatG), erfinderische "
            "Tätigkeit (§ 4 PatG), gewerbliche Anwendbarkeit (§ 5 PatG)."],
           merke="Merkmalsgliederung → Zeitrang → Stand der Technik → Neuheit → erfinderische Tätigkeit → § 5 PatG.", level=1,
           concepts=["pat_prioritaet", "pat_neuheit"], norms=["§ 3 Abs. 1 PatG", "§ 40 Abs. 1 PatG"], step=_PF + ".1", abschnitt="Definitionen und Normen"),
        mc("p05d-7", "Inhalt einer Anzeige",
           "Anspruch 2 betrifft ein Fahrzeug mit Regensensor und Steuerung, die bei Regen die Meldung „Dach schließen, Allrad zuschalten, "
           "Wischer an“ anzeigt. Wie behandeln Sie den Inhalt der Meldung bei § 4 PatG?",
           ["Er bleibt außer Betracht, weil nur Anweisungen zählen, die die Lösung des technischen Problems mit technischen Mitteln "
            "bestimmen oder beeinflussen",
            "Er macht den Anspruch als Wiedergabe von Informationen insgesamt unpatentierbar",
            "Er begründet für sich die erfinderische Tätigkeit, weil die Kombination neu ist",
            "Er ist nur bei der gewerblichen Anwendbarkeit zu prüfen"], 0,
           ["**BGH Wiedergabe topografischer Informationen.** Der Anspruch auf ein Fahrzeug mit Sensor ist technisch und nicht nach "
            "§ 1 Abs. 3 Nr. 4, Abs. 4 PatG ausgeschlossen. Bei der erfinderischen Tätigkeit zählen aber nur Anweisungen, die die Lösung "
            "des technischen Problems mit technischen Mitteln bestimmen oder beeinflussen; der Inhalt der Anzeige bleibt außer Betracht "
            "(TS II/2020)."],
           merke="Nichttechnische Merkmale: Ausschluss nur als solche, bei § 4 PatG unberücksichtigt.", level=2,
           concepts=["pat_erfinderische_taetigkeit", "pat_technizitaet"], norms=["§ 4 PatG", "§ 1 Abs. 3 PatG", "§ 1 Abs. 4 PatG"],
           cases=["pat_bgh_wiedergabe_topografischer_informationen"], step=_PF + ".4", abschnitt="Definitionen und Normen"),
        *fallkette("p05d-8", "Sieben Vorbenutzungen (nach TS I/2021)",
            "Munich Cool meldet am Mi 11.05.2016 ohne Priorität ein Kühlgerät an. Vorher: Vorführung auf der anerkannten Messe "
            "„Raumklima 2016“ (Angabe bei der Anmeldung fehlt), Erprobung mit dem Entwicklungspartner Piggy, Lieferung an die Mayer KG ohne "
            "Geheimhaltungsabrede, Verkauf an Rindshuber mit Geheimhaltungsvereinbarung, Kaufvertrag mit Nordic Crab am 09.05.2016, "
            "Lieferung am 14.05.2016.",
            [frage("Ist die Erprobung mit Piggy eine offenkundige Vorbenutzung?", False,
                   ["**Nein!** Bei gewerblicher Entwicklungs- und Erprobungstätigkeit mit betrieblichem Interesse an Geheimhaltung ist die "
                    "öffentliche Zugänglichkeit im Regelfall zu verneinen, solange nur Beteiligte Kenntnis haben (BGH Oberflächenbeschichtung)."],
                   merke="Entwicklung und Erprobung mit Partnern: regelmäßig nicht öffentlich.", titel="Erprobung",
                   norms=["§ 3 Abs. 1 PatG"], step=_PF + ".3.1"),
             frage("Macht die Lieferung an die Mayer KG das Gerät öffentlich zugänglich?", True,
                   ["**Ja!** Die Lieferung an einen Abnehmer ohne Geheimhaltungspflicht ist ein Kommunikationsakt; der Eigentümer darf das "
                    "Gerät untersuchen und weitergeben (BGH Presszange). Langjährige Geschäftsbeziehung oder Sonderpreis begründen allein keine "
                    "Schweigepflicht."],
                   merke="Lieferung ohne Geheimhaltungsabrede = offenkundige Vorbenutzung.", titel="Lieferung", norms=["§ 3 Abs. 1 PatG"],
                   step=_PF + ".3.1"),
             frage("Ist der Verkauf an Rindshuber mit Geheimhaltungsvereinbarung Stand der Technik?", False,
                   ["**Nein!** Ein zur Geheimhaltung verpflichteter Empfänger ist nicht die Öffentlichkeit; die Möglichkeit der Weitergabe an "
                    "beliebige Dritte liegt nicht nahe. Einen Bruch der Vereinbarung müsste der Angreifer darlegen und beweisen."],
                   merke="Geheimhaltungspflicht schließt Öffentlichkeit aus.", titel="Geheimhaltung", norms=["§ 3 Abs. 1 PatG"], step=_PF + ".3.1"),
             frage("Schadet der Kaufvertrag mit Nordic Crab vom 09.05.2016?", False,
                   ["**Nein!** Vor dem Anmeldetag liegt nur der Vertragsschluss; das Gerät kam erst am 14.05.2016, nach dem Anmeldetag, zum Kunden. "
                    "Ohne Kommunikationsakt, der die Lehre vor dem 11.05.2016 vermittelt, fehlt die Zugänglichkeit (BGH Presszange)."],
                   merke="Maßgeblich ist der Kommunikationsakt vor dem Zeitrangtag, nicht der Vertrag.", titel="Vertrag vor, Lieferung nach dem AT",
                   level=2, norms=["§ 3 Abs. 1 PatG"], step=_PF + ".3.1"),
             frage("Bleibt die Messevorführung nach § 3 Abs. 5 S. 1 Nr. 2 PatG außer Betracht?", False,
                   ["**Nein!** Die Messe ist amtlich anerkannt und lag innerhalb von sechs Monaten vor der Einreichung. Die Vorschrift greift "
                    "aber nur, wenn der Anmelder bei Einreichung angibt, dass die Erfindung zur Schau gestellt wurde, und binnen vier Monaten "
                    "eine Bescheinigung einreicht (§ 3 Abs. 5 S. 2 PatG). Die Angabe fehlt; Lieferungen und Verkäufe deckt § 3 Abs. 5 PatG ohnehin nicht."],
                   merke="Ausstellungsschutz: anerkannte Ausstellung · sechs Monate · Angabe bei Einreichung · Bescheinigung binnen vier Monaten.",
                   titel="Ausstellungsschutz", level=2, norms=["§ 3 Abs. 5 PatG"], step=_PF + ".3.1"),
            ],
            abschnitt="Klausurfall", level=1, concepts=["pat_neuheit"], norms=["§ 3 Abs. 1 PatG"]),
        *fallkette("p05d-9", "Stuhl mit fünf Beinen (nach TS II/2022)",
            "AZ1 vom 01.01.2018 offenbart einen Stuhl mit fünf Beinen. AZ2 vom 20.11.2018 beansprucht unter Inanspruchnahme der Priorität "
            "der AZ1 ein „Sitzmöbel mit fünf Beinen“ (Anspruch 1) und einen zentralen Schaft mit Sternfuß (Anspruch 2). D1 ist eine "
            "PCT-Anmeldung vom 09.07.2018 mit Deutschland als Bestimmungsstaat, veröffentlicht am 09.01.2020; sie zeigt ein Sofa mit fünf Beinen.",
            [frage("Hat Anspruch 1 für Sofas den Zeitrang der AZ1?", False,
                   ["**Nein!** Die Priorität kann nur für Merkmale in Anspruch genommen werden, die in der Gesamtheit der Unterlagen der "
                    "früheren Anmeldung deutlich offenbart sind (§ 40 Abs. 3 PatG). AZ1 zeigt nur Stühle; für andere Sitzmöbel gilt der "
                    "Anmeldetag 20.11.2018."],
                   merke="Verallgemeinerung über die Voranmeldung hinaus: insoweit kein Prioritätsrecht (§ 40 Abs. 3 PatG).", titel="V1 Zeitrang",
                   norms=["§ 40 Abs. 3 PatG"], concepts=["pat_prioritaet"], step=_PF + ".1"),
             frage("Ist D1 gegenüber Anspruch 1 vorveröffentlichter Stand der Technik?", False,
                   ["**Nein!** D1 wurde am 09.01.2020 veröffentlicht, nach beiden in Betracht kommenden Zeitrangtagen. Stand der Technik nach "
                    "§ 3 Abs. 1 S. 2 PatG ist nur, was vor dem Zeitrangtag öffentlich zugänglich war."],
                   merke="Nachveröffentlicht: nie § 3 Abs. 1 PatG, allenfalls § 3 Abs. 2 PatG.", titel="V4 Vorveröffentlichung",
                   norms=["§ 3 Abs. 1 PatG"], step=_PF + ".3.1"),
             frage("Kann D1 als ältere Anmeldung die Neuheit von Anspruch 1 für Sofas zerstören?", True,
                   ["**Ja,** aber nur unter einer Bedingung. D1 ist älter als der 20.11.2018 und danach veröffentlicht; als PCT-Anmeldung mit DPMA "
                    "als Bestimmungsamt fällt sie unter § 3 Abs. 2 S. 1 Nr. 3 PatG. Stand der Technik wird sie erst, wenn Gebühr und "
                    "Übersetzung für die nationale Phase vorliegen (Art. III § 8 Abs. 3 IntPatÜG i.V.m. Art. III § 4 Abs. 2 IntPatÜG)."],
                   merke="PCT als ältere Anmeldung erst nach Eintritt in die nationale Phase (Art. III § 8 Abs. 3 IntPatÜG).",
                   titel="V4 Ältere PCT-Anmeldung", level=3, norms=["§ 3 Abs. 2 PatG", "Art. III § 8 IntPatÜG", "Art. III § 4 IntPatÜG"],
                   concepts=["pat_pct_nationale_phase"], step=_PF + ".3.1"),
             frage("Darf die Prüfungsstelle Anspruch 2 als durch D1 nahegelegt zurückweisen?", False,
                   ["**Nein!** D1 kann allenfalls ältere Anmeldung sein; Unterlagen nach § 3 Abs. 2 PatG werden bei der erfinderischen "
                    "Tätigkeit nicht in Betracht gezogen (§ 4 S. 2 PatG). Für Anspruch 2 müsste die Prüfungsstelle anderen, vorveröffentlichten "
                    "Stand der Technik benennen (§ 45 Abs. 2 PatG)."],
                   merke="§ 4 S. 2 PatG: ältere Anmeldung nie gegen die erfinderische Tätigkeit.", titel="V7 Erfinderische Tätigkeit",
                   norms=["§ 4 PatG", "§ 45 Abs. 2 PatG"], step=_PF + ".4"),
             frage("Darf die Prüfungsstelle einen Anspruch zurückweisen, weil der beanspruchte Stuhl „nicht schön“ sei?", False,
                   ["**Nein!** Zurückgewiesen wird nur, wenn keine nach §§ 1 bis 5 PatG patentfähige Erfindung vorliegt (§ 48 S. 1 PatG). "
                    "Ästhetik ist kein Kriterium; ästhetische Formschöpfungen sind nur als solche ausgeschlossen (§ 1 Abs. 3 Nr. 2, Abs. 4 PatG). "
                    "Ein Lehnenbein gegen Kippen löst ein technisches Problem mit technischen Mitteln."],
                   merke="Patentfähigkeit: §§ 1 bis 5 PatG, nicht Schönheit.", titel="V3 Ästhetik", norms=["§ 48 PatG", "§ 1 Abs. 3 PatG"],
                   step=_PF + ".2.2"),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_neuheit", "pat_erfinderische_taetigkeit"]),
    ]),
    # ================================================================== p05e §§ 81, 22 PatG
    dict(id="p05e", titel="§§ 81, 22 PatG: Nichtigkeitsklage", einheiten=[
        intro("p05e-0", "Prüfungsschema",
              "**AGL:** § 81 Abs. 1 S. 1 PatG i.V.m. § 22 Abs. 1 PatG; europäisches Patent (deutscher Teil): Art. II § 6 Abs. 1 IntPatÜG "
              "i.V.m. § 81 Abs. 1 S. 1 PatG\n\n"
              "**A · Zulässigkeit**\n"
              "**V1 Zuständigkeit** – Nichtigkeitssenat des BPatG (§ 65 Abs. 1 PatG, § 81 Abs. 4 S. 1 PatG). Europäisches Patent: deutsche "
              "Gerichte nur, soweit sie nach dem EPGÜ weiter zuständig sind (Art. II § 6 Abs. 1 IntPatÜG): Übergangszeit (Art. 83 Abs. 1 EPGÜ) "
              "oder Opt-out (Art. 83 Abs. 3 EPGÜ). Daneben EPG: Klage auf Nichtigerklärung (Art. 32 Abs. 1 lit. d EPGÜ) bei der Zentralkammer, "
              "bei anhängiger Verletzungsklage zwischen denselben Parteien bei deren Lokal- oder Regionalkammer (Art. 33 Abs. 4 EPGÜ), ohne "
              "vorherigen EPA-Einspruch (Art. 33 Abs. 8 EPGÜ). Nationale Patente: nur BPatG.\n"
              "**V2 Keine Klagesperre** – § 81 Abs. 2 S. 1 PatG: unzulässig, solange Einspruch noch erhoben werden kann oder ein "
              "Einspruchsverfahren anhängig ist; Zweck: Subsidiarität, keine widersprechenden Entscheidungen (BGH Strahlungssteuerung). Gilt "
              "für den EPA-Einspruch, auch wenn die Klage nur auf ein älteres nationales Recht gestützt wird (BGH Mautberechnung).\n"
              "**V3 Parteien** – Beklagter: der im Register als Inhaber Eingetragene (§ 81 Abs. 1 S. 2 PatG). Kläger: jeder (Popularklage); "
              "widerrechtliche Entnahme nur der Verletzte (§ 81 Abs. 3 PatG); Nichtberechtigung des EP-Inhabers nur der Berechtigte "
              "(Art. II § 6 Abs. 4 IntPatÜG). Parteifähigkeit § 99 Abs. 1 PatG i.V.m. § 50 ZPO.\n"
              "**V4 Form und Inhalt** – schriftlich beim BPatG (§ 81 Abs. 4 S. 1 PatG); muss Kläger, Beklagten und Streitgegenstand bezeichnen, "
              "soll einen bestimmten Antrag enthalten; Tatsachen und Beweismittel sind anzugeben (§ 81 Abs. 5 S. 1, 2 PatG); Ergänzung auf "
              "Aufforderung (§ 81 Abs. 5 S. 3 PatG); Aktenzeichen und Streitwert des Verletzungsstreits sollen angegeben werden "
              "(§ 81 Abs. 5 S. 4 PatG); deutsch (§ 126 PatG).\n"
              "**V5 Gebühr** – 4,5 Gebühren nach dem Streitwert (§ 2 Abs. 2 PatKostG, Nr. 402 100 Anlage PatKostG), fällig mit Einreichung "
              "(§ 3 Abs. 1 S. 2 Nr. 4 PatKostG), zahlbar binnen drei Monaten ab Fälligkeit (§ 6 Abs. 1 S. 2 PatKostG), sonst gilt die Klage als "
              "zurückgenommen (§ 6 Abs. 2 PatKostG); Zustellung erst nach Zahlung (§ 5 Abs. 1 S. 3 PatKostG).\n"
              "**V6 Sicherheit** – Kläger ohne gewöhnlichen Aufenthalt in EU oder EWR auf Verlangen des Beklagten; Fristversäumnis: Klage gilt "
              "als zurückgenommen (§ 81 Abs. 6 PatG).\n"
              "**V7 Rechtsschutzbedürfnis** – nicht darzulegen, solange das Patent in Kraft ist; nach Erlöschen nur bei eigenem, in der Person "
              "des Klägers begründetem Interesse (BGH Leistungsüberwachungsgerät).\n"
              "**V8 Keine entgegenstehende Rechtskraft, kein Strohmann, keine Nichtangriffsabrede** – Rechtskraft nur zwischen den Parteien und "
              "ihren Rechtsnachfolgern (§ 99 Abs. 1 PatG i.V.m. § 325 Abs. 1 ZPO) und nur zur Frage, ob das Patent aus den geltend gemachten "
              "Gründen nichtig ist (BGH Palette); die GmbH ist an das Urteil gegen ihren Alleingesellschafter nicht gebunden (BGH "
              "Rohrreinigungsdüse); ein Strohmann ist wie sein gebundener Hintermann ausgeschlossen (BGH Ziehmaschinenzugeinheit II); "
              "Nichtangriffsabrede: Einwand unzulässiger Rechtsausübung (§ 242 BGB).\n\n"
              "**B · Begründetheit**\n"
              "**V9 Nichtigkeitsgrund** – § 22 Abs. 1 PatG: Gründe des § 21 Abs. 1 Nr. 1 bis 4 PatG oder Erweiterung des Schutzbereichs. "
              "Europäisches Patent: Art. II § 6 Abs. 1 Nr. 1 bis 5 IntPatÜG (Art. 52 bis 57 EPÜ, Ausführbarkeit, Erweiterung, Schutzbereich, "
              "Nichtberechtigung nach Art. 60 Abs. 1 EPÜ); ältere nationale Rechte wirken über Art. 139 Abs. 2 EPÜ. Abschließender Katalog: "
              "Doppelpatentierung und Unklarheit genügen nicht. Untersuchungsgrundsatz (§ 87 Abs. 1 PatG).\n\n"
              "**C · Verfahren und Verteidigung**\n"
              "**V10 Widerspruch** – binnen eines Monats nach Zustellung (§ 82 Abs. 1 PatG), sonst Entscheidung ohne mündliche Verhandlung "
              "mit Geständnisfiktion (§ 82 Abs. 2 PatG); Begründung binnen zwei Monaten nach Zustellung der Klage, Verlängerung um einen Monat "
              "(§ 82 Abs. 3 S. 2, 3 PatG). Berechnung § 99 Abs. 1 PatG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB; "
              "Verschiebung § 222 Abs. 2 ZPO.\n"
              "**V11 Beschränkte Verteidigung** – § 22 Abs. 2 PatG i.V.m. § 21 Abs. 2 PatG; europäisches Patent Art. II § 6 Abs. 2, 3 IntPatÜG. "
              "Qualifizierter Hinweis binnen sechs Monaten (§ 83 Abs. 1 S. 2 PatG), Frist zur Stellungnahme (§ 83 Abs. 2 PatG); verspätete "
              "Hilfsanträge nur zurückzuweisen, wenn Vertagung nötig, Verspätung unentschuldigt und Belehrung erfolgt (§ 83 Abs. 4 S. 1 Nr. 1 bis 3 PatG).\n\n"
              "**⇒ Rechtsfolge:** Urteil (§ 84 Abs. 1 PatG): Nichtigerklärung ganz oder teilweise, Wirkung von Anfang an (§ 22 Abs. 2 PatG i.V.m. "
              "§ 21 Abs. 3 PatG; Art. II § 6 Abs. 1 S. 2 IntPatÜG); Kosten nach der ZPO (§ 84 Abs. 2 PatG). Berufung zum BGH (§ 110 Abs. 1 PatG): "
              "ein Monat ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung (§ 110 Abs. 3 PatG), Begründung drei "
              "Monate (§ 112 Abs. 2 PatG). Klagerücknahme ohne Einwilligung, auch nach mündlicher Verhandlung (§ 99 Abs. 1 PatG i.V.m. § 269 ZPO; "
              "BGH Sitzgelenk); Ermäßigung auf 1,5 Gebühren nur vor Schluss der mündlichen Verhandlung oder bei Vergleich ohne vorausgegangenes "
              "Urteil (Nr. 402 110 Anlage PatKostG). Ein Vergleich (§ 278 Abs. 6 ZPO) beendet das Verfahren, nicht das Patent.\n"
              "**Streitwert:** gemeiner Wert des Patents bei Klageerhebung zuzüglich der bis dahin entstandenen Schadensersatzforderungen; "
              "Anhalt: Streitwert der Verletzungsklage plus ein Viertel (BGH Nichtigkeitsstreitwert; § 2 Abs. 2 S. 4 PatKostG i.V.m. "
              "§ 51 Abs. 1 GKG); Herabsetzung auf Antrag (§ 144 PatG).\n"
              "**Doppelschutz:** Ein deutsches Patent neben einem europäischen Patent desselben Erfinders mit derselben Priorität verliert seine "
              "Wirkung nur noch, wenn das europäische Patent wegen Opt-out nicht dem EPG unterliegt (Art. II § 8 Abs. 1 IntPatÜG); sonst Einrede "
              "der doppelten Inanspruchnahme (Art. II § 18 IntPatÜG). Der Angriff auf das deutsche Patent bleibt zulässig.\n\n"
              "**Klausurfallen:** Klage während laufender Einspruchsfrist (auch EPA); Rücknahme des Einspruchs hebt die Sperre nicht auf "
              "(§ 61 Abs. 1 S. 3 PatG); Klage gegen den materiellen statt den eingetragenen Inhaber; Rechtskraft gegen den Gesellschafter; "
              "Strohmann; Streitwerte mehrerer Verletzungsprozesse wegen derselben Ausführungsform nicht addieren; Rücknahme nach Schluss der "
              "Verhandlung ohne Gebührenermäßigung; Hilfsantrag nach Fristablauf ist nicht automatisch präkludiert; EPG als Alternative.\n\n"
              "**In den Klausuren:** TS III/2018 und TS II/2023 (deutscher Teil eines EP, ältere DE-Anmeldung über Art. 139 Abs. 2 EPÜ), TS I/2019 "
              "(Rechtskraft, Streitwert, Rücknahme, Vergleich), TS III/2019 (Teilpriorität, § 83 Abs. 4 PatG, Strohmann), TS I/2020 (Klage in der "
              "Einspruchsfrist), TS III/2021 (Klagesperre, EPG), TS III/2022.",
              concepts=["pat_nichtigkeitsklage", "pat_nichtigkeitsgruende", "pat_nichtigkeit_ep", "pat_qualifizierter_hinweis",
                        "pat_beschraenkte_verteidigung", "pat_streitwert", "pat_doppelschutz"],
              norms=["§ 81 Abs. 1 PatG", "§ 81 Abs. 2 PatG", "§ 22 Abs. 1 PatG", "§ 82 Abs. 1 PatG", "§ 83 Abs. 4 PatG", "§ 84 PatG",
                     "Art. II § 6 IntPatÜG", "Art. II § 8 IntPatÜG"],
              cases=["pat_bgh_benutzerauthentifizierung", "pat_bgh_fugenband"], abschnitt="Normenkette"),
        intro("p05e-1", "Definitionen",
              "**Nichtigkeitsklage:** Klage beim BPatG auf Erklärung der Nichtigkeit eines erteilten Patents aus den Gründen des § 22 Abs. 1 PatG "
              "(europäisches Patent: Art. II § 6 Abs. 1 IntPatÜG), gerichtet gegen den eingetragenen Inhaber (§ 81 Abs. 1 PatG).\n"
              "**Popularklage:** Jeder ist klagebefugt, ohne ein eigenes Interesse darzulegen, solange das Patent in Kraft ist; Ausnahmen: "
              "Entnahme (§ 81 Abs. 3 PatG) und Nichtberechtigung beim europäischen Patent (Art. II § 6 Abs. 4 IntPatÜG).\n"
              "**Subsidiarität (Klagesperre):** Die Nichtigkeitsklage ist ausgeschlossen, solange Einspruch noch erhoben werden kann oder ein "
              "Einspruchsverfahren anhängig ist (§ 81 Abs. 2 S. 1 PatG), um widersprechende Entscheidungen zu vermeiden (BGH Strahlungssteuerung).\n"
              "**Erweiterung des Schutzbereichs:** Die nach der Erteilung geänderte Fassung schützt mehr als die erteilte; nur Nichtigkeitsgrund "
              "(§ 22 Abs. 1 Alt. 2 PatG, Art. II § 6 Abs. 1 Nr. 4 IntPatÜG).\n"
              "**Strohmann:** Kläger, der ohne eigenes Interesse für einen Hintermann klagt, der selbst am Angriff gehindert ist; er ist in gleichem "
              "Maße ausgeschlossen wie dieser (BGH Ziehmaschinenzugeinheit II).\n"
              "**Streitwert:** gemeiner Wert des Patents bei Klageerhebung zuzüglich der bis dahin entstandenen Schadensersatzforderungen; mangels "
              "anderer Anhaltspunkte Streitwert des Verletzungsprozesses plus ein Viertel (BGH Nichtigkeitsstreitwert).\n"
              "**Qualifizierter Hinweis:** frühzeitiger Hinweis des Senats auf die voraussichtlich entscheidungserheblichen Gesichtspunkte, möglichst "
              "binnen sechs Monaten nach Zustellung der Klage (§ 83 Abs. 1 PatG).\n"
              "**Beschränkte Verteidigung:** Verteidigung des Patents mit geänderten, engeren Ansprüchen (Haupt- und Hilfsanträge); Teilnichtigkeit "
              "nach § 22 Abs. 2 PatG i.V.m. § 21 Abs. 2 PatG.",
              concepts=["pat_nichtigkeitsklage", "pat_nichtigkeitsgruende", "pat_streitwert", "pat_qualifizierter_hinweis"],
              norms=["§ 81 Abs. 1 PatG", "§ 81 Abs. 2 PatG", "§ 22 Abs. 1 PatG", "§ 83 Abs. 1 PatG"], abschnitt="Definitionen"),
        fall("p05e-2", "Der falsche Beklagte",
             "Die Flintenschuß KG hat ihr Patent im Januar an die Hirsch GmbH verkauft und übertragen; im Register ist sie noch als Inhaberin "
             "eingetragen. Die Knarrenbauer GmbH will Nichtigkeitsklage erheben.",
             "Muss die Klage gegen die Hirsch GmbH gerichtet werden?", False,
             ["**Nein!** Die Klage ist gegen den im Register als Patentinhaber Eingetragenen zu richten (§ 81 Abs. 1 S. 2 PatG), also gegen "
              "die Flintenschuß KG. Der Kläger soll sich auf das Register verlassen können und nicht die materielle Rechtslage ermitteln müssen. "
              "Eine spätere Umschreibung lässt das Verfahren unberührt; für die Rechtsnachfolge gilt die ZPO über § 99 Abs. 1 PatG."],
             merke="Beklagter = eingetragener Inhaber (§ 81 Abs. 1 S. 2 PatG).", level=1,
             concepts=["pat_nichtigkeitsklage", "pat_register"], norms=["§ 81 Abs. 1 PatG"], step=_N + ".1.2", abschnitt="Definitionen und Normen"),
        mc("p05e-3", "Gebühr der Nichtigkeitsklage",
           "Welche Gebühr fällt für die Nichtigkeitsklage an, wann ist sie zu zahlen, und was folgt aus der Nichtzahlung?",
           ["4,5 Gebühren nach dem Streitwert (Nr. 402 100 Anlage PatKostG), fällig mit der Klage, zahlbar binnen drei Monaten; sonst gilt "
            "die Klage als zurückgenommen",
            "Festgebühr 500 EUR, zahlbar mit Einreichung; sonst ist die Klage unzulässig",
            "4,5 Gebühren, zahlbar binnen eines Monats; sonst Versäumnisurteil",
            "Keine Gebühr, weil die Nichtigkeitsklage im öffentlichen Interesse liegt"], 0,
           ["**Nr. 402 100, § 3 Abs. 1 S. 2 Nr. 4, § 6 Abs. 1 S. 2, Abs. 2 PatKostG.** Für Klagen vor dem BPatG richten sich die Gebühren nach "
            "dem Streitwert (§ 2 Abs. 2 PatKostG). Fällig mit Einreichung; eine gesetzliche Klagefrist gibt es nicht, also drei Monate ab "
            "Fälligkeit (§ 6 Abs. 1 S. 2 PatKostG); sonst Rücknahmefiktion (§ 6 Abs. 2 PatKostG). Zugestellt wird erst nach Zahlung "
            "(§ 5 Abs. 1 S. 3 PatKostG)."],
           merke="Nr. 402 100 · fällig § 3 Abs. 1 S. 2 Nr. 4 PatKostG · drei Monate § 6 Abs. 1 S. 2 PatKostG · Rücknahmefiktion § 6 Abs. 2 PatKostG.",
           level=1, concepts=["pat_gebuehren"], norms=["§ 2 Abs. 2 PatKostG", "§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG"], step=_N + ".1.3",
           abschnitt="Definitionen und Normen"),
        fall("p05e-4", "Klage nach Erlöschen",
             "Das Patent ist durch Zeitablauf erloschen. Die K-GmbH wurde nie aus dem Patent in Anspruch genommen und hat das auch nicht zu "
             "befürchten; sie meint, die Allgemeinheit habe ein Interesse daran, dass ein zu Unrecht erteiltes Patent für nichtig erklärt wird.",
             "Ist ihre Nichtigkeitsklage zulässig?", False,
             ["**Nein!** Nach dem Erlöschen des Patents ist die Nichtigkeitsklage nur zulässig, wenn der Kläger ein eigenes, in seiner Person "
              "begründetes Interesse an der Nichtigerklärung hat, etwa weil er für die Vergangenheit in Anspruch genommen wird. Ein Interesse "
              "Dritter oder der Allgemeinheit genügt nicht (BGH Leistungsüberwachungsgerät). Die Popularklage endet mit dem Erlöschen."],
             merke="Erloschenes Patent: eigenes Rechtsschutzinteresse des Klägers nötig.", level=2,
             concepts=["pat_nichtigkeitsklage"], norms=["§ 81 Abs. 1 PatG"], step=_N + ".1.2", abschnitt="Definitionen und Normen"),
        mc("p05e-5", "Nichtigkeitsgründe gegen den deutschen Teil",
           "Die Mandantin, eine Wettbewerberin, will den deutschen Teil eines europäischen Patents angreifen. Auf welchen Grund kann sie sich "
           "nicht stützen?",
           ["Der Inhaber sei nach Art. 60 Abs. 1 EPÜ nicht berechtigt (Art. II § 6 Abs. 1 S. 1 Nr. 5 IntPatÜG)",
            "Fehlende erfinderische Tätigkeit (Art. II § 6 Abs. 1 S. 1 Nr. 1 IntPatÜG, Art. 56 EPÜ)",
            "Ältere nationale Anmeldung (Art. 139 Abs. 2 EPÜ, § 3 Abs. 2 S. 1 Nr. 1 PatG)",
            "Erweiterung des Schutzbereichs nach der Erteilung (Art. II § 6 Abs. 1 S. 1 Nr. 4 IntPatÜG)"], 0,
           ["**Nr. 5.** Den Grund der Nichtberechtigung kann nur der nach Art. 60 Abs. 1 EPÜ Berechtigte geltend machen "
            "(Art. II § 6 Abs. 4 IntPatÜG). Die übrigen Gründe stehen jedem offen; ältere nationale Rechte wirken gegen den deutschen Teil "
            "wie gegen ein nationales Patent (Art. 139 Abs. 2 EPÜ), und zwar im Rahmen des einheitlichen Grundes fehlender Patentfähigkeit "
            "(BGH Mautberechnung; TS II/2023)."],
           merke="Art. II § 6 Abs. 1 Nr. 1 bis 5 IntPatÜG; Nr. 5 nur der Berechtigte (Abs. 4).", level=2,
           concepts=["pat_nichtigkeit_ep"], norms=["Art. II § 6 IntPatÜG", "Art. 139 EPÜ"], step=_N + ".2", abschnitt="Definitionen und Normen"),
        mc("p05e-6", "Verspäteter Hilfsantrag",
           "Nach Ablauf der Frist zur Stellungnahme auf den qualifizierten Hinweis reicht die Beklagte einen Hilfsantrag ein: Anspruch 1 "
           "mit dem Merkmal des angegriffenen Anspruchs 2. Wann darf der Senat ihn zurückweisen?",
           ["Nur wenn Vertagung nötig wäre, die Verspätung nicht genügend entschuldigt ist und über die Folgen belehrt wurde",
            "Immer, weil die Frist nach § 83 Abs. 2 PatG abgelaufen ist",
            "Wenn eine der drei Voraussetzungen des § 83 Abs. 4 PatG vorliegt",
            "Nie, weil das BPatG den Sachverhalt von Amts wegen erforscht"], 0,
           ["**§ 83 Abs. 4 S. 1 Nr. 1 bis 3 PatG kumulativ.** Zurückweisung setzt voraus, dass die Berücksichtigung eine Vertagung des Termins "
            "erfordern würde (Nr. 1), die Verspätung nicht genügend entschuldigt ist (Nr. 2) und belehrt wurde (Nr. 3). Hier fehlt Nr. 1: "
            "Anspruch 2 ist schon Gegenstand des Angriffs und mit demselben Stand der Technik zu prüfen (TS III/2019)."],
           merke="§ 83 Abs. 4 PatG: Vertagung · keine Entschuldigung · Belehrung – alle drei.", level=2,
           concepts=["pat_qualifizierter_hinweis", "pat_beschraenkte_verteidigung"], norms=["§ 83 Abs. 2 PatG", "§ 83 Abs. 4 PatG"],
           step=_N + ".3.2", abschnitt="Definitionen und Normen"),
        mc("p05e-7", "Berufungsfrist",
           "Das Nichtigkeitsurteil wurde am 10.03. verkündet, das vollständige Urteil am 14.05. zugestellt. Wie lange läuft die Berufungsfrist?",
           ["Ein Monat ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung (§ 110 Abs. 3 PatG)",
            "Ein Monat ab Verkündung",
            "Zwei Monate ab Zustellung",
            "Drei Monate ab Zustellung, gleichzeitig mit der Begründung"], 0,
           ["**§ 110 Abs. 3 PatG.** Die Berufung zum BGH ist binnen eines Monats einzulegen; die Frist beginnt mit der Zustellung des in "
            "vollständiger Form abgefassten Urteils, spätestens mit Ablauf von fünf Monaten nach der Verkündung. Einlegung beim BGH "
            "(§ 110 Abs. 2 PatG). Die Begründungsfrist beträgt drei Monate ab Zustellung (§ 112 Abs. 2 S. 2, 3 PatG)."],
           merke="Berufung: ein Monat (§ 110 Abs. 3 PatG) · Begründung drei Monate (§ 112 Abs. 2 PatG).", level=1,
           concepts=["pat_nichtigkeitsberufung"], norms=["§ 110 Abs. 3 PatG", "§ 112 Abs. 2 PatG"], step=_N + ".5", abschnitt="Definitionen und Normen"),
        *fallkette("p05e-8", "Die zweite Klage der GmbH (nach TS I/2019)",
            "A klagte 2017 persönlich gegen den deutschen Teil des EP 1234567 der P; die Klage wurde rechtskräftig abgewiesen. Jetzt klagt die "
            "A-GmbH, deren Alleingesellschafter und Geschäftsführer A ist. P hat die A-GmbH vor dem LG Düsseldorf (Streitwert 2 Mio. EUR) "
            "und deren Abnehmerin wegen derselben Ausführungsform vor dem LG Mannheim (1 Mio. EUR) verklagt.",
            [frage("Steht die Rechtskraft des Urteils gegen A der Klage der A-GmbH entgegen?", False,
                   ["**Nein!** Das rechtskräftige Urteil wirkt nur für und gegen die Parteien und ihre Rechtsnachfolger (§ 99 Abs. 1 PatG i.V.m. "
                    "§ 325 Abs. 1 ZPO). Die GmbH ist eigene Rechtsperson, nicht Rechtsnachfolgerin; eine Kapitalgesellschaft muss sich die "
                    "Rechtskraft gegen ihren Alleingesellschafter nicht entgegenhalten lassen (BGH Rohrreinigungsdüse)."],
                   merke="Rechtskraft: nur Parteien und Rechtsnachfolger (§ 325 Abs. 1 ZPO).", titel="V8 Rechtskraft", level=2,
                   norms=["§ 99 Abs. 1 PatG"], step=_N + ".1.2"),
             frage("Ist die A-GmbH als Strohmann des A ausgeschlossen?", False,
                   ["**Nein!** Ausgeschlossen ist, wer ohne eigenes Interesse für einen gebundenen Hintermann klagt (BGH Ziehmaschinenzugeinheit II). "
                    "Die A-GmbH wird selbst vor dem LG Düsseldorf verklagt; sie hat ein eigenes Interesse an der Nichtigerklärung."],
                   merke="Eigene Verletzungsklage = eigenes Interesse, kein Strohmann.", titel="V8 Strohmann", level=2, step=_N + ".1.2"),
             frage("Wie hoch wird der Streitwert der Nichtigkeitsklage voraussichtlich festgesetzt?", 1,
                   ["**Rund 2,5 Mio. EUR.** Maßgeblich ist der gemeine Wert des Patents bei Klageerhebung zuzüglich entstandener "
                    "Schadensersatzforderungen; Anhalt ist der Verletzungsstreitwert plus ein Viertel (BGH Nichtigkeitsstreitwert). Beide "
                    "Verletzungsprozesse betreffen dieselbe Ausführungsform; sie werden nicht addiert: 2 Mio. EUR × 1,25."],
                   optionen=["2 Mio. EUR", "2,5 Mio. EUR", "3 Mio. EUR", "3,75 Mio. EUR"],
                   merke="Nichtigkeitsstreitwert: Verletzungsstreitwert + ein Viertel (§ 2 Abs. 2 S. 4 PatKostG, § 51 Abs. 1 GKG).",
                   titel="Streitwert", level=2, concepts=["pat_streitwert"], norms=["§ 2 Abs. 2 PatKostG"], step=_N + ".1.3"),
             frage("Kann die A-GmbH die Klage nach Schluss der mündlichen Verhandlung ohne Einwilligung der P zurücknehmen?", True,
                   ["**Ja!** § 269 Abs. 1 ZPO gilt über § 99 Abs. 1 PatG nur, soweit die Besonderheiten des Verfahrens nicht entgegenstehen; im "
                    "Nichtigkeitsverfahren kann die Klage auch nach Verhandlung zur Hauptsache und noch in der Berufungsinstanz ohne Einwilligung "
                    "des Beklagten zurückgenommen werden (BGH Sitzgelenk)."],
                   merke="Nichtigkeitsklage: Rücknahme ohne Einwilligung (BGH Sitzgelenk).", titel="Klagerücknahme", level=2,
                   norms=["§ 99 Abs. 1 PatG"], step=_N + ".4"),
             frage("Ermäßigt sich die Gerichtsgebühr dann von 4,5 auf 1,5?", False,
                   ["**Nein!** Die Ermäßigung setzt die Zurücknahme „vor dem Schluss der mündlichen Verhandlung“ voraus "
                    "(Nr. 402 110 Buchst. a Anlage PatKostG). Nach dem Schluss (§ 91 Abs. 3 S. 1 PatG) bleibt es bei 4,5 Gebühren; die Kosten "
                    "trägt die Klägerin (§ 269 Abs. 3 S. 2 ZPO)."],
                   merke="Gebührenermäßigung nur bei Rücknahme vor Schluss der mündlichen Verhandlung (Nr. 402 110).", titel="Gebührenermäßigung",
                   level=3, step=_N + ".4"),
             frage("Kann die A-GmbH nach der Rücknahme erneut klagen?", True,
                   ["**Ja!** Nach der Rücknahme ist der Rechtsstreit als nicht anhängig geworden anzusehen (§ 269 Abs. 3 S. 1 ZPO i.V.m. "
                    "§ 99 Abs. 1 PatG); eine rechtskräftige Abweisung gibt es nicht. Das ist der einzige Vorteil gegenüber einem klageabweisenden "
                    "Urteil; die Beklagte kann die Einlassung bis zur Erstattung der Kosten verweigern (§ 269 Abs. 6 ZPO)."],
                   merke="Rücknahme: keine Rechtskraft, neue Klage möglich, Kosten beim Kläger.", titel="Folge der Rücknahme", step=_N + ".4"),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_nichtigkeitsklage", "pat_nichtigkeit_ep"], norms=["§ 81 Abs. 1 PatG"]),
        *fallkette("p05e-9", "Klage während der Einsprüche (nach TS III/2021)",
            "Die Mandantin hat gegen DE 456 B1 fristgerecht Einspruch eingelegt; das Verfahren läuft. Gegen das europäische Patent EP 123 B1 "
            "derselben Inhaberin (kein Opt-out) ist beim EPA der Einspruch eines Dritten anhängig. Die Mandantin will sofort gegen beide "
            "Patente Nichtigkeitsklage erheben.",
            [frage("Ist eine Nichtigkeitsklage gegen DE 456 B1 jetzt zulässig?", False,
                   ["**Nein!** Klage auf Erklärung der Nichtigkeit kann nicht erhoben werden, solange ein Einspruchsverfahren anhängig ist "
                    "(§ 81 Abs. 2 S. 1 PatG). Der Wortlaut kennt keine Ausnahme für einzelne Nichtigkeitsgründe; die Vorschrift macht die "
                    "Nichtigkeitsklage gegenüber dem Einspruch subsidiär (BGH Strahlungssteuerung)."],
                   merke="Einspruch anhängig: Nichtigkeitsklage gesperrt (§ 81 Abs. 2 S. 1 PatG).", titel="V2 Klagesperre",
                   norms=["§ 81 Abs. 2 PatG"], step=_N + ".1.2"),
             frage("Kann die Mandantin die Sperre aufheben, indem sie ihren Einspruch zurücknimmt?", False,
                   ["**Nein!** Nach Rücknahme wird das Einspruchsverfahren von Amts wegen fortgesetzt (§ 61 Abs. 1 S. 3 PatG), bleibt also anhängig. "
                    "Die Klage ist erst nach rechtskräftigem Abschluss möglich, einschließlich Beschwerde (§ 73 Abs. 2 S. 1 PatG) und "
                    "Rechtsbeschwerde."],
                   merke="Rücknahme beseitigt die Sperre nicht (§ 61 Abs. 1 S. 3 PatG).", titel="Rücknahme des Einspruchs", level=2,
                   norms=["§ 61 Abs. 1 PatG", "§ 81 Abs. 2 PatG"], cases=["pat_bgh_gruppierungssystem"], step=_N + ".1.2"),
             frage("Kann sie beim BPatG Nichtigkeitsklage gegen den deutschen Teil des EP 123 B1 erheben?", False,
                   ["**Nein!** § 81 Abs. 2 S. 1 PatG gilt auch für Nichtigkeitsklagen gegen europäische Patente, solange beim EPA ein Einspruch "
                    "möglich oder anhängig ist (BGH Strahlungssteuerung), selbst wenn die Klage nur auf ein älteres nationales Recht gestützt "
                    "wird (BGH Mautberechnung)."],
                   merke="Klagesperre auch für den EPA-Einspruch (BGH Strahlungssteuerung).", titel="V2 EPA-Einspruch", level=2,
                   norms=["§ 81 Abs. 2 PatG", "Art. II § 6 IntPatÜG"], step=_N + ".1.2"),
             frage("Kann sie stattdessen sofort vor dem EPG gegen EP 123 B1 klagen?", True,
                   ["**Ja!** Das EPG ist für Klagen auf Nichtigerklärung europäischer Patente zuständig (Art. 32 Abs. 1 lit. d EPGÜ), die bei der "
                    "Zentralkammer zu erheben sind (Art. 33 Abs. 4 EPGÜ). Ein vorheriger Einspruch ist nicht nötig, und eine Einspruchssperre "
                    "gibt es nicht (Art. 33 Abs. 8 EPGÜ); das EPG kann bei rasch zu erwartender EPA-Entscheidung aussetzen (Art. 33 Abs. 10 EPGÜ)."],
                   merke="EPG: Zentralkammer, keine Einspruchssperre (Art. 33 Abs. 4, 8 EPGÜ); ausgeschlossen bei Opt-out.", titel="Alternative EPG",
                   level=2, norms=["Art. 32 Abs. 1 EPGÜ", "Art. 33 Abs. 4 EPGÜ", "Art. 33 Abs. 8 EPGÜ"], step=_N + ".1.1"),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_nichtigkeitsklage", "pat_nichtigkeit_ep"], norms=["§ 81 Abs. 2 PatG"]),
    ]),
    # ================================================================== p05f § 73 PatG
    dict(id="p05f", titel="§ 73 PatG: Beschwerde", einheiten=[
        intro("p05f-0", "Prüfungsschema",
              "**AGL:** § 73 Abs. 1 PatG (Entscheidung § 79 PatG)\n\n"
              "**A · Zulässigkeit**\n"
              "**V1 Statthaftigkeit** – Beschluss einer Prüfungsstelle oder Patentabteilung (§ 73 Abs. 1 PatG): Zurückweisung (§ 48 PatG), "
              "Entscheidung über den Einspruch (§ 61 Abs. 1 S. 1 PatG), Feststellung einer Rücknahmefiktion, Ablehnung der Wiedereinsetzung. "
              "Nicht: Prüfungsbescheide (§ 45 PatG) und Mitteilungen ohne Regelung; nicht selbständig anfechtbar ist die Zurückweisung eines "
              "formwidrigen Anhörungsantrags (§ 46 Abs. 1 S. 6 PatG). Kostenfestsetzung: Beschwerde binnen zwei Wochen (§ 62 Abs. 2 S. 4 PatG).\n"
              "**V2 Beschwerdeberechtigung** – nur die am Verfahren vor dem DPMA Beteiligten (§ 74 Abs. 1 PatG): Anmelder, Inhaber, "
              "Einsprechende, Beigetretene; nicht der Dritte, der den Prüfungsantrag gestellt hat (§ 44 Abs. 2 S. 1 PatG), nicht der Hinweisgeber "
              "(§ 43 Abs. 3 S. 2 PatG).\n"
              "**V3 Beschwer** – der Beschluss bleibt hinter dem Antrag des Beschwerdeführers zurück (z. B. Aufrechterhaltung nur nach "
              "Hilfsantrag; Aufrechterhaltung statt Widerruf).\n"
              "**V4 Form** – schriftlich beim DPMA, nicht beim BPatG oder einem PIZ (§ 73 Abs. 2 S. 1 PatG); elektronisch nach § 125a Abs. 1 PatG; "
              "Beschwerdeführer und angefochtener Beschluss müssen erkennbar sein; eine Begründung ist nicht vorgeschrieben, aber geboten.\n"
              "**V5 Frist** – ein Monat nach Zustellung (§ 73 Abs. 2 S. 1 PatG) · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung "
              "§ 193 BGB. Die Verkündung in der Anhörung setzt die Frist nicht in Lauf (§ 47 Abs. 1 S. 3 PatG); sie läuft nur bei "
              "ordnungsgemäßer Rechtsmittelbelehrung (§ 47 Abs. 2 S. 2 PatG; im Einspruchsverfahren über § 59 Abs. 5 PatG), sonst ein Jahr "
              "(§ 47 Abs. 2 S. 3 PatG). Zustellung nach dem VwZG (§ 127 Abs. 1 PatG): Empfangsbekenntnis (§ 5 Abs. 4 VwZG), Einschreiben am "
              "vierten Tag nach Aufgabe (§ 4 Abs. 2 S. 2 VwZG). Wiedereinsetzung möglich (§ 123 PatG), außer für den Einsprechenden gegen die "
              "Aufrechterhaltung (§ 123 Abs. 1 S. 2 Nr. 2 PatG).\n"
              "**V6 Gebühr** – 500 EUR gegen die Entscheidung der Patentabteilung über den Einspruch (Nr. 401 100 Anlage PatKostG), 200 EUR in "
              "anderen Fällen (Nr. 401 300 Anlage PatKostG), 50 EUR gegen Kostenfestsetzung (Nr. 401 200 Anlage PatKostG); fällig mit Einlegung "
              "(§ 3 Abs. 1 S. 2 Nr. 1 PatKostG), zahlbar in der Beschwerdefrist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt die Beschwerde als nicht "
              "eingelegt (§ 6 Abs. 2 PatKostG). Für jeden Beschwerdeführer gesondert; gemeinschaftliche Inhaber oder Anmelder, die gemeinsam "
              "Beschwerde einlegen, gelten seit dem 18.08.2021 als ein Antragsteller (Vorbemerkung Teil B Abs. 1 S. 2 Anlage PatKostG). Vorher: "
              "je eine Gebühr (BGH Mauersteinsatz), bei nur einer Gebühr Zuordnung, im Zweifel zum im Rubrum zuerst Genannten (BGH Mehrschichtlager).\n\n"
              "**B · Verfahren**\n"
              "**V7 Abhilfe** – hält die Stelle die Beschwerde für begründet, hilft sie ab (§ 73 Abs. 3 S. 1 PatG), ggf. mit Rückzahlung der Gebühr "
              "(§ 73 Abs. 3 S. 2 PatG); sonst Vorlage binnen eines Monats ohne sachliche Stellungnahme (§ 73 Abs. 3 S. 3 PatG). Keine Abhilfe, "
              "wenn dem Beschwerdeführer ein anderer Beteiligter gegenübersteht (§ 73 Abs. 4 PatG), also nicht im Einspruchsverfahren.\n"
              "**V8 Aufschiebende Wirkung** – § 75 Abs. 1 PatG.\n"
              "**V9 Beteiligte** – der Beschwerdeführer bestimmt den Gegenstand; mehrere Inhaber oder Anmelder sind notwendige Streitgenossen "
              "(§ 99 Abs. 1 PatG i.V.m. § 62 ZPO); Einsprechende sind Beschwerdegegner der Beschwerde des Inhabers. Der Beschwerdegegner kann "
              "sich auch nach Ablauf der Frist anschließen (§ 99 Abs. 1 PatG i.V.m. § 567 Abs. 3 S. 1 ZPO); die Anschließung verliert ihre "
              "Wirkung, wenn die Beschwerde zurückgenommen oder verworfen wird (§ 567 Abs. 3 S. 2 ZPO).\n\n"
              "**C · Begründetheit**\n"
              "**V10 Prüfungsrahmen** – Untersuchungsgrundsatz (§ 87 Abs. 1 PatG), neue Tatsachen und Beweismittel zulässig. Im "
              "Einspruchsbeschwerdeverfahren keine neuen Widerrufsgründe von Amts wegen; der Einsprechende darf sie in einer zulässigen "
              "Beschwerde geltend machen (BGH Ventileinrichtung). Verschlechterungsverbot: Abänderung nur, soweit beantragt (Rechtsgedanke "
              "§ 528 S. 2 ZPO i.V.m. § 99 Abs. 1 PatG). Im Erteilungsbeschwerdeverfahren neue Anträge im Rahmen des § 38 PatG.\n\n"
              "**⇒ Rechtsfolge:** Beschluss (§ 79 Abs. 1 PatG): Verwerfung als unzulässig, auch ohne mündliche Verhandlung (§ 79 Abs. 2 PatG); "
              "Zurückweisung; Aufhebung mit eigener Sachentscheidung oder Zurückverweisung, wenn das DPMA noch nicht in der Sache entschieden hat, "
              "das Verfahren wesentlich mangelhaft ist oder wesentliche neue Tatsachen oder Beweismittel bekannt werden (§ 79 Abs. 3 S. 1 Nr. 1 bis 3 "
              "PatG), mit Bindung des DPMA (§ 79 Abs. 3 S. 2 PatG). Mündliche Verhandlung auf Antrag (§ 78 Nr. 1 PatG). Kosten nach Billigkeit "
              "(§ 80 Abs. 1 PatG), Rückzahlung der Beschwerdegebühr (§ 80 Abs. 3 PatG). Danach Rechtsbeschwerde (§ 100 PatG).\n\n"
              "**Klausurfallen:** Beschwerde beim BPatG oder PIZ; Frist ab Verkündung gerechnet; zwei Inhaber, eine Gebühr (Rechtslage vor und "
              "nach dem 18.08.2021); 200 statt 500 EUR in Einspruchssachen; Abhilfe im zweiseitigen Verfahren; ein Einsprechender kann sich der "
              "Beschwerde des anderen nicht anschließen (kein Beschwerdegegner); Verschlechterungsverbot; Teilung neben der Beschwerde (die "
              "Anmeldung bleibt bis zum Ablauf der Beschwerdefrist anhängig).\n\n"
              "**In den Klausuren:** TS III/2020 (verkündete Zurückweisung), TS I/2021 (Beschwerde neben Teilung, Wiedereinsetzung), TS II/2021 "
              "(zwei Inhaberinnen, eine Gebühr, Beteiligte, Anschlussbeschwerde, Verschlechterungsverbot), TS II/2022 (Anmeldergemeinschaft vor "
              "und nach dem 18.08.2021), TS III/2022 (Feststellung der Rücknahmefiktion), TS I/2023 (Beschwerde gegen den Widerruf), TS II/2023 "
              "(neue Beweismittel), TS III/2023.",
              concepts=["pat_beschwerde", "pat_abhilfe", "pat_gebuehren", "pat_fristen"],
              norms=["§ 73 Abs. 1 PatG", "§ 73 Abs. 2 PatG", "§ 73 Abs. 3 PatG", "§ 73 Abs. 4 PatG", "§ 74 Abs. 1 PatG", "§ 79 PatG",
                     "§ 47 Abs. 2 PatG", "§ 6 Abs. 2 PatKostG"],
              cases=["pat_bgh_ventileinrichtung"], abschnitt="Normenkette"),
        intro("p05f-1", "Definitionen",
              "**Beschwerde:** Rechtsmittel der am Verfahren vor dem DPMA Beteiligten gegen Beschlüsse der Prüfungsstellen und Patentabteilungen "
              "zum BPatG, schriftlich beim DPMA binnen eines Monats nach Zustellung (§ 73 Abs. 1, 2 PatG, § 74 Abs. 1 PatG).\n"
              "**Beschluss:** Entscheidung des DPMA, die das Verfahren ganz oder teilweise abschließend regelt; zu begründen, zuzustellen und mit "
              "Rechtsmittelbelehrung zu versehen (§ 47 Abs. 1, 2 PatG). Ein Prüfungsbescheid (§ 45 PatG) regelt nichts und ist kein Beschluss.\n"
              "**Beschwer (formell):** Die angefochtene Entscheidung bleibt hinter dem im Verfahren gestellten Antrag des Beschwerdeführers zurück.\n"
              "**Abhilfe:** Aufhebung oder Änderung des eigenen Beschlusses durch die Stelle, die ihn erlassen hat, wenn sie die Beschwerde für "
              "begründet hält; nur im einseitigen Verfahren (§ 73 Abs. 3 S. 1, Abs. 4 PatG).\n"
              "**Unselbständige Anschlussbeschwerde:** Antrag des Beschwerdegegners, die angefochtene Entscheidung zu seinen Gunsten zu ändern, "
              "auch nach Ablauf der Beschwerdefrist; sie steht und fällt mit der Hauptbeschwerde (§ 99 Abs. 1 PatG i.V.m. § 567 Abs. 3 ZPO).\n"
              "**Verschlechterungsverbot:** Ohne Rechtsmittel des Gegners darf die Entscheidung nicht zum Nachteil des Beschwerdeführers geändert "
              "werden (Rechtsgedanke § 528 S. 2 ZPO).\n"
              "**Notwendige Streitgenossen:** mehrere Anmelder oder Inhaber, weil über Anmeldung und Patent nur einheitlich entschieden werden "
              "kann; säumige gelten als durch die nicht säumigen vertreten (§ 99 Abs. 1 PatG i.V.m. § 62 Abs. 1 ZPO).",
              concepts=["pat_beschwerde", "pat_abhilfe", "pat_beschluss_pruefungsstelle"],
              norms=["§ 73 Abs. 1 PatG", "§ 73 Abs. 3 PatG", "§ 74 Abs. 1 PatG", "§ 47 Abs. 1 PatG", "§ 99 Abs. 1 PatG"], abschnitt="Definitionen"),
        fall("p05f-2", "Beschwerde gegen den Prüfungsbescheid",
             "Die Prüfungsstelle teilt der Anmelderin in einem Bescheid nach § 45 Abs. 2 PatG mit, Anspruch 1 sei nicht neu, und setzt eine "
             "Frist zur Äußerung von vier Monaten. Die Anmelderin will sofort Beschwerde einlegen.",
             "Ist die Beschwerde statthaft?", False,
             ["**Nein!** Die Beschwerde findet nur gegen Beschlüsse der Prüfungsstellen und Patentabteilungen statt (§ 73 Abs. 1 PatG). Der "
              "Prüfungsbescheid regelt nichts, sondern gibt Gelegenheit zur Äußerung (§ 45 Abs. 2 PatG). Die Anmelderin muss erwidern, ändern "
              "(§ 38 PatG) oder die Anhörung beantragen (§ 46 Abs. 1 S. 3 PatG); erst gegen die Zurückweisung (§ 48 PatG) ist die Beschwerde gegeben."],
             merke="Beschwerde nur gegen Beschlüsse (§ 73 Abs. 1 PatG), nicht gegen Bescheide.", level=1,
             concepts=["pat_beschwerde", "pat_pruefungsbescheid"], norms=["§ 73 Abs. 1 PatG", "§ 45 Abs. 2 PatG", "§ 48 PatG"], step=_E + ".4.1",
             abschnitt="Definitionen und Normen"),
        mc("p05f-3", "Beschwerdegebühr",
           "Welche Beschwerdegebühr gilt gegen die Zurückweisung einer Anmeldung und welche gegen den Beschluss der Patentabteilung im "
           "Einspruchsverfahren?",
           ["200 EUR (Nr. 401 300) gegen die Zurückweisung, 500 EUR (Nr. 401 100) gegen die Einspruchsentscheidung, jeweils in der Beschwerdefrist",
            "Jeweils 200 EUR, zahlbar binnen drei Monaten",
            "500 EUR gegen die Zurückweisung, 200 EUR gegen die Einspruchsentscheidung",
            "Jeweils 500 EUR, zahlbar mit der Begründung"], 0,
           ["**Nr. 401 300 und 401 100 Anlage PatKostG.** Die Beschwerde gegen die Entscheidung der Patentabteilung über den Einspruch kostet "
            "500 EUR, andere Beschwerden 200 EUR. Fällig mit Einlegung (§ 3 Abs. 1 S. 2 Nr. 1 PatKostG), zu zahlen in der Monatsfrist des "
            "§ 73 Abs. 2 S. 1 PatG (§ 6 Abs. 1 S. 1 PatKostG); sonst gilt die Beschwerde als nicht eingelegt (§ 6 Abs. 2 PatKostG)."],
           merke="Erteilung: 200 EUR (401 300) · Einspruch: 500 EUR (401 100) · in der Beschwerdefrist.", level=1,
           concepts=["pat_gebuehren", "pat_beschwerde"], norms=["§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG", "§ 73 Abs. 2 PatG"], step=_E + ".4.1",
           abschnitt="Definitionen und Normen"),
        fall("p05f-4", "Zwei Anmelder, eine Gebühr (heute)",
             "Anton und Andrea Ackermann, gemeinsame Anmelder, legen am 23.08.2021 fristgerecht gemeinsam Beschwerde gegen die Zurückweisung "
             "ihrer Anmeldung ein und zahlen am selben Tag einmal 200 EUR.",
             "Ist die Beschwerde für beide wirksam eingelegt?", True,
             ["**Ja!** Die Beschwerdegebühren werden für jeden Antragsteller gesondert erhoben; gemeinschaftliche Anmelder oder Inhaber gelten "
              "aber als ein Antragsteller, wenn sie gemeinsam Beschwerde einlegen (Vorbemerkung Teil B Abs. 1 S. 2 Anlage PatKostG, seit "
              "18.08.2021). Die Gebühr wurde mit Einlegung am 23.08.2021 fällig, also nach neuem Recht (TS II/2022). Bei Einlegung vor dem "
              "18.08.2021 wären zwei Gebühren nötig gewesen."],
             merke="Seit 18.08.2021: gemeinsame Beschwerde gemeinschaftlicher Anmelder oder Inhaber = eine Gebühr.", level=2,
             concepts=["pat_gebuehren"], norms=["§ 3 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG"], step=_E + ".4.1", abschnitt="Definitionen und Normen"),
        fall("p05f-5", "Abhilfe im Einspruchsbeschwerdeverfahren",
             "Die Patentabteilung hat das Patent auf den Einspruch der E widerrufen. Die Inhaberin legt Beschwerde ein und legt neue "
             "Versuchsergebnisse vor, die die Patentabteilung überzeugen.",
             "Darf die Patentabteilung der Beschwerde abhelfen?", False,
             ["**Nein!** Steht dem Beschwerdeführer ein anderer am Verfahren Beteiligter gegenüber, gilt § 73 Abs. 3 S. 1 PatG nicht "
              "(§ 73 Abs. 4 PatG). Im Einspruchsverfahren ist die Einsprechende Gegnerin der Inhaberin; die Patentabteilung muss die Beschwerde "
              "ohne sachliche Stellungnahme binnen eines Monats dem BPatG vorlegen (§ 73 Abs. 3 S. 3 PatG)."],
             merke="Abhilfe nur im einseitigen Verfahren (§ 73 Abs. 3 S. 1, Abs. 4 PatG).", level=2,
             concepts=["pat_abhilfe"], norms=["§ 73 Abs. 3 PatG", "§ 73 Abs. 4 PatG"], step=_E + ".4.2", abschnitt="Definitionen und Normen"),
        mc("p05f-6", "Wiedereinsetzung in die Beschwerdefrist",
           "Wer kann Wiedereinsetzung in die versäumte Beschwerdefrist beantragen, wenn er ohne Verschulden verhindert war?",
           ["Die Inhaberin gegen den Widerruf ja, die Einsprechende gegen die Aufrechterhaltung nicht",
            "Beide ja, weil die Beschwerdefrist eine gesetzliche Frist ist",
            "Beide nicht, weil Rechtsmittelfristen nie wiedereinsetzungsfähig sind",
            "Die Einsprechende ja, die Inhaberin nicht"], 0,
           ["**§ 123 Abs. 1 S. 2 Nr. 2 PatG.** Ausgeschlossen ist die Wiedereinsetzung nur für den Einsprechenden in die Frist zur Beschwerde "
            "gegen die Aufrechterhaltung des Patents und zur Zahlung der Beschwerdegebühr. Die Inhaberin, deren Patent widerrufen wurde, und der "
            "Anmelder nach Zurückweisung können Wiedereinsetzung beantragen (§ 123 Abs. 1 S. 1 PatG), binnen zwei Monaten nach Wegfall des "
            "Hindernisses (§ 123 Abs. 2 PatG)."],
           merke="Keine Wiedereinsetzung für Einsprechende: Einspruchsfrist (Nr. 1), Beschwerde gegen Aufrechterhaltung (Nr. 2).", level=2,
           concepts=["pat_wiedereinsetzung"], norms=["§ 123 Abs. 1 PatG", "§ 123 Abs. 2 PatG"], step=_E + ".4.1", abschnitt="Definitionen und Normen"),
        fall("p05f-7", "Neue Druckschrift, neuer Grund",
             "Die Patentabteilung hält das Patent aufrecht. Die Einsprechende, deren Einspruch auf fehlende Neuheit gestützt war, legt "
             "zulässig Beschwerde ein und macht erstmals geltend, Anspruch 1 sei unzulässig erweitert.",
             "Darf das BPatG diesen neuen Widerrufsgrund prüfen?", True,
             ["**Ja!** Von Amts wegen darf das BPatG im Einspruchsbeschwerdeverfahren keine neuen Widerrufsgründe aufgreifen. Ist die "
              "aufrechterhaltende Entscheidung aber in zulässiger Weise angefochten, darf der Einsprechende zusätzliche Widerrufsgründe geltend "
              "machen (BGH Ventileinrichtung). Neue Beweismittel zum bisherigen Grund, etwa eine neue Druckschrift zur Neuheit, sind ohnehin "
              "zu berücksichtigen (§ 87 Abs. 1 PatG; TS II/2023)."],
             merke="Neuer Widerrufsgrund in der Beschwerde: nicht von Amts wegen, aber auf Antrag des beschwerdeführenden Einsprechenden.",
             level=3, concepts=["pat_beschwerde", "pat_widerrufsgruende"], norms=["§ 87 Abs. 1 PatG", "§ 21 Abs. 1 PatG"],
             cases=["pat_bgh_ventileinrichtung"], step=_E + ".4.3", abschnitt="Definitionen und Normen"),
        *fallkette("p05f-8", "Zwei Inhaberinnen, eine Gebühr (nach TS II/2021)",
            "Die Patentabteilung hält das Patent der A1-AG und der A2-GmbH auf die Einsprüche von E1 und E2 nur nach dem Hilfsantrag aufrecht; "
            "der Beschluss mit Belehrung wird am Mo 13.04.2015 zugestellt. Am Mo 04.05.2015 legen beide Inhaberinnen gemeinsam Beschwerde "
            "ein und zahlen einmal 500 EUR ohne Zuordnung. Es gilt das Recht von 2015.",
            [frage("Ist die Beschwerde statthaft und sind die Inhaberinnen beschwert?", True,
                   ["**Ja!** Die Entscheidung über den Einspruch ergeht durch Beschluss der Patentabteilung (§ 61 Abs. 1 S. 1 PatG), gegen den die "
                    "Beschwerde stattfindet (§ 73 Abs. 1 PatG). Die Inhaberinnen sind Beteiligte (§ 74 Abs. 1 PatG) und beschwert, weil ihr "
                    "Hauptantrag auf Aufrechterhaltung in der erteilten Fassung abgelehnt wurde."],
                   merke="Aufrechterhaltung nur nach Hilfsantrag beschwert den Inhaber.", titel="V1 bis V3", norms=["§ 73 Abs. 1 PatG", "§ 74 Abs. 1 PatG"],
                   step=_E + ".4.1"),
             frage("Wann endet die Beschwerdefrist?", 1,
                   ["**Mi 13.05.2015.** Ein Monat nach Zustellung (§ 73 Abs. 2 S. 1 PatG); der Zustellungstag zählt nicht (§ 187 Abs. 1 BGB), "
                    "Ende am Tag gleicher Zahl (§ 188 Abs. 2 BGB), ein Mittwoch (§ 193 BGB greift nicht). Die Belehrung lag vor (§ 47 Abs. 2 S. 2 "
                    "PatG i.V.m. § 59 Abs. 5 PatG). Die Beschwerde vom 04.05.2015 ist rechtzeitig."],
                   optionen=["Di 12.05.2015", "Mi 13.05.2015", "Fr 15.05.2015", "Mo 13.07.2015"],
                   merke="Beschwerdefrist § 73 Abs. 2 S. 1 PatG · § 187 Abs. 1, § 188 Abs. 2 BGB · § 193 BGB.", titel="V5 Frist", step=_E + ".4.1"),
             frage("Genügte 2015 eine Gebühr für beide Inhaberinnen?", False,
                   ["**Nein!** Legen mehrere Patentinhaber Beschwerde ein, hat jeder eine Gebühr zu entrichten (BGH Mauersteinsatz; Vorbemerkung "
                    "Teil B Abs. 1 Anlage PatKostG a.F.). Die Ausnahme für gemeinschaftliche Inhaber gilt erst seit dem 18.08.2021 und wirkt nicht "
                    "zurück. Mit 500 EUR ist nur eine Beschwerde bezahlt."],
                   merke="Vor 18.08.2021: Gebühr je Beschwerdeführer, auch für Mitinhaber.", titel="V6 Gebühr a.F.", level=2, step=_E + ".4.1"),
             frage("Für wen gilt die Beschwerde als eingelegt?", 0,
                   ["**Für die A1-AG.** Ist die eine Gebühr keinem Beteiligten zuzuordnen, ist die Erklärung im Zweifel so auszulegen, dass die "
                    "Beschwerde für den im Rubrum der angefochtenen Entscheidung an erster Stelle Genannten erhoben ist (BGH Mehrschichtlager). "
                    "Für die A2-GmbH gilt sie als nicht eingelegt (§ 6 Abs. 2 PatKostG); sie bleibt als notwendige Streitgenossin beteiligt "
                    "(§ 62 ZPO i.V.m. § 99 Abs. 1 PatG)."],
                   optionen=["Für die im Rubrum zuerst genannte A1-AG", "Für beide je zur Hälfte", "Für keine",
                             "Für die Inhaberin, die das DPMA wählt"],
                   merke="Eine Gebühr, mehrere Beschwerdeführer: Zuordnung, im Zweifel zum Erstgenannten im Rubrum.", titel="Zuordnung der Gebühr",
                   level=2, step=_E + ".4.1"),
             frage("Darf das BPatG das Patent auch in der Hilfsantragsfassung widerrufen, wenn nur die A1-AG Beschwerde führt?", False,
                   ["**Nein!** Über den Gegenstand des Beschwerdeverfahrens verfügt der Beschwerdeführer; die angefochtene Entscheidung darf nur "
                    "abgeändert werden, soweit dies beantragt ist (Verschlechterungsverbot, Rechtsgedanke § 528 S. 2 ZPO i.V.m. § 99 Abs. 1 PatG). "
                    "Ohne Rechtsmittel der Einsprechenden bleibt die Hilfsantragsfassung bestehen."],
                   merke="Verschlechterungsverbot: kein Widerruf auf die Beschwerde des Inhabers allein.", titel="V10 Verschlechterungsverbot",
                   level=2, step=_E + ".4.3"),
             frage("Kann sich E2 der Beschwerde in der mündlichen Verhandlung noch anschließen, um den vollständigen Widerruf zu erreichen?", True,
                   ["**Ja!** Der Beschwerdegegner kann sich der Beschwerde anschließen, selbst wenn die Beschwerdefrist verstrichen ist "
                    "(§ 567 Abs. 3 S. 1 ZPO i.V.m. § 99 Abs. 1 PatG), bis zum Schluss der mündlichen Verhandlung (§ 91 Abs. 3 S. 1 PatG). Die "
                    "Anschließung verliert ihre Wirkung, wenn die A1-AG ihre Beschwerde zurücknimmt (§ 567 Abs. 3 S. 2 ZPO)."],
                   merke="Unselbständige Anschlussbeschwerde: Beschwerdegegner, auch nach Fristablauf, abhängig von der Hauptbeschwerde.",
                   titel="Anschlussbeschwerde", level=3, step=_E + ".4.3"),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_beschwerde"], norms=["§ 73 Abs. 1 PatG"]),
        *fallkette("p05f-9", "Zurückweisung in der Anhörung (nach TS III/2020)",
            "In der Anhörung am Mi 24.09.2014 verkündet die Prüfungsstelle die Zurückweisung der Anmeldung der A-GmbH. Der begründete "
            "Beschluss mit Rechtsmittelbelehrung geht dem Patentanwalt am Mi 15.10.2014 gegen Empfangsbekenntnis zu.",
            [frage("Läuft die Beschwerdefrist schon ab der Verkündung in der Anhörung?", False,
                   ["**Nein!** Beschlüsse können am Ende einer Anhörung verkündet werden, sind aber trotzdem begründet zuzustellen "
                    "(§ 47 Abs. 1 S. 1, 3 PatG). Die Frist läuft ab Zustellung (§ 73 Abs. 2 S. 1 PatG) und nur mit Belehrung (§ 47 Abs. 2 S. 2 PatG)."],
                   merke="Fristbeginn: Zustellung des begründeten Beschlusses mit Belehrung, nicht Verkündung.", titel="V5 Fristbeginn",
                   norms=["§ 47 Abs. 1 PatG", "§ 47 Abs. 2 PatG"], step=_E + ".4.1"),
             frage("Wann endet die Beschwerdefrist?", 2,
                   ["**Mo 17.11.2014.** Zustellung mit dem Empfangsbekenntnis am 15.10.2014 (§ 127 Abs. 1 PatG i.V.m. § 5 Abs. 4 VwZG); ein Monat "
                    "endet am Sa 15.11.2014 (§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB) und verschiebt sich auf den nächsten Werktag (§ 193 BGB)."],
                   optionen=["Fr 24.10.2014", "Sa 15.11.2014", "Mo 17.11.2014", "Mo 15.12.2014"],
                   merke="Fristende am Samstag: nächster Werktag (§ 193 BGB).", titel="V5 Fristende", step=_E + ".4.1"),
             frage("Welche Gebühr ist in der Frist zu zahlen?", 0,
                   ["**200 EUR (Nr. 401 300 Anlage PatKostG).** Die Beschwerde richtet sich nicht gegen eine Einspruchsentscheidung, also „in "
                    "anderen Fällen“. Fällig mit Einlegung (§ 3 Abs. 1 S. 2 Nr. 1 PatKostG), zahlbar bis zum 17.11.2014 (§ 6 Abs. 1 S. 1 PatKostG); "
                    "beim SEPA-Basislastschriftmandat zählt der Eingang beim DPMA (§ 2 Nr. 3 PatKostZV)."],
                   optionen=["200 EUR (Nr. 401 300)", "500 EUR (Nr. 401 100)", "300 EUR (Nr. 400 000)", "50 EUR (Nr. 401 200)"],
                   merke="Beschwerde gegen Zurückweisung: 200 EUR, Nr. 401 300 Anlage PatKostG.", titel="V6 Gebühr", step=_E + ".4.1"),
             frage("Kann die Prüfungsstelle der Beschwerde mit geänderten Ansprüchen selbst abhelfen?", True,
                   ["**Ja!** Hält die Stelle, deren Beschluss angefochten ist, die Beschwerde für begründet, hat sie abzuhelfen (§ 73 Abs. 3 S. 1 PatG). "
                    "Im Erteilungsverfahren steht der Anmelderin kein anderer Beteiligter gegenüber; § 73 Abs. 4 PatG greift nicht. Sonst legt sie "
                    "binnen eines Monats dem BPatG vor (§ 73 Abs. 3 S. 3 PatG)."],
                   merke="Einseitiges Verfahren: Abhilfe möglich (§ 73 Abs. 3 S. 1 PatG).", titel="V7 Abhilfe", norms=["§ 73 Abs. 3 PatG"],
                   concepts=["pat_abhilfe"], step=_E + ".4.2"),
            ],
            abschnitt="Klausurfall", level=1, concepts=["pat_beschwerde"], norms=["§ 73 Abs. 2 PatG"]),
    ]),
    # ================================================================== p05g §§ 100 bis 102 PatG
    dict(id="p05g", titel="§§ 100 bis 102 PatG: Rechtsbeschwerde", einheiten=[
        intro("p05g-0", "Prüfungsschema",
              "**AGL:** § 100 Abs. 1 PatG (zugelassene Rechtsbeschwerde) oder § 100 Abs. 3 PatG (zulassungsfreie Rechtsbeschwerde)\n\n"
              "**A · Zulässigkeit**\n"
              "**V1 Statthaftigkeit** – Beschluss eines Beschwerdesenats des BPatG über eine Beschwerde nach § 73 PatG oder über Aufrechterhaltung "
              "oder Widerruf nach § 61 Abs. 2 PatG (§ 100 Abs. 1 PatG), auch wenn das BPatG an Stelle des DPMA den Einspruch verworfen hat (BGH "
              "Leistungshalbleiterbauelement). Nicht gegen Urteile der Nichtigkeitssenate (Berufung, § 110 PatG).\n"
              "**V2 Zulassung** – im Beschluss (§ 100 Abs. 1 PatG), zwingend bei Rechtsfrage von grundsätzlicher Bedeutung (§ 100 Abs. 2 Nr. 1 PatG) "
              "oder wenn Fortbildung des Rechts oder Sicherung einer einheitlichen Rechtsprechung eine Entscheidung des BGH erfordert "
              "(§ 100 Abs. 2 Nr. 2 PatG). Eine Nichtzulassungsbeschwerde gibt es nicht (§ 99 Abs. 2 PatG).\n"
              "**V2a oder: zulassungsfreier Mangel** – § 100 Abs. 3 PatG: Mangel liegt vor und wird gerügt: nicht vorschriftsmäßige Besetzung (Nr. 1), "
              "ausgeschlossener oder erfolgreich abgelehnter Richter (Nr. 2), Versagung des rechtlichen Gehörs (Nr. 3), Vertretungsmangel (Nr. 4), "
              "Verletzung der Öffentlichkeit (Nr. 5), Beschluss nicht mit Gründen versehen (Nr. 6). Materielle Fehler genügen nicht.\n"
              "**V3 Berechtigung** – Beteiligte des Beschwerdeverfahrens (§ 101 Abs. 1 PatG), beschwert durch den Beschluss.\n"
              "**V4 Frist und Form** – ein Monat nach Zustellung des Beschlusses, schriftlich beim BGH (§ 102 Abs. 1 PatG) · Berechnung "
              "§ 106 Abs. 1 S. 1 PatG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 222 Abs. 2 ZPO; "
              "Wiedereinsetzung nach der ZPO (§ 106 Abs. 1 S. 1 PatG).\n"
              "**V5 Begründung** – binnen eines Monats ab Einlegung, auf Antrag verlängerbar (§ 102 Abs. 3 PatG); Inhalt: Umfang der Anfechtung und "
              "Antrag, verletzte Rechtsnorm, bei Verfahrensrügen die Tatsachen, die den Mangel ergeben (§ 102 Abs. 4 Nr. 1 bis 3 PatG).\n"
              "**V6 Vertretung** – durch einen beim BGH zugelassenen Rechtsanwalt; dem Patentanwalt ist auf Antrag das Wort zu gestatten "
              "(§ 102 Abs. 5 PatG).\n\n"
              "**B · Begründetheit**\n"
              "**V7 Rechtsverletzung** – der Beschluss beruht auf einer Verletzung des Rechts (§ 101 Abs. 2 S. 1 PatG; § 546 ZPO und § 547 ZPO "
              "entsprechend, § 101 Abs. 2 S. 2 PatG); der BGH ist an die tatsächlichen Feststellungen gebunden (§ 107 Abs. 2 PatG). Die Auslegung "
              "von Patent und Anmeldung ist Rechtsfrage.\n\n"
              "**⇒ Rechtsfolge:** Prüfung der Zulässigkeit von Amts wegen, sonst Verwerfung (§ 104 PatG); aufschiebende Wirkung (§ 103 PatG); "
              "Entscheidung durch Beschluss (§ 107 Abs. 1 PatG); bei Aufhebung Zurückverweisung an das BPatG (§ 108 Abs. 1 PatG), das an die "
              "rechtliche Beurteilung gebunden ist (§ 108 Abs. 2 PatG).\n\n"
              "**Klausurfallen:** Zulassung beim BGH beantragen (gibt es nicht); materiellen Fehler als Gehörsverletzung verkleiden; falsche "
              "Begründung mit fehlender Begründung verwechseln; Einlegung beim BPatG; Patentanwalt allein; Begründungsfrist ab Zustellung statt "
              "ab Einlegung; Rechtsbeschwerde gegen das Nichtigkeitsurteil (richtig: Berufung).\n\n"
              "**In den Klausuren:** TS I/2023 (zugelassene und zulassungsfreie Rechtsbeschwerde nach Widerruf wegen Auswahl aus einer Formel), "
              "TS III/2021 (rechtskräftiger Abschluss des Einspruchsverfahrens einschließlich Rechtsbeschwerde vor der Nichtigkeitsklage).",
              concepts=["pat_rechtsbeschwerde", "pat_rechtliches_gehoer"],
              norms=["§ 100 Abs. 1 PatG", "§ 100 Abs. 2 PatG", "§ 100 Abs. 3 PatG", "§ 101 Abs. 2 PatG", "§ 102 Abs. 1 PatG", "§ 108 PatG"],
              cases=["pat_bgh_leistungshalbleiterbauelement", "pat_bgh_schwingungsdaempfer"], abschnitt="Normenkette"),
        intro("p05g-1", "Definitionen",
              "**Rechtsbeschwerde:** Rechtsmittel der Beteiligten des Beschwerdeverfahrens zum BGH gegen Beschlüsse der Beschwerdesenate, "
              "beschränkt auf Rechtsfehler (§ 100 Abs. 1 PatG, § 101 PatG).\n"
              "**Grundsätzliche Bedeutung:** Die Sache wirft eine entscheidungserhebliche, klärungsbedürftige Rechtsfrage auf, die sich in einer "
              "unbestimmten Vielzahl von Fällen stellen kann (§ 100 Abs. 2 Nr. 1 PatG; Begriff wie bei den Zulassungsgründen der ZPO).\n"
              "**Versagung des rechtlichen Gehörs:** Das Gericht hat erheblichen Vortrag nicht zur Kenntnis genommen oder seine Entscheidung auf "
              "einen Gesichtspunkt gestützt, zu dem sich der Beteiligte nicht äußern konnte und mit dem er nicht rechnen musste "
              "(Art. 103 Abs. 1 GG, § 100 Abs. 3 Nr. 3 PatG).\n"
              "**Nicht mit Gründen versehen:** Gründe fehlen ganz oder sind so unverständlich oder lückenhaft, dass sie die Entscheidung nicht "
              "tragen; eine bloß sachlich falsche Begründung genügt nicht (§ 100 Abs. 3 Nr. 6 PatG).\n"
              "**Zulassungsfreie Rechtsbeschwerde:** Rechtsbeschwerde ohne Zulassung wegen eines der in § 100 Abs. 3 Nr. 1 bis 6 PatG abschließend "
              "genannten Verfahrensmängel, der vorliegen und gerügt sein muss.",
              concepts=["pat_rechtsbeschwerde", "pat_rechtliches_gehoer"], norms=["§ 100 Abs. 2 PatG", "§ 100 Abs. 3 PatG", "§ 101 PatG"],
              abschnitt="Definitionen"),
        mc("p05g-2", "Wogegen findet die Rechtsbeschwerde statt?",
           "Gegen welche Entscheidung ist die Rechtsbeschwerde nach § 100 Abs. 1 PatG statthaft?",
           ["Beschluss des Beschwerdesenats über die Beschwerde gegen einen Widerrufsbeschluss der Patentabteilung",
            "Urteil des Nichtigkeitssenats",
            "Beschluss der Patentabteilung über den Einspruch",
            "Zwischenverfügung des Berichterstatters im Beschwerdeverfahren"], 0,
           ["**Beschwerdesenat, § 73 PatG oder § 61 Abs. 2 PatG.** Die Rechtsbeschwerde findet gegen Beschlüsse der Beschwerdesenate statt, durch "
            "die über eine Beschwerde nach § 73 PatG oder über Aufrechterhaltung oder Widerruf nach § 61 Abs. 2 PatG entschieden wird. Gegen "
            "Nichtigkeitsurteile gibt es die Berufung (§ 110 Abs. 1 PatG), gegen Beschlüsse der Patentabteilung die Beschwerde (§ 73 Abs. 1 PatG)."],
           merke="DPMA → Beschwerde (§ 73 PatG) → BPatG-Beschluss → Rechtsbeschwerde (§ 100 PatG); Nichtigkeitsurteil → Berufung (§ 110 PatG).", level=1,
           concepts=["pat_rechtsbeschwerde"], norms=["§ 100 Abs. 1 PatG", "§ 110 Abs. 1 PatG"], step=_E + ".4.3", abschnitt="Definitionen und Normen"),
        mc("p05g-3", "Zulassungsgründe",
           "Wann muss der Beschwerdesenat die Rechtsbeschwerde zulassen?",
           ["Bei einer Rechtsfrage von grundsätzlicher Bedeutung oder wenn Fortbildung des Rechts oder Einheitlichkeit der Rechtsprechung "
            "eine BGH-Entscheidung erfordert",
            "Wenn ein Beteiligter es beantragt",
            "Wenn der Streitwert 20.000 EUR übersteigt",
            "Wenn die Entscheidung von der des DPMA abweicht"], 0,
           ["**§ 100 Abs. 2 Nr. 1, 2 PatG.** Die Rechtsbeschwerde ist zuzulassen, wenn eine Rechtsfrage von grundsätzlicher Bedeutung zu "
            "entscheiden ist oder die Fortbildung des Rechts oder die Sicherung einer einheitlichen Rechtsprechung eine Entscheidung des BGH "
            "erfordert. Ein Antrag oder ein Streitwert spielt keine Rolle; gegen die Nichtzulassung gibt es kein Rechtsmittel (§ 99 Abs. 2 PatG)."],
           merke="Zulassung § 100 Abs. 2 PatG: grundsätzliche Bedeutung · Rechtsfortbildung · einheitliche Rechtsprechung.", level=1,
           concepts=["pat_rechtsbeschwerde"], norms=["§ 100 Abs. 2 PatG", "§ 99 Abs. 2 PatG"], step=_E + ".4.3", abschnitt="Definitionen und Normen"),
        mc("p05g-4", "Zulassungsfreie Rechtsbeschwerde",
           "Welcher Mangel eröffnet die Rechtsbeschwerde ohne Zulassung nicht?",
           ["Der Senat hat § 21 Abs. 1 Nr. 4 PatG falsch angewandt",
            "Ein Richter war von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen",
            "Der Senat hat entscheidungserheblichen Vortrag übergangen",
            "Der Beschluss enthält keine Gründe"], 0,
           ["**Materieller Fehler.** § 100 Abs. 3 PatG nennt abschließend Verfahrensmängel: Besetzung (Nr. 1), ausgeschlossener oder abgelehnter "
            "Richter (Nr. 2), Versagung des rechtlichen Gehörs (Nr. 3), Vertretung (Nr. 4), Öffentlichkeit (Nr. 5), fehlende Gründe (Nr. 6). "
            "Die falsche Anwendung des materiellen Rechts ist nur mit Zulassung angreifbar (§ 100 Abs. 1 PatG; TS I/2023)."],
           merke="§ 100 Abs. 3 PatG: nur die sechs Verfahrensmängel, die vorliegen und gerügt werden.", level=2,
           concepts=["pat_rechtsbeschwerde", "pat_rechtliches_gehoer"], norms=["§ 100 Abs. 3 PatG"], step=_E + ".4.3", abschnitt="Definitionen und Normen"),
        fall("p05g-5", "Einlegung durch den Patentanwalt",
             "Patentanwalt P legt für die Anmelderin fristgerecht schriftlich beim BGH Rechtsbeschwerde gegen den Beschluss des Beschwerdesenats "
             "ein; die Rechtsbeschwerde ist zugelassen. Ein beim BGH zugelassener Rechtsanwalt ist nicht beteiligt.",
             "Ist die Rechtsbeschwerde wirksam eingelegt?", False,
             ["**Nein!** Vor dem BGH müssen sich die Beteiligten durch einen beim BGH zugelassenen Rechtsanwalt als Bevollmächtigten vertreten "
              "lassen (§ 102 Abs. 5 S. 1 PatG); dem Patentanwalt ist nur auf Antrag das Wort zu gestatten (§ 102 Abs. 5 S. 2 PatG). Der BGH "
              "prüft die Form von Amts wegen und verwirft (§ 104 PatG). Anders die Nichtigkeitsberufung: dort genügt ein Patentanwalt (§ 113 PatG)."],
             merke="Rechtsbeschwerde: BGH-Anwalt (§ 102 Abs. 5 PatG); Nichtigkeitsberufung: auch Patentanwalt (§ 113 PatG).", level=2,
             concepts=["pat_rechtsbeschwerde"], norms=["§ 102 Abs. 5 PatG", "§ 104 PatG", "§ 113 PatG"], step=_E + ".4.3",
             abschnitt="Definitionen und Normen"),
        fall("p05g-6", "Neue Druckschrift beim BGH",
             "Nach Zustellung des zurückweisenden Beschlusses findet die Rechtsbeschwerdeführerin eine Druckschrift, die die vom BPatG "
             "festgestellte Neuheit widerlegt, und will sie im Rechtsbeschwerdeverfahren vorlegen.",
             "Berücksichtigt der BGH die neue Druckschrift?", False,
             ["**Nein!** Die Rechtsbeschwerde kann nur darauf gestützt werden, dass der Beschluss auf einer Verletzung des Rechts beruht "
              "(§ 101 Abs. 2 S. 1 PatG). Der BGH ist an die tatsächlichen Feststellungen des angefochtenen Beschlusses gebunden, außer bei "
              "zulässigen und begründeten Rügen gegen diese Feststellungen (§ 107 Abs. 2 PatG). Neue Tatsachen sind kein Rechtsfehler."],
             merke="BGH im Rechtsbeschwerdeverfahren: nur Rechtsfehler, gebunden an die Tatsachen (§ 107 Abs. 2 PatG).", level=2,
             concepts=["pat_rechtsbeschwerde"], norms=["§ 101 Abs. 2 PatG", "§ 107 Abs. 2 PatG"], step=_E + ".4.3", abschnitt="Definitionen und Normen"),
        fall("p05g-7", "Verwerfung des Einspruchs durch das BPatG",
             "Auf Antrag nach § 61 Abs. 2 PatG hat der Beschwerdesenat an Stelle der Patentabteilung über den Einspruch entschieden und ihn als "
             "unzulässig verworfen; er hat die Rechtsbeschwerde zugelassen.",
             "Ist die Rechtsbeschwerde der Einsprechenden statthaft?", True,
             ["**Ja!** Statthaft ist sie gegen Beschlüsse, durch die über die Aufrechterhaltung oder den Widerruf nach § 61 Abs. 2 PatG entschieden "
              "wird (§ 100 Abs. 1 PatG), und zwar auch dann, wenn das anstelle des Patentamts berufene Patentgericht den Einspruch verworfen hat "
              "(BGH Leistungshalbleiterbauelement)."],
             merke="Rechtsbeschwerde auch gegen die Verwerfung des Einspruchs durch das BPatG nach § 61 Abs. 2 PatG.", level=3,
             concepts=["pat_rechtsbeschwerde"], norms=["§ 100 Abs. 1 PatG", "§ 61 Abs. 2 PatG"], cases=["pat_bgh_leistungshalbleiterbauelement"],
             step=_E + ".4.3", abschnitt="Definitionen und Normen"),
        *fallkette("p05g-8", "W aus der Formel F (nach TS I/2023)",
            "Die Patentabteilung widerrief das Patent der A, weil Anspruch 1 den Wirkstoff W nennt, der ursprünglich nur als Teil der allgemeinen "
            "Formel F offenbart war. Der Beschwerdesenat weist die Beschwerde zurück und lässt die Rechtsbeschwerde zu: Grundsätzlich zu klären "
            "sei, ob BGH Winkelmesseinrichtung auf die Auswahl aus einer Formel passt. Der Beschluss wird am Do 15.07.2021 zugestellt.",
            [frage("Ist die Rechtsbeschwerde statthaft?", True,
                   ["**Ja!** Der Beschluss entscheidet über eine Beschwerde nach § 73 PatG, und der Senat hat die Rechtsbeschwerde zugelassen "
                    "(§ 100 Abs. 1 PatG) wegen einer Rechtsfrage von grundsätzlicher Bedeutung (§ 100 Abs. 2 Nr. 1 PatG). A war am "
                    "Beschwerdeverfahren beteiligt (§ 101 Abs. 1 PatG)."],
                   merke="Statthaft: Beschluss über die Beschwerde nach § 73 PatG + Zulassung (§ 100 Abs. 1, 2 PatG).", titel="V1, V2 Statthaftigkeit",
                   norms=["§ 100 Abs. 1 PatG", "§ 101 Abs. 1 PatG"], step=_E + ".4.3"),
             frage("Bis wann und wo muss A die Rechtsbeschwerde einlegen?", 1,
                   ["**Bis Mo 16.08.2021 beim BGH.** Ein Monat nach Zustellung, schriftlich beim BGH (§ 102 Abs. 1 PatG). Die Frist endet am "
                    "So 15.08.2021 (§ 106 Abs. 1 S. 1 PatG i.V.m. § 222 Abs. 1 ZPO, § 188 Abs. 2 BGB) und verschiebt sich auf den nächsten Werktag "
                    "(§ 222 Abs. 2 ZPO)."],
                   optionen=["Bis So 15.08.2021 beim BPatG", "Bis Mo 16.08.2021 beim BGH", "Bis Mo 16.08.2021 beim DPMA", "Bis Fr 15.10.2021 beim BGH"],
                   merke="Rechtsbeschwerde: ein Monat, beim BGH (§ 102 Abs. 1 PatG); Verschiebung § 222 Abs. 2 ZPO.", titel="V4 Frist und Stelle",
                   step=_E + ".4.3"),
             frage("Wann muss die Begründung spätestens eingehen, wenn A am 16.08.2021 einlegt und keine Verlängerung beantragt?", 2,
                   ["**Do 16.09.2021.** Die Begründungsfrist beträgt einen Monat und beginnt mit der Einlegung (§ 102 Abs. 3 S. 2 PatG), nicht mit "
                    "der Zustellung. Sie kann auf Antrag vom Vorsitzenden verlängert werden. Die Begründung muss Antrag und verletzte Rechtsnorm "
                    "enthalten (§ 102 Abs. 4 Nr. 1, 2 PatG)."],
                   optionen=["Mo 16.08.2021", "Mi 15.09.2021", "Do 16.09.2021", "Fr 15.10.2021"],
                   merke="Begründung: ein Monat ab Einlegung (§ 102 Abs. 3 PatG), Inhalt § 102 Abs. 4 PatG.", titel="V5 Begründung", level=2,
                   step=_E + ".4.3"),
             frage("Beruht der Beschluss auf einer Rechtsverletzung, wenn W eine offenbarte Lehre nur konkretisiert?", True,
                   ["**Ja!** Ein nicht offenbartes Merkmal, das eine ursprünglich als zur Erfindung gehörend offenbarte Lehre konkretisiert und "
                    "dessen Streichung den Schutzbereich erweitern würde, bleibt im Anspruch (BGH Winkelmesseinrichtung). Der Widerruf allein "
                    "deswegen verletzt § 21 Abs. 1 Nr. 4 PatG i.V.m. § 21 Abs. 2 PatG; der Beschluss beruht darauf (§ 101 Abs. 2 S. 1 PatG)."],
                   merke="Verkennung von Winkelmesseinrichtung ist Rechtsverletzung (§ 101 Abs. 2 PatG).", titel="V7 Rechtsverletzung", level=3,
                   norms=["§ 101 Abs. 2 PatG", "§ 21 Abs. 1 Nr. 4 PatG"], cases=["pat_bgh_winkelmesseinrichtung"], step=_E + ".4.3"),
             frage("Entscheidet der BGH dann selbst über die erfinderische Tätigkeit?", False,
                   ["**Nein!** Im Fall der Aufhebung ist die Sache zur anderweiten Verhandlung und Entscheidung an das BPatG zurückzuverweisen "
                    "(§ 108 Abs. 1 PatG), das die rechtliche Beurteilung des BGH zugrunde legen muss (§ 108 Abs. 2 PatG). Das BPatG prüft dann § 4 PatG, "
                    "ohne die Auswahl von W zugunsten der A zu berücksichtigen."],
                   merke="Rechtsbeschwerde erfolgreich: Aufhebung und Zurückverweisung mit Bindung (§ 108 PatG).", titel="Rechtsfolge",
                   norms=["§ 108 PatG"], step=_E + ".4.3"),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_rechtsbeschwerde"], norms=["§ 100 Abs. 1 PatG"]),
        *fallkette("p05g-9", "Ohne Zulassung (Abwandlung nach TS I/2023)",
            "Wie zuvor, aber der Beschwerdesenat lässt die Rechtsbeschwerde nicht zu. A meint, der Senat habe BGH Winkelmesseinrichtung verkannt "
            "und sie mit dem Ergebnis überrascht. Die Erweiterung war seit dem Beitritt der E3 Gegenstand des Verfahrens; A hatte sich schriftlich "
            "und in der mündlichen Verhandlung dazu geäußert.",
            [frage("Kann A beim BGH beantragen, die Rechtsbeschwerde zuzulassen?", False,
                   ["**Nein!** Eine Anfechtung der Entscheidungen des Patentgerichts findet nur statt, soweit das PatG sie zulässt "
                    "(§ 99 Abs. 2 PatG). Eine Nichtzulassungsbeschwerde sieht das PatG nicht vor; ohne Zulassung bleibt nur § 100 Abs. 3 PatG."],
                   merke="Keine Nichtzulassungsbeschwerde (§ 99 Abs. 2 PatG).", titel="Nichtzulassungsbeschwerde", norms=["§ 99 Abs. 2 PatG"],
                   step=_E + ".4.3"),
             frage("Eröffnet die Verkennung von BGH Winkelmesseinrichtung die zulassungsfreie Rechtsbeschwerde?", False,
                   ["**Nein!** § 100 Abs. 3 PatG nennt abschließend Verfahrensmängel. Die falsche Anwendung von § 21 Abs. 1 Nr. 4 PatG und § 21 Abs. 2 PatG "
                    "ist ein materieller Fehler und ohne Zulassung nicht angreifbar."],
                   merke="Materieller Fehler ≠ Mangel nach § 100 Abs. 3 PatG.", titel="V2a Materieller Fehler", step=_E + ".4.3"),
             frage("Wurde A das rechtliche Gehör versagt (§ 100 Abs. 3 Nr. 3 PatG)?", False,
                   ["**Nein!** Das Gehör ist versagt, wenn der Beteiligte sich zu einem tragenden Gesichtspunkt nicht äußern konnte oder erheblicher "
                    "Vortrag übergangen wurde. A konnte sich schriftlich und in der Verhandlung zur Erweiterung äußern; Überraschung über das Ergebnis "
                    "genügt nicht (vgl. BGH Schwingungsdämpfer zur Hinweispflicht)."],
                   merke="Gehörsrüge: fehlende Äußerungsmöglichkeit oder übergangener Vortrag, nicht ein unerwartetes Ergebnis.", titel="V2a Nr. 3",
                   level=2, cases=["pat_bgh_schwingungsdaempfer"], concepts=["pat_rechtliches_gehoer"], step=_E + ".4.3"),
             frage("Ist der Beschluss „nicht mit Gründen versehen“, weil seine Begründung falsch ist (§ 100 Abs. 3 Nr. 6 PatG)?", False,
                   ["**Nein!** Nr. 6 erfasst fehlende, nicht fehlerhafte Gründe. Der Beschluss begründet die Entscheidung zu Haupt- und Hilfsantrag; "
                    "dass die Gründe sachlich falsch sind, eröffnet die zulassungsfreie Rechtsbeschwerde nicht. Sie wäre zulässig, wenn ein Mangel "
                    "gerügt wird, aber unbegründet."],
                   merke="Nr. 6: Gründe fehlen; falsche Gründe genügen nicht.", titel="V2a Nr. 6", level=2, step=_E + ".4.3"),
            ],
            abschnitt="Klausurfall", level=2, concepts=["pat_rechtsbeschwerde"], norms=["§ 100 Abs. 3 PatG"]),
    ]),
]
