# -*- coding: utf-8 -*-
"""Kosten, Gebühren und Prozesskostensicherheit vor dem EPG, dazu die Gebühren des Einheitspatents beim EPA, im Jurafuchs-Format:
je Kapitel die Kernvorschriften, darin kurze Fallketten mit einer Frage je Auslegungselement."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

KURS = dict(
    id="u08", gebiet="upc", kompakt="fragen", titel="Kosten, Gebühren und Prozesskostensicherheit",
    untertitel="Gerichtsgebühren und Streitwert, Kostengrundentscheidung und Kostenfestsetzung, Sicherheit für die Kosten des Beklagten – und die Jahresgebühren, Lizenzbereitschaft und Registereintragungen des Einheitspatents beim EPA",
    farbe="#0f766e", icon="tabelle",
    beschreibung="Das Geld hinter dem Verfahren: Festgebühr und streitwertabhängige Gebühr nach R. 370 VerfO, Ermäßigung und Erstattung (Juul/NJOY, Roku/Dolby), der Streitwert nach R. 370.6 VerfO (Kodak/Fujifilm), die Kostengrundentscheidung nach Art. 69 EPGÜ mit Obergrenzen (SharkNinja, Strabag/Swarco), die Kostenfestsetzung nach R. 150 bis 157 VerfO mit ihrer Monatsfrist, die Kosten bei Erledigung nach R. 360 VerfO (Dolby/Roku) und die Prozesskostensicherheit nach Art. 69 Abs. 4 EPGÜ, R. 158 VerfO in der Linie Aarke/SodaStream, Hefei/Grundfos, Syntorr/Arthrex, La Siddhi/Athena und Suinno/Microsoft. Das vierte Kapitel wechselt vom Gericht zum EPA: Jahresgebühren des Einheitspatents nach Art. 2 GebOEPS mit Nachfrist und Erlöschen (R. 13, 14 DOEPS), 15 % Ermäßigung bei Lizenzbereitschaft (Art. 8 EPatVO, R. 12 DOEPS) und das Register für den einheitlichen Patentschutz (Art. 3 Abs. 2 EPatVO, R. 16 DOEPS).",
    kapitel=[
        dict(id="u08a", titel="R. 370 VerfO: Gerichtsgebühren und Streitwert", einheiten=[
            schema("u08a-0", "Prüfungsschema: Kosten, Gebühren und Prozesskostensicherheit", "upc_schema_kosten",
                   "Vier Stationen: die Gerichtsgebühren bei Einreichung (R. 370 VerfO), die Sicherheit für die Kosten des Beklagten während des Verfahrens (Art. 69 Abs. 4 EPGÜ, R. 158 VerfO), die Kostengrundentscheidung im Urteil (Art. 69 Abs. 1 bis 3 EPGÜ, R. 118.5 VerfO) und die Kostenfestsetzung danach (R. 150 bis 157 VerfO). Die Obergrenzen der erstattungsfähigen Vertretungskosten hängen am Streitwert (R. 152.2 VerfO). Nicht zu verwechseln mit den Jahresgebühren des Einheitspatents, die an das EPA gehen (Art. 11 EPatVO, R. 13 DOEPS, Art. 2 GebOEPS; viertes Kapitel dieses Kurses)."),
            *fallkette("u08a-1", "Zwei Patente, drei Beklagte",
                "Norvex erhebt Verletzungsklage aus zwei Patenten gegen drei Beklagte; der Streitwert beträgt 2 Mio. EUR. Die Beklagten "
                "erheben Widerklage auf Nichtigerklärung.",
                [frage("Welche Gebühren zahlt Norvex für die Verletzungsklage?", 1,
                       ["Für die Verletzungsklage fällt eine **Festgebühr** an (R. 370.2 lit. a VerfO). Weil der Streitwert 500.000 EUR "
                        "übersteigt, kommt eine **streitwertabhängige Gebühr** nach der Gebührentabelle hinzu (R. 370.3 VerfO)."],
                       optionen=["Nur eine Festgebühr", "Festgebühr und streitwertabhängige Gebühr", "Nur eine streitwertabhängige Gebühr"],
                       titel="Fest- und Wertgebühr"),
                 frage("Zahlt Norvex trotz zweier Patente und dreier Beklagter nur eine Festgebühr?", True,
                       ["**Ja!** Betrifft eine Klage mehrere Kläger, Beklagte oder Patente, ist nach R. 370.7 VerfO gleichwohl **nur eine** "
                        "Festgebühr und gegebenenfalls eine streitwertabhängige Gebühr zu zahlen."],
                       merke="Eine Gebühr je Klage, gleich wie viele Patente und Beklagte (R. 370.7 VerfO).", titel="Eine Klage, eine Gebühr"),
                 frage("Ist die Widerklage gebührenfrei, weil sie der Verteidigung dient?", False,
                       ["**Nein!** Auch die Widerklage auf Nichtigerklärung ist gebührenpflichtig (R. 370.4 lit. b VerfO), ebenso die "
                        "Nichtigkeitsklage vor der Zentralkammer (lit. a)."],
                       titel="Gebühr der Widerklage"),
                 frage("Bekommt Norvex die Hälfte der Gerichtsgebühren zurück?", False,
                       ["**Nein!** Die Erstattung von 50 % setzt voraus, dass die Klage **vor Abschluss des schriftlichen Verfahrens** "
                        "zurückgenommen wird (R. 370.9 lit. b VerfO in der Fassung ab 1.1.2026; EPG-BerG Juul/NJOY). Nach der "
                        "Zwischenanhörung ist es dafür zu spät."],
                       abwandlung="Norvex nimmt die Klage nach der Zwischenanhörung zurück.", level=2, titel="Erstattung bei Rücknahme",
                       cases=["upc_coa_juul_njoy_gebuehren"], concepts=["upc_ruecknahme"]),
                 frage("Kann Norvex als Kleinunternehmen ermäßigte Gebühren zahlen?", True,
                       ["**Ja!** Kleine Unternehmen und Kleinstunternehmen zahlen ermäßigte Gebühren, wenn sie die Erklärung nach R. 370.8 "
                        "VerfO abgeben. Gefährden die Gebühren die wirtschaftliche Existenz, kommt eine Erstattung nach R. 370.10 VerfO in "
                        "Betracht."],
                       abwandlung="Norvex ist ein Kleinunternehmen.", titel="Ermäßigung für KMU"),
                 ],
                abschnitt="R. 370.2 bis 370.10 VerfO: Gebühren", level=1,
                concepts=["upc_gerichtsgebuehren"], norms=["R. 370.2 VerfO", "R. 370.3 VerfO", "R. 370.7 VerfO", "R. 370.9 VerfO"],
                step="step:upc_schema_kosten.1"),
            *fallkette("u08a-2", "Vier Berufungen, eine Gebühr?",
                "Dolby verklagt Roku in vier Verfahren. Roku rügt jeweils mit demselben Einspruch die Zuständigkeit; die Lokalkammer weist alle "
                "vier zurück. Roku legt vier Berufungen ein, zahlt aber nur eine Berufungsgebühr.",
                [frage("Genügt eine Gebühr, weil die Rechtsfrage in allen vier Verfahren identisch ist?", False,
                       ["**Nein!** Die Berufungsgebühr ist **für jedes Berufungsverfahren** zu entrichten (R. 370.5, R. 228 VerfO). Jede "
                        "Berufung richtet sich gegen eine eigene Entscheidung; gleiche Fragen ändern daran nichts (EPG-BerG Roku/Dolby)."],
                       merke="Je Berufungsverfahren eine Gebühr, auch bei gleicher Rechtsfrage (Roku/Dolby).", titel="Je Verfahren eine Gebühr"),
                 frage("Bleibt es bei vier Gebühren, auch wenn das Berufungsgericht gemeinsam verhandelt?", True,
                       ["**Ja!** Die gemeinsame Verhandlung nach R. 220.5 VerfO ist eine Frage der Verfahrensleitung, nicht der Gebühr "
                        "(EPG-BerG Roku/Dolby)."],
                       titel="Gemeinsame Verhandlung", norms=["R. 220.5 VerfO"]),
                 frage("Hilft Roku die Regel für mehrere Patente und Parteien in R. 370.7 VerfO?", False,
                       ["**Nein!** R. 370.7 VerfO privilegiert mehrere Patente oder Parteien **innerhalb einer Klage**. Mehrere Klagen oder "
                        "Berufungen bleiben mehrere Verfahren."],
                       level=2, titel="Grenze von R. 370.7 VerfO"),
                 frage("Was droht, wenn Roku die fehlenden Gebühren nicht nachzahlt?", 1,
                       ["Zahlt der Berufungskläger die Gebühr nicht innerhalb der von der Kanzlei gesetzten Frist, weist der Präsident des "
                        "Berufungsgerichts die Berufung durch Versäumnisentscheidung als **unzulässig** zurück (R. 229.4 VerfO)."],
                       optionen=["Nichts, die Gebühr wird später eingezogen", "Die Berufung wird als unzulässig zurückgewiesen",
                                 "Roku verliert den Rechtsstreit in der Sache"],
                       titel="Folge der Nichtzahlung", norms=["R. 229 VerfO"]),
                 ],
                abschnitt="R. 370.5 VerfO: Berufungsgebühr", level=1,
                concepts=["upc_gerichtsgebuehren", "upc_berufung"], norms=["R. 370.5 VerfO", "R. 228 VerfO"],
                cases=["upc_coa_roku_dolby_einspruch"], step="step:upc_schema_kosten.1"),
            *fallkette("u08a-3", "Der Streitwert der Vollstreckung",
                "Gegen Kodak sind wegen Verstößen gegen eine Unterlassungsanordnung Zwangsgelder von 300.000 EUR festgesetzt. Kodak legt "
                "Berufung ein. Fujifilm, die vollstreckt, will den Streitwert auf 300.000 EUR festsetzen lassen.",
                [frage("Wessen Interesse bestimmt den Streitwert nach R. 370.6 VerfO?", 1,
                       ["Der Streitwert spiegelt das **objektive Interesse der Partei, die das Verfahren eingeleitet hat**, im Zeitpunkt der "
                        "Einleitung (R. 370.6 VerfO). Im Vollstreckungsverfahren ist das Fujifilm (EPG-BerG Kodak/Fujifilm 2026)."],
                       optionen=["Das Interesse von Kodak an der Abwehr", "Das Interesse der Partei, die das Verfahren eingeleitet hat",
                                 "Das Interesse des Gerichts an den Zwangsgeldern"],
                       titel="Maßstab"),
                 frage("Bleibt in Kodaks Berufung das Interesse von Fujifilm maßgeblich?", True,
                       ["**Ja!** Der Wert in der Berufung kann von der ersten Instanz abweichen. Bei einer Berufung des Beklagten bleibt aber "
                        "das Interesse des **Klägers** am Bestand der Entscheidung maßgeblich (EPG-BerG Kodak/Fujifilm 2026)."],
                       level=3, titel="Streitwert in der Berufung"),
                 frage("Ist die Summe der verfallenen Zwangsgelder das Interesse von Fujifilm?", False,
                       ["**Nein!** Zwangsgelder fließen **an das Gericht** (Art. 82 Abs. 4 EPGÜ, R. 354.3 VerfO), nicht an Fujifilm. "
                        "Maßgeblich ist Fujifilms Interesse an der Befolgung der Pflichten, zu der die Zwangsgelder anhalten sollen "
                        "(EPG-BerG Kodak/Fujifilm 2026)."],
                       merke="Zwangsgelder sind kein Streitwert; sie gehören dem Gericht.", titel="Zwangsgelder zählen nicht",
                       concepts=["upc_zwangsgeld"], norms=["Art. 82 Abs. 4 EPGÜ", "R. 354.3 VerfO"]),
                 frage("Kann Kodak die Streitwertfestsetzung ohne Zulassung anfechten, weil sie im Tenor steht?", False,
                       ["**Nein!** Die Streitwertfestsetzung ist eine Verfahrensentscheidung. Gegen sie steht nur der Weg über R. 220.2 und "
                        "220.3 VerfO offen, auch wenn sie im Tenor steht (EPG-BerG Kodak/Fujifilm 2026)."],
                       level=3, titel="Anfechtung", norms=["R. 220.2 VerfO"]),
                 ],
                abschnitt="R. 370.6 VerfO: Streitwert", level=2,
                concepts=["upc_streitwert"], norms=["R. 370.6 VerfO"],
                cases=["upc_coa_kodak_fujifilm_aufhebung_zwangsgeld"], step="step:upc_schema_kosten.1"),
        ]),
        dict(id="u08b", titel="Art. 69 Abs. 1 bis 3 EPGÜ, R. 150 bis 157 und 360 VerfO: Kostenentscheidung und Kostenfestsetzung", einheiten=[
            intro("u08b-0", "Wer zahlt, wie viel, und in welchem Verfahren",
                  "Art. 69 Abs. 1 EPGÜ enthält den Grundsatz: Die Kosten des Rechtsstreits und sonstigen Kosten der **obsiegenden Partei** trägt in der Regel die unterlegene Partei, soweit sie **zumutbar und angemessen** sind und **bis zu einer Obergrenze**, die der Verwaltungsausschuss nach dem Streitwert festlegt (R. 152.2 VerfO), sofern Billigkeitsgründe nicht entgegenstehen. Bei teilweisem Obsiegen oder außergewöhnlichen Umständen verteilt das Gericht die Kosten nach Billigkeit oder lässt jede Partei ihre Kosten tragen (Abs. 2); wer unnötige Kosten verursacht, soll sie tragen (Abs. 3). Das Gericht entscheidet in der Sachentscheidung **dem Grunde nach** über die Kostentragung (R. 118.5 VerfO) und kann eine vorläufige Kostenerstattung zusprechen (R. 150.2 VerfO). Die **Höhe** wird in einem gesonderten Verfahren festgesetzt: Antrag der obsiegenden Partei **binnen eines Monats** nach der Entscheidung mit Angabe der Kosten (R. 151 VerfO), Anhörung der Gegenseite, Entscheidung des Berichterstatters (R. 156 VerfO); erstattungsfähig sind die Gerichtsgebühren, die angemessenen und verhältnismäßigen Kosten der Vertretung (R. 152 VerfO), Kosten für Zeugen und Sachverständige (R. 153, 154 VerfO) und sonstige Ausgaben. Zwei Feinheiten aus der Rechtsprechung: Bei zwei Patenten und Erfolg nur mit einem sind die Kosten nach den Werten der Patente zu verteilen (EPG-BerG SharkNinja); der Streithelfer wird kostenrechtlich wie die Hauptpartei behandelt (EPG-BerG Strabag/Swarco). Erledigt sich das Verfahren, entscheidet das Gericht nach R. 360 VerfO über die Kosten danach, ob der Beklagte Anlass zur Klage gegeben hat. Art. 69 EPGÜ setzt Art. 14 DurchsetzungsRL um; das deutsche Pendant sind §§ 91 ff. ZPO mit der Streitwertbegünstigung des § 144 PatG.",
                  concepts=["upc_kostenerstattung", "upc_streithilfe"], norms=["Art. 69 Abs. 1 EPGÜ", "Art. 69 Abs. 2 EPGÜ", "R. 118.5 VerfO", "R. 152 VerfO"],
                  cases=["upc_coa_strabag_swarco_streithilfe"]),
            *fallkette("u08b-1", "Zwei Patente, ein Sieg",
                "SharkNinja wird aus zwei Patenten verklagt. Patent A ist verletzt; SharkNinja wird zur Unterlassung verurteilt. Patent B, "
                "das den größeren Teil des Streitwerts ausmacht, wird auf die Widerklage widerrufen.",
                [frage("Wer trägt nach Art. 69 Abs. 1 EPGÜ in der Regel die Kosten?", 0,
                       ["Die unterlegene Partei trägt in der Regel die Kosten der obsiegenden, soweit sie **zumutbar und angemessen** sind, "
                        "**bis zu einer Obergrenze** nach dem Streitwert und sofern Billigkeitsgründe nicht entgegenstehen (Art. 69 Abs. 1 "
                        "EPGÜ, R. 152.2 VerfO)."],
                       optionen=["Die unterlegene Partei, zumutbar, angemessen und bis zur Obergrenze",
                                 "Jede Partei ihre eigenen Kosten", "Stets der Beklagte"],
                       titel="Grundsatz", norms=["Art. 69 Abs. 1 EPGÜ"]),
                 frage("Hat die Klägerin voll obsiegt, weil sie die Unterlassung erreicht hat?", False,
                       ["**Nein!** Der Umfang des Obsiegens bemisst sich nach den **Streitgegenständen**, nicht nach dem wirtschaftlichen "
                        "Ergebnis. Mit Patent B ist die Klägerin unterlegen; die Kosten werden nach Billigkeit verteilt (Art. 69 Abs. 2 EPGÜ)."],
                       titel="Teilweises Obsiegen"),
                 frage("Wie verteilt das Gericht die Kosten in der Regel?", 1,
                       ["Haben zwei Patente unterschiedlichen Erfolg, ist es in der Regel angemessen, die Kosten **im Verhältnis der Werte "
                        "der Patente** zu verteilen; alternativ trägt jede Partei die Kosten, die dem jeweiligen Patent zuzuordnen sind "
                        "(EPG-BerG SharkNinja). Hier trägt die Klägerin den größeren Teil."],
                       optionen=["Je zur Hälfte", "Im Verhältnis der Werte der beiden Patente", "Ganz die Klägerin"],
                       merke="Zwei Patente, ein Erfolg: Kosten nach dem Wertverhältnis der Patente (SharkNinja).", level=2,
                       titel="Wertverhältnis"),
                 frage("Gilt diese Verteilung auch für die Kosten der Widerklage?", True,
                       ["**Ja!** Die Verteilung erfasst auch die Kosten der Widerklage, mit der SharkNinja gegen Patent B obsiegt hat "
                        "(EPG-BerG SharkNinja)."],
                       titel="Kosten der Widerklage"),
                 ],
                abschnitt="Art. 69 Abs. 1 und 2 EPGÜ: Obsiegen und Verteilung", level=2,
                concepts=["upc_kostenerstattung"], norms=["Art. 69 Abs. 2 EPGÜ", "R. 118.5 VerfO"],
                cases=["upc_coa_sharkninja_kosten"], step="step:upc_schema_kosten.3"),
            *fallkette("u08b-2", "Unterwerfung nach Abmahnung",
                "Edwards mahnt Meril ab und beantragt dann einstweilige Maßnahmen. Nach der Einreichung gibt Meril eine Unterlassungs- und "
                "Verpflichtungserklärung ab, die Edwards annimmt. Beide erklären das Verfahren für erledigt.",
                [frage("Kann das Gericht das Verfahren als erledigt abschließen?", True,
                       ["**Ja!** Ist eine Klage gegenstandslos geworden, weist das Gericht sie nach rechtlichem Gehör ab (R. 360 VerfO). Über "
                        "die Kosten entscheidet es nach Art. 69 EPGÜ; dazu muss es die obsiegende Partei bestimmen."],
                       titel="Erledigung", norms=["R. 360 VerfO"]),
                 frage("Muss das Gericht prüfen, ob der Eilantrag bei Abgabe der Erklärung zulässig und begründet war?", False,
                       ["**Nein!** Verpflichtet sich der Beklagte nach Einleitung des Verfahrens, den Anträgen nachzukommen, ist das in der "
                        "Regel nicht nötig. Die Erklärung zeigt selbst, dass die Anträge erfüllt wurden (EPG-BerG Meril/Edwards 2024)."],
                       titel="Keine Prüfung der Erfolgsaussicht"),
                 frage("Wer ist danach in der Regel obsiegende Partei?", 1,
                       ["In der Regel ist der **Kläger** obsiegende Partei im Sinne von Art. 69 Abs. 1 EPGÜ, weil die Erklärung seinen "
                        "Anträgen entspricht. Maßgeblich sind die Anträge und der Inhalt der Erklärung (EPG-BerG Meril/Edwards 2024)."],
                       optionen=["Meril, weil der Antrag abgewiesen wird", "Edwards, weil die Erklärung die Anträge erfüllt",
                                 "Niemand; die Kosten werden geteilt"],
                       merke="Unterwerfung nach Klage: In der Regel hat der Kläger obsiegt (Meril/Edwards 2024).", titel="Obsiegende Partei"),
                 ],
                abschnitt="Art. 69 Abs. 1 EPGÜ, R. 360 VerfO: Kosten bei Erledigung", level=2,
                concepts=["upc_kostenerstattung", "upc_einstweilige_massnahmen"], norms=["Art. 69 Abs. 1 EPGÜ"],
                cases=["upc_coa_meril_edwards_obsiegende_partei"], step="step:upc_schema_kosten.3"),
            *fallkette("u08b-3", "Ohne Abmahnung in die Erledigung",
                "Dolby beantragt ohne vorherige Abmahnung einstweilige Maßnahmen gegen Roku. Nach Zustellung gibt Roku sofort eine "
                "strafbewehrte Unterlassungserklärung ab. Beide erklären das Verfahren für erledigt.",
                [frage("War der Antrag auch ohne vorherige Abmahnung zulässig?", True,
                       ["**Ja!** Eine Abmahnung ist **keine Voraussetzung** für Zulässigkeit oder Begründetheit eines Antrags auf "
                        "einstweilige Maßnahmen (LK München Dolby/Roku)."],
                       titel="Abmahnung keine Voraussetzung"),
                 frage("Entfällt ohne Abmahnung die Dringlichkeit?", False,
                       ["**Nein!** Das Fehlen der Abmahnung lässt die Dringlichkeit nach R. 211.4 VerfO nicht entfallen (LK München "
                        "Dolby/Roku)."],
                       titel="Dringlichkeit"),
                 frage("Worauf stellt das Gericht bei der Kostenentscheidung ab?", 2,
                       ["Maßgeblich ist, ob der Beklagte **Anlass zur Klage** gegeben hat, beurteilt aus der objektiven Sicht einer Person in "
                        "der Lage des Klägers bei Einreichung (LK München Dolby/Roku)."],
                       optionen=["Allein auf die Erfolgsaussicht des Antrags", "Auf die Höhe der angefallenen Kosten",
                                 "Darauf, ob der Beklagte Anlass zum Antrag gegeben hat"],
                       titel="Veranlassung"),
                 frage("Kann Dolby die Kosten tragen müssen?", True,
                       ["**Ja!** Hat Roku erst durch den Antrag von der Verletzung erfahren und sich sofort unterworfen, hat sie keinen Anlass "
                        "gegeben; dann können die Kosten Dolby auferlegt werden (LK München Dolby/Roku). Der Gedanke entspricht § 93 ZPO."],
                       merke="Wer ohne Abmahnung vorgeht, riskiert bei sofortiger Unterwerfung die Kosten.", titel="Kostenrisiko"),
                 ],
                abschnitt="Art. 69 Abs. 2 EPGÜ, R. 360 VerfO: Veranlassung", level=2,
                concepts=["upc_ruecknahme", "upc_kostenerstattung", "upc_einstweilige_massnahmen"], norms=["R. 360 VerfO", "Art. 69 Abs. 2 EPGÜ", "Art. 62 EPGÜ"],
                cases=["upc_cfi_dolby_roku_veranlassung"], step="step:upc_schema_kosten.3"),
            *fallkette("u08b-4", "Die Rechnung von Ilion",
                "Die Lokalkammer verurteilt Tarsus am 5. Mai und legt ihr die Kosten auf. Ilion hat Vertretungskosten von 600.000 EUR "
                "aufgewandt; die Obergrenze für den Streitwert liegt bei 400.000 EUR.",
                [frage("Bis wann muss Ilion die Kostenfestsetzung beantragen?", 0,
                       ["Die obsiegende Partei muss den Antrag **innerhalb eines Monats nach der Entscheidung** stellen und die Kosten "
                        "angeben (R. 151 VerfO). Die Jahresfrist gilt für den Schadensersatz (R. 126 VerfO)."],
                       optionen=["Binnen eines Monats nach der Entscheidung", "Binnen eines Jahres", "Ohne Frist bis zur Verjährung"],
                       merke="Kostenfestsetzung: ein Monat (R. 151 VerfO).", titel="Monatsfrist", norms=["R. 151 VerfO"]),
                 frage("Bekommt Ilion die vollen 600.000 EUR erstattet?", False,
                       ["**Nein!** Erstattungsfähig sind nur **angemessene und verhältnismäßige** Vertretungskosten (R. 152.1 VerfO) und nur "
                        "**bis zur Obergrenze** der Tabelle des Verwaltungsausschusses (R. 152.2 VerfO). Ilion erhält höchstens 400.000 EUR."],
                       titel="Obergrenze", norms=["R. 152 VerfO"]),
                 frage("Entscheidet der Berichterstatter allein und schriftlich?", True,
                       ["**Ja!** Der **Berichterstatter** entscheidet schriftlich, nachdem die unterlegene Partei sich äußern konnte "
                        "(R. 156 VerfO). Gegen seine Entscheidung gibt es nur die Berufung nach R. 221 VerfO (R. 157 VerfO)."],
                       titel="Berichterstatter", norms=["R. 156 VerfO"]),
                 frage("Lässt sich die versäumte Frist nur durch Wiedereinsetzung heilen?", True,
                       ["**Ja!** Eine versäumte Frist nach R. 151 VerfO lässt sich nur durch **Wiedereinsetzung** in den vorigen Stand "
                        "heilen (R. 320 VerfO; EPG-BerG Hanshow/SES-imagotag)."],
                       abwandlung="Ilion stellt den Antrag erst eine Woche nach Fristablauf.", level=3, titel="Wiedereinsetzung",
                       cases=["upc_coa_hanshow_ses_kostenfrist"]),
                 frage("Läuft die Monatsfrist für die Kosten eines Eilverfahrens ab der Eilanordnung, wenn eine Hauptsache folgt?", False,
                       ["**Nein!** Die Frist beginnt mit Zustellung der **Sachentscheidung**. Nur wenn kein Hauptsacheverfahren folgt, etwa "
                        "nach erfolglosem Eilantrag, gelten R. 150 und 151 VerfO entsprechend ab Zustellung der Eilanordnung (EPG-BerG "
                        "Hanshow/SES-imagotag)."],
                       level=3, titel="Kosten des Eilverfahrens", cases=["upc_coa_hanshow_ses_kostenfrist"], norms=["R. 150 VerfO"]),
                 ],
                abschnitt="R. 150 bis 157 VerfO: Kostenfestsetzung", level=2,
                concepts=["upc_kostenerstattung"], norms=["Art. 69 Abs. 1 EPGÜ"],
                step="step:upc_schema_kosten.4"),
        ]),
        dict(id="u08c", titel="Art. 69 Abs. 4 EPGÜ, R. 158 VerfO: Prozesskostensicherheit", einheiten=[
            intro("u08c-0", "Sicherheit für die Kosten des Beklagten",
                  "Art. 69 Abs. 4 EPGÜ erlaubt dem Gericht, auf Antrag des Beklagten anzuordnen, dass der **Antragsteller** für die Kosten des Beklagten, die er möglicherweise tragen muss, angemessene **Sicherheit** leistet – insbesondere in den Fällen der Art. 59 bis 62 EPGÜ. R. 158.1 VerfO gestattet den Antrag zu jedem Zeitpunkt des Verfahrens; das Gericht bestimmt Frist und Form (Hinterlegung oder Bankbürgschaft), gewährt zuvor rechtliches Gehör (R. 158.2 VerfO) und weist darauf hin, dass bei Nichtleistung eine **Versäumnisentscheidung** nach R. 355 VerfO ergehen kann (R. 158.4, 158.5 VerfO). Die Anordnung ist mit Zulassung nach R. 220.2 VerfO anfechtbar (R. 158.3 VerfO). Die Voraussetzungen hat das Berufungsgericht in einer Linie von Entscheidungen geschärft: Der Antragsteller muss darlegen, dass die Vermögensverhältnisse des Klägers die Erstattung gefährden oder die Vollstreckung einer Kostenentscheidung unmöglich oder unangemessen beschwerlich wäre (LK München Edwards/Meril; EPG-BerG Aarke/SodaStream); maßgeblich ist die finanzielle Lage des Klägers selbst, nicht seines Konzerns; Sicherheit kann nur **gegen den Antragsteller** des jeweiligen Rechtszugs angeordnet werden, in erster Instanz also nur gegen den Kläger, in der Berufung nur gegen den Berufungskläger (Hefei/Grundfos; Suinno/Microsoft); eine Prozessfinanzierungsversicherung ist zu berücksichtigen (Syntorr/Arthrex); der KMU-Status befreit nicht, kann aber die Höhe beeinflussen, die sich an der Obergrenze der erstattungsfähigen Kosten orientiert (La Siddhi/Athena). Die Vorschrift entspricht funktional § 110 ZPO, ist aber nicht auf Kläger aus Drittstaaten beschränkt.",
                  concepts=["upc_prozesskostensicherheit", "upc_versaeumnisentscheidung"], norms=["Art. 69 Abs. 4 EPGÜ", "R. 158 VerfO", "R. 158.5 VerfO", "R. 355 VerfO"],
                  cases=["upc_cfi_edwards_meril_cms"]),
            *fallkette("u08c-1", "Der solvente Konzern",
                "Aarke, eine schwedische Gesellschaft mit geringem Eigenkapital und Verlusten, klagt gegen SodaStream. SodaStream beantragt "
                "Prozesskostensicherheit. Aarke verweist auf ihren finanzstarken Konzern.",
                [frage("Kommt es allein auf die finanzielle Lage von Aarke selbst an?", True,
                       ["**Ja!** Maßgeblich ist **allein die finanzielle Lage des Klägers selbst**. Die Konzernmutter ist nicht Partei, "
                        "und ihre Bereitschaft, einzustehen, ist rechtlich nicht gesichert (EPG-BerG Aarke/SodaStream)."],
                       merke="R. 158 VerfO: Es zählt die Kasse des Klägers, nicht die des Konzerns.", titel="Konzern"),
                 frage("Verhindert Aarkes Zusage, etwaige Kosten zu erstatten, die Anordnung?", False,
                       ["**Nein!** Die bloße Bereitschaft des Klägers zur Erstattung ist unerheblich (EPG-BerG Aarke/SodaStream)."],
                       titel="Erstattungszusage"),
                 frage("Prüft das Gericht die Erfolgsaussichten von Aarkes Klage?", False,
                       ["**Nein!** Die Erfolgsaussichten werden im Sicherheitsverfahren nicht geprüft (EPG-BerG Aarke/SodaStream)."],
                       titel="Keine Prüfung der Erfolgsaussicht"),
                 frage("Was muss SodaStream darlegen?", 1,
                       ["Der Antragsteller muss darlegen, dass die Vermögenslage des Klägers die Erstattung gefährdet oder die Vollstreckung "
                        "einer Kostenentscheidung **unmöglich oder unangemessen beschwerlich** wäre. Beweisen muss er die Unmöglichkeit nicht "
                        "(EPG-BerG Aarke/SodaStream)."],
                       optionen=["Dass Aarke den Prozess sicher verliert",
                                 "Dass Aarkes Vermögenslage die Erstattung gefährdet oder die Vollstreckung unangemessen erschwert",
                                 "Dass Aarke außerhalb der EU sitzt"],
                       titel="Darlegungslast"),
                 frage("Genügt der Sitz in einem anderen EU-Staat für die Sicherheit?", False,
                       ["**Nein!** Wer sich auf Vollstreckungshindernisse im Sitzstaat beruft, muss das dortige Recht und seine Anwendung "
                        "darlegen. Innerhalb der EU gelingt das wegen der Brüssel-Ia-VO selten (EPG-BerG Aarke/SodaStream)."],
                       abwandlung="Wie wäre es, wenn Aarke solvent wäre und SodaStream nur auf den Sitz in Schweden verwiese?", level=3,
                       titel="Sitz in der EU"),
                 ],
                abschnitt="R. 158.1 VerfO: Voraussetzungen", level=2,
                concepts=["upc_prozesskostensicherheit"], norms=["Art. 69 Abs. 4 EPGÜ", "R. 158.1 VerfO"],
                cases=["upc_coa_aarke_sodastream_sicherheit", "upc_cfi_edwards_meril_cms"], step="step:upc_schema_kosten.2"),
            *fallkette("u08c-2", "Sicherheit gegen den Widerkläger?",
                "Grundfos klagt gegen die chinesische Herstellerin Hefei. Hefei erhebt Widerklage auf Nichtigerklärung. Grundfos beantragt, "
                "Hefei Sicherheit für die Kosten der Widerklage aufzugeben.",
                [frage("Kann Sicherheit nach Art. 69 Abs. 4 EPGÜ nur gegen den Antragsteller des Rechtszugs ergehen?", True,
                       ["**Ja!** Art. 69 Abs. 4 EPGÜ erlaubt die Anordnung nur zu Lasten des **Antragstellers**, der den Rechtszug in Gang "
                        "bringt, und nur auf Antrag des **Beklagten**. In erster Instanz ist das der Kläger (EPG-BerG Hefei/Grundfos)."],
                       merke="Sicherheit nur gegen den, der den Rechtszug eröffnet.", titel="Nur gegen den Antragsteller"),
                 frage("Wird Hefei durch die Widerklage zur Antragstellerin?", False,
                       ["**Nein!** Die Widerklage ist die unmittelbare Folge der Verletzungsklage und macht den Beklagten nicht zum "
                        "Antragsteller im Sinne des Art. 69 Abs. 4 EPGÜ (EPG-BerG Hefei/Grundfos; bestätigt in Suinno/Microsoft)."],
                       titel="Widerklage", concepts=["upc_widerklage_nichtigkeit"]),
                 frage("Geht der weitere Wortlaut von R. 158.1 VerfO vor?", False,
                       ["**Nein!** R. 158.1 VerfO spricht zwar vom Antrag „einer Partei“ gegen „die andere Partei“. Die Regel ist aber im "
                        "Lichte des vorrangigen Übereinkommens auszulegen (Art. 41 Abs. 1 EPGÜ; EPG-BerG Hefei/Grundfos)."],
                       level=3, titel="Vorrang des EPGÜ"),
                 frage("Kann Grundfos nun für die Berufung Sicherheit von Hefei verlangen?", True,
                       ["**Ja!** In der Berufung gilt das Prinzip spiegelbildlich: Antragsbefugt ist der **Berufungsbeklagte**, Sicherheit "
                        "schuldet der Berufungskläger, auch wenn er erstinstanzlich Beklagter war (EPG-BerG Hefei/Grundfos)."],
                       abwandlung="Hefei verliert in erster Instanz und legt Berufung ein.", titel="Berufung"),
                 ],
                abschnitt="Art. 69 Abs. 4 EPGÜ: Wer Sicherheit schuldet", level=3,
                concepts=["upc_prozesskostensicherheit"], norms=["Art. 69 Abs. 4 EPGÜ", "R. 158.1 VerfO"],
                cases=["upc_coa_hefei_grundfos_sicherheit", "upc_coa_suinno_microsoft_prozesskostensicherheit"], step="step:upc_schema_kosten.2"),
            *fallkette("u08c-3", "Versichert und klein",
                "Syntorr, ein Kleinunternehmen mit Erklärung nach R. 370.8 VerfO, klagt gegen Arthrex. Arthrex beantragt Prozesskostensicherheit. "
                "Syntorr legt eine After-the-event-Versicherung vor, die Arthrex' Kosten im Unterliegensfall deckt.",
                [frage("Muss das Gericht die Versicherung berücksichtigen?", True,
                       ["**Ja!** Zu prüfen ist, ob eine **berechtigte und reale Sorge** besteht, dass eine Kostenentscheidung nicht "
                        "vollstreckt werden kann. Eine Versicherung, die die Kosten des Beklagten deckt, mindert diese Sorge und ist zu "
                        "berücksichtigen (EPG-BerG Syntorr/Arthrex)."],
                       titel="Versicherung zählt"),
                 frage("Worauf kommt es bei der Versicherung an?", 1,
                       ["Entscheidend ist, dass der Beklagte auf die Deckung **tatsächlich zugreifen** kann; dafür zählen Bedingungen, "
                        "Ausschlüsse und Kündbarkeit (EPG-BerG Syntorr/Arthrex)."],
                       optionen=["Auf die Höhe der Prämie", "Darauf, ob Arthrex tatsächlich auf die Deckung zugreifen kann",
                                 "Auf den Sitz des Versicherers"],
                       level=3, titel="Zugriff auf die Deckung"),
                 frage("Befreit der KMU-Status von der Sicherheit?", False,
                       ["**Nein!** KMU-Status und Erklärung nach R. 370.8 VerfO befreien nicht. Gebührenermäßigung und Sicherheit für die "
                        "Kosten der Gegenseite haben verschiedene Zwecke (EPG-BerG La Siddhi/Athena)."],
                       merke="Versicherung mindert die Sorge, KMU-Status allenfalls die Höhe.", titel="KMU",
                       cases=["upc_coa_lasiddhi_athena_kmu"], concepts=["upc_gerichtsgebuehren"]),
                 frage("Woran orientiert sich die Höhe der Sicherheit?", 1,
                       ["Die Höhe bemisst sich ausgehend von der **Obergrenze der erstattungsfähigen Kosten** nach allen Umständen; der "
                        "KMU-Status kann zu einer niedrigeren Sicherheit führen (EPG-BerG La Siddhi/Athena)."],
                       optionen=["An den schon gezahlten Gerichtsgebühren", "An der Obergrenze der erstattungsfähigen Kosten",
                                 "Am vollen Streitwert"],
                       titel="Höhe", cases=["upc_coa_lasiddhi_athena_kmu"]),
                 ],
                abschnitt="R. 158.1 VerfO: Ermessen und Höhe", level=2,
                concepts=["upc_prozesskostensicherheit"], norms=["Art. 69 Abs. 4 EPGÜ", "R. 158 VerfO", "R. 370.8 VerfO"],
                cases=["upc_coa_syntorr_arthrex_versicherung"], step="step:upc_schema_kosten.2"),
            *fallkette("u08c-4", "Die nicht geleistete Sicherheit",
                "Suinno hat gegen Microsoft verloren und Berufung eingelegt. Das Berufungsgericht ordnet an, dass Suinno binnen sechs Wochen "
                "Sicherheit leistet, mit Hinweis auf die Säumnisfolgen. Suinno zahlt nicht.",
                [frage("Kann gegen Suinno als Berufungsklägerin überhaupt Sicherheit angeordnet werden?", True,
                       ["**Ja!** Sicherheit wird gegen den Antragsteller des jeweiligen Rechtszugs angeordnet, in der Berufung also gegen den "
                        "Berufungskläger (EPG-BerG Hefei/Grundfos)."],
                       titel="Berufungskläger", cases=["upc_coa_hefei_grundfos_sicherheit"]),
                 frage("Kann das Gericht eine Versäumnisentscheidung erlassen?", True,
                       ["**Ja!** Wird die Sicherheit nicht fristgerecht geleistet, kann eine Versäumnisentscheidung nach R. 355 VerfO ergehen "
                        "(R. 158.5 VerfO). Die Anordnung muss diese Folge angekündigt haben (R. 158.4 VerfO)."],
                       titel="Säumnis", norms=["R. 158.5 VerfO"]),
                 frage("Schützt R. 355.2 VerfO Suinno, weil sie ursprünglich Klägerin war?", False,
                       ["**Nein!** Im Berufungsverfahren gilt der **Berufungskläger als Kläger** im Sinne der R. 355 VerfO. R. 355.2 VerfO greift "
                        "nicht, wenn der Berufungsbeklagte die Versäumnisentscheidung gegen ihn beantragt (EPG-BerG Suinno/Microsoft)."],
                       merke="In der Berufung ist der Berufungskläger der Kläger; R. 355.2 VerfO schützt ihn nicht.", level=3,
                       titel="R. 355.2 VerfO", norms=["R. 355 VerfO"]),
                 frage("Wie kann Suinno sich gegen die Versäumnisentscheidung wehren?", 0,
                       ["Mit dem **Einspruch** binnen eines Monats nach Zustellung (R. 356 VerfO, für das Berufungsgericht über R. 357 VerfO). "
                        "Er muss die Säumnis erklären, die Gebühr ist zu zahlen und die versäumte Handlung nachzuholen."],
                       optionen=["Einspruch binnen eines Monats, mit Erklärung und Nachholung", "Vorlage an den EuGH",
                                 "Gar nicht, die Entscheidung ist unanfechtbar"],
                       titel="Einspruch", norms=["R. 356 VerfO"]),
                 ],
                abschnitt="R. 158.5 und 355 VerfO: Folgen der Nichtleistung", level=3,
                concepts=["upc_prozesskostensicherheit", "upc_versaeumnisentscheidung"], norms=["R. 158 VerfO", "Art. 69 Abs. 4 EPGÜ"],
                cases=["upc_coa_suinno_microsoft_versaeumnis"], step="step:upc_schema_kosten.2"),
        ]),
        dict(id="u08d", titel="Art. 8 und 11 EPatVO, R. 12 bis 16 DOEPS, Art. 2 GebOEPS: Jahresgebühren, Lizenzbereitschaft, Register", einheiten=[
            intro("u08d-0", "Eine Gebühr, ein Register, eine Erklärung",
                  "Nach der Eintragung verwaltet das EPA das Einheitspatent zentral (Art. 9 EPatVO). **Jahresgebühren**: eine einzige Gebühr in Euro an das EPA für die Jahre nach dem Jahr des Erteilungshinweises (Art. 11 EPatVO, R. 13 Abs. 1 DOEPS), fällig am letzten Tag des Monats, der dem Anmeldemonat entspricht (R. 13 Abs. 2 DOEPS, wie R. 51 Abs. 1 EPÜ), frühestens drei Monate vorher zahlbar, von jedermann ohne Vertreter. Die Beträge stehen in **Art. 2 Abs. 1 Nr. 1 GebOEPS**: vom 2. Jahr (35 EUR) bis zum 20. Jahr (4 855 EUR), zusammen 35 555 EUR – die Summe der Gebühren der vier 2015 validierungsstärksten Staaten („True Top 4“); in den ersten zehn Jahren weniger als 5 000 EUR. Wer nicht rechtzeitig zahlt, hat eine **Nachfrist von sechs Monaten mit Zuschlag von 50 %** (R. 13 Abs. 3 DOEPS, Art. 2 Abs. 1 Nr. 2 GebOEPS); danach erlischt das Patent rückwirkend zum Fälligkeitstag (R. 14 Abs. 1 lit. b, Abs. 2 DOEPS), Wiedereinsetzung binnen eines Jahres (R. 22 DOEPS). Zwei Sicherheitsfristen: Gebühren, die binnen drei Monaten nach Zustellung der Eintragungsmitteilung fällig werden, sind in dieser Frist ohne Zuschlag zahlbar (R. 13 Abs. 4 DOEPS); Gebühren, die zwischen Erteilungshinweis und Mitteilung fällig geworden wären, werden erst mit der Mitteilung fällig (R. 13 Abs. 5 DOEPS). **Lizenzbereitschaft**: Erklärt der Inhaber gegenüber dem EPA, jedermann die Benutzung gegen angemessene Vergütung zu gestatten (Art. 8 EPatVO, R. 12 DOEPS), ermäßigen sich die Jahresgebühren um **15 %** (Art. 3 GebOEPS); die Lizenz gilt als Vertragslizenz, über die Vergütung entscheidet das EPG (Art. 32 Abs. 1 lit. h EPGÜ). **Register**: Das Register für den einheitlichen Patentschutz ist Teil des Europäischen Patentregisters (R. 15, 16 DOEPS) und nimmt Rechtsübergänge, Lizenzen, dingliche Rechte und Lizenzzusagen auf; Übertragung nur für alle Staaten, Lizenzen auch für Teilgebiete (Art. 3 Abs. 2 EPatVO). Einheitspatente erkennt man am Code „C0“.",
                  concepts=["upc_up_jahresgebuehren", "upc_up_lizenzbereitschaft", "upc_up_register", "upc_up_abteilung"],
                  norms=["Art. 11 EPatVO", "Art. 8 EPatVO", "R. 13 DOEPS", "R. 14 DOEPS", "R. 12 DOEPS", "R. 16 DOEPS", "Art. 2 GebOEPS", "Art. 3 GebOEPS"]),
            *fallkette("u08d-1", "Von Ultimo zu Ultimo",
                "Die europäische Patentanmeldung der G-GmbH wurde am 12. Februar 2021 eingereicht; das Patent ist Einheitspatent. Die "
                "Jahresgebühr für das 6. Jahr (475 EUR) zahlt die G-GmbH nicht rechtzeitig.",
                [frage("Wann wird die Gebühr für das 6. Jahr fällig?", 1,
                       ["Fällig ist sie am **letzten Tag des Monats**, der dem Anmeldemonat entspricht (R. 13 Abs. 2 DOEPS), hier am "
                        "28. Februar 2026."],
                       optionen=["Am 12. Februar 2026", "Am 28. Februar 2026", "Am 31. Dezember 2025"],
                       titel="Fälligkeit", norms=["R. 13 Abs. 2 DOEPS"]),
                 frage("Ist das Patent mit Ablauf des Fälligkeitstags erloschen?", False,
                       ["**Nein!** Es gibt eine **Nachfrist von sechs Monaten** mit einem Zuschlag von 50 % (R. 13 Abs. 3 DOEPS, Art. 2 "
                        "Abs. 1 Nr. 2 GebOEPS), hier 237,50 EUR."],
                       titel="Nachfrist", norms=["R. 13 Abs. 3 DOEPS"]),
                 frage("Ist die Zahlung noch rechtzeitig?", True,
                       ["**Ja!** Die Nachfrist läuft nach der Praxis des EPA „von Ultimo zu Ultimo“: Sie endet am letzten Tag des sechsten "
                        "Monats, hier am **31. August 2026** (UP-Richtlinien 3.11; R. 20 Abs. 2 lit. g DOEPS i.V.m. R. 131 EPÜ)."],
                       abwandlung="Die G-GmbH zahlt Gebühr und Zuschlag am 31. August 2026.", level=3, titel="Ende der Nachfrist"),
                 frage("Erlischt das Patent rückwirkend zum Fälligkeitstag?", True,
                       ["**Ja!** Wird auch in der Nachfrist nicht gezahlt, erlischt das Einheitspatent **rückwirkend** zum Fälligkeitstag, "
                        "hier zum 28. Februar 2026 (R. 14 Abs. 1 lit. b, Abs. 2 DOEPS)."],
                       abwandlung="Die G-GmbH zahlt gar nicht.", titel="Erlöschen", norms=["R. 14 DOEPS"]),
                 frage("Kann die G-GmbH danach noch Wiedereinsetzung beantragen?", True,
                       ["**Ja!** Die Wiedereinsetzung ist binnen zwei Monaten ab Wegfall des Hindernisses zu beantragen, höchstens binnen "
                        "eines Jahres nach Ablauf der versäumten Frist (R. 22 DOEPS)."],
                       titel="Wiedereinsetzung", norms=["R. 22 DOEPS"]),
                 ],
                abschnitt="R. 13 und 14 DOEPS: Jahresgebühren", level=2,
                concepts=["upc_up_jahresgebuehren", "upc_up_rechtsbehelf"], norms=["Art. 2 GebOEPS"],
                step="step:upc_schema_einheitliche_wirkung.5.1"),
            *fallkette("u08d-2", "Lizenzbereitschaft mit Folgen",
                "Die H-AG hat für ihr Einheitspatent eine ausschließliche Lizenz zugunsten der L-GmbH eintragen lassen. Um Jahresgebühren zu "
                "sparen, will sie eine Erklärung der Lizenzbereitschaft abgeben.",
                [frage("Kann die Erklärung eingetragen werden?", False,
                       ["**Nein!** Die Erklärung nach Art. 8 EPatVO ist ausgeschlossen, **solange eine ausschließliche Lizenz** eingetragen "
                        "oder beantragt ist (R. 12 Abs. 3 DOEPS)."],
                       merke="Lizenzbereitschaft und ausschließliche Lizenz schließen sich aus.", titel="Sperre durch Exklusivlizenz"),
                 frage("Um wie viel ermäßigen sich danach die Jahresgebühren?", 0,
                       ["Die Erklärung (Formblatt 7001) wird gebührenfrei eingetragen und ermäßigt die danach fällig werdenden Jahresgebühren "
                        "um **15 %** (Art. 3 GebOEPS)."],
                       optionen=["Um 15 %", "Um 50 %", "Um 25 %"],
                       abwandlung="Die ausschließliche Lizenz wird gelöscht; die H-AG gibt die Erklärung ab.", titel="15 %",
                       norms=["Art. 3 GebOEPS"]),
                 frage("Kann die H-AG danach wieder eine ausschließliche Lizenz eintragen lassen?", False,
                       ["**Nein!** Nach der Erklärung kann keine ausschließliche Lizenz mehr eingetragen werden (R. 12 Abs. 4 DOEPS)."],
                       titel="Keine neue Exklusivlizenz"),
                 frage("Kann die H-AG die Erklärung zurücknehmen?", True,
                       ["**Ja!** Die Rücknahme ist jederzeit möglich, wird aber erst wirksam, wenn der **volle Ermäßigungsbetrag** "
                        "zurückgezahlt ist (R. 12 Abs. 2 DOEPS)."],
                       titel="Rücknahme"),
                 frage("Wer entscheidet über die Vergütung eines Lizenznehmers, wenn man sich nicht einigt?", 1,
                       ["Eine so erworbene Lizenz gilt als Vertragslizenz (Art. 8 Abs. 2 EPatVO). Über die angemessene Vergütung entscheidet "
                        "auf Klage das **EPG** (Art. 32 Abs. 1 lit. h EPGÜ)."],
                       optionen=["Das EPA", "Das EPG", "Ein nationales Gericht"],
                       titel="Vergütung", norms=["Art. 32 Abs. 1 EPGÜ"]),
                 ],
                abschnitt="Art. 8 EPatVO, R. 12 DOEPS: Lizenzbereitschaft", level=2,
                concepts=["upc_up_lizenzbereitschaft", "upc_up_register"], norms=["Art. 8 EPatVO", "R. 12 DOEPS"],
                step="step:upc_schema_einheitliche_wirkung.5.2"),
            *fallkette("u08d-3", "Nur für Deutschland und Österreich",
                "Die I-S.p.A. hält ein Einheitspatent. Sie will es der K-GmbH „für Deutschland und Österreich“ übertragen und für die übrigen "
                "Staaten behalten. Beide beantragen die Eintragung beim EPA.",
                [frage("Kann das EPA die Übertragung nur für Deutschland und Österreich eintragen?", False,
                       ["**Nein!** Das Einheitspatent hat **einheitlichen Charakter**: Es kann nur für alle teilnehmenden Staaten übertragen, "
                        "beschränkt oder für nichtig erklärt werden (Art. 3 Abs. 2 UAbs. 2 EPatVO, R. 16 DOEPS; UP-Richtlinien 7.2)."],
                       merke="Übertragen nur ganz, lizenzieren auch teilweise (Art. 3 Abs. 2 EPatVO).", titel="Keine Teilübertragung"),
                 frage("Kann die I-S.p.A. stattdessen eine Lizenz nur für diese beiden Staaten erteilen?", True,
                       ["**Ja!** Lizenzen sind für die Gesamtheit oder einen **Teil** der Gebiete zulässig (Art. 3 Abs. 2 UAbs. 3 EPatVO) und "
                        "werden auf Antrag eingetragen (R. 20 Abs. 2 lit. b DOEPS i.V.m. R. 23 EPÜ)."],
                       titel="Teillizenz", norms=["R. 20 DOEPS"]),
                 frage("Nach welchem Recht richtet sich das Einheitspatent als Vermögensgegenstand?", 1,
                       ["Einheitlich nach dem Recht des Staates nach **Art. 7 EPatVO**, hier nach italienischem Recht, wenn die I-S.p.A. am "
                        "Anmeldetag ihren Sitz in Italien hatte. Beim Bündelpatent wäre jeder nationale Teil gesondert zu behandeln."],
                       optionen=["Nach dem Recht jedes teilnehmenden Staates gesondert", "Einheitlich nach dem Recht des Staates nach Art. 7 EPatVO",
                                 "Nach deutschem Recht, weil das EPA in München sitzt"],
                       level=3, titel="Anwendbares Recht", norms=["Art. 7 EPatVO"]),
                 ],
                abschnitt="Art. 3 Abs. 2 EPatVO, R. 16 DOEPS: Register", level=1,
                concepts=["upc_up_register", "upc_einheitspatent"], norms=["Art. 3 Abs. 2 EPatVO", "R. 16 DOEPS"],
                step="step:upc_schema_einheitliche_wirkung.5.3"),
        ]),
    ],
)
