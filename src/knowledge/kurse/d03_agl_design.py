# -*- coding: utf-8 -*-
"""Kurs d03: Anspruchsgrundlagen Design für die Klausur Rechtspraxis 1 (RP1) der Patentanwaltsprüfung.

Ein Kapitel je Anspruchsgrundlage oder Rechtsbehelf, aufgebaut wie die Klausurlösung: Prüfungsschema (AGL → Voraussetzungen mit Norm
→ Rechtsfolge, Fristen mit Frist · Berechnung · Verschiebung), Definitionen, Drill-Fragen zu Definitionen und Normenketten, Klausurfälle
als Fallketten. Grundlage: die Lösung zu RP1 II/2019 (klausuren/loesungen/rp1/PAP-2019-II-RP1.json) und die Aufgabentexte aller 17
RP1-Klausuren II/2018 bis III/2023. GGV in der konsolidierten Fassung vom 1.7.2026 (data/ggv.json): Nachahmungsschutz des nicht
eingetragenen Musters Art. 19 Abs. 4 GGV, Aufschiebung Art. 19 Abs. 5 GGV, Sanktionen Art. 89 Abs. 1, 2 GGV; Anmeldung nur noch beim
EUIPO (Art. 35 Abs. 1 GGV). VO (EU) Nr. 608/2013, ZPO, BGB, Brüssel-Ia-VO und Rom-II-VO stehen nur im Fließtext, nie in `norms`.
"""
from ._helpers import intro, fall, mc, frage, fallkette

SF = "step:des_schema_schutzfaehigkeit"
VL = "step:des_schema_designverletzung"
NV = "step:des_schema_nichtigkeitsverfahren"
AN = "step:des_schema_anmeldung"
UG = "step:des_schema_unionsgeschmacksmuster"
DN = "Definitionen und Normen"
KF = "Klausurfall"

KAPITEL = [
    # ================================================================== Überblick
    dict(id="d030", titel="Überblick: Anspruchsgrundlagen und Fristen", einheiten=[
        intro("d030-0", "Die Anspruchsgrundlagen im Überblick",
              "RP1 ist eine Designklausur: Fast jede Aufgabe fragt, ob ein **Schutzrecht besteht** (deutsches eingetragenes Design, eingetragenes "
              "oder nicht eingetragenes Unionsgeschmacksmuster), ob es **verletzt** ist, wie man es **angreift** und **wo** man klagt. Zuerst das "
              "Ziel des Mandanten bestimmen, dann die AGL wählen.\n\n"
              "**Schutzrecht wählen**\n"
              "**Deutsches Design** – § 2 Abs. 1 DesignG, § 27 DesignG: Eintragung beim DPMA, 25 Jahre (§ 27 Abs. 2 DesignG), Schutz nur in Deutschland\n"
              "**Eingetragenes Unionsgeschmacksmuster** – Art. 4 Abs. 1 GGV, Art. 12 GGV: Eintragung beim EUIPO, fünf Jahre, verlängerbar bis "
              "25 Jahre (Art. 12 Abs. 2 GGV), Schutz in der ganzen Union\n"
              "**Nicht eingetragenes Unionsgeschmacksmuster** – Art. 11 GGV: entsteht durch Offenbarung in der Union, drei Jahre, nur gegen "
              "Nachahmung (Art. 19 Abs. 4 GGV)\n\n"
              "**Ziel des Mandanten → AGL**\n"
              "**Unterlassung, Beseitigung** – § 42 Abs. 1 DesignG i.V.m. § 38 Abs. 1 S. 1 DesignG; Unionsmuster Art. 19 Abs. 1 GGV i.V.m. "
              "Art. 89 Abs. 1 GGV\n"
              "**Schadensersatz** – § 42 Abs. 2 DesignG; Unionsmuster Art. 89 Abs. 2 GGV, Art. 88 Abs. 2 GGV, Art. 8 Abs. 2 Rom-II-VO i.V.m. "
              "§ 62a Nr. 1 DesignG, § 42 Abs. 2 DesignG\n"
              "**Vernichtung, Rückruf, Auskunft** – § 43 DesignG, § 46 DesignG (Unionsmuster über § 62a Nr. 1 DesignG)\n"
              "**Fremdes Design beseitigen** – Antrag beim DPMA § 34a DesignG i.V.m. § 33 DesignG, § 34 DesignG oder Widerklage § 52b DesignG; "
              "Unionsmuster Art. 24 Abs. 1 GGV, Art. 25 GGV, Art. 52 GGV (EUIPO) oder Widerklage Art. 81 lit. d GGV; nicht eingetragenes "
              "Muster nur vor Gericht (Art. 24 Abs. 3 GGV, Art. 81 lit. c GGV)\n"
              "**Schnell verbieten (Messe)** – einstweilige Verfügung § 935 ZPO, § 940 ZPO i.V.m. § 42 Abs. 1 DesignG bzw. Art. 90 Abs. 1 GGV\n"
              "**Ware an der Grenze stoppen** – Antrag auf Tätigwerden nach der VO (EU) Nr. 608/2013 i.V.m. § 57a DesignG; national § 55 DesignG\n"
              "**Als Lizenznehmer klagen** – § 31 Abs. 3 DesignG, Art. 32 Abs. 3 GGV; Beitritt § 31 Abs. 4 DesignG, Art. 32 Abs. 4 GGV\n"
              "**Design anmelden** – § 11 DesignG, § 16 DesignG, § 19 DesignG; Unionsmuster Art. 35 GGV, Art. 36 GGV, Art. 38 GGV\n"
              "**Abwehr** – Schranken § 40 DesignG, Reparaturklausel § 40a DesignG, Vorbenutzung § 41 DesignG, Erschöpfung § 48 DesignG, "
              "Verjährung § 49 DesignG; Nichtigkeit nur über Widerklage oder Antrag (§ 52a DesignG, Art. 85 Abs. 1 GGV)\n\n"
              "**Klausurfallen:** Die GGV wurde 2024 reformiert (geltend seit 1.5.2025, konsolidiert 1.7.2026): Der Nachahmungsschutz des nicht "
              "eingetragenen Musters steht jetzt in Art. 19 Abs. 4 GGV (früher Abs. 2), die Aufschiebung in Art. 19 Abs. 5 GGV (früher Abs. 3), "
              "Art. 89 GGV hat keine Buchstaben mehr. Ältere Klausurlösungen zitieren die alte Nummerierung.\n\n"
              "**In den Klausuren:** Verletzung und Abwehr in fast allen RP1-Klausuren; Nichtigkeit beim EUIPO in I/2021, II/2022, III/2022; "
              "Zuständigkeit in II/2018, II/2020, II/2021, III/2022, II/2023; Messe und Zoll in II/2019; Lizenz in II/2021.",
              concepts=["des_anspruchsgrundlagen_eu", "des_ggm_eingetragen", "des_ggm_nicht_eingetragen", "des_unterlassung"],
              norms=["§ 42 DesignG", "§ 38 DesignG", "Art. 19 GGV", "Art. 89 GGV", "§ 62a DesignG", "§ 33 DesignG", "Art. 25 GGV"],
              distinctions=["d_des_anspruchsgrundlagen_eu"], abschnitt="Normenkette"),
        intro("d030-1", "Fristen und Gebühren",
              "Jede Frist mit drei Normen: **Frist · Berechnung · Verschiebung**. Vor dem DPMA gelten § 187 Abs. 1 BGB, § 188 Abs. 2 BGB und "
              "§ 193 BGB; vor Gericht § 222 Abs. 1 ZPO (Verweis auf das BGB) und § 222 Abs. 2 ZPO; Gebühren: Fälligkeit § 3 Abs. 1 PatKostG, "
              "Zahlungsfrist § 6 Abs. 1 PatKostG, Folge § 6 Abs. 2 PatKostG, Zahlungstag § 2 PatKostZV.\n\n"
              "**Neuheitsschonfrist** – zwölf Monate vor dem Anmeldetag (§ 6 S. 1 DesignG; Art. 7 Abs. 2 lit. b GGV) · Rückrechnung entsprechend "
              "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB · keine Verschiebung (Rückwärtsfrist ohne Handlungspflicht) · keine Gebühr\n"
              "**Priorität** – sechs Monate (Art. 4 C PVÜ, § 14 DesignG; Art. 41 Abs. 1 GGV); Ausstellungspriorität sechs Monate ab "
              "Zurschaustellung (§ 15 Abs. 1 DesignG); Angaben bis zum 16. Monat (§ 14 Abs. 1 S. 1 DesignG)\n"
              "**Anmeldegebühr DPMA** – fällig mit Einreichung (§ 3 Abs. 1 PatKostG) · drei Monate (§ 6 Abs. 1 S. 2 PatKostG) · § 193 BGB · "
              "sonst gilt die Anmeldung als zurückgenommen (§ 6 Abs. 2 PatKostG); 60 EUR elektronisch, 70 EUR Papier (Nr. 341 000, 341 100 "
              "Anlage PatKostG)\n"
              "**Anmeldegebühr EUIPO** – binnen eines Monats nach Einreichung, sonst kein Anmeldetag (Art. 38 GGV)\n"
              "**Aufschiebung der Bekanntmachung** – 30 Monate ab Anmeldetag (§ 21 Abs. 1 S. 1 DesignG; bis zu 30 Monate Art. 50 Abs. 1 GGV); "
              "Erstreckungsgebühr 40 EUR innerhalb der Aufschiebungsfrist (§ 21 Abs. 2 DesignG, § 7 Abs. 2 PatKostG, Nr. 341 600), sonst endet "
              "der Schutz (§ 21 Abs. 4 DesignG)\n"
              "**Schutzdauer** – 25 Jahre ab Anmeldetag (§ 27 Abs. 2 DesignG); Aufrechterhaltung ab dem 6. Jahr (§ 28 Abs. 1 DesignG), fällig am "
              "Monatsletzten (§ 3 Abs. 2 PatKostG), zahlbar bis Ablauf des zweiten Monats, mit Zuschlag bis Ablauf des sechsten Monats (§ 7 Abs. 1 "
              "PatKostG); Unionsmuster fünf Jahre je Periode (Art. 12 Abs. 2 GGV), Erneuerung binnen sechs Monaten vor Ablauf, Nachfrist sechs "
              "Monate mit Zuschlag (Art. 50d Abs. 3 GGV); nicht eingetragenes Muster drei Jahre ab erster Offenbarung in der Union (Art. 11 Abs. 1 GGV)\n"
              "**Nichtigkeitsantrag DPMA** – keine Antragsfrist, auch nach Erlöschen (§ 33 Abs. 5 DesignG); Gebühr 300 EUR je Design "
              "(Nr. 346 100), fällig mit Antrag (§ 3 Abs. 1 PatKostG), drei Monate (§ 6 Abs. 1 S. 2 PatKostG), sonst Rücknahmefiktion (§ 6 Abs. 2 PatKostG)\n"
              "**Widerspruch des Designinhabers** – ein Monat ab Zustellung (§ 34a Abs. 2 S. 1 DesignG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · "
              "§ 193 BGB · ohne Widerspruch wird die Nichtigkeit festgestellt oder erklärt (§ 34a Abs. 2 S. 2 DesignG)\n"
              "**Beitritt zum Nichtigkeitsverfahren** – drei Monate ab Klage oder Abmahnung (§ 34c Abs. 1 S. 2 DesignG)\n"
              "**Beschwerde zum BPatG** – ein Monat ab Zustellung (§ 23 Abs. 4 S. 4 DesignG i.V.m. § 73 Abs. 2 S. 1 PatG) · § 187 Abs. 1 BGB, "
              "§ 188 Abs. 2 BGB · § 193 BGB; Gebühr innerhalb der Frist (§ 6 Abs. 1 S. 1 PatKostG): 500 EUR im Nichtigkeitsverfahren "
              "(Nr. 401 100), sonst 200 EUR (Nr. 401 300)\n"
              "**Weiterbehandlung** – ein Monat ab Zustellung der Zurückweisung (§ 17 Abs. 2 DesignG), 100 EUR (Nr. 346 000)\n"
              "**Vindikation** – Ausschlussfrist drei Jahre ab Bekanntmachung (§ 9 Abs. 2 DesignG; Art. 15 Abs. 3 GGV), nicht bei Bösgläubigkeit\n"
              "**Verjährung** – drei Jahre ab Schluss des Jahres der Kenntnis (§ 49 S. 1 DesignG i.V.m. § 195 BGB, § 199 Abs. 1 BGB)\n"
              "**Vollziehung der einstweiligen Verfügung** – ein Monat (§ 929 Abs. 2 ZPO i.V.m. § 936 ZPO) · § 222 Abs. 1 ZPO i.V.m. "
              "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 222 Abs. 2 ZPO\n"
              "**Zoll** – Entscheidung über den Antrag binnen 30 Arbeitstagen, Bestätigung der Verletzung und Zustimmung zur Vernichtung binnen "
              "zehn Arbeitstagen (Art. 23 Abs. 1 VO (EU) Nr. 608/2013); national Widerspruch zwei Wochen (§ 56 Abs. 1 DesignG), gerichtliche "
              "Entscheidung binnen zwei Wochen (§ 56 Abs. 4 DesignG)\n\n"
              "**In den Klausuren:** Schonfrist in II/2019 (Rückrechnung ab Sa 17.02.2018), I/2020, I/2021, I/2023, II/2023, III/2023; Aufschiebung in "
              "I/2019 und III/2021; Erneuerung in I/2020 (nicht verlängertes Unionsmuster).",
              concepts=["des_neuheitsschonfrist", "des_aufschiebung", "des_schutzdauer", "des_nichtigkeitsverfahren_dpma", "des_verjaehrung"],
              norms=["§ 6 DesignG", "§ 21 DesignG", "§ 27 DesignG", "§ 28 DesignG", "§ 34a DesignG", "§ 23 DesignG", "§ 49 DesignG",
                     "Art. 7 GGV", "Art. 11 GGV", "Art. 12 GGV", "Art. 50 GGV", "§ 6 PatKostG"],
              abschnitt="Normenkette"),
        mc("d030-2", "Unionsweites Verbot",
           "Welche AGL trägt das Ziel, einem Wettbewerber den Vertrieb in der ganzen Union zu verbieten?",
           ["Art. 19 Abs. 1 GGV i.V.m. Art. 89 Abs. 1 GGV aus einem Unionsgeschmacksmuster",
            "§ 42 Abs. 1 DesignG aus dem deutschen Design, weil das Urteil in der Union vollstreckbar ist",
            "Art. 89 Abs. 1 GGV aus dem deutschen Design über § 62a DesignG",
            "§ 42 Abs. 1 DesignG i.V.m. Art. 7 Nr. 2 Brüssel-Ia-VO"], 0,
           ["**Art. 19 Abs. 1 GGV i.V.m. Art. 89 Abs. 1 GGV.** Nur das Unionsgeschmacksmuster wirkt einheitlich in der Union (Art. 1 Abs. 3 GGV). "
            "Das deutsche Design schützt nur in Deutschland; ein Verbot daraus reicht nicht weiter, gleich wo vollstreckt wird. Ein unionsweites "
            "Verbot spricht nur ein Gericht aus, das nach Art. 82 Abs. 1 bis 4 GGV zuständig ist (Art. 83 Abs. 1 GGV)."],
           sachverhalt="", merke="Unionsweit nur aus dem Unionsmuster: Art. 19 Abs. 1, Art. 89 Abs. 1 GGV · Reichweite Art. 83 Abs. 1 GGV.",
           level=1, concepts=["des_ggm_eingetragen", "des_unterlassung"], norms=["Art. 19 GGV", "Art. 89 GGV", "Art. 83 GGV"], step=f"{UG}.3",
           abschnitt="Ziel des Mandanten"),
        mc("d030-3", "Jüngeres Design beseitigen",
           "Die Mandantin will ein jüngeres deutsches Design eines Wettbewerbers aus dem Register bringen. Welcher Weg ist der Regelweg?",
           ["Antrag beim DPMA nach § 34a DesignG i.V.m. § 33 DesignG", "Löschungsklage beim Landgericht nach § 52 DesignG",
            "Einspruch beim DPMA binnen drei Monaten nach Bekanntmachung", "Antrag auf Nichtigerklärung beim EUIPO"], 0,
           ["**Antrag beim DPMA.** Seit 2014 stellt die Designabteilung des DPMA die Nichtigkeit fest oder erklärt sie (§ 33 Abs. 3 DesignG, "
            "§ 34a Abs. 1 DesignG, § 23 Abs. 2 DesignG). Die Landgerichte sind dafür nicht zuständig (§ 52 Abs. 1 DesignG), außer auf Widerklage "
            "im Verletzungsprozess (§ 52b DesignG). Einen Einspruch kennt das DesignG nicht; das EUIPO entscheidet nur über Unionsmuster."],
           sachverhalt="", merke="Nichtigkeit DE-Design: Antrag DPMA § 34a DesignG oder Widerklage § 52b DesignG; kein Einspruch.",
           level=1, concepts=["des_nichtigkeitsverfahren_dpma", "des_widerklage_nichtigkeit"], norms=["§ 34a DesignG", "§ 33 DesignG", "§ 52b DesignG"],
           step=f"{NV}.1", abschnitt="Ziel des Mandanten"),
        mc("d030-4", "Ware aus China vor der Messe",
           "Plagiate sollen aus China zur Messe nach Frankfurt eingeführt werden; die Hersteller sind unbekannt. Was hilft am schnellsten und günstigsten?",
           ["Antrag auf Tätigwerden der Zollbehörden nach der VO (EU) Nr. 608/2013", "Verletzungsklage beim Landgericht Frankfurt",
            "Nationale Beschlagnahme nach § 55 DesignG gegen Sicherheitsleistung", "Strafanzeige nach § 65 DesignG"], 0,
           ["**Antrag nach der VO (EU) Nr. 608/2013.** Der Zoll setzt die Überlassung schon bei Verdacht aus und nennt Absender und Empfänger; "
            "unbekannte Gegner sind kein Hindernis, Gebühren und Sicherheit fallen nicht an. § 55 Abs. 1 S. 1 DesignG gilt nur, soweit die "
            "Verordnung nicht anwendbar ist, und verlangt offensichtliche Verletzung und Sicherheitsleistung (Lösung RP1 II/2019)."],
           sachverhalt="", merke="Drittlandsware: VO (EU) Nr. 608/2013 i.V.m. § 57a DesignG; § 55 DesignG nur subsidiär.",
           level=2, concepts=["des_zollbeschlagnahme"], norms=["§ 55 DesignG", "§ 57a DesignG"], abschnitt="Ziel des Mandanten"),
        mc("d030-5", "Abmahnung erhalten",
           "Der Mandant erhält eine Abmahnung aus einem Unionsgeschmacksmuster und soll die Anwaltskosten des Gegners zahlen. Worauf stützt "
           "sich der Erstattungsanspruch, wenn die Abmahnung berechtigt ist?",
           ["Geschäftsführung ohne Auftrag (§ 677 BGB, § 683 S. 1 BGB, § 670 BGB) oder Schadensersatz", "§ 97a Abs. 3 UrhG analog",
            "§ 52 Abs. 4 DesignG unmittelbar", "Art. 89 Abs. 1 GGV"], 0,
           ["**Geschäftsführung ohne Auftrag.** Das DesignG regelt die Abmahnung nicht. Die berechtigte Abmahnung liegt im Interesse des "
            "Verletzers, weil sie ihm den teureren Prozess erspart; die Kosten sind daher nach § 677 BGB, § 683 S. 1 BGB, § 670 BGB zu ersetzen, "
            "bei Verschulden auch als Schaden. § 52 Abs. 4 DesignG betrifft Patentanwaltskosten im Prozess (RP1 III/2021, III/2022)."],
           sachverhalt="", merke="Abmahnkosten: § 677, § 683 S. 1, § 670 BGB; Unterlassungserklärung mit Vertragsstrafe beseitigt die Wiederholungsgefahr.",
           level=2, concepts=["des_unterlassung"], norms=["§ 42 DesignG"], abschnitt="Ziel des Mandanten"),
        mc("d030-6", "Lizenznehmer will klagen",
           "Die Mandantin hat eine einfache Lizenz an einem deutschen Design. Ein Wettbewerber verletzt es. Welche Norm entscheidet, ob sie selbst klagen darf?",
           ["§ 31 Abs. 3 DesignG: nur mit Zustimmung des Rechtsinhabers", "§ 42 Abs. 1 DesignG: jeder Verletzte darf klagen",
            "§ 31 Abs. 4 DesignG: nur als Streitgenosse des Inhabers", "§ 8 DesignG: nur der eingetragene Inhaber"], 0,
           ["**§ 31 Abs. 3 DesignG.** Der Lizenznehmer kann ein Verletzungsverfahren nur mit Zustimmung des Rechtsinhabers anhängig machen "
            "(S. 1); ohne Zustimmung nur der ausschließliche Lizenznehmer nach erfolgloser Aufforderung (S. 2). § 31 Abs. 4 DesignG erlaubt "
            "zusätzlich den Beitritt zur Klage des Inhabers. Für das Unionsmuster gilt Art. 32 Abs. 3, 4 GGV (RP1 II/2021)."],
           sachverhalt="", merke="Lizenznehmer: Klage § 31 Abs. 3 DesignG, Art. 32 Abs. 3 GGV · Beitritt § 31 Abs. 4 DesignG, Art. 32 Abs. 4 GGV.",
           level=1, concepts=["des_lizenz"], norms=["§ 31 DesignG", "Art. 32 GGV"], abschnitt="Ziel des Mandanten"),
        *fallkette("d030-7", "Pistole im Fachartikel (nach RP1 I/2023)",
            "Die österreichische Klingel GmbH hat ihre neue Pistole bisher nur in einer unveröffentlichten PCT-Anmeldung gezeigt. Letzte Woche "
            "stellte ein Fachartikel die fast gleich aussehende Pistole der Policepart KG vor, unabhängig entwickelt. Klingel will in zwei "
            "Monaten selbst ausstellen und fragt nach Designschutz.",
            [frage("Hat Klingel schon ein nicht eingetragenes Unionsgeschmacksmuster?", False,
                   ["**Nein!** Es entsteht erst, wenn das Muster in der Union so offenbart wird, dass die Fachkreise es kennen konnten "
                    "(Art. 11 Abs. 1, 2 GGV). Die PCT-Anmeldung ist noch nicht veröffentlicht; sie ist keine Offenbarung."],
                   merke="Nicht eingetragenes Muster: erste Offenbarung in der Union, Art. 11 GGV.", titel="Nicht eingetragenes Muster",
                   norms=["Art. 11 GGV"], concepts=["des_ggm_nicht_eingetragen"]),
             frage("Hilft die Neuheitsschonfrist gegen den Fachartikel der Policepart KG?", False,
                   ["**Nein!** § 6 DesignG und Art. 7 Abs. 2 GGV nehmen nur Offenbarungen des Entwerfers, seines Rechtsnachfolgers oder Dritter "
                    "als Folge ihrer Informationen aus. Policepart hat unabhängig entworfen; der Artikel gehört zum Formenschatz, der neuen "
                    "Anmeldungen von Klingel entgegensteht."],
                   merke="Schonfrist schützt nur vor eigenen Offenbarungen, nicht vor Parallelentwicklungen.", titel="Schonfrist",
                   norms=["§ 6 DesignG", "Art. 7 GGV"], concepts=["des_neuheitsschonfrist"]),
             frage("Klingel will die ganze Union abdecken. Welches Schutzrecht passt?", 1,
                   ["**Eingetragenes Unionsgeschmacksmuster.** Es wirkt einheitlich in der Union (Art. 1 Abs. 3 GGV) und schützt auch gegen "
                    "unabhängige Gestaltungen (Art. 19 Abs. 1 GGV). Das deutsche Design kann daneben treten, schützt aber nur in Deutschland; das "
                    "nicht eingetragene Muster schützt nur gegen Nachahmung."],
                   optionen=["Nur ein deutsches Design", "Eingetragenes Unionsgeschmacksmuster, gegebenenfalls zusätzlich deutsches Design",
                             "Nur das nicht eingetragene Unionsgeschmacksmuster nach der Ausstellung", "Ein Gebrauchsmuster"],
                   merke="Wahl: eingetragenes Unionsmuster für die Union, DE-Design als zweites Standbein.", titel="Wahl des Schutzrechts",
                   norms=["Art. 19 GGV"], concepts=["des_ggm_eingetragen", "des_abgrenzung_schutzrechte"]),
            ],
            abschnitt=KF, level=2, step=f"{AN}.8"),
    ]),
    # ================================================================== Schutzvoraussetzungen
    dict(id="d03a", titel="§§ 1 bis 6 DesignG, Art. 3 bis 11 GGV: Schutzvoraussetzungen", einheiten=[
        intro("d03a-0", "Prüfungsschema",
              "**AGL (Vorfrage jeder AGL):** Rechtsgültigkeit des Schutzrechts – § 2 Abs. 1 DesignG (eingetragenes Design), Art. 4 Abs. 1 GGV "
              "(Unionsgeschmacksmuster), Art. 11 Abs. 1 GGV (nicht eingetragenes Muster)\n\n"
              "**A · Schutzgegenstand**\n"
              "**V1 Design** – § 1 Nr. 1 DesignG, Art. 3 Nr. 1 GGV: Erscheinungsform eines Erzeugnisses (§ 1 Nr. 2 DesignG) oder eines Teils, "
              "nicht Idee, Verfahren oder Funktion\n"
              "**V2 Ein bestimmter Schutzgegenstand** – § 37 Abs. 1 DesignG, Art. 18a GGV: die sichtbar wiedergegebenen Merkmale; zeigt ein "
              "Einzeldesign mehrere Ausführungsformen, fehlt „ein“ Design (BGH Sporthelm)\n"
              "**V3 Kein Ausschluss** – § 3 Abs. 1 Nr. 1, 2 DesignG, Art. 8 Abs. 1, 2 GGV: nicht ausschließlich technisch bedingt, keine "
              "Verbindungselemente (Rückausnahme modulare Systeme § 3 Abs. 2 DesignG, Art. 8 Abs. 3 GGV); § 3 Abs. 1 Nr. 3, 4 DesignG, Art. 9 GGV\n\n"
              "**B · Stichtag und Formenschatz**\n"
              "**V4 Stichtag** – Anmeldetag § 13 Abs. 1 DesignG bzw. Prioritätstag § 13 Abs. 2 DesignG; Art. 5 Abs. 1 lit. b GGV, Art. 38 GGV; "
              "beim nicht eingetragenen Muster der Tag der ersten Offenbarung (Art. 5 Abs. 1 lit. a GGV)\n"
              "**V5 Keine schädliche Offenbarung** – § 5 S. 1 DesignG, Art. 7 Abs. 1 GGV: bekannt gemacht, ausgestellt, im Verkehr verwendet; "
              "unschädlich, wenn die Fachkreise der Union es nicht kennen konnten oder bei Vertraulichkeit (§ 5 S. 2 DesignG)\n"
              "**V6 Neuheitsschonfrist** – § 6 DesignG, Art. 7 Abs. 2, 3 GGV: eigene Offenbarung in den zwölf Monaten vor dem Stichtag bleibt "
              "unberücksichtigt · Rückrechnung entsprechend § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · keine Verschiebung\n\n"
              "**C · Neuheit und Eigenart**\n"
              "**V7 Neuheit** – § 2 Abs. 2 DesignG, Art. 5 GGV: kein identisches älteres Design\n"
              "**V8 Eigenart** – § 2 Abs. 3 DesignG, Art. 6 GGV: anderer Gesamteindruck beim informierten Benutzer, Gestaltungsfreiheit; "
              "Einzelvergleich (EuGH Karen Millen)\n"
              "**V9 Bauelement sichtbar** – § 4 DesignG, Art. 4 Abs. 2, 3 GGV: eingebaut bei bestimmungsgemäßer Verwendung sichtbar, nur "
              "sichtbare Merkmale zählen\n\n"
              "**D · Nicht eingetragenes Unionsgeschmacksmuster**\n"
              "**V10 Entstehung** – Art. 11 Abs. 1, 2 GGV: erste Offenbarung in der Union, den Fachkreisen bekannt; Inhaber nach Art. 14 GGV "
              "(Entwerfer, Rechtsnachfolger, Arbeitgeber)\n\n"
              "**⇒ Rechtsfolge:** Schutz 25 Jahre (§ 27 Abs. 2 DesignG), fünf Jahre je Periode bis 25 Jahre (Art. 12 Abs. 2 GGV) oder drei "
              "Jahre (Art. 11 Abs. 1 GGV); fehlt eine Voraussetzung, ist das Recht nichtig (§ 33 Abs. 1 DesignG, Art. 25 Abs. 1 lit. a, b GGV)\n\n"
              "**Klausurfallen:** Das DPMA prüft Neuheit und Eigenart nicht (§ 16 DesignG, § 18 DesignG); deshalb die Vermutung des § 39 DesignG. "
              "Offenbarung außerhalb der Union: Formenschatz ja, wenn die Fachkreise der Union sie kennen konnten (EuGH Gautzsch), Entstehung "
              "eines nicht eingetragenen Musters nein (BGH Gebäckpresse). Die Schonfrist hilft nicht gegen Parallelentwicklungen. Gestrichelte "
              "Linien zeigen nach der Praxis von DPMA und EUIPO nicht beanspruchte Teile.\n\n"
              "**In den Klausuren:** II/2019 (Präsentation in der Schonfrist), II/2018 (Kanaldeckel, Gießkanne, Gebrauchsmuster als Formenschatz), "
              "III/2019 (Helm mit sechs Ansichten), I/2020 (Messe Dubai), II/2020 (gestrichelte Linien, Verbindungselement), III/2020 (Messe Shanghai, "
              "Priorität), I/2021 (Nudel), I/2022 (Griffrohr), I/2023 (Fachartikel), II/2023 (Peking, Arbeitnehmer).",
              concepts=["des_design_begriff", "des_neuheit", "des_eigenart", "des_offenbarung", "des_neuheitsschonfrist", "des_ggm_nicht_eingetragen"],
              norms=["§ 1 DesignG", "§ 2 DesignG", "§ 3 DesignG", "§ 4 DesignG", "§ 5 DesignG", "§ 6 DesignG", "§ 37 DesignG",
                     "Art. 3 GGV", "Art. 4 GGV", "Art. 5 GGV", "Art. 6 GGV", "Art. 7 GGV", "Art. 8 GGV", "Art. 11 GGV"],
              abschnitt="Normenkette"),
        intro("d03a-1", "Definitionen",
              "**Design:** zwei- oder dreidimensionale Erscheinungsform eines ganzen Erzeugnisses oder eines Teils davon, die sich insbesondere "
              "aus Linien, Konturen, Farben, Gestalt, Oberflächenstruktur oder Werkstoffen ergibt (Legaldefinition § 1 Nr. 1 DesignG; Art. 3 Nr. 1 "
              "GGV, dort auch Bewegung und Animation)\n"
              "**Erzeugnis:** jeder industrielle oder handwerkliche Gegenstand einschließlich Verpackung, Ausstattung, grafischer Symbole, "
              "typografischer Schriftzeichen und Einzelteile; kein Computerprogramm (Legaldefinition § 1 Nr. 2 DesignG; Art. 3 Nr. 2 GGV)\n"
              "**Komplexes Erzeugnis:** Erzeugnis aus mehreren ersetzbaren Bauelementen, das sich auseinander- und wieder zusammenbauen lässt "
              "(Legaldefinition § 1 Nr. 3 DesignG; Art. 3 Nr. 3 GGV)\n"
              "**Bestimmungsgemäße Verwendung:** Verwendung durch den Endbenutzer ohne Instandhaltung, Wartung und Reparatur (Legaldefinition "
              "§ 1 Nr. 4 DesignG; Art. 4 Abs. 3 GGV); sichtbar aus Sicht des Endbenutzers und eines außenstehenden Beobachters (EuGH Monz)\n"
              "**Neuheit:** vor dem Anmeldetag kein identisches Design offenbart; identisch, wenn sich die Merkmale nur in unwesentlichen "
              "Einzelheiten unterscheiden (Legaldefinition § 2 Abs. 2 DesignG; Art. 5 GGV)\n"
              "**Eigenart:** der Gesamteindruck beim informierten Benutzer unterscheidet sich von dem jedes vor dem Anmeldetag offenbarten Designs; "
              "der Grad der Gestaltungsfreiheit ist zu berücksichtigen (Legaldefinition § 2 Abs. 3 DesignG; Art. 6 GGV)\n"
              "**Informierter Benutzer:** kennt verschiedene Designs des Sektors und die üblichen Gestaltungselemente, benutzt die Erzeugnisse "
              "mit vergleichsweise großer Aufmerksamkeit und vergleicht möglichst direkt; zwischen Durchschnittsverbraucher und Fachmann "
              "(EuGH PepsiCo)\n"
              "**Gestaltungsfreiheit:** Spielraum des Entwerfers nach technischen und rechtlichen Vorgaben und der Musterdichte; je größer, desto "
              "mehr Abstand ist für Eigenart nötig (BGH Untersetzer)\n"
              "**Offenbarung:** bekannt gemacht, ausgestellt, im Verkehr verwendet oder sonst der Öffentlichkeit zugänglich gemacht, es sei denn, "
              "die in der Union tätigen Fachkreise des Sektors konnten es im normalen Geschäftsverlauf nicht kennen; nicht bei Vertraulichkeit "
              "(Legaldefinition § 5 DesignG; Art. 7 Abs. 1 GGV)\n"
              "**Neuheitsschonfrist:** Offenbarung durch den Entwerfer, seinen Rechtsnachfolger oder Dritte als Folge ihrer Informationen oder "
              "durch Missbrauch in den zwölf Monaten vor dem Anmeldetag bleibt unberücksichtigt (§ 6 DesignG; Art. 7 Abs. 2, 3 GGV)\n"
              "**Ausschließlich technisch bedingt:** die technische Funktion war der einzige Faktor für das Merkmal, ästhetische Erwägungen "
              "spielten keine Rolle; objektiv nach allen Umständen (EuGH DOCERAM)\n"
              "**Nachahmung:** angegriffene Gestaltung beruht auf Kenntnis des Musters; keine Nachahmung bei unabhängiger Gestaltung eines "
              "Entwerfers, der das Muster berechtigterweise nicht kannte (Art. 19 Abs. 4 GGV)",
              concepts=["des_design_begriff", "des_erzeugnis", "des_informierter_benutzer", "des_gestaltungsfreiheit", "des_technisch_bedingt",
                        "des_bauelement_sichtbarkeit"],
              cases=["des_eugh_pepsico", "des_eugh_doceram", "des_eugh_monz", "des_bgh_untersetzer"], abschnitt="Definitionen"),
        mc("d03a-2", "Eigenart", "Wann hat ein Design Eigenart?",
           ["Wenn sein Gesamteindruck beim informierten Benutzer sich vom Gesamteindruck jedes einzelnen älteren Designs unterscheidet",
            "Wenn es die Durchschnittsgestaltung deutlich überragt (Gestaltungshöhe)",
            "Wenn es sich von einer Kombination der Merkmale mehrerer älterer Designs unterscheidet",
            "Wenn sich seine Merkmale in mehr als unwesentlichen Einzelheiten unterscheiden"], 0,
           ["**Anderer Gesamteindruck im Einzelvergleich** (§ 2 Abs. 3 DesignG, Art. 6 GGV). Gestaltungshöhe verlangt das neue Recht nicht "
            "(BGH Verlängerte Limousinen). Eine Merkmalscollage aus mehreren Entgegenhaltungen ist unzulässig (EuGH Karen Millen). Die "
            "„unwesentlichen Einzelheiten“ sind der Maßstab der Neuheit (§ 2 Abs. 2 S. 2 DesignG)."],
           merke="Eigenart § 2 Abs. 3 DesignG: Gesamteindruck · informierter Benutzer · Gestaltungsfreiheit · Einzelvergleich.",
           level=1, concepts=["des_eigenart", "des_gesamteindruck"], norms=["§ 2 Abs. 3 DesignG", "Art. 6 GGV"],
           cases=["des_eugh_karen_millen", "des_bgh_verlaengerte_limousinen"], step=f"{SF}.6", abschnitt=DN),
        mc("d03a-3", "Schonfrist beim Unionsmuster", "Wo steht die Neuheitsschonfrist für das eingetragene Unionsgeschmacksmuster, und wie lang ist sie?",
           ["Art. 7 Abs. 2 GGV, zwölf Monate vor dem Anmelde- oder Prioritätstag", "Art. 11 Abs. 1 GGV, drei Jahre ab Offenbarung",
            "Art. 41 Abs. 1 GGV, sechs Monate ab Erstanmeldung", "§ 6 DesignG, sechs Monate vor dem Anmeldetag"], 0,
           ["**Art. 7 Abs. 2 GGV.** Die Offenbarung durch den Entwerfer, seinen Rechtsnachfolger oder Dritte als Folge ihrer Informationen "
            "bleibt unberücksichtigt, wenn sie in den zwölf Monaten vor dem Anmeldetag oder Prioritätstag liegt (lit. b). Missbrauch erfasst "
            "Art. 7 Abs. 3 GGV. Für das deutsche Design gilt dasselbe nach § 6 DesignG, ebenfalls zwölf Monate. Sechs Monate ist die Prioritätsfrist."],
           merke="Schonfrist zwölf Monate: § 6 S. 1 DesignG, Art. 7 Abs. 2 lit. b GGV · Priorität sechs Monate: Art. 41 Abs. 1 GGV.",
           level=1, concepts=["des_neuheitsschonfrist"], norms=["Art. 7 GGV", "§ 6 DesignG"], step=f"{SF}.4", abschnitt=DN),
        fall("d03a-4", "Messe in Dubai als Formenschatz",
             "Die Design Pro GmbH zeigte Scheren auf der führenden internationalen Fachmesse der Branche in Dubai im Dezember 2018. Die Pfiff GmbH, "
             "deren Geschäftsführer die Messe besuchte, meldete ein fast gleiches Unionsmuster im Februar 2019 an.",
             "Gehören die in Dubai gezeigten Scheren zum Formenschatz gegen das Unionsmuster der Pfiff GmbH?", True,
             ["**Ja!** Auch eine Offenbarung außerhalb der Union zählt, wenn die in der Union tätigen Fachkreise sie im normalen Geschäftsverlauf "
              "kennen konnten (Art. 7 Abs. 1 GGV; EuGH Gautzsch). Bei der einschlägigen internationalen Fachmesse mit europäischen Besuchern liegt "
              "das nahe; Beweis über Messeberichte und Besucher. Pfiff kann sich nicht auf die Schonfrist berufen, weil sie nicht Entwerferin ist."],
             merke="Formenschatz: weltweite Offenbarung genügt, wenn die Fachkreise der Union sie kennen konnten (Art. 7 Abs. 1 GGV).",
             level=2, concepts=["des_offenbarung", "des_formenschatz"], norms=["Art. 7 GGV", "§ 5 DesignG"], cases=["des_eugh_gautzsch"],
             step=f"{SF}.4", abschnitt=DN),
        fall("d03a-5", "Messe in Dubai als Entstehungsgrund",
             "Die Design Pro GmbH zeigte ihre Scheren „Angel“ erstmals im Dezember 2018 auf einer Fachmesse in Dubai. In der Union wurden sie erst ab "
             "Juni 2019 vertrieben.",
             "Ist mit der Messe in Dubai ein nicht eingetragenes Unionsgeschmacksmuster entstanden?", False,
             ["**Nein!** Das nicht eingetragene Muster entsteht nur durch Offenbarung „innerhalb der Union“ (Art. 11 Abs. 1, 2 GGV). Eine "
              "Offenbarung außerhalb der Union genügt nicht, auch wenn die Fachkreise sie kennen konnten (BGH Gebäckpresse). Schutz entsteht erst "
              "mit dem Vertrieb in der Union im Juni 2019; die Messe bleibt aber Formenschatz gegen spätere Anmeldungen Dritter."],
             merke="Art. 11 GGV: Entstehung nur durch Offenbarung in der Union; Art. 7 GGV: Formenschatz weltweit.",
             level=2, concepts=["des_ggm_nicht_eingetragen", "des_offenbarung"], norms=["Art. 11 GGV", "Art. 7 GGV"], cases=["des_bgh_gebaeckpresse"],
             step=f"{UG}.1", abschnitt=DN),
        fall("d03a-6", "Mehrheit der Formen",
             "Ein Tankeinsatz könnte bei den Bohrungen und Schrauben auch anders gestaltet werden, ohne die Funktion zu beeinträchtigen. Der "
             "Verletzer meint, alle Merkmale seien technisch bedingt.",
             "Genügt es für den Schutz, dass es andere Formen mit derselben Funktion gibt?", False,
             ["**Nein!** Ausschließlich technisch bedingt ist ein Merkmal, wenn die Funktion der einzige Faktor für seine Wahl war (§ 3 Abs. 1 Nr. 1 "
              "DesignG, Art. 8 Abs. 1 GGV). Alternativformen sind nur ein Indiz; entscheidend sind alle objektiven Umstände (EuGH DOCERAM). Der "
              "Kragen, der passen muss, fällt zusätzlich unter Art. 8 Abs. 2 GGV (Verbindungselement; RP1 II/2020)."],
             merke="Technische Bedingtheit: Funktion einziger Faktor (DOCERAM), Merkmal für Merkmal (BGH Tellerschleifgerät).",
             level=2, concepts=["des_technisch_bedingt", "des_verbindungselemente"], norms=["§ 3 Abs. 1 DesignG", "Art. 8 GGV"],
             cases=["des_eugh_doceram", "des_bgh_tellerschleifgeraet"], step=f"{SF}.3", abschnitt=DN),
        fall("d03a-7", "Sechs Helme in einer Einzelanmeldung",
             "Herr Sport meldet beim DPMA ein Einzeldesign „Kinderhelm“ mit sechs Ansichten an. Die Ansichten zeigen Reit-, Ski- und Radhelme mit "
             "unterschiedlichen Schirmen, Farben und Grafiken.",
             "Hat das eingetragene Design einen einheitlichen Schutzgegenstand?", False,
             ["**Nein!** Geschützt sind die sichtbar wiedergegebenen Merkmale (§ 37 Abs. 1 DesignG). Zeigen die Ansichten eines Einzeldesigns "
              "verschiedene Ausführungsformen, geben sie nicht die Erscheinungsform „eines“ Erzeugnisses wieder; das Design ist nach § 33 Abs. 1 "
              "Nr. 1 DesignG nichtig (BGH Sporthelm). Richtig wäre eine Sammelanmeldung (§ 12 DesignG; RP1 III/2019)."],
             merke="Ein Einzeldesign = eine Erscheinungsform; Varianten in die Sammelanmeldung (§ 12 DesignG).",
             level=2, concepts=["des_schutzgegenstand", "des_wiedergabe", "des_sammelanmeldung"], norms=["§ 37 Abs. 1 DesignG", "§ 33 Abs. 1 DesignG", "§ 12 DesignG"],
             cases=["des_bgh_sporthelm"], step=f"{SF}.1", abschnitt=DN),
        *fallkette("d03a-8", "Handbrause DISC (nach RP1 II/2019)",
            "Die BRAUSEN GmbH präsentierte ihre Handbrause DISC am Sa 17.06.2017 öffentlich in ihrer Badausstellung. Am Sa 17.02.2018 meldete sie "
            "DISC ohne Priorität als deutsches Design an. Die Mandantin hält DISC für nicht neu.",
            [frage("Wann beginnt der Zwölfmonatszeitraum des § 6 DesignG?", 2,
                   ["**Fr 17.02.2017.** Rückwärtsfrist ab dem Anmeldetag Sa 17.02.2018, berechnet entsprechend § 187 Abs. 1 BGB, § 188 Abs. 2 BGB "
                    "(§ 186 BGB). Eine Verschiebung nach § 193 BGB gibt es nicht, weil keine Handlung vorzunehmen ist."],
                   optionen=["Sa 17.06.2017", "Mo 20.02.2017", "Fr 17.02.2017", "Do 16.02.2017"],
                   merke="Schonfrist: § 6 S. 1 DesignG · Rückrechnung § 187 Abs. 1, § 188 Abs. 2 BGB · keine Verschiebung.", titel="Fristbeginn",
                   level=2),
             frage("Schadet die Präsentation der Neuheit von DISC?", False,
                   ["**Nein!** Die eigene Offenbarung der Anmelderin am 17.06.2017 liegt innerhalb der zwölf Monate vor dem Anmeldetag und bleibt "
                    "nach § 6 S. 1 DesignG für § 2 Abs. 2, 3 DesignG unberücksichtigt. Ein Angriff über § 33 Abs. 1 Nr. 2 DesignG hat daher kaum "
                    "Aussicht; die Lösung greift DISC über das ältere Design DE2 an (§ 33 Abs. 2 Nr. 2 DesignG)."],
                   merke="Eigene Offenbarung in der Schonfrist ist kein Formenschatz.", titel="Wirkung der Schonfrist",
                   norms=["§ 6 DesignG", "§ 2 DesignG"], concepts=["des_neuheitsschonfrist"]),
             frage("Hat BRAUSEN mit der Präsentation zusätzlich ein nicht eingetragenes Unionsgeschmacksmuster erworben?", True,
                   ["**Ja**, bei Neuheit und Eigenart: erste Offenbarung in der Union, den Fachkreisen bekannt (Art. 11 Abs. 1, 2 GGV). Schutz drei "
                    "Jahre ab Sa 17.06.2017, also bis Di 16.06.2020, aber nur gegen Nachahmung (Art. 19 Abs. 4 GGV)."],
                   merke="Nicht eingetragenes Muster: drei Jahre ab Offenbarung, nur gegen Nachahmung (Art. 11, Art. 19 Abs. 4 GGV).",
                   titel="Nicht eingetragenes Muster", norms=["Art. 11 GGV", "Art. 19 GGV"], concepts=["des_ggm_nicht_eingetragen"]),
             frage("Wie wäre es, wenn BRAUSEN DISC schon am 15.01.2017 präsentiert hätte – wäre DISC dann neu?", False,
                   ["**Nein!** Die Präsentation läge vor Beginn der Schonfrist (17.02.2017) und gehört zum Formenschatz. Gegenüber dem identischen "
                    "eigenen Erzeugnis fehlt die Neuheit (§ 2 Abs. 2 DesignG); das Design wäre nach § 33 Abs. 1 Nr. 2 DesignG nichtig."],
                   abwandlung="Die Präsentation fand bereits am 15.01.2017 statt.",
                   merke="Eigene Offenbarung vor der Schonfrist zerstört die Neuheit.", titel="Außerhalb der Schonfrist", level=2),
            ],
            abschnitt=KF, level=2, step=f"{SF}.4"),
        *fallkette("d03a-9", "Nudel M1 (nach RP1 I/2021)",
            "Designer Frank, Angestellter der Pasta GmbH, entwarf im Dezember 2017 die Nudel M1. Pasta zeigte sie im März 2018 auf einer Schweizer "
            "Fachmesse und gab die Abbildung der Düse GmbH, die sie im Juni 2018 in ihrem Gebrauchsmuster veröffentlichte. Rechtsnachfolgerin "
            "Sapore meldete M1 am 30.01.2019 als Unionsmuster an.",
            [frage("Stand das Recht auf das Unionsmuster an M1 zunächst der Pasta GmbH zu?", True,
                   ["**Ja!** Entwirft ein Arbeitnehmer in Ausübung seiner Aufgaben, steht das Recht dem Arbeitgeber zu (Art. 14 Abs. 3 GGV). "
                    "Sapore ist Rechtsnachfolgerin (Art. 14 Abs. 1 GGV) und darf sich auf die Schonfrist berufen."],
                   merke="Arbeitnehmerdesign: Art. 14 Abs. 3 GGV, § 7 Abs. 2 DesignG.", titel="Berechtigung",
                   norms=["Art. 14 GGV"], concepts=["des_arbeitnehmerdesign"]),
             frage("Schadet die Messe in der Schweiz im März 2018 der Neuheit?", False,
                   ["**Nein!** Sie ist zwar eine Offenbarung, die die Fachkreise der Union kennen konnten (Art. 7 Abs. 1 GGV). Sie stammt aber von der "
                    "Rechtsvorgängerin und liegt in den zwölf Monaten vor dem 30.01.2019; sie bleibt unberücksichtigt (Art. 7 Abs. 2 GGV)."],
                   merke="Schonfrist deckt den Rechtsvorgänger: Art. 7 Abs. 2 lit. a GGV.", titel="Messe in der Schweiz",
                   norms=["Art. 7 GGV"], concepts=["des_neuheitsschonfrist"]),
             frage("Schadet die Veröffentlichung im Gebrauchsmuster der Düse GmbH?", False,
                   ["**Nein!** Ein Dritter hat M1 „als Folge von Informationen“ der Rechtsvorgängerin offenbart (Art. 7 Abs. 2 lit. a GGV); die "
                    "Kooperationsvereinbarung belegt die Herkunft der Abbildung. Juni 2018 liegt in der Schonfrist."],
                   merke="Offenbarung durch Dritte als Folge eigener Informationen ist geschont.", titel="Gebrauchsmuster der Düse GmbH",
                   level=2),
             frage("Hilft die Schonfrist auch gegen die ältere eigene Nudel M0 aus 2015?", False,
                   ["**Nein!** M0 wurde 2015 bekannt gemacht, also mehr als zwölf Monate vor dem 30.01.2019. M1 muss sich an M0 messen lassen: Die "
                    "zweite Randkontur und die Symmetrie müssen einen anderen Gesamteindruck ergeben (Art. 6 GGV). Technisch bedingte Unterschiede "
                    "gewichtet der informierte Benutzer gering."],
                   merke="Eigene Altdesigns außerhalb der Schonfrist sind Formenschatz.", titel="Eigenes älteres Design",
                   norms=["Art. 6 GGV"], concepts=["des_eigenart"], level=3),
            ],
            abschnitt=KF, level=2, step=f"{SF}.4"),
    ]),
    # ================================================================== Verletzung
    dict(id="d03b", titel="§ 42 DesignG, Art. 19, Art. 89 GGV: Verletzungsansprüche", einheiten=[
        intro("d03b-0", "Prüfungsschema",
              "**AGL:** § 42 Abs. 1 S. 1 DesignG i.V.m. § 38 Abs. 1 S. 1 DesignG (Beseitigung, Unterlassung), § 42 Abs. 2 DesignG (Schadensersatz); "
              "Unionsmuster: Art. 19 Abs. 1 GGV i.V.m. Art. 89 Abs. 1 GGV (Unterlassung), Folgeansprüche Art. 89 Abs. 2 GGV, Art. 88 Abs. 2 GGV, "
              "Art. 8 Abs. 2 Rom-II-VO i.V.m. § 62a Nr. 1 DesignG, § 42 Abs. 2 DesignG, § 43 DesignG, § 46 DesignG\n\n"
              "**A · Aktivlegitimation und Schutzrecht**\n"
              "**V1 Anspruchsteller** – § 1 Nr. 5 DesignG, § 8 DesignG (eingetragener Inhaber), Art. 17 GGV; Lizenznehmer nur nach § 31 Abs. 3 "
              "DesignG, Art. 32 Abs. 3 GGV; nicht eingetragenes Muster: Inhaberschaft nach Art. 14 GGV beweisen (BGH Bolerojäckchen)\n"
              "**V2 Wirksames Schutzrecht** – eingetragen und in Kraft (§ 27 DesignG, § 28 DesignG; Art. 12 GGV); Vermutung der Rechtsgültigkeit "
              "§ 39 DesignG, Art. 85 Abs. 1 GGV; nicht eingetragenes Muster: Art. 11 GGV beweisen und Eigenart angeben (Art. 85 Abs. 2 GGV)\n\n"
              "**B · Verletzung**\n"
              "**V3 Benutzungshandlung** – § 38 Abs. 1 S. 2 DesignG, Art. 19 Abs. 2 GGV: Herstellen, Anbieten, Inverkehrbringen, Einfuhr, Ausfuhr, "
              "Gebrauch, Besitz zu diesen Zwecken; im Schutzgebiet\n"
              "**V4 Schutzumfang** – § 38 Abs. 2 DesignG, Art. 10 GGV: kein anderer Gesamteindruck beim informierten Benutzer; Gestaltungsfreiheit "
              "und Abstand zum Formenschatz (BGH Untersetzer)\n"
              "**V5 Ohne Zustimmung, Nachahmung wo nötig** – § 38 Abs. 1 S. 1 DesignG; während der Aufschiebung nur gegen Nachahmung (§ 38 Abs. 3 "
              "DesignG, Art. 19 Abs. 5 GGV); nicht eingetragenes Muster nur gegen Nachahmung (Art. 19 Abs. 4 GGV)\n\n"
              "**C · Keine Einwendungen**\n"
              "**V6 Keine Schranke** – § 40 DesignG, Art. 20 GGV; Reparaturklausel § 40a DesignG, Art. 20a GGV; Erschöpfung § 48 DesignG, "
              "Art. 21 GGV; Vorbenutzungsrecht § 41 DesignG, Art. 22 GGV\n"
              "**V7 Nichtigkeit nicht wirksam geltend gemacht** – nur durch Widerklage oder Antrag (§ 52a S. 1 DesignG, Art. 85 Abs. 1 S. 2 GGV); "
              "im Eilverfahren Einwand zulässig (§ 52a S. 2 DesignG, Art. 90 Abs. 2 GGV)\n\n"
              "**D · Anspruchsspezifisch**\n"
              "**V8 Begehungsgefahr** – Wiederholungsgefahr nach Verletzung (§ 42 Abs. 1 S. 1 DesignG) oder Erstbegehungsgefahr (§ 42 Abs. 1 S. 2 "
              "DesignG; Art. 89 Abs. 1 GGV „zu verletzen droht“)\n"
              "**V9 Verschulden** – für Schadensersatz Vorsatz oder Fahrlässigkeit (§ 42 Abs. 2 S. 1 DesignG); dreifache Berechnung (§ 42 Abs. 2 "
              "S. 2, 3 DesignG)\n"
              "**V10 Folgeansprüche** – Vernichtung, Rückruf, Überlassung (§ 43 Abs. 1 bis 3 DesignG, Verhältnismäßigkeit § 43 Abs. 4 DesignG), "
              "Auskunft (§ 46 Abs. 1, 3 DesignG), Vorlage und Besichtigung (§ 46a DesignG), Urteilsbekanntmachung (§ 47 DesignG)\n\n"
              "**⇒ Rechtsfolge:** Unterlassung und die Folgeansprüche; Verbot aus dem Unionsmuster in der ganzen Union, wenn das Gericht nach "
              "Art. 82 Abs. 1 bis 4 GGV zuständig ist (Art. 83 Abs. 1 GGV); Verjährung § 49 S. 1 DesignG i.V.m. § 195 BGB, § 199 Abs. 1 BGB\n\n"
              "**Klausurfallen:** Ein eigenes jüngeres Design ist kein Benutzungsrecht (EuGH Celaya). Messeausstellung ist Anbieten; für den "
              "Inlandsvertrieb braucht es konkrete Anhaltspunkte der Erstbegehungsgefahr. Bei Ersatzteilen Reparaturklausel und Erschöpfung "
              "prüfen. Das alte Recht (Art. 89 Abs. 1 lit. a bis d GGV a.F.) zitiert § 62a Nr. 1 DesignG noch.\n\n"
              "**In den Klausuren:** II/2019 (Lösung: Unterlassung aus EU1 und DE1, Erstbegehungsgefahr), III/2018 (Kinderwagen: Unterlassung, "
              "Auskunft, Vernichtung), I/2019 (Abmahnung, Aufschiebung, Vorbenutzung), III/2019 (Helm), I/2020 (Scheren), II/2020 (Tankeinsatz), "
              "II/2021 (Trageschlaufe), III/2021 (Abmahnung, Erstbegehungsgefahr), I/2022 (Ersatzteil, Erschöpfung), III/2022 (Handyhalterung), "
              "III/2023 (Sonnenschirm gegen Regenschirm).",
              concepts=["des_benutzung", "des_schutzumfang", "des_unterlassung", "des_schadensersatz", "des_schranken", "des_vermutung_rechtsgueltigkeit"],
              norms=["§ 42 DesignG", "§ 38 DesignG", "§ 39 DesignG", "§ 40 DesignG", "§ 40a DesignG", "§ 41 DesignG", "§ 43 DesignG", "§ 46 DesignG",
                     "§ 48 DesignG", "§ 49 DesignG", "§ 52a DesignG", "§ 62a DesignG", "Art. 10 GGV", "Art. 19 GGV", "Art. 85 GGV", "Art. 89 GGV"],
              distinctions=["d_des_anspruchsgrundlagen_eu"], abschnitt="Normenkette"),
        intro("d03b-1", "Definitionen",
              "**Benutzung:** insbesondere Herstellung, Anbieten, Inverkehrbringen, Einfuhr, Ausfuhr, Gebrauch eines Erzeugnisses, in das das Design "
              "aufgenommen ist, und Besitz zu diesen Zwecken (§ 38 Abs. 1 S. 2 DesignG; Art. 19 Abs. 2 GGV, dort auch 3D-Druck-Dateien lit. d)\n"
              "**Anbieten:** wirtschaftlich zu verstehen; jede Handlung, die das Erzeugnis dem Erwerb durch Dritte zugänglich macht, auch "
              "Ausstellen auf einer Verkaufsmesse (Lösung RP1 II/2019)\n"
              "**Schutzumfang:** jedes Design, das beim informierten Benutzer keinen anderen Gesamteindruck erweckt; Gestaltungsfreiheit "
              "berücksichtigen (§ 38 Abs. 2 DesignG; Art. 10 GGV); je größer der Abstand zum Formenschatz, desto weiter (BGH Untersetzer)\n"
              "**Gesamteindruck bei der Verletzung:** Wahrnehmung des informierten Benutzers bei bestimmungsgemäßer Verwendung (BGH Armbanduhr); "
              "technisch bedingte Übereinstimmungen wiegen gering (BGH Kinderwagen II)\n"
              "**Wiederholungsgefahr:** durch eine begangene Verletzung vermutet; entfällt nur durch strafbewehrte Unterlassungserklärung "
              "(Rechtsprechung)\n"
              "**Erstbegehungsgefahr:** ernsthafte und greifbare Anhaltspunkte, dass eine Verletzung unmittelbar bevorsteht (§ 42 Abs. 1 S. 2 "
              "DesignG: „erstmalig droht“), etwa Ankündigung auf der Homepage (RP1 III/2021)\n"
              "**Verletzer:** wer entgegen § 38 Abs. 1 S. 1 DesignG ein eingetragenes Design benutzt (Legaldefinition § 42 Abs. 1 S. 1 DesignG)\n"
              "**Erschöpfung:** keine Rechte an Erzeugnissen, die der Rechtsinhaber oder ein Dritter mit seiner Zustimmung im EWR in Verkehr "
              "gebracht hat (§ 48 DesignG; Art. 21 GGV)\n"
              "**Vorbenutzungsrecht:** DesignG: gutgläubige Benutzung oder wirkliche und ernsthafte Anstalten im Inland vor dem Anmeldetag für "
              "ein identisches, unabhängig entwickeltes Design (§ 41 Abs. 1 DesignG; BGH Bettgestell); GGV: in der Union, für ein in den "
              "Schutzumfang fallendes, nicht nachgeahmtes Muster (Art. 22 Abs. 1 GGV)\n"
              "**Reparaturklausel:** kein Schutz für ein Bauelement eines komplexen Erzeugnisses, das allein zur Reparatur verwendet wird, um das "
              "ursprüngliche Erscheinungsbild wiederherzustellen, bei ordnungsgemäßer Information über den Ursprung (§ 40a DesignG; Art. 20a GGV: "
              "nur wenn das Erscheinungsbild des Bauelements von dem des komplexen Erzeugnisses abhängt)\n"
              "**Zitierung:** Wiedergabe als Belegstelle für eigene Ausführungen, vereinbar mit redlichem Geschäftsverkehr und mit Quellenangabe "
              "(§ 40 Nr. 3 DesignG; BGH ICE; EuGH Nintendo)",
              concepts=["des_benutzung", "des_schutzumfang", "des_erschoepfung", "des_vorbenutzungsrecht", "des_reparaturklausel", "des_zitierschranke"],
              cases=["des_bgh_untersetzer", "des_bgh_armbanduhr", "des_bgh_bettgestell", "des_bgh_ice"], abschnitt="Definitionen"),
        mc("d03b-2", "Vorbenutzungsrecht DE und EU", "Worin unterscheidet sich das Vorbenutzungsrecht des § 41 DesignG von Art. 22 GGV?",
           ["§ 41 DesignG verlangt ein identisches Design und Benutzung im Inland, Art. 22 GGV genügt ein in den Schutzumfang fallendes Muster in der Union",
            "Art. 22 GGV verlangt Benutzung in jedem Mitgliedstaat, § 41 DesignG in einem Bundesland",
            "Nur § 41 DesignG verlangt Gutgläubigkeit",
            "Nur Art. 22 GGV erlaubt die Vergabe von Lizenzen"], 0,
           ["**Identität und Inland gegen Schutzumfang und Union.** § 41 Abs. 1 S. 1 DesignG schützt den Dritten, der vor dem Anmeldetag im "
            "Inland ein identisches, unabhängig entwickeltes Design benutzt hat. Art. 22 Abs. 1 GGV lässt ein nicht nachgeahmtes Muster im "
            "Schutzumfang und Benutzung in der Union genügen. Gutgläubigkeit verlangen beide; Lizenzen sind beide Male ausgeschlossen."],
           merke="Vorbenutzung: § 41 DesignG identisch + Inland; Art. 22 GGV Schutzumfang + Union; keine Lizenzen.",
           level=2, concepts=["des_vorbenutzungsrecht"], norms=["§ 41 DesignG", "Art. 22 GGV"], cases=["des_bgh_bettgestell"], step=f"{VL}.5",
           abschnitt=DN),
        fall("d03b-3", "Unabhängige Gestaltung",
             "Die Policepart KG hat ihre Pistole unabhängig entworfen, ohne das ähnliche, auf einer Messe in Berlin gezeigte Modell der Klingel "
             "GmbH zu kennen. Klingel hat nur ein nicht eingetragenes Unionsgeschmacksmuster.",
             "Kann Klingel Policepart den Vertrieb verbieten?", False,
             ["**Nein!** Aus dem nicht eingetragenen Muster kann der Inhaber nur Benutzungen verbieten, die auf Nachahmung beruhen (Art. 19 Abs. 4 "
              "UAbs. 1 GGV). Keine Nachahmung ist die unabhängige Gestaltung eines Entwerfers, der das Muster berechtigterweise nicht kannte "
              "(UAbs. 2). Die Beweislast für die Nachahmung trägt der Inhaber (EuGH Gautzsch)."],
             merke="Nicht eingetragenes Muster: nur Nachahmungsschutz, Art. 19 Abs. 4 GGV.",
             level=1, concepts=["des_ggm_nicht_eingetragen"], norms=["Art. 19 GGV"], cases=["des_eugh_gautzsch"], step=f"{UG}.3", abschnitt=DN),
        mc("d03b-4", "Schutzumfang", "Wovon hängt die Weite des Schutzumfangs nach § 38 Abs. 2 DesignG ab?",
           ["Vom Abstand zum vorbekannten Formenschatz und von der Gestaltungsfreiheit des Entwerfers",
            "Von der Erzeugnisangabe in der Anmeldung", "Vom Bekanntheitsgrad des Erzeugnisses",
            "Von der Gestaltungsfreiheit des Verletzers"], 0,
           ["**Abstand und Gestaltungsfreiheit.** Je größer die Gestaltungsfreiheit und der Abstand zum Formenschatz, desto weiter der Schutz; "
            "bei hoher Musterdichte ist er eng (§ 38 Abs. 2 S. 2 DesignG; BGH Untersetzer). Die Erzeugnisangabe beeinflusst den Schutzumfang "
            "nicht (§ 11 Abs. 6 DesignG; RP1 III/2023: Sonnenschirm gegen Regenschirm)."],
           merke="Schutzumfang § 38 Abs. 2 DesignG = Spiegel der Eigenart; Erzeugnisangabe irrelevant (§ 11 Abs. 6 DesignG).",
           level=1, concepts=["des_schutzumfang", "des_gestaltungsfreiheit", "des_erzeugnisangabe"], norms=["§ 38 Abs. 2 DesignG", "§ 11 DesignG"],
           cases=["des_bgh_untersetzer"], step=f"{VL}.4", abschnitt=DN),
        fall("d03b-5", "Eigenes jüngeres Design",
             "Die BRAUSEN GmbH vertreibt ihre Handbrause DISC, für die sie ein eingetragenes Design hat. Die Mandantin klagt aus ihrem älteren "
             "Design DE2, in dessen Schutzumfang DISC fällt.",
             "Kann BRAUSEN sich auf ihr eigenes eingetragenes Design berufen?", False,
             ["**Nein!** Das Design gewährt ein Verbietungsrecht, kein positives Benutzungsrecht gegenüber älteren Rechten. Auch der Inhaber eines "
              "jüngeren eingetragenen Designs ist „Dritter“ (EuGH Celaya zu Art. 19 Abs. 1 GGV). Die Mandantin muss DISC nicht vorher "
              "beseitigen; sie kann zusätzlich die Einwilligung in die Löschung verlangen (§ 33 Abs. 6 DesignG)."],
             merke="Prioritätsprinzip: jüngeres Design schützt nicht vor älterem (EuGH Celaya).",
             level=2, concepts=["des_benutzung"], norms=["§ 38 Abs. 1 DesignG", "Art. 19 GGV"], cases=["des_eugh_celaya"], step=f"{VL}.5", abschnitt=DN),
        mc("d03b-6", "Schadensersatz aus dem Unionsmuster",
           "Ein Händler verletzt in Deutschland ein eingetragenes Unionsgeschmacksmuster. Auf welche Normenkette stützt der Inhaber vor einem "
           "deutschen Gericht den Schadensersatz?",
           ["Art. 89 Abs. 2 GGV, Art. 88 Abs. 2 GGV, Art. 8 Abs. 2 Rom-II-VO i.V.m. § 62a Nr. 1 DesignG, § 42 Abs. 2 DesignG",
            "Art. 89 Abs. 1 GGV allein", "§ 42 Abs. 2 DesignG unmittelbar",
            "Art. 19 Abs. 1 GGV i.V.m. § 823 Abs. 1 BGB"], 0,
           ["**Die Verweisungskette.** Die GGV regelt nur das Verbot selbst (Art. 89 Abs. 1 GGV). Für andere Maßnahmen gilt das anwendbare Recht "
            "(Art. 89 Abs. 2 GGV, Art. 88 Abs. 2 GGV): nach Art. 8 Abs. 2 Rom-II-VO das Recht des Staates der ursprünglichen Verletzungshandlung "
            "(EuGH Nintendo, Acacia/BMW). Deutsches Recht wendet über § 62a Nr. 1 DesignG den § 42 Abs. 2 DesignG entsprechend an."],
           merke="Unionsmuster: Verbot aus Art. 89 Abs. 1 GGV, Folgen über Art. 88 Abs. 2 GGV, Art. 8 Abs. 2 Rom-II-VO, § 62a DesignG.",
           level=2, concepts=["des_ggm_anwendbares_recht", "des_schadensersatz"], norms=["Art. 89 GGV", "Art. 88 GGV", "§ 62a DesignG", "§ 42 Abs. 2 DesignG"],
           cases=["des_eugh_nintendo", "des_eugh_acacia_bmw"], step=f"{UG}.5", abschnitt=DN),
        mc("d03b-7", "Verjährung", "Wann verjähren die Ansprüche aus § 42 DesignG?",
           ["In drei Jahren ab dem Schluss des Jahres der Kenntnis (§ 49 S. 1 DesignG i.V.m. § 195 BGB, § 199 Abs. 1 BGB)",
            "In drei Jahren ab der Verletzungshandlung (§ 49 DesignG)", "In fünf Jahren ab Eintragung des Designs",
            "Gar nicht, solange das Design in Kraft ist"], 0,
           ["**Regelverjährung.** § 49 S. 1 DesignG verweist auf das BGB: drei Jahre (§ 195 BGB) ab dem Schluss des Jahres, in dem der Anspruch "
            "entstanden ist und der Verletzte Kenntnis von Verletzung und Verletzer erlangt hat (§ 199 Abs. 1 BGB). Bei jeder neuen Verletzung "
            "entsteht der Unterlassungsanspruch neu; Restschadensersatz nach § 49 S. 2 DesignG, § 852 BGB."],
           merke="Verjährung: § 49 S. 1 DesignG · § 195 BGB · Beginn § 199 Abs. 1 BGB (Jahresschluss).",
           level=1, concepts=["des_verjaehrung"], norms=["§ 49 DesignG"], step=f"{VL}.7", abschnitt=DN),
        *fallkette("d03b-8", "Handbrause COPY1 auf der Messe (nach RP1 II/2019)",
            "Die Mandantin ist Inhaberin des Unionsmusters EU1 und des parallelen deutschen Designs DE1 für eine Handbrause, beide bekannt gemacht. "
            "Zulieferer berichten, mehrere chinesische Firmen und eine spanische Firma wollten auf der Frankfurter Messe in sechs Wochen die "
            "Brause COPY1 ausstellen. COPY1 hat zusätzlich eine Rippe auf der Rückseite.",
            [frage("Ist das Ausstellen auf einer Verkaufsmesse eine Benutzung?", True,
                   ["**Ja!** Anbieten ist wirtschaftlich zu verstehen und umfasst das Ausstellen zur Gewinnung von Abnehmern (Art. 19 Abs. 2 lit. a "
                    "GGV, § 38 Abs. 1 S. 2 DesignG). Die Einfuhr zur Messe ist eine weitere Benutzung (Art. 19 Abs. 2 lit. b GGV)."],
                   merke="Messeausstellung = Anbieten; Einfuhr zur Messe = Einfuhr.", titel="Benutzungshandlung",
                   norms=["Art. 19 GGV", "§ 38 Abs. 1 DesignG"], step=f"{VL}.3"),
             frage("Begründet die Rippe auf der Rückseite einen anderen Gesamteindruck?", False,
                   ["**Nein**, voraussichtlich nicht. Maßgeblich ist die Wahrnehmung bei bestimmungsgemäßer Verwendung (BGH Armbanduhr): Der Benutzer "
                    "blickt auf Strahlscheibe, Kopfform und Griff, die übereinstimmen. Bei weitem Schutzumfang ohne nahen Formenschatz tritt die "
                    "Rippe zurück (Art. 10 GGV, § 38 Abs. 2 DesignG)."],
                   merke="Gesamteindruck: Wahrnehmung im Gebrauch, prägende Merkmale vor Details.", titel="Schutzumfang",
                   norms=["Art. 10 GGV", "§ 38 Abs. 2 DesignG"], cases=["des_bgh_armbanduhr"], level=2, step=f"{VL}.4"),
             frage("Kann die Mandantin schon jetzt Unterlassung verlangen, obwohl COPY1 noch nicht ausgestellt wurde?", True,
                   ["**Ja**, bei Erstbegehungsgefahr (§ 42 Abs. 1 S. 2 DesignG; Art. 89 Abs. 1 GGV: „zu verletzen droht“). Sie braucht aber konkrete "
                    "Anhaltspunkte; das Hörensagen der Zulieferer genügt kaum. Belege sammeln: Ausstellerverzeichnis, Messekatalog, Vorab-Werbung."],
                   merke="Vorbeugende Unterlassung: Erstbegehungsgefahr konkret belegen.", titel="Erstbegehungsgefahr",
                   norms=["§ 42 Abs. 1 DesignG", "Art. 89 GGV"], level=2, step=f"{VL}.6"),
             frage("Können sich die Aussteller im Hauptsacheverfahren einfach auf die Nichtigkeit von EU1 berufen?", False,
                   ["**Nein!** Das Gericht geht von der Rechtsgültigkeit aus; bestreiten kann der Beklagte sie nur mit Widerklage (Art. 85 Abs. 1 GGV; "
                    "für DE1 § 39 DesignG, § 52a S. 1 DesignG). Im Eilverfahren ist der Einwand dagegen zulässig (Art. 90 Abs. 2 GGV, § 52a S. 2 DesignG)."],
                   merke="Nichtigkeit nur per Widerklage oder Antrag; im Eilverfahren als Einwand.", titel="Einwand der Nichtigkeit",
                   norms=["Art. 85 GGV", "§ 52a DesignG"], concepts=["des_vermutung_rechtsgueltigkeit"], step=f"{VL}.5"),
            ],
            abschnitt=KF, level=2, concepts=["des_benutzung", "des_unterlassung"]),
        *fallkette("d03b-9", "Griffrohr als Ersatzteil (nach RP1 I/2022)",
            "Die M GmbH hat ein deutsches Design für das Griffrohr ihres Staubsaugers; das Griffrohr wurde im Januar 2020 in einer Fachzeitschrift "
            "in der EU erstveröffentlicht. VP holte eine Charge Griffrohre bei M in Hannover ab und lieferte daraus an FairRepair in Berlin, die sie "
            "als Ersatzteil anbietet.",
            [frage("Verletzt das Angebot der Griffrohre aus der Charge von M das deutsche Design?", False,
                   ["**Nein!** Die Griffrohre hat M selbst im EWR in Verkehr gebracht; ihre Rechte sind erschöpft (§ 48 DesignG). Weitere Lieferung "
                    "und Angebot dieser Stücke sind frei."],
                   merke="Erschöpfung § 48 DesignG, Art. 21 GGV: Inverkehrbringen im EWR durch oder mit Zustimmung des Inhabers.",
                   titel="Erschöpfung", norms=["§ 48 DesignG"], concepts=["des_erschoepfung"], step=f"{VL}.5"),
             frage("VP lässt optisch identische Griffrohre in Vietnam fertigen und liefert sie zur Reparatur nach Deutschland. Greift § 40a DesignG?", True,
                   ["**Ja**, wenn das Bauelement allein zur Reparatur verwendet wird, um das ursprüngliche Erscheinungsbild wiederherzustellen "
                    "(§ 40a Abs. 1 DesignG), und die Verbraucher ordnungsgemäß über den Ursprung unterrichtet werden (§ 40a Abs. 2 DesignG). Ohne "
                    "Hinweis bleibt es bei der Verletzung."],
                   abwandlung="VP bezieht künftig nachgebaute Griffrohre aus Vietnam.",
                   merke="Reparaturklausel § 40a DesignG: nur Reparatur, ursprüngliches Erscheinungsbild, Ursprungshinweis.", titel="Reparaturklausel",
                   norms=["§ 40a DesignG"], concepts=["des_reparaturklausel"], cases=["des_bgh_kraftfahrzeugfelgen_ii"], level=2, step=f"{VL}.5"),
             frage("Kann M den Import der Nachbauten nach Polen aus dem deutschen Design verbieten?", False,
                   ["**Nein!** Das deutsche Design wirkt nur im Inland. In Betracht kommt das nicht eingetragene Unionsmuster aus der Veröffentlichung "
                    "im Januar 2020: drei Jahre bis Januar 2023 (Art. 11 Abs. 1 GGV), nur gegen Nachahmung (Art. 19 Abs. 4 GGV), vorbehaltlich der "
                    "Reparaturklausel des Art. 20a GGV."],
                   merke="Territorialität: DE-Design nur Inland; unionsweit nur Unionsmuster.", titel="Polen",
                   norms=["Art. 11 GGV", "Art. 19 GGV", "Art. 20a GGV"], concepts=["des_ggm_nicht_eingetragen"], level=3, step=f"{UG}.3"),
            ],
            abschnitt=KF, level=2),
    ]),
    # ================================================================== Nichtigkeit
    dict(id="d03c", titel="§§ 33, 34, 34a DesignG, Art. 24, 25 GGV: Nichtigkeit", einheiten=[
        intro("d03c-0", "Prüfungsschema",
              "**AGL:** Antrag auf Feststellung (§ 33 Abs. 1 DesignG) oder Erklärung (§ 33 Abs. 2 DesignG) der Nichtigkeit beim DPMA, § 34a Abs. 1 "
              "DesignG; Widerklage § 52b DesignG. Unionsmuster: Antrag beim EUIPO Art. 24 Abs. 1 GGV, Art. 52 GGV i.V.m. Art. 25 GGV oder "
              "Widerklage Art. 81 lit. d GGV, Art. 84 GGV; nicht eingetragenes Muster nur vor dem Unionsgeschmacksmustergericht (Art. 24 Abs. 3 "
              "GGV, Art. 81 lit. c GGV)\n\n"
              "**A · Zulässigkeit**\n"
              "**V1 Statthaftigkeit** – eingetragenes Design, auch nach Ablauf oder Verzicht (§ 33 Abs. 5 DesignG; Art. 24 Abs. 2 GGV: mit "
              "berechtigtem Interesse)\n"
              "**V2 Zuständigkeit** – DPMA, Designabteilung mit drei rechtskundigen Mitgliedern (§ 34a Abs. 1 S. 1 DesignG, § 23 Abs. 2 S. 1 DesignG); "
              "EUIPO, Nichtigkeitsabteilung (Art. 105 GGV)\n"
              "**V3 Antragsbefugnis** – § 33 Abs. 1 DesignG: jedermann (§ 34 S. 1 DesignG); § 33 Abs. 2 DesignG: nur der Inhaber des betroffenen "
              "Rechts (§ 34 S. 2 DesignG); GGV: Art. 25 Abs. 2 GGV (lit. a, b jedermann), Art. 25 Abs. 3 GGV (Berechtigter), Art. 25 Abs. 4 GGV "
              "(lit. d bis f nur Inhaber, Berechtigte, ermächtigte Lizenznehmer)\n"
              "**V4 Form** – schriftlich, Tatsachen und Beweismittel (§ 34a Abs. 1 S. 1, 2 DesignG); Art. 52 Abs. 2 GGV: schriftlich, begründet\n"
              "**V5 Gebühr** – 300 EUR je Design (Nr. 346 100 Anlage PatKostG), fällig mit Antrag (§ 3 Abs. 1 PatKostG), drei Monate (§ 6 Abs. 1 "
              "S. 2 PatKostG), sonst Rücknahmefiktion (§ 6 Abs. 2 PatKostG), Zahlungstag § 2 PatKostZV; EUIPO: Antrag gilt erst mit Zahlung als "
              "gestellt (Art. 52 Abs. 2 S. 2 GGV)\n"
              "**V6 Keine entgegenstehende Rechtskraft** – § 34a Abs. 1 S. 4 DesignG, Art. 52 Abs. 3 GGV\n\n"
              "**B · Verfahren**\n"
              "**V7 Widerspruch des Inhabers** – ein Monat ab Zustellung (§ 34a Abs. 2 S. 1 DesignG · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 "
              "BGB); ohne Widerspruch Feststellung oder Erklärung der Nichtigkeit ohne Sachprüfung (§ 34a Abs. 2 S. 2 DesignG); beim EUIPO keine "
              "solche Fiktion (Art. 53 Abs. 1 GGV)\n\n"
              "**C · Begründetheit**\n"
              "**V8 Absolute Gründe** – § 33 Abs. 1 Nr. 1 DesignG (kein Design), Nr. 2 (nicht neu, keine Eigenart), Nr. 3 (Ausschluss § 3 DesignG); "
              "Art. 25 Abs. 1 lit. a, b GGV\n"
              "**V9 Relative Gründe** – § 33 Abs. 2 Nr. 1 DesignG (Urheberrecht), Nr. 2 (eingetragenes Design älteren Zeitrangs, auch wenn erst nach "
              "dem Anmeldetag offenbart), Nr. 3 (Zeichen mit Unterscheidungskraft); Art. 25 Abs. 1 lit. d bis f GGV; Nichtberechtigung Art. 25 "
              "Abs. 1 lit. c GGV (im DesignG nur Vindikation, § 9 DesignG)\n\n"
              "**⇒ Rechtsfolge:** Beschluss (§ 34a Abs. 4 DesignG), Schutzwirkungen gelten mit Unanfechtbarkeit als von Anfang an nicht eingetreten "
              "(§ 33 Abs. 4 DesignG; Art. 26 Abs. 1 GGV); Teilaufrechterhaltung § 35 DesignG; Löschung § 36 Abs. 1 Nr. 5 DesignG; Kosten § 34a "
              "Abs. 5 DesignG; Beschwerde zum BPatG binnen eines Monats (§ 23 Abs. 4 S. 4 DesignG i.V.m. § 73 Abs. 2 S. 1 PatG), 500 EUR (Nr. 401 100)\n\n"
              "**Klausurfallen:** Inhaber kann nach § 33 Abs. 6 DesignG in die Löschung einwilligen; ohne vorherige Aufforderung trägt dann der "
              "Antragsteller die Kosten (BPatG Kühlergitter-Emblemhalterung). Ein Strohmann ist für absolute Gründe unschädlich. Der Rechtsnachfolger "
              "eines Unionsmusters kann Rechte erst nach Eintragung des Übergangs geltend machen (Art. 28 Abs. 6 GGV). Aussetzung des Verletzungsprozesses "
              "Art. 91 GGV (nicht, wenn die Klage vor dem EUIPO-Antrag erhoben wurde, BGH Kinderwagen I) und § 34b DesignG.\n\n"
              "**In den Klausuren:** II/2019 (Lösung: Antrag gegen DISC aus DE2), III/2018 (Aussetzung in der Revision), I/2019, I/2020, II/2020 "
              "(Nichtigkeit und Aussetzung), III/2020 (Erfolgsaussichten), I/2021 (EUIPO, Strohmann, deutsches Design von Frau Schulz), III/2021 "
              "(technische Bedingtheit), II/2022 (älteres Unionsmuster, Übertragung), III/2022 (Angriff, Verfahren, Sprache, Kosten).",
              concepts=["des_nichtigkeit", "des_nichtigkeitsverfahren_dpma", "des_widerklage_nichtigkeit", "des_teilweise_aufrechterhaltung"],
              norms=["§ 33 DesignG", "§ 34 DesignG", "§ 34a DesignG", "§ 34b DesignG", "§ 35 DesignG", "§ 52b DesignG", "§ 23 DesignG",
                     "Art. 24 GGV", "Art. 25 GGV", "Art. 26 GGV", "Art. 52 GGV", "Art. 53 GGV", "Art. 91 GGV"],
              cases=["des_bpatg_emblemhalterung", "des_bgh_kinderwagen_i"], abschnitt="Normenkette"),
        intro("d03c-1", "Definitionen",
              "**Feststellung der Nichtigkeit:** bei absoluten Gründen des § 33 Abs. 1 DesignG; das Design ist von Anfang an nichtig, der Beschluss "
              "stellt das nur fest (§ 33 Abs. 1, 3 DesignG)\n"
              "**Erklärung der Nichtigkeit:** bei relativen Gründen des § 33 Abs. 2 DesignG; das Design „wird für nichtig erklärt“, nur auf Antrag "
              "des Inhabers des älteren Rechts (§ 33 Abs. 2 DesignG, § 34 S. 2 DesignG)\n"
              "**Älterer Zeitrang:** früherer Anmelde- oder Prioritätstag (§ 13 DesignG); das ältere eingetragene Design wirkt auch, wenn es erst "
              "nach dem Anmeldetag des jüngeren offenbart wurde (§ 33 Abs. 2 Nr. 2 DesignG; Art. 25 Abs. 1 lit. d GGV)\n"
              "**Rückwirkung:** die Schutzwirkungen gelten mit Unanfechtbarkeit des Beschlusses oder Rechtskraft des Urteils als von Anfang an nicht "
              "eingetreten (§ 33 Abs. 4 DesignG; Art. 26 Abs. 1 GGV; Ausnahmen für vollstreckte Urteile und erfüllte Verträge Art. 26 Abs. 2 GGV)\n"
              "**Antragsbefugnis „jedermann“:** kein eigenes Interesse nötig; auch ein Strohmann kann absolute Gründe geltend machen (§ 34 S. 1 "
              "DesignG; Art. 25 Abs. 2 GGV: jede natürliche oder juristische Person)\n"
              "**Widerklage:** Gegenangriff im Verletzungsprozess vor dem Designgericht; zuständig, wenn sie im Zusammenhang mit einer Klage aus "
              "demselben Design erhoben wird (§ 52b Abs. 1 DesignG; Art. 81 lit. d GGV, Art. 84 GGV)\n"
              "**Einwilligung in die Löschung:** Erklärung des Inhabers gegenüber dem DPMA; Wirkung wie Nichtigkeit ex tunc (§ 33 Abs. 6 DesignG)\n"
              "**Teilweise Aufrechterhaltung:** das Design bleibt in geänderter Form bestehen, wenn es dann die Schutzvoraussetzungen erfüllt und "
              "seine Identität behält (§ 35 Abs. 1 DesignG)",
              concepts=["des_nichtigkeit", "des_teilweise_aufrechterhaltung", "des_widerklage_nichtigkeit"], abschnitt="Definitionen"),
        mc("d03c-2", "Antragsbefugnis", "Wer darf die Erklärung der Nichtigkeit wegen eines älteren eingetragenen Designs (§ 33 Abs. 2 Nr. 2 DesignG) beantragen?",
           ["Nur der Inhaber des älteren Designs (§ 34 S. 2 DesignG)", "Jedermann (§ 34 S. 1 DesignG)",
            "Jeder, der vom Inhaber abgemahnt wurde", "Nur das DPMA von Amts wegen"], 0,
           ["**Nur der Inhaber des betroffenen Rechts.** Relative Gründe schützen private Rechte; deshalb darf sie nur ihr Inhaber geltend machen "
            "(§ 34 S. 2 DesignG; für Unionsmuster Art. 25 Abs. 4 GGV). Die absoluten Gründe des § 33 Abs. 1 DesignG kann jedermann rügen "
            "(§ 34 S. 1 DesignG)."],
           merke="§ 33 Abs. 1 DesignG: jedermann (§ 34 S. 1 DesignG) · § 33 Abs. 2 DesignG: nur Inhaber (§ 34 S. 2 DesignG).",
           level=1, concepts=["des_nichtigkeit"], norms=["§ 34 DesignG", "§ 33 Abs. 2 DesignG", "Art. 25 GGV"], step=f"{NV}.1", abschnitt=DN),
        mc("d03c-3", "Gebühr", "Welche Gebühr fällt für den Nichtigkeitsantrag beim DPMA an, und was folgt aus der Nichtzahlung?",
           ["300 EUR je Design (Nr. 346 100); ohne Zahlung binnen drei Monaten gilt der Antrag als zurückgenommen (§ 6 Abs. 1 S. 2, Abs. 2 PatKostG)",
            "300 EUR je Antrag; der Antrag wird als unzulässig verworfen", "500 EUR; das DPMA setzt eine Nachfrist",
            "Keine Gebühr; die Kosten werden am Ende festgesetzt"], 0,
           ["**300 EUR je eingetragenem Design.** Die Gebühr ist mit dem Antrag fällig (§ 3 Abs. 1 PatKostG) und binnen drei Monaten zu zahlen "
            "(§ 6 Abs. 1 S. 2 PatKostG); sonst gilt der Antrag als zurückgenommen (§ 6 Abs. 2 PatKostG). Die 500 EUR sind die Gebühr für die "
            "Beschwerde gegen den Beschluss (Nr. 401 100)."],
           merke="Nichtigkeit DPMA: 300 EUR je Design · § 3 Abs. 1 PatKostG · § 6 Abs. 1 S. 2 PatKostG · § 6 Abs. 2 PatKostG.",
           level=1, norms=["§ 34a DesignG", "§ 6 PatKostG", "§ 3 PatKostG"], step=f"{NV}.1", abschnitt=DN),
        fall("d03c-4", "Schweigen des Inhabers beim EUIPO",
             "Die Sapore S.r.l. erhält vom EUIPO die Aufforderung, zu einem Nichtigkeitsantrag gegen ihr eingetragenes Unionsmuster Stellung zu "
             "nehmen. Sie überlegt, nicht zu reagieren.",
             "Wird das Muster dann ohne Sachprüfung für nichtig erklärt?", False,
             ["**Nein!** Anders als das DPMA (§ 34a Abs. 2 S. 2 DesignG) kennt die GGV keine Nichtigkeitsfiktion: Ist der Antrag zulässig, prüft das "
              "EUIPO die Gründe des Art. 25 GGV in der Sache (Art. 53 Abs. 1 GGV). Sapore verliert aber die Möglichkeit, Schonfrist und "
              "Rechtsnachfolge vorzutragen (RP1 I/2021)."],
             merke="DPMA: kein Widerspruch → Nichtigkeit (§ 34a Abs. 2 S. 2 DesignG); EUIPO: Sachprüfung (Art. 53 Abs. 1 GGV).",
             level=2, concepts=["des_nichtigkeit"], norms=["Art. 53 GGV", "§ 34a Abs. 2 DesignG"], step=f"{NV}.2", abschnitt=DN),
        fall("d03c-5", "Strohmann",
             "Rechtsanwalt Klein beantragt beim EUIPO im eigenen Namen die Nichtigerklärung eines Unionsmusters wegen fehlender Neuheit und Eigenart. "
             "Tatsächlich handelt er für Frank, der anonym bleiben will.",
             "Ist der Antrag des Strohmanns zulässig?", True,
             ["**Ja!** Fehlende Neuheit und Eigenart (Art. 25 Abs. 1 lit. b GGV) kann jede natürliche oder juristische Person geltend machen "
              "(Art. 25 Abs. 2 GGV, Art. 52 Abs. 1 GGV); ein eigenes Interesse ist nicht nötig. Für relative Gründe genügt der Strohmann nicht: Sie "
              "darf nur der Inhaber des älteren Rechts geltend machen (Art. 25 Abs. 4 GGV)."],
             merke="Absolute Gründe: jedermann, auch Strohmann; relative Gründe: nur Inhaber (Art. 25 Abs. 2, 4 GGV).",
             level=2, concepts=["des_nichtigkeit"], norms=["Art. 25 GGV", "Art. 52 GGV"], step=f"{NV}.1", abschnitt=DN),
        fall("d03c-6", "Älteres, später bekannt gemachtes Unionsmuster",
             "Das Unionsmuster GGM-A der A SA wurde vor dem Unionsmuster GGM-C der C GmbH angemeldet, aber erst nach dessen Anmeldung eingetragen und "
             "veröffentlicht. Beide zeigen fast identische Ultraschallgeräte.",
             "Kann GGM-C auf GGM-A gestützt für nichtig erklärt werden?", True,
             ["**Ja!** Art. 25 Abs. 1 lit. d GGV erfasst ein früheres Muster, das „vor oder nach“ dem Anmeldetag des jüngeren offenbart wurde, wenn "
              "es seit einem früheren Zeitpunkt geschützt ist (Ziff. i: Unionsmuster oder dessen Anmeldung). Den Antrag darf nur der Inhaber des "
              "älteren Rechts stellen (Art. 25 Abs. 4 GGV; RP1 II/2022)."],
             merke="Kollision mit älterem Recht: Art. 25 Abs. 1 lit. d GGV, § 33 Abs. 2 Nr. 2 DesignG – auch nachveröffentlicht.",
             level=2, concepts=["des_nichtigkeit"], norms=["Art. 25 GGV", "§ 33 Abs. 2 DesignG"], step=f"{SF}.7", abschnitt=DN),
        fall("d03c-7", "Aussetzung in der Revision",
             "Die Klägerin klagt aus einem Unionsmuster gegen einen Kinderwagenhändler. Während das Verfahren in der Revision liegt, stellt die "
             "Beklagte beim EUIPO einen Antrag auf Nichtigerklärung.",
             "Muss das Gericht den Verletzungsprozess aussetzen?", False,
             ["**Nein!** Art. 91 Abs. 1 GGV verlangt die Aussetzung nur, wenn der Nichtigkeitsantrag beim Amt bereits gestellt war, als die "
              "Verletzungsklage erhoben wurde. Ein später gestellter Antrag zwingt nicht zur Aussetzung (BGH Kinderwagen I; RP1 III/2018). "
              "Für deutsche Designs gilt § 34b DesignG: Aussetzung nach Ermessen, Pflicht, wenn das Gericht das Design für nichtig hält."],
             merke="Aussetzung: Art. 91 Abs. 1 GGV nur bei früherem Amtsantrag; § 34b DesignG Ermessen.",
             level=3, concepts=["des_widerklage_nichtigkeit"], norms=["Art. 91 GGV", "§ 34b DesignG"], cases=["des_bgh_kinderwagen_i"],
             step=f"{UG}.4", abschnitt=DN),
        *fallkette("d03c-8", "Angriff auf DISC (nach RP1 II/2019)",
            "Die Mandantin ist Inhaberin des am 12.01.2016 angemeldeten deutschen Designs DE2 für eine Strahlscheibe. Die BRAUSEN GmbH meldete am "
            "17.02.2018 das Design DISC an, dessen Strahlscheibe identisch ist; ihre eigene Präsentation fällt in die Schonfrist. Die Mandantin will "
            "DISC aus dem Register haben.",
            [frage("Ist die Mandantin befugt, die Erklärung der Nichtigkeit nach § 33 Abs. 2 Nr. 2 DesignG zu beantragen?", True,
                   ["**Ja!** Den relativen Grund darf nur der Inhaber des betroffenen Rechts geltend machen (§ 34 S. 2 DesignG); das ist die "
                    "Mandantin als Inhaberin von DE2."],
                   merke="Relativer Grund: Antragsbefugnis nur des Inhabers, § 34 S. 2 DesignG.", titel="Antragsbefugnis", step=f"{NV}.1"),
             frage("Welche Form verlangt der Antrag?", 1,
                   ["**Schriftlich beim DPMA, mit Tatsachen und Beweismitteln** (§ 34a Abs. 1 S. 1, 2 DesignG). Es entscheidet die Designabteilung "
                    "mit drei rechtskundigen Mitgliedern (§ 23 Abs. 2 S. 1 DesignG). Ein Einspruchsverfahren gibt es nicht."],
                   optionen=["Mündlich zu Protokoll der Designstelle", "Schriftlich beim DPMA mit Tatsachen und Beweismitteln",
                             "Klage beim Landgericht München I", "Einspruch binnen drei Monaten nach Bekanntmachung"],
                   merke="Antrag: § 34a Abs. 1 S. 1, 2 DesignG · Designabteilung § 23 Abs. 2 DesignG.", titel="Form", step=f"{NV}.1"),
             frage("Ist der Antrag begründet, obwohl DE2 erst am 17.01.2017 bekannt gemacht wurde?", True,
                   ["**Ja**, voraussichtlich. DE2 hat älteren Zeitrang (12.01.2016), und DISC fällt mit der identischen Strahlscheibe in seinen "
                    "Schutzumfang (§ 33 Abs. 2 Nr. 2 DesignG, § 38 Abs. 2 DesignG). Auf die Bekanntmachung kommt es nicht an: Die Norm erfasst auch "
                    "ältere Designs, die erst nach dem Anmeldetag offenbart wurden."],
                   merke="§ 33 Abs. 2 Nr. 2 DesignG: älterer Zeitrang genügt, Bekanntmachung gleichgültig.", titel="Begründetheit",
                   level=2, step=f"{NV}.3"),
             frage("Was gilt, wenn BRAUSEN dem zugestellten Antrag nicht binnen eines Monats widerspricht?", True,
                   ["**Dann wird die Nichtigkeit ohne Sachprüfung erklärt** (§ 34a Abs. 2 S. 2 DesignG). Frist: ein Monat ab Zustellung (§ 34a Abs. 2 "
                    "S. 1 DesignG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB."],
                   abwandlung="BRAUSEN reagiert auf den zugestellten Antrag nicht.",
                   merke="Widerspruch: ein Monat, § 34a Abs. 2 S. 1 DesignG · § 187, § 188 BGB · § 193 BGB.", titel="Kein Widerspruch", step=f"{NV}.2"),
             frage("Wirkt die Nichtigerklärung nur für die Zukunft?", False,
                   ["**Nein!** Mit Unanfechtbarkeit des Beschlusses gelten die Schutzwirkungen von DISC als von Anfang an nicht eingetreten "
                    "(§ 33 Abs. 4 DesignG); das Design wird gelöscht (§ 36 Abs. 1 Nr. 5 DesignG)."],
                   merke="Wirkung ex tunc ab Unanfechtbarkeit, § 33 Abs. 4 DesignG.", titel="Wirkung", step=f"{NV}.4"),
            ],
            abschnitt=KF, level=2, concepts=["des_nichtigkeitsverfahren_dpma"], norms=["§ 33 DesignG", "§ 34 DesignG", "§ 34a DesignG"]),
        *fallkette("d03c-9", "Das deutsche Design der Frau Schulz (nach RP1 I/2021)",
            "Die Pasta GmbH zeigte die Nudel M1 im März 2018 auf einer Fachmesse, die den Fachkreisen der Union bekannt war. Frau Schulz, die M1 nicht "
            "entworfen hat, meldete am 31.01.2019 ein deutsches Design an, das M1 identisch zeigt. Sapore, Rechtsnachfolgerin der Pasta GmbH, will "
            "es schnell beseitigen.",
            [frage("Ist das Design von Frau Schulz neu?", False,
                   ["**Nein!** Die Messe im März 2018 hat M1 vor dem Anmeldetag offenbart (§ 5 S. 1 DesignG). Auf die Schonfrist des § 6 DesignG kann "
                    "sich Frau Schulz nicht berufen, weil sie weder Entwerferin noch Rechtsnachfolgerin ist. Das Design ist nicht neu (§ 2 Abs. 2 DesignG)."],
                   merke="Schonfrist nur für Entwerfer und Rechtsnachfolger, § 6 DesignG.", titel="Neuheit", step=f"{SF}.5"),
             frage("Darf Sapore die Feststellung der Nichtigkeit wegen fehlender Neuheit beantragen?", True,
                   ["**Ja!** Den absoluten Grund des § 33 Abs. 1 Nr. 2 DesignG kann jedermann geltend machen (§ 34 S. 1 DesignG), also auch Sapore."],
                   merke="Absoluter Grund: jedermann, § 34 S. 1 DesignG.", titel="Antragsbefugnis", step=f"{NV}.1"),
             frage("Kann Sapore stattdessen die Übertragung des Designs auf sich verlangen?", True,
                   ["**Ja**, wenn Sapore beweist, dass sie nach § 7 DesignG berechtigt ist (§ 9 Abs. 1 S. 1 DesignG): Übertragung oder Einwilligung in "
                    "die Löschung, durch Klage binnen drei Jahren ab Bekanntmachung (§ 9 Abs. 2 DesignG). Die Nichtberechtigung ist im DesignG kein "
                    "Nichtigkeitsgrund. Der Beweis fehlt hier; der Weg über § 33 Abs. 1 Nr. 2 DesignG ist sicherer."],
                   merke="Nichtberechtigung: Vindikation § 9 DesignG, kein Nichtigkeitsgrund des § 33 DesignG.", titel="Vindikation",
                   concepts=["des_vindikation"], level=3),
            ],
            abschnitt=KF, level=2, concepts=["des_nichtigkeit"], norms=["§ 33 Abs. 1 DesignG", "§ 34 DesignG"]),
    ]),
    # ================================================================== Zuständigkeit
    dict(id="d03d", titel="Art. 80 bis 83 GGV, § 52 DesignG, Brüssel-Ia-VO: Zuständigkeit", einheiten=[
        intro("d03d-0", "Prüfungsschema",
              "**AGL:** Zulässigkeit der Verletzungsklage – internationale, sachliche und örtliche Zuständigkeit. Unionsmuster: Art. 80 GGV, "
              "Art. 81 GGV, Art. 82 GGV, Art. 83 GGV i.V.m. § 63 DesignG, § 63b DesignG; deutsches Design: Brüssel-Ia-VO i.V.m. § 52 DesignG und ZPO\n\n"
              "**A · Unionsgeschmacksmuster**\n"
              "**V1 Unionsgeschmacksmusterstreitsache** – Art. 81 GGV: Verletzung und drohende Verletzung (lit. a), negative Feststellung (lit. b), "
              "Nichtigkeit des nicht eingetragenen Musters (lit. c), Widerklage (lit. d); ausschließlich die Unionsgeschmacksmustergerichte "
              "(Art. 80 Abs. 1 GGV), in Deutschland die Landgerichte (§ 63 Abs. 1 DesignG) mit Konzentration (§ 63 Abs. 2 DesignG)\n"
              "**V2 Internationale Zuständigkeit** – Art. 82 Abs. 1 GGV: Mitgliedstaat, in dem der Beklagte ansässig ist, hilfsweise niedergelassen; "
              "Art. 82 Abs. 2 GGV: sonst Wohnsitz oder Niederlassung des Klägers; Art. 82 Abs. 3 GGV: sonst Spanien (Sitz des EUIPO); Art. 82 Abs. 4 "
              "GGV: Gerichtsstandsvereinbarung, rügelose Einlassung; Art. 82 Abs. 5 GGV: Staat der begangenen oder drohenden Verletzungshandlung. "
              "Art. 4, Art. 7 Nr. 2 Brüssel-Ia-VO gelten nicht (Art. 79 Abs. 2 lit. a GGV), wohl aber Art. 8 Nr. 1 Brüssel-Ia-VO (EuGH Nintendo)\n"
              "**V3 Reichweite** – Art. 83 Abs. 1 GGV: Zuständigkeit nach Art. 82 Abs. 1 bis 4 GGV erfasst Verletzungen in allen Mitgliedstaaten; "
              "Art. 83 Abs. 2 GGV: nach Art. 82 Abs. 5 GGV nur Verletzungen im Gerichtsstaat\n"
              "**V4 Örtliche Zuständigkeit** – § 63b S. 1 DesignG: wie bei einem deutschen Design, also § 12 ZPO, § 17 ZPO, § 32 ZPO; sonst "
              "allgemeiner Gerichtsstand des Klägers (§ 63b S. 2 DesignG)\n\n"
              "**B · Deutsches Design**\n"
              "**V5 Internationale Zuständigkeit** – Art. 4 Abs. 1 Brüssel-Ia-VO (Wohnsitz des Beklagten), Art. 7 Nr. 2 Brüssel-Ia-VO (Ort des "
              "schädigenden Ereignisses, nur für den Schaden im Inland); Beklagter außerhalb der Union: § 32 ZPO doppelfunktional; Gültigkeit "
              "ausschließlich in Deutschland (Art. 24 Nr. 4 Brüssel-Ia-VO)\n"
              "**V6 Sachliche Zuständigkeit** – Landgerichte ohne Rücksicht auf den Streitwert, ausschließlich (§ 52 Abs. 1 DesignG); Konzentration "
              "(§ 52 Abs. 2 DesignG)\n\n"
              "**C · Einstweilige Maßnahmen**\n"
              "**V7 Eilzuständigkeit** – Art. 90 Abs. 1 GGV: jedes Gericht eines Mitgliedstaats nach nationalem Recht, Wirkung im Gerichtsstaat; "
              "unionsweit nur das nach Art. 82 Abs. 1 bis 4 GGV zuständige Gericht (Art. 90 Abs. 3 GGV); deutsches Design Art. 35 Brüssel-Ia-VO\n\n"
              "**D · Anwendbares Recht**\n"
              "**V8 Sachrecht** – GGV zuerst (Art. 88 Abs. 1 GGV), im Übrigen nationales Recht einschließlich IPR (Art. 88 Abs. 2 GGV): Art. 8 Abs. 2 "
              "Rom-II-VO, Recht des Staates der ursprünglichen Verletzungshandlung (EuGH Nintendo); deutsches Design Art. 8 Abs. 1 Rom-II-VO "
              "(Schutzland); deutsches Recht über § 62a DesignG\n\n"
              "**⇒ Rechtsfolge:** Klage am Sitz des Beklagten für ein unionsweites Verbot; am Verletzungsort nur für den Gerichtsstaat. Verfahrensrecht "
              "des Gerichtsstaats (Art. 88 Abs. 3 GGV)\n\n"
              "**Klausurfallen:** Der unionsweite Antrag am Verletzungsort ist im Übrigen unzulässig. Ein ausländischer Rechtsinhaber verändert die "
              "Zuständigkeit nicht; es kommt auf den Beklagten an. Die Gerichte für Gemeinschaftsgeschmacksmuster in § 63 DesignG sind die "
              "Unionsgeschmacksmustergerichte nach neuer Terminologie.\n\n"
              "**In den Klausuren:** II/2018 Zusatzfrage (Verletzer in Frankreich, Verletzung in Deutschland), II/2019 (Lösung: Messe Frankfurt, Firmen "
              "aus China und Spanien), II/2020 (LG Frankfurt gegen französische A SA, unionsweiter Antrag), II/2021 (LG Hamburg gegen K Ltd. aus den "
              "USA), III/2022 (Gericht gegen Herrn Rossi in Aachen), II/2023 (unionsweites Verbot gegen die A GmbH in Düsseldorf).",
              concepts=["des_ggm_gericht", "des_designstreitsachen", "des_ggm_anwendbares_recht"],
              norms=["Art. 80 GGV", "Art. 81 GGV", "Art. 82 GGV", "Art. 83 GGV", "Art. 88 GGV", "Art. 90 GGV", "§ 52 DesignG", "§ 63 DesignG",
                     "§ 63b DesignG", "§ 62a DesignG"],
              cases=["des_eugh_nintendo"], abschnitt="Normenkette"),
        intro("d03d-1", "Definitionen",
              "**Unionsgeschmacksmustergericht:** nationales Gericht erster oder zweiter Instanz, das ein Mitgliedstaat für die Aufgaben der GGV "
              "benennt (Art. 80 Abs. 1 GGV); in Deutschland die Landgerichte, konzentriert nach Landesrecht (§ 63 Abs. 1, 2 DesignG)\n"
              "**Designstreitsache:** jede Klage, mit der ein Anspruch aus einem im DesignG geregelten Rechtsverhältnis geltend gemacht wird "
              "(Legaldefinition § 52 Abs. 1 DesignG)\n"
              "**Ansässig, niedergelassen:** Wohnsitz oder Sitz nach Art. 62, Art. 63 Brüssel-Ia-VO; Niederlassung ist eine auf Dauer angelegte "
              "Außenstelle mit eigener Geschäftsführung (Art. 79 Abs. 2 lit. c GGV stellt sie dem Wohnsitz gleich)\n"
              "**Verletzungsort (Art. 82 Abs. 5 GGV):** Mitgliedstaat, in dem die Verletzungshandlung begangen worden ist oder droht, bei einer "
              "Messeausstellung der Messestaat\n"
              "**Ursprüngliche Verletzungshandlung:** bei mehreren Handlungen eines Verletzers in mehreren Staaten die Handlung, aus der die übrigen "
              "hervorgehen, etwa das Einstellen eines Angebots (EuGH Nintendo zu Art. 8 Abs. 2 Rom-II-VO)\n"
              "**Rügelose Einlassung:** der Beklagte verhandelt zur Sache, ohne die Zuständigkeit zu rügen (Art. 26 Brüssel-Ia-VO über Art. 82 Abs. 4 "
              "lit. b GGV)",
              concepts=["des_ggm_gericht", "des_designstreitsachen", "des_ggm_anwendbares_recht"], cases=["des_eugh_nintendo"], abschnitt="Definitionen"),
        mc("d03d-2", "Verletzer in Frankreich", "Der Verletzer eines Unionsmusters hat seinen Sitz in Frankreich, die Verletzungshandlung geschieht in Deutschland. "
           "Wo erreicht der Inhaber in der Hauptsache ein unionsweites Verbot?",
           ["Vor dem Unionsgeschmacksmustergericht in Frankreich (Art. 82 Abs. 1, Art. 83 Abs. 1 GGV)",
            "Vor dem Landgericht am deutschen Verletzungsort (Art. 82 Abs. 5 GGV)",
            "Vor jedem Gericht nach Wahl des Klägers (Art. 7 Nr. 2 Brüssel-Ia-VO)",
            "Nur vor dem EUIPO in Alicante"], 0,
           ["**In Frankreich.** Unionsweit entscheidet das Gericht des Staates, in dem der Beklagte ansässig ist (Art. 82 Abs. 1 GGV, Art. 83 Abs. 1 "
            "GGV). Das deutsche Gericht ist nach Art. 82 Abs. 5 GGV zuständig, aber nur für Deutschland (Art. 83 Abs. 2 GGV). Art. 7 Nr. 2 "
            "Brüssel-Ia-VO gilt nicht (Art. 79 Abs. 2 lit. a GGV; RP1 II/2018)."],
           merke="Unionsweit: Beklagtensitz Art. 82 Abs. 1 GGV · Verletzungsort Art. 82 Abs. 5 GGV nur national (Art. 83 Abs. 2 GGV).",
           level=1, concepts=["des_ggm_gericht"], norms=["Art. 82 GGV", "Art. 83 GGV"], step=f"{UG}.4", abschnitt=DN),
        fall("d03d-3", "Unionsweiter Antrag in Frankfurt",
             "Die K Ltd. verklagt die A SA (Paris, keine Niederlassung außerhalb von Paris) beim Landgericht Frankfurt, weil A SA Tankeinsätze auch in "
             "Deutschland vertreibt. Sie beantragt ein Verbot „im Gebiet der Europäischen Union“.",
             "Ist das Landgericht Frankfurt für den ganzen Antrag zuständig?", False,
             ["**Nein!** Grundlage ist nur Art. 82 Abs. 5 GGV (Verletzung in Deutschland); die Zuständigkeit beschränkt sich auf Deutschland "
              "(Art. 83 Abs. 2 GGV). Für die übrige Union ist der Antrag unzulässig, es sei denn, A SA lässt sich rügelos ein (Art. 82 Abs. 4 lit. b "
              "GGV, Art. 26 Brüssel-Ia-VO; RP1 II/2020)."],
             merke="Verletzungsort: nur Gerichtsstaat; rügelose Einlassung öffnet die Union.",
             level=2, concepts=["des_ggm_gericht"], norms=["Art. 82 GGV", "Art. 83 GGV"], step=f"{UG}.4", abschnitt=DN),
        fall("d03d-4", "Beklagter in den USA",
             "Die A GmbH aus Hamburg klagt als Lizenznehmerin aus einem Unionsmuster der L SA (Paris) gegen die K Ltd. aus den USA, die keine "
             "Niederlassung in der Union hat und Trinkflaschen in der ganzen EU anbietet.",
             "Sind deutsche Gerichte international zuständig?", True,
             ["**Ja!** Hat der Beklagte weder Wohnsitz noch Niederlassung in der Union, sind die Gerichte des Mitgliedstaats zuständig, in dem der "
              "Kläger seinen Wohnsitz oder Sitz hat (Art. 82 Abs. 2 GGV). Kläger ist die A GmbH in Hamburg; der Sitz der Inhaberin ist gleichgültig. "
              "Die Zuständigkeit reicht unionsweit (Art. 83 Abs. 1 GGV; RP1 II/2021)."],
             merke="Beklagter außerhalb der Union: Klägersitz, Art. 82 Abs. 2 GGV, unionsweit.",
             level=2, concepts=["des_ggm_gericht", "des_lizenz"], norms=["Art. 82 GGV", "Art. 83 GGV"], step=f"{UG}.4", abschnitt=DN),
        mc("d03d-5", "Örtliche Zuständigkeit", "Deutsche Unionsgeschmacksmustergerichte sind international zuständig. Welche Norm bestimmt das örtlich zuständige Landgericht?",
           ["§ 63b DesignG: die Vorschriften für deutsche Designs, also §§ 12, 17, 32 ZPO, hilfsweise der allgemeine Gerichtsstand des Klägers",
            "Art. 82 Abs. 5 GGV unmittelbar", "§ 52 Abs. 1 DesignG: immer das Landgericht München I",
            "Art. 7 Nr. 2 Brüssel-Ia-VO"], 0,
           ["**§ 63b DesignG.** Die GGV regelt nur die internationale Zuständigkeit. Örtlich gilt, was für ein deutsches Design gälte: allgemeiner "
            "Gerichtsstand des Beklagten (§ 12 ZPO, § 17 ZPO) oder Tatort (§ 32 ZPO); fehlt beides, der allgemeine Gerichtsstand des Klägers "
            "(§ 63b S. 2 DesignG). Danach greift die Konzentration nach § 63 Abs. 2 DesignG."],
           merke="Örtlich: § 63b DesignG → ZPO; Konzentration § 63 Abs. 2 DesignG.",
           level=2, concepts=["des_ggm_gericht"], norms=["§ 63b DesignG", "§ 63 DesignG"], step=f"{UG}.4", abschnitt=DN),
        fall("d03d-6", "Streitgenossen",
             "Nintendo verklagt in Deutschland den deutschen Händler und dessen französischen Lieferanten aus Unionsmustern; der Lieferant beliefert "
             "den Händler.",
             "Kann das deutsche Gericht auch gegen den französischen Lieferanten unionsweit entscheiden?", True,
             ["**Ja!** Art. 8 Nr. 1 Brüssel-Ia-VO (Gerichtsstand der Streitgenossenschaft) ist von Art. 79 Abs. 2 lit. a GGV nicht ausgeschlossen. "
              "Das am Sitz eines Beklagten zuständige Gericht kann dann auch gegen den Mitbeklagten aus einem anderen Mitgliedstaat Maßnahmen für die "
              "ganze Union anordnen (EuGH Nintendo)."],
             merke="Streitgenossen: Art. 8 Nr. 1 Brüssel-Ia-VO bleibt anwendbar (EuGH Nintendo).",
             level=3, concepts=["des_ggm_gericht"], norms=["Art. 79 GGV", "Art. 82 GGV"], cases=["des_eugh_nintendo"], step=f"{UG}.4", abschnitt=DN),
        fall("d03d-7", "Deutsches Design gegen spanischen Hersteller",
             "Eine spanische Firma mit Produktion nur in Spanien will auf einer Messe in Frankfurt eine Brause ausstellen, die das deutsche Design DE1 "
             "der Mandantin verletzt.",
             "Sind deutsche Gerichte für die Klage aus DE1 zuständig?", True,
             ["**Ja!** Für das deutsche Design gilt die Brüssel-Ia-VO unmittelbar: Gerichtsstand der unerlaubten Handlung am Ort des drohenden "
              "Schadens in Deutschland (Art. 7 Nr. 2 Brüssel-Ia-VO), daneben Spanien als Wohnsitzstaat (Art. 4 Abs. 1 Brüssel-Ia-VO). Örtlich "
              "§ 32 ZPO, sachlich das Landgericht (§ 52 Abs. 1 DesignG; Lösung RP1 II/2019)."],
             merke="DE-Design: Art. 4 Abs. 1, Art. 7 Nr. 2 Brüssel-Ia-VO · § 32 ZPO · § 52 Abs. 1 DesignG.",
             level=2, concepts=["des_designstreitsachen"], norms=["§ 52 DesignG"], step=f"{VL}.7", abschnitt=DN),
        mc("d03d-8", "Anwendbares Recht", "Ein Verletzer bietet aus Deutschland über das Internet in mehreren Mitgliedstaaten an. Nach welchem Recht richten sich Schadensersatz und Auskunft aus dem Unionsmuster?",
           ["Nach dem Recht des Staates der ursprünglichen Verletzungshandlung, hier deutschem Recht (Art. 8 Abs. 2 Rom-II-VO)",
            "Nach dem Recht jedes Staates, in dem angeboten wird (Mosaik)", "Nach spanischem Recht als Sitz des EUIPO",
            "Nur nach der GGV"], 0,
           ["**Recht des Handlungsorts.** Art. 88 Abs. 2 GGV verweist auf das nationale Recht einschließlich IPR; Art. 8 Abs. 2 Rom-II-VO führt "
            "zum Recht des Staates, in dem die ursprüngliche Verletzungshandlung begangen wurde (EuGH Nintendo, Acacia/BMW). In Deutschland gelten "
            "dann über § 62a Nr. 1 DesignG § 42 Abs. 2 DesignG und § 46 DesignG."],
           merke="Folgeansprüche: Art. 88 Abs. 2 GGV · Art. 8 Abs. 2 Rom-II-VO · § 62a DesignG.",
           level=3, concepts=["des_ggm_anwendbares_recht"], norms=["Art. 88 GGV", "§ 62a DesignG"], cases=["des_eugh_nintendo", "des_eugh_acacia_bmw"],
           step=f"{UG}.5", abschnitt=DN),
        *fallkette("d03d-9", "Sitzbank-Tisch gegen die A GmbH (nach RP1 II/2023)",
            "Die M GmbH aus Mannheim hat Unionsmuster für eine Sitzbank-Tisch-Kombination. Die A GmbH mit Sitz in Düsseldorf verkauft die Möbel seit "
            "Mai 2023 nach Frankreich und vertreibt andere Produkte in fast allen Mitgliedstaaten. M will den Vertrieb möglichst unionsweit unterbinden.",
            [frage("Ist die Klage eine Unionsgeschmacksmusterstreitsache?", True,
                   ["**Ja!** Verletzungsklagen und Klagen wegen drohender Verletzung gehören ausschließlich vor die Unionsgeschmacksmustergerichte "
                    "(Art. 81 lit. a GGV); in Deutschland die Landgerichte (§ 63 Abs. 1 DesignG)."],
                   merke="Art. 81 lit. a GGV · § 63 Abs. 1 DesignG.", titel="Streitsache"),
             frage("Sind deutsche Gerichte für ein unionsweites Verbot zuständig?", True,
                   ["**Ja!** Die A GmbH ist in Deutschland ansässig (Art. 82 Abs. 1 GGV). Diese Zuständigkeit erfasst Verletzungen in allen "
                    "Mitgliedstaaten (Art. 83 Abs. 1 GGV), also auch die Verkäufe in Frankreich."],
                   merke="Beklagtensitz → unionsweit, Art. 82 Abs. 1, Art. 83 Abs. 1 GGV.", titel="International", level=2),
             frage("Welches Landgericht ist örtlich zuständig?", 1,
                   ["**LG Düsseldorf.** Örtlich gilt § 63b S. 1 DesignG mit § 12 ZPO, § 17 ZPO (Sitz der A GmbH); das Landgericht Düsseldorf ist "
                    "zugleich das für Nordrhein-Westfalen bestimmte Gericht (§ 63 Abs. 2 DesignG)."],
                   optionen=["LG Mannheim als Sitz der Klägerin", "LG Düsseldorf", "LG München I", "Jedes Landgericht nach Wahl"],
                   merke="Örtlich: § 63b DesignG · § 12, § 17 ZPO.", titel="Örtlich", level=2),
             frage("Wie wäre es, wenn M in Mannheim am Ort eines dortigen Verkaufs klagt – bekäme sie dort ein unionsweites Verbot?", False,
                   ["**Nein!** Am Verletzungsort ist das Gericht nur nach Art. 82 Abs. 5 GGV zuständig und nur für Verletzungen in Deutschland "
                    "(Art. 83 Abs. 2 GGV). Für die Union bleibt der Sitz der Beklagten maßgeblich."],
                   abwandlung="M klagt in Mannheim, weil die A GmbH dort einmal verkauft hat.",
                   merke="Gerichtsstand der Verletzung: nur nationale Reichweite.", titel="Abwandlung Verletzungsort"),
            ],
            abschnitt=KF, level=2, concepts=["des_ggm_gericht"], norms=["Art. 81 GGV", "Art. 82 GGV", "Art. 83 GGV", "§ 63 DesignG"], step=f"{UG}.4"),
    ]),
    # ================================================================== Eilrechtsschutz und Grenzbeschlagnahme
    dict(id="d03e", titel="§§ 935, 940 ZPO, Art. 90 GGV, §§ 55 bis 57a DesignG: Eilrechtsschutz und Grenzbeschlagnahme", einheiten=[
        intro("d03e-0", "Prüfungsschema",
              "**AGL:** einstweilige Verfügung § 935 ZPO, § 940 ZPO i.V.m. § 42 Abs. 1 DesignG bzw. Art. 89 Abs. 1 GGV, Art. 90 Abs. 1 GGV; "
              "Grenzbeschlagnahme Art. 17 VO (EU) Nr. 608/2013, Art. 23 VO (EU) Nr. 608/2013 i.V.m. § 57a DesignG; nationale Beschlagnahme § 55 "
              "Abs. 1 DesignG\n\n"
              "**A · Einstweilige Verfügung: Zulässigkeit**\n"
              "**V1 Zuständigkeit** – Gericht der Hauptsache (§ 937 Abs. 1 ZPO), Landgericht (§ 52 Abs. 1 DesignG, § 63 Abs. 1 DesignG); Unionsmuster "
              "bei jedem Gericht eines Mitgliedstaats (Art. 90 Abs. 1 GGV), unionsweit nur nach Art. 82 Abs. 1 bis 4 GGV (Art. 90 Abs. 3 GGV)\n"
              "**V2 Antrag und Glaubhaftmachung** – § 920 Abs. 1, 2 ZPO i.V.m. § 936 ZPO; Mittel § 294 ZPO (eidesstattliche Versicherung, Fotos, "
              "Registerauszug)\n\n"
              "**B · Begründetheit**\n"
              "**V3 Verfügungsanspruch** – Unterlassung (§ 42 Abs. 1 DesignG, Art. 89 Abs. 1 GGV); Sicherung der Vernichtung durch Sequestration "
              "(§ 43 DesignG, § 938 Abs. 2 ZPO); Auskunft nur bei offensichtlicher Verletzung (§ 46 Abs. 7 DesignG)\n"
              "**V4 Verfügungsgrund** – Dringlichkeit; das DesignG enthält keine Dringlichkeitsvermutung; zögerliches Vorgehen widerlegt sie selbst\n"
              "**V5 Nichtigkeitseinwand erfolglos** – im Eilverfahren ohne Widerklage zulässig (§ 52a S. 2 DesignG, Art. 90 Abs. 2 GGV)\n\n"
              "**C · Verfahren**\n"
              "**V6 Abmahnung** – vermeidet die Kostenfolge des sofortigen Anerkenntnisses (§ 93 ZPO); Kostenerstattung § 677 BGB, § 683 S. 1 BGB, "
              "§ 670 BGB\n"
              "**V7 Beschluss und Vollziehung** – ohne mündliche Verhandlung in dringenden Fällen (§ 937 Abs. 2 ZPO); Zustellung im Parteibetrieb "
              "(§ 922 Abs. 2 ZPO i.V.m. § 936 ZPO), binnen eines Monats (§ 929 Abs. 2 ZPO · § 222 Abs. 1 ZPO i.V.m. § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · "
              "§ 222 Abs. 2 ZPO); am Messestand (§ 177 ZPO)\n"
              "**V8 Rechtsbehelfe, Risiko** – Widerspruch (§ 924 ZPO), Frist zur Hauptsacheklage (§ 926 ZPO); verschuldensunabhängiger Schadensersatz "
              "bei ungerechtfertigter Verfügung (§ 945 ZPO)\n\n"
              "**D · Grenzbeschlagnahme**\n"
              "**V9 Anwendungsbereich** – Waren unter zollamtlicher Überwachung beim Verbringen in das Zollgebiet der Union (Art. 1 Abs. 1 VO (EU) "
              "Nr. 608/2013); national nur, soweit die Verordnung nicht gilt, bei offensichtlicher Verletzung und gegen Sicherheit (§ 55 Abs. 1 S. 1 "
              "DesignG)\n"
              "**V10 Antrag auf Tätigwerden** – bei der Generalzolldirektion (§ 57 Abs. 1 S. 1 DesignG i.V.m. § 57a DesignG); Unionsantrag nur für "
              "Rechte mit unionsweiter Wirkung (Art. 4 VO (EU) Nr. 608/2013), also das Unionsmuster; Entscheidung binnen 30 Arbeitstagen\n"
              "**V11 Aussetzung und Vernichtung** – Aussetzung der Überlassung bei Verdacht (Art. 17 VO (EU) Nr. 608/2013); Vernichtung ohne "
              "Verletzungsprozess, wenn der Rechtsinhaber binnen zehn Arbeitstagen bestätigt und der Besitzer zustimmt oder schweigt (Art. 23 Abs. 1 "
              "VO (EU) Nr. 608/2013); sonst muss der Rechtsinhaber ein Verletzungsverfahren einleiten (Art. 23 Abs. 3 VO (EU) Nr. 608/2013)\n"
              "**V12 Haftung** – Art. 28 VO (EU) Nr. 608/2013; national § 56 Abs. 5 DesignG\n\n"
              "**⇒ Rechtsfolge:** Unterlassungsgebot mit Ordnungsmittelandrohung (§ 890 ZPO), Sequestration; Zoll: Aussetzung, Vernichtung\n\n"
              "**Klausurfallen:** Unbekannte Gegner sind beim Zoll kein Problem, bei der einstweiligen Verfügung schon (Bezeichnung der Partei). "
              "Gegen Firmen aus dem Binnenmarkt (Spanien) hilft der Zoll nicht. Eine Unterlassungserklärung muss strafbewehrt sein, um die "
              "Wiederholungsgefahr zu beseitigen.\n\n"
              "**In den Klausuren:** II/2019 (Lösung: Unionsantrag gegen die chinesischen Firmen, einstweilige Verfügung gegen die spanische Firma), "
              "III/2021 (Abmahnung, Kosten), III/2022 (Reaktion auf die Abmahnung, Kosten), II/2023 (Einwendungen im Verfügungsverfahren), I/2019 "
              "(Abmahnung mit Wochenfrist).",
              concepts=["des_zollbeschlagnahme", "des_unterlassung", "des_vermutung_rechtsgueltigkeit"],
              norms=["§ 42 DesignG", "§ 43 DesignG", "§ 46 DesignG", "§ 52a DesignG", "§ 55 DesignG", "§ 56 DesignG", "§ 57 DesignG", "§ 57a DesignG",
                     "Art. 89 GGV", "Art. 90 GGV"],
              abschnitt="Normenkette"),
        intro("d03e-1", "Definitionen",
              "**Verfügungsanspruch:** der materielle Anspruch, dessen Sicherung begehrt wird, hier der Unterlassungsanspruch (§ 935 ZPO, § 940 ZPO)\n"
              "**Verfügungsgrund:** Dringlichkeit; der Antragsteller kann das Hauptsacheverfahren nicht abwarten und hat selbst zügig gehandelt\n"
              "**Glaubhaftmachung:** Nachweis überwiegender Wahrscheinlichkeit mit präsenten Beweismitteln einschließlich eidesstattlicher "
              "Versicherung (§ 294 ZPO)\n"
              "**Sequestration:** Verwahrung der Verletzungsgegenstände durch einen Gerichtsvollzieher zur Sicherung des Vernichtungsanspruchs "
              "(§ 938 Abs. 2 ZPO)\n"
              "**Vollziehung:** bei der Beschlussverfügung die Zustellung im Parteibetrieb binnen eines Monats (§ 929 Abs. 2 ZPO, § 922 Abs. 2 ZPO, "
              "§ 936 ZPO)\n"
              "**Abmahnung:** Aufforderung an den Verletzer, binnen Frist eine strafbewehrte Unterlassungserklärung abzugeben; inhaltlich: Schutzrecht, "
              "Verletzungshandlung, Aufforderung, Frist, Androhung gerichtlicher Schritte (RP1 III/2021)\n"
              "**Unionsantrag:** Antrag auf Tätigwerden der Zollbehörden mehrerer oder aller Mitgliedstaaten, nur für Rechte mit unionsweiter Wirkung "
              "(Art. 2 Nr. 11, Art. 4 VO (EU) Nr. 608/2013)\n"
              "**Offensichtliche Rechtsverletzung:** so eindeutig, dass eine Fehlentscheidung kaum möglich ist; Voraussetzung der nationalen "
              "Beschlagnahme (§ 55 Abs. 1 DesignG) und der Auskunft im Eilverfahren (§ 46 Abs. 7 DesignG)",
              concepts=["des_zollbeschlagnahme", "des_auskunft"], abschnitt="Definitionen"),
        mc("d03e-2", "Vollziehungsfrist", "Binnen welcher Frist muss eine Beschlussverfügung vollzogen werden, und wie?",
           ["Ein Monat ab Zustellung an den Antragsteller, durch Zustellung im Parteibetrieb (§ 929 Abs. 2 ZPO, § 922 Abs. 2 ZPO, § 936 ZPO)",
            "Zwei Wochen ab Erlass, durch Zustellung von Amts wegen", "Drei Monate ab Erlass, durch Gerichtsvollzieher",
            "Keine Frist; der Beschluss wirkt ab Erlass"], 0,
           ["**Ein Monat, Parteizustellung.** Die Vollziehung ist unstatthaft, wenn seit der Zustellung an den Antragsteller ein Monat verstrichen "
            "ist (§ 929 Abs. 2 ZPO i.V.m. § 936 ZPO). Die Beschlussverfügung muss der Antragsteller selbst zustellen lassen (§ 922 Abs. 2 ZPO). "
            "Berechnung § 222 Abs. 1 ZPO i.V.m. § 187 Abs. 1 BGB, § 188 Abs. 2 BGB; Verschiebung § 222 Abs. 2 ZPO."],
           merke="Vollziehung: § 929 Abs. 2 ZPO · § 222 Abs. 1 ZPO, § 187, § 188 BGB · § 222 Abs. 2 ZPO.",
           level=2, norms=["§ 42 DesignG"], abschnitt=DN),
        fall("d03e-3", "Nichtigkeitseinwand im Eilverfahren",
             "Die A GmbH verteidigt sich gegen eine einstweilige Verfügung aus einem Unionsmuster mit dem Einwand, das Muster sei mangels Neuheit "
             "nichtig. Eine Widerklage hat sie nicht erhoben.",
             "Darf das Gericht den Einwand berücksichtigen?", True,
             ["**Ja!** In Verfahren über einstweilige Maßnahmen ist der Einwand der Nichtigkeit auch ohne Widerklage zulässig (Art. 90 Abs. 2 S. 1 GGV). "
              "Für deutsche Designs gilt dasselbe (§ 52a S. 2 DesignG). Im Hauptsacheverfahren bräuchte die A GmbH dagegen eine Widerklage "
              "(Art. 85 Abs. 1 S. 2 GGV, § 52a S. 1 DesignG)."],
             merke="Eilverfahren: Nichtigkeitseinwand frei, Art. 90 Abs. 2 GGV, § 52a S. 2 DesignG.",
             level=1, concepts=["des_vermutung_rechtsgueltigkeit"], norms=["Art. 90 GGV", "§ 52a DesignG"], abschnitt=DN),
        fall("d03e-4", "Zoll gegen Ware aus Spanien",
             "Eine spanische Firma mit Produktionsstätten nur in Spanien will verletzende Brausen per Lkw zur Messe nach Frankfurt bringen.",
             "Kann die Mandantin die Ware mit einem Antrag nach der VO (EU) Nr. 608/2013 an der Grenze stoppen?", False,
             ["**Nein!** Die Verordnung erfasst Waren, die in das Zollgebiet der Union verbracht werden oder unter zollamtlicher Überwachung stehen "
              "(Art. 1 Abs. 1 VO (EU) Nr. 608/2013); Binnenmarktware fällt nicht darunter. § 55 Abs. 1 S. 2 DesignG greift im Verkehr mit "
              "Mitgliedstaaten nur, soweit Kontrollen stattfinden. Gegen die spanische Firma bleibt die einstweilige Verfügung (Lösung RP1 II/2019)."],
             merke="Zoll nur gegen Drittlandsware; Binnenmarkt: einstweilige Verfügung.",
             level=2, concepts=["des_zollbeschlagnahme"], norms=["§ 55 DesignG"], abschnitt=DN),
        mc("d03e-5", "Vereinfachtes Vernichtungsverfahren", "Der Zoll hat die Überlassung verdächtiger Ware ausgesetzt. Wann darf er sie ohne Verletzungsprozess vernichten?",
           ["Wenn der Rechtsinhaber binnen zehn Arbeitstagen die Verletzung bestätigt und zustimmt und der Besitzer zustimmt oder schweigt",
            "Sofort nach der Aussetzung, ohne Beteiligung des Besitzers", "Nur nach einem rechtskräftigen Urteil",
            "Wenn der Rechtsinhaber eine Sicherheit leistet"], 0,
           ["**Bestätigung binnen zehn Arbeitstagen und Zustimmung.** Art. 23 Abs. 1 VO (EU) Nr. 608/2013: Der Rechtsinhaber bestätigt schriftlich "
            "die Verletzung und stimmt der Vernichtung zu; der Besitzer stimmt zu oder schweigt, Schweigen gilt als Zustimmung. Widerspricht er, "
            "muss der Rechtsinhaber binnen zehn Arbeitstagen ein Verletzungsverfahren einleiten (Art. 23 Abs. 3 VO (EU) Nr. 608/2013)."],
           merke="Vernichtung: Art. 23 Abs. 1 VO (EU) Nr. 608/2013 · zehn Arbeitstage · Schweigen = Zustimmung.",
           level=2, concepts=["des_zollbeschlagnahme"], norms=["§ 57a DesignG"], abschnitt=DN),
        fall("d03e-6", "Dringlichkeit am letzten Messetag",
             "Die Mandantin entdeckt eine Verletzung eine Stunde vor Ende der Messe. Sie überlegt drei Monate, bevor sie eine einstweilige Verfügung "
             "beantragt.",
             "Besteht dann noch ein Verfügungsgrund?", False,
             ["**Nein**, regelmäßig nicht. Das DesignG kennt keine Dringlichkeitsvermutung; der Antragsteller muss die Eilbedürftigkeit glaubhaft machen. "
              "Wer nach Kenntnis von Verletzung und Verletzer lange zuwartet, widerlegt die Dringlichkeit selbst; die Gerichte setzen meist eine "
              "Grenze von etwa einem bis zwei Monaten. Am letzten Messetag kommt die Verfügung ohnehin zu spät (Lösung RP1 II/2019)."],
             merke="Verfügungsgrund: zügig handeln; langes Zuwarten widerlegt die Dringlichkeit.",
             level=2, norms=["§ 42 DesignG"], abschnitt=DN),
        mc("d03e-7", "Reaktion auf die Abmahnung", "Herr Rossi hat ein Unionsmuster nach eigenem Eingeständnis nachgeahmt; das Muster ist rechtsbeständig. Wie reagiert er kostengünstig auf die Abmahnung?",
           ["Strafbewehrte Unterlassungserklärung abgeben, gegebenenfalls modifiziert und nicht weiter als die Verletzung",
            "Nicht reagieren und die Klage abwarten", "Eine Unterlassungserklärung ohne Vertragsstrafe abgeben",
            "Sofort eine negative Feststellungsklage erheben"], 0,
           ["**Strafbewehrte Unterlassungserklärung.** Nur sie beseitigt die Wiederholungsgefahr und verhindert Klage oder Verfügung mit höheren "
            "Kosten. Er muss nur so weit unterschreiben, wie die Verletzung reicht; überschießende Formulierungen wie „ähnlich“ kann er "
            "streichen. Die berechtigte Abmahnung muss er nach § 677 BGB, § 683 S. 1 BGB, § 670 BGB bezahlen (RP1 III/2022)."],
           merke="Wiederholungsgefahr entfällt nur durch strafbewehrte Unterlassungserklärung.",
           level=2, concepts=["des_unterlassung"], norms=["§ 42 DesignG"], abschnitt=DN),
        *fallkette("d03e-8", "Messe Bad & Dusche (nach RP1 II/2019)",
            "Die Mandantin hat das Unionsmuster EU1 und das deutsche Design DE1. Unbekannte chinesische Firmen wollen die Kopie COPY1 in sechs Wochen "
            "auf der Frankfurter Messe ausstellen, eine spanische Firma ebenfalls. Die Mandantin will den Messeauftritt verhindern.",
            [frage("Kann die Mandantin gegen die chinesischen Firmen einen Unionsantrag stellen?", True,
                   ["**Ja!** Der Unionsantrag steht für Rechte mit unionsweiter Wirkung offen (Art. 4 VO (EU) Nr. 608/2013); EU1 ist ein solches Recht. "
                    "Er erfasst die Einfuhr über jeden Hafen der Union. Antrag bei der Generalzolldirektion (§ 57 Abs. 1 S. 1 DesignG i.V.m. § 57a DesignG)."],
                   merke="Unionsantrag nur aus dem Unionsmuster; DE1 nur nationaler Antrag.", titel="Unionsantrag", norms=["§ 57a DesignG"]),
             frage("Welches Risiko birgt der Zeitplan?", 2,
                   ["**Die Entscheidung über den Antrag.** Der Zoll entscheidet binnen 30 Arbeitstagen; sechs Wochen reichen nur knapp. Deshalb sofort "
                    "einen vollständigen Antrag stellen und die einstweilige Verfügung als Auffanglösung vorbereiten."],
                   optionen=["Die Vollziehungsfrist von einem Monat", "Die Widerspruchsfrist von zwei Wochen nach § 56 Abs. 1 DesignG",
                             "Die Entscheidungsfrist des Zolls von 30 Arbeitstagen", "Die Verjährung"],
                   merke="Zoll: 30 Arbeitstage bis zur Entscheidung über den Antrag.", titel="Zeitplan", level=2),
             frage("Gegen die spanische Firma beantragt die Mandantin eine einstweilige Verfügung. Muss sie die Firma vorher abmahnen?", False,
                   ["**Nein**, eine Pflicht besteht nicht. Ohne Abmahnung droht aber die Kostenlast bei sofortigem Anerkenntnis (§ 93 ZPO), und das "
                    "Gericht entscheidet ohne mündliche Verhandlung nur in dringenden Fällen (§ 937 Abs. 2 ZPO), regelmäßig nach Gelegenheit zur "
                    "Stellungnahme."],
                   merke="Abmahnung: keine Pflicht, aber Kostenrisiko § 93 ZPO.", titel="Abmahnung", level=2),
             frage("Kann das Gericht die Herausgabe der Ausstellungsstücke an einen Gerichtsvollzieher anordnen?", True,
                   ["**Ja!** Die Sequestration sichert den Vernichtungsanspruch (§ 43 Abs. 1 DesignG; Unionsmuster über § 62a Nr. 1 DesignG) und ist als "
                    "Inhalt der Verfügung zulässig (§ 938 Abs. 2 ZPO). Zugestellt und vollzogen wird am Messestand (§ 177 ZPO)."],
                   merke="Sequestration: § 938 Abs. 2 ZPO zur Sicherung von § 43 DesignG.", titel="Sequestration", norms=["§ 43 DesignG"]),
             frage("Haftet die Mandantin, wenn sich die Verfügung später als von Anfang an ungerechtfertigt erweist?", True,
                   ["**Ja**, verschuldensunabhängig auf Ersatz des Vollziehungsschadens (§ 945 ZPO). Das ist das Hauptrisiko neben den Kosten."],
                   merke="Risiko der Verfügung: § 945 ZPO, verschuldensunabhängig.", titel="Risiko"),
            ],
            abschnitt=KF, level=2, concepts=["des_zollbeschlagnahme", "des_unterlassung"], norms=["Art. 90 GGV"]),
    ]),
    # ================================================================== Lizenz
    dict(id="d03f", titel="§ 31 DesignG, Art. 32, 33 GGV: Lizenz und Rechtsübergang", einheiten=[
        intro("d03f-0", "Prüfungsschema",
              "**AGL:** Klage des Lizenznehmers aus § 42 DesignG i.V.m. § 31 Abs. 3 DesignG bzw. Art. 19 Abs. 1 GGV, Art. 89 Abs. 1 GGV i.V.m. "
              "Art. 32 Abs. 3 GGV; Beitritt zur Klage des Inhabers § 31 Abs. 4 DesignG, Art. 32 Abs. 4 GGV; Ansprüche des Inhabers gegen den "
              "Lizenznehmer § 31 Abs. 2 DesignG, Art. 32 Abs. 2 GGV\n\n"
              "**A · Lizenz**\n"
              "**V1 Wirksame Lizenz** – ausschließlich oder nicht ausschließlich, für das ganze Gebiet oder einen Teil (§ 31 Abs. 1 DesignG, "
              "Art. 32 Abs. 1 GGV); Sukzessionsschutz für ältere Lizenzen (§ 31 Abs. 5 DesignG)\n\n"
              "**B · Prozessführungsbefugnis**\n"
              "**V2 Zustimmung des Inhabers** – jeder Lizenznehmer klagt mit Zustimmung (§ 31 Abs. 3 S. 1 DesignG; Art. 32 Abs. 3 S. 1 GGV: „sofern "
              "im Lizenzvertrag nichts anderes bestimmt ist“); der Lizenzvertrag kann die Klagebefugnis selbst einräumen\n"
              "**V3 Ausschließlicher Lizenznehmer ohne Zustimmung** – wenn der Inhaber nach Aufforderung nicht binnen angemessener Frist selbst "
              "klagt (§ 31 Abs. 3 S. 2 DesignG, Art. 32 Abs. 3 S. 2 GGV)\n"
              "**V4 Registereintragung** – Wirkung der Lizenz gegenüber Dritten erst mit Eintragung (Art. 33 Abs. 1 GGV); für die Verletzungsklage "
              "des Lizenznehmers nicht erforderlich (EuGH Thomas Philipps)\n\n"
              "**C · Anspruch**\n"
              "**V5 Verletzung** – wie § 42 DesignG, Art. 19 GGV (Kapitel d03b)\n"
              "**V6 Eigener Schaden** – im eigenen Verfahren nach Art. 32 Abs. 3 GGV kann der Lizenznehmer seinen Schaden geltend machen (EuGH Thomas "
              "Philipps); im Verfahren des Inhabers durch Beitritt (§ 31 Abs. 4 DesignG: als Streitgenosse; Art. 32 Abs. 4 GGV)\n\n"
              "**D · Rechtsübergang**\n"
              "**V7 Übertragung** – deutsches Design formfrei übertragbar (§ 29 Abs. 1 DesignG), Eintragung auf Antrag (§ 29 Abs. 3 DesignG), "
              "legitimiert ist der eingetragene Inhaber (§ 1 Nr. 5 DesignG, § 8 DesignG); Unionsmuster: schriftlich und von beiden Parteien "
              "unterzeichnet, sonst nichtig (Art. 28 Abs. 1 GGV); im Übrigen das Recht des Mitgliedstaats nach Art. 27 GGV (Sitz laut Register, "
              "Art. 27 Abs. 2 GGV); Rechte aus der Eintragung erst nach Eintragung des Übergangs (Art. 28 Abs. 6 GGV)\n\n"
              "**⇒ Rechtsfolge:** Der Lizenznehmer klagt im eigenen Namen auf Unterlassung und eigenen Schaden; der Inhaber kann bei Vertragsverstößen "
              "aus dem Schutzrecht gegen den Lizenznehmer vorgehen (§ 31 Abs. 2 DesignG, Art. 32 Abs. 2 GGV)\n\n"
              "**Klausurfallen:** Die Klagebefugnis aus dem Lizenzvertrag ist die „Zustimmung“; auch der einfache Lizenznehmer klagt dann. Der Sitz "
              "des Lizenzgebers bestimmt nicht die Zuständigkeit (Kapitel d03d). Das neue Recht verlangt Schriftform für die Übertragung des "
              "eingetragenen Unionsmusters.\n\n"
              "**In den Klausuren:** II/2021 (einfache EU-weite Lizenz mit Klagebefugnis, eingetragen und nicht eingetragen, Schadensersatz, LG Hamburg), "
              "II/2022 (Kauf eines Unionsmusters, Form, Antragsbefugnis des Erwerbers), II/2023 (Lizenzvergabe in anderen Mitgliedstaaten).",
              concepts=["des_lizenz"], norms=["§ 31 DesignG", "§ 29 DesignG", "§ 8 DesignG", "Art. 27 GGV", "Art. 28 GGV", "Art. 32 GGV", "Art. 33 GGV"],
              cases=["des_eugh_thomas_philipps"], abschnitt="Normenkette"),
        intro("d03f-1", "Definitionen",
              "**Ausschließliche Lizenz:** Nutzungsrecht unter Ausschluss Dritter und, wenn vereinbart, des Inhabers selbst (§ 31 Abs. 1 S. 2 "
              "DesignG, Art. 32 Abs. 1 S. 2 GGV)\n"
              "**Einfache (nicht ausschließliche) Lizenz:** Nutzungsrecht neben dem Inhaber und weiteren Lizenznehmern (§ 31 Abs. 1 S. 2 DesignG)\n"
              "**Zustimmung:** Einverständnis des Inhabers mit der Klage des Lizenznehmers, im Einzelfall oder vorab im Lizenzvertrag (§ 31 Abs. 3 "
              "S. 1 DesignG, Art. 32 Abs. 3 S. 1 GGV)\n"
              "**Beitritt:** Eintritt des Lizenznehmers in die Verletzungsklage des Inhabers, um den eigenen Schaden geltend zu machen (§ 31 Abs. 4 "
              "DesignG: als Streitgenosse; Art. 32 Abs. 4 GGV)\n"
              "**Wirkung gegenüber Dritten:** Lizenz, Übertragung und dingliche Rechte am Unionsmuster wirken in allen Mitgliedstaaten erst mit "
              "Eintragung, außer gegenüber bösgläubigen Erwerbern (Art. 33 Abs. 1 GGV)\n"
              "**Sukzessionsschutz:** Rechtsübergang oder neue Lizenz berühren früher erteilte Lizenzen nicht (§ 31 Abs. 5 DesignG)",
              concepts=["des_lizenz"], cases=["des_eugh_thomas_philipps"], abschnitt="Definitionen"),
        mc("d03f-2", "Klagebefugnis des einfachen Lizenznehmers", "Unter welcher Voraussetzung kann ein einfacher Lizenznehmer aus einem Unionsmuster Verletzungsklage erheben?",
           ["Mit Zustimmung des Inhabers, die auch im Lizenzvertrag erteilt sein kann (Art. 32 Abs. 3 S. 1 GGV)",
            "Nie; nur der ausschließliche Lizenznehmer darf klagen", "Erst wenn der Inhaber nach Aufforderung nicht klagt",
            "Nur wenn die Lizenz im Register eingetragen ist"], 0,
           ["**Mit Zustimmung.** Art. 32 Abs. 3 S. 1 GGV (ebenso § 31 Abs. 3 S. 1 DesignG) lässt jeden Lizenznehmer mit Zustimmung des Inhabers "
            "klagen, „sofern im Lizenzvertrag nichts anderes bestimmt ist“. Die Untätigkeit des Inhabers nach Aufforderung hilft nur dem "
            "ausschließlichen Lizenznehmer (S. 2). Die Eintragung ist keine Voraussetzung (EuGH Thomas Philipps)."],
           merke="Lizenznehmer klagt mit Zustimmung (Art. 32 Abs. 3 S. 1 GGV); ausschließlicher auch nach Fristablauf (S. 2).",
           level=1, concepts=["des_lizenz"], norms=["Art. 32 GGV", "§ 31 DesignG"], cases=["des_eugh_thomas_philipps"], step=f"{UG}.2", abschnitt=DN),
        fall("d03f-3", "Ausschließlicher Lizenznehmer ohne Zustimmung",
             "Die B GmbH ist ausschließliche Lizenznehmerin an einem deutschen Design. Sie fordert den Inhaber auf, gegen einen Nachahmer zu klagen; "
             "der Inhaber reagiert zwei Monate nicht. Eine Klageklausel enthält der Vertrag nicht.",
             "Darf die B GmbH selbst klagen?", True,
             ["**Ja!** Der Inhaber einer ausschließlichen Lizenz braucht keine Zustimmung, wenn der Rechtsinhaber nach Aufforderung nicht binnen "
              "angemessener Frist selbst ein Verletzungsverfahren anhängig macht (§ 31 Abs. 3 S. 2 DesignG). Was angemessen ist, hängt vom Einzelfall "
              "ab; für das Unionsmuster gilt Art. 32 Abs. 3 S. 2 GGV."],
             merke="Ausschließlicher Lizenznehmer: Aufforderung + angemessene Frist (§ 31 Abs. 3 S. 2 DesignG).",
             level=2, concepts=["des_lizenz"], norms=["§ 31 DesignG"], step=f"{VL}.1", abschnitt=DN),
        fall("d03f-4", "Nicht eingetragene Lizenz",
             "Die A GmbH hat eine einfache, EU-weite Lizenz an einem Unionsmuster; der Vertrag erlaubt ihr, im eigenen Namen zu klagen. Die Lizenz ist "
             "nicht im Register eingetragen. Ein Wettbewerber wendet ein, Art. 33 Abs. 1 GGV stehe der Klage entgegen.",
             "Kann die A GmbH trotzdem auf Unterlassung klagen?", True,
             ["**Ja!** Art. 33 Abs. 1 GGV regelt die Wirkung der Lizenz gegenüber Dritten, die Rechte am Muster erwerben; er schützt nicht den "
              "Verletzer. Der Lizenznehmer kann deshalb auch ohne Eintragung klagen (EuGH Thomas Philipps, zur früheren Fassung). Die Klagebefugnis "
              "folgt aus dem Vertrag (Art. 32 Abs. 3 S. 1 GGV; RP1 II/2021)."],
             merke="Eintragung der Lizenz ist keine Klagevoraussetzung (EuGH Thomas Philipps).",
             level=2, concepts=["des_lizenz"], norms=["Art. 33 GGV", "Art. 32 GGV"], cases=["des_eugh_thomas_philipps"], step=f"{UG}.2", abschnitt=DN),
        mc("d03f-5", "Schaden des Lizenznehmers", "Wie macht ein Lizenznehmer den eigenen Schaden geltend, wenn der Inhaber des Unionsmusters selbst klagt?",
           ["Er tritt der Klage des Inhabers bei (Art. 32 Abs. 4 GGV)", "Gar nicht; der Schaden steht nur dem Inhaber zu",
            "Nur durch Abtretung an den Inhaber", "Durch eine Widerklage"], 0,
           ["**Durch Beitritt.** Jeder Lizenznehmer kann der Verletzungsklage des Inhabers beitreten, um Ersatz seines Schadens zu verlangen "
            "(Art. 32 Abs. 4 GGV; § 31 Abs. 4 DesignG: als Streitgenosse). Klagt der Lizenznehmer selbst nach Art. 32 Abs. 3 GGV, kann er den "
            "eigenen Schaden dort geltend machen (EuGH Thomas Philipps)."],
           merke="Eigener Schaden: Beitritt Art. 32 Abs. 4 GGV, § 31 Abs. 4 DesignG oder eigene Klage.",
           level=1, concepts=["des_lizenz", "des_schadensersatz"], norms=["Art. 32 GGV", "§ 31 DesignG"], cases=["des_eugh_thomas_philipps"],
           step=f"{UG}.2", abschnitt=DN),
        fall("d03f-6", "Qualitätsklausel",
             "Ein Lizenzvertrag über ein deutsches Design schreibt eine bestimmte Materialqualität vor. Der Lizenznehmer stellt billigere Ware her "
             "und verkauft sie.",
             "Kann der Inhaber aus dem Design gegen den Lizenznehmer vorgehen?", True,
             ["**Ja!** Verstößt der Lizenznehmer gegen eine Bestimmung über die Qualität der hergestellten Erzeugnisse, kann der Inhaber die Rechte aus "
              "dem eingetragenen Design gegen ihn geltend machen (§ 31 Abs. 2 Nr. 5 DesignG; Art. 32 Abs. 2 lit. d GGV), also auch Unterlassung nach "
              "§ 42 DesignG, nicht nur Vertragsansprüche."],
             merke="§ 31 Abs. 2 DesignG: Dauer, Form, Erzeugnisse, Gebiet, Qualität – Verstoß = Verletzung.",
             level=2, concepts=["des_lizenz"], norms=["§ 31 DesignG", "Art. 32 GGV"], step=f"{VL}.1", abschnitt=DN),
        *fallkette("d03f-7", "Trageschlaufe (nach RP1 II/2021)",
            "Die A GmbH (Hamburg) hat eine nicht ausschließliche EU-weite Lizenz am Unionsmuster der L SA (Paris) für eine Trageschlaufe. Eine Klausel des "
            "Vertrags erlaubt ihr, Verletzungsverfahren im eigenen Namen anhängig zu machen. Die K Ltd. aus den USA bietet ähnliche Schlaufen in der "
            "ganzen EU an.",
            [frage("Ist die A GmbH trotz einfacher Lizenz klagebefugt?", True,
                   ["**Ja!** Der Lizenzvertrag bestimmt die Klagebefugnis ausdrücklich; das ist die Zustimmung im Sinne von Art. 32 Abs. 3 S. 1 GGV."],
                   merke="Vertragliche Klageklausel = Zustimmung.", titel="Klagebefugnis"),
             frage("Ändert sich etwas, wenn die Lizenz nicht im Register eingetragen ist?", False,
                   ["**Nein!** Die Eintragung (Art. 33 Abs. 1 GGV) betrifft die Wirkung gegenüber Erwerbern von Rechten am Muster, nicht die Klage gegen "
                    "Verletzer (EuGH Thomas Philipps)."],
                   merke="Art. 33 Abs. 1 GGV schützt nicht den Verletzer.", titel="Eintragung", cases=["des_eugh_thomas_philipps"]),
             frage("Kann die A GmbH mit der Unterlassungsklage ihren eigenen Schaden geltend machen?", True,
                   ["**Ja!** Im eigenen Verfahren nach Art. 32 Abs. 3 GGV kann der Lizenznehmer Ersatz seines Schadens verlangen (EuGH Thomas Philipps). "
                    "Der Schadensersatz richtet sich über Art. 88 Abs. 2 GGV, Art. 8 Abs. 2 Rom-II-VO nach dem Recht des Handlungsorts."],
                   merke="Eigener Schaden im eigenen Verfahren des Lizenznehmers.", titel="Schaden", level=2),
             frage("Ist das LG Hamburg zuständig, obwohl die Lizenzgeberin in Paris sitzt?", True,
                   ["**Ja!** Maßgeblich ist der Beklagte: Die K Ltd. hat weder Sitz noch Niederlassung in der Union; dann entscheidet der Sitz des "
                    "Klägers (Art. 82 Abs. 2 GGV), also Deutschland, örtlich nach § 63b DesignG Hamburg. Die Zuständigkeit reicht unionsweit (Art. 83 "
                    "Abs. 1 GGV)."],
                   merke="Zuständigkeit folgt dem Beklagten, hilfsweise dem Kläger – nie dem Lizenzgeber.", titel="Zuständigkeit",
                   norms=["Art. 82 GGV", "§ 63b DesignG"], level=3),
            ],
            abschnitt=KF, level=2, concepts=["des_lizenz"], norms=["Art. 32 GGV", "Art. 33 GGV"], step=f"{UG}.2"),
        *fallkette("d03f-8", "Kauf des Unionsmusters GGM-A (nach RP1 II/2022)",
            "Die B GmbH (Frankfurt) will das eingetragene Unionsmuster GGM-A von der A SA kaufen, die heute in Paris sitzt, im Register aber noch mit "
            "Sitz in Hamburg steht. Danach will B das jüngere GGM-C der C GmbH beim EUIPO angreifen.",
            [frage("Welche Form verlangt die Übertragung von GGM-A?", 1,
                   ["**Schriftlich und von beiden Parteien unterzeichnet** (Art. 28 Abs. 1 UAbs. 1 GGV), sonst ist sie nichtig (UAbs. 2). Im Übrigen gilt "
                    "das Recht des Mitgliedstaats, in dem der Inhaber laut Register seinen Sitz hat (Art. 27 Abs. 1 lit. a, Abs. 2 GGV), hier deutsches Recht."],
                   optionen=["Notarielle Beurkundung nach französischem Recht", "Schriftlich, von beiden Parteien unterzeichnet",
                             "Formfrei nach § 398 BGB", "Eintragung in das Register als Wirksamkeitsvoraussetzung"],
                   merke="Übertragung Unionsmuster: Art. 28 Abs. 1 GGV Schriftform; Recht des Registersitzes (Art. 27 Abs. 2 GGV).", titel="Form",
                   norms=["Art. 28 GGV", "Art. 27 GGV"], level=2),
             frage("Kann die B GmbH den Nichtigkeitsantrag stellen, bevor der Übergang eingetragen ist?", False,
                   ["**Nein!** Solange der Rechtsübergang nicht eingetragen ist, kann der Rechtsnachfolger die Rechte aus der Eintragung nicht geltend "
                    "machen (Art. 28 Abs. 6 GGV); den Antrag aus dem älteren Muster darf nur dessen Inhaber stellen (Art. 25 Abs. 4 lit. a GGV). B muss "
                    "den Übergang zuerst eintragen lassen (Art. 28 Abs. 2 GGV)."],
                   merke="Erwerber: erst Umschreibung (Art. 28 Abs. 6 GGV), dann Antrag aus dem älteren Recht.", titel="Antragsbefugnis",
                   norms=["Art. 28 GGV", "Art. 25 GGV"], level=2),
            ],
            abschnitt=KF, level=2, concepts=["des_lizenz"]),
    ]),
    # ================================================================== Anmeldung und Eintragung
    dict(id="d03g", titel="§§ 11 bis 21 DesignG, Art. 35 bis 50 GGV: Anmeldung und Eintragung", einheiten=[
        intro("d03g-0", "Prüfungsschema",
              "**AGL:** Eintragung des Designs § 19 Abs. 2 DesignG nach Anmeldung § 11 DesignG und Prüfung § 16 DesignG, § 18 DesignG; "
              "Unionsmuster Art. 48 Abs. 1 GGV nach Anmeldung Art. 35 GGV, Art. 36 GGV und Prüfung Art. 45 GGV, Art. 47 GGV\n\n"
              "**A · Anmeldung**\n"
              "**V1 Berechtigter Anmelder** – Entwerfer oder Rechtsnachfolger, Arbeitgeber (§ 7 Abs. 1, 2 DesignG; Art. 14 GGV); das DPMA prüft die "
              "Berechtigung nicht (§ 19 Abs. 2 DesignG), der Anmelder gilt als berechtigt (§ 8 DesignG)\n"
              "**V2 Mindestinhalt für den Anmeldetag** – Antrag auf Eintragung, Angaben zur Identität, zur Bekanntmachung geeignete Wiedergabe "
              "(§ 11 Abs. 2 S. 1 DesignG, § 13 Abs. 1 DesignG); Unionsmuster: hinreichend klare Wiedergabe (Art. 36 Abs. 1 GGV) und Gebühr binnen eines "
              "Monats (Art. 38 GGV); Einreichung nur beim EUIPO (Art. 35 Abs. 1 GGV)\n"
              "**V3 Weitere Erfordernisse** – Erzeugnisangabe (§ 11 Abs. 3 DesignG, Art. 36 Abs. 2 GGV, ohne Einfluss auf den Schutzumfang § 11 Abs. 6 "
              "DesignG); Formvorschriften der DesignV (§ 11 Abs. 4 DesignG); fakultativ Beschreibung, Aufschiebung, Warenklassen, Entwerfer "
              "(§ 11 Abs. 5 DesignG)\n"
              "**V4 Sammelanmeldung** – bis zu 100 Designs (§ 12 Abs. 1 DesignG), beim EUIPO bis zu 50 (Art. 37 Abs. 1 GGV); Teilung lässt den "
              "Anmeldetag unberührt (§ 12 Abs. 2 DesignG)\n"
              "**V5 Gebühr** – fällig mit Einreichung (§ 3 Abs. 1 PatKostG), drei Monate (§ 6 Abs. 1 S. 2 PatKostG), sonst Rücknahmefiktion (§ 6 Abs. 2 "
              "PatKostG); 60 EUR elektronisch, 70 EUR Papier (Nr. 341 000, 341 100), Sammelanmeldung je Design (Nr. 341 200, 341 300)\n"
              "**V6 Priorität** – ausländische Priorität sechs Monate (§ 14 DesignG; Art. 41 GGV), Ausstellungspriorität sechs Monate (§ 15 Abs. 1 "
              "DesignG; Art. 44 GGV); der Prioritätstag ersetzt den Anmeldetag für §§ 2 bis 6 DesignG (§ 13 Abs. 2 DesignG)\n\n"
              "**B · Prüfung**\n"
              "**V7 Formalprüfung** – § 16 Abs. 1 DesignG: Gebühren, Anmeldetag, sonstige Erfordernisse; Mängelbeseitigung binnen gesetzter Frist, bei "
              "Mängeln des Mindestinhalts Anmeldetag erst mit Beseitigung (§ 16 Abs. 3 S. 2 DesignG); EUIPO: zwei Monate (Art. 45 Abs. 3, 4 GGV)\n"
              "**V8 Eintragungshindernisse** – kein Design (§ 1 Nr. 1 DesignG), öffentliche Ordnung, Hoheitszeichen (§ 18 DesignG; Art. 47 Abs. 1 GGV); "
              "keine Prüfung von Neuheit und Eigenart\n"
              "**V9 Rechtsbehelf** – Weiterbehandlung binnen eines Monats (§ 17 Abs. 2 DesignG, 100 EUR); Beschwerde zum BPatG (§ 23 Abs. 4 DesignG)\n\n"
              "**C · Eintragung und Bekanntmachung**\n"
              "**V10 Eintragung** – § 19 Abs. 2 DesignG; Schutz entsteht mit Eintragung (§ 27 Abs. 1 DesignG, Art. 12 Abs. 1 GGV)\n"
              "**V11 Bekanntmachung und Aufschiebung** – Bekanntmachung mit Wiedergabe (§ 20 DesignG); Aufschiebung um 30 Monate (§ 21 Abs. 1 "
              "DesignG; Art. 50 Abs. 1 GGV), in dieser Zeit Schutz nur gegen Nachahmung (§ 38 Abs. 3 DesignG, Art. 19 Abs. 5 GGV); Erstreckung "
              "durch Gebühr innerhalb der Aufschiebungsfrist (§ 21 Abs. 2 DesignG, § 7 Abs. 2 PatKostG)\n\n"
              "**⇒ Rechtsfolge:** eingetragenes Design mit Anmeldetag als Zeitrang; Mängel nach Eintragung: Unionsmuster nur in unwesentlichen "
              "Einzelheiten änderbar (Art. 50e Abs. 1 GGV), deutsches Design nur über Teilverzicht oder Teilnichtigkeit (§ 35 DesignG, § 36 Abs. 2 DesignG)\n\n"
              "**Klausurfallen:** Wiedergaben nie per Telefax (§ 4 S. 4 DesignV), Datenträger nur in den zugelassenen Typen und Formaten (§ 7 Abs. 3 "
              "DesignV). Ein Einzeldesign darf nur eine Erscheinungsform zeigen (BGH Sporthelm); Varianten gehören in die Sammelanmeldung. "
              "Ein Verfahren oder eine Idee ist kein Design (RP1 III/2019: Airbrush-Lackierung). Fehlen Bilder im Register, liegt meist eine "
              "Aufschiebung vor (RP1 I/2019). Früher konnte die Unionsmusteranmeldung beim DPMA eingereicht werden (Art. 35 GGV a.F., § 62 DesignG; "
              "RP1 I/2020); seit 1.5.2025 nur noch beim EUIPO.\n\n"
              "**In den Klausuren:** II/2018 (Ansichten verschiedener Designs, Mängelbescheid), I/2019 (Sammelanmeldung, Aufschiebung, Priorität), "
              "III/2019 (Anmeldung per Fax, Datenträger, Beschreibung), I/2020 (Anmeldetag bei Weiterleitung), III/2021 (Mängelbescheid, Aufschiebung), "
              "II/2023 (Mängel nach Eintragung), III/2023 (Eintragungsvoraussetzungen, nur eine Darstellung).",
              concepts=["des_anmeldung", "des_wiedergabe", "des_sammelanmeldung", "des_aufschiebung", "des_pruefung_dpma", "des_anmeldetag", "des_prioritaet"],
              norms=["§ 11 DesignG", "§ 12 DesignG", "§ 13 DesignG", "§ 16 DesignG", "§ 18 DesignG", "§ 19 DesignG", "§ 21 DesignG", "§ 38 Abs. 3 DesignG",
                     "Art. 35 GGV", "Art. 36 GGV", "Art. 37 GGV", "Art. 38 GGV", "Art. 45 GGV", "Art. 47 GGV", "Art. 50 GGV"],
              cases=["des_bgh_sporthelm"], abschnitt="Normenkette"),
        intro("d03g-1", "Definitionen",
              "**Wiedergabe:** die zur Bekanntmachung geeignete Darstellung des Designs; sie bestimmt den Schutzgegenstand (§ 11 Abs. 2 S. 1 Nr. 3 "
              "DesignG, § 37 Abs. 1 DesignG)\n"
              "**Sammelanmeldung:** Zusammenfassung mehrerer Designs in einer Anmeldung, beim DPMA bis zu 100 (Legaldefinition § 12 Abs. 1 DesignG), "
              "beim EUIPO bis zu 50 (Art. 37 Abs. 1 GGV); jedes Design bleibt selbständig (Art. 37 Abs. 4 GGV)\n"
              "**Anmeldetag:** Tag des Eingangs der Unterlagen mit dem Mindestinhalt des § 11 Abs. 2 DesignG beim DPMA (§ 13 Abs. 1 DesignG); beim "
              "EUIPO zusätzlich Zahlung binnen eines Monats (Art. 38 GGV)\n"
              "**Aufschiebung der Bekanntmachung:** Bekanntmachung nur der Eintragung ohne Wiedergabe für 30 Monate ab Anmeldetag (§ 21 Abs. 1 DesignG); "
              "Schutz in dieser Zeit nur gegen Nachahmung (§ 38 Abs. 3 DesignG)\n"
              "**Erzeugnisangabe:** Angabe der Erzeugnisse, in die das Design aufgenommen werden soll; Pflichtangabe ohne Einfluss auf den "
              "Schutzumfang (§ 11 Abs. 3, 6 DesignG)\n"
              "**Ausstellungspriorität:** Prioritätsrecht ab erstmaliger Zurschaustellung auf einer bekannt gemachten Ausstellung bei Anmeldung "
              "binnen sechs Monaten (§ 15 Abs. 1 DesignG)",
              concepts=["des_wiedergabe", "des_sammelanmeldung", "des_anmeldetag", "des_aufschiebung", "des_erzeugnisangabe"], abschnitt="Definitionen"),
        mc("d03g-2", "Was prüft das DPMA?", "Was prüft das DPMA vor der Eintragung eines Designs?",
           ["Gebühren, Anmeldetag, Formerfordernisse und die Eintragungshindernisse des § 18 DesignG",
            "Zusätzlich Neuheit und Eigenart von Amts wegen", "Nur die Zahlung der Gebühr",
            "Auch die Berechtigung des Anmelders"], 0,
           ["**Formalien und § 18 DesignG.** § 16 Abs. 1 DesignG: Gebühren, Voraussetzungen des Anmeldetags, sonstige Erfordernisse; § 18 DesignG: "
            "kein Design, öffentliche Ordnung, Hoheitszeichen. Neuheit und Eigenart prüft es nicht; die Berechtigung ebenfalls nicht (§ 19 Abs. 2 "
            "DesignG). Daher die Vermutung des § 39 DesignG (RP1 III/2023)."],
           merke="DPMA: § 16 DesignG Formalien + § 18 DesignG Hindernisse; keine Neuheit, keine Eigenart.",
           level=1, concepts=["des_pruefung_dpma"], norms=["§ 16 DesignG", "§ 18 DesignG", "§ 19 DesignG"], step=f"{AN}.5", abschnitt=DN),
        fall("d03g-3", "Keine Bilder im Register",
             "Die Cosmic GmbH findet im DPMA-Register zu einem Design der Formschön GmbH nur Nummer, Inhaberin, Anmelde- und Eintragungstag, aber keine "
             "Abbildungen. Die Abmahnung zeigt sieben Tiegel unter derselben Nummer.",
             "Spricht das für eine Sammelanmeldung mit aufgeschobener Bekanntmachung?", True,
             ["**Ja!** Bei Aufschiebung beschränkt sich die Bekanntmachung auf die Eintragung (§ 21 Abs. 1 S. 2 DesignG); bis zu 100 Designs können "
              "in einer Sammelanmeldung stehen (§ 12 Abs. 1 DesignG). Während der Aufschiebung schützt das Design nur gegen Nachahmung (§ 38 Abs. 3 "
              "DesignG; RP1 I/2019)."],
             merke="Keine Bilder: Aufschiebung § 21 DesignG; während der Aufschiebung nur Nachahmungsschutz (§ 38 Abs. 3 DesignG).",
             level=2, concepts=["des_aufschiebung", "des_sammelanmeldung"], norms=["§ 21 DesignG", "§ 12 DesignG", "§ 38 Abs. 3 DesignG"], step=f"{AN}.6",
             abschnitt=DN),
        mc("d03g-4", "Erstreckung", "Was muss der Inhaber bei aufgeschobener Bekanntmachung tun, um den Schutz über 30 Monate hinaus zu erhalten?",
           ["Innerhalb der Aufschiebungsfrist die Erstreckungsgebühr zahlen (§ 21 Abs. 2 DesignG, § 7 Abs. 2 PatKostG)",
            "Einen neuen Antrag auf Eintragung stellen", "Nichts; der Schutz läuft automatisch 25 Jahre",
            "Binnen zwei Monaten nach Ablauf die Aufrechterhaltungsgebühr zahlen"], 0,
           ["**Erstreckungsgebühr innerhalb der Aufschiebungsfrist.** Der Schutz wird auf die volle Schutzdauer erstreckt, wenn die Gebühr (40 EUR, "
            "Nr. 341 600) innerhalb der 30 Monate gezahlt wird (§ 21 Abs. 2 S. 1 DesignG, § 7 Abs. 2 PatKostG); bei flächenmäßigem Designabschnitt "
            "ist auch die Wiedergabe nachzureichen (S. 2). Sonst endet der Schutz mit Ablauf der Frist (§ 21 Abs. 4 S. 1 DesignG)."],
           merke="Erstreckung: § 21 Abs. 2 DesignG · § 7 Abs. 2 PatKostG · sonst Ende § 21 Abs. 4 DesignG.",
           level=2, concepts=["des_aufschiebung"], norms=["§ 21 DesignG", "§ 7 PatKostG"], step=f"{AN}.6", abschnitt=DN),
        fall("d03g-5", "Verfahren als Design",
             "Frau Schnee will ein „Verfahren zum Lackieren von Golfschlägern mit Airbrush“ als Design anmelden und dazu Bilder verschiedenfarbiger "
             "Schläger und eine Beschreibung einreichen.",
             "Kann das Verfahren als Design geschützt werden?", False,
             ["**Nein!** Design ist die Erscheinungsform eines Erzeugnisses (§ 1 Nr. 1 DesignG), nicht ein Verfahren oder eine Idee. Schützbar sind "
              "nur konkrete Lackierungen, jede als eigenes Design, etwa in einer Sammelanmeldung (§ 12 DesignG); das Verfahren selbst allenfalls "
              "als Patent (RP1 III/2019)."],
             merke="Design schützt Erscheinungsformen, keine Verfahren; Varianten per Sammelanmeldung.",
             level=1, concepts=["des_design_begriff"], norms=["§ 1 DesignG", "§ 18 DesignG", "§ 12 DesignG"], step=f"{AN}.2", abschnitt=DN),
        fall("d03g-6", "Mangel nach Eintragung",
             "Das Unionsmuster GGM-2 der A GmbH ist eingetragen und bekannt gemacht. Die Wiedergabe zeigt in einer Ansicht ein zusätzliches, nicht "
             "gewolltes Element, das den Gesamteindruck mitprägt.",
             "Kann die A GmbH die Wiedergabe jetzt noch entsprechend ändern?", False,
             ["**Nein!** Nach der Eintragung darf die Wiedergabe nur in unwesentlichen Einzelheiten geändert werden (Art. 50e Abs. 1 GGV). Ein "
              "prägendes Element zu streichen ändert den Schutzgegenstand. Es bleibt eine Neuanmeldung; die eigene Bekanntmachung von GGM-2 schadet "
              "ihr innerhalb der Schonfrist nicht (Art. 7 Abs. 2 GGV; RP1 II/2023)."],
             merke="Nach Eintragung: Änderung nur in unwesentlichen Einzelheiten (Art. 50e Abs. 1 GGV).",
             level=3, concepts=["des_wiedergabe"], norms=["Art. 50e GGV", "Art. 7 GGV"], step=f"{AN}.6", abschnitt=DN),
        *fallkette("d03g-7", "Kinderhelm per Fax (nach RP1 III/2019)",
            "Herr Sport faxt am 09.07.2018 Antrag und Wiedergabeformblatt mit sechs Ansichten an das DPMA. Das Original des Antrags kommt am 12.07.2018 "
            "ohne Wiedergabeblatt an, dafür mit einem USB-Stick. Am 12.12.2018 reicht er auf Nachfrage eine DVD mit den Ansichten nach. Eingetragen wird "
            "am 15.01.2019.",
            [frage("Hat das Fax vom 09.07.2018 einen Anmeldetag begründet?", False,
                   ["**Nein!** Wiedergaben dürfen zur Anmeldung nicht per Telefax eingereicht werden (§ 4 S. 4 DesignV). Ohne zulässige Wiedergabe "
                    "fehlt der Mindestinhalt des § 11 Abs. 2 S. 1 Nr. 3 DesignG; einen Anmeldetag gibt es erst mit allen drei Angaben (§ 13 Abs. 1 DesignG)."],
                   merke="Anmeldetag: Antrag, Identität, Wiedergabe (§ 11 Abs. 2 DesignG); Wiedergabe nie per Fax (§ 4 S. 4 DesignV).",
                   titel="Fax", level=2),
             frage("Welcher Tag wird Anmeldetag?", 2,
                   ["**Voraussichtlich der 12.12.2018.** Der USB-Stick ist kein vom DPMA zugelassener Datenträger, die Dateien entsprechen nicht dem "
                    "Format (JPEG, mindestens 300 dpi, § 7 Abs. 3 DesignV); ein nicht lesbarer Datenträger gilt als nicht eingereicht. Wird der Mangel "
                    "auf Aufforderung beseitigt, ist Anmeldetag der Tag der Beseitigung (§ 16 Abs. 3 S. 2 DesignG)."],
                   optionen=["09.07.2018", "12.07.2018", "12.12.2018", "15.01.2019"],
                   merke="Mangel des Mindestinhalts: Anmeldetag erst mit Beseitigung, § 16 Abs. 3 S. 2 DesignG.", titel="Anmeldetag", level=3),
             frage("Schadet dann die Ausstellung der Helme am 01.10.2018 der Neuheit?", False,
                   ["**Nein!** Sie liegt zwar vor dem Anmeldetag, ist aber eine eigene Offenbarung des Entwerfers in den zwölf Monaten davor und bleibt "
                    "nach § 6 S. 1 DesignG unberücksichtigt."],
                   merke="Verschobener Anmeldetag: Schonfrist § 6 DesignG fängt eigene Ausstellungen auf.", titel="Ausstellung",
                   norms=["§ 6 DesignG"]),
             frage("Ist das Einzeldesign mit sechs unterschiedlichen Helmen wirksam?", False,
                   ["**Nein!** Zeigen die Ansichten verschiedene Ausführungsformen, fehlt die Erscheinungsform „eines“ Erzeugnisses; das Design ist nach "
                    "§ 33 Abs. 1 Nr. 1 DesignG nichtig (BGH Sporthelm). Eine Verletzungsklage gegen die Snow GmbH hätte keine tragfähige Grundlage."],
                   merke="Einzeldesign mit Varianten: nichtig, § 33 Abs. 1 Nr. 1 DesignG (BGH Sporthelm).", titel="Einheitlicher Schutzgegenstand",
                   cases=["des_bgh_sporthelm"], level=2),
             frage("Was empfehlen Sie Herrn Sport für die Zukunft?", 2,
                   ["**Sammelanmeldung.** Jede Helmvariante als eigenes Design in einer Sammelanmeldung (§ 12 Abs. 1 DesignG); die Schonfrist des § 6 "
                    "DesignG läuft für die Ausstellung vom 01.10.2018 bis zum 01.10.2019. Anmelden sollte die Sport GmbH, wenn sie klagen will."],
                   optionen=["Nochmals ein Einzeldesign mit allen sechs Ansichten", "Ein Gebrauchsmuster für die Form",
                             "Eine Sammelanmeldung mit jeder Variante als eigenem Design", "Abwarten, bis ein nicht eingetragenes Muster entsteht"],
                   merke="Varianten: Sammelanmeldung § 12 DesignG; Schonfrist § 6 DesignG nutzen.", titel="Empfehlung", level=2),
            ],
            abschnitt=KF, level=2, concepts=["des_anmeldung", "des_anmeldetag"], norms=["§ 11 DesignG", "§ 13 DesignG", "§ 16 DesignG"], step=f"{AN}.2"),
    ]),
]

KURS = dict(
    id="d03", gebiet="designg", reihe="Anspruchsgrundlagen für die Klausur", kompakt="fragen",
    titel="Anspruchsgrundlagen Design",
    untertitel="RP1: Schutz, Verletzung, Nichtigkeit, Zuständigkeit, Eilrechtsschutz, Lizenz, Anmeldung",
    farbe="#b0562b", icon="hammer",
    beschreibung="Anspruchsgrundlage für Anspruchsgrundlage durch die Klausur Rechtspraxis 1: je Kapitel das Prüfungsschema mit Normenkette "
                 "und Fristen (Frist · Berechnung · Verschiebung), die Definitionen, Drill-Fragen zu Normen und Begriffen und ein Klausurfall "
                 "nach einer echten RP1-Klausur (II/2018 bis III/2023). Deutsches Design und Unionsgeschmacksmuster nebeneinander, GGV in der "
                 "Fassung vom 1.7.2026.",
    kapitel=KAPITEL,
)
