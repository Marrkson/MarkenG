# -*- coding: utf-8 -*-
"""Kapitel des Normkurses p03 (siehe p03_patg_normen.py). Jedes Kapitel trägt `order` (Sortierschlüssel nach Gesetz und Paragraph).
Teil Patentfähigkeit, Erteilung, Rechtsbestand, Verfahren: §§ 1, 3, 4, 21/22, 34/38, 59, 73/79, 81 bis 84, 99/100, 123 PatG und
§§ 1 bis 3, 15 bis 17 GebrMG. Die Fälle folgen BGH- und BPatG-Entscheidungen (patent/cases.py, patent/cases_p03a.py)."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

_PF = "step:pat_schema_patentfaehigkeit"

KAPITEL = [
    # ================================================================== § 1 PatG
    dict(id="p03n1", order=100, titel="§ 1 PatG: Erfindung und Ausschlüsse", einheiten=[
        intro("p03n1-0", "Technik und die Ausschlüsse „als solche“",
              "§ 1 Abs. 1 PatG verlangt eine **Erfindung auf einem Gebiet der Technik**, die neu, erfinderisch und gewerblich anwendbar ist. "
              "§ 1 Abs. 3 PatG nennt Gegenstände, die nicht als Erfindung gelten: Entdeckungen, Theorien und mathematische Methoden (Nr. 1), "
              "ästhetische Formschöpfungen (Nr. 2), Pläne und Regeln für gedankliche, spielerische oder geschäftliche Tätigkeiten sowie Programme "
              "(Nr. 3) und die Wiedergabe von Informationen (Nr. 4). Nach § 1 Abs. 4 PatG greift der Ausschluss nur, soweit Schutz für diese "
              "Gegenstände **als solche** begehrt wird.\n\n"
              "Der BGH prüft dreistufig: (1) Technizität, (2) konkretes technisches Problem mit technischen Mitteln gelöst, sonst Ausschluss "
              "als solches, (3) Neuheit und erfinderische Tätigkeit nur anhand der technischen Anweisungen (BGH Webseitenanzeige).",
              concepts=["pat_erfindung", "pat_technizitaet", "pat_programme"], norms=["§ 1 Abs. 1 PatG", "§ 1 Abs. 3 PatG", "§ 1 Abs. 4 PatG"],
              cases=["pat_bgh_webseitenanzeige"], abschnitt="Überblick"),
        schema("p03n1-0s", "Prüfungsschema programmbezogene Erfindung", "pat_schema_programmbezogene_erfindung", abschnitt="Überblick"),
        *fallkette("p03n1-1", "Der Webserver im Mikrocontroller",
            "Die A-GmbH meldet ein Verfahren an, mit dem ein ressourcenarmer, mikrocontrollerbasierter Leitrechner auf Anfrage eines Clients "
            "strukturierte Dokumente dynamisch erzeugt; das Programm ist so geschrieben, dass es mit dem knappen Speicher auskommt. Das BPatG "
            "hält die Lehre für ein Programm als solches.",
            [frage("Ist das Verfahren eine Lehre auf einem Gebiet der Technik im Sinne von § 1 Abs. 1 PatG?", True,
                   ["**Ja!** Ein Verfahren, das das **unmittelbare Zusammenwirken der Elemente eines Datenverarbeitungssystems** (Server und "
                    "Client) betrifft, ist stets technischer Natur. Ob die Anweisungen im Einzelnen technisch geprägt sind, spielt auf dieser "
                    "ersten Stufe keine Rolle (BGH Dynamische Dokumentengenerierung)."],
                   merke="Zusammenwirken von Server und Client ist stets technisch.", titel="Erste Stufe: Technizität", step="step:pat_schema_programmbezogene_erfindung.2"),
             frage("Ist der Ausschluss nach § 1 Abs. 3 Nr. 3, Abs. 4 PatG damit schon überwunden?", False,
                   ["**Nein!** Technizität ist nur die erste Hürde. Auf der zweiten Stufe muss die Lehre Anweisungen enthalten, die ein "
                    "**konkretes technisches Problem mit technischen Mitteln** lösen; sonst wird das Programm als solches beansprucht "
                    "(BGH Dynamische Dokumentengenerierung; BGH Webseitenanzeige)."],
                   merke="Zweite Stufe: konkretes technisches Problem, technische Mittel.", titel="Zweite Stufe: als solches", step="step:pat_schema_programmbezogene_erfindung.3.1"),
             frage("Genügt als technisches Mittel, dass das Programm auf die beschränkten Ressourcen des Rechners Rücksicht nimmt?", True,
                   ["**Ja!** Technische Mittel liegen nicht nur vor, wenn Systemkomponenten verändert oder neuartig adressiert werden. Es reicht, "
                    "dass der Programmablauf durch technische Gegebenheiten außerhalb der Anlage bestimmt wird oder das Programm gerade so "
                    "ausgestaltet ist, dass es **auf die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht nimmt** (BGH "
                    "Dynamische Dokumentengenerierung)."],
                   merke="Rücksicht auf technische Gegebenheiten der Anlage ist ein technisches Mittel.", titel="Technische Mittel", level=2,
                   step="step:pat_schema_programmbezogene_erfindung.3.2"),
            ],
            abschnitt="Abs. 1, 3 Nr. 3, Abs. 4: Programme", level=1, concepts=["pat_programme", "pat_technizitaet"],
            norms=["§ 1 Abs. 1 PatG", "§ 1 Abs. 3 Nr. 3 PatG", "§ 1 Abs. 4 PatG"], cases=["pat_bgh_dynamische_dokumentengenerierung"],
            step=_PF + ".2.2"),
        *fallkette("p03n1-2", "Die Rentabilität des Röntgengeräts",
            "Die S-AG meldet ein Verfahren an: Medizintechnische Geräte erfassen automatisch Einsatzdaten und senden sie an eine "
            "zentrale Datenbank; eine Auswerteeinrichtung errechnet daraus mit Vergütungs- und Kostendaten, ob sich ein weiteres Gerät "
            "rentiert. S meint, Messgrößen, Geräte und Datenbank machten das Verfahren technisch.",
            [frage("Ist ein Verfahren schon deshalb patentfähig, weil es sich zur Erreichung seines Erfolgs einer Datenverarbeitungsanlage "
                   "bedient?", False,
                   ["**Nein!** Weil § 1 Abs. 3 Nr. 3, Abs. 4 PatG Programme als solche ausschließt, muss die Lehre **Anweisungen zur Lösung eines "
                    "konkreten technischen Problems mit technischen Mitteln** enthalten. Der bloße Vorgang elektronischer Datenverarbeitung "
                    "genügt nicht (BGH Rentabilitätsermittlung)."],
                   merke="Datenverarbeitung allein macht kein Verfahren patentfähig.", titel="Datenverarbeitung genügt nicht"),
             frage("Gilt derselbe Maßstab, wenn es um den Ausschluss von Verfahren für geschäftliche Tätigkeiten geht?", True,
                   ["**Ja!** Für mathematische Methoden, Regeln für **geschäftliche Tätigkeiten** und die Wiedergabe von Informationen gilt "
                    "nichts anderes: Löst die Lehre ein konkretes technisches Problem, schadet ein geschäftlicher Zweck nicht; fehlt es daran, "
                    "greift der Ausschluss (BGH Rentabilitätsermittlung)."],
                   merke="Ein Maßstab für alle Ausschlüsse des § 1 Abs. 3 PatG.", titel="Geschäftliche Tätigkeit", norms=["§ 1 Abs. 3 Nr. 3 PatG"]),
             frage("Ist die Anmeldung danach dem Patentschutz zugänglich?", False,
                   ["**Nein!** Die Geräte werden weder verbessert noch gesteuert; die Lehre erschöpft sich in der **Aufbereitung "
                    "betriebswirtschaftlicher Daten**. Automatische Erfassung und Übertragung sind nur beiläufige Mittel des im Vordergrund "
                    "stehenden kaufmännischen Verfahrens (BGH Rentabilitätsermittlung)."],
                   merke="Kaufmännische Datenauswertung bleibt nicht technisch, auch wenn Geräte die Daten liefern.", titel="Ergebnis", level=2),
            ],
            abschnitt="Abs. 3 Nr. 3: Geschäftliche Tätigkeiten", level=1, concepts=["pat_programme", "pat_technizitaet"],
            norms=["§ 1 Abs. 3 Nr. 3 PatG", "§ 1 Abs. 4 PatG"], cases=["pat_bgh_rentabilitaetsermittlung"], step=_PF + ".2.2"),
        *fallkette("p03n1-3", "Die Kugel um die Messwerte",
            "Die F-GmbH meldet ein Verfahren an, das Position, Geschwindigkeit und Lage eines Flugzeugs ermittelt: Die Messwerte der "
            "Trägheitsanlage werden nicht unmittelbar in einen Kalman-Filter gegeben, sondern zuerst Mittelpunkt und Radius der kleinsten Kugel "
            "berechnet, die alle Messpunkte enthält. DPMA und BPatG sehen darin eine mathematische Methode.",
            [frage("Kann eine mathematische Methode trotz § 1 Abs. 3 Nr. 1 PatG patentfähig sein?", True,
                   ["**Ja!** Ausgeschlossen sind mathematische Methoden nur **als solche** (§ 1 Abs. 4 PatG). Patentierbar ist eine mathematische Methode, wenn sie "
                    "der **Lösung eines konkreten technischen Problems mit technischen Mitteln** dient (BGH Flugzeugzustand)."],
                   merke="Mathematik ist nur als solche ausgeschlossen.", titel="Mathematische Methode als solche"),
             frage("Hat das Verfahren den nötigen Bezug zur gezielten Anwendung von Naturkräften?", True,
                   ["**Ja!** Nichttechnisch ist eine mathematische Methode nur ohne Bezug zur gezielten Anwendung von Naturkräften. Hier dient sie "
                    "dazu, aus Messwerten **zuverlässigere Erkenntnisse über den Zustand des Flugzeugs** zu gewinnen und so die Funktionsweise des "
                    "Messsystems zu beeinflussen (BGH Flugzeugzustand)."],
                   merke="Auswertung von Messwerten über einen physikalischen Zustand ist technisch.", titel="Bezug zu Naturkräften", level=2),
             frage("Darf das BPatG die Patentfähigkeit verneinen, weil das Verfahren gegenüber dem Kalman-Filter allein keinen erkennbaren Vorteil "
                   "bietet?", False,
                   ["**Nein!** Ein Gegenstand, der neu ist und auf erfinderischer Tätigkeit beruht, ist nicht deshalb unpatentierbar, weil er "
                    "**keinen erkennbaren Vorteil** gegenüber dem Stand der Technik bietet. Ein technischer Fortschritt ist keine "
                    "Patentvoraussetzung (BGH Flugzeugzustand)."],
                   merke="Kein Vorteil, kein Fortschritt nötig.", titel="Kein Vorteil erforderlich", level=2),
            ],
            abschnitt="Abs. 3 Nr. 1: Entdeckungen und mathematische Methoden", level=1, concepts=["pat_technizitaet", "pat_erfindung"],
            norms=["§ 1 Abs. 3 Nr. 1 PatG", "§ 1 Abs. 4 PatG"], cases=["pat_bgh_flugzeugzustand"], step=_PF + ".2.2"),
        *fallkette("p03n1-4", "Das mutierte Leukämie-Gen",
            "T hält ein Patent auf ein Nukleinsäuremolekül, das für eine mutierte Rezeptortyrosinkinase (FLT3) codiert, wie sie bei Leukämie "
            "vorkommt; das Patent lehrt, die Sequenz zum Nachweis der Erkrankung zu nutzen. Klägerin K meint, T habe nur ein natürliches Gen "
            "entdeckt.",
            [frage("Ist die Bereitstellung der Sequenz mehr als eine bloße Entdeckung im Sinne von § 1 Abs. 3 Nr. 1 PatG?", True,
                   ["**Ja!** Eine Lehre, die die **Nutzung einer Entdeckung zur Herbeiführung eines bestimmten Erfolgs** lehrt, ist eine Lehre "
                    "zum technischen Handeln. Ausgeschlossen ist nur die Erkenntnis als solche (BGH Rezeptortyrosinkinase)."],
                   merke="Wer eine Entdeckung nutzbar macht, erfindet.", titel="Entdeckung oder Erfindung"),
             frage("Braucht die Lehre über die zweckgerichtete Nutzung des Naturgesetzes hinaus einen „erfinderischen Überschuss“?", False,
                   ["**Nein!** Die Lehre ist dem Patentschutz **unabhängig von einem erfinderischen Überschuss** zugänglich; das gilt auch für die "
                    "Bereitstellung einer für ein Humanprotein codierenden Nukleinsäuresequenz (BGH Rezeptortyrosinkinase)."],
                   merke="Kein erfinderischer Überschuss erforderlich.", titel="Erfinderischer Überschuss", level=2),
             frage("Muss der Anspruch die Sequenz ausdrücklich als „isoliert“ kennzeichnen, weil sie in der Natur vorkommt?", False,
                   ["**Nein!** Isoliertes biologisches Material kann nach § 1 Abs. 2 S. 2 PatG Gegenstand einer Erfindung sein, auch wenn es in "
                    "der Natur schon vorhanden war. Einer Kennzeichnung als isoliert oder technisch gewonnen **im Anspruch** bedarf es nicht "
                    "(BGH Rezeptortyrosinkinase)."],
                   merke="Kennzeichnung „isoliert“ im Anspruch ist entbehrlich.", titel="Kennzeichnung als isoliert", level=3,
                   norms=["§ 1 Abs. 2 PatG"], concepts=["pat_biotech"]),
            ],
            abschnitt="Abs. 3 Nr. 1: Entdeckungen und mathematische Methoden", level=1, concepts=["pat_technizitaet", "pat_biotech"],
            norms=["§ 1 Abs. 3 Nr. 1 PatG"], cases=["pat_bgh_rezeptortyrosinkinase"], step=_PF + ".2.2"),
        *fallkette("p03n1-5", "Das Entsperrbild",
            "A hält ein Patent auf das Entsperren eines Smartphones: Wischt der Nutzer mit dem Finger eine vorgegebene Bewegung, wird das "
            "Gerät entsperrt, und ein Entsperrbild bewegt sich mit dem Finger entlang eines angezeigten Pfads. M erhebt "
            "Nichtigkeitsklage.",
            [frage("Bleibt bei der erfinderischen Tätigkeit außer Betracht, wie das Entsperrbild gestaltet ist und dass es den Fingerweg "
                   "nachahmt?", True,
                   ["**Ja!** Anweisungen, die die **Vermittlung bestimmter Inhalte** betreffen und auf die menschliche Vorstellung zielen, bleiben "
                    "als solche außer Betracht (§ 1 Abs. 3 Nr. 4, Abs. 4 PatG). Dass das Bild die Steuerbewegung anschaulich imitiert, trägt nur dem "
                    "Vorstellungsvermögen Rechnung (BGH Entsperrbild)."],
                   merke="Inhalt und Gestaltung einer Anzeige zählen nicht.", titel="Inhalt der Information"),
             frage("Muss das Gericht prüfen, ob die Anzeige des Entsperrbildes zugleich ein technisches Lösungsmittel verkörpert?", True,
                   ["**Ja!** Informationsbezogene Merkmale sind darauf zu untersuchen, ob die Information zugleich ein **technisches "
                    "Lösungsmittel** verkörpert. Hier zeigt die Anzeige dem Nutzer, dass der Entsperrbefehl erkannt und ausgeführt wird; das erhöht "
                    "die Bedienungssicherheit und ist zu berücksichtigen (BGH Entsperrbild)."],
                   merke="Technische Wirkung der Anzeige zählt mit.", titel="Technisches Lösungsmittel", level=2),
             frage("Ist das Patent trotzdem nichtig, wenn der Stand der Technik einen virtuellen Schiebeschalter auf dem Touchscreen zeigt?", True,
                   ["**Ja!** Der Fachmann wurde durch den Stand der Technik angeregt, die Aufforderung zum Entsperren durch eine **optische Anzeige "
                    "der Befehlsausführung** zu ergänzen. Was dann bleibt, ist nur die nicht zu berücksichtigende Gestaltung der Information "
                    "(§ 4 PatG; BGH Entsperrbild)."],
                   merke="Nur die technischen Merkmale tragen die erfinderische Tätigkeit.", titel="Ergebnis", level=2, norms=["§ 4 PatG"],
                   step=_PF + ".4.3"),
            ],
            abschnitt="Abs. 3 Nr. 4: Wiedergabe von Informationen", level=1, concepts=["pat_programme", "pat_erfinderische_taetigkeit"],
            norms=["§ 1 Abs. 3 Nr. 4 PatG", "§ 1 Abs. 4 PatG"], cases=["pat_bgh_entsperrbild"], step=_PF + ".2.2"),
    ]),
    # ================================================================== § 3 PatG
    dict(id="p03n3", order=300, titel="§ 3 PatG: Neuheit", einheiten=[
        intro("p03n3-0", "Stand der Technik und Einzelvergleich",
              "Neu ist eine Erfindung, die nicht zum **Stand der Technik** gehört (§ 3 Abs. 1 S. 1 PatG). Dazu zählen alle Kenntnisse, die vor dem "
              "Zeitrang der Anmeldung durch Beschreibung, Benutzung oder in sonstiger Weise **der Öffentlichkeit zugänglich** waren (S. 2). "
              "§ 3 Abs. 2 PatG fügt **ältere, nachveröffentlichte Anmeldungen** hinzu, aber nur für die Neuheit (§ 4 S. 2 PatG). § 3 Abs. 3 "
              "und 4 PatG erlauben **zweckgebundenen Stoffschutz** für die erste und jede weitere medizinische Indikation; § 3 Abs. 5 PatG "
              "regelt die unschädliche Offenbarung.\n\n"
              "Geprüft wird im **Einzelvergleich**: Ist der Gegenstand des Anspruchs in einer einzelnen Entgegenhaltung **unmittelbar und "
              "eindeutig** offenbart, einschließlich dessen, was der Fachmann selbstverständlich mitliest (BGH Olanzapin)?",
              concepts=["pat_neuheit", "pat_offenbarung", "pat_zweite_indikation"], norms=["§ 3 Abs. 1 PatG", "§ 3 Abs. 2 PatG", "§ 3 Abs. 3 PatG"],
              cases=["pat_bgh_olanzapin"], abschnitt="Überblick"),
        *fallkette("p03n3-1", "Die Folien vom Workshop",
            "D hält ein Patent auf ein Verfahren, das Lackfehler auf Werkstücken optisch erkennt, dreidimensional vermisst und robotergestützt "
            "bearbeitet. Vor dem Anmeldetag hatte ein Mitarbeiter eines verbundenen Unternehmens auf einem frei zugänglichen Workshop Folien zu "
            "einem ähnlichen Verfahren gezeigt und als Ausdruck verteilt. K erhebt Nichtigkeitsklage.",
            [frage("Gehören die verteilten Folien zum Stand der Technik nach § 3 Abs. 1 S. 2 PatG?", True,
                   ["**Ja!** Öffentlich zugänglich ist, was ein **nicht abgegrenzter Personenkreis ohne Geheimhaltungspflicht** zur Kenntnis nehmen "
                    "kann. Die Folien wurden auf einem frei zugänglichen Workshop an Teilnehmer ausgehändigt, die keiner Geheimhaltung unterlagen "
                    "(BGH Oberflächendefekte)."],
                   merke="Ausgehändigte Vortragsfolien sind Stand der Technik.", titel="Öffentliche Zugänglichkeit"),
             frage("Wird der Offenbarungsgehalt der Folien dadurch beschränkt, dass der Referent im Vortrag mündlich erklärte, das Verfahren "
                   "laufe nur im Labor und nicht automatisiert?", False,
                   ["**Nein!** Der Offenbarungsgehalt von Präsentationsfolien, die den Teilnehmern überlassen wurden, ist **unabhängig von "
                    "einschränkenden Zusatzinformationen** aus dem Vortrag zu würdigen. Maßgeblich ist, was der Fachmann den Folien selbst entnimmt "
                    "(BGH Oberflächendefekte)."],
                   merke="Mündliche Einschränkungen begrenzen den Inhalt verteilter Folien nicht.", titel="Mündliche Einschränkung", level=2),
             frage("Wären die Folien Stand der Technik, wenn sie nur an Mitarbeiter eines Entwicklungspartners mit Vertraulichkeitsvereinbarung "
                   "gegangen wären?", False,
                   ["**Nein!** Wer zur **Geheimhaltung verpflichtet** ist, gehört nicht zur Öffentlichkeit. Kenntnisse, die nur einem solchen "
                    "geschlossenen Kreis mitgeteilt werden, sind nicht im Sinne von § 3 Abs. 1 S. 2 PatG der Öffentlichkeit zugänglich gemacht."],
                   merke="Geheimhaltungspflicht schließt Öffentlichkeit aus.", titel="Geschlossener Kreis",
                   abwandlung="Der Referent hatte die Folien nur an Mitarbeiter eines Entwicklungspartners gegeben, die eine Vertraulichkeitsvereinbarung unterzeichnet hatten."),
            ],
            abschnitt="Abs. 1: Stand der Technik", level=1, concepts=["pat_neuheit"], norms=["§ 3 Abs. 1 PatG"],
            cases=["pat_bgh_oberflaechendefekte"], step=_PF + ".3.1"),
        *fallkette("p03n3-2", "Das Tosylatsalz",
            "B hält ein Patent auf Sorafenib-Tosylat, ein Salz eines Krebswirkstoffs. Eine ältere Druckschrift nennt über 100 Wirkstoffe, "
            "darunter Sorafenib, die allein oder als Salz mit zahlreichen möglichen Salzbildnern zur Krebsbehandlung geeignet sein sollen; "
            "Tosylat steht in der Liste der Salzbildner.",
            [frage("Welcher Maßstab gilt für die neuheitsschädliche Offenbarung?", 1,
                   ["**Unmittelbar und eindeutig!** Neuheitsschädlich ist, was der Fachmann der Entgegenhaltung unmittelbar und eindeutig entnimmt, "
                    "einschließlich dessen, was er als **selbstverständlich mitliest**. Was er erst mit seinem Fachwissen ergänzt, ist nicht "
                    "offenbart (BGH Olanzapin)."],
                   optionen=["Alles, worauf der Fachmann mit seinem Fachwissen ohne Weiteres kommt",
                             "Was der Entgegenhaltung unmittelbar und eindeutig zu entnehmen ist, einschließlich des selbstverständlich Mitgelesenen",
                             "Nur, was in den Ansprüchen der Entgegenhaltung steht",
                             "Was die Entgegenhaltung ausdrücklich als ihre Erfindung bezeichnet"],
                   merke="Unmittelbar und eindeutig, mit dem Mitgelesenen.", titel="Maßstab der Offenbarung", cases=["pat_bgh_olanzapin"],
                   step=_PF + ".3.2"),
             frage("Ist Sorafenib-Tosylat durch die Druckschrift neuheitsschädlich vorweggenommen?", False,
                   ["**Nein!** Die Nennung von über 100 Wirkstoffen, die allein oder als Salz mit **zahlreichen Salzbildnern** in Betracht kommen, "
                    "offenbart nicht unmittelbar und eindeutig ein **bestimmtes Salz eines einzelnen Wirkstoffs**. Erst die Kombination aus zwei "
                    "Listen ergibt das Tosylat (BGH Sorafenib-Tosylat)."],
                   merke="Auswahl aus zwei Listen ist nicht offenbart.", titel="Auswahl aus Listen", level=2, step=_PF + ".3.2"),
             frage("Ist das Patent damit rechtsbeständig?", False,
                   ["**Nein!** Neuheit genügt nicht. Sorafenib war schlecht wasserlöslich; eine **Präformulierungsstudie mit Salzscreening** lag "
                    "nahe, und wegen des niedrigen pKs-Werts bot sich Tosylat als einer von wenigen geeigneten Salzbildnern an. Das Salz war nach "
                    "§ 4 PatG nahegelegt (BGH Sorafenib-Tosylat)."],
                   merke="Neu ist nicht gleich erfinderisch.", titel="Erfinderische Tätigkeit", level=2, norms=["§ 4 PatG"],
                   concepts=["pat_erfinderische_taetigkeit"], step=_PF + ".4.3"),
             frage("Ist das Salz jetzt vorweggenommen, obwohl die Druckschrift es nicht als Teil ihrer Erfindung beschreibt?", True,
                   ["**Ja!** Für die Neuheit kommt es, anders als bei der unzulässigen Erweiterung, nicht darauf an, ob der Gegenstand **als zur "
                    "Erfindung gehörend** offenbart ist. Es genügt, dass er in der Entgegenhaltung unmittelbar und eindeutig offenbart ist "
                    "(BGH Aufbaupfosten)."],
                   merke="Auch ein Vergleichsbeispiel nimmt die Neuheit.", titel="Offenbarung als Vergleichsbeispiel", level=3,
                   abwandlung="Eine weitere Druckschrift nennt Sorafenib-Tosylat ausdrücklich, aber nur als bekanntes Vergleichssalz, von dem sie abrät.",
                   cases=["pat_bgh_aufbaupfosten"], step=_PF + ".3.2"),
            ],
            abschnitt="Abs. 1: Offenbarung im Einzelvergleich", level=1, concepts=["pat_neuheit", "pat_offenbarung"], norms=["§ 3 Abs. 1 PatG"],
            cases=["pat_bgh_sorafenib_tosylat"], step=_PF + ".3.2"),
        *fallkette("p03n3-3", "Die zurückgenommene ältere Anmeldung",
            "P hält ein Patent auf ein Verfahren, mit dem Fernsehsender eine Zusatzinformation zum 16:9-Format (PALplus) übertragen. Eine ältere "
            "Anmeldung mit früherem Prioritätstag beschreibt dasselbe Verfahren; sie wurde erst nach dem Prioritätstag des Patents veröffentlicht "
            "und gilt seitdem wegen nicht gezahlter Jahresgebühr als zurückgenommen.",
            [frage("Kann die ältere Anmeldung der Neuheit entgegenstehen, obwohl sie am Prioritätstag noch nicht veröffentlicht war?", True,
                   ["**Ja!** Als Stand der Technik gilt auch der Inhalt **älterer Anmeldungen**, die erst an oder nach dem Zeitrang der jüngeren "
                    "Anmeldung veröffentlicht werden (§ 3 Abs. 2 PatG; für europäische Patente Art. 54 Abs. 3 EPÜ). Das verhindert "
                    "Doppelpatentierung."],
                   merke="Ältere Rechte zählen für die Neuheit.", titel="Ältere Anmeldung"),
             frage("Bleibt die ältere Anmeldung Stand der Technik, obwohl sie nach ihrer Veröffentlichung als zurückgenommen gilt?", True,
                   ["**Ja!** Eine ältere Anmeldung bleibt zu berücksichtigen, wenn sie bei ihrer **Veröffentlichung noch anhängig** war. Rücknahme "
                    "oder Rücknahmefiktion danach ändern daran nichts (BGH PALplus)."],
                   merke="Anhängigkeit bei Veröffentlichung genügt.", titel="Spätere Rücknahme", level=2),
             frage("Ist die ältere Anmeldung auch bei der Prüfung der erfinderischen Tätigkeit heranzuziehen?", False,
                   ["**Nein!** Unterlagen nach § 3 Abs. 2 PatG werden bei der erfinderischen Tätigkeit **nicht in Betracht gezogen** (§ 4 S. 2 PatG). "
                    "Sie schaden nur, wenn sie den Gegenstand vollständig vorwegnehmen."],
                   merke="Ältere Rechte: nur Neuheit, nie erfinderische Tätigkeit.", titel="Kein Naheliegen aus älteren Rechten", norms=["§ 4 PatG"]),
            ],
            abschnitt="Abs. 2: Ältere Anmeldungen", level=1, concepts=["pat_neuheit"], norms=["§ 3 Abs. 2 PatG"],
            cases=["pat_bgh_palplus"], step=_PF + ".3.1"),
        *fallkette("p03n3-4", "Das Enzym gegen Fructoseintoleranz",
            "F hält ein Patent auf ein „Mittel zur Anwendung bei Fructoseintoleranz“, das das seit Langem bekannte Enzym Glucoseisomerase mit "
            "Metallionen enthält. Die Beschreibung erklärt theoretisch, das Enzym wandle im Darm Fructose in Glucose um; Versuche enthält sie "
            "nicht. E legt Einspruch ein.",
            [frage("Kann der Anspruch neu sein, obwohl Glucoseisomerase längst bekannt ist?", True,
                   ["**Ja!** § 3 Abs. 3 und 4 PatG erlauben **zweckgebundenen Stoffschutz**: Ein bekannter Stoff ist für eine medizinische "
                    "Anwendung patentfähig, wenn diese Anwendung nicht zum Stand der Technik gehört. Gegenstand ist die **Eignung des Stoffs für den "
                    "medizinischen Zweck** (BGH Fructoseintoleranz)."],
                   merke="Bekannter Stoff, neue medizinische Anwendung: neu.", titel="Zweckgebundener Stoffschutz", step=_PF + ".3.3"),
             frage("Muss die Anmeldung die Wirkung durch In-vitro-, Tier- oder klinische Versuche belegen?", False,
                   ["**Nein!** Versuche sind nicht zwingend. Aus der Anmeldung muss sich aber eine **hinreichende Erwartung** ergeben, dass der Stoff "
                    "die beanspruchte Eignung hat; der Fachmann muss diese Wahrscheinlichkeit verlässlich einschätzen können (BGH Fructoseintoleranz)."],
                   merke="Keine Versuche nötig, aber hinreichende Erfolgserwartung.", titel="Beleg der Wirkung", level=2),
             frage("Darf das Patent widerrufen werden, obwohl E nicht bewiesen hat, dass das Enzym im Darm unwirksam ist?", True,
                   ["**Ja!** Allein fehlende Beweismittel tragen keinen Widerruf. Hier fehlt aber schon die **hinreichende Erwartung**: Die Annahme "
                    "beruht nur auf theoretischen Schlüssen ohne tatsächliche Anhaltspunkte; die Erfindung ist nicht ausführbar offenbart "
                    "(§ 21 Abs. 1 Nr. 2 PatG; BGH Fructoseintoleranz)."],
                   merke="Rein theoretische Wirkung: nicht ausführbar offenbart.", titel="Ergebnis", level=3, norms=["§ 21 Abs. 1 Nr. 2 PatG"],
                   concepts=["pat_ausfuehrbarkeit"]),
            ],
            abschnitt="Abs. 3 und 4: Medizinische Indikation", level=2, concepts=["pat_zweite_indikation"], norms=["§ 3 Abs. 3 PatG", "§ 3 Abs. 4 PatG"],
            cases=["pat_bgh_fructoseintoleranz"], step=_PF + ".3.3"),
    ]),
    # ================================================================== § 4 PatG
    dict(id="p03n4", order=400, titel="§ 4 PatG: Erfinderische Tätigkeit", einheiten=[
        intro("p03n4-0", "Nicht naheliegend für den Fachmann",
              "Eine Erfindung beruht auf erfinderischer Tätigkeit, wenn sie sich **für den Fachmann nicht in naheliegender Weise aus dem Stand "
              "der Technik ergibt** (§ 4 S. 1 PatG); ältere Rechte nach § 3 Abs. 2 PatG bleiben außer Betracht (§ 4 S. 2 PatG).\n\n"
              "Der BGH prüft in Schritten: (1) **Fachmann** und sein Fachwissen bestimmen; (2) **Ausgangspunkt** im Stand der Technik wählen, "
              "was einer Rechtfertigung bedarf; (3) **objektives technisches Problem** neutral formulieren; (4) **Veranlassung**: Hatte der "
              "Fachmann Anlass, den Ausgangspunkt in Richtung der Erfindung weiterzuentwickeln? Maßstab ist die Gesamtheit der Merkmale, nicht "
              "einzelne Teilaufgaben; jede Rückschau aus Kenntnis der Erfindung ist zu vermeiden. Hilfskriterien wie Bedürfnis oder Erfolg "
              "können das Ergebnis stützen.",
              concepts=["pat_erfinderische_taetigkeit", "pat_fachmann", "pat_aufgabe_loesung"], norms=["§ 4 PatG"],
              cases=["pat_bgh_fischbissanzeiger"], abschnitt="Überblick"),
        *fallkette("p03n4-1", "Der Fischbissanzeiger",
            "F hält ein Patent auf einen elektronischen Fischbissanzeiger: Die Angelschnur dreht ein Rad, ein Sensor erfasst die Drehung und "
            "löst ein Signal aus. Nichtigkeitsklägerin K stützt sich auf mehrere ältere Bissanzeiger und meint, ein erfahrener Angler wäre ohne "
            "Weiteres auf die Lösung gekommen.",
            [frage("Wer ist der für § 4 PatG maßgebliche Fachmann?", 2,
                   ["**Der Konstrukteur von Angelgeräten!** Fachmann ist, wer auf dem Gebiet **Geräte dieser Art entwickelt**, nicht der Anwender. "
                    "Ein Angler kennt die Bedürfnisse, aber nicht das konstruktive Wissen (BGH Fischbissanzeiger)."],
                   optionen=["Ein erfahrener Sportangler", "Ein Elektroingenieur ohne Bezug zu Angelgeräten",
                             "Ein Konstrukteur mit Erfahrung in der Entwicklung von Angelgeräten", "Ein Richter mit technischem Verständnis"],
                   merke="Fachmann ist der Entwickler, nicht der Nutzer.", titel="Maßgeblicher Fachmann", concepts=["pat_fachmann"],
                   step=_PF + ".4.1"),
             frage("Muss das Gericht von dem einen „nächstkommenden“ Stand der Technik ausgehen?", False,
                   ["**Nein!** Ein einziger nächstkommender Stand der Technik ist nicht zwingend. Die Wahl eines oder mehrerer **Ausgangspunkte "
                    "bedarf einer Rechtfertigung**, meist aus dem Bemühen des Fachmanns, für einen bestimmten Zweck eine bessere oder andere Lösung "
                    "zu finden (BGH Fischbissanzeiger)."],
                   merke="Ausgangspunkt wählen und begründen.", titel="Ausgangspunkt", level=2, step=_PF + ".4.2"),
             frage("Bedarf es für das Naheliegen einer Veranlassung, obwohl sich jedes Merkmal irgendwo im Stand der Technik findet?", True,
                   ["**Ja!** Das bloße Vorhandensein der Einzelmerkmale genügt nicht. Es bedarf einer **Veranlassung**, den Stand der Technik "
                    "gerade in Richtung der Erfindung weiterzuentwickeln und die Merkmale so zu kombinieren (BGH Fischbissanzeiger)."],
                   merke="Bekannte Einzelmerkmale machen die Kombination nicht naheliegend.", titel="Veranlassung", step=_PF + ".4.3"),
            ],
            abschnitt="Fachmann und Ausgangspunkt", level=1, concepts=["pat_erfinderische_taetigkeit"], norms=["§ 4 PatG"],
            cases=["pat_bgh_fischbissanzeiger"], step=_PF + ".4"),
        *fallkette("p03n4-2", "Das Mittel gegen die überaktive Blase",
            "Mirabegron war als Wirkstoff gegen Übergewicht und hohen Blutzucker bekannt. A hält ein Patent und ein Schutzzertifikat auf ein "
            "Mittel mit Mirabegron zur Behandlung der überaktiven Blase. Das BPatG formuliert die Aufgabe als „neue Indikationen für "
            "Mirabegron finden“ und hält das für naheliegend.",
            [frage("Darf das technische Problem so formuliert werden?", False,
                   ["**Nein!** Das Problem ist **allgemein und neutral** zu formulieren; Elemente der patentgemäßen Lösung, hier der Wirkstoff, "
                    "dürfen nicht einfließen. Ob die Befassung mit einer Aufgabe nahelag, ist erst bei der erfinderischen Tätigkeit zu prüfen "
                    "(BGH Mirabegron)."],
                   merke="Keine Lösungselemente in der Aufgabe.", titel="Neutrale Aufgabe", step=_PF + ".4.2"),
             frage("Wie lautet das Problem richtig?", 0,
                   ["**Ein wirksames Mittel zur Behandlung der überaktiven Blase bereitzustellen!** Das Problem wird aus dem entwickelt, was das "
                    "Patent tatsächlich leistet, ohne die Lösung vorwegzunehmen (BGH Mirabegron; BGH Gelenkanordnung)."],
                   optionen=["Ein wirksames Heilmittel zur Behandlung der überaktiven Blase bereitstellen",
                             "Eine neue Indikation für Mirabegron finden",
                             "Mirabegron für die Behandlung der überaktiven Blase einsetzen",
                             "Einen ß3-Agonisten mit neuer Wirkung finden"],
                   merke="Aufgabe = was das Patent leistet, ohne Lösung.", titel="Richtige Aufgabe", level=2, cases=["pat_bgh_gelenkanordnung"]),
             frage("Ist die zusätzliche Indikation schon deshalb naheliegend, weil es um einen bekannten Wirkstoff geht?", False,
                   ["**Nein!** Dass ein Patent eine **weitere Indikation für einen bekannten Stoff** betrifft, macht die Aufgabe nicht naheliegend. "
                    "Maßgeblich ist, ob der Stand der Technik konkret Anlass gab, den Wirkstoff für diese Krankheit zu erproben (BGH Mirabegron)."],
                   merke="Bekannter Stoff heißt nicht naheliegende Indikation.", titel="Bekannter Wirkstoff", level=2, step=_PF + ".4.3"),
            ],
            abschnitt="Technisches Problem", level=2, concepts=["pat_aufgabe_loesung", "pat_erfinderische_taetigkeit"], norms=["§ 4 PatG"],
            cases=["pat_bgh_mirabegron"], step=_PF + ".4.2"),
        *fallkette("p03n4-3", "Die Fingerprothese",
            "O hält ein Patent auf ein motorisch bewegtes Fingerelement für Handprothesen, bei dem die Gewindeschnecke axial beweglich auf der "
            "Antriebswelle gelagert ist. Klägerin K kombiniert eine über zehn Jahre ältere Fingerprothese mit einer US-Patentschrift von 1936 über "
            "Schneckengetriebe, die eine bewegliche Lagerung beschreibt.",
            [frage("Darf der Fachmann bei der Suche nach Verbesserungen auch sehr alte Schriften heranziehen?", True,
                   ["**Ja!** Bei der Suche nach Verbesserungen oder Alternativen sind grundsätzlich **auch ältere Lösungen** in Betracht zu "
                    "ziehen. Das Alter einer Schrift schließt sie nicht aus dem Stand der Technik aus (BGH Fingerelement)."],
                   merke="Alter schadet nicht, Stand der Technik ist Stand der Technik.", titel="Ältere Lösungen"),
             frage("Lag die Übertragung nahe, weil das Lagerprinzip seit über 70 Jahren bekannt war?", False,
                   ["**Nein!** Ist ein Funktionsprinzip seit vielen Jahrzehnten bekannt, bedarf es in der Regel einer **zusätzlichen Anregung**, um "
                    "es erstmals bei Vorrichtungen einzusetzen, deren Zweck und Aufbau ebenfalls lange bekannt sind. Dass es niemand früher tat, "
                    "spricht gegen das Naheliegen (BGH Fingerelement)."],
                   merke="Jahrzehntelang ungenutztes Prinzip: zusätzliche Anregung nötig.", titel="Jahrzehnte altes Prinzip", level=2),
             frage("Genügt als Veranlassung, dass bewegliche Lagerungen zum allgemeinen Fachwissen gehören und generell geeignet sind?", False,
                   ["**Nein!** Die generelle Eignung eines Mittels aus dem Fachwissen reicht nur, wenn für den Fachmann ohne Weiteres erkennbar "
                    "ist, dass sein Einsatz in der konkreten Lage **objektiv zweckmäßig** ist (BGH Kinderbett). In der kompakten Fingerprothese war "
                    "das nicht erkennbar (BGH Fingerelement)."],
                   merke="Fachwissen allein ist keine Veranlassung.", titel="Allgemeines Fachwissen", level=3, cases=["pat_bgh_kinderbett"]),
            ],
            abschnitt="Veranlassung", level=2, concepts=["pat_erfinderische_taetigkeit"], norms=["§ 4 PatG"],
            cases=["pat_bgh_fingerelement"], step=_PF + ".4.3"),
        *fallkette("p03n4-4", "Die Gleitlagerüberwachung",
            "G hält ein Patent auf ein Verfahren, das Lagerschäden in Verbrennungsmotoren an einem Thermostrom erkennt, der beim Abreißen des "
            "Schmierfilms fließt, und das Signal in bestimmten Schritten auswertet. Eine Vorveröffentlichung misst stattdessen "
            "Öldruckschwankungen, schlägt aber ähnliche Auswerteschritte vor. Die Patentbeschreibung kritisiert diese Schrift.",
            [frage("Zieht der Fachmann die Vorveröffentlichung heran, obwohl sie eine andere Messmethode verwendet?", True,
                   ["**Ja!** Will der Fachmann eine Methode durch weitere Schritte verfeinern, prüft er auch eine einschlägige Schrift, die "
                    "**im Ausgangspunkt eine andere Methode** wählt. Er rechnet damit, dass dort vorgeschlagene Schritte verallgemeinerungsfähig "
                    "sind (BGH Gleitlagerüberwachung)."],
                   merke="Andere Methode, übertragbare Schritte.", titel="Andere Messmethode", level=2),
             frage("Kann die Kritik der Patentbeschreibung an der Schrift belegen, dass der Fachmann Anlass hatte, einen anderen Weg zu gehen?", True,
                   ["**Ja,** aber nur eingeschränkt. Kritik an einem bekannten Lösungsweg kann auf einen Anlass zur Weiterentwicklung außerhalb "
                    "dieser Bahnen hindeuten, **sofern sie nicht rückschauend** aus Kenntnis der Erfindung gewonnen ist (BGH "
                    "Gleitlagerüberwachung)."],
                   merke="Kritik in der Beschreibung: Indiz, wenn nicht rückschauend.", titel="Kritik und Rückschau", level=3),
             frage("Darf das Gericht die Merkmale nach Teilaufgaben gruppieren und jede Gruppe für sich auf Naheliegen prüfen?", False,
                   ["**Nein!** Maßgeblich ist der Gegenstand der Erfindung **in der Gesamtheit seiner Lösungsmerkmale** und ihrem technischen "
                    "Zusammenhang. Eine Aufspaltung in Teilaufgaben, die einzeln nahegelegt sind, verfehlt die Kombination (BGH "
                    "Papiermaschinengewebe)."],
                   merke="Gesamtheit der Merkmale, keine Teilaufgaben.", titel="Keine Teilaufgaben", level=2,
                   cases=["pat_bgh_papiermaschinengewebe"], concepts=["pat_aufgabe_loesung"]),
            ],
            abschnitt="Rückschau und Gesamtbetrachtung", level=2, concepts=["pat_erfinderische_taetigkeit"], norms=["§ 4 PatG"],
            cases=["pat_bgh_gleitlagerueberwachung"], step=_PF + ".4.3"),
    ]),
    # ================================================================== §§ 21, 22 PatG
    dict(id="p03n21", order=2100, titel="§§ 21, 22 PatG: Widerrufs- und Nichtigkeitsgründe", einheiten=[
        intro("p03n21-0", "Vier Gründe und ein fünfter",
              "§ 21 Abs. 1 PatG zählt die **Widerrufsgründe** abschließend auf: fehlende Patentfähigkeit nach §§ 1 bis 5 PatG (Nr. 1), mangelnde "
              "**Ausführbarkeit** (Nr. 2), **widerrechtliche Entnahme** (Nr. 3) und **unzulässige Erweiterung** über die ursprünglich "
              "eingereichte Fassung, bei Teilanmeldungen über die Stammanmeldung (Nr. 4). Betrifft ein Grund nur einen Teil, wird das Patent "
              "beschränkt aufrechterhalten (§ 21 Abs. 2 PatG); der Widerruf wirkt zurück (§ 21 Abs. 3 PatG).\n\n"
              "§ 22 Abs. 1 PatG übernimmt diese Gründe als **Nichtigkeitsgründe** und fügt die **Erweiterung des Schutzbereichs** nach Erteilung "
              "hinzu; § 22 Abs. 2 PatG verweist auf § 21 Abs. 2 und 3 PatG. Mangelnde Klarheit ist kein Grund (BGH Fugenband).",
              concepts=["pat_widerrufsgruende", "pat_nichtigkeitsgruende", "pat_unzulaessige_erweiterung"],
              norms=["§ 21 Abs. 1 PatG", "§ 21 Abs. 2 PatG", "§ 22 Abs. 1 PatG"], cases=["pat_bgh_fugenband"], abschnitt="Überblick"),
        *fallkette("p03n21-1", "Die Spirale aus Laserpulsen",
            "L hält ein Patent auf eine Vorrichtung, die Material mit gepulster Laserstrahlung schneidet; die Wechselwirkungszonen werden entlang "
            "einer Spirale von außen nach innen gesetzt. Das Patent beruht auf einer Teilanmeldung. Die Stammanmeldung beschreibt die Spirale nur "
            "zusammen mit einer bestimmten Steuerung der Laserquelle, die als untrennbar dargestellt ist.",
            [frage("Ist für die unzulässige Erweiterung auf die Stammanmeldung abzustellen?", True,
                   ["**Ja!** Beruht das Patent auf einer **Teilanmeldung**, darf sein Gegenstand auch nicht über den Inhalt der früheren Anmeldung "
                    "in ihrer ursprünglich eingereichten Fassung hinausgehen (§ 21 Abs. 1 Nr. 4 Hs. 2 PatG)."],
                   merke="Teilanmeldung: Maßstab ist auch die Stammanmeldung.", titel="Maßstab bei Teilanmeldung", concepts=["pat_teilung"]),
             frage("Ist der Anspruch zulässig, obwohl er die Spirale ohne die Steuerung beansprucht?", False,
                   ["**Nein!** Eine Verallgemeinerung ist unzulässig, wenn die ursprünglichen Unterlagen erkennen lassen, dass Merkmale in "
                    "**untrennbarem Zusammenhang** stehen, der Anspruch sie aber nicht in ihrer Gesamtheit vorsieht. In dieser allgemeinen Form war "
                    "die Vorrichtung nicht als erfindungsgemäß offenbart (BGH Gepulste Laserstrahlung)."],
                   merke="Untrennbare Merkmale nur gemeinsam.", titel="Untrennbarer Zusammenhang", level=2),
             frage("Wäre der Anspruch zulässig, wenn die Stammanmeldung Spirale und Steuerung als je für sich vorteilhaft beschriebe?", True,
                   ["**Ja!** Von mehreren Merkmalen eines Ausführungsbeispiels, die **zusammen, aber auch je für sich** dem Erfolg der Erfindung "
                    "förderlich sind, darf auch nur eines in den Anspruch aufgenommen werden (BGH Schleifprodukt; BGH Gepulste Laserstrahlung)."],
                   merke="Je für sich förderliche Merkmale dürfen einzeln aufgenommen werden.", titel="Je für sich förderlich", level=2,
                   abwandlung="Die Stammanmeldung beschreibt Spirale und Steuerung als zwei Maßnahmen, die je für sich die Schnittqualität verbessern.",
                   cases=["pat_bgh_schleifprodukt"]),
            ],
            abschnitt="Abs. 1 Nr. 4: Unzulässige Erweiterung", level=2, concepts=["pat_unzulaessige_erweiterung"],
            norms=["§ 21 Abs. 1 Nr. 4 PatG"], cases=["pat_bgh_gepulste_laserstrahlung"], step="step:pat_schema_einspruch.2.4"),
        *fallkette("p03n21-2", "Der Procalcitonin-Schwellenwert",
            "B hält ein Patent auf ein Verfahren zur Diagnose bakterieller Lungenentzündung bei Herzinsuffizienz anhand des Markers Procalcitonin "
            "mit Schwellenwerten zwischen 0,01 und 1 ng/ml. Die Anmeldung nannte nur einen deutlich engeren Bereich als bevorzugt und sagte "
            "nichts dazu, welche anderen Werte vorteilhaft wären.",
            [frage("Deckt die Anmeldung den beanspruchten weiten Bereich?", False,
                   ["**Nein!** Benennt die Anmeldung nur einen bestimmten Bereich als bevorzugt und enthält sie **keinen Hinweis, welche weiteren "
                    "Wertebereiche** ebenfalls vorteilhaft sind, bildet sie keine Grundlage für einen deutlich weiteren Bereich (BGH "
                    "Procalcitonin-Schwellenwert). Das Patent ist nach § 22 Abs. 1 PatG in Verbindung mit § 21 Abs. 1 Nr. 4 PatG nichtig."],
                   merke="Bevorzugter Bereich trägt keinen viel weiteren Bereich.", titel="Wertebereiche", norms=["§ 22 Abs. 1 PatG"]),
             frage("Genügt es, dass der Fachmann aufgrund seines Fachwissens erkannt hätte, dass auch der weitere Bereich funktioniert?", False,
                   ["**Nein!** Maßgeblich ist, was die Unterlagen **unmittelbar und eindeutig als zur Erfindung gehörend** offenbaren. Was sich "
                    "erst aus eigenen, vom Fachwissen getragenen Überlegungen des Fachmanns ergibt, ist nicht offenbart (BGH Hubgliedertor I)."],
                   merke="Fachwissen ergänzt die Ursprungsoffenbarung nicht.", titel="Keine Ergänzung durch Fachwissen", level=2,
                   cases=["pat_bgh_hubgliedertor_i"]),
            ],
            abschnitt="Abs. 1 Nr. 4: Unzulässige Erweiterung", level=2, concepts=["pat_unzulaessige_erweiterung"],
            norms=["§ 21 Abs. 1 Nr. 4 PatG"], cases=["pat_bgh_procalcitonin_schwellenwert"], step="step:pat_schema_einspruch.2.4"),
        *fallkette("p03n21-3", "Die Passung in der Winkelmesseinrichtung",
            "W hält ein Patent auf eine Winkelmesseinrichtung, deren Gehäuse eine Passung für die Kabelhülse aufweist. Anspruch 1 enthält ein "
            "Merkmal zur Gestaltung der Passung, das in der Anmeldung nicht als zur Erfindung gehörend offenbart war; es engt die dort "
            "offenbarte Lehre aber nur ein. E legt Einspruch ein.",
            [frage("Kann das Patent trotz des nicht offenbarten Merkmals aufrechterhalten werden?", True,
                   ["**Ja!** Ein solches Merkmal kann **im Anspruch verbleiben**, wenn seine Einfügung nur zu einer **Einschränkung** führt, also "
                    "eine ursprünglich offenbarte Anweisung konkretisiert. Bei der Patentfähigkeit bleibt es zugunsten des Inhabers außer Betracht "
                    "(BGH Winkelmesseinrichtung)."],
                   merke="Einschränkendes, nicht offenbartes Merkmal: bleibt, zählt aber nicht.", titel="Einschränkendes Merkmal", level=2),
             frage("Kann W den Mangel beheben, indem er das Merkmal einfach streicht?", False,
                   ["**Nein!** Die Streichung würde den **Schutzbereich des erteilten Patents erweitern**; auch das ist ein Nichtigkeitsgrund "
                    "(§ 22 Abs. 1 PatG). Gerade deshalb lässt der BGH das einschränkende Merkmal stehen (BGH Winkelmesseinrichtung)."],
                   merke="Streichen erweitert den Schutzbereich.", titel="Streichung des Merkmals", level=3, norms=["§ 22 Abs. 1 PatG"]),
             frage("Muss die Patentschrift einen Hinweis (Disclaimer) enthalten, dass aus dem Merkmal keine Rechte hergeleitet werden?", False,
                   ["**Nein!** Um sicherzustellen, dass aus der Einfügung keine Rechte hergeleitet werden, bedarf es "
                    "**grundsätzlich keines Disclaimers** in der Patentschrift (BGH Winkelmesseinrichtung)."],
                   merke="Kein Disclaimer nötig.", titel="Disclaimer", level=3),
            ],
            abschnitt="Abs. 1 Nr. 4, Abs. 2: Einschränkende Erweiterung", level=2, concepts=["pat_unzulaessige_erweiterung"],
            norms=["§ 21 Abs. 1 Nr. 4 PatG", "§ 21 Abs. 2 PatG"], cases=["pat_bgh_winkelmesseinrichtung"], step="step:pat_schema_einspruch.2.4"),
        *fallkette("p03n21-4", "Das Klammernahtgerät",
            "E hält ein Patent auf ein chirurgisches Klammernahtgerät, dessen Führungstaschen keilförmige Seiten haben, damit sich schief "
            "liegende Klammern selbst ausrichten. Das BPatG erklärt das Patent für nichtig: Die Patentschrift erkläre nicht, durch welchen "
            "Mechanismus die Klammer sich ausrichte.",
            [frage("Wann ist eine Erfindung ausführbar offenbart (§ 21 Abs. 1 Nr. 2 PatG)?", 3,
                   ["**Wenn der Fachmann sie ohne erfinderisches Zutun und ohne unzumutbare Schwierigkeiten verwirklichen kann!** Maßstab ist die "
                    "Gesamtoffenbarung der Patentschrift zusammen mit dem Fachwissen; der angestrebte Erfolg muss erreichbar sein (BGH "
                    "Klammernahtgerät)."],
                   optionen=["Wenn jede Ausführungsform im Einzelnen beschrieben ist", "Wenn die Patentschrift den Wirkmechanismus erklärt",
                             "Wenn alle in der Beschreibung genannten Vorteile erreicht werden",
                             "Wenn der Fachmann sie ohne erfinderisches Zutun und ohne unzumutbare Schwierigkeiten verwirklichen kann"],
                   merke="Nacharbeitbar ohne Erfindung und unzumutbaren Aufwand.", titel="Maßstab der Ausführbarkeit"),
             frage("Hat das BPatG die Ausführbarkeit zu Recht verneint?", False,
                   ["**Nein!** Es genügt, dass der Fachmann Taschen mit der **beanspruchten Geometrie herstellen** kann und damit der Erfolg "
                    "eintritt. Eine Erklärung des Wirkmechanismus oder eine im Einzelnen beschriebene Ausführungsform wie bei der Neuheit ist nicht "
                    "nötig; Lücken darf der Fachmann notfalls mit orientierenden Versuchen schließen (BGH Klammernahtgerät)."],
                   merke="Wer nicht weiß, warum es funktioniert, kann es trotzdem ausführen.", titel="Kein Wirkmechanismus nötig", level=2),
             frage("Fehlt die Ausführbarkeit, wenn nicht alle Vorteile erreicht werden, die die Beschreibung der Erfindung zuschreibt?", False,
                   ["**Nein!** Die Ausführbarkeit der im Anspruch umschriebenen Lehre darf nicht mit der **Erreichbarkeit aller beschriebenen "
                    "Vorteile** gleichgesetzt werden (BGH Stabilisierung der Wasserqualität)."],
                   merke="Ausführbarkeit ist nicht Vorteilhaftigkeit.", titel="Vorteile der Beschreibung", level=2,
                   abwandlung="K wendet ein, die Klammern richteten sich nicht in jedem Fall so zuverlässig aus, wie die Beschreibung verspricht.",
                   cases=["pat_bgh_stabilisierung_der_wasserqualitaet"]),
            ],
            abschnitt="Abs. 1 Nr. 2: Ausführbarkeit", level=1, concepts=["pat_ausfuehrbarkeit"],
            norms=["§ 21 Abs. 1 Nr. 2 PatG"], cases=["pat_bgh_klammernahtgeraet"], step="step:pat_schema_einspruch.2.2"),
        *fallkette("p03n21-5", "Das unklare Fugenband",
            "F hält ein Patent auf ein Fugenband für Betonbauteile. Nichtigkeitsklägerin K meint, Anspruch 1 sei unklar "
            "formuliert und nicht neu. F verteidigt Anspruch 1 beschränkt durch Merkmale aus erteilten Unteransprüchen.",
            [frage("Worauf kann K die Nichtigkeitsklage nicht stützen?", 3,
                   ["**Auf mangelnde Klarheit!** Die Nichtigkeitsgründe sind in § 22 Abs. 1 PatG und § 21 Abs. 1 PatG **abschließend** aufgezählt; mangelnde "
                    "Klarheit gehört nicht dazu. Unklare Begriffe sind auszulegen (BGH Fugenband)."],
                   merke="Klarheit ist kein Nichtigkeitsgrund.", titel="Klarheit kein Grund",
                   optionen=["Fehlende Patentfähigkeit", "Mangelnde Ausführbarkeit", "Erweiterung des Schutzbereichs nach Erteilung",
                             "Mangelnde Klarheit des Anspruchs"]),
             frage("Prüft das Gericht die Klarheit des beschränkt verteidigten Anspruchs?", False,
                   ["**Nein,** jedenfalls nicht, wenn die aufgenommenen Merkmale **schon in erteilten Ansprüchen** standen. Dann ist eine etwaige "
                    "Unklarheit bereits im erteilten Patent angelegt (BGH Fugenband)."],
                   merke="Merkmale aus erteilten Ansprüchen: keine Klarheitsprüfung.", titel="Beschränkte Verteidigung", level=2,
                   concepts=["pat_beschraenkte_verteidigung"]),
             frage("Muss das Gericht den nebengeordneten Anspruch 8 gesondert auf seinen Rechtsbestand prüfen?", True,
                   ["**Ja!** Jeder angegriffene Anspruch ist **gesondert** zu prüfen; nebengeordnete Ansprüche teilen nicht automatisch das "
                    "Schicksal von Anspruch 1. Bei Teilnichtigkeit wird das Patent beschränkt (§ 22 Abs. 2 PatG in Verbindung mit § 21 Abs. 2 "
                    "PatG; BGH Sensoranordnung)."],
                   merke="Jeder Anspruch hat sein eigenes Schicksal.", titel="Nebengeordnete Ansprüche", level=2,
                   abwandlung="Das Patent enthält neben Anspruch 1 einen nebengeordneten Anspruch 8, den K ebenfalls angreift.",
                   norms=["§ 22 Abs. 2 PatG"], cases=["pat_bgh_sensoranordnung"]),
            ],
            abschnitt="§ 22 PatG: Nichtigkeitsgründe", level=1, concepts=["pat_nichtigkeitsgruende"],
            norms=["§ 22 Abs. 1 PatG"], cases=["pat_bgh_fugenband"], step="step:pat_schema_nichtigkeitsklage.2"),
    ]),
    # ================================================================== §§ 34, 38 PatG
    dict(id="p03n34", order=3400, titel="§§ 34, 38 PatG: Anmeldung und Änderungen", einheiten=[
        intro("p03n34-0", "Was die Anmeldung leisten muss",
              "§ 34 Abs. 3 PatG nennt den Inhalt der Anmeldung: Name, Erteilungsantrag, **Patentansprüche**, **Beschreibung** und Zeichnungen. "
              "Die Erfindung muss so deutlich und vollständig offenbart sein, dass ein Fachmann sie **ausführen** kann (§ 34 Abs. 4 PatG); fehlt "
              "es daran, ist das erteilte Patent nach § 21 Abs. 1 Nr. 2 PatG angreifbar. Die Anmeldung darf nur **eine Erfindung** oder eine "
              "Gruppe mit einer einzigen allgemeinen erfinderischen Idee enthalten (§ 34 Abs. 5 PatG); sonst wird ausgeschieden.\n\n"
              "**§ 38 PatG** erlaubt Änderungen bis zum Erteilungsbeschluss, soweit sie den Gegenstand **nicht erweitern** (S. 1); aus "
              "erweiternden Änderungen können keine Rechte hergeleitet werden (S. 2). Vor dem Prüfungsantrag sind nur bestimmte Änderungen "
              "zulässig.",
              concepts=["pat_anmeldung", "pat_ausfuehrbarkeit", "pat_einheitlichkeit", "pat_unzulaessige_erweiterung"],
              norms=["§ 34 Abs. 3 PatG", "§ 34 Abs. 4 PatG", "§ 34 Abs. 5 PatG", "§ 38 PatG"], abschnitt="Überblick"),
        *fallkette("p03n34-1", "Der unklare Anspruch",
            "B meldet ein Batterieüberwachungsgerät an. Die Prüfungsstelle weist die Anmeldung zurück, weil ein Begriff im Patentanspruch "
            "unklar sei und der Anspruch deshalb nicht angebe, was unter Schutz gestellt werden soll (§ 34 Abs. 3 Nr. 3 PatG). B legt "
            "Beschwerde ein.",
            [frage("Ist ein „unklarer Patentanspruch“ ein Zurückweisungsgrund?", False,
                   ["**Nein!** Einen Zurückweisungsgrund des unklaren Anspruchs kennt das PatG nicht; er folgt auch nicht aus § 34 Abs. 3 Nr. 3 PatG. "
                    "Unklare Merkmale sind **auszulegen**, nicht zu beanstanden (BPatG Batterieüberwachungsgerät)."],
                   merke="Unklarheit wird ausgelegt, nicht zurückgewiesen.", titel="Unklarheit als Zurückweisungsgrund", level=2),
             frage("Gelten für die Auslegung im Prüfungsverfahren andere Grundsätze als im Verletzungsverfahren?", False,
                   ["**Nein!** Die Anspruchsmerkmale sind **aus der Sicht des Fachmanns** auszulegen, im Prüfungsverfahren nach denselben "
                    "Grundsätzen wie im Einspruchs-, Nichtigkeits- und Verletzungsverfahren (BPatG Batterieüberwachungsgerät)."],
                   merke="Eine Auslegung für alle Verfahren.", titel="Einheitliche Auslegung", concepts=["pat_auslegung"]),
             frage("Kann trotz fehlender Beschreibung ein Patent erteilt werden?", True,
                   ["**Ja,** ausnahmsweise. Geht der sachliche Zusammenhang aus **Ansprüchen und Zeichnungen eindeutig** hervor, "
                    "kann trotz fehlender Beschreibung erteilt werden; die Formvorschriften dienen der Verständlichkeit, nicht dem Selbstzweck "
                    "(BPatG Aufreißdeckel)."],
                   merke="Formvorschriften sind kein Selbstzweck.", titel="Fehlende Beschreibung", level=3,
                   abwandlung="Eine andere Anmeldung enthält keine gesonderte Beschreibung, sondern nur Ansprüche und aussagekräftige Zeichnungen.",
                   norms=["§ 34 Abs. 3 Nr. 4 PatG"], cases=["pat_bpatg_aufreissdeckel"]),
            ],
            abschnitt="Abs. 3: Inhalt der Anmeldung", level=1, concepts=["pat_anmeldung", "pat_patentanspruch"],
            norms=["§ 34 Abs. 3 Nr. 3 PatG"], cases=["pat_bpatg_batterieueberwachungsgeraet"], step="step:pat_schema_anmeldung_erteilung.2.1"),
        *fallkette("p03n34-2", "Der Borreliose-Test",
            "R hält ein Patent auf ein Polypeptid aus Borrelia burgdorferi und ein In-vitro-Verfahren, das damit Antikörper gegen den "
            "Borreliose-Erreger nachweist. Der Anspruch umfasst den Test mit dem ganzen Polypeptid und mit nicht näher bestimmten Segmenten. "
            "Klägerin K meint, welche Segmente funktionieren, müsse der Fachmann erst erfinden.",
            [frage("Ist das Verfahren ausführbar offenbart, wenn der Test mit dem Polypeptid voller Länge praktisch brauchbare Ergebnisse "
                   "liefert?", True,
                   ["**Ja!** Das Verfahren ist **insgesamt** ausführbar offenbart, wenn es mit dem Polypeptid voller Sequenzlänge mit einem "
                    "praktisch brauchbaren Ergebnis ausgeführt werden kann (BGH Borrelioseassay)."],
                   merke="Eine brauchbare Ausführungsform trägt die Ausführbarkeit.", titel="Praktisch brauchbare Ausführung"),
             frage("Schadet es, dass besser geeignete Segmente nur mit erfinderischem Bemühen aufgefunden werden können?", False,
                   ["**Nein!** Dass **bessere Ausführungsformen** nicht ohne erfinderisches Bemühen auffindbar sind, nimmt die Ausführbarkeit "
                    "nicht, wenn eine offenbarte Ausführungsform praktisch brauchbar ist (BGH Borrelioseassay)."],
                   merke="Optimierung darf erfinderisch sein.", titel="Bessere Segmente", level=2),
            ],
            abschnitt="Abs. 4: Ausführbare Offenbarung", level=2, concepts=["pat_ausfuehrbarkeit"],
            norms=["§ 34 Abs. 4 PatG"], cases=["pat_bgh_borrelioseassay"], step="step:pat_schema_pruefungsverfahren_dpma.3.2"),
        *fallkette("p03n34-3", "Die Blutzuckersenker",
            "P hält ein Patent auf die „Verwendung von Effektoren der Dipeptidyl-Peptidase IV zur Senkung des Blutzuckerspiegels“. Die "
            "Beschreibung nennt nur wenige konkrete Hemmstoffe. Einsprechende E meint, der Anspruch erfasse auch Stoffe, die erst künftig "
            "gefunden würden, und sei deshalb nicht ausführbar.",
            [frage("Darf P den Schutz über die ausdrücklich beschriebenen Hemmstoffe hinaus verallgemeinern?", True,
                   ["**Ja!** Dem Anmelder ist es grundsätzlich unbenommen, **Verallgemeinerungen** vorzunehmen, um die Erfindung in vollem Umfang zu "
                    "erfassen (BGH Dipeptidyl-Peptidase-Inhibitoren)."],
                   merke="Verallgemeinern ist erlaubt.", titel="Verallgemeinerung"),
             frage("Wonach richtet sich, ob der verallgemeinerte Anspruch ausführbar offenbart ist?", 2,
                   ["**Nach der allgemeinsten Form der technischen Lehre!** Der Schutz darf nicht über das hinausgehen, was dem Fachmann anhand der "
                    "Beschreibung und der Beispiele als **allgemeinste Form der Lehre** erscheint, die das Problem löst (BGH "
                    "Dipeptidyl-Peptidase-Inhibitoren)."],
                   optionen=["Nach der Zahl der Ausführungsbeispiele", "Danach, ob jeder erfasste Stoff schon bekannt ist",
                             "Ob der Anspruch nicht über die allgemeinste Form der offenbarten Lehre hinausgeht",
                             "Ob der Anmelder für jeden Stoff Versuchsdaten vorlegt"],
                   merke="Maßstab: allgemeinste Form der Lehre.", titel="Maßstab bei Verallgemeinerung", level=2),
             frage("Steht der funktionellen Fassung entgegen, dass sie auch erst künftig bereitgestellte Stoffe erfasst?", False,
                   ["**Nein!** Die Umschreibung einer Stoffgruppe **nach ihrer Funktion** im Verwendungsanspruch ist zulässig, auch wenn sie künftige "
                    "Stoffe erfasst und deren Bereitstellung erfinderische Tätigkeit erfordern kann (BGH Dipeptidyl-Peptidase-Inhibitoren)."],
                   merke="Funktionelle Stoffgruppe: auch künftige Stoffe.", titel="Künftige Stoffe", level=3),
            ],
            abschnitt="Abs. 4: Ausführbare Offenbarung", level=2, concepts=["pat_ausfuehrbarkeit", "pat_patentanspruch"],
            norms=["§ 34 Abs. 4 PatG"], cases=["pat_bgh_dipeptidyl_peptidase_inhibitoren"], step="step:pat_schema_pruefungsverfahren_dpma.3.2"),
        *fallkette("p03n34-4", "Antrieb und Schwungrad",
            "A meldet einen Antrieb für Fördermittel im Bergbau an, dessen Räder direkt durch Nabenmotoren angetrieben werden. Ein weiterer "
            "unabhängiger Anspruch betrifft ein Versorgungsmodul mit Schwungradspeicher. Die Prüfungsstelle beanstandet die Uneinheitlichkeit, "
            "ohne zum Schwungrad zu recherchieren.",
            [frage("Ist die Anmeldung einheitlich im Sinne von § 34 Abs. 5 PatG?", False,
                   ["**Nein!** Eine Gruppe von Erfindungen muss eine **einzige allgemeine erfinderische Idee** verwirklichen. Daran fehlt es "
                    "jedenfalls, wenn für das mit jeder Erfindung objektiv Erreichte **kein technischer Zusammenhang** ersichtlich ist (BPatG "
                    "Fördermittelantrieb)."],
                   merke="Kein technischer Zusammenhang, keine Einheitlichkeit.", titel="Einheitliche Idee"),
             frage("Musste die Prüfungsstelle vor der Beanstandung zu allen Erfindungen recherchieren?", False,
                   ["**Nein!** Erkennt eine sachkundige Prüfungsstelle schon **aus den Unterlagen**, dass mehrere Erfindungen ohne gemeinsame Idee "
                    "vorliegen, bedarf es keiner Recherche zu allen (BPatG Fördermittelantrieb)."],
                   merke="Offensichtliche Uneinheitlichkeit braucht keine Recherche.", titel="Recherche", level=3),
             frage("Kann A das Versorgungsmodul weiterverfolgen, wenn er der Beanstandung folgt?", True,
                   ["**Ja!** Der uneinheitliche Teil wird **ausgeschieden** und kann als eigene Anmeldung mit dem ursprünglichen Zeitrang "
                    "weiterverfolgt werden; alternativ kann A teilen (§ 39 PatG). Weigert er sich, droht die Zurückweisung (§ 48 PatG)."],
                   merke="Uneinheitlich: ausscheiden, nicht aufgeben.", titel="Ausscheidung", norms=["§ 39 PatG", "§ 48 PatG"],
                   concepts=["pat_teilung"], step="step:pat_schema_anmeldung_erteilung.4.2"),
            ],
            abschnitt="Abs. 5: Einheitlichkeit", level=2, concepts=["pat_einheitlichkeit"],
            norms=["§ 34 Abs. 5 PatG"], cases=["pat_bpatg_foerdermittelantrieb"], step="step:pat_schema_pruefungsverfahren_dpma.3.5"),
        *fallkette("p03n34-5", "Die Handcreme ohne Lecithin",
            "H meldet die kosmetische Verwendung von Kochsalz und Glycerin in Hautcremes an. Um eine ältere Anmeldung zu umgehen, fügt sie im "
            "Prüfungsverfahren das Merkmal ein, die Zubereitungen seien „frei von Phosphatidylcholin“. Die Anmeldung nannte Lecithin nur als "
            "einen von Dutzenden möglichen Emulgatoren; ihre Beispiele enthalten keines.",
            [frage("Darf H den Anspruch im Prüfungsverfahren noch ändern?", True,
                   ["**Ja!** Bis zum Erteilungsbeschluss sind Änderungen zulässig, die den **Gegenstand der Anmeldung nicht erweitern** "
                    "(§ 38 S. 1 PatG). Nach Stellung des Prüfungsantrags gilt die Beschränkung auf Mängelbeseitigung nicht mehr."],
                   merke="Ändern ja, erweitern nein.", titel="Änderung im Prüfungsverfahren", step="step:pat_schema_anmeldung_erteilung.4.1"),
             frage("Kann ein nicht ursprünglich offenbartes, nur einschränkendes Merkmal im Erteilungsverfahren wie im Einspruchsverfahren im "
                   "Anspruch bleiben?", False,
                   ["**Nein!** Im Prüfungsverfahren muss eine unzulässige Erweiterung beseitigt werden. Behebt H sie nach Aufforderung nicht, wird "
                    "die Anmeldung **zurückgewiesen** (§ 48 PatG); die Grundsätze zum erteilten Patent (BGH Winkelmesseinrichtung) gelten hier "
                    "nicht (BGH Phosphatidylcholin)."],
                   merke="Vor Erteilung wird die Erweiterung beseitigt, nicht geduldet.", titel="Erteilungsverfahren", level=2,
                   norms=["§ 48 PatG"]),
             frage("Ist das Merkmal „frei von Phosphatidylcholin“ ohne Weiteres eine unzulässige Erweiterung?", False,
                   ["**Nein!** Die Aufnahme eines Merkmals, wonach die Zubereitung einen bestimmten Stoff **nicht enthalten** darf, ist nicht ohne "
                    "Weiteres eine Erweiterung. Die Anmeldung gibt keinen Anhalt, dass der Stoff notwendig oder vorteilhaft ist; "
                    "das Merkmal nimmt nur Zusammensetzungen aus, um sich vom Stand der Technik abzugrenzen, ohne neue technische Information "
                    "(BGH Phosphatidylcholin, Abgrenzung zu BGH Reifenabdichtmittel)."],
                   merke="Ausschluss eines Stoffes erweitert nicht automatisch.", titel="Ausschlussmerkmal", level=3,
                   cases=["pat_bgh_reifenabdichtmittel"]),
            ],
            abschnitt="§ 38 PatG: Änderungen", level=2, concepts=["pat_unzulaessige_erweiterung"],
            norms=["§ 38 PatG"], cases=["pat_bgh_phosphatidylcholin"], step="step:pat_schema_pruefungsverfahren_dpma.3.4"),
    ]),
    # ================================================================== § 59 PatG
    dict(id="p03n59", order=5900, titel="§ 59 PatG: Einspruch", einheiten=[
        intro("p03n59-0", "Neun Monate für jedermann",
              "Gegen ein erteiltes Patent kann **jeder** innerhalb von **neun Monaten nach Veröffentlichung der Erteilung** Einspruch erheben, "
              "bei widerrechtlicher Entnahme nur der Verletzte (§ 59 Abs. 1 S. 1 PatG). Der Einspruch ist schriftlich zu erklären und zu "
              "begründen; er kann nur auf die Widerrufsgründe des § 21 PatG gestützt werden, und die rechtfertigenden **Tatsachen sind im "
              "Einzelnen** bis zum Fristablauf anzugeben (§ 59 Abs. 1 S. 2 bis 5 PatG). Hinzu kommt die Einspruchsgebühr (§ 6 PatKostG).\n\n"
              "Wer wegen Verletzung verklagt ist oder negative Feststellungsklage erhoben hat, kann binnen drei Monaten **beitreten** "
              "(§ 59 Abs. 2 PatG). Angehört wird auf Antrag oder bei Sachdienlichkeit (§ 59 Abs. 3 PatG).",
              concepts=["pat_einspruch", "pat_beitritt"], norms=["§ 59 Abs. 1 PatG", "§ 59 Abs. 2 PatG"], abschnitt="Überblick"),
        schema("p03n59-0s", "Prüfungsschema Einspruch", "pat_schema_einspruch", abschnitt="Überblick"),
        *fallkette("p03n59-1", "Der Einspruch mit der älteren Anmeldung",
            "Gegen das Patent des H auf ein Leistungshalbleiterbauelement legt E fristgerecht Einspruch ein. Sie stützt ihn allein auf eine "
            "ältere, nachveröffentlichte Anmeldung und trägt vor, der Gegenstand beruhe nicht auf erfinderischer Tätigkeit. Das Patent hat "
            "mehrere Nebenansprüche; E greift nur Anspruch 1 an.",
            [frage("Welche Anforderungen stellt § 59 Abs. 1 S. 4 PatG an die Begründung?", 1,
                   ["**Tatsachen im Einzelnen, aus denen abschließende Folgerungen möglich sind!** Patentinhaber und Patentamt müssen aus der "
                    "Begründung ohne eigene Ermittlungen schließen können, ob der behauptete **Widerrufsgrund** vorliegt (BGH "
                    "Leistungshalbleiterbauelement)."],
                   optionen=["Die bloße Nennung eines Widerrufsgrunds", "Nachprüfbare Tatsachen zum Widerrufsgrund, aus denen abschließende "
                             "Folgerungen gezogen werden können", "Ein Sachverständigengutachten",
                             "Der Nachweis, dass der Einspruch begründet ist"],
                   merke="Substantiiert heißt: nachprüfbare Tatsachen zum Widerrufsgrund.", titel="Substantiierung",
                   step="step:pat_schema_einspruch.1.3"),
             frage("Ist der Einspruch zulässig, obwohl eine ältere Anmeldung bei der erfinderischen Tätigkeit gar nicht berücksichtigt wird?", True,
                   ["**Ja!** Ob die Tatsachen den Widerruf **tatsächlich rechtfertigen**, ist eine Frage der Begründetheit, nicht der Zulässigkeit. "
                    "Ein auf eine ältere Anmeldung gestützter Einspruch ist zulässig, gleich ob E mangelnde Neuheit oder fehlende erfinderische "
                    "Tätigkeit rügt (BGH Leistungshalbleiterbauelement)."],
                   merke="Zulässig ist nicht gleich schlüssig.", titel="Zulässigkeit und Begründetheit", level=2, norms=["§ 4 PatG"]),
             frage("Muss E Widerrufsgründe gegen sämtliche Nebenansprüche vortragen?", False,
                   ["**Nein!** Der Einsprechende kann bei mehreren Nebenansprüchen die Patentfähigkeit **nur eines Nebenanspruchs** angreifen; "
                    "der Einspruch ist trotzdem zulässig (BGH Automatisches Fahrzeuggetriebe)."],
                   merke="Ein angegriffener Nebenanspruch genügt.", titel="Nebenansprüche", level=2,
                   cases=["pat_bgh_automatisches_fahrzeuggetriebe"]),
            ],
            abschnitt="Abs. 1: Begründung", level=1, concepts=["pat_einspruch"], norms=["§ 59 Abs. 1 PatG"],
            cases=["pat_bgh_leistungshalbleiterbauelement"], step="step:pat_schema_einspruch.1.3"),
        *fallkette("p03n59-2", "Der Einsprechende aus Taichung",
            "Gegen das deutsche Patent der P auf eine Vorrichtung zur Kornfeinung von Metallschmelzen legt ein Unternehmen Einspruch ein. Inzwischen "
            "ist für P ein europäisches Patent mit derselben Priorität bestandskräftig erteilt, weshalb das deutsche Patent nach dem "
            "Doppelschutzverbot keine Wirkung mehr hat.",
            [frage("Braucht der Einsprechende ein besonderes Rechtsschutzbedürfnis, weil das deutsche Patent wirkungslos ist?", False,
                   ["**Nein!** Einspruch kann „jeder“ erheben (§ 59 Abs. 1 S. 1 PatG). Ein besonderes Rechtsschutzbedürfnis ist auch dann nicht "
                    "nötig, wenn das Patent wegen des **Doppelschutzverbots** keine Wirkung mehr hat (BGH Kornfeinung)."],
                   merke="Einspruch: Popularrechtsbehelf ohne Rechtsschutzbedürfnis.", titel="Rechtsschutzbedürfnis", level=2,
                   norms=["Art. II § 8 IntPatÜG"], concepts=["pat_doppelschutz"], step="step:pat_schema_einspruch.1.4"),
             frage("Ist ein Einspruch zulässig, der als Einsprechenden nur „Wang Wei, Taichung, Taiwan“ nennt?", False,
                   ["**Nein!** Die Identität des Einsprechenden muss **innerhalb der Einspruchsfrist zweifelsfrei** feststellbar sein. Ein häufiger "
                    "Name und eine Millionenstadt ohne Anschrift genügen nicht; der Einspruch ist unzulässig (BPatG Gabelschlüssel)."],
                   merke="Wer einspricht, muss in der Frist erkennbar sein.", titel="Identität des Einsprechenden",
                   abwandlung="Gegen ein anderes Patent geht ein Einspruch ein, der als Einsprechenden nur „Wang Wei, Taichung, Taiwan“ nennt; eine Anschrift folgt erst nach Fristablauf.",
                   cases=["pat_bpatg_gabelschluessel"], step="step:pat_schema_einspruch.1.4"),
             frage("Genügt es, wenn zwei Unternehmen gemeinsam Einspruch einlegen und nur eine Gebühr zahlen?", False,
                   ["**Nein!** Legen mehrere gemeinsam Einspruch ein, ist die Einspruchsgebühr **für jeden Einsprechenden gesondert** zu entrichten; "
                    "für den, dessen Gebühr fehlt, gilt der Einspruch als nicht erhoben (BPatG Einspruchsgebühren bei gemeinsamem Einspruch)."],
                   merke="Je Einsprechendem eine Gebühr.", titel="Gebühr bei gemeinsamem Einspruch", level=2, norms=["§ 6 Abs. 1 PatKostG"],
                   cases=["pat_bpatg_einspruchsgebuehren_gemeinsam"], step="step:pat_schema_einspruch.1.2"),
            ],
            abschnitt="Abs. 1: Einsprechender, Frist und Gebühr", level=1, concepts=["pat_einspruch"], norms=["§ 59 Abs. 1 PatG"],
            cases=["pat_bgh_kornfeinung"], step="step:pat_schema_einspruch.1"),
        *fallkette("p03n59-3", "Die Fondue-Einrichtung",
            "A und B entwickeln gemeinsam eine Fondue-Einrichtung; sie haben sich dafür zu einer GbR zusammengetan. A meldet die Erfindung allein "
            "an und erhält das Patent. B legt Einspruch wegen widerrechtlicher Entnahme ein.",
            [frage("Kann B den Einspruch auf widerrechtliche Entnahme stützen?", False,
                   ["**Nein!** Wegen widerrechtlicher Entnahme kann nur **der Verletzte** einsprechen (§ 59 Abs. 1 S. 1 PatG). Sind Einsprechender "
                    "und Patentinhaber **Mitberechtigte** an der Erfindung, etwa aus einer GbR, fehlt die Einspruchsberechtigung; wer Erfinder ist, "
                    "bleibt offen (BPatG Fondue-Einrichtung)."],
                   merke="Mitberechtigte sind keine Verletzten im Sinne der Entnahme.", titel="Einspruchsberechtigung", level=2,
                   step="step:pat_schema_einspruch.1.4"),
             frage("Muss das Patent wegen widerrechtlicher Entnahme auch dann widerrufen werden, wenn es ohnehin nicht patentfähig ist?", True,
                   ["**Ja!** Die widerrechtliche Entnahme (§ 21 Abs. 1 Nr. 3 PatG) ist ein **selbständiger Widerrufsgrund**. Das Patent ist auch "
                    "dann aus diesem Grund zu widerrufen, wenn sein Gegenstand nicht patentfähig ist (BGH Schweißheizung)."],
                   merke="Entnahme trägt den Widerruf auch bei fehlender Patentfähigkeit.", titel="Entnahme und Patentfähigkeit", level=3,
                   abwandlung="C, der die Erfindung allein gemacht hat, wirft A vor, sie ihm entnommen zu haben, und legt deshalb Einspruch ein.",
                   norms=["§ 21 Abs. 1 Nr. 3 PatG"], cases=["pat_bgh_schweissheizung"], step="step:pat_schema_einspruch.2.3"),
            ],
            abschnitt="Abs. 1: Widerrechtliche Entnahme", level=2, concepts=["pat_einspruch", "pat_recht_auf_patent"],
            norms=["§ 59 Abs. 1 PatG", "§ 21 Abs. 1 Nr. 3 PatG"], cases=["pat_bpatg_fondue_einrichtung"], step="step:pat_schema_einspruch.1.4"),
        *fallkette("p03n59-4", "Der Ratschenschlüssel",
            "Patentinhaber R erwirkt gegen Händlerin H eine einstweilige Verfügung wegen Verletzung seines Patents auf einen Ratschenschlüssel. "
            "Die Einspruchsfrist ist abgelaufen; das Einspruchsverfahren ist noch anhängig. Zwei Monate nach dem Verfügungsantrag erklärt H den "
            "Beitritt als Einsprechende.",
            [frage("Kann H dem Einspruchsverfahren beitreten, obwohl R keine Verletzungsklage erhoben hat?", True,
                   ["**Ja!** Beitreten kann auch, gegen wen der Patentinhaber wegen Verletzung den **Erlass einer einstweiligen Verfügung beantragt** "
                    "hat. Die Lage gleicht der einer Verletzungsklage (§ 59 Abs. 2 PatG; BGH Ratschenschlüssel)."],
                   merke="Verfügungsantrag genügt für den Beitritt.", titel="Beitritt nach einstweiliger Verfügung", level=2),
             frage("Hat H die Beitrittsfrist gewahrt?", True,
                   ["**Ja!** Der Beitritt ist innerhalb von **drei Monaten** nach Erhebung der Verletzungsklage schriftlich zu erklären und bis dahin "
                    "zu begründen (§ 59 Abs. 2 S. 1, 3 PatG). An die Stelle der Klage tritt hier der Verfügungsantrag; zwei Monate danach ist die "
                    "Frist gewahrt."],
                   merke="Beitritt: drei Monate ab Klage, schriftlich und begründet.", titel="Beitrittsfrist"),
             frage("Kann H mit dem Beitritt Widerrufsgründe geltend machen, die kein ursprünglicher Einsprechender vorgebracht hat?", True,
                   ["**Ja!** Für den Beitritt gilt § 59 Abs. 1 S. 3 bis 5 PatG entsprechend (§ 59 Abs. 2 S. 4 PatG): Der Beitretende ist "
                    "**Einsprechender** und kann Widerrufsgründe des § 21 PatG mit eigener Begründung geltend machen; H rügte hier mangelnde "
                    "Patentfähigkeit und unzulässige Erweiterung."],
                   merke="Der Beitretende ist vollwertiger Einsprechender.", titel="Eigene Widerrufsgründe", level=3),
            ],
            abschnitt="Abs. 2: Beitritt", level=2, concepts=["pat_beitritt"], norms=["§ 59 Abs. 2 PatG"],
            cases=["pat_bgh_ratschenschluessel"], step="step:pat_schema_einspruch.1.4"),
    ]),
    # ================================================================== §§ 73, 79 PatG
    dict(id="p03n73", order=7300, titel="§§ 73, 79 PatG: Beschwerde", einheiten=[
        intro("p03n73-0", "Vom DPMA zum Technischen Beschwerdesenat",
              "Gegen **Beschlüsse** der Prüfungsstellen und Patentabteilungen findet die Beschwerde statt (§ 73 Abs. 1 PatG). Sie ist binnen "
              "**eines Monats nach Zustellung** schriftlich **beim DPMA** einzulegen (§ 73 Abs. 2 PatG); die Beschwerdegebühr ist in derselben "
              "Frist zu zahlen (§ 6 Abs. 1 PatKostG). Hält die Ausgangsstelle die Beschwerde für begründet, hilft sie ab, außer im mehrseitigen "
              "Verfahren (§ 73 Abs. 3, 4 PatG).\n\n"
              "Das BPatG entscheidet durch Beschluss (§ 79 Abs. 1 PatG). Unstatthafte oder form- und fristwidrige Beschwerden werden als "
              "unzulässig verworfen (§ 79 Abs. 2 PatG). Statt selbst zu entscheiden, kann es aufheben und **zurückverweisen**, etwa bei einem "
              "wesentlichen Verfahrensmangel (§ 79 Abs. 3 PatG).",
              concepts=["pat_beschwerde", "pat_abhilfe"], norms=["§ 73 Abs. 1 PatG", "§ 73 Abs. 2 PatG", "§ 79 Abs. 3 PatG"], abschnitt="Überblick"),
        *fallkette("p03n73-1", "Die Mitteilung ohne Signatur",
            "Das DPMA teilt der PCT-Anmelderin A mit, das Verfahren sei beendet, weil sie die Anmeldegebühr nicht rechtzeitig gezahlt habe. Das "
            "Schreiben ist in der elektronischen Akte erstellt, trägt den Vermerk „ohne Unterschrift gültig“ und keine elektronische Signatur. A "
            "legt Beschwerde ein.",
            [frage("Kommt es für die Statthaftigkeit auf den materiellen Gehalt des Schreibens an?", True,
                   ["**Ja!** Ob ein Beschluss im Sinne von § 73 Abs. 1 PatG vorliegt, richtet sich nach dem **materiellen Gehalt**: Es muss eine "
                    "abschließende Regelung sein, die Rechte eines Beteiligten berührt. Bezeichnung und Form sind nicht entscheidend (BPatG "
                    "Formularmäßige Mitteilung II)."],
                   merke="Beschluss ist, was abschließend regelt.", titel="Materieller Beschlussbegriff", step="step:pat_schema_einspruch.4.1"),
             frage("Ist die Beschwerde gegen diese Mitteilung statthaft?", False,
                   ["**Nein!** Eine in der elektronischen Akte erstellte Mitteilung hat die Qualität eines Beschlusses nur, wenn sie die "
                    "**elektronische Signatur des Entscheidungsträgers** trägt; bei Papier bedarf es der Unterschrift. Ohne sie liegt kein "
                    "anfechtbarer Beschluss vor; die Beschwerde ist unzulässig (BPatG Formularmäßige Mitteilung II)."],
                   merke="Ohne Unterschrift oder Signatur kein Beschluss.", titel="Signatur", level=2),
            ],
            abschnitt="§ 73 Abs. 1 PatG: Statthaftigkeit", level=2, concepts=["pat_beschwerde"], norms=["§ 73 Abs. 1 PatG"],
            cases=["pat_bpatg_formularmaessige_mitteilung_ii"], step="step:pat_schema_einspruch.4.1"),
        *fallkette("p03n73-2", "Die verfallene Anmeldung",
            "Die Prüfungsstelle weist die Patentanmeldung der D-GmbH zurück. Kurz danach gilt die Anmeldung als zurückgenommen, weil die "
            "6. Jahresgebühr auch mit Zuschlag nicht gezahlt wurde. Erst danach legt D Beschwerde gegen den Zurückweisungsbeschluss ein.",
            [frage("Wo und binnen welcher Frist ist die Beschwerde einzulegen?", 0,
                   ["**Binnen eines Monats nach Zustellung schriftlich beim DPMA!** Die Beschwerde wird beim Amt eingelegt, nicht beim BPatG "
                    "(§ 73 Abs. 2 S. 1 PatG); die Beschwerdegebühr ist in derselben Frist zu zahlen (§ 6 Abs. 1 PatKostG)."],
                   optionen=["Binnen eines Monats nach Zustellung schriftlich beim DPMA",
                             "Binnen eines Monats nach Zustellung beim BPatG",
                             "Binnen zwei Monaten nach Verkündung beim DPMA",
                             "Binnen drei Monaten nach Zustellung beim BPatG"],
                   merke="Ein Monat, beim DPMA.", titel="Frist und Adressat", norms=["§ 6 Abs. 1 PatKostG"], step="step:pat_schema_einspruch.4.1"),
             frage("Ist die Beschwerde zulässig?", False,
                   ["**Nein!** Die Erteilungsbeschwerde setzt voraus, dass die Anmeldung **noch anhängig** ist. Ist sie weggefallen, fehlt die "
                    "**Beschwer**; die Beschwerde ist nach § 79 Abs. 2 PatG als unzulässig zu verwerfen (BPatG Dünnwandige Domsegmente)."],
                   merke="Keine Anmeldung, keine Beschwer.", titel="Beschwer", level=2),
             frage("Hätte die Prüfungsstelle einer zulässigen und begründeten Beschwerde selbst abhelfen dürfen?", True,
                   ["**Ja!** Im **einseitigen** Verfahren hat die Ausgangsstelle abzuhelfen, wenn sie die Beschwerde für begründet hält, und kann die "
                    "Rückzahlung der Beschwerdegebühr anordnen (§ 73 Abs. 3 PatG). Steht dem Beschwerdeführer ein anderer Beteiligter gegenüber, etwa "
                    "im Einspruchsverfahren, ist die Abhilfe ausgeschlossen (§ 73 Abs. 4 PatG)."],
                   merke="Abhilfe nur im einseitigen Verfahren.", titel="Abhilfe", norms=["§ 73 Abs. 3 PatG", "§ 73 Abs. 4 PatG"],
                   abwandlung="D hatte die Jahresgebühr rechtzeitig gezahlt, und die Prüfungsstelle erkennt nach der Beschwerde ihren Fehler.",
                   concepts=["pat_abhilfe"], step="step:pat_schema_einspruch.4.2"),
            ],
            abschnitt="§ 73 Abs. 2 bis 4 PatG, § 79 Abs. 2 PatG: Frist, Beschwer, Abhilfe", level=1, concepts=["pat_beschwerde"],
            norms=["§ 73 Abs. 2 PatG", "§ 79 Abs. 2 PatG"], cases=["pat_bpatg_duennwandige_domsegmente"], step="step:pat_schema_einspruch.4.1"),
        *fallkette("p03n73-3", "Die Begründung in drei Sätzen",
            "Die Prüfungsstelle weist eine Anmeldung für ein elektronisches Steuergerät nach § 48 PatG zurück. Begründung: Anspruch 1 lasse nicht "
            "eindeutig erkennen, was unter Schutz gestellt werden solle; einige Begriffe seien unklar. Weitere Ausführungen fehlen. Die "
            "Anmelderin legt Beschwerde ein.",
            [frage("Genügt der Beschluss der Begründungspflicht?", False,
                   ["**Nein!** Die Begründung muss die **tragenden Erwägungen** vollständig und aus sich heraus verständlich darlegen (§ 47 Abs. 1 S. 1 "
                    "PatG). Die bloße Annahme, der Anspruch sei nach § 34 Abs. 3 Nr. 3 PatG unklar, reicht nicht; Unklarheit ist ohnehin kein "
                    "Zurückweisungsgrund (BPatG Elektronisches Steuergerät)."],
                   merke="Unklarheit ist keine Begründung.", titel="Begründungspflicht", norms=["§ 47 Abs. 1 PatG"]),
             frage("Darf das BPatG den Beschluss aufheben und die Sache an das DPMA zurückverweisen, statt selbst zu entscheiden?", True,
                   ["**Ja!** Leidet das Verfahren vor dem DPMA an einem **wesentlichen Mangel**, kann das BPatG nach Ermessen aufheben und "
                    "zurückverweisen (§ 79 Abs. 3 S. 1 Nr. 2 PatG). Ein Begründungsmangel ist ein solcher Mangel (BPatG Elektronisches "
                    "Steuergerät)."],
                   merke="Wesentlicher Verfahrensmangel: Zurückverweisung.", titel="Zurückverweisung", level=2, step="step:pat_schema_einspruch.4.3"),
             frage("Ist das DPMA bei der erneuten Prüfung frei, die Anmeldung wieder wegen Unklarheit zurückzuweisen?", False,
                   ["**Nein!** Das DPMA hat die **rechtliche Beurteilung**, die der Aufhebung zugrunde liegt, auch seiner neuen Entscheidung "
                    "zugrunde zu legen (§ 79 Abs. 3 S. 2 PatG)."],
                   merke="Bindung an die Rechtsauffassung des BPatG.", titel="Bindungswirkung"),
             frage("Kann die Anmelderin die Beschwerdegebühr zurückerhalten?", True,
                   ["**Ja!** Das BPatG kann die **Rückzahlung der Beschwerdegebühr** anordnen (§ 80 Abs. 3 PatG). Maßstab ist die Billigkeit; ein "
                    "wesentlicher Verfahrensfehler des Amts ist der typische Fall. Hier wurde sie angeordnet (BPatG Elektronisches Steuergerät)."],
                   merke="Verfahrensfehler des Amts: Gebühr zurück.", titel="Rückzahlung der Gebühr", level=2, norms=["§ 80 Abs. 3 PatG"]),
            ],
            abschnitt="§ 79 Abs. 3 PatG: Zurückverweisung", level=2, concepts=["pat_beschwerde", "pat_beschluss_pruefungsstelle"],
            norms=["§ 79 Abs. 3 PatG"], cases=["pat_bpatg_elektronisches_steuergeraet"], step="step:pat_schema_einspruch.4.3"),
        *fallkette("p03n73-4", "Die Ventileinrichtung",
            "E hat gegen das Patent der V auf eine Ventileinrichtung für luftgefederte Fahrzeuge Einspruch wegen fehlender Patentfähigkeit "
            "eingelegt. Die Patentabteilung hält das Patent aufrecht. Mit ihrer Beschwerde rügt E zusätzlich eine unzulässige Erweiterung.",
            [frage("Darf E im Beschwerdeverfahren den zusätzlichen Widerrufsgrund geltend machen?", True,
                   ["**Ja!** Ist eine aufrechterhaltende Entscheidung **zulässig angefochten**, darf der Einsprechende im Beschwerdeverfahren "
                    "**zusätzliche Widerrufsgründe** geltend machen, die nicht Gegenstand der angefochtenen Entscheidung waren (BGH "
                    "Ventileinrichtung)."],
                   merke="Einsprechender darf in der Beschwerde nachlegen.", titel="Neuer Grund durch Einsprechenden", level=2),
             frage("Hätte das BPatG die unzulässige Erweiterung auch ohne Rüge von Amts wegen aufgreifen dürfen?", False,
                   ["**Nein!** Das BPatG ist nicht befugt, im Einspruchsbeschwerdeverfahren **von Amts wegen neue Widerrufsgründe** aufzugreifen, die "
                    "nicht Gegenstand des Einspruchsverfahrens vor dem Amt waren (BGH Ventileinrichtung)."],
                   merke="Kein neuer Widerrufsgrund von Amts wegen.", titel="Kein Aufgreifen von Amts wegen", level=2,
                   abwandlung="E hat in der Beschwerde nur die fehlende Patentfähigkeit weiterverfolgt; das BPatG stößt selbst auf die Erweiterung."),
             frage("Geht das Verfahren weiter, wenn E später ihre Beschwerde zurücknimmt, nachdem das BPatG das Patent widerrufen und V Rechtsbeschwerde eingelegt hat?", True,
                   ["**Ja!** Das Einspruchsverfahren wird nach Rücknahme des Einspruchs **von Amts wegen fortgesetzt** (§ 61 Abs. 1 S. 3 PatG); "
                    "das gilt auch im anschließenden Rechtsmittelverfahren. Durch Rücknahme der Beschwerde kann E dem Rechtsbeschwerdeverfahren "
                    "nicht die Grundlage entziehen (BGH Gruppierungssystem)."],
                   merke="Rücknahme beendet das Einspruchsverfahren nicht.", titel="Rücknahme", level=3,
                   norms=["§ 61 Abs. 1 PatG"], cases=["pat_bgh_gruppierungssystem"]),
            ],
            abschnitt="Prüfungsumfang im Einspruchsbeschwerdeverfahren", level=2, concepts=["pat_beschwerde", "pat_einspruch"],
            norms=["§ 73 Abs. 1 PatG", "§ 79 Abs. 1 PatG"], cases=["pat_bgh_ventileinrichtung"], step="step:pat_schema_einspruch.4.3"),
    ]),
    # ================================================================== §§ 81 bis 84 PatG
    dict(id="p03n81", order=8100, titel="§§ 81 bis 84 PatG: Nichtigkeitsverfahren", einheiten=[
        intro("p03n81-0", "Klage zum Nichtigkeitssenat",
              "Die Nichtigkeit wird durch **Klage** beim BPatG geltend gemacht, gerichtet gegen den im Register eingetragenen Inhaber "
              "(§ 81 Abs. 1, 4 PatG). Klagen kann **jeder** (Popularklage), bei widerrechtlicher Entnahme nur der Verletzte (§ 81 Abs. 3 PatG). "
              "Solange Einspruch noch möglich oder anhängig ist, ist die Klage gesperrt (§ 81 Abs. 2 PatG).\n\n"
              "Der Beklagte muss binnen eines Monats widersprechen (§ 82 Abs. 1 PatG). Das Gericht erteilt früh einen **qualifizierten Hinweis** "
              "(§ 83 Abs. 1 PatG), setzt Fristen (§ 83 Abs. 2 PatG) und kann verspätetes Vorbringen zurückweisen (§ 83 Abs. 4 PatG). Es entscheidet "
              "durch Urteil; über die Kosten nach der ZPO, soweit nicht die Billigkeit anderes erfordert (§ 84 Abs. 2 PatG).",
              concepts=["pat_nichtigkeitsklage", "pat_qualifizierter_hinweis", "pat_kostenerstattung"],
              norms=["§ 81 Abs. 1 PatG", "§ 81 Abs. 2 PatG", "§ 83 Abs. 1 PatG", "§ 84 Abs. 2 PatG"], abschnitt="Überblick"),
        schema("p03n81-0s", "Prüfungsschema Nichtigkeitsklage", "pat_schema_nichtigkeitsklage", abschnitt="Überblick"),
        *fallkette("p03n81-1", "Die Klage im Schatten des Einspruchs",
            "Generikahersteller G will das europäische Patent der T auf den Wirkstoff Torasemid angreifen. Beim EPA ist gegen das Patent "
            "noch ein Einspruch anhängig. G erhebt trotzdem beim BPatG Nichtigkeitsklage wegen fehlender Patentfähigkeit.",
            [frage("Gegen wen ist die Nichtigkeitsklage zu richten?", 2,
                   ["**Gegen den im Register als Patentinhaber Eingetragenen!** § 81 Abs. 1 S. 2 PatG knüpft an die **Registereintragung** an, "
                    "nicht an die materielle Inhaberschaft; das schafft Klarheit für den Kläger."],
                   optionen=["Gegen das DPMA", "Gegen den Erfinder", "Gegen den im Register eingetragenen Patentinhaber",
                             "Gegen den ausschließlichen Lizenznehmer"],
                   merke="Beklagter ist der Registerinhaber.", titel="Richtiger Beklagter", step="step:pat_schema_nichtigkeitsklage.1.2"),
             frage("Ist die Klage zulässig, solange der Einspruch beim EPA anhängig ist?", False,
                   ["**Nein!** Nichtigkeitsklage kann nicht erhoben werden, solange ein **Einspruch noch erhoben werden kann oder anhängig** ist "
                    "(§ 81 Abs. 2 S. 1 PatG). Das gilt auch für europäische Patente während eines Einspruchs vor dem EPA (BPatG Torasemid)."],
                   merke="Erst Einspruch, dann Nichtigkeit.", titel="Klagesperre", step="step:pat_schema_nichtigkeitsklage.1.2"),
             frage("Greift die Sperre auch, obwohl G sich auf einen Grund stützt, den das Einspruchsverfahren nicht kennt?", True,
                   ["**Ja!** Die Sperre gilt **unabhängig vom Klagegrund**, auch für die Erweiterung des Schutzbereichs, die kein Einspruchsgrund ist "
                    "(BPatG Torasemid)."],
                   merke="Klagesperre unabhängig vom Nichtigkeitsgrund.", titel="Sperre und Klagegrund", level=3,
                   abwandlung="G stützt die Klage auf eine Erweiterung des Schutzbereichs nach Erteilung, die im Einspruch nicht geltend gemacht werden kann."),
            ],
            abschnitt="§ 81 PatG: Klage, Beklagter, Klagesperre", level=2, concepts=["pat_nichtigkeitsklage", "pat_nichtigkeit_ep"],
            norms=["§ 81 Abs. 1 PatG", "§ 81 Abs. 2 PatG"], cases=["pat_bpatg_torasemid"], step="step:pat_schema_nichtigkeitsklage.1.2"),
        *fallkette("p03n81-2", "Das abgelaufene Patent",
            "K klagt gegen das Patent des P auf ein Verfahren zum Umkodieren von Datenbits. Während des Rechtsstreits läuft die Schutzdauer ab. "
            "K will das Patent trotzdem für die Vergangenheit vernichten lassen. P äußert sich auf Nachfrage nicht, ob er gegen K noch "
            "Ansprüche aus der Schutzdauer geltend machen will.",
            [frage("Braucht K für die Klage gegen ein noch laufendes Patent ein besonderes Rechtsschutzbedürfnis?", False,
                   ["**Nein!** Die Nichtigkeitsklage ist eine **Popularklage**; solange das Patent in Kraft ist, kann jeder klagen, ohne ein eigenes "
                    "Interesse darzulegen (§ 81 PatG)."],
                   merke="Laufendes Patent: Popularklage.", titel="Popularklage"),
             frage("Braucht K nach Ablauf der Schutzdauer ein eigenes Rechtsschutzbedürfnis?", True,
                   ["**Ja!** Nach Ablauf der Schutzdauer ist die Klage nur zulässig, soweit der Kläger ein **Rechtsschutzbedürfnis** hat, etwa weil "
                    "ihm Ansprüche wegen Benutzung in der Vergangenheit drohen; bei nebengeordneten Ansprüchen ist das **je Anspruch** zu prüfen "
                    "(BGH Aufzeichnungsträger)."],
                   merke="Erloschenes Patent: Rechtsschutzbedürfnis je Anspruch.", titel="Rechtsschutzbedürfnis nach Ablauf", level=2,
                   cases=["pat_bgh_aufzeichnungstraeger"]),
             frage("Besteht das Rechtsschutzbedürfnis fort, obwohl P schweigt?", True,
                   ["**Ja!** Solange der Patentinhaber auf die Aufforderung, zu erklären, ob er für die Vergangenheit noch Rechte gegen den Kläger "
                    "geltend machen will, **schweigt**, kann das Rechtsschutzbedürfnis nicht verneint werden (BPatG Rechtsschutzbedürfnis bei "
                    "Schweigen des Patentinhabers)."],
                   merke="Wer schweigt, lässt das Rechtsschutzbedürfnis bestehen.", titel="Schweigen des Inhabers", level=2,
                   cases=["pat_bpatg_rechtsschutzbeduerfnis_schweigen"]),
            ],
            abschnitt="§ 81 PatG: Klagebefugnis und Rechtsschutzbedürfnis", level=1, concepts=["pat_nichtigkeitsklage"],
            norms=["§ 81 PatG"], cases=["pat_bgh_aufzeichnungstraeger"], step="step:pat_schema_nichtigkeitsklage.1.2"),
        *fallkette("p03n81-3", "Der qualifizierte Hinweis",
            "K greift das Patent der B auf ein Kabelwickelband für Motorräume mit zwei Druckschriften an. Im Hinweis nach § 83 Abs. 1 PatG "
            "deutet das BPatG an, dieses Vorbringen könnte nicht ausreichen. K legt eine dritte Druckschrift nach; das BPatG weist die Klage "
            "trotzdem ab. In der Berufung legt K weitere Dokumente vor.",
            [frage("Bis wann soll der Hinweis nach § 83 Abs. 1 PatG erteilt werden?", 1,
                   ["**Innerhalb von sechs Monaten nach Zustellung der Klage!** Er soll die Parteien so früh wie möglich auf die voraussichtlich "
                    "entscheidenden Gesichtspunkte hinweisen (§ 83 Abs. 1 S. 1, 2 PatG) und ist bei anhängigem Verletzungsstreit auch dem "
                    "Verletzungsgericht zu übermitteln (S. 3)."],
                   optionen=["Erst in der mündlichen Verhandlung", "Innerhalb von sechs Monaten nach Zustellung der Klage",
                             "Innerhalb eines Monats nach Widerspruch", "Nur auf Antrag einer Partei"],
                   merke="Hinweis binnen sechs Monaten ab Zustellung.", titel="Zeitpunkt des Hinweises", step="step:pat_schema_nichtigkeitsklage.3.2"),
             frage("Musste K auf den Hinweis hin schon in erster Instanz neue Angriffsmittel vortragen?", True,
                   ["**Ja!** Legt der Hinweis dar, dass das Klagevorbringen **unzureichend sein könnte**, liegt es am Kläger, schon in erster "
                    "Instanz nachzulegen (BGH Kabelwickelband)."],
                   merke="Kritischer Hinweis: jetzt nachlegen.", titel="Reaktion auf den Hinweis", level=2),
             frage("Sind die neuen Dokumente in der Berufung zuzulassen, weil das BPatG auch die dritte Druckschrift nicht genügen ließ?", False,
                   ["**Nein!** Dass das BPatG auch die nachgeschobenen Angriffsmittel für unzureichend hält, rechtfertigt keine Zulassung weiterer "
                    "Angriffsmittel in der Berufung (§ 117 PatG), auch nicht für Dokumente außerhalb gängiger Recherchedatenbanken (BGH "
                    "Kabelwickelband)."],
                   merke="Keine zweite Chance in der Berufung.", titel="Neue Mittel in der Berufung", level=3, norms=["§ 117 PatG"]),
             frage("Hätte K nachlegen müssen, wenn der Hinweis ihre Argumentation zu diesem Punkt für zutreffend gehalten hätte?", False,
                   ["**Nein!** Erachtet der Hinweis die Argumentation des Klägers in einem Punkt **für zutreffend**, hat er in der Regel keinen "
                    "Anlass, dazu in erster Instanz weitere Angriffsmittel vorzutragen; weicht das Urteil ab, darf er in der Berufung nachlegen "
                    "(BGH Walzstraße)."],
                   merke="Günstiger Hinweis: kein Nachlegen nötig.", titel="Günstiger Hinweis", level=2,
                   abwandlung="Der Hinweis hatte die Angriffe der K als voraussichtlich durchgreifend bezeichnet; das Urteil weist die Klage dann doch ab.",
                   cases=["pat_bgh_walzstrasse"]),
            ],
            abschnitt="§ 83 Abs. 1 und 2 PatG: Hinweis und Frist", level=2, concepts=["pat_qualifizierter_hinweis", "pat_nichtigkeitsberufung"],
            norms=["§ 83 Abs. 1 PatG"], cases=["pat_bgh_kabelwickelband"], step="step:pat_schema_nichtigkeitsklage.3.2"),
        *fallkette("p03n81-4", "Der späte Hilfsantrag",
            "Im Nichtigkeitsverfahren gegen ein Patent auf eine photokatalytische Schicht verteidigt die Beklagte erst in der mündlichen "
            "Verhandlung eine neue Fassung mit Merkmalen aus einem Unteranspruch, obwohl der Hinweis schon Anlass dazu gab. K bringt daraufhin "
            "eine neue Druckschrift vor. Das BPatG weist sie als verspätet zurück.",
            [frage("Welche Voraussetzung gehört nicht zur Zurückweisung nach § 83 Abs. 4 PatG?", 3,
                   ["**Das Verschulden des Gegners!** § 83 Abs. 4 PatG verlangt Vorbringen **nach Ablauf der Frist** aus § 83 Abs. 2 PatG, dass die "
                    "Berücksichtigung eine **Vertagung** erfordern würde (Nr. 1), die Verspätung **nicht genügend entschuldigt** ist (Nr. 2) und "
                    "die Partei über die Folgen **belehrt** wurde (Nr. 3)."],
                   optionen=["Vorbringen nach Ablauf der gesetzten Frist", "Vertagung des Termins wäre erforderlich",
                             "Keine genügende Entschuldigung und Belehrung über die Folgen", "Verschulden des Gegners an der Verspätung"],
                   merke="Frist, Vertagung, keine Entschuldigung, Belehrung.", titel="Voraussetzungen der Präklusion",
                   step="step:pat_schema_nichtigkeitsklage.3.2"),
             frage("Durfte das BPatG das neue Angriffsmittel der K zurückweisen?", False,
                   ["**Nein!** Wer selbst erst in der Verhandlung eine Fassung verteidigt, die er nach dem Hinweis **schon in der Frist** hätte "
                    "formulieren können, kann nicht verlangen, dass der darauf reagierende Angriff des Klägers als verspätet zurückgewiesen wird "
                    "(BGH Photokatalytische Titandioxidschicht)."],
                   merke="Späte Verteidigung öffnet die Tür für späten Angriff.", titel="Reaktion auf späte Verteidigung", level=3),
             frage("Kann der BGH in der Berufung ein Angriffsmittel zurückweisen, das das BPatG nicht nach § 83 Abs. 4 PatG zurückgewiesen hat?", False,
                   ["**Nein!** Was das Patentgericht **nicht zurückgewiesen** hat, kann auch im Berufungsverfahren nicht zurückgewiesen werden; ein "
                    "sachlich beschiedener Nichtigkeitsgrund fällt in der Berufung ohne Weiteres an (BGH Einspritzventil)."],
                   merke="Nicht zurückgewiesen bleibt zugelassen.", titel="Berufungsinstanz", level=2,
                   abwandlung="Das BPatG hat die neue Druckschrift berücksichtigt und das Patent für nichtig erklärt; die Beklagte rügt in der Berufung die Verspätung.",
                   cases=["pat_bgh_einspritzventil"], step="step:pat_schema_nichtigkeitsklage.5"),
            ],
            abschnitt="§ 83 Abs. 4 PatG: Zurückweisung verspäteten Vorbringens", level=2,
            concepts=["pat_qualifizierter_hinweis", "pat_beschraenkte_verteidigung"], norms=["§ 83 Abs. 4 PatG"],
            cases=["pat_bgh_photokatalytische_titandioxidschicht"], step="step:pat_schema_nichtigkeitsklage.3.2"),
        *fallkette("p03n81-5", "Zwei Kläger aus einem Konzern",
            "Gegen das Patent der P auf eine Benutzerauthentifizierung klagt zunächst die A-GmbH. Später erhebt deren Schwestergesellschaft B "
            "eine eigene Nichtigkeitsklage, statt dem ersten Verfahren beizutreten. Beide sind wegen derselben Geräte aus dem Patent verklagt.",
            [frage("Ist die Klage der B zulässig, obwohl sie dem ersten Verfahren hätte beitreten können?", True,
                   ["**Ja!** Eine Nichtigkeitsklage ist nicht allein deshalb rechtsmissbräuchlich, weil sich der Kläger einem **bereits "
                    "anhängigen Verfahren** gegen dasselbe Patent hätte anschließen können (BGH Benutzerauthentifizierung)."],
                   merke="Zweite Klage statt Beitritt ist kein Missbrauch.", titel="Rechtsmissbrauch", level=2),
             frage("Muss P die Mehrkosten tragen, die durch das zweite Verfahren entstehen, wenn das Patent fällt?", False,
                   ["**Nein,** grundsätzlich nicht. Nach § 84 Abs. 2 S. 2 PatG gelten die ZPO-Kostenregeln nur, **soweit nicht die Billigkeit** "
                    "anderes erfordert. Nutzt ein verbundener Kläger die Beitrittsmöglichkeit nicht, ohne dass gegen ihn andere Verletzungsvorwürfe "
                    "bestehen, ist es unbillig, dem Beklagten die Mehrkosten aufzuerlegen (BGH Benutzerauthentifizierung)."],
                   merke="Vermeidbare Mehrkosten trägt nicht der Patentinhaber.", titel="Billigkeit bei den Kosten", level=3,
                   step="step:pat_schema_nichtigkeitsklage.4"),
             frage("Kann A neben dem Patentanwalt auch die Kosten eines Rechtsanwalts erstattet verlangen?", True,
                   ["**Ja!** Die Zuziehung eines Rechtsanwalts neben dem Patentanwalt ist typischerweise **notwendig** (§ 91 Abs. 1 S. 1 ZPO in "
                    "Verbindung mit § 84 Abs. 2 S. 2 PatG), wenn zeitgleich ein **Verletzungsstreit** über das Patent anhängig ist, an dem die Partei "
                    "oder ein verbundenes Unternehmen beteiligt ist (BGH Doppelvertretung im Nichtigkeitsverfahren)."],
                   merke="Paralleler Verletzungsstreit: Doppelvertretung erstattungsfähig.", titel="Doppelvertretung", level=2,
                   cases=["pat_bgh_doppelvertretung_i"]),
             frage("Gilt das auch, wenn P nur angekündigt hatte, aus dem Patent vorzugehen?", False,
                   ["**Nein!** Die bloße **Ankündigung** einer Inanspruchnahme, eine Schutzschrift oder eine Strafanzeige rechtfertigen bei "
                    "typisierender Betrachtung keine Doppelvertretung (BGH Doppelvertretung im Patentnichtigkeitsverfahren II)."],
                   merke="Ankündigung reicht nicht für Doppelvertretung.", titel="Bloße Ankündigung", level=2,
                   abwandlung="Gegen A war keine Verletzungsklage erhoben; P hatte nur angekündigt, gerichtlich vorzugehen.",
                   cases=["pat_bgh_doppelvertretung_ii"]),
            ],
            abschnitt="§ 84 Abs. 2 PatG: Kosten", level=2, concepts=["pat_kostenerstattung", "pat_nichtigkeitsklage"],
            norms=["§ 84 Abs. 2 PatG"], cases=["pat_bgh_benutzerauthentifizierung"], step="step:pat_schema_nichtigkeitsklage.4"),
    ]),
    # ================================================================== §§ 99, 100 PatG
    dict(id="p03n99", order=9900, titel="§§ 99, 100 PatG: Verfahren vor dem BPatG und Rechtsbeschwerde", einheiten=[
        intro("p03n99-0", "ZPO als Reserve, BGH nur auf Zulassung",
              "§ 99 Abs. 1 PatG füllt Lücken des PatG mit **GVG und ZPO**, soweit die Besonderheiten des Verfahrens nicht entgegenstehen. "
              "Anfechtbar sind Entscheidungen des BPatG nur, soweit das PatG es zulässt (§ 99 Abs. 2 PatG). § 99 Abs. 3 PatG regelt die "
              "**Akteneinsicht** Dritter.\n\n"
              "Gegen Beschlüsse der Beschwerdesenate über Beschwerden nach § 73 PatG oder über Einsprüche nach § 61 Abs. 2 PatG findet die "
              "**Rechtsbeschwerde** zum BGH statt, wenn das BPatG sie **zugelassen** hat (§ 100 Abs. 1 PatG), etwa wegen grundsätzlicher "
              "Bedeutung (§ 100 Abs. 2 PatG). **Ohne Zulassung** ist sie statthaft, wenn ein schwerer Verfahrensmangel des § 100 Abs. 3 PatG "
              "gerügt wird, in der Praxis vor allem die **Versagung rechtlichen Gehörs** (Nr. 3).",
              concepts=["pat_rechtsbeschwerde", "pat_rechtliches_gehoer", "pat_akteneinsicht"],
              norms=["§ 99 Abs. 1 PatG", "§ 100 Abs. 1 PatG", "§ 100 Abs. 2 PatG", "§ 100 Abs. 3 PatG"], abschnitt="Überblick"),
        *fallkette("p03n99-1", "Der Einspruch beim Patentgericht",
            "Gegen das Patent der H auf ein Leistungshalbleiterbauelement ist Einspruch eingelegt. Auf Antrag entscheidet nicht die "
            "Patentabteilung, sondern der Beschwerdesenat des BPatG über den Einspruch und verwirft ihn als unzulässig. Die Rechtsbeschwerde "
            "lässt er zu.",
            [frage("Ist die Rechtsbeschwerde statthaft, obwohl der Senat nicht über eine Beschwerde, sondern erstinstanzlich entschieden hat?", True,
                   ["**Ja!** § 100 Abs. 1 PatG erfasst auch Beschlüsse, mit denen das BPatG nach **§ 61 Abs. 2 PatG** über den Einspruch entscheidet. "
                    "Statthaft ist sie auch, wenn das Patentgericht den Einspruch als unzulässig verwirft (BGH Leistungshalbleiterbauelement)."],
                   merke="Auch die BPatG-Einspruchsentscheidung ist rechtsbeschwerdefähig.", titel="Statthaftigkeit", level=2,
                   norms=["§ 61 Abs. 2 PatG"]),
             frage("Aus welchem Grund muss das BPatG die Rechtsbeschwerde zulassen?", 2,
                   ["**Grundsätzliche Bedeutung oder Rechtsfortbildung und Einheitlichkeit der Rechtsprechung!** Zuzulassen ist, wenn eine "
                    "Rechtsfrage von grundsätzlicher Bedeutung zu entscheiden ist oder die Fortbildung des Rechts oder die Sicherung einer "
                    "einheitlichen Rechtsprechung eine Entscheidung des BGH erfordert (§ 100 Abs. 2 PatG)."],
                   optionen=["Wenn der Beschwerdewert 20.000 Euro übersteigt", "Wenn ein Beteiligter es beantragt",
                             "Bei grundsätzlicher Bedeutung, zur Rechtsfortbildung oder Sicherung einheitlicher Rechtsprechung",
                             "Wenn der Senat Zweifel an seiner Entscheidung hat"],
                   merke="Zulassung: Grundsatz, Fortbildung, Einheitlichkeit.", titel="Zulassungsgründe", norms=["§ 100 Abs. 2 PatG"]),
             frage("Kann das BPatG die Zulassung auf einzelne Löschungsgründe eines Gebrauchsmusters beschränken?", True,
                   ["**Ja!** Die Zulassung kann **beschränkt** werden; bei Gebrauchsmustern auch auf einzelne Löschungsgründe (BGH "
                    "Feuchtigkeitsabsorptionsbehälter)."],
                   merke="Beschränkte Zulassung ist möglich.", titel="Beschränkte Zulassung", level=3,
                   abwandlung="In einem Gebrauchsmuster-Löschungsverfahren lässt der Senat die Rechtsbeschwerde nur zur Frage der Neuheit zu.",
                   cases=["pat_bgh_feuchtigkeitsabsorptionsbehaelter"]),
            ],
            abschnitt="§ 100 Abs. 1 und 2 PatG: Zulassung", level=2, concepts=["pat_rechtsbeschwerde"],
            norms=["§ 100 Abs. 1 PatG"], cases=["pat_bgh_leistungshalbleiterbauelement"]),
        *fallkette("p03n99-2", "Der überraschende Beschluss",
            "Im Beschwerdeverfahren über die Löschung des Gebrauchsmusters der W erteilt der Senat einen Hinweis: Schutzanspruch 1 sei "
            "voraussichtlich neu. In der Verhandlung ändert sich nichts; der Senat löscht dann ohne weiteren Hinweis wegen fehlender Neuheit. "
            "Die Rechtsbeschwerde ist nicht zugelassen.",
            [frage("Kann W trotzdem Rechtsbeschwerde einlegen?", True,
                   ["**Ja!** Einer Zulassung bedarf es nicht, wenn ein Mangel des § 100 Abs. 3 PatG **vorliegt und gerügt wird**, hier die "
                    "**Versagung rechtlichen Gehörs** (Nr. 3). W muss den Verstoß in der Rechtsbeschwerde konkret rügen."],
                   merke="Gehörsverstoß öffnet die zulassungsfreie Rechtsbeschwerde.", titel="Zulassungsfreie Rechtsbeschwerde",
                   concepts=["pat_rechtliches_gehoer"]),
             frage("Hat der Senat das rechtliche Gehör verletzt?", True,
                   ["**Ja!** Von einem Hinweis darf das Gericht nur abweichen, wenn für die Beteiligten **erkennbar** wird, dass sich die Grundlage "
                    "geändert hat oder es nun eine andere Beurteilung erwägt. Sonst darf W auf den Hinweis vertrauen (BGH Werkstück)."],
                   merke="Abweichen vom Hinweis nur mit erneutem Hinweis.", titel="Abweichen vom Hinweis", level=2),
             frage("Liegt ein Gehörsverstoß vor, wenn sich die Verhandlung nur auf einen Widerrufsgrund konzentrierte und der Senat auf einen "
                   "anderen abstellt?", False,
                   ["**Nein!** Auch wenn der Schwerpunkt der Verhandlung auf einem Grund lag, weil der Senat diesem zunächst zuneigte, darf der "
                    "Inhaber nicht annehmen, **allein dieser Grund** sei entscheidungserheblich (BGH Sorbitol)."],
                   merke="Schwerpunkt der Verhandlung ist kein Vertrauenstatbestand.", titel="Schwerpunkt der Verhandlung", level=2,
                   abwandlung="In einem Einspruchsverfahren gab es keinen Hinweis; die Verhandlung drehte sich um die Ausführbarkeit, der Senat widerruft wegen fehlender erfinderischer Tätigkeit.",
                   cases=["pat_bgh_sorbitol"]),
             frage("Muss der Senat darauf hinweisen, dass er eine Zeichnung nur als schematische Darstellung und nicht als maßstabsgerecht "
                   "ansieht?", False,
                   ["**Nein!** Schematische Zeichnungen in Patentschriften zeigen regelmäßig nur das Prinzip, keine exakten Maße. Darauf muss das "
                    "Gericht nicht eigens hinweisen (BGH Steckverbindung)."],
                   merke="Kein Hinweis auf Selbstverständliches.", titel="Schematische Zeichnung", level=2, cases=["pat_bgh_steckverbindung"]),
            ],
            abschnitt="§ 100 Abs. 3 Nr. 3 PatG: Rechtliches Gehör", level=2, concepts=["pat_rechtsbeschwerde", "pat_rechtliches_gehoer"],
            norms=["§ 100 Abs. 3 Nr. 3 PatG"], cases=["pat_bgh_werkstueck"]),
        *fallkette("p03n99-3", "Die zwei Ansprüche des Schwingungsdämpfers",
            "S hat ein Patent auf einen Schwingungsdämpfer mit zwei nebengeordneten, im Wesentlichen inhaltsgleichen Ansprüchen. Im "
            "Einspruchsverfahren verteidigt sie den einen beschränkt, den anderen unverändert. Das BPatG hält den unveränderten Anspruch für "
            "nicht patentfähig und widerruft das Patent insgesamt.",
            [frage("Durfte das BPatG annehmen, S verteidige den beschränkten Anspruch nur zusammen mit dem unveränderten?", False,
                   ["**Nein!** Ohne weitere Anhaltspunkte darf das Gericht nicht unterstellen, der Inhaber wolle den beschränkten Anspruch nur für "
                    "den Fall verteidigen, dass auch der unbeschränkte bestehen bleibt. Der Widerruf insgesamt **verletzt das rechtliche Gehör** "
                    "(§ 100 Abs. 3 Nr. 3 PatG; BGH Schwingungsdämpfer)."],
                   merke="Im Zweifel nachfragen, was verteidigt wird.", titel="Unterstelltes Antragsverständnis", level=2),
             frage("Muss das BPatG ein Sachverständigengutachten einholen, wenn S meint, die technischen Fragen überstiegen die Sachkunde des "
                   "Senats?", False,
                   ["**Nein,** nicht ohne Weiteres. Der Technische Beschwerdesenat hat grundsätzlich die nötige **eigene Sachkunde**. Eine "
                    "Gehörsrüge hat nur Erfolg, wenn aufgezeigt wird, warum sich dem Senat die Notwendigkeit externer Sachkunde **aufdrängen** "
                    "musste (BGH Kommunikationsrouter)."],
                   merke="Technische Richter sind die Sachverständigen.", titel="Sachverständigengutachten", level=3,
                   cases=["pat_bgh_kommunikationsrouter"]),
            ],
            abschnitt="§ 100 Abs. 3 Nr. 3 PatG: Rechtliches Gehör", level=2, concepts=["pat_rechtsbeschwerde", "pat_rechtliches_gehoer"],
            norms=["§ 100 Abs. 3 Nr. 3 PatG"], cases=["pat_bgh_schwingungsdaempfer"]),
        *fallkette("p03n99-4", "Die Akte des Nichtigkeitsverfahrens",
            "Patentanwalt A beantragt Einsicht in die Akten eines Nichtigkeitsverfahrens, ohne zu sagen, für wen. Die Patentinhaberin "
            "widerspricht: Ihr Privatgutachter wolle nicht, dass sein Name und seine Tätigkeit für sie bekannt werden.",
            [frage("Muss A ein eigenes berechtigtes Interesse darlegen?", False,
                   ["**Nein,** in der Regel nicht. Für Akteneinsicht gilt § 31 PatG entsprechend (§ 99 Abs. 3 S. 1 PatG); Nichtigkeitsakten sind "
                    "grundsätzlich jedermann zugänglich. Versagt wird sie nur, soweit der Patentinhaber ein **entgegenstehendes schutzwürdiges "
                    "Interesse** dartut (§ 99 Abs. 3 S. 3 PatG; BGH Akteneinsicht XXIII)."],
                   merke="Nichtigkeitsakten: Einsicht ohne Interessennachweis.", titel="Berechtigtes Interesse", norms=["§ 31 PatG"]),
             frage("Ist A die Einsicht trotz des Interesses des Privatgutachters zu gewähren?", True,
                   ["**Ja!** Ein Widerspruch zwingt den Antragsteller nur zur Darlegung, wenn ein **eigenes entgegenstehendes Interesse** "
                    "aufgezeigt wird. Das Interesse eines Privatgutachters, nicht namentlich bekannt zu werden, tritt in der Regel zurück (BGH "
                    "Akteneinsicht XXIII)."],
                   merke="Gutachteranonymität schlägt Akteneinsicht nicht.", titel="Privatgutachter", level=2),
             frage("Wirkt der Beitritt einer weiteren Gesellschaft als Klägerin im Nichtigkeitsverfahren, obwohl die erste Klägerin "
                   "die Klage zurückgenommen hat?", True,
                   ["**Ja!** Über § 99 Abs. 1 PatG gelten die ZPO-Regeln zum Parteiwechsel. Der Beitritt ist möglich, **solange der Rechtsstreit "
                    "anhängig** ist; eine wirksame Beitrittserklärung verliert ihre Wirkung nicht, weil die Rücknahme dem Beklagten früher "
                    "zugestellt wurde (BGH Später Widerhall)."],
                   merke="Parteibeitritt bis zum Ende der Anhängigkeit.", titel="Beitritt einer Klägerin", level=3,
                   abwandlung="Kurz bevor die Klägerin die Klage zurücknimmt, erklärt eine weitere Gesellschaft den Beitritt als Klägerin; zugestellt wird er dem Beklagten erst nach der Rücknahme.",
                   norms=["§ 99 Abs. 1 PatG"], cases=["pat_bgh_spaeter_widerhall"]),
            ],
            abschnitt="§ 99 PatG: ZPO und Akteneinsicht", level=2, concepts=["pat_akteneinsicht"],
            norms=["§ 99 Abs. 3 PatG"], cases=["pat_bgh_akteneinsicht_xxiii"]),
    ]),
    # ================================================================== § 123 PatG
    dict(id="p03n123", order=12300, titel="§ 123 PatG: Wiedereinsetzung", einheiten=[
        intro("p03n123-0", "Ohne Verschulden verhindert",
              "Wer **ohne Verschulden** verhindert war, gegenüber DPMA oder BPatG eine gesetzliche Frist einzuhalten, deren Versäumung einen "
              "Rechtsnachteil bewirkt, wird auf Antrag wieder eingesetzt (§ 123 Abs. 1 S. 1 PatG). **Ausgeschlossen** sind die Fristen für "
              "Einspruch und Einspruchsgebühr, für die Beschwerde des Einsprechenden gegen die Aufrechterhaltung und für Nachanmeldungen mit "
              "innerer Priorität (S. 2 Nr. 1 bis 3).\n\n"
              "Antrag binnen **zwei Monaten nach Wegfall des Hindernisses**, mit glaubhaft gemachten Tatsachen und Nachholung der Handlung; "
              "nach **einem Jahr** ist alles ausgeschlossen (Abs. 2). Es entscheidet die Stelle, die über die nachgeholte Handlung befindet "
              "(Abs. 3); die Wiedereinsetzung ist unanfechtbar (Abs. 4). Gutgläubige Zwischenbenutzer erhalten ein **Weiterbenutzungsrecht** "
              "(Abs. 5). Anwaltsverschulden wird zugerechnet (§ 85 Abs. 2 ZPO in Verbindung mit § 99 Abs. 1 PatG).",
              concepts=["pat_wiedereinsetzung", "pat_fristen"], norms=["§ 123 Abs. 1 PatG", "§ 123 Abs. 2 PatG", "§ 123 Abs. 5 PatG"],
              abschnitt="Überblick"),
        schema("p03n123-0s", "Prüfungsschema Fristversäumung", "pat_schema_fristversaeumung", abschnitt="Überblick"),
        *fallkette("p03n123-1", "Die gelöschte Frist",
            "Die Inhaberin eines europäischen Patents auf eine Bergbaumaschine lässt die Frist zur Einreichung der deutschen Übersetzung "
            "verstreichen. Eine Fachangestellte ihrer deutschen Anwälte hatte einen Brief der australischen Anwälte missverstanden und die "
            "eingetragene Frist gelöscht. Die Kanzlei hatte angewiesen, alle erkennbaren Probleme mit dem Anwalt zu klären.",
            [frage("Muss sich die Patentinhaberin ein Verschulden ihrer Anwälte zurechnen lassen?", True,
                   ["**Ja!** Das Verschulden des Bevollmächtigten steht dem eigenen gleich (§ 85 Abs. 2 ZPO in Verbindung mit § 99 Abs. 1 PatG). Das "
                    "Verschulden **nichtanwaltlicher Hilfskräfte** wird dagegen nicht zugerechnet; dann kommt es auf ein eigenes "
                    "**Organisationsverschulden** des Anwalts an."],
                   merke="Anwaltsverschulden ja, Personalverschulden nein, Organisationsmangel ja.", titel="Zurechnung",
                   norms=["§ 99 Abs. 1 PatG"], step="step:pat_schema_fristversaeumung.3.3"),
             frage("Trifft die Anwälte ein Organisationsverschulden?", True,
                   ["**Ja!** Ein Anwalt muss durch **allgemeine Anweisungen** sicherstellen, dass das Personal eingetragene Fristen **nicht "
                    "eigenmächtig ändert oder löscht**, besonders bei ungewöhnlicher Verfahrensgestaltung. Das gilt auch für Validierungsfristen "
                    "(BGH Bergbaumaschine)."],
                   merke="Fristen löscht nur der Anwalt.", titel="Organisationsverschulden", level=2),
             frage("Genügt die Anweisung, alle erkennbaren Probleme mit dem Anwalt zu klären?", False,
                   ["**Nein!** Eine solche allgemeine Anweisung erfüllt die Organisationspflicht nicht; es bedarf einer konkreten Regel, dass "
                    "eingetragene Fristen nur auf Anweisung des Anwalts gestrichen werden (BGH Bergbaumaschine). Die Wiedereinsetzung scheitert."],
                   merke="Allgemeine Klärungspflicht ersetzt keine Fristenregel.", titel="Allgemeine Anweisung", level=2),
            ],
            abschnitt="Abs. 1: Verschulden und Büroorganisation", level=2, concepts=["pat_wiedereinsetzung"],
            norms=["§ 123 Abs. 1 PatG"], cases=["pat_bgh_bergbaumaschine"], step="step:pat_schema_fristversaeumung.3.3"),
        *fallkette("p03n123-2", "Das Einschreiben, das nie ankam",
            "Die Prüfungsstelle weist die Anmeldung des A zurück. Laut Empfangsbestätigung der Post wird der Beschluss seinem Patentanwalt am "
            "15. April zugestellt. Beschwerde und Gebühr gehen am 9. Juni ein. Der Anwalt beantragt Wiedereinsetzung: Der Brief stehe nicht in "
            "seiner Posteingangsliste, die Unterschrift sei nicht die seine.",
            [frage("Ist die Beschwerdefrist versäumt?", True,
                   ["**Ja!** Die Beschwerdefrist beträgt **einen Monat ab Zustellung** (§ 73 Abs. 2 S. 1 PatG) und lief hier bis zum 15. Mai. "
                    "Maßgeblich ist der durch die Empfangsbestätigung belegte Zustellungstag (BPatG Vorrichtung zum Brechen von Steinen)."],
                   merke="Beschwerdefrist: ein Monat ab Zustellung.", titel="Fristversäumnis", norms=["§ 73 Abs. 2 PatG"],
                   step="step:pat_schema_fristversaeumung.1"),
             frage("Was muss der Antrag innerhalb der Zweimonatsfrist des § 123 Abs. 2 PatG enthalten?", 0,
                   ["**Die Tatsachen, die die Wiedereinsetzung begründen, und die Nachholung der Handlung!** Bei Anwälten gehört dazu eine "
                    "geschlossene Schilderung der Abläufe, der **Büroorganisation** und der Auswahl und Kontrolle der Hilfskräfte; glaubhaft gemacht "
                    "werden kann noch im Verfahren (§ 123 Abs. 2 S. 1 bis 3 PatG)."],
                   optionen=["Die begründenden Tatsachen und die Nachholung der versäumten Handlung",
                             "Nur den Antrag; die Begründung kann jederzeit folgen",
                             "Eine eidesstattliche Versicherung des Anmelders selbst",
                             "Die Zustimmung des DPMA"],
                   merke="Tatsachen und Nachholung binnen zwei Monaten.", titel="Inhalt des Antrags", level=2),
             frage("Hat der Antrag Erfolg?", False,
                   ["**Nein!** Pauschales Bestreiten des Zugangs ersetzt keine Darlegung der **Büroorganisation** für fristauslösende Post. An "
                    "Anwälte sind strengere Sorgfaltsanforderungen zu stellen als an Einzelanmelder; das Verschulden wird dem Anmelder zugerechnet "
                    "(BPatG Vorrichtung zum Brechen von Steinen)."],
                   merke="Wer den Zugang bestreitet, muss seine Postorganisation darlegen.", titel="Ergebnis", level=2),
            ],
            abschnitt="Abs. 2: Antrag, Frist, Glaubhaftmachung", level=2, concepts=["pat_wiedereinsetzung", "pat_fristen"],
            norms=["§ 123 Abs. 2 PatG"], cases=["pat_bpatg_vorrichtung_zum_brechen_von_steinen"], step="step:pat_schema_fristversaeumung.3.3"),
        *fallkette("p03n123-3", "Die verspätete Einspruchsgebühr",
            "E legt fristgerecht Einspruch gegen das Patent der P ein, zahlt die Einspruchsgebühr aber erst Monate nach Ablauf der "
            "Einspruchsfrist. E beantragt Wiedereinsetzung in die Zahlungsfrist: Ihre Bank habe den Auftrag verloren.",
            [frage("Für welche Frist ist die Wiedereinsetzung ausgeschlossen?", 0,
                   ["**Für die Frist zur Zahlung der Einspruchsgebühr!** Für die Frist zur Erhebung des Einspruchs und zur **Zahlung der Einspruchsgebühr** ist die Wiedereinsetzung "
                    "ausgeschlossen (§ 123 Abs. 1 S. 2 Nr. 1 PatG). Der Einspruch gilt als nicht erhoben (BGH Verspätete Zahlung der "
                    "Einspruchsgebühr)."],
                   merke="Einspruchsfrist und -gebühr: keine Wiedereinsetzung.", titel="Ausschluss Einspruch", norms=["§ 6 PatKostG"],
                   optionen=["Frist zur Zahlung der Einspruchsgebühr", "Frist zur Zahlung einer Jahresgebühr",
                             "Beschwerdefrist des Anmelders gegen die Zurückweisung", "Frist zur Einreichung der Übersetzung eines europäischen Patents"],
                   step="step:pat_schema_fristversaeumung.3.4"),
             frage("Kann P Wiedereinsetzung beantragen, wenn sie die Frist für die Beschwerde gegen den Widerruf ihres Patents schuldlos "
                   "versäumt?", True,
                   ["**Ja!** Ausgeschlossen ist nur die Beschwerdefrist **des Einsprechenden** gegen die Aufrechterhaltung (§ 123 Abs. 1 S. 2 Nr. 2 "
                    "PatG). Der Patentinhaber kann Wiedereinsetzung in die Beschwerdefrist erhalten."],
                   merke="Ausschluss nur für den Einsprechenden.", titel="Beschwerde des Inhabers", level=2,
                   abwandlung="Die Patentabteilung widerruft das Patent; P versäumt die Beschwerdefrist, weil ihr Anwalt plötzlich schwer erkrankt."),
             frage("Ist die Wiedereinsetzung noch möglich, wenn P den Antrag erst 14 Monate nach Ablauf der Frist stellt?", False,
                   ["**Nein,** grundsätzlich nicht. **Ein Jahr** nach Ablauf der versäumten Frist kann die Wiedereinsetzung nicht mehr beantragt "
                    "werden (§ 123 Abs. 2 S. 4 PatG). Ausnahmen erkennt das BPatG nur in besonders gelagerten Fällen an, etwa wenn das Amt den "
                    "Rechtsverlust verschwiegen hat (BPatG Überwachungsvorrichtung)."],
                   merke="Nach einem Jahr ist Schluss.", titel="Jahresausschlussfrist", level=2, cases=["pat_bpatg_ueberwachungsvorrichtung"]),
            ],
            abschnitt="Abs. 1 S. 2, Abs. 2 S. 4: Ausgeschlossene Fristen", level=1, concepts=["pat_wiedereinsetzung", "pat_einspruch"],
            norms=["§ 123 Abs. 1 PatG"], cases=["pat_bgh_einspruchsgebuehr_verspaetet"], step="step:pat_schema_fristversaeumung.3.4"),
        *fallkette("p03n123-4", "Der Zwischenbenutzer",
            "Das Patent der V erlischt, weil die Jahresgebühr nicht gezahlt wurde. Wettbewerber W beginnt danach im Vertrauen auf das "
            "Erlöschen mit der Produktion. V beantragt Wiedereinsetzung und verklagt W wegen Verletzung; W will sich am "
            "Wiedereinsetzungsverfahren beteiligen.",
            [frage("Ist W am Wiedereinsetzungsverfahren der V beteiligt?", False,
                   ["**Nein!** Das Wiedereinsetzungsverfahren des Patentinhabers ist **einseitig**; ein wegen Verletzung in Anspruch genommener "
                    "Dritter ist nicht beteiligt (BGH Verdickerpolymer II)."],
                   merke="Dritte sind am Wiedereinsetzungsverfahren nicht beteiligt.", titel="Beteiligung Dritter", level=2),
             frage("Kann W die gewährte Wiedereinsetzung anfechten?", False,
                   ["**Nein!** Die Wiedereinsetzung ist **unanfechtbar** (§ 123 Abs. 4 PatG). W bleibt auf die Rechte aus § 123 Abs. 5 PatG "
                    "verwiesen (BGH Verdickerpolymer II)."],
                   merke="Wiedereinsetzung ist unanfechtbar.", titel="Unanfechtbarkeit", norms=["§ 123 Abs. 4 PatG"]),
             frage("Darf W nach der Wiedereinsetzung weiterproduzieren?", True,
                   ["**Ja!** Wer im Inland **gutgläubig** zwischen Erlöschen und Wiederinkrafttreten den Gegenstand in Benutzung genommen oder "
                    "Veranstaltungen dazu getroffen hat, darf ihn für die Bedürfnisse seines eigenen Betriebs **weiterbenutzen** (§ 123 Abs. 5 S. 1 "
                    "PatG). Das Recht geht nur mit dem Betrieb über (S. 2)."],
                   merke="Gutgläubiger Zwischenbenutzer darf weiterbenutzen.", titel="Weiterbenutzungsrecht", norms=["§ 123 Abs. 5 PatG"],
                   concepts=["pat_vorbenutzungsrecht"]),
             frage("Entscheidet das BPatG über den Antrag, wenn die Sache wegen einer Beschwerde schon dort liegt?", True,
                   ["**Ja!** Über den Antrag beschließt die Stelle, die über die nachgeholte Handlung zu beschließen hat (§ 123 Abs. 3 PatG). Ist "
                    "Beschwerde eingelegt, ist das Amt außer für die Abhilfe nicht mehr zuständig, auch nicht für die Wiedereinsetzung (BGH "
                    "Gehäusestruktur)."],
                   merke="Nach Beschwerde entscheidet das BPatG über die Wiedereinsetzung.", titel="Zuständigkeit", level=3,
                   abwandlung="In einem anderen Verfahren hat der Anmelder gegen einen Zurückweisungsbeschluss Beschwerde eingelegt und beantragt erst danach beim DPMA Wiedereinsetzung.",
                   norms=["§ 123 Abs. 3 PatG"], cases=["pat_bgh_gehaeusestruktur"]),
            ],
            abschnitt="Abs. 3 bis 5: Zuständigkeit, Unanfechtbarkeit, Weiterbenutzung", level=2, concepts=["pat_wiedereinsetzung"],
            norms=["§ 123 Abs. 4 PatG", "§ 123 Abs. 5 PatG"], cases=["pat_bgh_verdickerpolymer_ii"], step="step:pat_schema_fristversaeumung.3.3"),
    ]),
    # ================================================================== §§ 1 bis 3 GebrMG
    dict(id="p03g1", order=20100, titel="§§ 1 bis 3 GebrMG: Schutzfähigkeit", einheiten=[
        intro("p03g1-0", "Das kleine Patent mit eigenen Regeln",
              "Als Gebrauchsmuster werden Erfindungen geschützt, die **neu** sind, auf einem **erfinderischen Schritt** beruhen und gewerblich "
              "anwendbar sind (§ 1 Abs. 1 GebrMG); die Ausschlüsse des § 1 Abs. 2 GebrMG entsprechen § 1 Abs. 3 PatG und erfassen zusätzlich "
              "biotechnologische Erfindungen. **Verfahren** sind nach § 2 Nr. 3 GebrMG nicht schutzfähig.\n\n"
              "Der **Stand der Technik** ist enger als im Patentrecht: nur schriftliche Beschreibungen und Benutzungen **im Inland**, keine "
              "mündlichen Beschreibungen (§ 3 Abs. 1 S. 2 GebrMG). Eigene Beschreibungen und Benutzungen in den letzten **sechs Monaten** vor "
              "dem Zeitrang bleiben außer Betracht (**Neuheitsschonfrist**, § 3 Abs. 1 S. 3 GebrMG). Neuheit und erfinderischen Schritt prüft "
              "das DPMA bei der Eintragung nicht; sie werden erst im Löschungs- oder Verletzungsverfahren geklärt.",
              concepts=["pat_gebrauchsmuster", "pat_neuheit", "pat_erfinderische_taetigkeit"],
              norms=["§ 1 GebrMG", "§ 2 GebrMG", "§ 3 GebrMG"], abschnitt="Überblick"),
        *fallkette("p03g1-1", "Der Demonstrationsschrank",
            "D war Inhaberin eines Gebrauchsmusters auf einen Demonstrationsschrank für den naturwissenschaftlichen Unterricht, dessen Kammer von "
            "zwei Vertikalsäulen gehalten wird. Nach Erlöschen streiten die Beteiligten über die Unwirksamkeit. D meint, für den erfinderischen "
            "Schritt genüge ein geringeres Maß an Erfindungshöhe als im Patentrecht.",
            [frage("Ist der erfinderische Schritt ein quantitativ geringeres Maß als die erfinderische Tätigkeit?", False,
                   ["**Nein!** Wie die erfinderische Tätigkeit ist der erfinderische Schritt **kein quantitatives, sondern ein qualitatives** "
                    "Kriterium und das Ergebnis einer **Wertung** (BGH Demonstrationsschrank)."],
                   merke="Erfinderischer Schritt ist keine kleine Erfindungshöhe.", titel="Erfinderischer Schritt"),
             frage("Darf zur Beurteilung auf die Grundsätze zu § 4 PatG zurückgegriffen werden?", True,
                   ["**Ja!** Es kann auf die im Patentrecht entwickelten Grundsätze zurückgegriffen werden, unter Berücksichtigung des **abweichend "
                    "definierten Stands der Technik** in § 3 GebrMG: keine mündlichen Beschreibungen, keine Benutzungen im Ausland (BGH "
                    "Demonstrationsschrank; BGH Installiereinrichtung II)."],
                   merke="Gleiche Prüfung, anderer Stand der Technik.", titel="Patentrechtliche Grundsätze", level=2, norms=["§ 4 PatG"],
                   cases=["pat_bgh_installiereinrichtung_ii"]),
             frage("Kann die Fachperson eine Druckschrift von 1921 trotz des Abstands von fast 100 Jahren mit einer Internetveröffentlichung von 2018 kombinieren?", True,
                   ["**Ja,** das ist nicht ausgeschlossen. Gerade auf Gebieten mit **langen Entwicklungszyklen** kann die Fachperson auch sehr alte Lehren "
                    "heranziehen. Zu prüfen ist aber sorgfältig, ob der ältere Ansatz noch erkennbar im Umfeld der jüngeren Lehre lag (BPatG "
                    "Trocknung von Klärschlamm)."],
                   merke="Alter allein schließt Kombination nicht aus.", titel="Alte und neue Druckschrift", level=3,
                   abwandlung="In einem anderen Löschungsverfahren über eine Anlage zur Klärschlammtrocknung stützt sich die Antragstellerin auf eine Druckschrift von 1921 und eine Internetseite von 2018.",
                   cases=["pat_bpatg_trocknung_von_klaerschlamm"]),
            ],
            abschnitt="§ 1 GebrMG: Erfinderischer Schritt", level=2, concepts=["pat_gebrauchsmuster", "pat_erfinderische_taetigkeit"],
            norms=["§ 1 Abs. 1 GebrMG"], cases=["pat_bgh_demonstrationsschrank"]),
        *fallkette("p03g1-2", "Die Signalfolge",
            "A meldet ein Gebrauchsmuster für ein System zur variablen Tarifierung von Internetgebühren an. Ein Schutzanspruch richtet sich auf "
            "eine Signalfolge, die ein Programm zum Ablauf auf einem Rechner darstellt. Die Gebrauchsmusterstelle weist die Anmeldung insoweit "
            "zurück: Ohne körperliches Substrat sei das ein Verfahren.",
            [frage("Prüft die Gebrauchsmusterstelle bei der Eintragung, ob ein Schutzausschluss nach § 2 GebrMG vorliegt?", True,
                   ["**Ja!** Neuheit, erfinderischen Schritt und gewerbliche Anwendbarkeit prüft das DPMA nicht. Die Ausschlüsse des § 2 GebrMG, "
                    "etwa für **Verfahren**, gehören dagegen zur Eintragungsprüfung (BGH Feldmausbekämpfung)."],
                   merke="Eingetragen wird ungeprüft, aber nicht ohne Blick auf § 2 GebrMG.", titel="Prüfung bei Eintragung",
                   norms=["§ 8 GebrMG"], cases=["pat_bgh_feldmausbekaempfung"]),
             frage("Ist die Signalfolge als Verfahren nach § 2 Nr. 3 GebrMG ausgeschlossen?", False,
                   ["**Nein!** Aus dem Fehlen eines beständigen **körperlichen Substrats** folgt nicht, dass die Erfindung ein Verfahren ist. Einem "
                    "Anspruch auf eine Signalfolge, die ein Programm darstellt, steht § 2 Nr. 3 GebrMG nicht entgegen (BGH Signalfolge)."],
                   merke="Unkörperlich ist nicht gleich Verfahren.", titel="Signalfolge kein Verfahren", level=2),
             frage("Kann ein Anspruch auf die „Verwendung einer Lithiumsilikat-Glaskeramik als Dentalmaterial“ als Gebrauchsmuster geschützt sein?", True,
                   ["**Ja,** wenn sich in dem Verwendungsanspruch **stoffliche Eigenschaften** des Materials manifestieren und er nicht auf ein "
                    "Arbeits- oder Herstellungsverfahren gerichtet ist (BPatG Lithiumsilikat-Glaskeramik)."],
                   merke="Verwendungsanspruch mit Stoffeigenschaften ist kein Verfahren.", titel="Verwendungsanspruch", level=3,
                   abwandlung="Ein anderes Gebrauchsmuster beansprucht die Verwendung einer bestimmten Lithiumsilikat-Glaskeramik als Dentalmaterial.",
                   cases=["pat_bpatg_lithiumsilikat_glaskeramik"]),
            ],
            abschnitt="§ 2 Nr. 3 GebrMG: Keine Verfahren", level=2, concepts=["pat_gebrauchsmuster", "pat_patentkategorie"],
            norms=["§ 2 GebrMG"], cases=["pat_bgh_signalfolge"]),
        *fallkette("p03g1-3", "Der importierte Toilettendeckel",
            "T hält ein Gebrauchsmuster auf einen Toilettendeckel aus einer MDF-Kernschicht mit dekorativen Grafik- und Schutzschichten. "
            "Antragstellerin L stützt die Löschung auf baugleiche Deckel, die ein Händler vor dem Zeitrang nach Deutschland importiert hat; "
            "die Schichtung ist von außen nicht zu erkennen.",
            [frage("Ist die Erfindung schon mit dem Import der Deckel nach Deutschland zugänglich geworden?", False,
                   ["**Nein!** Ist die Erfindung von außen **nicht erkennbar**, etwa weil sie in einer Schichtung besteht, ist die Lehre erst ab dem "
                    "Zeitpunkt zugänglich, zu dem der Gegenstand **Endkunden in Verkaufsräumen** zum Kauf angeboten wird (BPatG Toilettendeckel aus "
                    "Schichtverbundstoff)."],
                   merke="Verborgene Lehre: zugänglich ab Angebot an Endkunden.", titel="Zugänglichkeit importierter Ware", level=2),
             frage("Welche der folgenden Kenntnisse gehört zum Stand der Technik nach § 3 Abs. 1 GebrMG?", 2,
                   ["**Der in Deutschland ausgelegte Prospekt!** Der Stand der Technik umfasst im Gebrauchsmusterrecht nur **schriftliche Beschreibungen** und Benutzungen **im "
                    "Geltungsbereich des GebrMG** (§ 3 Abs. 1 S. 2 GebrMG). Mündliche Beschreibungen und Benutzungen im Ausland zählen nicht; im "
                    "Patentrecht wäre das anders (§ 3 Abs. 1 PatG)."],
                   merke="Nur Schriftliches und Inlandsbenutzung.", titel="Mündliche Beschreibung im Ausland",
                   optionen=["Ein mündlicher Vortrag auf einer Messe in den USA", "Eine Benutzung des Deckels in den USA",
                             "Ein in Deutschland ausgelegter Prospekt mit Schnittzeichnung", "Ein mündlicher Vortrag auf einer Messe in Köln"],
                   abwandlung="L beruft sich zusätzlich auf Vorträge, Benutzungen und Prospekte eines Herstellers aus der Zeit vor dem Zeitrang.",
                   norms=["§ 3 Abs. 1 PatG"]),
            ],
            abschnitt="§ 3 Abs. 1 S. 2 GebrMG: Stand der Technik", level=2, concepts=["pat_gebrauchsmuster", "pat_neuheit"],
            norms=["§ 3 Abs. 1 GebrMG"], cases=["pat_bpatg_toilettendeckel"]),
        *fallkette("p03g1-4", "Der eigene Fenstersensor",
            "Professor I entwickelt einen Tür- und Fenstersensor mit Reflexlichtschranke. Eine Tochtergesellschaft, deren Geschäftsführer er ist, "
            "stellt das Produkt drei Wochen vor dem Anmeldetag auf ihre Website. Danach meldet die J-AG, deren Vorstand I ist, ein Gebrauchsmuster "
            "an. Antragstellerin K beantragt die Löschung wegen fehlender Neuheit.",
            [frage("Bleibt die Website-Veröffentlichung bei der Neuheit außer Betracht?", True,
                   ["**Ja!** Eine Beschreibung oder Benutzung innerhalb von **sechs Monaten** vor dem Zeitrang bleibt außer Betracht, wenn sie auf "
                    "der **Ausarbeitung des Anmelders oder seines Rechtsvorgängers** beruht (§ 3 Abs. 1 S. 3 GebrMG). Erfinder war I, die J-AG seine "
                    "Rechtsnachfolgerin (BPatG Tür- und Fenstersensor)."],
                   merke="Neuheitsschonfrist: sechs Monate für eigene Veröffentlichungen.", titel="Neuheitsschonfrist"),
             frage("Muss die J-AG die Kette vom Erfinder zu Veröffentlichung und Anmeldung lückenlos durch Zeugen beweisen?", False,
                   ["**Nein,** nicht zwingend. Die lückenlose Kette der Wissensvermittlung vom Erfinder zum Inhaber und zu den Veröffentlichungen "
                    "muss feststehen, kann aber in bestimmten Fällen auch durch **Anscheinsbeweis** belegt werden (BPatG Tür- und Fenstersensor)."],
                   merke="Neuheitsschonfrist kann durch Anscheinsbeweis belegt werden.", titel="Nachweis der Kette", level=3),
             frage("Wäre die Veröffentlichung auch bei einer Patentanmeldung unschädlich?", False,
                   ["**Nein!** Das PatG kennt **keine allgemeine Neuheitsschonfrist**. Unschädlich ist eine Offenbarung nur bei offensichtlichem "
                    "Missbrauch oder Zurschaustellung auf einer anerkannten Ausstellung (§ 3 Abs. 5 PatG). Für die eigene Veröffentlichung hilft "
                    "nur das Gebrauchsmuster."],
                   merke="Neuheitsschonfrist gibt es nur beim Gebrauchsmuster.", titel="Vergleich mit dem Patent", level=2,
                   norms=["§ 3 Abs. 5 PatG"]),
            ],
            abschnitt="§ 3 Abs. 1 S. 3 GebrMG: Neuheitsschonfrist", level=2, concepts=["pat_gebrauchsmuster", "pat_neuheit"],
            norms=["§ 3 Abs. 1 GebrMG"], cases=["pat_bpatg_tuer_und_fenstersensor"]),
    ]),
    # ================================================================== §§ 15 bis 17 GebrMG
    dict(id="p03g15", order=21500, titel="§§ 15 bis 17 GebrMG: Löschung", einheiten=[
        intro("p03g15-0", "Das Gegenstück zur Nichtigkeitsklage",
              "Weil das Gebrauchsmuster ungeprüft eingetragen wird, hat **jedermann** gegen den eingetragenen Inhaber einen Anspruch auf Löschung, "
              "wenn der Gegenstand nach §§ 1 bis 3 GebrMG nicht schutzfähig ist (Nr. 1), schon durch eine **frühere Patent- oder "
              "Gebrauchsmusteranmeldung** geschützt ist (Nr. 2) oder über die ursprüngliche Anmeldung hinausgeht (Nr. 3; § 15 Abs. 1 GebrMG). "
              "Bei widerrechtlicher Entnahme ist nur der Verletzte berechtigt (§ 15 Abs. 2 GebrMG); Teillöschung ist möglich (§ 15 Abs. 3 "
              "GebrMG).\n\n"
              "Der Antrag ist schriftlich beim **DPMA** mit Tatsachen zu stellen (§ 16 GebrMG). Widerspricht der Inhaber nicht binnen **eines "
              "Monats**, wird gelöscht (§ 17 Abs. 1 GebrMG); sonst entscheidet die Gebrauchsmusterabteilung durch Beschluss und auch über die "
              "Kosten (§ 17 Abs. 3, 4 GebrMG).",
              concepts=["pat_gebrauchsmuster_loeschung", "pat_gebrauchsmuster"],
              norms=["§ 15 Abs. 1 GebrMG", "§ 16 GebrMG", "§ 17 Abs. 1 GebrMG", "§ 17 Abs. 4 GebrMG"], abschnitt="Überblick"),
        *fallkette("p03g15-1", "Der Löschungsantrag",
            "F hält ein Gebrauchsmuster auf einen Formkörper mit Durchtrittsöffnungen. Antragstellerin A beantragt beim DPMA schriftlich die "
            "Löschung und legt dar, dass derselbe Gegenstand bereits durch ein Patent aus einer früheren Anmeldung geschützt ist.",
            [frage("Braucht A für den Löschungsantrag nach § 15 Abs. 1 Nr. 2 GebrMG ein eigenes Interesse?", False,
                   ["**Nein!** Den Löschungsanspruch nach § 15 Abs. 1 GebrMG hat **jedermann** gegen den als Inhaber Eingetragenen; ein eigenes "
                    "Interesse ist nicht nötig, solange das Gebrauchsmuster besteht."],
                   merke="Löschung: Popularantrag gegen den Eingetragenen.", titel="Antragsbefugnis"),
             frage("Kann F von A eine Sicherheit für die Verfahrenskosten verlangen?", True,
                   ["**Ja!** § 16 S. 3 GebrMG verweist auf § 81 Abs. 6 PatG: Antragsteller ohne gewöhnlichen Aufenthalt in EU oder EWR leisten auf "
                    "Verlangen **Sicherheit** wegen der Kosten."],
                   merke="Ausländische Antragsteller: Sicherheitsleistung.", titel="Sicherheitsleistung", level=2, norms=["§ 81 Abs. 6 PatG"],
                   abwandlung="A hat ihren Sitz in den USA."),
             frage("Was geschieht, wenn F dem Antrag nicht binnen eines Monats widerspricht?", 3,
                   ["**Das Gebrauchsmuster wird gelöscht!** Das DPMA fordert den Inhaber auf, sich binnen eines Monats zu erklären; widerspricht er "
                    "nicht rechtzeitig, erfolgt die Löschung ohne Sachprüfung (§ 17 Abs. 1 GebrMG)."],
                   optionen=["Das DPMA prüft die Schutzfähigkeit von Amts wegen", "Die Frist verlängert sich automatisch",
                             "Der Antrag gilt als zurückgenommen", "Das Gebrauchsmuster wird gelöscht"],
                   merke="Kein Widerspruch, Löschung.", titel="Fehlender Widerspruch", norms=["§ 17 Abs. 1 GebrMG"]),
             frage("Muss das BPatG im Beschwerdeverfahren erörtern, dass das ältere Patent theoretisch später für nichtig erklärt werden könnte?", False,
                   ["**Nein!** Stützt das Gericht die Löschung nach § 15 Abs. 1 Nr. 2 GebrMG auf ein älteres Patent, muss es sich mit der **bloß "
                    "theoretischen Möglichkeit** von dessen künftiger Nichtigerklärung nicht auseinandersetzen; ein Begründungsmangel liegt nicht vor "
                    "(BGH Formkörper mit Durchtrittsöffnungen)."],
                   merke="Älteres Schutzrecht zählt, wie es besteht.", titel="Älteres Patent", level=3, norms=["§ 100 Abs. 3 Nr. 6 PatG"]),
            ],
            abschnitt="§ 15 Abs. 1 GebrMG, §§ 16, 17 GebrMG: Antrag und Verfahren", level=1, concepts=["pat_gebrauchsmuster_loeschung"],
            norms=["§ 15 Abs. 1 Nr. 2 GebrMG", "§ 16 GebrMG"], cases=["pat_bgh_formkoerper_mit_durchtrittsoeffnungen"]),
        *fallkette("p03g15-2", "Das eingefügte Druckermerkmal",
            "T hält ein Gebrauchsmuster auf einen Tintenstrahldrucker. Schutzanspruch 1 enthält ein Merkmal, das in der ursprünglichen "
            "Anmeldung nicht als zur Erfindung gehörend offenbart war; es engt den Gegenstand aber nur ein. Antragstellerin E beantragt die "
            "Löschung nach § 15 Abs. 1 Nr. 3 GebrMG.",
            [frage("Bleibt das Gebrauchsmuster trotz des nicht offenbarten Merkmals bestehen?", True,
                   ["**Ja!** Die Löschung unterbleibt, wenn das nicht offenbarte Merkmal den Gegenstand **nur beschränkt** und keinen Schutz für "
                    "ein **Aliud** begründet. Die Grundsätze zum Patent gelten entsprechend (BGH Tintenstrahldrucker; BGH Winkelmesseinrichtung)."],
                   merke="Beschränkendes Merkmal: keine Löschung.", titel="Einschränkende Erweiterung", level=2,
                   cases=["pat_bgh_winkelmesseinrichtung"]),
             frage("Ändert sich das, weil das Merkmal auch in Ausgestaltungen vorkommen kann, in denen die Erfindung ihr Ziel verfehlt?", False,
                   ["**Nein,** nicht zwingend. Dass das eingefügte Merkmal auch bei **nicht offenbarten Ausgestaltungen** verwirklicht sein kann, mit "
                    "denen das Ziel der Erfindung nicht erreicht wird, führt nicht ohne Weiteres zu einer anderen Beurteilung (BGH "
                    "Tintenstrahldrucker)."],
                   merke="Mögliche Fehlschläge im Schutzumfang machen das Merkmal nicht zum Aliud.", titel="Nicht offenbarte Ausgestaltungen", level=3),
             frage("Kann das Gebrauchsmuster teilweise gelöscht werden, wenn nur einzelne Schutzansprüche nicht schutzfähig sind?", True,
                   ["**Ja!** Betreffen die Löschungsgründe nur einen Teil, wird nur in diesem Umfang gelöscht; die Beschränkung kann durch Änderung "
                    "der Schutzansprüche erfolgen (§ 15 Abs. 3 GebrMG)."],
                   merke="Teillöschung durch geänderte Schutzansprüche.", titel="Teillöschung", norms=["§ 15 Abs. 3 GebrMG"]),
            ],
            abschnitt="§ 15 Abs. 1 Nr. 3, Abs. 3 GebrMG: Erweiterung und Teillöschung", level=2,
            concepts=["pat_gebrauchsmuster_loeschung", "pat_unzulaessige_erweiterung"], norms=["§ 15 Abs. 1 Nr. 3 GebrMG"],
            cases=["pat_bgh_tintenstrahldrucker"]),
        *fallkette("p03g15-3", "Der Holzkohlegrill",
            "G mahnt Händlerin H aus einem Gebrauchsmuster auf einen Grill mit Holzkohlekammer ab. H kündigt einen Löschungsantrag an. Daraufhin "
            "reicht G geänderte Schutzansprüche ein und erklärt, nur noch Rechte aus diesen geltend zu machen. H beantragt trotzdem die Löschung "
            "der abgemahnten eingetragenen Ansprüche.",
            [frage("Haben die nachgereichten Schutzansprüche das eingetragene Gebrauchsmuster geändert?", False,
                   ["**Nein!** Zur Akte nachgereichte Schutzansprüche bewirken **keine unmittelbare Änderung** des eingetragenen Gebrauchsmusters. "
                    "Der Löschungsantrag ist gegen die **eingetragenen** Ansprüche zu richten (BPatG Grill und Holzkohlekammer)."],
                   merke="Eingetragen bleibt eingetragen.", titel="Nachgereichte Ansprüche", level=2, cases=["pat_bpatg_grill_und_holzkohlekammer"]),
             frage("Darf G einen angegriffenen Anspruch durch Kombination mit einem nicht angegriffenen Unteranspruch verteidigen?", False,
                   ["**Nein!** Wie im Nichtigkeitsverfahren ist die beschränkte Verteidigung eines mit **Teil-Löschungsantrag** angegriffenen "
                    "Anspruchs durch Kombination mit einem **nicht angegriffenen Unteranspruch** unzulässig. Zulässig ist die Ergänzung um nur einen "
                    "Teil von dessen Merkmalen (BGH Tischgrill)."],
                   merke="Nicht angegriffener Unteranspruch ist kein Rettungsanker.", titel="Beschränkte Verteidigung", level=3,
                   concepts=["pat_beschraenkte_verteidigung"]),
             frage("Muss H die Kosten tragen, soweit G die Löschung in diesem Umfang nicht mehr bekämpft?", True,
                   ["**Ja,** in der Regel. Über die Kosten gilt § 84 Abs. 2 S. 2 PatG entsprechend (§ 17 Abs. 4 GebrMG), also auch § 93 ZPO. Hat der "
                    "Inhaber sein Schutzbegehren schon **vor dem Antrag** auf die neuen Ansprüche beschränkt, fehlte insoweit der **Anlass** zum "
                    "Löschungsantrag (BGH Tischgrill)."],
                   merke="Vorab beschränkt: kein Anlass, Antragsteller trägt die Kosten.", titel="Kosten bei Anerkenntnis", level=3,
                   norms=["§ 17 Abs. 4 GebrMG", "§ 84 Abs. 2 PatG"], concepts=["pat_kostenerstattung"]),
            ],
            abschnitt="§ 17 Abs. 4 GebrMG: Verteidigung und Kosten", level=2, concepts=["pat_gebrauchsmuster_loeschung"],
            norms=["§ 15 Abs. 3 GebrMG", "§ 17 Abs. 4 GebrMG"], cases=["pat_bgh_tischgrill"]),
        *fallkette("p03g15-4", "Die entnommene Vorrichtung",
            "B meint, das Gebrauchsmuster des C auf eine Vorrichtung zur Immobilisierung beruhe auf ihrer Erfindung, und beantragt die Löschung "
            "wegen widerrechtlicher Entnahme. Während der Beschwerde erlischt das Gebrauchsmuster; C stellt B von allen Ansprüchen frei. B "
            "verfolgt die Löschung weiter.",
            [frage("Kann sich nur B auf die widerrechtliche Entnahme stützen?", True,
                   ["**Ja!** Im Fall der widerrechtlichen Entnahme (§ 13 Abs. 2 GebrMG) steht der Löschungsanspruch **nur dem Verletzten** zu "
                    "(§ 15 Abs. 2 GebrMG)."],
                   merke="Entnahme: nur der Verletzte.", titel="Antragsbefugnis bei Entnahme", norms=["§ 13 Abs. 2 GebrMG"]),
             frage("Ist die Hauptsache nach Erlöschen und Freistellung erledigt?", True,
                   ["**Ja!** Mit Erlöschen und Freistellung tritt **Erledigung der Hauptsache** ein, auch beim Löschungsgrund der Entnahme. "
                    "Verfolgt B die Löschung oder Feststellung der Unwirksamkeit weiter, ist ihre Beschwerde **mangels Beschwer** unzulässig (BPatG "
                    "Vorrichtung zur Immobilisierung)."],
                   merke="Erloschen und freigestellt: erledigt.", titel="Erledigung", level=3),
             frage("Kann der obsiegende Beteiligte im Löschungsverfahren Kosten für Patent- und Rechtsanwalt zugleich erstattet verlangen?", True,
                   ["**Ja,** unter denselben Voraussetzungen wie im Nichtigkeitsverfahren, typischerweise bei parallelem **Verletzungsstreit** "
                    "(BPatG Doppelvertretungskosten im Gebrauchsmuster-Löschungsverfahren; BGH Doppelvertretung im Nichtigkeitsverfahren)."],
                   merke="Doppelvertretung: Maßstab des Nichtigkeitsverfahrens.", titel="Doppelvertretung", level=2,
                   abwandlung="In einem anderen Löschungsverfahren läuft zugleich ein Verletzungsprozess aus dem Gebrauchsmuster gegen die Antragstellerin.",
                   cases=["pat_bpatg_doppelvertretung_gebrauchsmuster", "pat_bgh_doppelvertretung_i"]),
            ],
            abschnitt="§ 15 Abs. 2 GebrMG, § 17 GebrMG: Entnahme, Erledigung, Kosten", level=2, concepts=["pat_gebrauchsmuster_loeschung"],
            norms=["§ 15 Abs. 2 GebrMG"], cases=["pat_bpatg_immobilisierung_erledigung"]),
    ]),
]
