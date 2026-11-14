# -*- coding: utf-8 -*-
"""Anspruchsgrundlagen für die Klausur: Arbeitnehmererfinderrecht (Rechtspraxis 2 der Patentanwaltsprüfung).

Ein Kapitel je Anspruchsgrundlage bzw. Rechtsbehelf: Prüfungsschema in der Lösungssprache (AGL → Voraussetzungen mit Norm →
Rechtsfolge), Definitionen, Drill zu Normen und Fristen, Klausurfälle als Fallketten. Grundlage sind die Lösung zu RP2 I/2019
(klausuren/loesungen/rp2/PAP-2019-I-RP2.json) und die Aufgabentexte aller RP2-Klausuren II/2018 bis III/2023. Normtexte aus
data/arbnerfg.json (geltende Fassung) und data/patg.json, Vergütungsrichtlinien aus data/arbnerfg_vergrl.json („RL Nr. 34“);
Entscheidungen nur mit Aktenzeichen und Datum aus data/arbnerfg_decisions.json bzw. data/patent_decisions.json. Altfälle
(Meldung vor dem 1.10.2009) nach ArbnErfG a.F. (§ 43 Abs. 3 ArbnErfG); Aussagen zur a.F. nur, soweit Leitsätze sie belegen."""
from ._helpers import intro, mc, fall, frage, fallkette

D = "Definitionen und Normen"
K = "Klausurfall"

# ====================================================================== p070 Überblick
P070 = dict(id="p070", titel="Überblick: Anspruchsgrundlagen und Fristen", einheiten=[
    intro("p070-0", "Die Anspruchsgrundlagen im Überblick",
          "Fast jede RP2-Klausur ist ein Mandantenschreiben: Ein Arbeitnehmer will Geld, Nennung oder seine Erfindung zurück, ein "
          "Arbeitgeber will die Rechte, will weniger zahlen oder nicht anmelden. Erst das Ziel bestimmen, dann die AGL.\n\n"
          "**Arbeitnehmer will …**\n"
          "**Geld für die Erfindung** → § 9 Abs. 1 ArbnErfG (Grund), § 9 Abs. 2 ArbnErfG mit RL Nr. 39 (Höhe: V = E × A × Miterfinderanteil)\n"
          "**die Zahlen zum Rechnen** → Auskunft und Rechnungslegung, § 242 BGB i.V.m. § 9 Abs. 1 ArbnErfG\n"
          "**mehr als vereinbart oder festgesetzt** → Widerspruch § 12 Abs. 4 ArbnErfG (zwei Monate); Unwirksamkeit § 23 Abs. 1 ArbnErfG "
          "(Unbilligkeit bei Abschluss); Anpassung § 12 Abs. 6 ArbnErfG (spätere wesentliche Änderung)\n"
          "**überhaupt eine Regelung** → Festsetzungspflicht § 12 Abs. 3 ArbnErfG; Klage auf angemessenen Betrag § 38 ArbnErfG\n"
          "**die Erfindung selbst** → Freigabe § 8 ArbnErfG (Altfall: Freiwerden nach § 8 Abs. 1 Nr. 3 ArbnErfG a.F.); Übertragung bei "
          "Aufgabe § 16 Abs. 1 ArbnErfG; Auslandsfreigabe § 14 Abs. 2 ArbnErfG; Insolvenz § 27 Nr. 3 ArbnErfG\n"
          "**die Anmeldung** → Ersatzvornahme § 13 Abs. 3 ArbnErfG; Schadensersatz § 823 Abs. 2 BGB i.V.m. § 13 Abs. 1 ArbnErfG\n"
          "**als Erfinder genannt werden** → § 63 Abs. 2 S. 1 PatG\n"
          "**das Patent bei frei gewordener Erfindung** → § 8 S. 2 PatG i.V.m. § 8 S. 1 ArbnErfG\n\n"
          "**Arbeitgeber will …**\n"
          "**die Rechte an der Erfindung** → Inanspruchnahme § 6 Abs. 1 oder Abs. 2 ArbnErfG, Rechtsfolge § 7 Abs. 1 ArbnErfG\n"
          "**das Patent, das der Arbeitnehmer selbst angemeldet hat** → § 8 S. 2 PatG i.V.m. § 7 Abs. 1 ArbnErfG, § 7 Abs. 2 ArbnErfG\n"
          "**ein Benutzungsrecht an einer freien Erfindung** → § 19 Abs. 1 ArbnErfG; Vorbehalt bei Freigabe § 14 Abs. 3 ArbnErfG, "
          "bei Aufgabe § 16 Abs. 3 ArbnErfG\n"
          "**nicht anmelden** → § 13 Abs. 2 ArbnErfG (Freigabe, Zustimmung, Betriebsgeheimnis nach § 17 ArbnErfG)\n"
          "**ein Schutzrecht fallen lassen** → § 16 ArbnErfG\n"
          "**weniger zahlen** → § 12 Abs. 6 ArbnErfG; § 23 Abs. 1 ArbnErfG (auch der Arbeitgeber, BGH Chemische Verbrauchsmaterialien)\n\n"
          "**Durchsetzung:** Schiedsstelle beim DPMA (§ 28 S. 1 ArbnErfG, § 29 Abs. 1 ArbnErfG), Klage erst nach Schiedsverfahren "
          "(§ 37 Abs. 1 ArbnErfG) außer § 37 Abs. 2 ArbnErfG, ausschließlich bei den Patentstreitkammern (§ 39 Abs. 1 ArbnErfG, "
          "§ 143 Abs. 1 PatG).\n\n"
          "**In den Klausuren:** Vergütung (RP2 II/2018, II/2019, II/2020, III/2021, I/2022, III/2022, I/2023, II/2023), Anpassung und "
          "Unbilligkeit (RP2 III/2019, I/2021, II/2021, I/2022), Meldung und Inanspruchnahme (RP2 I/2019, III/2020, II/2021, I/2022, "
          "III/2023), Anmeldepflicht (RP2 I/2021, II/2023), Erfindernennung und Vindikation (RP2 III/2018, I/2019, I/2020, III/2023), "
          "Schiedsstelle (RP2 I/2020, II/2022), Verkauf und Insolvenz (RP2 III/2022, I/2023).",
          concepts=["arb_verguetungsanspruch", "arb_inanspruchnahme", "arb_schiedsstelle"],
          norms=["§ 9 ArbnErfG", "§ 6 ArbnErfG", "§ 12 ArbnErfG", "§ 63 PatG", "§ 8 PatG"], abschnitt="Überblick"),
    intro("p070-1", "Fristen und Gebühren",
          "Alle Fristen des ArbnErfG werden nach dem BGB berechnet (§ 186 BGB): Beginn am Tag nach dem Ereignis (§ 187 Abs. 1 BGB), "
          "Ende am Tag mit derselben Zahl (§ 188 Abs. 2 BGB), Verschiebung auf den nächsten Werktag (§ 193 BGB). Maßgeblich ist der "
          "Zugang der Erklärung (§ 130 Abs. 1 S. 1 BGB). Textform: § 126b BGB; Schriftform: § 126 Abs. 1 BGB.\n\n"
          "**Meldung** – unverzüglich (§ 5 Abs. 1 S. 1 ArbnErfG; „ohne schuldhaftes Zögern“, § 121 Abs. 1 S. 1 BGB) · Eingangsbestätigung "
          "unverzüglich in Textform (§ 5 Abs. 1 S. 3 ArbnErfG)\n"
          "**Beanstandung der Meldung** – zwei Monate ab Eingang (§ 5 Abs. 3 S. 1 ArbnErfG)\n"
          "**Freigabe, sonst Fiktion der Inanspruchnahme** – vier Monate ab Eingang der ordnungsgemäßen Meldung, Textform (§ 6 Abs. 2 ArbnErfG)\n"
          "**Bestreiten einer mitgeteilten freien Erfindung** – drei Monate ab Zugang, Textform (§ 18 Abs. 2 ArbnErfG)\n"
          "**Annahme des Benutzungsangebots** – drei Monate (§ 19 Abs. 2 ArbnErfG)\n"
          "**Festsetzung der Vergütung** – spätestens drei Monate nach Erteilung des Schutzrechts (§ 12 Abs. 3 S. 2 ArbnErfG)\n"
          "**Widerspruch gegen Festsetzung** – zwei Monate, Textform (§ 12 Abs. 4 S. 1 ArbnErfG)\n"
          "**Übertragungsverlangen bei Aufgabe** – drei Monate ab Zugang der Mitteilung (§ 16 Abs. 2 ArbnErfG)\n"
          "**Unbilligkeit geltend machen** – bis sechs Monate nach Beendigung des Arbeitsverhältnisses, Textform (§ 23 Abs. 2 ArbnErfG)\n"
          "**Insolvenz** – Angebot spätestens ein Jahr nach Eröffnung, Annahme binnen zwei Monaten (§ 27 Nr. 3 ArbnErfG)\n"
          "**Schiedsstelle** – Erweiterungsantrag des Gegners zwei Wochen nach Zustellung (§ 32 ArbnErfG); Widerspruch gegen den "
          "Einigungsvorschlag ein Monat nach Zustellung, schriftlich (§ 34 Abs. 3 ArbnErfG); Wiedereinsetzung ein Monat nach Wegfall des "
          "Hindernisses, höchstens ein Jahr (§ 34 Abs. 4 ArbnErfG); Klage ohne Abschluss nach sechs Monaten (§ 37 Abs. 2 Nr. 2 ArbnErfG)\n"
          "**Vindikation** – zwei Jahre nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG, § 58 Abs. 1 PatG), nach Einspruch ein Jahr "
          "nach dessen Abschluss (§ 8 S. 4 PatG), bei Bösgläubigkeit unbefristet (§ 8 S. 5 PatG)\n"
          "**Einspruch wegen widerrechtlicher Entnahme** – neun Monate nach Veröffentlichung der Erteilung (§ 59 Abs. 1 S. 1 PatG); "
          "Nachanmeldung binnen eines Monats (§ 7 Abs. 2 PatG)\n"
          "**Verjährung des Vergütungsanspruchs** – drei Jahre (§ 195 BGB) ab Schluss des Jahres von Entstehung und Kenntnis (§ 199 Abs. 1 BGB); "
          "Hemmung durch Verhandlungen (§ 203 BGB) und durch Anrufung der Schiedsstelle (§ 204 Abs. 1 Nr. 4 BGB analog, BGH Profilstrangpressverfahren)\n\n"
          "**Gebühren:** keine. Das Schiedsverfahren ist gebühren- und auslagenfrei (§ 36 ArbnErfG). Für die Klage gelten die Kosten der "
          "Patentstreitsache; Patentanwaltskosten sind zu erstatten (§ 143 Abs. 3 PatG, § 39 Abs. 1 S. 2 ArbnErfG).",
          concepts=["arb_erfindungsmeldung", "arb_festsetzung", "arb_unbilligkeit"],
          norms=["§ 5 ArbnErfG", "§ 6 ArbnErfG", "§ 12 ArbnErfG", "§ 16 ArbnErfG", "§ 23 ArbnErfG", "§ 34 ArbnErfG"], abschnitt="Überblick"),
    intro("p070-2", "Altfälle: Meldung vor dem 1.10.2009",
          "Auf Erfindungen, die vor dem 1.10.2009 gemeldet wurden, ist das ArbnErfG in der bis zum 30.9.2009 geltenden Fassung anzuwenden "
          "(§ 43 Abs. 3 S. 1 ArbnErfG). Maßgeblich ist das Datum der Meldung, bei unterlassener Meldung der Zeitpunkt, zu dem hätte "
          "gemeldet werden müssen (Schiedsstelle Arb.Erf. 21/09).\n\n"
          "**Was im Altfall anders ist (belegt):**\n"
          "**Schriftform statt Textform** – die Meldung muss unterschrieben im Original zugehen (§ 5 ArbnErfG a.F.; BGH Lichtschutzfolie, "
          "Fesoterodinhydrogenfumarat); ebenso der Widerspruch gegen die Festsetzung (E-Mail genügt nicht, Schiedsstelle Arb.Erf. 34/08) "
          "und die Geltendmachung der Unbilligkeit (Fax genügt nicht, Schiedsstelle Arb.Erf. 03/09).\n"
          "**Keine Fiktion** – der Arbeitgeber muss binnen vier Monaten nach Eingang der ordnungsgemäßen Meldung schriftlich in Anspruch "
          "nehmen (§ 6 Abs. 2 S. 2 ArbnErfG a.F.), sonst wird die Erfindung frei (§ 8 Abs. 1 Nr. 3 ArbnErfG a.F.; Schiedsstelle Arb.Erf. 15/03).\n"
          "**Beschränkte oder unbeschränkte Inanspruchnahme** – die beschränkte verschafft nur ein nichtausschließliches Benutzungsrecht "
          "(RL Nr. 25).\n\n"
          "**In den Klausuren:** RP2 II/2021 (Meldung 16.07.2009, Inanspruchnahme 24.11.2009), RP2 I/2022 (E1 gemeldet 2007), "
          "RP2 II/2022 (Meldung 2008), RP2 I/2023 (Patent A angemeldet 2008); dagegen neues Recht in RP2 II/2019 (Meldung 04.10.2009) "
          "und RP2 I/2022 (E2 gemeldet 05.10.2009).",
          concepts=["arb_altrecht"], norms=["§ 43 ArbnErfG", "§ 6 ArbnErfG"], abschnitt="Überblick"),
    mc("p070-3", "Pauschale später zu niedrig",
       "Der Mandant will mehr Geld – welche AGL prüfen Sie zuerst?",
       ["Anpassung nach § 12 Abs. 6 S. 1 ArbnErfG",
        "Unwirksamkeit wegen Unbilligkeit nach § 23 Abs. 1 ArbnErfG",
        "Widerspruch gegen die Festsetzung nach § 12 Abs. 4 ArbnErfG",
        "Übertragung des Patents nach § 16 Abs. 1 ArbnErfG"], 0,
       ["**§ 12 Abs. 6 S. 1 ArbnErfG.** Die Pauschale war bei Abschluss angemessen; erst danach haben sich die maßgebenden Umstände "
        "wesentlich geändert. Das ist der Fall der Anpassung. § 23 Abs. 1 ArbnErfG misst die Unbilligkeit am Zeitpunkt der Vereinbarung, "
        "§ 12 Abs. 4 ArbnErfG betrifft nur einseitige Festsetzungen."],
       sachverhalt="2014 vereinbarte Arbeitnehmer W eine angemessene Pauschalvergütung von 1.000 € für einen Abzug, dessen Einsatz damals "
                   "nicht geplant war. Heute sind alle Sportflinten seines Arbeitgebers damit ausgestattet (nach RP2 I/2021).",
       merke="Unbillig bei Abschluss → § 23 ArbnErfG; später wesentlich geändert → § 12 Abs. 6 ArbnErfG.", level=1,
       concepts=["arb_anpassung", "arb_unbilligkeit"], norms=["§ 12 Abs. 6 ArbnErfG", "§ 23 ArbnErfG"], abschnitt="Welche AGL?"),
    mc("p070-4", "Patent beim Arbeitnehmer",
       "Welche AGL hat der Arbeitgeber auf Herausgabe des Patents?",
       ["§ 8 S. 2 PatG i.V.m. § 7 Abs. 1 ArbnErfG nach Inanspruchnahme",
        "§ 16 Abs. 1 ArbnErfG",
        "§ 13 Abs. 3 ArbnErfG",
        "§ 63 Abs. 2 S. 1 PatG"], 0,
       ["**§ 8 S. 2 PatG i.V.m. § 7 Abs. 1 ArbnErfG.** Berechtigter ist der Arbeitgeber, sobald er die Diensterfindung in Anspruch "
        "genommen hat; die vorherige Anmeldung des Arbeitnehmers ist ihm gegenüber unwirksam (§ 7 Abs. 2 ArbnErfG). Ist das Patent "
        "erteilt, richtet sich der Anspruch auf Übertragung des Patents."],
       sachverhalt="Entwickler E meldet eine Diensterfindung nicht, sondern lässt sie auf eigenen Namen patentieren. Danach erklärt der "
                   "Arbeitgeber die Inanspruchnahme (nach RP2 I/2019).",
       merke="Vindikation des Arbeitgebers: § 8 S. 2 PatG + § 7 Abs. 1 ArbnErfG; Frist § 8 S. 3 PatG.", level=1,
       concepts=["arb_inanspruchnahme", "pat_recht_auf_patent"], norms=["§ 8 PatG", "§ 7 ArbnErfG"], abschnitt="Welche AGL?"),
    mc("p070-5", "Umsätze unbekannt",
       "Der ausgeschiedene Erfinder kennt die Konzernumsätze nicht. Worauf stützt er sein Verlangen nach Zahlen?",
       ["Auskunft und Rechnungslegung nach § 242 BGB als Hilfsanspruch zu § 9 Abs. 1 ArbnErfG",
        "§ 15 Abs. 1 ArbnErfG",
        "§ 12 Abs. 2 S. 2 ArbnErfG",
        "§ 24 Abs. 1 ArbnErfG"], 0,
       ["**§ 242 BGB.** Der Erfinder kann Auskunft und Rechnungslegung verlangen, soweit er die Angaben zur Berechnung braucht und der "
        "Arbeitgeber sie zumutbar geben kann. § 15 Abs. 1 ArbnErfG betrifft nur das Anmeldeverfahren, § 12 Abs. 2 S. 2 ArbnErfG nur "
        "Gesamthöhe und Anteile bei Miterfindern."],
       sachverhalt="Y ist 2016 ausgeschieden. Seine Erfindung nutzen auch Konzerngesellschaften in Frankreich und den USA; er erhielt "
                   "nur eine Tabelle mit Mengen und Umsätzen der Mutter (nach RP2 III/2018).",
       merke="Auskunft: § 242 BGB i.V.m. § 9 Abs. 1 ArbnErfG; Umfang folgt der Berechnungsmethode.", level=1,
       concepts=["arb_auskunft"], norms=["§ 9 ArbnErfG"], abschnitt="Welche AGL?"),
    mc("p070-6", "Nicht als Erfinder genannt",
       "Welche AGL hat die ehemalige Mitarbeiterin auf Nennung als Miterfinderin?",
       ["§ 63 Abs. 2 S. 1 PatG", "§ 8 S. 1 PatG", "§ 5 Abs. 2 ArbnErfG", "§ 12 Abs. 5 ArbnErfG"], 0,
       ["**§ 63 Abs. 2 S. 1 PatG.** Ist die Person des Erfinders unrichtig angegeben, müssen Anmelder und zu Unrecht Benannter der "
        "Berichtigung gegenüber dem DPMA zustimmen. Das ist ein Recht aus dem PatG, kein Recht aus dem ArbnErfG; die Schiedsstelle ist "
        "nicht vorzuschalten."],
       sachverhalt="Dr. P schlug vor, den hohlen Flintenschaft mit PU-Schaum zu füllen. In der Patentanmeldung ihres früheren Arbeitgebers "
                   "sind nur der Entwicklungsleiter und der Geschäftsführer als Erfinder benannt (nach RP2 I/2020).",
       merke="Nennung: § 63 Abs. 2 S. 1 PatG gegen Anmelder/Inhaber und zu Unrecht Benannten.", level=1,
       concepts=["pat_erfinderbenennung", "arb_miterfinder"], norms=["§ 63 PatG"], abschnitt="Welche AGL?"),
    mc("p070-7", "Patent soll verfallen",
       "Was muss der Arbeitgeber vor dem Fallenlassen tun?",
       ["Dem Erfinder die Aufgabeabsicht mitteilen und auf Verlangen das Patent übertragen (§ 16 Abs. 1 ArbnErfG)",
        "Das Patent in Textform freigeben (§ 8 S. 1 ArbnErfG)",
        "Die Schiedsstelle anrufen (§ 17 Abs. 2 ArbnErfG)",
        "Nichts, die Jahresgebühr nicht zu zahlen ist seine freie Entscheidung"], 0,
       ["**§ 16 Abs. 1 ArbnErfG.** Solange der Vergütungsanspruch nicht erfüllt ist, muss der Arbeitgeber die Aufgabe mitteilen und das "
        "Recht auf Verlangen und Kosten des Erfinders übertragen. Verlangt dieser nicht binnen drei Monaten, darf er aufgeben "
        "(§ 16 Abs. 2 ArbnErfG); ein Benutzungsrecht kann er sich vorbehalten (§ 16 Abs. 3 ArbnErfG)."],
       sachverhalt="Die Druckmaschinen-GmbH nutzt das Patent ihres früheren Mitarbeiters G nicht mehr und will die Jahresgebühren sparen; "
                   "vergütet ist nur die Nutzung bis 2012 (nach RP2 II/2022).",
       merke="Aufgabe vor Erfüllung: Mitteilung · drei Monate · Übertragung · Vorbehalt (§ 16 ArbnErfG).", level=1,
       concepts=["arb_aufgabe_schutzrecht"], norms=["§ 16 ArbnErfG"], abschnitt="Welche AGL?"),
    fall("p070-8", "Meldung 2008",
         "Fertigungsingenieurin M meldete eine Diensterfindung im Januar 2008 schriftlich. Der Arbeitgeber schwieg bis heute.",
         "Gilt die Inanspruchnahme nach § 6 Abs. 2 ArbnErfG als erklärt?", False,
         ["**Nein!** Die Meldung ging vor dem 1.10.2009 ein; anzuwenden ist das ArbnErfG a.F. (§ 43 Abs. 3 S. 1 ArbnErfG). Es kannte keine "
          "Fiktion: Ohne schriftliche Inanspruchnahme binnen vier Monaten wurde die Erfindung frei (§ 8 Abs. 1 Nr. 3 ArbnErfG a.F.)."],
         merke="Zuerst das Meldedatum: vor dem 1.10.2009 → a.F., keine Fiktion.", level=1,
         concepts=["arb_altrecht"], norms=["§ 43 ArbnErfG"], abschnitt="Welche AGL?"),
    fall("p070-9", "Meldung am 4. Oktober 2009",
         "Entwicklungsleiter L meldete seine Golfschlägererfindung ordnungsgemäß am 04.10.2009. Der Arbeitgeber reagierte nur mit "
         "Patentanmeldungen (nach RP2 II/2019).",
         "Gilt für die Inanspruchnahme das neue Recht?", True,
         ["**Ja!** Nur Meldungen vor dem 1.10.2009 bleiben beim alten Recht (§ 43 Abs. 3 S. 1 ArbnErfG). Hier gilt § 6 Abs. 2 ArbnErfG: "
          "Ohne Freigabe in Textform gilt die Erfindung vier Monate nach Eingang als in Anspruch genommen, also mit Ablauf des 04.02.2010 "
          "(§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB)."],
         merke="Stichtag 1.10.2009: Meldung danach → Fiktion nach § 6 Abs. 2 ArbnErfG.", level=2,
         concepts=["arb_altrecht", "arb_inanspruchnahme"], norms=["§ 43 ArbnErfG", "§ 6 Abs. 2 ArbnErfG"], abschnitt="Welche AGL?"),
])

# ====================================================================== p07a Diensterfindung und Meldung
P07A = dict(id="p07a", titel="§§ 4, 5, 18, 19 ArbnErfG: Diensterfindung und Meldung", einheiten=[
    intro("p07a-0", "Prüfungsschema",
          "**Prüfungsgegenstand:** Meldepflicht und ordnungsgemäße Meldung, § 5 Abs. 1 S. 1 ArbnErfG – Vorfrage für die Fiktion "
          "(§ 6 Abs. 2 ArbnErfG), die Anmeldepflicht (§ 13 Abs. 1 S. 1 ArbnErfG) und die Vergütung (§ 9 Abs. 1 ArbnErfG)\n\n"
          "**A · Anwendungsbereich**\n"
          "**V1 Arbeitnehmer** – § 1 ArbnErfG (privater und öffentlicher Dienst, Beamte, Soldaten); Arbeitnehmer ist, wer weisungsgebundene, "
          "fremdbestimmte Arbeit in persönlicher Abhängigkeit leistet (§ 611a Abs. 1 S. 1 BGB). Leiharbeitnehmer: Rechte und Pflichten "
          "gegenüber dem Entleiher (Schiedsstelle Arb.Erf. 24/23); nicht der GmbH-Geschäftsführer (Arb.Erf. 58/16)\n"
          "**V2 Erfindung** – § 2 ArbnErfG: patent- oder gebrauchsmusterfähig; sonst technischer Verbesserungsvorschlag (§ 3 ArbnErfG), "
          "vergütet nur bei Vorzugsstellung (§ 20 Abs. 1 ArbnErfG)\n"
          "**V3 Während des Arbeitsverhältnisses gemacht** – § 4 Abs. 2 ArbnErfG: fertig, sobald die Lehre ausführbar ist; nach dem "
          "Ausscheiden fertiggestellte Erfindungen sind frei\n"
          "**V4 Diensterfindung** – § 4 Abs. 2 Nr. 1 ArbnErfG (aus der obliegenden Tätigkeit) oder § 4 Abs. 2 Nr. 2 ArbnErfG (maßgeblich auf "
          "Erfahrungen oder Arbeiten des Betriebs); sonst freie Erfindung (§ 4 Abs. 3 ArbnErfG) → Mitteilung und Angebot (§ 18 ArbnErfG, "
          "§ 19 ArbnErfG)\n\n"
          "**B · Ordnungsgemäße Meldung**\n"
          "**V5 Unverzüglich** – § 5 Abs. 1 S. 1 ArbnErfG, ohne schuldhaftes Zögern (§ 121 Abs. 1 S. 1 BGB)\n"
          "**V6 Gesondert** – eigenes, als Erfindungsmeldung erkennbares Schriftstück, nicht Teil eines Berichts oder Antrags (BGH "
          "Fesoterodinhydrogenfumarat zur a.F.)\n"
          "**V7 Textform** – § 5 Abs. 1 S. 1 ArbnErfG, § 126b BGB; Altfall: Schriftform (§ 5 ArbnErfG a.F., BGH Lichtschutzfolie)\n"
          "**V8 Kenntlich als Meldung einer Erfindung** – § 5 Abs. 1 S. 1 ArbnErfG (fehlt bei einem „Produktvorschlag“ an die Kommission "
          "für Verbesserungsvorschläge, Schiedsstelle Arb.Erf. 01/02)\n"
          "**V9 Zugang beim Arbeitgeber** – § 130 Abs. 1 S. 1 BGB; Geschäftsführer, Patentabteilung oder angewiesene Patentabteilung der "
          "Konzernmutter als Empfangsvertreterin (Arb.Erf. 49/16); Miterfinder können gemeinsam melden (§ 5 Abs. 1 S. 2 ArbnErfG)\n"
          "**V10 Inhalt** – Aufgabe, Lösung, Zustandekommen (§ 5 Abs. 2 S. 1 ArbnErfG); Soll-Angaben zu Weisungen, Mitarbeitern und eigenem "
          "Anteil (§ 5 Abs. 2 S. 3 ArbnErfG). Mängel muss der Arbeitgeber binnen zwei Monaten beanstanden, sonst gilt die Meldung als "
          "ordnungsgemäß (§ 5 Abs. 3 S. 1 ArbnErfG; Arb.Erf. 34/06)\n\n"
          "**⇒ Rechtsfolge:** Eingangsbestätigung (§ 5 Abs. 1 S. 3 ArbnErfG), Lauf der Viermonatsfrist (§ 6 Abs. 2 ArbnErfG), Anmeldepflicht "
          "(§ 13 Abs. 1 ArbnErfG), Geheimhaltung (§ 24 Abs. 1 ArbnErfG, § 24 Abs. 2 ArbnErfG)\n\n"
          "**Ersatz der Meldung:** nur eine gleichwertige Dokumentation durch den Arbeitgeber, vor allem seine Patentanmeldung mit Benennung "
          "aller Erfinder (BGH Haftetikett, Initialidee, Lichtschutzfolie). Nicht: die eigene Anmeldung des Arbeitnehmers (BGH Initialidee; "
          "Arb.Erf. 58/16), bloßer Besitz vollständiger Unterlagen (Arb.Erf. 29/12), Versuchsberichte zu einer Initialidee (BGH Initialidee).\n\n"
          "**Freie Erfindung:** unverzüglich in Textform mitteilen (§ 18 Abs. 1 ArbnErfG), außer offensichtlich im Arbeitsbereich nicht "
          "verwendbar (§ 18 Abs. 3 ArbnErfG); Bestreiten binnen drei Monaten (§ 18 Abs. 2 ArbnErfG); vor anderweitiger Verwertung ein "
          "nichtausschließliches Benutzungsrecht anbieten, wenn die Erfindung in den vorhandenen oder vorbereiteten Arbeitsbereich fällt "
          "(§ 19 Abs. 1 ArbnErfG), Annahme binnen drei Monaten (§ 19 Abs. 2 ArbnErfG).\n\n"
          "**Klausurfallen:** Budgetantrag mit Anlagen ist keine Meldung, spätere Bezeichnung wirkt nicht zurück (RP2 I/2019); unverständliche "
          "Meldung nicht beanstandet → gilt als ordnungsgemäß (RP2 III/2020 E2, RP2 II/2021); E-Mail ohne Hinweis auf eine Erfindung "
          "(RP2 I/2021); „Methodik“ in einem Versuchsbericht (RP2 III/2019); Personalsachbearbeiterin als Diensterfinderin (RP2 III/2023); "
          "Leiharbeiter und Geschäftsführer als Miterfinder (RP2 II/2019, RP2 III/2022); Hochschullehrer (§ 42 Nr. 1 ArbnErfG; RP2 II/2022).",
          concepts=["arb_diensterfindung", "arb_erfindungsmeldung", "arb_freie_erfindung"],
          norms=["§ 4 ArbnErfG", "§ 5 ArbnErfG", "§ 18 ArbnErfG", "§ 19 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07a-1", "Definitionen",
          "**Erfindung:** nur, was patent- oder gebrauchsmusterfähig ist (Legaldefinition § 2 ArbnErfG).\n"
          "**Technischer Verbesserungsvorschlag:** Vorschlag für eine sonstige technische Neuerung, die nicht patent- oder "
          "gebrauchsmusterfähig ist (§ 3 ArbnErfG); qualifiziert, wenn er dem Arbeitgeber eine ähnliche Vorzugsstellung wie ein Schutzrecht "
          "gewährt (§ 20 Abs. 1 S. 1 ArbnErfG).\n"
          "**Diensterfindung:** während der Dauer des Arbeitsverhältnisses gemachte Erfindung, die aus der dem Arbeitnehmer im Betrieb "
          "obliegenden Tätigkeit entstanden ist (Nr. 1, Auftragserfindung) oder maßgeblich auf Erfahrungen oder Arbeiten des Betriebs beruht "
          "(Nr. 2, Erfahrungserfindung) (§ 4 Abs. 2 ArbnErfG).\n"
          "**Freie Erfindung:** jede sonstige Erfindung eines Arbeitnehmers (§ 4 Abs. 3 S. 1 ArbnErfG) und die frei gewordene Diensterfindung "
          "(§ 8 ArbnErfG).\n"
          "**Gemacht (fertig):** sobald die Lehre für den Fachmann ausführbar ist (Lösung RP2 I/2019: Prototyp funktioniert).\n"
          "**Unverzüglich:** ohne schuldhaftes Zögern (§ 121 Abs. 1 S. 1 BGB).\n"
          "**Gesondert:** die Meldung muss sich in der Fülle des betrieblichen Schriftverkehrs als Erfindungsmeldung abheben (BGH "
          "Fesoterodinhydrogenfumarat, X ZR 148/17, zu § 5 ArbnErfG a.F.).\n"
          "**Textform:** lesbare Erklärung, in der die Person des Erklärenden genannt ist, auf einem dauerhaften Datenträger (§ 126b S. 1 BGB).\n"
          "**Ordnungsgemäße Meldung:** erfüllt § 5 Abs. 1 ArbnErfG und beschreibt Aufgabe, Lösung und Zustandekommen (§ 5 Abs. 2 S. 1 ArbnErfG); "
          "eine inhaltlich mangelhafte Meldung gilt als ordnungsgemäß, wenn sie nicht binnen zwei Monaten beanstandet wird (§ 5 Abs. 3 S. 1 ArbnErfG).\n"
          "**Miterfinder:** wer einen eigenen, bestimmbaren schöpferischen Beitrag zu der beanspruchten Lehre geleistet hat; der Beitrag muss "
          "nicht für sich patentfähig, aber wesentlich für die Lösung sein (Schiedsstelle Arb.Erf. 46/20).\n"
          "**Arbeitsbereich (§ 19 Abs. 1 ArbnErfG):** vorhandener oder vorbereiteter Tätigkeitsbereich des Betriebs im Zeitpunkt des Angebots.",
          concepts=["arb_diensterfindung", "arb_freie_erfindung", "arb_tvv", "arb_erfindungsmeldung", "arb_miterfinder"],
          norms=["§ 2 ArbnErfG", "§ 3 ArbnErfG", "§ 4 ArbnErfG", "§ 5 ArbnErfG"], abschnitt="Definitionen"),
    mc("p07a-2", "Erfahrungserfindung",
       "Wann ist eine Erfindung eine Diensterfindung nach § 4 Abs. 2 Nr. 2 ArbnErfG?",
       ["Wenn sie während des Arbeitsverhältnisses gemacht wurde und maßgeblich auf Erfahrungen oder Arbeiten des Betriebs beruht",
        "Wenn sie in der Arbeitszeit gemacht wurde",
        "Wenn sie in den Arbeitsbereich des Betriebs fällt",
        "Wenn der Arbeitgeber die Aufgabe gestellt hat"], 0,
       ["**Maßgeblich auf Erfahrungen oder Arbeiten des Betriebs.** Arbeitszeit ist kein Merkmal. Die Aufgabenstellung gehört zur "
        "Auftragserfindung (Nr. 1, obliegende Tätigkeit) und zum Anteilsfaktor (RL Nr. 31). Der Arbeitsbereich entscheidet bei freien "
        "Erfindungen über die Anbietungspflicht (§ 19 Abs. 1 ArbnErfG)."],
       merke="Nr. 1 Auftragserfindung (obliegende Tätigkeit) · Nr. 2 Erfahrungserfindung (Betriebswissen) · Rest frei (§ 4 Abs. 3 ArbnErfG).",
       level=1, concepts=["arb_diensterfindung"], norms=["§ 4 Abs. 2 ArbnErfG"], abschnitt=D),
    fall("p07a-3", "Die Personalsachbearbeiterin",
         "B arbeitet im Personalwesen eines Folienherstellers. Für eine Idee ihres Sohnes recherchiert sie in den internen Datenbanken, "
         "spricht mit Entwicklern und erkennt so, dass sich eine Firmenfolie durch günstiges Prägen strukturieren lässt (nach RP2 III/2023).",
         "Kann B eine Diensterfindung gemacht haben, obwohl Technik nicht zu ihren Aufgaben gehört?", True,
         ["**Ja!** Fehlt die Auftragserfindung (§ 4 Abs. 2 Nr. 1 ArbnErfG), bleibt die Erfahrungserfindung: Sie verlangt nur, dass die "
          "Erfindung maßgeblich auf Erfahrungen oder Arbeiten des Betriebs beruht (§ 4 Abs. 2 Nr. 2 ArbnErfG). Die Stellung der B ist dafür "
          "gleichgültig. Ihr Wissen aus internen Datenbanken und Gesprächen mit der Entwicklung spricht hier dafür; dann muss sie melden."],
         merke="Erfahrungserfindung: Betriebswissen maßgeblich – Aufgabenbereich gleichgültig.", level=2,
         concepts=["arb_diensterfindung"], norms=["§ 4 Abs. 2 ArbnErfG", "§ 5 ArbnErfG"], abschnitt=D),
    mc("p07a-4", "Mindesterfordernisse der Meldung",
       "Welche Mängel hindern den Lauf der Viermonatsfrist auch ohne Beanstandung?",
       ["Fehlen der Textform, der gesonderten Meldung oder der Kenntlichmachung (§ 5 Abs. 1 ArbnErfG)",
        "Fehlende Beschreibung der Lösung (§ 5 Abs. 2 S. 1 ArbnErfG)",
        "Fehlende Angaben zum eigenen Anteil (§ 5 Abs. 2 S. 3 ArbnErfG)",
        "Fehlende Zeichnungen (§ 5 Abs. 2 S. 2 ArbnErfG)"], 0,
       ["**§ 5 Abs. 1 ArbnErfG.** Nur eine Meldung, die die Mindesterfordernisse des Abs. 1 erfüllt, setzt die Frist in Gang. Inhaltliche "
        "Mängel nach § 5 Abs. 2 ArbnErfG, selbst eine unverständliche Lehre, gelten als geheilt, wenn der Arbeitgeber nicht binnen zwei "
        "Monaten beanstandet (§ 5 Abs. 3 S. 1 ArbnErfG; Schiedsstelle Arb.Erf. 34/06)."],
       merke="Abs. 1 (Form) ist zwingend; Abs. 2 (Inhalt) heilt durch Schweigen nach zwei Monaten (§ 5 Abs. 3 ArbnErfG).", level=2,
       concepts=["arb_erfindungsmeldung"], norms=["§ 5 Abs. 1 ArbnErfG", "§ 5 Abs. 3 ArbnErfG"], abschnitt=D),
    fall("p07a-5", "Die abgeheftete E-Mail",
         "Fertigungsplaner W schickt dem Komplementär eine E-Mail zur Fertigungsplanung, in der er nebenbei eine neue Visierung für "
         "Flinten beschreibt. Ein Hinweis, dass er eine Erfindung melden wolle, fehlt; der Komplementär heftet sie ab (nach RP2 I/2021).",
         "Ist die E-Mail eine Erfindungsmeldung?", False,
         ["**Nein!** Textform liegt vor (§ 126b BGB), aber die Meldung muss gesondert sein und kenntlich machen, dass eine Erfindung gemeldet "
          "wird (§ 5 Abs. 1 S. 1 ArbnErfG). Eine Beschreibung im Rahmen anderer Mitteilungen genügt nicht (Schiedsstelle Arb.Erf. 01/02). "
          "Folge: Die Viermonatsfrist läuft nicht; der Arbeitgeber kann aber jederzeit durch Erklärung in Anspruch nehmen (§ 6 Abs. 1 ArbnErfG)."],
         merke="Keine kenntliche Meldung → keine Fiktion, aber Inanspruchnahme durch Erklärung jederzeit möglich.", level=2,
         concepts=["arb_erfindungsmeldung"], norms=["§ 5 Abs. 1 ArbnErfG", "§ 6 Abs. 1 ArbnErfG"], abschnitt=D),
    mc("p07a-6", "Unverständliche Meldung",
       "Was muss der Arbeitgeber tun, damit die Meldung E2 nicht als ordnungsgemäß gilt?",
       ["Binnen zwei Monaten nach Eingang erklären, dass und in welcher Hinsicht die Meldung ergänzt werden muss (§ 5 Abs. 3 S. 1 ArbnErfG)",
        "Binnen vier Monaten die Erfindung freigeben (§ 6 Abs. 2 ArbnErfG)",
        "Den Eingang nicht bestätigen (§ 5 Abs. 1 S. 3 ArbnErfG)",
        "Binnen drei Monaten bestreiten, dass eine Diensterfindung vorliegt (§ 18 Abs. 2 ArbnErfG)"], 0,
       ["**§ 5 Abs. 3 S. 1 ArbnErfG.** Die Beanstandung muss binnen zwei Monaten zugehen und konkret sagen, was fehlt; der Arbeitgeber muss "
        "bei der Ergänzung helfen (§ 5 Abs. 3 S. 2 ArbnErfG). Erst die ergänzte Meldung setzt dann die Viermonatsfrist in Gang. Frist: "
        "§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB, § 193 BGB."],
       sachverhalt="Am 16.09.2020 geht eine Meldung E2 ein, aus der weder der Geschäftsführer noch die Entwicklerin entnehmen können, wie die "
                   "Energiegewinnung funktionieren soll (nach RP2 III/2020).",
       merke="Beanstandung: zwei Monate ab Eingang, konkret (§ 5 Abs. 3 ArbnErfG); hier bis Mo 16.11.2020.", level=2,
       concepts=["arb_erfindungsmeldung"], norms=["§ 5 Abs. 3 ArbnErfG"], abschnitt=D),
    fall("p07a-7", "Die Solarbeschichtung",
         "Entwicklerin Z hat in ihrer Freizeit eine wetterfeste Beschichtung für ihre privaten Solarpaneele erfunden. Ihr Arbeitgeber baut "
         "Kommunikationsmodule für Fabrikhallen und hat keinerlei Erfahrung mit Beschichtungen (nach RP2 III/2020).",
         "Muss Z die Erfindung dem Arbeitgeber nach § 18 Abs. 1 ArbnErfG mitteilen?", False,
         ["**Nein!** Es ist eine freie Erfindung (§ 4 Abs. 3 S. 1 ArbnErfG). Die Mitteilungspflicht entfällt, wenn sie offensichtlich im "
          "Arbeitsbereich des Betriebs nicht verwendbar ist (§ 18 Abs. 3 ArbnErfG). Das ist hier so. Eine strengere Vertragsklausel wirkt "
          "nur, soweit sie den Arbeitnehmer nicht schlechter stellt als das Gesetz (§ 22 S. 1 ArbnErfG)."],
         merke="Freie Erfindung: Mitteilung § 18 Abs. 1 ArbnErfG, außer offensichtlich nicht verwendbar (§ 18 Abs. 3 ArbnErfG).", level=2,
         concepts=["arb_freie_erfindung"], norms=["§ 18 ArbnErfG", "§ 4 Abs. 3 ArbnErfG"], abschnitt=D),
    mc("p07a-8", "Anbietungspflicht",
       "Was muss Z vor einer Verwertung anbieten, und wann erlischt das Vorrecht?",
       ["Mindestens ein nichtausschließliches Benutzungsrecht zu angemessenen Bedingungen; ohne Annahme binnen drei Monaten erlischt es",
        "Die Übertragung der Erfindung; das Vorrecht erlischt nach vier Monaten",
        "Eine ausschließliche Lizenz; das Vorrecht erlischt nach zwei Monaten",
        "Nichts, freie Erfindungen sind frei verfügbar"], 0,
       ["**§ 19 Abs. 1, 2 ArbnErfG.** Fällt die freie Erfindung in den vorhandenen oder vorbereiteten Arbeitsbereich, muss der Arbeitnehmer "
        "vor anderweitiger Verwertung mindestens ein nichtausschließliches Benutzungsrecht anbieten. Nimmt der Arbeitgeber nicht binnen "
        "drei Monaten an, erlischt das Vorrecht. Ein bloß geheim erwogenes Projekt ab 2025 ist kaum „vorbereitet“."],
       sachverhalt="Der Arbeitgeber der Z plant streng geheim, frühestens ab 2025 Produkte für den Außeneinsatz zu entwickeln, und hätte "
                   "gern eine Option auf ihre Beschichtung (nach RP2 III/2020).",
       merke="§ 19 ArbnErfG: Arbeitsbereich im Zeitpunkt des Angebots · einfaches Benutzungsrecht · drei Monate.", level=2,
       concepts=["arb_freie_erfindung"], norms=["§ 19 ArbnErfG"], abschnitt=D),
    fall("p07a-9", "Der Professor und die Anzeige",
         "Professor G hält § 42 Nr. 1 ArbnErfG für verfassungswidrig, weil er seine Diensterfindung zwei Monate vor einer Veröffentlichung "
         "anzeigen muss. Er klagt auf Feststellung, dazu nicht verpflichtet zu sein (nach RP2 II/2022).",
         "Ist § 42 Nr. 1 ArbnErfG verfassungswidrig?", False,
         ["**Nein!** Der BGH hat entschieden, dass § 42 Nr. 1 ArbnErfG von der Gesetzgebungskompetenz des Bundes nach Art. 73 Abs. 1 Nr. 9 GG "
          "gedeckt ist und die Wissenschaftsfreiheit (Art. 5 Abs. 3 GG) nicht verletzt (BGH selbststabilisierendes Kniegelenk, X ZR 167/05). "
          "Wer gar nicht offenbaren will, muss nicht melden (§ 42 Nr. 2 S. 1 ArbnErfG)."],
         merke="Hochschule: Anzeige zwei Monate vor Offenbarung (§ 42 Nr. 1 ArbnErfG) – verfassungsgemäß.", level=2,
         concepts=["arb_hochschulerfindung"], norms=["§ 42 ArbnErfG"], abschnitt=D),
    *fallkette("p07a-10", "Das Budgetschreiben (nach RP2 I/2019)",
        "E1 stellt am 08.06.2015 funktionierende Prototypen zweier Diensterfindungen fertig. Am 07.07.2015 bittet er den Geschäftsführer "
        "unterschrieben um 100.000 € Sonderbudget, „um dieses Projekt zu zumindest einer Erfindung zu bringen“; technische Beschreibungen "
        "liegen an. Am 24.12.2016 übergibt er zwei Dokumente „Erfindungsmeldung“, die auf eine „Erfindungsmeldung vom 07.07.2015“ verweisen.",
        [frage("Ist die Textform des § 5 Abs. 1 S. 1 ArbnErfG gewahrt?", True,
               ["**Ja!** Das Schreiben ist lesbar, nennt E1 als Erklärenden und liegt auf Papier vor (§ 126b BGB); die Unterschrift erfüllt "
                "sogar die Schriftform. Die Form ist hier nicht das Problem."],
               merke="Textform: lesbar · Person genannt · dauerhafter Datenträger (§ 126b BGB).", titel="V7 Textform", level=1),
         frage("Ist das Schreiben vom 07.07.2015 gesondert und als Meldung einer Erfindung kenntlich?", False,
               ["**Nein!** Es ist ein Budgetantrag; die Anlagen sind Beiwerk. Der Text verneint sogar eine fertige Erfindung. Gesondert ist "
                "nur, was sich in der Fülle des Schriftverkehrs als Meldung abhebt (BGH Fesoterodinhydrogenfumarat). Keine Meldung "
                "(§ 5 Abs. 1 S. 1 ArbnErfG)."],
               merke="Budget- oder Projektantrag ist keine Erfindungsmeldung.", titel="V6, V8 Gesondert und kenntlich", level=2),
         frage("Ersetzt der Besitz der vollständigen Anlagen beim Geschäftsführer die Meldung?", False,
               ["**Nein!** Die Meldung ersetzt nur eine Dokumentation des Arbeitgebers nach außen, dass er sie nicht mehr braucht, etwa seine "
                "Patentanmeldung mit Erfinderbenennung (BGH Haftetikett, Initialidee). Bloßer Besitz von Unterlagen genügt nicht "
                "(Schiedsstelle Arb.Erf. 29/12)."],
               merke="Ersatz nur durch Dokumentation des Arbeitgebers (Anmeldung + Benennung), nicht durch Aktenbesitz.",
               titel="Ersatz der Meldung", level=2),
         frage("Macht die Bezugnahme vom 24.12.2016 das Schreiben vom 07.07.2015 rückwirkend zur Meldung?", False,
               ["**Nein!** Ob eine Meldung vorliegt, entscheidet ihr Inhalt bei Zugang. Erst die Dokumente vom 24.12.2016 sind ordnungsgemäße "
                "Meldungen; sie setzen die Viermonatsfrist mit Zugang in Gang (§ 6 Abs. 2 ArbnErfG). Das entscheidet in RP2 I/2019 über den "
                "Vorrang gegenüber der Meldung des Kollegen E2 vom 05.10.2016."],
               merke="Meldung wirkt ab Zugang, nicht zurück.", titel="Spätere Bezeichnung", level=2),
         ],
        abschnitt=K, level=2, concepts=["arb_erfindungsmeldung"], norms=["§ 5 Abs. 1 ArbnErfG"]),
])

# ====================================================================== p07b Inanspruchnahme
P07B = dict(id="p07b", titel="§§ 6, 7 ArbnErfG: Inanspruchnahme", einheiten=[
    intro("p07b-0", "Prüfungsschema",
          "**AGL (Arbeitgeber):** Rechtsübergang nach § 7 Abs. 1 ArbnErfG i.V.m. § 6 Abs. 1 ArbnErfG (Erklärung) oder § 6 Abs. 2 ArbnErfG "
          "(Fiktion) – Grundlage der Vindikation (§ 8 S. 2 PatG), der Anmeldepflicht (§ 13 Abs. 1 ArbnErfG) und der Vergütung "
          "(§ 9 Abs. 1 ArbnErfG)\n\n"
          "**A · Gegenstand**\n"
          "**V1 Diensterfindung eines Arbeitnehmers** – § 4 Abs. 2 ArbnErfG (Schema p07a); bei Miterfindern je Anteil prüfen\n"
          "**V2 Anwendbares Recht** – Meldung vor dem 1.10.2009 → a.F. (§ 43 Abs. 3 S. 1 ArbnErfG)\n\n"
          "**B · Inanspruchnahme**\n"
          "**V3a durch Erklärung** – § 6 Abs. 1 ArbnErfG: einseitige, empfangsbedürftige, formfreie Erklärung gegenüber dem Arbeitnehmer "
          "(Zugang § 130 Abs. 1 S. 1 BGB); möglich ab Fertigstellung, auch ohne Meldung. Ohne ordnungsgemäße Meldung läuft keine Frist: "
          "Die Erklärung wirkt auch Jahre nach einer Patentanmeldung (Schiedsstelle Arb.Erf. 21/09)\n"
          "**V3b oder durch Fiktion** – § 6 Abs. 2 ArbnErfG: (1) ordnungsgemäße Meldung (§ 5 Abs. 2 S. 1, 3 ArbnErfG oder geheilt nach § 5 Abs. 3 "
          "ArbnErfG) oder gleichwertige Dokumentation des Arbeitgebers (BGH Haftetikett, Initialidee, Lichtschutzfolie), (2) Eingang beim "
          "Arbeitgeber, (3) keine Freigabe in Textform binnen vier Monaten. Frist: Beginn § 187 Abs. 1 BGB, Ende § 188 Abs. 2 BGB, "
          "Verschiebung § 193 BGB (Freigabe ist fristgebundene Willenserklärung)\n"
          "**V4 Keine vorherige Freigabe** – § 8 S. 1 ArbnErfG (Textform); Schweigen ist keine Freigabe\n"
          "**V5 Keine Sperre nach § 18 Abs. 2 ArbnErfG** – hat der Arbeitgeber eine als frei mitgeteilte Erfindung nicht binnen drei Monaten "
          "bestritten, kann er sie nicht mehr in Anspruch nehmen\n\n"
          "**⇒ Rechtsfolge:** alle vermögenswerten Rechte gehen über (§ 7 Abs. 1 ArbnErfG), auch das Recht auf das Patent (§ 6 S. 1 PatG: "
          "Rechtsnachfolger); frühere Verfügungen des Arbeitnehmers sind dem Arbeitgeber gegenüber unwirksam, soweit sie seine Rechte "
          "beeinträchtigen (§ 7 Abs. 2 ArbnErfG); Vergütungsanspruch entsteht dem Grunde nach (§ 9 Abs. 1 ArbnErfG); das Recht auf Nennung "
          "bleibt beim Erfinder (§ 63 PatG).\n\n"
          "**Altfall (a.F.):** nur schriftliche Erklärung binnen vier Monaten nach Eingang der ordnungsgemäßen Meldung (§ 6 Abs. 2 S. 2 "
          "ArbnErfG a.F.), unbeschränkt oder beschränkt (RL Nr. 25); sonst wird die Erfindung frei (§ 8 Abs. 1 Nr. 3 ArbnErfG a.F.; "
          "Schiedsstelle Arb.Erf. 15/03). Auch dort setzt die Anmeldung des Arbeitgebers mit Benennung aller Erfinder die Frist in Gang "
          "(BGH Lichtschutzfolie).\n\n"
          "**Miterfinder verschiedener Arbeitgeber:** Jeder Arbeitgeber erhält mit dem Anteil seines Arbeitnehmers eine Nutzungsbefugnis an der "
          "ganzen Erfindung; der eigene Arbeitnehmer wird für die Vergütung wie ein Alleinerfinder behandelt (Schiedsstelle Arb.Erf. 14/06).\n\n"
          "**In den Klausuren:** RP2 I/2019 (Fiktion Mo 06.02.2017 und Mo 24.04.2017; schriftliche Inanspruchnahme am 29.01.2019 nach "
          "Eigenanmeldung), RP2 II/2021 (Altfall: Beanstandung und Inanspruchnahme zu spät), RP2 I/2022 (E1: rechtzeitige Beanstandung, dann "
          "Schweigen), RP2 III/2023 (P2 nie gemeldet), RP2 I/2023 (schriftliche Inanspruchnahme Sa 27.12.2008), RP2 III/2019 (BETA).",
          concepts=["arb_inanspruchnahme", "arb_freigabe", "arb_altrecht"],
          norms=["§ 6 ArbnErfG", "§ 7 ArbnErfG", "§ 8 ArbnErfG", "§ 43 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07b-1", "Definitionen",
          "**Inanspruchnahme:** einseitige, empfangsbedürftige Erklärung des Arbeitgebers gegenüber dem Arbeitnehmer, die Diensterfindung "
          "an sich zu ziehen (§ 6 Abs. 1 ArbnErfG); seit 1.10.2009 formfrei und fingiert, wenn nicht binnen vier Monaten freigegeben wird "
          "(§ 6 Abs. 2 ArbnErfG).\n"
          "**Vermögenswerte Rechte (§ 7 Abs. 1 ArbnErfG):** das Recht auf das Patent (§ 6 S. 1 PatG), der Anspruch auf Erteilung und die "
          "Rechte aus Anmeldung und Schutzrecht; nicht das Erfinderpersönlichkeitsrecht.\n"
          "**Verfügung (§ 7 Abs. 2 ArbnErfG):** Rechtsgeschäft, das ein Recht an der Erfindung überträgt, belastet oder aufgibt, etwa "
          "Lizenz oder Übertragung an Dritte; die Unwirksamkeit ist relativ (nur gegenüber dem Arbeitgeber).\n"
          "**Freigabe:** einseitige, empfangsbedürftige Erklärung in Textform, die Diensterfindung nicht an sich zu ziehen (§ 8 S. 1 ArbnErfG).\n"
          "**Gleichwertige Dokumentation:** der Arbeitgeber dokumentiert nach außen, dass er die Kenntnis hat, die die Meldung verschaffen "
          "soll, insbesondere durch eigene Patentanmeldung und Benennung des Arbeitnehmers als Erfinder (BGH Initialidee, X ZR 72/10).\n"
          "**Unbeschränkte / beschränkte Inanspruchnahme (a.F.):** Übergang aller Rechte bzw. nur ein nichtausschließliches "
          "Benutzungsrecht (RL Nr. 1, RL Nr. 25).",
          concepts=["arb_inanspruchnahme", "arb_freigabe"], norms=["§ 6 ArbnErfG", "§ 7 ArbnErfG", "§ 8 ArbnErfG"], abschnitt="Definitionen"),
    mc("p07b-2", "Form der Erklärung",
       "Welche Form verlangt die Inanspruchnahme durch Erklärung nach § 6 Abs. 1 ArbnErfG?",
       ["Keine; sie muss dem Arbeitnehmer aber zugehen",
        "Textform (§ 126b BGB)",
        "Schriftform (§ 126 Abs. 1 BGB)",
        "Notarielle Beurkundung"], 0,
       ["**Keine Form.** § 6 Abs. 1 ArbnErfG verlangt nur eine Erklärung gegenüber dem Arbeitnehmer; sie wird mit Zugang wirksam "
        "(§ 130 Abs. 1 S. 1 BGB). Textform verlangt das Gesetz nur für die Freigabe (§ 6 Abs. 2 ArbnErfG, § 8 S. 1 ArbnErfG). Im Altfall war "
        "die Schriftform nötig (§ 6 Abs. 2 S. 2 ArbnErfG a.F.)."],
       merke="Inanspruchnahme formfrei · Freigabe Textform · a.F. schriftlich.", level=1,
       concepts=["arb_inanspruchnahme"], norms=["§ 6 Abs. 1 ArbnErfG", "§ 8 ArbnErfG"], abschnitt=D),
    fall("p07b-3", "Eigene Anmeldung statt Meldung",
         "Ingenieur I meldet seine Diensterfindung nicht, sondern lässt sie auf eigenen Namen zum Patent anmelden. Der Arbeitgeber erfährt "
         "von der Offenlegung, unternimmt aber zwei Jahre nichts.",
         "Gilt die Erfindung nach § 6 Abs. 2 ArbnErfG als in Anspruch genommen?", False,
         ["**Nein!** Die Fiktion setzt eine ordnungsgemäße Meldung oder eine gleichwertige Dokumentation durch den Arbeitgeber voraus. Die "
          "eigene Anmeldung des Arbeitnehmers ist keine solche Dokumentation (BGH Initialidee; Schiedsstelle Arb.Erf. 58/16). Der "
          "Arbeitgeber kann aber weiterhin durch Erklärung in Anspruch nehmen (§ 6 Abs. 1 ArbnErfG)."],
         merke="Eigenanmeldung des Arbeitnehmers ersetzt die Meldung nicht – keine Fiktion, keine Frist.", level=2,
         concepts=["arb_inanspruchnahme", "arb_erfindungsmeldung"], norms=["§ 6 ArbnErfG"], abschnitt=D),
    mc("p07b-4", "Fristende",
       "Wann tritt die Fiktion ein?",
       ["Mit Ablauf des Mo 06.02.2017", "Mit Ablauf des So 05.02.2017", "Mit Ablauf des Do 05.01.2017", "Mit Ablauf des Mi 05.04.2017"], 0,
       ["**Mo 06.02.2017.** Vier Monate ab Eingang (§ 6 Abs. 2 ArbnErfG): Beginn am 06.10.2016 (§ 187 Abs. 1 BGB), Ende am Tag gleicher "
        "Zahl, So 05.02.2017 (§ 188 Abs. 2 BGB). Weil bis dahin eine Freigabe in Textform erklärt werden kann, verschiebt § 193 BGB das "
        "Ende auf den nächsten Werktag."],
       sachverhalt="Erfinder E2 übergibt dem Geschäftsführer am Mi 05.10.2016 eine ordnungsgemäße Meldung „Monitorverstellung“ (nach "
                   "RP2 I/2019).",
       merke="Vier Monate § 6 Abs. 2 ArbnErfG · § 187 Abs. 1 BGB · § 188 Abs. 2 BGB · § 193 BGB.", level=2,
       concepts=["arb_inanspruchnahme"], norms=["§ 6 Abs. 2 ArbnErfG"], abschnitt=D),
    fall("p07b-5", "Lizenz vor der Inanspruchnahme",
         "Chemiker C räumt einem Wettbewerber eine Lizenz an seiner gemeldeten Diensterfindung ein. Drei Monate später erklärt der "
         "Arbeitgeber die Inanspruchnahme.",
         "Kann der Wettbewerber dem Arbeitgeber die Lizenz entgegenhalten?", False,
         ["**Nein!** Verfügungen des Arbeitnehmers vor der Inanspruchnahme sind dem Arbeitgeber gegenüber unwirksam, soweit sie seine "
          "Rechte beeinträchtigen (§ 7 Abs. 2 ArbnErfG). Mit der Inanspruchnahme erwirbt der Arbeitgeber die Erfindung unbelastet "
          "(§ 7 Abs. 1 ArbnErfG). C hat zudem gegen seine Geheimhaltungspflicht verstoßen (§ 24 Abs. 2 ArbnErfG)."],
         merke="Verfügungen vor Inanspruchnahme: relativ unwirksam (§ 7 Abs. 2 ArbnErfG).", level=1,
         concepts=["arb_inanspruchnahme"], norms=["§ 7 Abs. 2 ArbnErfG", "§ 24 ArbnErfG"], abschnitt=D),
    fall("p07b-6", "Schweigen im Altfall",
         "M meldet am 27.08.2007 schriftlich eine Diensterfindung. Der Arbeitgeber beanstandet am Mo 29.10.2007, die Lösung fehle; M liefert "
         "sie am 25.02.2008 nach. Danach hört M nichts mehr (nach RP2 I/2022).",
         "Ist die Erfindung in Anspruch genommen?", False,
         ["**Nein!** Altfall (§ 43 Abs. 3 S. 1 ArbnErfG). Die Beanstandung war rechtzeitig: Fristende Sa 27.10.2007, verschoben auf Mo "
          "29.10.2007 (§ 5 Abs. 3 S. 1 ArbnErfG, § 193 BGB). Die ergänzte Meldung setzte die Viermonatsfrist in Gang (§ 6 Abs. 2 S. 2 "
          "ArbnErfG a.F.); ohne schriftliche Inanspruchnahme bis 25.06.2008 wurde die Erfindung frei (§ 8 Abs. 1 Nr. 3 ArbnErfG a.F.)."],
         merke="Altfall: Schweigen nach Meldung → frei; kein Vergütungsanspruch aus § 9 ArbnErfG.", level=3,
         concepts=["arb_altrecht", "arb_inanspruchnahme"], norms=["§ 43 ArbnErfG", "§ 5 Abs. 3 ArbnErfG"], abschnitt=D),
    mc("p07b-7", "Miterfinder zweier Arbeitgeber",
       "Was erwirbt die A GmbH, wenn sie nur den Anteil ihres Arbeitnehmers in Anspruch nimmt?",
       ["Eine Nutzungsbefugnis an der ganzen Erfindung; ihr Arbeitnehmer wird für die Vergütung wie ein Alleinerfinder behandelt",
        "Nur einen Bruchteil der Erfindung, den sie nicht nutzen darf",
        "Nichts, solange der andere Arbeitgeber nicht zustimmt",
        "Die ganze Erfindung zur alleinigen Verwertung"], 0,
       ["**Nutzungsbefugnis am Ganzen.** Jeder Miterfinder vermittelt seinem Arbeitgeber mit der Inanspruchnahme seines Anteils die "
        "Nutzungsbefugnis an der gesamten Erfindung. Bemessungsgrundlage der Vergütung ist der Nutzen dieses Arbeitgebers; die Anteile "
        "der fremden Arbeitnehmer bleiben außer Betracht (Schiedsstelle Arb.Erf. 14/06)."],
       sachverhalt="Bei einer Kooperation erfinden Entwickler der A GmbH und der B GmbH gemeinsam (je 50 %). Beide Arbeitgeber nehmen "
                   "den Anteil ihres Arbeitnehmers in Anspruch (nach RP2 III/2020).",
       merke="Kooperation: eigener Arbeitnehmer = Alleinerfinder im Verhältnis zum eigenen Arbeitgeber (Arb.Erf. 14/06).", level=3,
       concepts=["arb_miterfinder", "arb_inanspruchnahme"], norms=["§ 7 Abs. 1 ArbnErfG", "§ 9 ArbnErfG"], abschnitt=D),
    *fallkette("p07b-8", "Tastaturbeleuchtung (nach RP2 I/2019)",
        "Die Diensterfindung „Tastaturbeleuchtung“ des E1 lag dem Geschäftsführer 2015 nur als Anlage zu einem Budgetantrag vor, eine "
        "Meldung gab es nie. Am 08.07.2017 meldet E1 sie auf eigenen Namen zum Patent an; Erteilung am 25.01.2019. Am 29.01.2019 erklärt "
        "der Geschäftsführer schriftlich gegenüber E1 die Inanspruchnahme für die A GmbH.",
        [frage("Ist die Inanspruchnahme vor dem 29.01.2019 fingiert worden?", False,
               ["**Nein!** Ohne ordnungsgemäße Meldung beginnt die Viermonatsfrist nicht (§ 6 Abs. 2 ArbnErfG). Eine gleichwertige "
                "Dokumentation des Arbeitgebers fehlt; die Anmeldung des E1 genügt nicht (BGH Initialidee; Schiedsstelle Arb.Erf. 58/16)."],
               merke="Fiktion nur nach ordnungsgemäßer Meldung oder Dokumentation durch den Arbeitgeber.", titel="V3b Fiktion", level=2),
         frage("Konnte die A GmbH am 29.01.2019 noch wirksam in Anspruch nehmen?", True,
               ["**Ja!** § 6 Abs. 1 ArbnErfG kennt keine Frist, solange keine ordnungsgemäße Meldung vorliegt; die Erklärung wirkt auch Jahre "
                "nach einer Patentanmeldung (Schiedsstelle Arb.Erf. 21/09). Die schriftliche Erklärung des Geschäftsführers ist der A GmbH "
                "zuzurechnen (§ 35 Abs. 1 S. 1 GmbHG) und ging E1 zu (§ 130 Abs. 1 S. 1 BGB)."],
               merke="Keine Meldung → keine Frist → Inanspruchnahme jederzeit (§ 6 Abs. 1 ArbnErfG).", titel="V3a Erklärung", level=2),
         frage("Bleibt die Anmeldung des E1 der A GmbH gegenüber wirksam?", False,
               ["**Nein!** Die Anmeldung ist eine Verfügung vor der Inanspruchnahme; sie ist der A GmbH gegenüber unwirksam, soweit sie deren "
                "Rechte beeinträchtigt (§ 7 Abs. 2 ArbnErfG). Die A GmbH ist Berechtigte (§ 7 Abs. 1 ArbnErfG, § 6 S. 1 PatG) und kann "
                "Übertragung des Patents verlangen (§ 8 S. 2 PatG; Kapitel p07g)."],
               merke="Inanspruchnahme + § 7 Abs. 2 ArbnErfG → Vindikation nach § 8 S. 2 PatG.", titel="Rechtsfolge § 7 ArbnErfG", level=2),
         frage("Kann die A GmbH auch dann noch in Anspruch nehmen?", False,
               ["**Nein!** Die Freigabe in Textform macht die Diensterfindung frei (§ 8 S. 1 ArbnErfG); E1 darf über sie ohne die "
                "Beschränkungen der § 18 ArbnErfG und § 19 ArbnErfG verfügen (§ 8 S. 2 ArbnErfG). Eine spätere Inanspruchnahme geht ins Leere."],
               merke="Freigabe ist endgültig: danach keine Inanspruchnahme mehr.", titel="V4 Freigabe",
               abwandlung="Der Geschäftsführer hatte E1 am 01.08.2017 per E-Mail mitgeteilt, die Tastaturbeleuchtung interessiere die A GmbH "
                          "nicht, E1 könne damit machen, was er wolle.", level=2),
         ],
        abschnitt=K, level=2, concepts=["arb_inanspruchnahme"], norms=["§ 6 ArbnErfG", "§ 7 ArbnErfG"]),
    *fallkette("p07b-9", "Die Spulenanordnung (nach RP2 II/2021)",
        "F übergibt am 16.07.2009 eine unterschriebene Erfindungsmeldung, die am Sa 18.07.2009 eingeht. Am 04.10.2009 schreibt der "
        "Geschäftsführer, man verstehe die Funktion nicht; F ergänzt am 10.10.2009 einen Satz. Am 24.11.2009 erklärt der Arbeitgeber "
        "schriftlich die unbeschränkte Inanspruchnahme. Das Patent wurde 2010 erteilt; F verlangt es 2021 heraus.",
        [frage("Welches Recht gilt?", 0,
               ["**ArbnErfG a.F.** Die Meldung ging vor dem 1.10.2009 ein (§ 43 Abs. 3 S. 1 ArbnErfG); die Ergänzung im Oktober betrifft "
                "dieselbe Erfindung und ändert das nicht. Also schriftliche Inanspruchnahme binnen vier Monaten, keine Fiktion."],
               optionen=["ArbnErfG in der bis 30.09.2009 geltenden Fassung", "ArbnErfG in der heutigen Fassung",
                         "a.F. für die Meldung, n.F. für die Inanspruchnahme", "Patentgesetz allein"],
               merke="Meldedatum vor 1.10.2009 → a.F. für das ganze Verfahren.", titel="V2 Anwendbares Recht", level=1),
         frage("War die Beanstandung vom 04.10.2009 rechtzeitig?", False,
               ["**Nein!** Zwei Monate ab Eingang (§ 5 Abs. 3 S. 1 ArbnErfG): Ende Fr 18.09.2009 (§ 187 Abs. 1 BGB, § 188 Abs. 2 BGB). Die "
                "Meldung gilt als ordnungsgemäß; die Viermonatsfrist lief ab dem 18.07.2009."],
               merke="Verspätete Beanstandung: Meldung gilt als ordnungsgemäß.", titel="V3b Ordnungsgemäße Meldung", level=2),
         frage("War die Inanspruchnahme vom 24.11.2009 rechtzeitig?", False,
               ["**Nein!** Die Frist endete am Mi 18.11.2009 (§ 6 Abs. 2 S. 2 ArbnErfG a.F., § 188 Abs. 2 BGB). Die Erfindung wurde frei "
                "(§ 8 Abs. 1 Nr. 3 ArbnErfG a.F.); das Recht auf das Patent blieb bei F (§ 6 S. 1 PatG)."],
               merke="a.F.: verspätete Inanspruchnahme → Erfindung frei.", titel="Inanspruchnahme a.F.", level=2),
         frage("Kann F das Patent 2021 noch nach § 8 S. 2 PatG herausverlangen?", False,
               ["**Nein!** Die Klage muss binnen zwei Jahren nach Veröffentlichung der Erteilung erhoben werden (§ 8 S. 3 PatG); die Frist "
                "lief 2012 ab. Nur wenn der Arbeitgeber beim Erwerb nicht in gutem Glauben war, gilt sie nicht (§ 8 S. 5 PatG) – das müsste F "
                "beweisen."],
               merke="Frei gewordene Erfindung: Vindikation nur binnen zwei Jahren (§ 8 S. 3 PatG), außer Bösgläubigkeit (§ 8 S. 5 PatG).",
               titel="Folge: Vindikation", level=3),
         ],
        abschnitt=K, level=2, concepts=["arb_altrecht", "arb_inanspruchnahme"], norms=["§ 43 ArbnErfG", "§ 8 PatG"]),
])

# ====================================================================== p07c Freigabe, Anmeldung, Aufgabe
P07C = dict(id="p07c", titel="§§ 8, 13, 14, 16, 17 ArbnErfG: Freigabe, Schutzrechtsanmeldung und Aufgabe", einheiten=[
    intro("p07c-0", "Prüfungsschema",
          "**AGL 1 (Arbeitnehmer): Ersatzvornahme der Anmeldung**, § 13 Abs. 3 ArbnErfG; daneben Schadensersatz § 823 Abs. 2 BGB i.V.m. "
          "§ 13 Abs. 1 ArbnErfG (Schiedsstelle Arb.Erf. 27/20)\n"
          "**V1 Gemeldete Diensterfindung** – § 13 Abs. 1 S. 1 ArbnErfG (Schema p07a)\n"
          "**V2 Inanspruchnahme** – § 13 Abs. 3 ArbnErfG, § 6 ArbnErfG (Schema p07b)\n"
          "**V3 Anmeldepflicht nicht entfallen** – § 13 Abs. 2 ArbnErfG: Nr. 1 frei geworden (§ 8 ArbnErfG), Nr. 2 Zustimmung des Arbeitnehmers "
          "zur Nichtanmeldung, Nr. 3 Betriebsgeheimnis (§ 17 ArbnErfG)\n"
          "**V4 Pflicht verletzt** – unverzüglich (§ 13 Abs. 1 S. 3 ArbnErfG), im Inland, zum Patent, außer der Gebrauchsmusterschutz erscheint "
          "bei verständiger Würdigung der Verwertbarkeit zweckdienlicher (§ 13 Abs. 1 S. 2 ArbnErfG); bloße Zweifel an der Patentfähigkeit "
          "genügen nicht (Arb.Erf. 27/20). Erfüllt durch prioritätsbegründendes Gebrauchsmuster mit PCT-Nachanmeldung, die DE erfasst "
          "(Arb.Erf. 31/10)\n"
          "**V5 Angemessene Nachfrist gesetzt und fruchtlos** – § 13 Abs. 3 ArbnErfG\n"
          "**⇒** Arbeitnehmer meldet für den Arbeitgeber auf dessen Namen und Kosten an.\n\n"
          "**AGL 2 (Arbeitnehmer): Freigabe für das Ausland**, § 14 Abs. 2 ArbnErfG\n"
          "**V1 Inanspruchnahme** (§ 14 Abs. 1 ArbnErfG) **V2 Staat, in dem der Arbeitgeber keine Schutzrechte erwerben will** **V3 rechtzeitig**, "
          "damit der Arbeitnehmer die Prioritätsfristen nutzen kann (§ 14 Abs. 2 S. 2 ArbnErfG)\n"
          "**⇒** Freigabe und Ermöglichung des Erwerbs; Vorbehalt eines nichtausschließlichen Benutzungsrechts gegen angemessene Vergütung "
          "(§ 14 Abs. 3 ArbnErfG).\n\n"
          "**AGL 3 (Arbeitnehmer): Übertragung bei Aufgabe**, § 16 Abs. 1 ArbnErfG\n"
          "**V1 Anmeldung oder Schutzrecht auf die Diensterfindung** **V2 vor Erfüllung des Vergütungsanspruchs** (nicht nach vollständig "
          "gezahlter Pauschale) **V3 Absicht, nicht weiterzuverfolgen oder nicht aufrechtzuerhalten** **V4 Mitteilung an den Arbeitnehmer** "
          "**V5 Verlangen binnen drei Monaten nach Zugang** (§ 16 Abs. 2 ArbnErfG; danach keine Pflicht mehr, auch wenn der Arbeitgeber doch "
          "nicht aufgibt: BGH Zündlanze)\n"
          "**⇒** Übertragung auf Kosten des Arbeitnehmers mit den nötigen Unterlagen; Vorbehalt eines Benutzungsrechts gegen angemessene "
          "Vergütung (§ 16 Abs. 3 ArbnErfG). Ohne Verlangen darf der Arbeitgeber aufgeben (§ 16 Abs. 2 ArbnErfG).\n\n"
          "**AGL 4 (Arbeitgeber): Absehen von der Anmeldung als Betriebsgeheimnis**, § 17 ArbnErfG\n"
          "**V1 Berechtigte Belange des Betriebs** verlangen Geheimhaltung (kein freies Wahlrecht, Arb.Erf. 23/11 vom 17.01.2013) "
          "**V2 Anerkennung der Schutzfähigkeit** gegenüber dem Arbeitnehmer (§ 17 Abs. 1 ArbnErfG) **oder** Anrufung der Schiedsstelle "
          "(§ 17 Abs. 2 ArbnErfG)\n"
          "**⇒** keine Anmeldepflicht (§ 13 Abs. 2 Nr. 3 ArbnErfG); Vergütung wie für ein Schutzrecht plus Ausgleich der Nachteile "
          "(§ 17 Abs. 3 ArbnErfG, RL Nr. 27). Möglich auch nach der Anmeldung, solange sie nicht offengelegt ist (Arb.Erf. 02/23).\n\n"
          "**Freigabe** (§ 8 S. 1 ArbnErfG): Textform; Wirkung: freie Verfügung (§ 8 S. 2 ArbnErfG), allein der Arbeitnehmer darf anmelden, "
          "Rechte aus einer schon eingereichten Anmeldung gehen über (§ 13 Abs. 4 ArbnErfG). **Unterrichtung** (§ 15 Abs. 1 ArbnErfG): "
          "Abschriften, Fortgang, Einsicht; Mitwirkung des Arbeitnehmers (§ 15 Abs. 2 ArbnErfG). **Abweichende Regeln** (Verzicht auf "
          "§ 14 ArbnErfG, § 15 ArbnErfG, § 16 ArbnErfG) nur durch Vereinbarung nach der Meldung (§ 22 S. 2 ArbnErfG), Grenze § 23 ArbnErfG.\n\n"
          "**In den Klausuren:** RP2 I/2021 (Anmeldepflicht, Gebrauchsmuster, Hinauszögern, Laufbohrung als Betriebsgeheimnis), RP2 II/2023 "
          "(Anmeldung durch fremde Kanzlei, „Papierkrieg“ nach § 14 ArbnErfG bis § 16 ArbnErfG), RP2 III/2019 (Rücknahme vor Offenlegung), "
          "RP2 II/2022 (Übertragung mit Vorbehalt 2021), RP2 II/2019 (Italien ohne Schutz), RP2 III/2022 (Vertrag: Betriebsgeheimnis und "
          "Fallenlassen ohne Anbietung), RP2 III/2023 (Betriebsgeheimnis vereinbart, B meldet trotzdem an).",
          concepts=["arb_schutzrechtsanmeldung", "arb_aufgabe_schutzrecht", "arb_freigabe"],
          norms=["§ 13 ArbnErfG", "§ 14 ArbnErfG", "§ 16 ArbnErfG", "§ 17 ArbnErfG", "§ 8 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07c-1", "Definitionen",
          "**Unverzüglich (§ 13 Abs. 1 S. 3 ArbnErfG):** ohne schuldhaftes Zögern (§ 121 Abs. 1 S. 1 BGB); Liquiditätsgründe rechtfertigen "
          "kein Abwarten.\n"
          "**Zweckdienlicher Gebrauchsmusterschutz (§ 13 Abs. 1 S. 2 ArbnErfG):** Ausnahme, wenn innerbetrieblich und außerbetrieblich ein "
          "Gebrauchsmuster bei verständiger Würdigung der Verwertbarkeit sinnvoller ist, etwa bei kurzer wirtschaftlicher Lebensdauer "
          "(Schiedsstelle Arb.Erf. 27/20).\n"
          "**Angemessene Nachfrist (§ 13 Abs. 3 ArbnErfG):** vom Arbeitnehmer gesetzte Frist, in der eine Anmeldung bei ordnungsgemäßer "
          "Bearbeitung möglich ist.\n"
          "**Berechtigte Belange (§ 17 Abs. 1 ArbnErfG):** sachliche Gründe, die Erfindung nicht bekannt werden zu lassen, etwa ein am "
          "Erzeugnis nicht erkennbares Herstellungsverfahren; die bloße Präferenz des Arbeitgebers genügt nicht.\n"
          "**Anerkennung der Schutzfähigkeit:** Erklärung gegenüber dem Arbeitnehmer, die Erfindung als patent- oder gebrauchsmusterfähig "
          "zu behandeln; sie bindet für die Vergütung.\n"
          "**Aufgabe (§ 16 ArbnErfG):** Nichtweiterverfolgen der Anmeldung oder Nichtaufrechterhalten des Schutzrechts (z. B. Rücknahme, "
          "Nichtzahlung der Jahresgebühr, Verzicht).\n"
          "**Erfüllung des Vergütungsanspruchs (§ 16 Abs. 1 ArbnErfG):** vollständige Abgeltung, typischerweise durch gezahlte "
          "Pauschalabfindung; bei laufender Vergütung nicht erfüllt.\n"
          "**Prioritätsfrist (§ 14 Abs. 2 S. 2 ArbnErfG):** das Prioritätsjahr der zwischenstaatlichen Verträge (Pariser Verbandsübereinkunft).",
          concepts=["arb_schutzrechtsanmeldung", "arb_aufgabe_schutzrecht"], norms=["§ 13 ArbnErfG", "§ 16 ArbnErfG", "§ 17 ArbnErfG"],
          abschnitt="Definitionen"),
    fall("p07c-2", "Gebrauchsmuster genügt?",
         "Komplementär B ist sich nicht sicher, ob die ordnungsgemäß gemeldete und fingiert in Anspruch genommene Visier-Erfindung seines "
         "Mitarbeiters patentfähig ist. Er möchte deshalb nur ein Gebrauchsmuster anmelden (nach RP2 I/2021).",
         "Erfüllt B damit seine Anmeldepflicht?", False,
         ["**Nein!** Eine patentfähige Diensterfindung ist zum Patent anzumelden, außer der Gebrauchsmusterschutz erscheint bei verständiger "
          "Würdigung der Verwertbarkeit zweckdienlicher (§ 13 Abs. 1 S. 2 ArbnErfG). Zweifel an der Patentfähigkeit klärt das "
          "Prüfungsverfahren; sie sind kein Grund für die Ausnahme (Schiedsstelle Arb.Erf. 27/20)."],
         merke="Grundsatz Patent (§ 13 Abs. 1 S. 2 ArbnErfG); GM nur, wenn zweckdienlicher, nicht wegen Zweifeln.", level=2,
         concepts=["arb_schutzrechtsanmeldung"], norms=["§ 13 Abs. 1 ArbnErfG"], abschnitt=D),
    mc("p07c-3", "Hinauszögern",
       "Wie kann B die Anmeldung der gemeldeten Diensterfindung rechtmäßig vermeiden oder aufschieben?",
       ["Durch Freigabe in Textform oder mit Zustimmung des Arbeitnehmers zur Nichtanmeldung (§ 13 Abs. 2 Nr. 1, 2 ArbnErfG)",
        "Durch Abwarten, bis sich die Liquidität bessert",
        "Durch Anmeldung erst kurz vor Ablauf von 18 Monaten",
        "Durch Hinweis auf fehlende Erfinderqualität des Arbeitnehmers"], 0,
       ["**§ 13 Abs. 2 ArbnErfG.** Die Anmeldung hat unverzüglich zu geschehen (§ 13 Abs. 1 S. 3 ArbnErfG); wirtschaftliche Engpässe "
        "ändern daran nichts. Die Pflicht entfällt nur bei Freigabe (Nr. 1), Zustimmung des Arbeitnehmers (Nr. 2) oder Betriebsgeheimnis "
        "(Nr. 3, § 17 ArbnErfG). Sonst drohen Ersatzvornahme (§ 13 Abs. 3 ArbnErfG) und Schadensersatz."],
       merke="Anmeldepflicht entfällt: frei · Zustimmung · Betriebsgeheimnis (§ 13 Abs. 2 ArbnErfG).", level=1,
       concepts=["arb_schutzrechtsanmeldung"], norms=["§ 13 ArbnErfG"], abschnitt=D),
    fall("p07c-4", "Laufbohrung ohne Anerkennung",
         "W meldet ein Verfahren, mit dem die Laufbohrung billiger eingebracht wird; am fertigen Lauf ist es nicht erkennbar. B will es "
         "geheim halten, hält es aber für nicht erfinderisch und will das W nicht bestätigen (nach RP2 I/2021).",
         "Darf B von der Anmeldung absehen, ohne die Schutzfähigkeit anzuerkennen oder die Schiedsstelle anzurufen?", False,
         ["**Nein!** Berechtigte Belange liegen vor, weil das Verfahren am Produkt nicht erkennbar ist. Ohne Anerkennung der Schutzfähigkeit "
          "(§ 17 Abs. 1 ArbnErfG) darf B aber nur absehen, wenn er zur Einigung über die Schutzfähigkeit die Schiedsstelle anruft "
          "(§ 17 Abs. 2 ArbnErfG). Vergütet wird wie bei einem Schutzrecht, zuzüglich der Nachteile (§ 17 Abs. 3 ArbnErfG, RL Nr. 27)."],
         merke="Betriebsgeheimnis: berechtigte Belange + Anerkennung oder Schiedsstelle (§ 17 Abs. 1, 2 ArbnErfG).", level=2,
         concepts=["arb_schutzrechtsanmeldung"], norms=["§ 17 ArbnErfG", "§ 13 Abs. 2 ArbnErfG"], abschnitt=D),
    mc("p07c-5", "Frist für das Übertragungsverlangen",
       "Bis wann muss die Erfinderin die Übertragung verlangen, und was gilt bei Versäumung?",
       ["Drei Monate nach Zugang der Mitteilung; danach entfällt die Übertragungspflicht, auch wenn der Arbeitgeber doch nicht aufgibt",
        "Vier Monate nach Zugang; danach wird das Patent frei",
        "Zwei Monate nach Zugang; danach kann sie nur noch Schadensersatz verlangen",
        "Bis zum Ablauf der nächsten Jahresgebühr"], 0,
       ["**Drei Monate (§ 16 Abs. 2 ArbnErfG).** Der Arbeitgeber muss nur übertragen, wenn das Verlangen innerhalb der Frist geäußert wird; "
        "das gilt auch, wenn er später an der Aufgabeabsicht nicht festhält (BGH Zündlanze, X ZR 61/20). Berechnung § 187 Abs. 1 BGB, "
        "§ 188 Abs. 2 BGB, § 193 BGB."],
       sachverhalt="Die Arbeitgeberin teilt Erfinderin E am 10.03. mit, sie wolle das Patent nicht aufrechterhalten. E meldet sich erst im "
                   "Juli.",
       merke="§ 16 ArbnErfG: Mitteilung · drei Monate ab Zugang · Übertragung auf Kosten des Arbeitnehmers.", level=2,
       concepts=["arb_aufgabe_schutzrecht"], norms=["§ 16 ArbnErfG"], abschnitt=D),
    fall("p07c-6", "Pauschale schon gezahlt",
         "Erfinder P erhielt 2015 eine Pauschalabfindung, mit der alle Vergütungsansprüche für seine Diensterfindung abgegolten sind. 2024 "
         "will der Arbeitgeber das Patent verfallen lassen.",
         "Muss der Arbeitgeber P die Aufgabe nach § 16 Abs. 1 ArbnErfG mitteilen?", False,
         ["**Nein!** Die Pflicht besteht nur „vor Erfüllung des Anspruchs des Arbeitnehmers auf angemessene Vergütung“ (§ 16 Abs. 1 ArbnErfG). "
          "Mit der gezahlten Pauschalabfindung ist der Anspruch erfüllt; der Arbeitgeber darf frei aufgeben. Bei laufender Vergütung dagegen "
          "muss er mitteilen, sonst schuldet er Schadensersatz."],
         merke="§ 16 ArbnErfG nur vor Erfüllung – nach voller Pauschale frei aufgebbar.", level=2,
         concepts=["arb_aufgabe_schutzrecht"], norms=["§ 16 Abs. 1 ArbnErfG"], abschnitt=D),
    mc("p07c-7", "Weg mit dem Papierkrieg",
       "Wie entgeht der Geschäftsführer rechtmäßig den Pflichten aus § 14 ArbnErfG, § 15 ArbnErfG und § 16 ArbnErfG?",
       ["Durch Vereinbarungen mit den Erfindern nach der jeweiligen Meldung, etwa gegen eine Einmalzahlung (§ 22 S. 2 ArbnErfG)",
        "Durch eine Klausel im Arbeitsvertrag, die auf diese Rechte verzichtet",
        "Durch eine Betriebsanweisung",
        "Gar nicht, die Pflichten sind unabdingbar"], 0,
       ["**§ 22 S. 2 ArbnErfG.** Zuungunsten des Arbeitnehmers kann vom Gesetz nicht abgewichen werden (§ 22 S. 1 ArbnErfG); eine "
        "Vorausklausel im Arbeitsvertrag ist insoweit unwirksam. Nach der Meldung sind Vereinbarungen über die Diensterfindung zulässig, "
        "etwa ein Verzicht auf Auslandsfreigabe und Übertragungsangebot gegen Zahlung; sie dürfen nicht erheblich unbillig sein "
        "(§ 23 Abs. 1 ArbnErfG)."],
       sachverhalt="Der Geschäftsführer möchte nicht mehr nach jeder Anmeldung fragen müssen, ob der Erfinder im Ausland anmelden will, ob "
                   "er aufgegebene Schutzrechte übernehmen will, und ihn über das Verfahren unterrichten (nach RP2 II/2023).",
       merke="Abweichung nur nach Meldung (§ 22 S. 2 ArbnErfG), Grenze Unbilligkeit (§ 23 ArbnErfG).", level=2,
       concepts=["arb_aufgabe_schutzrecht", "arb_unbilligkeit"], norms=["§ 22 ArbnErfG", "§ 14 ArbnErfG", "§ 16 ArbnErfG"], abschnitt=D),
    fall("p07c-8", "Golfschläger aus Italien",
         "Das europäische Patent auf die Diensterfindung des L wurde nur in DE, FR, UK und IE validiert. Eine 2017 gegründete Tochter "
         "fertigt die Golfschläger in Italien und verkauft sie nur dort; dem L wurde Italien nie freigegeben (nach RP2 II/2019).",
         "Schuldet der Arbeitgeber für die italienischen Umsätze eine Vergütung nach § 9 ArbnErfG?", False,
         ["**Nein!** Benutzung im schutzrechtsfreien Ausland mit dortiger Herstellung wird im Allgemeinen nicht vergütet (RL Nr. 26); "
          "Wettbewerber könnten dort ebenso tätig werden. Das Problem liegt in § 14 Abs. 2 ArbnErfG: Für Staaten ohne eigene Anmeldung hätte "
          "der Arbeitgeber rechtzeitig freigeben müssen, mit Vorbehalt eines Benutzungsrechts (§ 14 Abs. 3 ArbnErfG)."],
         merke="Schutzrechtsfreies Ausland: keine Vergütung (RL Nr. 26) – aber Freigabepflicht § 14 Abs. 2 ArbnErfG.", level=3,
         concepts=["arb_schutzrechtsanmeldung", "arb_erfindungswert"], norms=["§ 14 ArbnErfG", "§ 9 ArbnErfG"], abschnitt=D),
    *fallkette("p07c-9", "Visier und Laufbohrung (nach RP2 I/2021)",
        "Komplementär B erhielt am 06.12.2018 eine ordnungsgemäße Meldung seines Mitarbeiters W über eine neue Visierung und reagierte "
        "nicht. 2021 fragt W, was aus der Anmeldung werde. B möchte wegen knapper Liquidität möglichst nicht oder spät anmelden.",
        [frage("Ist B zur Anmeldung im Inland verpflichtet?", True,
               ["**Ja!** Mangels Freigabe gilt die Erfindung seit Ablauf des 08.04.2019 als in Anspruch genommen (§ 6 Abs. 2 ArbnErfG; "
                "06.04.2019 war ein Samstag, § 193 BGB). B ist verpflichtet und allein berechtigt, unverzüglich anzumelden "
                "(§ 13 Abs. 1 S. 1, 3 ArbnErfG); eine Ausnahme nach § 13 Abs. 2 ArbnErfG liegt nicht vor."],
               merke="Fiktion + keine Ausnahme → unverzügliche Inlandsanmeldung (§ 13 Abs. 1 ArbnErfG).", titel="V1–V3 Anmeldepflicht", level=2),
         frage("Was kann W tun, wenn B weiter untätig bleibt?", 0,
               ["**Nachfrist und Ersatzvornahme.** W setzt eine angemessene Nachfrist und meldet nach deren Ablauf selbst auf Namen und Kosten "
                "des B an (§ 13 Abs. 3 ArbnErfG). Für den Schaden aus der Verzögerung, etwa durch zwischenzeitlichen Stand der Technik, haftet B "
                "nach § 823 Abs. 2 BGB i.V.m. § 13 Abs. 1 ArbnErfG (Schiedsstelle Arb.Erf. 27/20)."],
               optionen=["Nachfrist setzen, dann selbst auf Namen und Kosten des B anmelden; daneben Schadensersatz",
                         "Sofort auf eigenen Namen anmelden",
                         "Die Erfindung gilt als frei; W kann sie verwerten",
                         "Nur die Schiedsstelle anrufen; weitere Rechte hat W nicht"],
               merke="Ersatzvornahme: Nachfrist → Anmeldung auf Namen und Kosten des Arbeitgebers (§ 13 Abs. 3 ArbnErfG).",
               titel="V5 Ersatzvornahme", level=2),
         frage("Kann B die Anmeldung des Verfahrens vermeiden, ohne die Schutzfähigkeit anzuerkennen?", True,
               ["**Ja!** Berechtigte Belange liegen vor, weil das Verfahren am Lauf nicht erkennbar ist. B kann zur Einigung über die "
                "Schutzfähigkeit die Schiedsstelle anrufen und von der Anmeldung absehen (§ 17 Abs. 2 ArbnErfG); erkennt er an, gilt "
                "§ 17 Abs. 1 ArbnErfG. Vergütet wird auch das Betriebsgeheimnis (§ 17 Abs. 3 ArbnErfG, RL Nr. 27)."],
               merke="Geheimes Verfahren: § 17 Abs. 2 ArbnErfG (Schiedsstelle) statt Anerkennung.", titel="AGL 4 Betriebsgeheimnis",
               abwandlung="W meldet ein neues Bohrverfahren, das am fertigen Lauf nicht zu sehen ist; B hält es für nicht erfinderisch.", level=2),
         ],
        abschnitt=K, level=2, concepts=["arb_schutzrechtsanmeldung"], norms=["§ 13 ArbnErfG", "§ 17 ArbnErfG"]),
    *fallkette("p07c-10", "Die fremde Kanzlei (nach RP2 II/2023)",
        "Die ordnungsgemäße Meldung des Dr. L ging vor neun Monaten ein; der Geschäftsführer gab sie einer Kanzlei und vergaß den Vorgang. "
        "Vor drei Monaten forderte L ihn per E-Mail mit sechswöchiger Frist zur Anmeldung auf. Nun schickt L die Rechnung einer anderen "
        "Kanzlei, die auf den Namen der GmbH angemeldet hat.",
        [frage("Durfte L die Anmeldung auf den Namen der GmbH bewirken?", True,
               ["**Ja!** Die Erfindung gilt als in Anspruch genommen (§ 6 Abs. 2 ArbnErfG); die GmbH hat nicht unverzüglich angemeldet "
                "(§ 13 Abs. 1 S. 3 ArbnErfG). Nach fruchtlosem Ablauf einer angemessenen Nachfrist darf der Arbeitnehmer für den Arbeitgeber "
                "auf dessen Namen anmelden (§ 13 Abs. 3 ArbnErfG). Darin liegt seine gesetzliche Befugnis, den Vertreter zu beauftragen."],
               merke="§ 13 Abs. 3 ArbnErfG: gesetzliche Befugnis zur Anmeldung im Namen des Arbeitgebers.", titel="V1–V5 Ersatzvornahme", level=2),
         frage("Muss die GmbH die Kosten der Anmeldung tragen?", True,
               ["**Ja!** Die Ersatzvornahme geschieht „auf dessen Namen und Kosten“ (§ 13 Abs. 3 ArbnErfG). Dass die eigene Kanzlei billiger "
                "wäre, ändert dem Grunde nach nichts; die GmbH hätte selbst rechtzeitig anmelden können. Zu prüfen bleibt nur, ob die Kosten "
                "für die Anmeldung erforderlich waren."],
               merke="Ersatzvornahme auf Kosten des säumigen Arbeitgebers.", titel="Rechtsfolge: Kosten", level=2),
         frage("Durfte L dann ebenfalls auf den Namen der GmbH anmelden?", False,
               ["**Nein!** § 13 Abs. 3 ArbnErfG verlangt eine vom Arbeitnehmer gesetzte angemessene Nachfrist. Eine bloße Aufforderung "
                "genügt dem Wortlaut nicht; L hätte erst eine angemessene Frist setzen müssen. Die Kosten kann er dann nicht nach "
                "§ 13 Abs. 3 ArbnErfG auf die GmbH abwälzen."],
               merke="Ohne gesetzte Nachfrist keine Ersatzvornahme (§ 13 Abs. 3 ArbnErfG).", titel="V5 Nachfrist",
               abwandlung="Die E-Mail des L forderte nur zur Anmeldung auf, ohne eine Frist zu nennen.", level=3),
         ],
        abschnitt=K, level=2, concepts=["arb_schutzrechtsanmeldung"], norms=["§ 13 ArbnErfG"]),
])

# ====================================================================== p07d Vergütung
P07D = dict(id="p07d", titel="§§ 9, 12, 23 ArbnErfG mit Vergütungsrichtlinien: Vergütung", einheiten=[
    intro("p07d-0", "Prüfungsschema",
          "**AGL:** § 9 Abs. 1 ArbnErfG (Grund), Bemessung § 9 Abs. 2 ArbnErfG i.V.m. RL Nr. 39: **V = E × A** (bei Miterfindern × Anteil); "
          "Lizenzanalogie **E = B × L**, also **V = B × L × A**\n\n"
          "**A · Anspruch dem Grunde nach**\n"
          "**V1 Diensterfindung eines Arbeitnehmers** – § 4 Abs. 2 ArbnErfG; Hochschulbeschäftigte: 30 % der Einnahmen (§ 42 Nr. 4 ArbnErfG); "
          "qualifizierter Verbesserungsvorschlag: § 20 Abs. 1 ArbnErfG; GmbH-Geschäftsführer: kein Anspruch (Arb.Erf. 58/16)\n"
          "**V2 Inanspruchnahme** – § 9 Abs. 1 ArbnErfG mit § 6 ArbnErfG; Betriebsgeheimnis wie Schutzrecht (§ 17 Abs. 3 ArbnErfG, RL Nr. 27)\n"
          "**V3 Parteien** – Gläubiger: Erfinder, nach dem Tod sein Erbe (§ 1922 Abs. 1 BGB; Anspruch vererblich, Schiedsstelle Arb.Erf. 14/06); "
          "Schuldner: Arbeitgeber, bei Leiharbeit der Entleiher (Arb.Erf. 24/23), im Insolvenzfall § 27 ArbnErfG, bei Gesamtrechtsnachfolge "
          "der übernehmende Rechtsträger (Arb.Erf. 23/21 vom 14.11.2023); Fortbestand nach Ausscheiden (§ 26 ArbnErfG)\n"
          "**V4 Kein wirksamer Ausschluss** – Vorausverzicht unwirksam (§ 22 S. 1 ArbnErfG; „durch das Gehalt abgegolten“, Arb.Erf. 53/99); "
          "Vereinbarung nach der Meldung zulässig (§ 22 S. 2 ArbnErfG), Grenze § 23 ArbnErfG\n\n"
          "**B · Höhe (§ 9 Abs. 2 ArbnErfG)**\n"
          "**V5 Erfindungswert E** – Eigennutzung: Lizenzanalogie (RL Nr. 3, RL Nr. 6 bis RL Nr. 11), erfassbarer Nutzen (RL Nr. 12), "
          "Schätzung (RL Nr. 13). Bezugsgröße: Umsatz ab Werk, konzerninterner Verrechnungspreis ausnahmsweise mit Aufschlag auf den Marktpreis "
          "(RL Nr. 7; Arb.Erf. 29/12); Konzernumsätze grundsätzlich nicht, außer der Konzern ist wirtschaftlich eine Einheit (Arb.Erf. 12/08). "
          "Lizenzsatz nach Branche (RL Nr. 10: Elektro 0,5–5 %, Maschinen 1/3–10 %, Chemie 2–5 %, Pharma 2–10 %); Abstaffelung nur bei "
          "branchenüblicher Kausalitätsverschiebung (RL Nr. 11; Arb.Erf. 18/13). Lizenzvergabe: Nettolizenzeinnahme (RL Nr. 14), "
          "vereinfacht 20–50 % der Bruttolizenzeinnahme (RL Nr. 15); Know-how-Entgelt abziehen (RL Nr. 14). Verkauf: Nettoerlös (RL Nr. 16). "
          "Austausch: Anteil am Gesamtnutzen (RL Nr. 17). Sperr-, Vorrats-, nicht verwertete Patente RL Nr. 18 bis RL Nr. 24 (Prüfungszeit "
          "drei bis fünf Jahre, RL Nr. 23). Ausland: Belieferung vom Inland zählt mit, im schutzrechtsfreien Ausland Hergestelltes nicht "
          "(RL Nr. 26). Benutzt ist nur, was ein Patent einem Wettbewerber verbieten könnte (Arb.Erf. 46/20)\n"
          "**V6 Anteilsfaktor A** – Summe der Wertzahlen a (Aufgabe, RL Nr. 31) + b (Lösung, RL Nr. 32) + c (Stellung, RL Nr. 33 bis RL Nr. 36) "
          "→ Tabelle RL Nr. 37\n"
          "**V7 Miterfinderanteil** – für jeden gesondert (§ 12 Abs. 2 S. 1 ArbnErfG)\n\n"
          "**C · Feststellung, Festsetzung, Korrektur (§ 12 ArbnErfG, § 23 ArbnErfG)**\n"
          "**V8 Vereinbarung** (§ 12 Abs. 1 ArbnErfG) **oder Festsetzung** durch begründete Erklärung in Textform, spätestens drei Monate nach "
          "Erteilung (§ 12 Abs. 3 ArbnErfG); Widerspruch in Textform binnen zwei Monaten, sonst verbindlich (§ 12 Abs. 4 ArbnErfG); Widerspruch "
          "eines Miterfinders gegen seinen Anteil macht sie für alle unverbindlich (§ 12 Abs. 5 ArbnErfG)\n"
          "**V9 Anpassung** – wesentliche Änderung der maßgebenden Umstände, keine Rückforderung (§ 12 Abs. 6 ArbnErfG); bei Pauschalen erst ab "
          "etwa dreifacher Nutzung gegenüber der Prognose (Arb.Erf. 52/13)\n"
          "**V10 Unbilligkeit** – erhebliche Unbilligkeit bei Abschluss (§ 23 Abs. 1 ArbnErfG): objektives Missverhältnis nach der Praxis der Schiedsstelle "
          "grundsätzlich ab Faktor 2 (vom BGH für die Überzahlung gebilligt, BGH Chemische Verbrauchsmaterialien; auch der Arbeitgeber kann "
          "sich auf § 23 ArbnErfG berufen), bei Pauschalabfindungen erst ab Faktor 3 (Arb.Erf. 03/09); Geltendmachung in Textform bis sechs Monate "
          "nach Beendigung des Arbeitsverhältnisses (§ 23 Abs. 2 ArbnErfG)\n\n"
          "**D · Hilfsansprüche und Einwendungen** – Auskunft und Rechnungslegung (§ 242 BGB; Umfang nach Berechnungsmethode, BGH "
          "Abwasserbehandlung; nicht über Gewinne, BGH Türinnenverstärkung); Verjährung drei Jahre (§ 195 BGB, § 199 Abs. 1 BGB), Hemmung "
          "(§ 203 BGB; § 204 Abs. 1 Nr. 4 BGB analog, BGH Profilstrangpressverfahren); Zuwarten allein begründet keine Verwirkung (BGH Ozon).\n\n"
          "**⇒ Rechtsfolge:** Zahlung von V, laufend (jährlich, RL Nr. 40) oder als Gesamtabfindung (bei Patenten Ansatz von sechs Jahren "
          "Laufdauer, RL Nr. 41).\n\n"
          "**In den Klausuren:** Verrechnungspreis, Lizenz mit Know-how, Erbin (RP2 II/2018); Konzernnutzung, Kreuzlizenzen, Auskunft (RP2 III/2018); "
          "Vereinbarung 2.000 €, Leiharbeiter, Lizenz mit Export (RP2 II/2019); Pauschale und Lizenzeinnahmen 5 % von 10 Mio. € (RP2 II/2020); "
          "Betriebsvereinbarung 1.500 €, Lizenzen, Export (RP2 III/2021); Pauschale 1.000 € und Umsatzschwelle (RP2 I/2022); fünf Erfinder, "
          "Hochschule, Leiharbeiter, Abstaffelung im Lizenzvertrag (RP2 III/2022); Verkauf (RP2 I/2023); deaktivierte Funktionen (RP2 II/2023); "
          "Anpassung bei Betriebsgeheimnis (RP2 III/2019); Anpassung einer Pauschale (RP2 I/2021, RP2 II/2021).",
          concepts=["arb_verguetungsanspruch", "arb_erfindungswert", "arb_anteilsfaktor", "arb_lizenzanalogie", "arb_festsetzung"],
          norms=["§ 9 ArbnErfG", "§ 12 ArbnErfG", "§ 22 ArbnErfG", "§ 23 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07d-1", "Definitionen und Rechenhilfe",
          "**Erfindungswert:** Preis, den der Arbeitgeber einem freien Erfinder für die Erfindung zahlen würde (wirtschaftliche "
          "Verwertbarkeit, § 9 Abs. 2 ArbnErfG; RL Nr. 3).\n"
          "**Lizenzanalogie:** Erfindungswert = Bezugsgröße × Lizenzsatz, den vernünftige Parteien für eine vergleichbare freie Erfindung "
          "vereinbart hätten (RL Nr. 6, RL Nr. 7, RL Nr. 39).\n"
          "**Bezugsgröße:** Umsatz oder Erzeugung, in der Regel der Rechnungswert des das Werk verlassenden Erzeugnisses (RL Nr. 7); ganze "
          "Vorrichtung oder wertbeeinflusster Teil (RL Nr. 8).\n"
          "**Nettolizenzeinnahme:** Bruttolizenzeinnahme abzüglich Entwicklungs-, Betriebsreife-, Schutzrechts- und Lizenzkosten sowie des "
          "Know-how-Anteils (RL Nr. 14).\n"
          "**Anteilsfaktor:** Prozentsatz des Erfindungswerts, der dem Arbeitnehmer bleibt, weil es keine freie Erfindung ist (RL Nr. 30).\n"
          "**Wertzahl a (RL Nr. 31):** 1 Aufgabe mit Lösungsweg gestellt · 2 Aufgabe ohne Lösungsweg · 3 Mängel durch Betriebszugehörigkeit "
          "bekannt, nicht selbst festgestellt · 4 selbst festgestellt · 5 Aufgabe selbst gestellt im Aufgabenbereich · 6 außerhalb.\n"
          "**Wertzahl b (RL Nr. 32):** 1, wenn die Lösung mit beruflich geläufigen Überlegungen, auf Grund betrieblicher Arbeiten oder "
          "Kenntnisse und mit technischen Hilfsmitteln des Betriebs gefunden wurde; 6, wenn keines davon vorliegt; dazwischen abgestuft.\n"
          "**Wertzahl c (RL Nr. 34):** 1 Leiter der gesamten Forschung · 2 Leiter der Entwicklungsabteilung · 3 Gruppenleiter in Entwicklung, "
          "Ingenieure in der Forschung · 4 Ingenieure und Chemiker in der Entwicklung · 5 in der Fertigung · 6 Meister, Techniker · "
          "7 Facharbeiter, Laboranten · 8 Ungelernte. In kleinen Betrieben Leiter eher in Gruppe 2 bis 4 (RL Nr. 34 a.E.).\n"
          "**Tabelle RL Nr. 37 (a + b + c → A):** 3 → 2 % · 4 → 4 % · 5 → 7 % · 6 → 10 % · 7 → 13 % · 8 → 15 % · 9 → 18 % · 10 → 21 % · "
          "11 → 25 % · 12 → 32 % · 13 → 39 % · 14 → 47 % · 15 → 55 % · 16 → 63 % · 17 → 72 % · 18 → 81 % · 19 → 90 %.\n"
          "**Beispiel RL Nr. 39:** Jahresumsatz 400.000, L = 3 %, a + b + c = 8 → A = 15 %: V = 400.000 × 3 % × 15 % = 1.800.\n"
          "**Erhebliche Unbilligkeit (§ 23 Abs. 1 ArbnErfG):** objektives Missverhältnis zwischen vereinbarter und gesetzlich geschuldeter "
          "Vergütung im Zeitpunkt der Vereinbarung.\n"
          "**Wesentliche Änderung (§ 12 Abs. 6 ArbnErfG):** nachträgliche Veränderung, die ein so auffallendes Missverhältnis schafft, dass "
          "Festhalten unzumutbar ist (Schiedsstelle Arb.Erf. 29/20).",
          concepts=["arb_erfindungswert", "arb_lizenzanalogie", "arb_anteilsfaktor", "arb_unbilligkeit", "arb_anpassung"],
          norms=["§ 9 Abs. 2 ArbnErfG", "§ 12 Abs. 6 ArbnErfG", "§ 23 ArbnErfG"], abschnitt="Definitionen"),
    fall("p07d-2", "Durch das Gehalt abgegolten",
         "Ein Golfschlägerhersteller will in neue Arbeitsverträge schreiben: „Möglicherweise entstehende Erfindervergütungen sind durch das "
         "Gehalt abgegolten.“ Der Entwicklungsleiter verdient 150.000 € im Jahr (nach RP2 II/2019).",
         "Entfällt damit künftig der Vergütungsanspruch?", False,
         ["**Nein!** Die Vergütung ist eine Sonderleistung neben dem Lohn (§ 9 Abs. 1 ArbnErfG). Vor der Meldung kann zuungunsten des "
          "Arbeitnehmers nicht abgewichen werden (§ 22 S. 1 ArbnErfG); eine solche Vorausklausel erfasst künftige Erfindungen nicht "
          "(Schiedsstelle Arb.Erf. 53/99). Das hohe Gehalt wirkt nur im Anteilsfaktor (Wertzahl c, RL Nr. 33, RL Nr. 35)."],
         merke="Vorausverzicht unwirksam (§ 22 S. 1 ArbnErfG); Stellung und Gehalt nur im Anteilsfaktor.", level=1,
         concepts=["arb_verguetungsanspruch", "arb_anteilsfaktor"], norms=["§ 22 ArbnErfG", "§ 9 ArbnErfG"], abschnitt=D),
    fall("p07d-3", "Der Konzernverrechnungspreis",
         "Die Sauklar GmbH verkauft erfindungsgemäße Zielfernrohre für 600 € an eine Konzernschwester; Dritten gegenüber kostet dasselbe "
         "Zielfernrohr 1.300 € (nach RP2 II/2018).",
         "Darf der Erfinder als Bezugsgröße mehr als 600 € je Stück ansetzen?", True,
         ["**Ja!** Bezugsgröße ist in der Regel der Rechnungswert ab Werk; ein betriebsinterner Verrechnungswert ist kritisch zu prüfen "
          "(RL Nr. 7). Liegt der konzerninterne Preis unter dem Marktpreis, ist ausnahmsweise ein Aufschlag gerechtfertigt, bemessen nach der "
          "Differenz zum Preis unabhängiger Dritter (Schiedsstelle Arb.Erf. 29/12). Hier also bis 1.300 €."],
         merke="Verrechnungspreis unter Markt → Aufschlag bis zum Drittpreis (Arb.Erf. 29/12).", level=2,
         concepts=["arb_lizenzanalogie", "arb_erfindungswert"], norms=["§ 9 Abs. 2 ArbnErfG"], abschnitt=D),
    fall("p07d-4", "Export ins patentfreie Ausland",
         "Die DD GmbH stellt den patentierten Mikroorganismus in Deutschland her; die Hälfte des Umsatzes von 30 Mio. € erzielt sie mit "
         "Lieferungen in Länder ohne Patentschutz (nach RP2 III/2022).",
         "Gehört auch der Exportumsatz zur Bezugsgröße?", True,
         ["**Ja!** Wird das Ausland vom Inland aus beliefert, ist bei der Lizenzanalogie der Umsatz auch insoweit zu berücksichtigen "
          "(RL Nr. 26 S. 2). Die Herstellung im Inland ist Benutzung des deutschen Patents. Nur bei Herstellung und Vertrieb im "
          "schutzrechtsfreien Ausland entfällt die Vergütung im Allgemeinen (RL Nr. 26 a.E.)."],
         merke="Inlandsherstellung, Export ins patentfreie Ausland: vergütungspflichtig (RL Nr. 26).", level=2,
         concepts=["arb_erfindungswert"], norms=["§ 9 Abs. 2 ArbnErfG"], abschnitt=D),
    mc("p07d-5", "Umfang der Auskunft",
       "Worüber muss der Arbeitgeber bei der Lizenzanalogie in der Regel Auskunft geben?",
       ["Über Umsätze und Stückzahlen mit erfindungsgemäßen Produkten, nicht über den Gewinn",
        "Über seinen Gewinn mit den Produkten",
        "Über alle Kosten der Entwicklung",
        "Über nichts; der Erfinder muss die Zahlen selbst ermitteln"], 0,
       ["**Umsätze, nicht Gewinne.** Der Anspruch aus § 242 BGB reicht so weit, wie der Erfinder die Angaben für die gewählte "
        "Berechnungsmethode braucht (BGH Abwasserbehandlung). Bei der Lizenzanalogie kommt es auf den Umsatz an; Auskunft über den "
        "Gewinn schuldet der Arbeitgeber regelmäßig nicht (BGH Türinnenverstärkung, X ZR 137/07)."],
       merke="Auskunft: § 242 BGB; Inhalt folgt der Methode (Lizenzanalogie → Umsatz).", level=2,
       concepts=["arb_auskunft"], norms=["§ 9 ArbnErfG"], abschnitt=D),
    fall("p07d-6", "Schiedsstelle und Verjährung",
         "Erfinder V ruft im Dezember 2024 die Schiedsstelle an; sein Vergütungsanspruch für 2021 würde mit Ablauf des 31.12.2024 verjähren.",
         "Hemmt die Anrufung der Schiedsstelle die Verjährung?", True,
         ["**Ja!** Die Schiedsstelle steht einer Gütestelle gleich; ihre Anrufung hemmt die Verjährung entsprechend § 204 Abs. 1 Nr. 4 BGB, "
          "nicht nach § 204 Abs. 1 Nr. 12 BGB (BGH Profilstrangpressverfahren, X ZR 3/13). Frist: drei Jahre (§ 195 BGB) ab Schluss des "
          "Jahres von Entstehung und Kenntnis (§ 199 Abs. 1 BGB)."],
         merke="Verjährung § 195 BGB, § 199 Abs. 1 BGB; Hemmung durch Schiedsstelle analog § 204 Abs. 1 Nr. 4 BGB.", level=2,
         concepts=["arb_verguetungsanspruch", "arb_schiedsstelle"], norms=["§ 9 ArbnErfG", "§ 28 ArbnErfG"], abschnitt=D),
    *fallkette("p07d-7", "Das Zielfernrohr (nach RP2 II/2018)",
        "Entwicklungsleiter Z einer GmbH mit 26 Mitarbeitern und Kollege A melden im Mai 2014 gemeinsam eine Erfindung (je 50 %). Bis Mai "
        "2018 werden 4.040 Stück an eine Konzernschwester verkauft (600 € statt Marktpreis 1.300 €); Lizenzeinnahmen 59.500 €, dazu 10.000 € "
        "für Know-how. Am 01.10.2017 setzt die GmbH in Textform begründet 500 € fest. A ist verstorben, seine Witwe Alleinerbin.",
        [frage("Z hat das Problem selbst erkannt (a = 4), die Lösung mit betrieblichen Mitteln gefunden (b = 2); als Entwicklungsleiter im "
               "Kleinbetrieb ist c = 3. Wie hoch ist der Anteilsfaktor?", 0,
               ["**18 %.** a + b + c = 4 + 2 + 3 = 9; nach der Tabelle in RL Nr. 37 ergibt 9 einen Anteilsfaktor von 18 %. In kleinen Betrieben "
                "gehört der Leiter der Entwicklung nicht in Gruppe 2, sondern je nach Lage in Gruppe 2 bis 4 (RL Nr. 34 a.E.)."],
               optionen=["18 %", "15 %", "21 %", "9 %"],
               merke="A aus RL Nr. 37: Summe 9 → 18 %.", titel="V6 Anteilsfaktor", level=2),
         frage("Welche Vergütung schuldet die GmbH dem Z für die Eigenumsätze bei einem Lizenzsatz von 3 % (ohne Abstaffelung)?", 0,
               ["**14.180,40 €.** V = B × L × A × Anteil (RL Nr. 39): 4.040 × 1.300 € = 5.252.000 € (Marktpreis statt Verrechnungspreis, "
                "Arb.Erf. 29/12); × 3 % = 157.560 €; × 18 % = 28.360,80 €; × 50 % = 14.180,40 €."],
               optionen=["14.180,40 €", "6.544,80 €", "28.360,80 €", "78.780,00 €"],
               merke="V = B × L × A × Miterfinderanteil (RL Nr. 39).", titel="V5 Erfindungswert aus Eigennutzung", level=2),
         frage("Welche Vergütung folgt aus den Lizenzeinnahmen, wenn der Erfindungswert mit 30 % der Bruttolizenzeinnahme angesetzt wird?", 0,
               ["**1.606,50 €.** Erfindungswert ist die Nettolizenzeinnahme (RL Nr. 14), vereinfacht 20–50 % der Bruttoeinnahme (RL Nr. 15). "
                "Das Know-how-Entgelt bleibt außer Ansatz (RL Nr. 14). 59.500 € × 30 % = 17.850 €; × 18 % × 50 % = 1.606,50 €."],
               optionen=["1.606,50 €", "1.876,50 €", "3.213,00 €", "5.355,00 €"],
               merke="Lizenzvergabe: E = Nettolizenzeinnahme (RL Nr. 14, RL Nr. 15), ohne Know-how.", titel="V5 Erfindungswert aus Lizenzen", level=3),
         frage("Kann Z die Festsetzung vom 01.10.2017 im Juni 2018 noch durch Widerspruch beseitigen?", False,
               ["**Nein!** Die Festsetzung ist begründet und in Textform erklärt (§ 12 Abs. 3 S. 1 ArbnErfG). Der Widerspruch hätte binnen zwei "
                "Monaten zugehen müssen, bis 01.12.2017 (§ 12 Abs. 4 S. 1 ArbnErfG). Sie ist verbindlich (§ 12 Abs. 4 S. 2 ArbnErfG). Z bleibt "
                "die erhebliche Unbilligkeit (§ 23 ArbnErfG): 500 € gegenüber über 15.000 € sind ein krasses Missverhältnis."],
               merke="Verpasster Widerspruch → Festsetzung verbindlich; Ausweg § 23 ArbnErfG.", titel="V8 Festsetzung und Widerspruch", level=2),
         frage("Kann Z den Vergütungsanspruch des verstorbenen A für sich geltend machen?", False,
               ["**Nein!** Der Vergütungsanspruch ist vererblich (Schiedsstelle Arb.Erf. 14/06); er ging mit dem Tod auf die Alleinerbin über "
                "(§ 1922 Abs. 1 BGB). Z kann allenfalls im Auftrag der Witwe handeln. Gesondert festzustellen ist der Anspruch jedes "
                "Miterfinders (§ 12 Abs. 2 S. 1 ArbnErfG)."],
               merke="Tod des Erfinders: Anspruch geht auf die Erben über (§ 1922 Abs. 1 BGB).", titel="V3 Gläubiger", level=1),
         ],
        abschnitt=K, level=2, concepts=["arb_verguetungsanspruch", "arb_anteilsfaktor", "arb_lizenzanalogie"], norms=["§ 9 ArbnErfG", "§ 12 ArbnErfG"]),
    *fallkette("p07d-8", "Die Pauschale von 1.000 € (nach RP2 I/2022)",
        "Entwicklungsingenieurin M und Kollege K (je 50 %) erhielten eine Aufgabe ohne Lösungsweg und lösten sie mit beruflich geläufigen "
        "Überlegungen, Betriebswissen und betrieblichen Hilfsmitteln. Anfang 2020 unterschreibt M eine Pauschalvereinbarung über einmalig "
        "1.000 € für die weltweite Nutzung. Branchenüblicher Lizenzsatz 3 %.",
        [frage("Wie hoch ist der Anteilsfaktor der M?", 0,
               ["**13 %.** a = 2 (Aufgabe ohne Lösungsweg, RL Nr. 31), b = 1 (alle drei Merkmale, RL Nr. 32), c = 4 (Ingenieurin in der "
                "Entwicklung, RL Nr. 34). Summe 7 → 13 % (RL Nr. 37)."],
               optionen=["13 %", "10 %", "15 %", "7 %"],
               merke="2 + 1 + 4 = 7 → 13 % (RL Nr. 37).", titel="V6 Anteilsfaktor", level=2),
         frage("Ab welchem Gesamtumsatz ist die Pauschale erheblich unbillig, wenn die Schiedsstelle das Dreifache verlangt?", 0,
               ["**Rund 1,54 Mio. €.** Gesetzliche Vergütung: U × 3 % × 13 % × 50 % = U × 0,00195. Erheblich unbillig ist eine Pauschale, wenn "
                "die gesetzliche Vergütung sie um das Dreifache übersteigt (Arb.Erf. 03/09): U × 0,00195 > 3.000 € → U > 1.538.462 €. Mit dem "
                "allgemeinen Faktor 2 wären es rund 1,03 Mio. €."],
               optionen=["Rund 1,54 Mio. €", "Rund 1,03 Mio. €", "Rund 0,51 Mio. €", "Rund 3,08 Mio. €"],
               merke="Schwelle: V(gesetzlich) > Faktor × Pauschale; V = U × L × A × Anteil.", titel="V10 Unbilligkeit", level=3),
         frage("Bis wann muss M die Unbilligkeit geltend machen?", 0,
               ["**Bis sechs Monate nach Beendigung des Arbeitsverhältnisses, in Textform** (§ 23 Abs. 2 ArbnErfG). Solange M angestellt ist, "
                "läuft die Frist nicht ab. Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB, § 193 BGB."],
               optionen=["Bis sechs Monate nach Beendigung des Arbeitsverhältnisses, in Textform",
                         "Binnen zwei Monaten nach Unterzeichnung",
                         "Binnen drei Jahren ab Kenntnis",
                         "Binnen eines Monats nach Zahlung"],
               merke="§ 23 Abs. 2 ArbnErfG: Textform, spätestens sechs Monate nach Ende des Arbeitsverhältnisses.", titel="V10 Frist", level=1),
         frage("Welche AGL trägt jetzt eine höhere Vergütung?", 0,
               ["**§ 12 Abs. 6 S. 1 ArbnErfG.** Unbilligkeit wird am Zeitpunkt der Vereinbarung gemessen. Spätere wesentliche Änderungen führen "
                "zur Anpassung; bei Pauschalen sieht die Schiedsstelle die Schwelle bei etwa dem Dreifachen der Prognose (Arb.Erf. 52/13). "
                "Gezahltes wird nicht zurückgefordert (§ 12 Abs. 6 S. 2 ArbnErfG)."],
               optionen=["§ 12 Abs. 6 S. 1 ArbnErfG", "§ 23 Abs. 1 ArbnErfG", "§ 12 Abs. 4 ArbnErfG", "§ 16 Abs. 1 ArbnErfG"],
               merke="Spätere Entwicklung → § 12 Abs. 6 ArbnErfG; Fehler von Anfang an → § 23 ArbnErfG.", titel="V9 Anpassung",
               abwandlung="Die 1.000 € entsprachen der damals realistischen Umsatzprognose; danach verfünffacht sich der Umsatz unerwartet.", level=2),
         ],
        abschnitt=K, level=2, concepts=["arb_unbilligkeit", "arb_anpassung", "arb_anteilsfaktor"], norms=["§ 23 ArbnErfG", "§ 12 Abs. 6 ArbnErfG"]),
])

# ====================================================================== p07e Ausscheiden, Insolvenz, Übertragung
P07E = dict(id="p07e", titel="§§ 26, 27 ArbnErfG: Ausscheiden, Insolvenz und Verkauf", einheiten=[
    intro("p07e-0", "Prüfungsschema",
          "**AGL 1: Vergütung nach dem Ausscheiden**, § 9 Abs. 1 ArbnErfG i.V.m. § 26 ArbnErfG\n"
          "**V1 Diensterfindung während des Arbeitsverhältnisses gemacht** – § 4 Abs. 2 ArbnErfG; nach dem Ausscheiden gemachte Erfindungen "
          "fallen nicht unter das Gesetz (Pensionär: Schiedsstelle Arb.Erf. 24/06)\n"
          "**V2 Inanspruchnahme** – § 6 ArbnErfG\n"
          "**V3 Fortgeltung** – Rechte und Pflichten werden durch die Auflösung nicht berührt (§ 26 ArbnErfG); der Vergütungsanspruch besteht "
          "fort, solange der Arbeitgeber Vorteile aus der Monopolstellung zieht (Arb.Erf. 23/21 vom 14.06.2023)\n"
          "**Folgen des Ausscheidens:** Klage ohne Schiedsverfahren (§ 37 Abs. 2 Nr. 3 ArbnErfG); Ausschlussfrist für die Unbilligkeit läuft "
          "sechs Monate ab Beendigung (§ 23 Abs. 2 ArbnErfG; bei Wechsel zur Konzernschwester als Geschäftsführer ab dem Wechsel, "
          "Arb.Erf. 04/19).\n\n"
          "**AGL 2: Vergütung im Insolvenzverfahren des Arbeitgebers**, § 27 ArbnErfG\n"
          "**V1 Inanspruchnahme vor Eröffnung** – § 27 ArbnErfG Einleitungssatz\n"
          "**V2 Eröffnung des Insolvenzverfahrens über das Vermögen des Arbeitgebers**\n"
          "**V3 Verwertungsart** –\n"
          "Nr. 1: Veräußerung **mit dem Geschäftsbetrieb** → Erwerber tritt ab Eröffnung in die Vergütungspflicht ein, auch wenn das "
          "Arbeitsverhältnis nicht übergeht (Arb.Erf. 51/12, Arb.Erf. 49/16); er kann sich wie der Arbeitgeber nach § 16 ArbnErfG für die "
          "Zukunft befreien (Arb.Erf. 08/12)\n"
          "Nr. 2: Verwertung **im Unternehmen des Schuldners** → angemessene Vergütung aus der Masse\n"
          "Nr. 3: **alle anderen Fälle** → Angebot an den Arbeitnehmer spätestens ein Jahr nach Eröffnung, § 16 ArbnErfG entsprechend; Annahme "
          "binnen zwei Monaten nach Zugang; sonst Veräußerung ohne Geschäftsbetrieb oder Aufgabe; Vergütung durch den Erwerber nur bei "
          "Vereinbarung mit dem Verwalter, sonst aus dem Veräußerungserlös\n"
          "Nr. 4: im Übrigen nur als Insolvenzgläubiger\n\n"
          "**AGL 3: Vergütung beim Verkauf der Erfindung**, § 9 Abs. 1 ArbnErfG i.V.m. RL Nr. 16\n"
          "**V1 Inanspruchnahme** **V2 Verkauf des Schutzrechts** **V3 Erfindungswert = Nettoertrag**: Bruttokaufpreis abzüglich Kosten der "
          "Entwicklung nach Fertigstellung, Betriebsreife, Schutzrechtserlangung und -übertragung, Verkaufskosten, Gemeinkostenanteil und "
          "Know-how-Anteil (RL Nr. 16)\n"
          "**⇒** Schuldner bleibt der Arbeitgeber; der Erfinder wird aus dem Kaufpreis abschließend vergütet, der Erwerber schuldet nichts "
          "(Arb.Erf. 23/21 vom 14.06.2023). Anders beim Betriebsübergang (§ 613a Abs. 1 BGB) und bei Gesamtrechtsnachfolge nach dem "
          "Umwandlungsgesetz (Arb.Erf. 23/21 vom 14.11.2023); beim Share Deal bleibt der Arbeitgeber Schuldner.\n\n"
          "**Vor dem Verkauf: Inhaberschaft prüfen** – Recht auf das Patent je Miterfinder (§ 6 S. 2 PatG): Arbeitnehmer nur nach Inanspruchnahme "
          "(§ 7 Abs. 1 ArbnErfG), Geschäftsführer und freie Mitarbeiter nur durch Vertrag; über das Patent im Ganzen können Mitinhaber nur "
          "gemeinschaftlich verfügen (§ 747 S. 2 BGB) – Stimmenmehrheit genügt nicht.\n\n"
          "**In den Klausuren:** RP2 III/2022 (Frage 5: Verkauf durch den Insolvenzverwalter an FE), RP2 I/2023 (Verkauf zweier Patente für "
          "1,5 Mio. €, Inhaberschaft unklar), RP2 III/2018, RP2 II/2019, RP2 II/2021, RP2 II/2022 (Ansprüche nach dem Ausscheiden).",
          concepts=["arb_verguetungsanspruch", "arb_erfindungswert"],
          norms=["§ 26 ArbnErfG", "§ 27 ArbnErfG", "§ 9 ArbnErfG", "§ 16 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07e-1", "Definitionen",
          "**Auflösung des Arbeitsverhältnisses (§ 26 ArbnErfG):** jede Beendigung (Kündigung, Aufhebung, Ruhestand, Tod).\n"
          "**Veräußerung mit dem Geschäftsbetrieb (§ 27 Nr. 1 ArbnErfG):** der Insolvenzverwalter überträgt die Diensterfindung zusammen mit "
          "dem Betrieb oder Betriebsteil, in dem sie verwertet wird.\n"
          "**Insolvenzgläubiger (§ 27 Nr. 4 ArbnErfG):** Gläubiger, der nur die Quote aus der Masse erhält.\n"
          "**Nettoertrag beim Verkauf (RL Nr. 16):** Bruttoertrag abzüglich der dort genannten Aufwendungen; künftige Belastungen des "
          "Verkäufers sind anders als bei der Lizenz meist nicht zu berücksichtigen.\n"
          "**Betriebsübergang (§ 613a Abs. 1 S. 1 BGB):** Übergang eines Betriebs oder Betriebsteils durch Rechtsgeschäft; der Erwerber tritt in "
          "die Arbeitsverhältnisse ein.\n"
          "**Share Deal / Asset Deal:** Verkauf der Gesellschaftsanteile (Arbeitgeber bleibt derselbe) bzw. Einzelübertragung der "
          "Wirtschaftsgüter (Schiedsstelle Arb.Erf. 20/20).\n"
          "**Verfügung über das Ganze (§ 747 S. 2 BGB):** Übertragung des gemeinschaftlichen Patents; nur durch alle Teilhaber gemeinsam.",
          concepts=["arb_verguetungsanspruch"], norms=["§ 26 ArbnErfG", "§ 27 ArbnErfG"], abschnitt="Definitionen"),
    fall("p07e-2", "Nach dem Ruhestand",
         "Entwicklungsleiter L ging am 31.01.2019 in den Ruhestand. Sein Arbeitgeber verkauft die erfindungsgemäßen Golfschläger weiter "
         "(nach RP2 II/2019).",
         "Schuldet der Arbeitgeber auch für die Umsätze nach dem 31.01.2019 Vergütung?", True,
         ["**Ja!** Die Rechte und Pflichten aus dem ArbnErfG werden durch die Auflösung des Arbeitsverhältnisses nicht berührt (§ 26 ArbnErfG). "
          "Der Anspruch aus § 9 Abs. 1 ArbnErfG besteht fort, solange die Erfindung verwertet wird und das Schutzrecht besteht (RL Nr. 42)."],
         merke="§ 26 ArbnErfG: Ausscheiden lässt Vergütungsansprüche unberührt.", level=1,
         concepts=["arb_verguetungsanspruch"], norms=["§ 26 ArbnErfG", "§ 9 ArbnErfG"], abschnitt=D),
    fall("p07e-3", "Erfindung des Pensionärs",
         "Chemiker P vollendet die Erfindung zwei Monate nach seinem Eintritt in den Ruhestand zu Hause; die Idee hatte er schon im Betrieb.",
         "Ist die Erfindung eine Diensterfindung?", False,
         ["**Nein!** Diensterfindungen sind nur während der Dauer des Arbeitsverhältnisses gemachte Erfindungen (§ 4 Abs. 2 ArbnErfG). Auf "
          "Erfindungen, die ein Pensionär nach dem Ausscheiden macht, ist das ArbnErfG nicht anzuwenden (Schiedsstelle Arb.Erf. 24/06). Anders "
          "nur, wenn er die Fertigstellung treuwidrig hinausgezögert hat."],
         merke="Fertigstellung nach dem Ausscheiden → keine Diensterfindung.", level=2,
         concepts=["arb_diensterfindung"], norms=["§ 4 Abs. 2 ArbnErfG"], abschnitt=D),
    mc("p07e-4", "Verkauf mit dem Betrieb",
       "Wer schuldet die Vergütung für Benutzungen nach der Eröffnung?",
       ["Der Erwerber, ab Eröffnung des Insolvenzverfahrens (§ 27 Nr. 1 ArbnErfG)",
        "Der Insolvenzverwalter aus der Masse (§ 27 Nr. 2 ArbnErfG)",
        "Niemand; der Erfinder ist nur Insolvenzgläubiger (§ 27 Nr. 4 ArbnErfG)",
        "Der Erwerber erst ab dem Tag des Kaufvertrags"], 0,
       ["**§ 27 Nr. 1 ArbnErfG.** Veräußert der Insolvenzverwalter die Diensterfindung mit dem Geschäftsbetrieb, tritt der Erwerber für die "
        "Zeit ab Eröffnung in die Vergütungspflicht ein. Das gilt auch für Erfinder, deren Arbeitsverhältnis nicht übergeht (Schiedsstelle "
        "Arb.Erf. 51/12, Arb.Erf. 49/16). Für die Zeit vor Eröffnung bleibt nur die Insolvenzforderung (§ 27 Nr. 4 ArbnErfG)."],
       sachverhalt="Der Insolvenzverwalter der X GmbH verkauft den Geschäftsbereich samt den Patenten auf die Diensterfindungen von Y an "
                   "die Z AG. Y war schon vorher ausgeschieden.",
       merke="Insolvenz + Verkauf mit Betrieb → Erwerber zahlt ab Eröffnung (§ 27 Nr. 1 ArbnErfG).", level=2,
       concepts=["arb_verguetungsanspruch"], norms=["§ 27 ArbnErfG"], abschnitt=D),
    fall("p07e-5", "Verkauf außerhalb der Insolvenz",
         "Die F GmbH verkauft ein Patent auf eine vergütete Diensterfindung für 750.000 € an den Wettbewerber K. Der Betrieb bleibt bei F; "
         "K produziert künftig selbst (nach RP2 I/2023).",
         "Muss K den Erfindern künftig Vergütung zahlen?", False,
         ["**Nein!** Vergütungsschuldner ist der Arbeitgeber. Beim Verkauf an einen unabhängigen Dritten wird der Schuldner nicht ausgetauscht; "
          "die Erfinder werden aus dem Kaufpreis abschließend vergütet (Schiedsstelle Arb.Erf. 23/21 vom 14.06.2023), Erfindungswert ist der "
          "Nettoertrag (RL Nr. 16). Anders nur bei einem Betriebsübergang nach § 613a Abs. 1 BGB."],
         merke="Patentverkauf: F vergütet aus dem Nettokaufpreis (RL Nr. 16); K schuldet nichts.", level=2,
         concepts=["arb_erfindungswert"], norms=["§ 9 ArbnErfG"], abschnitt=D),
    fall("p07e-6", "Die Umwandlung",
         "Der Geschäftsbereich mit den Patenten des ausgeschiedenen Erfinders E wird nach dem Umwandlungsgesetz auf eine neue Gesellschaft "
         "abgespalten, die die Erfindungen weiter nutzt.",
         "Schuldet die neue Gesellschaft dem E künftig die Vergütung?", True,
         ["**Ja!** Bei Verschmelzung oder Spaltung geht das Vermögen im Wege der Gesamtrechtsnachfolge einschließlich der Verbindlichkeiten über; "
          "dazu gehören die Vergütungsansprüche aus den Diensterfindungen. Der übernehmende Rechtsträger muss E an den Vorteilen künftiger "
          "Verwertung beteiligen (Schiedsstelle Arb.Erf. 23/21 vom 14.11.2023)."],
         merke="Gesamtrechtsnachfolge (Umwandlung) → neuer Rechtsträger vergütet; Einzelverkauf → Arbeitgeber aus Kaufpreis.", level=3,
         concepts=["arb_verguetungsanspruch"], norms=["§ 9 ArbnErfG", "§ 26 ArbnErfG"], abschnitt=D),
    mc("p07e-7", "Die Patentgemeinschaft",
       "Kann F das Patent allein an K verkaufen, weil F „bei Weitem Stimmenmehrheit“ hat?",
       ["Nein, über das Patent im Ganzen können die Teilhaber nur gemeinschaftlich verfügen (§ 747 S. 2 BGB)",
        "Ja, Stimmenmehrheit genügt (§ 745 Abs. 1 BGB)",
        "Ja, wenn F die übrigen Teilhaber nachträglich vergütet",
        "Ja, als eingetragene Inhaberin"], 0,
       ["**Nein.** Steht das Recht mehreren zu, gelten die Regeln der Bruchteilsgemeinschaft (§ 6 S. 2 PatG, § 741 BGB). Mehrheitsbeschlüsse "
        "decken nur Verwaltung und Benutzung (§ 745 Abs. 1 BGB); über das Patent im Ganzen verfügen die Teilhaber nur gemeinschaftlich "
        "(§ 747 S. 2 BGB). F kann nur ihren Anteil verkaufen (§ 747 S. 1 BGB) oder muss die anderen Anteile vorher erwerben."],
       sachverhalt="Vier Miterfinder je 25 %; die F GmbH hat die Anteile von drei Arbeitnehmern erworben, der vierte (früher Geschäftsführer) "
                   "hat seinen Anteil nicht übertragen und ist Mitinhaber (nach RP2 I/2023).",
       merke="Mitinhaber: Nutzung § 743 Abs. 2 BGB · Verwaltung § 745 BGB · Verfügung über das Ganze nur gemeinsam § 747 S. 2 BGB.", level=2,
       concepts=["pat_recht_auf_patent", "arb_miterfinder"], norms=["§ 6 PatG"], abschnitt=D),
    *fallkette("p07e-8", "Mikroplastik in der Insolvenz (nach RP2 III/2022)",
        "Die DD GmbH hat die Diensterfindung ihres Gruppenleiters Dr. Z in Anspruch genommen; Patente in mehreren Ländern sind erteilt. 2022 "
        "wird das Insolvenzverfahren eröffnet. Der Verwalter will nur die Patente an den Meistbietenden verkaufen; die Lizenznehmerin FE GmbH "
        "hat Interesse. Der Betrieb soll nicht mitverkauft werden.",
        [frage("Muss der Verwalter die Patente zuerst Dr. Z anbieten?", True,
               ["**Ja!** Eine Veräußerung ohne Geschäftsbetrieb fällt unter § 27 Nr. 3 ArbnErfG: Der Verwalter muss dem Arbeitnehmer die "
                "Diensterfindung und die Schutzrechtspositionen anbieten; § 16 ArbnErfG gilt entsprechend. Ein Verkauf unter Übergehung des "
                "Erfinders lässt sich nicht rückabwickeln, kann aber den Verwalter haftbar machen (Schiedsstelle Arb.Erf. 08/04, zur a.F.)."],
               merke="Insolvenz ohne Betrieb: erst dem Erfinder anbieten (§ 27 Nr. 3 ArbnErfG).", titel="V3 Nr. 3: Angebot", level=2),
         frage("Welche Fristen gelten für Angebot und Annahme?", 0,
               ["**Ein Jahr, zwei Monate.** Der Verwalter muss spätestens nach Ablauf eines Jahres nach Eröffnung anbieten; nimmt der Arbeitnehmer "
                "nicht binnen zwei Monaten nach Zugang an, darf der Verwalter ohne Geschäftsbetrieb veräußern oder das Recht aufgeben "
                "(§ 27 Nr. 3 S. 1, 2 ArbnErfG). Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB, § 193 BGB."],
               optionen=["Angebot spätestens ein Jahr nach Eröffnung; Annahme binnen zwei Monaten nach Zugang",
                         "Angebot binnen drei Monaten; Annahme binnen drei Monaten",
                         "Angebot unverzüglich; Annahme binnen vier Monaten",
                         "Keine Fristen; der Verwalter darf sofort verkaufen"],
               merke="§ 27 Nr. 3 ArbnErfG: ein Jahr (Angebot) · zwei Monate (Annahme).", titel="Fristen", level=2),
         frage("Schuldet die FE GmbH nach dem Erwerb der Patente Dr. Z Vergütung?", False,
               ["**Nein!** Nur wenn der Verwalter mit ihr vereinbart, dass sie die Vergütung nach § 9 ArbnErfG zahlt (§ 27 Nr. 3 S. 3 ArbnErfG). "
                "Ohne Vereinbarung zahlt der Verwalter dem Arbeitnehmer die Vergütung aus dem Veräußerungserlös (§ 27 Nr. 3 S. 4 ArbnErfG)."],
               merke="Erwerber ohne Betrieb zahlt nur bei Vereinbarung; sonst Vergütung aus dem Erlös.", titel="Rechtsfolge Nr. 3", level=2),
         frage("Wer schuldet dann die Vergütung für die Nutzung ab Eröffnung?", 0,
               ["**Die FE GmbH.** Bei Veräußerung mit dem Geschäftsbetrieb tritt der Erwerber ab Eröffnung in die Vergütungspflicht ein "
                "(§ 27 Nr. 1 ArbnErfG); ein Angebot an Dr. Z ist nicht nötig."],
               optionen=["Die FE GmbH ab Eröffnung des Insolvenzverfahrens", "Der Verwalter aus der Masse", "Niemand",
                         "Die FE GmbH ab Abschluss des Kaufvertrags"],
               merke="Mit Betrieb verkauft → Erwerber tritt ein (§ 27 Nr. 1 ArbnErfG).", titel="V3 Nr. 1",
               abwandlung="Die FE GmbH übernimmt den gesamten Geschäftsbetrieb der DD GmbH samt Patenten.", level=2),
         ],
        abschnitt=K, level=2, concepts=["arb_verguetungsanspruch", "arb_aufgabe_schutzrecht"], norms=["§ 27 ArbnErfG"]),
    *fallkette("p07e-9", "1,5 Mio. € für zwei Patente (nach RP2 I/2023)",
        "Die F GmbH will ihr Patent A, das sie nicht mehr nutzt, für 750.000 € an den Wettbewerber K verkaufen. Erfinder sind vier Personen zu "
        "je 25 %: A1 war damals Geschäftsführer, A2 und A3 Entwickler, A4 ist 2010 ausgeschieden.",
        [frage("Hat A1 einen Vergütungsanspruch nach § 9 ArbnErfG?", False,
               ["**Nein!** Geschäftsführer einer GmbH repräsentieren den Arbeitgeber; sie haben für ihre Erfindungen keine Vergütungsansprüche "
                "nach dem ArbnErfG (Schiedsstelle Arb.Erf. 58/16). Sein Anteil geht nur durch Vertrag auf die GmbH über, hier durch seine "
                "Erklärung, sein Anteil gehöre der F GmbH."],
               merke="Organ ist kein Arbeitnehmer: Übertragung und Vergütung nur nach Vertrag.", titel="V1 Arbeitnehmer?", level=2),
         frage("Wie hoch ist die Vergütung des A3, wenn vom Kaufpreis 600.000 € Nettoertrag bleiben und sein Anteilsfaktor 15 % beträgt?", 0,
               ["**22.500 €.** Erfindungswert beim Verkauf ist der Nettoertrag (RL Nr. 16). V = E × A × Anteil (RL Nr. 39): "
                "600.000 € × 15 % × 25 % = 22.500 €."],
               optionen=["22.500 €", "90.000 €", "28.125 €", "150.000 €"],
               merke="Verkauf: V = Nettoertrag (RL Nr. 16) × A × Miterfinderanteil.", titel="V3 Erfindungswert beim Verkauf", level=2),
         frage("Muss A4 vor einer Klage auf seine Vergütung aus dem Verkauf die Schiedsstelle anrufen?", False,
               ["**Nein!** Ist der Arbeitnehmer aus dem Betrieb ausgeschieden, ist das Schiedsverfahren keine Klagevoraussetzung "
                "(§ 37 Abs. 2 Nr. 3 ArbnErfG). Zuständig ist die Patentstreitkammer (§ 39 Abs. 1 S. 1 ArbnErfG); er kann auf einen vom Gericht "
                "zu bestimmenden angemessenen Betrag klagen (§ 38 ArbnErfG)."],
               merke="Ausgeschieden → direkt zur Patentstreitkammer (§ 37 Abs. 2 Nr. 3 ArbnErfG).", titel="Durchsetzung", level=1),
         ],
        abschnitt=K, level=2, concepts=["arb_erfindungswert", "arb_verguetungsanspruch"], norms=["§ 9 ArbnErfG", "§ 37 ArbnErfG"]),
])

# ====================================================================== p07f Schiedsstelle und Klage
P07F = dict(id="p07f", titel="§§ 28 bis 39 ArbnErfG: Schiedsstelle und Klage", einheiten=[
    intro("p07f-0", "Prüfungsschema",
          "**Rechtsbehelf 1: Anrufung der Schiedsstelle**, § 28 S. 1 ArbnErfG\n"
          "**A · Zulässigkeit**\n"
          "**V1 Streitfall zwischen Arbeitgeber und Arbeitnehmer auf Grund des ArbnErfG** – § 28 S. 1 ArbnErfG; auch nach dem Ausscheiden "
          "(§ 26 ArbnErfG), auch zwischen Leiharbeitnehmer und Entleiher (Schiedsstelle Arb.Erf. 51/07). Nicht: streitige (Mit-)Erfinderschaft "
          "(Arb.Erf. 45/11), Nennung nach § 63 PatG, Streit mit dem Geschäftsführer persönlich\n"
          "**V2 Schriftlicher Antrag** – § 31 Abs. 1 S. 1 ArbnErfG; soll in zwei Stücken mit kurzer Sachverhaltsdarstellung, Name und Anschrift "
          "des Gegners eingereicht werden (§ 31 Abs. 1 S. 2, 3 ArbnErfG); ein bezifferter Betrag ist nicht nötig (Arb.Erf. 21/09)\n"
          "**V3 Zuständige Stelle** – Schiedsstelle beim DPMA (§ 29 Abs. 1 ArbnErfG); eigene Schiedsstellen öffentlicher Verwaltungen "
          "(§ 40 Nr. 5 ArbnErfG)\n\n"
          "**B · Besetzung und Verfahren**\n"
          "**V4 Besetzung** – Vorsitzender oder Vertreter mit Befähigung zum Richteramt und zwei Beisitzer aus dem DPMA mit Erfahrung auf dem "
          "Gebiet der Technik (§ 30 Abs. 1 bis 3 ArbnErfG); auf Antrag erweitert um je einen Beisitzer aus Arbeitgeber- und Arbeitnehmerkreisen "
          "(§ 30 Abs. 4 ArbnErfG): Antragsteller zugleich mit der Anrufung, Gegner binnen zwei Wochen nach Zustellung (§ 32 ArbnErfG)\n"
          "**V5 Verfahren** – Zustellung an den Gegner mit Äußerungsfrist (§ 31 Abs. 2 ArbnErfG); § 41 ZPO bis § 48 ZPO (Ausschluss und "
          "Ablehnung) sinngemäß; Patentanwälte dürfen nicht zurückgewiesen werden (§ 33 Abs. 1 ArbnErfG); im Übrigen bestimmt die Schiedsstelle "
          "das Verfahren selbst (§ 33 Abs. 2 ArbnErfG); Beschlüsse mit Stimmenmehrheit (§ 34 Abs. 1 ArbnErfG)\n"
          "**C · Ergebnis**\n"
          "**V6 Einigungsvorschlag** – begründet, von allen Mitgliedern unterschrieben, mit Belehrung, zugestellt (§ 34 Abs. 2 ArbnErfG); gilt als "
          "angenommen, wenn nicht binnen eines Monats nach Zustellung ein schriftlicher Widerspruch bei der Schiedsstelle eingeht (§ 34 Abs. 3 "
          "ArbnErfG); Wiedereinsetzung bei unabwendbarem Zufall binnen eines Monats nach Wegfall des Hindernisses, ausgeschlossen ein Jahr nach "
          "Zustellung (§ 34 Abs. 4 ArbnErfG)\n"
          "**V7 Erfolglose Beendigung** – keine Äußerung, Ablehnung der Einlassung, Widerspruch (§ 35 Abs. 1 Nr. 1 bis 3 ArbnErfG)\n"
          "**Kosten:** keine Gebühren und Auslagen (§ 36 ArbnErfG); eine Kostenerstattung sieht das Gesetz nicht vor. **Verjährung:** gehemmt "
          "entsprechend § 204 Abs. 1 Nr. 4 BGB (BGH Profilstrangpressverfahren).\n\n"
          "**Rechtsbehelf 2: Klage**\n"
          "**V1 Zuständigkeit** – Patentstreitkammern der Landgerichte, streitwertunabhängig und ausschließlich (§ 39 Abs. 1 S. 1 ArbnErfG, "
          "§ 143 Abs. 1 PatG); Verfahrensrecht der Patentstreitsachen (§ 39 Abs. 1 S. 2 ArbnErfG). Ausnahme: Klage nur auf Zahlung einer "
          "festgestellten oder festgesetzten Vergütung (§ 39 Abs. 2 ArbnErfG) → allgemeine Zuständigkeit (Arbeitsgericht)\n"
          "**V2 Schiedsverfahren vorausgegangen** – für Rechte, die im ArbnErfG geregelt sind (§ 37 Abs. 1 ArbnErfG); entbehrlich bei Klage aus "
          "einer Vereinbarung nach § 12 ArbnErfG, § 19 ArbnErfG, § 22 ArbnErfG, § 34 ArbnErfG oder gegen deren Wirksamkeit (§ 37 Abs. 2 Nr. 1 "
          "ArbnErfG), sechs Monate nach Anrufung (Nr. 2), nach Ausscheiden (Nr. 3), bei schriftlichem Verzicht nach Eintritt des Streitfalls "
          "(Nr. 4), bei rügeloser Verhandlung zur Hauptsache (§ 37 Abs. 3 ArbnErfG), für Arrest und einstweilige Verfügung (§ 37 Abs. 4 ArbnErfG)\n"
          "**V3 Antrag** – auf Zahlung eines vom Gericht zu bestimmenden angemessenen Betrags (§ 38 ArbnErfG); Streitwert nach Schätzung "
          "(BGH antimykotischer Nagellack II); Stufenklage mit Auskunft (§ 242 BGB)\n\n"
          "**In den Klausuren:** RP2 I/2020 (Frage I: Zuständigkeit, Besetzung, Kosten, Verfahren; Verweis auf die Schiedsstelle im "
          "Erfinderstreit), RP2 II/2022 (kostengünstiger Weg; Verzicht auf die Schiedsstelle, Verweisung vom VG ans LG), RP2 II/2018 (Klage "
          "sofort?), RP2 III/2018, RP2 II/2019, RP2 II/2021 (Wie und wo geltend machen?).",
          concepts=["arb_schiedsstelle"], norms=["§ 28 ArbnErfG", "§ 30 ArbnErfG", "§ 34 ArbnErfG", "§ 36 ArbnErfG", "§ 37 ArbnErfG",
                                                "§ 39 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07f-1", "Definitionen",
          "**Streitfall (§ 28 S. 1 ArbnErfG):** Meinungsverschiedenheit zwischen Arbeitgeber und Arbeitnehmer über Rechte und Pflichten aus dem "
          "ArbnErfG; ein berechtigtes Interesse besteht, solange es keine verbindliche Regelung gibt (Schiedsstelle Arb.Erf. 09/10).\n"
          "**Einigungsvorschlag (§ 34 Abs. 2 ArbnErfG):** begründeter Vorschlag zur gütlichen Einigung; wird er nicht fristgerecht widersprochen, "
          "gilt eine entsprechende Vereinbarung als zustande gekommen (§ 34 Abs. 3 ArbnErfG). Er bindet nur die Beteiligten, nicht andere "
          "Miterfinder (Arb.Erf. 03/09).\n"
          "**Schriftlich (§ 31 Abs. 1 ArbnErfG, § 34 Abs. 3 ArbnErfG):** eigenhändig unterschrieben (§ 126 Abs. 1 BGB).\n"
          "**Unabwendbarer Zufall (§ 34 Abs. 4 ArbnErfG):** Ereignis, das auch mit äußerster zumutbarer Sorgfalt nicht abzuwenden war.\n"
          "**Patentstreitsache (§ 143 Abs. 1 PatG):** Klage, mit der ein Anspruch aus einem im PatG geregelten Rechtsverhältnis geltend gemacht "
          "wird; für Arbeitnehmererfindungen erweitert durch § 39 Abs. 1 ArbnErfG auf alle Rechtsstreitigkeiten über Erfindungen eines "
          "Arbeitnehmers.\n"
          "**Ausgeschieden (§ 37 Abs. 2 Nr. 3 ArbnErfG):** das Arbeitsverhältnis ist beendet; ein Wechsel in eine Organstellung steht dem für "
          "§ 23 ArbnErfG gleich (Arb.Erf. 04/19).",
          concepts=["arb_schiedsstelle"], norms=["§ 28 ArbnErfG", "§ 34 ArbnErfG", "§ 37 ArbnErfG", "§ 39 ArbnErfG"], abschnitt="Definitionen"),
    mc("p07f-2", "Besetzung der Schiedsstelle",
       "Wie ist die Schiedsstelle im Regelfall besetzt?",
       ["Vorsitzender mit Befähigung zum Richteramt und zwei Beisitzer aus dem DPMA",
        "Drei Richter des BPatG",
        "Ein Prüfer des DPMA als Einzelentscheider",
        "Je ein Vertreter von Arbeitgeber- und Arbeitnehmerverbänden und ein Vorsitzender"], 0,
       ["**§ 30 Abs. 1 bis 3 ArbnErfG.** Der Vorsitzende soll die Befähigung zum Richteramt haben und wird für vier Jahre berufen; die zwei "
        "Beisitzer sind Mitglieder des DPMA mit Erfahrung auf dem technischen Gebiet. Verbandsbeisitzer kommen nur auf Antrag hinzu "
        "(§ 30 Abs. 4 ArbnErfG, Antrag nach § 32 ArbnErfG)."],
       merke="1 Vorsitzender + 2 DPMA-Beisitzer; erweitert auf Antrag um 2 Verbandsbeisitzer (§ 30 ArbnErfG).", level=1,
       concepts=["arb_schiedsstelle"], norms=["§ 30 ArbnErfG", "§ 32 ArbnErfG"], abschnitt=D),
    mc("p07f-3", "Widerspruch gegen den Einigungsvorschlag",
       "Wie und bis wann muss der Arbeitgeber widersprechen, um eine Bindung zu verhindern?",
       ["Schriftlich bei der Schiedsstelle, Eingang binnen eines Monats nach Zustellung",
        "In Textform gegenüber dem Arbeitnehmer binnen zwei Monaten",
        "Mündlich in der Verhandlung",
        "Durch Klage binnen drei Monaten"], 0,
       ["**§ 34 Abs. 3 ArbnErfG.** Der Vorschlag gilt als angenommen, wenn nicht binnen eines Monats nach Zustellung ein schriftlicher "
        "Widerspruch bei der Schiedsstelle eingeht. Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB, § 193 BGB. Nach Widerspruch ist das "
        "Verfahren erfolglos beendet (§ 35 Abs. 1 Nr. 3 ArbnErfG); dann ist die Klage zulässig (§ 37 Abs. 1 ArbnErfG)."],
       sachverhalt="Der Einigungsvorschlag der Schiedsstelle wird beiden Beteiligten am Mo 03.03. zugestellt. Der Arbeitgeber hält ihn für "
                   "zu teuer (nach RP2 I/2020).",
       merke="Widerspruch: schriftlich · bei der Schiedsstelle · ein Monat ab Zustellung (§ 34 Abs. 3 ArbnErfG).", level=1,
       concepts=["arb_schiedsstelle"], norms=["§ 34 ArbnErfG", "§ 35 ArbnErfG"], abschnitt=D),
    fall("p07f-4", "Streit um die Miterfinderschaft",
         "Dr. P, inzwischen bei einem Wettbewerber, meint, sie sei Miterfinderin der Flinte ihres früheren Arbeitgebers. Dieser bestreitet "
         "jeden schöpferischen Beitrag. P ruft die Schiedsstelle an (nach RP2 I/2020).",
         "Ist die Schiedsstelle für die Klärung der Miterfinderschaft zuständig?", False,
         ["**Nein!** Für Fragen streitiger Miterfinderschaft ist die Schiedsstelle sachlich unzuständig und stellt das Verfahren ein "
          "(Schiedsstelle Arb.Erf. 45/11). Die Erfinderschaft ergibt sich aus dem PatG (§ 6 PatG, § 63 PatG), nicht aus dem ArbnErfG. P muss vor "
          "der Patentstreitkammer klagen (§ 143 Abs. 1 PatG); ein Schiedsverfahren ist dafür nicht Voraussetzung (§ 37 Abs. 1 ArbnErfG)."],
         merke="Erfinderschaft streitig → Landgericht, nicht Schiedsstelle (Arb.Erf. 45/11).", level=2,
         concepts=["arb_schiedsstelle", "arb_miterfinder"], norms=["§ 28 ArbnErfG", "§ 63 PatG"], abschnitt=D),
    fall("p07f-5", "Sofort klagen?",
         "Entwicklungsleiter Z, noch ein Jahr bis zur Rente im Betrieb, will seine Vergütung für eine in Anspruch genommene Diensterfindung "
         "sofort einklagen. Eine Vereinbarung gibt es nicht (nach RP2 II/2018).",
         "Ist die Klage ohne vorheriges Schiedsverfahren zulässig?", False,
         ["**Nein!** Rechte aus dem ArbnErfG können erst nach einem Verfahren vor der Schiedsstelle eingeklagt werden (§ 37 Abs. 1 ArbnErfG). "
          "Keine Ausnahme greift: Z ist nicht ausgeschieden (§ 37 Abs. 2 Nr. 3 ArbnErfG), stützt sich auf keine Vereinbarung (Nr. 1), und ein "
          "Verzicht fehlt (Nr. 4). Rügt der Arbeitgeber nicht und verhandelt zur Hauptsache, wird der Mangel geheilt (§ 37 Abs. 3 ArbnErfG)."],
         merke="Klage über ArbnErfG-Rechte erst nach Schiedsverfahren (§ 37 Abs. 1 ArbnErfG); Ausnahmen § 37 Abs. 2 ArbnErfG.", level=1,
         concepts=["arb_schiedsstelle"], norms=["§ 37 ArbnErfG"], abschnitt=D),
    mc("p07f-6", "Zuständiges Gericht",
       "Vor welchem Gericht klagt der ausgeschiedene Erfinder auf angemessene Vergütung?",
       ["Ausschließlich vor der Patentstreitkammer des Landgerichts, ohne Rücksicht auf den Streitwert",
        "Vor dem Arbeitsgericht",
        "Vor dem Amtsgericht, weil der Streitwert unter 5.000 € liegt",
        "Vor dem Bundespatentgericht"], 0,
       ["**§ 39 Abs. 1 S. 1 ArbnErfG.** Für alle Rechtsstreitigkeiten über Erfindungen eines Arbeitnehmers sind die Patentstreitgerichte nach "
        "§ 143 PatG ausschließlich zuständig. Nur reine Zahlungsklagen aus einer festgestellten oder festgesetzten Vergütung sind ausgenommen "
        "(§ 39 Abs. 2 ArbnErfG). Der Antrag kann unbeziffert sein (§ 38 ArbnErfG)."],
       sachverhalt="Der ausgeschiedene Erfinder F hält seine Pauschale von 2.000 € für viel zu niedrig und verlangt eine angemessene Vergütung; "
                   "der Streitwert liegt bei 4.000 € (nach RP2 II/2021).",
       merke="Erfinderstreit → Patentstreitkammer, streitwertunabhängig (§ 39 Abs. 1 ArbnErfG).", level=1,
       concepts=["arb_schiedsstelle"], norms=["§ 39 ArbnErfG", "§ 143 PatG"], abschnitt=D),
    fall("p07f-7", "Nur noch zahlen",
         "Arbeitgeber und Erfinder haben die Vergütung auf 13.000 € festgestellt; der Arbeitgeber zahlt nicht. Der Erfinder klagt nur auf "
         "Zahlung dieses Betrags.",
         "Ist die Patentstreitkammer ausschließlich zuständig?", False,
         ["**Nein!** Ausgenommen sind Rechtsstreitigkeiten, die ausschließlich Ansprüche auf Leistung einer festgestellten oder festgesetzten "
          "Vergütung betreffen (§ 39 Abs. 2 ArbnErfG). Es geht nicht mehr um die Erfindung, nur um Zahlung; zuständig ist das Arbeitsgericht. "
          "Ein Schiedsverfahren ist entbehrlich, weil Rechte aus einer Vereinbarung geltend gemacht werden (§ 37 Abs. 2 Nr. 1 ArbnErfG)."],
         merke="Nur Zahlung festgestellter Vergütung → nicht Patentstreitkammer (§ 39 Abs. 2 ArbnErfG).", level=2,
         concepts=["arb_festsetzung"], norms=["§ 39 ArbnErfG", "§ 37 ArbnErfG"], abschnitt=D),
    *fallkette("p07f-8", "Der Chef als Miterfinder (nach RP2 I/2020)",
        "Entwicklungsleiter B meldet eine Erfindung (hohler Flintenschaft) als Alleinerfinder. Geschäftsführer F lässt sich und B als "
        "Erfinder benennen, weil er die Aufgabe gestellt habe. B verlangt Berichtigung; F meint, B könne sich ja an die Schiedsstelle wenden.",
        [frage("Ist die Schiedsstelle für das Berichtigungsverlangen zuständig?", False,
               ["**Nein!** Der Anspruch auf Berichtigung folgt aus § 63 Abs. 2 S. 1 PatG, nicht aus dem ArbnErfG; über streitige "
                "Erfinderschaft entscheidet die Schiedsstelle nicht (Arb.Erf. 45/11). Gegen F persönlich besteht ohnehin kein Streit zwischen "
                "Arbeitgeber und Arbeitnehmer (§ 28 S. 1 ArbnErfG)."],
               merke="§ 63 PatG-Streit ist kein Schiedsstellenfall.", titel="V1 Streitfall nach dem ArbnErfG", level=2),
         frage("Wo klagt B, und muss er vorher ein Schiedsverfahren durchführen?", 0,
               ["**Patentstreitkammer, ohne Schiedsverfahren.** Zuständig ist ausschließlich das Landgericht (§ 143 Abs. 1 PatG, "
                "§ 39 Abs. 1 S. 1 ArbnErfG). § 37 Abs. 1 ArbnErfG erfasst nur im ArbnErfG geregelte Rechte."],
               optionen=["Vor der Patentstreitkammer des Landgerichts, ohne Schiedsverfahren",
                         "Vor dem Arbeitsgericht nach einem Schiedsverfahren",
                         "Vor dem DPMA im Berichtigungsverfahren",
                         "Vor dem BPatG"],
               merke="Nennung: LG Patentstreitkammer, keine Schiedsstelle (§ 143 Abs. 1 PatG, § 37 Abs. 1 ArbnErfG).", titel="Klage", level=2),
         frage("Muss B dann vor der Klage die Schiedsstelle anrufen?", True,
               ["**Ja!** Die Vergütung ist ein im ArbnErfG geregeltes Recht (§ 9 ArbnErfG); B ist noch beschäftigt, eine Ausnahme nach "
                "§ 37 Abs. 2 ArbnErfG liegt nicht vor (§ 37 Abs. 1 ArbnErfG). Das Verfahren ist kostenfrei (§ 36 ArbnErfG)."],
               merke="Vergütungsstreit im laufenden Arbeitsverhältnis → erst Schiedsstelle.", titel="V2 Vorverfahren",
               abwandlung="B streitet mit der GmbH nur noch über die Höhe seiner Vergütung; er ist weiter beschäftigt.", level=1),
         frage("Ist ein Widerspruch per einfacher E-Mail gegen den Einigungsvorschlag wirksam?", False,
               ["**Nein!** § 34 Abs. 3 ArbnErfG verlangt einen schriftlichen Widerspruch, also eigenhändig unterschrieben (§ 126 Abs. 1 BGB). "
                "Eine einfache E-Mail wahrt nur die Textform (§ 126b BGB). Ohne formgerechten Widerspruch binnen eines Monats gilt der Vorschlag "
                "als angenommen."],
               merke="Widerspruch § 34 Abs. 3 ArbnErfG: Schriftform, nicht Textform.", titel="V6 Widerspruch", level=2),
         ],
        abschnitt=K, level=2, concepts=["arb_schiedsstelle"], norms=["§ 28 ArbnErfG", "§ 37 ArbnErfG"]),
    *fallkette("p07f-9", "Kostengünstig zur Nachvergütung (nach RP2 II/2022)",
        "G schied Ende 2011 aus. Nach einem Schiedsverfahren vereinbarte er 2013 eine „abschließende“ Vergütung von 13.000 € für die Nutzung "
        "bis Ende 2012; „für eine eventuelle weitere Nutzung entsteht ein gesonderter Anspruch“. Im November 2021 erfährt er, dass der "
        "Arbeitgeber die Erfindung bis Ende 2014 nutzte. G will kostengünstig vorgehen (Bearbeitung 2022).",
        [frage("Darf G trotz seines Ausscheidens die Schiedsstelle anrufen?", True,
               ["**Ja!** Die Schiedsstelle kann in allen Streitfällen aufgrund des ArbnErfG jederzeit angerufen werden (§ 28 S. 1 ArbnErfG); "
                "das Ausscheiden lässt die Rechte unberührt (§ 26 ArbnErfG). Das Verfahren ist gebührenfrei (§ 36 ArbnErfG) und hemmt die "
                "Verjährung (BGH Profilstrangpressverfahren)."],
               merke="Schiedsstelle: jederzeit, kostenfrei, hemmt die Verjährung.", titel="V1 Zulässigkeit", level=1),
         frage("Darf G stattdessen sofort klagen?", True,
               ["**Ja!** Er ist ausgeschieden (§ 37 Abs. 2 Nr. 3 ArbnErfG) und stützt sich auf die Vereinbarung (§ 37 Abs. 2 Nr. 1 ArbnErfG). "
                "Zuständig ist die Patentstreitkammer (§ 39 Abs. 1 S. 1 ArbnErfG); der Antrag kann auf einen angemessenen Betrag gehen "
                "(§ 38 ArbnErfG), verbunden mit Auskunft (§ 242 BGB)."],
               merke="Ausgeschieden oder Vereinbarung → Klage ohne Schiedsverfahren.", titel="Klage", level=1),
         frage("Muss G seinen Anspruch im Antrag an die Schiedsstelle beziffern?", False,
               ["**Nein!** Der Antrag muss schriftlich sein und soll den Sachverhalt und den Gegner nennen (§ 31 Abs. 1 ArbnErfG); einen "
                "bezifferten Betrag verlangt die Anrufung nicht (Schiedsstelle Arb.Erf. 21/09)."],
               merke="Anrufung: schriftlich, Sachverhalt, Gegner – keine Bezifferung (§ 31 Abs. 1 ArbnErfG).", titel="V2 Antrag", level=1),
         frage("Ist der Anspruch für die Nutzung 2013 und 2014 verjährt?", False,
               ["**Nein!** Die Frist von drei Jahren (§ 195 BGB) beginnt erst mit dem Schluss des Jahres, in dem G von den anspruchsbegründenden "
                "Umständen Kenntnis erlangte (§ 199 Abs. 1 Nr. 2 BGB), also Ende 2021; die Höchstfrist von zehn Jahren ab Entstehung "
                "(§ 199 Abs. 4 BGB) ist 2022 noch nicht abgelaufen."],
               merke="Verjährung: § 195 BGB, Beginn § 199 Abs. 1 BGB, Höchstfrist § 199 Abs. 4 BGB.", titel="Einrede der Verjährung", level=3),
         ],
        abschnitt=K, level=2, concepts=["arb_schiedsstelle", "arb_verguetungsanspruch"], norms=["§ 28 ArbnErfG", "§ 37 ArbnErfG", "§ 39 ArbnErfG"]),
])

# ====================================================================== p07g PatG im Arbeitsverhältnis
P07G = dict(id="p07g", titel="§§ 6, 8, 63 PatG im Arbeitsverhältnis: Erfinderschaft, Vindikation, Erfindernennung", einheiten=[
    intro("p07g-0", "Prüfungsschema",
          "**AGL 1: Zustimmung zur Berichtigung der Erfindernennung**, § 63 Abs. 2 S. 1 PatG\n"
          "**A · Anspruchsvoraussetzungen**\n"
          "**V1 Nennung unrichtig oder unterblieben** – § 63 Abs. 2 S. 1 PatG, § 63 Abs. 1 S. 1 PatG; Erfinder ist, wer einen schöpferischen "
          "Beitrag zum geschützten Gegenstand geleistet hat; „versehentlich“ ist unerheblich\n"
          "**V2 Anspruchsteller ist Erfinder der patentierten Erfindung** – schöpferischer Beitrag zum Gegenstand der unter Schutz gestellten "
          "Erfindung, gesamte Erfindung einschließlich ihres Zustandekommens; Schutzfähigkeit unerheblich (BGH Atemgasdrucksteuerung, "
          "X ZR 53/08)\n"
          "**V2.1** Er hat die Lehre gemacht (§ 6 S. 1 PatG) · **V2.2** das Patent beruht auf seinem Beitrag, nicht auf einer unabhängigen "
          "Doppelerfindung (§ 6 S. 3 PatG: Recht des Erstanmelders; kennt der Anmelder die Erfindung des Anspruchstellers, muss er die "
          "Doppelerfindung eingehend substantiieren, BGH Schleppfahrzeug, X ZR 227/99) · **V2.3** das Recht des Anmelders stammt von ihm "
          "(§ 37 Abs. 1 S. 2 PatG; beim Arbeitgeber durch Inanspruchnahme, § 7 Abs. 1 ArbnErfG)\n"
          "**V3 Anspruchsgegner** – Patentsucher oder Patentinhaber **und** der zu Unrecht Benannte (§ 63 Abs. 2 S. 1 PatG)\n"
          "**B · Durchsetzung** – Patentstreitkammer (§ 143 Abs. 1 PatG, § 39 Abs. 1 S. 1 ArbnErfG), keine Schiedsstelle (§ 37 Abs. 1 ArbnErfG; "
          "Arb.Erf. 45/11); Zustimmung unwiderruflich (§ 63 Abs. 2 S. 2 PatG); Klage hält die Erteilung nicht auf (§ 63 Abs. 2 S. 3 PatG); "
          "veröffentlichte Druckschriften werden nicht berichtigt (§ 63 Abs. 3 PatG), wohl aber das Register (§ 63 Abs. 1 S. 2 PatG)\n"
          "**⇒** Zustimmung gegenüber dem DPMA zur Berichtigung oder Nachholung der Nennung.\n\n"
          "**AGL 2: Übertragung des Patents (Vindikation)**, § 8 S. 2 PatG (vor Erteilung: Abtretung des Erteilungsanspruchs, § 8 S. 1 PatG)\n"
          "**V1 Anspruchsteller ist Berechtigter** – Erfinder oder Rechtsnachfolger (§ 6 S. 1 PatG); Arbeitgeber durch Inanspruchnahme "
          "(§ 7 Abs. 1 ArbnErfG), Arbeitnehmer bei frei gewordener Erfindung (§ 8 S. 1 ArbnErfG, § 13 Abs. 4 ArbnErfG)\n"
          "**V2 Anmeldung durch einen Nichtberechtigten** – § 8 S. 1 PatG; Verfügungen des Arbeitnehmers vor der Inanspruchnahme sind dem "
          "Arbeitgeber gegenüber unwirksam (§ 7 Abs. 2 ArbnErfG); Geheimhaltungspflicht (§ 24 Abs. 2 ArbnErfG)\n"
          "**V3 Identität** – Gegenstand des Patents ist die Erfindung des Berechtigten; Patentfähigkeit unerheblich (BGH Schleppfahrzeug)\n"
          "**V4 Klagefrist** – zwei Jahre nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG, § 58 Abs. 1 PatG); nach Einspruch wegen "
          "widerrechtlicher Entnahme ein Jahr nach dessen rechtskräftigem Abschluss (§ 8 S. 4 PatG); keine Frist bei Bösgläubigkeit des "
          "Inhabers beim Erwerb (§ 8 S. 5 PatG). Berechnung § 187 Abs. 1 BGB, § 188 Abs. 2 BGB, Verschiebung § 193 BGB\n"
          "**B · Einwendungen** – Verwirkung (§ 242 BGB: Zeit- und Umstandsmoment)\n"
          "**⇒** Übertragung des Patents; bei Miterfinderschaft Einräumung einer Mitberechtigung (§ 6 S. 2 PatG).\n\n"
          "**Mitberechtigung:** Bruchteilsgemeinschaft (§ 741 BGB): eigener Gebrauch (§ 743 Abs. 2 BGB), Verwaltung durch Mehrheit (§ 745 Abs. 1 "
          "BGB; Lizenz an Dritte nur, wenn die übrigen Teilhaber auf ihren Anteil an den Nutzungen zugreifen können, BGH Penetrometer, "
          "X ZR 142/18), Verfügung über das Ganze nur gemeinsam (§ 747 S. 2 BGB). **Europäisches Patent:** Art. II § 5 Abs. 1 IntPatÜG, Frist "
          "zwei Jahre nach Hinweis auf die Erteilung im Europäischen Patentblatt (Art. II § 5 Abs. 2 IntPatÜG). **Alternative:** Einspruch "
          "wegen widerrechtlicher Entnahme (§ 21 Abs. 1 Nr. 3 PatG, § 59 Abs. 1 S. 1 PatG: nur der Verletzte, neun Monate) und Nachanmeldung "
          "binnen eines Monats (§ 7 Abs. 2 PatG).\n\n"
          "**In den Klausuren:** RP2 I/2019 (Nennung bei Doppelerfindung; Vindikation nach später Inanspruchnahme), RP2 III/2023 (P1 trotz "
          "Inanspruchnahme selbst angemeldet, P2 nie gemeldet; Kind als Miterfinder?), RP2 I/2020 (Chef als Erfinder, Beitrag der früheren "
          "Mitarbeiterin), RP2 III/2018 (Kollegen statt des Erfinders benannt), RP2 II/2020 (Lebensgefährtin als Miterfinderin, Abteilungsleiter "
          "ohne Beitrag benannt), RP2 III/2019 (Doppelerfindung ALPHA), RP2 III/2022 (Laborant, Geschäftsführer), RP2 III/2021 (Nutzungsrecht "
          "eines Miterfinders).",
          concepts=["pat_erfinderbenennung", "pat_recht_auf_patent", "arb_miterfinder"],
          norms=["§ 6 PatG", "§ 8 PatG", "§ 63 PatG", "§ 37 PatG", "§ 7 ArbnErfG"], abschnitt="Normenkette"),
    intro("p07g-1", "Definitionen",
          "**Erfinder / berechtigt nach § 63 PatG und § 8 PatG:** wer einen schöpferischen Beitrag zum Gegenstand der unter Schutz gestellten "
          "Erfindung geleistet hat; zu betrachten ist die gesamte Erfindung einschließlich ihres Zustandekommens, die Ansprüche nur insoweit, "
          "als sie Teile der Beschreibung vom Schutz ausnehmen (BGH Atemgasdrucksteuerung, X ZR 53/08).\n"
          "**Miterfinder:** wer einen eigenen, bestimmbaren schöpferischen Beitrag geleistet hat, der für sich nicht patentfähig, aber für die "
          "Lösung wesentlich sein muss (Schiedsstelle Arb.Erf. 46/20). Nicht: bloße Anregung, Aufgabenstellung ohne Lösungsweg, rein "
          "handwerkliche Mitarbeit nach Weisung.\n"
          "**Doppelerfindung:** mehrere haben die Erfindung unabhängig voneinander gemacht; das Recht steht dem zu, der zuerst beim DPMA "
          "angemeldet hat (§ 6 S. 3 PatG).\n"
          "**Nichtberechtigter (§ 8 S. 1 PatG):** Anmelder, dem das Recht auf das Patent nicht zusteht.\n"
          "**Widerrechtliche Entnahme:** der wesentliche Inhalt des Patents ist den Beschreibungen, Zeichnungen, Modellen, Gerätschaften oder "
          "Einrichtungen eines anderen oder einem von diesem angewendeten Verfahren ohne dessen Einwilligung entnommen (Legaldefinition "
          "§ 21 Abs. 1 Nr. 3 PatG).\n"
          "**Nicht in gutem Glauben (§ 8 S. 5 PatG):** der Inhaber wusste beim Erwerb, dass ihm das Recht nicht zusteht, oder verschloss sich "
          "dieser Kenntnis.\n"
          "**Zu Unrecht Benannter (§ 63 Abs. 2 S. 1 PatG):** wer als Erfinder genannt ist, ohne einen schöpferischen Beitrag geleistet zu haben.",
          concepts=["pat_erfinderbenennung", "pat_recht_auf_patent", "arb_miterfinder"], norms=["§ 6 PatG", "§ 8 PatG", "§ 21 PatG", "§ 63 PatG"],
          abschnitt="Definitionen"),
    fall("p07g-2", "Der Laborant",
         "Leiharbeiter A führte im Labor der DD GmbH alle Versuche zum neuen Mikroorganismus streng nach Anweisung des Gruppenleiters Dr. Z "
         "durch. In der Anmeldung ist er mit 20 % als Miterfinder benannt (nach RP2 III/2022).",
         "Ist A Miterfinder?", False,
         ["**Nein!** Miterfinder ist nur, wer einen eigenen schöpferischen Beitrag zur Lösung leistet, der für diese wesentlich ist "
          "(Schiedsstelle Arb.Erf. 46/20). Weisungsgebundene, rein handwerkliche Versuchsdurchführung genügt nicht. Die Benennung durch den "
          "Arbeitgeber ist nur ein Indiz (BGH Haftetikett)."],
         merke="Ausführen nach Anweisung ist kein schöpferischer Beitrag.", level=1,
         concepts=["arb_miterfinder"], norms=["§ 6 PatG"], abschnitt=D),
    fall("p07g-3", "Der Chef, der die Aufgabe stellte",
         "Geschäftsführer F bat seinen Entwicklungsleiter, „sich etwas einfallen zu lassen“, weil die Flinte zu schwer sei. Den hohlen Schaft "
         "erfand der Entwicklungsleiter. F lässt sich als Miterfinder benennen (nach RP2 I/2020).",
         "Ist F durch die Aufgabenstellung Miterfinder geworden?", False,
         ["**Nein!** Die bloße Aufgabe ohne Hinweis auf einen Lösungsweg ist in der Regel kein schöpferischer Beitrag zur Lösung "
          "(Schiedsstelle Arb.Erf. 46/20). Die Aufgabenstellung wirkt im Anteilsfaktor (Wertzahl a, RL Nr. 31). F ist zu Unrecht benannt und "
          "muss neben der GmbH der Berichtigung zustimmen (§ 63 Abs. 2 S. 1 PatG)."],
         merke="Aufgabe stellen ≠ erfinden; Folge nur im Anteilsfaktor (RL Nr. 31).", level=1,
         concepts=["arb_miterfinder", "pat_erfinderbenennung"], norms=["§ 63 PatG"], abschnitt=D),
    fall("p07g-4", "PU-Schaum ist doch bekannt",
         "Die frühere Mitarbeiterin P schlug vor, den hohlen Schaft mit PU-Schaum zu füllen; das steht in der Beschreibung. Der Arbeitgeber meint, "
         "ihr Beitrag sei für sich nicht patentfähig, Hohlräume auszuschäumen kenne jeder Trockenbauer (nach RP2 I/2020).",
         "Schließt die fehlende eigene Patentfähigkeit ihres Beitrags die Miterfinderschaft aus?", False,
         ["**Nein!** Der Einzelbeitrag muss nicht für sich alle Voraussetzungen einer patentfähigen Erfindung erfüllen, aber für die Lösung "
          "wesentlich sein (Schiedsstelle Arb.Erf. 46/20); auf die Schutzfähigkeit kommt es für die Nennung ohnehin nicht an (BGH "
          "Atemgasdrucksteuerung). Entscheidend ist, ob die Füllung zur geschützten Lehre gehört und deren Stabilitätsproblem löst."],
         merke="Miterfinder: wesentlicher Beitrag, nicht eigene Patentfähigkeit.", level=2,
         concepts=["arb_miterfinder", "pat_erfinderbenennung"], norms=["§ 63 PatG", "§ 6 PatG"], abschnitt=D),
    mc("p07g-5", "Fristende der Vindikation",
       "Bis wann muss die Firma A gegen B auf Übertragung von P2 klagen, wenn B gutgläubig war?",
       ["Bis Mo 07.10.2024", "Bis Sa 05.10.2024", "Bis Mi 05.07.2023", "Ohne Frist"], 0,
       ["**Mo 07.10.2024.** Zwei Jahre nach Veröffentlichung der Erteilung (§ 8 S. 3 PatG, § 58 Abs. 1 PatG): Beginn am 06.10.2022 "
        "(§ 187 Abs. 1 BGB), Ende Sa 05.10.2024 (§ 188 Abs. 2 BGB), verschoben auf den nächsten Werktag (§ 193 BGB). War B beim Erwerb "
        "nicht in gutem Glauben, gilt keine Frist (§ 8 S. 5 PatG)."],
       sachverhalt="Die Erteilung des Patents P2, das die frühere Mitarbeiterin B auf eigenen Namen angemeldet hat, wurde am Mi 05.10.2022 "
                   "veröffentlicht (nach RP2 III/2023).",
       merke="Vindikation: zwei Jahre ab Veröffentlichung der Erteilung (§ 8 S. 3 PatG) · § 187 Abs. 1, § 188 Abs. 2, § 193 BGB.", level=2,
       concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG", "§ 58 PatG"], abschnitt=D),
    fall("p07g-6", "Lizenz durch einen Mitinhaber",
         "Ex-Geschäftsführer H ist Mitinhaber (20 %) der Patente der DD GmbH. Er will seiner neuen GG GmbH eine Lizenz erteilen, damit sie "
         "ihren Mikroorganismus vermarkten kann (nach RP2 III/2022).",
         "Kann H der GG GmbH ohne Zustimmung der übrigen Teilhaber wirksam eine Lizenz erteilen?", False,
         ["**Nein!** Jeder Teilhaber darf den Gegenstand selbst gebrauchen (§ 743 Abs. 2 BGB) und über seinen Anteil verfügen (§ 747 S. 1 BGB). "
          "Die Gestattung an Dritte ist Verwaltung; sie verlangt einen Mehrheitsbeschluss (§ 745 Abs. 1 BGB), der die übrigen Teilhaber an den "
          "Nutzungen beteiligt (BGH Penetrometer). Mit 20 % hat H keine Mehrheit."],
         merke="Mitinhaber: eigene Nutzung ja (§ 743 Abs. 2 BGB), Lizenz an Dritte nur per Mehrheit (§ 745 Abs. 1 BGB).", level=3,
         concepts=["pat_recht_auf_patent", "arb_miterfinder"], norms=["§ 6 PatG"], abschnitt=D),
    *fallkette("p07g-7", "Verstellung und Markisen (nach RP2 I/2019)",
        "E1 macht 2015 „Verstellung“ und „Markisen“, meldet sie aber erst am Sa 24.12.2016 ordnungsgemäß. E2 aus einem anderen Team erfindet "
        "beides unabhängig: „Monitorverstellung“ meldet er am 05.10.2016, A meldet sie am selben Tag an; „Markisenvorrichtung“ meldet er am "
        "15.05.2017, A meldet sie am 07.07.2017 an. Als Erfinder ist jeweils Geschäftsführer GF genannt.",
        [frage("Ist die Nennung des GF unrichtig?", True,
               ["**Ja!** GF hat keinen schöpferischen Beitrag geleistet (§ 63 Abs. 2 S. 1 PatG, § 63 Abs. 1 S. 1 PatG); dass er „versehentlich“ "
                "benannt wurde, ist unerheblich. Offen ist nur, wer an seine Stelle tritt."],
               merke="V1: Nennung unrichtig, Verschulden egal.", titel="V1 Unrichtige Nennung", level=1),
         frage("Kann E1 verlangen, im Patent „Monitorverstellung“ genannt zu werden?", False,
               ["**Nein!** Es ist eine unabhängige Doppelerfindung (§ 6 S. 3 PatG). A meldete am 05.10.2016 aus dem Recht des E2 an; E1 hatte "
                "die Lehre bis dahin nicht gemeldet, A hatte sein Recht nicht erworben (§ 7 Abs. 1 ArbnErfG). Das Patent beruht auf dem Beitrag "
                "des E2; ihm steht die Nennung zu (BGH Atemgasdrucksteuerung)."],
               merke="Doppelerfindung: Patent beruht auf dem, aus dessen Recht angemeldet wurde.", titel="V2.2, V2.3 Monitorverstellung", level=3),
         frage("Kann E1 verlangen, im Patent „Markisenvorrichtung“ genannt zu werden?", True,
               ["**Ja!** Seine Meldung vom 24.12.2016 führte mit Ablauf des Mo 24.04.2017 zur fingierten Inanspruchnahme (§ 6 Abs. 2 ArbnErfG); "
                "A hielt sein Recht (§ 7 Abs. 1 ArbnErfG), bevor E2 am 15.05.2017 meldete. Die Anmeldung vom 07.07.2017 beruht damit auf dem "
                "Recht des früheren Erfinders E1 (Wertung des § 6 S. 3 PatG); so jedenfalls die Lösung."],
               merke="Wer zuerst erfindet und meldet, vermittelt dem Arbeitgeber das Recht (Lösung RP2 I/2019).", titel="V2 Markisenvorrichtung", level=3),
         frage("Gegen wen richtet sich der Anspruch?", 0,
               ["**Gegen A und GF.** Verpflichtet sind der Patentinhaber und der zu Unrecht Benannte; beide müssen gegenüber dem DPMA zustimmen "
                "(§ 63 Abs. 2 S. 1 PatG). Die Zustimmung ist unwiderruflich (§ 63 Abs. 2 S. 2 PatG)."],
               optionen=["Gegen die A GmbH als Inhaberin und gegen GF als zu Unrecht Benannten", "Nur gegen die A GmbH",
                         "Nur gegen GF", "Gegen das DPMA"],
               merke="§ 63 Abs. 2 S. 1 PatG: Inhaber + zu Unrecht Benannter.", titel="V3 Anspruchsgegner", level=1),
         frage("Muss E1 vor der Klage die Schiedsstelle anrufen?", False,
               ["**Nein!** Der Anspruch folgt aus § 63 Abs. 2 S. 1 PatG; das Schiedsverfahren ist nur für Rechte vorgeschrieben, die im ArbnErfG "
                "geregelt sind (§ 37 Abs. 1 ArbnErfG). Gegen GF fehlt ohnehin ein Streit zwischen Arbeitgeber und Arbeitnehmer (§ 28 S. 1 "
                "ArbnErfG). Zuständig: Patentstreitkammer (§ 143 Abs. 1 PatG)."],
               merke="Nennungsklage: direkt zum Landgericht.", titel="B Durchsetzung", level=1),
         ],
        abschnitt=K, level=2, concepts=["pat_erfinderbenennung", "arb_inanspruchnahme"], norms=["§ 63 PatG", "§ 6 PatG"]),
    *fallkette("p07g-8", "Die Saurierhaut (nach RP2 III/2023)",
        "Personalsachbearbeiterin B meldet eine Prägevorrichtung ordnungsgemäß; A nimmt sie in Anspruch, erkennt die Schutzfähigkeit an und "
        "vereinbart mit B, sie als Betriebsgeheimnis zu behandeln. B meldet sie dennoch selbst an (P1, Erteilung veröffentlicht am Mi "
        "03.05.2023). Eine Folie mit Saurierhaut-Struktur, eine Diensterfindung, meldet B nie, sondern lässt sie selbst patentieren (P2).",
        [frage("Ist A Berechtigte an P1?", True,
               ["**Ja!** Mit der Inanspruchnahme sind alle vermögenswerten Rechte auf A übergegangen (§ 7 Abs. 1 ArbnErfG), also das Recht auf "
                "das Patent (§ 6 S. 1 PatG). Das Betriebsgeheimnis (§ 17 Abs. 1 ArbnErfG) ändert an der Zuordnung nichts (Schiedsstelle "
                "Arb.Erf. 02/23). B hat als Nichtberechtigte angemeldet und ihre Geheimhaltungspflicht verletzt (§ 24 Abs. 2 ArbnErfG)."],
               merke="Inanspruchnahme → Recht auf das Patent beim Arbeitgeber (§ 7 Abs. 1 ArbnErfG).", titel="V1, V2 P1", level=1),
         frage("Bis wann muss A auf Übertragung von P1 klagen?", 0,
               ["**Ohne Frist.** An sich zwei Jahre nach Veröffentlichung der Erteilung, Ende Sa 03.05.2025, verschoben auf Mo 05.05.2025 "
                "(§ 8 S. 3 PatG, § 188 Abs. 2 BGB, § 193 BGB). B wusste aber von Inanspruchnahme und Geheimhaltungsabrede; sie war beim Erwerb "
                "nicht in gutem Glauben, die Frist gilt nicht (§ 8 S. 5 PatG)."],
               optionen=["Ohne Frist, weil B bösgläubig war (§ 8 S. 5 PatG)", "Bis Mo 05.05.2025", "Bis Sa 03.05.2025",
                         "Bis neun Monate nach Veröffentlichung der Erteilung"],
               merke="Bösgläubiger Inhaber: keine Ausschlussfrist (§ 8 S. 5 PatG).", titel="V4 Klagefrist P1", level=2),
         frage("Kann A die nie gemeldete Erfindung P2 noch in Anspruch nehmen?", True,
               ["**Ja!** Ohne Meldung läuft keine Frist; A kann durch Erklärung in Anspruch nehmen (§ 6 Abs. 1 ArbnErfG). Die Eigenanmeldung der "
                "B ersetzt die Meldung nicht (BGH Initialidee) und ist A gegenüber unwirksam (§ 7 Abs. 2 ArbnErfG). Danach kann A Übertragung "
                "verlangen (§ 8 S. 2 PatG)."],
               merke="Nicht gemeldet + selbst angemeldet → erst in Anspruch nehmen, dann vindizieren.", titel="V1 P2", level=2),
         frage("Kann A dann Übertragung von P2 verlangen?", False,
               ["**Nein!** Eine freie Erfindung geht nicht über; A bleibt nur die Anbietungspflicht der B: mindestens ein nichtausschließliches "
                "Benutzungsrecht zu angemessenen Bedingungen (§ 19 Abs. 1 ArbnErfG). Mitteilung (§ 18 Abs. 1 ArbnErfG) und Angebot hat B "
                "unterlassen; A kann beides verlangen."],
               merke="Freie Erfindung: kein Übergang, nur Benutzungsrecht nach § 19 ArbnErfG.", titel="Abwandlung: freie Erfindung",
               abwandlung="P2 ist eine freie Erfindung, fällt aber in den Arbeitsbereich der Firma A.", level=2),
         ],
        abschnitt=K, level=2, concepts=["pat_recht_auf_patent", "arb_inanspruchnahme"], norms=["§ 8 PatG", "§ 7 ArbnErfG"]),
])

KURS = dict(
    id="p07", gebiet="patent", reihe="Anspruchsgrundlagen für die Klausur", kompakt="fragen",
    titel="Anspruchsgrundlagen ArbnErfG",
    untertitel="Rechtspraxis 2: Meldung, Inanspruchnahme, Anmeldung, Vergütung, Schiedsstelle, Erfindernennung und Vindikation",
    farbe="#2f6b4f", icon="hammer",
    beschreibung="Die Anspruchsgrundlagen der RP2-Klausur Schritt für Schritt: Prüfungsschema in der Lösungssprache mit Normenkette, "
                 "Definitionen, Fristen mit Berechnung und Klausurfälle nach den Klausuren II/2018 bis III/2023. Vergütung nach "
                 "Erfindungswert und Anteilsfaktor mit nachvollziehbaren Rechenwegen aus den Vergütungsrichtlinien, Unbilligkeit und "
                 "Anpassung, Altfälle nach dem ArbnErfG a.F., Insolvenz und Verkauf, Schiedsstelle und Klage, Berichtigung der "
                 "Erfindernennung und Vindikation nach dem PatG.",
    kapitel=[P070, P07A, P07B, P07C, P07D, P07E, P07F, P07G],
)
