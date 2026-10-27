# -*- coding: utf-8 -*-
"""Rechtsfolgen und Vollstreckung vor dem EPG im Jurafuchs-Format: je Kapitel die Kernvorschriften, darin kurze Fallketten mit
einer Frage je Auslegungselement."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

KURS = dict(
    id="u07", gebiet="upc", kompakt="fragen", titel="Rechtsfolgen, Zwangsgeld und Vollstreckung",
    untertitel="Unterlassung, Abhilfe, Auskunft, Schadensersatz – und wie das EPG seine Anordnungen durchsetzt",
    farbe="#c2410c", icon="rechtsfolgen",
    beschreibung="Was der Kläger nach festgestellter Verletzung bekommt: die Unterlassungsanordnung nach Art. 63 EPGÜ und ihre Reichweite (Dyson/Dreame), Abhilfemaßnahmen (Art. 64 EPGÜ), Auskunft (Art. 67 EPGÜ), Veröffentlichung (Art. 80 EPGÜ) und Schadensersatz mit dem gesonderten Festsetzungsverfahren (Art. 68 EPGÜ, R. 125 ff. VerfO). Dazu das System der Zwangsgelder nach Kodak/Fujifilm, die Pflichten des Adressaten bei Plattformen und Geoblocking (Lepu/Occlutech), der Rechtsweg gegen die Zwangsgeldfestsetzung (EOFlow/Insulet) und die Rückwirkung der Aufhebung.",
    kapitel=[
        dict(id="u07a", titel="Art. 63, 64, 67 und 80 EPGÜ: Unterlassung, Abhilfe, Auskunft, Veröffentlichung", einheiten=[
            schema("u07a-0", "Prüfungsschema: Verletzungsklage vor dem EPG", "upc_schema_verletzungsklage",
                   "Dieser Kurs behandelt den Abschnitt C des Schemas: Wird die Verletzung festgestellt, folgen Unterlassung und Zwangsgeld (Art. 63 EPGÜ), Abhilfe, Auskunft und Veröffentlichung (Art. 64, 67, 80 EPGÜ), Schadensersatz (Art. 68 EPGÜ) sowie Kosten und Vollstreckung (Art. 69, 82 EPGÜ). Alle Anordnungen stehen im Ermessen des Gerichts („kann“) und unterliegen der Verhältnismäßigkeit nach Art. 42 EPGÜ."),
            *fallkette("u07a-1", "Nur das Angebot?",
                "Die Lokalkammer stellt fest, dass Dreame durch das Anbieten eines Saugroboters ein Patent von Dyson verletzt. Sie verbietet "
                "Dreame Anbieten, Inverkehrbringen, Gebrauchen, Einführen und Besitzen dieses Geräts.",
                [frage("Muss das Verbot auf das nachgewiesene Anbieten beschränkt werden?", False,
                       ["**Nein!** Art. 63 Abs. 1 EPGÜ erlaubt eine Verfügung, die die **Fortsetzung der Verletzung** untersagt. Weder "
                        "Art. 63 EPGÜ noch Art. 25 lit. a EPGÜ beschränken sie auf die schon begangene Benutzungsart (EPG-BerG Dyson/Dreame)."],
                       merke="Wer einmal verletzt hat, dem droht das Verbot aller Benutzungsarten des Art. 25 EPGÜ.", titel="Keine Beschränkung"),
                 frage("Droht auch das Inverkehrbringen, obwohl Dreame noch nichts verkauft hat?", True,
                       ["**Ja!** Wer eine Verletzungshandlung begangen hat, begründet in der Regel die Gefahr, dass er die Verletzung auch "
                        "durch andere Benutzungshandlungen fortsetzt: Wer anbietet, wird liefern und in Verkehr bringen (EPG-BerG "
                        "Dyson/Dreame)."],
                       titel="Gefahr weiterer Handlungen"),
                 frage("Wie verhalten sich die Benutzungsarten des Art. 25 EPGÜ zueinander?", 1,
                       ["Die Benutzungshandlungen des Art. 25 EPGÜ sind zwar **selbständig**, gehören aber zu **demselben "
                        "Ausschließlichkeitsrecht**. Deshalb erfasst die Gefahr der Fortsetzung der Verletzung auch die bisher nicht "
                        "begangenen Handlungen (EPG-BerG Dyson/Dreame)."],
                       optionen=["Jede ist ein eigenes Recht mit eigener Wiederholungsgefahr",
                                 "Sie sind selbständige Handlungen desselben Ausschließlichkeitsrechts",
                                 "Nur Herstellen und Inverkehrbringen sind verboten"],
                       level=3, titel="Ein Recht, viele Handlungen", norms=["Art. 25 EPGÜ"]),
                 frage("Darf das Verbot auch Geräte erfassen, deren Verletzung nicht festgestellt ist?", False,
                       ["**Nein!** Grenze ist die Verhältnismäßigkeit (Art. 42 EPGÜ). Das Verbot muss sich auf die verletzende "
                        "Ausführungsform und die zu erwartenden Handlungen beziehen, nicht auf beliebige andere Produkte."],
                       abwandlung="Dyson beantragt, Dreame auch alle anderen Saugroboter zu verbieten.", titel="Grenze der Verhältnismäßigkeit",
                       norms=["Art. 42 EPGÜ"]),
                 ],
                abschnitt="Art. 63 Abs. 1 EPGÜ: Reichweite des Verbots", level=2,
                concepts=["upc_unterlassungsanordnung", "upc_unmittelbare_verletzung"], norms=["Art. 63 Abs. 1 EPGÜ", "Art. 25 EPGÜ"],
                cases=["upc_coa_dyson_dreame_auslegung"], step="step:upc_schema_verletzungsklage.3.1"),
            *fallkette("u07a-2", "Ladegeräte aus dem Lager",
                "Das Gericht stellt fest, dass Belkin mit Ladegeräten ein Patent von Philips verletzt. Die Geräte werden über das Lager eines "
                "Logistikdienstleisters ausgeliefert. Philips beantragt Unterlassung.",
                [frage("Muss das Gericht die Unterlassung anordnen, weil die Verletzung feststeht?", False,
                       ["**Nein!** Art. 63 Abs. 1 EPGÜ sagt „kann“: Das Gericht hat **Ermessen** und prüft die Verhältnismäßigkeit nach "
                        "Art. 42 EPGÜ. In der Regel übt es das Ermessen aber zugunsten des Verbots aus."],
                       titel="Ermessen", norms=["Art. 42 EPGÜ"]),
                 frage("Kann das Verbot auch gegen den Logistikdienstleister ergehen, obwohl er selbst nicht verletzt?", True,
                       ["**Ja!** Art. 63 Abs. 1 Satz 2 EPGÜ erlaubt eine Verfügung gegen **Mittelspersonen**, deren Dienste ein Dritter zur "
                        "Verletzung in Anspruch nimmt. Eigene Verletzerhaftung ist nicht nötig. Das setzt Art. 11 Satz 3 DurchsetzungsRL um."],
                       merke="Mittelspersonen können Adressat sein, ohne selbst zu verletzen.", titel="Mittelsperson",
                       norms=["Art. 11 DurchsetzungsRL"]),
                 frage("Haftet der Geschäftsführer von Belkin allein wegen seiner Organstellung als Mittäter?", False,
                       ["**Nein!** Die bloße Organstellung genügt nicht. Der Geschäftsführer haftet nur, wenn er das Unternehmen "
                        "zweckgerichtet zur Verletzung nutzt oder trotz Kenntnis und Zumutbarkeit nicht einschreitet (EPG-BerG Belkin/Philips)."],
                       level=3, titel="Geschäftsführer", concepts=["upc_verletzer"]),
                 frage("An wen fließt ein Zwangsgeld nach Art. 63 Abs. 2 EPGÜ?", 1,
                       ["Zwangsgelder sind **an das Gericht** zu zahlen (Art. 63 Abs. 2, Art. 82 Abs. 4 EPGÜ). Sie lassen den "
                        "Schadensersatzanspruch des Klägers unberührt."],
                       optionen=["An Philips, als Teil des Schadensersatzes", "An das Gericht", "Je zur Hälfte an Gericht und Philips"],
                       titel="Empfänger des Zwangsgelds", norms=["Art. 63 Abs. 2 EPGÜ"]),
                 ],
                abschnitt="Art. 63 EPGÜ: Ermessen, Mittelspersonen, Zwangsgeld", level=2,
                concepts=["upc_unterlassungsanordnung"], norms=["Art. 63 Abs. 1 EPGÜ"],
                cases=["upc_coa_belkin_philips_anbieten"], step="step:upc_schema_verletzungsklage.3.1"),
            *fallkette("u07a-3", "Umbau statt Vernichtung",
                "Filteranlagen von Ventra verletzen ein Patent von Aquilon; 400 Anlagen lagern noch bei Ventra. Das verletzende Ventilmodul "
                "lässt sich mit geringem Aufwand gegen ein nicht verletzendes tauschen. Ventra ist dazu bereit.",
                [frage("Muss das Gericht die Vernichtung der Anlagen anordnen?", False,
                       ["**Nein!** Abhilfemaßnahmen ordnet das Gericht auf Antrag an und hat dabei **Ermessen** („kann“, Art. 64 Abs. 1 "
                        "EPGÜ). Eine zwingende Vernichtung kennt das EPGÜ nicht."],
                       titel="Kein Vernichtungszwang"),
                 frage("Welche Maßnahme nennt Art. 64 Abs. 2 EPGÜ gleichrangig neben der Vernichtung?", 2,
                       ["Art. 64 Abs. 2 EPGÜ nennt die Feststellung der Verletzung (lit. a), den Rückruf (lit. b), die **Beseitigung der "
                        "verletzenden Eigenschaft** (lit. c), die endgültige Entfernung aus den Vertriebswegen (lit. d) und die Vernichtung "
                        "(lit. e)."],
                       optionen=["Eine Geldbuße an den Patentinhaber", "Die Beschlagnahme durch den Zoll",
                                 "Die Beseitigung der verletzenden Eigenschaft"],
                       titel="Katalog des Abs. 2", norms=["Art. 64 Abs. 2 EPGÜ"]),
                 frage("Zählt Ventras Bereitschaft zum Umbau bei der Auswahl der Maßnahme?", True,
                       ["**Ja!** Nach Art. 64 Abs. 4 EPGÜ berücksichtigt das Gericht die Verhältnismäßigkeit, die **Bereitschaft des "
                        "Verletzers, das Material in einen nichtverletzenden Zustand zu versetzen**, und die Interessen Dritter. Hier genügt "
                        "der Austausch des Moduls; die Vernichtung wäre das schärfere Mittel ohne Mehrwert."],
                       merke="Art. 64 Abs. 4 EPGÜ: Vernichtung nur, wenn mildere Mittel nicht genügen.", titel="Verhältnismäßigkeit",
                       norms=["Art. 64 Abs. 4 EPGÜ"]),
                 frage("Trägt Ventra die Kosten des Umbaus?", True,
                       ["**Ja!** Die Maßnahmen werden **auf Kosten des Verletzers** durchgeführt, es sei denn, es werden besondere Gründe "
                        "dagegen geltend gemacht (Art. 64 Abs. 3 EPGÜ). Das entspricht Art. 10 DurchsetzungsRL und § 140a PatG."],
                       titel="Kosten der Abhilfe"),
                 ],
                abschnitt="Art. 64 EPGÜ: Abhilfemaßnahmen", level=2,
                concepts=["upc_abhilfemassnahmen", "upc_verfahrensgrundsaetze"], norms=["Art. 64 EPGÜ", "Art. 42 EPGÜ", "R. 118 VerfO"],
                step="step:upc_schema_verletzungsklage.3.2"),
            *fallkette("u07a-4", "Auskunft vom Spediteur",
                "Die Herstellerin Corvid ist wegen Verletzung eines Patents von Meridian verurteilt. Die Spedition Lorentz hat die "
                "verletzenden Pumpen gewerblich für Corvid eingelagert und an Händler in drei Staaten ausgeliefert.",
                [frage("Kann Meridian von Corvid Auskunft über Vertriebswege, Mengen und Preise verlangen?", True,
                       ["**Ja!** Auf begründeten, verhältnismäßigen Antrag ordnet das Gericht an, dass der Verletzer Auskunft gibt über "
                        "Ursprung und Vertriebswege, Mengen und Preise sowie beteiligte Dritte (Art. 67 Abs. 1 lit. a bis c EPGÜ)."],
                       titel="Auskunft des Verletzers", norms=["Art. 67 Abs. 1 EPGÜ"]),
                 frage("Kann auch Lorentz zur Auskunft verpflichtet werden, obwohl sie keine Verletzerin ist?", True,
                       ["**Ja!** Art. 67 Abs. 2 EPGÜ erstreckt die Pflicht auf **jede dritte Partei**, die verletzende Erzeugnisse "
                        "gewerblich besessen (lit. a) oder für die Verletzung genutzte Dienstleistungen gewerblich erbracht hat (lit. b). "
                        "Eine Spedition, die einlagert und ausliefert, erfüllt beides."],
                       merke="Art. 67 Abs. 2 EPGÜ: Auskunft auch vom Nichtverletzer.", titel="Drittauskunft"),
                 frage("Ist die Auskunftsanordnung nur mit Zulassung anfechtbar?", False,
                       ["**Nein!** Anordnungen nach Art. 67 EPGÜ sind ohne Zulassung mit der Berufung anfechtbar, binnen 15 Tagen (Art. 73 "
                        "Abs. 2 lit. a EPGÜ, R. 220.1 lit. c VerfO)."],
                       level=3, titel="Anfechtung", norms=["Art. 73 Abs. 2 EPGÜ"]),
                 frage("Welcher deutschen Vorschrift entspricht Art. 67 Abs. 2 EPGÜ?", 0,
                       ["Art. 67 EPGÜ setzt Art. 8 DurchsetzungsRL um. Im deutschen Recht entspricht die Drittauskunft § 140b Abs. 2 PatG "
                        "und § 19 Abs. 2 MarkenG. § 140c PatG regelt dagegen Vorlage und Besichtigung."],
                       optionen=["§ 140b Abs. 2 PatG", "§ 140c PatG", "§ 139 Abs. 2 PatG"],
                       titel="Deutsche Parallele", norms=["Art. 8 DurchsetzungsRL"]),
                 ],
                abschnitt="Art. 67 EPGÜ: Auskunft", level=2,
                concepts=["upc_auskunft", "upc_beweisanordnung"], norms=["Art. 67 Abs. 2 EPGÜ", "R. 191 VerfO"],
                step="step:upc_schema_verletzungsklage.3.2"),
            *fallkette("u07a-5", "Die Auskunft kommt zu spät",
                "Belkin ist verurteilt, Philips Auskunft nach Art. 67 EPGÜ zu erteilen; eine Frist nennt die Entscheidung nicht. Philips "
                "teilt die Vollstreckungsabsicht mit und setzt eine Frist. Belkin antwortet erst nach deren Ablauf.",
                [frage("Gehört die Frist für die Auskunft schon in den Antrag des Klägers?", True,
                       ["**Ja!** Der Antrag nach Art. 67 Abs. 1 EPGÜ soll in der Regel die Frist zur Auskunft enthalten, damit sie schon in "
                        "der Entscheidung steht. Sie läuft ab der Mitteilung nach R. 118.8 VerfO, im Eilverfahren ab Zustellung der "
                        "Anordnung (EPG-BerG Belkin/Philips 2025)."],
                       titel="Frist im Antrag"),
                 frage("Durfte Philips die Frist selbst setzen?", True,
                       ["**Ja!** Fehlt die Frist in der Entscheidung, ist es Sache des Klägers, sie mit der Mitteilung der "
                        "Vollstreckungsabsicht nach R. 118.8 VerfO zu setzen (EPG-BerG Belkin/Philips 2025)."],
                       titel="Frist mit der Vollstreckungsmitteilung", norms=["R. 118.8 VerfO"]),
                 frage("Entfällt das Zwangsgeld, weil Belkin die Auskunft inzwischen erteilt hat?", False,
                       ["**Nein!** Das Zwangsgeld hat nicht nur Beuge-, sondern auch **Strafcharakter**. Es kann deshalb auch verhängt "
                        "werden, wenn der Beklagte die Auskunft inzwischen, aber verspätet erteilt hat (EPG-BerG Belkin/Philips 2025)."],
                       merke="Verspätete Auskunft schützt nicht vor dem Zwangsgeld (Belkin/Philips 2025).", level=3,
                       titel="Verspätete Erfüllung", concepts=["upc_zwangsgeld"], norms=["R. 354 VerfO"]),
                 frage("Wer muss beweisen, dass die Auskunft vollständig erteilt ist?", 1,
                       ["Die Darlegungs- und Beweislast für die Erfüllung der Auskunftspflicht trägt der **Beklagte** (EPG-BerG "
                        "Belkin/Philips 2025). Er kennt seine Geschäftsvorgänge."],
                       optionen=["Philips", "Belkin", "Das Gericht von Amts wegen"],
                       titel="Beweislast"),
                 frage("Muss Belkin auch die Preise nennen, die sie selbst dem Hersteller gezahlt hat?", True,
                       ["**Ja!** Art. 67 Abs. 1 lit. b EPGÜ umfasst auch die vom Verletzer gezahlten Einkaufspreise (Herstellerpreise). Ist "
                        "keine Form angeordnet, darf Belkin schriftlich oder elektronisch Auskunft geben (EPG-BerG Belkin/Philips 2025)."],
                       titel="Einkaufspreise", norms=["Art. 67 Abs. 1 EPGÜ"]),
                 ],
                abschnitt="Art. 67 EPGÜ, R. 118.8 VerfO: Frist und Inhalt der Auskunft", level=2,
                concepts=["upc_auskunft", "upc_vollstreckung"], norms=["Art. 67 EPGÜ", "R. 118.8 VerfO"],
                cases=["upc_coa_belkin_philips_auskunft"], step="step:upc_schema_verletzungsklage.3.2"),
            *fallkette("u07a-6", "Die eigene Erklärung im Netz",
                "Fujifilm verklagt Kodak aus einem Patent für Druckplatten. Für den Fall des Erfolgs beantragt Fujifilm, Kodak zu verpflichten, "
                "auf der eigenen Website eine Erklärung zur Verletzung zu veröffentlichen.",
                [frage("Ist eine solche Erklärung nur bei besonderen Umständen gerechtfertigt?", True,
                       ["**Ja!** Die Veröffentlichung einer eigenen Erklärung des Verletzers auf seiner Website nach Art. 80 EPGÜ ist nur "
                        "bei **besonderen Umständen** gerechtfertigt: als Korrektur von Folgen der Verletzung, die sich nicht rückgängig machen "
                        "oder anders ausgleichen lassen (EPG-BerG Fujifilm/Kodak)."],
                       merke="Art. 80 EPGÜ: Veröffentlichung als Korrekturmittel, nicht als Regelfolge.", titel="Art. 80 EPGÜ"),
                 frage("Ist ein Zwangsgeld für eine vollstreckbare Geldschuld angemessen?", False,
                       ["**Nein!** Es ist nicht angemessen und verhältnismäßig, ein Zwangsgeld für die Nichterfüllung einer vollstreckbaren "
                        "**Zahlungspflicht** anzuordnen (EPG-BerG Fujifilm/Kodak). Geldforderungen werden nach dem Recht des "
                        "Vollstreckungsstaats beigetrieben (Art. 82 Abs. 3 EPGÜ)."],
                       abwandlung="Fujifilm beantragt außerdem, eine Zahlungspflicht von Kodak mit Zwangsgeld zu bewehren.", level=3,
                       titel="Kein Zwangsgeld für Geldschulden", concepts=["upc_zwangsgeld"], norms=["Art. 82 EPGÜ"]),
                 ],
                abschnitt="Art. 80 EPGÜ: Veröffentlichung", level=2,
                concepts=["upc_unterlassungsanordnung"], norms=["Art. 80 EPGÜ"],
                cases=["upc_coa_fujifilm_kodak_nichtigkeit"], step="step:upc_schema_verletzungsklage.3.2"),
        ]),
        dict(id="u07b", titel="Art. 68 EPGÜ, R. 125 bis 131 VerfO: Schadensersatz und Festsetzungsverfahren", einheiten=[
            intro("u07b-0", "Zwei Stufen: Grund im Urteil, Höhe im gesonderten Verfahren",
                  "Art. 68 Abs. 1 EPGÜ verpflichtet den Verletzer, der **wusste oder vernünftigerweise hätte wissen müssen**, dass er eine Verletzung begeht, zu angemessenem Schadensersatz. Ziel ist der Ausgleich des tatsächlichen Schadens: Die geschädigte Partei ist so zu stellen, wie sie ohne die Verletzung stünde, dem Verletzer darf kein Nutzen bleiben, ein **Strafcharakter** ist ausgeschlossen (Abs. 2). Bei der Bemessung berücksichtigt das Gericht alle Aspekte, insbesondere Gewinneinbußen des Geschädigten und Verletzergewinn, in geeigneten Fällen auch immaterielle Schäden (Abs. 3 lit. a), oder es setzt stattdessen einen **Pauschalbetrag** auf Grundlage mindestens der hypothetischen Lizenzgebühr fest (Abs. 3 lit. b). Der gutgläubige Verletzer schuldet keinen Schadensersatz, kann aber zur Herausgabe der Gewinne oder zu einer Entschädigung verpflichtet werden (Abs. 4). Das ist die Umsetzung von Art. 13 DurchsetzungsRL und entspricht der dreifachen Schadensberechnung des § 139 Abs. 2 PatG. Verfahrensrechtlich arbeitet das EPG zweistufig: In der Entscheidung in der Sache spricht das Gericht den Schadensersatz dem Grunde nach zu und kann eine vorläufige Zahlung anordnen (R. 118.1, R. 119 VerfO); die **Höhe** wird auf Antrag binnen **eines Jahres** nach Zustellung der Endentscheidung in einem gesonderten Verfahren festgesetzt (R. 125, 126 VerfO), das mit einem Antrag auf **Offenlegung der Bücher** verbunden werden kann (R. 131.1 lit. c, R. 141 ff. VerfO).",
                  concepts=["upc_schadensersatz", "upc_auskunft"], norms=["Art. 68 Abs. 1 EPGÜ", "Art. 68 Abs. 3 EPGÜ", "R. 118.1 VerfO", "R. 126 VerfO"]),
            *fallkette("u07b-1", "Das französische Urteil",
                "Ein französisches Gericht hat REEL 2022 dem Grunde nach zum Schadensersatz wegen Verletzung eines europäischen Patents von "
                "Fives verurteilt. 2024 klagt Fives beim EPG auf Festsetzung der Höhe für Handlungen von 2019 bis 2022.",
                [frage("Ist das EPG für eine Klage nur auf die Höhe des Schadensersatzes zuständig?", True,
                       ["**Ja!** Die Zuständigkeit für Verletzungsklagen (Art. 32 Abs. 1 lit. a EPGÜ) umfasst auch eine **selbständige "
                        "Klage auf Festsetzung von Schadensersatz**, nachdem ein nationales Gericht die Ersatzpflicht dem Grunde nach "
                        "festgestellt hat. Das EPGÜ trennt Grund und Höhe selbst (R. 118.1, R. 125 ff. VerfO; EPG-BerG Fives/REEL)."],
                       titel="Klage auf die Höhe"),
                 frage("Steht entgegen, dass die Handlungen vor dem 1. Juni 2023 liegen?", False,
                       ["**Nein!** Die Zuständigkeit erfasst auch Handlungen vor Inkrafttreten des EPGÜ, solange das Patent am 1. Juni 2023 "
                        "noch nicht erloschen war; Art. 32 EPGÜ enthält keine zeitliche Beschränkung (EPG-BerG Fives/REEL)."],
                       merke="Altfälle: zuständig, wenn das Patent am 1. Juni 2023 noch in Kraft war (Fives/REEL).", titel="Altfälle"),
                 frage("Ist das für 2019 bis 2022 anwendbare Recht eine Frage der Zuständigkeit?", False,
                       ["**Nein!** Welches materielle Recht für die Altzeit gilt und ob ein Rückwirkungsverbot greift, ist eine Frage der "
                        "**Begründetheit** (EPG-BerG Knaus Tabbert). Der Einspruch nach R. 19 VerfO hilft REEL insoweit nicht."],
                       level=3, titel="Anwendbares Recht", cases=["upc_coa_knaus_tabbert_altfaelle"], norms=["R. 19 VerfO"]),
                 ],
                abschnitt="Art. 68 und 32 EPGÜ: Schadensersatzklage", level=3,
                concepts=["upc_schadensersatz", "upc_altfaelle", "upc_sachliche_zustaendigkeit"], norms=["Art. 68 EPGÜ", "Art. 32 Abs. 1 EPGÜ", "R. 125 VerfO"],
                cases=["upc_coa_fives_reel_altfaelle"], step="step:upc_schema_verletzungsklage.3.3"),
            *fallkette("u07b-2", "Die Zahlen fehlen",
                "Die Lokalkammer verurteilt Solvix zur Unterlassung und zum Schadensersatz dem Grunde nach. Die Entscheidung wird am 10. März "
                "zugestellt und nicht angefochten. Helion kennt weder Stückzahlen noch Preise von Solvix.",
                [frage("Bis wann muss Helion die Festsetzung des Schadensersatzes beantragen?", 1,
                       ["Der Antrag ist **binnen eines Jahres** nach Zustellung der Endentscheidung zu Verletzung und Rechtsbestand zu stellen "
                        "(R. 126 VerfO). Die Monatsfrist gehört zur Kostenfestsetzung (R. 151 VerfO)."],
                       optionen=["Binnen eines Monats nach der Entscheidung", "Binnen eines Jahres nach Zustellung",
                                 "Nur im Verletzungsurteil selbst"],
                       merke="Ein Jahr für den Schadensersatz (R. 126 VerfO), ein Monat für die Kosten (R. 151 VerfO).", titel="Jahresfrist"),
                 frage("Kann Helion zuerst die Offenlegung der Bücher verlangen und erst danach beziffern?", True,
                       ["**Ja!** Der Antrag kann einen Antrag auf **Offenlegung der Bücher** enthalten (R. 126, R. 131.1 lit. c, R. 141 ff. "
                        "VerfO). Erst nach der Offenlegung muss Helion Wiedergutmachung, Berechnung und Beweismittel angeben (R. 131.2 VerfO)."],
                       titel="Offenlegung der Bücher", norms=["R. 131 VerfO"]),
                 frage("Zahlt Helion für den Antrag auf Offenlegung der Bücher Gerichtsgebühren?", True,
                       ["**Ja!** Der Antrag auf Offenlegung der Bücher ist Teil des Verfahrens zur Festsetzung des Schadensersatzes. Wer ihn "
                        "stellt, schuldet dessen **Festgebühr und streitwertabhängige Gebühr** (EPG-BerG Bruker/10x Genomics)."],
                       level=3, titel="Gebühren", cases=["upc_coa_bruker_10x_buecher"], concepts=["upc_gerichtsgebuehren"]),
                 frage("Konnte die Lokalkammer schon im Urteil eine Zahlung anordnen?", True,
                       ["**Ja!** Die Höhe kann im Urteil angegeben oder im gesonderten Verfahren bestimmt werden (R. 118.1 VerfO). Das "
                        "Gericht kann außerdem eine vorläufige Zahlung anordnen (R. 119 VerfO)."],
                       titel="Zahlung im Urteil", norms=["R. 118.1 VerfO"]),
                 frage("Kann Helion das Doppelte der üblichen Lizenzgebühr verlangen, weil Solvix vorsätzlich handelte?", False,
                       ["**Nein!** Der Schadensersatz hat **keinen Strafcharakter** (Art. 68 Abs. 2 Satz 3 EPGÜ). Die Lizenzanalogie nach "
                        "Art. 68 Abs. 3 lit. b EPGÜ ist eine Pauschale auf Grundlage „mindestens“ der angemessenen Gebühr, kein Zuschlag."],
                       abwandlung="Solvix hat trotz Abmahnung weiter verletzt.", titel="Kein Verletzerzuschlag", norms=["Art. 68 Abs. 2 EPGÜ"]),
                 ],
                abschnitt="R. 125 bis 131 VerfO: Festsetzungsverfahren", level=2,
                concepts=["upc_schadensersatz"], norms=["R. 125 VerfO", "R. 126 VerfO"],
                step="step:upc_schema_verletzungsklage.3.3"),
        ]),
        dict(id="u07c", titel="Art. 82 EPGÜ, R. 354 VerfO: Vollstreckung und Zwangsgeld", einheiten=[
            intro("u07c-0", "Wie das EPG vollstreckt: Vollstreckungsstaat, Zwangsgeld, Rückwirkung",
                  "Entscheidungen und Anordnungen des EPG sind in **allen Vertragsmitgliedstaaten** vollstreckbar; das Vollstreckungsverfahren richtet sich nach dem Recht des Vollstreckungsstaats (Art. 82 Abs. 1, 3 EPGÜ). Sie sind ab Zustellung unmittelbar vollstreckbar (R. 354.1 VerfO), das Gericht kann die Vollstreckung aber von einer Sicherheitsleistung abhängig machen (Art. 82 Abs. 2 EPGÜ, R. 352 VerfO). Zwei Hürden stehen vor der Vollstreckung einer Sachentscheidung: Der Kläger muss dem Gericht mitteilen, **welchen Teil** der Anordnungen er vollstrecken will (Notice of intention to enforce), und gegebenenfalls eine beglaubigte Übersetzung in die Amtssprache des Vollstreckungsstaats vorlegen; erst mit Zustellung dieser Mitteilung an den Beklagten wird die Anordnung gegen ihn vollstreckbar (R. 118.8 VerfO). Das eigentliche Druckmittel des EPG ist das **Zwangsgeld**: Anordnungen können für den Fall der Zuwiderhandlung wiederholte, an das Gericht zahlbare Zwangsgeldzahlungen vorsehen (R. 354.3 VerfO, Art. 82 Abs. 4 EPGÜ); bei behaupteter Zuwiderhandlung setzt der erstinstanzliche Spruchkörper auf Antrag oder von Amts wegen das Zwangsgeld fest (R. 354.4 VerfO), nach Anhörung beider Parteien im Verfahren der R. 264 VerfO. Das Berufungsgericht hat das System in Kodak/Fujifilm geordnet: Androhung im Urteil oder nachträglich, Bestimmung nach Zeitraum, Stück oder Handlung, abschreckend aber verhältnismäßig. Wird die vollstreckte Anordnung später aufgehoben, wirkt das zurück (Art. 75 Abs. 1 EPGÜ) – und der Vollstreckungsschuldner kann Ersatz des Vollstreckungsschadens verlangen (R. 354.2 VerfO).",
                  concepts=["upc_vollstreckung", "upc_zwangsgeld"], norms=["Art. 82 EPGÜ", "R. 354 VerfO", "R. 118.8 VerfO", "R. 352 VerfO"],
                  cases=["upc_coa_kodak_fujifilm_zwangsgeld"]),
            *fallkette("u07c-1", "Die vergessene Androhung",
                "Die Lokalkammer verurteilt Kodak zur Unterlassung, ohne ein Zwangsgeld anzudrohen. Kodak liefert weiter. Fujifilm beantragt, "
                "die Anordnung nachträglich mit einem Zwangsgeld von 50.000 EUR je Verstoß zu versehen.",
                [frage("Kann die Lokalkammer das Zwangsgeld nachträglich gesondert androhen?", True,
                       ["**Ja!** Nach R. 354.3 VerfO kann eine Anordnung Zwangsgeld für den Fall vorsehen, dass eine Partei sie „oder eine "
                        "**frühere** Anordnung“ nicht befolgt. Die Androhung kann also ausnahmsweise später ergehen; in der Regel steht sie "
                        "der Rechtssicherheit wegen im Urteil (EPG-BerG Kodak/Fujifilm)."],
                       merke="R. 354.3 VerfO: Zwangsgeld im Urteil oder nachträglich.", titel="Nachträgliche Androhung"),
                 frage("Braucht Fujifilm dafür eine Berufung gegen das Urteil?", False,
                       ["**Nein!** Ein späterer Antrag auf Androhung erfordert keine Berufung gegen die Hauptsacheentscheidung, auch wenn ein "
                        "früherer Antrag abgelehnt wurde. Die Umstände können sich ändern und eine neue Bewertung rechtfertigen (EPG-BerG "
                        "Kodak/Fujifilm)."],
                       titel="Keine Berufung nötig"),
                 frage("Nach welchem Maßstab bemisst das Gericht die Höhe?", 2,
                       ["Das Gericht setzt den Betrag nach der Bedeutung der Anordnung fest (R. 354.3 VerfO). Er muss **abschreckend** genug "
                        "sein, um Druck zu erzeugen, aber in vernünftigen Grenzen bleiben, also **verhältnismäßig** sein (EPG-BerG "
                        "Kodak/Fujifilm)."],
                       optionen=["Nach dem Schaden von Fujifilm", "Nach dem Gewinn von Kodak",
                                 "Abschreckend, aber verhältnismäßig zur Bedeutung der Anordnung"],
                       titel="Höhe"),
                 frage("Muss die Androhung festlegen, wofür der Betrag verfällt?", True,
                       ["**Ja!** Die Androhung bestimmt das Ereignis: als Pauschale oder besser je Zeitraum, Stück oder Handlung, "
                        "gegebenenfalls mit Höchstbetrag, der später erhöht werden kann. Muss nicht sofort befolgt werden, nennt die "
                        "Entscheidung auch die Frist zur Befolgung (EPG-BerG Kodak/Fujifilm)."],
                       titel="Bestimmtheit"),
                 frage("Kann die Berichterstatterin allein das verwirkte Zwangsgeld festsetzen?", False,
                       ["**Nein!** Über die Festsetzung von Zwangsgeld nach R. 354.4 VerfO entscheidet der **Spruchkörper** (EPG-BerG "
                        "Hybridgenerator/Infotech). Er hört vorher beide Parteien an (R. 264 VerfO)."],
                       abwandlung="Fujifilm behauptet neue Verstöße und beantragt die Festsetzung.", level=3, titel="Spruchkörper",
                       cases=["upc_coa_hybridgenerator_infotech_zwangsgeld"], norms=["R. 354.4 VerfO"]),
                 ],
                abschnitt="R. 354.3 und 354.4 VerfO: Androhung und Festsetzung", level=2,
                concepts=["upc_zwangsgeld", "upc_vollstreckung"], norms=["R. 354.3 VerfO", "Art. 82 Abs. 4 EPGÜ"],
                cases=["upc_coa_kodak_fujifilm_zwangsgeld"], step="step:upc_schema_verletzungsklage.3.4"),
            *fallkette("u07c-2", "Geoblocking auf dem Marktplatz",
                "Lepu ist verboten, Herzokkluder in drei Staaten anzubieten und in Verkehr zu bringen. Lepu liefert Beschreibungen, Bilder und "
                "Preise an eine Verkaufsplattform. Für diese Staaten sperrt Lepu nur die Kaufoption; die Produktseiten bleiben abrufbar.",
                [frage("Kann Lepu die Verantwortung für die Plattform auf deren Betreiber abwälzen?", False,
                       ["**Nein!** Der Adressat eines Verbots muss **Dritte kontrollieren**, denen er Aufgaben überträgt. Liefert er die "
                        "Inhalte selbst, muss er sicherstellen, dass sie nicht gegen die Anordnung verstoßen (EPG-BerG Lepu/Occlutech)."],
                       merke="Wer Inhalte an eine Plattform liefert, haftet für sie.", titel="Kontrolle Dritter"),
                 frage("Genügt die Sperre der Kaufoption, um das Verbot zu befolgen?", False,
                       ["**Nein!** Anbieten und Inverkehrbringen sind selbständige Benutzungshandlungen (Art. 25 lit. a EPGÜ), beide sind "
                        "verboten. Die abrufbare Produktseite bleibt ein Angebot für die verbotenen Gebiete (EPG-BerG Lepu/Occlutech)."],
                       titel="Geoblocking"),
                 frage("Kann schon eine Präsentation ohne Preis ein „Angebot“ sein?", True,
                       ["**Ja!** Anbieten ist wirtschaftlich zu verstehen. Es genügt eine Präsentation, auf die Betrachter ein Angebot zur "
                        "Überlassung abgeben können; Preisangabe und Lieferbereitschaft sind nicht nötig (EPG-BerG Belkin/Philips)."],
                       level=2, titel="Begriff des Anbietens", cases=["upc_coa_belkin_philips_anbieten"], concepts=["upc_anbieten"]),
                 frage("Kann ein Disclaimer auf der Website ausreichen?", True,
                       ["**Ja!** Ein zutreffender **Website-Disclaimer** kann genügen, wenn kein Besucher den Inhalt vernünftigerweise als "
                        "Angebot für die verbotenen Gebiete verstehen kann (EPG-BerG Lepu/Occlutech)."],
                       abwandlung="Lepu ergänzt deutlich: „Nicht erhältlich in Deutschland, Frankreich und den Niederlanden.“",
                       titel="Disclaimer"),
                 ],
                abschnitt="R. 354.4 VerfO: Was Befolgung verlangt", level=3,
                concepts=["upc_vollstreckung", "upc_unterlassungsanordnung"], norms=["R. 354.4 VerfO", "Art. 25 EPGÜ", "Art. 63 EPGÜ"],
                cases=["upc_coa_lepu_occlutech_vollstreckung"], step="step:upc_schema_verletzungsklage.3.4"),
            *fallkette("u07c-3", "Berufung gegen das Zwangsgeld",
                "Die Lokalkammer setzt gegen EOFlow wegen Verstößen gegen eine einstweilige Maßnahme ein Zwangsgeld fest und lässt die "
                "Berufung nicht zu. EOFlow legt binnen 15 Tagen Berufung ein.",
                [frage("Hat die Zwangsgeldfestsetzung eine eigene Rechtsgrundlage im Vollstreckungsrecht?", True,
                       ["**Ja!** Die Festsetzung beruht auf Art. 82 Abs. 4 EPGÜ und R. 354.4 VerfO, also auf einer eigenen Rechtsgrundlage "
                        "der Vollstreckung, auch wenn sie eine einstweilige Maßnahme durchsetzt (EPG-BerG EOFlow/Insulet)."],
                       titel="Eigene Rechtsgrundlage"),
                 frage("Ist die Berufung ohne Zulassung statthaft?", False,
                       ["**Nein!** Zulassungsfrei sind nur Anordnungen nach Art. 49 Abs. 5, 59 bis 62 und 67 EPGÜ (Art. 73 Abs. 2 lit. a "
                        "EPGÜ, R. 220.1 lit. c VerfO). Für die Festsetzung verweist R. 354.4 VerfO ausdrücklich auf R. 220.2 VerfO "
                        "(EPG-BerG EOFlow/Insulet)."],
                       merke="Zwangsgeldfestsetzung: Berufung nur nach R. 220.2 VerfO.", titel="Keine freie Berufung"),
                 frage("Welcher Weg bleibt EOFlow?", 0,
                       ["Verweigert das Gericht erster Instanz die Zulassung, kann EOFlow binnen 15 Kalendertagen beim Berufungsgericht die "
                        "**Ermessensüberprüfung** beantragen (R. 220.3 VerfO). Darüber entscheidet der ständige Richter (R. 220.4 VerfO)."],
                       optionen=["Antrag auf Ermessensüberprüfung beim Berufungsgericht", "Einspruch bei der Lokalkammer",
                                 "Klage vor dem nationalen Vollstreckungsgericht"],
                       titel="Ermessensüberprüfung", concepts=["upc_ermessensueberpruefung"], norms=["R. 220.3 VerfO", "R. 220.4 VerfO"]),
                 ],
                abschnitt="Art. 73 EPGÜ: Rechtsmittel gegen das Zwangsgeld", level=3,
                concepts=["upc_zwangsgeld", "upc_berufung"], norms=["R. 354.4 VerfO", "Art. 73 Abs. 2 EPGÜ", "R. 220.2 VerfO"],
                cases=["upc_coa_eoflow_insulet_zwangsgeld_berufung"], step="step:upc_schema_verletzungsklage.3.4"),
            *fallkette("u07c-4", "Aufgehoben – und die Zwangsgelder?",
                "Kodak wurde zur Unterlassung verurteilt; wegen dreier Verstöße sind Zwangsgelder festgesetzt. Auf Kodaks Berufung hebt das "
                "Berufungsgericht die Unterlassungsanordnung auf.",
                [frage("Wirkt die Aufhebung zurück?", True,
                       ["**Ja!** Die Aufhebung nach Art. 75 Abs. 1 EPGÜ, R. 242.1 VerfO wirkt in der Regel **zurück**: Die Anordnung gilt als "
                        "nie wirksam gewesen (EPG-BerG Kodak/Fujifilm 2026)."],
                       titel="Rückwirkung"),
                 frage("Bleiben die Zwangsgelder für Verstöße vor der Aufhebung bestehen?", False,
                       ["**Nein!** Mit der Anordnung entfällt die Grundlage jeder Zwangsgeldentscheidung, auch für Verstöße vor der "
                        "Aufhebung (EPG-BerG Kodak/Fujifilm 2026)."],
                       merke="Aufhebung wirkt zurück: Mit der Anordnung fallen die Zwangsgelder.", titel="Zwangsgelder entfallen"),
                 frage("Muss Kodak Vollstreckungskosten tragen, weil sie zu spät befolgt hat?", False,
                       ["**Nein!** Rückwirkend war Kodak zu nichts verpflichtet. Ob sie unnötig Vollstreckungskosten verursacht hat, lässt "
                        "sich auf Grundlage einer nie wirksamen Entscheidung nicht beurteilen (EPG-BerG Kodak/Fujifilm 2026)."],
                       level=3, titel="Vollstreckungskosten"),
                 frage("Kann Kodak Ersatz des Schadens aus der Vollstreckung verlangen?", True,
                       ["**Ja!** Wird eine vollstreckte Entscheidung aufgehoben, kann das Gericht auf Antrag anordnen, dass der Gläubiger "
                        "angemessenen Ersatz für den durch die Vollstreckung verursachten Schaden leistet (R. 354.2 VerfO)."],
                       titel="Vollstreckungsschaden", norms=["R. 354.2 VerfO"]),
                 frage("Richtet sich der Streitwert der Berufung nach der Summe der Zwangsgelder?", False,
                       ["**Nein!** Maßgeblich ist das Interesse der Partei, die das Vollstreckungsverfahren eingeleitet hat (R. 370.6 VerfO). "
                        "Die Zwangsgelder fließen an das Gericht und messen dieses Interesse nicht (EPG-BerG Kodak/Fujifilm 2026)."],
                       level=3, titel="Streitwert", norms=["R. 370.6 VerfO"], concepts=["upc_streitwert"]),
                 ],
                abschnitt="Art. 75 EPGÜ, R. 354.2 VerfO: Aufhebung", level=3,
                concepts=["upc_vollstreckung", "upc_zwangsgeld"], norms=["Art. 75 Abs. 1 EPGÜ", "R. 242.1 VerfO"],
                cases=["upc_coa_kodak_fujifilm_aufhebung_zwangsgeld"], step="step:upc_schema_verletzungsklage.3.4"),
        ]),
    ],
)
