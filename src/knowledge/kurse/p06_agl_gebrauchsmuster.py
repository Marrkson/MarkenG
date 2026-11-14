# -*- coding: utf-8 -*-
"""Kurs p06: Anspruchsgrundlagen Gebrauchsmuster für die Klausur (TS, RP1).

Ein Kapitel je Anspruchsgrundlage bzw. Rechtsbehelf des GebrMG: Prüfungsschema in Lösungssprache (AGL → Voraussetzungen mit
Norm → Rechtsfolge), Definitionen, Drill zu Normen und Fristen, Klausurfälle als Fallketten nach den TS-Klausuren II/2018 bis
III/2023. Das GebrMG hat keine Graph-Knoten: GebrMG-Zitate stehen nur im Fließtext, `norms` nennt allein die verwiesenen
PatG-/PatKostG-Vorschriften (§ 40 PatG, § 84 PatG …). Normtexte: GebrMG nach dem 2. PatModG (Fassung 2021 ff.)."""
from ._helpers import intro, mc, fall, frage, fallkette

G = ["pat_gebrauchsmuster"]
A = ["pat_gebrauchsmuster_abzweigung"]
L = ["pat_gebrauchsmuster_loeschung"]

KURS = dict(
    id="p06", gebiet="patent", reihe="Anspruchsgrundlagen für die Klausur", kompakt="fragen",
    titel="Anspruchsgrundlagen Gebrauchsmuster",
    untertitel="Schutzfähigkeit, Abzweigung, Priorität, Löschung, Verletzung und Schutzdauer – Normenketten, Definitionen und Fristen",
    farbe="#2f6b4f", icon="hammer",
    beschreibung="Das Gebrauchsmuster in der Klausur, Anspruchsgrundlage für Anspruchsgrundlage: die Abzweigung aus der Patentanmeldung "
                 "(§ 5 GebrMG, in elf TS-Klausuren gefragt), der relative Stand der Technik mit Neuheitsschonfrist (§ 3 GebrMG), innere, "
                 "Unions- und Ausstellungspriorität (§§ 6, 6a GebrMG), der Löschungsantrag mit Widerspruch und Kosten (§§ 15 bis 17 GebrMG), "
                 "die Verletzungsansprüche mit dem Einwand der Schutzunfähigkeit (§§ 13, 19, 24 GebrMG) sowie Eintragung und Schutzdauer. "
                 "Jedes Kapitel: Prüfungsschema, Definitionen, Normendrill und Klausurfall nach den TS-Klausuren 2018 bis 2023.",
    kapitel=[
        # ================================================================== Überblick
        dict(id="p060", titel="Überblick: Anspruchsgrundlagen und Fristen", einheiten=[
            intro("p060-0", "Die Anspruchsgrundlagen im Überblick",
                  "**Ziel des Mandanten → Anspruchsgrundlage (Normenkette)**\n\n"
                  "**Schnellen Schutz aus einer (gescheiterten) Patentanmeldung** → Abzweigung § 5 Abs. 1 S. 1 GebrMG · Priorität bleibt § 5 Abs. 1 S. 2 GebrMG · "
                  "Frist § 5 Abs. 1 S. 3 GebrMG · Unterlagen § 5 Abs. 2 GebrMG · Schutzdauer § 23 Abs. 1 GebrMG\n"
                  "**Neues Gebrauchsmuster anmelden** → § 4 Abs. 1, 3 GebrMG · Anmeldetag § 4a Abs. 1 GebrMG · Übersetzung § 4b GebrMG · "
                  "Eintragung ohne Sachprüfung § 8 Abs. 1 GebrMG · Schutzfähigkeit § 1 Abs. 1 GebrMG, § 2 GebrMG, § 3 GebrMG\n"
                  "**Zeitrang einer früheren Anmeldung nutzen** → innere Priorität § 6 Abs. 1 GebrMG i.V.m. § 40 PatG · Unionspriorität "
                  "§ 6 Abs. 2 GebrMG i.V.m. § 41 PatG und Art. 4 PVÜ · Ausstellungspriorität § 6a GebrMG\n"
                  "**Fremdes Gebrauchsmuster beseitigen** → Löschungsantrag § 15 Abs. 1 Nr. 1 bis 3 GebrMG, § 16 GebrMG, § 17 GebrMG · bei Entnahme "
                  "§ 15 Abs. 2 GebrMG mit § 13 Abs. 2 GebrMG · Übertragung § 13 Abs. 3 GebrMG i.V.m. § 8 PatG\n"
                  "**Gegen einen Verletzer vorgehen** → Unterlassung § 24 Abs. 1 GebrMG · Schadensersatz § 24 Abs. 2 GebrMG · Vernichtung und Rückruf "
                  "§ 24a GebrMG · Auskunft § 24b GebrMG · Vorlage und Besichtigung § 24c GebrMG · Landgericht § 27 Abs. 1 GebrMG\n"
                  "**Sich gegen eine Verletzungsklage verteidigen** → Einwand der Schutzunfähigkeit § 13 Abs. 1 GebrMG · Löschungsantrag und "
                  "Aussetzung § 19 GebrMG · Vorbenutzungsrecht § 13 Abs. 3 GebrMG i.V.m. § 12 PatG · Schranken § 12 GebrMG\n"
                  "**Gegen einen Beschluss der Gebrauchsmusterstelle oder -abteilung** → Beschwerde § 18 Abs. 1 GebrMG i.V.m. § 73 PatG\n"
                  "**Schutz erhalten** → Aufrechterhaltungsgebühren § 23 Abs. 2 GebrMG, § 3 Abs. 2 PatKostG, § 7 Abs. 1 PatKostG; Erlöschen "
                  "§ 23 Abs. 3 GebrMG\n\n"
                  "**In den Klausuren:** Die Abzweigung ist die häufigste Gebrauchsmusterfrage der TS (II/2018, II/2019, III/2019, II/2020, I/2021, "
                  "III/2021, I/2022, II/2022, III/2022, II/2023, III/2023), meist als Rettungsweg nach Widerruf, Zurückweisung oder Rücknahme. Danach "
                  "folgen der relative Stand der Technik (§ 3 Abs. 1 GebrMG) und der Löschungsantrag.",
                  concepts=G + A + L, norms=["§ 40 PatG", "§ 41 PatG", "§ 8 PatG", "§ 12 PatG", "§ 73 PatG", "§ 3 Abs. 2 PatKostG", "§ 7 Abs. 1 PatKostG"],
                  abschnitt="Überblick"),
            intro("p060-1", "Fristen und Gebühren",
                  "**Frist · Norm · Berechnung · Verschiebung · Gebühr**\n\n"
                  "**Abzweigung:** zwei Monate nach Ende des Monats der Erledigung bzw. des Abschlusses des Einspruchsverfahrens, längstens Ablauf des "
                  "zehnten Jahres nach dem Anmeldetag (§ 5 Abs. 1 S. 3 GebrMG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · Anmeldegebühr 30 EUR "
                  "elektronisch (Nr. 321 000 Anlage PatKostG), 40 EUR Papier (Nr. 321 100 Anlage PatKostG), fällig mit Anmeldung (§ 3 Abs. 1 S. 1 PatKostG), "
                  "zahlbar binnen drei Monaten (§ 6 Abs. 1 S. 2 PatKostG), sonst gilt die Anmeldung als zurückgenommen (§ 6 Abs. 2 PatKostG)\n"
                  "**Angaben zur Abzweigung:** zwei Monate nach Zustellung der Aufforderung (§ 5 Abs. 2 S. 1 GebrMG; Zustellung § 21 Abs. 1 GebrMG "
                  "i.V.m. § 127 PatG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · sonst Verwirkung (§ 5 Abs. 2 S. 3 GebrMG)\n"
                  "**Übersetzung:** drei Monate nach Einreichung (§ 4b S. 1 GebrMG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · sonst Rücknahmefiktion (§ 4b S. 2 GebrMG)\n"
                  "**Innere Priorität:** zwölf Monate ab Anmeldetag der früheren DPMA-Anmeldung (§ 6 Abs. 1 S. 1 GebrMG); Erklärung binnen zwei Monaten "
                  "nach dem Anmeldetag der späteren Anmeldung (§ 6 Abs. 1 S. 2 GebrMG i.V.m. § 40 Abs. 4 PatG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · "
                  "keine Wiedereinsetzung in die Zwölfmonatsfrist (§ 21 Abs. 1 GebrMG i.V.m. § 123 Abs. 1 S. 2 Nr. 3 PatG)\n"
                  "**Unionspriorität:** zwölf Monate (Art. 4 C Abs. 1 PVÜ); Angaben bis Ablauf des 16. Monats nach dem Prioritätstag (§ 6 Abs. 2 GebrMG "
                  "i.V.m. § 41 Abs. 1 PatG) · Art. 4 C Abs. 2 PVÜ · Art. 4 C Abs. 3 PVÜ\n"
                  "**Ausstellungspriorität:** Anmeldung binnen sechs Monaten seit der ersten Zurschaustellung (§ 6a Abs. 1 GebrMG); Angaben und Nachweis "
                  "vor Ablauf des 16. Monats (§ 6a Abs. 4 GebrMG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB\n"
                  "**Neuheitsschonfrist:** sechs Monate vor dem Zeitrangtag (§ 3 Abs. 1 S. 3 GebrMG), rückwärts gerechnet\n"
                  "**Widerspruch gegen den Löschungsantrag:** ein Monat nach Zustellung der Mitteilung (§ 17 Abs. 1 S. 1 GebrMG) · § 187 Abs. 1 BGB, "
                  "§ 188 Abs. 2 BGB · § 193 BGB · sonst Löschung (§ 17 Abs. 1 S. 2 GebrMG)\n"
                  "**Löschungsantrag:** keine Frist; Gebühr 300 EUR je Antragsteller (Nr. 323 100 Anlage PatKostG), fällig mit Antrag (§ 3 Abs. 1 S. 1 "
                  "PatKostG), zahlbar binnen drei Monaten (§ 6 Abs. 1 S. 2 PatKostG), sonst Rücknahmefiktion (§ 6 Abs. 2 PatKostG)\n"
                  "**Kostenantrag ohne Hauptsacheentscheidung:** ein Monat nach Zustellung der Mitteilung über die Beendigung (§ 17 Abs. 4 S. 3 GebrMG)\n"
                  "**Beschwerde:** ein Monat nach Zustellung (§ 18 Abs. 2 S. 1 GebrMG i.V.m. § 73 Abs. 2 S. 1 PatG) · § 99 Abs. 1 PatG, § 222 Abs. 1 ZPO, "
                  "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 222 Abs. 2 ZPO · 500 EUR im Löschungsverfahren (Nr. 401 100 Anlage PatKostG), sonst 200 EUR "
                  "(Nr. 401 300 Anlage PatKostG), innerhalb der Beschwerdefrist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt sie als nicht eingelegt (§ 6 Abs. 2 PatKostG)\n"
                  "**Aufrechterhaltung:** fällig am letzten Tag des Anmeldemonats vor dem 4., 7. und 9. Schutzjahr (§ 3 Abs. 2 S. 1 PatKostG), zahlbar "
                  "bis Ablauf des zweiten Monats nach Fälligkeit, mit 50 EUR Zuschlag bis Ablauf des sechsten Monats (§ 7 Abs. 1 PatKostG) · § 193 BGB · "
                  "210, 350, 530 EUR (Nr. 322 100, Nr. 322 200, Nr. 322 300 Anlage PatKostG) · sonst Erlöschen (§ 23 Abs. 3 Nr. 2 GebrMG)\n"
                  "**Weiterbehandlung:** ein Monat nach Zustellung der Zurückweisung (§ 21 Abs. 1 GebrMG i.V.m. § 123a Abs. 2 PatG), 100 EUR (Nr. 323 000 Anlage PatKostG)\n"
                  "**Wiedereinsetzung:** zwei Monate nach Wegfall des Hindernisses, höchstens ein Jahr (§ 21 Abs. 1 GebrMG i.V.m. § 123 Abs. 2 PatG)\n\n"
                  "Zahlungstag: § 2 PatKostZV (Gutschrift, Bareinzahlung, bei SEPA-Mandat Eingang beim DPMA).",
                  concepts=["pat_fristen", "pat_gebuehren", "pat_zahlungsfristen"] + G,
                  norms=["§ 3 Abs. 1 PatKostG", "§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG", "§ 7 Abs. 1 PatKostG", "§ 40 Abs. 4 PatG", "§ 41 Abs. 1 PatG",
                         "§ 73 Abs. 2 PatG", "§ 123 PatG", "§ 123a PatG"],
                  abschnitt="Überblick"),
            intro("p060-2", "Gebrauchsmuster und Patent: die Unterschiede",
                  "**Gegenstand:** keine Verfahren (§ 2 Nr. 3 GebrMG), keine biotechnologischen Erfindungen (§ 1 Abs. 2 Nr. 5 GebrMG); Erzeugnisse, "
                  "Vorrichtungen, Stoffe und Verwendungsansprüche, die sich in Sacheigenschaften niederschlagen, sind zulässig.\n"
                  "**Stand der Technik:** schriftliche Beschreibungen weltweit, Benutzungen nur im Inland, keine mündliche Beschreibung (§ 3 Abs. 1 S. 2 GebrMG); "
                  "keine älteren nachveröffentlichten Anmeldungen (kein Gegenstück zu § 3 Abs. 2 PatG), stattdessen Löschungsgrund des Doppelschutzes "
                  "(§ 15 Abs. 1 Nr. 2 GebrMG).\n"
                  "**Schonfrist:** sechs Monate für jede Beschreibung oder Benutzung, die auf der Ausarbeitung des Anmelders beruht (§ 3 Abs. 1 S. 3 GebrMG); "
                  "beim Patent nur Missbrauch und Ausstellung (§ 3 Abs. 5 PatG).\n"
                  "**Erfinderischer Schritt:** gleicher Maßstab wie die erfinderische Tätigkeit (BGH Demonstrationsschrank), aber gegenüber dem engeren Stand der Technik.\n"
                  "**Verfahren:** Eintragung ohne Prüfung auf Neuheit, erfinderischen Schritt und gewerbliche Anwendbarkeit (§ 8 Abs. 1 S. 2 GebrMG); "
                  "kein Einspruch, keine Nichtigkeitsklage, sondern Löschungsantrag beim DPMA (§ 15 GebrMG, § 16 GebrMG).\n"
                  "**Schutzdauer:** zehn Jahre nach Ablauf des Anmeldemonats (§ 23 Abs. 1 GebrMG) statt zwanzig Jahre ab dem Anmeldetag (§ 16 PatG); kein Schutzzertifikat.\n"
                  "**Durchsetzung:** Schutz ab Eintragung (§ 11 Abs. 1 GebrMG), keine Entschädigung vorher (anders § 33 PatG); das Verletzungsgericht prüft die "
                  "Schutzfähigkeit selbst (§ 13 Abs. 1 GebrMG), kein Trennungsprinzip.",
                  concepts=G + ["pat_doppelschutz", "pat_trennungsprinzip"], norms=["§ 3 Abs. 2 PatG", "§ 3 Abs. 5 PatG", "§ 16 PatG", "§ 33 PatG"],
                  cases=["pat_bgh_demonstrationsschrank"], abschnitt="Überblick"),
            mc("p060-3", "Patentanmeldung zurückgewiesen",
               "Die Patentanmeldung des Mandanten ist rechtskräftig zurückgewiesen. Er will trotzdem schnell ein Schutzrecht mit dem alten Anmeldetag. Welche AGL?",
               ["Abzweigung nach § 5 Abs. 1 S. 1 GebrMG", "Innere Priorität nach § 6 Abs. 1 GebrMG", "Weiterbehandlung nach § 123a PatG",
                "Teilung nach § 39 Abs. 1 PatG"], 0,
               ["**§ 5 Abs. 1 S. 1 GebrMG.** Nur die Abzweigung gibt den Anmeldetag der Patentanmeldung selbst; die Frist läuft noch zwei Monate "
                "nach Ende des Monats der Erledigung (§ 5 Abs. 1 S. 3 GebrMG). Die innere Priorität gibt nur den Prioritätstag und läuft zwölf Monate. "
                "Weiterbehandlung setzt eine Fristversäumung voraus, Teilung eine anhängige Anmeldung."],
               merke="Gescheiterte Patentanmeldung → Abzweigung § 5 GebrMG (Anmeldetag bleibt).", level=1, concepts=A, norms=["§ 39 Abs. 1 PatG", "§ 123a PatG"],
               abschnitt="Welche Anspruchsgrundlage?"),
            mc("p060-4", "Konkurrent hat ein Gebrauchsmuster",
               "Ein Wettbewerber hat ein eingetragenes Gebrauchsmuster; die Mandantin hält es wegen einer älteren Druckschrift für nicht neu und will es beseitigen. Welcher Rechtsbehelf?",
               ["Einspruch nach § 59 Abs. 1 PatG", "Nichtigkeitsklage nach § 81 PatG", "Löschungsantrag nach § 15 Abs. 1 Nr. 1 GebrMG, § 16 GebrMG",
                "Beschwerde nach § 18 Abs. 1 GebrMG"], 2,
               ["**§ 15 Abs. 1 Nr. 1 GebrMG, § 16 GebrMG.** Gegen ein Gebrauchsmuster gibt es weder Einspruch noch Nichtigkeitsklage. Jedermann kann beim "
                "DPMA schriftlich die Löschung beantragen, wenn der Gegenstand nach §§ 1 bis 3 GebrMG nicht schutzfähig ist. Gebühr 300 EUR "
                "(Nr. 323 100 Anlage PatKostG). Die Beschwerde richtet sich erst gegen den Beschluss der Gebrauchsmusterabteilung."],
               merke="Gebrauchsmuster angreifen = Löschungsantrag beim DPMA, ohne Frist.", level=1, concepts=L, norms=["§ 59 Abs. 1 PatG", "§ 81 PatG"],
               abschnitt="Welche Anspruchsgrundlage?"),
            mc("p060-5", "Verletzungsklage aus ungeprüftem Recht",
               "Die Mandantin wird aus einem Gebrauchsmuster auf Unterlassung verklagt. Sie hält es für nicht schutzfähig. Was ist ihre erste Verteidigungslinie im Prozess?",
               ["Nichtigkeitsklage beim BPatG und Aussetzung nach § 148 ZPO", "Einwand der Schutzunfähigkeit nach § 13 Abs. 1 GebrMG im Verletzungsprozess",
                "Einspruch beim DPMA", "Antrag auf Recherche nach § 7 GebrMG"], 1,
               ["**§ 13 Abs. 1 GebrMG.** Der Schutz entsteht nicht, soweit ein Löschungsanspruch für jedermann besteht. Das Verletzungsgericht prüft "
                "die Schutzfähigkeit deshalb selbst. Daneben kann sie Löschung beantragen; dann kann das Gericht nach § 19 S. 1 GebrMG aussetzen. "
                "Eine Nichtigkeitsklage gibt es gegen ein Gebrauchsmuster nicht."],
               merke="Gebrauchsmuster: kein Trennungsprinzip – Einwand § 13 Abs. 1 GebrMG, daneben Löschung und § 19 GebrMG.", level=2,
               concepts=G + ["pat_trennungsprinzip", "pat_aussetzung"], abschnitt="Welche Anspruchsgrundlage?"),
            mc("p060-6", "Messe vor der Anmeldung",
               "Der Mandant hat seine Erfindung vor vier Monaten auf einer Fachmesse in Köln selbst gezeigt und noch nichts angemeldet. Er will Schutz in Deutschland. Was raten Sie?",
               ["Patentanmeldung, da § 3 Abs. 5 PatG greift", "Gebrauchsmusteranmeldung; die eigene Vorführung ist nach § 3 Abs. 1 S. 3 GebrMG unschädlich",
                "Kein Schutz mehr möglich", "Gebrauchsmuster nur mit Ausstellungspriorität nach § 6a GebrMG"], 1,
               ["**§ 3 Abs. 1 S. 3 GebrMG.** Die Vorführung ist eine Benutzung im Inland, beruht auf der Ausarbeitung des Anmelders und liegt "
                "innerhalb von sechs Monaten vor dem Anmeldetag: Sie bleibt außer Betracht. Für ein Patent ist sie neuheitsschädlich; § 3 Abs. 5 "
                "PatG hilft nur bei Missbrauch oder amtlich anerkannter internationaler Ausstellung. § 6a GebrMG ist nicht nötig, schützt aber auch gegen Zwischenoffenbarungen Dritter."],
               merke="Eigene Vorveröffentlichung ≤ 6 Monate: Gebrauchsmuster (§ 3 Abs. 1 S. 3 GebrMG), nicht Patent.", level=1, concepts=G + ["pat_neuheit"],
               norms=["§ 3 Abs. 5 PatG"], abschnitt="Welche Anspruchsgrundlage?"),
            mc("p060-7", "Herstellungsverfahren schützen",
               "Die Mandantin hat ein neues Schweißverfahren entwickelt und will möglichst schnell ein eingetragenes Schutzrecht. Welcher Weg?",
               ["Gebrauchsmuster auf das Verfahren", "Gebrauchsmuster auf das Verfahrenserzeugnis nach § 9 S. 2 Nr. 3 PatG",
                "Patentanmeldung mit Prüfungsantrag; für das Verfahren ist kein Gebrauchsmuster möglich", "Gebrauchsmuster mit Recherche nach § 7 GebrMG"], 2,
               ["**Patentanmeldung.** Verfahren sind als Gebrauchsmuster nicht geschützt (§ 2 Nr. 3 GebrMG); die Gebrauchsmusterstelle prüft das bei "
                "der Eintragung (BGH Feldmausbekämpfung). Einen Erzeugnisschutz für Verfahrenserzeugnisse kennt § 11 Abs. 1 S. 2 GebrMG nicht. "
                "Ein Gebrauchsmuster bleibt nur für eine Vorrichtung, die selbst neu und erfinderisch ist (TS II/2020)."],
               merke="Verfahren → nur Patent; Gebrauchsmuster allenfalls für die Vorrichtung.", level=1, concepts=G + ["pat_patentkategorie"],
               norms=["§ 9 PatG"], cases=["pat_bgh_feldmausbekaempfung"], abschnitt="Welche Anspruchsgrundlage?"),
            fall("p060-8", "Ältere Anmeldung als Stand der Technik?",
                 "Ein Gebrauchsmuster wurde am 1.6.2025 angemeldet. Eine Patentanmeldung eines Dritten mit gleichem Inhalt ist vom 1.3.2025 und wurde im September 2026 offengelegt.",
                 "Gehört die Patentanmeldung des Dritten zum Stand der Technik des Gebrauchsmusters?", False,
                 ["**Nein!** Das GebrMG kennt keine Fiktion älterer nachveröffentlichter Anmeldungen (anders § 3 Abs. 2 PatG). Stand der Technik ist "
                  "nur, was vor dem Zeitrangtag schriftlich beschrieben oder im Inland benutzt und öffentlich zugänglich war (§ 3 Abs. 1 S. 2 GebrMG). "
                  "Erst wenn aus der älteren Anmeldung ein Schutzrecht mit identischem Gegenstand entsteht, greift der Löschungsgrund des § 15 Abs. 1 Nr. 2 GebrMG."],
                 merke="Ältere Rechte: Patent § 3 Abs. 2 PatG (Neuheit) – Gebrauchsmuster § 15 Abs. 1 Nr. 2 GebrMG (Doppelschutz).", level=2,
                 concepts=G + ["pat_doppelschutz", "pat_neuheit"], norms=["§ 3 Abs. 2 PatG"], abschnitt="Vergleich mit dem Patent"),
            fall("p060-9", "Schutz vor der Eintragung?",
                 "Die Mandantin hat aus ihrer Patentanmeldung vom 15.1.2024 ein Gebrauchsmuster abgezweigt; es wird am 10.9.2026 eingetragen. Ein Wettbewerber verkauft seit März 2026 Nachbauten.",
                 "Hat die Mandantin aus dem Gebrauchsmuster Schadensersatzansprüche für März bis August 2026?", False,
                 ["**Nein!** Die Wirkung des § 11 Abs. 1 GebrMG knüpft an die Eintragung an; erst ab dem 10.9.2026 ist die Benutzung verboten. Der "
                  "abgezweigte Anmeldetag bestimmt nur Zeitrang und Schutzdauer (§ 23 Abs. 1 GebrMG). Für die Zeit davor bleibt allenfalls die "
                  "Entschädigung aus der offengelegten Patentanmeldung (§ 33 Abs. 1 PatG)."],
                 merke="Gebrauchsmuster: Rechte erst ab Eintragung (§ 11 Abs. 1 GebrMG); Zeitrang ≠ Schutzbeginn.", level=2, concepts=A + ["pat_schadensersatz"],
                 norms=["§ 33 Abs. 1 PatG"], abschnitt="Vergleich mit dem Patent"),
            fall("p060-10", "Zehn plus zehn?",
                 "Ein Gebrauchsmuster wurde am 15.5.2026 angemeldet. Der Inhaber fragt, ob er die Schutzdauer wie bei einer Marke nach zehn Jahren verlängern kann.",
                 "Kann der Schutz über den 31.5.2036 hinaus verlängert werden?", False,
                 ["**Nein!** Die Schutzdauer endet zehn Jahre nach Ablauf des Monats, in den der Anmeldetag fällt (§ 23 Abs. 1 GebrMG), hier am "
                  "31.5.2036. Die Aufrechterhaltungsgebühren für das 4. bis 6., 7. und 8., 9. und 10. Jahr (§ 23 Abs. 2 GebrMG) erhalten den Schutz "
                  "nur innerhalb dieser Höchstdauer; ein Schutzzertifikat gibt es nicht."],
                 merke="Schutzdauer § 23 Abs. 1 GebrMG: Monatsende + zehn Jahre, keine Verlängerung.", level=1, concepts=G + ["pat_laufzeit_jahresgebuehren"],
                 abschnitt="Vergleich mit dem Patent"),
            mc("p060-11", "Mandant ist Arbeitgeber",
               "Ein Arbeitgeber fragt, ob er eine gemeldete, wohl patentfähige Diensterfindung statt zum Patent nur als Gebrauchsmuster anmelden darf (RP2 I/2021). Welche Norm entscheidet?",
               ["§ 13 Abs. 1 S. 2 ArbnErfG", "§ 5 Abs. 1 GebrMG", "§ 6 Abs. 1 ArbnErfG", "§ 1 Abs. 1 GebrMG"], 0,
               ["**§ 13 Abs. 1 S. 2 ArbnErfG.** Eine patentfähige Diensterfindung ist zum Patent anzumelden, sofern nicht bei verständiger Würdigung "
                "der Verwertbarkeit der Gebrauchsmusterschutz zweckdienlicher erscheint. Kurze Marktphase und geringe Kosten können dafür sprechen. "
                "Die Anmeldung muss unverzüglich erfolgen (§ 13 Abs. 1 S. 3 ArbnErfG)."],
               merke="Gebrauchsmuster statt Patent beim Arbeitgeber: § 13 Abs. 1 S. 2 ArbnErfG (zweckdienlicher).", level=2, concepts=G,
               norms=["§ 13 Abs. 1 ArbnErfG"], abschnitt="Welche Anspruchsgrundlage?"),
        ]),

        # ================================================================== §§ 1 bis 3 GebrMG
        dict(id="p06a", titel="§§ 1 bis 3 GebrMG: Schutzfähigkeit", einheiten=[
            intro("p06a-0", "Prüfungsschema",
                  "**AGL:** § 1 Abs. 1 GebrMG (Schutzfähigkeit; geprüft als Vorfrage der Eintragung § 8 Abs. 1 GebrMG, der Löschung § 15 Abs. 1 Nr. 1 GebrMG "
                  "und der Verletzung § 13 Abs. 1 GebrMG)\n\n"
                  "**A · Schutzgegenstand**\n"
                  "**V1 Erfindung** – § 1 Abs. 1 GebrMG: technische Lehre; kein Gegenstand des Ausschlusskatalogs **als solcher** (§ 1 Abs. 2, 3 GebrMG)\n"
                  "**V2 Kein Ausschluss nach § 2 GebrMG** – Nr. 1 ordre public, Nr. 2 Pflanzensorten und Tierarten, **Nr. 3 Verfahren**; dazu "
                  "biotechnologische Erfindungen (§ 1 Abs. 2 Nr. 5 GebrMG). Die Gebrauchsmusterstelle prüft § 2 GebrMG schon bei der Eintragung\n\n"
                  "**B · Neuheit (§ 3 Abs. 1 GebrMG)**\n"
                  "**V3 Zeitrangtag** – Anmeldetag (§ 4a Abs. 1 GebrMG), abgezweigter Anmeldetag (§ 5 Abs. 1 S. 1 GebrMG) oder Prioritätstag "
                  "(§ 5 Abs. 1 S. 2 GebrMG, § 6 GebrMG, § 6a GebrMG); je Schutzanspruch bestimmen\n"
                  "**V4 Stand der Technik** – § 3 Abs. 1 S. 2 GebrMG: **schriftliche Beschreibung** (weltweit) oder **Benutzung im Inland**, vor dem "
                  "Zeitrangtag der Öffentlichkeit zugänglich; nicht: mündliche Beschreibung, Auslandsbenutzung, ältere nachveröffentlichte Anmeldungen\n"
                  "**V5 Keine Neuheitsschonfrist** – § 3 Abs. 1 S. 3 GebrMG: Beschreibung oder Benutzung innerhalb von sechs Monaten vor dem Zeitrangtag "
                  "bleibt außer Betracht, wenn sie auf der Ausarbeitung des Anmelders oder seines Rechtsvorgängers beruht\n"
                  "**V6 Nicht neuheitsschädlich offenbart** – nicht alle Merkmale des Schutzanspruchs unmittelbar und eindeutig offenbart\n\n"
                  "**C · Erfinderischer Schritt und gewerbliche Anwendbarkeit**\n"
                  "**V7 Erfinderischer Schritt** – § 1 Abs. 1 GebrMG: Maßstab wie § 4 PatG (BGH Demonstrationsschrank), aber nur gegenüber dem SdT nach V4\n"
                  "**V8 Gewerbliche Anwendbarkeit** – § 3 Abs. 2 GebrMG\n\n"
                  "**⇒ Ergebnis:** schutzfähig; sonst Zurückweisung (nur V1/V2), Löschungsanspruch (§ 15 Abs. 1 Nr. 1 GebrMG) und kein Schutz (§ 13 Abs. 1 GebrMG)\n\n"
                  "**Klausurfallen:** Die Schonfrist gilt nur für das Gebrauchsmuster, nicht für ein Patent mit Priorität aus dem Gebrauchsmuster "
                  "(TS III/2022). Ausländische Messen und Vorführungen sind keine Benutzung im Inland, ein dort verteilter Prospekt ist aber eine "
                  "schriftliche Beschreibung (TS I/2021, TS II/2022). Fristen: Schonfrist sechs Monate rückwärts ab dem Zeitrangtag (§ 187 Abs. 1 BGB, "
                  "§ 188 Abs. 2 BGB entsprechend).\n\n"
                  "**In den Klausuren:** TS II/2018 (Vorführung im Schonzeitraum), TS II/2020 (Schweißverfahren), TS I/2021 (sieben Benutzungen, Bozen, "
                  "Prospekt), TS III/2021 (Fachartikel, Priorität je Anspruch), TS I/2022 (inzidente Prüfung), TS II/2022 (Las Vegas), TS III/2022 "
                  "(Blogeintrag eines Ex-Mitarbeiters), TS III/2023.",
                  concepts=G + ["pat_neuheit", "pat_erfinderische_taetigkeit"], norms=["§ 4 PatG", "§ 3 Abs. 2 PatG"],
                  cases=["pat_bgh_demonstrationsschrank", "pat_bgh_feldmausbekaempfung"], abschnitt="Normenkette"),
            intro("p06a-1", "Definitionen",
                  "**Erfindung:** Lehre zum planmäßigen Handeln unter Einsatz beherrschbarer Naturkräfte zur Erreichung eines kausal übersehbaren Erfolgs "
                  "(Rechtsprechung zu § 1 PatG, für § 1 Abs. 1 GebrMG gleich)\n"
                  "**Verfahren (§ 2 Nr. 3 GebrMG):** Lehre, die eine Folge von Handlungsschritten (Arbeits- oder Herstellungsverfahren) unter Schutz stellt; "
                  "kein Verfahren ist ein Verwendungsanspruch, in dem sich Sacheigenschaften manifestieren, und ein Erzeugnis ohne körperliches Substrat "
                  "wie eine Signalfolge (BGH Signalfolge; BPatG Lithiumsilikat-Glaskeramik)\n"
                  "**Neu:** nicht zum Stand der Technik gehörend (Legaldefinition § 3 Abs. 1 S. 1 GebrMG)\n"
                  "**Stand der Technik:** alle Kenntnisse, die vor dem für den Zeitrang maßgeblichen Tag durch schriftliche Beschreibung oder durch eine "
                  "im Inland erfolgte Benutzung der Öffentlichkeit zugänglich gemacht worden sind (Legaldefinition § 3 Abs. 1 S. 2 GebrMG)\n"
                  "**Schriftliche Beschreibung:** jede verkörperte, reproduzierbare Wiedergabe der Lehre (Druckschrift, Prospekt, Internetseite, "
                  "Gebrauchsmusterschrift), gleich wo veröffentlicht (Lehre)\n"
                  "**Öffentlich zugänglich:** nicht beschränkter Personenkreis hat die nicht nur theoretische Möglichkeit der Kenntnisnahme; bei einem "
                  "importierten Erzeugnis mit äußerlich nicht erkennbarer Lehre erst ab dem Angebot an Endkunden (BPatG Toilettendeckel aus Schichtverbundstoff)\n"
                  "**Ausarbeitung des Anmelders (§ 3 Abs. 1 S. 3 GebrMG):** die Offenbarung geht über eine lückenlose Kette der Wissensvermittlung "
                  "auf den Erfinder oder Anmelder zurück; auf Missbrauch oder Einverständnis kommt es nicht an; Anscheinsbeweis möglich (BPatG Tür- und Fenstersensor)\n"
                  "**Erfinderischer Schritt:** qualitatives Kriterium und Ergebnis einer Wertung wie die erfinderische Tätigkeit (BGH Demonstrationsschrank)\n"
                  "**Gewerblich anwendbar:** auf irgendeinem gewerblichen Gebiet einschließlich der Landwirtschaft herstellbar oder benutzbar "
                  "(Legaldefinition § 3 Abs. 2 GebrMG)",
                  concepts=G + ["pat_erfindung", "pat_neuheit", "pat_erfinderische_taetigkeit", "pat_gewerbliche_anwendbarkeit"],
                  cases=["pat_bgh_demonstrationsschrank", "pat_bgh_signalfolge", "pat_bpatg_lithiumsilikat_glaskeramik", "pat_bpatg_toilettendeckel",
                         "pat_bpatg_tuer_und_fenstersensor"], abschnitt="Definitionen"),
            mc("p06a-2", "Was ist Stand der Technik?",
               "Welche Offenbarung vor dem Zeitrangtag gehört zum Stand der Technik eines deutschen Gebrauchsmusters?",
               ["Ein Vortrag auf einer Konferenz in Berlin ohne Manuskript", "Die Vorführung des Geräts auf einer Messe in Las Vegas",
                "Ein Prospekt, der nur in Italien verteilt wurde", "Eine ältere, erst nach dem Zeitrangtag offengelegte Patentanmeldung"], 2,
               ["**Der italienische Prospekt.** Schriftliche Beschreibungen zählen weltweit (§ 3 Abs. 1 S. 2 GebrMG). Mündliche Beschreibungen "
                "zählen gar nicht, Benutzungen nur im Inland. Ältere nachveröffentlichte Anmeldungen sind kein Stand der Technik; dafür gibt es "
                "§ 15 Abs. 1 Nr. 2 GebrMG."],
               merke="SdT GebrM: schriftlich weltweit + Benutzung im Inland; nie mündlich, nie Auslandsbenutzung.", level=1, concepts=G + ["pat_neuheit"],
               abschnitt="Definitionen und Normen"),
            fall("p06a-3", "Erklärung auf der Messe",
                 "Der Vertriebsleiter eines Dritten erklärt auf einer Messe in München vor Publikum mündlich die Funktion der Erfindung, ohne das Gerät zu zeigen. Zwei Wochen später meldet die Mandantin ein Gebrauchsmuster an.",
                 "Ist die mündliche Erklärung Stand der Technik?", False,
                 ["**Nein!** § 3 Abs. 1 S. 2 GebrMG nennt nur die schriftliche Beschreibung und die Benutzung im Inland. Eine bloß mündliche Beschreibung "
                  "gehört nicht dazu, auch wenn sie im Inland öffentlich war. Wird das Gerät auf der Messe gezeigt oder vorgeführt, liegt dagegen eine "
                  "Benutzung im Inland vor (TS I/2021)."],
                 merke="Mündliche Beschreibung ist beim Gebrauchsmuster nie Stand der Technik.", level=1, concepts=G + ["pat_neuheit"],
                 abschnitt="Definitionen und Normen"),
            mc("p06a-4", "Reichweite der Schonfrist",
               "Für welche Offenbarung gilt die Neuheitsschonfrist des § 3 Abs. 1 S. 3 GebrMG?",
               ["Nur für Offenbarungen auf amtlich anerkannten Ausstellungen", "Nur bei offensichtlichem Missbrauch zum Nachteil des Anmelders",
                "Für jede Beschreibung oder Benutzung binnen sechs Monaten, die auf der Ausarbeitung des Anmelders oder Rechtsvorgängers beruht",
                "Für jede Offenbarung binnen zwölf Monaten vor dem Anmeldetag"], 2,
               ["**Ausarbeitung des Anmelders.** Erfasst sind eigene Veröffentlichungen und solche Dritter, die auf das Wissen des Anmelders "
                "zurückgehen, auch ohne Missbrauch (BPatG Tür- und Fenstersensor). Die Frist von sechs Monaten rechnet ab dem Zeitrangtag, also "
                "auch ab dem Prioritäts- oder abgezweigten Anmeldetag. Unabhängige Offenbarungen Dritter deckt sie nicht."],
               merke="Schonfrist § 3 Abs. 1 S. 3 GebrMG: 6 Monate vor Zeitrangtag · eigene Ausarbeitung · kein Missbrauch nötig.", level=1,
               concepts=G + ["pat_neuheit"], cases=["pat_bpatg_tuer_und_fenstersensor"], abschnitt="Definitionen und Normen"),
            fall("p06a-5", "Schonfrist über die Priorität ins Patent?",
                 "M meldet am 15.4.2019 ein Gebrauchsmuster an und am 13.3.2020 ein Patent mit dessen innerer Priorität. Ein Ex-Mitarbeiter veröffentlichte die Erfindung am 3.2.2019 im Internet.",
                 "Schützt die Schonfrist des § 3 Abs. 1 S. 3 GebrMG auch das Patent vor dem Blogeintrag?", False,
                 ["**Nein!** Die Schonfrist gilt nur für das Gebrauchsmuster. Für das Patent ist der Blogeintrag vor dem Prioritätstag Stand der "
                  "Technik (§ 3 Abs. 1 PatG). § 3 Abs. 5 S. 1 Nr. 1 PatG hilft nur bei Missbrauch und rechnet ab der tatsächlichen Einreichung "
                  "(13.3.2020); der 3.2.2019 liegt außerhalb der sechs Monate (TS III/2022)."],
                 merke="Schonfrist des GebrMG wirkt nicht über die Priorität für ein Patent.", level=3, concepts=G + ["pat_neuheit", "pat_prioritaet"],
                 norms=["§ 3 Abs. 1 PatG", "§ 3 Abs. 5 PatG", "§ 40 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06a-6", "Signalfolge als Verfahren?",
                 "Die Anmelderin beansprucht als Gebrauchsmuster eine Signalfolge, die ein Programm zum Ablauf auf einem Rechner darstellt. Die Gebrauchsmusterstelle meint, ohne körperliches Substrat liege ein Verfahren vor.",
                 "Steht § 2 Nr. 3 GebrMG der Eintragung entgegen?", False,
                 ["**Nein!** Aus dem Fehlen eines beständigen körperlichen Substrats folgt nicht, dass ein Verfahren vorliegt (BGH Signalfolge). Verfahren "
                  "im Sinne des § 2 Nr. 3 GebrMG sind Arbeits- und Herstellungsverfahren. Ob die Signalfolge technisch ist und nicht als Programm als "
                  "solches ausgeschlossen ist, prüft man getrennt (§ 1 Abs. 2 Nr. 3, Abs. 3 GebrMG)."],
                 merke="§ 2 Nr. 3 GebrMG: Arbeits- und Herstellungsverfahren; unkörperliche Erzeugnisse sind keine Verfahren.", level=3,
                 concepts=G + ["pat_programme", "pat_patentkategorie"], cases=["pat_bgh_signalfolge"], abschnitt="Definitionen und Normen"),
            mc("p06a-7", "Wer prüft was?",
               "Welche Schutzvoraussetzung prüft die Gebrauchsmusterstelle vor der Eintragung?",
               ["Neuheit nach § 3 Abs. 1 GebrMG", "Erfinderischen Schritt nach § 1 Abs. 1 GebrMG",
                "Den Ausschluss von Verfahren nach § 2 Nr. 3 GebrMG", "Gewerbliche Anwendbarkeit nach § 3 Abs. 2 GebrMG"], 2,
               ["**§ 2 Nr. 3 GebrMG.** Neuheit, erfinderischer Schritt und gewerbliche Anwendbarkeit werden nicht geprüft (§ 8 Abs. 1 S. 2 GebrMG). "
                "Die Schutzhindernisse des § 2 GebrMG und die formalen Erfordernisse der §§ 4, 4a, 4b GebrMG prüft die Gebrauchsmusterstelle dagegen "
                "(BGH Feldmausbekämpfung). Der Rest bleibt dem Löschungs- oder Verletzungsverfahren."],
               merke="Eintragung: Form + § 2 GebrMG; Neuheit, Schritt, Anwendbarkeit erst bei Löschung/Verletzung.", level=1, concepts=G,
               cases=["pat_bgh_feldmausbekaempfung"], abschnitt="Definitionen und Normen"),
            *fallkette("p06a-8", "Sieben Benutzungen (nach TS I/2021)",
                "Munich Cool meldet am 11.5.2016 ein Patent an und am 8.6.2016 ein Gebrauchsmuster mit dessen innerer Priorität. Vorher zeigte sie das "
                "Gerät im März 2016 selbst auf einer Messe in München. Calfreddo bot ein gleiches Gerät in Bozen an und schickte einen Prospekt mit "
                "Leistungsdaten nach Garmisch.",
                [frage("Ist für den Stand der Technik auf den 11.5.2016 abzustellen?", True,
                       ["**Ja!** Maßgeblich ist der für den Zeitrang der Anmeldung maßgebliche Tag (§ 3 Abs. 1 S. 2 GebrMG). Die innere Priorität der "
                        "DPMA-Patentanmeldung ist binnen zwölf Monaten wirksam beansprucht (§ 6 Abs. 1 S. 1 GebrMG); die Patentanmeldung gilt dabei nicht "
                        "als zurückgenommen (§ 6 Abs. 1 S. 2 GebrMG)."],
                       merke="Zeitrang: Anmeldetag oder Prioritätstag, je Schutzanspruch.", norms=["§ 40 PatG"], concepts=["pat_prioritaet"]),
                 frage("Ist die eigene Messevorführung vom März 2016 neuheitsschädlich?", False,
                       ["**Nein!** Sie ist eine Benutzung im Inland, beruht aber auf der Ausarbeitung der Anmelderin und liegt innerhalb von sechs Monaten "
                        "vor dem Zeitrangtag 11.5.2016, also nach dem 11.11.2015. Sie bleibt außer Betracht (§ 3 Abs. 1 S. 3 GebrMG)."],
                       merke="Eigene Benutzung im Schonzeitraum bleibt außer Betracht."),
                 frage("Ist das Angebot der Geräte in Bozen Stand der Technik?", False,
                       ["**Nein!** Benutzungen zählen nur, wenn sie im Geltungsbereich des GebrMG erfolgt sind (§ 3 Abs. 1 S. 2 GebrMG). Das Angebot in "
                        "Italien ist eine Auslandsbenutzung, auch wenn deutsche Fachkreise davon wussten."],
                       merke="Auslandsbenutzung ist kein Stand der Technik des Gebrauchsmusters."),
                 frage("Macht der nach Garmisch geschickte Prospekt das Gebrauchsmuster neuheitsschädlich vorweg?", False,
                       ["**Nein!** Ein Prospekt ist eine schriftliche Beschreibung und zählt weltweit. Neuheitsschädlich ist er aber nur, wenn er alle "
                        "Merkmale des Schutzanspruchs offenbart. Bloße Leistungsdaten offenbaren die technische Lehre nicht."],
                       merke="Schriftliche Beschreibung schadet nur, soweit sie die Lehre vollständig offenbart."),
                 frage("Calfreddo veröffentlichte am 2.5.2016 ein italienisches Handbuch mit allen Merkmalen. Hilft der Anmelderin die Schonfrist?", False,
                       ["**Nein!** Das Handbuch ist eine schriftliche Beschreibung vor dem Zeitrangtag und offenbart alle Merkmale. Die Schonfrist deckt "
                        "nur Offenbarungen, die auf der Ausarbeitung der Anmelderin beruhen; Calfreddo hat unabhängig entwickelt. Die Schutzansprüche "
                        "sind nicht neu; Löschungsgrund § 15 Abs. 1 Nr. 1 GebrMG."],
                       merke="Unabhängige Drittoffenbarung: keine Schonfrist.", concepts=L),
                ], abschnitt="Klausurfall", level=2, concepts=G + ["pat_neuheit"]),
            *fallkette("p06a-9", "Schweißverfahren (nach TS II/2020)",
                "Die PI GmbH hat ein schnelleres und billigeres Verfahren zum Verschweißen von Gehäusen entwickelt. Die Gehäuse selbst sind bekannt. Sie "
                "will sofort ein Gebrauchsmuster, weil das Patent erst in Jahren erteilt wäre.",
                [frage("Kann das Schweißverfahren als Gebrauchsmuster eingetragen werden?", False,
                       ["**Nein!** Verfahren werden als Gebrauchsmuster nicht geschützt (§ 2 Nr. 3 GebrMG). Die Gebrauchsmusterstelle prüft diesen "
                        "Ausschluss schon im Eintragungsverfahren und weist die Anmeldung zurück, wenn nicht auf Sachansprüche umgestellt wird "
                        "(BGH Feldmausbekämpfung)."],
                       merke="Verfahrensanspruch → Zurückweisung der GebrM-Anmeldung.", cases=["pat_bgh_feldmausbekaempfung"]),
                 frage("Schützt ein Gebrauchsmuster auf die Schweißvorrichtung auch die mit dem Verfahren hergestellten Gehäuse?", False,
                       ["**Nein!** § 11 Abs. 1 S. 2 GebrMG verbietet nur Handlungen mit einem Erzeugnis, das Gegenstand des Gebrauchsmusters ist. "
                        "Einen Schutz unmittelbarer Verfahrenserzeugnisse wie § 9 S. 2 Nr. 3 PatG kennt das GebrMG nicht."],
                       merke="Kein Verfahrenserzeugnisschutz im GebrMG.", norms=["§ 9 PatG"], concepts=["pat_verfahrenserzeugnis"]),
                 frage("Ist ein Gebrauchsmuster auf die bekannten Gehäuse schutzfähig?", False,
                       ["**Nein!** Ein Sachanspruch ist zwar zulässig, muss aber selbst neu sein und auf einem erfinderischen Schritt beruhen "
                        "(§ 1 Abs. 1 GebrMG). Liegt das Neue allein im Verfahren, fehlt dem Gehäuse die Neuheit. Bleibt nur die Patentanmeldung "
                        "für das Verfahren."],
                       merke="Neuheit im Verfahren trägt keinen Sachanspruch."),
                ], abschnitt="Klausurfall", level=1, concepts=G + ["pat_patentkategorie"]),
        ]),

        # ================================================================== § 5 GebrMG
        dict(id="p06b", titel="§ 5 GebrMG: Abzweigung", einheiten=[
            intro("p06b-0", "Prüfungsschema",
                  "**AGL:** § 5 Abs. 1 S. 1 GebrMG (Inanspruchnahme des Anmeldetags der Patentanmeldung für die Gebrauchsmusteranmeldung)\n\n"
                  "**A · Voraussetzungen der Abzweigung**\n"
                  "**V1 Frühere Patentanmeldung mit Wirkung für Deutschland** – § 5 Abs. 1 S. 1 GebrMG: deutsche Anmeldung, europäische Anmeldung mit "
                  "Benennung DE (Art. 66 EPÜ) oder internationale Anmeldung mit Bestimmung DE (Art. 11 Abs. 3 PCT, Art. III § 4 Abs. 1 IntPatÜG); auch "
                  "Teilanmeldung; mindestens einen Tag vor der GebrM-Anmeldung\n"
                  "**V2 Derselbe Anmelder** – § 5 Abs. 1 S. 1 GebrMG: Anmelder der Patentanmeldung oder sein Rechtsnachfolger; der durch Entnahme "
                  "Verletzte nur nach Rechtsübergang (BGH Angussvorrichtung für Spritzgießwerkzeuge II, X ZB 3/08)\n"
                  "**V3 Dieselbe Erfindung** – § 5 Abs. 1 S. 1 GebrMG: nicht über den Inhalt der Patentanmeldung hinaus; eine Erweiterung macht die "
                  "Abzweigung nicht unwirksam, gibt aber keine Rechte (BGH Momentanpol, X ZR 226/00; § 15 Abs. 1 Nr. 3 GebrMG)\n"
                  "**V4 Abzweigungserklärung mit der Gebrauchsmusteranmeldung** – § 5 Abs. 1 S. 1 GebrMG; auf Aufforderung binnen zwei Monaten "
                  "Aktenzeichen, Anmeldetag, Abschrift (entbehrlich bei DPMA-Anmeldung), sonst Verwirkung (§ 5 Abs. 2 GebrMG)\n"
                  "**V5 Frist** – § 5 Abs. 1 S. 3 GebrMG: bis zwei Monate nach Ende des Monats, in dem die Patentanmeldung **erledigt** oder ein "
                  "etwaiges **Einspruchsverfahren abgeschlossen** ist, längstens bis Ablauf des **zehnten Jahres** nach dem Anmeldetag · Berechnung "
                  "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB; keine Frühgrenze\n"
                  "**V6 Anmeldeerfordernisse** – § 4 Abs. 3 GebrMG, § 4a GebrMG, deutsche Übersetzung binnen drei Monaten (§ 4b GebrMG); Anmeldegebühr "
                  "30 EUR (Nr. 321 000 Anlage PatKostG), 40 EUR Papier (Nr. 321 100), zahlbar binnen drei Monaten (§ 6 Abs. 1 S. 2 PatKostG); "
                  "kein Verfahren (§ 2 Nr. 3 GebrMG)\n\n"
                  "**B · Rechtsfolge**\n"
                  "**⇒** Anmeldetag der Patentanmeldung (§ 5 Abs. 1 S. 1 GebrMG); deren Priorität bleibt erhalten, aber nur so wirksam wie dort "
                  "(§ 5 Abs. 1 S. 2 GebrMG); Schutzdauer ab dem in Anspruch genommenen Anmeldetag (§ 23 Abs. 1 GebrMG); Eintragung ohne Sachprüfung "
                  "(§ 8 Abs. 1 S. 2 GebrMG); Schutzwirkung erst ab Eintragung (§ 11 Abs. 1 GebrMG). Verspätet: kein Anmeldetag, Zurückweisung; eigene "
                  "Offenlegung wird Stand der Technik (BGH Sintervorrichtung, X ZB 26/98)\n\n"
                  "**Klausurfallen:** „Erledigt“ ist die Anmeldung mit Rechtskraft der Zurückweisung, mit Rücknahme, Rücknahmefiktion oder Erteilung; "
                  "läuft ein Einspruch, beginnt die Frist erst mit dessen Abschluss. Die Abzweigung ist auch während des Einspruchs oder vor der "
                  "Erteilung zulässig. Der Bestand ist eine zweite Frage: Ist die Erfindung wegen schriftlicher Vorveröffentlichungen nicht neu, "
                  "wird das Gebrauchsmuster zwar eingetragen, ist aber löschungsreif (TS III/2023).\n\n"
                  "**In den Klausuren:** TS II/2018, TS II/2019 (PCT-Basis, drei Abzweigungen, Einspruch), TS III/2019 (zu spät), TS II/2020, TS I/2021 "
                  "(aus Stamm- und Teilanmeldung), TS III/2021, TS I/2022, TS II/2022, TS III/2022, TS II/2023, TS III/2023 (nach Rücknahme).",
                  concepts=A + G, norms=["Art. 66 EPÜ", "Art. III § 4 Abs. 1 IntPatÜG", "§ 6 Abs. 1 PatKostG"], abschnitt="Normenkette"),
            intro("p06b-1", "Definitionen",
                  "**Abzweigung:** Inanspruchnahme des für eine frühere Patentanmeldung maßgebenden Anmeldetags durch Erklärung in der "
                  "Gebrauchsmusteranmeldung (§ 5 Abs. 1 S. 1 GebrMG)\n"
                  "**Patent nachgesucht mit Wirkung für Deutschland:** Patentanmeldung, die in Deutschland die Wirkung einer nationalen Anmeldung hat – "
                  "DPMA-Anmeldung, Euro-PCT oder europäische Anmeldung mit Benennung DE (Art. 66 EPÜ), PCT-Anmeldung mit Bestimmung DE (Art. 11 Abs. 3 PCT)\n"
                  "**Dieselbe Erfindung:** der Gegenstand der Gebrauchsmusteranmeldung ist in der Patentanmeldung offenbart; aus Erweiterungen folgen "
                  "keine Rechte (BGH Momentanpol)\n"
                  "**Erledigt:** die Patentanmeldung ist nicht mehr anhängig – durch rechtskräftige Zurückweisung, Rücknahme, Rücknahmefiktion "
                  "(etwa § 58 Abs. 3 PatG, § 6 Abs. 2 PatKostG) oder Erteilung (Lehre; TS III/2023: auch die Rücknahme)\n"
                  "**Einspruchsverfahren abgeschlossen:** bestandskräftige Entscheidung über den Einspruch oder Ende des Verfahrens nach Rücknahme "
                  "und Einstellung (§ 5 Abs. 1 S. 3 GebrMG)\n"
                  "**Anmeldetag (abgezweigt):** der für die Patentanmeldung maßgebende Anmeldetag, bei PCT das internationale Anmeldedatum; nicht "
                  "der Prioritätstag (§ 5 Abs. 1 S. 1, 2 GebrMG)",
                  concepts=A, norms=["Art. 66 EPÜ", "§ 58 Abs. 3 PatG", "§ 6 Abs. 2 PatKostG"], abschnitt="Definitionen"),
            mc("p06b-2", "Abzweigungsfrist",
               "Bis wann kann das Abzweigungsrecht ausgeübt werden?",
               ["Bis zwei Monate nach Erledigung der Patentanmeldung",
                "Bis zwei Monate nach Ende des Monats der Erledigung oder des Abschlusses eines Einspruchs, längstens bis Ablauf des zehnten Jahres",
                "Bis zwölf Monate nach dem Anmeldetag der Patentanmeldung", "Bis zur Veröffentlichung der Erteilung"], 1,
               ["**§ 5 Abs. 1 S. 3 GebrMG.** Die Frist knüpft an das Monatsende an: zwei Monate nach Ende des Monats, in dem die Patentanmeldung "
                "erledigt oder ein etwaiges Einspruchsverfahren abgeschlossen ist. Die Höchstgrenze ist der Ablauf des zehnten Jahres nach dem "
                "Anmeldetag der Patentanmeldung. Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB, Verschiebung § 193 BGB."],
               merke="Frist § 5 Abs. 1 S. 3 GebrMG · Berechnung § 187 Abs. 1, § 188 Abs. 2 BGB · Verschiebung § 193 BGB.", level=1, concepts=A + ["pat_fristen"],
               abschnitt="Definitionen und Normen"),
            fall("p06b-3", "Fristende am Wochenende",
                 "Die Bohr AG nimmt ihre Patentanmeldung am 20.8.2026 zurück. Am Montag, 2.11.2026, reicht sie eine Gebrauchsmusteranmeldung mit Abzweigungserklärung ein.",
                 "Ist die Abzweigung rechtzeitig?", True,
                 ["**Ja!** Mit der Rücknahme ist die Anmeldung im August erledigt. Die Frist beginnt mit Ablauf des 31.8.2026 und endet zwei Monate "
                  "später am 31.10.2026 (§ 5 Abs. 1 S. 3 GebrMG, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB). Das ist ein Samstag; die Frist endet daher am "
                  "Montag, 2.11.2026 (§ 193 BGB)."],
                 merke="Rücknahme = Erledigung; Monatsende + zwei Monate; § 193 BGB beachten.", level=2, concepts=A + ["pat_fristen"],
                 abschnitt="Definitionen und Normen"),
            fall("p06b-4", "Abzweigung aus der PCT-Anmeldung",
                 "Die Elektro AG hat eine internationale Anmeldung beim EPA mit Bestimmung DE eingereicht. Die nationale Phase ist später ordnungsgemäß eingeleitet. Vorher meldet sie ein Gebrauchsmuster mit Abzweigungserklärung an.",
                 "Kann der internationale Anmeldetag in Anspruch genommen werden?", True,
                 ["**Ja!** Mit Wirkung für Deutschland ist ein Patent auch durch eine internationale Anmeldung mit Bestimmung DE nachgesucht; sie hat "
                  "ab dem internationalen Anmeldedatum die Wirkung einer nationalen Anmeldung (Art. 11 Abs. 3 PCT). Eine Frühgrenze kennt § 5 Abs. 1 "
                  "S. 3 GebrMG nicht. Die Abschrift kann das DPMA anfordern, weil die Anmeldung nicht dort eingereicht wurde (§ 5 Abs. 2 S. 1, 2 GebrMG)."],
                 merke="Basis der Abzweigung: DE, EP mit DE, PCT mit DE.", level=2, concepts=A + ["pat_pct_nationale_phase"],
                 norms=["Art. III § 4 Abs. 1 IntPatÜG"], abschnitt="Definitionen und Normen"),
            fall("p06b-5", "Der Verletzte zweigt ab",
                 "Nolte hat erfolgreich wegen widerrechtlicher Entnahme Einspruch gegen das Patent der Ackermanns eingelegt. Ohne Übertragung des Patents will er aus deren Anmeldung ein Gebrauchsmuster abzweigen.",
                 "Kann Nolte den Anmeldetag der Patentanmeldung der Ackermanns in Anspruch nehmen?", False,
                 ["**Nein!** Abzweigen kann nur der Anmelder der Patentanmeldung oder sein Rechtsnachfolger. Ohne Übergang des Rechts kann der durch "
                  "widerrechtliche Entnahme Verletzte den Anmeldetag nicht nutzen (BGH Angussvorrichtung für Spritzgießwerkzeuge II, X ZB 3/08). Er hat "
                  "das Nachanmelderecht des § 7 Abs. 2 PatG oder die Vindikation nach § 8 PatG."],
                 merke="Abzweigung nur durch den Anmelder; Verletzter: § 7 Abs. 2 PatG, § 8 PatG.", level=3, concepts=A + ["pat_recht_auf_patent"],
                 norms=["§ 7 Abs. 2 PatG", "§ 8 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06b-6", "Erweiterte Schutzansprüche",
                 "Die abgezweigte Gebrauchsmusteranmeldung enthält einen Schutzanspruch mit einem Merkmal, das in der Patentanmeldung nicht offenbart ist.",
                 "Ist die Abzweigung deshalb insgesamt unwirksam?", False,
                 ["**Nein!** Dass die abgezweigte Anmeldung über die Patentanmeldung hinausgeht, steht der Wirksamkeit der Abzweigung als solcher "
                  "nicht entgegen; aus der Erweiterung können aber keine Rechte hergeleitet werden (BGH Momentanpol, X ZR 226/00). Insoweit droht "
                  "die Löschung nach § 15 Abs. 1 Nr. 3 GebrMG."],
                 merke="Erweiterung: Abzweigung wirksam, aber keine Rechte aus dem Überschuss.", level=2, concepts=A + ["pat_unzulaessige_erweiterung"],
                 abschnitt="Definitionen und Normen"),
            fall("p06b-7", "Priorität geht mit",
                 "Die Patentanmeldung DE 456 nimmt wirksam die innere Priorität der DE 450 in Anspruch. Aus DE 456 wird ein Gebrauchsmuster abgezweigt. Herr Müller meint, die Priorität gehe dabei verloren.",
                 "Hat Herr Müller recht?", False,
                 ["**Nein!** Ein für die Patentanmeldung beanspruchtes Prioritätsrecht bleibt für die Gebrauchsmusteranmeldung erhalten (§ 5 Abs. 1 "
                  "S. 2 GebrMG). Es trägt aber nur so weit wie bei der Patentanmeldung: nur für Merkmale, die in der früheren Anmeldung deutlich "
                  "offenbart sind (§ 40 Abs. 3 PatG), also je Schutzanspruch prüfen (TS III/2021)."],
                 merke="Abzweigung übernimmt Anmeldetag und Priorität (§ 5 Abs. 1 S. 1, 2 GebrMG).", level=2, concepts=A + ["pat_prioritaet"],
                 norms=["§ 40 Abs. 3 PatG"], abschnitt="Definitionen und Normen"),
            mc("p06b-8", "Schutzdauer des abgezweigten Gebrauchsmusters",
               "Die Patentanmeldung hat den Anmeldetag 1.6.2015 und die Priorität vom 4.6.2014. Das abgezweigte Gebrauchsmuster wird 2017 eingereicht. Wann endet sein Schutz spätestens?",
               ["30.6.2024", "30.6.2025", "30.6.2027", "31.12.2027"], 1,
               ["**30.6.2025.** Die Schutzdauer beginnt mit dem Anmeldetag und endet zehn Jahre nach Ablauf des Anmeldemonats (§ 23 Abs. 1 GebrMG). "
                "Maßgeblich ist der in Anspruch genommene Anmeldetag 1.6.2015, nicht der Prioritätstag und nicht der Eingang der Abzweigung (TS II/2019). "
                "Das Monatsende wird nicht nach § 193 BGB verschoben."],
               merke="Abgezweigtes GBM: Schutz endet 10 Jahre nach Ende des Monats des Patent-Anmeldetags.", level=2,
               concepts=A + ["pat_laufzeit_jahresgebuehren"], abschnitt="Definitionen und Normen"),
            *fallkette("p06b-9", "Drei Abzweigungen (nach TS II/2019)",
                "Die Elektro AG hat am 1.6.2015 eine PCT-Anmeldung mit Bestimmung DE eingereicht (nationale Phase DE 333). Sie zweigt GBM 666 am "
                "10.7.2015 ab, GBM 555 am 1.6.2017 nach dem Erteilungsbeschluss, aber vor dessen Unanfechtbarkeit. Gegen das erteilte Patent läuft "
                "seit dem 10.4.2018 ein Einspruch; GBM 777 folgt am 25.4.2018.",
                [frage("Ist GBM 666 trotz der frühen Einreichung rechtzeitig abgezweigt?", True,
                       ["**Ja!** § 5 Abs. 1 S. 3 GebrMG setzt nur ein Fristende, keine Frühgrenze. Die PCT-Anmeldung wirkt ab dem 1.6.2015 als "
                        "nationale Anmeldung (Art. 11 Abs. 3 PCT); damit war das Patent „früher“ nachgesucht."],
                       merke="Keine Frühgrenze; frühere Anmeldung mindestens einen Tag vorher."),
                 frage("Ist GBM 555 rechtzeitig, obwohl der Erteilungsbeschluss schon ergangen war?", True,
                       ["**Ja!** Bis zur Unanfechtbarkeit des Erteilungsbeschlusses ist die Anmeldung noch anhängig, also nicht erledigt (§ 73 Abs. 2 "
                        "S. 1 PatG: ein Monat Beschwerdefrist). Danach läuft die Frist noch zwei Monate nach Monatsende."],
                       merke="Erteilungsbeschluss allein erledigt die Anmeldung nicht.", norms=["§ 73 Abs. 2 PatG"]),
                 frage("Kann GBM 777 noch während des laufenden Einspruchs abgezweigt werden?", True,
                       ["**Ja!** Die Frist endet erst zwei Monate nach Ende des Monats, in dem ein etwaiges Einspruchsverfahren abgeschlossen ist "
                        "(§ 5 Abs. 1 S. 3 GebrMG). Während des Einspruchs ist die Abzweigung jederzeit möglich, höchstens bis zum Ablauf des zehnten "
                        "Jahres nach dem 1.6.2015."],
                       merke="Einspruch verlängert die Abzweigungsfrist bis zu seinem Abschluss.", concepts=["pat_einspruch"]),
                 frage("Erhalten die Gebrauchsmuster als Zeitrang den 1.6.2015?", True,
                       ["**Ja!** Sie erhalten den für die Patentanmeldung maßgebenden Anmeldetag, bei PCT das internationale Anmeldedatum (§ 5 Abs. 1 "
                        "S. 1 GebrMG). Eine für die Patentanmeldung beanspruchte Priorität bliebe erhalten (§ 5 Abs. 1 S. 2 GebrMG), aber nur, wenn sie "
                        "dort wirksam war."],
                       merke="Zeitrang = Anmeldetag der Patentanmeldung (+ deren Priorität)."),
                 frage("Muss die Elektro AG auf Aufforderung eine Abschrift der Patentanmeldung einreichen?", True,
                       ["**Ja!** Das DPMA fordert binnen zwei Monaten nach Zustellung Aktenzeichen, Anmeldetag und Abschrift an (§ 5 Abs. 2 S. 1 GebrMG). "
                        "Entbehrlich ist die Abschrift nur bei einer DPMA-Anmeldung (§ 5 Abs. 2 S. 2 GebrMG); die PCT-Anmeldung ging beim EPA ein. "
                        "Versäumnis: Verwirkung (§ 5 Abs. 2 S. 3 GebrMG)."],
                       merke="Frist § 5 Abs. 2 S. 1 GebrMG (2 Monate ab Zustellung) · Folge Verwirkung S. 3."),
                ], abschnitt="Klausurfall", level=2, concepts=A),
            *fallkette("p06b-10", "Rettung nach der Rücknahme (nach TS III/2023)",
                "Die Anmelderin hat ihre Patentanmeldung DE1 vom 1.7.2018 am 17.2.2020 wirksam zurückgenommen. Die Erfindung ist eine Fahrradbremse. "
                "Eine Druckschrift E2 von 2017 nimmt den Inhalt von DE1 vorweg. Sie fragt, was ihr bleibt.",
                [frage("Kann sie aus der zurückgenommenen DE1 noch ein Gebrauchsmuster abzweigen?", True,
                       ["**Ja!** Auch die Rücknahme erledigt die Anmeldung. Die Frist läuft bis zwei Monate nach Ende des Februars 2020, also bis "
                        "30.4.2020 (§ 5 Abs. 1 S. 3 GebrMG, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB; § 193 BGB greift nicht, Donnerstag)."],
                       merke="Rücknahme startet die Abzweigungsfrist sofort."),
                 frage("Steht § 2 Nr. 3 GebrMG der Abzweigung entgegen?", False,
                       ["**Nein!** Die Bremse ist eine Vorrichtung, kein Verfahren. Verfahrensansprüche der Patentanmeldung dürften nicht übernommen "
                        "werden; Sachansprüche sind gebrauchsmusterfähig."],
                       merke="Bei der Abzweigung nur Sachansprüche übernehmen."),
                 frage("Wird das Gebrauchsmuster eingetragen?", True,
                       ["**Ja!** Neuheit und erfinderischer Schritt werden nicht geprüft (§ 8 Abs. 1 S. 2 GebrMG). Bei formgerechter Anmeldung, "
                        "Übersetzung (§ 4b GebrMG) und Gebühr von 30 EUR (Nr. 321 000 Anlage PatKostG) wird eingetragen."],
                       merke="Eintragung ohne Sachprüfung (§ 8 Abs. 1 S. 2 GebrMG)."),
                 frage("Ist das Gebrauchsmuster rechtsbeständig?", False,
                       ["**Nein!** E2 ist eine schriftliche Beschreibung vor dem Zeitrangtag und zählt weltweit (§ 3 Abs. 1 S. 2 GebrMG); die "
                        "Schonfrist hilft nicht, E2 stammt nicht von der Anmelderin. Jedermann kann Löschung verlangen (§ 15 Abs. 1 Nr. 1 GebrMG); im "
                        "Verletzungsprozess entsteht kein Schutz (§ 13 Abs. 1 GebrMG)."],
                       merke="Eintragung ≠ Bestand: schriftlicher SdT schadet dem GBM wie dem Patent.", concepts=L),
                ], abschnitt="Klausurfall", level=2, concepts=A),
        ]),

        # ================================================================== §§ 6, 6a GebrMG
        dict(id="p06c", titel="§§ 6, 6a GebrMG: Priorität", einheiten=[
            intro("p06c-0", "Prüfungsschema",
                  "**AGL:** § 6 Abs. 1 S. 1 GebrMG (innere Priorität) · § 6 Abs. 2 GebrMG i.V.m. § 41 PatG, Art. 4 PVÜ (Unionspriorität) · § 6a Abs. 1 GebrMG "
                  "(Ausstellungspriorität)\n\n"
                  "**A · Innere Priorität (§ 6 Abs. 1 GebrMG)**\n"
                  "**V1 Frühere Anmeldung beim DPMA** – § 6 Abs. 1 S. 1 GebrMG: Patent- **oder** Gebrauchsmusteranmeldung, eingereicht beim DPMA (Anmeldungen beim EPA oder im Ausland: Unionspriorität)\n"
                  "**V2 Keine Kettenpriorität** – § 6 Abs. 1 S. 1 GebrMG: für die frühere Anmeldung ist keine inländische oder ausländische Priorität beansprucht\n"
                  "**V3 Dieselbe Erfindung, derselbe Anmelder** – § 6 Abs. 1 S. 1 GebrMG; Priorität nur für Merkmale, die in der Gesamtheit der früheren "
                  "Unterlagen deutlich offenbart sind (§ 6 Abs. 1 S. 2 GebrMG i.V.m. § 40 Abs. 3 PatG); mehrere Prioritäten möglich (§ 40 Abs. 2 PatG)\n"
                  "**V4 Frist** – zwölf Monate nach dem Anmeldetag der früheren Anmeldung (§ 6 Abs. 1 S. 1 GebrMG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · "
                  "§ 193 BGB · keine Wiedereinsetzung (§ 21 Abs. 1 GebrMG i.V.m. § 123 Abs. 1 S. 2 Nr. 3 PatG)\n"
                  "**V5 Erklärung** – binnen zwei Monaten nach dem Anmeldetag der späteren Anmeldung, wirksam erst mit Aktenzeichen (§ 6 Abs. 1 S. 2 "
                  "GebrMG i.V.m. § 40 Abs. 4 PatG)\n"
                  "**⇒ Rechtsfolge:** Zeitrang des Prioritätstags für SdT und Schonfrist (§ 3 Abs. 1 GebrMG); **keine Rücknahmefiktion für eine frühere "
                  "Patentanmeldung** (§ 6 Abs. 1 S. 2 GebrMG mit Maßgabe zu § 40 Abs. 5 S. 1 PatG); eine noch anhängige frühere Gebrauchsmusteranmeldung "
                  "gilt als zurückgenommen; Schutzdauer ab dem eigenen Anmeldetag (§ 23 Abs. 1 GebrMG)\n\n"
                  "**B · Unionspriorität (§ 6 Abs. 2 GebrMG)**\n"
                  "**V1** erste Anmeldung eines Patents oder Gebrauchsmusters in einem Verbandsstaat (Art. 4 A Abs. 1 PVÜ; Gebrauchsmuster aus Patent und "
                  "umgekehrt, Art. 4 E Abs. 2 PVÜ) · **V2** zwölf Monate (Art. 4 C Abs. 1 PVÜ) · **V3** Angaben und Abschrift bis Ablauf des 16. Monats "
                  "nach dem Prioritätstag, sonst Verwirkung (§ 41 Abs. 1 PatG)\n\n"
                  "**C · Ausstellungspriorität (§ 6a GebrMG)**\n"
                  "**V1** Zurschaustellung auf einer amtlich bekanntgemachten Ausstellung (§ 6a Abs. 1 bis 3 GebrMG) · **V2** Anmeldung binnen sechs "
                  "Monaten seit der ersten Zurschaustellung · **V3** Tag und Ausstellung angeben und Nachweis einreichen vor Ablauf des 16. Monats "
                  "(§ 6a Abs. 4 GebrMG) · **⇒** Priorität ab der Zurschaustellung; keine Verlängerung der Fristen des § 6 Abs. 1 GebrMG (§ 6a Abs. 5 GebrMG)\n\n"
                  "**Klausurfallen:** Innere Priorität statt Abzweigung bringt bis zu zwölf Monate mehr Laufzeit, weil die Schutzdauer ab dem eigenen "
                  "Anmeldetag läuft (TS II/2018), erlaubt Weiterbildungen (TS III/2021) und lässt die Patentanmeldung bestehen. Umgekehrt: Patent mit "
                  "Priorität eines Gebrauchsmusters – das Gebrauchsmuster gilt nicht als zurückgenommen (§ 40 Abs. 5 S. 2 PatG; TS III/2022).\n\n"
                  "**In den Klausuren:** TS II/2018, TS I/2021, TS III/2021, (TS III/2022 umgekehrte Richtung).",
                  concepts=["pat_prioritaet"] + G, norms=["§ 40 PatG", "§ 41 Abs. 1 PatG", "§ 123 Abs. 1 PatG"], abschnitt="Normenkette"),
            intro("p06c-1", "Definitionen",
                  "**Innere Priorität:** Recht, für eine Gebrauchsmusteranmeldung den Anmeldetag einer früheren DPMA-Anmeldung derselben Erfindung "
                  "als Zeitrang zu beanspruchen (§ 6 Abs. 1 S. 1 GebrMG)\n"
                  "**Kettenpriorität:** Priorität aus einer Anmeldung, die selbst schon eine Priorität beansprucht; für die innere Priorität "
                  "ausgeschlossen (§ 6 Abs. 1 S. 1 GebrMG)\n"
                  "**Deutlich offenbart (§ 40 Abs. 3 PatG):** die Merkmale ergeben sich für die Fachperson unmittelbar und eindeutig aus der Gesamtheit "
                  "der früheren Unterlagen (Rechtsprechung zum Prioritätsrecht)\n"
                  "**Erste Anmeldung (Art. 4 C Abs. 4 PVÜ):** die erste Anmeldung derselben Erfindung in einem Verbandsstaat; spätere Anmeldungen geben "
                  "nur ausnahmsweise eine neue Prioritätsfrist\n"
                  "**Zurschaustellung (§ 6a Abs. 1 GebrMG):** öffentliches Zeigen der Erfindung auf einer vom BMJV im Bundesanzeiger bekanntgemachten "
                  "internationalen oder sonstigen Ausstellung\n"
                  "**Prioritätserklärung:** Angabe von Tag und Aktenzeichen der früheren Anmeldung; bei innerer Priorität erst mit Aktenzeichen "
                  "abgegeben (§ 40 Abs. 4 PatG)",
                  concepts=["pat_prioritaet"], norms=["§ 40 Abs. 3 PatG", "§ 40 Abs. 4 PatG"], abschnitt="Definitionen"),
            fall("p06c-2", "Patentanmeldung bleibt bestehen",
                 "Die Mandantin hat am 18.5.2026 ein Patent beim DPMA angemeldet. Am 16.12.2026 meldet sie für dieselbe Erfindung ein Gebrauchsmuster unter Inanspruchnahme dieser Priorität an.",
                 "Gilt die Patentanmeldung damit als zurückgenommen?", False,
                 ["**Nein!** § 6 Abs. 1 S. 2 GebrMG verweist auf § 40 Abs. 5 S. 1 PatG nur mit der Maßgabe, dass eine frühere Patentanmeldung "
                  "nicht als zurückgenommen gilt. Patentanmeldung und Gebrauchsmuster bestehen nebeneinander; ein Doppelschutzverbot zwischen "
                  "Patent und Gebrauchsmuster gibt es nicht. Die Patentanmeldung bleibt auch Basis für Auslandsanmeldungen."],
                 merke="Innere Priorität fürs GBM: frühere Patentanmeldung bleibt (§ 6 Abs. 1 S. 2 GebrMG).", level=1, concepts=["pat_prioritaet"] + G,
                 norms=["§ 40 Abs. 5 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06c-3", "Frühere Gebrauchsmusteranmeldung",
                 "Die Mandantin hat am 1.2.2026 ein Gebrauchsmuster angemeldet, das noch nicht eingetragen ist. Am 1.10.2026 meldet sie eine verbesserte Fassung als Gebrauchsmuster mit deren Priorität an.",
                 "Gilt die erste Gebrauchsmusteranmeldung als zurückgenommen?", True,
                 ["**Ja!** Die Maßgabe des § 6 Abs. 1 S. 2 GebrMG schützt nur eine frühere Patentanmeldung. Für eine frühere, noch beim DPMA anhängige "
                  "Gebrauchsmusteranmeldung bleibt es bei § 40 Abs. 5 S. 1 PatG: Sie gilt mit der Prioritätserklärung als zurückgenommen. Ist das "
                  "erste Gebrauchsmuster schon eingetragen, ist es keine anhängige Anmeldung mehr."],
                 merke="GBM aus GBM: frühere, noch anhängige Anmeldung gilt als zurückgenommen (§ 40 Abs. 5 S. 1 PatG).", level=3,
                 concepts=["pat_prioritaet"] + G, norms=["§ 40 Abs. 5 PatG"], abschnitt="Definitionen und Normen"),
            mc("p06c-4", "Prioritätserklärung",
               "Bis wann muss die innere Priorität für die Gebrauchsmusteranmeldung erklärt werden?",
               ["Mit der Anmeldung, später nicht mehr", "Binnen zwei Monaten nach dem Anmeldetag der späteren Anmeldung, mit Aktenzeichen",
                "Bis zum Ablauf des 16. Monats nach dem Prioritätstag", "Bis zur Eintragung"], 1,
               ["**§ 40 Abs. 4 PatG i.V.m. § 6 Abs. 1 S. 2 GebrMG.** Die Priorität kann nur binnen zwei Monaten nach dem Anmeldetag der späteren "
                "Anmeldung in Anspruch genommen werden; die Erklärung gilt erst mit Angabe des Aktenzeichens als abgegeben. Die 16-Monats-Frist gilt "
                "für die Unionspriorität (§ 41 Abs. 1 PatG) und die Ausstellungspriorität (§ 6a Abs. 4 GebrMG)."],
               merke="Innere Priorität: Erklärung 2 Monate (§ 40 Abs. 4 PatG); Unions-/Ausstellungspriorität: Angaben 16 Monate.", level=2,
               concepts=["pat_prioritaet", "pat_fristen"], norms=["§ 40 Abs. 4 PatG", "§ 41 Abs. 1 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06c-5", "Priorität einer Patentanmeldung aus dem Ausland",
                 "Ein US-Unternehmen hat vor zehn Monaten in den USA ein Patent angemeldet. Es will in Deutschland nur ein Gebrauchsmuster mit dieser Priorität.",
                 "Kann ein Gebrauchsmuster die Priorität einer ausländischen Patentanmeldung beanspruchen?", True,
                 ["**Ja!** Nach Art. 4 E Abs. 2 PVÜ kann ein Gebrauchsmuster mit der Priorität einer Patentanmeldung angemeldet werden und umgekehrt; "
                  "Frist zwölf Monate (Art. 4 C Abs. 1 PVÜ). Zeit, Land und Aktenzeichen sind bis zum Ablauf des 16. Monats nach dem Prioritätstag "
                  "anzugeben, sonst Verwirkung (§ 6 Abs. 2 GebrMG i.V.m. § 41 Abs. 1 PatG)."],
                 merke="Unionspriorität GBM: Art. 4 E Abs. 2, Art. 4 C Abs. 1 PVÜ · Angaben § 41 Abs. 1 PatG (16 Monate).", level=2,
                 concepts=["pat_prioritaet"], norms=["§ 41 Abs. 1 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06c-6", "Versäumte Prioritätsfrist",
                 "Die Kanzlei hat die Zwölfmonatsfrist für eine Gebrauchsmusteranmeldung mit innerer Priorität um zwei Tage versäumt, weil ein sonst zuverlässiger Mitarbeiter erkrankte.",
                 "Kommt Wiedereinsetzung in die Prioritätsfrist in Betracht?", False,
                 ["**Nein!** § 21 Abs. 1 GebrMG verweist auf § 123 PatG. Dessen Abs. 1 S. 2 Nr. 3 schließt die Wiedereinsetzung für die Frist zur "
                  "Einreichung von Anmeldungen aus, für die eine Priorität nach § 40 PatG beansprucht werden kann. Ohne Priorität zählt der eigene "
                  "Anmeldetag; eigene Offenbarungen der letzten sechs Monate deckt aber § 3 Abs. 1 S. 3 GebrMG."],
                 merke="Keine Wiedereinsetzung in die Frist der inneren Priorität (§ 123 Abs. 1 S. 2 Nr. 3 PatG).", level=3,
                 concepts=["pat_prioritaet", "pat_wiedereinsetzung"], norms=["§ 123 Abs. 1 PatG", "§ 40 PatG"], abschnitt="Definitionen und Normen"),
            mc("p06c-7", "Abzweigung oder innere Priorität?",
               "Welcher Vorteil spricht für die innere Priorität statt der Abzweigung aus derselben Patentanmeldung?",
               ["Die Patentanmeldung gilt nicht als zurückgenommen", "Längere Schutzdauer und Raum für Weiterbildungen",
                "Kein Stand der Technik zwischen Prioritätstag und Anmeldetag", "Die Neuheitsschonfrist läuft ab dem Prioritätstag"], 1,
               ["**Laufzeit und Weiterbildungen.** Die Schutzdauer läuft bei Priorität ab dem eigenen Anmeldetag (§ 23 Abs. 1 GebrMG), bei der "
                "Abzweigung ab dem älteren Anmeldetag. Neue Merkmale erhalten bei der Priorität den eigenen Zeitrang; bei der Abzweigung gäben sie "
                "keine Rechte. Die anderen Punkte gelten für beide Wege (§ 5 Abs. 1 GebrMG, § 6 Abs. 1 S. 2 GebrMG, § 3 Abs. 1 GebrMG)."],
               merke="Priorität: Laufzeit ab eigenem AT, Weiterbildungen möglich; Abzweigung: alter AT, auch nach Erledigung.", level=2,
               concepts=["pat_prioritaet"] + A, abschnitt="Definitionen und Normen"),
            *fallkette("p06c-8", "Schwimmflügel (nach TS II/2018)",
                "Die Mandantin hat am 15.5.2026 ein Patent auf neuartige Schwimmflügel beim DPMA angemeldet, ohne Priorität. Sie hatte sie am 15.1.2026 "
                "selbst vorgeführt; das Patent ist deshalb nicht zu retten. Sie will ein Gebrauchsmuster mit möglichst langer Laufzeit.",
                [frage("Kann sie am 16.12.2026 ein Gebrauchsmuster mit der inneren Priorität der Patentanmeldung anmelden?", True,
                       ["**Ja!** Frühere DPMA-Patentanmeldung ohne eigene Priorität, dieselbe Erfindung, Frist zwölf Monate bis 15.5.2027 (§ 6 Abs. 1 "
                        "S. 1 GebrMG, § 188 Abs. 2 BGB); der 15.5.2027 ist ein Samstag, Fristende Montag, 17.5.2027 (§ 193 BGB). Erklärung mit Aktenzeichen "
                        "binnen zwei Monaten (§ 40 Abs. 4 PatG)."],
                       merke="Frist § 6 Abs. 1 S. 1 GebrMG · § 187 Abs. 1, § 188 Abs. 2 BGB · § 193 BGB.", norms=["§ 40 Abs. 4 PatG"]),
                 frage("Schadet ihr die eigene Vorführung vom 15.1.2026?", False,
                       ["**Nein!** Maßgeblich ist der Zeitrangtag 15.5.2026. Die Vorführung liegt innerhalb der sechs Monate davor (ab 15.11.2025) und "
                        "beruht auf ihrer eigenen Ausarbeitung (§ 3 Abs. 1 S. 3 GebrMG)."],
                       merke="Schonfrist rechnet ab dem Prioritätstag."),
                 frage("Endet der Schutz bei innerer Priorität später als bei einer Abzweigung?", True,
                       ["**Ja!** Mit Priorität läuft die Schutzdauer ab dem eigenen Anmeldetag 16.12.2026 bis 31.12.2036, bei Abzweigung ab 15.5.2026 nur "
                        "bis 31.5.2036 (§ 23 Abs. 1 GebrMG): gut sieben Monate mehr."],
                       merke="Schutzdauer ab eigenem Anmeldetag – Priorität verschiebt nur den Zeitrang."),
                 frage("Sollte sie die Patentanmeldung sofort zurücknehmen?", False,
                       ["**Nein!** Die Priorität hängt nicht vom späteren Schicksal der Erstanmeldung ab (Art. 4 A Abs. 3 PVÜ), aber die Abzweigung "
                        "als Rückfallposition und Auslandsanmeldungen brauchen sie. Erst nach Einreichung des Gebrauchsmusters zurücknehmen oder "
                        "zurückweisen lassen; die Abzweigungsfrist läuft dann noch zwei Monate nach Monatsende (§ 5 Abs. 1 S. 3 GebrMG)."],
                       merke="Erstanmeldung erst nach Sicherung der Nachanmeldungen aufgeben.", concepts=A),
                ], abschnitt="Klausurfall", level=2, concepts=["pat_prioritaet"] + G),
            *fallkette("p06c-9", "Prototyp auf der Messe",
                "Die Mandantin zeigt ihren Prototyp am 1.3.2026 auf einer vom BMJV im Bundesanzeiger bekanntgemachten Fachausstellung in Frankfurt. "
                "Am 20.4.2026 veröffentlicht ein Konkurrent unabhängig eine gleiche Lösung. Die Mandantin meldet am 15.8.2026 ein Gebrauchsmuster an.",
                [frage("Hilft ihr gegen die Veröffentlichung des Konkurrenten die Neuheitsschonfrist?", False,
                       ["**Nein!** § 3 Abs. 1 S. 3 GebrMG deckt nur Offenbarungen, die auf der Ausarbeitung der Anmelderin beruhen. Die unabhängige "
                        "Veröffentlichung vom 20.4.2026 liegt vor dem Anmeldetag und ist Stand der Technik. Unschädlich ist nur die eigene Ausstellung."],
                       merke="Schonfrist schützt nicht gegen unabhängige Zwischenveröffentlichungen."),
                 frage("Kann sie die Ausstellungspriorität vom 1.3.2026 in Anspruch nehmen?", True,
                       ["**Ja!** Die Ausstellung ist bekanntgemacht (§ 6a Abs. 1 Nr. 2, Abs. 3 GebrMG), die Anmeldung erfolgt innerhalb von sechs Monaten "
                        "seit der ersten Zurschaustellung, also bis 1.9.2026 (§ 6a Abs. 1 GebrMG, § 188 Abs. 2 BGB). Zeitrang ist der 1.3.2026; die "
                        "Konkurrenzveröffentlichung wird kein Stand der Technik."],
                       merke="Ausstellungspriorität: 6 Monate ab Zurschaustellung, Zeitrang = Ausstellungstag."),
                 frage("Muss sie Tag, Ausstellung und Nachweis schon mit der Anmeldung einreichen?", False,
                       ["**Nein!** Die Angaben und der Nachweis sind vor Ablauf des 16. Monats nach dem Tag der ersten Zurschaustellung einzureichen, "
                        "hier bis 1.7.2027 (§ 6a Abs. 4 GebrMG). Die Ausstellungspriorität verlängert die Frist für eine spätere innere Priorität nicht "
                        "(§ 6a Abs. 5 GebrMG)."],
                       merke="Angaben § 6a Abs. 4 GebrMG: vor Ablauf des 16. Monats; § 6a Abs. 5 GebrMG keine Fristverlängerung."),
                ], abschnitt="Klausurfall", level=2, concepts=["pat_prioritaet"] + G),
        ]),

        # ================================================================== §§ 15 bis 17 GebrMG
        dict(id="p06d", titel="§§ 15 bis 17 GebrMG: Löschung", einheiten=[
            intro("p06d-0", "Prüfungsschema",
                  "**AGL:** § 15 Abs. 1 GebrMG i.V.m. § 16 GebrMG (Anspruch auf Löschung gegen den als Inhaber Eingetragenen)\n\n"
                  "**A · Zulässigkeit**\n"
                  "**V1 Statthaftigkeit** – eingetragenes Gebrauchsmuster; nach Erlöschen nur Antrag auf Feststellung der Unwirksamkeit mit "
                  "besonderem Rechtsschutzinteresse\n"
                  "**V2 Antragsberechtigung** – jedermann (§ 15 Abs. 1 GebrMG); bei widerrechtlicher Entnahme nur der Verletzte (§ 15 Abs. 2 GebrMG "
                  "i.V.m. § 13 Abs. 2 GebrMG); Antragsgegner ist der als Inhaber Eingetragene\n"
                  "**V3 Form und Inhalt** – schriftlich beim DPMA, Angabe der stützenden Tatsachen (§ 16 S. 1, 2 GebrMG); Sicherheitsleistung bei "
                  "Sitz außerhalb EU/EWR (§ 16 S. 3 GebrMG i.V.m. § 81 Abs. 6 PatG); Druckschriften (§ 125 PatG); Inlandsvertreter (§ 28 GebrMG)\n"
                  "**V4 Gebühr** – 300 EUR je Antragsteller (Nr. 323 100 Anlage PatKostG, Vorbemerkung Teil A Abs. 2), fällig mit Antrag (§ 3 Abs. 1 S. 1 "
                  "PatKostG), zahlbar binnen drei Monaten (§ 6 Abs. 1 S. 2 PatKostG), sonst gilt der Antrag als zurückgenommen (§ 6 Abs. 2 PatKostG)\n"
                  "**V5 Rechtsschutzbedürfnis** – bei eingetragenem Gebrauchsmuster nicht gesondert zu prüfen (Popularantrag); keine Frist\n\n"
                  "**B · Begründetheit: Löschungsgrund**\n"
                  "**V6a Fehlende Schutzfähigkeit** – § 15 Abs. 1 Nr. 1 GebrMG i.V.m. §§ 1 bis 3 GebrMG\n"
                  "**V6b Doppelschutz** – § 15 Abs. 1 Nr. 2 GebrMG: Gegenstand schon aufgrund einer früheren Patent- oder Gebrauchsmusteranmeldung "
                  "geschützt (Identität des Schutzbereichs, Schutzrecht entstanden)\n"
                  "**V6c Unzulässige Erweiterung** – § 15 Abs. 1 Nr. 3 GebrMG: über die ursprünglich eingereichte Fassung hinaus\n"
                  "**V6d Widerrechtliche Entnahme** – § 15 Abs. 2 GebrMG i.V.m. § 13 Abs. 2 GebrMG\n\n"
                  "**C · Verfahren und Rechtsfolge**\n"
                  "**V7 Kein (rechtzeitiger) Widerspruch** – Mitteilung an den Inhaber, Erklärung binnen eines Monats (§ 17 Abs. 1 S. 1 GebrMG · "
                  "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB); ohne Widerspruch Löschung ohne Sachprüfung (§ 17 Abs. 1 S. 2 GebrMG); mit "
                  "Widerspruch Beweisaufnahme, mündliche Verhandlung auf Antrag (§ 17 Abs. 2 GebrMG), Beschluss der Gebrauchsmusterabteilung "
                  "(§ 17 Abs. 3 GebrMG, § 10 Abs. 3 GebrMG)\n"
                  "**⇒ Rechtsfolge:** Löschung, bei Teilbegründetheit Teillöschung, auch durch Änderung der Schutzansprüche (§ 15 Abs. 3 GebrMG); "
                  "Kosten nach Quote im Beschluss (§ 17 Abs. 4 S. 1 GebrMG), sonst nur auf Antrag binnen eines Monats (§ 17 Abs. 4 S. 2, 3 GebrMG); "
                  "Maßstab § 84 Abs. 2 S. 2 PatG mit §§ 91 ff. ZPO, § 93 ZPO (§ 17 Abs. 4 S. 4 GebrMG); Beschwerde zum BPatG (§ 18 Abs. 1 GebrMG)\n\n"
                  "**Klausurfallen:** Kein Einspruch, keine Nichtigkeitsklage; ältere nachveröffentlichte Anmeldungen nur über § 15 Abs. 1 Nr. 2 GebrMG. "
                  "Wer nicht widerspricht, trägt trotzdem die Kosten, wenn er Anlass zum Antrag gegeben hat (Verwarnung, unbeantwortete "
                  "Verzichtsaufforderung). Gebühr je Antragsteller – gemeinsamer Antrag einer GbR spart die zweite Gebühr (TS III/2022).\n\n"
                  "**In den Klausuren:** TS II/2019 (Doppelschutz, Kosten ohne Widerspruch), TS I/2021 (Benutzungen, Erlöschen), TS III/2021, TS III/2022 "
                  "(Blogeintrag, Schonfrist), TS III/2023; (TS II/2022 Entnahme, TS II/2023 Doppelschutz).",
                  concepts=L + ["pat_doppelschutz", "pat_kostenerstattung"],
                  norms=["§ 81 Abs. 6 PatG", "§ 125 PatG", "§ 84 Abs. 2 PatG", "§ 62 Abs. 2 PatG", "§ 3 Abs. 1 PatKostG", "§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG"],
                  cases=["pat_bgh_formkoerper_mit_durchtrittsoeffnungen", "pat_bgh_tischgrill"], abschnitt="Normenkette"),
            intro("p06d-1", "Definitionen",
                  "**Löschungsanspruch:** materiell-rechtlicher Anspruch jedermanns gegen den als Inhaber Eingetragenen auf Beseitigung der Eintragung "
                  "(§ 15 Abs. 1 GebrMG); er schließt zugleich den Schutz aus (§ 13 Abs. 1 GebrMG)\n"
                  "**Bereits geschützt (§ 15 Abs. 1 Nr. 2 GebrMG):** Identität der Gegenstände (gleicher Schutzbereich) und entstandener Schutz aus der "
                  "früheren Anmeldung; die bloße Möglichkeit, dass das ältere Patent später vernichtet wird, ist unbeachtlich (BGH Formkörper mit Durchtrittsöffnungen)\n"
                  "**Erweiterung (§ 15 Abs. 1 Nr. 3 GebrMG):** Gegenstand geht über den Inhalt der ursprünglich eingereichten Anmeldung hinaus; ein nicht "
                  "offenbartes, nur beschränkendes Merkmal ohne Aliud führt nicht zur Löschung (BGH Tintenstrahldrucker)\n"
                  "**Widerrechtliche Entnahme (§ 13 Abs. 2 GebrMG):** der wesentliche Inhalt der Eintragung ist Beschreibungen, Zeichnungen, Modellen, "
                  "Gerätschaften oder Einrichtungen eines anderen ohne dessen Einwilligung entnommen (Legaldefinition)\n"
                  "**Veranlassung zum Antrag (§ 93 ZPO):** der Inhaber hat sich so verhalten, dass der Antragsteller annehmen musste, ohne Verfahren nicht "
                  "zum Ziel zu kommen – etwa Verwarnung oder keine Reaktion auf eine Verzichtsaufforderung (BGH Druckdatenübertragungsverfahren, X ZR 73/12)\n"
                  "**Sofortiges Anerkenntnis im Löschungsverfahren:** Nichtwiderspruch oder sofortiger Verzicht bzw. Beschränkung (BGH Dynamisches Mikrofon, "
                  "X ZR 26/00, zum Nichtigkeitsverfahren)\n"
                  "**Besonderes Rechtsschutzinteresse nach Erlöschen:** eigenes Interesse an der Feststellung der Unwirksamkeit für die Vergangenheit, "
                  "vor allem drohende oder erhobene Ansprüche aus der Schutzdauer; entfällt bei Freistellung (BPatG Vorrichtung zur Immobilisierung)",
                  concepts=L + ["pat_doppelschutz", "pat_kostenerstattung", "pat_unzulaessige_erweiterung"],
                  cases=["pat_bgh_formkoerper_mit_durchtrittsoeffnungen", "pat_bgh_tintenstrahldrucker", "pat_bpatg_immobilisierung_erledigung"],
                  abschnitt="Definitionen"),
            mc("p06d-2", "Löschungsgebühr",
               "Welche Norm regelt die Löschungsgebühr und die Folge der Nichtzahlung?",
               ["§ 16 GebrMG – der Antrag ist unzulässig", "Nr. 323 100 Anlage PatKostG, § 6 Abs. 1 S. 2 PatKostG, § 6 Abs. 2 PatKostG – Rücknahmefiktion",
                "§ 17 Abs. 4 GebrMG – Kostenlast", "Nr. 401 100 Anlage PatKostG – Beschwerde gilt als nicht eingelegt"], 1,
               ["**Nr. 323 100 Anlage PatKostG.** 300 EUR, fällig mit dem Antrag (§ 3 Abs. 1 S. 1 PatKostG). Da der Löschungsantrag fristlos ist, gilt "
                "die Dreimonatsfrist des § 6 Abs. 1 S. 2 PatKostG; danach gilt der Antrag als zurückgenommen (§ 6 Abs. 2 PatKostG). Die Gebühr fällt "
                "je Antragsteller an (Vorbemerkung Teil A Abs. 2)."],
               merke="Löschung: 300 EUR je Antragsteller · 3 Monate (§ 6 Abs. 1 S. 2 PatKostG) · sonst Rücknahmefiktion.", level=1,
               concepts=L + ["pat_gebuehren"], norms=["§ 6 Abs. 1 PatKostG", "§ 6 Abs. 2 PatKostG"], abschnitt="Definitionen und Normen"),
            fall("p06d-3", "Entnahme durch einen Dritten gerügt",
                 "Die Stator GmbH beantragt die Löschung eines Gebrauchsmusters, weil die Inhaberin die Erfindung dem Ingenieur Nolte entnommen habe. Nolte selbst unternimmt nichts.",
                 "Kann die Stator GmbH die Löschung auf die widerrechtliche Entnahme stützen?", False,
                 ["**Nein!** Im Fall des § 13 Abs. 2 GebrMG steht nur dem Verletzten ein Anspruch auf Löschung zu (§ 15 Abs. 2 GebrMG). Nolte "
                  "könnte löschen lassen oder Übertragung verlangen (§ 13 Abs. 3 GebrMG i.V.m. § 8 PatG). Die Stator GmbH bleibt auf die Gründe des "
                  "§ 15 Abs. 1 GebrMG beschränkt."],
                 merke="Entnahme: nur der Verletzte (§ 15 Abs. 2 GebrMG); sonst jedermann.", level=1, concepts=L + ["pat_recht_auf_patent"],
                 norms=["§ 8 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06d-4", "Verteidigung mit nicht angegriffenem Unteranspruch",
                 "Der Antragsteller greift nur Schutzanspruch 1 an. Die Inhaberin verteidigt Schutzanspruch 1 hilfsweise in Kombination mit dem nicht angegriffenen Unteranspruch 3.",
                 "Ist diese beschränkte Verteidigung zulässig?", False,
                 ["**Nein!** Auch im Löschungsverfahren ist es unzulässig, einen mit Teil-Löschungsantrag angegriffenen Anspruch durch Kombination mit "
                  "einem nicht angegriffenen Unteranspruch zu verteidigen; zulässig ist die Ergänzung um nur einen Teil von dessen Merkmalen (BGH "
                  "Tischgrill). Die Beschränkung durch Änderung der Schutzansprüche erlaubt § 15 Abs. 3 S. 2 GebrMG nur im Rahmen des Angriffs."],
                 merke="Teillöschung § 15 Abs. 3 GebrMG: Verteidigung nur innerhalb des Angriffs (BGH Tischgrill).", level=3,
                 concepts=L + ["pat_beschraenkte_verteidigung"], cases=["pat_bgh_tischgrill"], abschnitt="Definitionen und Normen"),
            fall("p06d-5", "Nach Erlöschen",
                 "Das angegriffene Gebrauchsmuster ist am 30.6.2026 durch Zeitablauf erloschen. Die Inhaberin hat die Antragstellerin wegen Lieferungen im Jahr 2025 abgemahnt.",
                 "Kann die Antragstellerin das Verfahren als Antrag auf Feststellung der Unwirksamkeit fortführen?", True,
                 ["**Ja!** Nach Erlöschen geht die Löschung ins Leere; zulässig bleibt die Feststellung der Unwirksamkeit, wenn ein besonderes "
                  "Rechtsschutzinteresse besteht. Das liegt in der drohenden Inanspruchnahme für die Vergangenheit. Stellt die Inhaberin sie von allen "
                  "Ansprüchen frei, tritt Erledigung ein (BPatG Vorrichtung zur Immobilisierung)."],
                 merke="Erloschenes GBM: Feststellung der Unwirksamkeit nur mit besonderem Rechtsschutzinteresse.", level=2, concepts=L,
                 cases=["pat_bpatg_immobilisierung_erledigung"], abschnitt="Definitionen und Normen"),
            mc("p06d-6", "Kostenmaßstab",
               "Nach welchem Maßstab entscheidet die Gebrauchsmusterabteilung über die Kosten des Löschungsverfahrens?",
               ["Jeder trägt seine Kosten selbst (§ 62 Abs. 1 PatG)", "Nach billigem Ermessen ohne Bindung an das Ergebnis",
                "ZPO-Kostenrecht entsprechend, soweit nicht die Billigkeit anderes erfordert (§ 17 Abs. 4 S. 4 GebrMG, § 84 Abs. 2 S. 2 PatG)",
                "Der Antragsteller trägt stets die Kosten"], 2,
               ["**§ 17 Abs. 4 GebrMG i.V.m. § 84 Abs. 2 S. 2 PatG.** Die Abteilung bestimmt im Beschluss die Kostenquote (§ 17 Abs. 4 S. 1 GebrMG). "
                "Entsprechend gelten §§ 91 ff. ZPO, also auch § 93 ZPO; erstattungsfähig sind die notwendigen Kosten der Beteiligten (§ 62 Abs. 2 PatG). "
                "Anders als im Einspruch trägt der Unterliegende in der Regel die Kosten."],
               merke="Kosten Löschung: § 17 Abs. 4 GebrMG · § 84 Abs. 2 S. 2 PatG · § 91, § 93 ZPO · § 62 Abs. 2 PatG.", level=2,
               concepts=L + ["pat_kostenerstattung"], norms=["§ 84 Abs. 2 PatG", "§ 62 Abs. 2 PatG", "§ 62 Abs. 1 PatG"], abschnitt="Definitionen und Normen"),
            mc("p06d-7", "Beschwerde gegen den Löschungsbeschluss",
               "Die Gebrauchsmusterabteilung löscht das Gebrauchsmuster. Was gilt für die Beschwerde der Inhaberin?",
               ["Ein Monat, 200 EUR (Nr. 401 300 Anlage PatKostG)", "Ein Monat, 500 EUR (Nr. 401 100 Anlage PatKostG) innerhalb der Frist",
                "Zwei Monate, 500 EUR", "Rechtsbeschwerde zum BGH ohne Zulassung"], 1,
               ["**Nr. 401 100 Anlage PatKostG.** Beschwerde zum BPatG (§ 18 Abs. 1 GebrMG) binnen eines Monats nach Zustellung (§ 18 Abs. 2 S. 1 "
                "GebrMG i.V.m. § 73 Abs. 2 S. 1 PatG), Gebühr 500 EUR innerhalb der Frist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt sie als nicht "
                "eingelegt (§ 6 Abs. 2 PatKostG). Kosten nach § 84 Abs. 2 PatG (§ 18 Abs. 2 S. 2 GebrMG)."],
               merke="Beschwerde Löschung: 1 Monat (§ 73 Abs. 2 PatG) · 500 EUR in der Frist · Folge § 6 Abs. 2 PatKostG.", level=2,
               concepts=L + ["pat_beschwerde"], norms=["§ 73 Abs. 2 PatG", "§ 6 Abs. 1 PatKostG", "§ 84 Abs. 2 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06d-8", "Älteres Patent mit Restrisiko",
                 "Die Gebrauchsmusterabteilung löscht nach § 15 Abs. 1 Nr. 2 GebrMG wegen eines älteren erteilten Patents mit identischem Schutzbereich. Die Inhaberin rügt, das ältere Patent könne selbst noch für nichtig erklärt werden.",
                 "Muss das Patentgericht sich mit dieser Möglichkeit auseinandersetzen?", False,
                 ["**Nein!** Für § 15 Abs. 1 Nr. 2 GebrMG genügt, dass der Gegenstand aufgrund der früheren Anmeldung geschützt ist. Die bloß "
                  "theoretische Möglichkeit einer künftigen Nichtigerklärung des älteren Patents muss nicht erörtert werden (BGH Formkörper mit "
                  "Durchtrittsöffnungen)."],
                 merke="Doppelschutz: älteres Schutzrecht mit identischem Gegenstand genügt.", level=2, concepts=L + ["pat_doppelschutz"],
                 cases=["pat_bgh_formkoerper_mit_durchtrittsoeffnungen"], abschnitt="Definitionen und Normen"),
            *fallkette("p06d-9", "Stator gegen GBM 444 (nach TS II/2019)",
                "Die Elektro AG verwarnte die Stator GmbH am 5.5.2017 aus GBM 444 (Zeitrang 1.6.2015) und drohte mit einstweiliger Verfügung. Stator "
                "forderte sie am 10.5.2017 unter Hinweis auf das 2016 erteilte Patent E1 (angemeldet 2014, praktisch identischer Schutzbereich) zum "
                "Verzicht auf; keine Antwort. Stator beantragt die Löschung.",
                [frage("Ist der Löschungsantrag zulässig, obwohl Stator kein eigenes Interesse darlegt?", True,
                       ["**Ja!** Antragsberechtigt ist jedermann (§ 15 Abs. 1 GebrMG); bei eingetragenem Gebrauchsmuster wird ein Rechtsschutzinteresse "
                        "nicht geprüft. Schriftlich mit Tatsachen (§ 16 GebrMG) und 300 EUR binnen drei Monaten (Nr. 323 100 Anlage PatKostG, § 6 Abs. 1 "
                        "S. 2 PatKostG)."],
                       merke="Löschungsantrag: Popularantrag, keine Frist."),
                 frage("Ist E1 neuheitsschädlicher Stand der Technik für GBM 444?", False,
                       ["**Nein!** E1 wurde frühestens 18 Monate nach dem Anmeldetag offengelegt (§ 31 Abs. 2 S. 1 Nr. 2 PatG), also nach dem 1.6.2015. "
                        "Eine Fiktion wie § 3 Abs. 2 PatG kennt das GebrMG nicht (§ 3 Abs. 1 S. 2 GebrMG)."],
                       merke="Ältere nachveröffentlichte Anmeldung: kein SdT des GBM.", norms=["§ 31 Abs. 2 PatG", "§ 3 Abs. 2 PatG"]),
                 frage("Ist GBM 444 nach § 15 Abs. 1 Nr. 2 GebrMG zu löschen?", True,
                       ["**Ja!** Der Gegenstand ist aufgrund der früheren Patentanmeldung E1 bereits geschützt: älterer Zeitrang (2014), erteilt 2016, "
                        "praktisch identischer Schutzbereich trotz anderer Wortwahl. Die Möglichkeit, dass E1 später fällt, ist unbeachtlich (BGH "
                        "Formkörper mit Durchtrittsöffnungen)."],
                       merke="§ 15 Abs. 1 Nr. 2 GebrMG: früherer Zeitrang + Schutz entstanden + Identität.", cases=["pat_bgh_formkoerper_mit_durchtrittsoeffnungen"],
                       concepts=["pat_doppelschutz"]),
                 frage("Die Elektro AG widerspricht nicht. Wird ohne Sachprüfung gelöscht?", True,
                       ["**Ja!** Widerspricht der Inhaber nicht binnen eines Monats nach Zustellung der Mitteilung, erfolgt die Löschung (§ 17 Abs. 1 "
                        "S. 1, 2 GebrMG). Eine Hauptsacheentscheidung ergeht nicht; über die Kosten wird nur auf Antrag binnen eines Monats entschieden "
                        "(§ 17 Abs. 4 S. 2, 3 GebrMG)."],
                       merke="Kein Widerspruch → Löschung (§ 17 Abs. 1 S. 2 GebrMG); Kosten nur auf Antrag (§ 17 Abs. 4 S. 2, 3 GebrMG)."),
                 frage("Kann sich die Elektro AG auf § 93 ZPO berufen und Stator die Kosten auferlegen lassen?", False,
                       ["**Nein!** Nichtwiderspruch steht zwar einem sofortigen Anerkenntnis gleich (§ 17 Abs. 4 S. 4 GebrMG, § 84 Abs. 2 S. 2 PatG). Die "
                        "Elektro AG hat aber Anlass zum Antrag gegeben: Verwarnung und unbeantwortete Verzichtsaufforderung (BGH "
                        "Druckdatenübertragungsverfahren, X ZR 73/12). Sie trägt die Kosten (§ 91 Abs. 1 S. 1 ZPO)."],
                       merke="§ 93 ZPO nur ohne Veranlassung; Verwarnung oder Schweigen auf Verzichtsaufforderung = Veranlassung.",
                       norms=["§ 84 Abs. 2 PatG"], concepts=["pat_kostenerstattung"]),
                ], abschnitt="Klausurfall", level=2, concepts=L),
            *fallkette("p06d-10", "Blogeintrag des Ex-Mitarbeiters (nach TS III/2022)",
                "M hat am 15.4.2019 GBM 444 angemeldet. D, ein früherer Mitarbeiter von M und nie Erfinder, veröffentlichte am 3.2.2019 einen Blogeintrag "
                "mit fast wörtlich allen Einzelheiten. A und B, Gesellschafter einer GbR, wollen GBM 444 löschen lassen.",
                [frage("Ist der Blogeintrag eine schriftliche Beschreibung im Sinne des § 3 Abs. 1 S. 2 GebrMG?", True,
                       ["**Ja!** Eine im Internet abrufbare Veröffentlichung ist eine schriftliche Beschreibung; sie war vor dem Zeitrangtag 15.4.2019 "
                        "der Öffentlichkeit zugänglich. Inhalt und Datum müssen bewiesen werden (Archivausdruck, Zeuge D)."],
                       merke="Internetveröffentlichung = schriftliche Beschreibung."),
                 frage("Bleibt der Blogeintrag nach § 3 Abs. 1 S. 3 GebrMG außer Betracht?", True,
                       ["**Ja!** Er liegt innerhalb von sechs Monaten vor dem 15.4.2019 (ab 15.10.2018) und beruht erkennbar auf der Ausarbeitung von M "
                        "und seinen Erfindern; auf Missbrauch kommt es nicht an. Die Kette der Wissensvermittlung kann per Anscheinsbeweis belegt werden "
                        "(BPatG Tür- und Fenstersensor)."],
                       merke="Schonfrist: Kette der Wissensvermittlung, Anscheinsbeweis möglich.", cases=["pat_bpatg_tuer_und_fenstersensor"]),
                 frage("Müssen A und B je 300 EUR zahlen, wenn sie den Antrag gemeinsam stellen?", True,
                       ["**Ja!** Die Gebühr Nr. 323 100 wird für jeden Antragsteller gesondert erhoben (Vorbemerkung Teil A Abs. 2 Anlage PatKostG); die "
                        "Ausnahme für gemeinschaftliche Inhaber gilt dafür nicht. Stellt die GbR als eine Antragstellerin den Antrag, fällt nur eine "
                        "Gebühr an."],
                       merke="Löschungsgebühr je Antragsteller; GbR als eine Antragstellerin."),
                 frage("Ist der Löschungsantrag aussichtsreich?", False,
                       ["**Nein!** Zulässig ja, aber der einzige Stand der Technik bleibt außer Betracht. M wird widersprechen (§ 17 Abs. 1 GebrMG). Gegen "
                        "das Patent DE 555 mit Priorität aus GBM 444 schadet derselbe Blogeintrag dagegen (§ 3 Abs. 1 PatG)."],
                       merke="Gleicher SdT, verschiedene Ergebnisse: GBM mit Schonfrist, Patent ohne.", norms=["§ 3 Abs. 1 PatG"]),
                ], abschnitt="Klausurfall", level=2, concepts=L + ["pat_neuheit"]),
        ]),

        # ================================================================== § 24 GebrMG
        dict(id="p06e", titel="§ 24 GebrMG: Verletzungsansprüche", einheiten=[
            intro("p06e-0", "Prüfungsschema",
                  "**AGL:** § 24 Abs. 1 GebrMG (Unterlassung) · § 24 Abs. 2 GebrMG (Schadensersatz) · § 24a GebrMG (Vernichtung, Rückruf) · § 24b GebrMG "
                  "(Auskunft) · § 24c GebrMG (Vorlage, Besichtigung) · § 24d GebrMG (Bank- und Handelsunterlagen) · § 24e GebrMG (Urteilsbekanntmachung)\n\n"
                  "**A · Anspruchsvoraussetzungen**\n"
                  "**V1 Eingetragenes Gebrauchsmuster** – § 11 Abs. 1 S. 1 GebrMG: Schutz ab Eintragung, innerhalb der Schutzdauer (§ 23 Abs. 1 GebrMG), "
                  "nicht erloschen (§ 23 Abs. 3 GebrMG)\n"
                  "**V2 Aktivlegitimation** – Verletzter: eingetragener Inhaber (§ 8 Abs. 4 S. 2 GebrMG), ausschließlicher Lizenznehmer (§ 22 Abs. 2 GebrMG)\n"
                  "**V3 Benutzung** – unmittelbar: Erzeugnis, das Gegenstand des Gebrauchsmusters ist, herstellen, anbieten, in Verkehr bringen, "
                  "gebrauchen, einführen oder besitzen (§ 11 Abs. 1 S. 2 GebrMG); mittelbar (§ 11 Abs. 2 GebrMG); Schutzbereich nach den Schutzansprüchen, "
                  "ausgelegt mit Beschreibung und Zeichnungen (§ 12a GebrMG), auch äquivalent\n"
                  "**V4 Schutzfähigkeit (Einwand)** – § 13 Abs. 1 GebrMG: kein Schutz, soweit ein Löschungsanspruch für jedermann besteht (§ 15 Abs. 1, 3 "
                  "GebrMG); das Verletzungsgericht prüft inzident; bei Entnahme kein Schutz gegenüber dem Verletzten (§ 13 Abs. 2 GebrMG)\n"
                  "**V5 Keine Schranke, kein Gegenrecht** – § 12 GebrMG (privat, Versuche, § 11 Nr. 4 bis 6 PatG); Vorbenutzungsrecht (§ 13 Abs. 3 GebrMG "
                  "i.V.m. § 12 PatG); Erschöpfung; Lizenz; älteres Gebrauchsmuster gegen jüngeres Patent (§ 14 GebrMG)\n"
                  "**V6a Unterlassung** – Wiederholungs- oder Erstbegehungsgefahr (§ 24 Abs. 1 S. 1, 2 GebrMG); keine unverhältnismäßige Härte "
                  "(§ 24 Abs. 1 S. 3 GebrMG, sonst Ausgleich in Geld S. 4)\n"
                  "**V6b Schadensersatz** – Vorsatz oder Fahrlässigkeit; drei Berechnungsarten: konkreter Schaden, Verletzergewinn, Lizenzanalogie "
                  "(§ 24 Abs. 2 S. 1 bis 3 GebrMG)\n\n"
                  "**B · Durchsetzung**\n"
                  "Landgericht ausschließlich (§ 27 Abs. 1 GebrMG); Patentanwaltskosten (§ 27 Abs. 3 GebrMG); Inlandsvertreter (§ 28 GebrMG); Aussetzung "
                  "bei anhängigem Löschungsverfahren (§ 19 S. 1 GebrMG), zwingend, wenn das Gericht die Eintragung für unwirksam hält (§ 19 S. 2 GebrMG); "
                  "Bindung an die Zurückweisung des Löschungsantrags nur zwischen denselben Parteien (§ 19 S. 3 GebrMG); einstweilige Verfügung "
                  "(§ 935 ZPO, § 940 ZPO); Verjährung (§ 24f GebrMG i.V.m. § 195 BGB, § 199 BGB)\n\n"
                  "**⇒ Rechtsfolge:** Unterlassung, Schadensersatz, Vernichtung und Rückruf, Auskunft über Herkunft und Vertriebsweg\n\n"
                  "**Klausurfallen:** Das Gebrauchsmuster schützt kein Verfahren und kein Verfahrenserzeugnis; Ansprüche bestehen erst ab Eintragung. "
                  "Weil niemand die Schutzfähigkeit vorher geprüft hat, steht sie im Prozess voll zur Prüfung; stützen Sie die Klage auf den stärksten "
                  "Schutzanspruch. Schutzfähigkeit mit dem GebrM-Stand der Technik prüfen (keine älteren Anmeldungen, Schonfrist).\n\n"
                  "**In den Klausuren:** TS I/2022 (Prägemaschine, G1), TS III/2021 (Einwand und § 19 GebrMG), (RP1 III/2021 Frage 2d: Reaktion des "
                  "Beklagten auf Klagen aus Gebrauchsmuster und Design).",
                  concepts=["pat_verletzung", "pat_unterlassung", "pat_schadensersatz", "pat_rechtsfolgen_nebenanspruche", "pat_aussetzung"] + G,
                  norms=["§ 11 PatG", "§ 12 PatG", "§ 139 PatG", "§ 140a PatG", "§ 140b PatG"], cases=["pat_bgh_kunststoffbuegel"], abschnitt="Normenkette"),
            intro("p06e-1", "Definitionen",
                  "**Gegenstand des Gebrauchsmusters:** das durch die Schutzansprüche bestimmte Erzeugnis; Beschreibung und Zeichnungen sind zur Auslegung "
                  "heranzuziehen (§ 12a GebrMG)\n"
                  "**Anbieten:** jede Handlung, die das Erzeugnis der Nachfrage zum Erwerb äußerlich wahrnehmbar zugänglich macht, auch ohne Lieferbereitschaft "
                  "(BGH Kunststoffbügel, für § 9 S. 2 Nr. 1 PatG und § 11 Abs. 1 GebrMG gleich)\n"
                  "**Wiederholungsgefahr:** ernsthafte Gefahr erneuter Verletzung, durch eine vollendete Verletzung vermutet und nur durch strafbewehrte "
                  "Unterlassungserklärung auszuräumen (Rechtsprechung)\n"
                  "**Erstbegehungsgefahr:** ernsthaft und greifbar drohende erstmalige Verletzung (§ 24 Abs. 1 S. 2 GebrMG)\n"
                  "**Fahrlässigkeit:** Außerachtlassen der im Verkehr erforderlichen Sorgfalt (Legaldefinition § 276 Abs. 2 BGB); Gewerbetreibende müssen "
                  "sich über fremde Schutzrechte unterrichten\n"
                  "**Verletzer:** wer entgegen §§ 11 bis 14 GebrMG das Gebrauchsmuster benutzt (§ 24 Abs. 1 S. 1 GebrMG)\n"
                  "**Offensichtliche Rechtsverletzung (§ 24b Abs. 7 GebrMG):** Verletzung so eindeutig, dass eine Fehlentscheidung kaum möglich ist (Lehre)",
                  concepts=["pat_verletzung", "pat_unterlassung", "pat_schadensersatz", "pat_benutzungshandlungen", "pat_schutzbereich"],
                  cases=["pat_bgh_kunststoffbuegel"], abschnitt="Definitionen"),
            mc("p06e-2", "Benutzungshandlungen",
               "Welche Handlung verletzt ein Gebrauchsmuster auf eine Vorrichtung nicht unmittelbar?",
               ["Einfuhr der Vorrichtung zum Weiterverkauf", "Besitz der Vorrichtung zum Anbieten",
                "Anwendung eines mit der Vorrichtung ausführbaren Verfahrens im Ausland und Verkauf der Erzeugnisse im Inland", "Angebot auf einer Messe im Inland"], 2,
               ["**Verfahrenserzeugnisse.** § 11 Abs. 1 S. 2 GebrMG verbietet Herstellen, Anbieten, Inverkehrbringen, Gebrauchen, Einführen und "
                "Besitzen des Erzeugnisses, das Gegenstand des Gebrauchsmusters ist. Verfahren und ihre unmittelbaren Erzeugnisse sind nicht erfasst; "
                "eine Vorrichtung, die nur im Ausland genutzt wird, gibt keinen Anspruch."],
               merke="§ 11 Abs. 1 S. 2 GebrMG: nur Erzeugnis-Handlungen; kein Verfahrens(erzeugnis)schutz.", level=1, concepts=["pat_benutzungshandlungen"] + G,
               norms=["§ 9 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06e-3", "Muss das Gericht aussetzen?",
                 "Der Beklagte hat Löschung beantragt. Das Landgericht hält das Gebrauchsmuster nach eigener Prüfung für nicht schutzfähig.",
                 "Muss das Landgericht den Verletzungsrechtsstreit aussetzen?", True,
                 ["**Ja!** Ist während eines Löschungsverfahrens ein Rechtsstreit anhängig, der vom Bestehen des Gebrauchsmusterschutzes abhängt, kann "
                  "das Gericht aussetzen (§ 19 S. 1 GebrMG); es **hat** auszusetzen, wenn es die Eintragung für unwirksam hält (§ 19 S. 2 GebrMG). "
                  "Ohne anhängiges Löschungsverfahren würde es die Klage nach § 13 Abs. 1 GebrMG abweisen."],
                 merke="§ 19 S. 1 GebrMG kann aussetzen · S. 2 muss bei Unwirksamkeit · S. 3 Bindung nur inter partes.", level=3,
                 concepts=["pat_aussetzung"] + L, abschnitt="Definitionen und Normen"),
            fall("p06e-4", "Bindung an die Zurückweisung",
                 "Die Gebrauchsmusterabteilung hat den Löschungsantrag eines Dritten X bestandskräftig zurückgewiesen. Im Verletzungsprozess gegen Y beruft sich der Kläger auf diese Entscheidung.",
                 "Ist das Verletzungsgericht an die Zurückweisung gebunden?", False,
                 ["**Nein!** Ist der Löschungsantrag zurückgewiesen worden, bindet die Entscheidung das Gericht nur, wenn sie zwischen denselben Parteien "
                  "ergangen ist (§ 19 S. 3 GebrMG). Y kann die Schutzunfähigkeit weiter einwenden (§ 13 Abs. 1 GebrMG). Eine Löschung wirkt dagegen "
                  "gegenüber jedermann."],
                 merke="Zurückweisung bindet nur inter partes (§ 19 S. 3 GebrMG); Löschung wirkt erga omnes.", level=2,
                 concepts=["pat_aussetzung"] + L, abschnitt="Definitionen und Normen"),
            mc("p06e-5", "Schadensberechnung",
               "Welche Norm erlaubt die Berechnung des Schadensersatzes nach der Lizenzanalogie?",
               ["§ 24 Abs. 2 S. 3 GebrMG", "§ 24b Abs. 1 GebrMG", "§ 139 Abs. 1 PatG unmittelbar", "§ 24a Abs. 1 GebrMG"], 0,
               ["**§ 24 Abs. 2 S. 3 GebrMG.** Der Schaden kann auf der Grundlage der angemessenen Vergütung berechnet werden, die der Verletzer für "
                "eine Erlaubnis hätte zahlen müssen. Daneben stehen konkreter Schaden und Verletzergewinn (§ 24 Abs. 2 S. 2 GebrMG). Voraussetzung ist "
                "Vorsatz oder Fahrlässigkeit (§ 24 Abs. 2 S. 1 GebrMG)."],
               merke="Schadensersatz § 24 Abs. 2 GebrMG: Verschulden · konkret / Verletzergewinn (S. 2) / Lizenzanalogie (S. 3).", level=1,
               concepts=["pat_schadensersatz"], norms=["§ 139 Abs. 2 PatG"], abschnitt="Definitionen und Normen"),
            fall("p06e-6", "Einstweilige Verfügung aus dem Gebrauchsmuster",
                 "Die Inhaberin will einen Messeauftritt des Wettbewerbers per einstweiliger Verfügung unterbinden. Das Gebrauchsmuster ist ungeprüft; der Wettbewerber legt eine neuheitsschädliche Druckschrift vor.",
                 "Ist der Erlass einer einstweiligen Verfügung wahrscheinlich?", False,
                 ["**Nein!** Neben Verfügungsanspruch und Dringlichkeit (§ 935 ZPO, § 940 ZPO) verlangen die Gerichte einen hinreichend gesicherten "
                  "Rechtsbestand. Beim ungeprüften Gebrauchsmuster muss die Inhaberin die Schutzfähigkeit glaubhaft machen (§ 936 ZPO, § 920 Abs. 2 ZPO); "
                  "eine vorgelegte neuheitsschädliche Druckschrift steht dem entgegen."],
                 merke="Einstweilige Verfügung aus GBM: Rechtsbestand muss glaubhaft gesichert sein.", level=2, concepts=["pat_unterlassung"] + G,
                 abschnitt="Definitionen und Normen"),
            fall("p06e-7", "Vorbenutzung",
                 "F hat die erfindungsgemäße Fahrradnabe vor dem Zeitrangtag des Gebrauchsmusters im Inland entwickelt und in seinem Betrieb bereits hergestellt, ohne sie öffentlich zugänglich zu machen.",
                 "Kann F sich gegen die Unterlassungsklage auf ein Vorbenutzungsrecht berufen?", True,
                 ["**Ja!** Die Vorschriften des PatG über das Vorbenutzungsrecht gelten entsprechend (§ 13 Abs. 3 GebrMG i.V.m. § 12 Abs. 1 PatG). F "
                  "war im Erfindungsbesitz und hat die Erfindung im Inland benutzt; er darf sie für die Bedürfnisse seines Betriebs weiter nutzen. Mangels "
                  "Öffentlichkeit ist die Nutzung kein Stand der Technik."],
                 merke="Vorbenutzungsrecht beim GBM: § 13 Abs. 3 GebrMG i.V.m. § 12 PatG.", level=2, concepts=["pat_vorbenutzungsrecht"],
                 norms=["§ 12 Abs. 1 PatG"], abschnitt="Definitionen und Normen"),
            *fallkette("p06e-8", "Prägemaschine (nach TS I/2022)",
                "Die P GmbH ist Inhaberin des am 10.12.2019 eingetragenen Gebrauchsmusters G1 (Anmeldetag 19.9.2019) auf eine Prägemaschine mit zweiter "
                "Prägewalze und Goldprägung (Schutzansprüche 1 bis 5). Die Hessenleder AG verkauft eine Maschine, die die Schutzansprüche 1, 2, 4 und 5 "
                "verwirklicht. Eine ältere, erst danach veröffentlichte EP-Anmeldung zeigt Anspruch 1.",
                [frage("Besteht G1 noch, so dass Ansprüche aus § 24 GebrMG in Betracht kommen?", True,
                       ["**Ja!** Das Gebrauchsmuster ist eingetragen (§ 11 Abs. 1 GebrMG); die Schutzdauer läuft bis 30.9.2029 (§ 23 Abs. 1 GebrMG), "
                        "sofern die Aufrechterhaltungsgebühren gezahlt werden (§ 23 Abs. 2 GebrMG)."],
                       merke="V1: eingetragen, Schutzdauer, nicht erloschen."),
                 frage("Benutzt die Hessenleder AG den Gegenstand des Gebrauchsmusters?", True,
                       ["**Ja!** Sie bringt ein Erzeugnis in Verkehr und bietet es an, das die Merkmale der Schutzansprüche 1, 2, 4 und 5 wortsinngemäß "
                        "verwirklicht (§ 11 Abs. 1 S. 2 GebrMG, § 12a GebrMG)."],
                       merke="V3: Merkmalsanalyse der Schutzansprüche (§ 12a GebrMG)."),
                 frage("Kann die Hessenleder AG die ältere EP-Anmeldung als neuheitsschädlich einwenden?", False,
                       ["**Nein!** Ältere nachveröffentlichte Anmeldungen sind kein Stand der Technik (§ 3 Abs. 1 S. 2 GebrMG). Sie zählen nur über "
                        "§ 15 Abs. 1 Nr. 2 GebrMG, wenn daraus ein Schutzrecht mit identischem Gegenstand entstanden ist; dann fehlt der Schutz nach "
                        "§ 13 Abs. 1 GebrMG."],
                       merke="Einwand § 13 Abs. 1 GebrMG mit dem GebrM-Stand der Technik prüfen.", concepts=["pat_doppelschutz"]),
                 frage("Sollte die P GmbH die Klage vor allem auf Schutzanspruch 5 stützen?", True,
                       ["**Ja!** Das Gericht prüft die Schutzfähigkeit inzident (§ 13 Abs. 1 GebrMG). Schutzanspruch 5 (Goldprägung) hat die Prüfungsstelle "
                        "im Parallelpatent für patentfähig gehalten; Anspruch 1 ist angreifbar. Die Verletzung des engeren Anspruchs genügt für alle Ansprüche."],
                       merke="Klage auf den stärksten verletzten Schutzanspruch stützen."),
                 frage("Hat die P GmbH neben Unterlassung auch Anspruch auf Auskunft über Herkunft und Vertriebsweg?", True,
                       ["**Ja!** Wer entgegen §§ 11 bis 14 GebrMG benutzt, schuldet unverzügliche Auskunft über Herkunft und Vertriebsweg (§ 24b Abs. 1 "
                        "GebrMG); Verschulden ist nicht nötig. Schadensersatz verlangt Fahrlässigkeit (§ 24 Abs. 2 GebrMG), die beim Gewerbetreibenden "
                        "regelmäßig vorliegt."],
                       merke="Auskunft § 24b GebrMG verschuldensunabhängig; Schadensersatz § 24 Abs. 2 GebrMG mit Verschulden.",
                       concepts=["pat_rechtsfolgen_nebenanspruche"]),
                ], abschnitt="Klausurfall", level=2, concepts=["pat_verletzung"] + G),
            *fallkette("p06e-9", "Klage aus Gebrauchsmuster und Design (nach RP1 III/2021)",
                "P verklagt K aus seinem Gebrauchsmuster auf eine Inkubationsrinne und zugleich aus einem eingetragenen Design. K hält beide Rechte für "
                "nicht rechtsbeständig und fragt, was er tun kann.",
                [frage("Kann K die fehlende Schutzfähigkeit des Gebrauchsmusters im Verletzungsprozess selbst einwenden?", True,
                       ["**Ja!** Der Gebrauchsmusterschutz entsteht nicht, soweit ein Löschungsanspruch für jedermann besteht (§ 13 Abs. 1 GebrMG). Das "
                        "Landgericht prüft das inzident; ein Trennungsprinzip wie beim Patent gibt es nicht."],
                       merke="GBM: Schutzunfähigkeit als Einwand im Verletzungsprozess.", concepts=["pat_trennungsprinzip"]),
                 frage("Ist es zusätzlich sinnvoll, beim DPMA Löschung zu beantragen?", True,
                       ["**Ja!** Die Löschung wirkt gegenüber jedermann; mit anhängigem Löschungsverfahren kann K die Aussetzung beantragen (§ 19 S. 1 "
                        "GebrMG), die das Gericht anordnen muss, wenn es die Eintragung für unwirksam hält (§ 19 S. 2 GebrMG)."],
                       merke="Löschungsantrag + Aussetzungsantrag § 19 GebrMG.", concepts=L + ["pat_aussetzung"]),
                 frage("Kann K gegen das eingetragene Design ebenso nur einwenden, es sei nicht rechtsbeständig?", False,
                       ["**Nein!** Beim eingetragenen Design wird die Rechtsgültigkeit vermutet (§ 39 DesignG). Den Einwand der Nichtigkeit kann K nur "
                        "durch Widerklage oder Antrag beim DPMA geltend machen (§ 52a DesignG); beim Gebrauchsmuster genügt der Einwand."],
                       merke="Design: Widerklage oder Nichtigkeitsantrag (§ 52a DesignG); GBM: Einwand (§ 13 Abs. 1 GebrMG).",
                       norms=["§ 39 DesignG", "§ 52a DesignG"]),
                ], abschnitt="Klausurfall", level=2, concepts=["pat_verletzung"] + G),
        ]),

        # ================================================================== §§ 4, 8, 23 GebrMG
        dict(id="p06f", titel="§§ 4, 8, 23 GebrMG: Eintragung und Schutzdauer", einheiten=[
            intro("p06f-0", "Prüfungsschema",
                  "**AGL:** § 8 Abs. 1 S. 1 GebrMG (Anspruch auf Eintragung) · § 23 GebrMG (Schutzdauer und Aufrechterhaltung)\n\n"
                  "**A · Eintragung**\n"
                  "**V1 Anmeldung beim DPMA** – § 4 Abs. 1 GebrMG (oder Patentinformationszentrum, § 4 Abs. 2 GebrMG); eine Erfindung je Anmeldung\n"
                  "**V2 Anmeldetag** – Eingang von Name, Eintragungsantrag und Beschreibung (§ 4a Abs. 1 GebrMG i.V.m. § 4 Abs. 3 Nr. 1, 2, 4 GebrMG); "
                  "fehlende Zeichnungen oder Teile: Nachreichung binnen eines Monats verschiebt den Anmeldetag (§ 4a Abs. 2, 3 GebrMG)\n"
                  "**V3 Inhalt** – Name, Antrag, Schutzansprüche, Beschreibung, Zeichnungen (§ 4 Abs. 3 GebrMG); Form nach der GebrMV (§ 4 Abs. 4 GebrMG)\n"
                  "**V4 Sprache** – deutsche Übersetzung binnen drei Monaten, sonst Rücknahmefiktion (§ 4b GebrMG)\n"
                  "**V5 Gebühr** – 30 EUR elektronisch, 40 EUR Papier (Nr. 321 000, Nr. 321 100 Anlage PatKostG); zahlbar binnen drei Monaten "
                  "(§ 6 Abs. 1 S. 2 PatKostG), sonst gilt die Anmeldung als zurückgenommen (§ 6 Abs. 2 PatKostG)\n"
                  "**V6 Kein Schutzhindernis nach § 2 GebrMG**; keine Prüfung von Neuheit, erfinderischem Schritt, gewerblicher Anwendbarkeit (§ 8 Abs. 1 S. 2 GebrMG)\n"
                  "**⇒** Eintragung ins Register (§ 8 Abs. 1 S. 1 GebrMG), Bekanntmachung im Patentblatt (§ 8 Abs. 3 GebrMG); auf Antrag Aussetzung "
                  "der Eintragung bis 15 Monate ab Anmelde- oder Prioritätstag (§ 8 Abs. 1 S. 3 GebrMG i.V.m. § 49 Abs. 2 PatG); Änderungen bis zur "
                  "Verfügung über die Eintragung ohne Erweiterung (§ 4 Abs. 5 GebrMG); Teilung jederzeit (§ 4 Abs. 6 GebrMG); Beschwerde gegen die "
                  "Zurückweisung (§ 18 Abs. 1 GebrMG, 200 EUR Nr. 401 300 Anlage PatKostG)\n\n"
                  "**B · Schutzdauer**\n"
                  "**V7 Höchstdauer** – Beginn mit dem Anmeldetag, Ende zehn Jahre nach Ablauf des Anmeldemonats (§ 23 Abs. 1 GebrMG)\n"
                  "**V8 Aufrechterhaltung** – Gebühren für das 4. bis 6., 7. und 8., 9. und 10. Jahr (§ 23 Abs. 2 GebrMG): 210, 350, 530 EUR; fällig am "
                  "letzten Tag des Anmeldemonats (§ 3 Abs. 2 S. 1 PatKostG), bei späterer Eintragung am Ende des Eintragungsmonats (§ 3 Abs. 2 S. 2 "
                  "PatKostG); zahlbar bis Ablauf des zweiten Monats, mit Zuschlag 50 EUR bis Ablauf des sechsten Monats nach Fälligkeit (§ 7 Abs. 1 PatKostG); "
                  "Vorauszahlung höchstens ein Jahr vor Fälligkeit (§ 5 Abs. 2 PatKostG)\n"
                  "**⇒ Erlöschen** durch Verzicht (§ 23 Abs. 3 Nr. 1 GebrMG) oder Nichtzahlung (§ 23 Abs. 3 Nr. 2 GebrMG)\n\n"
                  "**Klausurfallen:** Schutzdauerende wird nicht nach § 193 BGB verschoben, Zahlungsfristen schon. Beim abgezweigten Gebrauchsmuster "
                  "laufen Schutzdauer und Fälligkeit ab dem abgezweigten Anmeldetag; ist die erste Schutzfrist schon vorbei, wird die Gebühr am Ende des "
                  "Eintragungsmonats fällig.\n\n"
                  "**In den Klausuren:** TS II/2018, TS II/2019 (Fälligkeit 30.6.2018), TS II/2020, TS I/2021, TS III/2021, TS I/2022, TS II/2022; "
                  "(RP1 III/2021: Mangel nach der GebrMV, Aussetzung der Eintragung um zwölf Monate).",
                  concepts=G + ["pat_laufzeit_jahresgebuehren", "pat_faelligkeit", "pat_zahlungsfristen"],
                  norms=["§ 49 Abs. 2 PatG", "§ 3 Abs. 2 PatKostG", "§ 5 Abs. 2 PatKostG", "§ 6 Abs. 1 PatKostG", "§ 7 Abs. 1 PatKostG"], abschnitt="Normenkette"),
            intro("p06f-1", "Definitionen",
                  "**Anmeldetag:** Tag des Eingangs der Unterlagen nach § 4 Abs. 3 Nr. 1, 2 GebrMG und von Angaben, die dem Anschein nach eine Beschreibung "
                  "sind (Legaldefinition § 4a Abs. 1 GebrMG)\n"
                  "**Schutzanspruch:** Angabe, was als schutzfähig unter Schutz gestellt werden soll (§ 4 Abs. 3 Nr. 3 GebrMG)\n"
                  "**Schutzdauer:** Zeitraum ab dem Anmeldetag bis zehn Jahre nach Ablauf des Anmeldemonats (§ 23 Abs. 1 GebrMG)\n"
                  "**Aufrechterhaltungsgebühr:** Gebühr für eine weitere Schutzfrist (4. bis 6., 7. und 8., 9. und 10. Jahr), gerechnet vom Anmeldetag "
                  "(§ 23 Abs. 2 GebrMG)\n"
                  "**Fälligkeit (§ 3 Abs. 2 S. 1 PatKostG):** letzter Tag des Monats, der durch seine Benennung dem Anmeldemonat entspricht\n"
                  "**Recherche (§ 7 Abs. 1 GebrMG):** auf Antrag des Anmelders, Inhabers oder jedes Dritten ermittelter Stand der Technik zur Beurteilung "
                  "der Schutzfähigkeit, 250 EUR (Nr. 321 200 Anlage PatKostG); spätere Anträge gelten als nicht gestellt (§ 7 Abs. 4 GebrMG)",
                  concepts=G + ["pat_laufzeit_jahresgebuehren", "pat_faelligkeit", "pat_anmeldetag"], norms=["§ 3 Abs. 2 PatKostG"], abschnitt="Definitionen"),
            mc("p06f-2", "Erste Aufrechterhaltungsgebühr",
               "Ein Gebrauchsmuster wurde am 15.5.2026 angemeldet und im Juli 2026 eingetragen. Wann ist die erste Aufrechterhaltungsgebühr fällig, bis wann zuschlagsfrei zahlbar?",
               ["Fällig 15.5.2029, zahlbar bis 15.7.2029", "Fällig 31.5.2029, zahlbar bis 31.7.2029",
                "Fällig 31.7.2026, zahlbar bis 30.9.2026", "Fällig 31.5.2029, zahlbar bis 30.11.2029"], 1,
               ["**31.5.2029 / 31.7.2029.** Die Gebühr für das 4. bis 6. Jahr wird am letzten Tag des Monats fällig, der dem Anmeldemonat entspricht "
                "(§ 3 Abs. 2 S. 1 PatKostG), und ist bis Ablauf des zweiten Monats danach zu zahlen (§ 7 Abs. 1 S. 1 PatKostG); mit 50 EUR Zuschlag bis "
                "30.11.2029 (§ 7 Abs. 1 S. 2 PatKostG). Betrag 210 EUR (Nr. 322 100 Anlage PatKostG)."],
               merke="Fälligkeit § 3 Abs. 2 PatKostG · Zahlung § 7 Abs. 1 PatKostG (2 bzw. 6 Monate) · sonst § 23 Abs. 3 Nr. 2 GebrMG.", level=2,
               concepts=["pat_faelligkeit", "pat_zahlungsfristen"], norms=["§ 3 Abs. 2 PatKostG", "§ 7 Abs. 1 PatKostG"], abschnitt="Definitionen und Normen"),
            fall("p06f-3", "Späte Eintragung",
                 "Ein Gebrauchsmuster wird am 1.6.2015 abgezweigt angemeldet (Anmeldetag der Patentanmeldung) und erst im Oktober 2018 eingetragen.",
                 "Wird die Gebühr für das 4. bis 6. Jahr am 30.6.2018 fällig?", False,
                 ["**Nein!** Wird ein Gebrauchsmuster erst nach Beendigung der ersten Schutzfrist eingetragen, ist die Aufrechterhaltungsgebühr am "
                  "letzten Tag des Eintragungsmonats fällig (§ 3 Abs. 2 S. 2 PatKostG), hier am 31.10.2018. Zahlbar ist sie dann bis 31.12.2018 "
                  "(§ 7 Abs. 1 S. 1 PatKostG)."],
                 merke="Eintragung nach Ablauf der ersten Schutzfrist: Fälligkeit Ende des Eintragungsmonats (§ 3 Abs. 2 S. 2 PatKostG).", level=3,
                 concepts=["pat_faelligkeit"] + A, norms=["§ 3 Abs. 2 PatKostG", "§ 7 Abs. 1 PatKostG"], abschnitt="Definitionen und Normen"),
            fall("p06f-4", "Aussetzung der Eintragung",
                 "P will, dass sein Gebrauchsmuster erst später eingetragen und bekanntgemacht wird, weil er noch Auslandsanmeldungen vorbereitet. Er beantragt die Aussetzung der Eintragung um zwölf Monate.",
                 "Ist eine Aussetzung der Eintragung möglich?", True,
                 ["**Ja!** § 8 Abs. 1 S. 3 GebrMG erklärt § 49 Abs. 2 PatG für entsprechend anwendbar: Auf Antrag wird die Eintragung bis zum Ablauf "
                  "von fünfzehn Monaten ab dem Anmelde- oder Prioritätstag ausgesetzt. Bis zur Eintragung kann P die Anmeldung noch zurücknehmen "
                  "(RP1 III/2021)."],
                 merke="Aussetzung der Eintragung: § 8 Abs. 1 S. 3 GebrMG i.V.m. § 49 Abs. 2 PatG, max. 15 Monate.", level=2, concepts=G,
                 norms=["§ 49 Abs. 2 PatG"], abschnitt="Definitionen und Normen"),
            mc("p06f-5", "Anmeldung in englischer Sprache",
               "Eine Gebrauchsmusteranmeldung wird in englischer Sprache eingereicht. Was gilt?",
               ["Sie erhält keinen Anmeldetag", "Deutsche Übersetzung binnen drei Monaten nach Einreichung, sonst gilt sie als zurückgenommen (§ 4b GebrMG)",
                "Übersetzung binnen zwölf Monaten (§ 35a PatG entsprechend)", "Übersetzung auf Aufforderung binnen eines Monats"], 1,
               ["**§ 4b GebrMG.** Die fremdsprachige Anmeldung erhält einen Anmeldetag (§ 4a Abs. 1 GebrMG). Die deutsche Übersetzung ist binnen drei "
                "Monaten nach Einreichung nachzureichen; sonst gilt die Anmeldung als zurückgenommen. Die Frist des § 35a PatG für Patente in "
                "englischer Sprache gilt nicht."],
               merke="Übersetzung GBM: 3 Monate ab Einreichung (§ 4b GebrMG).", level=2, concepts=G + ["pat_anmeldetag"], norms=["§ 35a PatG"],
               abschnitt="Definitionen und Normen"),
            fall("p06f-6", "Recherche durch den Wettbewerber",
                 "Der Anmelder hat bereits eine Recherche nach § 7 GebrMG beantragt. Ein Wettbewerber stellt danach ebenfalls einen Rechercheantrag und zahlt 250 EUR.",
                 "Wird für den Wettbewerber eine eigene Recherche durchgeführt?", False,
                 ["**Nein!** Ist ein Antrag nach § 7 Abs. 1 GebrMG eingegangen, gelten spätere Anträge als nicht gestellt (§ 7 Abs. 4 S. 1 GebrMG). Der "
                  "Wettbewerber kann aber jederzeit Hinweise zum Stand der Technik geben (§ 7 Abs. 3 S. 3 GebrMG). Das Ergebnis wird ohne Gewähr "
                  "mitgeteilt (§ 7 Abs. 6 GebrMG)."],
                 merke="Recherche § 7 GebrMG: jedermann, 250 EUR, nur ein Antrag.", level=2, concepts=G, norms=["§ 43 Abs. 4 PatG"],
                 abschnitt="Definitionen und Normen"),
            fall("p06f-7", "Gebühr vergessen",
                 "Die Gebühr für das 7. und 8. Schutzjahr eines Gebrauchsmusters war am 31.3.2026 fällig. Der Inhaber zahlt weder zuschlagsfrei binnen zwei Monaten noch mit Zuschlag bis 30.9.2026.",
                 "Ist das Gebrauchsmuster erloschen?", True,
                 ["**Ja!** Die Aufrechterhaltungsgebühr wurde nicht rechtzeitig gezahlt (§ 7 Abs. 1 PatKostG); das Gebrauchsmuster erlischt "
                  "(§ 23 Abs. 3 Nr. 2 GebrMG). War der Inhaber ohne Verschulden verhindert, bleibt die Wiedereinsetzung binnen zwei Monaten nach "
                  "Wegfall des Hindernisses (§ 21 Abs. 1 GebrMG i.V.m. § 123 Abs. 1, 2 PatG)."],
                 merke="Erlöschen § 23 Abs. 3 Nr. 2 GebrMG · Zahlungsfristen § 7 Abs. 1 PatKostG · Rettung § 123 PatG.", level=1,
                 concepts=["pat_zahlungsfristen", "pat_wiedereinsetzung"] + G, norms=["§ 7 Abs. 1 PatKostG", "§ 123 PatG"], abschnitt="Definitionen und Normen"),
            *fallkette("p06f-8", "Rinne mit Mängeln (nach RP1 III/2021)",
                "PA reicht am 1.7.2021 für P eine Gebrauchsmusteranmeldung ein. Das DPMA rügt am 21.7.2021 einen Formmangel nach der GebrMV mit "
                "einer Frist von drei Monaten; PA behebt ihn am 4.9.2021. Auf Antrag setzt das DPMA die Eintragung um zwölf Monate aus.",
                [frage("Behält die Anmeldung den Anmeldetag 1.7.2021?", True,
                       ["**Ja!** Der Anmeldetag hängt nur am Eingang von Name, Eintragungsantrag und Beschreibung (§ 4a Abs. 1 GebrMG). Formmängel nach "
                        "der GebrMV (§ 4 Abs. 4 GebrMG) verschieben ihn nicht, wenn sie fristgerecht behoben werden."],
                       merke="Formmangel ≠ Anmeldetagsmangel (§ 4a Abs. 1 GebrMG).", concepts=["pat_anmeldetag"]),
                 frage("Prüft das DPMA vor der Eintragung, ob die Rinne neu ist?", False,
                       ["**Nein!** Eine Prüfung auf Neuheit, erfinderischen Schritt und gewerbliche Anwendbarkeit findet nicht statt (§ 8 Abs. 1 S. 2 "
                        "GebrMG). Geprüft werden Form und Schutzhindernisse (§ 2 GebrMG)."],
                       merke="§ 8 Abs. 1 S. 2 GebrMG: keine Sachprüfung."),
                 frage("Kann P vor Ablauf der Aussetzung aus dem Gebrauchsmuster gegen Nachahmer vorgehen?", False,
                       ["**Nein!** Die Schutzwirkung entsteht erst mit der Eintragung (§ 11 Abs. 1 GebrMG). Bis dahin bleibt P nur ein Vorgehen aus "
                        "anderen Rechten, etwa dem Design. Er kann die Aussetzung aber beenden lassen."],
                       merke="Keine Rechte vor Eintragung (§ 11 Abs. 1 GebrMG)."),
                 frage("Endet der Schutz am 31.7.2031, wenn alle Gebühren gezahlt werden?", True,
                       ["**Ja!** Zehn Jahre nach Ablauf des Anmeldemonats Juli 2021 (§ 23 Abs. 1 GebrMG); die Aussetzung der Eintragung verlängert die "
                        "Schutzdauer nicht."],
                       merke="Schutzdauer läuft ab Anmeldetag, unabhängig vom Eintragungstag."),
                ], abschnitt="Klausurfall", level=2, concepts=G),
        ]),
    ],
)
