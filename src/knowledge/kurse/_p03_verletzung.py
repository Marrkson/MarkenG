# -*- coding: utf-8 -*-
"""Kapitel des Normkurses p03 (siehe p03_patg_normen.py). Jedes Kapitel trägt `order` (Sortierschlüssel nach Gesetz und Paragraph).

Teil Schutzbereich, Benutzung und Anspruchsgrundlagen der Verletzungsklage: §§ 6, 8, 9, 10, 11, 12, 14, 24, 33, 139, 140a bis 140e,
141, 141a, 145 PatG. Die Fälle folgen BGH-Entscheidungen des X. Zivilsenats (patent/cases.py, patent/cases_p03b.py); Sachverhalte und
Prüfungspunkte aus den Volltexten der RheinIP-Datenbank. Fälle ohne `cases` sind Lehrfälle."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

VS = "step:pat_schema_patentverletzung"

KAPITEL = [
    # ================================================================== §§ 6, 8 PatG
    dict(id="p03n6", order=600, titel="§§ 6, 8 PatG: Recht auf das Patent und Vindikation", einheiten=[
        intro("p03n6-0", "Wem die Erfindung gehört",
              "§ 6 S. 1 PatG weist das Recht auf das Patent dem Erfinder oder seinem Rechtsnachfolger zu. Miterfindern steht es "
              "gemeinschaftlich zu (§ 6 S. 2 PatG), bei unabhängigen Doppelerfindungen dem Erstanmelder (§ 6 S. 3 PatG). Im Verfahren vor dem "
              "DPMA gilt der Anmelder als berechtigt (§ 7 Abs. 1 PatG). Der wahre Berechtigte wehrt sich mit der Vindikation: Abtretung des "
              "Erteilungsanspruchs (§ 8 S. 1 PatG), nach Erteilung Übertragung des Patents (§ 8 S. 2 PatG), durch Klage binnen zwei Jahren nach "
              "Veröffentlichung der Erteilung (§ 8 S. 3 PatG), länger nach einem Einspruch (§ 8 S. 4 PatG) und gegen den bösgläubigen Inhaber "
              "(§ 8 S. 5 PatG). Für europäische Anmeldungen und Patente gilt Art. II § 5 IntPatÜG. Prüfung: Lehre des Klägers, Übereinstimmung "
              "mit der Anmeldung, Umfang (Übertragung oder Mitberechtigung), Frist und Verjährung.",
              norms=["§ 6 PatG", "§ 7 PatG", "§ 8 PatG", "Art. II § 5 IntPatÜG"], concepts=["pat_recht_auf_patent"], abschnitt="Überblick"),
        *fallkette("p03n6-1", "Die Mitralklappe",
            "Das US-Unternehmen K entwickelt Rahmen für Mitralklappenprothesen und schickt der Firma N unter einer Geheimhaltungsvereinbarung "
            "Konstruktionsunterlagen. Nach dem Ende der Zusammenarbeit meldet N eine Mitralklappenprothese beim EPA an. K verlangt Abtretung "
            "der Anmeldung, hilfsweise eine Mitberechtigung.",
            [frage("Auf welche Vorschrift stützt K den Anspruch auf Abtretung der europäischen Anmeldung?", 1,
                   ["**Art. II § 5 Abs. 1 IntPatÜG.** Er gibt dem nach Art. 60 Abs. 1 EPÜ Berechtigten, dessen Erfindung ein Nichtberechtigter "
                    "angemeldet hat, den Anspruch auf Abtretung des Erteilungsanspruchs und nach Erteilung auf Übertragung des Patents; er "
                    "entspricht § 8 S. 1 und 2 PatG. Art. 61 EPÜ regelt erst das Verfahren vor dem EPA nach einer rechtskräftigen Entscheidung."],
                   optionen=["§ 8 S. 1 PatG unmittelbar", "Art. II § 5 Abs. 1 IntPatÜG", "§ 812 Abs. 1 BGB", "Art. 61 EPÜ"],
                   merke="Europäische Anmeldung: Vindikation aus Art. II § 5 IntPatÜG, nationale: § 8 PatG.", titel="Anspruchsgrundlage", level=1,
                   norms=["Art. II § 5 Abs. 1 IntPatÜG"]),
             frage("Genügt es für die widerrechtliche Entnahme, dass die Anmeldung von N im Gesamteindruck den Unterlagen von K ähnelt?", False,
                   ["**Nein!** Ob und inwieweit eine Entnahme vorliegt, ist in einer Gesamtschau zu beurteilen, die auf **festgestellten "
                    "Übereinstimmungen** zwischen der als entnommen geltend gemachten und der angemeldeten Lehre beruht. Das Gericht muss Merkmal "
                    "für Merkmal klären, was N aus den Unterlagen von K übernommen hat (BGH Mitralklappenprothese)."],
                   merke="Erst Übereinstimmungen feststellen, dann gesamtschauend bewerten.", titel="Prüfender Vergleich", level=2,
                   cases=["pat_bgh_mitralklappenprothese"]),
             frage("Kann K weiter die volle Abtretung verlangen?", False,
                   ["**Nein!** Geht die Anmeldung nur teilweise auf den Beitrag des Berechtigten zurück, kann er nur die **Einräumung einer "
                    "Mitberechtigung** verlangen, auch wenn die Anmeldung teilbar wäre (BGH Blendschutzbehang). Den Umfang ergibt der prüfende "
                    "Vergleich der Lehren (BGH Brustimplantat)."],
                   abwandlung="Die Anmeldung enthält neben dem Rahmen von K eine eigene, wesentliche Klappenbefestigung, die N entwickelt hat.",
                   merke="Teilweise Entnahme: Mitberechtigung statt Übertragung.", titel="Mitberechtigung", level=2,
                   cases=["pat_bgh_blendschutzbehang", "pat_bgh_brustimplantat"]),
             ],
            abschnitt="S. 1 und 2: Abtretung und Übertragung", level=1, concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG"],
            cases=["pat_bgh_mitralklappenprothese"]),
        *fallkette("p03n6-2", "Die Stromdüse",
            "Berater K schlägt dem Schweißtechnikhersteller B vor, Stromdüsen im Tiefbohrverfahren herzustellen. B meldet das Verfahren mit "
            "ihrem Ingenieur S als Alleinerfinder zum Patent an. K klagt auf Übertragung des Patents. Im Prozess stellt sich heraus, dass K und "
            "S die Lösung gemeinsam gefunden haben.",
            [frage("Muss das Gericht die Klage abweisen, weil K nur die volle Übertragung beantragt hat?", False,
                   ["**Nein!** Der Anspruch auf Einräumung einer Mitberechtigung ist gegenüber dem Übertragungsanspruch des Alleinerfinders ein "
                    "**Minus**; er ist im Verlangen nach voller Übertragung von vornherein enthalten (BGH Schneidbrennerstromdüse). Das Gericht "
                    "kann K die Mitberechtigung zusprechen, ohne über den Antrag hinauszugehen (§ 308 Abs. 1 ZPO)."],
                   merke="Mitberechtigung ist im Übertragungsantrag enthalten.", titel="Mitberechtigung als Minus", level=2,
                   cases=["pat_bgh_schneidbrennerstromduese"]),
             frage("Steht K und S das Recht auf das Patent gemeinschaftlich zu?", True,
                   ["**Ja!** Haben mehrere gemeinsam eine Erfindung gemacht, steht ihnen das Recht auf das Patent gemeinschaftlich zu "
                    "(§ 6 S. 2 PatG). Ohne abweichende Vereinbarung bilden Miterfinder eine **Bruchteilsgemeinschaft** nach §§ 741 ff. BGB; "
                    "jeder kann über seinen Anteil frei verfügen (BGH Rollenantriebseinheit)."],
                   merke="Miterfinder = Bruchteilsgemeinschaft (§§ 741 ff. BGB).", titel="Miterfinder", level=1,
                   norms=["§ 6 PatG"], cases=["pat_bgh_rollenantriebseinheit"]),
             frage("Kann das Gericht K eine Mitberechtigung allein an diesem Anspruch einräumen?", False,
                   ["**Nein!** Eine Mitberechtigung kann nur an der Patentanmeldung oder dem Patent **als Ganzem** eingeräumt werden, nicht an "
                    "einzelnen Patentansprüchen (BGH Blendschutzbehang). Der Beitrag von K bestimmt nur die Höhe seines Anteils."],
                   abwandlung="K verlangt die Mitberechtigung nur an Anspruch 3, der das Tiefbohrverfahren enthält.",
                   merke="Mitberechtigung nur am ganzen Schutzrecht.", titel="Keine Teilmitberechtigung", level=2,
                   cases=["pat_bgh_blendschutzbehang"]),
             frage("Ist die Alleinanmeldung durch B als notwendige Maßnahme zur Erhaltung der gemeinsamen Erfindung gedeckt?", False,
                   ["**Nein!** Stehen Miterfindern die Rechte in Bruchteilsgemeinschaft zu, ist die Anmeldung durch einen Mitberechtigten **nur im "
                    "eigenen Namen** keine notwendige Erhaltungsmaßnahme (§ 744 Abs. 2 BGB). Der übergangene Mitberechtigte hat einen "
                    "Schadensersatzanspruch, der auch einen Ausgleich für gezogene Gebrauchsvorteile umfassen kann (BGH Beschichtungsverfahren)."],
                   abwandlung="K war Miterfinder; B hat allein im eigenen Namen angemeldet und nutzt das Verfahren seit Jahren.",
                   merke="Alleinanmeldung im eigenen Namen: Ersatzpflicht gegenüber Miterfindern.", titel="Alleinanmeldung", level=3,
                   cases=["pat_bgh_beschichtungsverfahren"]),
             ],
            abschnitt="Miterfinder (S. 2)", level=1, concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG", "§ 6 PatG"],
            cases=["pat_bgh_schneidbrennerstromduese"]),
        *fallkette("p03n6-3", "Der Brennerreiniger",
            "B entwickelt eine Reinigungseinrichtung für Schweißbrenner und führt sie Anfang 1983 einem Kunden vor. Kurz darauf meldet M die "
            "Einrichtung zum Patent an; das Patent geht später auf K über. Viele Jahre nach der Erteilung verklagt K den B wegen "
            "Patentverletzung. B beruft sich auf widerrechtliche Entnahme.",
            [frage("Kann B von K noch die Übertragung des Patents verlangen, wenn K gutgläubig erworben hat?", False,
                   ["**Nein!** Der Vindikationsanspruch kann nur binnen **zwei Jahren nach Veröffentlichung der Erteilung** durch Klage geltend "
                    "gemacht werden (§ 8 S. 3 PatG); ein Einspruch wegen widerrechtlicher Entnahme verlängert die Frist bis ein Jahr nach "
                    "Abschluss des Einspruchsverfahrens (§ 8 S. 4 PatG). Beide Fristen sind abgelaufen."],
                   merke="Vindikation: zwei Jahre ab Veröffentlichung der Erteilung.", titel="Zweijahresfrist", level=1,
                   norms=["§ 8 PatG"]),
             frage("Kann B die Entnahme dem gutgläubigen K wenigstens als Einwand gegen die Verletzungsklage entgegenhalten?", False,
                   ["**Nein!** Nach Ablauf der Fristen des § 8 S. 3 und 4 PatG kann der Beklagte die widerrechtliche Entnahme nur einem "
                    "Patentinhaber entgegenhalten, der beim Erwerb **nicht in gutem Glauben** war. Der gutgläubige Inhaber handelt nicht arglistig, "
                    "wenn er seine verfestigte Rechtsstellung nutzt (BGH Schweißbrennerreinigung)."],
                   merke="Nach Fristablauf kein Entnahmeeinwand gegen den gutgläubigen Inhaber.", titel="Entnahmeeinwand", level=2,
                   cases=["pat_bgh_schweissbrennerreinigung"]),
             frage("Kann B sich jetzt auf die widerrechtliche Entnahme berufen?", True,
                   ["**Ja!** Die Fristen gelten nicht, wenn der Patentinhaber beim Erwerb des Patents **nicht in gutem Glauben** war "
                    "(§ 8 S. 5 PatG). Maßgeblich ist der gute Glaube des jetzigen Inhabers im Zeitpunkt seines Erwerbs (BGH Schweißbrennerreinigung). "
                    "B muss aber beweisen, dass M die Erfindung ihm entnommen hat."],
                   abwandlung="K wusste beim Erwerb des Patents, dass B die Einrichtung schon vor der Anmeldung vorgeführt hatte.",
                   merke="Bösgläubiger Erwerber: keine Ausschlussfrist (§ 8 S. 5 PatG).", titel="Bösgläubiger Erwerber", level=2,
                   cases=["pat_bgh_schweissbrennerreinigung"]),
             ],
            abschnitt="S. 3 bis 5: Frist und guter Glaube", level=2, concepts=["pat_recht_auf_patent"], norms=["§ 8 PatG"],
            cases=["pat_bgh_schweissbrennerreinigung"]),
        *fallkette("p03n6-4", "Die PCR-Kooperation",
            "K und B arbeiten an Echtzeit-PCR-Geräten zusammen. Nach dem Ende der Kooperation meldet B 2010 beim EPA eine Erfindung an, die "
            "nach Ansicht von K auf ihren Entwicklungen beruht; K fordert schon 2013 schriftlich die Übertragung. Die Erteilung wird im "
            "Dezember 2016 bekannt gemacht, K klagt im Februar 2017.",
            [frage("Verjährt der Übertragungsanspruch aus Art. II § 5 Abs. 1 IntPatÜG in dreißig Jahren?", False,
                   ["**Nein!** Der Anspruch ist kein Herausgabeanspruch aus einem dinglichen Recht im Sinne von § 197 Abs. 1 Nr. 2 BGB; er "
                    "unterliegt der **regelmäßigen Verjährung von drei Jahren** (§ 195 BGB) (BGH Automatisierte Wärmebehandlung)."],
                   merke="Vindikation verjährt nach § 195 BGB in drei Jahren.", titel="Verjährungsfrist", level=2,
                   cases=["pat_bgh_automatisierte_waermebehandlung"]),
             frage("Begann die Verjährung schon 2013, weil K damals alles wusste?", False,
                   ["**Nein!** Die Verjährung beginnt **frühestens mit dem Schluss des Jahres, in dem das Patent erteilt worden ist** (BGH "
                    "Automatisierte Wärmebehandlung), hier mit Ablauf des Jahres 2016. Ansprüche auf Teilanmeldungen und die darauf erteilten "
                    "Patente sind gesondert zu beurteilen."],
                   merke="Verjährungsbeginn frühestens Ende des Erteilungsjahres.", titel="Verjährungsbeginn", level=2,
                   cases=["pat_bgh_automatisierte_waermebehandlung"]),
             frage("Hat K auch die zweijährige Ausschlussfrist für die Klage gewahrt?", True,
                   ["**Ja!** Der Übertragungsanspruch kann binnen **zwei Jahren** nach dem Hinweis auf die Erteilung im Europäischen Patentblatt "
                    "gerichtlich geltend gemacht werden (Art. II § 5 Abs. 2 IntPatÜG). Die Klage folgt zwei Monate nach dem Hinweis."],
                   merke="Ausschlussfrist zwei Jahre ab Hinweis auf die Erteilung.", titel="Ausschlussfrist", level=1,
                   norms=["Art. II § 5 Abs. 2 IntPatÜG"]),
             frage("Verliert K dann auch den Anspruch auf Ersatz für die Nutzung der Erfindung durch B?", False,
                   ["**Nein!** Die Verjährung des Vindikationsanspruchs steht Ansprüchen auf **Schadensersatz und Herausgabe von Vorteilen** aus "
                    "der Nutzung der zu Unrecht angemeldeten Erfindung nicht entgegen (BGH Automatisierte Wärmebehandlung, im Anschluss an "
                    "Steuervorrichtung)."],
                   abwandlung="Der Übertragungsanspruch von K wäre verjährt.",
                   merke="Verjährte Vindikation lässt Ausgleichsansprüche bestehen.", titel="Ersatzansprüche", level=3,
                   cases=["pat_bgh_automatisierte_waermebehandlung"]),
             ],
            abschnitt="Europäisches Patent: Art. II § 5 IntPatÜG", level=2, concepts=["pat_recht_auf_patent"],
            norms=["Art. II § 5 Abs. 1 IntPatÜG"], cases=["pat_bgh_automatisierte_waermebehandlung"]),
    ]),
    # ================================================================== § 9 PatG
    dict(id="p03n9", order=900, titel="§ 9 PatG: Unmittelbare Benutzung und Erschöpfung", einheiten=[
        intro("p03n9-0", "Die Benutzungshandlungen",
              "§ 9 S. 1 PatG gibt allein dem Patentinhaber die Befugnis, die Erfindung zu benutzen. § 9 S. 2 PatG zählt abschließend auf, was "
              "Dritten ohne Zustimmung verboten ist: beim **Erzeugnis** Herstellen, Anbieten, Inverkehrbringen, Gebrauchen sowie Einführen oder "
              "Besitzen zu diesen Zwecken (Nr. 1); beim **Verfahren** das Anwenden und, bei Kenntnis oder Offensichtlichkeit, das Anbieten zur "
              "Anwendung im Inland (Nr. 2); beim **unmittelbaren Verfahrenserzeugnis** dieselben Handlungen wie bei Nr. 1 außer dem Herstellen "
              "(Nr. 3). Jede Handlung ist selbständig und muss im Inland stattfinden. Ungeschrieben gilt die **Erschöpfung**: Was der Inhaber "
              "oder ein Dritter mit seiner Zustimmung im EWR in Verkehr gebracht hat, darf bestimmungsgemäß gebraucht und weiterverkauft "
              "werden; die Neuherstellung bleibt verboten.",
              norms=["§ 9 PatG"], concepts=["pat_benutzungshandlungen", "pat_erschoepfung"], abschnitt="Überblick"),
        *fallkette("p03n9-1", "Der Wäschebügel",
            "K hat ein Gebrauchsmuster auf einen Wäschebügel aus Kunststoff. Hersteller B stellt einer großen Handelskette seine Bügel vor, "
            "damit sie in deren Liste zugelassener Bügel aufgenommen werden. Die Lieferanten der Kette bestellen daraufhin bei B und liefern ihre "
            "Wäsche auf diesen Bügeln an die deutschen Filialen.",
            [frage("Hat B die Bügel der Handelskette angeboten, obwohl die Kette selbst keine Bügel kaufen will?", True,
                   ["**Ja!** Anbieten ist jede Handlung, die das Erzeugnis der Nachfrage zum Erwerb zugänglich macht. Das Vorstellen zur Aufnahme "
                    "in die **Listung** ist ein an das Handelsunternehmen gerichtetes Angebot, weil die Listung die Lieferanten veranlasst, die "
                    "Bügel nachzufragen (BGH Kunststoffbügel). Das gilt für § 9 S. 2 Nr. 1 PatG und § 11 Abs. 1 GebrMG gleichermaßen."],
                   merke="Anbieten verlangt keinen Kaufvertrag mit dem Angebotsempfänger.", titel="Vorstellen zur Listung", level=1),
             frage("Umfasst der Schadensersatz für das Anbieten auch den Schaden aus den Bügelbestellungen der Lieferanten?", True,
                   ["**Ja!** Die Ersatzpflicht für die Benutzungsform des Anbietens erfasst auch den Schaden aus Lieferungen Dritter, die durch "
                    "das Angebot **adäquat und zurechenbar verursacht** worden sind (BGH Kunststoffbügel; § 139 Abs. 2 PatG, § 24 Abs. 2 GebrMG)."],
                   merke="Das Angebot haftet für die Geschäfte, die es auslöst.", titel="Schaden aus Folgegeschäften", level=2,
                   norms=["§ 139 Abs. 2 PatG"]),
             ],
            abschnitt="S. 2 Nr. 1: Anbieten", level=1, concepts=["pat_benutzungshandlungen"], norms=["§ 9 PatG"],
            cases=["pat_bgh_kunststoffbuegel"], step=VS + ".3.1"),
        *fallkette("p03n9-2", "Die Anzeige in der Ärztezeitung",
            "Das ergänzende Schutzzertifikat von K für den Wirkstoff Simvastatin läuft am 6. Mai 2003 ab. Generikahersteller B wirbt ab März "
            "2003 in der Ärztezeitung für sein Simvastatin-Präparat, das ab 7. Mai lieferbar sei.",
            [frage("Wie ist die Werbung im März und April 2003 zu beurteilen?", 1,
                   ["**Als patentverletzendes Anbieten.** Für das Schutzzertifikat gelten die Vorschriften über die Wirkung des Patents (§ 16a Abs. 2 PatG). Dass "
                    "sich das Angebot auf Lieferungen **nach Ablauf** der Schutzdauer bezieht, steht der Verletzung durch Anbieten nicht entgegen "
                    "(BGH Simvastatin). Das Anbieten ist eine selbständige Benutzungshandlung."],
                   optionen=["Keine Verletzung, weil die Lieferung erst nach Ablauf erfolgt", "Verletzung durch Anbieten",
                             "Nur mittelbare Verletzung nach § 10 PatG", "Nur Vorbereitungshandlung ohne Rechtsfolgen"],
                   merke="Angebot in der Laufzeit verletzt, auch für Lieferung danach.", titel="Angebot vor Ablauf", level=1,
                   norms=["§ 16a PatG"], cases=["pat_bgh_simvastatin"]),
             frage("Kommt es darauf an, ob die Anzeige die geschützten Merkmale des Erzeugnisses erkennen lässt?", False,
                   ["**Nein!** Ein Werbemittel mit der Darstellung eines patentgemäßen Erzeugnisses ist in aller Regel ein Anbieten. Ob es die "
                    "Merkmale offenbart, ist gleichgültig, wenn **objektiv** ein Erzeugnis angeboten wird, das sie aufweist (BGH Kupplung für "
                    "optische Geräte)."],
                   merke="Maßgeblich ist das angebotene Erzeugnis, nicht der Inhalt der Werbung.", titel="Werbung ohne Merkmale", level=2,
                   cases=["pat_bgh_kupplung_optische_geraete"]),
             frage("Kann K noch Unterlassung der Werbung verlangen, nachdem das Schutzzertifikat abgelaufen ist?", False,
                   ["**Nein!** Der Unterlassungsanspruch (§ 139 Abs. 1 PatG) sichert nur künftige Benutzungen; mit dem Ende des Schutzes kann "
                    "keine Verletzung mehr drohen. Für die Angebote während der Laufzeit bleiben **Schadensersatz**, Auskunft und Rechnungslegung."],
                   abwandlung="K klagt erst im Juni 2003.",
                   merke="Nach Schutzablauf nur noch Ansprüche für die Vergangenheit.", titel="Unterlassung nach Ablauf", level=1,
                   norms=["§ 139 Abs. 1 PatG"], step=VS + ".5.1"),
             ],
            abschnitt="S. 2 Nr. 1: Anbieten", level=1, concepts=["pat_benutzungshandlungen"], norms=["§ 9 PatG"],
            cases=["pat_bgh_simvastatin"], step=VS + ".3.1"),
        *fallkette("p03n9-3", "Die Testbestellung",
            "K hat ein Patent auf ein Verfahren zur Codierung von Videobildern. Eine von K beauftragte Testkäuferin schickt dem griechischen "
            "Presswerk B ein Masterband mit bereits codierten Videodaten und bestellt DVDs. B presst die DVDs und liefert sie nach Köln; eine "
            "Lizenz hat B nicht.",
            [frage("Kann die codierte Videodatenfolge ein unmittelbares Verfahrenserzeugnis sein?", True,
                   ["**Ja!** Eine Folge von Videobilddaten kann unmittelbares Ergebnis eines Herstellungsverfahrens sein und genießt dann "
                    "**Erzeugnisschutz** nach § 9 S. 2 Nr. 3 PatG (BGH MPEG-2-Videosignalcodierung). Anders das bloße Ergebnis eines "
                    "Analyseverfahrens: Information ohne sachlich-technische, durch das Verfahren geprägte Eigenschaften ist kein Erzeugnis (BGH "
                    "Rezeptortyrosinkinase II)."],
                   merke="Datenfolge mit technischen Eigenschaften = Verfahrenserzeugnis.", titel="Datenfolge als Erzeugnis", level=2,
                   concepts=["pat_verfahrenserzeugnis"], cases=["pat_bgh_rezeptortyrosinkinase_ii"]),
             frage("Erfasst der Schutz auch die DVDs, auf die B die Daten presst?", True,
                   ["**Ja!** Der Erzeugnisschutz erstreckt sich auf jeden **Datenträger**, auf dem die erfindungsgemäß gewonnene Datenfolge "
                    "gespeichert ist oder der eine Vervielfältigung eines solchen Datenträgers darstellt (BGH MPEG-2-Videosignalcodierung)."],
                   merke="Der Datenträger teilt den Schutz der Datenfolge.", titel="Datenträger", level=2),
             frage("Ist die Lieferung der DVDs nach Köln patentverletzend?", False,
                   ["**Nein!** Das Masterband hat die Testkäuferin im Auftrag von K, also **mit Zustimmung** des Inhabers in Verkehr gebracht. "
                    "Die Herstellung weiterer Datenträger mit der Datenfolge hält sich dann im Rahmen des bestimmungsgemäßen Gebrauchs, den die "
                    "**Erschöpfung** erlaubt (BGH MPEG-2-Videosignalcodierung)."],
                   merke="Testkauf mit eigenem Material: Erschöpfung.", titel="Erschöpfung beim Testkauf", level=3,
                   concepts=["pat_erschoepfung"], step=VS + ".4.2"),
             frage("Kann K trotzdem Unterlassung künftiger Lieferungen verlangen?", True,
                   ["**Ja!** Auch eine rechtmäßige Lieferung kann die **Gefahr künftiger Verletzungen** begründen, wenn der Lieferant in "
                    "Unkenntnis der Erschöpfung gehandelt hat: B hätte ebenso Masterbänder ohne Lizenz verarbeitet (BGH "
                    "MPEG-2-Videosignalcodierung; § 139 Abs. 1 S. 2 PatG)."],
                   merke="Wer nicht weiß, dass er erschöpfte Ware liefert, zeigt Begehungsgefahr.", titel="Begehungsgefahr", level=3,
                   norms=["§ 139 Abs. 1 PatG"], concepts=["pat_unterlassung"], step=VS + ".5.1"),
             ],
            abschnitt="S. 2 Nr. 3: Unmittelbares Verfahrenserzeugnis", level=2, concepts=["pat_verfahrenserzeugnis"], norms=["§ 9 PatG"],
            cases=["pat_bgh_mpeg2_videosignalcodierung"], step=VS + ".3.1"),
        *fallkette("p03n9-4", "Die Bremsbeläge",
            "K hat ein Patent auf eine Scheibenbremse, bei der ein Bremsträger die Bremsbeläge führt; die Beläge sind Teil des Anspruchs. B "
            "verkauft Ersatzbelagsätze mit Verschleißblechen für die Bremsen, die K selbst in Verkehr gebracht hat. K sieht darin eine "
            "mittelbare Patentverletzung.",
            [frage("Darf der Käufer einer von K verkauften Bremse abgefahrene Beläge ersetzen?", True,
                   ["**Ja!** Mit dem Inverkehrbringen durch den Inhaber ist das Patent an diesem Exemplar **erschöpft**. Zum bestimmungsgemäßen "
                    "Gebrauch gehört auch die Erhaltung der Gebrauchstauglichkeit; gehört der Austausch bestimmter Teile dazu, darf er erfolgen "
                    "(BGH Palettenbehälter II)."],
                   merke="Erschöpfung deckt Gebrauch und Erhaltung, nicht Neuherstellung.", titel="Bestimmungsgemäßer Gebrauch", level=1,
                   cases=["pat_bgh_palettenbehaelter_ii"]),
             frage("Ist der Belagwechsel eine Neuherstellung, weil die Beläge im Anspruch stehen und verschleißen?", False,
                   ["**Nein!** Neuherstellung liegt nur vor, wenn sich die **technischen Wirkungen der Erfindung** in den ausgetauschten Teilen "
                    "widerspiegeln, weil diese in besonderer, auf die Erfindung abgestimmter Weise ausgestaltet sind, etwa durch ihre Form. Dass "
                    "ein Teil bloß verschleißt, genügt nicht (BGH Scheibenbremse II)."],
                   merke="Verschleiß allein macht den Austausch nicht zur Neuherstellung.", titel="Keine Neuherstellung", level=2),
             frage("Verletzt B das Patent mittelbar (§ 10 Abs. 1 PatG)?", False,
                   ["**Nein!** § 10 Abs. 1 PatG verbietet nur die Lieferung an Personen, die zur Benutzung nicht berechtigt sind. Die Käufer "
                    "dürfen die Beläge wechseln, weil dies durch die Erschöpfung gedeckt ist. Der BGH hat die Klage deshalb abgewiesen (BGH "
                    "Scheibenbremse II)."],
                   merke="Liefern für erlaubte Reparatur ist keine mittelbare Verletzung.", titel="Keine mittelbare Verletzung", level=2,
                   norms=["§ 10 Abs. 1 PatG"], concepts=["pat_mittelbare_verletzung"]),
             frage("Kann der Austausch jetzt eine Neuherstellung sein?", True,
                   ["**Ja!** Treten die technischen Wirkungen der Erfindung **gerade in dem ausgewechselten Teil** in Erscheinung, kann sein "
                    "Austausch der Neuherstellung gleichkommen, auch wenn er üblich ist (BGH Pipettensystem, Palettenbehälter II). Dann wird "
                    "der Abnehmer zum Verletzer und B liefert an einen Nichtberechtigten."],
                   abwandlung="Die Beläge haben eine besondere, auf die Führung im Bremsträger abgestimmte Form, in der sich die Erfindung zeigt.",
                   merke="Erfindung steckt im Teil: Austausch kann Neuherstellung sein.", titel="Erfindungswesentliches Teil", level=3,
                   cases=["pat_bgh_pipettensystem", "pat_bgh_palettenbehaelter_ii"]),
             ],
            abschnitt="Erschöpfung und Neuherstellung", level=2, concepts=["pat_erschoepfung"], norms=["§ 9 PatG"],
            cases=["pat_bgh_scheibenbremse_ii"], step=VS + ".4.2"),
        *fallkette("p03n9-5", "Die Einparksensoren",
            "Der taiwanische Hersteller B liefert in Asien Ultraschallwandler für Einparkhilfen an einen Automobilzulieferer, der sie in "
            "Fahrzeuge einbaut, die auch in Deutschland verkauft werden. K hat ein deutsches Patent auf den Wandler und weist B schriftlich "
            "auf diese Lieferwege hin. B liefert weiter.",
            [frage("Muss ein ausländischer Lieferant grundsätzlich überwachen, ob sein ausländischer Abnehmer die Ware nach Deutschland bringt?", False,
                   ["**Nein!** Ein im Ausland ansässiger Lieferant, der einen ebenfalls im Ausland ansässigen Abnehmer beliefert, ist **nicht ohne "
                    "weiteres** verpflichtet, die weitere Verwendung der Ware zu prüfen oder zu überwachen (BGH Abdichtsystem)."],
                   merke="Keine generelle Überwachungspflicht des Auslandslieferanten.", titel="Keine Überwachungspflicht", level=2,
                   cases=["pat_bgh_abdichtsystem"]),
             frage("Haftet B nach dem Hinweis von K für die weiteren Lieferungen?", True,
                   ["**Ja!** Liegen **konkrete Anhaltspunkte** vor, dass der Abnehmer die Ware im Inland anbieten oder in Verkehr bringen wird, "
                    "muss der Lieferant den Sachverhalt prüfen. Wer schuldhaft eine fremde Verletzung im Inland ermöglicht oder fördert, haftet "
                    "nach §§ 139 ff. PatG, sofern es zur Verletzung gekommen ist oder sie droht (BGH Abdichtsystem, Ultraschallwandler)."],
                   merke="Konkrete Anhaltspunkte begründen eine Prüfungspflicht.", titel="Prüfungspflicht", level=2,
                   norms=["§ 139 PatG"], cases=["pat_bgh_abdichtsystem"]),
             frage("Kann K verlangen, dass B jegliche Lieferungen an alle Abnehmer unterlässt?", False,
                   ["**Nein!** Ansprüche wegen Lieferungen an **andere Abnehmer** bestehen nur, soweit dort dieselben charakteristischen Umstände "
                    "vorliegen, die die Lieferung an den ersten Abnehmer rechtswidrig machen. Antrag und Urteil müssen diese Umstände konkret "
                    "umschreiben (BGH Ultraschallwandler)."],
                   merke="Verbot nur für Lieferungen unter denselben Umständen.", titel="Reichweite des Verbots", level=3),
             ],
            abschnitt="Inlandsbezug: Lieferungen aus dem Ausland", level=2, concepts=["pat_benutzungshandlungen"], norms=["§ 9 PatG"],
            cases=["pat_bgh_ultraschallwandler"], step=VS + ".3.1"),
    ]),
    # ================================================================== § 10 PatG
    dict(id="p03n10", order=1000, titel="§ 10 PatG: Mittelbare Patentverletzung", einheiten=[
        intro("p03n10-0", "Tatbestand der mittelbaren Verletzung",
              "§ 10 Abs. 1 PatG verlagert den Schutz vor: Verboten ist schon das **Anbieten oder Liefern von Mitteln** an Nichtberechtigte. "
              "Prüfung: (1) Mittel, das sich auf ein **wesentliches Element** der Erfindung bezieht; (2) Anbieten oder Liefern im Inland an "
              "nicht zur Benutzung Berechtigte; (3) zur Benutzung der Erfindung im Inland (**doppelter Inlandsbezug**); (4) objektive Eignung "
              "und Bestimmung durch den Abnehmer; (5) Wissen des Lieferanten oder Offensichtlichkeit, jeweils im Zeitpunkt von Angebot oder "
              "Lieferung. Ausnahme für **allgemein im Handel erhältliche Erzeugnisse**, es sei denn, der Lieferant veranlasst den Abnehmer "
              "bewusst zur Verletzung (§ 10 Abs. 2 PatG). Wer nach § 11 Nr. 1 bis 3 PatG privilegiert handelt, gilt nicht als berechtigt "
              "(§ 10 Abs. 3 PatG). Eine unmittelbare Verletzung durch den Abnehmer ist nicht Voraussetzung.",
              norms=["§ 10 PatG"], concepts=["pat_mittelbare_verletzung"], abschnitt="Überblick"),
        *fallkette("p03n10-1", "Die Messkapsel",
            "Patentiert ist ein Flügelradzähler aus Gehäuse und auswechselbarer Messkapsel mit Flügelrad und Zählwerk; K vertreibt die Gehäuse "
            "mit einem nur von ihr verwendeten Gewinde. B verkauft Messkapseln, die in diese Gehäuse passen und dort eingeschraubt werden.",
            [frage("Bezieht sich die Messkapsel auf ein wesentliches Element der Erfindung?", True,
                   ["**Ja!** Ein Mittel bezieht sich auf ein wesentliches Element, wenn es geeignet ist, mit einem oder mehreren Merkmalen des "
                    "Anspruchs bei der Verwirklichung des Erfindungsgedankens **funktional zusammenzuwirken** (BGH Flügelradzähler). Die Kapsel "
                    "trägt Flügelrad und Zählwerk und wirkt mit dem Gehäuse zusammen."],
                   merke="Wesentlich = funktionales Zusammenwirken mit Anspruchsmerkmalen.", titel="Wesentliches Element", level=1),
             frage("Ist das Mittel trotzdem wesentlich?", False,
                   ["**Nein!** Ein Merkmal kann als **nichtwesentliches Element** außer Betracht bleiben, wenn es zum Leistungsergebnis der "
                    "Erfindung, also zur Lösung des technischen Problems, nichts beiträgt (BGH Pipettensystem; schon Flügelradzähler für völlig "
                    "untergeordnete Merkmale)."],
                   abwandlung="Das Teil, das B liefert, verwirklicht nur ein Merkmal, das zur Lösung des technischen Problems nichts beiträgt.",
                   merke="Völlig untergeordnete Merkmale scheiden aus.", titel="Nichtwesentliches Element", level=2,
                   cases=["pat_bgh_pipettensystem"]),
             frage("Entscheidet allein die Üblichkeit des Kapselwechsels, ob die Kunden das Patent durch Neuherstellung verletzen?", False,
                   ["**Nein!** Ob der Austausch von Teilen der Neuherstellung gleichkommt, verlangt eine die **Eigenart des Erzeugnisses** "
                    "berücksichtigende Abwägung zwischen dem Verwertungsinteresse des Inhabers und dem Interesse des Abnehmers am ungehinderten "
                    "Gebrauch (BGH Flügelradzähler). Nur wenn die Kunden nicht berechtigt sind, liefert B an Nichtberechtigte."],
                   merke="Neuherstellung: Interessenabwägung nach Eigenart des Erzeugnisses.", titel="Berechtigte Abnehmer?", level=3,
                   concepts=["pat_erschoepfung"]),
             ],
            abschnitt="Abs. 1: Wesentliches Element", level=1, concepts=["pat_mittelbare_verletzung"], norms=["§ 10 Abs. 1 PatG"],
            cases=["pat_bgh_fluegelradzaehler"], step=VS + ".3.2"),
        *fallkette("p03n10-2", "Der Audiocodec",
            "K hat ein Patent auf ein Verfahren zur Übertragung digitaler Tonsignale; der Anspruch legt nur die Behandlung der Skalenfaktoren "
            "näher fest. Der chinesische Hersteller B verkauft Geräte, die Tonsignale vor der Übertragung nach MPEG-2 codieren. B liefert "
            "in China an einen Händler, der die Geräte, wie B weiß und will, nach Deutschland weiterliefert.",
            [frage("Bezieht sich das Gerät auf ein wesentliches Element, weil es einen notwendigen, dem Anspruch vorgelagerten Schritt ausführt?", False,
                   ["**Nein!** Ein Mittel bezieht sich nicht schon dann auf ein wesentliches Element, wenn es einen Verfahrensschritt ausführt, "
                    "der den Anspruchsschritten **vorausgeht**, auch wenn er für sie notwendig ist und das Mittel nur dafür taugt. Gleiches gilt "
                    "für Schritte, deren Ausgestaltung für die Erfindung ohne Bedeutung ist (BGH Audiosignalcodierung)."],
                   merke="Vorgelagerte Schritte sind keine wesentlichen Elemente.", titel="Vorgelagerter Schritt", level=3),
             frage("Liefert B im Inland, obwohl die Übergabe in China stattfindet?", True,
                   ["**Ja!** Wer im Ausland ein Mittel an einen Dritten liefert, der es **mit seinem Wissen und Wollen** zur Benutzung der "
                    "Erfindung nach Deutschland weiterliefert, veranlasst eine Lieferung im Geltungsbereich des Patentgesetzes (BGH "
                    "Audiosignalcodierung)."],
                   merke="Veranlasste Weiterlieferung ins Inland ist Lieferung im Inland.", titel="Lieferung über Dritte", level=2),
             ],
            abschnitt="Abs. 1: Wesentliches Element", level=2, concepts=["pat_mittelbare_verletzung"], norms=["§ 10 Abs. 1 PatG"],
            cases=["pat_bgh_audiosignalcodierung"], step=VS + ".3.2"),
        *fallkette("p03n10-3", "Das Räderwerk",
            "Z liefert aus Deutschland Räderwerke für Funkuhren an den Hersteller H in Asien. H baut sie in Funkwecker ein, die ein deutsches "
            "Warenhaus bestellt hat. P hat ein deutsches Patent auf eine Anzeigestellungs-Erkennung für Funkuhren; die Räderwerke beziehen "
            "sich auf ein wesentliches Element.",
            [frage("Ist die Lieferung der Räderwerke ins Ausland eine Lieferung im Geltungsbereich des Patentgesetzes?", True,
                   ["**Ja!** Eine Lieferung vom Inland ins Ausland findet **teilweise im Inland** statt (BGH Funkuhr II). Damit ist der erste "
                    "Inlandsbezug des § 10 Abs. 1 PatG erfüllt."],
                   merke="Lieferung aus Deutschland ins Ausland = Lieferung im Inland.", titel="Erster Inlandsbezug", level=1),
             frage("Verletzt Z das Patent mittelbar, weil die Wecker für Deutschland bestimmt sind?", True,
                   ["**Ja!** Erfolgt die Lieferung zur Benutzung der Erfindung **im Inland**, hier zum Einbau in Wecker für ein deutsches "
                    "Warenhaus, wird gerade die Gefährdung des inländischen Patents herbeigeführt, der § 10 PatG vorbeugen soll (BGH Funkuhr II). "
                    "Wissen oder Offensichtlichkeit muss hinzukommen."],
                   merke="Zweiter Inlandsbezug: Benutzung der Erfindung in Deutschland.", titel="Zweiter Inlandsbezug", level=2),
             frage("Liegt dann noch eine mittelbare Verletzung vor?", False,
                   ["**Nein!** Soll die Erfindung **im Ausland** benutzt werden, gefährdet die Lieferung das Verbietungsrecht aus § 9 PatG nicht; "
                    "sie fällt nicht unter § 10 PatG (BGH Funkuhr II, Flügelradzähler)."],
                   abwandlung="Die Wecker sind ausschließlich für den Verkauf in den USA bestimmt.",
                   merke="Benutzung im Ausland: keine mittelbare Verletzung.", titel="Benutzung im Ausland", level=2),
             frage("Haftet Z nach § 10 PatG, wenn er nur handelsübliche Normschrauben für die Wecker liefert?", False,
                   ["**Nein!** Bei **allgemein im Handel erhältlichen Erzeugnissen** greift § 10 Abs. 1 PatG nicht, es sei denn, der Lieferant "
                    "veranlasst den Belieferten bewusst zu einer nach § 9 S. 2 PatG verbotenen Handlung (§ 10 Abs. 2 PatG)."],
                   merke="Stapelware nur bei bewusster Veranlassung.", titel="Handelsübliche Erzeugnisse", level=1,
                   norms=["§ 10 Abs. 2 PatG"]),
             ],
            abschnitt="Abs. 1 und 2: Inlandsbezug und Stapelware", level=2, concepts=["pat_mittelbare_verletzung"], norms=["§ 10 PatG"],
            cases=["pat_bgh_funkuhr_ii"], step=VS + ".3.2"),
        *fallkette("p03n10-4", "Der Aufzugsantrieb",
            "K hat ein Patent auf einen Treibscheibenaufzug, dessen flacher Antrieb im Aufzugsschacht sitzt. B verkauft Antriebseinheiten, die "
            "sich auch anders einbauen lassen; ihr Prospekt zeigt aber den Einbau in einer Nische der Schachtwand, und auf der Messe "
            "„Interlift“ stellt B ein Aufzugmodell mit so eingebauter Einheit aus.",
            [frage("Muss K beweisen, dass ein Abnehmer sich bereits für den patentgemäßen Einbau entschieden hat?", False,
                   ["**Nein!** Die mittelbare Verletzung setzt nicht voraus, dass der Abnehmer die Bestimmung schon getroffen hat. Es genügt, dass "
                    "der Lieferant weiß oder es offensichtlich ist, dass der Abnehmer die Mittel patentverletzend verwenden wird; maßgeblich ist "
                    "eine **hinreichend sichere Erwartung** (BGH Deckenheizung)."],
                   merke="Hinreichend sichere Erwartung genügt.", titel="Bestimmung durch den Abnehmer", level=2,
                   cases=["pat_bgh_deckenheizung"]),
             frage("Kann der Prospekt die Bestimmung zur patentgemäßen Verwendung belegen?", True,
                   ["**Ja!** Zum Nachweis der Bestimmung kann es genügen, dass der Angebotsempfänger in **Bedienungsanleitungen, Prospekten oder "
                    "dergleichen** auf die patentgemäße Verwendung hingewiesen wird (BGH Antriebsscheibenaufzug)."],
                   merke="Hinweise des Lieferanten belegen die Bestimmung.", titel="Prospekt als Beleg", level=1),
             frage("Was kann K verlangen, wenn die Einheiten auch patentfrei sinnvoll verwendbar sind?", 1,
                   ["**Regelmäßig ein eingeschränktes Verbot.** Welche Vorsorge der Lieferant treffen muss, damit eine patentgemäße Verwendung "
                    "nicht zu erwarten ist (Warnhinweis, Vertragsstrafenversprechen der Abnehmer), entscheidet der Tatrichter im Einzelfall (BGH "
                    "Deckenheizung). Ein weitergehendes Vertriebsverbot setzt besondere Umstände voraus (BGH Haubenstretchautomat)."],
                   optionen=["Stets ein Schlechthinverbot", "Ein eingeschränktes Verbot mit Vorsorgemaßnahmen, je nach Einzelfall",
                             "Nichts, weil § 10 Abs. 2 PatG eingreift", "Nur Schadensersatz, keine Unterlassung"],
                   merke="Doppelt verwendbare Mittel: Warnhinweis statt Schlechthinverbot.", titel="Umfang des Verbots", level=3,
                   cases=["pat_bgh_deckenheizung", "pat_bgh_haubenstretchautomat"], step=VS + ".5.1"),
             ],
            abschnitt="Abs. 1: Bestimmung, Wissen, Offensichtlichkeit", level=2, concepts=["pat_mittelbare_verletzung"], norms=["§ 10 Abs. 1 PatG"],
            cases=["pat_bgh_antriebsscheibenaufzug"], step=VS + ".3.2"),
        *fallkette("p03n10-5", "Der Haubenstretchautomat",
            "K hat ein Patent auf ein Verfahren, Stapel mit einer Haube aus Stretchfolie zu umhüllen. B verkauft Maschinen, mit denen sich das "
            "Verfahren ausführen lässt; nach der Bedienungsanleitung ist streitig, ob die Schweißnaht noch unter den Anspruch fällt. K verlangt "
            "Unterlassung, Auskunft und Schadensersatz.",
            [frage("Kommt es für die Offensichtlichkeit auf die Umstände im Zeitpunkt der Lieferung an?", True,
                   ["**Ja!** Objektive und subjektive Voraussetzungen müssen **im Zeitpunkt des Angebots oder der Lieferung** vorliegen. "
                    "Offensichtlich ist die Bestimmung, wenn die drohende Verletzung aus der objektivierten Sicht des Lieferanten so deutlich "
                    "erkennbar ist, dass die Lieferung einer wissentlichen Patentgefährdung gleichsteht (BGH Haubenstretchautomat)."],
                   merke="Maßgeblicher Zeitpunkt: Angebot oder Lieferung.", titel="Zeitpunkt", level=2),
             frage("Liegt der zu ersetzende Schaden von K schon in der Lieferung der Maschinen?", False,
                   ["**Nein!** Zu ersetzen ist der Schaden, der durch die **unmittelbare Verletzung des Abnehmers** entsteht; in diesem Rahmen "
                    "kann auch der Gewinn des mittelbaren Verletzers abgeschöpft werden (BGH Haubenstretchautomat, Antriebsscheibenaufzug)."],
                   merke="Schaden der mittelbaren Verletzung = Schaden der Abnehmer-Benutzung.", titel="Schaden", level=2,
                   norms=["§ 139 Abs. 2 PatG"], concepts=["pat_schadensersatz"], cases=["pat_bgh_antriebsscheibenaufzug"], step=VS + ".5.2"),
             frage("Kann K trotzdem die Feststellung der Schadensersatzpflicht verlangen, ohne Benutzungen der Abnehmer nachzuweisen?", True,
                   ["**Ja!** Die für die Feststellungsklage nötige **Wahrscheinlichkeit eines Schadens** ist in der Regel zu bejahen, wenn "
                    "zumindest eine rechtswidrige und schuldhafte mittelbare Verletzungshandlung stattgefunden hat, auch durch bloßes Anbieten "
                    "(BGH Fräsverfahren)."],
                   merke="Eine schuldhafte mittelbare Verletzung macht den Schaden wahrscheinlich.", titel="Feststellungsklage", level=3,
                   cases=["pat_bgh_fraesverfahren"], step=VS + ".5.2"),
             ],
            abschnitt="Rechtsfolgen der mittelbaren Verletzung", level=2, concepts=["pat_mittelbare_verletzung"], norms=["§ 10 Abs. 1 PatG"],
            cases=["pat_bgh_haubenstretchautomat"], step=VS + ".3.2"),
    ]),
    # ================================================================== §§ 11, 12 PatG
    dict(id="p03n11", order=1100, titel="§§ 11, 12 PatG: Schranken und Vorbenutzungsrecht", einheiten=[
        intro("p03n11-0", "Wo die Wirkung des Patents endet",
              "§ 11 PatG nimmt Handlungen von der Wirkung des Patents aus: im **privaten Bereich zu nichtgewerblichen Zwecken** (Nr. 1, beides "
              "zusammen), **Versuche**, die sich auf den Gegenstand der Erfindung beziehen (Nr. 2), Pflanzenzüchtung (Nr. 2a), Studien und "
              "Versuche für eine **arzneimittelrechtliche Zulassung** in der EU oder in Drittstaaten (Nr. 2b, Bolar), die Einzelzubereitung in "
              "Apotheken (Nr. 3) sowie Verkehrsmittel aus Verbandsstaaten (Nr. 4 bis 6). § 12 PatG schützt den **Vorbenutzer**: Wer zur Zeit "
              "der Anmeldung (bei Priorität: der früheren Anmeldung, § 12 Abs. 2 PatG) im Inland die Erfindung in Benutzung genommen oder "
              "Veranstaltungen dazu getroffen hatte, darf sie für die Bedürfnisse seines Betriebs weiter nutzen. Voraussetzung ist "
              "**Erfindungsbesitz**; übertragbar ist das Recht nur mit dem Betrieb. Für Gebrauchsmuster gilt § 12 PatG entsprechend "
              "(§ 13 Abs. 3 GebrMG).",
              norms=["§ 11 PatG", "§ 12 PatG"], concepts=["pat_schranken", "pat_vorbenutzungsrecht"], abschnitt="Überblick"),
        *fallkette("p03n11-1", "Die Gartenbewässerung",
            "Ingenieur I liest die Patentschrift von P über eine sensorgesteuerte Gartenbewässerung und baut die Anlage für seinen eigenen "
            "Garten nach. P verlangt Unterlassung.",
            [frage("Ist der Nachbau von der Wirkung des Patents ausgenommen?", True,
                   ["**Ja!** Handlungen im **privaten Bereich zu nichtgewerblichen Zwecken** fallen nicht unter das Patent (§ 11 Nr. 1 PatG). I "
                    "baut und gebraucht die Anlage nur für sich."],
                   merke="Privat und nichtgewerblich: beides muss vorliegen.", titel="Privater Bereich", level=1),
             frage("Bleibt es bei der Privilegierung?", False,
                   ["**Nein!** Wer Anlagen herstellt und verkauft, handelt zu **gewerblichen Zwecken**; schon das Anbieten im Internet ist eine "
                    "Benutzung nach § 9 S. 2 Nr. 1 PatG. § 11 Nr. 1 PatG verlangt, dass die Handlung privat **und** nichtgewerblich ist."],
                   abwandlung="I baut weitere Anlagen und bietet sie auf einer Verkaufsplattform an.",
                   merke="Verkauf ist gewerblich, auch für Privatleute.", titel="Verkauf über das Internet", level=1,
                   norms=["§ 9 PatG"]),
             frage("Greift § 11 Nr. 1 PatG, wenn I die Anlage nur in seinem eigenen Gärtnereibetrieb einsetzt?", False,
                   ["**Nein!** Der Gebrauch im Betrieb ist weder privat noch nichtgewerblich. Gebrauchen ist eine eigene Benutzungshandlung "
                    "(§ 9 S. 2 Nr. 1 PatG), auch wenn I die Anlage nicht verkauft."],
                   merke="Gebrauch im Betrieb ist nie privilegiert.", titel="Gebrauch im Betrieb", level=1),
             ],
            abschnitt="§ 11 Nr. 1 PatG: Privater Bereich", level=1, concepts=["pat_schranken"], norms=["§ 11 PatG"], step=VS + ".4.1"),
        *fallkette("p03n11-2", "Die Generikastudie",
            "P hat ein Patent auf einen Wirkstoff gegen Bluthochdruck. Generikahersteller G untersucht den Wirkstoff während der Laufzeit in "
            "eigenen Versuchsreihen und führt die Studien durch, die er für die Zulassung seines Generikums in der EU und in den USA braucht.",
            [frage("Sind Versuche, die neue Erkenntnisse über Wirkungen des Wirkstoffs liefern sollen, privilegiert?", True,
                   ["**Ja!** Frei sind Handlungen zu **Versuchszwecken, die sich auf den Gegenstand der Erfindung beziehen** (§ 11 Nr. 2 PatG), "
                    "also planmäßige Versuche, um Erkenntnisse über die Erfindung selbst zu gewinnen, etwa über Wirkungen oder neue Anwendungen. "
                    "Ein auch kommerzielles Ziel schadet nicht (BGH Klinische Versuche I und II)."],
                   merke="Versuche über die Erfindung sind frei.", titel="Versuchsprivileg", level=2),
             frage("Sind die Zulassungsstudien für das Generikum ebenfalls erlaubt, auch für die USA?", True,
                   ["**Ja!** § 11 Nr. 2b PatG (Bolar-Regelung) nimmt Studien und Versuche und die sich daraus ergebenden praktischen "
                    "Anforderungen aus, die für eine **arzneimittelrechtliche Genehmigung** in der EU oder eine Zulassung in Mitgliedstaaten oder "
                    "**Drittstaaten** erforderlich sind."],
                   merke="Bolar: Zulassungsstudien auch für Drittstaaten.", titel="Bolar-Privileg", level=1),
             frage("Ist auch dieser Einsatz durch das Versuchsprivileg gedeckt?", False,
                   ["**Nein!** Nach herrschender Auffassung erfasst § 11 Nr. 2 PatG nur Versuche **mit Bezug auf den Gegenstand** der Erfindung. "
                    "Wird die Erfindung bloß als Werkzeug für die Erforschung anderer Gegenstände eingesetzt, ist das eine gewöhnliche Benutzung."],
                   abwandlung="G nutzt den Wirkstoff nur als Vergleichssubstanz, um eigene, andere Wirkstoffe zu testen.",
                   merke="Versuche über die Erfindung ja, mit der Erfindung als Werkzeug nein.", titel="Forschungswerkzeug", level=3),
             frage("Darf G das Generikum schon während der Patentlaufzeit auf Vorrat herstellen, um es am Tag nach Ablauf zu verkaufen?", False,
                   ["**Nein!** Herstellen und Besitzen zum Inverkehrbringen sind Benutzungen nach § 9 S. 2 Nr. 1 PatG. § 11 Nr. 2b PatG deckt "
                    "nur Studien und Versuche für die Zulassung, nicht die Produktion für den Markt."],
                   merke="Bolar deckt keine Vorratsproduktion.", titel="Vorratsproduktion", level=2, norms=["§ 9 PatG"]),
             ],
            abschnitt="§ 11 Nr. 2 und 2b PatG: Versuche und Zulassung", level=2, concepts=["pat_schranken"], norms=["§ 11 PatG"],
            step=VS + ".4.1"),
        *fallkette("p03n11-3", "Die Desmopressin-Tabletten",
            "K hat ein Gebrauchsmuster auf Desmopressin-Tabletten mit einer Obergrenze für Oxidationsmittel; die Beschreibung hebt die bessere "
            "Haltbarkeit hervor. B hatte vor dem Prioritätstag eine Rezeptur mit allen Merkmalen entwickelt und hergestellt, ohne die "
            "Haltbarkeitswirkung zu kennen. Die Tabletten vertreibt Vertriebspartner V.",
            [frage("Was setzt das Vorbenutzungsrecht neben Benutzung oder Veranstaltungen im Inland voraus?", 2,
                   ["**Selbständigen Erfindungsbesitz.** Die technische Lehre muss **objektiv fertig** sein und der Handelnde muss **subjektiv "
                    "erkannt** haben, dass ihre Ausführung möglich ist (BGH Desmopressin). Eine Anmeldung oder Veröffentlichung ist nicht nötig."],
                   optionen=["Eine eigene Schutzrechtsanmeldung", "Die Kenntnis aller in der Beschreibung genannten Vorteile",
                             "Eine fertige, als ausführbar erkannte Lehre (Erfindungsbesitz)", "Eine öffentliche Vorbenutzung"],
                   merke="Erfindungsbesitz: objektiv fertig, subjektiv erkannt.", titel="Erfindungsbesitz", level=1),
             frage("Fehlt B der Erfindungsbesitz, weil B die bessere Haltbarkeit nicht kannte?", False,
                   ["**Nein!** Die subjektive Erkenntnis liegt vor, wenn das Handeln **planmäßig** auf eine Lehre gerichtet ist, die alle Merkmale "
                    "verwirklicht, hier eine bestimmte Rezeptur. Ob der Handelnde die in der Beschreibung genannten Wirkungen kennt, ist "
                    "unerheblich (BGH Desmopressin)."],
                   merke="Kenntnis der Vorteile ist nicht nötig.", titel="Kenntnis der Wirkung", level=2),
             frage("Kann sich Vertriebspartner V auf das Vorbenutzungsrecht von B berufen?", True,
                   ["**Ja!** Der Vorbenutzer darf die Erfindung für die Bedürfnisse seines Betriebs in **eigenen oder fremden Werkstätten** "
                    "ausnutzen (§ 12 Abs. 1 S. 2 PatG); dazu gehört der Vertrieb über Vertriebspartner, auch wenn B den Partner nach dem "
                    "Prioritätstag wechselt (BGH Desmopressin)."],
                   merke="Das Vorbenutzungsrecht deckt auch Vertriebspartner.", titel="Vertriebspartner", level=2),
             frage("Hat B dann ein Vorbenutzungsrecht?", False,
                   ["**Nein!** Stehen Benutzer und Erfinder in vertraglicher Beziehung und wurde der Erfindungsbesitz im Zusammenhang mit der "
                    "Erfüllung dieses Vertrags erlangt, ist ein Vorbenutzungsrecht **in aller Regel ausgeschlossen** (BGH Füllstoff). Sonst könnte "
                    "der Vertragspartner die Erfindung des anderen frei nutzen."],
                   abwandlung="B kannte die Rezeptur nur aus einem Entwicklungsauftrag, den er für den Erfinder von K ausgeführt hatte.",
                   merke="Erfindungsbesitz aus Vertrag mit dem Erfinder: kein Vorbenutzungsrecht.", titel="Besitz aus Vertrag", level=3,
                   cases=["pat_bgh_fuellstoff"]),
             ],
            abschnitt="§ 12 Abs. 1 PatG: Erfindungsbesitz", level=2, concepts=["pat_vorbenutzungsrecht"], norms=["§ 12 Abs. 1 PatG"],
            cases=["pat_bgh_desmopressin"], step=VS + ".4.1"),
        *fallkette("p03n11-4", "Die Nabenschaltung",
            "F hatte vor dem Prioritätstag eine Fahrrad-Dreigangnabe entwickelt und im Inland benutzt, die das spätere Gebrauchsmuster von K "
            "verwirklicht. F verkauft den Geschäftsbereich Nabenschaltungen an B. B lässt einen Teil der Fertigung in Werkstätten von F "
            "ausführen.",
            [frage("Kann das Vorbenutzungsrecht mit dem Geschäftsbereich auf B übergehen?", True,
                   ["**Ja!** Das Recht kann nur zusammen mit dem Betrieb vererbt oder veräußert werden (§ 12 Abs. 1 S. 3 PatG). Die Übertragung "
                    "eines **abgrenzbaren Betriebsteils** steht der Übertragung des ganzen Betriebs gleich (BGH Nabenschaltung III)."],
                   merke="Betriebsteil genügt für den Übergang.", titel="Übertragung mit Betriebsteil", level=2),
             frage("Schadet es, dass B einen Teil der Fertigung bei F als Vertragspartner ausführen lässt?", False,
                   ["**Nein!** Der Übergang ist nicht ausgeschlossen, weil der Übernehmer Arbeiten in **fremden Werkstätten** ausführen lässt, "
                    "auch in denen seines Vertragspartners (BGH Nabenschaltung III; § 12 Abs. 1 S. 2 PatG)."],
                   merke="Fremde Werkstätten sind erlaubt.", titel="Fremde Werkstätten", level=2),
             frage("Ist die neue Nabe vom Vorbenutzungsrecht gedeckt?", False,
                   ["**Nein!** Der Vorbenutzer ist auf seinen Besitzstand beschränkt. Weiterentwicklungen, die **erstmals alle Merkmale** des "
                    "Schutzanspruchs verwirklichen, greifen in den Gegenstand des Schutzrechts ein und sind verwehrt (BGH Biegevorrichtung)."],
                   abwandlung="Die vorbenutzte Nabe hatte ein Anspruchsmerkmal noch nicht; erst B baut es ein.",
                   merke="Erst die Weiterentwicklung trifft den Anspruch: verwehrt.", titel="Weiterentwicklung", level=2,
                   cases=["pat_bgh_biegevorrichtung"]),
             frage("Kann eine Modifikation gedeckt sein, wenn die alte Nabe schon alle Merkmale des unabhängigen Anspruchs hatte?", True,
                   ["**Ja!** Verwirklichte der vorbenutzte Gegenstand bereits alle Merkmale eines unabhängigen Anspruchs, kann auch seine "
                    "Modifikation gedeckt sein, selbst wenn ihm Merkmale einer beschränkten Fassung fehlten (BGH Faserstoffbahn). Die Grenze ist "
                    "überschritten, wenn ein Merkmal technisch anders verwirklicht oder ein zusätzlicher, hervorgehobener Vorteil genutzt wird."],
                   merke="Modifikation innerhalb des Besitzstands: Gesamtwürdigung.", titel="Modifikation", level=3,
                   cases=["pat_bgh_faserstoffbahn"]),
             ],
            abschnitt="§ 12 Abs. 1 PatG: Umfang und Übertragung", level=2, concepts=["pat_vorbenutzungsrecht"], norms=["§ 12 Abs. 1 PatG"],
            cases=["pat_bgh_nabenschaltung_iii"], step=VS + ".4.1"),
    ]),
    # ================================================================== § 14 PatG
    dict(id="p03n14", order=1400, titel="§ 14 PatG: Schutzbereich, Auslegung und Äquivalenz", einheiten=[
        intro("p03n14-0", "Vom Anspruch zum Schutzbereich",
              "Der Schutzbereich wird durch die **Patentansprüche** bestimmt; Beschreibung und Zeichnungen sind zur Auslegung heranzuziehen "
              "(§ 14 PatG, gleichlautend Art. 69 Abs. 1 EPÜ mit dem Auslegungsprotokoll). Prüfung: (1) Merkmalsgliederung; (2) **Auslegung** "
              "jedes Merkmals aus Sicht des Fachmanns, funktionsorientiert und im Gesamtzusammenhang, die Patentschrift als ihr eigenes Lexikon; "
              "(3) **wortsinngemäße** Verwirklichung; (4) sonst **Äquivalenz** nach den drei Schneidmesser-Fragen: Gleichwirkung, Auffindbarkeit "
              "ohne erfinderische Überlegungen, Gleichwertigkeit (Orientierung am Anspruch). Grenzen: Die **Auswahlentscheidung** des Anspruchs "
              "schließt nicht beanspruchte, aber beschriebene Alternativen aus; mit dem **Formstein-Einwand** kann der Beklagte geltend machen, "
              "die äquivalente Ausführung sei durch den Stand der Technik nicht patentfähig.",
              norms=["§ 14 PatG"], concepts=["pat_schutzbereich", "pat_auslegung", "pat_aequivalenz"], abschnitt="Überblick"),
        *fallkette("p03n14-1", "Die Führungsnut",
            "Anspruch 1 des Patents von K verlangt einen Rahmen „mit einer Führungsnut“. Alle Ausführungsbeispiele zeigen eine durchgehende Nut; "
            "Unteranspruch 3 nennt sie ausdrücklich. Im Erteilungsverfahren hatte K erklärt, gemeint seien nur durchgehende Nuten. B verwendet "
            "eine unterbrochene Nut, die dieselbe Führung leistet.",
            [frage("Beschränken die Ausführungsbeispiele den Anspruch auf durchgehende Nuten?", False,
                   ["**Nein!** Ausführungsbeispiele erläutern den Anspruch, sie beschränken einen allgemein gefassten Anspruch **regelmäßig "
                    "nicht** (BGH Bodenseitige Vereinzelungseinrichtung). Maßgeblich ist, welche Funktion das Merkmal im Zusammenhang der "
                    "Erfindung hat (BGH Drehzahlermittlung)."],
                   merke="Ausführungsbeispiele beschränken nicht.", titel="Ausführungsbeispiele", level=1,
                   cases=["pat_bgh_bodenseitige_vereinzelungseinrichtung", "pat_bgh_drehzahlermittlung"]),
             frage("Engt Unteranspruch 3 den Hauptanspruch auf durchgehende Nuten ein?", False,
                   ["**Nein!** Unteransprüche können zur Auslegung des Hauptanspruchs beitragen, **engen ihn aber regelmäßig nicht ein**; wie "
                    "Ausführungsbeispiele zeigen sie nur Möglichkeiten der Ausgestaltung, gegebenenfalls mit einem zusätzlichen Vorteil (BGH "
                    "Wärmetauscher)."],
                   merke="Unteranspruch = Ausgestaltung, keine Einschränkung.", titel="Unteranspruch", level=2,
                   cases=["pat_bgh_waermetauscher"]),
             frage("Ist K an seine Erklärung im Erteilungsverfahren gebunden?", False,
                   ["**Nein!** Für den Schutzbereich kommt es grundsätzlich **nicht auf Vorgänge im Erteilungsverfahren** an; sie zählen nur, "
                    "soweit sie in der Patentschrift ihren Niederschlag gefunden haben. Die Patentschrift ist ihr eigenes Lexikon (BGH "
                    "Kunststoffrohrteil)."],
                   merke="Erteilungsakten sind kein Auslegungsmaterial.", titel="Erteilungsakten", level=2,
                   cases=["pat_bgh_kunststoffrohrteil"]),
             frage("Muss das Verletzungsgericht die Auslegung des BPatG aus dem Nichtigkeitsverfahren übernehmen?", False,
                   ["**Nein!** Das Verletzungsgericht legt das Patent **selbständig** aus und ist an die Auslegung im Nichtigkeitsverfahren weder "
                    "rechtlich noch tatsächlich gebunden; es muss sich aber mit ihr auseinandersetzen (BGH Kreuzgestänge)."],
                   abwandlung="Das BPatG hat im Nichtigkeitsurteil angenommen, die Nut müsse durchgehend sein.",
                   merke="Eigene Auslegung, aber Auseinandersetzung mit dem BPatG.", titel="Bindung an das BPatG", level=2,
                   cases=["pat_bgh_kreuzgestaenge"]),
             ],
            abschnitt="S. 2: Auslegung", level=1, concepts=["pat_auslegung"], norms=["§ 14 PatG"], step=VS + ".2.1"),
        *fallkette("p03n14-2", "Die Luftkappe",
            "Das Patent von K schützt eine Luftkappe für Farbspritzpistolen mit einem Mittel, das den Luftstrom durch die Formungsbohrung "
            "„blockiert“. Die Patentschrift schildert als Problem im Stand der Technik Blockieren und Drosseln ohne Unterschied. Die "
            "Spritzpistole von B drosselt den Luftstrom nur.",
            [frage("Folgt aus dem Wort „blockieren“, dass bloßes Drosseln für die Lehre nicht genügt?", False,
                   ["**Nein!** Nennt die Patentschrift zwei nur graduell verschiedene Maßnahmen undifferenziert als Ausgangspunkt, lässt sich aus "
                    "der Nennung der stärkeren im Anspruch **nicht ohne weiteres** schließen, die schwächere reiche nicht aus (BGH "
                    "Luftkappensystem). Maßgeblich ist die Funktion des Merkmals."],
                   merke="Wortlaut nicht isoliert, sondern funktional lesen.", titel="Funktionsorientierte Auslegung", level=2),
             frage("Kann B einwenden, ihre wortsinngemäß verletzende Pistole sei durch den Stand der Technik nahegelegt?", False,
                   ["**Nein!** Der **Formstein-Einwand** hat nur bei äquivalenter Verletzung Bedeutung (BGH Luftkappensystem). Bei wortsinngemäßer "
                    "Benutzung prüft das Verletzungsgericht den Rechtsbestand nicht; B muss Nichtigkeitsklage erheben und Aussetzung beantragen "
                    "(§ 148 ZPO)."],
                   merke="Formstein-Einwand nur gegen Äquivalenz.", titel="Formstein bei Wortsinn", level=2,
                   concepts=["pat_trennungsprinzip"]),
             frage("Kann B jetzt geltend machen, diese Ausführung sei im Stand der Technik vorweggenommen oder nahegelegt?", True,
                   ["**Ja!** Mit dem **Formstein-Einwand** kann der Beklagte geltend machen, die angegriffene äquivalente Ausführungsform sei mit "
                    "Rücksicht auf den Stand der Technik keine patentfähige Erfindung; dann fällt sie nicht in den Schutzbereich (BGH Formstein)."],
                   abwandlung="B verwirklicht das Merkmal nicht wortsinngemäß, sondern nur mit einem gleichwirkenden Ersatzmittel.",
                   merke="Äquivalenz endet am freien Stand der Technik.", titel="Formstein-Einwand", level=3, step=VS + ".2.3"),
             ],
            abschnitt="S. 2: Auslegung", level=2, concepts=["pat_auslegung", "pat_aequivalenz"], norms=["§ 14 PatG"],
            cases=["pat_bgh_luftkappensystem"], step=VS + ".2.1"),
        *fallkette("p03n14-3", "Das Schneidmesser",
            "K ist ausschließliche Lizenznehmerin eines Patents auf ein Schneidmesser für Papierschneidanlagen; nach dem Anspruch schließen die "
            "Klingen mit dem Radius einen Winkel von 9° bis 12° ein. B liefert passende Ersatzmesser, deren Winkel 8° 40' beträgt.",
            [frage("Bestimmen und begrenzen Zahlenangaben im Anspruch den Schutzgegenstand?", True,
                   ["**Ja!** In den Anspruch aufgenommene Zahlen- und Maßangaben bestimmen den Schutzgegenstand mit und begrenzen ihn. Wie jeder "
                    "Bestandteil des Anspruchs sind sie aber **der Auslegung fähig**, etwa mit Blick auf übliche Toleranzen (BGH Schneidmesser I)."],
                   merke="Zahlenangaben begrenzen, sind aber auslegungsfähig.", titel="Zahlenangaben", level=1, step=VS + ".2.2"),
             frage("Welche Frage gehört nicht zur Prüfung der Äquivalenz?", 3,
                   ["**Die Kenntnis des Verletzers.** Äquivalent ist eine Abwandlung, wenn sie (1) das der Erfindung zugrunde liegende Problem mit "
                    "**gleicher Wirkung** löst, (2) der Fachmann sie mit seinen Fachkenntnissen **auffinden** konnte und (3) seine Überlegungen so "
                    "am Sinngehalt des Anspruchs **orientiert** sind, dass er sie als gleichwertig in Betracht zog (BGH Schneidmesser I)."],
                   optionen=["Gleichwirkung", "Auffindbarkeit ohne erfinderische Überlegungen", "Orientierung am Sinngehalt des Anspruchs",
                             "Kenntnis des Verletzers vom Patent"],
                   merke="Schneidmesser: gleichwirkend, naheliegend, gleichwertig.", titel="Schneidmesser-Fragen", level=1),
             frage("Ist ein Winkel außerhalb des Zahlenbereichs von vornherein vom Schutz ausgeschlossen?", False,
                   ["**Nein!** Zahlenangaben sind einer äquivalenten Verletzung nicht von vornherein entzogen. Erschließt sich dem Fachmann aber "
                    "kein abweichender Wert als gleichwirkend, reicht der Schutz nicht über den Anspruch hinaus (BGH Schneidmesser I). Hier hat der "
                    "BGH die Verletzung durch die Messer mit 8° 40' bestätigt."],
                   merke="Auch Zahlenbereiche lassen Äquivalenz zu.", titel="Abweichender Winkel", level=2, step=VS + ".2.3"),
             frage("Darf das Gericht die Äquivalenz Merkmal für Merkmal isoliert prüfen?", False,
                   ["**Nein!** Es genügt nicht, nur für einzelne Merkmale zu prüfen, ob ein gleichwertiges Ersatzmittel vorhanden ist. Die angegriffene "
                    "Ausführung ist, soweit für die patentgemäße Lösung bedeutsam, **als Gesamtheit** zu erfassen und daraufhin zu prüfen, ob sie eine "
                    "auffindbar gleichwertige Lösung darstellt (BGH Pumpeinrichtung)."],
                   merke="Äquivalenz: die Ausführung als Ganzes betrachten.", titel="Gesamtbetrachtung", level=3,
                   cases=["pat_bgh_pumpeinrichtung"], step=VS + ".2.3"),
             frage("Wird eine Abweichung dann noch gleichwertig sein?", False,
                   ["**Regelmäßig nein!** Versteht der Fachmann die Zahlenangabe als **abschließende Festlegung**, sind Abweichungen nur selten "
                    "gleichwertig; die Schneidmesser-Fragen gelten aber auch hier (BGH Custodiol II)."],
                   abwandlung="Die Patentschrift betont, nur genau dieser Winkelbereich verhindere das Einreißen des Papiers.",
                   merke="Abschließende Zahlenangabe: Äquivalenz die Ausnahme.", titel="Abschließende Festlegung", level=3,
                   cases=["pat_bgh_custodiol_ii"], step=VS + ".2.3"),
             ],
            abschnitt="Äquivalenz: Schneidmesser-Fragen", level=2, concepts=["pat_aequivalenz", "pat_schutzbereich"], norms=["§ 14 PatG"],
            cases=["pat_bgh_schneidmesser_i"], step=VS + ".2.3"),
        *fallkette("p03n14-4", "Die Okklusionsvorrichtung",
            "Das Patent von K schützt ein Implantat aus geflochtenem Metallgewebe, dessen Drahtenden an beiden Enden durch Klemmen "
            "zusammengehalten werden. Die Beschreibung erwähnt, die Enden ließen sich auch verlöten, verschweißen oder anders fixieren. B "
            "fixiert die Drahtenden durch Verschweißen.",
            [frage("Fällt das Verschweißen unter den Wortsinn von „Klemmen“, weil die Beschreibung es nennt?", False,
                   ["**Nein!** Bei Widersprüchen zwischen Anspruch und Beschreibung haben die **Ansprüche Vorrang**. Teile der Beschreibung, die im "
                    "Anspruch keinen Niederschlag gefunden haben, sind nicht geschützt; die Beschreibung zählt nur, soweit sie sich als Erläuterung "
                    "des Anspruchs lesen lässt (BGH Okklusionsvorrichtung)."],
                   merke="Beschreibung erläutert, sie erweitert nicht.", titel="Vorrang der Ansprüche", level=2, step=VS + ".2.1"),
             frage("Ist das Verschweißen ein äquivalentes Mittel?", False,
                   ["**Nein!** Offenbart die Beschreibung mehrere Möglichkeiten, eine Wirkung zu erzielen, ist aber nur eine in den Anspruch "
                    "aufgenommen, begründet die Benutzung einer anderen **regelmäßig keine äquivalente Verletzung**. Die Überlegungen des Fachmanns "
                    "müssen mit dieser **Auswahlentscheidung** in Einklang stehen (BGH Okklusionsvorrichtung, Diglycidverbindung)."],
                   merke="Beschrieben, aber nicht beansprucht: keine Äquivalenz.", titel="Auswahlentscheidung", level=2,
                   cases=["pat_bgh_diglycidverbindung"]),
             ],
            abschnitt="Äquivalenz: Auswahlentscheidung", level=2, concepts=["pat_aequivalenz"], norms=["§ 14 PatG"],
            cases=["pat_bgh_okklusionsvorrichtung"], step=VS + ".2.3"),
        *fallkette("p03n14-5", "Das Kaliumsalz",
            "Das Patent von L schützt die Verwendung von Pemetrexeddinatrium für ein Krebsmedikament in Kombination mit Vitamin B12. "
            "Generikahersteller A teilt L mit, nach Ablauf des Schutzzertifikats ein Präparat mit Pemetrexeddikalium auf den Markt zu bringen. "
            "L klagt auf Unterlassung.",
            [frage("Verwirklicht das Dikaliumsalz das Merkmal „Pemetrexeddinatrium“ wortsinngemäß?", False,
                   ["**Nein!** Der Anspruch nennt ein bestimmtes Salz; ein anderes Salz fällt nicht unter den Wortsinn. In Betracht kommt nur eine "
                    "**äquivalente** Verletzung."],
                   merke="Anderes Salz: Wortsinn verfehlt, Äquivalenz prüfen.", titel="Wortsinn", level=1, step=VS + ".2.2"),
             frage("Scheidet Äquivalenz aus, weil der Fachmann das Dinatriumsalz als Anwendungsfall eines allgemeinen Prinzips erkennt?", False,
                   ["**Nein!** Der Grundsatz der Auswahlentscheidung greift nicht schon dann, wenn sich die beanspruchte Ausführungsform als "
                    "**spezieller Anwendungsfall eines allgemeineren Lösungsprinzips** darstellt und der Fachmann deshalb weitere Ausführungsformen "
                    "auffinden kann (BGH Pemetrexed). Der BGH hat zur Prüfung der Äquivalenz zurückverwiesen."],
                   merke="Allgemeines Prinzip erkennbar: Auswahlentscheidung nicht automatisch.", titel="Grenzen der Auswahlentscheidung", level=3,
                   step=VS + ".2.3"),
             frage("Kann L Unterlassung verlangen, obwohl A noch nichts verkauft hat?", True,
                   ["**Ja!** Der Unterlassungsanspruch besteht auch, wenn eine Zuwiderhandlung **erstmalig droht** (§ 139 Abs. 1 S. 2 PatG). Die "
                    "konkrete Ankündigung der Markteinführung begründet Erstbegehungsgefahr."],
                   merke="Ernsthafte Ankündigung = Erstbegehungsgefahr.", titel="Erstbegehungsgefahr", level=1,
                   norms=["§ 139 Abs. 1 PatG"], concepts=["pat_unterlassung"], step=VS + ".5.1"),
             ],
            abschnitt="Äquivalenz: Auswahlentscheidung", level=3, concepts=["pat_aequivalenz"], norms=["§ 14 PatG"],
            cases=["pat_bgh_pemetrexed"], step=VS + ".2.3"),
    ]),
    # ================================================================== § 24 PatG
    dict(id="p03n24", order=2400, titel="§ 24 PatG: Zwangslizenz", einheiten=[
        intro("p03n24-0", "Benutzung gegen den Willen des Inhabers",
              "Die Zwangslizenz ist eine **nicht ausschließliche** Benutzungsbefugnis, die das **Bundespatentgericht** im Einzelfall durch "
              "Urteil erteilt (§ 24 Abs. 1 PatG; Klage nach § 81 Abs. 1 PatG, vorläufig durch einstweilige Verfügung nach § 85 Abs. 1 PatG). "
              "Voraussetzungen: (1) der Lizenzsucher hat sich innerhalb angemessener Zeit **erfolglos um eine vertragliche Lizenz** zu "
              "angemessenen geschäftsüblichen Bedingungen bemüht (§ 24 Abs. 1 Nr. 1 PatG); (2) das **öffentliche Interesse** gebietet die "
              "Lizenz (§ 24 Abs. 1 Nr. 2 PatG). Für **abhängige Erfindungen** tritt an die Stelle des öffentlichen Interesses ein wichtiger "
              "technischer Fortschritt von erheblicher wirtschaftlicher Bedeutung (§ 24 Abs. 2 PatG). Erteilung erst nach Patenterteilung, "
              "gegen angemessene Vergütung (§ 24 Abs. 6 PatG). Davon zu trennen ist der kartellrechtliche Zwangslizenzeinwand im "
              "Verletzungsprozess.",
              norms=["§ 24 PatG", "§ 85 PatG"], concepts=["pat_zwangslizenz"], abschnitt="Überblick"),
        *fallkette("p03n24-1", "Das HIV-Medikament",
            "M vertreibt seit 2008 das HIV-Medikament Isentress mit dem Wirkstoff Raltegravir. S, Inhaberin eines europäischen Patents, das "
            "den Wirkstoff erfasst, verklagt M 2015 auf Unterlassung; Lizenzverhandlungen sind gescheitert. M beantragt, ihr die Benutzung "
            "vorläufig zu gestatten.",
            [frage("Bei welchem Gericht und in welcher Form beantragt M die vorläufige Gestattung?", 1,
                   ["**Beim Bundespatentgericht durch einstweilige Verfügung.** Die Zwangslizenz wird durch Klage beim BPatG verfolgt "
                    "(§ 81 Abs. 1 PatG); in diesem Verfahren kann die Benutzung vorläufig gestattet werden, wenn der Kläger die Voraussetzungen "
                    "des § 24 PatG glaubhaft macht und die alsbaldige Erlaubnis im öffentlichen Interesse dringend geboten ist (§ 85 Abs. 1 PatG)."],
                   optionen=["Beim Landgericht als Einwand im Verletzungsprozess", "Beim BPatG durch einstweilige Verfügung",
                             "Beim DPMA durch Antrag auf Lizenzbereitschaft", "Beim EPA im Einspruchsverfahren"],
                   merke="Zwangslizenz: BPatG, vorläufig nach § 85 PatG.", titel="Zuständigkeit und Verfahren", level=1,
                   norms=["§ 85 Abs. 1 PatG", "§ 81 Abs. 1 PatG"]),
             frage("Richten sich die nötigen Lizenzbemühungen nach den Umständen des Einzelfalls?", True,
                   ["**Ja!** Ob sich der Lizenzsucher innerhalb eines **angemessenen Zeitraums** erfolglos um eine Lizenz zu angemessenen "
                    "geschäftsüblichen Bedingungen bemüht hat (§ 24 Abs. 1 Nr. 1 PatG), ist anhand der Umstände des Einzelfalls zu beurteilen "
                    "(BGH Raltegravir)."],
                   merke="Lizenzbemühen: Einzelfallprüfung.", titel="Lizenzbemühungen", level=1),
             frage("Fehlt das öffentliche Interesse, weil nur eine relativ kleine Gruppe von Patienten auf Isentress angewiesen ist?", False,
                   ["**Nein!** Ein öffentliches Interesse kann auch bestehen, wenn nur eine **relativ kleine Patientengruppe** betroffen ist, "
                    "insbesondere wenn sie ohne das Medikament einer besonders hohen Gefährdung ausgesetzt wäre (BGH Raltegravir)."],
                   merke="Auch kleine, stark gefährdete Gruppen begründen öffentliches Interesse.", titel="Öffentliches Interesse", level=2),
             frage("Braucht M zusätzlich einen Verfügungsgrund nach §§ 935, 940 ZPO?", False,
                   ["**Nein!** Die einstweilige Verfügung nach § 85 Abs. 1 PatG bedarf nicht zusätzlich der Voraussetzungen der §§ 935, 940 ZPO. "
                    "Ein zögerliches Verhalten des Lizenzsuchers fließt in die Interessenabwägung ein, spricht aber nicht ohne weiteres gegen das "
                    "öffentliche Interesse (BGH Raltegravir)."],
                   merke="§ 85 PatG ist eine eigenständige Verfügungsgrundlage.", titel="Verfügungsgrund", level=3,
                   norms=["§ 85 Abs. 1 PatG"]),
             ],
            abschnitt="Abs. 1: Lizenzbemühen und öffentliches Interesse", level=2, concepts=["pat_zwangslizenz"], norms=["§ 24 Abs. 1 PatG"],
            cases=["pat_bgh_raltegravir"], step=VS + ".4.3"),
        *fallkette("p03n24-2", "Der Cholesterinsenker",
            "S vertreibt den Cholesterinsenker Praluent (Alirocumab); Patentinhaberin A klagt wegen Verletzung ihres Patents auf "
            "PCSK9-Antikörper. Ein anderes PCSK9-Präparat ist auf dem Markt. Auf eine Anfrage erklärt A, Lizenzen grundsätzlich abzulehnen, "
            "unter außergewöhnlichen Umständen aber zu erwägen. S beantragt kurz darauf eine vorläufige Zwangslizenz.",
            [frage("Durfte S nach dieser Erklärung von weiteren Lizenzbemühungen absehen?", False,
                   ["**Nein!** Umfang und Dauer der Bemühungen hängen auch von der Reaktion des Inhabers ab. Weitere Bemühungen sind nur entbehrlich, "
                    "wenn er die Zustimmung **schlechthin verweigert**; die Erklärung, Lizenzen grundsätzlich abzulehnen, aber unter "
                    "außergewöhnlichen Umständen zu erwägen, genügt dafür nicht (BGH Alirocumab)."],
                   merke="Nur die endgültige Verweigerung erspart weitere Bemühungen.", titel="Verweigerung", level=2),
             frage("Begründet schon das Bedürfnis nach einem zweiten Präparat ein öffentliches Interesse?", False,
                   ["**Nein!** Ein öffentliches Interesse kann zu bejahen sein, wenn etwa durch **statistisch signifikante Studienergebnisse** belegt "
                    "ist, dass der Wirkstoff bei schweren Erkrankungen therapeutische Eigenschaften hat, die andere Mittel nicht oder nicht in "
                    "gleichem Maß bieten, insbesondere ein geringeres Sterberisiko (BGH Alirocumab). Das hatte S nicht belegt."],
                   merke="Öffentliches Interesse: belegter therapeutischer Mehrwert.", titel="Therapeutischer Mehrwert", level=2),
             ],
            abschnitt="Abs. 1: Lizenzbemühen und öffentliches Interesse", level=2, concepts=["pat_zwangslizenz"], norms=["§ 24 Abs. 1 PatG"],
            cases=["pat_bgh_alirocumab"], step=VS + ".4.3"),
        *fallkette("p03n24-3", "Die Verbesserungserfindung",
            "J hat ein Patent auf eine verbesserte Wärmepumpe, die sich nur mit dem Verdichter aus dem älteren Patent von Ä bauen lässt. J hat Ä "
            "über Monate eine Lizenz zu marktüblichen Bedingungen angeboten; Ä lehnt jede Lizenz ab.",
            [frage("Kann J eine Zwangslizenz verlangen, ohne ein öffentliches Interesse darzulegen?", True,
                   ["**Ja!** Kann der Lizenzsucher seine jüngere patentierte Erfindung nicht verwerten, ohne das ältere Patent zu verletzen, hat er "
                    "Anspruch auf eine Zwangslizenz, wenn er sich erfolglos bemüht hat und seine Erfindung einen **wichtigen technischen Fortschritt "
                    "von erheblicher wirtschaftlicher Bedeutung** aufweist (§ 24 Abs. 2 S. 1 PatG)."],
                   merke="Abhängige Erfindung: Fortschritt statt öffentliches Interesse.", titel="Abhängige Erfindung", level=2),
             frage("Kann Ä im Gegenzug eine Lizenz an der Erfindung von J verlangen?", True,
                   ["**Ja!** Der Inhaber des älteren Patents kann eine **Gegenlizenz** zu angemessenen Bedingungen für die Benutzung der jüngeren "
                    "Erfindung verlangen (§ 24 Abs. 2 S. 2 PatG)."],
                   merke="Abhängigkeitslizenz gegen Gegenlizenz.", titel="Gegenlizenz", level=1),
             frage("Kann J die Zwangslizenz später ohne sein eigenes Patent an einen Dritten übertragen?", False,
                   ["**Nein!** Die Zwangslizenz an einer Erfindung, die Gegenstand eines älteren Patents ist, kann nur **zusammen mit dem Patent mit "
                    "jüngerem Zeitrang** übertragen werden (§ 24 Abs. 7 S. 2 PatG). Ä erhält außerdem eine angemessene Vergütung "
                    "(§ 24 Abs. 6 S. 4 PatG)."],
                   merke="Abhängigkeitslizenz folgt dem jüngeren Patent.", titel="Übertragung", level=2),
             ],
            abschnitt="Abs. 2, 6 und 7: Abhängige Erfindung", level=2, concepts=["pat_zwangslizenz"], norms=["§ 24 PatG"], step=VS + ".4.3"),
        *fallkette("p03n24-4", "Der Mobilfunkstandard",
            "Das Patent von P ist für einen Mobilfunkstandard essenziell; P hat erklärt, Lizenzen zu fairen, angemessenen und "
            "nichtdiskriminierenden Bedingungen (FRAND) zu vergeben. Gerätehersteller H nutzt den Standard ohne Lizenz. Im Verletzungsprozess "
            "vor dem Landgericht verlangt H, P müsse ihm eine Lizenz geben.",
            [frage("Kann H im Verletzungsprozess eine Zwangslizenz nach § 24 PatG geltend machen?", False,
                   ["**Nein!** Über die Zwangslizenz nach § 24 PatG entscheidet allein das **Bundespatentgericht** auf Klage (§ 81 Abs. 1 PatG). "
                    "Im Verletzungsprozess kommt nur ein Einwand aus anderen Vorschriften in Betracht."],
                   merke="§ 24 PatG gehört vor das BPatG, nicht vor das Landgericht.", titel="Zwangslizenz im Verletzungsprozess", level=1),
             frage("Kann H dem Unterlassungsanspruch einen kartellrechtlichen Einwand entgegenhalten?", True,
                   ["**Ja!** Verweigert ein marktbeherrschender Inhaber die Lizenz missbräuchlich (Art. 102 AEUV), kann der Beklagte dies dem "
                    "Unterlassungsanspruch entgegenhalten (BGH Orange-Book-Standard). Für standardessenzielle Patente mit FRAND-Erklärung hat der "
                    "EuGH die Pflichten beider Seiten konkretisiert (EuGH Huawei/ZTE)."],
                   merke="Kartellrechtlicher Zwangslizenzeinwand: Art. 102 AEUV.", titel="Kartellrechtlicher Einwand", level=2,
                   concepts=["pat_unterlassung"]),
             frage("Genügt es, dass H im Prozess allgemein seine Lizenzbereitschaft erklärt?", False,
                   ["**Nein!** Der Benutzer muss sich selbst **lizenzwillig** verhalten: nach einem Verletzungshinweis und einem FRAND-Angebot des "
                    "Inhabers zügig ein konkretes Gegenangebot machen und für die Benutzung Sicherheit leisten (EuGH Huawei/ZTE). Wer nur "
                    "verzögert, kann sich auf den Einwand nicht berufen."],
                   merke="FRAND-Einwand nur für den lizenzwilligen Benutzer.", titel="Lizenzwilligkeit", level=3),
             ],
            abschnitt="Abgrenzung: kartellrechtlicher Zwangslizenzeinwand", level=3, concepts=["pat_zwangslizenz", "pat_lizenz"],
            norms=["§ 24 PatG"], step=VS + ".4.3"),
    ]),
    # ================================================================== § 33 PatG
    dict(id="p03n33", order=3300, titel="§ 33 PatG: Entschädigung aus der offengelegten Anmeldung", einheiten=[
        intro("p03n33-0", "Der vorläufige Schutz",
              "Vor der Erteilung hat die Anmeldung noch keine Verbietungswirkung (§ 58 Abs. 1 S. 3 PatG). Ab der Veröffentlichung des Hinweises "
              "auf die Akteneinsicht (§ 32 Abs. 5 PatG) gibt § 33 Abs. 1 PatG dem Anmelder aber einen Anspruch auf **angemessene "
              "Entschädigung** gegen jeden, der den Gegenstand der Anmeldung benutzt, obwohl er wusste oder wissen musste, dass er Gegenstand "
              "der Anmeldung ist. **Weitergehende Ansprüche** (Unterlassung, Schadensersatz) sind ausgeschlossen. Kein Anspruch bei offensichtlich "
              "fehlender Patentfähigkeit (§ 33 Abs. 2 PatG); Verjährung frühestens ein Jahr nach Erteilung (§ 33 Abs. 3 PatG). Wird die "
              "Anmeldung zurückgenommen oder zurückgewiesen, gilt die Wirkung als nicht eingetreten (§ 58 Abs. 2 PatG). Für europäische "
              "Anmeldungen gilt Art. II § 1 IntPatÜG.",
              norms=["§ 33 PatG", "§ 58 PatG", "Art. II § 1 IntPatÜG"], concepts=["pat_akteneinsicht", "pat_schadensersatz"], abschnitt="Überblick"),
        *fallkette("p03n33-1", "Die Kamerakupplung",
            "Die Anmeldung von K für eine Kupplung zweier optischer Geräte wird offengelegt; zwei Jahre später wird das Patent erteilt. "
            "Zulieferer Z stellt genau in der Zeit dazwischen 84 Kupplungen her und verkauft sie, obwohl er die Offenlegungsschrift kennt.",
            [frage("Kann K für diesen Zeitraum Unterlassung und Schadensersatz nach § 139 PatG verlangen?", False,
                   ["**Nein!** Die gesetzlichen Wirkungen des Patents treten erst mit der Veröffentlichung der Erteilung ein (§ 58 Abs. 1 S. 3 "
                    "PatG). Für die Zeit davor gewährt § 33 Abs. 1 PatG nur Entschädigung; **weitergehende Ansprüche sind ausgeschlossen**."],
                   merke="Vor Erteilung keine Ansprüche aus § 139 PatG.", titel="Keine Verbietungswirkung", level=1,
                   norms=["§ 58 Abs. 1 PatG"]),
             frage("Was schuldet Z für die Zeit zwischen Offenlegung und Erteilung?", 2,
                   ["**Eine angemessene Entschädigung.** Z hat den Gegenstand der Anmeldung nach Veröffentlichung des Hinweises (§ 32 Abs. 5 PatG) benutzt und **wusste**, dass "
                    "er Gegenstand der Anmeldung war (§ 33 Abs. 1 PatG). Fahrlässige Unkenntnis („wissen musste“) hätte genügt."],
                   optionen=["Nichts, weil das Patent noch nicht erteilt war", "Schadensersatz nach § 139 Abs. 2 PatG",
                             "Eine angemessene Entschädigung", "Nur Unterlassung für die Zukunft"],
                   merke="Entschädigung: Benutzung nach Offenlegung plus Kenntnis oder Kennenmüssen.", titel="Entschädigung", level=1),
             frage("Kann K statt einer Lizenzgebühr den Gewinn herausverlangen, den Z erzielt hat?", False,
                   ["**Nein!** Die Entschädigung nach § 33 PatG umfasst **nicht die Herausgabe des Verletzergewinns**; geschuldet ist eine den "
                    "Umständen nach angemessene Vergütung, regelmäßig nach Art einer Lizenzgebühr (BGH Sektionaltor II unter Hinweis auf "
                    "Offenendspinnmaschine)."],
                   merke="Entschädigung = Lizenzgebühr, kein Verletzergewinn.", titel="Kein Verletzergewinn", level=2,
                   cases=["pat_bgh_sektionaltor_ii"]),
             frage("Ist der Entschädigungsanspruch dann verjährt?", False,
                   ["**Nein!** Für die Verjährung gilt zwar das BGB, sie tritt aber **frühestens ein Jahr nach Erteilung** des Patents ein "
                    "(§ 33 Abs. 3 S. 1 PatG)."],
                   abwandlung="K klagt erst fünf Jahre nach den Verkäufen, aber sechs Monate nach der Erteilung, die sich verzögert hatte.",
                   merke="Verjährung frühestens ein Jahr nach Erteilung.", titel="Verjährung", level=2, norms=["§ 33 Abs. 3 PatG"]),
             ],
            abschnitt="Abs. 1 und 3: Entschädigung und Verjährung", level=1, concepts=["pat_schadensersatz"], norms=["§ 33 Abs. 1 PatG"],
            step=VS + ".5.2"),
        *fallkette("p03n33-2", "Die zurückgewiesene Anmeldung",
            "A meldet ein Verfahren zur Wasseraufbereitung zum Patent an; die Anmeldung wird offengelegt. Wettbewerber W wendet das Verfahren "
            "danach in Kenntnis der Anmeldung an. A verlangt Entschädigung.",
            [frage("Muss W zahlen, wenn die Anmeldung offensichtlich nicht patentfähig ist, weil das Verfahren seit Jahren in Lehrbüchern steht?", False,
                   ["**Nein!** Der Anspruch besteht nicht, wenn der Gegenstand der Anmeldung **offensichtlich nicht patentfähig** ist "
                    "(§ 33 Abs. 2 PatG). Offensichtlich ist der Mangel, wenn er sich ohne eingehende Prüfung aufdrängt."],
                   merke="Offensichtlich nicht patentfähig: keine Entschädigung.", titel="Offensichtlich nicht patentfähig", level=1,
                   norms=["§ 33 Abs. 2 PatG"]),
             frage("Behält A den Anspruch für die Zeit bis zur Zurückweisung?", False,
                   ["**Nein!** Wird die Anmeldung nach der Offenlegung zurückgenommen oder zurückgewiesen oder gilt sie als zurückgenommen, gilt die "
                    "Wirkung nach § 33 Abs. 1 PatG **als nicht eingetreten** (§ 58 Abs. 2 PatG)."],
                   abwandlung="Die Prüfungsstelle weist die Anmeldung später rechtskräftig zurück.",
                   merke="Zurückweisung beseitigt den Entschädigungsanspruch rückwirkend.", titel="Zurückweisung", level=2,
                   norms=["§ 58 Abs. 2 PatG"]),
             ],
            abschnitt="Abs. 2: Ausschluss", level=1, concepts=["pat_schadensersatz"], norms=["§ 33 PatG"], step=VS + ".5.2"),
        *fallkette("p03n33-3", "Die englische Anmeldung",
            "Die europäische Anmeldung von K, mit der auch für Deutschland Schutz begehrt wird, ist auf Englisch veröffentlicht. B benutzt die "
            "Erfindung in Deutschland und kennt die Anmeldung. Erst ein Jahr später übermittelt K dem B eine deutsche Übersetzung der Ansprüche.",
            [frage("Schuldet B schon ab der Veröffentlichung der englischen Anmeldung Entschädigung?", False,
                   ["**Nein!** Ist die europäische Anmeldung nicht auf Deutsch veröffentlicht, steht die Entschädigung erst ab dem Tag zu, an dem "
                    "das DPMA eine **deutsche Übersetzung der Ansprüche** veröffentlicht oder der Anmelder sie dem Benutzer übermittelt hat "
                    "(Art. II § 1 Abs. 2 IntPatÜG)."],
                   merke="EP-Anmeldung: Entschädigung erst ab deutscher Übersetzung der Ansprüche.", titel="Übersetzung", level=2,
                   norms=["Art. II § 1 Abs. 2 IntPatÜG"]),
             frage("Kann K für die Zeit vor der Erteilung Unterlassung verlangen?", False,
                   ["**Nein!** Auch für europäische Anmeldungen gibt es nur eine angemessene Entschädigung; weitergehende Ansprüche nach "
                    "Art. 67 Abs. 1 EPÜ sind ausgeschlossen (Art. II § 1 Abs. 1 S. 3 IntPatÜG)."],
                   merke="Vor Erteilung nur Entschädigung, auch beim EP.", titel="Keine Unterlassung", level=1),
             ],
            abschnitt="Europäische Anmeldung: Art. II § 1 IntPatÜG", level=2, concepts=["pat_ep_validierung"], norms=["Art. II § 1 IntPatÜG"],
            step=VS + ".5.2"),
    ]),
    # ================================================================== § 139 PatG
    dict(id="p03n139", order=13900, titel="§ 139 PatG: Unterlassung und Schadensersatz", einheiten=[
        intro("p03n139-0", "Die Anspruchsgrundlage der Verletzungsklage",
              "§ 139 PatG gibt dem Verletzten gegen jeden, der **entgegen §§ 9 bis 13 PatG** eine patentierte Erfindung benutzt, zwei "
              "Ansprüche. **Abs. 1: Unterlassung**, verschuldensunabhängig, bei Wiederholungsgefahr (S. 1) oder Erstbegehungsgefahr (S. 2); "
              "ausgeschlossen, soweit die Inanspruchnahme eine **unverhältnismäßige**, durch das Ausschließlichkeitsrecht nicht gerechtfertigte "
              "Härte wäre, dann Ausgleich in Geld (S. 3 bis 5). **Abs. 2: Schadensersatz** bei Vorsatz oder Fahrlässigkeit, berechnet nach "
              "entgangenem Gewinn, Verletzergewinn oder Lizenzanalogie. **Abs. 3**: Beweiserleichterung bei Verfahren zur Herstellung neuer "
              "Erzeugnisse. Prüfung: Aktivlegitimation, Schutzbereich (§ 14 PatG), Benutzung (§§ 9, 10 PatG), keine Einwendung (§§ 11, 12 PatG, "
              "Erschöpfung, Lizenz), Passivlegitimation, Rechtsfolge. Daneben stehen die Ansprüche der §§ 140a bis 140e PatG.",
              norms=["§ 139 PatG"], concepts=["pat_unterlassung", "pat_schadensersatz", "pat_verletzung"], abschnitt="Überblick"),
        schema("p03n139-s", "Prüfungsschema Patentverletzung", "pat_schema_patentverletzung", abschnitt="Überblick"),
        *fallkette("p03n139-1", "Die Dosierpumpe",
            "P hat ein Patent auf eine Dosierpumpe. Importeur I, eine GmbH, führt baugleiche Pumpen eines chinesischen Herstellers ein, bietet "
            "sie auf ihrer Website an und hat 20 Stück verkauft. Vom Patent wusste niemand bei I. P verlangt Unterlassung und Schadensersatz.",
            [frage("Auf welche Vorschrift stützt P den Unterlassungsanspruch?", 1,
                   ["**§ 139 Abs. 1 S. 1 PatG.** Er gibt den Anspruch gegen den, der **entgegen §§ 9 bis 13 PatG** die Erfindung benutzt. § 9 PatG "
                    "beschreibt nur, welche Handlungen verboten sind; hier Einführen, Anbieten und Inverkehrbringen (§ 9 S. 2 Nr. 1 PatG)."],
                   optionen=["§ 9 S. 2 Nr. 1 PatG", "§ 139 Abs. 1 S. 1 PatG", "§ 1004 Abs. 1 BGB analog", "§ 140a Abs. 1 PatG"],
                   merke="§ 9 PatG verbietet, § 139 PatG gibt den Anspruch.", titel="Anspruchsgrundlage", level=1, step=VS + ".5.1"),
             frage("Entfällt die Wiederholungsgefahr, wenn I verspricht, keine Pumpen mehr zu verkaufen?", False,
                   ["**Nein!** Eine begangene Verletzung **indiziert** die Wiederholungsgefahr. Sie entfällt regelmäßig nur durch eine "
                    "**strafbewehrte Unterlassungserklärung**; ein einfaches Versprechen genügt nicht (§ 139 Abs. 1 S. 1 PatG)."],
                   merke="Wiederholungsgefahr: nur strafbewehrte Unterlassungserklärung beseitigt sie.", titel="Wiederholungsgefahr", level=1,
                   step=VS + ".5.1"),
             frage("Hängt der Unterlassungsanspruch davon ab, dass I das Patent kannte?", False,
                   ["**Nein!** Der Unterlassungsanspruch ist **verschuldensunabhängig**; er setzt nur die rechtswidrige Benutzung und Begehungsgefahr "
                    "voraus. Verschulden verlangt erst der Schadensersatz (§ 139 Abs. 2 S. 1 PatG)."],
                   merke="Unterlassung ohne Verschulden.", titel="Kein Verschulden nötig", level=1, step=VS + ".5.1"),
             frage("Handelt I fahrlässig, obwohl niemand dort das Patent kannte?", True,
                   ["**Ja!** Wer ein Erzeugnis herstellt oder **erstmals im Inland in Verkehr bringt**, muss die Schutzrechtslage prüfen; die "
                    "Anforderungen sind streng. Unkenntnis des Patents entlastet nicht (vgl. BGH Glasfasern II). I schuldet Schadensersatz "
                    "(§ 139 Abs. 2 S. 1 PatG)."],
                   merke="Hersteller und Importeur müssen Schutzrechte prüfen.", titel="Verschulden des Importeurs", level=2,
                   norms=["§ 139 Abs. 2 PatG"], cases=["pat_bgh_glasfasern_ii"], step=VS + ".5.2"),
             frage("Haftet auch G persönlich auf Schadensersatz?", True,
                   ["**Ja!** Der gesetzliche Vertreter einer Gesellschaft, die ein verletzendes Erzeugnis herstellt oder erstmals im Inland in "
                    "Verkehr bringt, haftet, wenn er die möglichen und zumutbaren Maßnahmen unterlässt, die **Geschäftstätigkeit so einzurichten**, "
                    "dass keine technischen Schutzrechte Dritter verletzt werden (BGH Glasfasern II)."],
                   abwandlung="P verklagt zusätzlich den Geschäftsführer G der I-GmbH.",
                   merke="Geschäftsführer haftet für Organisationsversagen.", titel="Geschäftsführerhaftung", level=2,
                   norms=["§ 139 Abs. 2 PatG"], cases=["pat_bgh_glasfasern_ii"], step=VS + ".5.2"),
             frage("Muss P im Einzelnen darlegen, welche organisatorischen Fehler G begangen hat?", False,
                   ["**Nein!** Dass die schuldhafte Verletzung durch die Gesellschaft auf einem schuldhaften Fehlverhalten ihres gesetzlichen "
                    "Vertreters beruht, bedarf im Regelfall **keines näheren Klägervortrags** und keiner näheren Feststellungen (BGH Glasfasern II)."],
                   merke="Organisationsverschulden des Geschäftsführers wird regelmäßig angenommen.", titel="Darlegungslast", level=3,
                   cases=["pat_bgh_glasfasern_ii"], step=VS + ".5.2"),
             ],
            abschnitt="Abs. 1 und 2: Grundfall", level=1, concepts=["pat_unterlassung", "pat_schadensersatz"], norms=["§ 139 Abs. 1 PatG"],
            step=VS + ".5.1"),
        *fallkette("p03n139-2", "Der Messestand",
            "Der italienische Hersteller B stellt auf einer Messe in Hannover eine Verpackungsmaschine aus, die das deutsche Patent von K "
            "verletzt; am Stand liegen Prospekte mit Preisen aus. Verkauft hat B in Deutschland noch keine Maschine.",
            [frage("Besteht Wiederholungsgefahr, obwohl B noch nichts verkauft hat?", True,
                   ["**Ja!** Das Ausstellen mit Prospekten und Preisen macht die Maschine der Nachfrage zugänglich und ist ein **Anbieten** im "
                    "Inland (§ 9 S. 2 Nr. 1 PatG; vgl. BGH Kupplung für optische Geräte). Mit der begangenen Verletzung ist die Wiederholungsgefahr "
                    "indiziert."],
                   merke="Messeangebot im Inland ist schon Verletzung.", titel="Anbieten auf der Messe", level=1,
                   norms=["§ 9 PatG"], cases=["pat_bgh_kupplung_optische_geraete"]),
             frage("Kann K schon jetzt Unterlassung verlangen?", True,
                   ["**Ja!** Der Anspruch besteht auch, wenn eine Zuwiderhandlung **erstmalig droht** (§ 139 Abs. 1 S. 2 PatG). Eine ernsthafte, "
                    "konkrete Ankündigung, die Maschine in Deutschland zu vertreiben, begründet Erstbegehungsgefahr."],
                   abwandlung="B stellt nur auf einer Messe in Mailand aus und kündigt in einer deutschen Fachzeitschrift den Vertrieb in Deutschland ab Januar an.",
                   merke="Konkrete Ankündigung: Erstbegehungsgefahr.", titel="Erstbegehungsgefahr", level=2),
             frage("Kann B die Erstbegehungsgefahr ohne strafbewehrte Unterlassungserklärung beseitigen?", True,
                   ["**Ja!** Anders als die Wiederholungsgefahr wird die Erstbegehungsgefahr nicht vermutet. Sie entfällt schon durch ein "
                    "**ernsthaftes, unmissverständliches Abrücken** von der Ankündigung (actus contrarius)."],
                   merke="Erstbegehungsgefahr: Widerruf der Ankündigung genügt.", titel="Wegfall der Erstbegehungsgefahr", level=3),
             ],
            abschnitt="Abs. 1: Wiederholungs- und Erstbegehungsgefahr", level=2, concepts=["pat_unterlassung"], norms=["§ 139 Abs. 1 PatG"],
            step=VS + ".5.1"),
        *fallkette("p03n139-3", "Der Lizenzgeber",
            "P hat seiner Gesellschaft L, deren Alleingesellschafter er ist, eine ausschließliche Lizenz an seinem Patent für Tintenpatronen "
            "erteilt. V vertreibt nachgebaute Patronen. P und L klagen jeweils auf Unterlassung und Schadensersatz.",
            [frage("Kann P trotz der ausschließlichen Lizenz selbst Unterlassung verlangen?", True,
                   ["**Ja!** Dem Patentinhaber steht der Unterlassungsanspruch **grundsätzlich auch dann** zu, wenn er eine ausschließliche Lizenz "
                    "vergeben hat (BGH Tintenpatrone). Der ausschließliche Lizenznehmer ist daneben aus eigenem Recht klagebefugt (§ 15 Abs. 2 PatG)."],
                   merke="Inhaber und ausschließlicher Lizenznehmer können beide klagen.", titel="Unterlassung des Inhabers", level=2,
                   cases=["pat_bgh_tintenpatrone"], step=VS + ".1"),
             frage("Hat P auch einen eigenen Schadensersatzanspruch?", True,
                   ["**Ja!** Der Inhaber hat eigene Ansprüche, wenn ihm aus der Lizenzvergabe **fortdauernde materielle Vorteile** erwachsen. Dafür "
                    "genügt, dass er als Alleingesellschafter am Gewinn des Lizenznehmers beteiligt ist (BGH Cinch-Stecker)."],
                   merke="Wirtschaftliche Teilhabe begründet eigenen Schaden des Inhabers.", titel="Schaden des Lizenzgebers", level=2,
                   cases=["pat_bgh_cinch_stecker"], step=VS + ".5.2"),
             frage("Sind P und L hinsichtlich des Schadensersatzes Mitgläubiger?", False,
                   ["**Nein!** Inhaber und ausschließlicher Lizenznehmer sind **keine Mitgläubiger**; jeder kann den Verletzer unabhängig vom anderen "
                    "in Anspruch nehmen und hat einen eigenen Anspruch auf Auskunft und Rechnungslegung (BGH Tintenpatrone)."],
                   merke="Inhaber und Lizenznehmer: getrennte Ansprüche.", titel="Keine Mitgläubiger", level=3,
                   cases=["pat_bgh_tintenpatrone"]),
             ],
            abschnitt="Aktivlegitimation", level=2, concepts=["pat_lizenz", "pat_schadensersatz"], norms=["§ 139 PatG"],
            cases=["pat_bgh_cinch_stecker"], step=VS + ".1"),
        *fallkette("p03n139-4", "Die Polstermaschine",
            "B hat patentverletzende Maschinen, die Papier zu Polstermaterial umformen, verkauft und verleast. Daneben verkauft B das Papier, "
            "das in den Maschinen verarbeitet wird. K verlangt Schadensersatz.",
            [frage("Welche Berechnung des Schadens sieht § 139 Abs. 2 PatG nicht vor?", 3,
                   ["**Die pauschale doppelte Lizenzgebühr.** K kann wählen zwischen dem **konkreten Schaden** einschließlich entgangenen Gewinns "
                    "(§ 139 Abs. 2 S. 1 PatG), dem **Verletzergewinn** (S. 2) und der **Lizenzanalogie** (S. 3). Einen Strafzuschlag kennt das Gesetz "
                    "nicht."],
                   optionen=["Entgangener eigener Gewinn", "Herausgabe des Verletzergewinns", "Angemessene Lizenzgebühr",
                             "Pauschal doppelte Lizenzgebühr"],
                   merke="Drei Berechnungsarten, freie Wahl.", titel="Berechnungsarten", level=1, step=VS + ".5.2"),
             frage("Gehören die Gewinne aus dem Papierverkauf zum herauszugebenden Verletzergewinn?", True,
                   ["**Ja!** Zu berücksichtigen sind alle Gewinne, die mit der Verletzung **in ursächlichem Zusammenhang** stehen, auch aus "
                    "Zusatzgeschäften, die selbst keine Benutzung nach § 9 oder § 10 PatG sind, aber einen hinreichenden Bezug zum verletzenden "
                    "Gegenstand haben (BGH Polsterumarbeitungsmaschine)."],
                   merke="Zusatzgeschäfte zählen zum Verletzergewinn.", titel="Zusatzgeschäfte", level=2),
             frage("Muss B den gesamten Gewinn herausgeben, wenn Kunden die Maschine auch wegen anderer Eigenschaften kaufen?", False,
                   ["**Nein!** Herauszugeben ist nur der Anteil, der **auf der Benutzung der Erfindung beruht**. Dabei zählt, ob die erfindungsgemäße "
                    "Ausgestaltung und ihre Vorteile für die Abnehmer erkennbar waren oder in der Werbung herausgestellt wurden (BGH Kabelschloss)."],
                   merke="Verletzergewinn: nur der kausale Anteil.", titel="Kausalanteil", level=2,
                   cases=["pat_bgh_kabelschloss"]),
             frage("Zählen die Gewinne aus diesem Auftrag zum Schaden?", True,
                   ["**Ja!** Gewinne aus einem Vertrag, der in ursächlichem Zusammenhang mit einem verletzenden Angebot im Inland steht, bleiben "
                    "nicht deshalb unberücksichtigt, weil der Vertrag **im patentfreien Ausland** erfüllt wurde (BGH Verdampfungstrockneranlage)."],
                   abwandlung="B hat eine Anlage in Deutschland nur angeboten; gebaut und geliefert wurde sie in einem Land ohne Patentschutz.",
                   merke="Inländisches Angebot: auch Auslandsgeschäft zählt.", titel="Angebot und Auslandsgeschäft", level=3,
                   cases=["pat_bgh_verdampfungstrockneranlage"]),
             frage("Kann B einwenden, er hätte den Auftrag auch mit einer patentfreien Anlage erhalten?", False,
                   ["**Nein!** Der Einwand, dasselbe wirtschaftliche Ergebnis wäre auch durch nicht verletzende Handlungen erreichbar gewesen, "
                    "schließt den Schadensersatz grundsätzlich **nicht** aus (BGH Verdampfungstrockneranlage)."],
                   merke="Kein Einwand rechtmäßigen Alternativverhaltens.", titel="Alternativverhalten", level=3,
                   cases=["pat_bgh_verdampfungstrockneranlage"]),
             ],
            abschnitt="Abs. 2: Schadensberechnung", level=2, concepts=["pat_schadensersatz"], norms=["§ 139 Abs. 2 PatG"],
            cases=["pat_bgh_polsterumarbeitungsmaschine"], step=VS + ".5.2"),
        *fallkette("p03n139-5", "Die Cabrio-Heizung",
            "K hat ein Patent auf ein Heizsystem für Cabriolets, das warme Luft in den Nackenbereich der Insassen bläst. Autohersteller B "
            "verbaut es serienmäßig und wird zur Unterlassung verurteilt. B verlangt, die bereits bestellten Fahrzeuge noch ausliefern zu dürfen.",
            [frage("Genügt für eine Aufbrauchfrist, dass die Umstellung der Produktion Zeit und Geld kostet?", False,
                   ["**Nein!** Eine Aufbrauchfrist kommt nur in Betracht, wenn die sofortige Durchsetzung wegen **besonderer Umstände des "
                    "Einzelfalls** eine unverhältnismäßige, durch das Ausschließlichkeitsrecht und die **regelmäßigen Folgen** seiner Durchsetzung "
                    "nicht gerechtfertigte Härte wäre und daher treuwidrig (BGH Wärmetauscher). Umstellungskosten sind regelmäßige Folgen."],
                   merke="Regelmäßige Folgen der Verurteilung sind keine Härte.", titel="Aufbrauchfrist", level=2,
                   cases=["pat_bgh_waermetauscher"]),
             frage("Können bei der Härte auch Interessen Dritter berücksichtigt werden, etwa der Kunden mit bestellten Fahrzeugen?", True,
                   ["**Ja!** Seit 2021 ist der Unterlassungsanspruch ausgeschlossen, soweit er aufgrund der besonderen Umstände und der Gebote von Treu "
                    "und Glauben **für den Verletzer oder Dritte** zu einer unverhältnismäßigen, durch das Ausschließlichkeitsrecht nicht "
                    "gerechtfertigten Härte führen würde (§ 139 Abs. 1 S. 3 PatG)."],
                   merke="Unverhältnismäßigkeit: auch Drittinteressen zählen.", titel="Interessen Dritter", level=2),
             frage("Geht K leer aus, wenn das Gericht die Unterlassung insoweit ausschließt?", False,
                   ["**Nein!** Dem Verletzten ist ein **angemessener Ausgleich in Geld** zu gewähren (§ 139 Abs. 1 S. 4 PatG); der "
                    "Schadensersatzanspruch nach Abs. 2 bleibt unberührt (§ 139 Abs. 1 S. 5 PatG)."],
                   merke="Statt Unterlassung: Geldausgleich plus Schadensersatz.", titel="Geldausgleich", level=1),
             ],
            abschnitt="Abs. 1 S. 3 bis 5: Unverhältnismäßigkeit", level=2, concepts=["pat_unterlassung"], norms=["§ 139 Abs. 1 PatG"],
            step=VS + ".5.1"),
        *fallkette("p03n139-6", "Der neue Kunststoff",
            "K hat ein Patent auf ein Verfahren zur Herstellung eines neuen Kunststoffs. B vertreibt denselben Kunststoff und behauptet, ihn auf "
            "andere Weise herzustellen; sein Verfahren will B nicht offenlegen.",
            [frage("Muss K beweisen, dass B nach dem patentierten Verfahren herstellt?", False,
                   ["**Nein!** Ist Gegenstand des Patents ein Verfahren zur Herstellung eines **neuen Erzeugnisses**, gilt das gleiche Erzeugnis eines "
                    "anderen bis zum Beweis des Gegenteils als nach dem patentierten Verfahren hergestellt (§ 139 Abs. 3 S. 1 PatG). B muss sein "
                    "abweichendes Verfahren beweisen."],
                   merke="Neues Erzeugnis: Vermutung der Verfahrensbenutzung.", titel="Beweisvermutung", level=1),
             frage("Muss B dafür seine Betriebsgeheimnisse vollständig offenlegen?", False,
                   ["**Nein!** Bei der Erhebung des Gegenbeweises sind die berechtigten Interessen des Beklagten an der Wahrung seiner **Herstellungs- "
                    "und Betriebsgeheimnisse** zu berücksichtigen (§ 139 Abs. 3 S. 2 PatG), etwa durch Begutachtung unter Verschwiegenheitspflichten."],
                   merke="Gegenbeweis mit Geheimnisschutz.", titel="Geheimnisschutz", level=2),
             frage("Bleibt K dann ohne Beweiserleichterung?", False,
                   ["**Nein!** Die Vermutung des § 139 Abs. 3 PatG greift nicht, aber nach Treu und Glauben kann B eine **sekundäre Darlegungslast** "
                    "treffen: Er muss Tatsachen spezifizieren, die K nicht zugänglich sind, ihm aber ohne weiteres möglich und zumutbar (BGH "
                    "Blasenfreie Gummibahn II). Daneben kommt Besichtigung nach § 140c PatG in Betracht."],
                   abwandlung="Der Kunststoff war schon vor der Anmeldung bekannt; nur das Verfahren ist neu.",
                   merke="Bekanntes Erzeugnis: sekundäre Darlegungslast und Besichtigung.", titel="Sekundäre Darlegungslast", level=3,
                   cases=["pat_bgh_blasenfreie_gummibahn_ii"]),
             ],
            abschnitt="Abs. 3: Beweislast bei Verfahrenspatenten", level=2, concepts=["pat_verletzung", "pat_verfahrenserzeugnis"],
            norms=["§ 139 Abs. 3 PatG"], step=VS + ".3.1"),
    ]),
    # ================================================================== §§ 140a bis 140e PatG
    dict(id="p03n140", order=14000, titel="§§ 140a bis 140e PatG: Vernichtung, Rückruf, Auskunft, Besichtigung", einheiten=[
        intro("p03n140-0", "Die Nebenansprüche",
              "Neben Unterlassung und Schadensersatz kann der Verletzte verlangen: **Vernichtung** verletzender Erzeugnisse im Besitz oder "
              "Eigentum des Verletzers und der vorwiegend zur Herstellung genutzten Geräte (§ 140a Abs. 1 und 2 PatG), **Rückruf** und "
              "endgültiges **Entfernen aus den Vertriebswegen** (§ 140a Abs. 3 PatG), jeweils unter Verhältnismäßigkeitsvorbehalt "
              "(§ 140a Abs. 4 PatG); **Auskunft** über Herkunft und Vertriebsweg, unter Umständen auch von Dritten (§ 140b PatG); **Vorlage "
              "und Besichtigung** schon bei hinreichender Wahrscheinlichkeit einer Verletzung (§ 140c PatG); Vorlage von **Bank-, Finanz- und "
              "Handelsunterlagen** zur Sicherung des Schadensersatzes (§ 140d PatG); **Urteilsbekanntmachung** (§ 140e PatG). Für die "
              "Bezifferung des Schadens tritt die Rechnungslegung aus § 242 BGB hinzu.",
              norms=["§ 140a PatG", "§ 140b PatG", "§ 140c PatG", "§ 140d PatG", "§ 140e PatG"],
              concepts=["pat_rechtsfolgen_nebenanspruche", "pat_besichtigung"], abschnitt="Überblick"),
        *fallkette("p03n140-1", "Die MP3-Player",
            "Der Zoll hält am Frankfurter Flughafen eine Sammelsendung MP3-Player aus Shanghai an, die das Patent von P verletzen sollen. "
            "Befördert hat sie der Expressdienstleister T, der in der zollamtlichen Anordnung als Besitzer genannt ist. P verlangt von T "
            "Zustimmung zur Vernichtung.",
            [frage("Kann nur Schuldner des Vernichtungsanspruchs sein, wer selbst einen Benutzungstatbestand des § 9 PatG verwirklicht?", False,
                   ["**Nein!** Verletzer ist auch, wer die Benutzung durch einen Dritten **ermöglicht oder fördert**, obwohl er sich mit zumutbarem "
                    "Aufwand die Kenntnis verschaffen kann, dass die unterstützte Handlung das Patent verletzt (BGH MP3-Player-Import). Er schuldet "
                    "Unterlassung und Vernichtung."],
                   merke="Auch der Förderer kann Verletzer sein.", titel="Förderer als Verletzer", level=2),
             frage("Muss T jede transportierte Ware auf Schutzrechtsverletzungen prüfen?", False,
                   ["**Nein!** Den Spediteur trifft **keine generelle Prüfungspflicht** im Hinblick auf Schutzrechtsverletzungen durch die "
                    "transportierte Ware (BGH MP3-Player-Import)."],
                   merke="Keine allgemeine Prüfpflicht des Spediteurs.", titel="Keine generelle Prüfpflicht", level=1),
             frage("Muss T jetzt Erkundigungen einholen?", True,
                   ["**Ja!** Liegen dem Spediteur **konkrete Anhaltspunkte** für eine Schutzrechtsverletzung vor, kann er verpflichtet sein, "
                    "Erkundigungen einzuholen und die Ware gegebenenfalls selbst zu prüfen (BGH MP3-Player-Import)."],
                   abwandlung="P hat T vor der Ankunft mit Testergebnissen auf die Verletzung durch genau diese Player hingewiesen.",
                   merke="Konkrete Hinweise begründen Prüfpflichten.", titel="Konkrete Anhaltspunkte", level=2),
             frage("Darf T im Prozess die Übereinstimmung der Player mit dem Patent mit Nichtwissen bestreiten?", True,
                   ["**Ja!** Den auf Vernichtung in Anspruch genommenen Spediteur trifft keine Obliegenheit, sich die Informationen über die "
                    "Beschaffenheit der Ware für ein qualifiziertes Bestreiten zu beschaffen (BGH MP3-Player-Import; § 138 Abs. 4 ZPO)."],
                   merke="Spediteur darf mit Nichtwissen bestreiten.", titel="Bestreiten mit Nichtwissen", level=3),
             ],
            abschnitt="§ 140a PatG: Vernichtung", level=2, concepts=["pat_rechtsfolgen_nebenanspruche"], norms=["§ 140a Abs. 1 PatG"],
            cases=["pat_bgh_mp3_player_import"], step=VS + ".5.3"),
        *fallkette("p03n140-2", "Die Reifenreparatursets",
            "Die italienische B liefert Reparatursets für Autoreifen, die das Patent von K verletzen, an Händler in Deutschland. K verlangt "
            "Rückruf der Sets und ihr endgültiges Entfernen aus den Vertriebswegen.",
            [frage("Kann K Rückruf und endgültiges Entfernen nebeneinander verlangen?", True,
                   ["**Ja!** Die Ansprüche auf Rückruf und auf endgültiges Entfernen aus den Vertriebswegen (§ 140a Abs. 3 S. 1 PatG) können "
                    "**nebeneinander** geltend gemacht werden (BGH Abdichtsystem)."],
                   merke="Rückruf und Entfernen: kumulativ.", titel="Rückruf und Entfernen", level=1),
             frage("Scheitert der Rückruf daran, dass B im Ausland sitzt?", False,
                   ["**Nein!** Der Anspruch auf Rückruf ist nicht deshalb ausgeschlossen, weil der Verpflichtete **im Ausland ansässig** ist "
                    "(BGH Abdichtsystem)."],
                   merke="Rückruf auch gegen ausländische Verletzer.", titel="Verletzer im Ausland", level=1),
             frage("Kann K dann die Vernichtung der ganzen Maschinen verlangen?", False,
                   ["**Nein!** Die Ansprüche aus § 140a Abs. 1 bis 3 PatG sind ausgeschlossen, wenn die Inanspruchnahme im Einzelfall "
                    "**unverhältnismäßig** ist; auch Interessen Dritter zählen (§ 140a Abs. 4 PatG). Lässt sich die Verletzung durch Ausbau eines "
                    "Teils beseitigen, ist die Vernichtung des Ganzen unverhältnismäßig."],
                   abwandlung="Die verletzende Pumpe ist ein austauschbares Bauteil teurer Abfüllmaschinen, die B ebenfalls vertreibt.",
                   merke="Mildere Mittel gehen der Vernichtung vor.", titel="Verhältnismäßigkeit", level=2,
                   norms=["§ 140a Abs. 4 PatG"]),
             ],
            abschnitt="§ 140a PatG: Rückruf und Verhältnismäßigkeit", level=1, concepts=["pat_rechtsfolgen_nebenanspruche"],
            norms=["§ 140a Abs. 3 PatG"], cases=["pat_bgh_abdichtsystem"], step=VS + ".5.3"),
        *fallkette("p03n140-3", "Die Abnehmerliste",
            "B ist wegen patentverletzender Werkzeuggriffe zur Auskunft über Hersteller, Lieferanten und gewerbliche Abnehmer verurteilt. B "
            "fürchtet, K werde die Abnehmer abwerben, legt ein Rechtsmittel ein und beantragt, die Zwangsvollstreckung einzustellen. Das Patent ist "
            "inzwischen abgelaufen.",
            [frage("Worüber muss B nach § 140b Abs. 3 PatG keine Auskunft geben?", 3,
                   ["**Über Gewinn und Gestehungskosten.** § 140b Abs. 3 PatG verlangt Namen und Anschriften der Hersteller, Lieferanten, "
                    "Vorbesitzer und gewerblichen Abnehmer sowie Mengen und Preise. Gewinn und Kosten sind Gegenstand der **Rechnungslegung** "
                    "nach § 242 BGB, die der Bezifferung des Schadensersatzes dient."],
                   optionen=["Namen und Anschriften der Lieferanten", "Gewerbliche Abnehmer und Verkaufsstellen",
                             "Mengen und bezahlte Preise", "Erzielter Gewinn und Gestehungskosten"],
                   merke="Auskunft: Lieferkette; Rechnungslegung: Zahlen zum Schaden.", titel="Inhalt der Auskunft", level=1,
                   norms=["§ 140b Abs. 3 PatG"]),
             frage("Wird die Vollstreckung wegen des drohenden Nachteils durch die Abnehmerauskunft eingestellt?", False,
                   ["**Nein!** Ist der Schuldner zur Auskunft über Vertriebsweg und gewerbliche Abnehmer verurteilt, überwiegt regelmäßig das "
                    "Interesse des Gläubigers an der Durchsetzung, **auch wenn das Patent abgelaufen ist** (BGH Werkzeuggriff)."],
                   merke="Abnehmerauskunft wird regelmäßig vollstreckt.", titel="Einstellung der Vollstreckung", level=2,
                   cases=["pat_bgh_werkzeuggriff"]),
             frage("Kann K auch vom Logistikunternehmen L Auskunft verlangen, das die Griffe für B gelagert und versandt hat?", True,
                   ["**Ja!** Bei offensichtlicher Rechtsverletzung oder nach Klageerhebung gegen den Verletzer besteht der Anspruch auch gegen "
                    "Dritte, die in gewerblichem Ausmaß für verletzende Tätigkeiten genutzte **Dienstleistungen erbracht** haben (§ 140b Abs. 2 S. 1 "
                    "Nr. 3 PatG), sofern kein Zeugnisverweigerungsrecht besteht."],
                   merke="Drittauskunft gegen Dienstleister der Verletzung.", titel="Drittauskunft", level=2,
                   norms=["§ 140b Abs. 2 PatG"]),
             frage("Muss B über die Umsätze mit dem ganzen Werkzeug Rechnung legen, obwohl nur der Griff patentiert ist?", True,
                   ["**Ja!** Bei zusammengesetzten Vorrichtungen, von denen nur ein Teil patentiert ist, erstreckt sich der Anspruch auf Auskunft und "
                    "Rechnungslegung grundsätzlich auch auf die mit der **Gesamtvorrichtung** erzielten Umsätze und Gewinne (BGH Aufschlussgerät)."],
                   merke="Rechnungslegung erfasst die Gesamtvorrichtung.", titel="Gesamtvorrichtung", level=3,
                   cases=["pat_bgh_aufschlussgeraet"]),
             ],
            abschnitt="§ 140b PatG: Auskunft", level=2, concepts=["pat_rechtsfolgen_nebenanspruche"], norms=["§ 140b PatG"],
            step=VS + ".5.3"),
        *fallkette("p03n140-4", "Das Schweißwerk",
            "P hat ein Patent auf ein Verfahren zum Laserschweißen. Aus einer Dissertation schließt P, dass Autohersteller A das Verfahren in "
            "einem Werk anwendet. Bevor P klagt, will er die Schweißstationen durch einen Sachverständigen untersuchen lassen.",
            [frage("Kann P die Besichtigung schon vor einer Klage im Eilverfahren durchsetzen?", True,
                   ["**Ja!** Wer **mit hinreichender Wahrscheinlichkeit** ein Patent benutzt, muss die Besichtigung einer Sache oder eines Verfahrens "
                    "dulden, wenn sie zur Begründung der Ansprüche erforderlich ist (§ 140c Abs. 1 PatG); die Duldung kann durch **einstweilige "
                    "Verfügung** angeordnet werden (§ 140c Abs. 3 PatG), regelmäßig verbunden mit einem selbständigen Beweisverfahren."],
                   merke="Besichtigung: hinreichende Wahrscheinlichkeit, eilig per Verfügung.", titel="Besichtigungsanspruch", level=1,
                   norms=["§ 140c Abs. 1 PatG", "§ 140c Abs. 3 PatG"]),
             frage("Darf P das Gutachten sofort selbst lesen?", False,
                   ["**Nein!** Geheimhaltungsinteressen des vermeintlichen Verletzers werden regelmäßig gewahrt, indem zunächst nur **namentlich "
                    "benannte, zur Verschwiegenheit verpflichtete Anwälte** Einsicht erhalten. Dem Inhaber selbst darf es erst freigegeben werden, "
                    "wenn A seine Geheimhaltungsinteressen geltend machen konnte (BGH Lichtbogenschnürung)."],
                   merke="Gutachten zuerst nur an verpflichtete Anwälte.", titel="Einsicht in das Gutachten", level=2,
                   cases=["pat_bgh_lichtbogenschnuerung"]),
             frage("Genügt es, dass A sich pauschal auf Betriebsgeheimnisse beruft?", False,
                   ["**Nein!** A muss **im Einzelnen** darlegen, welche Informationen im Gutachten geheimhaltungswürdig sind und welche Nachteile ihm "
                    "aus der Offenbarung drohen (BGH Lichtbogenschnürung)."],
                   merke="Geheimnisse konkret darlegen.", titel="Darlegung der Geheimnisse", level=2,
                   cases=["pat_bgh_lichtbogenschnuerung"]),
             frage("Kommt es für die Herausgabe dann noch darauf an, wie wahrscheinlich die Verletzung ist?", False,
                   ["**Nein!** Die Wahrscheinlichkeit von Verletzungsansprüchen ist für die Herausgabe des Gutachtens nur erheblich, wenn der "
                    "Antragsgegner **berechtigte Geheimhaltungsinteressen dargelegt** hat (BGH Ästhetische Behandlung). Gegen die Entscheidung über "
                    "die Herausgabe ist die sofortige Beschwerde statthaft."],
                   abwandlung="A legt keine konkreten Geheimhaltungsinteressen dar.",
                   merke="Ohne dargelegte Geheimnisse: Herausgabe des Gutachtens.", titel="Herausgabe ohne Geheimnisse", level=3,
                   cases=["pat_bgh_aesthetische_behandlung"]),
             frage("Muss das Gericht im Prozess die Begutachtung der Anlage anordnen, weil P sonst beweisfällig bleibt?", False,
                   ["**Nein!** Aus § 286 ZPO folgt keine Pflicht, die Vorlage (§ 142 ZPO) oder Begutachtung (§ 144 ZPO) eines Gegenstands im Besitz der "
                    "nicht beweisbelasteten Partei anzuordnen. Das Gericht ist dazu allenfalls verpflichtet, wenn die Voraussetzungen eines Anspruchs "
                    "aus § 140c PatG vorliegen (BGH Rohrmuffe)."],
                   abwandlung="P hat auf die Besichtigung verzichtet und sofort Verletzungsklage erhoben.",
                   merke="Prozessuale Anordnung folgt den Maßstäben des § 140c PatG.", titel="Vorlage im Prozess", level=3,
                   cases=["pat_bgh_rohrmuffe"]),
             ],
            abschnitt="§ 140c PatG: Vorlage und Besichtigung", level=2, concepts=["pat_besichtigung"], norms=["§ 140c PatG"],
            cases=["pat_bgh_lichtbogenschnuerung"], step=VS + ".5.3"),
        *fallkette("p03n140-5", "Die Fachpresse",
            "K hat gegen B ein Verletzungsurteil erstritten. B hatte zuvor in Fachzeitschriften verbreitet, das Patent von K sei wertlos und "
            "seine Produkte seien frei. Außerdem verschiebt B Vermögen ins Ausland; die Verletzungen erfolgten in großem Umfang.",
            [frage("Kann das Gericht K die Befugnis zusprechen, das Urteil auf Kosten von B bekannt zu machen?", True,
                   ["**Ja!** Der obsiegenden Partei kann im Urteil die Befugnis zugesprochen werden, das Urteil auf Kosten der unterliegenden Partei "
                    "öffentlich bekannt zu machen, wenn sie ein **berechtigtes Interesse** darlegt (§ 140e S. 1 PatG). Die Äußerungen von B in der "
                    "Fachpresse begründen ein solches Interesse."],
                   merke="Urteilsbekanntmachung bei berechtigtem Interesse.", titel="Bekanntmachungsbefugnis", level=1,
                   norms=["§ 140e PatG"]),
             frage("Darf K das Urteil sofort nach Verkündung veröffentlichen?", False,
                   ["**Nein!** Der Ausspruch ist **nicht vorläufig vollstreckbar** (§ 140e S. 4 PatG). Die Befugnis erlischt, wenn K sie nicht "
                    "innerhalb von **drei Monaten nach Rechtskraft** nutzt (§ 140e S. 3 PatG)."],
                   merke="Bekanntmachung erst nach Rechtskraft, binnen drei Monaten.", titel="Zeitpunkt", level=2,
                   norms=["§ 140e PatG"]),
             frage("Kann K von B Vorlage von Bankunterlagen verlangen, um den Schadensersatz zu sichern?", True,
                   ["**Ja!** Bei einer in **gewerblichem Ausmaß** begangenen Verletzung kann der Verletzte im Fall des § 139 Abs. 2 PatG Vorlage von "
                    "Bank-, Finanz- oder Handelsunterlagen verlangen, wenn ohne sie die Erfüllung des Schadensersatzanspruchs **fraglich** ist "
                    "(§ 140d Abs. 1 PatG)."],
                   merke="§ 140d PatG sichert die Durchsetzung des Schadensersatzes.", titel="Bankunterlagen", level=2,
                   norms=["§ 140d Abs. 1 PatG"]),
             ],
            abschnitt="§§ 140d, 140e PatG: Unterlagen und Bekanntmachung", level=2, concepts=["pat_rechtsfolgen_nebenanspruche"],
            norms=["§ 140e PatG"], step=VS + ".5.3"),
    ]),
    # ================================================================== §§ 141, 141a, 145 PatG
    dict(id="p03n141", order=14100, titel="§§ 141, 141a, 145 PatG: Verjährung, Restschadensersatz, Klagenkonzentration", einheiten=[
        intro("p03n141-0", "Zeitliche und prozessuale Grenzen",
              "Ansprüche wegen Patentverletzung verjähren nach dem BGB (§ 141 S. 1 PatG): regelmäßig in **drei Jahren** ab dem Schluss des "
              "Jahres, in dem der Anspruch entstanden ist und der Verletzte Kenntnis erlangt hat (§ 195 BGB, § 199 Abs. 1 BGB). Auch nach Verjährung "
              "muss der Verletzer herausgeben, was er auf Kosten des Berechtigten erlangt hat (**Restschadensersatz**, § 141 S. 2 PatG mit "
              "§ 852 BGB). Ansprüche aus anderen Vorschriften, etwa Bereicherungsrecht, bleiben unberührt (§ 141a PatG). Unabhängig von der "
              "Verjährung kann ein Anspruch nach § 242 BGB **verwirkt** sein. Prozessual zwingt § 145 PatG den Kläger, gegen dieselbe oder eine "
              "gleichartige Handlung alle Patente in einer Klage geltend zu machen (**Klagenkonzentration**).",
              norms=["§ 141 PatG", "§ 141a PatG", "§ 145 PatG"], concepts=["pat_schadensersatz", "pat_klagekonzentration"], abschnitt="Überblick"),
        *fallkette("p03n141-1", "Die Netzteile",
            "K weiß seit 2014, dass B patentverletzende Netzteile verkauft; B verkauft sie bis Ende 2015. K klagt erst im Mai 2019 auf "
            "Schadensersatz und Rechnungslegung. B erhebt die Einrede der Verjährung.",
            [frage("Wann endete die Verjährungsfrist für den Schadensersatz aus den Verkäufen 2015?", 1,
                   ["**Mit Ablauf des Jahres 2018.** Nach § 141 S. 1 PatG gelten § 195 BGB und § 199 Abs. 1 BGB: Die Frist von drei Jahren beginnt mit dem Schluss des Jahres, in "
                    "dem der Anspruch entstanden ist und K Kenntnis hatte. Die Klage im Mai 2019 kam zu spät."],
                   optionen=["Ende 2016", "Ende 2018", "Mai 2019", "Ende 2025"],
                   merke="Drei Jahre ab Jahresende der Kenntnis.", titel="Regelverjährung", level=1,
                   norms=["§ 141 PatG"]),
             frage("Muss B den durch die Verletzung erzielten Gewinn trotzdem herausgeben?", True,
                   ["**Ja!** Hat der Verpflichtete durch die Verletzung auf Kosten des Berechtigten etwas erlangt, gilt § 852 BGB entsprechend "
                    "(§ 141 S. 2 PatG). Der Verletzer hat auch nach Verjährung den **erzielten Gewinn** nach Bereicherungsrecht herauszugeben (BGH "
                    "Spannungsversorgungsvorrichtung)."],
                   merke="Restschadensersatz: Gewinn bleibt herauszugeben.", titel="Restschadensersatz", level=2),
             frage("Muss B auch über Gestehungskosten und Werbung Rechnung legen?", True,
                   ["**Ja!** Zur Durchsetzung des Restschadensersatzes hat der Verletzer über den erzielten Gewinn und seine **Gestehungskosten** "
                    "Rechnung zu legen und schuldet Angaben zur **Werbung** für den Verletzungsgegenstand (BGH Spannungsversorgungsvorrichtung). "
                    "Gewinne aus Zusatzgeschäften zählen auch hier mit (BGH Polsterumarbeitungsmaschine)."],
                   merke="Rechnungslegung auch beim Restschadensersatz.", titel="Rechnungslegung", level=2,
                   cases=["pat_bgh_polsterumarbeitungsmaschine"]),
             ],
            abschnitt="§ 141 PatG: Verjährung und Restschadensersatz", level=2, concepts=["pat_schadensersatz"], norms=["§ 141 PatG"],
            cases=["pat_bgh_spannungsversorgungsvorrichtung"], step=VS + ".4.5"),
        *fallkette("p03n141-2", "Das Aufschlussgerät",
            "K erwirkt 2015 ein rechtskräftiges Urteil, das die Schadensersatzpflicht von B wegen eines patentverletzenden Aufschlussgeräts "
            "feststellt. Erst 2023 verlangt K Rechnungslegung, um den Schaden zu beziffern. B hält den Anspruch auf Rechnungslegung für "
            "verjährt.",
            [frage("Verjährt der rechtskräftig festgestellte Schadensersatzanspruch in drei Jahren?", False,
                   ["**Nein!** Rechtskräftig festgestellte Ansprüche verjähren in **dreißig Jahren** (§ 197 Abs. 1 Nr. 3 BGB)."],
                   merke="Titulierter Anspruch: dreißig Jahre.", titel="Festgestellter Anspruch", level=1),
             frage("Ist der Anspruch auf Rechnungslegung nach drei Jahren verjährt?", False,
                   ["**Nein!** Der auf § 242 BGB gestützte, akzessorische Anspruch auf Auskunft und Rechnungslegung verjährt **nicht vor dem "
                    "Hauptanspruch**, dessen Durchsetzung er dient, auch wenn dieser rechtskräftig festgestellt ist und dreißig Jahre läuft (BGH "
                    "Aufschlussgerät)."],
                   merke="Hilfsanspruch verjährt nicht vor dem Hauptanspruch.", titel="Akzessorische Rechnungslegung", level=2),
             ],
            abschnitt="§ 141 PatG: Verjährung und Restschadensersatz", level=2, concepts=["pat_schadensersatz", "pat_rechtsfolgen_nebenanspruche"],
            norms=["§ 141 PatG"], cases=["pat_bgh_aufschlussgeraet"], step=VS + ".4.5"),
        *fallkette("p03n141-3", "Der Temperaturwächter",
            "P weiß seit zwölf Jahren, dass B einen patentgemäßen Temperaturwächter vertreibt, und unternimmt nichts. B baut im Vertrauen darauf "
            "seine Fertigung aus. Dann verlangt P Schadensersatz und Herausgabe der Bereicherung.",
            [frage("Kann der Anspruch verwirkt sein, auch wenn er noch nicht verjährt ist?", True,
                   ["**Ja!** Ansprüche wegen Patentverletzung können **verwirkt** sein, wenn sich der Verletzer wegen der Duldung über einen längeren "
                    "Zeitraum bei objektiver Beurteilung darauf einrichten durfte und eingerichtet hat, dass der Inhaber sein Recht nicht mehr "
                    "geltend macht (§ 242 BGB; BGH Temperaturwächter)."],
                   merke="Verwirkung: Duldung plus schutzwürdiges Einrichten.", titel="Verwirkung", level=2),
             frage("Ist die Verwirkung gegenüber dem Bereicherungsanspruch ausgeschlossen?", False,
                   ["**Nein!** Bereicherungsansprüche bleiben neben § 139 PatG zwar bestehen (§ 141a PatG), doch ist auch ihnen gegenüber der Einwand "
                    "der Verwirkung **nicht schlechthin oder regelmäßig ausgeschlossen** (BGH Temperaturwächter)."],
                   merke="Auch Bereicherungsansprüche können verwirkt sein.", titel="Bereicherungsanspruch", level=3,
                   norms=["§ 141a PatG"]),
             frage("Genügt für die Verwirkung schon der lange Zeitablauf?", False,
                   ["**Nein!** Zeit- und Umstandsmoment stehen in **Wechselwirkung**; zeitliche und sonstige Umstände müssen in ihrer Gesamtheit "
                    "tragen, dass Treu und Glauben die Verfolgung des Anspruchs verwehren (BGH Temperaturwächter)."],
                   merke="Zeit allein verwirkt nicht.", titel="Zeit- und Umstandsmoment", level=2),
             ],
            abschnitt="Verwirkung und § 141a PatG", level=2, concepts=["pat_schadensersatz"], norms=["§ 141 PatG"],
            cases=["pat_bgh_temperaturwaechter"], step=VS + ".4.5"),
        *fallkette("p03n141-4", "Die Fensterprofile",
            "K hat B aus Patent 1 wegen Fensterprofilrahmen verklagt und gewonnen. Danach erhebt K eine neue Klage gegen B wegen derselben "
            "Rahmen, diesmal aus Patent 2, das K schon während des ersten Prozesses gehörte.",
            [frage("Kann K die zweite Klage erheben?", False,
                   ["**Nein!** Wer eine Klage nach § 139 PatG erhoben hat, kann gegen den Beklagten wegen **derselben oder einer gleichartigen "
                    "Handlung** aus einem anderen Patent nur dann erneut klagen, wenn er ohne Verschulden nicht in der Lage war, dieses Patent im "
                    "früheren Rechtsstreit geltend zu machen (§ 145 PatG). B kann die Einrede erheben."],
                   merke="Alle Patente gegen dieselbe Handlung in eine Klage.", titel="Klagenkonzentration", level=1),
             frage("Ist die abgewandelte Ausführung eine gleichartige Handlung im Sinne von § 145 PatG?", False,
                   ["**Nein!** Gleichartig sind nur Handlungen mit zusätzlichen oder abgewandelten Merkmalen, bei denen es sich wegen eines **engen "
                    "technischen Zusammenhangs** aufdrängt, sie gemeinsam aus mehreren Patenten anzugreifen. Dass einzelne Teile auch für das "
                    "zweite Patent bedeutsam sind, genügt nicht (BGH Raffvorhang)."],
                   abwandlung="Die zweite Klage betrifft eine neue Rahmenform, von der nur einzelne Teile auch im ersten Prozess eine Rolle spielten.",
                   merke="Gleichartig nur bei engem technischen Zusammenhang.", titel="Gleichartige Handlung", level=2,
                   cases=["pat_bgh_raffvorhang"]),
             frage("Steht § 145 PatG einer neuen Klage aus demselben Patent 1 entgegen?", False,
                   ["**Nein!** § 145 PatG ist weder unmittelbar noch entsprechend anwendbar, wenn derselbe Beklagte **aus demselben Patent** erneut "
                    "verklagt wird. Entgegenstehen können aber Rechtshängigkeit oder Rechtskraft der ersten Klage (BGH Fensterflügel)."],
                   abwandlung="K klagt gegen die neue Rahmenform aus Patent 1.",
                   merke="Dasselbe Patent: nicht § 145 PatG, sondern Rechtskraft.", titel="Dasselbe Patent", level=2,
                   cases=["pat_bgh_fensterfluegel"]),
             ],
            abschnitt="§ 145 PatG: Klagenkonzentration", level=2, concepts=["pat_klagekonzentration"], norms=["§ 145 PatG"],
            cases=["pat_bgh_fensterfluegel"], step=VS + ".1"),
    ]),
]
