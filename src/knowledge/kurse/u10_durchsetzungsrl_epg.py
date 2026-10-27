# -*- coding: utf-8 -*-
"""EPGÜ und Durchsetzungsrichtlinie im Jurafuchs-Format: je Kapitel die Entsprechungen, darin kurze Fallketten mit einer Frage je
Auslegungselement (richtlinienkonforme Auslegung durch das Berufungsgericht)."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

KURS = dict(
    id="u10", gebiet="upc", kompakt="fragen", titel="EPGÜ und Durchsetzungsrichtlinie: eine Richtlinie, drei Gesetze",
    untertitel="Warum Art. 59 bis 69 und 80 EPGÜ dieselbe Struktur haben wie §§ 139 bis 140e PatG und §§ 18 bis 19c MarkenG",
    farbe="#8b3fb2", icon="richtlinie",
    beschreibung="Die Durchsetzungsrichtlinie 2004/48/EG ist der gemeinsame Nenner: Beweisvorlage, Beweissicherung, Auskunft, einstweilige Maßnahmen, Abhilfe, Unterlassung, Schadensersatz, Kosten und Veröffentlichung stehen im EPGÜ (Art. 59 bis 69, 80), im PatG (§§ 139 bis 140e) und im MarkenG (§§ 14, 18 bis 19c). Der Kurs zeigt die Entsprechungen und wie das Berufungsgericht das EPGÜ richtlinienkonform auslegt: hinreichende Sicherheit (NanoString/10x), Beweissicherung (Centripetal/Palo Alto), Mittelspersonen und Verletzerbegriff (Belkin/Philips), Auskunft (Hurom/NUC), Kostenobergrenzen und Schadensersatz ohne Strafcharakter.",
    kapitel=[
        dict(id="u10a", titel="Art. 60, 62, 63 und 67 EPGÜ ↔ Art. 7, 8, 9, 11 DurchsetzungsRL: Beweis, Eilrechtsschutz, Verbot, Auskunft", einheiten=[
            intro("u10a-0", "Eine Richtlinie, drei Gesetze",
                  "Die **Durchsetzungsrichtlinie 2004/48/EG** verpflichtet die Mitgliedstaaten, für alle Rechte des geistigen Eigentums dieselben Maßnahmen, Verfahren und Rechtsbehelfe bereitzustellen: Beweisvorlage (Art. 6 DurchsetzungsRL), Beweissicherung (Art. 7 DurchsetzungsRL), Auskunft (Art. 8 DurchsetzungsRL), einstweilige Maßnahmen (Art. 9 DurchsetzungsRL), Abhilfemaßnahmen (Art. 10 DurchsetzungsRL), gerichtliche Anordnungen einschließlich solcher gegen Mittelspersonen (Art. 11 DurchsetzungsRL), Schadensersatz (Art. 13 DurchsetzungsRL), Prozesskosten (Art. 14 DurchsetzungsRL) und Veröffentlichung (Art. 15 DurchsetzungsRL) – alles fair, wirksam, verhältnismäßig und abschreckend (Art. 3 DurchsetzungsRL). Deutschland hat sie 2008 mit dem Durchsetzungsgesetz als Artikelgesetz umgesetzt: im PatG als §§ 139 bis 140e PatG, im MarkenG als §§ 14, 18, 19 bis 19c MarkenG. Das **EPGÜ** setzt dieselbe Richtlinie für das gemeinsame Gericht um, und zwar in seinem Teil über Befugnisse des Gerichts: **Art. 59 EPGÜ ↔ Art. 6 DurchsetzungsRL** (Beweisvorlage), **Art. 60 EPGÜ ↔ Art. 7 DurchsetzungsRL** (Beweissicherung und Besichtigung), **Art. 67 EPGÜ ↔ Art. 8 DurchsetzungsRL** (Auskunft), **Art. 62 EPGÜ ↔ Art. 9 DurchsetzungsRL** (einstweilige Maßnahmen), **Art. 64 EPGÜ ↔ Art. 10 DurchsetzungsRL** (Rückruf, Entfernung, Vernichtung), **Art. 63 EPGÜ ↔ Art. 11 DurchsetzungsRL** (Unterlassung, Mittelspersonen), **Art. 68 EPGÜ ↔ Art. 13 DurchsetzungsRL** (Schadensersatz), **Art. 69 EPGÜ ↔ Art. 14 DurchsetzungsRL** (Kosten), **Art. 80 EPGÜ ↔ Art. 15 DurchsetzungsRL** (Veröffentlichung). Weil das EPG als gemeinsames Gericht der Mitgliedstaaten an das Unionsrecht gebunden ist (Art. 1 Satz 2, Art. 20 EPGÜ) und die Richtlinie nach Art. 24 Abs. 1 lit. a EPGÜ vorrangige Rechtsquelle ist, legt das Berufungsgericht die Vorschriften des EPGÜ **richtlinienkonform** aus und greift auf die Rechtsprechung des EuGH zur Richtlinie zurück. Die Tabelle zeigt die Zuordnung Artikel für Artikel mit den Regeln der VerfO und den deutschen Parallelnormen. Für die Klausur heißt das: Wer § 140b PatG oder § 19 MarkenG kennt, kennt Art. 67 EPGÜ; die Unterschiede liegen im Verfahren (Ermessen des Gerichts, Antrag, R. 191 VerfO), nicht in der Struktur.",
                  concepts=["upc_durchsetzungsrl_bezug", "durchsetzungsrl"], norms=["Art. 24 EPGÜ", "Art. 3 DurchsetzungsRL", "Art. 63 EPGÜ", "Art. 11 DurchsetzungsRL"],
                  distinctions=["d_upc_entsprechung_durchsetzungsrl"]),
            *fallkette("u10a-1", "Wie sicher ist hinreichend sicher?",
                "10x Genomics beantragt gegen NanoString einstweilige Maßnahmen aus einem Einheitspatent. Die Lokalkammer hält Berechtigung und "
                "Verletzung für überwiegend wahrscheinlich und erlässt die Anordnung. NanoString legt Berufung ein.",
                [frage("Genügt es, dass das Gericht Berechtigung und Verletzung für überwiegend wahrscheinlich hält?", True,
                       ["**Ja!** Art. 62 Abs. 4 EPGÜ und R. 211.2 VerfO verlangen **hinreichende Sicherheit**. Sie liegt vor, wenn das "
                        "Gericht Berechtigung und Verletzung für **überwiegend wahrscheinlich** hält (EPG-BerG NanoString/10x)."],
                       merke="Hinreichende Sicherheit = überwiegende Wahrscheinlichkeit (NanoString/10x).", titel="Beweismaß"),
                 frage("Woraus leitet das Berufungsgericht diesen Maßstab ab?", 0,
                       ["Es legt Art. 62 Abs. 4 EPGÜ **richtlinienkonform** aus: Nach Art. 9 Abs. 3 DurchsetzungsRL muss der Antragsteller "
                        "„mit ausreichender Sicherheit“ nachweisen, dass er Rechtsinhaber ist und sein Recht verletzt wird (EPG-BerG "
                        "NanoString/10x)."],
                       optionen=["Aus Art. 9 Abs. 3 DurchsetzungsRL", "Aus § 294 ZPO", "Aus der Praxis des EPA"],
                       titel="Richtlinienkonforme Auslegung", norms=["Art. 9 Abs. 3 DurchsetzungsRL"]),
                 frage("Fehlt die hinreichende Sicherheit schon, wenn das Patent möglicherweise nichtig ist?", False,
                       ["**Nein!** Sie fehlt erst, wenn das Gericht die Nichtigkeit des Patents für **überwiegend wahrscheinlich** hält "
                        "(EPG-BerG NanoString/10x)."],
                       level=3, titel="Rechtsbestand"),
                 frage("Wer trägt die Darlegungs- und Beweislast für die Nichtigkeit?", 1,
                       ["Für Berechtigung und Verletzung trägt sie der Antragsteller, für die **Nichtigkeit der Antragsgegner** (EPG-BerG "
                        "NanoString/10x)."],
                       optionen=["10x Genomics", "NanoString", "Das Gericht von Amts wegen"],
                       titel="Beweislast", concepts=["upc_beweismittel_beweislast"]),
                 frage("Womit gleicht die VerfO das geringere Beweismaß aus?", 0,
                       ["Mit Interessenabwägung (R. 211.3 VerfO), Dringlichkeit (R. 211.4 VerfO), Sicherheitsleistung (R. 211.5 VerfO) und "
                        "Schadensersatz bei Aufhebung (Art. 62 Abs. 5 EPGÜ i.V.m. Art. 60 Abs. 9 EPGÜ, Art. 9 Abs. 7 DurchsetzungsRL)."],
                       optionen=["Mit Abwägung, Dringlichkeit, Sicherheit und Schadensersatz bei Aufhebung",
                                 "Mit einer zweiten Tatsacheninstanz", "Gar nicht"],
                       titel="Ausgleich", norms=["R. 211.3 VerfO"]),
                 ],
                abschnitt="Art. 62 EPGÜ ↔ Art. 9 DurchsetzungsRL: einstweilige Maßnahmen", level=2,
                concepts=["upc_hinreichende_sicherheit", "upc_durchsetzungsrl_bezug"], norms=["Art. 62 Abs. 4 EPGÜ", "R. 211.2 VerfO"],
                cases=["upc_coa_nanostring_10x"], step="step:upc_schema_einstweilige_massnahmen.2.1"),
            *fallkette("u10a-2", "Beweissicherung ohne Beweis",
                "Centripetal vermutet, dass die Firewall-Software von Palo Alto ihr patentiertes Verfahren nutzt; der Quellcode ist nicht "
                "zugänglich. Sie beantragt ohne Anhörung eine Beweissicherung mit Besichtigung und legt Produktdokumentation und ein Gutachten vor.",
                [frage("Ist die Hürde niedriger als bei der Verletzungsklage?", True,
                       ["**Ja!** Die Hürde ist **niedriger**, gerade für Aspekte, zu denen der Antragsteller keinen Zugang hat. Die "
                        "Beweissicherung soll die fehlenden Beweise ja erst beschaffen (EPG-BerG Centripetal/Palo Alto)."],
                       merke="Die Besichtigung soll den Beweis erst beschaffen.", titel="Niedrigere Hürde"),
                 frage("Was muss Centripetal vorlegen?", 0,
                       ["Alle **vernünftigerweise verfügbaren Beweismittel** für die Verletzung (Art. 60 Abs. 1 EPGÜ). Art. 7 Abs. 1 "
                        "DurchsetzungsRL verwendet dieselbe Formel."],
                       optionen=["Alle vernünftigerweise verfügbaren Beweismittel", "Den Quellcode", "Ein gerichtliches Sachverständigengutachten"],
                       titel="Verfügbare Beweismittel", norms=["Art. 7 DurchsetzungsRL"]),
                 frage("Genügt die bloße Vermutung einer Verletzung?", False,
                       ["**Nein!** Um Ausforschung („fishing expeditions“) zu verhindern, muss die Verletzung **plausibel** sein. Das Beweismaß "
                        "darf weder zu hoch noch zu niedrig angesetzt werden (EPG-BerG Centripetal/Palo Alto)."],
                       titel="Plausibilität"),
                 frage("Muss Centripetal im Antrag auch ihr ungünstige Tatsachen offenlegen?", True,
                       ["**Ja!** Bei Anträgen ohne Anhörung des Gegners muss der Antragsteller alle ihm bekannten wesentlichen Tatsachen "
                        "offenlegen (R. 192.3 VerfO; EPG-BerG Ecovacs/Roborock)."],
                       level=3, titel="Offenlegungspflicht", cases=["upc_coa_ecovacs_roborock_exparte"], norms=["R. 192 VerfO"]),
                 frage("Wie wird Palo Alto bei der Besichtigung geschützt?", 2,
                       ["Die Besichtigung greift in Art. 7 GRCh ein und verlangt wirksame Schutzvorkehrungen, etwa Vertraulichkeitsanordnungen "
                        "(R. 196, R. 262A VerfO; EPG-BerG Centripetal/Palo Alto)."],
                       optionen=["Gar nicht, weil Beweissicherung geheim bleibt", "Durch eine Pflicht des Antragstellers zur Strafanzeige",
                                 "Durch Schutzvorkehrungen wie Vertraulichkeitsanordnungen"],
                       titel="Schutz des Gegners", norms=["R. 196 VerfO"]),
                 ],
                abschnitt="Art. 60 EPGÜ ↔ Art. 7 DurchsetzungsRL: Beweissicherung", level=3,
                concepts=["upc_beweissicherung", "upc_durchsetzungsrl_bezug"], norms=["Art. 60 Abs. 1 EPGÜ", "R. 194 VerfO"],
                cases=["upc_coa_centripetal_paloalto_beweissicherung"], step="step:upc_schema_beweissicherung.2.1"),
            *fallkette("u10a-3", "Geschäftsführer und Lager",
                "Philips erwirkt gegen Belkin ein Unterlassungsurteil wegen patentverletzender Ladegeräte. Philips will das Verbot auf Belkins "
                "Geschäftsführer und auf den Logistikdienstleister erstrecken, über dessen Lager die Geräte ausgeliefert werden.",
                [frage("Kann das Verbot gegen den Logistikdienstleister als Mittelsperson ergehen?", True,
                       ["**Ja!** Art. 63 Abs. 1 Satz 2 EPGÜ ist die Umsetzung von Art. 11 Satz 3 DurchsetzungsRL, den der EuGH weit versteht "
                        "(L'Oréal/eBay). Ein Logistikdienstleister, dessen Dienste der Verletzer nutzt, ist Mittelsperson; eigene "
                        "Verletzung ist nicht nötig."],
                       merke="Art. 63 EPGÜ ist Art. 11 DurchsetzungsRL: Mittelspersonen ja.", titel="Mittelsperson"),
                 frage("Ist der Geschäftsführer Mittelsperson im Sinne von Art. 63 Abs. 1 Satz 2 EPGÜ?", False,
                       ["**Nein!** Der Geschäftsführer vertritt das Unternehmen. Das Unternehmen ist ihm gegenüber nicht „Dritter“ im Sinne "
                        "von Art. 63 EPGÜ und Art. 11 DurchsetzungsRL; die Funktion allein begründet keine Haftung als Mittelsperson (EPG-BerG "
                        "Philips/Belkin 2024)."],
                       level=3, titel="Kein „Dritter“", cases=["upc_coa_philips_belkin_aufschiebend"]),
                 frage("Haftet der Geschäftsführer allein wegen seiner Organstellung als Mittäter?", False,
                       ["**Nein!** Er haftet nur, wenn er das Unternehmen zweckgerichtet zur Verletzung nutzt oder trotz Kenntnis und "
                        "Zumutbarkeit nicht einschreitet (EPG-BerG Belkin/Philips 2025). Ähnlich begrenzt der BGH die Haftung seit "
                        "Geschäftsführerhaftung (I ZR 242/12) auf eigene Pflichtverletzungen."],
                       titel="Organstellung"),
                 frage("Wird der Verletzerbegriff autonom ausgelegt?", True,
                       ["**Ja!** Verletzer ist auch, wem Handlungen Dritter als Anstifter, Mittäter oder Gehilfe zuzurechnen sind. Die "
                        "Zurechnung folgt der **autonomen Auslegung** des EPGÜ, nicht § 830 BGB (EPG-BerG Belkin/Philips 2025)."],
                       titel="Autonomer Verletzerbegriff"),
                 ],
                abschnitt="Art. 63 EPGÜ ↔ Art. 11 DurchsetzungsRL: Verletzer und Mittelspersonen", level=2,
                concepts=["upc_verletzer", "upc_unterlassungsanordnung", "upc_durchsetzungsrl_bezug"], norms=["Art. 63 Abs. 1 EPGÜ", "Art. 11 DurchsetzungsRL"],
                cases=["upc_coa_belkin_philips_anbieten"], step="step:upc_schema_verletzungsklage.3.1"),
            *fallkette("u10a-4", "Auskunft trotz Berufung",
                "Die Lokalkammer verpflichtet NUC, Hurom Auskunft über Herkunft und Vertriebswege der verletzenden Erzeugnisse zu erteilen. NUC "
                "legt Berufung ein und beantragt aufschiebende Wirkung: Mit der Auskunft liefe die Berufung insoweit leer.",
                [frage("Welcher Vorschrift der Richtlinie entspricht Art. 67 EPGÜ?", 0,
                       ["Art. 67 EPGÜ spiegelt **Art. 8 DurchsetzungsRL** (Recht auf Auskunft). Sie soll genaue Informationen über Herkunft, "
                        "Vertriebswege und beteiligte Dritte sichern (Erwägungsgrund 21; EPG-BerG Hurom/NUC)."],
                       optionen=["Art. 8 DurchsetzungsRL", "Art. 6 DurchsetzungsRL", "Art. 13 DurchsetzungsRL"],
                       titel="Art. 8 DurchsetzungsRL"),
                 frage("Wird die Auskunft nur ausnahmsweise bis zur Berufungsentscheidung ausgesetzt?", True,
                       ["**Ja!** Die Auskunft gehört zu den Maßnahmen, die ein **hohes Schutzniveau** sichern. Ihre Vollstreckung kann nur "
                        "unter außergewöhnlichen Umständen nach R. 223 VerfO ausgesetzt werden (EPG-BerG Hurom/NUC)."],
                       merke="Auskunft ist Kern der Durchsetzung; Aussetzung nur ausnahmsweise (Hurom/NUC).", titel="Nur ausnahmsweise"),
                 frage("Genügt es, dass die Auskunft den Zweck der Berufung teilweise unterläuft?", False,
                       ["**Nein!** Dass die Auskunft vor der Berufungsentscheidung den Zweck der Berufung teilweise unterläuft, reicht nicht "
                        "(EPG-BerG Hurom/NUC)."],
                       titel="Teilweise Vereitelung"),
                 frage("Was hätte NUC zeigen müssen?", 0,
                       ["NUC hätte zeigen müssen, dass die Berufung ohne aufschiebende Wirkung **gegenstandslos** würde und ihr "
                        "Geheimhaltungsinteresse das Interesse von Hurom an sofortiger Information **überwiegt**, etwa um weitere "
                        "Verletzungen zu verhindern (EPG-BerG Hurom/NUC)."],
                       optionen=["Gegenstandslosigkeit der Berufung und überwiegendes Geheimhaltungsinteresse",
                                 "Gute Erfolgsaussichten der Berufung", "Hohe Kosten der Auskunft"],
                       level=3, titel="Abwägung"),
                 ],
                abschnitt="Art. 67 EPGÜ ↔ Art. 8 DurchsetzungsRL: Auskunft", level=2,
                concepts=["upc_auskunft", "upc_aufschiebende_wirkung", "upc_durchsetzungsrl_bezug"], norms=["Art. 67 EPGÜ", "Art. 8 DurchsetzungsRL", "R. 223 VerfO"],
                cases=["upc_coa_hurom_nuc_auskunft"], step="step:upc_schema_berufung.4"),
        ]),
        dict(id="u10b", titel="Art. 68, 69 und 80 EPGÜ ↔ Art. 13, 14, 15 DurchsetzungsRL: Schadensersatz, Kosten, Veröffentlichung", einheiten=[
            intro("u10b-0", "Dieselben Rechtsfolgen, drei Adressen",
                  "**Schadensersatz**: Art. 13 Abs. 1 DurchsetzungsRL verlangt Ersatz für den Verletzer, der wusste oder vernünftigerweise hätte wissen müssen, dass er eine Verletzung begeht, bemessen entweder nach allen Aspekten einschließlich Gewinneinbußen, Verletzergewinn und immateriellem Schaden (lit. a) oder als Pauschale auf Grundlage mindestens der hypothetischen Lizenzgebühr (lit. b); für den gutgläubigen Verletzer erlaubt Abs. 2 die Herausgabe der Gewinne oder eine Entschädigung. Art. 68 EPGÜ übernimmt das nahezu wörtlich und fügt in Abs. 2 hinzu, dass der Schadensersatz keinen Strafcharakter hat; § 139 Abs. 2 PatG und § 14 Abs. 6 MarkenG enthalten dieselben drei Berechnungsarten, gehen aber mit der Verschuldenshaftung nach deutschem Muster (Vorsatz oder Fahrlässigkeit) über die Richtlinie hinaus, was Art. 2 Abs. 1 DurchsetzungsRL als günstigere Regelung erlaubt. **Kosten**: Art. 14 DurchsetzungsRL will, dass die Prozesskosten und sonstigen Kosten der obsiegenden Partei in der Regel von der unterlegenen Partei getragen werden, soweit sie **zumutbar und angemessen** sind und Billigkeitsgründe nicht entgegenstehen; Art. 69 Abs. 1 EPGÜ wiederholt das und ergänzt die **Obergrenze** nach der Verfahrensordnung, die der EuGH in United Video Properties für Pauschalen des nationalen Rechts gebilligt hat, sofern ein erheblicher und angemessener Teil der tatsächlichen Kosten erstattet wird. Im deutschen Recht leisten §§ 91 ff. ZPO mit der Erstattung nach RVG und der Streitwertbegünstigung des § 144 PatG dasselbe. **Veröffentlichung**: Art. 15 DurchsetzungsRL, Art. 80 EPGÜ, § 140e PatG und § 19c MarkenG erlauben auf Antrag des Obsiegenden und auf Kosten des Verletzers die Bekanntmachung der Entscheidung. Die Unterschiede liegen im Verfahren: Das EPG setzt die Höhe des Schadensersatzes im gesonderten Verfahren nach R. 125 ff. VerfO fest, die Kosten nach R. 150 ff. VerfO – anders als die deutsche Stufenklage mit Auskunft, Rechnungslegung und Bezifferung.",
                  concepts=["upc_schadensersatz", "upc_kostenerstattung", "upc_durchsetzungsrl_bezug"], norms=["Art. 68 EPGÜ", "Art. 13 DurchsetzungsRL", "Art. 69 Abs. 1 EPGÜ", "Art. 14 DurchsetzungsRL"]),
            *fallkette("u10b-1", "Die doppelte Lizenz",
                "Nach rechtskräftiger Verurteilung verlangt Helion im Festsetzungsverfahren von Solvix das Doppelte der üblichen Lizenzgebühr. "
                "Solvix habe trotz Abmahnung weiter verletzt; ein Zuschlag sei nötig, damit sich Verletzung nicht lohne.",
                [frage("Schließt Art. 68 EPGÜ einen Strafcharakter des Schadensersatzes aus?", True,
                       ["**Ja!** Art. 68 Abs. 2 Satz 3 EPGÜ schließt den Strafcharakter ausdrücklich aus. Ziel ist der Ausgleich des "
                        "tatsächlichen Schadens und die Abschöpfung des Nutzens (Art. 68 Abs. 1, Abs. 2 Satz 2 EPGÜ)."],
                       merke="Art. 68 Abs. 2 EPGÜ: Ausgleich und Abschöpfung, keine Strafe.", titel="Kein Strafcharakter",
                       norms=["Art. 68 Abs. 2 EPGÜ"]),
                 frage("Öffnet das Wort „mindestens“ in Art. 68 Abs. 3 lit. b EPGÜ den Weg zu einem Zuschlag?", False,
                       ["**Nein!** Die Pauschale beruht auf „mindestens“ der Lizenzgebühr. Das öffnet den Betrag für Zinsen, "
                        "Rechtsverfolgungsaufwand und die Unsicherheiten der Lizenzanalogie, nicht für einen Zuschlag als Sanktion."],
                       titel="„Mindestens“", norms=["Art. 68 Abs. 3 EPGÜ"]),
                 frage("Hätte die Richtlinie eine doppelte Lizenzgebühr erlaubt?", True,
                       ["**Ja!** Der EuGH hat in OTK (C-367/15) eine nationale Regel mit doppelter Lizenzgebühr als günstigere Vorschrift nach "
                        "Art. 2 Abs. 1 DurchsetzungsRL gebilligt. Das EPGÜ nutzt diese Option nicht, sondern schreibt in Art. 68 Abs. 2 EPGÜ "
                        "das Gegenteil fest."],
                       level=3, titel="Mindestharmonisierung", norms=["Art. 2 DurchsetzungsRL"]),
                 frage("Kennt das deutsche Recht einen Verletzerzuschlag?", False,
                       ["**Nein!** § 139 Abs. 2 PatG und § 14 Abs. 6 MarkenG gewähren die einfache Lizenzanalogie als eine von drei "
                        "Berechnungsarten."],
                       titel="Deutsches Recht"),
                 frage("Was kann Helion stattdessen tun?", 0,
                       ["Helion kann den Verletzergewinn oder den entgangenen Gewinn wählen (Art. 68 Abs. 3 lit. a EPGÜ) und die Offenlegung "
                        "der Bücher verlangen (R. 131.1 lit. c, R. 141 VerfO)."],
                       optionen=["Verletzergewinn oder entgangenen Gewinn wählen und Offenlegung der Bücher verlangen",
                                 "Einen Strafantrag beim EPG stellen", "Den Zuschlag vor einem nationalen Gericht einklagen"],
                       titel="Alternativen", norms=["R. 141 VerfO"]),
                 ],
                abschnitt="Art. 68 EPGÜ ↔ Art. 13 DurchsetzungsRL: Schadensersatz", level=2,
                concepts=["upc_schadensersatz", "upc_durchsetzungsrl_bezug"], norms=["Art. 68 EPGÜ", "Art. 13 DurchsetzungsRL"],
                step="step:upc_schema_verletzungsklage.3.3"),
            *fallkette("u10b-2", "Die Obergrenze und die Richtlinie",
                "Ilion hat gegen Tarsus obsiegt und 1,2 Mio. EUR Vertretungskosten aufgewandt. Die Obergrenze für den Streitwert liegt bei "
                "600.000 EUR. Ilion hält die Obergrenze für richtlinienwidrig.",
                [frage("Verlangt Art. 14 DurchsetzungsRL die Erstattung aller tatsächlichen Kosten?", False,
                       ["**Nein!** Die unterlegene Partei trägt die Kosten „in der Regel“ und nur, soweit sie **zumutbar und angemessen** sind "
                        "und Billigkeitsgründe nicht entgegenstehen (Art. 14 DurchsetzungsRL). Art. 69 Abs. 1 EPGÜ übernimmt das."],
                       titel="Zumutbar und angemessen"),
                 frage("Sind Obergrenzen mit Art. 14 DurchsetzungsRL vereinbar?", True,
                       ["**Ja!** Nach EuGH United Video Properties (C-57/15) sind Höchstbeträge zulässig, wenn ein **erheblicher und "
                        "angemessener Teil** der tatsächlichen zumutbaren Kosten erstattet wird. Unzulässig wären Grenzen, die von der "
                        "Durchsetzung abschrecken."],
                       merke="Obergrenzen ja, wenn ein erheblicher und angemessener Teil erstattet wird.", titel="United Video Properties"),
                 frage("Muss das EPG die Obergrenze unangewendet lassen?", False,
                       ["**Nein!** Die Obergrenzen sind streitwertgestaffelt; die Tabelle erlaubt bei besonderer Komplexität oder mehreren "
                        "Sprachen eine Anhebung auf Antrag. Ilion muss diese im Kostenfestsetzungsverfahren beantragen (R. 152, R. 156 VerfO)."],
                       level=3, titel="Anhebung statt Verwerfung", norms=["R. 152 VerfO"]),
                 ],
                abschnitt="Art. 69 EPGÜ ↔ Art. 14 DurchsetzungsRL: Kosten", level=3,
                concepts=["upc_kostenerstattung", "upc_durchsetzungsrl_bezug"], norms=["Art. 69 Abs. 1 EPGÜ", "Art. 14 DurchsetzungsRL"],
                step="step:upc_schema_verletzungsklage.3.4"),
            *fallkette("u10b-3", "Welche Norm gehört zu welcher?",
                "Eine Mandantin fragt, wo die Maßnahmen der Durchsetzungsrichtlinie im EPGÜ und im deutschen Recht stehen.",
                [frage("Wo steht die Abhilfe nach Art. 10 DurchsetzungsRL?", 0,
                       ["Art. 10 DurchsetzungsRL (Rückruf, Entfernung, Vernichtung) setzt Art. 64 EPGÜ für das EPG um, mit der zusätzlichen "
                        "Beseitigung der verletzenden Eigenschaft; im deutschen Recht § 140a PatG und § 18 MarkenG."],
                       optionen=["Art. 64 EPGÜ, § 140a PatG, § 18 MarkenG", "Art. 59 EPGÜ, § 140c PatG", "Art. 80 EPGÜ, § 140e PatG"],
                       titel="Abhilfe", norms=["Art. 64 EPGÜ", "Art. 10 DurchsetzungsRL"]),
                 frage("Wo steht die Auskunft nach Art. 8 DurchsetzungsRL?", 1,
                       ["Art. 8 DurchsetzungsRL entspricht Art. 67 EPGÜ, § 140b PatG und § 19 MarkenG. Art. 59 EPGÜ und § 140c PatG betreffen "
                        "dagegen die Beweisvorlage nach Art. 6 DurchsetzungsRL."],
                       optionen=["Art. 59 EPGÜ, § 140c PatG", "Art. 67 EPGÜ, § 140b PatG, § 19 MarkenG", "Art. 60 EPGÜ, § 19a MarkenG"],
                       titel="Auskunft", norms=["Art. 67 EPGÜ", "Art. 8 DurchsetzungsRL"]),
                 frage("Welche Vorschrift des EPGÜ entspricht den einstweiligen Maßnahmen nach Art. 9 DurchsetzungsRL?", 2,
                       ["Art. 9 DurchsetzungsRL entspricht Art. 62 EPGÜ und im deutschen Recht §§ 935 ff. ZPO. Art. 60 EPGÜ ist die "
                        "Beweissicherung nach Art. 7 DurchsetzungsRL."],
                       optionen=["Art. 60 EPGÜ", "Art. 69 EPGÜ", "Art. 62 EPGÜ"],
                       titel="Einstweilige Maßnahmen", norms=["Art. 62 EPGÜ"]),
                 frage("Wo steht die Veröffentlichung nach Art. 15 DurchsetzungsRL?", 1,
                       ["Art. 15 DurchsetzungsRL entspricht Art. 80 EPGÜ, § 140e PatG und § 19c MarkenG. Art. 69 EPGÜ regelt die Kosten nach "
                        "Art. 14 DurchsetzungsRL. Merkhilfe: Das EPGÜ folgt dem Verfahren (59, 60 – 62 – 63, 64, 67, 68 – 69 – 80)."],
                       optionen=["Art. 69 EPGÜ", "Art. 80 EPGÜ, § 140e PatG, § 19c MarkenG", "Art. 63 EPGÜ"],
                       merke="Beweis 59/60 ↔ 6/7, Eil 62 ↔ 9, Verbot 63 ↔ 11, Abhilfe 64 ↔ 10, Auskunft 67 ↔ 8, Schaden 68 ↔ 13, Kosten 69 ↔ 14, Veröffentlichung 80 ↔ 15.",
                       titel="Veröffentlichung", norms=["Art. 80 EPGÜ"]),
                 ],
                abschnitt="Überblick: die Entsprechungen", level=1,
                concepts=["upc_durchsetzungsrl_bezug", "upc_abhilfemassnahmen"], norms=["Art. 64 EPGÜ", "Art. 10 DurchsetzungsRL"],
                step="step:upc_schema_verletzungsklage.3.2"),
        ]),
    ],
)
