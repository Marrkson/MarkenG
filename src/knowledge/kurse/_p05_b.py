# -*- coding: utf-8 -*-
"""Kurs p05 „Anspruchsgrundlagen Patent“, Teil B: Erteilungsverfahren, Fristen, Verletzung, Recht auf das Patent.

Kapitel p05h bis p05n, je eine Anspruchsgrundlage bzw. ein Rechtsbehelf: Prüfungsschema (Lösungssprache: AGL → Voraussetzungen mit
Norm → Rechtsfolge), Definitionen, Drill zu Normen und Fristen, Klausurfälle als Fallketten. Grundlage sind die Lösungen der TS-Klausuren
II/2018 bis III/2023 und der RP2-Klausur I/2019 (klausuren/loesungen); Fristen, Gebühren und Voraussetzungen sind am Normtext
(data/patg.json, patkostg.json, intpatueg.json) geprüft. Entscheidungen nur aus patent/cases*.py, epc/cases.py oder data/patent_decisions.json."""
from ._helpers import intro, mc, fall, frage, fallkette  # noqa: F401

DN = "Definitionen und Normen"
KF = "Klausurfall"

# ====================================================================================================== p05h Anmeldung und Erteilung
K_H = dict(id="p05h", titel="§§ 34 bis 49 PatG: Anmeldung und Erteilungsverfahren", einheiten=[
    intro("p05h-0", "Prüfungsschema",
          "**AGL:** § 49 Abs. 1 PatG (Erteilungsbeschluss) i.V.m. § 34 PatG, § 35 PatG, § 44 PatG; Gegenstück: Zurückweisung nach § 48 S. 1 PatG "
          "bzw. § 42 Abs. 3 S. 1 PatG\n\n"
          "**A · Wirksame Anmeldung**\n"
          "**V1 Anmeldetag** – § 35 Abs. 1 PatG: Name des Anmelders (§ 34 Abs. 3 Nr. 1 PatG), Erteilungsantrag (§ 34 Abs. 3 Nr. 2 PatG) und "
          "Angaben, die dem Anschein nach eine Beschreibung sind (§ 34 Abs. 3 Nr. 4 PatG), eingegangen beim DPMA oder einem bekanntgemachten "
          "Patentinformationszentrum (§ 35 Abs. 1 Nr. 1, 2 PatG); fehlen Zeichnungen oder Beschreibungsteile: Aufforderung mit Monatsfrist, "
          "Nachreichung verschiebt den Anmeldetag (§ 35 Abs. 2, 3 PatG)\n"
          "**V2 Deutsche Übersetzung** – § 35a Abs. 1 S. 1 PatG: drei Monate nach Einreichung; Englisch/Französisch zwölf Monate, bei "
          "Priorität höchstens 15 Monate ab Prioritätstag (§ 35a Abs. 2 PatG); sonst Rücknahmefiktion (§ 35a Abs. 1 S. 2 PatG) · Berechnung "
          "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB\n"
          "**V3 Anmeldegebühr** – Nr. 311 000 GV PatKostG: 40 EUR elektronisch bis zehn Ansprüche, je weiterer Anspruch 20 EUR "
          "(Nr. 311 050 GV PatKostG), in Papierform das 1,5fache (Nr. 311 100 GV PatKostG); fällig mit Einreichung (§ 3 Abs. 1 S. 1 PatKostG), "
          "Zahlungsfrist drei Monate (§ 6 Abs. 1 S. 2 PatKostG), sonst gilt die Anmeldung als zurückgenommen (§ 6 Abs. 2 PatKostG) · Zahlungstag "
          "§ 2 PatKostZV · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB\n\n"
          "**B · Offensichtlichkeitsprüfung**\n"
          "**V4 Keine offensichtlichen Mängel** – § 42 Abs. 1 S. 1 PatG: Anforderungen der § 34 PatG, § 36 PatG, § 37 PatG, § 38 PatG; "
          "PatV-Formmängel (§ 34 Abs. 6 PatG) darf die Prüfungsstelle bis zum Prüfungsverfahren zurückstellen (§ 42 Abs. 1 S. 2 PatG); "
          "Zusammenfassung bis 15 Monate (§ 36 Abs. 1 PatG), Erfinderbenennung binnen 15 Monaten (§ 37 Abs. 1 S. 1 PatG)\n"
          "**V5 Nicht offensichtlich schutzunfähig** – § 42 Abs. 2 S. 1 PatG: keine Erfindung (Nr. 1), nicht gewerblich anwendbar (Nr. 2), "
          "ausgeschlossen nach § 1a Abs. 1 PatG, § 2 PatG oder § 2a Abs. 1 PatG (Nr. 3); Benachrichtigung mit Äußerungsfrist, sonst "
          "Zurückweisung (§ 42 Abs. 3 S. 1 PatG)\n\n"
          "**C · Prüfungsverfahren**\n"
          "**V6 Prüfungsantrag** – § 44 Abs. 1 PatG, § 44 Abs. 2 S. 1 PatG: Anmelder oder Dritter, bis sieben Jahre nach Einreichung; "
          "Prüfungsgebühr 350 EUR (Nr. 311 400 GV PatKostG), 150 EUR nach Rechercheantrag (Nr. 311 300 GV PatKostG), zahlbar drei Monate ab "
          "Fälligkeit, spätestens bis Ablauf der sieben Jahre (§ 44 Abs. 2 S. 2, 3 PatG); ohne Antrag Rücknahmefiktion (§ 58 Abs. 3 PatG)\n"
          "**V7 Erfordernisse der § 34 PatG, § 37 PatG, § 38 PatG** – Ausführbarkeit (§ 34 Abs. 4 PatG), Einheitlichkeit (§ 34 Abs. 5 PatG), "
          "keine Erweiterung (§ 38 S. 1 PatG); Mängel rügt die Prüfungsstelle mit Frist (§ 45 Abs. 1 S. 1 PatG)\n"
          "**V8 Patentfähigkeit nach §§ 1 bis 5 PatG** – sonst Bescheid mit Gründen und Äußerungsfrist (§ 45 Abs. 2 PatG)\n"
          "**V9 Rechtliches Gehör** – Zurückweisung nur auf mitgeteilte Umstände (§ 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG); Anhörung auf "
          "schriftlichen Antrag bis zum Erteilungsbeschluss (§ 46 Abs. 1 S. 3, 4 PatG); Niederschrift (§ 46 Abs. 2 PatG)\n"
          "**V10 Beantragte Fassung** – Erteilung nur in einer vom Anmelder beantragten Fassung; über Haupt- und Hilfsanträge wird einheitlich "
          "entschieden (BPatG Teilbeschluss)\n\n"
          "**⇒ Rechtsfolge:** Erteilungsbeschluss (§ 49 Abs. 1 PatG; auf Antrag ausgesetzt bis 15 Monate nach Anmelde- oder Prioritätstag, "
          "§ 49 Abs. 2 PatG); Veröffentlichung im Patentblatt, Eintritt der Wirkungen (§ 58 Abs. 1 S. 3 PatG). Sonst Zurückweisung "
          "(§ 48 S. 1 PatG) → Beschwerde (§ 73 Abs. 1 PatG) oder Weiterbehandlung (§ 123a PatG)\n\n"
          "**Klausurfallen:** Unterschrift, Patentansprüche und deutsche Sprache sind keine Anmeldetagserfordernisse. Bleibt nur die "
          "Recherchegebühr aus, entfällt nur der Rechercheantrag. Jahresgebühren ersetzen den Prüfungsantrag nicht: § 58 Abs. 3 PatG enthält "
          "zwei selbständige Fiktionen. Die Rücknahme der Anmeldung ist formfrei und in der Anhörung zu Protokoll wirksam. Eine Teilanmeldung "
          "darf ohne neuen Bescheid zurückgewiesen werden, wenn die Gründe aus der Stammanmeldung mitgeteilt sind.\n\n"
          "**In den Klausuren:** TS III/2022 (Faxanmeldung, Gebühren, § 42 PatG, § 58 Abs. 3 PatG), TS II/2019 (§ 35a PatG), TS III/2023 "
          "(Übersetzung, Anhörung, Rücknahme), TS I/2022 (Mängelrüge, Zusammenfassung), TS III/2020 (Anhörung, Hilfsanträge, Teilanmeldung), "
          "TS II/2022 (Ausführbarkeit), TS II/2018 (Prüfungsbescheid).",
          concepts=["pat_anmeldetag", "pat_anmeldung", "pat_offensichtlichkeitspruefung", "pat_pruefungsantrag", "pat_pruefungsbescheid",
                    "pat_anhoerung", "pat_beschluss_pruefungsstelle"],
          norms=["§ 34 PatG", "§ 35 PatG", "§ 35a PatG", "§ 42 PatG", "§ 44 PatG", "§ 45 PatG", "§ 46 PatG", "§ 48 PatG", "§ 49 PatG",
                 "§ 6 PatKostG"],
          cases=["pat_bpatg_teilbeschluss"], abschnitt="Normenkette"),
    intro("p05h-1", "Definitionen",
          "**Anmeldetag:** Tag, an dem Name des Anmelders, Erteilungsantrag und Angaben, die dem Anschein nach als Beschreibung anzusehen sind, "
          "beim DPMA oder einem bekanntgemachten Patentinformationszentrum eingegangen sind (Legaldefinition § 35 Abs. 1 PatG)\n"
          "**Ausführbare Offenbarung:** Die Anmeldung vermittelt dem Fachmann so viel technische Information, dass er die Erfindung mit seinem "
          "Fachwissen und Fachkönnen erfolgreich ausführen kann; ein gangbarer Weg genügt (§ 34 Abs. 4 PatG; BGH Klammernahtgerät, BGH Taxol)\n"
          "**Einheitlichkeit:** eine einzige Erfindung oder eine Gruppe von Erfindungen, die eine einzige allgemeine erfinderische Idee "
          "verwirklichen (§ 34 Abs. 5 PatG)\n"
          "**Zusammenfassung:** dient ausschließlich der technischen Unterrichtung; Bezeichnung, Kurzfassung mit technischem Gebiet, Problem, "
          "Lösung und Verwendung, kennzeichnende Zeichnung (§ 36 Abs. 2 PatG)\n"
          "**Offensichtlicher Mangel:** Verstoß gegen § 34 PatG, § 36 PatG, § 37 PatG oder § 38 PatG, der ohne eingehende Sachprüfung "
          "zweifelsfrei erkennbar ist (§ 42 Abs. 1 S. 1 PatG; DPMA-Prüfungsrichtlinien)\n"
          "**Prüfungsbescheid:** Mitteilung der Prüfungsstelle über Mängel (§ 45 Abs. 1 PatG) oder über die fehlende Patentfähigkeit mit Gründen "
          "(§ 45 Abs. 2 PatG), jeweils mit Frist zur Äußerung\n"
          "**Rücknahmefiktion:** kraft Gesetzes eintretender Wegfall der Anmeldung ohne Beschluss (§ 35a Abs. 1 S. 2 PatG, § 58 Abs. 3 PatG, "
          "§ 6 Abs. 2 PatKostG); Rechtsbehelf ist die Wiedereinsetzung, nicht die Weiterbehandlung (§ 123a Abs. 1 PatG setzt eine Zurückweisung "
          "voraus)\n"
          "**Fälligkeit:** Gebühren werden mit Einreichung der Anmeldung oder des Antrags fällig, soweit gesetzlich nichts anderes bestimmt ist "
          "(§ 3 Abs. 1 S. 1 PatKostG); Jahresgebühren am letzten Tag des Anmeldemonats (§ 3 Abs. 2 S. 1 PatKostG)\n"
          "**Zahlungstag:** Gutschrift auf dem Konto der Bundeskasse, Tag der Bareinzahlung oder Eingang des SEPA-Basislastschriftmandats beim "
          "DPMA (§ 2 PatKostZV)",
          concepts=["pat_anmeldetag", "pat_ausfuehrbarkeit", "pat_einheitlichkeit", "pat_faelligkeit", "pat_zahlungsfristen"],
          norms=["§ 35 PatG", "§ 34 PatG", "§ 36 PatG", "§ 3 PatKostG"], cases=["pat_bgh_klammernahtgeraet", "pat_bgh_taxol"],
          abschnitt="Definitionen"),
    mc("p05h-2", "Anmeldetagserfordernisse", "Welche Unterlagen müssen beim DPMA eingegangen sein, damit die Anmeldung einen Anmeldetag erhält?",
       ["Name, Erteilungsantrag und Angaben, die dem Anschein nach eine Beschreibung sind",
        "Name, unterschriebener Erteilungsantrag und mindestens ein Patentanspruch",
        "alle Unterlagen nach § 34 Abs. 3 PatG und die Anmeldegebühr",
        "Erteilungsantrag, Beschreibung in deutscher Sprache und Zeichnungen"], 0,
       ["**§ 35 Abs. 1 PatG.** Anmeldetag ist der Tag des Eingangs von Name (§ 34 Abs. 3 Nr. 1 PatG), Erteilungsantrag (§ 34 Abs. 3 Nr. 2 PatG) "
        "und Angaben, die dem Anschein nach Beschreibung sind (§ 34 Abs. 3 Nr. 4 PatG).",
        "Ansprüche, Unterschrift, Gebühr und deutsche Fassung sind nachholbar (§ 35a PatG, § 6 PatKostG) und verschieben den Anmeldetag nicht."],
       merke="Anmeldetag = Name + Antrag + Beschreibung dem Anschein nach (§ 35 Abs. 1 PatG).", level=1,
       concepts=["pat_anmeldetag"], norms=["§ 35 PatG", "§ 34 PatG"], abschnitt=DN),
    fall("p05h-3", "Englische Anmeldung ohne Übersetzung",
         "Die Elektro AG reicht am Mi 04.06.2014 eine vollständig englische Patentanmeldung ohne Prioritätsanspruch beim DPMA in München ein. "
         "Eine deutsche Übersetzung reicht sie nicht ein.",
         "Gilt die Anmeldung schon mit Ablauf von drei Monaten als zurückgenommen?", False,
         ["**Nein!** Für englische und französische Anmeldungen verlängert sich die Frist des § 35a Abs. 1 S. 1 PatG auf zwölf Monate "
          "(§ 35a Abs. 2 S. 1 PatG), bei Priorität endet sie spätestens 15 Monate nach dem Prioritätstag (§ 35a Abs. 2 S. 2 PatG).",
          "Ende Do 04.06.2015 (§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB), Fronleichnam in Bayern: Fr 05.06.2015 (§ 193 BGB). Danach "
          "Rücknahmefiktion (§ 35a Abs. 1 S. 2 PatG)."],
         merke="Übersetzung § 35a PatG: drei Monate, Englisch/Französisch zwölf, höchstens 15 ab Prioritätstag · § 187 Abs. 1, § 188 Abs. 2, "
               "§ 193 BGB.", level=1, norms=["§ 35a PatG"], abschnitt=DN),
    mc("p05h-4", "Anmeldegebühr bei Telefax", "Wie hoch ist die Anmeldegebühr und was gilt bei Nichtzahlung?",
       ["40 EUR; bei Nichtzahlung wird die Anmeldung zurückgewiesen",
        "120 EUR binnen drei Monaten; sonst gilt die ganze Anmeldung als zurückgenommen",
        "120 EUR; bei Teilzahlung entfallen nur die Ansprüche 11 und 12",
        "60 EUR binnen eines Monats; sonst Weiterbehandlung"], 1,
       ["**120 EUR.** Telefax ist Papierform: 1,5fache Gebühr (Nr. 311 100 GV PatKostG), also 60 EUR (Nr. 311 000 GV PatKostG) und "
        "2 × 30 EUR (Nr. 311 050 GV PatKostG).",
        "Fällig mit Einreichung (§ 3 Abs. 1 S. 1 PatKostG), Zahlung binnen drei Monaten (§ 6 Abs. 1 S. 2 PatKostG). Nicht vollständig gezahlt: "
        "Die ganze Anmeldung gilt als zurückgenommen (§ 6 Abs. 2 PatKostG)."],
       sachverhalt="Die A & B GbR reicht eine Anmeldung mit zwölf Patentansprüchen per Telefax beim DPMA ein.",
       merke="Fälligkeit § 3 Abs. 1 PatKostG · Frist § 6 Abs. 1 S. 2 PatKostG · Folge § 6 Abs. 2 PatKostG · Zahlungstag § 2 PatKostZV.",
       level=2, concepts=["pat_gebuehren", "pat_zahlungsfristen"], norms=["§ 6 PatKostG", "§ 3 PatKostG"], abschnitt=DN),
    fall("p05h-5", "Nur die Recherchegebühr fehlt",
         "Mit der Anmeldung stellt die A & B GbR Rechercheantrag. Sie zahlt fristgerecht die Anmeldegebühr, die Recherchegebühr von 300 EUR "
         "(Nr. 311 200 GV PatKostG) aber nie.",
         "Gilt die Anmeldung als zurückgenommen?", False,
         ["**Nein!** § 6 Abs. 2 PatKostG knüpft die Folge an die jeweilige Gebühr: Ohne Recherchegebühr gilt nur der **Rechercheantrag** als "
          "zurückgenommen (§ 43 Abs. 1 PatG). Die Anmeldung bleibt anhängig.",
          "Folge für später: Die Prüfungsgebühr beträgt dann 350 EUR statt 150 EUR (Nr. 311 400 GV PatKostG)."],
         merke="§ 6 Abs. 2 PatKostG: Wegfall nur der Handlung, deren Gebühr fehlt.", level=2,
         concepts=["pat_zahlungsfristen", "pat_recherche_pruefung"], norms=["§ 6 PatKostG", "§ 43 PatG"], abschnitt=DN),
    fall("p05h-6", "Jahresgebühren statt Prüfungsantrag",
         "C zahlt für eine Anmeldung vom Mi 11.07.2018 pünktlich alle Jahresgebühren. Einen Prüfungsantrag stellt niemand.",
         "Bleibt die Anmeldung über Fr 11.07.2025 hinaus anhängig?", False,
         ["**Nein!** Der Prüfungsantrag ist bis zum Ablauf von sieben Jahren nach Einreichung zu stellen (§ 44 Abs. 2 S. 1 PatG), hier bis "
          "Fr 11.07.2025 (§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB).",
          "§ 58 Abs. 3 PatG enthält zwei selbständige Rücknahmefiktionen: fehlender Prüfungsantrag und nicht gezahlte Jahresgebühr. Die Zahlung "
          "der Jahresgebühren hält die Anmeldung nur bis zum Ablauf der Antragsfrist."],
         merke="Prüfungsantrag § 44 Abs. 2 S. 1 PatG (sieben Jahre) · Folge § 58 Abs. 3 PatG · Jahresgebühren ersetzen ihn nicht.", level=1,
         concepts=["pat_pruefungsantrag"], norms=["§ 44 PatG", "§ 58 PatG"], abschnitt=DN),
    mc("p05h-7", "Antrag auf Anhörung", "Wann darf die Prüfungsstelle einen Antrag des Anmelders auf Anhörung zurückweisen?",
       ["wenn die Anhörung nicht sachdienlich ist",
        "nur wenn der Antrag nicht schriftlich gestellt ist",
        "wenn bereits zwei Prüfungsbescheide ergangen sind",
        "wenn sie die Anmeldung ohnehin erteilen will"], 1,
       ["**§ 46 Abs. 1 S. 3 bis 5 PatG.** Bis zum Beschluss über die Erteilung ist der Anmelder auf Antrag zu hören; der Antrag ist schriftlich "
        "einzureichen. Zurückweisen darf die Prüfungsstelle nur den formwidrigen Antrag, und dieser Beschluss ist selbständig nicht anfechtbar "
        "(§ 46 Abs. 1 S. 6 PatG).",
        "Auf Sachdienlichkeit kommt es nur noch bei Anhörungen von Amts wegen an (§ 46 Abs. 1 S. 1 PatG)."],
       merke="Anhörung: Antrag schriftlich bis zum Erteilungsbeschluss, dann Pflicht (§ 46 Abs. 1 S. 3, 4 PatG).", level=1,
       concepts=["pat_anhoerung"], norms=["§ 46 PatG"], abschnitt=DN),
    mc("p05h-8", "Zurückweisung ohne neuen Bescheid",
       "Darf die Prüfungsstelle eine Teilanmeldung mit den unveränderten, bereits beanstandeten Ansprüchen der Stammanmeldung ohne neuen "
       "Bescheid zurückweisen?",
       ["Nein, jede Teilanmeldung braucht einen eigenen Erstbescheid",
        "Ja, weil die Teilanmeldung im Verfahrensstand der Stammanmeldung fortgeführt wird und die Gründe mitgeteilt sind",
        "Ja, aber nur nach Anhörung von Amts wegen",
        "Nein, die Zurückweisung der Stammanmeldung erfasst die Teilanmeldung schon"], 1,
       ["**Ja, § 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG.** Neu mitzuteilen sind nur Umstände, die dem Anmelder noch nicht bekannt waren.",
        "Die Teilanmeldung wird in der Verfahrenslage der Stammanmeldung weitergeführt; deren Bescheide gelten als in ihr erlassen (BPatG "
        "Prüfungsbescheid in Nachanmeldung, 20 W (pat) 28/09). Neue Ansprüche zwingen dagegen zu neuer Mitteilung."],
       merke="Gehör § 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG: nur neue Gründe neu mitteilen.", level=2,
       concepts=["pat_rechtliches_gehoer", "pat_teilung"], norms=["§ 48 PatG", "§ 42 PatG"], abschnitt=DN),
    *fallkette("p05h-9", "Faxanmeldung der GbR (nach TS III/2022)",
        "Die A & B GbR reicht am Mi 11.07.2018 per Telefax beim DPMA eine Patentanmeldung für eine Ellenbogenprothese ein: nicht unterschriebener "
        "Erteilungsantrag, Beschreibung, zwölf Ansprüche, drei Figuren, Rechercheantrag. Eine Zusammenfassung fehlt. Die Ansprüche 7 bis 12 "
        "betreffen das Implantieren der Prothese.",
        [frage("Erhält die Anmeldung trotz fehlender Unterschrift den Anmeldetag 11.07.2018?", True,
               ["**Ja!** § 35 Abs. 1 PatG verlangt nur Name, Erteilungsantrag und Angaben, die dem Anschein nach Beschreibung sind. Die "
                "Unterschrift ist Formerfordernis der PatV (§ 4 Abs. 2 Nr. 5 PatV) und nachholbar; die GbR ist als Anmelderin identifizierbar."],
               merke="Formmängel außerhalb des § 35 Abs. 1 PatG kosten den Anmeldetag nicht.", titel="V1 Anmeldetag", norms=["§ 35 PatG"]),
         frage("Bis wann sind Anmelde- und Recherchegebühr zu zahlen?", 1,
               ["**Do 11.10.2018.** Beide Gebühren sind mit Einreichung fällig (§ 3 Abs. 1 S. 1 PatKostG), zahlbar binnen drei Monaten "
                "(§ 6 Abs. 1 S. 2 PatKostG): 120 EUR Anmeldegebühr in Papierform und 300 EUR Recherchegebühr. Berechnung § 187 Abs. 1 BGB, "
                "§ 188 Abs. 2 BGB; Zahlungstag § 2 PatKostZV."],
               optionen=["Mi 11.07.2018", "Do 11.10.2018", "Fr 11.01.2019", "Mo 15.10.2018"],
               merke="Gebühr mit Einreichung fällig, drei Monate Zahlungsfrist (§ 6 Abs. 1 S. 2 PatKostG).", titel="V3 Gebühren",
               norms=["§ 6 PatKostG"]),
         frage("Rügt die Prüfungsstelle die fehlende Zusammenfassung schon in der Offensichtlichkeitsprüfung?", True,
               ["**Ja!** § 42 Abs. 1 S. 1 PatG erfasst die Anforderungen des § 36 PatG. Die Zusammenfassung ist bis 15 Monate nach dem "
                "Anmeldetag nachreichbar (§ 36 Abs. 1 PatG), hier bis Fr 11.10.2019.",
                "Die fehlende Unterschrift (PatV-Form) darf die Prüfungsstelle dagegen bis zum Prüfungsverfahren zurückstellen "
                "(§ 42 Abs. 1 S. 2 PatG)."],
               merke="§ 42 Abs. 1 PatG: Mängel der § 34, § 36, § 37, § 38 PatG; PatV-Mängel zurückstellbar.", titel="V4 Formmängel",
               norms=["§ 42 PatG", "§ 36 PatG"]),
         frage("Darf die Prüfungsstelle die Ansprüche 7 bis 12 schon jetzt beanstanden?", True,
               ["**Ja!** Verfahren zur chirurgischen Behandlung des menschlichen Körpers sind ausgeschlossen (§ 2a Abs. 1 Nr. 2 PatG); das ist "
                "offensichtlich (§ 42 Abs. 2 S. 1 Nr. 3 PatG). Die Prothese selbst bleibt patentierbar (§ 2a Abs. 1 Nr. 2 S. 2 PatG).",
                "Hält die GbR an den Ansprüchen fest, wird die ganze Anmeldung zurückgewiesen (§ 42 Abs. 3 S. 1 PatG)."],
               merke="Offensichtlicher Ausschluss: Benachrichtigung mit Frist (§ 42 Abs. 2 PatG), dann Zurückweisung (§ 42 Abs. 3 PatG).",
               titel="V5 Offensichtlicher Ausschluss", norms=["§ 42 PatG", "§ 2a PatG"]),
         frage("Gilt die Anmeldung mit Ablauf des Fr 11.07.2025 als zurückgenommen, obwohl C die Jahresgebühren gezahlt hat?", True,
               ["**Ja!** Ohne Prüfungsantrag binnen sieben Jahren nach Einreichung (§ 44 Abs. 2 S. 1 PatG) gilt die Anmeldung als zurückgenommen "
                "(§ 58 Abs. 3 PatG). Die Jahresgebühren betreffen den zweiten, selbständigen Fiktionstatbestand."],
               abwandlung="A und B verlassen sich darauf, dass C „die Formalien“ erledigt; C zahlt nur die Jahresgebühren.",
               merke="Sieben Jahre § 44 Abs. 2 S. 1 PatG · Folge § 58 Abs. 3 PatG.", titel="V6 Prüfungsantrag", norms=["§ 44 PatG", "§ 58 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_anmeldung", "pat_offensichtlichkeitspruefung"], norms=["§ 35 PatG", "§ 42 PatG"]),
    *fallkette("p05h-10", "Anhörung, Hilfsantrag, Rücknahme (nach TS III/2020 und TS III/2023)",
        "Die Prüfungsstelle hält Anspruch 1 der Anmeldung DE1 im Bescheid für nicht erfinderisch. Die Anmelderin K beantragt schriftlich eine "
        "Anhörung und will dort einen Hauptantrag (ursprüngliche Unterlagen) und einen Hilfsantrag mit einem zusätzlichen Merkmal stellen.",
        [frage("Muss die Prüfungsstelle die Anhörung durchführen?", True,
               ["**Ja!** Bis zum Beschluss über die Erteilung ist der Anmelder auf schriftlichen Antrag zu hören (§ 46 Abs. 1 S. 3, 4 PatG). Eine "
                "Sachdienlichkeitsprüfung findet nicht statt."],
               merke="Anhörung auf schriftlichen Antrag ist Pflicht (§ 46 Abs. 1 S. 3 PatG).", titel="V9 Anhörung", norms=["§ 46 PatG"]),
         frage("Darf die Prüfungsstelle den Hauptantrag durch Teilbeschluss zurückweisen und über den Hilfsantrag später entscheiden?", False,
               ["**Nein!** Über Haupt- und Hilfsanträge ist einheitlich zu entscheiden (BPatG Teilbeschluss). Tenor: Patent nach dem Hilfsantrag "
                "erteilt (§ 49 Abs. 1 PatG), im Übrigen zurückgewiesen (§ 48 S. 1 PatG).",
                "Nur so bleibt K für die Beschwerde beschwert (§ 73 Abs. 1 PatG): Die ursprünglichen Unterlagen müssen beantragt und abgelehnt sein."],
               merke="Ein Beschluss: Erteilung nach dem ersten gewährbaren Antrag, im Übrigen Zurückweisung.", titel="V10 Einheitliche Entscheidung",
               cases=["pat_bpatg_teilbeschluss"], norms=["§ 49 PatG", "§ 48 PatG"]),
         frage("Ist die mündlich erklärte Rücknahme wirksam?", True,
               ["**Ja!** Die Rücknahme ist formfrei; Schriftform verlangt das PatG nur für Teilung (§ 39 Abs. 1 S. 2 PatG) und Anhörungsantrag "
                "(§ 46 Abs. 1 S. 4 PatG). Die Niederschrift hält rechtserhebliche Erklärungen fest (§ 46 Abs. 2 PatG i.V.m. § 162 Abs. 1 ZPO).",
                "Die Rücknahme ist unwiderruflich, selbst eine versehentlich abgesandte (BPatG Versehentliche Rücknahmeerklärung, 7 W (pat) 31/15)."],
               abwandlung="Nach ungünstigem Verlauf der Anhörung erklärt K die Rücknahme der Anmeldung; sie wird protokolliert und genehmigt.",
               merke="Rücknahme: formfrei, zu Protokoll, unwiderruflich.", titel="Rücknahme in der Anhörung", norms=["§ 46 PatG"]),
         frage("Kann K danach noch Beschwerde einlegen oder die Anmeldung teilen?", False,
               ["**Nein!** Mit der Rücknahme ist die Anmeldung erledigt; bereits ergangene Beschlüsse werden wirkungslos (BGH Telefonsystem, "
                "X ZB 8/10). Beschwerde (§ 73 Abs. 1 PatG) und Teilung (§ 39 Abs. 1 S. 1 PatG) setzen eine anhängige Anmeldung voraus.",
                "Offen bleiben die Gebrauchsmusterabzweigung (§ 5 Abs. 1 S. 3 GebrMG) und eine Nachanmeldung mit noch laufender Priorität."],
               merke="Nach Rücknahme: keine Beschwerde, keine Teilung; Abzweigung bis zwei Monate nach Monatsende der Erledigung.",
               titel="Folgen der Rücknahme", norms=["§ 39 PatG", "§ 73 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_anhoerung", "pat_beschluss_pruefungsstelle"], norms=["§ 46 PatG"]),
])

# ====================================================================================================== p05i § 38 PatG
K_I = dict(id="p05i", titel="§ 38 PatG: Änderungen und unzulässige Erweiterung im Erteilungsverfahren", einheiten=[
    intro("p05i-0", "Prüfungsschema",
          "**AGL:** § 38 S. 1 PatG (Zulässigkeit der Änderung); Folge eines Verstoßes § 38 S. 2 PatG, Rüge § 45 Abs. 1 S. 1 PatG, Zurückweisung "
          "§ 48 S. 1 PatG; nach Erteilung Widerrufs- und Nichtigkeitsgrund § 21 Abs. 1 Nr. 4 PatG, § 22 Abs. 1 PatG\n\n"
          "**V1 Zeitpunkt** – § 38 S. 1 PatG: bis zum Beschluss über die Erteilung; vor Eingang des Prüfungsantrags (§ 44 PatG) nur Berichtigung "
          "offensichtlicher Unrichtigkeiten, Beseitigung der von der Prüfungsstelle bezeichneten Mängel und Änderungen des Patentanspruchs\n"
          "**V2 Form und Sprache** – deutsche Fassung (§ 126 PatG); § 35a PatG erlaubt nur die Anmeldung selbst in fremder Sprache; geänderte "
          "Fassungen als Haupt- und Hilfsanträge, über die einheitlich entschieden wird (§ 49 Abs. 1 PatG; BPatG Teilbeschluss)\n"
          "**V3 Keine Erweiterung** – § 38 S. 1 PatG: Maßstab ist, was der Fachmann den ursprünglich eingereichten Unterlagen (bei "
          "fremdsprachiger Anmeldung dem Original, vgl. § 21 Abs. 1 Nr. 4 PatG) unmittelbar und eindeutig als zur Erfindung gehörend entnimmt "
          "(BGH Hubgliedertor I, BGH Fälschungssicheres Dokument); Prioritätsunterlagen gehören nicht dazu\n"
          "  **V3.1 Merkmale aus Ausführungsbeispielen und Figuren** – einzeln oder gemeinsam aufnehmbar, wenn sie den Erfolg der Erfindung "
          "fördern und die Kombination als mögliche Ausgestaltung entnehmbar ist (BGH Schleifprodukt); schematische Zeichnungen offenbaren nur "
          "das Prinzip, keine Maße (BGH Steckverbindung)\n"
          "  **V3.2 Zwischenverallgemeinerung** – ein Merkmal wird ohne die mit ihm offenbarten, funktional zugehörigen Merkmale aufgenommen: "
          "Erweiterung, wenn die Unterlagen die allgemeinere Kombination nicht als zur Erfindung gehörend zeigen (BGH Einkaufswagen II; BGH "
          "Digitales Buch, X ZR 63/15)\n"
          "  **V3.3 Weglassen und Verallgemeinern** – bis zur Erteilung auch weiter gefasste Ansprüche, soweit ursprünglich als Erfindung "
          "offenbart; „besteht aus“ ist durch „enthält“ nicht ohne Weiteres offenbart (BGH Reifenabdichtmittel)\n"
          "**V4 Antrag** – erteilt wird nur, was der Anmelder beantragt; hält er an einer unzulässig erweiterten Fassung fest, wird die ganze "
          "Anmeldung zurückgewiesen (BGH Phosphatidylcholin)\n\n"
          "**⇒ Rechtsfolge:** Zulässige Änderung: Prüfung der neuen Fassung; über neuen Prüfungsstoff ist vor der Zurückweisung Gehör zu gewähren "
          "(§ 45 Abs. 2 PatG, § 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG). Unzulässige Änderung: aus ihr können Rechte nicht hergeleitet "
          "werden (§ 38 S. 2 PatG); Rüge mit Aufforderung zur Streichung, bei Festhalten Zurückweisung (§ 48 S. 1 PatG); nach Erteilung Widerruf "
          "oder Nichtigerklärung (§ 21 Abs. 1 Nr. 4 PatG, § 22 Abs. 1 PatG), ein nur beschränkendes Merkmal kann als uneigentliche Erweiterung "
          "im Anspruch bleiben (BGH Winkelmesseinrichtung)\n\n"
          "**Klausurfallen:** Was nur in der Prioritätsunterlage steht, ist nicht Inhalt der Anmeldung (TS III/2023: „alle Räder“ nur in US1). "
          "Maßstab einer Teilanmeldung ist die Stammanmeldung in der ursprünglichen Fassung (§ 21 Abs. 1 Nr. 4 Hs. 2 PatG). Ein nicht offenbartes "
          "Merkmal macht die Teilung nicht unwirksam, sondern die Fassung unzulässig. Die Berichtigung einer fehlerhaften Übersetzung auf das "
          "Original erweitert nicht.\n\n"
          "**In den Klausuren:** TS III/2023 („alle Räder“, Elektromotor aus US2), TS III/2020 (Hilfsanträge, Teilanmeldung 2), TS I/2021 "
          "(japanische Stammanmeldung), TS II/2022 („Stuhl“ statt „Sitzmöbel“), TS II/2018 (Beschränkung gegen Vorführung).",
          concepts=["pat_unzulaessige_erweiterung", "pat_offenbarung"], norms=["§ 38 PatG", "§ 21 PatG", "§ 45 PatG", "§ 48 PatG"],
          cases=["pat_bgh_hubgliedertor_i", "pat_bgh_faelschungssicheres_dokument", "pat_bgh_schleifprodukt", "pat_bgh_phosphatidylcholin"],
          abschnitt="Normenkette"),
    intro("p05i-1", "Definitionen",
          "**Unzulässige Erweiterung:** Der Gegenstand geht über das hinaus, was der Fachmann den ursprünglichen Unterlagen unmittelbar und "
          "eindeutig als zur Erfindung gehörend entnimmt; es genügt nicht, dass er ihn erst aufgrund eigener, von Fachwissen getragener "
          "Überlegungen findet (§ 38 S. 1 PatG; BGH Hubgliedertor I)\n"
          "**Offenbarungsgehalt:** Gesamtinhalt von Beschreibung, Ansprüchen und Zeichnungen einschließlich des für den Fachmann "
          "Selbstverständlichen, nicht aber Erkenntnisse, zu denen er durch Fachwissen oder Abwandlung gelangt (BGH Fälschungssicheres Dokument)\n"
          "**Gegenstand der Anmeldung:** Inhalt der Anmeldung in der ursprünglich eingereichten Fassung, nicht der Prioritätsunterlagen "
          "(§ 38 S. 1 PatG, § 21 Abs. 1 Nr. 4 PatG)\n"
          "**Zwischenverallgemeinerung:** Aufnahme eines Merkmals aus einem Ausführungsbeispiel ohne die mit ihm zusammen offenbarten Merkmale; "
          "zulässig nur, wenn die so gebildete Kombination als mögliche Ausgestaltung der Erfindung offenbart ist (Begriff der EPA-Praxis; BGH "
          "Schleifprodukt)\n"
          "**Verallgemeinerung:** Fassung des Anspruchs über die Ausführungsbeispiele hinaus; zulässig, wenn die allgemeinere Lehre als zur "
          "Erfindung gehörend erkennbar war (BGH Einkaufswagen II)\n"
          "**Aliud:** Änderung, die den Gegenstand nicht beschränkt, sondern durch einen anderen ersetzt; anders als die uneigentliche "
          "Erweiterung (nur beschränkendes, nicht offenbartes Merkmal) führt sie zum Widerruf (BGH Winkelmesseinrichtung)\n"
          "**Offensichtliche Unrichtigkeit:** Fehler in den Unterlagen, den der Fachmann ebenso wie die richtige Fassung sofort erkennt; ihre "
          "Berichtigung ist schon vor dem Prüfungsantrag zulässig (§ 38 S. 1 PatG; Lehre)",
          concepts=["pat_unzulaessige_erweiterung", "pat_offenbarung"], norms=["§ 38 PatG"],
          cases=["pat_bgh_hubgliedertor_i", "pat_bgh_faelschungssicheres_dokument", "pat_bgh_einkaufswagen_ii", "pat_bgh_winkelmesseinrichtung"],
          abschnitt="Definitionen"),
    mc("p05i-2", "Änderungen vor dem Prüfungsantrag", "Welche Änderungen sind vor Eingang des Prüfungsantrags zulässig?",
       ["alle Änderungen, die den Gegenstand nicht erweitern",
        "nur Berichtigung offensichtlicher Unrichtigkeiten, Beseitigung gerügter Mängel und Änderungen des Patentanspruchs",
        "keine, das Verfahren ruht bis zum Prüfungsantrag",
        "nur Streichungen von Patentansprüchen"], 1,
       ["**§ 38 S. 1 Hs. 2 PatG.** Bis zum Eingang des Prüfungsantrags (§ 44 PatG) sind nur diese drei Arten von Änderungen zulässig; danach "
        "bis zum Erteilungsbeschluss jede Änderung, die den Gegenstand nicht erweitert."],
       merke="§ 38 S. 1 PatG: zeitliche Grenze Erteilungsbeschluss, sachliche Grenze ursprüngliche Offenbarung.", level=1,
       concepts=["pat_unzulaessige_erweiterung"], norms=["§ 38 PatG"], abschnitt=DN),
    fall("p05i-3", "Merkmal nur in der Prioritätsunterlage",
         "Die Anmeldung DE1 offenbart, dass der Motor „einige, bevorzugt zwei“ Räder antreibt. Die Prioritätsanmeldung US1 enthält zusätzlich "
         "einen Anspruch „Motor treibt alle Räder an“. K nimmt „alle Räder“ in Anspruch 1 auf.",
         "Ist die Änderung zulässig, weil „alle Räder“ in der in Anspruch genommenen Prioritätsunterlage steht?", False,
         ["**Nein!** § 38 S. 1 PatG stellt auf den **Gegenstand der Anmeldung** ab, also den Inhalt von DE1 in der ursprünglichen Fassung. "
          "Prioritätsunterlagen sind nicht Teil der Anmeldung.",
          "DE1 offenbart „alle“ nicht unmittelbar und eindeutig; ob „einige“ auch „alle“ umfasst, ist gerade offen. Die Fassung erweitert."],
         merke="Maßstab des § 38 PatG: Anmeldung wie eingereicht, nicht die Prioritätsunterlage.", level=2,
         concepts=["pat_unzulaessige_erweiterung"], norms=["§ 38 PatG"], abschnitt=DN),
    fall("p05i-4", "Winkel aus der Zeichnung",
         "Figur 2 zeigt schematisch einen Haltearm, der etwa im Winkel von 30° absteht. Beschreibung und Ansprüche nennen keinen Winkel. Die "
         "Anmelderin nimmt „Winkel von 30°“ in Anspruch 1 auf.",
         "Ist der Winkel ursprünglich offenbart?", False,
         ["**Nein!** Schematische Zeichnungen in Patentschriften offenbaren regelmäßig nur das Prinzip, nicht exakte Abmessungen oder Winkel "
          "(BGH Steckverbindung). Ohne Stütze in Beschreibung oder Ansprüchen ist die konkrete Zahl nicht unmittelbar und eindeutig "
          "offenbart; die Änderung erweitert (§ 38 S. 1 PatG)."],
         merke="Merkmale aus Figuren: ja; Maße aus schematischen Figuren: in der Regel nein.", level=2,
         concepts=["pat_unzulaessige_erweiterung", "pat_offenbarung"], norms=["§ 38 PatG"], cases=["pat_bgh_steckverbindung"], abschnitt=DN),
    fall("p05i-5", "Magnet ohne Federklemme",
         "Im einzigen Ausführungsbeispiel hält ein Magnet die Lampe nur zusammen mit einer Federklemme, die ihn gegen Abrutschen sichert; die "
         "Beschreibung betont, dass der Magnet allein nicht genügt. Der neue Anspruch 1 nimmt nur den Magneten auf.",
         "Ist die Änderung zulässig?", False,
         ["**Nein!** Merkmale eines Ausführungsbeispiels dürfen einzeln aufgenommen werden, wenn sie je für sich den Erfolg fördern und die "
          "Kombination als Ausgestaltung der Erfindung entnehmbar ist (BGH Schleifprodukt).",
          "Hier ist der Magnet nur zusammen mit der Federklemme offenbart; der Anspruch ist eine nicht offenbarte Zwischenverallgemeinerung "
          "(§ 38 S. 1 PatG)."],
         merke="Zwischenverallgemeinerung: funktional verbundene Merkmale nicht auseinanderreißen.", level=3,
         concepts=["pat_unzulaessige_erweiterung"], norms=["§ 38 PatG"], cases=["pat_bgh_schleifprodukt"], abschnitt=DN),
    mc("p05i-6", "Enthält oder besteht aus", "Die Anmeldung offenbart ein Dichtmittel, das die Bestandteile A, B und C „enthält“. Ist „besteht "
       "aus A, B und C“ offenbart?",
       ["Ja, „besteht aus“ ist eine bloße Beschränkung und stets zulässig",
        "Nein, in der Regel nicht; es bedarf weiterer Anhaltspunkte, etwa des Hinweises, dass weitere Bestandteile unerwünscht sind",
        "Ja, wenn das Ausführungsbeispiel nur A, B und C nennt, ausnahmslos",
        "Nein, eine Änderung des Anspruchs ist nach Prüfungsantrag ausgeschlossen"], 1,
       ["**Nein, in der Regel nicht.** Dass ein Erzeugnis bestimmte Bestandteile enthalten soll, offenbart nicht ohne Weiteres, dass keine "
        "weiteren hinzukommen dürfen; dafür bedarf es weiterer Anhaltspunkte (BGH Reifenabdichtmittel). Sonst erweitert die Fassung "
        "(§ 38 S. 1 PatG)."],
       merke="„Enthält“ offenbart nicht ohne Weiteres „besteht aus“.", level=2,
       concepts=["pat_unzulaessige_erweiterung"], norms=["§ 38 PatG"], cases=["pat_bgh_reifenabdichtmittel"], abschnitt=DN),
    fall("p05i-7", "Kein Hilfsantrag",
         "Der Anmelder verteidigt nur einen Anspruch 1 mit einem nicht ursprünglich offenbarten Merkmal. Hilfsanträge stellt er trotz Rüge "
         "nicht. Der ursprüngliche Anspruch 1 wäre gewährbar.",
         "Darf die Prüfungsstelle das Patent mit dem ursprünglichen Anspruch 1 erteilen?", False,
         ["**Nein!** Die Prüfungsstelle erteilt nur in einer vom Anmelder beantragten Fassung (§ 49 Abs. 1 PatG). Geht der zur Prüfung "
          "gestellte Anspruch über die ursprüngliche Offenbarung hinaus, ist die Anmeldung zurückzuweisen (§ 48 S. 1 PatG); der Anmelder kann "
          "keine Erteilung mit einem anderen, zulässigen Anspruch verlangen (BGH Phosphatidylcholin)."],
         merke="Keine Erteilung gegen den Antrag: Hilfsanträge stellen!", level=2,
         concepts=["pat_unzulaessige_erweiterung", "pat_beschluss_pruefungsstelle"], norms=["§ 48 PatG", "§ 49 PatG"],
         cases=["pat_bgh_phosphatidylcholin"], abschnitt=DN),
    mc("p05i-8", "Übersehene Erweiterung nach Erteilung",
       "Die Prüfungsstelle übersieht, dass ein nur beschränkendes Merkmal nicht ursprünglich offenbart ist. Was gilt im Einspruchsverfahren?",
       ["Das Patent ist zwingend vollständig zu widerrufen",
        "Das Merkmal kann im Anspruch bleiben, darf aber bei der Patentfähigkeit nicht zugunsten des Inhabers berücksichtigt werden",
        "Die Erweiterung ist mit der Erteilung geheilt",
        "Das Merkmal wird von Amts wegen gestrichen, auch wenn der Schutzbereich dadurch größer wird"], 1,
       ["**Uneigentliche Erweiterung.** § 21 Abs. 1 Nr. 4 PatG ist Widerrufsgrund. Beschränkt das nicht offenbarte Merkmal den Anspruch nur "
        "(kein Aliud), bleibt es im Anspruch, wird aber bei der Prüfung der Patentfähigkeit nicht zugunsten des Inhabers berücksichtigt "
        "(BGH Winkelmesseinrichtung)."],
       merke="Erweiterung nach Erteilung: § 21 Abs. 1 Nr. 4 PatG; nur beschränkendes Merkmal: uneigentliche Erweiterung.", level=3,
       concepts=["pat_unzulaessige_erweiterung", "pat_widerrufsgruende"], norms=["§ 21 PatG"], cases=["pat_bgh_winkelmesseinrichtung"],
       abschnitt=DN),
    *fallkette("p05i-9", "Kraftfahrzeug DE1 (nach TS III/2023)",
        "DE1 wurde englisch eingereicht; Anspruch 1: Kfz mit Motor, Bremse und mindestens vier Rädern, von denen der Motor „einige, bevorzugt "
        "zwei“ antreibt. E2 nimmt das vorweg. Nach dem Prüfungsantrag reicht K einen englischen Anspruch „Motor treibt alle Räder an“ ein; "
        "„alle“ steht nur in der Prioritätsanmeldung US1.",
        [frage("Sind Änderungen nach dem Prüfungsantrag bis zum Erteilungsbeschluss grundsätzlich zulässig?", True,
               ["**Ja!** Nach Eingang des Prüfungsantrags ist bis zum Beschluss über die Erteilung jede Änderung zulässig, die den Gegenstand "
                "nicht erweitert (§ 38 S. 1 PatG)."],
               merke="Zeitgrenze: Erteilungsbeschluss (§ 38 S. 1 PatG).", titel="V1 Zeitpunkt"),
         frage("Ist der englische Anspruch sofort zu berücksichtigen?", False,
               ["**Nein!** Die Sprache vor dem DPMA ist deutsch (§ 126 PatG). § 35a PatG lässt nur die Anmeldung selbst fremdsprachig zu, nicht "
                "spätere Änderungen. Zu berücksichtigen ist der Anspruch erst ab Eingang einer deutschen Fassung."],
               merke="Änderungen deutsch einreichen (§ 126 PatG).", titel="V2 Sprache", level=3),
         frage("Ist „alle Räder“ ursprünglich offenbart?", False,
               ["**Nein!** Maßstab ist DE1 in der ursprünglichen (englischen) Fassung, nicht US1. DE1 nennt nur „einige, bevorzugt zwei“. Umfasst "
                "„einige“ nicht „alle“, ist die Änderung ein Aliud; umfasst es „alle“, ist diese Auswahl nicht offenbart. Beides erweitert "
                "(§ 38 S. 1 PatG)."],
               merke="Auswahl aus einem Oberbegriff muss selbst offenbart sein.", titel="V3 Keine Erweiterung",
               cases=["pat_bgh_faelschungssicheres_dokument"]),
         frage("Kann K stattdessen „Kfz mit Elektromotor und Bremse“ beanspruchen und Räder und Antrieb weglassen?", False,
               ["**Nein!** Den Elektromotor nennt nur US2, DE1 spricht allgemein vom Motor. Das Weglassen ist ebenfalls unzulässig: DE1 offenbart "
                "Motor und Bremse nur zusammen mit den vier Rädern und dem Antrieb; weist jede Ausführung ein Merkmal auf, das die Lösung voraussetzt, "
                "ist Schutz ohne es nicht offenbart (BGH Digitales Buch, X ZR 63/15)."],
               merke="Weglassen von Merkmalen = Verallgemeinerung; nur zulässig, wenn als Erfindung offenbart.", titel="V3.3 Weglassen"),
         frage("Was droht, wenn K nur an dieser Fassung festhält?", 0,
               ["**Zurückweisung der ganzen Anmeldung** (§ 48 S. 1 PatG). Die Prüfungsstelle ist an den Antrag gebunden (§ 49 Abs. 1 PatG) und "
                "erteilt nicht mit einer anderen Fassung (BGH Phosphatidylcholin). Dagegen Beschwerde (§ 73 Abs. 1 PatG)."],
               optionen=["Zurückweisung der Anmeldung", "Erteilung mit dem ursprünglichen Anspruch 1",
                         "Erteilung, aber ohne Rechte aus dem erweiternden Merkmal (§ 38 S. 2 PatG)", "Aussetzung bis zur Klärung der Priorität"],
               merke="Unzulässige Fassung ohne Hilfsantrag: Zurückweisung.", titel="V4 Antrag", cases=["pat_bgh_phosphatidylcholin"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_unzulaessige_erweiterung"], norms=["§ 38 PatG"]),
    *fallkette("p05i-10", "Japanische Stammanmeldung (nach TS I/2021)",
        "Die Stammanmeldung wurde japanisch eingereicht, eine deutsche Übersetzung liegt vor. Kurz vor Ablauf der Beschwerdefrist gegen die "
        "Zurückweisung teilt die Anmelderin und reicht für die Teilanmeldung Ansprüche ein, die Merkmale der Beschreibung neu kombinieren.",
        [frage("Ist Maßstab der Erweiterungsprüfung die deutsche Übersetzung der Stammanmeldung?", False,
               ["**Nein!** Maßstab ist die Stammanmeldung in der Fassung, in der sie ursprünglich eingereicht worden ist (§ 21 Abs. 1 Nr. 4 Hs. 2 "
                "PatG), also die japanische. Die Übersetzung ist Arbeitsgrundlage des Verfahrens."],
               merke="Teilanmeldung: Maßstab Stammanmeldung, ursprüngliche Fassung.", titel="V3 Maßstab", norms=["§ 21 PatG"]),
         frage("Macht ein nicht offenbartes Merkmal die Teilungserklärung unwirksam?", False,
               ["**Nein!** Die Teilungserklärung gilt nur als nicht abgegeben, wenn Unterlagen oder Gebühren nicht binnen drei Monaten eingehen "
                "(§ 39 Abs. 3 PatG). Ein nicht offenbartes Merkmal ist ein Mangel nach § 38 PatG: Rüge (§ 45 Abs. 1 S. 1 PatG), bei Festhalten "
                "Zurückweisung (§ 48 S. 1 PatG)."],
               merke="Erweiterung betrifft die Zulässigkeit der Fassung, nicht die Wirksamkeit der Teilung.", titel="Wirksamkeit der Teilung",
               norms=["§ 39 PatG"]),
         frage("Muss die Prüfungsstelle vor der Zurückweisung der neuen Ansprüche Gelegenheit zur Äußerung geben?", True,
               ["**Ja!** Über bisher nicht geprüfte Ansprüche darf sie nicht ohne vorherige Mitteilung der Gründe entscheiden (§ 45 Abs. 2 PatG, "
                "§ 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG). Die Anmelderin sollte zugleich schriftlich Anhörung beantragen (§ 46 Abs. 1 S. 3 "
                "PatG)."],
               merke="Neuer Prüfungsstoff = neuer Bescheid.", titel="Rechtliches Gehör", norms=["§ 45 PatG", "§ 48 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_unzulaessige_erweiterung", "pat_teilung"], norms=["§ 38 PatG"]),
])

# ====================================================================================================== p05j § 39 PatG
K_J = dict(id="p05j", titel="§ 39 PatG: Teilung der Anmeldung", einheiten=[
    intro("p05j-0", "Prüfungsschema",
          "**AGL:** § 39 Abs. 1 S. 1 PatG (Teilungserklärung); Wirksamkeit § 39 Abs. 3 PatG\n\n"
          "**V1 Anhängige Anmeldung** – § 39 Abs. 1 S. 1 PatG „jederzeit“: bis zur Erteilung und nach Erteilungs- oder Zurückweisungsbeschluss "
          "bis zum Ablauf der Beschwerdefrist, auch ohne Beschwerde (BGH Graustufenbild, X ZB 36/98); während Beschwerde und Rechtsbeschwerde "
          "(BGH Abstandsberechnungsverfahren, X ZB 9/18); nicht nach Rücknahme, Rücknahmefiktion oder Bestandskraft der Zurückweisung · "
          "Beschwerdefrist § 73 Abs. 2 S. 1 PatG · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB\n"
          "**V2 Erklärung** – schriftlich (§ 39 Abs. 1 S. 2 PatG), elektronisch nach § 125a Abs. 1 PatG i.V.m. § 130a ZPO; gegenüber dem DPMA, "
          "nach Einlegung der Beschwerde gegenüber dem BPatG (BGH Abstandsberechnungsverfahren); kein gegenständlich bestimmter Teil nötig "
          "(BGH Sammelhefter, zur Patentteilung nach § 60 PatG a.F.)\n"
          "**V3 Unterlagen binnen drei Monaten** – Unterlagen nach § 34 PatG, § 35 PatG, § 35a PatG, § 36 PatG binnen drei Monaten nach Eingang "
          "der Teilungserklärung (§ 39 Abs. 3 PatG) · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB\n"
          "**V4 Gebühren binnen drei Monaten** – für die Zeit bis zur Teilung die gleichen Gebühren wie für die Stammanmeldung (§ 39 Abs. 2 S. 1 "
          "PatG): Anmeldegebühr nach der Anspruchszahl der Stammanmeldung (BPatG Gebühren für die Teilanmeldung I, 7 W (pat) 30/15), "
          "Prüfungsgebühr, wenn der Prüfungsantrag gestellt war (§ 39 Abs. 1 S. 3 PatG), bis zur Teilung fällig gewordene Jahresgebühren; "
          "Recherchegebühr nicht, wenn vor dem Prüfungsantrag geteilt und kein neuer Rechercheantrag gestellt wird (§ 39 Abs. 2 S. 2 PatG); "
          "unbezahlte Mehranspruchsgebühren sind unschädlich (BGH Schwammkörper, X ZB 6/17) · Zahlungstag § 2 PatKostZV\n\n"
          "**⇒ Rechtsfolge:** selbständige Teilanmeldung mit Anmeldetag und Priorität der Stammanmeldung (§ 39 Abs. 1 S. 4 PatG); Prüfungsantrag "
          "gilt als gestellt, wenn nach dem Prüfungsantrag geteilt (§ 39 Abs. 1 S. 3 PatG); Fortführung im Verfahrensstand der Stammanmeldung; "
          "Inhalt darf nicht über die Stammanmeldung in der ursprünglichen Fassung hinausgehen (§ 38 S. 1 PatG, § 21 Abs. 1 Nr. 4 Hs. 2 PatG). "
          "Fehlen Unterlagen oder Gebühren: Teilungserklärung gilt als nicht abgegeben (§ 39 Abs. 3 PatG)\n\n"
          "**Klausurfallen:** Teilung ersetzt die Beschwerde nicht: Die zurückgewiesene Stammanmeldung wird mit Ablauf der Beschwerdefrist "
          "bestandskräftig. Neue Merkmale machen die Teilung nicht unwirksam. Nach wirksamer Rücknahme ist nichts mehr teilbar. Die Teilanmeldung "
          "kann ohne neuen Bescheid zurückgewiesen werden, wenn sie die schon beanstandeten Ansprüche enthält. Teilung und Abzweigung eines "
          "Gebrauchsmusters (§ 5 Abs. 1 GebrMG) laufen nebeneinander.\n\n"
          "**In den Klausuren:** TS I/2021 (Teilung in letzter Minute), TS III/2020 (zwei Teilanmeldungen), TS III/2023, TS II/2022, "
          "TS I/2020 (Entschädigung aus der Teilanmeldung).",
          concepts=["pat_teilung"], norms=["§ 39 PatG", "§ 38 PatG", "§ 73 PatG"], cases=["pat_bgh_sammelhefter"], abschnitt="Normenkette"),
    intro("p05j-1", "Definitionen",
          "**Teilung:** einseitige, schriftliche Erklärung des Anmelders, mit der aus der anhängigen Anmeldung eine selbständige Teilanmeldung "
          "abgetrennt wird (§ 39 Abs. 1 S. 1, 2 PatG)\n"
          "**Teilanmeldung:** eigenständiger Verfahrensgegenstand mit Zeitrang und Priorität der Stammanmeldung (§ 39 Abs. 1 S. 4 PatG); sie wird "
          "in der Verfahrenslage weitergeführt, in der sich die Stammanmeldung bei der Teilung befand, deren Bescheide gelten als in ihr erlassen "
          "(BPatG Prüfungsbescheid in Nachanmeldung, 20 W (pat) 28/09)\n"
          "**Anhängigkeit:** Die Anmeldung ist weder zurückgenommen noch gilt sie als zurückgenommen noch ist sie bestandskräftig zurückgewiesen "
          "oder erteilt; nach dem Beschluss dauert sie bis zum Ablauf der Beschwerdefrist (BGH Graustufenbild)\n"
          "**Ausscheidung:** Abtrennung eines uneinheitlichen Teils auf Beanstandung der Prüfungsstelle (§ 34 Abs. 5 PatG), mit eigenen Gebühren "
          "(BPatG Prüfungsgebühr für Ausscheidungsanmeldung); anders als die Teilung nicht frei gewählt\n"
          "**Fiktion der Nichtabgabe:** Werden Unterlagen oder Gebühren nicht binnen drei Monaten nach Eingang der Teilungserklärung eingereicht, "
          "gilt die Teilungserklärung als nicht abgegeben (§ 39 Abs. 3 PatG); die Stammanmeldung bleibt unverändert",
          concepts=["pat_teilung", "pat_einheitlichkeit"], norms=["§ 39 PatG", "§ 34 PatG"], cases=["pat_bpatg_pruefungsgebuehr_ausscheidung"],
          abschnitt="Definitionen"),
    mc("p05j-2", "Teilung nach Zurückweisung", "Bis wann kann der Anmelder nach Zustellung eines Zurückweisungsbeschlusses noch teilen?",
       ["bis zur Zustellung des Zurückweisungsbeschlusses",
        "bis zum Ablauf der Beschwerdefrist, auch wenn er keine Beschwerde einlegt",
        "nur zusammen mit einer Beschwerde",
        "bis zu drei Monate nach Bestandskraft"], 1,
       ["**Bis zum Ablauf der Beschwerdefrist.** „Jederzeit“ (§ 39 Abs. 1 S. 1 PatG) heißt: solange die Anmeldung anhängig ist. Die Möglichkeit "
        "der Teilung bleibt bis zum Ablauf der Beschwerdefrist erhalten, unabhängig davon, ob Beschwerde eingelegt wird (BGH Graustufenbild, "
        "X ZB 36/98). Frist: ein Monat nach Zustellung (§ 73 Abs. 2 S. 1 PatG)."],
       merke="Teilung: bis Ablauf der Beschwerdefrist (§ 39 Abs. 1 S. 1 PatG, § 73 Abs. 2 S. 1 PatG).", level=1,
       concepts=["pat_teilung"], norms=["§ 39 PatG", "§ 73 PatG"], abschnitt=DN),
    fall("p05j-3", "Teilung während der Beschwerde",
         "Die Anmelderin hat gegen die Zurückweisung Beschwerde eingelegt; das Verfahren liegt beim BPatG. Sie will nun teilen.",
         "Ist die Teilung gegenüber dem DPMA zu erklären?", False,
         ["**Nein!** Sobald Beschwerde eingelegt und das Verfahren beim Patentgericht anhängig ist, ist die Teilung gegenüber dem **BPatG** zu "
          "erklären, bei dem auch die Prüfung der Teilanmeldung anfällt; geteilt werden kann sogar noch während der Rechtsbeschwerde (BGH "
          "Abstandsberechnungsverfahren, X ZB 9/18)."],
         merke="Adressat der Teilung: dort, wo die Anmeldung anhängig ist.", level=2, concepts=["pat_teilung"], norms=["§ 39 PatG"],
         abschnitt=DN),
    mc("p05j-4", "Frist für Unterlagen und Gebühren", "Bis wann sind Unterlagen und Gebühren der Teilanmeldung einzureichen, und was gilt sonst?",
       ["ein Monat nach Teilung; sonst wird die Teilanmeldung zurückgewiesen",
        "drei Monate nach Eingang der Teilungserklärung; sonst gilt die Teilungserklärung als nicht abgegeben",
        "drei Monate nach Fälligkeit; sonst gilt die Stammanmeldung als zurückgenommen",
        "bis zum Prüfungsbescheid; sonst Weiterbehandlung"], 1,
       ["**§ 39 Abs. 3 PatG.** Drei Monate nach Eingang der Teilungserklärung müssen die Unterlagen nach § 34 PatG, § 35 PatG, § 35a PatG, "
        "§ 36 PatG und die Gebühren (§ 39 Abs. 2 PatG) vorliegen. Sonst gilt die Teilungserklärung als nicht abgegeben; die Stammanmeldung "
        "bleibt, wie sie war. Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB."],
       merke="Teilung: Unterlagen + Gebühren drei Monate (§ 39 Abs. 3 PatG).", level=1, concepts=["pat_teilung"], norms=["§ 39 PatG"],
       abschnitt=DN),
    fall("p05j-5", "Mehr Ansprüche in der Teilanmeldung",
         "Die Stammanmeldung hatte zehn Ansprüche. Die Teilanmeldung reicht fristgerecht 14 Ansprüche ein; die Anmelderin zahlt die Gebühren der "
         "Stammanmeldung, nicht aber die Gebühr für die vier zusätzlichen Ansprüche.",
         "Gilt die Teilungserklärung als nicht abgegeben?", False,
         ["**Nein!** Zu zahlen sind „für die Zeit bis zur Teilung“ die Gebühren der Stammanmeldung (§ 39 Abs. 2 S. 1 PatG). Die Teilungserklärung "
          "gilt nicht deshalb als nicht abgegeben, weil Gebühren für eine erhöhte Anspruchszahl ausbleiben (BGH Schwammkörper, X ZB 6/17). Die "
          "Mehrgebühr folgt § 3 Abs. 1 S. 2 Nr. 5 PatKostG."],
         merke="§ 39 Abs. 3 PatG: nur die Gebühren der Stammanmeldung sind wirksamkeitsrelevant.", level=3,
         concepts=["pat_teilung", "pat_gebuehren"], norms=["§ 39 PatG", "§ 3 PatKostG"], abschnitt=DN),
    fall("p05j-6", "Recherchegebühr für die Teilanmeldung",
         "In der Stammanmeldung wurden Rechercheantrag gestellt und 300 EUR gezahlt; ein Prüfungsantrag ist nicht gestellt. Die Anmelderin teilt "
         "und stellt für die Teilanmeldung keinen eigenen Rechercheantrag.",
         "Muss sie für die Teilanmeldung die Recherchegebühr zahlen?", False,
         ["**Nein!** Grundsätzlich sind die Gebühren der Stammanmeldung nachzuzahlen (§ 39 Abs. 2 S. 1 PatG). Das gilt nicht für die "
          "Recherchegebühr (§ 43 PatG), wenn die Teilung vor dem Prüfungsantrag erklärt wird, es sei denn, für die Teilanmeldung wird ebenfalls "
          "Recherche beantragt (§ 39 Abs. 2 S. 2 PatG)."],
         merke="Recherchegebühr nur bei Teilung nach Prüfungsantrag oder neuem Rechercheantrag (§ 39 Abs. 2 S. 2 PatG).", level=2,
         concepts=["pat_teilung", "pat_gebuehren"], norms=["§ 39 PatG"], abschnitt=DN),
    fall("p05j-7", "Teilung statt Beschwerde",
         "Die Prüfungsstelle weist die Stammanmeldung zurück. Die Anmelderin erklärt innerhalb der Beschwerdefrist nur die Teilung, legt aber "
         "keine Beschwerde ein.",
         "Bleibt die Stammanmeldung anhängig?", False,
         ["**Nein!** Die Teilung lässt die Zurückweisung der Stammanmeldung unberührt; sie wird mit Ablauf der Beschwerdefrist bestandskräftig "
          "(§ 73 Abs. 2 S. 1 PatG). Weiter läuft nur die Teilanmeldung als eigenes Verfahren mit Zeitrang der Stammanmeldung "
          "(§ 39 Abs. 1 S. 4 PatG). Wer beides offenhalten will, legt zusätzlich Beschwerde ein (200 EUR, Nr. 401 300 GV PatKostG)."],
         merke="Teilung ≠ Rechtsmittel: Stammanmeldung nur mit Beschwerde retten.", level=2, concepts=["pat_teilung", "pat_beschwerde"],
         norms=["§ 39 PatG", "§ 73 PatG"], abschnitt=DN),
    *fallkette("p05j-8", "Teilung in letzter Minute (nach TS I/2021)",
        "Die Anmeldung vom 24.09.2018 (Priorität 27.09.2017) wird zurückgewiesen; der Beschluss wird am Fr 17.07.2020 zugestellt. Am "
        "Mo 17.08.2020 um 23:30 Uhr erklärt die Anmelderin über das elektronische Postfach des DPMA die Teilung. Beschwerde legt sie nicht ein.",
        [frage("Ist die Anmeldung am Mo 17.08.2020 noch teilbar?", True,
               ["**Ja!** Die Anmeldung ist bis zum Ablauf der Beschwerdefrist anhängig (BGH Graustufenbild). Die Frist von einem Monat nach "
                "Zustellung (§ 73 Abs. 2 S. 1 PatG) endet am Mo 17.08.2020 (§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB)."],
               merke="„Jederzeit“ = solange anhängig.", titel="V1 Anhängigkeit", norms=["§ 73 PatG"]),
         frage("Wahrt die Erklärung um 23:30 Uhr über das elektronische Postfach die Schriftform?", True,
               ["**Ja!** Die Teilung ist schriftlich zu erklären (§ 39 Abs. 1 S. 2 PatG); ein elektronisches Dokument genügt (§ 125a Abs. 1 PatG "
                "i.V.m. § 130a ZPO). Eingegangen ist es, sobald es auf dem Server des DPMA gespeichert ist (§ 130a Abs. 5 ZPO)."],
               merke="Schriftform elektronisch: § 125a Abs. 1 PatG i.V.m. § 130a ZPO.", titel="V2 Form", norms=["§ 125a PatG"]),
         frage("Bis wann müssen Unterlagen und Gebühren der Teilanmeldung eingehen?", 2,
               ["**Di 17.11.2020.** Drei Monate nach Eingang der Teilungserklärung (§ 39 Abs. 3 PatG; § 187 Abs. 1 BGB, § 188 Abs. 2 BGB); "
                "Zahlungstag § 2 PatKostZV."],
               optionen=["Mo 17.08.2020", "Do 17.09.2020", "Di 17.11.2020", "Mi 17.02.2021"],
               merke="Unterlagen und Gebühren: drei Monate ab Eingang der Erklärung.", titel="V3, V4 Frist"),
         frage("Muss mit diesen Gebühren schon die Jahresgebühr für das 3. Jahr gezahlt werden?", False,
               ["**Nein!** § 39 Abs. 2 S. 1 PatG erfasst nur Gebühren „für die Zeit bis zur Teilung“. Die 3. Jahresgebühr wird erst am "
                "Mi 30.09.2020 fällig (§ 3 Abs. 2 S. 1 PatKostG), also nach der Teilung, und ist dann regulär für die Teilanmeldung zu zahlen "
                "(§ 7 Abs. 1 PatKostG)."],
               merke="Nachzahlen nur, was bis zur Teilung fällig war.", titel="V4 Gebühren", norms=["§ 39 PatG", "§ 3 PatKostG"]),
         frage("Bleibt die Stammanmeldung anhängig?", False,
               ["**Nein!** Ohne Beschwerde ist sie mit Ablauf des Mo 17.08.2020 bestandskräftig zurückgewiesen. Die Teilanmeldung behält AT "
                "24.09.2018 und Priorität 27.09.2017 (§ 39 Abs. 1 S. 4 PatG); der Prüfungsantrag gilt als gestellt (§ 39 Abs. 1 S. 3 PatG)."],
               merke="Teilanmeldung: AT und Priorität bleiben (§ 39 Abs. 1 S. 4 PatG).", titel="Rechtsfolge"),
         ],
        abschnitt=KF, level=2, concepts=["pat_teilung"], norms=["§ 39 PatG"]),
    *fallkette("p05j-9", "Zwei Teilanmeldungen des Druckers (nach TS III/2020)",
        "Nach Bescheid, Ladungszusatz zur Druckschrift D2 und Anhörung teilt der Anmelder die Anmeldung zweimal. Teilanmeldung 1 enthält die "
        "unveränderten ursprünglichen Ansprüche, Teilanmeldung 2 einen Anspruch mit einem Merkmal, das in der Stammanmeldung nicht offenbart ist. "
        "Unterlagen und Gebühren gehen fristgerecht ein.",
        [frage("Darf die Prüfungsstelle Teilanmeldung 1 ohne neuen Bescheid zurückweisen?", True,
               ["**Ja!** Die Teilanmeldung wird im Verfahrensstand der Stammanmeldung fortgeführt; Bescheid, Ladungszusatz und Anhörung betrafen "
                "genau diese Ansprüche. Neue Umstände, die erst mitzuteilen wären (§ 48 S. 2 PatG i.V.m. § 42 Abs. 3 S. 2 PatG), gibt es nicht."],
               merke="Unveränderte Ansprüche: bekannte Gründe tragen die Zurückweisung.", titel="Teilanmeldung 1", norms=["§ 48 PatG"]),
         frage("Ist die Teilung für Teilanmeldung 2 unwirksam?", False,
               ["**Nein!** Unwirksam ist sie nur unter den Voraussetzungen des § 39 Abs. 3 PatG; Unterlagen und Gebühren sind eingegangen. Das neue "
                "Merkmal betrifft die Zulässigkeit der Fassung (§ 38 S. 1 PatG)."],
               merke="§ 39 Abs. 3 PatG abschließend: nur Unterlagen und Gebühren.", titel="Teilanmeldung 2: Wirksamkeit"),
         frage("Wie verfährt die Prüfungsstelle mit Teilanmeldung 2?", 0,
               ["**Rüge mit Frist zur Streichung** (§ 45 Abs. 1 S. 1 PatG i.V.m. § 38 PatG), bei Festhalten Zurückweisung (§ 48 S. 1 PatG). Aus "
                "der Erweiterung können keine Rechte hergeleitet werden (§ 38 S. 2 PatG); eine Erteilung mit ihr ist ausgeschlossen."],
               optionen=["Rüge nach § 45 Abs. 1 S. 1 PatG, bei Festhalten Zurückweisung",
                         "Feststellung, dass die Teilungserklärung als nicht abgegeben gilt",
                         "Erteilung mit Hinweis auf § 38 S. 2 PatG", "Aussetzung bis zur Entscheidung über die Stammanmeldung"],
               merke="Erweiterung in der Teilanmeldung: Rüge, dann Zurückweisung.", titel="Teilanmeldung 2: Verfahren", norms=["§ 45 PatG", "§ 38 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_teilung", "pat_unzulaessige_erweiterung"], norms=["§ 39 PatG"]),
])

# ====================================================================================================== p05k Priorität
K_K = dict(id="p05k", titel="§§ 40, 41 PatG, Art. 4 PVÜ, Art. 87 EPÜ: Priorität", einheiten=[
    intro("p05k-0", "Prüfungsschema",
          "**AGL:** innere Priorität § 40 Abs. 1 PatG; Auslandspriorität Art. 4 A Abs. 1 PVÜ i.V.m. § 41 Abs. 1 PatG; europäische Nachanmeldung "
          "Art. 87 Abs. 1 EPÜ; internationale Anmeldung Art. 8 PCT i.V.m. Art. III § 4 IntPatÜG\n\n"
          "**V1 Prioritätsbegründende Voranmeldung** – innere Priorität: frühere Patent- oder Gebrauchsmusteranmeldung beim DPMA, für die nicht "
          "schon eine Priorität in Anspruch genommen worden ist (§ 40 Abs. 1 PatG; Verbot der Kettenpriorität); Auslandspriorität: "
          "vorschriftsmäßige erste Hinterlegung in einem Verbandsstaat (Art. 4 A Abs. 1, 3 PVÜ, Art. 4 C Abs. 2, 4 PVÜ); das spätere Schicksal "
          "der Voranmeldung ist unerheblich (Art. 4 A Abs. 3 PVÜ, Art. 87 Abs. 3 EPÜ)\n"
          "**V2 Berechtigung** – Anmelder der Voranmeldung oder sein Rechtsnachfolger (§ 40 Abs. 1 PatG „dem Anmelder“, Art. 4 A Abs. 1 PVÜ, "
          "Art. 87 Abs. 1 EPÜ); Übertragung formlos, aber vor der Nachanmeldung (BGH Fahrzeugscheibe); vor dem EPA widerlegbare Vermutung der "
          "Berechtigung, auch bei gemeinsamer PCT-Anmeldung (EPA G 1/22); im Nichtigkeitsverfahren Darlegungs- und Beweislast beim Kläger "
          "(BGH Sorafenib-Tosylat)\n"
          "**V3 Dieselbe Erfindung** – nur für Merkmale, die in der Gesamtheit der Unterlagen der Voranmeldung deutlich offenbart sind "
          "(§ 40 Abs. 3 PatG, Art. 4 H PVÜ); die Prioritätsunterlagen müssen die Gesamtheit der Anspruchsmerkmale offenbaren (BGH "
          "UV-unempfindliche Druckplatte, X ZR 3/10); Maßstab wie bei der unzulässigen Erweiterung (BGH Kommunikationskanal; EPA G 2/98); "
          "Mehrfachpriorität (§ 40 Abs. 2 PatG, Art. 4 F PVÜ, Art. 88 Abs. 2 EPÜ) und Teilpriorität für abgrenzbare Alternativen (EPA G 1/15), "
          "aber kein Mosaik mehrerer Voranmeldungen in einem Anspruch\n"
          "**V4 Prioritätsfrist zwölf Monate** – § 40 Abs. 1 PatG; Art. 4 C Abs. 1 PVÜ; Art. 87 Abs. 1 EPÜ · Berechnung Art. 4 C Abs. 2 PVÜ, "
          "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB (EPA: R. 131 Abs. 2, 4 EPÜ) · Verschiebung Art. 4 C Abs. 3 PVÜ, § 193 BGB (EPA: R. 134 Abs. 1 "
          "EPÜ); innere Priorität: keine Wiedereinsetzung in die Nachanmeldefrist (§ 123 Abs. 1 S. 2 Nr. 3 PatG); Auslandspriorität: "
          "Wiedereinsetzung möglich, § 123 Abs. 7 PatG setzt sie voraus\n"
          "**V5 Prioritätserklärung** – innere Priorität binnen zwei Monaten nach dem Anmeldetag der Nachanmeldung, abgegeben erst mit dem "
          "Aktenzeichen der Voranmeldung (§ 40 Abs. 4 PatG); Auslandspriorität: Zeit, Land, Aktenzeichen und Abschrift vor Ablauf des "
          "16. Monats nach dem Prioritätstag, sonst Verwirkung (§ 41 Abs. 1 S. 1, 3 PatG); EPA: R. 52 Abs. 2 EPÜ\n\n"
          "**⇒ Rechtsfolge:** Zeitrang des Prioritätstags für die prioritätsbegründend offenbarten Merkmale (§ 3 Abs. 1 S. 2 PatG; Art. 89 EPÜ); "
          "maßgeblich auch für das Vorbenutzungsrecht (§ 12 Abs. 2 PatG). Innere Priorität: die noch anhängige frühere Patentanmeldung gilt mit "
          "Abgabe der Erklärung als zurückgenommen (§ 40 Abs. 5 S. 1 PatG), eine frühere Gebrauchsmusteranmeldung nicht (§ 40 Abs. 5 S. 2 PatG); "
          "bei internationaler Nachanmeldung erst mit Erfüllung der Voraussetzungen des Art. III § 4 Abs. 2 IntPatÜG und Ablauf der 31 Monate "
          "(Art. III § 4 Abs. 4 IntPatÜG); europäische Nachanmeldung: keine Rücknahmefiktion\n\n"
          "**Klausurfallen:** Was erst nach dem Prioritätstag offenbart ist, hat nur den Anmeldetag. Eine Voranmeldung ohne Anmeldetag begründet "
          "keine Priorität (TS III/2020). Die Abschrift der Voranmeldung kommt mit der Akteneinsicht zu den Akten der Nachanmeldung (§ 40 Abs. 6 "
          "PatG) und ist dann öffentlich zugänglich (BGH Gesperre, X ZR 36/21). Das Prioritätsrecht aus einer Voranmeldung kann für mehrere "
          "Nachanmeldungen genutzt werden.\n\n"
          "**In den Klausuren:** TS III/2023 (zwei US-Prioritäten, Mosaik), TS II/2022 (innere Priorität), TS III/2020 (innere Priorität ohne "
          "Anmeldetag), TS III/2022 (PCT, Art. III § 4 Abs. 4 IntPatÜG), TS III/2021 (EP, DE, GebrM-Nachanmeldung), TS III/2018 "
          "(Prioritätsberechtigung, Art. 87 EPÜ), TS II/2019 und TS II/2018 (Auslandsanmeldungen).",
          concepts=["pat_prioritaet", "pat_pct_nationale_phase"], norms=["§ 40 PatG", "§ 41 PatG", "Art. 87 EPÜ", "Art. III § 4 IntPatÜG"],
          cases=["pat_bgh_fahrzeugscheibe", "pat_bgh_kommunikationskanal", "pat_bgh_sorafenib_tosylat", "epc_g_1_22", "epc_g_2_98"],
          abschnitt="Normenkette"),
    intro("p05k-1", "Definitionen",
          "**Prioritätsrecht:** Recht, für die Nachanmeldung derselben Erfindung den Zeitrang einer früheren Anmeldung in Anspruch zu nehmen "
          "(§ 40 Abs. 1 PatG; Art. 4 A Abs. 1, Art. 4 B PVÜ)\n"
          "**Dieselbe Erfindung:** Der Fachmann kann den Gegenstand des Anspruchs unter Heranziehung des allgemeinen Fachwissens unmittelbar und "
          "eindeutig der Voranmeldung als Ganzes entnehmen (EPA G 2/98); national: die Merkmale sind in der Gesamtheit der Unterlagen der "
          "Voranmeldung deutlich offenbart (§ 40 Abs. 3 PatG; BGH UV-unempfindliche Druckplatte)\n"
          "**Vorschriftsmäßige Hinterlegung:** jede Hinterlegung, die zur Festlegung des Anmeldetags ausreicht, ohne Rücksicht auf ihr späteres "
          "Schicksal (Art. 4 A Abs. 3 PVÜ, Art. 87 Abs. 3 EPÜ)\n"
          "**Erste Anmeldung:** Die Frist läuft ab der ersten Anmeldung derselben Erfindung (Art. 4 C Abs. 2 PVÜ); eine spätere Anmeldung gilt nur "
          "unter den Voraussetzungen des Art. 4 C Abs. 4 PVÜ als erste\n"
          "**Mehrfachpriorität:** Prioritäten mehrerer Voranmeldungen für verschiedene Merkmale oder Ansprüche einer Nachanmeldung (§ 40 Abs. 2 "
          "PatG, Art. 4 F PVÜ)\n"
          "**Teilpriorität:** Priorität für die alternativen Gegenstände eines generischen „Oder“-Anspruchs, die in der Voranmeldung erstmals, "
          "unmittelbar oder zumindest implizit, eindeutig und ausführbar offenbart sind (EPA G 1/15)\n"
          "**Kettenpriorität:** Inanspruchnahme einer Voranmeldung, die ihrerseits schon eine Priorität beansprucht; für die innere Priorität "
          "ausgeschlossen (§ 40 Abs. 1 Hs. 2 PatG)\n"
          "**Prioritätstag:** Anmeldetag der Voranmeldung; er tritt für den Stand der Technik an die Stelle des Anmeldetags (§ 3 Abs. 1 S. 2 PatG: "
          "„für den Zeitrang der Anmeldung maßgeblicher Tag“)",
          concepts=["pat_prioritaet"], norms=["§ 40 PatG", "§ 41 PatG", "Art. 87 EPÜ"], cases=["epc_g_2_98", "epc_g_1_15"],
          abschnitt="Definitionen"),
    mc("p05k-2", "Wiedereinsetzung in die Prioritätsfrist", "In welche Prioritätsfrist ist Wiedereinsetzung ausgeschlossen?",
       ["in die Zwölfmonatsfrist der Auslandspriorität nach Art. 4 C Abs. 1 PVÜ",
        "in die Frist zur Einreichung der Nachanmeldung bei innerer Priorität (§ 40 PatG)",
        "in die Sechzehnmonatsfrist des § 41 Abs. 1 PatG",
        "in keine, Prioritätsfristen sind stets wiedereinsetzungsfähig"], 1,
       ["**§ 123 Abs. 1 S. 2 Nr. 3 PatG.** Ausgeschlossen ist die Wiedereinsetzung in die Frist zur Einreichung von Anmeldungen, für die eine "
        "Priorität nach § 7 Abs. 2 PatG und § 40 PatG beansprucht werden kann. Für die Auslandspriorität (§ 41 PatG) setzt § 123 Abs. 7 PatG "
        "die Wiedereinsetzung gerade voraus."],
       merke="Innere Priorität: Nachanmeldefrist endgültig; Auslandspriorität: Wiedereinsetzung möglich (§ 123 Abs. 7 PatG).", level=2,
       concepts=["pat_prioritaet", "pat_wiedereinsetzung"], norms=["§ 123 PatG", "§ 40 PatG"], cases=["pat_bpatg_mehrfach_funkgeraet"],
       abschnitt=DN),
    fall("p05k-3", "Gebrauchsmuster als Voranmeldung",
         "R meldet am 01.02.2025 ein Gebrauchsmuster an und reicht am 15.01.2026 eine Patentanmeldung derselben Erfindung ein, für die er "
         "rechtzeitig die innere Priorität des Gebrauchsmusters beansprucht.",
         "Gilt die Gebrauchsmusteranmeldung mit der Prioritätserklärung als zurückgenommen?", False,
         ["**Nein!** Die Rücknahmefiktion des § 40 Abs. 5 S. 1 PatG gilt nicht, wenn die frühere Anmeldung ein Gebrauchsmuster betrifft "
          "(§ 40 Abs. 5 S. 2 PatG). R kann Gebrauchsmuster und Patent nebeneinander halten."],
         merke="Innere Priorität: frühere Patentanmeldung fällt weg, früheres Gebrauchsmuster bleibt (§ 40 Abs. 5 PatG).", level=1,
         concepts=["pat_prioritaet"], norms=["§ 40 PatG"], abschnitt=DN),
    mc("p05k-4", "Angaben zur Auslandspriorität", "Bis wann müssen bei einer Auslandspriorität Zeit, Land, Aktenzeichen und Abschrift der "
       "Voranmeldung vorliegen?",
       ["mit Einreichung der Nachanmeldung", "binnen zwei Monaten nach dem Anmeldetag der Nachanmeldung",
        "vor Ablauf des 16. Monats nach dem Prioritätstag", "bis zum Erteilungsbeschluss"], 2,
       ["**§ 41 Abs. 1 S. 1 PatG.** Vor Ablauf des 16. Monats nach dem Prioritätstag; innerhalb der Frist können die Angaben geändert werden "
        "(§ 41 Abs. 1 S. 2 PatG). Sonst ist der Prioritätsanspruch verwirkt (§ 41 Abs. 1 S. 3 PatG). Die Zweimonatsfrist gilt nur für die "
        "innere Priorität (§ 40 Abs. 4 PatG)."],
       merke="Auslandspriorität: Angaben bis Ende 16. Monat (§ 41 Abs. 1 PatG); innere: Erklärung zwei Monate (§ 40 Abs. 4 PatG).", level=1,
       concepts=["pat_prioritaet"], norms=["§ 41 PatG", "§ 40 PatG"], abschnitt=DN),
    fall("p05k-5", "Übertragung nach der Nachanmeldung",
         "Die US-Voranmeldung stammt vom Erfinder E. Die X-GmbH reicht in der Prioritätsfrist eine deutsche Nachanmeldung ein; E überträgt ihr "
         "die Rechte an der Erfindung erst zwei Wochen später.",
         "Kann die X-GmbH die Priorität wirksam beanspruchen?", False,
         ["**Nein!** Prioritätsberechtigt ist nur der Anmelder der Voranmeldung oder sein Rechtsnachfolger (Art. 4 A Abs. 1 PVÜ). Die "
          "Übertragung ist formlos möglich, muss aber **vor** der Nachanmeldung erfolgt sein (BGH Fahrzeugscheibe). Eine nachträgliche "
          "Übertragung heilt nicht."],
         merke="Prioritätsrecht: Rechtsnachfolge vor der Nachanmeldung.", level=2, concepts=["pat_prioritaet"], norms=["§ 41 PatG"],
         cases=["pat_bgh_fahrzeugscheibe"], abschnitt=DN),
    fall("p05k-6", "Europäische Nachanmeldung",
         "Die Konkurrenz GmbH reicht binnen zwölf Monaten nach ihrer deutschen Erstanmeldung eine europäische Anmeldung mit deren Priorität ein.",
         "Gilt die deutsche Erstanmeldung damit als zurückgenommen?", False,
         ["**Nein!** Die Rücknahmefiktion des § 40 Abs. 5 S. 1 PatG gilt nur für die deutsche Nachanmeldung mit innerer Priorität. Die "
          "europäische Nachanmeldung stützt sich auf Art. 87 Abs. 1 EPÜ; die Erstanmeldung bleibt anhängig. Doppelschutz regelt erst Art. II § 8 "
          "IntPatÜG."],
         merke="Nur die innere Priorität kostet die Voranmeldung (§ 40 Abs. 5 PatG).", level=1, concepts=["pat_prioritaet"],
         norms=["Art. 87 EPÜ", "§ 40 PatG"], abschnitt=DN),
    mc("p05k-7", "Kettenpriorität", "A beansprucht für ihre deutsche Patentanmeldung P2 die Priorität einer US-Anmeldung. Kann eine weitere "
       "deutsche Anmeldung P3 die innere Priorität von P2 beanspruchen?",
       ["Ja, wenn P3 binnen zwölf Monaten nach P2 eingeht",
        "Nein, für P2 ist schon eine ausländische Priorität in Anspruch genommen",
        "Ja, aber nur für Merkmale, die nicht in der US-Anmeldung stehen, ausnahmslos",
        "Nein, innere Priorität gibt es nur für Gebrauchsmuster"], 1,
       ["**Nein, § 40 Abs. 1 Hs. 2 PatG.** Die innere Priorität besteht nicht, wenn für die frühere Anmeldung schon eine inländische oder "
        "ausländische Priorität in Anspruch genommen worden ist (Verbot der Kettenpriorität)."],
       merke="Keine innere Priorität aus einer Anmeldung, die selbst Priorität beansprucht.", level=2, concepts=["pat_prioritaet"],
       norms=["§ 40 PatG"], abschnitt=DN),
    *fallkette("p05k-8", "Innere Priorität in der PCT-Anmeldung (nach TS III/2022)",
        "Die A & B GbR meldet DE 111 am Mi 11.07.2018 beim DPMA an. Gesellschafter B reicht am Di 09.07.2019 allein eine PCT-Anmeldung mit der "
        "Priorität von DE 111 ein, die Deutschland für ein Patent bestimmt. Die nationale Phase vor dem DPMA wird rechtzeitig eingeleitet.",
        [frage("Ist die Prioritätsfrist gewahrt?", True,
               ["**Ja!** Zwölf Monate ab dem Anmeldetag (Art. 8 Abs. 2 PCT, Art. 4 C Abs. 1, 2 PVÜ; § 187 Abs. 1 BGB, § 188 Abs. 2 BGB): Ende "
                "Do 11.07.2019; Einreichung am Di 09.07.2019."],
               merke="Prioritätsfrist zwölf Monate, Tag der Voranmeldung zählt nicht mit.", titel="V4 Frist"),
         frage("Gilt DE 111 schon mit Einreichung der PCT-Anmeldung als zurückgenommen?", False,
               ["**Nein!** Für internationale Anmeldungen verdrängt Art. III § 4 Abs. 4 S. 1 IntPatÜG den § 40 Abs. 5 PatG: Die Voranmeldung gilt "
                "erst als zurückgenommen, wenn die Voraussetzungen des Art. III § 4 Abs. 2 IntPatÜG (Gebühr, Übersetzung) erfüllt und die "
                "31 Monate abgelaufen sind, hier mit Ablauf des Do 11.02.2021."],
               merke="PCT mit DE-Priorität: Fiktion erst nach nationaler Phase und 31 Monaten (Art. III § 4 Abs. 4 IntPatÜG).",
               titel="Rücknahmefiktion", norms=["Art. III § 4 IntPatÜG"]),
         frage("Wann tritt die Fiktion ein, wenn B vorzeitige Bearbeitung beantragt?", 1,
               ["**Mit Eingang des Antrags**, sofern die Voraussetzungen des Art. III § 4 Abs. 2 IntPatÜG erfüllt sind (Art. III § 4 Abs. 4 S. 2 "
                "IntPatÜG, Art. 23 Abs. 2 PCT)."],
               optionen=["mit Einreichung der PCT-Anmeldung", "mit Eingang des Antrags beim DPMA, wenn Gebühr und Übersetzung vorliegen",
                         "erst mit Ablauf der 31 Monate", "nie"],
               abwandlung="B stellt am Do 15.10.2020 beim DPMA einen Antrag auf vorzeitige Bearbeitung nach Art. 23 Abs. 2 PCT.",
               merke="Vorzeitige Bearbeitung zieht die Fiktion vor (Art. III § 4 Abs. 4 S. 2 IntPatÜG).", titel="Vorzeitige Bearbeitung", level=3,
               norms=["Art. III § 4 IntPatÜG"]),
         frage("Tritt die Fiktion nach dem Wortlaut auch ein, obwohl B allein möglicherweise nicht prioritätsberechtigt ist?", True,
               ["**Ja, nach dem Wortlaut.** Art. III § 4 Abs. 4 S. 1 IntPatÜG knüpft an die Beanspruchung der Priorität an, nicht an ihre "
                "Wirksamkeit; Zweck ist die Vermeidung doppelter Verfahren. Zu § 40 Abs. 5 PatG hindert selbst eine unzulässige Kettenpriorität die "
                "Fiktion nicht (BPatG 35 W (pat) 26/13). Dagegen bleibt ein Feststellungsantrag mit Beschwerde (§ 73 Abs. 1 PatG)."],
               merke="Fiktion knüpft an die Erklärung, nicht an die materielle Berechtigung.", titel="V2 Berechtigung", level=3),
         frage("Hilft eine Wiedereinsetzung gegen den Wegfall von DE 111?", False,
               ["**Nein!** Wiedereinsetzung setzt die Versäumung einer Frist voraus (§ 123 Abs. 1 S. 1 PatG). Die Fiktion beruht nicht auf einer "
                "Säumnis, sondern auf der eigenen Prioritätserklärung."],
               merke="Keine Säumnis, keine Wiedereinsetzung.", titel="Rechtsbehelf", norms=["§ 123 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_prioritaet", "pat_pct_nationale_phase"], norms=["§ 40 PatG"]),
    *fallkette("p05k-9", "Zwei US-Prioritäten (nach TS III/2023)",
        "K reicht DE1 am Mo 01.07.2019 ein und beansprucht die Prioritäten US1 (01.07.2018) und US2 (01.04.2019). Anspruch 1: Kfz mit Motor, "
        "Bremse und mindestens vier Rädern, der Motor treibt einige Räder an. US1 zeigt Räder und Antrieb, aber keine Bremse; US2 die Bremse, "
        "aber weder vier Räder noch Antrieb.",
        [frage("Sind beide Prioritäten fristgerecht beansprucht?", True,
               ["**Ja!** Die Zwölfmonatsfrist aus US1 endet am Mo 01.07.2019 (Art. 4 C Abs. 1, 2 PVÜ; § 188 Abs. 2 BGB), die aus US2 am "
                "Mi 01.04.2020. Die Angaben nach § 41 Abs. 1 S. 1 PatG sind bis zum Ablauf des 16. Monats nach dem frühesten Prioritätstag zu machen."],
               merke="Mehrere Prioritäten zulässig (Art. 4 F PVÜ); jede Frist gesondert.", titel="V4, V5 Fristen", norms=["§ 41 PatG"]),
         frage("Hat Anspruch 1 den Zeitrang von US1?", False,
               ["**Nein!** Die Prioritätsunterlagen müssen die Gesamtheit der Merkmale des Anspruchs deutlich offenbaren (BGH UV-unempfindliche "
                "Druckplatte, X ZR 3/10; Art. 4 H PVÜ). US1 fehlt die Bremse."],
               merke="Priorität nur für vollständig vorweg offenbarte Anspruchsgegenstände.", titel="V3 Dieselbe Erfindung"),
         frage("Kann K für Anspruch 1 die Merkmale aus US1 und US2 kombinieren?", False,
               ["**Nein!** Art. 4 F PVÜ erlaubt mehrere Prioritäten für verschiedene Merkmale oder Ansprüche, aber kein Mosaik mehrerer "
                "Voranmeldungen in einem Anspruch. Eine Teilpriorität (EPA G 1/15) scheidet aus, weil keine Alternative des Anspruchs vollständig "
                "in US1 oder US2 steht."],
               merke="Kein Mosaik: Ein Anspruch braucht eine Voranmeldung, die alle seine Merkmale zeigt.", titel="V3 Mehrfachpriorität",
               cases=["epc_g_1_15"]),
         frage("Welcher Zeitrang gilt für Anspruch 1?", 0,
               ["**Der Anmeldetag Mo 01.07.2019** (§ 3 Abs. 1 S. 2 PatG). Was davor veröffentlicht wurde, ist voller Stand der Technik."],
               optionen=["Anmeldetag 01.07.2019", "Prioritätstag US1 01.07.2018", "Prioritätstag US2 01.04.2019", "kein Zeitrang"],
               merke="Unwirksame Priorität: Anmeldetag maßgeblich.", titel="⇒ Zeitrang"),
         frage("Bis wann kann K eine weitere Nachanmeldung mit der Priorität US2 einreichen?", 2,
               ["**Mi 01.04.2020.** Das Prioritätsrecht kann für mehrere Nachanmeldungen genutzt werden; US2 ist für die Bremse die erste "
                "Anmeldung (Art. 4 C Abs. 2, 4 PVÜ). Frist zwölf Monate ab US2 (Art. 4 C Abs. 1 PVÜ)."],
               optionen=["Mo 01.07.2019", "Di 01.10.2019", "Mi 01.04.2020", "Do 01.10.2020"],
               merke="Prioritätsrecht verbraucht sich nicht mit der ersten Nachanmeldung.", titel="Neue Nachanmeldung"),
         ],
        abschnitt=KF, level=2, concepts=["pat_prioritaet"], norms=["§ 41 PatG"]),
])

# ====================================================================================================== p05l §§ 123, 123a PatG
K_L = dict(id="p05l", titel="§§ 123, 123a PatG: Wiedereinsetzung und Weiterbehandlung", einheiten=[
    intro("p05l-0", "Prüfungsschema",
          "**AGL:** § 123 Abs. 1 S. 1 PatG (Wiedereinsetzung); § 123a Abs. 1 PatG (Weiterbehandlung)\n\n"
          "**A · Wiedereinsetzung (§ 123 PatG)**\n"
          "**V1 Statthaftigkeit** – versäumte Frist gegenüber DPMA oder BPatG, deren Versäumung kraft Gesetzes einen Rechtsnachteil hat "
          "(§ 123 Abs. 1 S. 1 PatG); ausgeschlossen: Einspruchsfrist und Einspruchsgebühr (§ 123 Abs. 1 S. 2 Nr. 1 PatG), Beschwerdefrist und "
          "Beschwerdegebühr des Einsprechenden gegen die Aufrechterhaltung (§ 123 Abs. 1 S. 2 Nr. 2 PatG), Nachanmeldefrist bei Priorität nach "
          "§ 7 Abs. 2 PatG und § 40 PatG (§ 123 Abs. 1 S. 2 Nr. 3 PatG), Weiterbehandlungsfrist und -gebühr (§ 123a Abs. 3 PatG)\n"
          "**V2 Antrag, Form, Berechtigung** – schriftlich (§ 123 Abs. 2 S. 1 PatG); Mitanmelder: Erhaltungsmaßnahme eines Teilhabers "
          "(§ 744 Abs. 2 BGB)\n"
          "**V3 Antragsfrist** – zwei Monate nach Wegfall des Hindernisses (§ 123 Abs. 2 S. 1 PatG) · Berechnung § 187 Abs. 1 BGB, "
          "§ 188 Abs. 2 BGB · Verschiebung § 193 BGB\n"
          "**V4 Begründung und Glaubhaftmachung** – Tatsachen im Antrag angeben, bei Antragstellung oder im Verfahren glaubhaft machen "
          "(§ 123 Abs. 2 S. 2 PatG; § 294 Abs. 1 ZPO)\n"
          "**V5 Nachholung** – versäumte Handlung innerhalb der Antragsfrist (§ 123 Abs. 2 S. 3 PatG); Zahlungstag § 2 PatKostZV; ist sie "
          "nachgeholt, kann Wiedereinsetzung auch ohne Antrag gewährt werden\n"
          "**V6 Ausschlussfrist** – ein Jahr nach Ablauf der versäumten Frist, unabhängig von Kenntnis (§ 123 Abs. 2 S. 4 PatG) · Berechnung "
          "§ 188 Abs. 2 BGB · Verschiebung § 193 BGB\n"
          "**V7 Ohne Verschulden verhindert** – jede Fahrlässigkeit schadet (Maßstab § 276 Abs. 2 BGB); Verschulden des Bevollmächtigten steht dem "
          "eigenen gleich (§ 85 Abs. 2 ZPO entsprechend), Versehen von Hilfspersonen nicht, wenn Auswahl, Anweisung und Fristenkontrolle "
          "genügen (BGH Bergbaumaschine); Rechtsunkenntnis und bewusstes Untätigbleiben entlasten nicht\n"
          "**⇒ Rechtsfolge:** Die Handlung gilt als rechtzeitig; Entscheidung durch die Stelle, die über die nachgeholte Handlung beschließt "
          "(§ 123 Abs. 3 PatG); Gewährung unanfechtbar (§ 123 Abs. 4 PatG); Weiterbenutzungsrecht gutgläubiger Zwischenbenutzer "
          "(§ 123 Abs. 5 bis 7 PatG; BGH Verdickerpolymer II); das GV PatKostG sieht keine Gebühr vor\n\n"
          "**B · Weiterbehandlung (§ 123a PatG)**\n"
          "**V1 Zurückweisung der Patentanmeldung nach Versäumung einer vom DPMA bestimmten Frist** (§ 123a Abs. 1 PatG); nicht bei gesetzlichen "
          "Fristen, Rücknahmefiktionen oder im Einspruchsverfahren\n"
          "**V2 Antrag binnen eines Monats nach Zustellung des Zurückweisungsbeschlusses** (§ 123a Abs. 2 S. 1 PatG), nicht verlängerbar (BPatG "
          "Weiterbehandlung) · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB\n"
          "**V3 Nachholung in derselben Frist**, vollständig; ein Fristgesuch genügt nicht (§ 123a Abs. 2 S. 2 PatG; BPatG Weiterbehandlung II)\n"
          "**V4 Gebühr 100 EUR** (Nr. 313 000 GV PatKostG) in derselben Frist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt der Antrag als "
          "zurückgenommen (§ 6 Abs. 2 PatKostG); keine Wiedereinsetzung (§ 123a Abs. 3 PatG)\n"
          "**⇒ Rechtsfolge:** Der Zurückweisungsbeschluss wird wirkungslos, ohne dass er aufgehoben werden muss (§ 123a Abs. 1 PatG); Verschulden "
          "wird nicht geprüft; Entscheidung § 123a Abs. 4 PatG\n\n"
          "**C · Jahresgebühren (§ 17 PatG, § 7 PatKostG)**\n"
          "Fällig am letzten Tag des Monats, der durch seine Benennung dem Anmeldemonat entspricht (§ 3 Abs. 2 S. 1 PatKostG); zahlbar bis zum "
          "Ablauf des zweiten Monats nach Fälligkeit (§ 7 Abs. 1 S. 1 PatKostG), mit Verspätungszuschlag von 50 EUR (z. B. Nr. 312 032 GV "
          "PatKostG) bis zum Ablauf des sechsten Monats (§ 7 Abs. 1 S. 2 PatKostG) · Verschiebung § 193 BGB. Danach: Anmeldung gilt als "
          "zurückgenommen (§ 58 Abs. 3 PatG), Patent erlischt (§ 20 Abs. 1 Nr. 2 PatG) → nur Wiedereinsetzung, Jahresfrist ab Ablauf der "
          "Zuschlagsfrist\n\n"
          "**Klausurfallen:** Weiterbehandlung hilft nie gegen Rücknahmefiktionen (§ 35a Abs. 1 S. 2 PatG, § 58 Abs. 3 PatG, § 6 Abs. 2 PatKostG), "
          "weil kein Zurückweisungsbeschluss vorliegt. Gegen die Zurückweisung nach Amtsfrist stehen Weiterbehandlung und Beschwerde nebeneinander. "
          "Die Einspruchsgebühr ist nicht wiedereinsetzungsfähig (BGH Verspätete Zahlung der Einspruchsgebühr). Insolvenz unterbricht "
          "Zahlungsfristen nicht (BPatG Sägeblatt).\n\n"
          "**In den Klausuren:** TS II/2019 (Übersetzungsfrist, Weiterbehandlung), TS I/2020 (18. Jahresgebühr, Dienstleister), TS I/2021 "
          "(Beschwerde der Stammanmeldung), TS III/2022 (Prüfungsantrag, Art. III § 4 Abs. 4 IntPatÜG), TS I/2023 (Einspruchsgebühr), "
          "TS III/2023 (Weiterbehandlung nach Rücknahme), TS II/2018 (Rechtsunkenntnis).",
          concepts=["pat_wiedereinsetzung", "pat_weiterbehandlung", "pat_jahresgebuehren", "pat_fristen"],
          norms=["§ 123 PatG", "§ 123a PatG", "§ 7 PatKostG", "§ 6 PatKostG"],
          cases=["pat_bgh_bergbaumaschine", "pat_bgh_verdickerpolymer_ii", "pat_bpatg_weiterbehandlung", "pat_bpatg_weiterbehandlung_ii"],
          abschnitt="Normenkette"),
    intro("p05l-1", "Definitionen",
          "**Wiedereinsetzung in den vorigen Stand:** Beseitigung der Folgen einer schuldlos versäumten gesetzlichen Frist gegenüber DPMA oder "
          "BPatG auf Antrag (§ 123 Abs. 1 S. 1 PatG)\n"
          "**Rechtsnachteil kraft Gesetzes:** Die Folge der Säumnis tritt unmittelbar aus dem Gesetz ein, etwa Rücknahmefiktion, Erlöschen oder "
          "„gilt als nicht vorgenommen“ (§ 35a Abs. 1 S. 2 PatG, § 20 Abs. 1 Nr. 2 PatG, § 6 Abs. 2 PatKostG)\n"
          "**Wegfall des Hindernisses:** Zeitpunkt, in dem der Säumige oder sein Vertreter die Säumnis kennt oder bei gebotener Sorgfalt hätte "
          "erkennen müssen (Rechtsprechung zu § 123 Abs. 2 S. 1 PatG)\n"
          "**Verschulden:** Außerachtlassen der im Verkehr erforderlichen Sorgfalt (§ 276 Abs. 2 BGB); bei § 123 PatG schadet jede Fahrlässigkeit\n"
          "**Bevollmächtigter:** Vertreter mit Vollmacht für das Verfahren; sein Verschulden wird zugerechnet (§ 85 Abs. 2 ZPO entsprechend); "
          "Hilfspersonen (Büropersonal, Zahlungsdienstleister ohne Vollmacht) sind keine Bevollmächtigten\n"
          "**Glaubhaftmachung:** Beweisführung mit allen Beweismitteln einschließlich der Versicherung an Eides statt, die überwiegende "
          "Wahrscheinlichkeit genügen lässt (§ 294 Abs. 1 ZPO)\n"
          "**Weiterbehandlung:** verschuldensunabhängiger Rechtsbehelf gegen die Zurückweisung einer Patentanmeldung nach Versäumung einer "
          "Amtsfrist (§ 123a Abs. 1 PatG)\n"
          "**Amtsfrist:** vom DPMA bestimmte Frist, etwa im Bescheid nach § 42 Abs. 1 PatG oder § 45 PatG\n"
          "**Weiterbenutzungsrecht:** Befugnis dessen, der im Inland in gutem Glauben zwischen Erlöschen und Wiederinkrafttreten die Erfindung in "
          "Benutzung genommen oder Veranstaltungen getroffen hat, sie für den eigenen Betrieb weiterzubenutzen (§ 123 Abs. 5 PatG)",
          concepts=["pat_wiedereinsetzung", "pat_weiterbehandlung"], norms=["§ 123 PatG", "§ 123a PatG"], abschnitt="Definitionen"),
    mc("p05l-2", "Ausgeschlossene Fristen", "In welche Frist ist die Wiedereinsetzung ausgeschlossen?",
       ["Frist zur Zahlung der Einspruchsgebühr", "Frist zur Stellung des Prüfungsantrags (§ 44 Abs. 2 PatG)",
        "Übersetzungsfrist des § 35a PatG", "Frist zur Zahlung einer Jahresgebühr mit Zuschlag"], 0,
       ["**§ 123 Abs. 1 S. 2 Nr. 1 PatG.** Ausgeschlossen sind die Frist zur Erhebung des Einspruchs und zur Zahlung der Einspruchsgebühr "
        "(§ 6 Abs. 1 S. 1 PatKostG). Wer zu spät zahlt, dessen Einspruch gilt als nicht erhoben (BGH Verspätete Zahlung der "
        "Einspruchsgebühr). Prüfungsantrag, Übersetzung und Jahresgebühr sind wiedereinsetzungsfähig."],
       merke="Ausgeschlossen: Einspruch, Beschwerde des Einsprechenden, Nachanmeldung § 7 Abs. 2, § 40 PatG, Weiterbehandlung.", level=1,
       concepts=["pat_wiedereinsetzung"], norms=["§ 123 PatG"], cases=["pat_bgh_einspruchsgebuehr_verspaetet"], abschnitt=DN),
    fall("p05l-3", "Fehler des Inlandsvertreters",
         "Patentanwalt P vertritt die japanische Anmelderin mit Vollmacht. Er notiert die Frist zur Zahlung der Prüfungsgebühr falsch; die "
         "Anmelderin selbst trifft kein Vorwurf.",
         "Ist die Anmelderin „ohne Verschulden verhindert“?", False,
         ["**Nein!** Das Verschulden des Bevollmächtigten steht dem Verschulden der Partei gleich (§ 85 Abs. 2 ZPO, im Verfahren nach "
          "§ 123 PatG entsprechend). Eine eigene falsche Fristnotierung des Anwalts ist Fahrlässigkeit; die Wiedereinsetzung ist unbegründet."],
         merke="Vertreterverschulden = eigenes Verschulden (§ 85 Abs. 2 ZPO).", level=1, concepts=["pat_wiedereinsetzung"],
         norms=["§ 123 PatG"], abschnitt=DN),
    fall("p05l-4", "Büroversehen",
         "In der Kanzlei des P löscht eine sonst zuverlässige Fachangestellte eigenmächtig eine Frist im Kalender. P hatte keine Anweisung "
         "erteilt, dass Fristen nur nach Rücksprache gestrichen werden dürfen.",
         "Ist das Versäumnis entschuldigt?", False,
         ["**Nein!** Fehler von Hilfspersonen werden nicht nach § 85 Abs. 2 ZPO zugerechnet; es zählt das eigene Organisationsverschulden des "
          "Anwalts. Er muss durch allgemeine Anweisungen sicherstellen, dass Personal eingetragene Fristen nicht eigenmächtig ändert oder "
          "löscht (BGH Bergbaumaschine). Fehlt die Anweisung, liegt Verschulden vor."],
         merke="Büroversehen entlastet nur bei ordnungsgemäßer Organisation und Kontrolle.", level=2,
         concepts=["pat_wiedereinsetzung"], norms=["§ 123 PatG"], cases=["pat_bgh_bergbaumaschine"], abschnitt=DN),
    mc("p05l-5", "Weiterbehandlung: Frist und Gebühr", "Was muss der Anmelder für die Weiterbehandlung bis wann tun?",
       ["binnen eines Monats nach Zustellung der Zurückweisung Antrag stellen, die versäumte Handlung nachholen und 100 EUR zahlen",
        "binnen zwei Monaten nach Wegfall des Hindernisses Antrag stellen und das fehlende Verschulden glaubhaft machen",
        "binnen eines Monats Beschwerde einlegen und 200 EUR zahlen",
        "binnen drei Monaten Antrag stellen; die Nachholung kann später folgen"], 0,
       ["**§ 123a Abs. 2 PatG, Nr. 313 000 GV PatKostG.** Antrag und Nachholung binnen eines Monats nach Zustellung des "
        "Zurückweisungsbeschlusses, Gebühr 100 EUR in derselben Frist (§ 6 Abs. 1 S. 1 PatKostG). Verschulden spielt keine Rolle; die Frist ist "
        "nicht verlängerbar (BPatG Weiterbehandlung) und nicht wiedereinsetzungsfähig (§ 123a Abs. 3 PatG)."],
       merke="Weiterbehandlung: ein Monat · Nachholung · 100 EUR · keine Wiedereinsetzung (§ 123a Abs. 3 PatG).", level=1,
       concepts=["pat_weiterbehandlung"], norms=["§ 123a PatG", "§ 6 PatKostG"], cases=["pat_bpatg_weiterbehandlung"], abschnitt=DN),
    fall("p05l-6", "Jahresgebühr im dritten Monat",
         "Die 5. Jahresgebühr eines Patents ist am 31.03. fällig. Der Inhaber hat sie am 15.06. noch nicht gezahlt.",
         "Ist das Patent schon erloschen?", False,
         ["**Nein!** Zuschlagsfrei zahlbar bis Ablauf des zweiten Monats nach Fälligkeit (§ 7 Abs. 1 S. 1 PatKostG), danach mit "
          "Verspätungszuschlag von 50 EUR (Nr. 312 052 GV PatKostG) bis zum Ablauf des sechsten Monats nach Fälligkeit, hier bis 30.09. "
          "(§ 7 Abs. 1 S. 2 PatKostG). Erst dann erlischt das Patent (§ 20 Abs. 1 Nr. 2 PatG)."],
         merke="Jahresgebühr: Fälligkeit § 3 Abs. 2 PatKostG · zwei Monate · Zuschlag bis sechs Monate (§ 7 Abs. 1 PatKostG).", level=1,
         concepts=["pat_jahresgebuehren"], norms=["§ 7 PatKostG", "§ 20 PatG"], abschnitt=DN),
    *fallkette("p05l-7", "Die 18. Jahresgebühr (nach TS I/2020)",
        "DE1 wurde am Sa 22.09.2001 angemeldet; die 18. Jahresgebühr war am So 30.09.2018 fällig. ACME beauftragt am Sa 23.03.2019 einen "
        "sorgfältig ausgewählten Zahlungsdienstleister, der versehentlich nicht zahlt. Erst am Do 16.01.2020 erfährt ACME vom Erlöschen. "
        "Die COPY GmbH vertreibt seit Mai 2019 gutgläubig die patentierte Klemme.",
        [frage("Konnte die Gebühr am Sa 23.03.2019 noch gezahlt werden?", True,
               ["**Ja!** Zuschlagsfrei bis Fr 30.11.2018 (§ 7 Abs. 1 S. 1 PatKostG), mit 50 EUR Zuschlag bis Ablauf des sechsten Monats nach "
                "Fälligkeit (§ 7 Abs. 1 S. 2 PatKostG): So 31.03.2019, verschoben auf Mo 01.04.2019 (§ 193 BGB)."],
               merke="Zuschlagsfrist: Ablauf des sechsten Monats nach Fälligkeit.", titel="Frist", norms=["§ 7 PatKostG"]),
         frage("Welche Folge trat mit Ablauf des Mo 01.04.2019 ein?", 0,
               ["**Das Patent ist erloschen** (§ 20 Abs. 1 Nr. 2 PatG). Die Rücknahmefiktion des § 58 Abs. 3 PatG gilt nur für Anmeldungen."],
               optionen=["Erlöschen des Patents", "Rücknahmefiktion nach § 58 Abs. 3 PatG", "Zurückweisung durch Beschluss",
                         "nichts, solange das DPMA nicht mahnt"],
               merke="Patent: Erlöschen (§ 20 Abs. 1 Nr. 2 PatG); Anmeldung: Rücknahmefiktion (§ 58 Abs. 3 PatG).", titel="Rechtsnachteil",
               norms=["§ 20 PatG"]),
         frage("Ist Weiterbehandlung statthaft?", False,
               ["**Nein!** Es gibt weder eine Zurückweisung noch eine Amtsfrist (§ 123a Abs. 1 PatG); die Zahlungsfrist ist gesetzlich."],
               merke="Jahresgebühr versäumt: nur Wiedereinsetzung.", titel="Weiterbehandlung", norms=["§ 123a PatG"]),
         frage("Bis wann muss ACME Antrag stellen und zahlen?", 1,
               ["**Mo 16.03.2020, spätestens Mi 01.04.2020.** Zwei Monate nach Wegfall des Hindernisses mit Kenntnis am Do 16.01.2020 "
                "(§ 123 Abs. 2 S. 1, 3 PatG; § 187 Abs. 1 BGB, § 188 Abs. 2 BGB); Ausschlussfrist ein Jahr nach Ablauf der versäumten Frist "
                "(§ 123 Abs. 2 S. 4 PatG). Gebühr und Zuschlag sind nachzuzahlen (§ 2 PatKostZV)."],
               optionen=["Do 16.01.2020", "Mo 16.03.2020, spätestens Mi 01.04.2020", "Mo 01.04.2019", "unbefristet"],
               merke="Antragsfrist ab Kenntnis, Jahresfrist ab Fristablauf.", titel="V3, V6 Fristen", norms=["§ 123 PatG"]),
         frage("Ist ACME das Versehen des Dienstleisters als Verschulden zuzurechnen?", False,
               ["**Nein, voraussichtlich nicht.** § 85 Abs. 2 ZPO erfasst nur Bevollmächtigte; ein Zahlungsdienstleister ist Hilfsperson. ACME "
                "haftet nur für eigene Auswahl-, Anweisungs- und Überwachungsfehler; der Auftrag neun Tage vor Fristablauf an ein zuverlässiges "
                "Fachunternehmen genügt."],
               merke="Hilfspersonen: nur eigenes Organisationsverschulden schadet.", titel="V7 Verschulden", level=3),
         frage("Darf die COPY GmbH nach der Wiedereinsetzung weiter verkaufen?", True,
               ["**Ja!** Wer im Inland gutgläubig zwischen Erlöschen und Wiederinkrafttreten die Benutzung aufgenommen hat, darf sie für den eigenen "
                "Betrieb fortsetzen (§ 123 Abs. 5 PatG). Am Wiedereinsetzungsverfahren ist COPY nicht beteiligt (BGH Verdickerpolymer II)."],
               merke="Zwischenbenutzer: Weiterbenutzungsrecht (§ 123 Abs. 5 PatG), keine Beteiligung.", titel="⇒ Weiterbenutzungsrecht",
               cases=["pat_bgh_verdickerpolymer_ii"], norms=["§ 123 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_wiedereinsetzung", "pat_jahresgebuehren"], norms=["§ 123 PatG"]),
    *fallkette("p05l-8", "Bewusst nichts veranlasst (nach TS II/2019)",
        "Die Elektro AG und die Motor KG melden DE 111 am Mi 04.06.2014 gemeinsam in englischer Sprache an. Nach Zugang des Rechercheberichts "
        "entscheiden beide bewusst, nichts weiter zu veranlassen. Eine Übersetzung geht nie ein. Später will die Elektro AG die Anmeldung retten.",
        [frage("Gilt DE 111 als zurückgenommen?", True,
               ["**Ja!** Zwölf Monate für Englisch (§ 35a Abs. 2 S. 1 PatG): Fristende Do 04.06.2015, für den Erklärungsort München wegen "
                "Fronleichnam Fr 05.06.2015 (§ 193 BGB). Danach Rücknahmefiktion (§ 35a Abs. 1 S. 2 PatG)."],
               merke="Gesetzliche Frist, Fiktion ohne Beschluss.", titel="Rechtsnachteil", norms=["§ 35a PatG"]),
         frage("Ist die Wiedereinsetzung statthaft?", True,
               ["**Ja!** Gesetzliche Frist gegenüber dem DPMA mit Rechtsnachteil kraft Gesetzes (§ 123 Abs. 1 S. 1 PatG); die Übersetzungsfrist "
                "steht nicht im Ausnahmekatalog des § 123 Abs. 1 S. 2 PatG."],
               merke="Statthaft: gesetzliche Frist + Rechtsnachteil + kein Ausschluss.", titel="V1 Statthaftigkeit", norms=["§ 123 PatG"]),
         frage("Darf die Elektro AG den Antrag allein stellen?", True,
               ["**Ja!** Mitanmelder handeln grundsätzlich gemeinsam; jeder Teilhaber darf aber die zur Erhaltung des gemeinschaftlichen Gegenstands "
                "notwendigen Maßregeln allein treffen (§ 744 Abs. 2 BGB)."],
               merke="Erhaltungsmaßnahme: jeder Teilhaber allein (§ 744 Abs. 2 BGB).", titel="V2 Berechtigung"),
         frage("Ist der Antrag begründet?", False,
               ["**Nein!** „Verhindert“ ist nicht, wer bewusst entscheidet, die Frist verstreichen zu lassen. Ein späterer Sinneswandel ist kein "
                "Hindernis im Sinne des § 123 Abs. 1 S. 1 PatG."],
               merke="Bewusstes Untätigbleiben ist keine Verhinderung.", titel="V7 Verschulden"),
         frage("Kommt hilfsweise eine Weiterbehandlung in Betracht?", False,
               ["**Nein!** Es fehlt eine Zurückweisung nach Versäumung einer vom DPMA bestimmten Frist (§ 123a Abs. 1 PatG)."],
               merke="Fiktion ≠ Zurückweisung: keine Weiterbehandlung.", titel="Weiterbehandlung", norms=["§ 123a PatG"]),
         ],
        abschnitt=KF, level=1, concepts=["pat_wiedereinsetzung"], norms=["§ 123 PatG"]),
])

# ====================================================================================================== p05m § 139 PatG
K_M = dict(id="p05m", titel="§ 139 PatG: Ansprüche wegen Patentverletzung", einheiten=[
    intro("p05m-0", "Prüfungsschema",
          "**AGL:** Unterlassung § 139 Abs. 1 S. 1 PatG, vorbeugend § 139 Abs. 1 S. 2 PatG; Schadensersatz § 139 Abs. 2 PatG; Vernichtung und "
          "Rückruf § 140a Abs. 1, 3 PatG; Auskunft § 140b Abs. 1 PatG; Rechnungslegung § 242 BGB; vor der Erteilung Entschädigung § 33 Abs. 1 PatG\n\n"
          "**A · Zulässigkeit**\n"
          "**V1 Zuständigkeit** – Patentstreitsache: Landgericht ohne Rücksicht auf den Streitwert ausschließlich (§ 143 Abs. 1 PatG), "
          "Konzentration nach Landesrecht (§ 143 Abs. 2 PatG); örtlich Begehungsort (§ 32 ZPO)\n\n"
          "**B · Begründetheit**\n"
          "**V2 Patent in Kraft** – Wirkungen ab Veröffentlichung der Erteilung (§ 58 Abs. 1 S. 3 PatG) bis Laufzeitende (§ 16 PatG) oder "
          "Erlöschen (§ 20 PatG); das Verletzungsgericht ist an die Erteilung gebunden (Trennungsprinzip)\n"
          "**V3 Aktivlegitimation** – der Verletzte: Patentinhaber; ausschließlicher Lizenznehmer; der Inhaber behält trotz ausschließlicher Lizenz "
          "eigene Ansprüche (BGH Cinch-Stecker)\n"
          "**V4 Benutzungshandlung** – unmittelbar: Erzeugnis herstellen, anbieten, in Verkehr bringen, gebrauchen, einführen oder besitzen "
          "(§ 9 S. 2 Nr. 1 PatG); Verfahren anwenden oder anbieten (§ 9 S. 2 Nr. 2 PatG); unmittelbares Verfahrenserzeugnis (§ 9 S. 2 Nr. 3 PatG); "
          "mittelbar: Mittel, die sich auf ein wesentliches Element beziehen, an Nichtberechtigte im Inland zur Benutzung im Inland anbieten oder "
          "liefern, bei Wissen oder Offensichtlichkeit der Eignung und Bestimmung (§ 10 Abs. 1 PatG; Ausnahme Handelsware § 10 Abs. 2 PatG)\n"
          "**V5 Im Schutzbereich** – § 14 PatG: Patentansprüche, ausgelegt mit Beschreibung und Zeichnungen; wortsinngemäß oder äquivalent "
          "(Gleichwirkung, Auffindbarkeit, Gleichwertigkeit: BGH Schneidmesser I)\n"
          "**V6 Rechtswidrig, keine Einwendung** – ohne Zustimmung (§ 9 S. 2 PatG); keine Schranke (§ 11 PatG); kein Vorbenutzungsrecht "
          "(§ 12 PatG); kein Weiterbenutzungsrecht (§ 123 Abs. 5 PatG); keine Erschöpfung\n"
          "**V7 Wiederholungs- oder Erstbegehungsgefahr** – § 139 Abs. 1 S. 1, 2 PatG; kein Ausschluss wegen unverhältnismäßiger Härte "
          "(§ 139 Abs. 1 S. 3 PatG; sonst Ausgleich in Geld, § 139 Abs. 1 S. 4 PatG)\n"
          "**V8 Verschulden** – nur für Schadensersatz: Vorsatz oder Fahrlässigkeit (§ 139 Abs. 2 S. 1 PatG)\n"
          "**V9 Keine Verjährung** – § 141 S. 1 PatG i.V.m. § 195 BGB, § 199 Abs. 1 BGB; danach Herausgabe des Erlangten (§ 141 S. 2 PatG "
          "i.V.m. § 852 BGB)\n\n"
          "**⇒ Rechtsfolge:** Unterlassung; Schadensersatz nach Wahl des Verletzten: konkreter Schaden (§ 249 BGB, § 252 BGB), Verletzergewinn "
          "(§ 139 Abs. 2 S. 2 PatG), Lizenzanalogie (§ 139 Abs. 2 S. 3 PatG); Vernichtung und Rückruf (§ 140a Abs. 1, 3 PatG, Grenze "
          "Verhältnismäßigkeit § 140a Abs. 4 PatG); Auskunft über Herkunft und Vertriebsweg (§ 140b Abs. 1 PatG); Urteilsbekanntmachung "
          "(§ 140e PatG)\n\n"
          "**C · Verteidigung und Begleitverfahren**\n"
          "**Aussetzung** – Einspruch oder Nichtigkeitsklage und Aussetzung des Verletzungsprozesses bei hinreichender Erfolgsaussicht "
          "(§ 148 Abs. 1 ZPO; BGH Mautberechnung, X ZR 124/10)\n"
          "**Berechtigungsanfrage oder Schutzrechtsverwarnung** – die Anfrage ist Meinungsaustausch ohne Unterlassungsverlangen; die unberechtigte "
          "Verwarnung ist Eingriff in den eingerichteten und ausgeübten Gewerbebetrieb (§ 823 Abs. 1 BGB), auch der Anwalt kann haften "
          "(BGH Unberechtigte Schutzrechtsverwarnung II, X ZR 170/12); Feststellungsinteresse schon bei Berühmung (§ 256 Abs. 1 ZPO; BGH "
          "Besonderer Mechanismus, X ZR 56/09); ohne Abmahnung Kostenrisiko (§ 93 ZPO)\n"
          "**Einstweilige Verfügung** – § 935 ZPO, § 940 ZPO: Verfügungsanspruch (§ 139 Abs. 1 PatG) und Verfügungsgrund, also Dringlichkeit und "
          "hinreichend gesicherter Rechtsbestand; Glaubhaftmachung (§ 920 Abs. 2 ZPO, § 294 ZPO)\n"
          "**Entschädigung** – ab Veröffentlichung des Hinweises (§ 32 Abs. 5 PatG) bis zur Erteilung; Benutzer wusste oder musste wissen; "
          "angemessene Entschädigung, weitergehende Ansprüche ausgeschlossen (§ 33 Abs. 1 PatG); nicht bei offensichtlich fehlender "
          "Patentfähigkeit (§ 33 Abs. 2 PatG); rückwirkender Wegfall mit der Anmeldung (§ 58 Abs. 2 PatG) oder dem Patent (§ 21 Abs. 3 S. 1 PatG, "
          "§ 22 Abs. 2 PatG); Verjährung frühestens ein Jahr nach Erteilung (§ 33 Abs. 3 S. 1 PatG)\n\n"
          "**Klausurfallen:** Benutzung im Offenlegungszeitraum begründet keine Wiederholungsgefahr, sondern nur Entschädigung. Der Einwand "
          "fehlender Neuheit gehört in Einspruch oder Nichtigkeitsklage, nicht in den Verletzungsprozess. Das Vorbenutzungsrecht ist nur mit dem "
          "Betrieb übertragbar. Für die Teilanmeldung beginnt die Entschädigung jedenfalls mit ihrem eigenen Hinweis.\n\n"
          "**In den Klausuren:** TS III/2021 (Wanderstock: Ansprüche, Vorbenutzung, Berechtigungsanfrage), TS I/2020 (Entschädigung aus DE1 bis "
          "DE3, vorbeugende Unterlassung), TS III/2019 (Äquivalenz nach beschränkter Aufrechterhaltung), TS I/2022 (Patent und Gebrauchsmuster, "
          "einstweilige Verfügung), TS II/2020 (§ 9 S. 2 Nr. 3 PatG).",
          concepts=["pat_verletzung", "pat_unterlassung", "pat_schadensersatz", "pat_benutzungshandlungen", "pat_schutzbereich",
                    "pat_trennungsprinzip", "pat_aussetzung"],
          norms=["§ 139 PatG", "§ 140a PatG", "§ 140b PatG", "§ 9 PatG", "§ 10 PatG", "§ 14 PatG", "§ 12 PatG", "§ 33 PatG", "§ 143 PatG"],
          cases=["pat_bgh_schneidmesser_i", "pat_bgh_cinch_stecker"], abschnitt="Normenkette"),
    intro("p05m-1", "Definitionen",
          "**Benutzung:** jede der in § 9 S. 2 PatG abschließend genannten Handlungen ohne Zustimmung des Inhabers; mittelbar die Handlungen des "
          "§ 10 Abs. 1 PatG\n"
          "**Anbieten:** jede Handlung, die das Erzeugnis Dritten zum Erwerb bereitstellt; schon der Werbeprospekt mit Abbildung genügt in aller "
          "Regel (BGH Kupplung für optische Geräte), auch das Angebot während der Schutzdauer für Lieferungen danach (BGH Simvastatin)\n"
          "**Unmittelbares Verfahrenserzeugnis:** Erzeugnis, das durch das patentierte Verfahren hergestellt ist und seine Eigenschaften nicht durch "
          "weitere Bearbeitung verloren hat (§ 9 S. 2 Nr. 3 PatG; Lehre)\n"
          "**Wesentliches Element:** Merkmal, das zur Verwirklichung der geschützten Lehre beiträgt; ein Merkmal, das zur Lösung nichts beiträgt, "
          "ist keines (§ 10 Abs. 1 PatG; BGH Pipettensystem)\n"
          "**Äquivalenz:** Die Abwandlung löst das Problem mit objektiv gleicher Wirkung, der Fachmann findet sie ohne erfinderische Überlegungen, "
          "und seine Überlegungen orientieren sich am Sinngehalt des Anspruchs (§ 14 PatG; BGH Schneidmesser I)\n"
          "**Wiederholungsgefahr:** ernsthafte Besorgnis weiterer Verletzungen; die begangene Verletzung indiziert sie (§ 139 Abs. 1 S. 1 PatG; "
          "Rechtsprechung)\n"
          "**Erstbegehungsgefahr:** ernsthafte und greifbare tatsächliche Anhaltspunkte, dass eine Verletzung in naher Zukunft bevorsteht "
          "(§ 139 Abs. 1 S. 2 PatG; Rechtsprechung); Darlegungslast beim Inhaber\n"
          "**Erfindungsbesitz:** Die Lehre ist objektiv fertig und subjektiv als ausführbar erkannt; planmäßiges Handeln, das alle Merkmale "
          "verwirklicht, genügt (§ 12 Abs. 1 S. 1 PatG; BGH Desmopressin)\n"
          "**Erschöpfung:** Die Rechte aus dem Patent an einem bestimmten Erzeugnis sind verbraucht, wenn es vom Inhaber oder mit seiner "
          "Zustimmung im EWR in Verkehr gebracht wurde (ungeschriebener Grundsatz); die Neuherstellung verdrängt sie (BGH Scheibenbremse II)\n"
          "**Schutzrechtsverwarnung:** ernsthaftes und endgültiges Verlangen, eine bestimmte Benutzung zu unterlassen; die Berechtigungsanfrage "
          "fragt nur nach dem Benutzungsrecht des Adressaten (Rechtsprechung)",
          concepts=["pat_benutzungshandlungen", "pat_mittelbare_verletzung", "pat_aequivalenz", "pat_vorbenutzungsrecht", "pat_erschoepfung",
                    "pat_verfahrenserzeugnis"],
          norms=["§ 9 PatG", "§ 10 PatG", "§ 12 PatG", "§ 14 PatG", "§ 139 PatG"],
          cases=["pat_bgh_kupplung_optische_geraete", "pat_bgh_simvastatin", "pat_bgh_pipettensystem", "pat_bgh_desmopressin",
                 "pat_bgh_scheibenbremse_ii"], abschnitt="Definitionen"),
    mc("p05m-2", "Berechnung des Schadensersatzes", "Welche Berechnungsart regelt § 139 Abs. 2 S. 3 PatG?",
       ["konkreter Schaden einschließlich entgangenen Gewinns", "Herausgabe des Verletzergewinns", "Lizenzanalogie",
        "pauschaler Strafzuschlag"], 2,
       ["**Lizenzanalogie.** Der Schaden kann auf der Grundlage des Betrags berechnet werden, den der Verletzer als angemessene Vergütung hätte "
        "entrichten müssen (§ 139 Abs. 2 S. 3 PatG). Den Verletzergewinn nennt § 139 Abs. 2 S. 2 PatG, der konkrete Schaden folgt aus "
        "§ 249 BGB, § 252 BGB. Der Verletzte wählt."],
       merke="Drei Berechnungsarten: konkret · Verletzergewinn (S. 2) · Lizenzanalogie (S. 3).", level=1,
       concepts=["pat_schadensersatz"], norms=["§ 139 PatG"], cases=["pat_bgh_kabelschloss"], abschnitt=DN),
    fall("p05m-3", "Vertrieb vor der Erteilung",
         "COPY vertreibt von April 2002 bis Oktober 2017 eine Klemme, die Gegenstand der 2002 offengelegten Anmeldung DE1 ist. DE1 wird erst "
         "2019 erteilt. ACME verlangt Unterlassung und Schadensersatz.",
         "Bestehen Ansprüche aus § 139 PatG?", False,
         ["**Nein!** § 139 PatG setzt eine Benutzung entgegen § 9 PatG voraus; die Wirkungen des Patents treten erst mit der Veröffentlichung der "
          "Erteilung ein (§ 58 Abs. 1 S. 3 PatG). Benutzungen im Offenlegungszeitraum sind nicht verboten, sondern nur entschädigungspflichtig "
          "(§ 33 Abs. 1 PatG); sie begründen auch keine Wiederholungsgefahr."],
         merke="Vor Erteilung: Entschädigung (§ 33 PatG), nach Erteilung: § 139 PatG.", level=1,
         concepts=["pat_verletzung", "pat_unterlassung"], norms=["§ 139 PatG", "§ 33 PatG", "§ 58 PatG"], abschnitt=DN),
    fall("p05m-4", "Verfahren in den USA",
         "Das Patent schützt ein Schweißverfahren für Sensorgehäuse. Der Wettbewerber wendet es nur in seinem Werk in den USA an und führt die "
         "geschweißten Gehäuse nach Deutschland ein.",
         "Verletzt die Einfuhr das Patent?", True,
         ["**Ja!** Die Anwendung in den USA ist nicht erfasst (§ 9 S. 2 Nr. 2 PatG wirkt nur im Inland). Verboten ist aber, das durch das "
          "Verfahren **unmittelbar hergestellte Erzeugnis** anzubieten, in Verkehr zu bringen, zu gebrauchen oder einzuführen (§ 9 S. 2 Nr. 3 "
          "PatG). Die Beweislastumkehr des § 139 Abs. 3 PatG hilft nur bei neuen Erzeugnissen."],
         merke="Verfahrenspatent: Schutz auch für das unmittelbare Erzeugnis (§ 9 S. 2 Nr. 3 PatG).", level=2,
         concepts=["pat_verfahrenserzeugnis", "pat_benutzungshandlungen"], norms=["§ 9 PatG", "§ 139 PatG"], abschnitt=DN),
    mc("p05m-5", "Maßgeblicher Zeitpunkt des Vorbenutzungsrechts", "Auf welchen Zeitpunkt kommt es für das Vorbenutzungsrecht an, wenn der "
       "Patentinhaber eine Priorität beansprucht?",
       ["Veröffentlichung der Erteilung", "Anmeldetag der Nachanmeldung", "Anmeldetag der prioritätsbegründenden früheren Anmeldung",
        "Erhebung der Verletzungsklage"], 2,
       ["**§ 12 Abs. 2 S. 1 PatG.** Steht dem Inhaber ein Prioritätsrecht zu, ist an Stelle der Anmeldung die frühere Anmeldung maßgebend. Der "
        "Vorbenutzer muss an diesem Tag im Inland Erfindungsbesitz gehabt und die Erfindung benutzt oder Veranstaltungen getroffen haben "
        "(§ 12 Abs. 1 S. 1 PatG)."],
       merke="Vorbenutzung: Stichtag Anmelde- bzw. Prioritätstag (§ 12 Abs. 1, 2 PatG).", level=1,
       concepts=["pat_vorbenutzungsrecht"], norms=["§ 12 PatG"], abschnitt=DN),
    fall("p05m-6", "Neuheitseinwand im Verletzungsprozess",
         "Die Beklagte meint, das Klagepatent sei wegen einer eigenen Messevorführung vor dem Prioritätstag nicht neu, und beantragt, die Klage "
         "deshalb abzuweisen.",
         "Prüft das Landgericht die Neuheit selbst?", False,
         ["**Nein!** Trennungsprinzip: Das Verletzungsgericht ist an das erteilte Patent gebunden. Über den Rechtsbestand entscheiden DPMA und "
          "BPatG im Einspruch (§ 59 Abs. 1 PatG) oder auf Nichtigkeitsklage (§ 81 Abs. 1 PatG). Die Beklagte muss diese Verfahren einleiten und "
          "die Aussetzung beantragen (§ 148 Abs. 1 ZPO; BGH Mautberechnung, X ZR 124/10)."],
         merke="Rechtsbestand nur im Einspruch oder Nichtigkeitsverfahren; im Verletzungsprozess Aussetzung (§ 148 ZPO).", level=1,
         concepts=["pat_trennungsprinzip", "pat_aussetzung"], norms=["§ 59 PatG", "§ 81 PatG"], abschnitt=DN),
    mc("p05m-7", "Einstweilige Verfügung", "Was muss der Patentinhaber für eine einstweilige Verfügung auf Unterlassung glaubhaft machen?",
       ["nur die Verletzung; die Dringlichkeit wird stets vermutet",
        "Verfügungsanspruch und Verfügungsgrund: Verletzung, Dringlichkeit und hinreichend gesicherten Rechtsbestand",
        "nur, dass eine Nichtigkeitsklage abgewiesen wurde",
        "Verschulden des Verletzers und die Höhe des Schadens"], 1,
       ["**§ 935 ZPO, § 940 ZPO.** Verfügungsanspruch ist der Unterlassungsanspruch (§ 139 Abs. 1 PatG), Verfügungsgrund die Eilbedürftigkeit; "
        "in Patentsachen verlangt die Rechtsprechung zudem einen hinreichend gesicherten Rechtsbestand. Glaubhaftmachung nach § 920 Abs. 2 ZPO, "
        "§ 294 ZPO; zögerliches Vorgehen widerlegt die Dringlichkeit."],
       merke="Einstweilige Verfügung: Anspruch + Grund (Dringlichkeit, Rechtsbestand), glaubhaft gemacht.", level=2,
       concepts=["pat_unterlassung"], norms=["§ 139 PatG"], abschnitt=DN),
    fall("p05m-8", "Berechtigungsanfrage",
         "Die Konkurrenz GmbH schreibt der Erfindungen GmbH sachlich, sie halte DE 456 B1, und fragt, weshalb diese sich zum Vertrieb ihres "
         "Stocks für berechtigt halte. Ein Unterlassungsverlangen enthält das Schreiben nicht. Später wird DE 456 B1 widerrufen.",
         "Haftet die Konkurrenz GmbH aus § 823 Abs. 1 BGB?", False,
         ["**Nein!** Haftungsträchtig ist nur die unberechtigte **Schutzrechtsverwarnung**, also das ernsthafte Unterlassungsverlangen, als "
          "Eingriff in den eingerichteten und ausgeübten Gewerbebetrieb (§ 823 Abs. 1 BGB). Die Berechtigungsanfrage ist bloßer Meinungsaustausch; "
          "sie verschafft dem Inhaber Informationen und begründet für spätere Ansprüche Kenntnis (§ 139 Abs. 2 PatG, § 33 Abs. 1 PatG)."],
         merke="Erst anfragen, dann verwarnen: Berechtigungsanfrage ohne Haftungsrisiko.", level=2, concepts=["pat_verletzung"],
         abschnitt=DN),
    *fallkette("p05m-9", "Der Wanderstock (nach TS III/2021)",
        "Die Konkurrenz GmbH ist Inhaberin des DE 456 B1. Die Erfindungen GmbH bietet seit der Erteilung einen Wanderstock an, der alle Merkmale "
        "von Anspruch 1 wortsinngemäß verwirklicht. Einen baugleichen Stock hatte sie schon vor dem Prioritätstag auf einer Messe in Deutschland "
        "vorgeführt und verkauft, den Vertrieb dann zeitweise eingestellt.",
        [frage("Ist das Anbieten des Stocks eine Benutzung?", True,
               ["**Ja!** Anbieten eines Erzeugnisses, das Gegenstand des Patents ist (§ 9 S. 2 Nr. 1 PatG), im Schutzbereich nach § 14 PatG, ohne "
                "Zustimmung der Inhaberin."],
               merke="§ 9 S. 2 Nr. 1 PatG: herstellen, anbieten, in Verkehr bringen, gebrauchen, einführen, besitzen.", titel="V4 Benutzung",
               norms=["§ 9 PatG"]),
         frage("Kann die Erfindungen GmbH im Verletzungsprozess einwenden, das Patent sei wegen der Vorführung nicht neu?", False,
               ["**Nein!** Das Landgericht ist an die Erteilung gebunden. Die Vorführung ist offenkundige Vorbenutzung (§ 3 Abs. 1 S. 2 PatG) und "
                "Widerrufsgrund (§ 21 Abs. 1 Nr. 1 PatG); geltend zu machen im Einspruch (§ 59 Abs. 1 PatG) oder mit Nichtigkeitsklage, verbunden "
                "mit einem Aussetzungsantrag (§ 148 Abs. 1 ZPO)."],
               merke="Rechtsbestand: eigenes Verfahren + Aussetzung.", titel="V2 Trennungsprinzip", concepts=["pat_trennungsprinzip"]),
         frage("Kann der Erfindungen GmbH ein Vorbenutzungsrecht zustehen?", True,
               ["**Ja!** Sie hatte vor dem Prioritätstag (§ 12 Abs. 2 S. 1 PatG) im Inland Erfindungsbesitz und hat die Erfindung benutzt "
                "(§ 12 Abs. 1 S. 1 PatG; BGH Desmopressin). Der Besitzstand muss am Stichtag noch bestehen: Eine bloße Unterbrechung schadet nicht, "
                "die endgültige Aufgabe des Benutzungswillens schon. Das ist hier aufzuklären."],
               merke="Vorbenutzungsrecht: Erfindungsbesitz + Benutzung im Inland + Stichtag.", titel="V6 Vorbenutzungsrecht",
               cases=["pat_bgh_desmopressin"], norms=["§ 12 PatG"], level=3),
         frage("Darf sie das Vorbenutzungsrecht einem Wettbewerber als Lizenz einräumen?", False,
               ["**Nein!** Die Befugnis gilt für die Bedürfnisse des eigenen Betriebs und kann nur zusammen mit dem Betrieb vererbt oder veräußert "
                "werden (§ 12 Abs. 1 S. 2, 3 PatG); ein abgrenzbarer Betriebsteil genügt (BGH Nabenschaltung III). Lizenzen kann sie nicht vergeben."],
               merke="Vorbenutzungsrecht: betriebsgebunden, nicht lizenzierbar.", titel="V6 Umfang", cases=["pat_bgh_nabenschaltung_iii"],
               norms=["§ 12 PatG"]),
         frage("Welche Ansprüche hat die Konkurrenz GmbH, wenn kein Vorbenutzungsrecht besteht?", 3,
               ["**Alle.** Unterlassung (§ 139 Abs. 1 S. 1 PatG), Schadensersatz bei Fahrlässigkeit (§ 139 Abs. 2 PatG), Auskunft (§ 140b Abs. 1 "
                "PatG), Rechnungslegung (§ 242 BGB), Vernichtung und Rückruf (§ 140a PatG); für die Zeit vor der Erteilung Entschädigung "
                "(§ 33 Abs. 1 PatG)."],
               optionen=["nur Unterlassung", "nur Schadensersatz, weil die Vorführung Gutgläubigkeit begründet",
                         "nur Entschädigung nach § 33 PatG", "Unterlassung, Schadensersatz, Auskunft, Vernichtung, Rückruf und Entschädigung"],
               merke="Anspruchsbündel § 139, § 140a, § 140b PatG, § 242 BGB, § 33 PatG.", titel="⇒ Rechtsfolgen",
               norms=["§ 139 PatG", "§ 140a PatG", "§ 140b PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_verletzung", "pat_vorbenutzungsrecht"], norms=["§ 139 PatG"]),
    *fallkette("p05m-10", "Klemmvorrichtung: vor und nach der Erteilung (nach TS I/2020)",
        "COPY vertreibt vom 01.04.2002 bis 20.10.2017 eine Klemme, die Gegenstand der Anmeldung DE1 der ACME ist. DE1 wurde am Sa 20.04.2002 "
        "offengelegt und am Mi 20.02.2019 erteilt (Veröffentlichung). 2016 hat ACME aus DE1 die Teilanmeldung DE2 abgetrennt; der Hinweis auf "
        "DE2 erschien am Mo 28.11.2016.",
        [frage("Hat ACME aus DE1 einen Entschädigungsanspruch für die Zeit ab 20.04.2002?", True,
               ["**Ja!** Ab Veröffentlichung des Hinweises (§ 32 Abs. 5 PatG) kann der Anmelder von dem, der den Gegenstand der Anmeldung benutzt, "
                "obwohl er wusste oder wissen musste, dass er Gegenstand der Anmeldung war, eine angemessene Entschädigung verlangen (§ 33 Abs. 1 "
                "PatG), bemessen wie eine Lizenz. Ausgeschlossen bei offensichtlich fehlender Patentfähigkeit (§ 33 Abs. 2 PatG)."],
               merke="Entschädigung: Hinweis § 32 Abs. 5 PatG · Kenntnis · angemessen · nicht mehr (§ 33 Abs. 1 PatG).", titel="§ 33 Abs. 1 PatG",
               norms=["§ 33 PatG"]),
         frage("Kann ACME die Entschädigung aus DE1 noch durch Klage bis Do 20.02.2020 sichern?", True,
               ["**Ja!** Auf die Verjährung sind die Regeln des BGB entsprechend anzuwenden, sie tritt aber frühestens ein Jahr nach Erteilung ein "
                "(§ 33 Abs. 3 S. 1 PatG): Do 20.02.2020. Hemmung durch Klageerhebung (§ 204 Abs. 1 Nr. 1 BGB)."],
               merke="Verjährung der Entschädigung: frühestens ein Jahr nach Erteilung (§ 33 Abs. 3 S. 1 PatG).", titel="Verjährung",
               norms=["§ 33 PatG"]),
         frage("Steht ACME aus der Teilanmeldung DE2 jedenfalls ab Mo 28.11.2016 Entschädigung zu?", True,
               ["**Ja!** DE2 behält Zeitrang und Priorität von DE1 (§ 39 Abs. 1 S. 4 PatG); jedenfalls mit dem eigenen Hinweis (§ 32 Abs. 5 PatG) "
                "beginnt der Entschädigungszeitraum. Ob er schon mit der Offenlegung der Stammanmeldung 2002 beginnt, ist offen und vertretbar."],
               merke="Teilanmeldung: Entschädigung sicher ab eigenem Hinweis.", titel="Teilanmeldung", norms=["§ 39 PatG", "§ 33 PatG"], level=3),
         frage("Entfällt die Entschädigung aus DE2, wenn DE2 nach Erteilung für nichtig erklärt wird?", True,
               ["**Ja!** Mit der Nichtigerklärung gelten die Wirkungen des Patents und der Anmeldung als von Anfang an nicht eingetreten "
                "(§ 22 Abs. 2 PatG i.V.m. § 21 Abs. 3 S. 1 PatG). Das erfasst auch den Anspruch aus § 33 Abs. 1 PatG."],
               merke="Wegfall ex tunc: § 21 Abs. 3 S. 1, § 22 Abs. 2 PatG; vor Erteilung § 58 Abs. 2 PatG.", titel="Rückwirkender Wegfall",
               norms=["§ 22 PatG", "§ 21 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_verletzung"], norms=["§ 33 PatG"]),
])

# ====================================================================================================== p05n §§ 6, 7, 8, 63 PatG
K_N = dict(id="p05n", titel="§§ 6, 7, 8, 63 PatG: Recht auf das Patent, Vindikation, Erfindernennung", einheiten=[
    intro("p05n-0", "Prüfungsschema",
          "**AGL:** Vindikation § 8 S. 1 PatG (Abtretung des Erteilungsanspruchs), § 8 S. 2 PatG (Übertragung des Patents); europäisch "
          "Art. II § 5 Abs. 1 IntPatÜG; Berichtigung der Erfindernennung § 63 Abs. 2 S. 1 PatG; Widerruf wegen widerrechtlicher Entnahme "
          "§ 21 Abs. 1 Nr. 3 PatG i.V.m. § 59 Abs. 1 S. 1 PatG mit Nachanmelderecht § 7 Abs. 2 PatG; Nichtigkeit § 22 Abs. 1 PatG, § 81 Abs. 3 PatG\n\n"
          "**A · Vindikation (§ 8 PatG)**\n"
          "**V1 Anspruchsteller ist Berechtigter** – Erfinder oder Rechtsnachfolger (§ 6 S. 1 PatG); Miterfinder gemeinschaftlich (§ 6 S. 2 PatG; "
          "Bruchteilsgemeinschaft §§ 741 ff. BGB); bei unabhängigen Doppelerfindungen der Erstanmelder (§ 6 S. 3 PatG); Arbeitgeber durch "
          "Inanspruchnahme der Diensterfindung (§ 6 ArbnErfG, § 7 Abs. 1 ArbnErfG)\n"
          "**V2 Anmeldung durch Nichtberechtigten oder widerrechtliche Entnahme** – § 8 S. 1 PatG; im Verfahren vor dem DPMA gilt der Anmelder "
          "als berechtigt (§ 7 Abs. 1 PatG), die Berechtigung klärt nur das Zivilgericht\n"
          "**V3 Übereinstimmung der Lehren** – prüfender Vergleich der Lehre des Berechtigten mit der angemeldeten (BGH Mitralklappenprothese); "
          "teilweise Übereinstimmung: Einräumung einer Mitberechtigung, nur am Schutzrecht als Ganzem (BGH Blendschutzbehang), als Minus im "
          "Übertragungsantrag enthalten (BGH Schneidbrennerstromdüse)\n"
          "**V4 Frist** – vor der Erteilung keine; Klage auf Übertragung binnen zwei Jahren nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG), "
          "nach Einspruch wegen Entnahme bis ein Jahr nach rechtskräftigem Abschluss (§ 8 S. 4 PatG), unbefristet gegen den beim Erwerb "
          "bösgläubigen Inhaber (§ 8 S. 5 PatG) · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB; europäisch "
          "Ausschlussfrist zwei Jahre ab Hinweis auf die Erteilung im Europäischen Patentblatt (Art. II § 5 Abs. 2 IntPatÜG); Verjährung "
          "§ 195 BGB (BGH Automatisierte Wärmebehandlung)\n"
          "**V5 Zuständigkeit** – Landgericht (§ 143 Abs. 1 PatG; bei Arbeitnehmererfindungen § 39 Abs. 1 S. 1 ArbnErfG)\n"
          "**⇒ Rechtsfolge:** Abtretung des Erteilungsanspruchs bzw. Übertragung des Patents oder Einräumung einer Mitberechtigung; Zeitrang und "
          "Verfahrensstand bleiben erhalten\n\n"
          "**B · Widerrechtliche Entnahme als Widerrufs- und Nichtigkeitsgrund**\n"
          "**V1 Einspruch nur durch den Verletzten** – § 59 Abs. 1 S. 1 PatG, binnen neun Monaten nach Veröffentlichung der Erteilung, Gebühr "
          "200 EUR (Nr. 313 600 GV PatKostG; § 6 Abs. 1 S. 1 PatKostG) · Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB · Verschiebung § 193 BGB; "
          "unzulässig zwischen Mitberechtigten (BPatG Fondue-Einrichtung)\n"
          "**V2 Entnahme** – wesentlicher Inhalt des Patents den Beschreibungen, Zeichnungen, Modellen, Gerätschaften oder Einrichtungen eines "
          "anderen oder einem von ihm angewendeten Verfahren ohne dessen Einwilligung entnommen (§ 21 Abs. 1 Nr. 3 PatG); Widerruf auch, wenn der "
          "Gegenstand nicht patentfähig ist (BGH Schweißheizung)\n"
          "**⇒ Rechtsfolge:** Widerruf; der Einsprechende kann binnen eines Monats nach der amtlichen Mitteilung selbst anmelden und die Priorität "
          "des früheren Patents beanspruchen (§ 7 Abs. 2 PatG), ohne Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 3 PatG); Nichtigkeitsklage wegen "
          "Entnahme nur durch den Verletzten (§ 81 Abs. 3 PatG)\n\n"
          "**C · Erfindernennung**\n"
          "**V1 Erfinderbenennung durch den Anmelder** – binnen 15 Monaten ab Anmelde- oder Prioritätstag, mit Versicherung und Angabe, wie das "
          "Recht auf ihn gelangt ist (§ 37 Abs. 1 S. 1, 2 PatG); das DPMA prüft die Richtigkeit nicht (§ 37 Abs. 1 S. 3 PatG); Nennung auf den "
          "Schriften und im Register (§ 63 Abs. 1 S. 1, 2 PatG)\n"
          "**V2 Anspruch auf Zustimmung zur Berichtigung** – Person des Erfinders unrichtig oder nicht angegeben (§ 63 Abs. 2 S. 1 PatG); "
          "Anspruchsteller hat einen schöpferischen Beitrag zum geschützten Gegenstand geleistet, unabhängig von der Schutzfähigkeit (BGH "
          "Atemgasdrucksteuerung, X ZR 53/08); Anspruchsgegner sind Patentsucher oder -inhaber und der zu Unrecht Benannte\n"
          "**⇒ Rechtsfolge:** unwiderrufliche Zustimmung gegenüber dem DPMA (§ 63 Abs. 2 S. 2 PatG); die Klage hält das Erteilungsverfahren nicht "
          "auf (§ 63 Abs. 2 S. 3 PatG); veröffentlichte Druckschriften werden nicht berichtigt (§ 63 Abs. 3 PatG)\n\n"
          "**Klausurfallen:** Unter Mitberechtigten ist der Entnahme-Einspruch unzulässig, und der Widerruf vernichtete auch den eigenen Anteil: "
          "Vindikation ist der richtige Weg. Meldet ein Mitberechtigter allein an, ist das keine Erhaltungsmaßnahme; er schuldet Ersatz (BGH "
          "Beschichtungsverfahren). Nach Ablauf der Fristen des § 8 PatG kann die Entnahme nur dem bösgläubigen Inhaber entgegengehalten werden "
          "(BGH Schweißbrennerreinigung).\n\n"
          "**In den Klausuren:** TS III/2021 (Mitberechtigung, Vindikation, Erfindernennung, Entnahme-Einspruch), TS II/2022 (Entnahme-Einspruch, "
          "§ 7 Abs. 2 PatG), RP2 I/2019 (Vindikation der Diensterfindung, Berichtigung der Erfindernennung), TS III/2022 und TS I/2022 "
          "(Erfinderbenennung).",
          concepts=["pat_recht_auf_patent", "pat_erfinderbenennung"],
          norms=["§ 6 PatG", "§ 7 PatG", "§ 8 PatG", "§ 63 PatG", "§ 37 PatG", "§ 21 PatG", "Art. II § 5 IntPatÜG"],
          cases=["pat_bgh_mitralklappenprothese", "pat_bgh_blendschutzbehang", "pat_bgh_schneidbrennerstromduese", "pat_bpatg_fondue_einrichtung",
                 "pat_bgh_schweissheizung", "pat_bgh_automatisierte_waermebehandlung"], abschnitt="Normenkette"),
    intro("p05n-1", "Definitionen",
          "**Recht auf das Patent:** Recht des Erfinders oder seines Rechtsnachfolgers, die Erfindung anzumelden und das Patent zu erhalten "
          "(§ 6 S. 1 PatG)\n"
          "**Erfinder, Miterfinder:** wer einen schöpferischen Beitrag zur Erfindung geleistet hat; maßgeblich ist der Gegenstand der geschützten "
          "Erfindung nach Haupt- und Unteransprüchen (BGH Verkranzungsverfahren, X ZR 142/01; BGH Atemgasdrucksteuerung)\n"
          "**Bruchteilsgemeinschaft:** Rechtsverhältnis der Miterfinder ohne abweichende Vereinbarung (§§ 741 ff. BGB; BGH Rollenantriebseinheit); "
          "jeder verfügt über seinen Anteil (§ 747 S. 1 BGB), Erhaltungsmaßnahmen allein (§ 744 Abs. 2 BGB)\n"
          "**Doppelerfindung:** dieselbe Erfindung unabhängig voneinander gemacht; das Recht hat der Erstanmelder (§ 6 S. 3 PatG)\n"
          "**Widerrechtliche Entnahme:** Der wesentliche Inhalt des Patents ist den Unterlagen oder dem Verfahren eines anderen ohne dessen "
          "Einwilligung entnommen (Legaldefinition § 21 Abs. 1 Nr. 3 PatG)\n"
          "**Nichtberechtigter:** wer weder Erfinder noch dessen Rechtsnachfolger ist (§ 6 S. 1 PatG, § 8 S. 1 PatG)\n"
          "**Vindikation:** Anspruch des Berechtigten auf Abtretung des Erteilungsanspruchs oder Übertragung des Patents (§ 8 S. 1, 2 PatG)\n"
          "**Diensterfindung:** während des Arbeitsverhältnisses gemachte Erfindung, die aus der obliegenden Tätigkeit entstanden ist oder "
          "maßgeblich auf Erfahrungen oder Arbeiten des Betriebs beruht (§ 4 Abs. 2 ArbnErfG)",
          concepts=["pat_recht_auf_patent"], norms=["§ 6 PatG", "§ 8 PatG", "§ 21 PatG"], cases=["pat_bgh_rollenantriebseinheit"],
          abschnitt="Definitionen"),
    mc("p05n-2", "Frist der Vindikationsklage", "Bis wann muss der Berechtigte nach der Erteilung auf Übertragung des Patents klagen?",
       ["binnen neun Monaten nach Veröffentlichung der Erteilung",
        "binnen zwei Jahren nach Veröffentlichung der Erteilung, gegen den bösgläubigen Inhaber ohne Frist",
        "binnen drei Jahren ab Kenntnis, höchstens zehn Jahre",
        "jederzeit, solange das Patent besteht"], 1,
       ["**§ 8 S. 3, 5 PatG.** Klage binnen zwei Jahren nach der Veröffentlichung der Erteilung (§ 58 Abs. 1 PatG); hat der Verletzte Einspruch "
        "wegen Entnahme erhoben, noch ein Jahr nach dessen rechtskräftigem Abschluss (§ 8 S. 4 PatG); keine Frist gegen den bei Erwerb "
        "bösgläubigen Inhaber (§ 8 S. 5 PatG). Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB."],
       merke="Vindikation: zwei Jahre ab Erteilungsveröffentlichung · ein Jahr nach Einspruch · bösgläubig unbefristet.", level=1,
       concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG"], abschnitt=DN),
    fall("p05n-3", "Mitberechtigung statt Übertragung",
         "K verlangt Übertragung des Patents, weil die Erfindung von ihm stamme. Im Prozess ergibt sich, dass K und der Ingenieur S der "
         "Patentinhaberin die Lösung gemeinsam gefunden haben.",
         "Muss das Gericht die Klage abweisen, weil K nur die volle Übertragung beantragt hat?", False,
         ["**Nein!** Miterfindern steht das Recht gemeinschaftlich zu (§ 6 S. 2 PatG). Der Anspruch auf Einräumung einer Mitberechtigung ist "
          "gegenüber dem Übertragungsanspruch ein **Minus** und im Übertragungsantrag enthalten (BGH Schneidbrennerstromdüse)."],
         merke="Mitberechtigung ist im Übertragungsantrag enthalten.", level=2, concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG", "§ 6 PatG"],
         cases=["pat_bgh_schneidbrennerstromduese"], abschnitt=DN),
    fall("p05n-4", "Mitberechtigung an einem Anspruch",
         "K hat nur zum Gegenstand des Anspruchs 3 beigetragen und verlangt eine Mitberechtigung allein an diesem Anspruch.",
         "Kann das Gericht ihm die Mitberechtigung nur an Anspruch 3 einräumen?", False,
         ["**Nein!** Eine Mitberechtigung kann nur an der Patentanmeldung oder dem Patent **als Ganzem** eingeräumt werden, nicht an einzelnen "
          "Patentansprüchen (BGH Blendschutzbehang). Der Umfang des Beitrags bestimmt nur die Höhe des Anteils."],
         merke="Mitberechtigung nur am ganzen Schutzrecht.", level=2, concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG"],
         cases=["pat_bgh_blendschutzbehang"], abschnitt=DN),
    mc("p05n-5", "Wer darf wegen Entnahme einsprechen?", "Wer darf einen Einspruch auf widerrechtliche Entnahme (§ 21 Abs. 1 Nr. 3 PatG) "
       "stützen?",
       ["jeder", "nur der Verletzte", "nur ein eingetragener Lizenznehmer", "nur das DPMA von Amts wegen"], 1,
       ["**Nur der Verletzte** (§ 59 Abs. 1 S. 1 PatG). Gleiches gilt für die Nichtigkeitsklage wegen Entnahme (§ 81 Abs. 3 PatG). Sind "
        "Einsprechender und Inhaber Mitberechtigte, etwa aus einer gemeinsamen Entwicklungs-GbR, ist der Einspruch mangels Berechtigung "
        "unzulässig (BPatG Fondue-Einrichtung)."],
       merke="Entnahme: Einspruch und Nichtigkeitsklage nur durch den Verletzten.", level=1, concepts=["pat_recht_auf_patent", "pat_einspruch"],
       norms=["§ 59 PatG", "§ 81 PatG"], cases=["pat_bpatg_fondue_einrichtung"], abschnitt=DN),
    fall("p05n-6", "Nachanmeldefrist versäumt",
         "Auf den Entnahme-Einspruch der N wird das Patent widerrufen; die amtliche Mitteilung geht ihr am 02.03. zu. N reicht ihre eigene "
         "Anmeldung erst am 15.04. ein und beantragt Wiedereinsetzung.",
         "Kann N die Priorität des widerrufenen Patents noch beanspruchen?", False,
         ["**Nein!** Die Nachanmeldung mit der Priorität des früheren Patents muss binnen eines Monats nach der amtlichen Mitteilung eingehen "
          "(§ 7 Abs. 2 PatG), hier bis 02.04. In diese Frist gibt es keine Wiedereinsetzung (§ 123 Abs. 1 S. 2 Nr. 3 PatG)."],
         merke="Nachanmelderecht § 7 Abs. 2 PatG: ein Monat, keine Wiedereinsetzung.", level=2, concepts=["pat_recht_auf_patent"],
         norms=["§ 7 PatG", "§ 123 PatG"], abschnitt=DN),
    fall("p05n-7", "Berichtigung trotz fehlender Schutzfähigkeit",
         "E verlangt von der Patentinhaberin und dem benannten G die Zustimmung, statt G als Erfinder genannt zu werden. Die Inhaberin wendet ein, "
         "das Patent sei ohnehin nicht rechtsbeständig.",
         "Hängt der Berichtigungsanspruch von der Schutzfähigkeit der Erfindung ab?", False,
         ["**Nein!** Der Anspruch aus § 63 Abs. 2 S. 1 PatG besteht unabhängig von der Schutzfähigkeit. Er steht, wie die Vindikation, dem zu, "
          "der einen schöpferischen Beitrag zum Gegenstand der geschützten Erfindung geleistet hat (BGH Atemgasdrucksteuerung, X ZR 53/08)."],
         merke="Berichtigung § 63 Abs. 2 PatG: schöpferischer Beitrag genügt, Schutzfähigkeit egal.", level=2,
         concepts=["pat_erfinderbenennung"], norms=["§ 63 PatG"], abschnitt=DN),
    mc("p05n-8", "Erfinderbenennung", "Bis wann muss der Anmelder den Erfinder benennen?",
       ["mit der Anmeldung", "binnen 15 Monaten nach dem Anmelde- oder Prioritätstag", "binnen sieben Jahren mit dem Prüfungsantrag",
        "erst nach der Erteilung"], 1,
       ["**§ 37 Abs. 1 S. 1 PatG.** Binnen 15 Monaten nach dem Anmeldetag oder dem früheren maßgeblichen Zeitpunkt; dazu die Versicherung, "
        "dass weitere Personen nicht beteiligt sind, und, wenn der Anmelder nicht Erfinder ist, wie das Recht auf ihn gelangt ist "
        "(§ 37 Abs. 1 S. 2 PatG). Verlängerung nur bis zum Erteilungsbeschluss (§ 37 Abs. 2 S. 2 PatG)."],
       merke="Erfinderbenennung: 15 Monate (§ 37 Abs. 1 PatG), Form § 7 PatV.", level=1, concepts=["pat_erfinderbenennung"],
       norms=["§ 37 PatG", "§ 7 PatV"], abschnitt=DN),
    *fallkette("p05n-9", "Herr Reich als Miterfinder (nach TS III/2021)",
        "Frau Neuer, Arbeitnehmerin der Konkurrenz GmbH, und der freie Konstrukteur Reich entwickeln gemeinsam einen Wanderstock. Die GmbH nimmt "
        "Neuers Diensterfindung in Anspruch, meldet allein an und benennt nur Neuer als Erfinderin. Die Erteilung des DE 456 B1 wurde vor einem "
        "Jahr veröffentlicht.",
        [frage("Steht Reich ein Anteil am Recht auf das Patent zu?", True,
               ["**Ja!** Haben mehrere gemeinsam eine Erfindung gemacht, steht ihnen das Recht gemeinschaftlich zu (§ 6 S. 2 PatG). Miterfinder ist, "
                "wer einen schöpferischen Beitrag geleistet hat (BGH Verkranzungsverfahren, X ZR 142/01). Die GmbH hält nur Neuers Anteil "
                "(§ 7 Abs. 1 ArbnErfG)."],
               merke="Miterfinder: schöpferischer Beitrag, Bruchteilsgemeinschaft.", titel="V1 Berechtigung", norms=["§ 6 PatG"]),
         frage("Kann Reich die Übertragung des ganzen Patents verlangen?", False,
               ["**Nein!** Er kann nur die Einräumung einer Mitberechtigung verlangen (§ 8 S. 2 PatG; BGH Blendschutzbehang), und zwar am Patent als "
                "Ganzem."],
               merke="Teilweise Berechtigung: Mitberechtigung, keine Vollübertragung.", titel="V3 Umfang", cases=["pat_bgh_blendschutzbehang"]),
         frage("Ist die Klage noch fristgerecht?", True,
               ["**Ja!** Zwei Jahre nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG; § 187 Abs. 1 BGB, § 188 Abs. 2 BGB); erst ein Jahr ist "
                "verstrichen. War die GmbH beim Erwerb bösgläubig, gilt keine Frist (§ 8 S. 5 PatG)."],
               merke="§ 8 S. 3 PatG: zwei Jahre ab Veröffentlichung der Erteilung.", titel="V4 Frist", norms=["§ 8 PatG"]),
         frage("Ist ein Einspruch wegen widerrechtlicher Entnahme der bessere Weg?", False,
               ["**Nein!** Zwischen Mitberechtigten ist er mangels Berechtigung unzulässig (BPatG Fondue-Einrichtung). Selbst ein Widerruf "
                "vernichtete auch Reichs eigenen Anteil; das Nachanmelderecht (§ 7 Abs. 2 PatG) hilft ihm wenig. Die Vindikation erhält das Patent."],
               merke="Mitberechtigter: Vindikation statt Entnahme-Einspruch.", titel="Entnahme-Einspruch", cases=["pat_bpatg_fondue_einrichtung"]),
         frage("Kann Reich verlangen, als Miterfinder genannt zu werden?", True,
               ["**Ja!** Die Erfindernennung ist unrichtig (§ 63 Abs. 2 S. 1 PatG). Die GmbH als Inhaberin und Neuer als allein Benannte müssen der "
                "Berichtigung gegenüber dem DPMA zustimmen, unwiderruflich (§ 63 Abs. 2 S. 2 PatG); die Patentschrift selbst wird nicht berichtigt "
                "(§ 63 Abs. 3 PatG)."],
               merke="§ 63 Abs. 2 PatG: Zustimmung von Inhaber und zu Unrecht (allein) Benannter.", titel="C Erfindernennung", norms=["§ 63 PatG"]),
         ],
        abschnitt=KF, level=2, concepts=["pat_recht_auf_patent", "pat_erfinderbenennung"], norms=["§ 8 PatG"]),
    *fallkette("p05n-10", "Die Tastaturbeleuchtung (nach RP2 I/2019)",
        "Ingenieur E1 der A-GmbH macht im Rahmen seiner Entwicklungsaufgaben eine Erfindung, meldet sie der A nicht und erwirkt ein Patent auf "
        "seinen Namen. Die Erteilung wurde vor einem Jahr veröffentlicht. Die A erfährt davon, nimmt die Erfindung am Di 29.01.2019 durch "
        "Erklärung gegenüber E1 in Anspruch und verlangt Übertragung.",
        [frage("Ist die A durch die Inanspruchnahme Berechtigte geworden?", True,
               ["**Ja!** Diensterfindung (§ 4 Abs. 2 Nr. 1 ArbnErfG). Die Inanspruchnahme durch Erklärung (§ 6 Abs. 1 ArbnErfG) ist ohne Meldung an "
                "keine Frist gebunden. Mit ihr gehen alle vermögenswerten Rechte über (§ 7 Abs. 1 ArbnErfG); die A ist Rechtsnachfolgerin "
                "(§ 6 S. 1 PatG)."],
               merke="Arbeitgeber wird durch Inanspruchnahme Rechtsnachfolger des Erfinders.", titel="V1 Berechtigung"),
         frage("Ist § 8 S. 2 PatG die richtige Anspruchsgrundlage?", True,
               ["**Ja!** Die Anmeldung des Nichtberechtigten hat bereits zum Patent geführt; der Berechtigte verlangt vom Patentinhaber Übertragung "
                "(§ 8 S. 2 PatG). Vor der Erteilung wäre es die Abtretung des Erteilungsanspruchs (§ 8 S. 1 PatG), beim europäischen Patent "
                "Art. II § 5 Abs. 1 IntPatÜG."],
               merke="Vor Erteilung § 8 S. 1 PatG, nach Erteilung § 8 S. 2 PatG; EP: Art. II § 5 IntPatÜG.", titel="AGL", norms=["§ 8 PatG"]),
         frage("Ist die Klage noch fristgerecht?", True,
               ["**Ja!** Zwei Jahre nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG) sind nicht abgelaufen. Zudem musste E1 die nicht frei "
                "gewordene Diensterfindung geheim halten (§ 24 Abs. 2 ArbnErfG); war er beim Erwerb bösgläubig, gilt keine Frist (§ 8 S. 5 PatG)."],
               merke="Frist § 8 S. 3 PatG; bösgläubiger Inhaber § 8 S. 5 PatG.", titel="V4 Frist"),
         frage("Wird die A Berechtigte, wenn sie nach ordnungsgemäßer Meldung vier Monate schweigt?", True,
               ["**Ja!** Die Inanspruchnahme gilt als erklärt, wenn der Arbeitgeber nicht binnen vier Monaten nach Eingang der ordnungsgemäßen "
                "Meldung in Textform freigibt (§ 6 Abs. 2 ArbnErfG). Schweigen ist keine Freigabe (§ 8 S. 1 ArbnErfG)."],
               abwandlung="E1 hatte die Erfindung der A ordnungsgemäß gemeldet; die A reagiert nicht.",
               merke="Fiktion der Inanspruchnahme nach vier Monaten (§ 6 Abs. 2 ArbnErfG).", titel="Abwandlung: Meldung"),
         ],
        abschnitt=KF, level=2, concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG"]),
])

KAPITEL = [K_H, K_I, K_J, K_K, K_L, K_M, K_N]
