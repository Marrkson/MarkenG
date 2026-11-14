# -*- coding: utf-8 -*-
"""Kurs 15: Anspruchsgrundlagen Marken – Anspruchsgrundlage für Anspruchsgrundlage für die NS-Klausur.

Je Kapitel eine Anspruchsgrundlage bzw. ein Rechtsbehelf: Prüfungsschema in der Lösungssprache (AGL → V1 … Vn mit Norm →
Rechtsfolge), Definitionen, Drill-Fragen zu Normen und Begriffen, danach Klausurfälle als Fallketten in der Reihenfolge
des Schemas. Grundlage: Lösung NS II/2019 (klausuren/loesungen/ns), Aufgabentexte NS II/2018 bis III/2023, Kurse k12/k13,
`klausur.py`. MarkenG in der Fassung 2026 (data/markeng.json), Gebühren nach der Anlage zu § 2 Abs. 1 PatKostG.

Konvention: Im Fließtext jedes Zitat mit Gesetz („§ 42 Abs. 1 MarkenG“). In `norms` nur MarkenG, PatKostG und MarkenRL;
ZPO, BGB, MarkenV, PatKostZV, VwZG, UMV, HGB nur im Fließtext.
"""
from ._helpers import intro, fall, mc, frage, fallkette

N = "Definitionen und Normen"
K = "Klausurfall"

KURS = dict(
    id="k15", gebiet="marken", reihe="Anspruchsgrundlagen für die Klausur", kompakt="fragen",
    titel="Anspruchsgrundlagen Marken", untertitel="Widerspruch, Einrede, Nichtigkeit, Verfall, Verletzung, Rechtsbehelfe, Kosten – Normenketten zum Auswendiglernen",
    farbe="#1482e3", icon="hammer",
    beschreibung="Jede Anspruchsgrundlage der NS-Klausur als Prüfungsschema mit Normenkette (Frist, Form, Gebühr, Berechtigung, Rechtsfolge), "
                 "den Definitionen, die in der Klausur verlangt werden, Drill-Fragen und Klausurfällen nach den NS-Klausuren II/2018 bis III/2023.",
    kapitel=[
        # ==============================================================
        dict(id="k150", titel="Überblick: Anspruchsgrundlagen und Fristen", einheiten=[
            intro("k150-0", "Die Anspruchsgrundlagen im Überblick",
                  "**Prüfungsaufbau jeder AGL:** 0 · Wirksamkeit (Gebühr gezahlt? § 64a MarkenG i.V.m. § 6 Abs. 2 PatKostG) → A · Zulässigkeit → B · Begründetheit → ⇒ Rechtsfolge. "
                  "Fehlt die Gebühr, gilt die Handlung als nicht vorgenommen; das ist kein Unzulässigkeitsgrund, sondern ein Nichtakt.\n\n"
                  "**Ziel des Mandanten → AGL**\n"
                  "**Jüngere Marke schnell und billig beseitigen (bis drei Monate nach Veröffentlichung)** → Widerspruch § 42 Abs. 1 MarkenG i.V.m. § 42 Abs. 2 Nr. 1–5 MarkenG, Löschung § 43 Abs. 2 S. 1 MarkenG (Kapitel k15a)\n"
                  "**Sich gegen den Widerspruch aus einer unbenutzten Marke verteidigen** → Einrede § 43 Abs. 1 S. 1 MarkenG i.V.m. § 26 MarkenG (k15b)\n"
                  "**Kollision begründen** → § 9 Abs. 1 Nr. 1 MarkenG (Doppelidentität), § 9 Abs. 1 Nr. 2 MarkenG (Verwechslungsgefahr), § 9 Abs. 1 Nr. 3 MarkenG (bekannte Marke) (k15c)\n"
                  "**Bösgläubige oder beschreibende Marke löschen** → § 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 MarkenG, Antrag § 53 Abs. 1 MarkenG (k15d)\n"
                  "**Nach Ablauf der Widerspruchsfrist aus älterem Recht vorgehen** → § 51 Abs. 1 MarkenG i.V.m. § 9 bis § 13 MarkenG; Antrag § 53 MarkenG oder Klage § 55 MarkenG (k15e)\n"
                  "**Unbenutzte oder zur Gattung gewordene Marke löschen** → § 49 Abs. 1, 2 MarkenG; Antrag § 53 MarkenG oder Klage § 55 MarkenG (k15f)\n"
                  "**Benutzung eines Zeichens verbieten, Schadensersatz** → § 14 Abs. 5, 6 MarkenG, § 15 Abs. 4, 5 MarkenG, § 18 MarkenG, § 19 MarkenG; LG § 140 Abs. 1 MarkenG (k15g)\n"
                  "**Beschluss des DPMA angreifen** → Erinnerung § 64 MarkenG, Beschwerde § 66 MarkenG; gegen das BPatG Rechtsbeschwerde § 83 MarkenG (k15h)\n"
                  "**Frist versäumt** → Wiedereinsetzung § 91 MarkenG, Weiterbehandlung § 91a MarkenG (k15i)\n"
                  "**Kosten vom Gegner** → § 63 MarkenG (DPMA), § 71 MarkenG (BPatG), § 91 ZPO mit § 140 Abs. 4 MarkenG (Gericht) (k15j)\n\n"
                  "**Beschwerdeklausur (Perspektive BPatG):** Zulässigkeit der Beschwerde → Begründetheit der Beschwerde; darin Wirksamkeit, Zulässigkeit und Begründetheit des Widerspruchs bzw. Antrags.\n\n"
                  "**Klausuren:** Fast jede NS-Klausur seit 2018 ist ein Widerspruchs- oder Beschwerdefall (NS III/2018, I/2019, III/2019, III/2020, II/2021, III/2021, I/2022, III/2022, II/2023); "
                  "Beratungsklausuren fragen nach Nichtigkeit, Verfall und Verletzung (NS II/2019, I/2020, I/2021, II/2022, I/2023).",
                  concepts=["widerspruch", "nichtigkeit", "verfall", "beschwerde", "zahlungstag"],
                  norms=["§ 42 MarkenG", "§ 43 MarkenG", "§ 49 MarkenG", "§ 50 MarkenG", "§ 51 MarkenG", "§ 53 MarkenG", "§ 14 MarkenG", "§ 66 MarkenG", "§ 91 MarkenG", "§ 63 MarkenG"],
                  abschnitt="Normenkette"),
            intro("k150-1", "Fristen und Gebühren",
                  "Je Zeile: **Frist** · Norm · Berechnung · Verschiebung · Gebühr.\n\n"
                  "**Widerspruch:** drei Monate nach dem Tag der Veröffentlichung · § 42 Abs. 1 S. 1 MarkenG (IR-Marke: Beginn erster Tag des Folgemonats, § 114 Abs. 2 MarkenG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · 250 € Nr. 331 600, je weiteres Kennzeichen 50 € Nr. 331 610 (Anlage PatKostG), in der Frist zu zahlen (§ 6 Abs. 1 S. 1 PatKostG), sonst nicht erhoben (§ 6 Abs. 2 PatKostG); keine Wiedereinsetzung (§ 91 Abs. 1 S. 2 MarkenG)\n"
                  "**Erinnerung:** ein Monat nach Zustellung · § 64 Abs. 2 MarkenG · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB · 150 € Nr. 333 000\n"
                  "**Beschwerde:** ein Monat nach Zustellung, beim DPMA · § 66 Abs. 2 MarkenG · § 82 Abs. 1 MarkenG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 222 Abs. 2 ZPO · 200 € Nr. 401 300, in Verfalls- und Nichtigkeitsverfahren 500 € Nr. 401 100\n"
                  "**Rechtsbeschwerde:** ein Monat nach Zustellung, beim BGH · § 85 Abs. 1 MarkenG; Begründung ein Monat ab Einlegung § 85 Abs. 3 MarkenG · § 222 ZPO\n"
                  "**Widerspruch des Inhabers gegen Verfalls- oder Nichtigkeitsantrag:** zwei Monate nach Zustellung der Mitteilung · § 53 Abs. 4, 5 MarkenG · BGB wie oben; Weiterverfolgung des Verfallsantrags ein Monat nach Zustellung des Widerspruchs · § 53 Abs. 5 S. 4 MarkenG · 300 € Nr. 333 450\n"
                  "**Verfalls- und Nichtigkeitsantrag:** keine Antragsfrist (Ausnahme § 50 Abs. 2 S. 3 MarkenG: zehn Jahre seit Eintragung für § 8 Abs. 2 Nr. 1–3 MarkenG) · Verfall 100 € Nr. 333 400, Nichtigkeit 400 € Nr. 333 300, je weiteres älteres Recht 100 € Nr. 333 350; Zahlung drei Monate ab Fälligkeit (§ 3 Abs. 1 PatKostG, § 6 Abs. 1 S. 2 PatKostG)\n"
                  "**Wiedereinsetzung:** zwei Monate nach Wegfall des Hindernisses, höchstens ein Jahr nach Fristablauf · § 91 Abs. 2, 5 MarkenG\n"
                  "**Weiterbehandlung:** ein Monat nach Zustellung der Zurückweisung · § 91a Abs. 2 MarkenG · 100 € Nr. 333 050\n\n"
                  "**Zeiträume (keine Verschiebung nach § 193 BGB):** Benutzungszeitraum im Widerspruch fünf Jahre vor Anmelde- oder Prioritätstag der angegriffenen Marke (§ 43 Abs. 1 S. 1 MarkenG); Schonfrist fünf Jahre (§ 26 Abs. 5 MarkenG, § 49 Abs. 1 S. 1 MarkenG); Duldung fünf Jahre (§ 51 Abs. 2 MarkenG, § 21 Abs. 1 MarkenG); Amtsnichtigkeit zwei Jahre ab Eintragung (§ 50 Abs. 3 Nr. 1 MarkenG).\n\n"
                  "**Zustellung und Zahlung:** Einschreiben am vierten Tag nach Aufgabe zur Post (§ 94 Abs. 1 MarkenG i.V.m. § 4 Abs. 2 S. 2 VwZG), Abholfach am dritten Tag nach Niederlegung (§ 94 Abs. 1 Nr. 3 MarkenG); Zahlungstag: Überweisung Gutschrift (§ 2 Nr. 1 PatKostZV), SEPA-Mandat Eingang beim DPMA (§ 2 Nr. 3 PatKostZV).",
                  concepts=["fristberechnung", "zahlungstag", "zustellung"],
                  norms=["§ 42 MarkenG", "§ 64 MarkenG", "§ 66 MarkenG", "§ 85 MarkenG", "§ 53 MarkenG", "§ 91 MarkenG", "§ 91a MarkenG", "§ 94 MarkenG", "§ 6 PatKostG", "Anlage PatKostG"],
                  abschnitt="Fristen"),
            mc("k150-2", "Die frisch veröffentlichte Marke",
               "Die Eintragung einer ähnlichen jüngeren Marke für identische Waren ist vor sechs Wochen veröffentlicht worden. Welche AGL ist der schnellste und billigste Weg?",
               ["Widerspruch nach § 42 Abs. 1 MarkenG i.V.m. § 42 Abs. 2 Nr. 1, § 9 Abs. 1 Nr. 2 MarkenG",
                "Nichtigkeitsantrag nach § 50 Abs. 1 MarkenG",
                "Verfallsantrag nach § 49 Abs. 1 MarkenG",
                "Unterlassungsklage nach § 14 Abs. 5 MarkenG gegen die Eintragung"], 0,
               ["**Widerspruch.** Die Dreimonatsfrist des § 42 Abs. 1 S. 1 MarkenG läuft noch; die Gebühr beträgt 250 € (Nr. 331 600 Anlage PatKostG), vor dem DPMA herrscht kein Anwaltszwang.",
                "§ 50 MarkenG erfasst nur absolute Schutzhindernisse, § 49 MarkenG setzt fünf Jahre Nichtbenutzung voraus. Die Verletzungsklage richtet sich gegen die Benutzung, nicht gegen die Eintragung."],
               merke="Ältere Marke + Frist offen ⇒ Widerspruch § 42 MarkenG; Frist abgelaufen ⇒ § 51 MarkenG mit § 53 oder § 55 MarkenG.",
               level=1, concepts=["widerspruch"], norms=["§ 42 Abs. 1 MarkenG", "§ 42 Abs. 2 MarkenG"], abschnitt="Ziel des Mandanten"),
            mc("k150-3", "Die Widerspruchsfrist ist abgelaufen",
               "Die Mandantin bemerkt die verwechselbare jüngere Marke erst ein Jahr nach deren Veröffentlichung. Welcher Weg bleibt im Jahr 2026?",
               ["Keiner; die Eintragung ist bestandskräftig",
                "Antrag auf Erklärung der Nichtigkeit wegen älterer Rechte beim DPMA (§ 51 Abs. 1, § 53 Abs. 1 MarkenG) oder Klage vor dem LG (§ 55 MarkenG)",
                "Widerspruch mit Wiedereinsetzung in die Widerspruchsfrist",
                "Nur die Klage vor dem LG"], 1,
               ["**§ 51 Abs. 1 MarkenG mit § 53 oder § 55 MarkenG.** Seit 1. Mai 2020 kann die Nichtigkeit wegen älterer Rechte auch beim DPMA beantragt werden; vorher blieb nur die Klage.",
                "Wiedereinsetzung in die Widerspruchsfrist ist ausgeschlossen (§ 91 Abs. 1 S. 2 MarkenG)."],
               merke="Ältere Rechte nach Fristablauf: § 51 MarkenG – DPMA (§ 53 MarkenG, 400 €) oder LG (§ 55, § 140 Abs. 1 MarkenG).",
               level=1, concepts=["nichtigkeit", "verwaltungsverfahren_loeschung"], norms=["§ 51 Abs. 1 MarkenG", "§ 53 Abs. 1 MarkenG", "§ 55 MarkenG"], abschnitt="Ziel des Mandanten"),
            mc("k150-4", "Die Vorratsmarke des Konkurrenten",
               "Ein Konkurrent hält seit sieben Jahren eine eingetragene Marke, die er nie benutzt hat. Die Mandantin will das Zeichen selbst verwenden. Welche AGL?",
               ["§ 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 Nr. 1 MarkenG",
                "§ 49 Abs. 1 S. 1 MarkenG (Verfall wegen Nichtbenutzung), Antrag nach § 53 Abs. 1 MarkenG",
                "§ 43 Abs. 1 MarkenG",
                "§ 25 Abs. 1 MarkenG"], 1,
               ["**§ 49 Abs. 1 S. 1 MarkenG.** Nach Ablauf der fünfjährigen Schonfrist ist die Marke auf Antrag jeder Person für verfallen zu erklären (§ 53 Abs. 2 MarkenG); Gebühr 100 € (Nr. 333 400 Anlage PatKostG).",
                "§ 43 Abs. 1 und § 25 MarkenG sind Einreden in fremden Verfahren, keine Angriffsmittel."],
               merke="Nichtbenutzung als Angriff: § 49 MarkenG; als Verteidigung: § 43 Abs. 1, § 25, § 53 Abs. 6 MarkenG.",
               level=1, concepts=["verfall", "benutzungsschonfrist"], norms=["§ 49 Abs. 1 MarkenG", "§ 53 MarkenG"], abschnitt="Ziel des Mandanten"),
            mc("k150-5", "Die bösgläubige Anmeldung",
               "Der frühere Vertriebspartner der Mandantin hat deren Produktnamen als Marke angemeldet, um ihr den Markteintritt zu versperren. Die Widerspruchsfrist läuft noch. Welche AGL trägt den Vorwurf der Bösgläubigkeit?",
               ["Widerspruch nach § 42 Abs. 2 MarkenG",
                "Nichtigkeitsantrag nach § 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 Nr. 14 MarkenG",
                "Erinnerung nach § 64 MarkenG",
                "Eintragungsbewilligungsklage nach § 44 MarkenG"], 1,
               ["**§ 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 Nr. 14 MarkenG.** Bösgläubigkeit ist ein absolutes Schutzhindernis. Die Widerspruchsgründe des § 42 Abs. 2 MarkenG sind abschließend (BPatG Engelbrecht).",
                "Parallel kann ein Widerspruch aus der Agentenmarke (§ 42 Abs. 2 Nr. 3, § 11 MarkenG) sinnvoll sein."],
               merke="Bösgläubigkeit nie im Widerspruch, immer § 50 Abs. 1 MarkenG mit § 53 MarkenG.",
               level=2, concepts=["boesglaeubigkeit", "agentenmarke"], norms=["§ 50 Abs. 1 MarkenG", "§ 8 Abs. 2 MarkenG", "§ 42 Abs. 2 MarkenG"],
               cases=["bpatg_engelbrecht"], abschnitt="Ziel des Mandanten"),
            mc("k150-6", "Der Wettbewerber verkauft schon",
               "Ein Wettbewerber vertreibt Taschen unter einem Zeichen, das der eingetragenen Marke der Mandantin zum Verwechseln ähnlich ist. Sie will den Vertrieb stoppen. Welche AGL und welches Gericht?",
               ["Widerspruch beim DPMA",
                "§ 14 Abs. 5 S. 1 MarkenG i.V.m. § 14 Abs. 2 S. 1 Nr. 2 MarkenG vor dem LG (§ 140 Abs. 1 MarkenG)",
                "§ 14 Abs. 5 MarkenG vor dem Amtsgericht bei geringem Streitwert",
                "§ 51 Abs. 1 MarkenG vor dem BPatG"], 1,
               ["**§ 14 Abs. 5 S. 1 MarkenG vor dem LG.** Kennzeichenstreitsachen gehören ohne Rücksicht auf den Streitwert ausschließlich vor die Landgerichte (§ 140 Abs. 1 MarkenG).",
                "Widerspruch und Nichtigkeit beseitigen nur eine Eintragung, nicht die Benutzung."],
               merke="Benutzung verbieten: § 14 Abs. 5 MarkenG, LG ausschließlich (§ 140 Abs. 1 MarkenG).",
               level=1, concepts=["unterlassungsanspruch"], norms=["§ 14 Abs. 5 MarkenG", "§ 140 Abs. 1 MarkenG"], abschnitt="Ziel des Mandanten"),
            *fallkette("k150-7", "Wege gegen die Brückenmarke (nach NS II/2019)",
                       "Die dänische Betreiberin der Øresundbrücke (Unionsmarke „ØRESUNDSBRON“) will gegen die am Mittwoch, 15. Mai 2019, veröffentlichte deutsche Marke „oeresund-bruecke“ ihres früheren Ticketvertriebspartners K vorgehen. Sie hält K für „bösartig“ und will, dass er ihr Honorar zahlt.",
                       [frage("Ist gegen die Verwechslungsgefahr mit der Unionsmarke der Widerspruch die richtige AGL?", True,
                              ["**Ja!** § 42 Abs. 1 MarkenG i.V.m. § 42 Abs. 2 Nr. 1 MarkenG, § 9 Abs. 1 Nr. 2 MarkenG; eingetragene Unionsmarken stehen deutschen Marken gleich (§ 119 Nr. 1 MarkenG). Die Frist läuft drei Monate ab Veröffentlichung."],
                              merke="Unionsmarke als Widerspruchsmarke: § 42 Abs. 2 Nr. 1 MarkenG, § 119 Nr. 1 MarkenG.",
                              norms=["§ 42 MarkenG", "§ 119 MarkenG"], concepts=["unionsmarke"]),
                        frage("Für den Vorwurf der Bösgläubigkeit: Welche AGL?", 2,
                              ["**§ 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 Nr. 14 MarkenG**, Antrag beim DPMA (§ 53 Abs. 1 MarkenG), unbefristet. Im Widerspruch ist Bösgläubigkeit kein Grund."],
                              optionen=["Widerspruch nach § 42 Abs. 2 Nr. 1 MarkenG", "Klage nach § 55 MarkenG", "Nichtigkeitsantrag nach § 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 Nr. 14 MarkenG", "Erinnerung nach § 64 MarkenG"],
                              merke="Bösgläubigkeit: § 50 Abs. 1, § 8 Abs. 2 Nr. 14, § 53 MarkenG – nur DPMA, keine Klage.",
                              norms=["§ 50 MarkenG", "§ 8 MarkenG", "§ 53 MarkenG"], concepts=["boesglaeubigkeit"]),
                        frage("Aus dem Vertriebsverhältnis: Kommt ein zusätzlicher Widerspruchsgrund in Betracht?", True,
                              ["**Ja!** Agentenmarke: § 42 Abs. 2 Nr. 3 MarkenG i.V.m. § 11 MarkenG. Ob K die „Marke“ der Betreiberin angemeldet hat und ob nachvertragliche Pflichten fortwirken, ist zu klären (Lösung NS II/2019: wohl (–), weil nur die Sachbezeichnung übereinstimmt)."],
                              merke="Agentenmarke: § 11 MarkenG – Widerspruch § 42 Abs. 2 Nr. 3, Unterlassung § 17 MarkenG.",
                              norms=["§ 11 MarkenG", "§ 42 MarkenG"], concepts=["agentenmarke"]),
                        frage("Muss K im Widerspruchsverfahren die Anwaltskosten der Betreiberin tragen, wenn er unterliegt?", False,
                              ["**Nein!** Grundsatz: Jeder Beteiligte trägt seine Kosten selbst (§ 63 Abs. 1 S. 3 MarkenG). Eine Auferlegung setzt Billigkeitsgründe voraus (§ 63 Abs. 1 S. 1 MarkenG); Unterliegen allein genügt nicht."],
                              merke="DPMA-Kosten: § 63 Abs. 1 S. 1 (Billigkeit), S. 3 (Grundsatz) MarkenG.",
                              norms=["§ 63 MarkenG"], concepts=["kostenentscheidung"]),
                        ], abschnitt=K, level=2, cases=["bpatg_oeresundbruecke"]),
        ]),
        # ==============================================================
        dict(id="k15a", titel="§ 42 MarkenG: Widerspruch", einheiten=[
            intro("k15a-0", "Prüfungsschema",
                  "**AGL:** § 42 Abs. 1 S. 1 MarkenG i.V.m. § 42 Abs. 2 Nr. 1–5 MarkenG; Rechtsfolge § 43 Abs. 2 MarkenG\n\n"
                  "**0 · Wirksamkeit**\n"
                  "**V0 Widerspruchsgebühr** – 250 € für ein Widerspruchskennzeichen (Nr. 331 600 Anlage PatKostG), 50 € für jedes weitere (Nr. 331 610 Anlage PatKostG); fällig mit Erhebung (§ 3 Abs. 1 S. 1 PatKostG), zu zahlen innerhalb der Widerspruchsfrist (§ 64a MarkenG i.V.m. § 6 Abs. 1 S. 1 PatKostG), sonst gilt der Widerspruch als nicht erhoben (§ 6 Abs. 2 PatKostG); Zahlungstag § 2 PatKostZV; bei Unterzahlung Zuordnung klären (BPatG Silberweide)\n\n"
                  "**A · Zulässigkeit**\n"
                  "**V1 Statthaftigkeit** – § 42 Abs. 1 S. 1 MarkenG: eingetragene und nach § 41 Abs. 2 MarkenG veröffentlichte Marke; gegen IR-Marken Widerspruch gegen die Schutzgewährung (§ 114 Abs. 1, 3 MarkenG); schon ab Eintragung möglich\n"
                  "**V2 Beteiligten- und Prozessfähigkeit** – Markenrechtsfähigkeit § 7 MarkenG; § 50 ZPO, § 51 ZPO entsprechend; juristische Personen handeln durch Organe\n"
                  "**V3 Vertretung** – ohne Wohnsitz, Sitz oder Niederlassung im Inland nur mit Inlandsvertreter (§ 96 Abs. 1 MarkenG); Vollmacht § 15 DPMAV\n"
                  "**V4 Widerspruchsberechtigung** – Inhaber einer Marke oder geschäftlichen Bezeichnung mit älterem Zeitrang (§ 42 Abs. 1 S. 1 MarkenG, § 6 MarkenG), Berechtigte aus g.U./g.g.A. (§ 42 Abs. 1 S. 2 MarkenG); Unionsmarke § 119 Nr. 1 MarkenG; IR-Marke § 112 Abs. 1 MarkenG; Vermutung für den Registerinhaber § 28 Abs. 1 MarkenG; Rechtsnachfolger erst ab Eingang des Umschreibungsantrags (§ 28 Abs. 2 S. 1 MarkenG)\n"
                  "**V5 Frist** – drei Monate nach dem Tag der Veröffentlichung (§ 42 Abs. 1 S. 1 MarkenG) · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB (Feiertag am Erklärungsort); IR-Marke: Beginn am ersten Tag des Folgemonats (§ 114 Abs. 2 MarkenG, dann § 187 Abs. 2 BGB); keine Wiedereinsetzung (§ 91 Abs. 1 S. 2 MarkenG); Altanmeldungen § 158 Abs. 2, 3 MarkenG\n"
                  "**V6 Form, Inhalt** – ein Widerspruch je Kennzeichen, bei demselben Inhaber nur ein Widerspruch (§ 29 Abs. 1 MarkenV, § 42 Abs. 3 MarkenG); Formblatt (§ 29 Abs. 2 MarkenV, Soll); Identität von angegriffener Marke, Widerspruchskennzeichen und Widersprechendem (§ 30 Abs. 1 MarkenV), Soll-Angaben einschließlich Umfang (§ 30 Abs. 2 Nr. 9, 10 MarkenV)\n\n"
                  "**B · Begründetheit**\n"
                  "**V7 Widerspruchsgrund** – abschließend § 42 Abs. 2 MarkenG: Nr. 1 ältere Marke § 9 MarkenG · Nr. 2 notorische Marke § 10 MarkenG · Nr. 3 Agentenmarke § 11 MarkenG · Nr. 4 Benutzungsmarke § 4 Nr. 2 MarkenG oder geschäftliche Bezeichnung § 5 MarkenG, jeweils i.V.m. § 12 MarkenG (bundesweite Untersagungsbefugnis) · Nr. 5 g.U./g.g.A. i.V.m. § 13 MarkenG\n"
                  "**V8 Benutzung nachgewiesen, falls die Einrede erhoben ist** – § 43 Abs. 1 MarkenG (Kapitel k15b)\n\n"
                  "**⇒ Rechtsfolge:** Löschung ganz oder teilweise (§ 43 Abs. 2 S. 1 MarkenG), Wirkung von Anfang an (§ 43 Abs. 4 MarkenG i.V.m. § 52 Abs. 2 MarkenG); sonst Zurückweisung (§ 43 Abs. 2 S. 2 MarkenG). Aussetzung weiterer Widersprüche § 43 Abs. 3 MarkenG, Einigungsfrist § 42 Abs. 4 MarkenG; Korrektiv: Eintragungsbewilligungsklage binnen sechs Monaten (§ 44 MarkenG).\n\n"
                  "**Klausurfallen:** Gebühr vor der Zulässigkeit prüfen. Bösgläubigkeit und absolute Schutzhindernisse sind keine Widerspruchsgründe. Das Unternehmenskennzeichen eines regionalen Betriebs trägt keinen Widerspruch (§ 12 MarkenG). Feiertag am DPMA-Sitz (München, Jena, Berlin) prüfen.\n\n"
                  "**In den Klausuren:** NS II/2019 (Unionsmarke, Agentenmarke, Unternehmenskennzeichen; Fristende nach Mariä Himmelfahrt), NS III/2019 (wie viele Widersprüche nach dem MaMoG, Gebühr), NS II/2018 (Fristende Samstag), NS III/2021 (Telefax und SEPA-Mandat am letzten Tag), NS III/2020 (Rechtsnachfolge in die Widerspruchsmarke), NS III/2022 (Inlandsvertreter, zwei Widersprüche), NS I/2025 (Zuordnung der Gebühr), NS II/2025 (regionales Unternehmenskennzeichen).",
                  concepts=["widerspruch", "inlandsvertreter", "zahlungstag", "fristberechnung"],
                  norms=["§ 42 MarkenG", "§ 43 MarkenG", "§ 41 MarkenG", "§ 28 MarkenG", "§ 96 MarkenG", "§ 114 MarkenG", "§ 119 MarkenG", "§ 64a MarkenG", "§ 6 PatKostG", "Anlage PatKostG"],
                  abschnitt="Normenkette"),
            intro("k15a-1", "Definitionen",
                  "**Widerspruchskennzeichen:** jede Marke, geschäftliche Bezeichnung, geschützte Ursprungsbezeichnung oder geografische Angabe, wegen der Widerspruch erhoben wird (Legaldefinition § 29 Abs. 1 S. 1 MarkenV).\n"
                  "**Älterer Zeitrang:** bei angemeldeten oder eingetragenen Marken der Anmelde- oder Prioritätstag (§ 6 Abs. 2 MarkenG), bei Benutzungsmarken, notorischen Marken und geschäftlichen Bezeichnungen der Zeitpunkt des Rechtserwerbs (§ 6 Abs. 3 MarkenG).\n"
                  "**Unternehmenskennzeichen:** Zeichen, die im geschäftlichen Verkehr als Name, als Firma oder als besondere Bezeichnung eines Geschäftsbetriebs oder eines Unternehmens benutzt werden (Legaldefinition § 5 Abs. 2 S. 1 MarkenG).\n"
                  "**Bundesweite Untersagungsbefugnis:** Das nicht eingetragene Recht muss seinen Inhaber berechtigen, die Benutzung der jüngeren Marke im gesamten Gebiet der Bundesrepublik zu untersagen (§ 12 MarkenG); fehlt bei regional tätigen Unternehmen (BPatG Engelbrecht).\n"
                  "**Agent oder Vertreter:** wer aufgrund eines Vertragsverhältnisses (Vertrieb, Handelsvertretung) die geschäftlichen Interessen des Markeninhabers wahrzunehmen hat (§ 11 MarkenG, weite Auslegung in der Rechtsprechung).\n"
                  "**Notorisch bekannte Marke:** Marke, die im Sinne des Art. 6bis PVÜ im Inland allgemein bekannt ist, auch ohne Eintragung (§ 4 Nr. 3 MarkenG).\n"
                  "**Inlandsvertreter:** Rechts- oder Patentanwalt, den bestellen muss, wer im Inland weder Wohnsitz, Sitz noch Niederlassung hat (§ 96 Abs. 1 MarkenG); maßgeblich ist der Ort, nicht die Staatsangehörigkeit.\n"
                  "**Teilwiderspruch:** Widerspruch nur gegen einen Teil der Waren und Dienstleistungen der angegriffenen Marke (§ 30 Abs. 2 Nr. 10 MarkenV); Folge ist die Teillöschung (§ 43 Abs. 2 S. 1 MarkenG).",
                  concepts=["widerspruch", "unternehmenskennzeichen", "agentenmarke", "notorische_bekanntheit", "prioritaet"],
                  norms=["§ 5 MarkenG", "§ 6 MarkenG", "§ 11 MarkenG", "§ 12 MarkenG", "§ 4 MarkenG"],
                  cases=["bpatg_engelbrecht"], abschnitt="Definitionen"),
            mc("k15a-2", "Gebühr und Folge der Nichtzahlung",
               "Welche Normenkette regelt Höhe, Zahlungsfrist und Folge der Nichtzahlung der Widerspruchsgebühr?",
               ["Nr. 331 600, 331 610 Anlage PatKostG · § 6 Abs. 1 S. 1 PatKostG · § 6 Abs. 2 PatKostG (gilt als nicht erhoben)",
                "Nr. 333 300 Anlage PatKostG · § 6 Abs. 1 S. 2 PatKostG · Unzulässigkeit",
                "Nr. 331 600 Anlage PatKostG · § 6 Abs. 1 S. 2 PatKostG (drei Monate ab Fälligkeit) · § 6 Abs. 2 PatKostG",
                "§ 42 Abs. 1 MarkenG · § 91 MarkenG (Wiedereinsetzung möglich)"], 0,
               ["**Nr. 331 600, 331 610 · § 6 Abs. 1 S. 1 · § 6 Abs. 2 PatKostG.** Weil für den Widerspruch eine gesetzliche Frist gilt, ist die Gebühr innerhalb dieser Frist zu zahlen (§ 6 Abs. 1 S. 1 PatKostG), nicht binnen drei Monaten ab Fälligkeit.",
                "Folge: Der Widerspruch gilt als nicht erhoben (§ 6 Abs. 2 PatKostG); Wiedereinsetzung ist ausgeschlossen (§ 91 Abs. 1 S. 2 MarkenG)."],
               merke="Widerspruchsgebühr: Nr. 331 600/331 610 · § 6 Abs. 1 S. 1 PatKostG · § 6 Abs. 2 PatKostG · § 91 Abs. 1 S. 2 MarkenG.",
               level=1, concepts=["zahlungstag", "widerspruch"], norms=["§ 6 PatKostG", "Anlage PatKostG", "§ 91 Abs. 1 MarkenG"],
               step="step:schema_zulaessigkeit_widerspruch.1", abschnitt=N),
            fall("k15a-3", "Fristende am Samstag (NS II/2018)",
                 "Die Eintragung der Marke „Fassbrause“ wird am 20. Oktober 2017 veröffentlicht. Der Widerspruch geht am Montag, 22. Januar 2018, ein; der 20. Januar 2018 war ein Samstag.",
                 "Ist der Widerspruch rechtzeitig?", True,
                 ["**Ja!** Frist: drei Monate (§ 42 Abs. 1 S. 1 MarkenG). Der Veröffentlichungstag zählt nicht (§ 187 Abs. 1 BGB); Ende mit Ablauf des 20. Januar 2018 (§ 188 Abs. 2 BGB). Fällt das Ende auf einen Samstag, tritt der nächste Werktag an seine Stelle (§ 193 BGB): Montag, 22. Januar 2018.",
                  "Die Gebühr muss bis zu diesem Tag gezahlt sein."],
                 merke="Frist § 42 Abs. 1 S. 1 MarkenG · Berechnung § 187 Abs. 1, § 188 Abs. 2 BGB · Verschiebung § 193 BGB.",
                 level=1, concepts=["fristberechnung"], norms=["§ 42 Abs. 1 MarkenG"], step="step:schema_zulaessigkeit_widerspruch.6", abschnitt=N),
            fall("k15a-4", "250 Euro für zwei Kennzeichen (NS I/2025)",
                 "B erhebt einen Widerspruch aus seiner Wortmarke „INTREDA“ und seinem Unternehmenskennzeichen „INTREDA“, zahlt aber nur 250 €. Nach Fristablauf erklärt er, der Widerspruch solle „aus der Wortmarke“ gelten.",
                 "Gilt der Widerspruch insgesamt als nicht erhoben?", False,
                 ["**Nein!** 250 € decken die Gebühr für ein Widerspruchskennzeichen (Nr. 331 600 Anlage PatKostG). Bleibt offen, wofür gezahlt ist, muss das DPMA Gelegenheit zur Klarstellung geben; sie ist auch nach Fristablauf möglich, weil sie nur eine fristgerechte Zahlung zuordnet (BPatG Silberweide).",
                  "Nur für das Unternehmenskennzeichen gilt der Widerspruch als nicht erhoben (§ 6 Abs. 2 PatKostG)."],
                 merke="Unterzahlung bei mehreren Kennzeichen: Zuordnung klären, nicht alles verwerfen.",
                 level=2, concepts=["zahlungstag", "widerspruch"], norms=["§ 42 Abs. 3 MarkenG", "§ 6 PatKostG"], cases=["bpatg_silberweide"],
                 step="step:schema_zulaessigkeit_widerspruch.1", abschnitt=N),
            fall("k15a-5", "Die Erwerberin der Widerspruchsmarke",
                 "Die G AG erwirbt die Widerspruchsmarke durch Vertrag und erhebt im eigenen Namen Widerspruch. Einen Antrag auf Umschreibung hat beim DPMA bisher niemand gestellt; im Register steht noch die Veräußerin.",
                 "Kann die G AG die Rechte aus der Marke im Widerspruchsverfahren schon jetzt geltend machen?", False,
                 ["**Nein!** Der Rechtsnachfolger kann im Verfahren vor dem DPMA den Anspruch aus der Marke erst ab dem Zeitpunkt geltend machen, in dem dem DPMA der Antrag auf Eintragung des Rechtsübergangs zugegangen ist (§ 28 Abs. 2 S. 1 MarkenG).",
                  "Sicherer Weg: Umschreibungsantrag spätestens mit dem Widerspruch in der Frist stellen oder im Namen der eingetragenen Inhaberin widersprechen (§ 28 Abs. 1 MarkenG)."],
                 merke="Rechtsnachfolge: § 28 Abs. 1 MarkenG (Vermutung), § 28 Abs. 2 S. 1 MarkenG (ab Umschreibungsantrag), § 27 MarkenG (Übertragung).",
                 level=2, concepts=["aktivlegitimation", "widerspruch"], norms=["§ 28 Abs. 2 MarkenG", "§ 27 MarkenG"], step="step:schema_zulaessigkeit_widerspruch.4", abschnitt=N),
            fall("k15a-6", "Nur gegen die Bekleidung",
                 "Die jüngere Marke ist für Bekleidung (Klasse 25) und Bürobedarf (Klasse 16) eingetragen. Die Widersprechende wendet sich nur gegen die Waren der Klasse 25 und zahlt 250 €.",
                 "Ist ein auf Klasse 25 beschränkter Widerspruch zulässig?", True,
                 ["**Ja!** Der Widerspruch kann sich gegen einen Teil der Waren richten; das Verzeichnis der angegriffenen Waren ist Soll-Angabe (§ 30 Abs. 2 Nr. 10 MarkenV). Ist er begründet, wird die Eintragung nur teilweise gelöscht (§ 43 Abs. 2 S. 1 MarkenG). Die Gebühr hängt von der Zahl der Widerspruchskennzeichen ab, nicht vom Umfang."],
                 merke="Teilwiderspruch: § 30 Abs. 2 Nr. 10 MarkenV · Teillöschung § 43 Abs. 2 S. 1 MarkenG.",
                 level=1, concepts=["widerspruch"], norms=["§ 43 Abs. 2 MarkenG"], step="step:schema_zulaessigkeit_widerspruch.5", abschnitt=N),
            fall("k15a-7", "Widerspruch gegen eine IR-Marke",
                 "Die Schutzerstreckung einer IR-Marke auf Deutschland ist im WIPO-Veröffentlichungsblatt mit dem Ausgabemonat März 2024 veröffentlicht. Die deutsche Markeninhaberin erhebt am 20. Juni 2024 Widerspruch.",
                 "Ist der Widerspruch rechtzeitig?", True,
                 ["**Ja!** Bei IR-Marken beginnt die Widerspruchsfrist am ersten Tag des Monats, der dem Ausgabemonat folgt (§ 114 Abs. 2 MarkenG), hier am 1. April 2024. Dieser Tag zählt mit (§ 187 Abs. 2 BGB); die Frist endet mit Ablauf des 30. Juni 2024 (§ 188 Abs. 2 BGB).",
                  "An die Stelle der Löschung tritt die Schutzverweigerung (§ 114 Abs. 3 MarkenG)."],
                 merke="IR-Marke: § 114 Abs. 2 MarkenG · § 187 Abs. 2, § 188 Abs. 2 BGB · Schutzverweigerung § 114 Abs. 3 MarkenG.",
                 level=3, concepts=["ir_schutzverweigerung", "fristberechnung"], norms=["§ 114 MarkenG", "§ 42 Abs. 1 MarkenG"], abschnitt=N),
            mc("k15a-8", "Die Stadtbäckerei (NS II/2025)",
               "Eine Bäckerei mit zwölf Filialen in zwei Städten und Internetauftritt widerspricht aus ihrem Unternehmenskennzeichen der Marke „Gold-Bärger“ für Backwaren. Woran scheitert der Widerspruch?",
               ["An der fehlenden Eintragung des Kennzeichens",
                "An der fehlenden bundesweiten Untersagungsbefugnis (§ 42 Abs. 2 Nr. 4 MarkenG i.V.m. § 12 MarkenG)",
                "An der Widerspruchsfrist, weil Unternehmenskennzeichen keine Frist kennen",
                "Am Fehlen der Branchennähe"], 1,
               ["**§ 12 MarkenG.** Ein Unternehmenskennzeichen trägt den Widerspruch nur, wenn es seinen Inhaber berechtigt, die Benutzung der jüngeren Marke im gesamten Bundesgebiet zu untersagen. Der Schutz reicht nur so weit wie der Tätigkeitsbereich; ein Internetauftritt macht eine regionale Bäckerei nicht bundesweit tätig (BPatG Engelbrecht)."],
               merke="§ 42 Abs. 2 Nr. 4 MarkenG → § 5 Abs. 2 MarkenG → § 12 MarkenG (gesamtes Bundesgebiet).",
               level=2, concepts=["unternehmenskennzeichen"], norms=["§ 42 Abs. 2 MarkenG", "§ 12 MarkenG", "§ 5 Abs. 2 MarkenG"], cases=["bpatg_engelbrecht"],
               step="step:schema_zulaessigkeit_widerspruch.4.4", abschnitt=N),
            *fallkette("k15a-9", "Die Brückenbetreiberin widerspricht (nach NS II/2019)",
                       "OK mit Sitz in Kopenhagen ist Inhaberin der Unionsmarke „ØRESUNDSBRON“ und führt die Firma „Øresundsbro Konsortiet“. Die deutsche Marke „oeresund-bruecke“ des K wurde am Mittwoch, 15. Mai 2019, veröffentlicht. Der 15. August ist in München (Sitz des DPMA) Feiertag, in Jena und Berlin nicht.",
                       [frage("V3: Kann OK den Widerspruch ohne Inlandsvertreter selbst erheben?", False,
                              ["**Nein!** Wer im Inland weder Wohnsitz, Sitz noch Niederlassung hat, kann am Verfahren vor dem DPMA nur mit einem Rechts- oder Patentanwalt als Vertreter teilnehmen (§ 96 Abs. 1 MarkenG). Vollmacht durch die vertretungsberechtigte Person (§ 15 DPMAV)."],
                              merke="Sitz im Ausland ⇒ Inlandsvertreter § 96 Abs. 1 MarkenG.",
                              norms=["§ 96 MarkenG"], concepts=["inlandsvertreter"], step="step:schema_zulaessigkeit_widerspruch.3"),
                        frage("V4: Ist OK aus der Unionsmarke widerspruchsberechtigt?", True,
                              ["**Ja!** Widerspruch erheben kann der Inhaber einer Marke mit älterem Zeitrang (§ 42 Abs. 1 S. 1 MarkenG); Unionsmarken stehen deutschen Marken gleich (§ 119 Nr. 1 MarkenG). Zeitrang vor dem Anmeldetag der Marke des K und Inhaberschaft im EUIPO-Register prüfen."],
                              merke="Widerspruchsberechtigung: § 42 Abs. 1 S. 1, § 6 Abs. 2, § 119 Nr. 1 MarkenG.",
                              norms=["§ 42 MarkenG", "§ 119 MarkenG"], concepts=["unionsmarke"], step="step:schema_zulaessigkeit_widerspruch.4.1"),
                        frage("V5: Wann endet die Widerspruchsfrist?", 2,
                              ["**Freitag, 16. August 2019 (nach der Lösung NS II/2019).** Fristende rechnerisch Do 15.08.2019 (§ 42 Abs. 1 S. 1 MarkenG, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB); Feiertag am Sitz München verschiebt auf den nächsten Werktag (§ 193 BGB).",
                               "Weil die Annahmestellen Jena und Berlin geöffnet sind, Eingang vorsorglich bis Mi 14.08.2019 notieren."],
                              optionen=["Mittwoch, 14. August 2019", "Donnerstag, 15. August 2019, ohne Ausnahme", "Freitag, 16. August 2019; vorsorglich Eingang bis 14. August 2019", "Montag, 19. August 2019"],
                              merke="Feiertag nur am Erklärungsort (§ 193 BGB); im Zweifel den früheren Tag notieren.",
                              norms=["§ 42 Abs. 1 MarkenG"], concepts=["fristberechnung"], step="step:schema_zulaessigkeit_widerspruch.6"),
                        frage("V0/V6: Wie viel kostet ein Widerspruch aus Unionsmarke und Unternehmenskennzeichen?", 1,
                              ["**300 €:** ein Widerspruch, weil beide Kennzeichen OK gehören (§ 42 Abs. 3 MarkenG, § 29 Abs. 1 S. 2 MarkenV); 250 € Grundbetrag (Nr. 331 600) plus 50 € für das weitere Kennzeichen (Nr. 331 610 Anlage PatKostG)."],
                              optionen=["250 €", "300 €", "500 € (zwei Widersprüche)", "400 €"],
                              merke="Mehrere Kennzeichen desselben Inhabers = ein Widerspruch, 250 € + 50 € je weiteres.",
                              norms=["§ 42 Abs. 3 MarkenG", "Anlage PatKostG"], concepts=["widerspruch"]),
                        frage("V7: Kann OK den Widerspruch zusätzlich auf die Bösgläubigkeit des K stützen?", False,
                              ["**Nein!** Die Widerspruchsgründe sind in § 42 Abs. 2 MarkenG abschließend aufgezählt; Bösgläubigkeit (§ 8 Abs. 2 Nr. 14 MarkenG) ist ein absolutes Schutzhindernis und nur im Nichtigkeitsverfahren geltend zu machen (§ 50 Abs. 1, § 53 MarkenG)."],
                              merke="§ 42 Abs. 2 MarkenG abschließend: nur ältere Rechte, keine absoluten Schutzhindernisse.",
                              norms=["§ 42 Abs. 2 MarkenG", "§ 50 MarkenG"], concepts=["boesglaeubigkeit"], cases=["bpatg_engelbrecht"]),
                        ], abschnitt=K, level=2, cases=["bpatg_oeresundbruecke"]),
        ]),
        # ==============================================================
        dict(id="k15b", titel="§ 43 MarkenG mit § 26 MarkenG: Einrede mangelnder Benutzung", einheiten=[
            intro("k15b-0", "Prüfungsschema",
                  "**AGL (Verteidigung):** § 43 Abs. 1 S. 1 MarkenG i.V.m. § 26 MarkenG; Unionsmarke § 119 Nr. 4 MarkenG i.V.m. Art. 18 UMV; IR-Marke § 116 Abs. 1 MarkenG\n\n"
                  "**A · Zulässigkeit der Einrede**\n"
                  "**V1 Widerspruch aus einer eingetragenen Marke** – § 43 Abs. 1 S. 1 MarkenG (nicht bei Widerspruch aus angemeldeter Marke oder geschäftlicher Bezeichnung)\n"
                  "**V2 Einrede erhoben** – durch den Inhaber der angegriffenen Marke, eindeutig (BGH Silver Horse/Power Horse), in jedem Verfahrensstadium, auch erstmals vor dem BPatG; durch Organ, Prokuristen (§ 49 Abs. 1 HGB) oder Bevollmächtigten\n"
                  "**V3 Schonfrist der Widerspruchsmarke abgelaufen** – am Anmelde- oder Prioritätstag der angegriffenen Marke seit mindestens fünf Jahren kein Widerspruch mehr möglich (§ 43 Abs. 1 S. 1 MarkenG; Widerspruchsverfahren: § 26 Abs. 5 MarkenG); Unionsmarke: Eintragungstag (Art. 18 Abs. 1 UMV, § 119 Nr. 4 MarkenG); IR-Marke: § 116 Abs. 1 MarkenG i.V.m. § 115 Abs. 2 MarkenG · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Zeitraum, keine Verschiebung nach § 193 BGB\n\n"
                  "**B · Begründetheit (Nachweis durch den Widersprechenden)**\n"
                  "**V4 Benutzungszeitraum** – fünf Jahre vor dem Anmelde- oder Prioritätstag der angegriffenen Marke (§ 43 Abs. 1 S. 1 MarkenG); Widerspruch vor dem 14.01.2019: § 43 Abs. 1 a.F. mit zwei Zeiträumen (§ 158 Abs. 5 MarkenG)\n"
                  "**V5 Ernsthafte Benutzung als Marke** – § 26 Abs. 1 MarkenG: für die eingetragenen Waren/DL, im Inland (Unionsmarke: in der Union), funktionsgemäß als Herkunftshinweis\n"
                  "**V6 Durch den Inhaber oder mit Zustimmung** – § 26 Abs. 2 MarkenG (Lizenznehmer, Konzern, Pächter)\n"
                  "**V7 Form** – eingetragene Form oder Abweichung ohne Veränderung des kennzeichnenden Charakters (§ 26 Abs. 3 MarkenG)\n"
                  "**V8 Hilfsweise berechtigte Gründe für die Nichtbenutzung** – § 26 Abs. 1 a.E. MarkenG\n"
                  "**V9 Nachweis** – § 43 Abs. 1 S. 1 MarkenG; auch durch eidesstattliche Versicherung (§ 43 Abs. 1 S. 2 MarkenG) mit Unterlagen (Rechnungen, Abbildungen, Kataloge)\n\n"
                  "**⇒ Rechtsfolge:** Berücksichtigt werden nur die Waren/DL, für die die Benutzung nachgewiesen ist (§ 43 Abs. 1 S. 3 MarkenG); ohne Nachweis Zurückweisung des Widerspruchs (§ 43 Abs. 2 S. 2 MarkenG).\n\n"
                  "**Klausurfallen:** Fassung 2026 verlangt „Nachweis“; ältere Lösungen und § 43 Abs. 1 a.F. sprechen von Glaubhaftmachung. Schweigen ist keine Einrede. Die Einrede gegen eine noch junge Widerspruchsmarke ist unzulässig.\n\n"
                  "**In den Klausuren:** NS III/2019 (Zeitraum nach dem MaMoG), NS III/2021 (ab wann die Einrede zulässig ist), NS III/2018 (Einrede erst vor dem BPatG, Wellenlinie), NS I/2022 (Prokurist, ®-Symbol, eidesstattliche Versicherung), NS II/2021 (Sweatshirt-Aufdruck), NS II/2023 (Hotelutensilien), NS II/2020 (Benutzung durch die Pächterin), NS I/2019 (nur Rotwein benutzt), NS I/2024 (junge Unionsmarke).",
                  concepts=["nichtbenutzungseinrede", "rechtserhaltende_benutzung", "benutzungsschonfrist", "benutzung_union", "ir_benutzungsschonfrist"],
                  norms=["§ 43 MarkenG", "§ 26 MarkenG", "§ 119 MarkenG", "§ 116 MarkenG", "§ 115 MarkenG", "§ 158 MarkenG"],
                  cases=["bgh_silver_horse"], abschnitt="Normenkette"),
            intro("k15b-1", "Definitionen",
                  "**Ernsthafte Benutzung:** tatsächliche Benutzung entsprechend der Hauptfunktion der Marke, um für die Waren oder Dienstleistungen einen Absatzmarkt zu erschließen oder zu sichern; rein symbolische Benutzung zur Rechtserhaltung genügt nicht (EuGH Ansul).\n"
                  "**Benutzung als Marke:** Verwendung des Zeichens als Hinweis auf die betriebliche Herkunft gerade der eingetragenen Waren oder Dienstleistungen; die bloße Firmen- oder Geschäftsbezeichnung genügt nicht (EuGH Céline).\n"
                  "**Benutzungsschonfrist:** Fünfjahreszeitraum ab dem Tag, ab dem kein Widerspruch mehr gegen die Marke möglich ist, bei Widerspruch ab Rechtskraft der Entscheidung oder Rücknahme (§ 26 Abs. 5 MarkenG, § 49 Abs. 1 S. 1 MarkenG).\n"
                  "**Benutzung in abweichender Form:** Abweichung von der Eintragung, die den kennzeichnenden Charakter der Marke nicht verändert (§ 26 Abs. 3 MarkenG); der Verkehr sieht in der benutzten Form noch dieselbe Marke.\n"
                  "**Benutzung mit Zustimmung:** Benutzung durch Dritte mit Zustimmung des Inhabers gilt als Benutzung durch den Inhaber (§ 26 Abs. 2 MarkenG); Zustimmung auch konkludent, etwa durch Verpachtung des Betriebs samt Bezeichnung.\n"
                  "**Benutzung der Unionsmarke:** ernsthafte Benutzung in der Union; die Grenzen der Mitgliedstaaten bleiben außer Betracht (Art. 18 Abs. 1 UMV, EuGH Leno Merken).\n"
                  "**Berechtigte Gründe:** Hindernisse, die vom Willen des Inhabers unabhängig sind und die Benutzung unmöglich oder unzumutbar machen (§ 26 Abs. 1 a.E. MarkenG, Rechtsprechung).",
                  concepts=["ernsthafte_benutzung", "abweichende_form", "benutzungsschonfrist", "benutzung_union"],
                  norms=["§ 26 MarkenG", "§ 49 MarkenG"], cases=["eugh_ansul", "eugh_celine", "eugh_leno_merken"], abschnitt="Definitionen"),
            mc("k15b-2", "Welcher Zeitraum? (NS III/2019)",
               "Die Widerspruchsmarke „NordSport“ ist seit Dezember 2006 eingetragen, die angegriffene Marke „sportnord“ am 4. November 2016 angemeldet. Für welchen Zeitraum ist nach § 43 Abs. 1 S. 1 MarkenG n.F. die Benutzung nachzuweisen?",
               ["4. November 2011 bis 3. November 2016",
                "fünf Jahre vor der Entscheidung über den Widerspruch",
                "fünf Jahre vor der Veröffentlichung der angegriffenen Marke und zusätzlich fünf Jahre vor der Entscheidung",
                "Dezember 2006 bis Dezember 2011"], 0,
               ["**4.11.2011 bis 3.11.2016.** Maßgeblich sind die letzten fünf Jahre vor dem Anmelde- oder Prioritätstag der angegriffenen Marke (§ 43 Abs. 1 S. 1 MarkenG), berechnet nach § 187 Abs. 1 BGB, § 188 Abs. 2 BGB.",
                "Die Doppelprüfung (Option 3) galt nach § 43 Abs. 1 a.F.; sie bleibt für vor dem 14.01.2019 erhobene Widersprüche anwendbar (§ 158 Abs. 5 MarkenG)."],
               merke="Zeitraum § 43 Abs. 1 S. 1 MarkenG: fünf Jahre vor Anmeldetag der jüngeren Marke; Altfälle § 158 Abs. 5 MarkenG.",
               level=2, concepts=["nichtbenutzungseinrede"], norms=["§ 43 Abs. 1 MarkenG", "§ 158 MarkenG"], cases=["bpatg_sportnord"],
               step="step:schema_benutzungszwang.2", abschnitt=N),
            fall("k15b-3", "Einrede erst vor dem BPatG (NS III/2018)",
                 "Die Markenstelle hat den Widerspruch aus „ROCA“ zurückgewiesen. Erst im Beschwerdeverfahren erhebt die Inhaberin von „villa rocca“ die Einrede der Nichtbenutzung. Die Widersprechende rügt Verspätung.",
                 "Ist die Einrede zu berücksichtigen?", True,
                 ["**Ja!** Die Einrede kann in jedem Verfahrensstadium erhoben werden, auch erstmals im Beschwerdeverfahren; eine Präklusion kennt § 43 Abs. 1 MarkenG nicht. Das BPatG ist Tatsacheninstanz und prüft den Benutzungsnachweis selbst; es kann allenfalls zurückverweisen (§ 70 Abs. 3 MarkenG)."],
                 merke="Einrede jederzeit, auch erstmals vor dem BPatG.",
                 level=2, concepts=["nichtbenutzungseinrede"], norms=["§ 43 Abs. 1 MarkenG", "§ 70 Abs. 3 MarkenG"], step="step:schema_widerspruch.2", abschnitt=N),
            fall("k15b-4", "Einrede gegen eine junge Unionsmarke (NS I/2024)",
                 "Die Unionswiderspruchsmarke wurde am 18. März 2016 eingetragen, die angegriffene deutsche Marke am 16. Januar 2019 angemeldet. Der Markeninhaber erhebt „vorsorglich“ die Einrede der Nichtbenutzung.",
                 "Ist die Einrede zulässig?", False,
                 ["**Nein!** Die Einrede setzt voraus, dass am Anmeldetag der angegriffenen Marke seit mindestens fünf Jahren kein Widerspruch mehr gegen die Widerspruchsmarke möglich war (§ 43 Abs. 1 S. 1 MarkenG). Bei der Unionsmarke tritt Art. 18 UMV an die Stelle des § 26 MarkenG (§ 119 Nr. 4 MarkenG); die Frist knüpft an die Eintragung an. Am 16.01.2019 war die Marke noch keine drei Jahre eingetragen."],
                 merke="Erst Schonfrist (V3), dann Benutzung (V4 ff.); junge Marke ⇒ Einrede unzulässig.",
                 level=2, concepts=["benutzung_union", "nichtbenutzungseinrede"], norms=["§ 43 Abs. 1 MarkenG", "§ 119 MarkenG"], step="step:schema_benutzungszwang.1", abschnitt=N),
            fall("k15b-5", "Die Pächterin benutzt (NS II/2020)",
                 "Die Sanders GmbH hat ihr Wellnessbad samt der Bezeichnung „Balidrom“ verpachtet. Benutzt hat die Marke nur die Pächterin. Gegen den Widerspruch aus „Balidrom“ wird die Nichtbenutzungseinrede erhoben.",
                 "Kann sich die Sanders GmbH auf die Benutzung durch die Pächterin berufen?", True,
                 ["**Ja!** Die Benutzung mit Zustimmung des Inhabers gilt als Benutzung durch den Inhaber (§ 26 Abs. 2 MarkenG). Wer einen Betrieb samt Bezeichnung verpachtet, stimmt der Benutzung konkludent zu. Zu prüfen bleibt, ob die Benutzung in den maßgeblichen Zeitraum fällt (§ 43 Abs. 1 MarkenG, ggf. a.F. über § 158 Abs. 5 MarkenG)."],
                 merke="Benutzung durch Dritte: § 26 Abs. 2 MarkenG (Zustimmung genügt, auch konkludent).",
                 level=1, concepts=["rechtserhaltende_benutzung"], norms=["§ 26 Abs. 2 MarkenG"], cases=["bpatg_liquidrom"],
                 step="step:schema_benutzungszwang.3.5", abschnitt=N),
            fall("k15b-6", "Die Wellenlinie unter ROCA (NS III/2018)",
                 "Die Unionswortmarke „ROCA“ wird auf Waschbecken nur zusammen mit einer schmückenden Wellenlinie benutzt. Die Gegnerin meint, die eingetragene Wortmarke sei nicht benutzt.",
                 "Ist die Benutzung rechtserhaltend?", True,
                 ["**Ja!** Als Benutzung gilt auch eine abweichende Form, die den kennzeichnenden Charakter nicht verändert (§ 26 Abs. 3 MarkenG; für Unionsmarken Art. 18 Abs. 1 UAbs. 2 lit. a UMV). Eine Wortmarke darf mit üblichen Gestaltungen und bildlichen Zutaten benutzt werden, solange das Wort als eigenständiges Kennzeichen erkennbar bleibt."],
                 merke="Abweichende Form: § 26 Abs. 3 MarkenG – Zutat schadet nicht, wenn der kennzeichnende Charakter bleibt.",
                 level=1, concepts=["abweichende_form"], norms=["§ 26 Abs. 3 MarkenG"], step="step:schema_benutzungszwang.3.6", abschnitt=N),
            fall("k15b-7", "Kugelschreiber im Hotelzimmer (NS II/2023)",
                 "Die Marke „Louis C. Jacob“ ist für Schreibwaren (Klasse 16) und Beherbergung (Klasse 43) eingetragen. Belegt sind Kugelschreiber und Schreibblöcke mit der Marke, die den Hotelgästen kostenlos im Zimmer ausliegen.",
                 "Ist die Marke für Schreibwaren rechtserhaltend benutzt?", False,
                 ["**Nein!** Ernsthaft ist nur eine Benutzung, die für die Waren einen Absatzmarkt erschließen oder sichern soll (EuGH Ansul). Gratisartikel im Hotelzimmer sind Hilfsmittel der Beherbergung; sie kennzeichnen die Dienstleistung, nicht eigene Schreibwaren. Für Klasse 43 ist die Benutzung dagegen belegt."],
                 merke="Werbe- und Gratisartikel ≠ Benutzung für diese Waren (§ 26 Abs. 1 MarkenG).",
                 level=2, concepts=["ernsthafte_benutzung"], norms=["§ 26 Abs. 1 MarkenG"], cases=["eugh_ansul"], step="step:schema_benutzungszwang.3.3", abschnitt=N),
            mc("k15b-8", "Nur Rotwein benutzt (NS I/2019)",
               "„JEAN LEON“ ist für „alkoholische Getränke (ausgenommen Biere)“ eingetragen; die Benutzung ist nach zulässiger Einrede nur für Rotwein nachgewiesen. Die jüngere Marke beansprucht Schaumwein. Wovon geht die Prüfung der Verwechslungsgefahr aus?",
               ["Von allen eingetragenen alkoholischen Getränken",
                "Nur von Rotwein (§ 43 Abs. 1 S. 3 MarkenG)",
                "Von gar keiner Ware; der Widerspruch ist zurückzuweisen",
                "Vom Oberbegriff „Wein“ insgesamt"], 1,
               ["**Nur Rotwein.** Bei der Entscheidung werden nur die Waren berücksichtigt, für die die Benutzung nachgewiesen ist (§ 43 Abs. 1 S. 3 MarkenG). Rotwein und Schaumwein bleiben ähnlich (gleiche Hersteller, Vertriebswege, Verwendung)."],
               merke="Teilbenutzung ⇒ Prüfung nur mit den benutzten Waren (§ 43 Abs. 1 S. 3 MarkenG).",
               level=2, concepts=["nichtbenutzungseinrede", "warenaehnlichkeit"], norms=["§ 43 Abs. 1 MarkenG"], step="step:schema_benutzungszwang.6", abschnitt=N),
            *fallkette("k15b-9", "SILVER HORSE gegen POWER HORSE (nach NS I/2022)",
                       "Die Inhaberin der IR-Marke „POWER HORSE“ (Energydrinks, Schutz für Deutschland) widerspricht der Marke „SILVER HORSE“. Der Prokurist der Inhaberin von „SILVER HORSE“, einer deutschen AG, erhebt schriftlich die Einrede der mangelnden Benutzung. Die Widersprechende legt eine eidesstattliche Versicherung ihres Finanzchefs über jährlich fünf Millionen verkaufte Dosen sowie Abbildungen der Dose mit „POWER HORSE®“ vor.",
                       [frage("V2: Kann der Prokurist die Einrede wirksam erheben?", True,
                              ["**Ja!** Die Prokura ermächtigt zu allen gerichtlichen und außergerichtlichen Geschäften, die der Betrieb eines Handelsgewerbes mit sich bringt (§ 49 Abs. 1 HGB). Vor DPMA und BPatG besteht kein Anwaltszwang (§ 81 Abs. 1 MarkenG). Die Einrede muss eindeutig erklärt sein (BGH Silver Horse/Power Horse)."],
                              merke="Einrede: eindeutig, durch Organ, Prokuristen oder Bevollmächtigten.",
                              norms=["§ 43 Abs. 1 MarkenG", "§ 81 MarkenG"], cases=["bgh_silver_horse"]),
                        frage("V3: Woran knüpft die Schonfrist bei einer IR-Widerspruchsmarke an?", 1,
                              ["**An den Abschluss des Schutzerstreckungsverfahrens** bzw. den Ablauf der Frist nach Art. 5 Abs. 2a PMMA (§ 116 Abs. 1 MarkenG i.V.m. § 115 Abs. 2 MarkenG), nicht an die Basismarke."],
                              optionen=["An die Eintragung der Basismarke im Ursprungsland", "An den Abschluss des Schutzerstreckungsverfahrens (§ 116 Abs. 1, § 115 Abs. 2 MarkenG)", "An den Tag der internationalen Registrierung", "An die Veröffentlichung der angegriffenen Marke"],
                              merke="IR-Marke: § 116 Abs. 1 MarkenG → § 115 Abs. 2 MarkenG statt „kein Widerspruch mehr möglich“.",
                              norms=["§ 116 MarkenG", "§ 115 MarkenG"], concepts=["ir_benutzungsschonfrist"]),
                        frage("V7: Schadet das ®-Symbol hinter dem Schriftzug der Benutzung in eingetragener Form?", False,
                              ["**Nein!** Das ®-Symbol weist nur auf die Registrierung hin und verändert nicht, welches Zeichen der Verkehr als Herkunftshinweis wahrnimmt. Es ist allenfalls eine unwesentliche Abweichung (§ 26 Abs. 3 MarkenG)."],
                              merke="®, TM, übliche Zusätze ⇒ keine Veränderung des kennzeichnenden Charakters.",
                              norms=["§ 26 Abs. 3 MarkenG"], concepts=["abweichende_form"]),
                        frage("V9: Ist eine eidesstattliche Versicherung ein zulässiges Nachweismittel?", True,
                              ["**Ja!** Der Nachweis kann auch durch eidesstattliche Versicherung erbracht werden (§ 43 Abs. 1 S. 2 MarkenG). Sie muss Art, Zeitraum, Umfang und Form der Benutzung konkret angeben; „insbesondere“-Formulierungen sind schwach und sollten durch Abbildungen und Rechnungen ergänzt werden."],
                              merke="Nachweis § 43 Abs. 1 S. 1, 2 MarkenG: eidesstattliche Versicherung + Unterlagen.",
                              norms=["§ 43 Abs. 1 MarkenG"], concepts=["glaubhaftmachung"]),
                        ], abschnitt=K, level=2, cases=["bpatg_silver_horse"]),
        ]),
        # ==============================================================
        dict(id="k15c", titel="§ 9 Abs. 1 Nr. 1–3 MarkenG: relative Schutzhindernisse", einheiten=[
            intro("k15c-0", "Prüfungsschema",
                  "**AGL:** § 42 Abs. 2 Nr. 1 MarkenG bzw. § 51 Abs. 1 MarkenG i.V.m. § 9 Abs. 1 Nr. 1, 2 oder 3 MarkenG\n\n"
                  "**V1 Ältere angemeldete oder eingetragene Marke** – § 9 Abs. 1 MarkenG, Zeitrang § 6 Abs. 2 MarkenG; Anmeldung nur, wenn sie eingetragen wird (§ 9 Abs. 2 MarkenG); Unionsmarke § 119 Nr. 1 MarkenG; IR-Marke § 112 Abs. 1 MarkenG\n\n"
                  "**Nr. 1 · Doppelidentität**\n"
                  "**V2 Zeichenidentität** und **V3 Waren-/DL-Identität** – § 9 Abs. 1 Nr. 1 MarkenG; keine Verwechslungsgefahr zu prüfen\n\n"
                  "**Nr. 2 · Verwechslungsgefahr**\n"
                  "**V2 Waren-/DL-Identität oder -Ähnlichkeit** – Registerlage; Klasseneinteilung unerheblich (§ 9 Abs. 3 MarkenG); nach Einrede nur benutzte Waren (§ 43 Abs. 1 S. 3 MarkenG)\n"
                  "**V3 Kennzeichnungskraft der älteren Marke** – originär (fünf Grade, BGH Culinaria), gesteigert durch Benutzung, geschwächt durch benutzte Drittmarken; maßgeblich auch am Anmeldetag der jüngeren Marke (§ 51 Abs. 4 S. 2 MarkenG)\n"
                  "**V4 Zeichenähnlichkeit** – Gesamteindruck; klanglich, schriftbildlich/bildlich, begrifflich; Ähnlichkeit in einer Richtung genügt; Prägung durch einen Bestandteil; selbständig kennzeichnende Stellung\n"
                  "**V5 Gesamtabwägung** – Wechselwirkung (EuGH Canon)\n"
                  "**V6 Art** – unmittelbare Verwechslungsgefahr; gedankliches Inverbindungbringen (§ 9 Abs. 1 Nr. 2 a.E. MarkenG: Serienzeichen, wirtschaftliche Verbindung)\n\n"
                  "**Nr. 3 · Bekanntheitsschutz**\n"
                  "**V2 Im Inland bekannte Marke** – Unionsmarke: Bekanntheit in der Union (§ 119 Nr. 1 MarkenG)\n"
                  "**V3 Identität oder Ähnlichkeit, gedankliche Verknüpfung** – keine Waren-/DL-Ähnlichkeit erforderlich\n"
                  "**V4 Ausnutzung oder Beeinträchtigung** der Unterscheidungskraft oder Wertschätzung\n"
                  "**V5 Ohne rechtfertigenden Grund in unlauterer Weise**\n\n"
                  "**⇒ Rechtsfolge:** Löschung im Widerspruchsverfahren (§ 43 Abs. 2 S. 1 MarkenG) bzw. Nichtigkeit (§ 51 Abs. 1 MarkenG), ganz oder teilweise.\n\n"
                  "**Klausurfallen:** Im Register- und Widerspruchsverfahren entscheidet die Registerlage, nicht das tatsächliche Sortiment. Übereinstimmungen in schutzunfähigen Bestandteilen begründen keine Verwechslungsgefahr. Kauf auf Sicht verdrängt den Klang nur bei reinen Sichtkäufen. Schwächung durch Drittmarken nur bei nachgewiesener Benutzung.\n\n"
                  "**In den Klausuren:** NS III/2019 (Silbenrotation sportnord/NordSport), NS III/2021 (Serienzeichen VITA), NS I/2022 (SILVER HORSE/POWER HORSE), NS II/2019 (geografisch-beschreibender Bestandteil, Bekanntheit in der Union), NS I/2019 (Vor- und Nachname, Rotwein/Crémant), NS III/2020 (gelbfunk/Gelbe Seiten), NS II/2021 (Black Panther/PANTHER), NS II/2023 (LOUIS HOTEL/Louis C. Jacob), NS II/2018 (Fassbrause).",
                  concepts=["relative_schutzhindernisse", "verwechslungsgefahr", "warenaehnlichkeit", "kennzeichnungskraft", "zeichenaehnlichkeit", "wechselwirkung", "relative_schutzhindernis_bekannt"],
                  norms=["§ 9 MarkenG", "§ 42 Abs. 2 MarkenG", "§ 51 MarkenG", "§ 119 MarkenG"], cases=["eugh_canon", "bgh_culinaria"], abschnitt="Normenkette"),
            intro("k15c-1", "Definitionen",
                  "**Verwechslungsgefahr:** Gefahr, dass das Publikum glauben könnte, die betreffenden Waren oder Dienstleistungen stammten aus demselben oder aus wirtschaftlich miteinander verbundenen Unternehmen; umfassend unter Berücksichtigung aller Umstände zu beurteilen (EuGH Canon, EuGH SABEL/Puma).\n"
                  "**Wechselwirkung:** Ein geringerer Grad der Waren-/DL-Ähnlichkeit kann durch einen höheren Grad der Zeichenähnlichkeit oder eine erhöhte Kennzeichnungskraft ausgeglichen werden und umgekehrt (EuGH Canon).\n"
                  "**Waren-/DL-Ähnlichkeit:** zu berücksichtigen sind alle erheblichen Faktoren, insbesondere Art, Verwendungszweck, Nutzung und Eigenart als konkurrierende oder einander ergänzende Waren (EuGH Canon), ferner Herstellungsstätte und Vertriebswege (Rechtsprechung).\n"
                  "**Kennzeichnungskraft:** Eignung der Marke, die Waren als von einem bestimmten Unternehmen stammend zu kennzeichnen; zu bestimmen nach Eigenart, Marktanteil, Intensität, Dauer und Werbeaufwand (EuGH Lloyd). Fünf Grade: sehr gering, gering, durchschnittlich, erhöht, sehr hoch (BGH Culinaria).\n"
                  "**Durchschnittsverbraucher:** durchschnittlich informiert, aufmerksam und verständig; er nimmt die Marken selten gleichzeitig wahr und verlässt sich auf sein unvollkommenes Erinnerungsbild (EuGH Lloyd).\n"
                  "**Prägung:** Ein Bestandteil prägt den Gesamteindruck, wenn die übrigen Bestandteile für den Verkehr weitgehend in den Hintergrund treten (BGH Culinaria).\n"
                  "**Selbständig kennzeichnende Stellung:** Die ältere Marke wird in ein jüngeres Kombinationszeichen übernommen und behält dort eine eigenständige Stellung, ohne den Gesamteindruck zu dominieren (EuGH THOMSON LIFE); Ausnahme, die besondere Umstände verlangt (BGH Culinaria).\n"
                  "**Serienzeichen:** Der Verkehr erkennt in einem übereinstimmenden, hinweiskräftigen Stammbestandteil den Hinweis auf eine Zeichenserie desselben Unternehmens; regelmäßig setzt das die Benutzung mehrerer Marken mit diesem Stamm voraus (Rechtsprechung).\n"
                  "**Bekannte Marke:** Marke, die einem bedeutenden Teil des Publikums bekannt ist, das von den erfassten Waren oder Dienstleistungen betroffen ist; feste Prozentsätze gibt es nicht (EuGH General Motors).\n"
                  "**Zeichenidentität:** Das Zeichen gibt ohne Änderung oder Hinzufügung alle Elemente der Marke wieder, oder die Abweichungen sind so geringfügig, dass sie dem Durchschnittsverbraucher entgehen können (st. Rspr. des EuGH).",
                  concepts=["verwechslungsgefahr", "wechselwirkung", "warenaehnlichkeit", "kennzeichnungskraft", "praegetheorie", "selbstaendig_kennzeichnende_stellung", "serienmarke", "bekannte_marke", "durchschnittsverbraucher", "doppelidentitaet"],
                  norms=["§ 9 Abs. 1 MarkenG"], cases=["eugh_canon", "eugh_sabel_puma", "eugh_lloyd", "bgh_culinaria", "eugh_thomson_life", "eugh_general_motors"],
                  abschnitt="Definitionen"),
            mc("k15c-2", "Klasse und Ähnlichkeit",
               "Welche Aussage zur Waren- und Dienstleistungsähnlichkeit trifft zu?",
               ["Waren derselben Nizza-Klasse sind stets ähnlich",
                "Waren verschiedener Klassen sind stets unähnlich",
                "Die Klasseneinteilung ist für sich allein unerheblich (§ 9 Abs. 3 MarkenG); maßgeblich sind Art, Zweck, Nutzung, Wettbewerbs- oder Ergänzungsverhältnis, Herkunft und Vertrieb",
                "Maßgeblich ist, welche Waren die Widersprechende tatsächlich herstellt, auch ohne Einrede"], 2,
               ["**§ 9 Abs. 3 MarkenG.** Waren sind nicht schon deshalb ähnlich oder unähnlich, weil sie in derselben oder in verschiedenen Klassen stehen. Entscheidend sind die Canon-Kriterien. Ohne Nichtbenutzungseinrede gilt die Registerlage."],
               merke="§ 9 Abs. 3 MarkenG: Klasse ist kein Kriterium; Canon-Faktoren + Registerlage.",
               level=1, concepts=["warenaehnlichkeit", "klassifizierung"], norms=["§ 9 Abs. 3 MarkenG"], cases=["eugh_canon"],
               step="step:schema_verwechslungsgefahr.2", abschnitt=N),
            fall("k15c-3", "Rotwein gegen Crémant (NS I/2019)",
                 "Die Unionsmarke „JEAN LEON“ ist für „alkoholische Getränke (ausgenommen Biere)“ eingetragen, die jüngere Marke „MICHEL LEON“ für Schaumweine. Die Widersprechende produziert nur spanischen Rotwein; eine Einrede ist nicht erhoben.",
                 "Liegt Warenidentität vor?", True,
                 ["**Ja!** Ohne Einrede entscheidet die Registerlage. Der Oberbegriff „alkoholische Getränke (ausgenommen Biere)“ umfasst Schaumweine; damit sind die Waren identisch. Was die Widersprechende tatsächlich herstellt und wo Crémant erzeugt werden darf, spielt keine Rolle."],
                 merke="Registerlage: Oberbegriff umfasst Unterbegriff ⇒ Identität.",
                 level=1, concepts=["warenaehnlichkeit"], norms=["§ 9 Abs. 1 MarkenG"], step="step:schema_verwechslungsgefahr.2", abschnitt=N),
            fall("k15c-4", "sportnord gegen NordSport (NS III/2019)",
                 "Die Wort-/Bildmarke „sportnord“ steht der älteren Wortmarke „NordSport“ für identische Sportbekleidung gegenüber. Die Inhaberin der jüngeren Marke meint, die vertauschte Reihenfolge der Silben unterscheide die Zeichen.",
                 "Besteht Verwechslungsgefahr?", True,
                 ["**Ja!** „NordSport“ ist nur ein vager Hinweis und durchschnittlich kennzeichnungskräftig. Die Bildelemente treten zurück, weil sich der Verkehr am Wort orientiert. Klanglich gleiche Silben und Vokalfolge, nur vertauscht: Der Verkehr behält die Bestandteile, nicht ihre Reihenfolge (BPatG sportnord/NordSport). Bei Warenidentität genügt das."],
                 merke="Silbenrotation + Warenidentität ⇒ klangliche Verwechslungsgefahr.",
                 level=2, concepts=["zeichenaehnlichkeit", "verwechslungsgefahr"], norms=["§ 9 Abs. 1 MarkenG"], cases=["bpatg_sportnord"],
                 step="step:schema_verwechslungsgefahr.4.3", abschnitt=N),
            fall("k15c-5", "Kauf auf Sicht (NS I/2022)",
                 "Die Inhaberin von „SILVER HORSE“ trägt vor, Energydrinks würden im Supermarkt nur auf Sicht gekauft; auf die klangliche Ähnlichkeit mit „POWER HORSE“ komme es nicht an.",
                 "Ist die klangliche Ähnlichkeit außer Betracht zu lassen?", False,
                 ["**Nein!** Ähnlichkeit in einer Wahrnehmungsrichtung genügt. Der Klang tritt nur bei Waren zurück, die regelmäßig nur auf Sicht gekauft werden. Energydrinks werden auch mündlich empfohlen, beworben und an Kiosk oder Theke bestellt (BPatG SILVER HORSE/POWER HORSE)."],
                 merke="Eine Wahrnehmungsrichtung genügt; Sichtkauf nur bei reinem Sichtkauf.",
                 level=2, concepts=["zeichenaehnlichkeit"], norms=["§ 9 Abs. 1 MarkenG"], cases=["bpatg_silver_horse"], step="step:schema_verwechslungsgefahr.4.3", abschnitt=N),
            fall("k15c-6", "gelbfunk gegen Gelbe Seiten (NS III/2020)",
                 "Die kraft Verkehrsdurchsetzung eingetragene Marke „Gelbe Seiten“ steht der jüngeren Wortmarke „gelbfunk“ gegenüber. Die Widersprechende verweist auf Dutzende eigene Marken mit „Gelb“.",
                 "Besteht Verwechslungsgefahr?", False,
                 ["**Nein!** Die Zeichen stimmen nur im beschreibenden Element „gelb“ überein; Übereinstimmungen in schutzunfähigen Bestandteilen begründen keine Verwechslungsgefahr. Der Schutz einer durchgesetzten Marke beschränkt sich auf die Gesamtbezeichnung. Ein Serienzeichen scheitert, weil der beschreibende Farbbegriff kein hinweiskräftiger Stamm ist."],
                 merke="Schutzunfähiger Bestandteil prägt nicht und trägt keine Serie.",
                 level=2, concepts=["praegetheorie", "serienmarke", "verkehrsdurchsetzung"], norms=["§ 9 Abs. 1 MarkenG"], step="step:schema_verwechslungsgefahr.4.2", abschnitt=N),
            mc("k15c-7", "Was braucht Nr. 3 nicht?",
               "Welche Voraussetzung ist für den Bekanntheitsschutz nach § 9 Abs. 1 Nr. 3 MarkenG nicht erforderlich?",
               ["Bekanntheit der älteren Marke im Inland",
                "Ähnlichkeit der Waren oder Dienstleistungen",
                "Ausnutzung oder Beeinträchtigung der Unterscheidungskraft oder Wertschätzung",
                "Fehlen eines rechtfertigenden Grundes, Unlauterkeit"], 1,
               ["**Waren-/DL-Ähnlichkeit.** § 9 Abs. 1 Nr. 3 MarkenG schützt die bekannte Marke über den Ähnlichkeitsbereich hinaus; verlangt sind Bekanntheit, Zeichenähnlichkeit mit gedanklicher Verknüpfung, Ausnutzung oder Beeinträchtigung sowie Unlauterkeit ohne rechtfertigenden Grund. Bei Unionsmarken tritt die Bekanntheit in der Union an die Stelle (§ 119 Nr. 1 MarkenG)."],
               merke="Nr. 3: bekannt · ähnlich + Verknüpfung · Ausnutzung/Beeinträchtigung · unlauter – Waren egal.",
               level=1, concepts=["relative_schutzhindernis_bekannt", "bekanntheit_union", "gedankliche_verknuepfung"], norms=["§ 9 Abs. 1 MarkenG", "§ 119 MarkenG"],
               cases=["eugh_general_motors"], step="step:schema_widerspruch.3.3", abschnitt=N),
            *fallkette("k15c-8", "vita+lebenskraft gegen VITA (nach NS III/2021)",
                       "Die Unionsmarke „VITA“ ist für Dentalkeramik eingetragen; in den Fachkreisen der Zahnärzte und Zahntechniker kennen sie 96 %. Die Widersprechende benutzt eine Serie VITAFOL, VITAPAN, VITA In-Ceram und führt „VITA“ als Firmenschlagwort. Die jüngere Marke „vita+lebenskraft“ ist für identische Dentalwaren eingetragen.",
                       [frage("V2: Auf wessen Verständnis kommt es an?", 0,
                              ["**Auf die Fachkreise.** Maßgeblich sind die Verkehrskreise, an die sich die Waren richten; Dentalkeramik kaufen Zahnärzte und Zahntechniker mit erhöhter Aufmerksamkeit."],
                              optionen=["Zahnärzte und Zahntechniker als Fachkreise", "Die Allgemeinheit der Verbraucher", "Nur Patienten", "Das Prüferkollegium des DPMA"],
                              merke="Verkehrskreise nach den Waren bestimmen; Fachpublikum = höhere Aufmerksamkeit.",
                              concepts=["durchschnittsverbraucher"], step="step:schema_verwechslungsgefahr.1"),
                        frage("V3: Ist die Kennzeichnungskraft von „VITA“ gesteigert?", True,
                              ["**Ja!** Ein Bekanntheitsgrad von 96 % in den Fachkreisen steigert die von Haus aus wegen des Anklangs an „vital“ eher geringe Kennzeichnungskraft (EuGH Lloyd: Marktanteil, Intensität, Dauer)."],
                              merke="Kennzeichnungskraft: originär + Benutzung (Bekanntheitsgrad).",
                              concepts=["kennzeichnungskraft"], step="step:schema_verwechslungsgefahr.3"),
                        frage("V4: Prägt „vita“ den Gesamteindruck von „vita+lebenskraft“?", False,
                              ["**Nein!** Das BPatG sieht in „vita+lebenskraft“ einen Gesamtbegriff; „lebenskraft“ tritt nicht zurück. Eine unmittelbare Verwechslungsgefahr scheidet aus."],
                              merke="Prägung nur, wenn die übrigen Bestandteile weitgehend zurücktreten.",
                              concepts=["praegetheorie"], step="step:schema_verwechslungsgefahr.4.2"),
                        frage("V6: Besteht Verwechslungsgefahr durch gedankliches Inverbindungbringen?", True,
                              ["**Ja!** Die Fachkreise kennen „VITA“ als Stamm einer benutzten Zeichenserie und als Firmenschlagwort und ordnen ein weiteres „vita“-Zeichen für Dentalwaren der Widersprechenden zu (§ 9 Abs. 1 Nr. 2 a.E. MarkenG; BPatG vita+lebenskraft/VITA). Folge: Teillöschung für die Dentalwaren."],
                              merke="Serienzeichen: benutzte Serie + hinweiskräftiger Stamm + gleiche Funktion im jüngeren Zeichen.",
                              concepts=["serienmarke", "verwechslungsgefahr_weiterer_sinn"], step="step:schema_verwechslungsgefahr.6"),
                        ], abschnitt=K, level=2, norms=["§ 9 Abs. 1 MarkenG"], cases=["bpatg_vita_lebenskraft"]),
        ]),
        # ==============================================================
        dict(id="k15d", titel="§§ 50, 8, 53 MarkenG: Nichtigkeit wegen absoluter Schutzhindernisse", einheiten=[
            intro("k15d-0", "Prüfungsschema",
                  "**AGL:** § 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 MarkenG (bzw. § 3, § 7 MarkenG); Verfahren § 53 MarkenG\n\n"
                  "**0 · Wirksamkeit**\n"
                  "**V0 Gebühr** – 400 € (Nr. 333 300 Anlage PatKostG); fällig mit Antrag (§ 3 Abs. 1 PatKostG), Zahlung binnen drei Monaten ab Fälligkeit (§ 6 Abs. 1 S. 2 PatKostG), sonst gilt der Antrag als zurückgenommen (§ 6 Abs. 2 PatKostG)\n\n"
                  "**A · Zulässigkeit**\n"
                  "**V1 Statthaftigkeit** – Antrag beim DPMA (§ 53 Abs. 1 S. 1 MarkenG); eine Klage wegen absoluter Schutzhindernisse gibt es nicht (§ 55 Abs. 1 MarkenG nur Verfall und ältere Rechte); IR-Marke: Schutzentziehung (§ 115 Abs. 1 MarkenG)\n"
                  "**V2 Antragsbefugnis** – jede natürliche oder juristische Person, Interessenverbände (§ 53 Abs. 2 MarkenG); kein eigenes Interesse nötig\n"
                  "**V3 Form** – schriftlich, Tatsachen und Beweismittel angeben (§ 53 Abs. 1 S. 1, 2 MarkenG); Inlandsvertreter § 96 Abs. 1 MarkenG\n"
                  "**V4 Keine entgegenstehende Entscheidung** – unanfechtbar entschieden über denselben Streitgegenstand zwischen denselben Parteien (§ 53 Abs. 1 S. 4 MarkenG)\n"
                  "**V5 Frist** – grundsätzlich keine; § 8 Abs. 2 Nr. 1–3 MarkenG: Antrag binnen zehn Jahren seit dem Tag der Eintragung (§ 50 Abs. 2 S. 3 MarkenG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB; Verfahren von Amts wegen nur binnen zwei Jahren seit Eintragung für § 8 Abs. 2 Nr. 4–14 MarkenG (§ 50 Abs. 3 Nr. 1 MarkenG)\n\n"
                  "**B · Begründetheit**\n"
                  "**V6 Eintragung entgegen § 3, § 7 oder § 8 MarkenG** – maßgeblich ist die Rechtslage am Anmeldetag (Bösgläubigkeit: Zeitpunkt der Anmeldung)\n"
                  "**V7 Hindernis besteht noch bei der Entscheidung** – § 50 Abs. 2 S. 1 MarkenG (für § 3, § 7, § 8 Abs. 2 Nr. 1–13 MarkenG; nicht für Nr. 14)\n"
                  "**V8 Keine Verkehrsdurchsetzung bis zum Antrag** – § 50 Abs. 2 S. 2 MarkenG (nur Nr. 1–3)\n\n"
                  "**C · Verfahren**\n"
                  "Mitteilung an den Inhaber mit Zweimonatsfrist (§ 53 Abs. 4 MarkenG); kein Widerspruch → Nichtigkeit ohne Sachprüfung (§ 53 Abs. 5 S. 1 MarkenG); Widerspruch → Mitteilung an den Antragsteller, Fortsetzung (§ 53 Abs. 5 S. 2 MarkenG); Entscheidung der Markenabteilung (§ 56 Abs. 3 MarkenG).\n\n"
                  "**⇒ Rechtsfolge:** Nichtigerklärung und Löschung, ggf. teilweise (§ 50 Abs. 1, 4 MarkenG); Wirkung von Anfang an (§ 52 Abs. 2 MarkenG); Beschwerdegebühr später 500 € (Nr. 401 100 Anlage PatKostG).\n\n"
                  "**Klausurfallen:** Bösgläubigkeit nie im Widerspruch. Ein nur lokal geschütztes Kennzeichen trägt den Bösgläubigkeitsvorwurf nicht allein (BGH LIQUIDROM). Wer eine Sachangabe anmeldet, ist nicht deshalb bösgläubig (BPatG Öresundbrücke). Urheber- und Namensrechte gehören zu § 51 MarkenG, nicht zu § 50 MarkenG.\n\n"
                  "**In den Klausuren:** NS II/2019 (Marke des Ticketverkäufers), NS II/2020 (Balidrom: Pächterin meldet an), NS I/2020 (ACRIGLAS als Gattungsbezeichnung), NS I/2021 (fremdsprachiger Begriff „Kumas“), NS II/2018 (Fassbrause beschreibend), NS II/2025 (Bösgläubigkeit im Widerspruch).",
                  concepts=["nichtigkeit", "absolute_schutzhindernisse", "boesglaeubigkeit", "verwaltungsverfahren_loeschung"],
                  norms=["§ 50 MarkenG", "§ 8 MarkenG", "§ 53 MarkenG", "§ 52 MarkenG", "§ 56 MarkenG", "Art. 45 MarkenRL", "§ 6 PatKostG", "Anlage PatKostG"],
                  cases=["bgh_liquidrom", "bpatg_oeresundbruecke"], abschnitt="Normenkette"),
            intro("k15d-1", "Definitionen",
                  "**Bösgläubige Anmeldung (§ 8 Abs. 2 Nr. 14 MarkenG):** Anmeldung, die rechtsmissbräuchlich oder sittenwidrig ist, insbesondere weil der Anmelder die Marke nicht zur Förderung des eigenen Absatzes, sondern in erster Linie als Mittel des Wettbewerbskampfes anmeldet (Sperrmarke) oder einen schutzwürdigen Besitzstand eines anderen stört; Gesamtwürdigung, maßgeblich ist die Anmeldung, späteres Verhalten ist Indiz (BGH GLÜCKSPILZ).\n"
                  "**Unterscheidungskraft (§ 8 Abs. 2 Nr. 1 MarkenG):** die einer Marke innewohnende konkrete Eignung, vom Verkehr als Unterscheidungsmittel für die Waren oder Dienstleistungen eines Unternehmens gegenüber denen anderer aufgefasst zu werden (st. Rspr. des BGH).\n"
                  "**Beschreibende Angabe (§ 8 Abs. 2 Nr. 2 MarkenG):** Zeichen oder Angabe, die im Verkehr zur Bezeichnung von Merkmalen der Waren oder Dienstleistungen dienen kann; es genügt, dass dies vernünftigerweise für die Zukunft zu erwarten ist (EuGH Windsurfing Chiemsee).\n"
                  "**Üblich gewordene Bezeichnung (§ 8 Abs. 2 Nr. 3 MarkenG):** Zeichen, das im allgemeinen Sprachgebrauch oder in den redlichen und ständigen Verkehrsgepflogenheiten zur Bezeichnung der Waren oder Dienstleistungen üblich geworden ist (Gattungsbezeichnung).\n"
                  "**Verkehrsdurchsetzung (§ 8 Abs. 3, § 50 Abs. 2 S. 2 MarkenG):** Ein erheblicher Teil der beteiligten Verkehrskreise ordnet die Waren aufgrund der Marke einem bestimmten Unternehmen zu; feste Prozentsätze gibt es nicht (EuGH Windsurfing Chiemsee).\n"
                  "**Popularantrag:** Antragsbefugt ist jede natürliche oder juristische Person ohne eigenes Interesse (§ 53 Abs. 2 MarkenG).\n"
                  "**Nichtigkeit:** Beseitigung der Eintragung mit Wirkung von Anfang an, weil die Marke nicht hätte eingetragen werden dürfen (§ 50 Abs. 1, § 52 Abs. 2 MarkenG).",
                  concepts=["boesglaeubigkeit", "unterscheidungskraft", "freihaltebeduerfnis", "uebliche_bezeichnung", "verkehrsdurchsetzung", "nichtigkeit"],
                  norms=["§ 8 MarkenG", "§ 50 MarkenG", "§ 52 MarkenG", "§ 53 MarkenG"], cases=["bgh_glueckspilz", "eugh_chiemsee"], abschnitt="Definitionen"),
            mc("k15d-2", "Wer darf den Antrag stellen?",
               "Wer ist befugt, die Nichtigkeit einer Marke wegen absoluter Schutzhindernisse zu beantragen?",
               ["Nur der Inhaber eines älteren Rechts",
                "Jede natürliche oder juristische Person sowie Interessenverbände (§ 53 Abs. 2 MarkenG)",
                "Nur Wettbewerber mit eigenem Interesse",
                "Nur der Präsident des DPMA"], 1,
               ["**§ 53 Abs. 2 MarkenG.** Der Antrag wegen absoluter Schutzhindernisse ist ein Popularantrag; er dient dem Allgemeininteresse an einem bereinigten Register. Nur für ältere Rechte ist der Inhaber dieser Rechte antragsbefugt (§ 53 Abs. 3 MarkenG)."],
               merke="Absolut und Verfall: jedermann (§ 53 Abs. 2 MarkenG); ältere Rechte: nur Inhaber (§ 53 Abs. 3 MarkenG).",
               level=1, concepts=["verwaltungsverfahren_loeschung"], norms=["§ 53 Abs. 2 MarkenG", "§ 53 Abs. 3 MarkenG"], step="step:schema_loeschung.2", abschnitt=N),
            mc("k15d-3", "Fristen für den Nichtigkeitsantrag",
               "Eine Marke ist seit elf Jahren eingetragen. Gegen sie soll die Nichtigkeit wegen (a) beschreibender Angabe (§ 8 Abs. 2 Nr. 2 MarkenG) und (b) Bösgläubigkeit (§ 8 Abs. 2 Nr. 14 MarkenG) beantragt werden. Was gilt?",
               ["(a) und (b) sind verfristet",
                "(a) ist ausgeschlossen, weil die Zehnjahresfrist abgelaufen ist (§ 50 Abs. 2 S. 3 MarkenG); (b) ist unbefristet",
                "(a) und (b) sind unbefristet",
                "(b) ist nach zwei Jahren ausgeschlossen (§ 50 Abs. 3 Nr. 1 MarkenG)"], 1,
               ["**§ 50 Abs. 2 S. 3 MarkenG** begrenzt nur § 8 Abs. 2 Nr. 1, 2 und 3 MarkenG auf zehn Jahre seit Eintragung. Für die Bösgläubigkeit gibt es keine Frist. Die Zweijahresfrist des § 50 Abs. 3 Nr. 1 MarkenG gilt nur für das Verfahren von Amts wegen."],
               merke="Nr. 1–3: zehn Jahre (§ 50 Abs. 2 S. 3) · Amtsverfahren: zwei Jahre (§ 50 Abs. 3 Nr. 1) · Nr. 14 auf Antrag unbefristet.",
               level=2, concepts=["nichtigkeit"], norms=["§ 50 Abs. 2 MarkenG", "§ 50 Abs. 3 MarkenG"], step="step:schema_loeschung.2", abschnitt=N),
            fall("k15d-4", "Bösgläubigkeit im Widerspruch (NS II/2025)",
                 "Die Widersprechende trägt vor, „Gold-Bärger“ sei bösgläubig angemeldet worden; die Markenstelle müsse die Marke wegen des Amtsermittlungsgrundsatzes und analog § 50 Abs. 3 MarkenG löschen.",
                 "Kann die Bösgläubigkeit im Widerspruchsverfahren berücksichtigt werden?", False,
                 ["**Nein!** Das Widerspruchsverfahren entscheidet nur über die älteren Rechte des § 42 Abs. 2 MarkenG. Bösgläubigkeit ist im Nichtigkeitsverfahren vor der Markenabteilung geltend zu machen (§ 50 Abs. 1, § 53 MarkenG). § 50 Abs. 3 MarkenG ist wegen der getrennten Zuständigkeiten (§ 56 Abs. 2, 3 MarkenG) nicht analog anwendbar (BPatG Engelbrecht)."],
                 merke="Markenstelle (Widerspruch) ≠ Markenabteilung (Nichtigkeit), § 56 MarkenG.",
                 level=2, concepts=["boesglaeubigkeit", "widerspruch"], norms=["§ 42 Abs. 2 MarkenG", "§ 50 MarkenG", "§ 56 MarkenG"], cases=["bpatg_engelbrecht"], abschnitt=N),
            fall("k15d-5", "Nur lokal geschützt (NS II/2020)",
                 "Die frühere Pächterin meldet „Balidrom“ als Marke an. Die Markenabteilung löscht wegen Bösgläubigkeit allein mit der Begründung, die Anmeldung beeinträchtige das Unternehmenskennzeichen der Verpächterin, das nur für ein Bad in Berlin geschützt ist.",
                 "Trägt diese Begründung die Löschung?", False,
                 ["**Nein!** Ein räumlich beschränktes Unternehmenskennzeichen könnte der Marke nicht einmal nach § 51 Abs. 1 MarkenG i.V.m. § 12 MarkenG entgegengehalten werden; dieser Wertung darf § 8 Abs. 2 Nr. 14 MarkenG nicht ausweichen (BGH LIQUIDROM). Zu prüfen bleibt, ob die Marke als zweckfremdes Mittel des Wettbewerbskampfes angemeldet wurde."],
                 merke="Bösgläubigkeit: Besitzstandsstörung nur, wo das ältere Kennzeichen selbst Schutz hätte; sonst Sperrzweck prüfen.",
                 level=3, concepts=["boesglaeubigkeit", "unternehmenskennzeichen"], norms=["§ 8 Abs. 2 MarkenG", "§ 12 MarkenG"], cases=["bgh_liquidrom", "bpatg_liquidrom"], abschnitt=N),
            fall("k15d-6", "Früher beschreibend, heute nicht mehr",
                 "Eine Wortmarke war bei der Anmeldung 2018 für Software eine gängige Fachangabe. Seit 2023 verwendet niemand mehr den Begriff; 2026 wird die Nichtigkeit nach § 8 Abs. 2 Nr. 2 MarkenG beantragt.",
                 "Ist die Marke für nichtig zu erklären?", False,
                 ["**Nein!** Bei § 8 Abs. 2 Nr. 1–13 MarkenG muss das Schutzhindernis auch noch im Zeitpunkt der Entscheidung über den Antrag bestehen (§ 50 Abs. 2 S. 1 MarkenG). Ist der Begriff nicht mehr beschreibend und auch künftig nicht dazu geeignet, entfällt der Nichtigkeitsgrund."],
                 merke="Zwei Zeitpunkte: Anmeldung (Eintragung „entgegen“) und Entscheidung (§ 50 Abs. 2 S. 1 MarkenG).",
                 level=2, concepts=["freihaltebeduerfnis", "nichtigkeit"], norms=["§ 50 Abs. 2 MarkenG"], abschnitt=N),
            fall("k15d-7", "Durchgesetzt bis zum Antrag",
                 "Eine bei der Anmeldung nicht unterscheidungskräftige Farbmarke hat sich nach der Eintragung durch intensive Benutzung im Verkehr durchgesetzt, bevor ein Wettbewerber die Nichtigkeit beantragt.",
                 "Ist die Marke wegen § 8 Abs. 2 Nr. 1 MarkenG für nichtig zu erklären?", False,
                 ["**Nein!** § 8 Abs. 2 Nr. 1, 2 oder 3 MarkenG findet im Nichtigkeitsverfahren keine Anwendung, wenn sich die Marke bis zum Antrag infolge ihrer Benutzung in den beteiligten Verkehrskreisen durchgesetzt hat (§ 50 Abs. 2 S. 2 MarkenG). Den Grad der Durchsetzung muss der Inhaber belegen, meist mit einer Verkehrsbefragung."],
                 merke="Nachträgliche Verkehrsdurchsetzung heilt Nr. 1–3 bis zum Antrag (§ 50 Abs. 2 S. 2 MarkenG).",
                 level=2, concepts=["verkehrsdurchsetzung", "farbmarke"], norms=["§ 50 Abs. 2 MarkenG", "§ 8 Abs. 3 MarkenG"], abschnitt=N),
            *fallkette("k15d-8", "Die Marke des Ticketverkäufers (nach NS II/2019)",
                       "K hat bis 2017 in Deutschland Tickets für die Øresundbrücke vertrieben und bietet selbst Reisen an. Er meldet am 13. Februar 2019 eine Wort-/Bildmarke „oeresund-bruecke“ mit naturgetreuer Brückenzeichnung für Reise- und Ticketdienstleistungen an; eingetragen am 8. April 2019. Die Betreiberin hält das für bösgläubig.",
                       [frage("V0: Welche Gebühr fällt an, und bis wann ist sie zu zahlen?", 2,
                              ["**400 € (Nr. 333 300 Anlage PatKostG), binnen drei Monaten ab Fälligkeit** (§ 3 Abs. 1, § 6 Abs. 1 S. 2 PatKostG), weil für den Antrag keine gesetzliche Frist gilt; sonst gilt der Antrag als zurückgenommen (§ 6 Abs. 2 PatKostG)."],
                              optionen=["250 € mit dem Antrag", "100 € binnen eines Monats", "400 € binnen drei Monaten ab Fälligkeit", "500 € sofort"],
                              merke="Nichtigkeit: 400 € · § 6 Abs. 1 S. 2 PatKostG · § 6 Abs. 2 PatKostG.",
                              norms=["§ 6 PatKostG", "Anlage PatKostG"], concepts=["zahlungstag"]),
                        frage("V1: Kann die Betreiberin statt des Antrags beim DPMA Klage auf Nichtigerklärung wegen Bösgläubigkeit vor dem LG erheben?", False,
                              ["**Nein!** Die Klage nach § 55 Abs. 1 MarkenG gibt es nur für Verfall (§ 49 MarkenG) und ältere Rechte (§ 51 MarkenG). Absolute Schutzhindernisse einschließlich der Bösgläubigkeit sind nur durch Antrag beim DPMA geltend zu machen (§ 53 Abs. 1 MarkenG)."],
                              merke="§ 50 MarkenG nur DPMA; § 49 und § 51 MarkenG: DPMA oder LG.",
                              norms=["§ 53 Abs. 1 MarkenG", "§ 55 MarkenG"]),
                        frage("V5: Ist der Antrag wegen Bösgläubigkeit fristgebunden?", False,
                              ["**Nein!** Für § 8 Abs. 2 Nr. 14 MarkenG gelten weder die Zehnjahresfrist (§ 50 Abs. 2 S. 3 MarkenG) noch das Fortbestehen (§ 50 Abs. 2 S. 1 MarkenG). Eine Anregung zum Amtsverfahren war nur bis 8. April 2021 möglich (§ 50 Abs. 3 Nr. 1 MarkenG)."],
                              merke="Bösgläubigkeit: Antrag jederzeit; Amtsverfahren zwei Jahre ab Eintragung.",
                              norms=["§ 50 Abs. 2 MarkenG", "§ 50 Abs. 3 MarkenG"]),
                        frage("V6: Ist die Anmeldung bösgläubig?", False,
                              ["**Nein!** „Öresundbrücke“ ist eine geografische Sachangabe; an ihr hat die Betreiberin keinen schutzwürdigen Besitzstand. Die Absicht, einen gebräuchlichen Begriff zu monopolisieren, genügt nicht; K erbringt die Dienstleistungen selbst, Indizien für eine Sperrmarke fehlen (BPatG Öresundbrücke). Aus der Sachangabe gewährt die Marke ohnehin keine Rechte (§ 23 Abs. 1 Nr. 2 MarkenG)."],
                              merke="Bösgläubigkeit: Besitzstand, Sperrzweck oder Behinderung – nicht schon Monopolisierungswunsch.",
                              norms=["§ 8 Abs. 2 MarkenG", "§ 23 MarkenG"], concepts=["boesglaeubigkeit"]),
                        ], abschnitt=K, level=2, norms=["§ 50 MarkenG"], cases=["bpatg_oeresundbruecke"]),
        ]),
        # ==============================================================
        dict(id="k15e", titel="§§ 51, 53, 55 MarkenG: Nichtigkeit wegen älterer Rechte", einheiten=[
            intro("k15e-0", "Prüfungsschema",
                  "**AGL:** § 51 Abs. 1 MarkenG i.V.m. § 9 bis § 13 MarkenG; Verfahren § 53 MarkenG (DPMA, seit 01.05.2020) oder § 55 MarkenG (Klage, LG nach § 140 Abs. 1 MarkenG)\n\n"
                  "**0 · Wirksamkeit (DPMA)**\n"
                  "**V0 Gebühr** – 400 € (Nr. 333 300 Anlage PatKostG), für jedes weitere ältere Recht 100 € (Nr. 333 350 Anlage PatKostG); § 6 Abs. 1 S. 2, Abs. 2 PatKostG\n\n"
                  "**A · Zulässigkeit**\n"
                  "**V1 Statthaftigkeit, Wahl des Verfahrens** – Antrag beim DPMA (§ 53 Abs. 1 S. 1 MarkenG) oder Klage (§ 55 Abs. 1 MarkenG); kein Doppelverfahren: Antrag unzulässig bei rechtskräftiger Entscheidung oder rechtshängiger Klage (§ 53 Abs. 1 S. 4, 5 MarkenG), Klage unzulässig bei Entscheidung oder anhängigem Antrag nach § 53 MarkenG (§ 55 Abs. 1 S. 2 MarkenG)\n"
                  "**V2 Antrags- bzw. Klagebefugnis** – nur Inhaber der Rechte nach § 9 bis § 13 MarkenG und Berechtigte aus g.U./g.g.A. (§ 53 Abs. 3 MarkenG; § 55 Abs. 2 Nr. 2, 3 MarkenG); mehrere Rechte desselben Inhabers in einem Antrag (§ 51 Abs. 1 S. 2 MarkenG)\n"
                  "**V3 Richtiger Gegner (Klage)** – eingetragener Inhaber oder Rechtsnachfolger (§ 55 Abs. 1 S. 1 MarkenG); Rechtsnachfolge § 53 Abs. 7, § 55 Abs. 4 MarkenG\n"
                  "**V4 Form** – schriftlich, Tatsachen und Beweismittel (§ 53 Abs. 1 S. 1, 2 MarkenG); Klage: Anwaltszwang (§ 78 ZPO); Inlandsvertreter § 96 Abs. 1 MarkenG\n\n"
                  "**B · Begründetheit**\n"
                  "**V5 Älteres Recht** – Marke (§ 9 MarkenG), notorische Marke (§ 10 MarkenG), Agentenmarke (§ 11 MarkenG), Benutzungsmarke oder geschäftliche Bezeichnung mit bundesweiter Untersagungsbefugnis (§ 12 MarkenG, § 5 Abs. 2 MarkenG), sonstige Rechte (§ 13 MarkenG: Namen, Bildnis, Urheberrecht, Sortenbezeichnung, geografische Herkunftsangabe); Zeitrang § 6 MarkenG\n"
                  "**V6 Kollision** – § 9 Abs. 1 Nr. 1–3 MarkenG; bei geschäftlichen Bezeichnungen § 15 Abs. 2, 3 MarkenG; bei § 13 MarkenG Verletzung des sonstigen Rechts\n"
                  "**V7 Kein Ausschluss** – Duldung fünf Jahre in Kenntnis (§ 51 Abs. 2 S. 1, 2 MarkenG), Zustimmung (§ 51 Abs. 2 S. 3 MarkenG), Bekanntheit erst nach dem Zeitrangtag (§ 51 Abs. 3 MarkenG), ältere Marke selbst verfalls- oder nichtigkeitsreif am Zeitrangtag (§ 51 Abs. 4 MarkenG)\n"
                  "**V8 Benutzung auf Einrede** – DPMA § 53 Abs. 6 MarkenG, Klage § 55 Abs. 3 MarkenG: fünf Jahre vor Antrag bzw. Klage; endet die Schonfrist danach, fünf Jahre vor Entscheidung bzw. Schluss der mündlichen Verhandlung; zusätzlich keine Verfallsreife am Anmeldetag der jüngeren Marke; Unionsmarke § 119 Nr. 5 MarkenG; IR-Marke § 116 Abs. 2 MarkenG\n\n"
                  "**C · Verfahren DPMA:** Mitteilung mit Zweimonatsfrist (§ 53 Abs. 4 MarkenG); kein Widerspruch → Nichtigkeit (§ 53 Abs. 5 S. 1 MarkenG).\n\n"
                  "**⇒ Rechtsfolge:** Nichtigerklärung und Löschung, ggf. teilweise (§ 51 Abs. 1, 5 MarkenG); Wirkung von Anfang an (§ 52 Abs. 2 MarkenG); Klage: Kosten § 91 ZPO, Patentanwalt § 140 Abs. 4 MarkenG.\n\n"
                  "**Klausurfallen:** Vor dem 01.05.2020 gab es nur die Klage. Eine Unionsmarke kann das DPMA nicht für nichtig erklären (EUIPO oder Widerklage vor dem Unionsmarkengericht). Urheber- und Namensrechte (§ 13 MarkenG) gehören hierher, nicht zu § 50 MarkenG.\n\n"
                  "**In den Klausuren:** NS II/2019 (Namens- und Urheberrecht an der Brücke), NS I/2024 (Nichtigkeitsantrag gegen die Unionswiderspruchsmarke), NS II/2020 (lokales Unternehmenskennzeichen), NS III/2019 Frage 4 (Weg nach versäumter Widerspruchsfrist), NS I/2021 (kostengünstiges Vorgehen gegen „RAMI“).",
                  concepts=["nichtigkeit", "relative_schutzhindernisse", "verwaltungsverfahren_loeschung", "unternehmenskennzeichen", "geschaeftliche_bezeichnung"],
                  norms=["§ 51 MarkenG", "§ 53 MarkenG", "§ 55 MarkenG", "§ 12 MarkenG", "§ 13 MarkenG", "§ 140 MarkenG", "§ 119 MarkenG", "Art. 45 MarkenRL", "Anlage PatKostG"],
                  cases=["bpatg_aussetzung_unionsmarke", "bpatg_oeresundbruecke"], abschnitt="Normenkette"),
            intro("k15e-1", "Definitionen",
                  "**Älteres Recht:** Recht im Sinne der § 9 bis § 13 MarkenG mit früherem Zeitrang als die angegriffene Marke (§ 51 Abs. 1 S. 1 MarkenG, § 6 MarkenG).\n"
                  "**Geschäftliche Bezeichnungen:** Unternehmenskennzeichen und Werktitel (§ 5 Abs. 1 MarkenG); Unternehmenskennzeichen sind Zeichen, die im geschäftlichen Verkehr als Name, Firma oder besondere Bezeichnung eines Geschäftsbetriebs oder Unternehmens benutzt werden (§ 5 Abs. 2 S. 1 MarkenG).\n"
                  "**Bundesweite Untersagungsbefugnis:** Das nicht eingetragene Recht berechtigt, die Benutzung der jüngeren Marke im gesamten Gebiet der Bundesrepublik Deutschland zu untersagen (§ 12, § 13 Abs. 1 MarkenG).\n"
                  "**Sonstige Rechte:** insbesondere Namensrechte, Recht an der eigenen Abbildung, Urheberrechte, Sortenbezeichnungen, geografische Herkunftsangaben und sonstige gewerbliche Schutzrechte (§ 13 Abs. 2 MarkenG).\n"
                  "**Duldung:** Der Inhaber des älteren Rechts hat die Benutzung der eingetragenen jüngeren Marke während fünf aufeinanderfolgender Jahre in Kenntnis dieser Benutzung hingenommen; ausgenommen bösgläubige Anmeldung (§ 51 Abs. 2 S. 1 MarkenG).\n"
                  "**Kennzeichenstreitsache:** jede Klage, durch die ein Anspruch aus einem der im MarkenG geregelten Rechtsverhältnisse geltend gemacht wird (Legaldefinition § 140 Abs. 1 MarkenG).",
                  concepts=["geschaeftliche_bezeichnung", "unternehmenskennzeichen", "verwirkung"],
                  norms=["§ 5 MarkenG", "§ 12 MarkenG", "§ 13 MarkenG", "§ 51 MarkenG", "§ 140 MarkenG"], abschnitt="Definitionen"),
            mc("k15e-2", "Seit wann beim DPMA?",
               "Seit wann kann die Nichtigkeit einer deutschen Marke wegen älterer Rechte beim DPMA beantragt werden?",
               ["Seit jeher", "Seit dem 14. Januar 2019", "Seit dem 1. Mai 2020; vorher nur durch Klage vor den ordentlichen Gerichten", "Gar nicht; nur das LG ist zuständig"], 2,
               ["**Seit 1. Mai 2020.** Das MaMoG hat das Amtsverfahren für ältere Rechte (§ 51, § 53 MarkenG) eingeführt; diese Teile traten am 1. Mai 2020 in Kraft. Seither hat der Inhaber die Wahl zwischen Antrag beim DPMA und Klage nach § 55 MarkenG."],
               merke="Ältere Rechte: DPMA seit 01.05.2020 (§ 53 MarkenG) oder LG (§ 55 MarkenG).",
               level=1, concepts=["verwaltungsverfahren_loeschung"], norms=["§ 53 MarkenG", "§ 55 MarkenG"], step="step:schema_loeschung.3", abschnitt=N),
            mc("k15e-3", "Marke und Firma in einem Antrag",
               "Die Mandantin stützt ihren Nichtigkeitsantrag beim DPMA auf ihre eingetragene Marke und ihr Unternehmenskennzeichen. Welche Gebühr fällt an?",
               ["400 €", "500 € (400 € + 100 € für das weitere Recht)", "800 € (zwei Anträge)", "300 €"], 1,
               ["**500 €.** Der Antrag kann auf mehrere ältere Rechte desselben Inhabers gestützt werden (§ 51 Abs. 1 S. 2 MarkenG). Gebühr: 400 € (Nr. 333 300) plus 100 € für jedes weitere Recht (Nr. 333 350 Anlage PatKostG)."],
               merke="Nichtigkeit ältere Rechte: 400 € + 100 € je weiteres Recht.",
               level=1, concepts=["verwaltungsverfahren_loeschung"], norms=["§ 51 Abs. 1 MarkenG", "Anlage PatKostG"], abschnitt=N),
            fall("k15e-4", "Sechs Jahre zugesehen",
                 "Die Inhaberin einer älteren Marke weiß seit sechs Jahren, dass ein Wettbewerber seine eingetragene jüngere, verwechselbare Marke benutzt. Jetzt beantragt sie die Nichtigkeit. Anhaltspunkte für eine bösgläubige Anmeldung fehlen.",
                 "Ist die Nichtigerklärung ausgeschlossen?", True,
                 ["**Ja!** Hat der Inhaber der älteren Marke die Benutzung der jüngeren eingetragenen Marke während fünf aufeinanderfolgender Jahre in Kenntnis geduldet, kann die Eintragung nicht für nichtig erklärt werden, es sei denn, die Anmeldung war bösgläubig (§ 51 Abs. 2 S. 1 MarkenG). Spiegelbildlich sind Unterlassungsansprüche verwirkt (§ 21 Abs. 1 MarkenG)."],
                 merke="Duldung fünf Jahre in Kenntnis ⇒ § 51 Abs. 2 MarkenG, § 21 Abs. 1 MarkenG.",
                 level=2, concepts=["verwirkung"], norms=["§ 51 Abs. 2 MarkenG", "§ 21 MarkenG"], abschnitt=N),
            fall("k15e-5", "Die Vorratsmarke als Angriffsmittel",
                 "Die Antragstellerin stützt ihren Nichtigkeitsantrag beim DPMA auf eine seit acht Jahren eingetragene Marke, die sie nie benutzt hat. Der Markeninhaber erhebt die Einrede der Nichtbenutzung.",
                 "Scheitert der Antrag?", True,
                 ["**Ja!** Auf Einrede muss die Antragstellerin nachweisen, dass ihre Marke in den letzten fünf Jahren vor Antragstellung gemäß § 26 MarkenG benutzt worden ist, sofern zu diesem Zeitpunkt seit mindestens fünf Jahren kein Widerspruch mehr gegen sie möglich war (§ 53 Abs. 6 S. 1 MarkenG). Nur benutzte Waren zählen (§ 53 Abs. 6 S. 4 MarkenG)."],
                 merke="Einrede: Widerspruch § 43 Abs. 1 · DPMA-Nichtigkeit § 53 Abs. 6 · Klage § 55 Abs. 3 · Verletzung § 25 Abs. 2 MarkenG.",
                 level=2, concepts=["nichtbenutzungseinrede"], norms=["§ 53 Abs. 6 MarkenG", "§ 26 MarkenG"], abschnitt=N),
            fall("k15e-6", "Angriff auf die Unionsmarke (NS I/2024)",
                 "Im Widerspruchsbeschwerdeverfahren aus einer Unionsmarke beantragt der Markeninhaber beim DPMA, die Unionswiderspruchsmarke wegen eines älteren deutschen Rechts für nichtig zu erklären, und will das Beschwerdeverfahren deshalb aussetzen lassen.",
                 "Kann das DPMA die Unionsmarke für nichtig erklären?", False,
                 ["**Nein!** Über die Nichtigkeit einer Unionsmarke entscheiden nur das EUIPO (Art. 63 UMV) oder ein Unionsmarkengericht auf Widerklage (Art. 128 UMV, § 122 MarkenG). Der Antrag beim DPMA ist für das Beschwerdeverfahren daher nicht vorgreiflich und rechtfertigt keine Aussetzung (BPatG, 29 W (pat) 522/20)."],
                 merke="Unionsmarke angreifen: EUIPO oder Widerklage vor dem Unionsmarkengericht, nie DPMA.",
                 level=3, concepts=["unionsmarke", "aussetzung"], norms=["§ 51 MarkenG", "§ 53 MarkenG", "§ 122 MarkenG"], cases=["bpatg_aussetzung_unionsmarke"], abschnitt=N),
            fall("k15e-7", "Zwei Verfahren zugleich",
                 "Die Mandantin hat beim DPMA die Nichtigkeit wegen ihrer älteren Marke beantragt; das Verfahren läuft. Zur Beschleunigung erhebt sie zusätzlich Klage auf Nichtigerklärung aus derselben Marke gegen denselben Inhaber vor dem LG.",
                 "Ist die Klage zulässig?", False,
                 ["**Nein!** Die Klage ist unzulässig, wenn über denselben Streitgegenstand zwischen den Parteien ein Antrag nach § 53 MarkenG beim DPMA anhängig ist (§ 55 Abs. 1 S. 2 Nr. 2 MarkenG). Umgekehrt ist der Antrag unzulässig, wenn die Klage zuerst rechtshängig war (§ 53 Abs. 1 S. 5 MarkenG)."],
                 merke="DPMA oder LG – nie beides (§ 53 Abs. 1 S. 4, 5, § 55 Abs. 1 S. 2 MarkenG).",
                 level=2, concepts=["verwaltungsverfahren_loeschung"], norms=["§ 55 Abs. 1 MarkenG", "§ 53 Abs. 1 MarkenG"], abschnitt=N),
            *fallkette("k15e-8", "Name und Bild der Brücke (nach NS II/2019)",
                       "Die Betreiberin der Øresundbrücke will die Wort-/Bildmarke „oeresund-bruecke“ des K mit naturgetreuer Zeichnung der Brücke im Jahr 2026 beseitigen. Sie beruft sich auf ein Namensrecht an der Bezeichnung des Bauwerks und auf das Urheberrecht am Brückenbau.",
                       [frage("V1: Ist der Antrag auf Nichtigkeit wegen älterer Rechte beim DPMA statthaft?", True,
                              ["**Ja!** Seit 1. Mai 2020 kann die Nichtigkeit wegen älterer Rechte beim DPMA beantragt werden (§ 51 Abs. 1, § 53 Abs. 1 MarkenG); alternativ Klage vor dem LG (§ 55 Abs. 1, § 140 Abs. 1 MarkenG)."],
                              merke="§ 51 MarkenG: Antrag § 53 oder Klage § 55 MarkenG.", norms=["§ 51 MarkenG", "§ 53 MarkenG"]),
                        frage("Kann das Urheberrecht stattdessen im Nichtigkeitsverfahren wegen Bösgläubigkeit (§ 50 MarkenG) geltend gemacht werden?", False,
                              ["**Nein!** Ein Urheberrecht ist ein sonstiges älteres Recht (§ 13 Abs. 2 Nr. 3 MarkenG); es ist nach § 51 MarkenG geltend zu machen, nicht im Verfahren wegen absoluter Schutzhindernisse (BPatG Öresundbrücke). Antragsbefugt ist dann nur der Inhaber des Rechts (§ 53 Abs. 3 MarkenG)."],
                              merke="§ 13 MarkenG-Rechte ⇒ § 51 MarkenG, Antragsbefugnis § 53 Abs. 3 MarkenG.", norms=["§ 13 MarkenG", "§ 53 Abs. 3 MarkenG"]),
                        frage("V5: Hat die Betreiberin ein älteres Namensrecht an der deutschen Bezeichnung „Öresund-Brücke“?", False,
                              ["**Nein!** „Öresundbrücke“ ist die deutsche Sachbezeichnung des Bauwerks, kein Name der Betreiberin; ein Namensrecht (§ 13 Abs. 2 Nr. 1 MarkenG, § 12 BGB) setzt eine Namensfunktion für eine Person oder ein Unternehmen voraus (Lösung NS II/2019)."],
                              merke="Sachbezeichnung eines Bauwerks ≠ Name des Betreibers.", norms=["§ 13 MarkenG"]),
                        frage("V6: Verletzt die Brückenzeichnung in der Marke voraussichtlich das Urheberrecht am Bauwerk?", False,
                              ["**Nein, voraussichtlich nicht!** Werke, die sich bleibend an öffentlichen Wegen befinden, dürfen mit Mitteln der Malerei oder Grafik vervielfältigt und verbreitet werden (Panoramafreiheit, § 59 Abs. 1 UrhG). Die Lösung NS II/2019 verneint deshalb ein durchgreifendes älteres Recht."],
                              merke="§ 13 Abs. 2 Nr. 3 MarkenG + Schranken des UrhG mitprüfen (§ 59 UrhG).", norms=["§ 13 MarkenG"]),
                        ], abschnitt=K, level=3, concepts=["nichtigkeit"], cases=["bpatg_oeresundbruecke"]),
        ]),
        # ==============================================================
        dict(id="k15f", titel="§§ 49, 53 MarkenG: Verfall", einheiten=[
            intro("k15f-0", "Prüfungsschema",
                  "**AGL:** § 49 Abs. 1 S. 1 MarkenG (Nichtbenutzung) bzw. § 49 Abs. 2 Nr. 1–3 MarkenG; Verfahren § 53 MarkenG (DPMA) oder § 55 MarkenG (Klage)\n\n"
                  "**0 · Wirksamkeit**\n"
                  "**V0 Antragsgebühr** – 100 € (Nr. 333 400 Anlage PatKostG), § 6 Abs. 1 S. 2, Abs. 2 PatKostG\n\n"
                  "**A · Zulässigkeit**\n"
                  "**V1 Statthaftigkeit** – Antrag beim DPMA (§ 53 Abs. 1 S. 1 MarkenG) oder Klage (§ 55 Abs. 1 MarkenG, LG § 140 Abs. 1 MarkenG); IR-Marke: Antrag auf Schutzentziehung (§ 115 Abs. 1 MarkenG)\n"
                  "**V2 Antragsbefugnis** – jede natürliche oder juristische Person, Interessenverbände (§ 53 Abs. 2 MarkenG; Klage § 55 Abs. 2 Nr. 1 MarkenG)\n"
                  "**V3 Form** – schriftlich, Tatsachen und Beweismittel (§ 53 Abs. 1 S. 1, 2 MarkenG); Inlandsvertreter § 96 Abs. 1 MarkenG\n\n"
                  "**B · Verfahren vor dem DPMA**\n"
                  "**V4 Mitteilung** – Zustellung an den Inhaber mit Aufforderung, sich binnen zwei Monaten zu erklären (§ 53 Abs. 4 MarkenG)\n"
                  "**V5 Widerspruch des Inhabers** – innerhalb von zwei Monaten nach Zustellung (§ 53 Abs. 5 S. 1 MarkenG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB; zulässig schon ab Eingang des Antrags; ohne Fristsetzung läuft keine Frist (BPatG AUTOMATOR)\n"
                  "**V6 Weiterverfolgungsgebühr** – 300 € (Nr. 333 450 Anlage PatKostG) innerhalb eines Monats nach Zustellung des Widerspruchs (§ 53 Abs. 5 S. 4 MarkenG), sonst gilt das Verfallsverfahren als abgeschlossen (§ 53 Abs. 5 S. 5 MarkenG); Alternative Klage nach § 55 MarkenG binnen drei Monaten nach Zustellung der Mitteilung – dann bleibt der DPMA-Antrag für § 49 Abs. 1 S. 3 MarkenG maßgeblich (§ 49 Abs. 1 S. 4 MarkenG)\n\n"
                  "**C · Begründetheit**\n"
                  "**V7 Benutzungsschonfrist abgelaufen** – fünf Jahre ab dem Tag, ab dem kein Widerspruch mehr möglich ist (§ 49 Abs. 1 S. 1 MarkenG, § 26 Abs. 5 MarkenG); IR-Marke § 115 Abs. 2 MarkenG\n"
                  "**V8 Ununterbrochen fünf Jahre keine Benutzung gemäß § 26 MarkenG** – ernsthaft, als Marke, für die eingetragenen Waren, im Inland (§ 26 Abs. 1 MarkenG)\n"
                  "**V9 Keine Heilung** – Benutzungsaufnahme nach Ablauf und vor Antrag heilt (§ 49 Abs. 1 S. 2 MarkenG); unbeachtlich, wenn innerhalb von drei Monaten vor Antrag und nach Kenntnis vom drohenden Antrag vorbereitet (§ 49 Abs. 1 S. 3 MarkenG)\n"
                  "**V10 Keine berechtigten Gründe** – § 26 Abs. 1 a.E. MarkenG\n"
                  "**Abs. 2:** Nr. 1 gebräuchliche Bezeichnung infolge Verhaltens oder Untätigkeit des Inhabers · Nr. 2 Täuschungseignung infolge der Benutzung · Nr. 3 Wegfall der Voraussetzungen des § 7 MarkenG\n\n"
                  "**⇒ Rechtsfolge:** Verfallserklärung und Löschung, ggf. teilweise (§ 49 Abs. 1, 3 MarkenG); Wirkung ab Antrag bzw. Klage (§ 52 Abs. 1 S. 1 MarkenG), auf Antrag ab früherem Verfallszeitpunkt (§ 52 Abs. 1 S. 2 MarkenG). Ohne fristgerechten Widerspruch: Verfall ohne Sachprüfung (§ 53 Abs. 5 S. 1 MarkenG).\n\n"
                  "**Klausurfallen:** Benutzung nur im Ausland ist keine Inlandsbenutzung (anders Unionsmarke). Ohne Fristsetzung in der Mitteilung kein Fristablauf. Übergangsrecht für Anträge vor dem 14.01.2019: § 158 Abs. 6 MarkenG.\n\n"
                  "**In den Klausuren:** NS III/2023 (MEGACAPS: Widerspruch vor Fristbeginn, Benutzung in Frankreich), NS I/2020 (ACRIGLAS: Gefahr der Gattungsbezeichnung, Löschungsrisiko), NS III/2021 Frage 3 (ab wann gegen die angegriffene Marke die Einrede zulässig ist).",
                  concepts=["verfall", "benutzungsschonfrist", "rechtserhaltende_benutzung", "verwaltungsverfahren_loeschung", "ir_benutzungsschonfrist"],
                  norms=["§ 49 MarkenG", "§ 53 MarkenG", "§ 55 MarkenG", "§ 26 MarkenG", "§ 52 MarkenG", "§ 115 MarkenG", "Art. 45 MarkenRL", "Anlage PatKostG"],
                  cases=["bpatg_automator"], abschnitt="Normenkette"),
            intro("k15f-1", "Definitionen",
                  "**Verfall:** Löschung einer zunächst wirksam eingetragenen Marke wegen nachträglich eingetretener Gründe, mit Wirkung ab Antrag oder Klage (§ 49, § 52 Abs. 1 MarkenG).\n"
                  "**Nichtbenutzung:** keine Benutzung gemäß § 26 MarkenG, also nicht ernsthaft, nicht als Marke, nicht für die eingetragenen Waren oder nicht im Inland, während eines ununterbrochenen Zeitraums von fünf Jahren nach Ablauf der Schonfrist (§ 49 Abs. 1 S. 1 MarkenG).\n"
                  "**Tag, ab dem kein Widerspruch mehr möglich ist:** Ablauf der Widerspruchsfrist; bei Widerspruch der Eintritt der Rechtskraft der beendenden Entscheidung oder die Rücknahme (§ 26 Abs. 5 MarkenG); IR-Marke: Abschluss des Schutzerstreckungsverfahrens (§ 115 Abs. 2 MarkenG).\n"
                  "**Heilung:** Beginn oder Wiederaufnahme der Benutzung nach Ende des Fünfjahreszeitraums und vor Antragstellung (§ 49 Abs. 1 S. 2 MarkenG).\n"
                  "**Gebräuchliche Bezeichnung (§ 49 Abs. 2 Nr. 1 MarkenG):** Die Marke ist infolge des Verhaltens oder der Untätigkeit des Inhabers im geschäftlichen Verkehr zur Bezeichnung der Waren selbst geworden; der Verkehr versteht sie nicht mehr als Herkunftshinweis.\n"
                  "**Widerspruch des Inhabers (§ 53 Abs. 5 MarkenG):** Erklärung des Markeninhabers, der Löschung zu widersprechen; sie verhindert die Verfallserklärung ohne Sachprüfung.",
                  concepts=["verfall", "benutzungsschonfrist", "uebliche_bezeichnung"], norms=["§ 49 MarkenG", "§ 26 Abs. 5 MarkenG", "§ 52 MarkenG", "§ 53 Abs. 5 MarkenG", "§ 115 MarkenG"],
                  abschnitt="Definitionen"),
            mc("k15f-2", "Die Gebühren des Verfallsverfahrens",
               "Welche Gebühren fallen im Verfallsverfahren vor dem DPMA an, wenn der Inhaber widerspricht?",
               ["Nur 400 € Antragsgebühr",
                "100 € Antragsgebühr (Nr. 333 400) und 300 € Weiterverfolgungsgebühr (Nr. 333 450) binnen eines Monats nach Zustellung des Widerspruchs",
                "100 € Antragsgebühr; der Widerspruch des Inhabers kostet 300 €",
                "250 € wie beim Widerspruch"], 1,
               ["**100 € + 300 €.** Der Antrag kostet 100 € (Nr. 333 400 Anlage PatKostG). Widerspricht der Inhaber, wird das Verfahren nur fortgesetzt, wenn der Antragsteller binnen eines Monats nach Zustellung des Widerspruchs die Weiterverfolgungsgebühr zahlt (§ 53 Abs. 5 S. 4 MarkenG); sonst gilt es als abgeschlossen (§ 53 Abs. 5 S. 5 MarkenG)."],
               merke="Verfall: 100 € · Widerspruch des Inhabers · 300 € binnen eines Monats (§ 53 Abs. 5 S. 4, 5 MarkenG).",
               level=1, concepts=["verwaltungsverfahren_loeschung", "verfall"], norms=["§ 53 Abs. 5 MarkenG", "Anlage PatKostG"], abschnitt=N),
            fall("k15f-3", "Spät, aber rechtzeitig benutzt",
                 "Eine seit 2015 eingetragene Marke war bis Juni 2025 unbenutzt. Im Juli 2025 nimmt der Inhaber, ohne von Angriffsplänen zu wissen, die ernsthafte Benutzung auf. Im Februar 2026 wird der Verfall beantragt.",
                 "Ist die Marke für verfallen zu erklären?", False,
                 ["**Nein!** Der Verfall kann nicht geltend gemacht werden, wenn nach Ende des Fünfjahreszeitraums und vor Antragstellung eine Benutzung gemäß § 26 MarkenG begonnen oder wieder aufgenommen worden ist (§ 49 Abs. 1 S. 2 MarkenG). Die Benutzung begann mehr als drei Monate vor dem Antrag und ohne Kenntnis; § 49 Abs. 1 S. 3 MarkenG greift nicht."],
                 merke="Heilung § 49 Abs. 1 S. 2 MarkenG; Ausnahme drei Monate + Kenntnis (S. 3).",
                 level=2, concepts=["verfall", "rechtserhaltende_benutzung"], norms=["§ 49 Abs. 1 MarkenG"], step="step:schema_loeschung.1.1", abschnitt=N),
            fall("k15f-4", "Benutzung nach der Abmahnung",
                 "Nach fünf Jahren Nichtbenutzung erhält der Inhaber ein Schreiben, man werde den Verfall beantragen. Daraufhin bereitet er Werbung vor und nimmt sechs Wochen später die Benutzung auf; einen Monat danach geht der Verfallsantrag ein.",
                 "Ist die Marke für verfallen zu erklären?", True,
                 ["**Ja!** Eine Benutzung, die innerhalb von drei Monaten vor dem Antrag begonnen wird, bleibt unberücksichtigt, wenn die Vorbereitungen erst nach Kenntnis vom drohenden Antrag stattfanden (§ 49 Abs. 1 S. 3 MarkenG). Beide Voraussetzungen liegen vor."],
                 merke="Drei Monate + Kenntnis ⇒ keine Heilung (§ 49 Abs. 1 S. 3 MarkenG).",
                 level=2, concepts=["verfall"], norms=["§ 49 Abs. 1 MarkenG"], step="step:schema_loeschung.1.1", abschnitt=N),
            fall("k15f-5", "Benutzung in Frankreich (NS III/2023)",
                 "Die Inhaberin der IR-Marke „MEGACAPS“ belegt Verkäufe von Hüten und T-Shirts unter der Marke in Bekleidungsmärkten in Frankreich; Belege für Deutschland betreffen nur die Jahre 2005 bis 2008.",
                 "Erhalten die Verkäufe in Frankreich den deutschen Schutzrechtsanteil?", False,
                 ["**Nein!** Rechtserhaltend ist nur eine Benutzung im Inland (§ 26 Abs. 1 MarkenG); die IR-Marke wirkt in Deutschland wie eine nationale Marke (§ 112 Abs. 1 MarkenG). Benutzung in anderen Staaten zählt nur bei Unionsmarken (Art. 18 UMV). Belege aus 2005 bis 2008 liegen außerhalb des maßgeblichen Zeitraums."],
                 merke="Deutsche Marke und deutscher IR-Anteil: Benutzung im Inland (§ 26 Abs. 1 MarkenG).",
                 level=2, concepts=["rechtserhaltende_benutzung", "ir_marke"], norms=["§ 26 Abs. 1 MarkenG", "§ 112 MarkenG"], step="step:schema_benutzungszwang.3.4", abschnitt=N),
            fall("k15f-6", "Der Inhaber schweigt",
                 "Das DPMA stellt dem Inhaber den Verfallsantrag mit der Aufforderung zu, sich binnen zwei Monaten zu erklären. Der Inhaber reagiert nicht.",
                 "Wird die Marke ohne Prüfung der Benutzung für verfallen erklärt?", True,
                 ["**Ja!** Widerspricht der Inhaber der Löschung nicht innerhalb der Frist des § 53 Abs. 4 MarkenG, wird der Verfall erklärt und die Eintragung gelöscht (§ 53 Abs. 5 S. 1 MarkenG), ohne Sachprüfung. Wiedereinsetzung in die Widerspruchsfrist des Inhabers ist nach § 91 MarkenG möglich; ausgeschlossen ist nur die Frist des § 42 MarkenG."],
                 merke="Schweigen auf § 53 Abs. 4 MarkenG ⇒ Verfall ohne Sachprüfung (§ 53 Abs. 5 S. 1 MarkenG).",
                 level=1, concepts=["verwaltungsverfahren_loeschung"], norms=["§ 53 Abs. 4 MarkenG", "§ 53 Abs. 5 MarkenG", "§ 91 MarkenG"], abschnitt=N),
            mc("k15f-7", "ACRIGLAS als Gattungsbegriff (NS I/2020)",
               "Die Marke ACRIGLAS war bei der Eintragung unterscheidungskräftig. Weil die Inhaberin nie gegen fremde Verwendungen vorgegangen ist, nennt der Handel heute jedes Acrylglas so. Welche AGL kommt in Betracht?",
               ["§ 50 Abs. 1 MarkenG i.V.m. § 8 Abs. 2 Nr. 3 MarkenG",
                "§ 49 Abs. 2 Nr. 1 MarkenG (Verfall wegen Entwicklung zur gebräuchlichen Bezeichnung)",
                "§ 49 Abs. 1 MarkenG (Nichtbenutzung)",
                "§ 51 Abs. 1 MarkenG"], 1,
               ["**§ 49 Abs. 2 Nr. 1 MarkenG.** Die Entwicklung zur Gattungsbezeichnung nach der Eintragung infolge Untätigkeit des Inhabers ist ein Verfallsgrund (Wirkung ab Antrag, § 52 Abs. 1 MarkenG). § 50 MarkenG verlangt, dass das Hindernis schon bei der Eintragung bestand. Gegenmittel: Hinweise an Händler und Lexika (§ 16 MarkenG), Abmahnungen."],
               merke="Gattung von Anfang an: § 50/§ 8 Abs. 2 Nr. 3 MarkenG; später durch Untätigkeit: § 49 Abs. 2 Nr. 1 MarkenG.",
               level=2, concepts=["verfall", "uebliche_bezeichnung", "nachschlagewerke"], norms=["§ 49 Abs. 2 MarkenG", "§ 16 MarkenG"], step="step:schema_loeschung.1.2", abschnitt=N),
            *fallkette("k15f-8", "MEGACAPS (nach NS III/2023)",
                       "Gegen den deutschen Anteil der IR-Marke „MEGACAPS“ (Inhaberin in Frankreich) wird am 27.10.2021 Verfall beantragt. Das DPMA schreibt am 28.10.2021 nur, sie brauche einen Inlandsvertreter. Ihre Vertreterin widerspricht am 09.12.2021. Die Mitteilung nach § 53 Abs. 4 MarkenG, ohne konkrete Frist, wird am 17.12.2021 zugestellt. Am 11.03.2022 erklärt die Markenabteilung den Verfall ohne Sachprüfung.",
                       [frage("V1: Wie heißt der statthafte Antrag gegen den deutschen Anteil einer IR-Marke?", 3,
                              ["**Antrag auf Schutzentziehung** (§ 115 Abs. 1 MarkenG); er tritt an die Stelle des Verfallsantrags, im Übrigen gelten § 49 und § 53 MarkenG entsprechend (§ 107 Abs. 1 MarkenG)."],
                              optionen=["Widerspruch nach § 114 MarkenG", "Löschungsklage nur vor dem LG", "Antrag beim Internationalen Büro der WIPO", "Antrag auf Schutzentziehung (§ 115 Abs. 1 MarkenG)"],
                              merke="IR-Marke: Schutzverweigerung (§ 114 Abs. 3) statt Löschung, Schutzentziehung (§ 115 Abs. 1 MarkenG) statt Verfall.",
                              norms=["§ 115 MarkenG", "§ 107 MarkenG"], concepts=["ir_marke"]),
                        frage("V5: Ist der Widerspruch vom 09.12.2021 vor Zustellung der Mitteilung wirksam?", True,
                              ["**Ja!** Der Widerspruch gegen den Verfallsantrag ist schon ab Eingang des Antrags beim DPMA zulässig; das Wort „innerhalb“ in § 53 Abs. 5 S. 1 MarkenG legt nur das Fristende fest, wie beim Widerspruch gegen die Eintragung (BPatG AUTOMATOR)."],
                              merke="Widerspruch gegen Verfallsantrag: ab Antragseingang möglich.",
                              norms=["§ 53 Abs. 5 MarkenG"], cases=["bpatg_automator"]),
                        frage("V5: Hat die Mitteilung vom 17.12.2021 die Zweimonatsfrist in Lauf gesetzt?", False,
                              ["**Nein!** Die Frist des § 53 Abs. 4 MarkenG beginnt nur mit einer Mitteilung, die den Inhaber auffordert, sich innerhalb von zwei Monaten zu erklären. Fehlt die Fristsetzung, läuft keine Frist ab; der Verfall durfte nicht ohne Sachprüfung erklärt werden (BPatG AUTOMATOR)."],
                              merke="Keine Fristsetzung ⇒ kein Fristbeginn ⇒ keine Verfallserklärung nach § 53 Abs. 5 S. 1 MarkenG.",
                              norms=["§ 53 Abs. 4 MarkenG"], cases=["bpatg_automator"]),
                        frage("⇒: Wie entscheidet das BPatG über die Beschwerde der Inhaberin?", 0,
                              ["**Aufhebung und Zurückverweisung** wegen eines wesentlichen Verfahrensmangels (§ 70 Abs. 3 Nr. 2 MarkenG), weil das DPMA nicht in der Sache geprüft hat; Rückzahlung der Beschwerdegebühr (500 €, Nr. 401 100 Anlage PatKostG) aus Billigkeit (§ 71 Abs. 3 MarkenG)."],
                              optionen=["Aufhebung, Zurückverweisung (§ 70 Abs. 3 Nr. 2 MarkenG), Rückzahlung der Beschwerdegebühr (§ 71 Abs. 3 MarkenG)", "Zurückweisung der Beschwerde", "Verwerfung als unzulässig", "Eigene Verfallserklärung durch das BPatG"],
                              merke="Verfahrensfehler des DPMA ⇒ § 70 Abs. 3 Nr. 2 und § 71 Abs. 3 MarkenG.",
                              norms=["§ 70 MarkenG", "§ 71 MarkenG"], cases=["bpatg_automator"]),
                        ], abschnitt=K, level=3, concepts=["verfall", "verwaltungsverfahren_loeschung"], cases=["bpatg_automator"]),
        ]),
        # ==============================================================
        dict(id="k15g", titel="§§ 14, 15, 18, 19 MarkenG: Verletzungsansprüche", einheiten=[
            intro("k15g-0", "Prüfungsschema",
                  "**AGL:** § 14 Abs. 5 S. 1 MarkenG (Unterlassung) i.V.m. § 14 Abs. 2 S. 1 Nr. 1–3 MarkenG; § 14 Abs. 6 MarkenG (Schadensersatz); § 18 MarkenG (Vernichtung, Rückruf); § 19 MarkenG (Auskunft); geschäftliche Bezeichnung § 15 Abs. 2, 4, 5 MarkenG; Unionsmarke Art. 9 Abs. 2 UMV, Folgeansprüche § 119 Nr. 2 MarkenG\n\n"
                  "**A · Zulässigkeit der Klage**\n"
                  "**V1 Zuständigkeit** – LG ohne Rücksicht auf den Streitwert ausschließlich (§ 140 Abs. 1 MarkenG), Konzentration (§ 140 Abs. 2 MarkenG); Unionsmarke: Unionsmarkengericht (§ 122 Abs. 1 MarkenG); örtlich § 32 ZPO; Anwaltszwang § 78 ZPO\n\n"
                  "**B · Begründetheit**\n"
                  "**V2 Geschützte Marke, Aktivlegitimation** – Schutz nach § 4 MarkenG (Eintragung, Verkehrsgeltung, notorische Bekanntheit); Inhaber, Vermutung § 28 Abs. 1 MarkenG; Lizenznehmer nur mit Zustimmung (§ 30 Abs. 3 MarkenG)\n"
                  "**V3 Benutzung im geschäftlichen Verkehr** – § 14 Abs. 2 S. 1 MarkenG\n"
                  "**V4 Ohne Zustimmung des Inhabers** – § 14 Abs. 2 S. 1 MarkenG\n"
                  "**V5 Benutzung für Waren/DL, markenmäßig** – § 14 Abs. 2 S. 1, Abs. 3 MarkenG (Beispiele)\n"
                  "**V6 Kollisionstatbestand** – Nr. 1 Doppelidentität · Nr. 2 Verwechslungsgefahr · Nr. 3 bekannte Marke (Kapitel k15c)\n"
                  "**V7 Keine Schranke, keine Einwendung** – § 23 MarkenG (Name, beschreibende Angabe, Bestimmungshinweis; anständige Gepflogenheiten § 23 Abs. 2 MarkenG), § 24 MarkenG (Erschöpfung), § 25 MarkenG (Nichtbenutzung auf Einrede, § 25 Abs. 2), § 21 MarkenG (Verwirkung), § 20 MarkenG (Verjährung nach BGB)\n"
                  "**V8 Anspruchsspezifisch** – Unterlassung: Wiederholungs- oder Erstbegehungsgefahr (§ 14 Abs. 5 S. 1, 2 MarkenG); Schadensersatz: Vorsatz oder Fahrlässigkeit (§ 14 Abs. 6 S. 1 MarkenG), Berechnung über Verletzergewinn (S. 2) oder Lizenzanalogie (S. 3); Vernichtung und Rückruf (§ 18 Abs. 1, 2 MarkenG), nicht bei Unverhältnismäßigkeit (§ 18 Abs. 3 MarkenG); Auskunft (§ 19 Abs. 1 MarkenG), gegen Dritte (§ 19 Abs. 2 MarkenG); Haftung des Betriebsinhabers (§ 14 Abs. 7 MarkenG)\n\n"
                  "**⇒ Rechtsfolge:** Verurteilung zu Unterlassung, Auskunft, Schadensersatz (dem Grunde nach), Vernichtung; einstweilige Verfügung ohne Darlegung der Dringlichkeit (§ 140 Abs. 3 MarkenG); Patentanwaltskosten nach § 140 Abs. 4 MarkenG, soweit notwendig (BGH Kosten des Patentanwalts VII).\n\n"
                  "**Klausurfallen:** Modellbezeichnungen neben einer Herstellermarke können markenmäßig benutzt sein. Unterlassung ist verschuldensunabhängig, Schadensersatz nicht. Unionsmarke: Verbot aus Art. 9 UMV, Schadensersatz und Auskunft über § 119 Nr. 2 MarkenG.\n\n"
                  "**In den Klausuren:** NS II/2022 (EMOTION rims: Verletzung einer Unionsmarke, Beratungsschreiben), NS I/2023 (gelbe Kaffeemühlen: Benutzungsmarke), NS I/2020 (ACRIGLASS® – das Original aus Italien), NS I/2021 (rahi/RAMI, Beratung), NS II/2024 (Esro.Med: Nichtbenutzungseinrede nach § 25 MarkenG).",
                  concepts=["unterlassungsanspruch", "schadensersatz", "vernichtung_auskunft", "geschaeftlicher_verkehr", "markenmaessige_benutzung", "schranke_23", "erschoepfung"],
                  norms=["§ 14 MarkenG", "§ 15 MarkenG", "§ 18 MarkenG", "§ 19 MarkenG", "§ 23 MarkenG", "§ 24 MarkenG", "§ 25 MarkenG", "§ 140 MarkenG", "§ 119 MarkenG", "Art. 10 MarkenRL"],
                  cases=["bgh_kosten_patentanwalt_vii"], abschnitt="Normenkette"),
            intro("k15g-1", "Definitionen",
                  "**Benutzung im geschäftlichen Verkehr:** Benutzung im Zusammenhang mit einer auf einen wirtschaftlichen Vorteil gerichteten kommerziellen Tätigkeit und nicht im privaten Bereich (EuGH-Rspr., Arsenal).\n"
                  "**Markenmäßige Benutzung:** Benutzung, die die Funktionen der Marke, insbesondere die Herkunftsfunktion, beeinträchtigt oder beeinträchtigen kann (EuGH Arsenal); eine bloße Firmenbezeichnung ist erst dann Benutzung für Waren, wenn der Verkehr eine Verbindung zu den Waren herstellt (EuGH Céline).\n"
                  "**Wiederholungsgefahr:** wird durch eine begangene Verletzung vermutet; sie entfällt in der Regel nur durch eine strafbewehrte Unterlassungserklärung (Rechtsprechung).\n"
                  "**Erstbegehungsgefahr:** ernsthafte und greifbare Anhaltspunkte dafür, dass eine Verletzung erstmals droht (§ 14 Abs. 5 S. 2 MarkenG, Rechtsprechung).\n"
                  "**Dreifache Schadensberechnung:** konkreter Schaden, Herausgabe des Verletzergewinns (§ 14 Abs. 6 S. 2 MarkenG) oder angemessene Lizenzgebühr (§ 14 Abs. 6 S. 3 MarkenG).\n"
                  "**Erschöpfung:** Der Inhaber kann die Benutzung für Waren nicht untersagen, die unter der Marke von ihm oder mit seiner Zustimmung im EWR in den Verkehr gebracht worden sind, außer aus berechtigten Gründen (§ 24 Abs. 1, 2 MarkenG).\n"
                  "**Verkehrsgeltung (§ 4 Nr. 2 MarkenG):** Das Zeichen wird innerhalb der beteiligten Verkehrskreise als Herkunftshinweis eines bestimmten Unternehmens verstanden; Schutz ohne Eintragung.",
                  concepts=["geschaeftlicher_verkehr", "markenmaessige_benutzung", "unterlassungsanspruch", "schadensersatz", "lizenzanalogie", "erschoepfung", "verkehrsgeltung"],
                  norms=["§ 14 MarkenG", "§ 24 MarkenG", "§ 4 MarkenG"], cases=["eugh_arsenal", "eugh_celine"], abschnitt="Definitionen"),
            mc("k15g-2", "Das zuständige Gericht",
               "Der Streitwert einer Unterlassungsklage aus einer deutschen Marke beträgt 3.000 €. Welches Gericht ist zuständig?",
               ["Das Amtsgericht wegen des geringen Streitwerts",
                "Das LG ausschließlich, ohne Rücksicht auf den Streitwert (§ 140 Abs. 1 MarkenG), ggf. ein Konzentrationsgericht (§ 140 Abs. 2 MarkenG)",
                "Das BPatG",
                "Das DPMA"], 1,
               ["**§ 140 Abs. 1 MarkenG.** Kennzeichenstreitsachen gehören streitwertunabhängig ausschließlich vor die Landgerichte; die Länder haben sie bei bestimmten Landgerichten konzentriert (§ 140 Abs. 2 MarkenG). Vor dem LG gilt Anwaltszwang (§ 78 ZPO)."],
               merke="Kennzeichenstreitsache: § 140 Abs. 1 MarkenG – LG, ausschließlich, streitwertunabhängig.",
               level=1, concepts=["unterlassungsanspruch"], norms=["§ 140 MarkenG"], abschnitt=N),
            fall("k15g-3", "Nur eine Modellbezeichnung? (NS II/2022)",
                 "K vertreibt Autofelgen mit dem Zeichen „Emotion FANCY BLACK“; auf der Nabe steht seine Herstellerkennzeichnung „CCT“. Er meint, „Emotion“ werde nur als Modellbezeichnung verstanden, nicht als Marke.",
                 "Ist eine markenmäßige Benutzung deshalb ausgeschlossen?", False,
                 ["**Nein!** Ein Produkt kann neben der Herstellermarke weitere Kennzeichen tragen; der Verkehr ist an Zweitmarken und Modellnamen gewöhnt, die ebenfalls auf die Herkunft hinweisen. Entscheidend ist, ob das Zeichen als Herkunftshinweis verstanden werden kann (EuGH Arsenal). Gegen eine rein beschreibende Verwendung („electric motion“) spricht der Fantasiegehalt von „Emotion“ für Felgen (§ 23 Abs. 1 Nr. 2 MarkenG prüfen)."],
                 merke="Herstellermarke daneben schließt markenmäßige Benutzung nicht aus.",
                 level=2, concepts=["markenmaessige_benutzung"], norms=["§ 14 Abs. 2 MarkenG", "§ 23 MarkenG"], cases=["eugh_arsenal"],
                 step="step:schema_markenverletzung.3.4", abschnitt=N),
            fall("k15g-4", "Unterlassung ohne Verschulden",
                 "Ein Händler verkauft gutgläubig Taschen mit einem verwechselbaren Zeichen, die er von einem seriösen Großhändler bezogen hat. Er konnte die Markenverletzung nicht erkennen.",
                 "Kann der Markeninhaber Unterlassung verlangen?", True,
                 ["**Ja!** Der Unterlassungsanspruch (§ 14 Abs. 5 S. 1 MarkenG) setzt nur eine rechtswidrige Verletzung und Wiederholungsgefahr voraus, kein Verschulden. Schadensersatz verlangt dagegen Vorsatz oder Fahrlässigkeit (§ 14 Abs. 6 S. 1 MarkenG); an die Sorgfalt im Handel stellt die Rechtsprechung allerdings strenge Anforderungen."],
                 merke="Unterlassung verschuldensunabhängig (§ 14 Abs. 5), Schadensersatz mit Verschulden (§ 14 Abs. 6 MarkenG).",
                 level=1, concepts=["unterlassungsanspruch", "schadensersatz"], norms=["§ 14 Abs. 5 MarkenG", "§ 14 Abs. 6 MarkenG"], step="step:schema_markenverletzung.5", abschnitt=N),
            fall("k15g-5", "Originalware aus Frankreich",
                 "Ein Händler kauft in Frankreich Originalparfums, die der Markeninhaber dort selbst in den Verkehr gebracht hat, und verkauft sie unverändert in Deutschland unter der Marke.",
                 "Kann der Markeninhaber den Verkauf untersagen?", False,
                 ["**Nein!** Das Markenrecht ist erschöpft, wenn die Waren unter der Marke vom Inhaber oder mit seiner Zustimmung im EWR in den Verkehr gebracht worden sind (§ 24 Abs. 1 MarkenG). Berechtigte Gründe wie eine Veränderung der Ware (§ 24 Abs. 2 MarkenG) liegen nicht vor."],
                 merke="Erschöpfung: Inverkehrbringen im EWR durch den Inhaber oder mit Zustimmung (§ 24 Abs. 1 MarkenG).",
                 level=1, concepts=["erschoepfung", "berechtigte_gruende"], norms=["§ 24 MarkenG"], step="step:schema_markenverletzung.4.2", abschnitt=N),
            fall("k15g-6", "Firmenname im Briefkopf (NS II/2024)",
                 "B klagt aus seiner seit 1998 eingetragenen Marke „EsroMedi“ (pharmazeutische Erzeugnisse). Belegt sind nur Rechnungen und Visitenkarten mit dem Briefkopf „EsroMedi Medizinproduktehandel“. Die Beklagte erhebt die Einrede der Nichtbenutzung.",
                 "Scheitert die Klage an der Einrede?", True,
                 ["**Ja!** Auf Einrede muss der Kläger die Benutzung in den letzten fünf Jahren vor Klageerhebung nachweisen (§ 25 Abs. 2 S. 1 MarkenG). Ein Firmenname im Briefkopf ist firmenmäßige, keine markenmäßige Benutzung für Waren (EuGH Céline); Medizinprodukte sind zudem keine pharmazeutischen Erzeugnisse."],
                 merke="Verletzungsklage: Einrede § 25 Abs. 2 MarkenG; Firmenbenutzung ≠ Markenbenutzung.",
                 level=2, concepts=["nichtbenutzungseinrede", "firmenmaessiger_gebrauch"], norms=["§ 25 MarkenG", "§ 26 MarkenG"], cases=["eugh_celine"],
                 step="step:schema_markenverletzung.4.3", abschnitt=N),
            mc("k15g-7", "Ansprüche aus der Unionsmarke (NS II/2022)",
               "M ist Inhaber der Unionsmarke „EMOTION rims“ und verlangt von K in Deutschland Unterlassung, Auskunft und Schadensersatz. Auf welche Normen stützt er die Ansprüche?",
               ["Alle Ansprüche auf § 14 MarkenG unmittelbar",
                "Unterlassung auf Art. 9 Abs. 2 UMV (Verbot durch das Unionsmarkengericht, Art. 130 UMV); Auskunft und Schadensersatz auf § 119 Nr. 2 MarkenG i.V.m. § 19, § 14 Abs. 6 MarkenG",
                "Alle Ansprüche nur auf die UMV",
                "Auf § 15 MarkenG"], 1,
               ["**Art. 9 Abs. 2 UMV + § 119 Nr. 2 MarkenG.** Das Verbotsrecht folgt aus der UMV; dem Inhaber einer Unionsmarke stehen daneben Schadensersatz (§ 14 Abs. 6, 7 MarkenG), Vernichtung (§ 18 MarkenG) und Auskunft (§ 19 MarkenG) zu (§ 119 Nr. 2 MarkenG). Zuständig ist das LG als Unionsmarkengericht (§ 122 Abs. 1 MarkenG)."],
               merke="Unionsmarke: Verbot Art. 9 UMV · Folgeansprüche § 119 Nr. 2 MarkenG · Gericht § 122 MarkenG.",
               level=2, concepts=["unionsmarke", "unionsmarkengericht"], norms=["§ 119 MarkenG", "§ 122 MarkenG"], abschnitt=N),
            *fallkette("k15g-8", "Die gelbe Kaffeemühle (nach NS I/2023)",
                       "Ein Familienunternehmen vertreibt seit Jahren Kaffeemühlen in einem besonderen Gelbton; nach seinen Angaben versteht der Verkehr die Farbe als Hinweis auf das Unternehmen. Ein eingetragenes Schutzrecht besteht nicht. Seit wenigen Wochen färbt ein Wettbewerber seine Kaffeemühlen im selben Ton.",
                       [frage("V2: Kann ohne Eintragung Markenschutz an der Farbe bestehen?", True,
                              ["**Ja!** Markenschutz entsteht auch durch Benutzung, soweit das Zeichen innerhalb beteiligter Verkehrskreise als Marke Verkehrsgeltung erworben hat (§ 4 Nr. 2 MarkenG). Auch eine Farbe ist markenfähig (§ 3 Abs. 1 MarkenG)."],
                              merke="Benutzungsmarke: § 4 Nr. 2 MarkenG (Verkehrsgeltung).",
                              norms=["§ 4 MarkenG", "§ 3 MarkenG"], concepts=["verkehrsgeltung", "farbmarke"]),
                        frage("V2: Genügt es, dass einige Stammkunden die Farbe dem Unternehmen zuordnen?", False,
                              ["**Nein!** Verkehrsgeltung verlangt, dass ein erheblicher Teil der beteiligten Verkehrskreise das Zeichen als Herkunftshinweis versteht. Bei Farben, die von Haus aus nicht unterscheidungskräftig sind, legt die Rechtsprechung einen hohen Zuordnungsgrad an; der Nachweis gelingt meist nur durch eine Verkehrsbefragung."],
                              merke="Farbe als Benutzungsmarke: hoher Zuordnungsgrad, Verkehrsbefragung.",
                              concepts=["verkehrsgeltung"]),
                        frage("V6/V8: Kann das Unternehmen bei nachgewiesener Verkehrsgeltung Unterlassung verlangen?", True,
                              ["**Ja!** Auch die Benutzungsmarke gewährt das ausschließliche Recht (§ 14 Abs. 1 MarkenG). Identischer Farbton für identische Waren: § 14 Abs. 2 S. 1 Nr. 1 MarkenG, jedenfalls Nr. 2. Die begangene Verletzung begründet Wiederholungsgefahr (§ 14 Abs. 5 S. 1 MarkenG); Klage vor dem LG (§ 140 Abs. 1 MarkenG)."],
                              merke="§ 14 Abs. 1 MarkenG gilt für alle Marken nach § 4 MarkenG.",
                              norms=["§ 14 MarkenG", "§ 140 MarkenG"], concepts=["unterlassungsanspruch"], step="step:schema_markenverletzung.5"),
                        frage("V8: Wie kann der Schaden berechnet werden?", 2,
                              ["**Dreifach:** konkreter Schaden, Verletzergewinn (§ 14 Abs. 6 S. 2 MarkenG) oder Lizenzanalogie (§ 14 Abs. 6 S. 3 MarkenG); Voraussetzung ist Verschulden (§ 14 Abs. 6 S. 1 MarkenG). Zur Bezifferung dient der Auskunftsanspruch (§ 19 MarkenG; § 242 BGB)."],
                              optionen=["Nur als konkret entgangener Gewinn", "Nur pauschal nach dem Streitwert", "Konkreter Schaden, Verletzergewinn oder Lizenzanalogie (§ 14 Abs. 6 S. 2, 3 MarkenG)", "Gar nicht, weil die Marke nicht eingetragen ist"],
                              merke="Schaden: § 14 Abs. 6 S. 1–3 MarkenG + Auskunft § 19 MarkenG.",
                              norms=["§ 14 Abs. 6 MarkenG", "§ 19 MarkenG"], concepts=["schadensersatz", "lizenzanalogie"], step="step:schema_markenverletzung.6.1"),
                        ], abschnitt=K, level=2),
        ]),
        # ==============================================================
        dict(id="k15h", titel="§§ 64, 66, 83 MarkenG: Erinnerung, Beschwerde, Rechtsbeschwerde", einheiten=[
            intro("k15h-0", "Prüfungsschema",
                  "**AGL:** Beschwerde § 66 Abs. 1 S. 1 MarkenG; Erinnerung § 64 Abs. 1 MarkenG; Rechtsbeschwerde § 83 Abs. 1 MarkenG\n\n"
                  "**0 · Wirksamkeit**\n"
                  "**V0 Gebühr** – Beschwerde 200 € (Nr. 401 300), in Verfalls- und Nichtigkeitsverfahren 500 € (Nr. 401 100), gegen Kostenfestsetzung 50 € (Nr. 401 200 Anlage PatKostG); Erinnerung 150 € (Nr. 333 000); innerhalb der Rechtsbehelfsfrist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt der Rechtsbehelf als nicht eingelegt (§ 6 Abs. 2 PatKostG); Zahlungstag § 2 PatKostZV\n\n"
                  "**A · Zulässigkeit der Beschwerde**\n"
                  "**V1 Statthaftigkeit** – Beschluss einer Markenstelle oder Markenabteilung (§ 66 Abs. 1 S. 1 MarkenG); bei Beschlüssen des gehobenen Dienstes wahlweise Erinnerung (§ 64 Abs. 1, 6 MarkenG)\n"
                  "**V2 Beschwerdeberechtigung, Beschwer** – Beteiligter des Verfahrens vor dem DPMA (§ 66 Abs. 1 S. 2 MarkenG); Beschluss bleibt hinter dem Antrag zurück\n"
                  "**V3 Beteiligten- und Prozessfähigkeit, Vertretung** – § 82 Abs. 1 MarkenG i.V.m. § 50 ZPO, § 51 ZPO; kein Anwaltszwang (§ 81 Abs. 1 MarkenG), aber § 96 Abs. 1 MarkenG\n"
                  "**V4 Form und Ort** – schriftlich beim DPMA (§ 66 Abs. 2 MarkenG), nicht beim BPatG; elektronisch nur nach § 95a MarkenG i.V.m. § 130a ZPO\n"
                  "**V5 Frist** – ein Monat nach Zustellung (§ 66 Abs. 2 MarkenG) · Berechnung § 82 Abs. 1 MarkenG i.V.m. § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 222 Abs. 2 ZPO; Zustellung nach VwZG (§ 94 Abs. 1 MarkenG): Einschreiben am vierten Tag nach Aufgabe (§ 4 Abs. 2 S. 2 VwZG), Abholfach am dritten Tag (§ 94 Abs. 1 Nr. 3 MarkenG); bei Versäumung § 91 MarkenG\n"
                  "**Abhilfe:** nur ohne Gegenbeteiligten (§ 66 Abs. 5 S. 1, 2 MarkenG); sonst Vorlage an das BPatG binnen eines Monats (§ 66 Abs. 5 S. 4 MarkenG). Aufschiebende Wirkung § 66 Abs. 1 S. 3 MarkenG.\n\n"
                  "**B · Begründetheit:** Der angefochtene Beschluss ist rechtswidrig; BPatG entscheidet selbst oder verweist zurück (§ 70 Abs. 3 MarkenG); Rückzahlung der Beschwerdegebühr § 71 Abs. 3 MarkenG.\n\n"
                  "**Erinnerung:** ein Monat nach Zustellung beim DPMA (§ 64 Abs. 2 MarkenG), Abhilfe nur ohne Gegenbeteiligten (§ 64 Abs. 3 MarkenG), Entscheidung durch ein Mitglied des DPMA (§ 64 Abs. 4 MarkenG); Durchgriffsbeschwerde nach sechs bzw. zehn Monaten (§ 66 Abs. 3 MarkenG).\n"
                  "**Rechtsbeschwerde:** gegen Beschwerdebeschlüsse des BPatG, wenn zugelassen (§ 83 Abs. 1, 2 MarkenG) oder zulassungsfrei bei den Verfahrensmängeln des § 83 Abs. 3 Nr. 1–6 MarkenG; ein Monat beim BGH (§ 85 Abs. 1 MarkenG), Begründung ein Monat (§ 85 Abs. 3 MarkenG), BGH-Anwalt (§ 85 Abs. 5 MarkenG).\n\n"
                  "**⇒ Tenor:** „Die Beschwerde gilt als nicht eingelegt“ (Gebühr fehlt) · „wird als unzulässig verworfen“ · „wird zurückgewiesen“ · „Der Beschluss … wird aufgehoben“.\n\n"
                  "**In den Klausuren:** NS III/2018 (Abholfach), NS I/2019 (Frist und 150 € statt 200 €), NS III/2020 (E-Mail ans BPatG), NS II/2021 (Amtsliste), NS I/2022 (Beschwerde der obsiegenden Partei), NS III/2022 (Teilanfechtung), NS III/2023 (Unterzeichnung „iV“, Zurückverweisung), NS III/2024 (gelöschte UG), NS III/2025 (gehobener oder höherer Dienst).",
                  concepts=["beschwerde", "erinnerung", "rechtsbeschwerde", "beschwer", "zustellung", "zahlungstag"],
                  norms=["§ 66 MarkenG", "§ 64 MarkenG", "§ 83 MarkenG", "§ 85 MarkenG", "§ 70 MarkenG", "§ 82 MarkenG", "§ 94 MarkenG", "§ 6 PatKostG", "Anlage PatKostG"],
                  abschnitt="Normenkette"),
            intro("k15h-1", "Definitionen",
                  "**Statthaftigkeit:** Der Rechtsbehelf ist gegen diese Art von Entscheidung gesetzlich vorgesehen (§ 66 Abs. 1 S. 1, § 64 Abs. 1, § 83 Abs. 1 MarkenG); Entscheidungen des BPatG sind nur anfechtbar, soweit das Gesetz es zulässt (§ 82 Abs. 2 MarkenG).\n"
                  "**Beschwer:** Der angefochtene Beschluss bleibt hinter dem zurück, was der Beschwerdeführer beantragt hat (formelle Beschwer); wer voll obsiegt, ist nicht beschwert (Rechtsprechung).\n"
                  "**Abhilfe:** Die Stelle, deren Beschluss angefochten wird, hebt ihn selbst auf, wenn sie den Rechtsbehelf für begründet hält; nicht im mehrseitigen Verfahren (§ 64 Abs. 3, § 66 Abs. 5 MarkenG).\n"
                  "**Zustellung:** förmliche Bekanntgabe eines Schriftstücks in der gesetzlichen Form; vor dem DPMA nach dem VwZG mit den Maßgaben des § 94 Abs. 1 MarkenG, vor dem BPatG nach der ZPO (§ 94 Abs. 2 MarkenG).\n"
                  "**Durchgriffsbeschwerde:** Beschwerde unmittelbar gegen den Erstbeschluss, wenn über eine Erinnerung nicht rechtzeitig entschieden wird (§ 66 Abs. 3 MarkenG).\n"
                  "**Zulassungsfreie Rechtsbeschwerde:** Rechtsbeschwerde ohne Zulassung, beschränkt auf die Rüge schwerer Verfahrensmängel wie Besetzung, Befangenheit, Versagung rechtlichen Gehörs, Vertretungsmangel, Öffentlichkeit, fehlende Gründe (§ 83 Abs. 3 MarkenG).",
                  concepts=["beschwer", "beschwerde", "erinnerung", "rechtsbeschwerde", "zustellung"],
                  norms=["§ 64 MarkenG", "§ 66 MarkenG", "§ 83 MarkenG", "§ 94 MarkenG", "§ 82 MarkenG"], abschnitt="Definitionen"),
            fall("k15h-2", "Beschluss im Abholfach (NS III/2018)",
                 "Der Beschluss wird am Dienstag, 10. Juni 2014, in das Abholfach des Vertreters beim DPMA gelegt; der Vertreter entnimmt ihn am 11. Juni. Die Beschwerde geht am Montag, 14. Juli 2014, ein.",
                 "Ist die Beschwerde rechtzeitig?", True,
                 ["**Ja!** Die Zustellung durch Niederlegung im Abholfach gilt am dritten Tag nach der Niederlegung als bewirkt (§ 94 Abs. 1 Nr. 3 MarkenG), hier am 13. Juni 2014; die frühere Entnahme ändert die Fiktion nicht. Die Monatsfrist (§ 66 Abs. 2 MarkenG) endet am Sonntag, 13. Juli, und verschiebt sich auf Montag, 14. Juli 2014 (§ 82 Abs. 1 MarkenG i.V.m. § 222 Abs. 2 ZPO)."],
                 merke="Abholfach: dritter Tag (§ 94 Abs. 1 Nr. 3 MarkenG) · Frist § 66 Abs. 2 · Verschiebung § 222 Abs. 2 ZPO.",
                 level=2, concepts=["zustellung", "fristberechnung"], norms=["§ 94 MarkenG", "§ 66 Abs. 2 MarkenG"], step="step:schema_zulaessigkeit_beschwerde.5.1", abschnitt=N),
            fall("k15h-3", "150 Euro statt 200 Euro",
                 "Gegen einen Widerspruchsbeschluss legt die Widersprechende fristgerecht Beschwerde ein, zahlt aber innerhalb der Beschwerdefrist nur 150 €.",
                 "Gilt die Beschwerde als nicht eingelegt?", True,
                 ["**Ja!** Die Beschwerdegebühr beträgt in Widerspruchssachen 200 € (Nr. 401 300 Anlage PatKostG) und ist innerhalb der Beschwerdefrist zu zahlen (§ 6 Abs. 1 S. 1 PatKostG). Eine unvollständige Zahlung steht der Nichtzahlung gleich: Die Beschwerde gilt als nicht eingelegt (§ 6 Abs. 2 PatKostG). Tenor: Feststellung, keine Verwerfung."],
                 merke="Teilzahlung = Nichtzahlung (§ 6 Abs. 2 PatKostG: „nicht vollständig“).",
                 level=1, concepts=["zahlungstag"], norms=["§ 6 PatKostG", "Anlage PatKostG"], step="step:schema_zulaessigkeit_beschwerde.6", abschnitt=N),
            fall("k15h-4", "Beschwerde per E-Mail ans BPatG (NS III/2020)",
                 "L scannt seine unterschriebene Beschwerde ein und mailt sie am vorletzten Tag der Frist an die zentrale Adresse des BPatG. Das BPatG leitet sie per Dienstpost an das DPMA weiter, wo sie einen Tag nach Fristablauf eingeht.",
                 "Ist die Frist gewahrt?", False,
                 ["**Nein!** Die Beschwerde ist beim DPMA einzulegen (§ 66 Abs. 2 MarkenG); maßgeblich ist der Eingang dort. Zudem wahrt eine einfache E-Mail mit eingescannter Unterschrift die Schriftform nicht; elektronisch nur nach § 95a MarkenG i.V.m. § 130a ZPO. Bleibt nur Wiedereinsetzung (§ 91 MarkenG)."],
                 merke="Beschwerde: schriftlich, beim DPMA (§ 66 Abs. 2 MarkenG), elektronisch nur § 95a MarkenG.",
                 level=2, concepts=["beschwerde"], norms=["§ 66 Abs. 2 MarkenG", "§ 95a MarkenG"], step="step:schema_zulaessigkeit_beschwerde.4", abschnitt=N),
            mc("k15h-5", "Erinnerung oder Beschwerde? (NS III/2025)",
               "Über die Widersprüche entscheidet ein Prüfer, der Beamter des höheren Dienstes ist. Welcher Rechtsbehelf ist statthaft?",
               ["Nur die Erinnerung (§ 64 MarkenG)", "Nur die Beschwerde zum BPatG (§ 66 Abs. 1 MarkenG)", "Wahlweise Erinnerung oder Beschwerde", "Unmittelbar die Rechtsbeschwerde"], 1,
               ["**Nur die Beschwerde.** Die Erinnerung findet nur gegen Beschlüsse statt, die ein Beamter des gehobenen Dienstes oder ein vergleichbarer Angestellter erlassen hat (§ 64 Abs. 1 MarkenG); nur dann besteht die Wahl (§ 64 Abs. 6 MarkenG). Gegen Beschlüsse des höheren Dienstes ist allein die Beschwerde statthaft (§ 66 Abs. 1 S. 1 MarkenG)."],
               merke="Gehobener Dienst: Erinnerung oder Beschwerde; höherer Dienst: nur Beschwerde.",
               level=1, concepts=["erinnerung", "beschwerde"], norms=["§ 64 Abs. 1 MarkenG", "§ 66 Abs. 1 MarkenG"], step="step:schema_zulaessigkeit_beschwerde.1", abschnitt=N),
            fall("k15h-6", "Die Beschwerde des Siegers (NS I/2022)",
                 "Die Markenstelle hat den Widerspruch zurückgewiesen. Die Inhaberin der angegriffenen Marke legt trotzdem „Beschwerde“ ein, um die Einrede der Nichtbenutzung zu erheben.",
                 "Ist ihre Beschwerde zulässig?", False,
                 ["**Nein!** Es fehlt die Beschwer: Der Beschluss gibt ihr in vollem Umfang recht. Das Schreiben ist als Verfahrenserklärung im Beschwerdeverfahren der Gegenseite auszulegen; die Einrede kann sie dort jederzeit erheben (§ 43 Abs. 1 MarkenG)."],
                 merke="Ohne Beschwer keine Beschwerde; Erklärung in Schriftsatz umdeuten.",
                 level=1, concepts=["beschwer"], norms=["§ 66 Abs. 1 MarkenG"], step="step:schema_zulaessigkeit_beschwerde.2", abschnitt=N),
            mc("k15h-7", "Zulassungsfreie Rechtsbeschwerde",
               "Das BPatG hat die Rechtsbeschwerde nicht zugelassen. Welche Rüge eröffnet die Rechtsbeschwerde trotzdem?",
               ["Das BPatG hat die Verwechslungsgefahr falsch beurteilt",
                "Die Sache habe grundsätzliche Bedeutung",
                "Einem Beteiligten wurde das rechtliche Gehör versagt (§ 83 Abs. 3 Nr. 3 MarkenG)",
                "Das BPatG hätte die Rechtsbeschwerde zulassen müssen"], 2,
               ["**§ 83 Abs. 3 Nr. 3 MarkenG.** Zulassungsfrei sind nur die Verfahrensrügen des § 83 Abs. 3 MarkenG. Grundsätzliche Bedeutung ist ein Zulassungsgrund (§ 83 Abs. 2 Nr. 1 MarkenG); die unterlassene Zulassung ist kein Begründungsmangel nach Nr. 6 (BGH Silver Horse/Power Horse)."],
               merke="Zugelassen § 83 Abs. 1, 2 · zulassungsfrei § 83 Abs. 3 Nr. 1–6 MarkenG · Frist § 85 Abs. 1 MarkenG.",
               level=2, concepts=["rechtsbeschwerde"], norms=["§ 83 MarkenG", "§ 85 MarkenG"], cases=["bgh_silver_horse"], abschnitt=N),
            fall("k15h-8", "Abhilfe im Widerspruchsverfahren?",
                 "Gegen die Löschung ihrer Marke auf Widerspruch legt die Markeninhaberin Beschwerde ein. Die Markenstelle hält die Beschwerde für begründet und möchte ihren Beschluss selbst aufheben.",
                 "Darf die Markenstelle abhelfen?", False,
                 ["**Nein!** Abhilfe ist ausgeschlossen, wenn dem Beschwerdeführer ein anderer Beteiligter gegenübersteht (§ 66 Abs. 5 S. 2 MarkenG); im Widerspruchsverfahren ist das die Widersprechende. Die Beschwerde ist dem BPatG unverzüglich vorzulegen (§ 66 Abs. 5 S. 5 MarkenG)."],
                 merke="Abhilfe nur im einseitigen Verfahren (§ 64 Abs. 3, § 66 Abs. 5 MarkenG).",
                 level=1, concepts=["beschwerde"], norms=["§ 66 Abs. 5 MarkenG"], abschnitt=N),
            *fallkette("k15h-9", "MICHEL LEON gegen JEAN LEON (nach NS I/2019)",
                       "Die Markenstelle (Beamter des höheren Dienstes) weist den Widerspruch aus der Unionsmarke „JEAN LEON“ zurück; der Beschluss wird am Freitag, 15. Juni 2018, zugestellt. Die Beschwerde der Widersprechenden geht per einfachem Brief am Dienstag, 17. Juli 2018, beim DPMA ein; am 20. Juli 2018 gehen 150 € „Beschwerdegebühr“ ein.",
                       [frage("V0: Ist die Beschwerdegebühr wirksam gezahlt?", False,
                              ["**Nein!** Geschuldet sind 200 € (Nr. 401 300 Anlage PatKostG) innerhalb der Beschwerdefrist (§ 6 Abs. 1 S. 1 PatKostG). 150 € am 20. Juli sind weder vollständig noch rechtzeitig; die Beschwerde gilt als nicht eingelegt (§ 6 Abs. 2 PatKostG)."],
                              merke="Gebühr zuerst prüfen: Nr. 401 300 · § 6 Abs. 1 S. 1 · § 6 Abs. 2 PatKostG.",
                              norms=["§ 6 PatKostG", "Anlage PatKostG"], step="step:schema_zulaessigkeit_beschwerde.6"),
                        frage("V1 (hilfsweise): Ist die Beschwerde statthaft?", True,
                              ["**Ja!** Gegen den Beschluss einer Markenstelle findet die Beschwerde zum BPatG statt (§ 66 Abs. 1 S. 1 MarkenG); eine Erinnerung scheidet aus, weil ein Beamter des höheren Dienstes entschieden hat (§ 64 Abs. 1 MarkenG)."],
                              merke="Statthaft: § 66 Abs. 1 S. 1 MarkenG.", norms=["§ 66 Abs. 1 MarkenG"], step="step:schema_zulaessigkeit_beschwerde.1"),
                        frage("V5: Wann endete die Beschwerdefrist?", 1,
                              ["**Montag, 16. Juli 2018.** Ein Monat ab Zustellung am 15. Juni (§ 66 Abs. 2 MarkenG; § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB, § 188 Abs. 2 BGB) ergibt Sonntag, 15. Juli; Verschiebung auf den nächsten Werktag (§ 222 Abs. 2 ZPO). Der Eingang am 17. Juli ist verspätet; maßgeblich ist der Eingang beim DPMA, nicht die Absendung."],
                              optionen=["Sonntag, 15. Juli 2018", "Montag, 16. Juli 2018", "Dienstag, 17. Juli 2018", "Freitag, 20. Juli 2018"],
                              merke="Frist § 66 Abs. 2 MarkenG · § 222 Abs. 1 ZPO, § 188 Abs. 2 BGB · § 222 Abs. 2 ZPO.",
                              norms=["§ 66 Abs. 2 MarkenG", "§ 82 MarkenG"], step="step:schema_zulaessigkeit_beschwerde.5.3"),
                        frage("⇒: Welchen Tenor schlagen Sie vor?", 0,
                              ["**Feststellung, dass die Beschwerde als nicht eingelegt gilt**, weil die Gebühr nicht vollständig gezahlt ist (§ 6 Abs. 2 PatKostG); die gezahlten 150 € werden erstattet (§ 10 Abs. 2 PatKostG). Die Verspätung trägt hilfsweise eine Verwerfung als unzulässig."],
                              optionen=["„Es wird festgestellt, dass die Beschwerde als nicht eingelegt gilt.“", "„Die Beschwerde wird als unbegründet zurückgewiesen.“", "„Der Beschluss der Markenstelle wird aufgehoben.“", "„Die Beschwerde wird an das DPMA zurückverwiesen.“"],
                              merke="Gebühr fehlt ⇒ Feststellungstenor, nicht Verwerfung.",
                              norms=["§ 6 PatKostG", "§ 10 PatKostG"]),
                        ], abschnitt=K, level=2, concepts=["beschwerde"]),
        ]),
        # ==============================================================
        dict(id="k15i", titel="§§ 91, 91a MarkenG: Wiedereinsetzung und Weiterbehandlung", einheiten=[
            intro("k15i-0", "Prüfungsschema",
                  "**AGL:** § 91 Abs. 1 S. 1 MarkenG (Wiedereinsetzung); § 91a Abs. 1 MarkenG (Weiterbehandlung der Anmeldung)\n\n"
                  "**A · Wiedereinsetzung – Zulässigkeit**\n"
                  "**V1 Statthaftigkeit** – Versäumung einer Frist gegenüber DPMA oder BPatG, deren Versäumung nach gesetzlicher Vorschrift einen Rechtsnachteil zur Folge hat (§ 91 Abs. 1 S. 1 MarkenG); ausgeschlossen: Widerspruchsfrist und Frist zur Zahlung der Widerspruchsgebühr (§ 91 Abs. 1 S. 2 MarkenG), Weiterbehandlungsfrist und -gebühr (§ 91a Abs. 3 MarkenG)\n"
                  "**V2 Antrag** – § 91 Abs. 1 S. 1 MarkenG; entbehrlich, wenn die Handlung fristgerecht nachgeholt ist (§ 91 Abs. 4 S. 2 MarkenG)\n"
                  "**V3 Antragsfrist** – zwei Monate nach Wegfall des Hindernisses (§ 91 Abs. 2 MarkenG) · § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · § 193 BGB (vor dem BPatG § 222 Abs. 2 ZPO über § 82 Abs. 1 MarkenG); Ausschlussfrist ein Jahr nach Ablauf der versäumten Frist (§ 91 Abs. 5 MarkenG)\n"
                  "**V4 Nachholung der versäumten Handlung** innerhalb der Antragsfrist (§ 91 Abs. 4 S. 1 MarkenG), einschließlich der Gebühr\n"
                  "**V5 Begründung und Glaubhaftmachung** – Tatsachen angeben, bei Antragstellung oder im Verfahren glaubhaft machen (§ 91 Abs. 3 MarkenG; § 294 ZPO)\n\n"
                  "**B · Begründetheit**\n"
                  "**V6 Ohne Verschulden verhindert** – Maßstab: übliche Sorgfalt eines ordentlichen Beteiligten bzw. Anwalts; Verschulden des Vertreters steht dem der Partei gleich (§ 85 Abs. 2 ZPO entsprechend, vor dem BPatG über § 82 Abs. 1 MarkenG); Fehler von Kanzleikräften entlasten bei ordnungsgemäßer Auswahl, Anweisung und Überwachung\n\n"
                  "**⇒ Rechtsfolge:** Die versäumte Handlung gilt als rechtzeitig; Entscheidung durch die Stelle, die über die nachgeholte Handlung beschließt (§ 91 Abs. 6 MarkenG), unanfechtbar (§ 91 Abs. 7 MarkenG); Weiterbenutzungsrecht gutgläubiger Dritter (§ 91 Abs. 8 MarkenG).\n\n"
                  "**C · Weiterbehandlung (§ 91a MarkenG)**\n"
                  "**V1 Statthaft** – Zurückweisung einer Markenanmeldung nach Versäumung einer vom DPMA bestimmten Frist (§ 91a Abs. 1 MarkenG)\n"
                  "**V2 Antrag und Nachholung** innerhalb eines Monats nach Zustellung der Zurückweisung (§ 91a Abs. 2 MarkenG)\n"
                  "**V3 Gebühr** 100 € (Nr. 333 050 Anlage PatKostG) in derselben Frist (§ 6 Abs. 1 S. 1 PatKostG)\n"
                  "**⇒** Der Zurückweisungsbeschluss wird wirkungslos (§ 91a Abs. 1 MarkenG); keine Verschuldensprüfung; keine Wiedereinsetzung in die Weiterbehandlungsfrist (§ 91a Abs. 3 MarkenG).\n\n"
                  "**In den Klausuren:** NS II/2021 (Amtsliste, verschollene Beschwerdeschrift), NS I/2022 (Überweisung am letzten Tag), NS III/2020 („zunächst vergessen“), NS II/2023 (öffentliche Zustellung).",
                  concepts=["wiedereinsetzung", "weiterbehandlung", "glaubhaftmachung"],
                  norms=["§ 91 MarkenG", "§ 91a MarkenG", "§ 82 MarkenG", "Anlage PatKostG"], abschnitt="Normenkette"),
            intro("k15i-1", "Definitionen",
                  "**Verschulden:** Außerachtlassen der Sorgfalt, die ein gewissenhafter Verfahrensbeteiligter bzw. ein ordentlicher Anwalt vernünftigerweise aufwenden muss; schon leichte Fahrlässigkeit schließt die Wiedereinsetzung aus (Rechtsprechung).\n"
                  "**Wegfall des Hindernisses:** Zeitpunkt, in dem der Beteiligte oder sein Vertreter die Säumnis erkennt oder bei gebotener Sorgfalt hätte erkennen können (Rechtsprechung).\n"
                  "**Vertreterverschulden:** Das Verschulden des Bevollmächtigten steht dem Verschulden der Partei gleich (§ 85 Abs. 2 ZPO).\n"
                  "**Büroversehen:** Fehler einer Kanzleikraft, die dem Anwalt nicht zugerechnet werden, wenn er eine zuverlässige Fristen- und Ausgangskontrolle eingerichtet, das Personal sorgfältig ausgewählt, angewiesen und überwacht hat (Rechtsprechung).\n"
                  "**Glaubhaftmachung:** Nachweis überwiegender Wahrscheinlichkeit; alle Beweismittel einschließlich eidesstattlicher Versicherung (§ 294 Abs. 1 ZPO).\n"
                  "**Weiterbehandlung:** verschuldensunabhängiger Rechtsbehelf des Anmelders gegen die Zurückweisung der Markenanmeldung wegen Versäumung einer Amtsfrist (§ 91a MarkenG).",
                  concepts=["wiedereinsetzung", "weiterbehandlung", "glaubhaftmachung"], norms=["§ 91 MarkenG", "§ 91a MarkenG"], abschnitt="Definitionen"),
            fall("k15i-2", "Wiedereinsetzung in die Widerspruchsfrist?",
                 "Der Widerspruch einer schwer erkrankten Einzelunternehmerin geht einen Tag nach Ablauf der Widerspruchsfrist ein. Sie konnte nachweislich niemanden beauftragen.",
                 "Kann Wiedereinsetzung in die Widerspruchsfrist gewährt werden?", False,
                 ["**Nein!** Wiedereinsetzung ist für die Frist zur Erhebung des Widerspruchs und zur Zahlung der Widerspruchsgebühr ausgeschlossen (§ 91 Abs. 1 S. 2 MarkenG), unabhängig vom Verschulden. Ihr bleibt der Nichtigkeitsantrag wegen älterer Rechte (§ 51 Abs. 1, § 53 MarkenG)."],
                 merke="Widerspruchsfrist: keine Wiedereinsetzung (§ 91 Abs. 1 S. 2 MarkenG) ⇒ § 51 MarkenG.",
                 level=1, concepts=["wiedereinsetzung"], norms=["§ 91 Abs. 1 MarkenG", "§ 51 MarkenG"], step="step:schema_wiedereinsetzung.1", abschnitt=N),
            fall("k15i-3", "Die späte Überweisung (NS I/2022)",
                 "Die Beschwerdefrist endet am 18. März 2020. Die Rechtsanwältin gibt die Überweisung der Beschwerdegebühr am Vormittag des 18. März als einfache Überweisung frei; die Gutschrift erfolgt am 19. März.",
                 "Ist Wiedereinsetzung in die Frist zur Zahlung der Beschwerdegebühr zu gewähren?", False,
                 ["**Nein!** Zahlungstag ist bei Überweisung der Tag der Gutschrift (§ 2 Nr. 1 PatKostZV); die Gebühr ist verspätet. Wiedereinsetzung scheitert am zurechenbaren Verschulden (§ 85 Abs. 2 ZPO): Wer am letzten Tag freigibt, muss ein Zahlungsmittel wählen, das die Gutschrift noch am selben Tag sichert, etwa Echtzeitüberweisung oder SEPA-Mandat (§ 2 Nr. 3 PatKostZV)."],
                 merke="Letzter Tag: SEPA-Mandat (Eingang) oder Echtzeitüberweisung (§ 2 PatKostZV).",
                 level=2, concepts=["wiedereinsetzung", "zahlungstag"], norms=["§ 91 MarkenG"], step="step:schema_wiedereinsetzung.4.2", abschnitt=N),
            fall("k15i-4", "„Zunächst vergessen“ (NS III/2020)",
                 "L hat die Beschwerdefrist versäumt. Sein Anwalt beantragt Wiedereinsetzung mit der Begründung, L habe die Sache „zunächst vergessen“.",
                 "Ist Wiedereinsetzung zu gewähren?", False,
                 ["**Nein!** Vergessen ist Verschulden. Wiedereinsetzung setzt voraus, dass der Beteiligte ohne Verschulden verhindert war (§ 91 Abs. 1 S. 1 MarkenG); die begründenden Tatsachen sind glaubhaft zu machen (§ 91 Abs. 3 MarkenG). Ein vom eigenen Willen abhängiges Versäumnis entschuldigt nicht."],
                 merke="Vergessen, Arbeitsüberlastung, Rechtsirrtum ⇒ verschuldet.",
                 level=1, concepts=["wiedereinsetzung"], norms=["§ 91 MarkenG"], step="step:schema_wiedereinsetzung.4.4", abschnitt=N),
            mc("k15i-5", "Die zwei Fristen des § 91 MarkenG",
               "Welche Fristen gelten für den Wiedereinsetzungsantrag?",
               ["Ein Monat ab Fristablauf",
                "Zwei Monate nach Wegfall des Hindernisses (§ 91 Abs. 2 MarkenG); spätestens ein Jahr nach Ablauf der versäumten Frist (§ 91 Abs. 5 MarkenG)",
                "Zwei Wochen nach Wegfall des Hindernisses wie im Zivilprozess",
                "Drei Monate ab Zustellung des Beschlusses"], 1,
               ["**Zwei Monate · ein Jahr.** Innerhalb der Antragsfrist ist die versäumte Handlung nachzuholen (§ 91 Abs. 4 S. 1 MarkenG). Nach einem Jahr seit Ablauf der versäumten Frist ist Wiedereinsetzung ausgeschlossen (§ 91 Abs. 5 MarkenG). Die Zweiwochenfrist des § 234 ZPO gilt nicht."],
               merke="§ 91 Abs. 2 MarkenG zwei Monate · § 91 Abs. 4 Nachholung · § 91 Abs. 5 ein Jahr.",
               level=1, concepts=["wiedereinsetzung"], norms=["§ 91 Abs. 2 MarkenG", "§ 91 Abs. 5 MarkenG"], step="step:schema_wiedereinsetzung.2", abschnitt=N),
            fall("k15i-6", "Die vergessene Mängelbeseitigung",
                 "Der Anmelder versäumt die vom DPMA gesetzte Frist, das Warenverzeichnis zu konkretisieren; die Anmeldung wird zurückgewiesen. Drei Wochen nach Zustellung beantragt er Weiterbehandlung, reicht das Verzeichnis nach und zahlt 100 €.",
                 "Wird der Zurückweisungsbeschluss wirkungslos?", True,
                 ["**Ja!** Weiterbehandlung ist statthaft, weil eine vom DPMA bestimmte Frist versäumt und die Anmeldung deshalb zurückgewiesen wurde (§ 91a Abs. 1 MarkenG). Antrag und Nachholung erfolgten binnen eines Monats nach Zustellung (§ 91a Abs. 2 MarkenG), die Gebühr von 100 € (Nr. 333 050 Anlage PatKostG) ebenfalls. Auf Verschulden kommt es nicht an."],
                 merke="Weiterbehandlung: Amtsfrist · Zurückweisung · ein Monat · 100 € · kein Verschulden.",
                 level=1, concepts=["weiterbehandlung"], norms=["§ 91a MarkenG", "Anlage PatKostG"], abschnitt=N),
            fall("k15i-7", "Weiterbehandlung bei der Beschwerdefrist?",
                 "Die Widersprechende hat die Beschwerdefrist gegen einen Widerspruchsbeschluss versäumt und beantragt Weiterbehandlung, weil diese ohne Verschuldensprüfung auskommt.",
                 "Ist die Weiterbehandlung statthaft?", False,
                 ["**Nein!** Weiterbehandlung gibt es nur, wenn eine Markenanmeldung nach Versäumung einer vom DPMA bestimmten Frist zurückgewiesen worden ist (§ 91a Abs. 1 MarkenG). Die Beschwerdefrist ist eine gesetzliche Frist; hier hilft nur die Wiedereinsetzung (§ 91 MarkenG)."],
                 merke="Gesetzliche Frist ⇒ § 91 MarkenG; Amtsfrist im Anmeldeverfahren ⇒ § 91a MarkenG.",
                 level=1, concepts=["weiterbehandlung", "wiedereinsetzung"], norms=["§ 91a MarkenG", "§ 91 MarkenG"], abschnitt=N),
            *fallkette("k15i-8", "Die verschwundene Beschwerdeschrift (nach NS II/2021)",
                       "Die Bevollmächtigte unterschreibt am 20.12.2018 Beschwerde und Einzugsermächtigung und gibt beides einer seit Jahren zuverlässigen Fachangestellten zur Post. Fristen werden erst gestrichen, wenn die vom DPMA abgestempelte Amtsliste zurück ist. Die Angestellte streicht die Frist trotz fehlender Beschwerde in der Amtsliste. Am 21.01.2019 fällt das auf; am 24.01.2019 werden Wiedereinsetzung beantragt, Beschwerde eingelegt und die Gebühr gezahlt.",
                       [frage("V1: Ist Wiedereinsetzung in die Beschwerdefrist statthaft?", True,
                              ["**Ja!** Die Beschwerdefrist (§ 66 Abs. 2 MarkenG) ist eine gesetzliche Frist mit Rechtsnachteil; der Ausschluss des § 91 Abs. 1 S. 2 MarkenG betrifft nur die Widerspruchsfrist."],
                              merke="Ausschluss nur Widerspruch und Weiterbehandlung.", norms=["§ 91 Abs. 1 MarkenG"], step="step:schema_wiedereinsetzung.1"),
                        frage("V3: Ist der Antrag vom 24.01.2019 rechtzeitig?", True,
                              ["**Ja!** Das Hindernis entfiel mit Kenntnis am 21.01.2019; die Antragsfrist von zwei Monaten (§ 91 Abs. 2 MarkenG) ist gewahrt, die Jahresfrist (§ 91 Abs. 5 MarkenG) ebenso."],
                              merke="Fristbeginn: Kenntnis oder Kennenmüssen der Säumnis.", norms=["§ 91 Abs. 2 MarkenG"], step="step:schema_wiedereinsetzung.2"),
                        frage("V4: Musste die Beschwerde samt Gebühr innerhalb der Antragsfrist nachgeholt werden?", True,
                              ["**Ja!** Die versäumte Handlung ist innerhalb der Antragsfrist nachzuholen (§ 91 Abs. 4 S. 1 MarkenG); zur Beschwerde gehört die Gebühr (§ 6 Abs. 1 PatKostG). Beides ist am 24.01.2019 geschehen."],
                              merke="Wiedereinsetzung = Antrag + Glaubhaftmachung + Nachholung.", norms=["§ 91 Abs. 4 MarkenG", "§ 6 PatKostG"]),
                        frage("V6: War die Bevollmächtigte ohne Verschulden verhindert?", True,
                              ["**Ja, vertretbar!** Zugerechnet wird nur das Verschulden der Bevollmächtigten selbst (§ 85 Abs. 2 ZPO). Eine Ausgangskontrolle über die abgestempelte Amtsliste, sorgfältige Auswahl und stichprobenartige Überwachung genügen; der eigenmächtige Fehler einer bewährten Fachangestellten ist ein entschuldigtes Büroversehen. Die Tatsachen sind glaubhaft zu machen (§ 91 Abs. 3 MarkenG)."],
                              merke="Büroversehen entschuldigt, wenn Organisation, Auswahl und Kontrolle stimmen.", norms=["§ 91 Abs. 3 MarkenG"], step="step:schema_wiedereinsetzung.4.3"),
                        ], abschnitt=K, level=2, concepts=["wiedereinsetzung"], norms=["§ 91 MarkenG"]),
        ]),
        # ==============================================================
        dict(id="k15j", titel="§§ 63, 71 MarkenG: Kosten", einheiten=[
            intro("k15j-0", "Prüfungsschema",
                  "**AGL:** § 63 Abs. 1 S. 1 MarkenG (DPMA); § 71 Abs. 1 S. 1 MarkenG (BPatG); § 90 Abs. 1 MarkenG (BGH); Kennzeichenstreitsachen § 91 Abs. 1 ZPO mit § 140 Abs. 4 MarkenG\n\n"
                  "**V1 Mehrseitiges Verfahren** – mehrere Beteiligte (§ 63 Abs. 1 S. 1, § 71 Abs. 1 S. 1 MarkenG)\n"
                  "**V2 Billigkeit** – Grundsatz: jeder trägt seine Kosten selbst (§ 63 Abs. 1 S. 3, § 71 Abs. 1 S. 2 MarkenG); Auferlegung nur bei besonderen Umständen, etwa Verfahren in erkennbar aussichtsloser Lage oder Verletzung prozessualer Sorgfalt\n"
                  "**V3 Auch bei Rücknahme, Verzicht oder Nichtverlängerung** – § 63 Abs. 1 S. 2, § 71 Abs. 4 MarkenG, nach denselben Billigkeitsmaßstäben\n"
                  "**V4 Erstattungsfähige Kosten** – zur zweckentsprechenden Wahrung der Ansprüche und Rechte notwendig (§ 63 Abs. 1 S. 1 MarkenG); Gegenstandswert (§ 63 Abs. 2 MarkenG); Festsetzung auf Antrag (§ 63 Abs. 4 MarkenG bzw. § 71 Abs. 5 MarkenG, jeweils mit § 103 bis § 107 ZPO)\n\n"
                  "**Gebührenrückzahlung:** Widerspruchs-, Verfalls- und Nichtigkeitsgebühr (§ 63 Abs. 3 MarkenG); Erinnerungsgebühr (§ 64 Abs. 5 MarkenG); Beschwerdegebühr bei Abhilfe (§ 66 Abs. 5 S. 3 MarkenG) oder durch das BPatG (§ 71 Abs. 3 MarkenG); Wegfall bei Rücknahmefiktion ohne Amtshandlung (§ 10 Abs. 2 PatKostG).\n"
                  "**Kostenfestsetzung:** Beschwerde binnen zwei Wochen (§ 63 Abs. 4 S. 4 MarkenG), Gebühr 50 € (Nr. 401 200 Anlage PatKostG).\n"
                  "**Rechtsbeschwerde:** Kosten der erfolglosen Rechtsbeschwerde trägt der Beschwerdeführer (§ 90 Abs. 2 S. 1 MarkenG).\n"
                  "**Kennzeichenstreitsache:** Der Unterliegende trägt die Kosten (§ 91 Abs. 1 ZPO); Patentanwaltskosten nach § 13 RVG nur, soweit die Mitwirkung notwendig war (§ 140 Abs. 4 MarkenG, richtlinienkonform: BGH Kosten des Patentanwalts VII, EuGH NovaText).\n\n"
                  "**⇒ Rechtsfolge:** Kostenauferlegung ganz oder teilweise; sonst trägt jeder seine Kosten.\n\n"
                  "**In den Klausuren:** NS II/2019 („dass der Gegner Ihr Honorar zahlen muss“), NS I/2020 (Kosten sämtlicher Verfahren auferlegen), NS III/2021 (Schweigen, Gegenstandswert), NS III/2023 (Rückzahlung der Beschwerdegebühr), NS III/2024 (Rücknahme des Widerspruchs), NS II/2025 (aussichtslose Beschwerde), NS I/2025 (Rückzahlung nach Zuordnungsfehler).",
                  concepts=["kostenentscheidung", "prozesskosten_erstattung"],
                  norms=["§ 63 MarkenG", "§ 71 MarkenG", "§ 90 MarkenG", "§ 140 MarkenG", "§ 10 PatKostG", "Anlage PatKostG"],
                  cases=["bgh_kosten_patentanwalt_vii", "eugh_novatext", "bpatg_engelbrecht"], abschnitt="Normenkette"),
            intro("k15j-1", "Definitionen",
                  "**Kostengrundsatz:** Soweit keine Kostenbestimmung getroffen wird, trägt jeder Beteiligte die ihm erwachsenen Kosten selbst (§ 63 Abs. 1 S. 3, § 71 Abs. 1 S. 2 MarkenG).\n"
                  "**Billigkeit:** Eine Kostenauferlegung entspricht der Billigkeit nur bei besonderen Umständen, insbesondere wenn ein Beteiligter in einer nach anerkannten Beurteilungsgesichtspunkten aussichtslosen Lage ein Verfahren betreibt oder fortführt (BPatG Engelbrecht); bloßes Unterliegen genügt nicht.\n"
                  "**Notwendige Kosten:** Kosten, die zur zweckentsprechenden Wahrung der Ansprüche und Rechte notwendig waren (§ 63 Abs. 1 S. 1, § 71 Abs. 1 S. 1 MarkenG).\n"
                  "**Gegenstandswert:** Wert, nach dem die Anwaltsgebühren im Amtsverfahren berechnet werden; das DPMA setzt ihn bei einer Kostenentscheidung fest (§ 63 Abs. 2 MarkenG).\n"
                  "**Rückzahlung der Beschwerdegebühr:** Anordnung aus Billigkeit, insbesondere wenn ein Verfahrensfehler des DPMA die Beschwerde veranlasst hat (§ 71 Abs. 3 MarkenG; BPatG AUTOMATOR).",
                  concepts=["kostenentscheidung"], norms=["§ 63 MarkenG", "§ 71 MarkenG"], cases=["bpatg_engelbrecht", "bpatg_automator"], abschnitt="Definitionen"),
            fall("k15j-2", "Wer verliert, zahlt?",
                 "Der Widerspruch hat Erfolg; die Marke wird gelöscht. Die Widersprechende beantragt, der Markeninhaberin die Kosten aufzuerlegen, weil sie unterlegen sei.",
                 "Sind die Kosten der Markeninhaberin aufzuerlegen?", False,
                 ["**Nein!** Im Verfahren vor dem DPMA trägt grundsätzlich jeder Beteiligte seine Kosten selbst (§ 63 Abs. 1 S. 3 MarkenG). Eine Auferlegung setzt Billigkeitsgründe voraus (§ 63 Abs. 1 S. 1 MarkenG); das Unterliegen allein ist keiner. Anders im Zivilprozess (§ 91 Abs. 1 ZPO)."],
                 merke="DPMA und BPatG: Billigkeit, nicht Unterliegen (§ 63, § 71 MarkenG).",
                 level=1, concepts=["kostenentscheidung"], norms=["§ 63 Abs. 1 MarkenG"], abschnitt=N),
            fall("k15j-3", "Rücknahme des Widerspruchs (NS III/2024)",
                 "Die Widersprechende nimmt ihren Widerspruch im Beschwerdeverfahren nach einem Hinweis des Senats zurück. Die Markeninhaberin meint, nun müsse die Gegenseite automatisch alle Kosten tragen.",
                 "Trifft das zu?", False,
                 ["**Nein!** Auch bei Rücknahme gilt der Billigkeitsmaßstab (§ 71 Abs. 4 i.V.m. § 71 Abs. 1 MarkenG). Eine automatische Kostenfolge wie § 269 Abs. 3 ZPO gibt es nicht; die Rücknahme nach einem Hinweis ist sogar prozessökonomisch."],
                 merke="Rücknahme ⇒ § 71 Abs. 4 MarkenG: gleicher Billigkeitsmaßstab, keine Automatik.",
                 level=1, concepts=["kostenentscheidung"], norms=["§ 71 MarkenG"], abschnitt=N),
            fall("k15j-4", "Die aussichtslose Beschwerde (NS II/2025)",
                 "Die Widersprechende hält trotz gefestigter Rechtsprechung und eines Hinweises des Senats an der Beschwerde fest, mit der sie die Bösgläubigkeit der angegriffenen Marke im Widerspruchsverfahren geltend macht.",
                 "Können ihr die Kosten des Beschwerdeverfahrens auferlegt werden?", True,
                 ["**Ja!** Wer ein Verfahren in einer nach anerkannten Beurteilungsgesichtspunkten aussichtslosen Lage betreibt, verletzt die prozessuale Sorgfalt; die Kostenauferlegung entspricht der Billigkeit (§ 71 Abs. 1 S. 1 MarkenG; BPatG Engelbrecht)."],
                 merke="Aussichtslosigkeit trotz Hinweis = typischer Billigkeitsgrund.",
                 level=2, concepts=["kostenentscheidung"], norms=["§ 71 Abs. 1 MarkenG"], cases=["bpatg_engelbrecht"], abschnitt=N),
            fall("k15j-5", "Fehler des Amtes (NS III/2023)",
                 "Die Markenabteilung hat den Verfall ohne Sachprüfung erklärt, obwohl die Zweimonatsfrist mangels Fristsetzung nie zu laufen begonnen hatte. Das BPatG hebt auf und verweist zurück.",
                 "Ist die Rückzahlung der Beschwerdegebühr anzuordnen?", True,
                 ["**Ja!** Das BPatG kann die Rückzahlung anordnen (§ 71 Abs. 3 MarkenG); sie entspricht der Billigkeit, wenn ein Verfahrensfehler des DPMA die Beschwerde veranlasst hat (BPatG AUTOMATOR)."],
                 merke="Rückzahlung: Abhilfe § 66 Abs. 5 S. 3, BPatG § 71 Abs. 3 MarkenG.",
                 level=2, concepts=["kostenentscheidung"], norms=["§ 71 Abs. 3 MarkenG"], cases=["bpatg_automator"], abschnitt=N),
            mc("k15j-6", "Beschwerde gegen den Kostenfestsetzungsbeschluss",
               "Welche Frist und Gebühr gelten für die Beschwerde gegen einen Kostenfestsetzungsbeschluss des DPMA?",
               ["Ein Monat, 200 €", "Zwei Wochen (§ 63 Abs. 4 S. 4 MarkenG), 50 € (Nr. 401 200 Anlage PatKostG)", "Zwei Wochen, gebührenfrei", "Ein Monat, 50 €"], 1,
               ["**Zwei Wochen, 50 €.** An die Stelle der Erinnerung tritt die Beschwerde, die innerhalb von zwei Wochen einzulegen ist (§ 63 Abs. 4 S. 3, 4 MarkenG). Gebühr 50 € nach Nr. 401 200 Anlage PatKostG."],
               merke="Kostenfestsetzung: § 63 Abs. 4 MarkenG · zwei Wochen · 50 €.",
               level=2, concepts=["kostenentscheidung"], norms=["§ 63 Abs. 4 MarkenG", "Anlage PatKostG"], abschnitt=N),
            *fallkette("k15j-7", "Das Honorar soll der Gegner zahlen (nach NS II/2019)",
                       "Die Brückenbetreiberin will, dass K ihr Anwaltshonorar zahlt, und zwar für den Widerspruch beim DPMA und für eine mögliche Nichtigkeitsklage vor dem LG. Patentanwalt Dr. Emsig soll in beiden Verfahren mitwirken.",
                       [frage("V1: Ist im Widerspruchsverfahren überhaupt eine Kostenentscheidung möglich?", True,
                              ["**Ja!** Das Widerspruchsverfahren ist mehrseitig; das DPMA kann einem Beteiligten die Kosten auferlegen (§ 63 Abs. 1 S. 1 MarkenG)."],
                              merke="Mehrseitig ⇒ Kostenentscheidung möglich.", norms=["§ 63 Abs. 1 MarkenG"]),
                        frage("V2: Trägt K die Kosten schon deshalb, weil er unterliegt?", False,
                              ["**Nein!** Grundsatz ist die Kostentragung durch jeden Beteiligten selbst (§ 63 Abs. 1 S. 3 MarkenG); nötig sind Billigkeitsgründe. Eine bösgläubige Anmeldung könnte einer sein, ist hier aber nicht festzustellen."],
                              merke="Billigkeit ≠ Unterliegen.", norms=["§ 63 Abs. 1 MarkenG"]),
                        frage("V4: Wer setzt die zu erstattenden Kosten fest, wenn das DPMA sie K auferlegt?", 0,
                              ["**Das DPMA auf Antrag** (§ 63 Abs. 4 S. 1 MarkenG) nach den Vorschriften der ZPO über das Kostenfestsetzungsverfahren (§ 103 bis § 107 ZPO); zuvor setzt es den Gegenstandswert fest (§ 63 Abs. 2 MarkenG)."],
                              optionen=["Das DPMA auf Antrag (§ 63 Abs. 4 MarkenG)", "Das BPatG von Amts wegen", "Das LG", "Niemand; Erstattung nur durch Vergleich"],
                              merke="Festsetzung: § 63 Abs. 4 MarkenG (DPMA), § 71 Abs. 5 MarkenG (BPatG).", norms=["§ 63 Abs. 4 MarkenG"]),
                        frage("Vor dem LG: Sind die Kosten des mitwirkenden Patentanwalts stets zu erstatten, wenn die Betreiberin obsiegt?", False,
                              ["**Nein, nicht stets!** Der Unterliegende trägt die Kosten (§ 91 Abs. 1 ZPO); Patentanwaltskosten nach § 140 Abs. 4 MarkenG sind aber richtlinienkonform nur erstattungsfähig, wenn die Mitwirkung zur zweckentsprechenden Rechtsverfolgung notwendig war; die Partei muss das darlegen (BGH Kosten des Patentanwalts VII)."],
                              merke="§ 140 Abs. 4 MarkenG nur bei Notwendigkeit (Art. 14 DurchsetzungsRL).", norms=["§ 140 MarkenG"], cases=["bgh_kosten_patentanwalt_vii", "eugh_novatext"]),
                        ], abschnitt=K, level=2, concepts=["kostenentscheidung", "prozesskosten_erstattung"]),
        ]),
    ],
)
