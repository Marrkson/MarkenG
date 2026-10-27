# -*- coding: utf-8 -*-
"""Nichtigkeit vor dem EPG im Jurafuchs-Format: je Kapitel die Kernvorschriften, darin kurze Fallketten mit einer Frage je
Auslegungselement (Maßstab, Grenzfall, Abwandlung)."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

KURS = dict(
    id="u06", gebiet="upc", kompakt="fragen", titel="Nichtigkeit, Widerklage und Änderung des Patents", untertitel="Art. 65 EPGÜ, Art. 138 EPÜ, R. 25 bis 30 und 42 bis 50 VerfO",
    farbe="#9d3e6e", icon="loeschung",
    beschreibung="Der Angriff auf den Rechtsbestand vor dem EPG: Nichtigkeitsklage bei der Zentralkammer und Widerklage vor der Lokalkammer, Klagebefugnis (Pari/Philips), Substantiierung und Verteidigung von Unteransprüchen (Fujifilm/Kodak), bedingte Widerklage (Emboline/AorticLab), die Nichtigkeitsgründe des Art. 138 EPÜ in der Rechtsprechung des Berufungsgerichts (expert/Seoul Viosys, Knaus Tabbert, NanoString/10x, Meril/Edwards, Abbott/Sinocare) sowie Änderung des Patents und Erwiderung (Meril/Edwards, VMR/NJOY), Aussetzung bei EPA-Einspruch und aufschiebende Wirkung.",
    kapitel=[
        dict(id="u06a", titel="Art. 47 Abs. 6 und Art. 33 EPGÜ, R. 25 und 29A VerfO: Nichtigkeitsklage und Widerklage", einheiten=[
            schema("u06a-0", "Prüfungsschema: Nichtigkeitsklage und Widerklage auf Nichtigerklärung", "upc_schema_nichtigkeit",
                   "Zwei Wege zum selben Ziel: die selbständige Nichtigkeitsklage bei der Zentralkammer (Art. 33 Abs. 4 EPGÜ, R. 42 ff. VerfO) und die Widerklage auf Nichtigerklärung in der Klageerwiderung vor der Lokal- oder Regionalkammer (R. 25 VerfO), über deren Schicksal die Kammer nach Art. 33 Abs. 3 EPGÜ entscheidet. Anders als im deutschen Recht gibt es keine Einspruchsfrist-Sperre: Die Nichtigkeitsklage ist auch während eines EPA-Einspruchs möglich; das Gericht kann aussetzen (R. 295 lit. a VerfO, Art. 33 Abs. 10 EPGÜ)."),
            *fallkette("u06a-1", "Freedom to operate",
                "Pari entwickelt Inhalationsgeräte und plant ein Produkt, das unter ein Patent von Philips fallen könnte. Philips hat Pari "
                "weder abgemahnt noch verklagt. Pari erhebt Nichtigkeitsklage.",
                [frage("Wer ist nach Art. 47 Abs. 6 EPGÜ zur Nichtigkeitsklage befugt?", 1,
                       ["Klagen kann, wer von dem Patent **betroffen** und nach dem für ihn geltenden nationalen Recht klageberechtigt ist "
                        "(Art. 47 Abs. 6 EPGÜ). Eine Popularklage ist das nicht; eine Abmahnung oder Verletzungsklage verlangt die Vorschrift "
                        "aber auch nicht (ZK Mailand Pari/Philips)."],
                       optionen=["Nur wer vom Patentinhaber abgemahnt oder verklagt wurde",
                                 "Wer von dem Patent betroffen und nach seinem nationalen Recht klageberechtigt ist",
                                 "Jedermann, ohne weitere Voraussetzung"],
                       titel="Wer klagen darf"),
                 frage("Ist Pari „betroffen“, obwohl kein konkreter Konflikt mit Philips besteht?", True,
                       ["**Ja!** Betroffen ist jede Person, die ihre **Freedom to operate** klären will, also jeder, der auf dem technischen "
                        "Gebiet des Patents tätig ist oder werden könnte (ZK Mailand Pari/Philips). Pari arbeitet in der Inhalationstechnik "
                        "und plant ein Produkt im möglichen Schutzbereich."],
                       merke="Betroffen ist, wer auf dem Gebiet des Patents tätig ist oder werden könnte (Pari/Philips).",
                       titel="Betroffenheit"),
                 frage("Genügen Betroffenheit und Klageberechtigung, ohne besonderes Rechtsschutzbedürfnis?", True,
                       ["**Ja!** Neben Betroffenheit und Klageberechtigung nach Art. 47 Abs. 6 EPGÜ verlangt das EPG kein besonderes "
                        "Rechtsschutzbedürfnis; auch eine Abmahnung oder Verletzungsklage ist nicht nötig (ZK Mailand Pari/Philips)."],
                       titel="Kein Rechtsschutzbedürfnis"),
                 frage("Bei welcher Kammer erhebt Pari die Klage?", 1,
                       ["Nichtigkeitsklagen gehören vor die **Zentralkammer** (Art. 33 Abs. 4 EPGÜ). Die Abteilung richtet sich nach der "
                        "IPC-Klasse des Patents (Anhang II EPGÜ, R. 17.3 VerfO). Anders ist es, wenn zwischen denselben Parteien schon eine "
                        "Verletzungsklage bei einer Lokalkammer anhängig ist."],
                       optionen=["Bei der Lokalkammer an ihrem Sitz", "Bei der Zentralkammer, Abteilung nach der IPC-Klasse",
                                 "Beim Berufungsgericht"],
                       titel="Zentralkammer"),
                 ],
                abschnitt="Art. 47 Abs. 6 EPGÜ: Klagebefugnis", level=1,
                concepts=["upc_nichtigkeitsklage", "upc_zentralkammer"], norms=["Art. 47 Abs. 6 EPGÜ", "Art. 33 Abs. 4 EPGÜ", "R. 42 VerfO"],
                cases=["upc_cfi_pari_philips_klagebefugnis"], step="step:upc_schema_nichtigkeit.1.2"),
            *fallkette("u06a-2", "„Alle Ansprüche“",
                "Fujifilm verklagt Kodak vor der Lokalkammer Mannheim aus einem Patent. Kodak erhebt Widerklage auf Nichtigerklärung "
                "„aller Ansprüche“, begründet aber nur den Hauptanspruch 1. Fujifilm verteidigt hilfsweise die Unteransprüche 4 und 7.",
                [frage("Muss Kodak jeden angegriffenen Anspruch einzeln substantiieren?", True,
                       ["**Ja!** Wer die Nichtigerklärung begehrt, muss angeben, in welchem Umfang er die Nichtigerklärung begehrt, und dies **für jeden "
                        "angegriffenen Anspruch** substantiieren (R. 25.1 lit. a bis d, R. 44 VerfO; EPG-BerG Fujifilm/Kodak). Grund ist das "
                        "front-loaded-Verfahren: Der Gegner soll von Anfang an wissen, wogegen er sich verteidigt."],
                       titel="Substantiierung je Anspruch"),
                 frage("Fallen die Unteransprüche schon deshalb, weil Kodak „alle Ansprüche“ angreift?", False,
                       ["**Nein!** Wer pauschal alle Ansprüche angreift, aber nur den Hauptanspruch begründet, bringt die Unteransprüche "
                        "nicht zu Fall. Insoweit ist der Angriff unsubstantiiert (EPG-BerG Fujifilm/Kodak)."],
                       titel="Pauschaler Angriff"),
                 frage("Muss Fujifilm einen Antrag auf Änderung des Patents stellen, um Anspruch 4 zu verteidigen?", False,
                       ["**Nein!** Nach R. 29A lit. c VerfO gibt der Patentinhaber in der Erwiderung substantiiert an, welche Unteransprüche "
                        "er für rechtsbeständig hält. Ein Antrag nach R. 30 VerfO ist nur nötig, wenn der **Wortlaut** der Ansprüche geändert "
                        "werden soll (EPG-BerG Fujifilm/Kodak)."],
                       merke="Unteransprüche verteidigen ja, Hilfsantrag nur bei geändertem Wortlaut (Fujifilm/Kodak).",
                       titel="Verteidigung ohne Hilfsantrag"),
                 frage("Muss Fujifilm die verteidigten Kombinationen ausdrücklich benennen?", True,
                       ["**Ja!** Ergibt sich eine Kombination nicht unmittelbar aus dem Wortlaut der Rückbezüge, muss der Patentinhaber "
                        "sie klar und in der Sprache des Patents benennen. Die Zahl der Kombinationen muss nach dem Gebot des fairen "
                        "Verfahrens **angemessen** sein (EPG-BerG Fujifilm/Kodak)."],
                       abwandlung="Anspruch 7 ist auf „einen der vorhergehenden Ansprüche“ rückbezogen.", titel="Zahl der Kombinationen"),
                 frage("Wann braucht Fujifilm doch einen Antrag auf Änderung des Patents?", 1,
                       ["Ein Änderungsantrag nach R. 30 VerfO ist erforderlich, wenn der Patentinhaber den Wortlaut der erteilten Ansprüche "
                        "ändern oder **Kombinationen vorschlagen** will, die darin nicht ausdrücklich enthalten sind, und so den Schutzbereich "
                        "beschränkt. Wer nur erteilte Unteransprüche und davon umfasste Kombinationen verteidigt, braucht ihn nicht "
                        "(EPG-BerG Fujifilm/Kodak)."],
                       optionen=["Sobald er überhaupt Unteransprüche verteidigt",
                                 "Wenn er den Wortlaut ändert oder nicht enthaltene Kombinationen vorschlägt",
                                 "Nie, Änderungen sind dem EPA vorbehalten"],
                       level=3, titel="Grenze zum Änderungsantrag"),
                 ],
                abschnitt="R. 25 und 29A VerfO: Substantiierung und Unteransprüche", level=2,
                concepts=["upc_nichtigkeitsgruende", "upc_aenderung_patent", "upc_front_loaded"], norms=["R. 25 VerfO", "R. 29A VerfO", "R. 30 VerfO", "R. 44 VerfO"],
                cases=["upc_coa_fujifilm_kodak_nichtigkeit"], step="step:upc_schema_nichtigkeit.1.3"),
            *fallkette("u06a-3", "Widerklage unter Bedingung",
                "Emboline verklagt AorticLab vor einer Lokalkammer wegen Patentverletzung. AorticLab erhebt Widerklage auf Nichtigerklärung "
                "„für den Fall, dass das Gericht eine Verletzung feststellt“.",
                [frage("Darf die Widerklage unter diese Bedingung gestellt werden?", True,
                       ["**Ja!** Eine Widerklage auf Nichtigerklärung darf unter die Bedingung einer Verletzungsfeststellung gestellt werden "
                        "(EPG-BerG Emboline/AorticLab). Der Beklagte kann so vermeiden, dass über den Rechtsbestand entschieden wird, wenn "
                        "die Verletzung ohnehin verneint wird."],
                       merke="Die bedingte Widerklage ist zulässig (Emboline/AorticLab).", titel="Bedingung zulässig"),
                 frage("Ist die Widerklage bis zum Eintritt der Bedingung noch nicht anhängig?", False,
                       ["**Nein!** Verletzungsklage und Widerklage sind **getrennte Klagen**. Die Bedingung verknüpft sie nur "
                        "(„inter-prozedurale“ Bedingung) und lässt die Anhängigkeit der Widerklage unberührt (EPG-BerG AorticLab/Emboline)."],
                       titel="Anhängigkeit"),
                 frage("Kann die Bedingung auch durch das Berufungsgericht eintreten?", True,
                       ["**Ja!** Ohne gegenteilige Angabe meint „das Gericht“ **beide Instanzen** (EPG-BerG AorticLab/Emboline). Die "
                        "Bedingung kann also auch eintreten, wenn erst das Berufungsgericht die Verletzung feststellt."],
                       titel="Beide Instanzen"),
                 frage("Verweist das Berufungsgericht die Widerklage zur Entscheidung an die Lokalkammer zurück?", False,
                       ["**Nein!** Das Berufungsgericht entscheidet die Widerklage in der Regel selbst (Art. 75 Abs. 1 EPGÜ, R. 242.2 lit. b "
                        "VerfO). Dass die erste Instanz eine Frage nicht entschieden hat, ist kein Ausnahmefall, der die Zurückverweisung "
                        "rechtfertigt (EPG-BerG Emboline/AorticLab)."],
                       abwandlung="Die Lokalkammer verneint die Verletzung und bescheidet die Widerklage nicht. Das Berufungsgericht bejaht die Verletzung.",
                       level=3, titel="Keine Zurückverweisung", norms=["Art. 75 EPGÜ", "R. 242.2 VerfO"]),
                 ],
                abschnitt="R. 25 VerfO: Widerklage auf Nichtigerklärung", level=2,
                concepts=["upc_widerklage_nichtigkeit", "upc_nichtigkeitsklage"], norms=["R. 25 VerfO", "Art. 33 Abs. 3 EPGÜ", "R. 263 VerfO"],
                cases=["upc_coa_emboline_aorticlab_bedingte_widerklage", "upc_coa_aorticlab_emboline_getrennte_klagen"], step="step:upc_schema_nichtigkeit.1.1"),
            *fallkette("u06a-4", "Widerklage in Düsseldorf, Einspruch in München",
                "Gegen eine Verletzungsklage vor der Lokalkammer Düsseldorf erhebt die Beklagte Widerklage auf Nichtigerklärung. Gegen "
                "dasselbe Patent läuft ein Einspruch beim EPA.",
                [frage("Was darf die Lokalkammer mit der Widerklage tun?", 2,
                       ["Art. 33 Abs. 3 EPGÜ lässt der Lokalkammer nach Anhörung der Parteien die Wahl: beide Klagen selbst verhandeln, mit "
                        "einem technisch qualifizierten Richter aus dem Pool; die Widerklage an die Zentralkammer verweisen; oder mit "
                        "Zustimmung der Parteien beide Klagen verweisen. Sie entscheidet nach R. 37 VerfO, in der Praxis fast immer für die "
                        "gemeinsame Verhandlung."],
                       optionen=["Sie muss die Widerklage an die Zentralkammer verweisen",
                                 "Sie muss die Widerklage wegen des Einspruchs abweisen",
                                 "Sie kann selbst verhandeln, die Widerklage verweisen oder mit Zustimmung beide Klagen verweisen"],
                       titel="Drei Optionen"),
                 frage("Ist die Widerklage trotz des laufenden Einspruchs zulässig?", True,
                       ["**Ja!** Anders als im deutschen Recht gibt es keine Sperre durch das Einspruchsverfahren. Widerklage und "
                        "Nichtigkeitsklage sind auch während eines EPA-Einspruchs möglich; das Gericht kann nur aussetzen (Art. 33 Abs. 10 "
                        "EPGÜ, R. 295 lit. a VerfO)."],
                       titel="Keine Einspruchssperre"),
                 frage("Muss die Lokalkammer bis zur Entscheidung des EPA aussetzen?", False,
                       ["**Nein!** Die Aussetzung steht im Ermessen des Gerichts und setzt voraus, dass eine **rasche** Entscheidung des EPA zu "
                        "erwarten ist (Art. 33 Abs. 10 EPGÜ, R. 295 lit. a VerfO). Darüber entscheidet grundsätzlich das Gericht erster "
                        "Instanz, nicht das Berufungsgericht (EPG-BerG Sun Patent/Vivo)."],
                       titel="Aussetzung nach Ermessen"),
                 frage("Steht die wahrscheinliche Beschwerde einer Aussetzung entgegen?", False,
                       ["**Nein!** Art. 33 Abs. 10 EPGÜ und R. 295 lit. a VerfO verlangen keine rasche **rechtskräftige** Entscheidung des "
                        "EPA. Es genügt, dass die Einspruchsabteilung rasch entscheiden wird, auch wenn wahrscheinlich Beschwerde folgt. Die "
                        "Aussetzung soll Widersprüche zwischen Verletzungsurteil und Widerruf vermeiden (EPG-BerG Meril/Edwards 2024)."],
                       abwandlung="Die Einspruchsabteilung wird in drei Monaten entscheiden; eine Beschwerde gilt als sicher.", level=3,
                       titel="Rasche Entscheidung", cases=["upc_coa_meril_edwards_rechtsargument"]),
                 frage("Hat eine Berufung gegen die Entscheidung über die Widerklage aufschiebende Wirkung?", True,
                       ["**Ja!** Die Berufung gegen Entscheidungen über Nichtigkeitsklagen und Widerklagen auf Nichtigerklärung hat **stets** "
                        "aufschiebende Wirkung (Art. 74 Abs. 2 EPGÜ). Bei Verletzungsentscheidungen ist es umgekehrt: keine aufschiebende "
                        "Wirkung, außer das Berufungsgericht ordnet sie an (Art. 74 Abs. 1 EPGÜ, R. 223 VerfO)."],
                       titel="Aufschiebende Wirkung", norms=["Art. 74 Abs. 2 EPGÜ"], concepts=["upc_aufschiebende_wirkung"]),
                 ],
                abschnitt="Art. 33 Abs. 3 und 10 EPGÜ: Widerklage und EPA-Einspruch", level=2,
                concepts=["upc_widerklage_nichtigkeit", "upc_aussetzung"], norms=["Art. 33 Abs. 3 EPGÜ", "Art. 33 Abs. 10 EPGÜ", "R. 295 VerfO"],
                cases=["upc_coa_sunpatent_vivo_aussetzung", "upc_coa_emboline_aorticlab_bedingte_widerklage"], step="step:upc_schema_nichtigkeit.1.4"),
        ]),
        dict(id="u06b", titel="Art. 65 EPGÜ, Art. 138 EPÜ: Nichtigkeitsgründe", einheiten=[
            intro("u06b-0", "Die Gründe kommen aus dem EPÜ, der Maßstab vom Berufungsgericht",
                  "Das EPG kann ein Patent nur aus den Gründen des **Art. 138 Abs. 1 und Art. 139 Abs. 2 EPÜ** ganz oder teilweise für nichtig erklären (Art. 65 Abs. 2 EPGÜ): fehlende Patentierbarkeit (Neuheit, erfinderische Tätigkeit, Ausschlüsse), unzureichende Offenbarung, unzulässige Erweiterung, Erweiterung des Schutzbereichs, fehlende Berechtigung. Betreffen die Gründe nur einen Teil, wird das Patent durch Änderung der Ansprüche beschränkt (Art. 65 Abs. 3 EPGÜ); es kann auch im Umfang einzelner selbständiger Ansprüche bestehen bleiben, wenn diese nicht so aufeinander aufbauen, dass der Wegfall des einen den des anderen erzwingt (LK Hamburg Avago/Tesla). Die Nichtigerklärung wirkt **ex tunc** (Art. 65 Abs. 4 EPGÜ). Die Maßstäbe hat das Berufungsgericht in wenigen Jahren geprägt: Die **Auslegung** folgt für Verletzung und Rechtsbestand denselben Regeln (NanoString/10x). Der **Offenbarungsmaßstab** „unmittelbar und eindeutig“ gilt gleichermaßen für Neuheit, unzulässige Erweiterung und Priorität; ein allgemeiner Begriff offenbart nicht ohne Weiteres alle Unterbegriffe (Knaus Tabbert), und aus schematischen Zeichnungen leitet die Fachperson keine Abmessungen ab (Pari/Philips). Bei **Teilanmeldungen** gilt Art. 123 Abs. 2 EPÜ gegenüber jeder früheren Anmeldung, auch der PCT-Stammanmeldung (expert/Seoul Viosys); die unzulässige Erweiterung ist Rechtsfrage, das Gericht darf die ganze Anmeldung heranziehen (Amgen/Regeneron). Für die **erfinderische Tätigkeit** gibt es keinen starren Aufgabe-Lösungs-Ansatz: realistischer Ausgangspunkt, Fachperson mit Aussicht auf Erfolg, „would“ statt „could“ (NanoString/10x, Meril/Edwards), Pointer für Kombinationen (Fujifilm/Kodak), keine vorschnelle Ausklammerung nichttechnischer Merkmale (Abbott/Sinocare). Die Zentralkammer Paris prüft in drei Schritten: objektive Aufgabe, Stand der Technik mit realistischen Ausgangspunkten, Naheliegen (Meril/Edwards). **Ausführbarkeit**: Die Fachperson muss den Gegenstand ohne erfinderisches Zutun und ohne unzumutbaren Aufwand nacharbeiten können; ein Weg genügt (Amgen/Regeneron).",
                  concepts=["upc_nichtigkeitsgruende", "upc_fachperson", "upc_offenbarungsgehalt"], norms=["Art. 65 Abs. 2 EPGÜ", "Art. 65 Abs. 3 EPGÜ", "Art. 65 Abs. 4 EPGÜ"], cases=["upc_cfi_avago_tesla_teilnichtigkeit", "upc_coa_nanostring_10x", "upc_coa_amgen_regeneron_auslegung"]),
            *fallkette("u06b-4", "Zwei selbständige Ansprüche",
                "P verklagt B vor einer Lokalkammer aus einem Patent mit den selbständigen Ansprüchen 1 und 10. B erhebt Widerklage auf "
                "Nichtigerklärung. Nur Anspruch 1 ist nicht neu.",
                [frage("Kann das Gericht das Patent nur teilweise für nichtig erklären?", True,
                       ["**Ja!** Das Patent wird nur so weit für nichtig erklärt, wie die Nichtigkeitsgründe reichen; betreffen sie nur einen "
                        "Teil, wird es beschränkt (Art. 65 Abs. 3 EPGÜ)."],
                       titel="Teilweise Nichtigkeit"),
                 frage("Kann Anspruch 10 bestehen bleiben, wenn er nicht auf Anspruch 1 aufbaut?", True,
                       ["**Ja!** Ein Patent kann im Umfang einzelner selbständiger Ansprüche bestehen bleiben, wenn diese nicht so "
                        "aufeinander aufbauen, dass der Wegfall des einen den des anderen erzwingt (LK Hamburg Avago/Tesla)."],
                       titel="Selbständiger Anspruch"),
                 frage("Wirkt die Nichtigerklärung von Anspruch 1 nur für die Zukunft?", False,
                       ["**Nein!** Soweit das Patent für nichtig erklärt wird, gelten seine Wirkungen als von Anfang an nicht eingetreten "
                        "(**ex tunc**, Art. 65 Abs. 4 EPGÜ)."],
                       titel="Wirkung ex tunc", norms=["Art. 65 Abs. 4 EPGÜ"]),
                 ],
                abschnitt="Art. 65 Abs. 3 und 4 EPGÜ: Umfang und Wirkung", level=1,
                concepts=["upc_nichtigkeitsgruende"], norms=["Art. 65 Abs. 3 EPGÜ"], cases=["upc_cfi_avago_tesla_teilnichtigkeit"],
                step="step:upc_schema_nichtigkeit.4"),
            *fallkette("u06b-1", "Die Teilanmeldung",
                "Seoul Viosys hält ein Patent aus einer Teilanmeldung; die Kette reicht über eine europäische Stammanmeldung bis zu einer "
                "PCT-Anmeldung. Der Anspruch kombiniert zwei Merkmale, die die PCT-Anmeldung nur in getrennten Ausführungsformen beschreibt.",
                [frage("Welcher Maßstab gilt für die unzulässige Erweiterung?", 0,
                       ["Der Anspruch darf nicht über den Inhalt der ursprünglichen Anmeldung hinausgehen (Art. 138 Abs. 1 lit. c EPÜ, "
                        "Art. 65 Abs. 2 EPGÜ). Maßgeblich ist, was die Fachperson am Anmeldetag der Gesamtheit der Anmeldung **unmittelbar "
                        "und eindeutig** entnimmt, einschließlich implizit Offenbartem (EPG-BerG expert/Seoul Viosys)."],
                       optionen=["Was die Fachperson der Anmeldung unmittelbar und eindeutig entnimmt",
                                 "Was die Anmeldung der Fachperson nahelegt",
                                 "Allein der Wortlaut der ursprünglichen Ansprüche"],
                       titel="Maßstab"),
                 frage("Genügt es, dass die Kombination in der unmittelbar vorangehenden Stammanmeldung steht?", False,
                       ["**Nein!** Bei Patenten aus Teilanmeldungen muss der Gegenstand in **jeder** früheren Anmeldung der Kette offenbart "
                        "sein, auch in der PCT-Stammanmeldung (EPG-BerG expert/Seoul Viosys)."],
                       merke="Teilanmeldung: Art. 123 Abs. 2 EPÜ gegenüber jeder früheren Anmeldung (expert/Seoul Viosys).",
                       titel="Jede frühere Anmeldung"),
                 frage("Ist die Kombination offenbart, wenn die PCT-Anmeldung die Merkmale nur getrennt beschreibt?", False,
                       ["**Nein!** Zwei Merkmale aus verschiedenen Ausführungsformen ergeben noch keine offenbarte Kombination, solange die "
                        "Fachperson sie nicht als zusammengehörig mitliest. Der erteilte Anspruch geht dann über den Inhalt der Anmeldung "
                        "hinaus (EPG-BerG expert/Seoul Viosys)."],
                       titel="Getrennte Ausführungsformen"),
                 frage("Ist die unzulässige Erweiterung eine Rechtsfrage?", True,
                       ["**Ja!** Sie ist eine **Rechtsfrage**, die auf Grundlage der vorgetragenen Tatsachen entschieden wird, nämlich der "
                        "Ansprüche und der Anmeldung. Das Gericht darf die gesamte Anmeldung heranziehen und aus eigener Sachkunde feststellen, "
                        "dass eine Offenbarung fehlt (EPG-BerG Amgen/Regeneron)."],
                       level=3, titel="Rechtsfrage"),
                 frage("Kann Seoul Viosys das Patent durch eine Änderung retten?", True,
                       ["**Ja!** Der Patentinhaber kann das Patent mit einem Antrag auf Änderung auf eine ursprünglich offenbarte Fassung "
                        "beschränken (R. 30, R. 50 VerfO). Sonst ist es insoweit für nichtig zu erklären (Art. 65 Abs. 2 und 3 EPGÜ)."],
                       titel="Beschränkung als Ausweg", concepts=["upc_aenderung_patent"]),
                 ],
                abschnitt="Art. 138 Abs. 1 lit. c EPÜ: unzulässige Erweiterung", level=2,
                concepts=["upc_unzulaessige_erweiterung", "upc_fachperson"], norms=["Art. 65 Abs. 2 EPGÜ"],
                cases=["upc_coa_expert_seoulviosys_erweiterung", "upc_coa_amgen_regeneron_auslegung"], step="step:upc_schema_nichtigkeit.2.4"),
            *fallkette("u06b-2", "„Kunststoff“",
                "Knaus Tabbert verteidigt ein Patent auf ein Wohnwagen-Bauteil aus einem bestimmten Werkstoff mit bestimmter Struktur. Eine "
                "ältere Druckschrift nennt für dasselbe Bauteil nur allgemein „Kunststoff“.",
                [frage("Ist neuheitsschädlich nur, was die Fachperson der Druckschrift unmittelbar und eindeutig entnimmt?", True,
                       ["**Ja!** Neuheitsschädlich ist, was die Fachperson bei aufmerksamer Lektüre **unmittelbar und eindeutig** entnimmt, "
                        "einschließlich dessen, was sie als selbstverständlich mitliest (EPG-BerG Knaus Tabbert)."],
                       titel="Maßstab der Neuheit"),
                 frage("Offenbart „Kunststoff“ alle darunter fallenden Werkstoffe und Strukturen?", False,
                       ["**Nein!** Ein allgemeiner Begriff offenbart nicht ohne Weiteres alle darunter fallenden, nicht genannten "
                        "Unterbegriffe (EPG-BerG Knaus Tabbert). Die Druckschrift nimmt den Anspruch nicht vorweg; der Angriff verlagert sich "
                        "auf die erfinderische Tätigkeit."],
                       merke="Der Oberbegriff offenbart nicht den Unterbegriff (Knaus Tabbert).", titel="Oberbegriff und Unterbegriff"),
                 frage("Gilt derselbe Offenbarungsmaßstab für unzulässige Erweiterung und Priorität?", True,
                       ["**Ja!** Der Maßstab „unmittelbar und eindeutig“ gilt für Neuheit, unzulässige Erweiterung und Priorität "
                        "gleichermaßen (EPG-BerG Knaus Tabbert)."],
                       titel="Einheitlicher Maßstab"),
                 frage("Offenbart die Zeichnung diese Maße?", False,
                       ["**Nein!** Aus schematischen Zeichnungen leitet die Fachperson keine Abmessungen ab (ZK Mailand Pari/Philips). "
                        "Offenbart ist nur, was die Zeichnung erkennbar als technische Lehre zeigt."],
                       abwandlung="Die Druckschrift enthält eine schematische Zeichnung, aus der sich Wandstärken abmessen ließen.",
                       titel="Schematische Zeichnung", cases=["upc_cfi_pari_philips_klagebefugnis"]),
                 frage("Bleibt ein Erzeugnisanspruch, der ein Herstellungsverfahren nennt, ein Erzeugnisanspruch?", True,
                       ["**Ja!** Ein product-by-process-Anspruch bleibt Erzeugnisanspruch. Zu prüfen ist, ob sich das Verfahren in "
                        "**Eigenschaften des Erzeugnisses** niederschlägt; nur diese zählen für die Neuheit (EPG-BerG Knaus Tabbert)."],
                       level=3, titel="product-by-process"),
                 ],
                abschnitt="Art. 138 Abs. 1 lit. a EPÜ: Neuheit", level=2,
                concepts=["upc_offenbarungsgehalt", "upc_fachperson"], norms=["Art. 65 Abs. 2 EPGÜ"],
                cases=["upc_coa_knaus_tabbert_altfaelle"], step="step:upc_schema_nichtigkeit.2.2"),
            *fallkette("u06b-3", "Von D1 zur Erfindung",
                "Meril greift ein Patent von Edwards wegen fehlender erfinderischer Tätigkeit an. Sie geht von der Druckschrift D1 aus und "
                "entnimmt das fehlende Merkmal der Druckschrift D2.",
                [frage("Wendet das Berufungsgericht den Aufgabe-Lösungs-Ansatz des EPA zwingend an?", False,
                       ["**Nein!** Das Berufungsgericht folgt keinem starren Schema (NanoString/10x, Meril/Edwards). Die Zentralkammer Paris "
                        "prüft in drei Schritten: objektive Aufgabe im Lichte der Patentschrift, realistische Ausgangspunkte im Stand der "
                        "Technik, Naheliegen der Erfindung als Ganzes (ZK Paris Meril/Edwards)."],
                       titel="Kein starres Schema"),
                 frage("Darf Meril jeden beliebigen Stand der Technik als Ausgangspunkt wählen?", False,
                       ["**Nein!** Ausgangspunkt muss ein **realistischer** Stand der Technik sein, den die Fachperson für die Aufgabe in "
                        "Betracht ziehen würde. Mehrere realistische Ausgangspunkte sind möglich; ihre Auswahl ist Sache der Parteien "
                        "(EPG-BerG Meril/Edwards; ZK Paris Meril/Edwards)."],
                       titel="Realistischer Ausgangspunkt"),
                 frage("Muss die Fachperson von D1 mit Aussicht auf Erfolg zur Erfindung gelangen?", True,
                       ["**Ja!** Die Fachperson muss von dort mit **Aussicht auf Erfolg** zur Erfindung gelangen („would“), nicht nur "
                        "gelangen können („could“) (EPG-BerG NanoString/10x, Meril/Edwards)."],
                       merke="Would, not could: Naheliegend ist, wozu die Fachperson mit Erfolgsaussicht greifen würde.",
                       titel="Would statt could"),
                 frage("Kann sich die Motivation zur Kombination aus D2 selbst ergeben?", False,
                       ["**Nein!** Ohne Anregung („pointer“), den Ausgangspunkt mit einer weiteren Schrift zu kombinieren, lässt sich die "
                        "Motivation nicht aus dem Inhalt der Kombinationsschrift herleiten. Ohne Anlass zieht die Fachperson D2 gar nicht "
                        "heran (EPG-BerG Fujifilm/Kodak)."],
                       abwandlung="D1 enthält keinen Hinweis, eine Lösung wie in D2 zu suchen.", level=3, titel="Pointer",
                       cases=["upc_coa_fujifilm_kodak_nichtigkeit"]),
                 frage("Bleibt ein solches Merkmal als nichttechnisch außer Betracht?", False,
                       ["**Nein!** Ein Merkmal ist nicht schon deshalb auszuklammern, weil es für sich genommen nichttechnisch wäre. Es kann "
                        "im Zusammenwirken mit den übrigen Merkmalen zum technischen Charakter beitragen; die Merkmale sind gemeinsam zu "
                        "würdigen (EPG-BerG Abbott/Sinocare)."],
                       abwandlung="Ein Anspruchsmerkmal betrifft für sich genommen nur die Anzeige von Messwerten.", level=3,
                       titel="Nichttechnische Merkmale", cases=["upc_coa_abbott_sinocare_erfinderisch"]),
                 ],
                abschnitt="Art. 138 Abs. 1 lit. a EPÜ: erfinderische Tätigkeit", level=2,
                concepts=["upc_erfinderische_taetigkeit", "upc_fachperson"], norms=["Art. 65 Abs. 2 EPGÜ"],
                cases=["upc_coa_meril_edwards_parteien", "upc_cfi_meril_edwards_erfinderisch"], step="step:upc_schema_nichtigkeit.2.3"),
        ]),
        dict(id="u06c", titel="R. 30, 43 und 50 VerfO: Änderung des Patents und Erwiderung", einheiten=[
            intro("u06c-0", "Hilfsanträge nach R. 30 und R. 50 VerfO",
                  "Der Patentinhaber verteidigt sich auf zwei Ebenen. Erstens mit der **Erwiderung** (R. 29A VerfO bei der Widerklage, R. 49, 50.1 VerfO bei der Nichtigkeitsklage): Tatsachen, Beweise, Gründe, warum die Klage abzuweisen ist, und die Angabe, welche Unteransprüche oder Kombinationen er für rechtsbeständig hält (Fujifilm/Kodak). Zweitens mit dem **Antrag auf Änderung des Patents** (R. 30.1, R. 50.2 VerfO), der die geänderten Ansprüche, gegebenenfalls Hilfsanträge in angemessener Zahl, die Begründung nach Art. 84, 123 Abs. 2 und 3 EPÜ und die Angabe enthalten muss, ob die Änderung bedingt oder unbedingt ist. Der Antrag gehört in die Erwiderung; **spätere Anträge** sind nur mit Erlaubnis des Gerichts zulässig (R. 30.2 VerfO), das prüft, ob die Änderung bei angemessener Sorgfalt nicht früher möglich war und die Gegenseite nicht unangemessen behindert wird; das Gericht erster Instanz hat dabei Ermessen, die Kontrolle durch das Berufungsgericht ist beschränkt (Meril/Edwards). Auf den Änderungsantrag folgt die **Erwiderung des Klägers** (R. 32, R. 43.3 VerfO) mit Ausführungen nach R. 44 lit. d bis h VerfO; sie darf keine neuen Nichtigkeitsgründe oder Entgegenhaltungen gegen die erteilte Fassung einführen, es sei denn, eine Klageänderung nach R. 263 VerfO wird zugelassen (VMR/NJOY). Läuft ein anderes Verfahren zu dem Patent, ist die zuständige Stelle über den Änderungsantrag zu unterrichten (R. 30.3 VerfO). Am Ende steht die Entscheidung nach Art. 65 Abs. 3 EPGÜ: Beschränkung durch die geänderten Ansprüche und teilweise Nichtigerklärung.",
                  concepts=["upc_aenderung_patent", "upc_nichtigkeitsklage", "upc_front_loaded"], norms=["R. 30 VerfO", "R. 50 VerfO", "R. 43 VerfO", "R. 29A VerfO"], cases=["upc_coa_meril_edwards_parteien", "upc_coa_vmr_njoy_aenderung", "upc_coa_fujifilm_kodak_nichtigkeit"]),
            *fallkette("u06c-1", "Drei Hilfsanträge zu spät",
                "Edwards stellt in der Erwiderung auf Merils Widerklage vier Hilfsanträge. Kurz vor der Zwischenanhörung reicht Edwards drei "
                "weitere ein. Sie antworten auf Einwände, die schon in der Widerklage standen.",
                [frage("Wohin gehört der Antrag auf Änderung des Patents?", 0,
                       ["Der Antrag auf Änderung gehört in die **Erwiderung** auf die Widerklage (R. 30.1 VerfO), bei der Nichtigkeitsklage "
                        "in die Klageerwiderung (R. 50.2 VerfO). Im front-loaded-Verfahren gehören alle Verteidigungslinien in den ersten "
                        "Schriftsatz."],
                       optionen=["In die Erwiderung auf die Widerklage", "In die mündliche Verhandlung",
                                 "In einen beliebigen Schriftsatz vor der Zwischenanhörung"],
                       titel="Ort des Antrags"),
                 frage("Sind spätere Hilfsanträge ausgeschlossen?", False,
                       ["**Nein!** Spätere Anträge auf Änderung sind mit **Erlaubnis des Gerichts** möglich (R. 30.2, R. 50.2 VerfO). Das "
                        "Gericht prüft, ob die Änderung bei angemessener Sorgfalt nicht früher möglich war und ob die Gegenseite unangemessen "
                        "behindert wird (EPG-BerG Meril/Edwards)."],
                       titel="Spätere Anträge mit Erlaubnis"),
                 frage("Bekommt Edwards die Erlaubnis für die drei neuen Anträge?", False,
                       ["**Nein!** Die Anträge reagieren auf Einwände, die schon in der Widerklage standen. Bei angemessener Sorgfalt wären "
                        "sie also schon in der Erwiderung möglich gewesen; eine Begründung für die Verspätung fehlt (EPG-BerG Meril/Edwards)."],
                       merke="Hilfsanträge in die Erwiderung; spätere nur mit Erlaubnis und Grund (Meril/Edwards).",
                       titel="Kein Grund für die Verspätung"),
                 frage("Prüft das Berufungsgericht die Nichtzulassung nur auf Ermessensfehler?", True,
                       ["**Ja!** Das Gericht erster Instanz hat bei der Zulassung **Ermessen**. Das Berufungsgericht prüft nur, ob es "
                        "fehlerfrei ausgeübt wurde, nicht, ob es selbst anders entschieden hätte (EPG-BerG Meril/Edwards)."],
                       abwandlung="Die Lokalkammer lässt die drei Anträge nicht zu; Edwards legt Berufung ein.", level=3,
                       titel="Ermessen der ersten Instanz"),
                 frage("Was muss ein Antrag auf Änderung unter anderem enthalten?", 1,
                       ["Der Antrag enthält die geänderten Ansprüche, gegebenenfalls Hilfsanträge in angemessener Zahl, die Begründung, "
                        "warum die Änderung Art. 84 und Art. 123 Abs. 2 und 3 EPÜ genügt, und die Angabe, ob sie **bedingt oder unbedingt** "
                        "ist (R. 30.1 VerfO)."],
                       optionen=["Nur die geänderten Ansprüche",
                                 "Die geänderten Ansprüche, die Begründung nach Art. 84 und 123 EPÜ und ob die Änderung bedingt ist",
                                 "Eine Erklärung des EPA, dass es die Änderung billigt"],
                       titel="Inhalt des Antrags"),
                 ],
                abschnitt="R. 30 und 50 VerfO: Antrag auf Änderung", level=2,
                concepts=["upc_aenderung_patent", "upc_front_loaded"], norms=["R. 30 VerfO", "R. 50 VerfO"],
                cases=["upc_coa_meril_edwards_parteien"], step="step:upc_schema_nichtigkeit.3"),
            *fallkette("u06c-2", "Neue Druckschriften in der Erwiderung",
                "NJOY greift ein Patent von VMR mit drei Entgegenhaltungen an. VMR beantragt hilfsweise eine geänderte Fassung. In der "
                "Erwiderung darauf legt NJOY zwei neue Druckschriften vor.",
                [frage("Darf NJOY die neuen Druckschriften gegen die geänderte Fassung einsetzen?", True,
                       ["**Ja!** Auf den Änderungsantrag folgt die Erwiderung des Klägers (R. 43.3 VerfO) mit Ausführungen nach R. 44 lit. d "
                        "bis h VerfO. Sie ist gerade dazu da, die **geänderte** Fassung anzugreifen (EPG-BerG VMR/NJOY)."],
                       titel="Angriff auf die geänderte Fassung"),
                 frage("Darf NJOY damit auch die erteilte Fassung neu angreifen?", False,
                       ["**Nein!** Die Erwiderung eröffnet keine neuen Nichtigkeitsgründe oder Entgegenhaltungen gegen das Patent **in "
                        "erteilter Fassung** (EPG-BerG VMR/NJOY). Diese Angriffe gehören in die Klage (R. 44 VerfO)."],
                       merke="Die Erwiderung nach R. 43.3 VerfO zielt auf die geänderte Fassung (VMR/NJOY).",
                       titel="Kein neuer Angriff auf die erteilte Fassung"),
                 frage("Wie kann NJOY neue Angriffe auf die erteilte Fassung doch einführen?", 1,
                       ["Nur über eine **Klageänderung**, die das Gericht nach R. 263 VerfO zulässt (EPG-BerG VMR/NJOY). Das Gericht prüft "
                        "dann, ob die Änderung früher möglich war und die Gegenseite unangemessen behindert."],
                       optionen=["Gar nicht", "Mit einer nach R. 263 VerfO zugelassenen Klageänderung",
                                 "Mit einem einfachen Hinweis in der Duplik"],
                       titel="Weg über R. 263 VerfO", norms=["R. 263 VerfO"], concepts=["upc_klageaenderung"]),
                 frage("Kann das Lehrbuch noch berücksichtigt werden?", True,
                       ["**Ja!** Die Fairness kann neue **Beweise zum allgemeinen Fachwissen** als Reaktion auf die Klageerwiderung "
                        "erlauben, denn das Fachwissen ist eine beweisbedürftige Tatsache (EPG-BerG VMR/NJOY)."],
                       abwandlung="NJOY legt zusätzlich ein Lehrbuch vor, um das Fachwissen zu belegen, auf das VMR sich in der Klageerwiderung beruft.",
                       level=3, titel="Beweis zum Fachwissen", concepts=["upc_beweismittel_beweislast"]),
                 ],
                abschnitt="R. 43.3 VerfO: Erwiderung auf den Änderungsantrag", level=3,
                concepts=["upc_aenderung_patent"], norms=["R. 43 VerfO", "R. 44 VerfO", "R. 32 VerfO"],
                cases=["upc_coa_vmr_njoy_aenderung"], step="step:upc_schema_nichtigkeit.3"),
        ]),
    ],
)
