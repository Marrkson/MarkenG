# -*- coding: utf-8 -*-
"""Berufung und Rechtsbehelfe vor dem EPG im Jurafuchs-Format: je Kapitel die Kernvorschriften, darin kurze Fallketten mit einer
Frage je Auslegungselement."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

KURS = dict(
    id="u09", gebiet="upc", kompakt="fragen", titel="Berufung und Rechtsbehelfe",
    untertitel="Statthaftigkeit, Frist, Beschwer, aufschiebende Wirkung, neues Vorbringen, Entscheidung und Wiederaufnahme",
    farbe="#6d28d9", icon="pruefungspunkt",
    beschreibung="Der Weg nach Luxemburg: Welche Entscheidungen und Anordnungen des Gerichts erster Instanz frei anfechtbar sind und welche die Zulassung oder die Ermessensüberprüfung brauchen (EOFlow/Insulet), wann die Berufungsfrist beginnt (Belkin/Philips), wer beschwert ist und wie Anschlussberufung und bedingte Berufung funktionieren (Abbott/Sinocare, Emboline/AorticLab), was der Streithelfer darf (Strabag/Swarco), wann die Berufung aufschiebende Wirkung hat (Amycel, Siemens/Hologic, Philips/Belkin), was in der Berufung neu vorgebracht werden darf (Hefei/Grundfos, Meril/Edwards, ICPillar/Arm), wie das Berufungsgericht entscheidet und zurückwirkt (Kodak/Fujifilm) und wann ein rechtskräftiges Verfahren wiederaufgenommen wird (Suinno/Microsoft).",
    kapitel=[
        dict(id="u09a", titel="Art. 73 EPGÜ, R. 220 und 224 VerfO: Statthaftigkeit und Frist", einheiten=[
            schema("u09a-0", "Prüfungsschema: Berufung zum Berufungsgericht", "upc_schema_berufung",
                   "Sechs Stationen: Statthaftigkeit (welche Entscheidung oder Anordnung, mit oder ohne Zulassung), Frist und Form, Beschwer mit Anschlussberufung und Streithelfer, aufschiebende Wirkung, Prüfungsumfang mit neuem Vorbringen, Entscheidung des Berufungsgerichts."),
            intro("u09a-1", "Drei Wege zum Berufungsgericht",
                  "Art. 73 EPGÜ unterscheidet **Entscheidungen** und **Anordnungen**. Gegen Endentscheidungen des Gerichts erster Instanz und Entscheidungen, die das Verfahren bezüglich einer Partei beenden, ist die Berufung ohne weiteres statthaft, Frist zwei Monate ab Zustellung (Art. 73 Abs. 1 EPGÜ, R. 220.1 lit. a, b, R. 224.1 lit. a VerfO); die Berufungsbegründung folgt binnen vier Monaten (R. 224.2 lit. a VerfO). Ebenso frei anfechtbar sind die in Art. 73 Abs. 2 lit. a EPGÜ genannten Anordnungen nach Art. 49 Abs. 5, 59 bis 62 und 67 EPGÜ, also Sprachwechsel, Beweisvorlage, Beweissicherung, Arrest, einstweilige Maßnahmen und Auskunft, hier aber binnen **15 Tagen** (R. 220.1 lit. c, R. 224.1 lit. b VerfO). Alle **anderen Anordnungen** – verfahrensleitende Anordnungen, Streitwertfestsetzung, Zwangsgeldfestsetzung, Vertraulichkeitsanordnungen, Entscheidungen nach R. 333 VerfO – sind nur zusammen mit der Berufung gegen die Endentscheidung angreifbar oder wenn das Gericht erster Instanz die Berufung **zulässt** (Art. 73 Abs. 2 lit. b EPGÜ, R. 220.2 VerfO). Verweigert es die Zulassung binnen 15 Tagen, kann binnen weiterer 15 Kalendertage beim Berufungsgericht der Antrag auf **Ermessensüberprüfung** (discretionary review) gestellt werden, über den der ständige Richter entscheidet und den er ohne Begründung abweisen kann (R. 220.3, 220.4 VerfO). Die Berufung kann auf rechtliche und tatsächliche Gesichtspunkte gestützt werden (Art. 73 Abs. 3 EPGÜ), neue Tatsachen und Beweismittel aber nur unter den Voraussetzungen des Art. 73 Abs. 4 EPGÜ und der R. 222.2 VerfO. Für jedes Berufungsverfahren ist die Gebühr zu zahlen (R. 228, R. 370.5 VerfO).",
                  concepts=["upc_berufung", "upc_ermessensueberpruefung", "upc_berufungsfrist"], norms=["Art. 73 Abs. 1 EPGÜ", "Art. 73 Abs. 2 EPGÜ", "R. 220 VerfO", "R. 224 VerfO"],
                  distinctions=["d_upc_berufung_entscheidung_anordnung"]),
            *fallkette("u09a-2", "Drei Anordnungen, ein Urteil",
                "Im Verletzungsstreit A gegen B erlässt die Lokalkammer nacheinander: eine einstweilige Maßnahme nach Art. 62 EPGÜ, die "
                "Ablehnung einer Fristverlängerung durch den Berichterstatter und schließlich die Endentscheidung.",
                [frage("Kann B die Endentscheidung ohne Zulassung anfechten?", True,
                       ["**Ja!** Gegen Endentscheidungen ist die Berufung ohne Weiteres statthaft, binnen **zwei Monaten** ab Zustellung "
                        "(Art. 73 Abs. 1 EPGÜ, R. 220.1 lit. a, R. 224.1 lit. a VerfO). Die Begründung folgt binnen vier Monaten "
                        "(R. 224.2 lit. a VerfO)."],
                       titel="Endentscheidung", step="step:upc_schema_berufung.1.1"),
                 frage("Ist auch die einstweilige Maßnahme ohne Zulassung anfechtbar?", True,
                       ["**Ja!** Anordnungen nach Art. 62 EPGÜ gehören zu den frei anfechtbaren Anordnungen (Art. 73 Abs. 2 lit. a EPGÜ, "
                        "R. 220.1 lit. c VerfO), hier aber binnen **15 Tagen** (R. 224.1 lit. b VerfO). Das Ausgangsverfahren läuft weiter "
                        "(Art. 74 Abs. 3 EPGÜ)."],
                       titel="Einstweilige Maßnahme"),
                 frage("Welche Anordnungen sind nach Art. 73 Abs. 2 lit. a EPGÜ zulassungsfrei anfechtbar?", 0,
                       ["Zulassungsfrei sind nur die Anordnungen nach **Art. 49 Abs. 5, 59 bis 62 und 67 EPGÜ**: Sprachwechsel, "
                        "Beweisvorlage, Beweissicherung, Arrest, einstweilige Maßnahmen und Auskunft. Alle anderen Anordnungen brauchen die "
                        "Zulassung oder die Ermessensüberprüfung (R. 220.2, 220.3 VerfO)."],
                       optionen=["Anordnungen nach Art. 49 Abs. 5, 59 bis 62 und 67 EPGÜ", "Alle Anordnungen eines Spruchkörpers",
                                 "Nur Anordnungen mit Zwangsgeld"],
                       merke="Frei anfechtbar: Endentscheidung und Anordnungen nach Art. 49 Abs. 5, 59 bis 62, 67 EPGÜ.", titel="Katalog"),
                 frage("Kann B gegen die abgelehnte Fristverlängerung sofort Berufung einlegen?", False,
                       ["**Nein!** Gegen eine verfahrensleitende Anordnung des Berichterstatters ist zuerst die Überprüfung durch den "
                        "Spruchkörper zu beantragen (R. 333 VerfO). Erst dessen Entscheidung ist mit Zulassung oder nach Ermessensüberprüfung "
                        "anfechtbar (R. 220.3 Satz 1 VerfO)."],
                       level=3, titel="Verfahrensleitende Anordnung", norms=["R. 333 VerfO"]),
                 ],
                abschnitt="Art. 73 Abs. 1 und 2 EPGÜ: Was anfechtbar ist", level=2,
                concepts=["upc_berufung", "upc_ermessensueberpruefung"], norms=["Art. 73 Abs. 2 EPGÜ", "R. 220.1 VerfO", "R. 220.2 VerfO"],
                cases=["upc_coa_eoflow_insulet_zwangsgeld_berufung", "upc_coa_kodak_fujifilm_aufhebung_zwangsgeld"], step="step:upc_schema_berufung.1.2"),
            *fallkette("u09a-3", "Berufung gegen das Zwangsgeld",
                "Die Lokalkammer setzt gegen EOFlow wegen Verstoßes gegen eine einstweilige Maßnahme ein Zwangsgeld fest und lässt die "
                "Berufung nicht zu. EOFlow legt Berufung ein und beantragt hilfsweise die Ermessensüberprüfung.",
                [frage("Ist die Berufung ohne Zulassung statthaft?", False,
                       ["**Nein!** Die Zwangsgeldfestsetzung nach Art. 82 Abs. 4 EPGÜ, R. 354.4 VerfO ist keine Anordnung nach Art. 73 "
                        "Abs. 2 lit. a EPGÜ, auch wenn sie eine einstweilige Maßnahme durchsetzt. Sie ist nur mit Zulassung oder nach "
                        "Ermessensüberprüfung anfechtbar (EPG-BerG EOFlow/Insulet)."],
                       merke="Vollstreckung ist nicht Eilverfahren: Zwangsgeld nur mit Zulassung oder Ermessensüberprüfung.",
                       titel="Keine freie Berufung", norms=["R. 354.4 VerfO"], concepts=["upc_zwangsgeld"]),
                 frage("Binnen welcher Frist ist die Ermessensüberprüfung zu beantragen?", 0,
                       ["Lässt das Gericht erster Instanz die Berufung nicht binnen 15 Tagen zu, kann **binnen 15 Kalendertagen** nach Ende "
                        "dieses Zeitraums die Ermessensüberprüfung beim Berufungsgericht beantragt werden (R. 220.3 VerfO)."],
                       optionen=["15 Kalendertage nach Ablauf der 15-tägigen Zulassungsfrist", "Zwei Monate ab Zustellung",
                                 "Ein Monat ab Zustellung"],
                       titel="Frist", norms=["R. 220.3 VerfO"]),
                 frage("Ist der Antrag auf Ermessensüberprüfung gebührenpflichtig?", True,
                       ["**Ja!** Der Antrag muss die Angaben nach R. 221.2 VerfO enthalten und kostet eine Gebühr (R. 370.5 lit. d VerfO)."],
                       titel="Gebühr"),
                 frage("Muss der ständige Richter eine Ablehnung begründen?", False,
                       ["**Nein!** Der ständige Richter kann den Antrag **ohne Angabe von Gründen** abweisen (R. 220.4 VerfO)."],
                       titel="Keine Begründung nötig", norms=["R. 220.4 VerfO"]),
                 frage("Wer entscheidet nach der Zulassung über die Berufung?", 1,
                       ["Gibt der ständige Richter dem Antrag statt, weist der Präsident des Berufungsgerichts die Überprüfung einem "
                        "**Spruchkörper** des Berufungsgerichts zu (R. 220.4 VerfO)."],
                       optionen=["Der ständige Richter allein", "Ein Spruchkörper des Berufungsgerichts", "Die Lokalkammer"],
                       abwandlung="Der ständige Richter gibt dem Antrag nach Anhörung von Insulet statt.", titel="Spruchkörper"),
                 ],
                abschnitt="R. 220.2 bis 220.4 VerfO: Zulassung und Ermessensüberprüfung", level=2,
                concepts=["upc_ermessensueberpruefung", "upc_berufung"], norms=["Art. 73 Abs. 2 EPGÜ"],
                cases=["upc_coa_eoflow_insulet_zwangsgeld_berufung"], step="step:upc_schema_berufung.1.3"),
            *fallkette("u09a-4", "Tenor heute, Gründe später",
                "Die Lokalkammer verkündet am 2. Februar nur den Tenor: Belkin wird zur Unterlassung verurteilt. Die Entscheidung mit Gründen "
                "wird am 20. März zugestellt. Belkin legt am 15. Mai Berufung ein.",
                [frage("Darf das Gericht den Tenor vor den Gründen verkünden?", True,
                       ["**Ja!** Das Gericht kann seine Entscheidung unmittelbar nach der mündlichen Verhandlung verkünden und die Begründung "
                        "nachreichen (R. 118.7 VerfO)."],
                       titel="Tenor vor Gründen", norms=["R. 118.7 VerfO"]),
                 frage("Beginnt die Berufungsfrist mit der Verkündung des Tenors?", False,
                       ["**Nein!** Die Frist beginnt erst, wenn die **Entscheidung mit Gründen** zugestellt ist (EPG-BerG Belkin/Philips 2026, "
                        "im Anschluss an Ballino/Kinexon). Nur die Gründe zeigen, ob und womit die Berufung begründet werden kann."],
                       merke="Die Berufungsfrist läuft ab Zustellung der begründeten Entscheidung.", titel="Fristbeginn"),
                 frage("Ist die Berufung vom 15. Mai rechtzeitig?", True,
                       ["**Ja!** Die Zweimonatsfrist (Art. 73 Abs. 1 EPGÜ, R. 224.1 lit. a VerfO) lief ab dem 20. März und endete am 20. Mai "
                        "(R. 300 VerfO)."],
                       titel="Rechtzeitig"),
                 frage("Bis wann muss Belkin die Berufung begründen?", 0,
                       ["Die Berufungsbegründung ist binnen **vier Monaten** ab Zustellung der Entscheidung einzureichen (R. 224.2 lit. a "
                        "VerfO), hier also bis zum 20. Juli."],
                       optionen=["Binnen vier Monaten ab Zustellung", "Zusammen mit der Berufungsschrift", "Binnen sechs Wochen"],
                       titel="Begründungsfrist"),
                 frage("Wird die Begründungsfrist verlängert?", False,
                       ["**Nein!** Fristverlängerungen nach R. 9.3 lit. a VerfO gibt es angesichts des strengen Fristenregimes nur bei "
                        "außergewöhnlichen Umständen. Die Angleichung an ein Parallelverfahren ist keiner, wenn das Berufungsgericht beide "
                        "Verfahren nach R. 220.5 VerfO gemeinsam verhandeln kann (EPG-BerG bioMérieux/Labrador)."],
                       abwandlung="Belkin beantragt, die Begründungsfrist an die spätere Frist in einem parallelen Verfahren anzugleichen.",
                       level=3, titel="Keine Angleichung", cases=["upc_coa_biomerieux_labrador_fristen"], norms=["R. 9.3 VerfO"]),
                 ],
                abschnitt="R. 224 VerfO: Frist", level=2,
                concepts=["upc_berufungsfrist", "upc_fristen"], norms=["Art. 73 Abs. 1 EPGÜ", "R. 224.1 VerfO"],
                cases=["upc_coa_belkin_philips_berufungsfrist"], step="step:upc_schema_berufung.2"),
        ]),
        dict(id="u09b", titel="Art. 73 Abs. 1 EPGÜ, R. 237 und 313 VerfO: Beschwer, Anschlussberufung, Streithelfer", einheiten=[
            intro("u09b-0", "Wer darf, und wie: Beschwer und Anschluss",
                  "Berufung kann nur einlegen, wer mit seinen Anträgen ganz oder teilweise **unterlegen** ist (Art. 73 Abs. 1 EPGÜ), in der Sprache der VerfO die „beschwerte Partei“ (R. 220.1 VerfO). Wer die Berufungsfrist versäumt hat, kann sich mit der **Anschlussberufung** anschließen, wenn eine andere Partei Berufung eingelegt hat; sie muss in der Berufungserwiderung enthalten sein, den Anforderungen der R. 225, 226 VerfO genügen und ist gebührenpflichtig (R. 237.1 bis 237.4 VerfO). Wird die Berufung zurückgenommen, gilt auch die Anschlussberufung als zurückgenommen (R. 237.5 VerfO). Auch die Anschlussberufung setzt Beschwer voraus: Wer gewonnen hat und nur die Begründung ändern will, ist nicht beschwert (EPG-BerG Abbott/Sinocare). Eine Besonderheit ist die **bedingte Widerklage**: Der Beklagte darf seine Widerklage auf Nichtigerklärung unter die Bedingung stellen, dass die Verletzung festgestellt wird; weist das Gericht die Verletzungsklage ab und bescheidet die Widerklage deshalb nicht, ist der Widerkläger beschwert, sobald der Kläger Berufung einlegt, und kann seine Berufung unter der Bedingung einlegen, dass der Kläger Berufung einlegt (Emboline/AorticLab). Weil Verletzungsklage und Widerklage getrennte Klagen sind, braucht es dafür eine gesonderte Berufung und keine Anschlussberufung (AorticLab/Emboline). Der **Streithelfer** (R. 313 ff. VerfO) hat keine eigenständige Stellung: Seine Prozesshandlungen sind nur zulässig, soweit sie die Anträge der unterstützten Partei unterstützen (Strabag/Swarco). Die Rüge der internationalen Zuständigkeit ist in der Berufung verloren, wenn sie in erster Instanz unterblieben ist (Art. 26 Abs. 1 Brüssel-Ia-VO, R. 19.7 VerfO; Sinocare/Abbott).",
                  concepts=["upc_beschwer", "upc_streithilfe", "upc_widerklage_nichtigkeit"], norms=["Art. 73 Abs. 1 EPGÜ", "R. 220.1 VerfO", "R. 237 VerfO", "R. 313 VerfO"]),
            *fallkette("u09b-1", "Gewonnen, aber mit der falschen Begründung",
                "Die Zentralkammer weist die Nichtigkeitsklage von Sinocare gegen Abbotts Patent ab. Sinocare legt Berufung ein. Abbott schließt "
                "sich an, um die erfinderische Tätigkeit mit einem anderen Grund bestätigt zu bekommen.",
                [frage("Wer kann Berufung einlegen?", 1,
                       ["Berufung kann nur einlegen, wer mit seinen Anträgen ganz oder teilweise **unterlegen** ist (Art. 73 Abs. 1 EPGÜ), "
                        "also die „beschwerte Partei“ (R. 220.1 VerfO)."],
                       optionen=["Jede Partei des Verfahrens", "Wer mit seinen Anträgen ganz oder teilweise unterlegen ist", "Nur der Kläger"],
                       titel="Beschwerte Partei"),
                 frage("Ergibt sich die Beschwer allein aus dem Tenor?", True,
                       ["**Ja!** Die Beschwer ergibt sich aus dem **Tenor**, nicht aus den Gründen. Abbott hat vollständig obsiegt: Die "
                        "Nichtigkeitsklage wurde abgewiesen (EPG-BerG Abbott/Sinocare)."],
                       merke="Beschwer liegt im Tenor, nicht in den Gründen.", titel="Tenor, nicht Gründe"),
                 frage("Ist Abbotts Anschlussberufung zulässig?", False,
                       ["**Nein!** Auch die Anschlussberufung setzt Beschwer voraus (R. 237 VerfO). Wer nur die Begründung einer für ihn "
                        "günstigen Entscheidung ändern will, ist nicht beschwert (EPG-BerG Abbott/Sinocare)."],
                       titel="Anschlussberufung unzulässig", norms=["R. 237 VerfO"]),
                 frage("Kann Abbott den anderen Grund trotzdem vortragen?", True,
                       ["**Ja!** Als Berufungsbeklagte kann Abbott in der Berufungserwiderung alle Gründe vortragen, die das Ergebnis tragen "
                        "(R. 235, 236 VerfO). Das Berufungsgericht kann die Abweisung mit anderer Begründung bestätigen (R. 222.1 VerfO)."],
                       titel="Vortrag in der Erwiderung"),
                 frage("Was wird aus einer Anschlussberufung, wenn die Berufung zurückgenommen wird?", 2,
                       ["Wird die Berufung zurückgenommen, gilt auch jede Anschlussberufung als zurückgenommen (R. 237.5 VerfO). Die "
                        "Anschlussberufung steht in der Berufungserwiderung und ist gebührenpflichtig wie eine Berufung (R. 237.2, 237.4 VerfO)."],
                       optionen=["Sie wird als selbständige Berufung fortgeführt", "Sie wird an die erste Instanz verwiesen",
                                 "Sie gilt ebenfalls als zurückgenommen"],
                       abwandlung="Angenommen, Abbott wäre beschwert und hätte zulässig angeschlossen. Sinocare nimmt die Berufung zurück.",
                       level=3, titel="Abhängigkeit"),
                 ],
                abschnitt="Art. 73 Abs. 1 EPGÜ, R. 237 VerfO: Beschwer und Anschlussberufung", level=2,
                concepts=["upc_beschwer", "upc_berufung"], norms=["Art. 73 Abs. 1 EPGÜ", "R. 220.1 VerfO"],
                cases=["upc_coa_abbott_sinocare_erfinderisch"], step="step:upc_schema_berufung.3"),
            *fallkette("u09b-2", "Die bedingte Berufung des Widerklägers",
                "Emboline klagt gegen AorticLab; AorticLab erhebt Widerklage auf Nichtigerklärung für den Fall einer Verletzung. Die Lokalkammer "
                "weist die Klage ab und bescheidet die Widerklage nicht. Emboline legt Berufung ein.",
                [frage("Ist AorticLab beschwert, obwohl sie gewonnen hat?", True,
                       ["**Ja!** Der Widerkläger ist beschwert, sobald der Kläger Berufung einlegt: Stellt das Berufungsgericht die Verletzung "
                        "fest, tritt die Bedingung ein, und die unbeschiedene Widerklage muss entschieden werden (EPG-BerG Emboline/AorticLab)."],
                       titel="Beschwer des Widerklägers"),
                 frage("Kann AorticLab ihre Berufung unter die Bedingung stellen, dass Emboline Berufung einlegt?", True,
                       ["**Ja!** Die bedingte Berufung ist zulässig. Die Gebühr wird erst mit Eintritt der Bedingung fällig (EPG-BerG "
                        "Emboline/AorticLab)."],
                       merke="Bedingte Widerklage, bedingte Berufung: gesondert, nicht als Anschluss.", titel="Bedingte Berufung"),
                 frage("Ist die Anschlussberufung der richtige Weg?", False,
                       ["**Nein!** Verletzungsklage und Widerklage sind **getrennte Klagen**; die Bedingung zwischen ihnen ist "
                        "„inter-prozedural“. Deshalb braucht es eine gesonderte Berufung (EPG-BerG AorticLab/Emboline)."],
                       titel="Keine Anschlussberufung"),
                 frage("Bleibt die Widerklage in der Berufung bedingt?", True,
                       ["**Ja!** Sie bleibt bedingt, sofern die Bedingung nicht nach R. 263 VerfO analog und R. 222.2 VerfO fallengelassen "
                        "wird (EPG-BerG Emboline/AorticLab)."],
                       level=3, titel="Bedingung bleibt"),
                 ],
                abschnitt="R. 220.1 VerfO: bedingte Berufung", level=3,
                concepts=["upc_beschwer", "upc_widerklage_nichtigkeit"], norms=["R. 220.1 VerfO", "R. 237 VerfO", "Art. 33 Abs. 3 EPGÜ", "R. 242.2 VerfO"],
                cases=["upc_coa_emboline_aorticlab_bedingte_widerklage", "upc_coa_aorticlab_emboline_getrennte_klagen"], step="step:upc_schema_berufung.3"),
            *fallkette("u09b-3", "Der Streithelfer will weiterkämpfen",
                "Swarco ist dem Verletzungsstreit von Strabag gegen eine Zulieferin als Streithelferin der Beklagten beigetreten. Beide legen "
                "Berufung ein. Die Beklagte vergleicht sich mit Strabag und nimmt ihre Berufung zurück.",
                [frage("Ist Swarco an die Prozesshandlungen der Beklagten gebunden?", True,
                       ["**Ja!** Der Streithelfer unterstützt eine Partei (R. 313 VerfO). Seine Prozesshandlungen sind nur zulässig, soweit "
                        "sie deren Anträge unterstützen; er darf sich nicht in Widerspruch zu ihr setzen (EPG-BerG Strabag/Swarco)."],
                       titel="Kein Widerspruch"),
                 frage("Kann Swarco ihre eigene Berufung fortführen?", False,
                       ["**Nein!** Berufungen von Partei und Streithelfer bilden ein **einheitliches Rechtsmittel**. Mit der Rücknahme durch die "
                        "Partei wird es gegenstandslos und ist nach R. 360 VerfO erledigt (EPG-BerG Strabag/Swarco)."],
                       merke="Der Streithelfer folgt der Partei.", titel="Einheitliches Rechtsmittel", norms=["R. 360 VerfO"]),
                 frage("Wird der Streithelfer bei den Kosten wie die Hauptpartei behandelt?", True,
                       ["**Ja!** Kostenrechtlich steht der Streithelfer der Hauptpartei gleich und trägt seine Kosten der erledigten Berufung "
                        "nach den für die Partei geltenden Regeln (EPG-BerG Strabag/Swarco)."],
                       titel="Kosten", concepts=["upc_kostenerstattung"]),
                 frage("Wie kann Swarco das Patent dennoch angreifen?", 0,
                       ["Swarco bleibt die eigene **Nichtigkeitsklage** vor der Zentralkammer (Art. 47 Abs. 6 EPGÜ). Eine eigenständige "
                        "Fortführung der Streithilfe kennt die VerfO nicht, anders als § 69 ZPO."],
                       optionen=["Mit einer eigenen Nichtigkeitsklage", "Mit einem Antrag auf Wiederaufnahme", "Mit einer Anschlussberufung"],
                       titel="Eigene Klage", norms=["Art. 47 Abs. 6 EPGÜ"]),
                 ],
                abschnitt="R. 313 VerfO: Streithelfer", level=2,
                concepts=["upc_streithilfe", "upc_ruecknahme"], norms=["R. 313 VerfO", "R. 265 VerfO"],
                cases=["upc_coa_strabag_swarco_streithilfe"], step="step:upc_schema_berufung.3"),
        ]),
        dict(id="u09c", titel="Art. 74, 75 und 81 EPGÜ, R. 222 und 223 VerfO: aufschiebende Wirkung, neues Vorbringen, Entscheidung, Wiederaufnahme", einheiten=[
            intro("u09c-0", "Was die Berufung bewirkt und was das Berufungsgericht tut",
                  "Die Berufung hat **keine aufschiebende Wirkung**; erstinstanzliche Entscheidungen sind trotz Berufung vollstreckbar (Art. 74 Abs. 1 EPGÜ, R. 354.1 VerfO). Ausnahmen: Entscheidungen über Nichtigkeitsklagen und Widerklagen auf Nichtigerklärung sowie über Klagen gegen Entscheidungen des EPA haben stets aufschiebende Wirkung (Art. 74 Abs. 2 EPGÜ), und das Berufungsgericht kann sie auf begründeten Antrag anordnen (Art. 74 Abs. 1 EPGÜ, R. 223 VerfO). Dafür verlangt es außergewöhnliche Umstände, etwa einen offensichtlichen Fehler oder einen unverhältnismäßigen, nicht wiedergutzumachenden Schaden; ein Verstoß gegen das rechtliche Gehör kann ein solcher Umstand sein (Siemens/Hologic). Der Antrag muss vollständig sein (Amycel). Gegenstand des Berufungsverfahrens sind die Anträge, Tatsachen, Beweismittel und Rechtsausführungen der Parteien (R. 222.1 VerfO); **neues Vorbringen** kann das Berufungsgericht außer Acht lassen, wobei es prüft, ob es in erster Instanz vernünftigerweise nicht möglich war, wie erheblich es ist und wie die Gegenseite dazu steht (R. 222.2 VerfO; Hefei/Grundfos, Onward/Niche). Das Berufungsgericht weist die Berufung zurück oder hebt die Entscheidung ganz oder teilweise auf und **ersetzt sie durch eine eigene**, auch zu den Kosten beider Instanzen (Art. 75 Abs. 1 EPGÜ, R. 242.1 VerfO); es kann alle Befugnisse des Gerichts erster Instanz ausüben und verweist nur in Ausnahmefällen zurück (R. 242.2, R. 243 VerfO). Die Aufhebung wirkt in der Regel **zurück**: Die erstinstanzliche Anordnung gilt als nie wirksam gewesen, festgesetzte Zwangsgelder verlieren ihre Grundlage (Kodak/Fujifilm 2026). Gegen die rechtskräftige Entscheidung bleibt nur die **Wiederaufnahme** nach Art. 81 EPGÜ, R. 245 ff. VerfO: bei einer entscheidenden neuen Tatsache, die auf einer strafbaren Handlung beruht, oder bei einem grundlegenden Verfahrensfehler, binnen zehn Jahren ab Entscheidung und zwei Monaten ab Entdeckung.",
                  concepts=["upc_aufschiebende_wirkung", "upc_neues_vorbringen_berufung", "upc_wiederaufnahme"], norms=["Art. 74 EPGÜ", "R. 222.2 VerfO", "Art. 75 Abs. 1 EPGÜ", "Art. 81 EPGÜ"],
                  cases=["upc_coa_kodak_fujifilm_aufhebung_zwangsgeld", "upc_coa_siemens_hologic_gehoer"]),
            *fallkette("u09c-1", "Der nachgeschobene Antrag",
                "Amycel wird zur Unterlassung verurteilt und legt Berufung ein. Ihr Antrag auf aufschiebende Wirkung, knapp begründet mit "
                "Umsatzeinbußen, wird zurückgewiesen. Zwei Wochen später stellt sie einen zweiten Antrag mit Argumenten, die sie schon kannte.",
                [frage("Bleibt das Unterlassungsurteil trotz der Berufung vollstreckbar?", True,
                       ["**Ja!** Die Berufung hat keine aufschiebende Wirkung, außer das Berufungsgericht beschließt sie auf begründeten "
                        "Antrag (Art. 74 Abs. 1 EPGÜ). Das Übereinkommen will die sofortige Vollstreckbarkeit."],
                       titel="Grundsatz"),
                 frage("Ist der zweite Antrag zulässig?", False,
                       ["**Nein!** Auch der Antrag auf aufschiebende Wirkung muss **vollständig** sein (R. 223.2 VerfO, front-loaded). Ein "
                        "weiterer Antrag ist nur zulässig, wenn er sich auf Vorbringen stützt, das im ersten vernünftigerweise nicht möglich "
                        "war (EPG-BerG Amycel)."],
                       merke="Der Antrag auf aufschiebende Wirkung hat nur einen Schuss.", titel="Kein zweiter Antrag"),
                 frage("Genügen drohende Umsatzeinbußen als außergewöhnlicher Umstand?", False,
                       ["**Nein!** Nötig sind **außergewöhnliche Umstände**, etwa ein offensichtlicher Fehler oder ein unverhältnismäßiger, "
                        "nicht wiedergutzumachender Schaden. Umsatzeinbußen gleicht der Ersatzanspruch nach R. 354.2 VerfO aus."],
                       titel="Umsatzeinbußen"),
                 frage("Kann eine Verletzung des rechtlichen Gehörs genügen?", True,
                       ["**Ja!** Eine Verletzung des rechtlichen Gehörs nach Art. 76 Abs. 2 EPGÜ kann ein außergewöhnlicher Umstand sein "
                        "(EPG-BerG Siemens/Hologic)."],
                       level=3, titel="Rechtliches Gehör", cases=["upc_coa_siemens_hologic_gehoer"], norms=["Art. 76 Abs. 2 EPGÜ"]),
                 frage("Wer entscheidet in Fällen äußerster Dringlichkeit?", 0,
                       ["In Fällen äußerster Dringlichkeit kann der Antrag jederzeit formlos beim **ständigen Richter** gestellt werden, der "
                        "alle Befugnisse des Berufungsgerichts hat (R. 223.4 VerfO)."],
                       optionen=["Der ständige Richter", "Die Lokalkammer", "Der Präsident des Gerichts erster Instanz"],
                       titel="Äußerste Dringlichkeit"),
                 ],
                abschnitt="Art. 74 EPGÜ, R. 223 VerfO: aufschiebende Wirkung", level=2,
                concepts=["upc_aufschiebende_wirkung", "upc_front_loaded"], norms=["Art. 74 Abs. 1 EPGÜ", "R. 223 VerfO"],
                cases=["upc_coa_amycel_aufschiebend"], step="step:upc_schema_berufung.4"),
            *fallkette("u09c-4", "Die Geschäftsführer im Tenor",
                "Die Lokalkammer verurteilt Belkin-Gesellschaften und ihre Geschäftsführer zur Unterlassung; die Geschäftsführer haften danach "
                "als Mittelspersonen. Belkin legt Berufung ein und beantragt aufschiebende Wirkung.",
                [frage("Muss der Antrag aus sich heraus eine Entscheidung erlauben?", True,
                       ["**Ja!** Der Antrag muss Gründe, Tatsachen, Beweismittel und Rechtsausführungen enthalten (R. 223.2 VerfO) und aus "
                        "sich heraus eine Entscheidung erlauben. Verweise sind nur zulässig, wenn die Textstellen konkret bezeichnet sind "
                        "(EPG-BerG Philips/Belkin)."],
                       titel="Inhalt des Antrags"),
                 frage("Wann ordnet das Berufungsgericht aufschiebende Wirkung regelmäßig an?", 1,
                       ["Wenn die angefochtene Entscheidung **evident fehlerhaft** ist: wenn ihre tragenden Feststellungen oder Erwägungen "
                        "schon bei summarischer Prüfung nicht halten (EPG-BerG Philips/Belkin)."],
                       optionen=["Wenn die Berufung möglicherweise Erfolg hat",
                                 "Wenn die tragenden Erwägungen schon bei summarischer Prüfung nicht halten",
                                 "Immer, wenn der Berufungskläger Sicherheit anbietet"],
                       titel="Evidenter Fehler"),
                 frage("Kommt es darauf an, ob das Urteil aus anderen Gründen richtig sein könnte?", False,
                       ["**Nein!** Halten die tragenden Gründe nicht, ist die aufschiebende Wirkung in der Regel anzuordnen, auch wenn sich "
                        "das Urteil mit anderen Feststellungen oder Erwägungen als richtig erweisen könnte (EPG-BerG Philips/Belkin)."],
                       level=3, titel="Andere Gründe"),
                 frage("Haftet ein Geschäftsführer schon wegen seiner Funktion als Mittelsperson?", False,
                       ["**Nein!** Der Geschäftsführer vertritt das Unternehmen; es ist ihm gegenüber nicht „Dritter“ im Sinne von Art. 63 "
                        "EPGÜ. Die Verurteilung als Mittelsperson war insoweit evident fehlerhaft; für die Geschäftsführer wurde die "
                        "aufschiebende Wirkung angeordnet (EPG-BerG Philips/Belkin)."],
                       titel="Geschäftsführer", norms=["Art. 63 Abs. 1 EPGÜ"], concepts=["upc_verletzer"]),
                 frage("Wann ist eine Sicherheit nach R. 352.1 VerfO anzuordnen?", 0,
                       ["Die Sicherheitsleistung für die Vollstreckung ist **mit Erlass der Entscheidung** oder Anordnung anzuordnen "
                        "(R. 352.1 VerfO; EPG-BerG Philips/Belkin)."],
                       optionen=["Mit Erlass der Entscheidung", "Erst im Vollstreckungsverfahren", "Erst nach Einlegung der Berufung"],
                       level=3, titel="Vollstreckungssicherheit", norms=["R. 352 VerfO"]),
                 ],
                abschnitt="Art. 74 EPGÜ, R. 223 VerfO: aufschiebende Wirkung", level=2,
                concepts=["upc_aufschiebende_wirkung"], norms=["Art. 74 Abs. 1 EPGÜ", "R. 223 VerfO"],
                cases=["upc_coa_philips_belkin_aufschiebend"], step="step:upc_schema_berufung.4"),
            *fallkette("u09c-2", "Alte Druckschrift, neue Lehre",
                "In der Berufung stützt Hefei die fehlende erfinderische Tätigkeit auf die Druckschrift D3. In erster Instanz diente D3 nur als "
                "Beleg für das Fachwissen; nun leitet Hefei aus einer Zeichnung erstmals ein Konstruktionsdetail her.",
                [frage("Ist die Konkretisierung eines schon schlüssigen Vortrags „neu“?", False,
                       ["**Nein!** Ob Vorbringen neu im Sinne der R. 222.2 VerfO ist, hängt davon ab, wie allgemein es in erster Instanz war. "
                        "Die Konkretisierung eines bereits schlüssigen Vortrags ist nicht neu (EPG-BerG Hefei/Grundfos)."],
                       titel="Konkretisierung"),
                 frage("Ist die Herleitung des Details aus D3 neu, obwohl D3 schon in der Akte war?", True,
                       ["**Ja!** Die **erstmalige Herleitung konkreter technischer Informationen** aus einer bereits vorgelegten Druckschrift "
                        "ist neuer Vortrag (EPG-BerG Hefei/Grundfos). Das Berufungsgericht kann ihn außer Acht lassen."],
                       merke="Verdeutlichen ist erlaubt; eine neue Lehre aus alter Schrift ist neu (Hefei/Grundfos).", titel="Neue Lehre"),
                 frage("Was berücksichtigt das Berufungsgericht bei seinem Ermessen?", 0,
                       ["Nach R. 222.2 lit. a bis c VerfO zählt, ob das Vorbringen in erster Instanz vernünftigerweise nicht möglich war, wie "
                        "erheblich es ist und wie die Gegenseite dazu steht. Dasselbe gilt für neue Hilfsanträge (Onward/Niche)."],
                       optionen=["Frühere Möglichkeit, Erheblichkeit und Haltung der Gegenseite", "Nur die Erheblichkeit",
                                 "Nur die Zustimmung der Gegenseite"],
                       titel="Ermessenskriterien", cases=["upc_coa_onward_niche_mittelbar"]),
                 frage("Kann Hefei die Rüge noch erheben?", False,
                       ["**Nein!** Wer die Zuständigkeit in erster Instanz nicht mit dem Einspruch nach R. 19 VerfO rügt, hat sich rügelos "
                        "eingelassen (Art. 26 Abs. 1 Brüssel-Ia-VO, R. 19.7 VerfO). In der Berufung ist die Rüge verloren (EPG-BerG "
                        "Sinocare/Abbott)."],
                       abwandlung="Hefei rügt erstmals in der Berufung die internationale Zuständigkeit des EPG.", level=3,
                       titel="Zuständigkeitsrüge", cases=["upc_coa_sinocare_abbott_zustaendigkeit"], concepts=["upc_einlassung"],
                       norms=["R. 19.7 VerfO"]),
                 ],
                abschnitt="R. 222 VerfO: neues Vorbringen", level=3,
                concepts=["upc_neues_vorbringen_berufung", "upc_front_loaded"], norms=["R. 222.2 VerfO", "Art. 73 Abs. 4 EPGÜ", "R. 226 VerfO"],
                cases=["upc_coa_hefei_grundfos_neues_vorbringen"], step="step:upc_schema_berufung.5"),
            *fallkette("u09c-5", "Neues Argument, neues Dokument",
                "In der Berufung trägt Meril ein rechtliches Argument vor, das sie in erster Instanz nicht gebracht hat. Es stützt sich nur auf "
                "Tatsachen und Beweismittel aus der ersten Instanz.",
                [frage("Kann das Berufungsgericht das Argument nach R. 222.2 VerfO außer Acht lassen?", False,
                       ["**Nein!** R. 222.2 VerfO erfasst nur „Anträge, Tatsachen und Beweismittel“, nicht rechtliche Ausführungen. Ein neues "
                        "Rechtsargument auf Grundlage des erstinstanzlichen Tatsachenstoffs ist zulässig (EPG-BerG Meril/Edwards 2024)."],
                       merke="R. 222.2 VerfO sperrt neue Tatsachen, keine neuen Rechtsargumente.", titel="Rechtsargumente frei"),
                 frage("Muss das Berufungsgericht das Dokument berücksichtigen, weil Edwards nicht widerspricht?", False,
                       ["**Nein!** Das Berufungsgericht prüft **von Amts wegen**, wie es sein Ermessen nach R. 222.2 VerfO ausübt. Es kann "
                        "verspätete Tatsachen und Beweismittel auch ohne Widerspruch der Gegenseite außer Acht lassen (EPG-BerG ICPillar/Arm)."],
                       abwandlung="Meril legt zusätzlich ein Dokument vor, das sie schon in erster Instanz hatte. Edwards erhebt keine Einwände.",
                       titel="Ermessen von Amts wegen", cases=["upc_coa_icpillar_arm_neues_vorbringen"]),
                 frage("Musste Meril das Dokument schon in erster Instanz vorlegen?", True,
                       ["**Ja!** Aus R. 172.1 VerfO folgt die Pflicht, verfügbare Beweismittel vorzulegen. Ob das Gericht selbst die Vorlage "
                        "anordnet, steht dagegen in seinem Ermessen (R. 172.2 VerfO; EPG-BerG ICPillar/Arm)."],
                       level=3, titel="Vorlagepflicht", cases=["upc_coa_icpillar_arm_neues_vorbringen"], norms=["R. 172 VerfO"],
                       concepts=["upc_beweismittel_beweislast"]),
                 ],
                abschnitt="R. 222 VerfO: neues Vorbringen", level=2,
                concepts=["upc_neues_vorbringen_berufung"], norms=["R. 222 VerfO"],
                cases=["upc_coa_meril_edwards_rechtsargument"], step="step:upc_schema_berufung.5"),
            *fallkette("u09c-3", "Wiederaufnahme nach rechtskräftiger Entscheidung",
                "Das Berufungsgericht hat Suinnos Berufung gegen Microsoft rechtskräftig zurückgewiesen. Suinno beantragt die Wiederaufnahme: "
                "Der Stand der Technik sei falsch gewürdigt, und ein Zeuge habe unvollständig ausgesagt.",
                [frage("Ist die Wiederaufnahme ein außerordentlicher Rechtsbehelf?", True,
                       ["**Ja!** Die Wiederaufnahme nach Art. 81 EPGÜ ist ein **außerordentlicher Rechtsbehelf** gegen rechtskräftige "
                        "Entscheidungen, den das Berufungsgericht nur ausnahmsweise gewährt (EPG-BerG Suinno/Microsoft)."],
                       titel="Außerordentlicher Rechtsbehelf"),
                 frage("Ist die falsche Würdigung des Standes der Technik ein grundlegender Verfahrensfehler?", False,
                       ["**Nein!** Anträge nach Art. 81 Abs. 1 lit. b EPGÜ sind auf die Fehler der R. 247 VerfO beschränkt, etwa fehlerhafte "
                        "Besetzung oder Verletzung des rechtlichen Gehörs. Die Würdigung des Standes der Technik ist ein Angriff auf die "
                        "Sachentscheidung (EPG-BerG Suinno/Microsoft)."],
                       merke="Wiederaufnahme: keine dritte Instanz für die Beweiswürdigung.", titel="Verfahrensfehler", norms=["R. 247 VerfO"]),
                 frage("Rechtfertigt die unvollständige Zeugenaussage die Wiederaufnahme?", False,
                       ["**Nein!** Eine neue Tatsache trägt die Wiederaufnahme nur, wenn sie auf einer Handlung beruht, die ein nationales "
                        "Gericht durch Endentscheidung als **Straftat** qualifiziert hat (Art. 81 Abs. 1 lit. a EPGÜ)."],
                       titel="Neue Tatsache"),
                 frage("Kann Microsoft trotz des Antrags weiter vollstrecken?", True,
                       ["**Ja!** Der Antrag hat keine aufschiebende Wirkung, es sei denn, das Berufungsgericht entscheidet anders (Art. 81 "
                        "Abs. 2 Satz 2 EPGÜ)."],
                       titel="Keine aufschiebende Wirkung"),
                 frage("Bis wann muss der Antrag gestellt werden?", 0,
                       ["Binnen **zehn Jahren** ab der Entscheidung, spätestens **zwei Monate** nach Bekanntwerden der Tatsache oder des "
                        "Verfahrensfehlers (Art. 81 Abs. 2 Satz 1 EPGÜ). Gutgläubige Nutzer des Patents werden geschützt (Art. 81 Abs. 4 EPGÜ)."],
                       optionen=["Zehn Jahre ab Entscheidung, spätestens zwei Monate ab Bekanntwerden", "Ein Monat ab Zustellung",
                                 "Ohne Frist"],
                       titel="Frist"),
                 ],
                abschnitt="Art. 81 EPGÜ: Wiederaufnahme", level=3,
                concepts=["upc_wiederaufnahme", "upc_rechtliches_gehoer"], norms=["Art. 81 Abs. 1 EPGÜ", "Art. 81 Abs. 2 EPGÜ", "R. 245 VerfO"],
                cases=["upc_coa_suinno_microsoft_wiederaufnahme"], step="step:upc_schema_berufung.6"),
        ]),
    ],
)
