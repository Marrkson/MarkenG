# -*- coding: utf-8 -*-
"""Kapitel des Normkurses e01 (siehe e01_epue_paper_d.py): Einspruch und Beitritt (Art. 99 bis 101, 105 EPÜ), Beschränkung und Widerruf
(Art. 105a bis 105c EPÜ), Beschwerde und Überprüfungsantrag (Art. 106 bis 112a EPÜ), Euro-PCT (Art. 153 EPÜ, R. 159 bis 165 EPÜ) und die
internationale Phase vor dem EPA (Art. 150 bis 152 EPÜ). `order` = Artikel × 100."""
from ._helpers import intro, schema, frage, fallkette

_ES = "step:epc_schema_einspruch"
_BS = "step:epc_schema_beschwerde"
_EP = "step:epc_schema_euro_pct"
_FV = "step:epc_schema_fristversaeumnis"

KAPITEL = [
    # ================================================================== Art. 99 bis 101, 105 EPÜ
    dict(id="e01n99", order=9900, titel="Art. 99 bis 101, 105 EPÜ: Einspruch und Beitritt", einheiten=[
        intro("e01n99-0", "Wer, bis wann, mit welchen Gründen",
              "Einspruchsfragen kommen in Paper D fast jedes Jahr vor (2015 Q2, 2017 Q2, 2018 Q2, 2019 Q4, 2022 Q6, 2023 Q3, 2024 Q3 und Q4). "
              "Gefragt wird selten die Neuheit selbst, sondern das Verfahren: **wer** einsprechen darf, **bis wann** und mit welcher Gebühr "
              "(Art. 99 Abs. 1 EPÜ), welche Mängel nur in der Einspruchsfrist heilbar sind (R. 77 EPÜ), welche **Gründe** zählen (Art. 100 EPÜ) "
              "und wie weit die Einspruchsabteilung prüft (G 9/91, G 10/91, G 3/14). Dazu kommen der Übergang der Einsprechendenstellung, die "
              "Fortsetzung von Amts wegen (R. 84 EPÜ) und der **Beitritt** des vermeintlichen Verletzers (Art. 105 EPÜ).",
              concepts=["epc_einspruch", "epc_einspruchsgruende", "epc_einsprechendenstellung", "epc_beitritt"],
              norms=["Art. 99 EPÜ", "Art. 100 EPÜ", "Art. 101 EPÜ", "Art. 105 EPÜ"], distinctions=["d_epc_angriffe_nach_erteilung"],
              abschnitt="Überblick"),
        schema("e01n99-0s", "Prüfungsschema Einspruch", "epc_schema_einspruch", abschnitt="Überblick"),
        *fallkette("e01n99-1", "Der Einspruch in fremdem Auftrag",
            "Der Hinweis auf die Erteilung des Patents EP-P der Firma P wird am 4.6.2025 bekannt gemacht. Patentanwalt S legt am 2.3.2026 im "
            "eigenen Namen Einspruch ein; tatsächlich handelt er für einen Wettbewerber, der ungenannt bleiben will. Die Einspruchsgebühr geht "
            "am 6.3.2026 ein.",
            [frage("Ist der Einspruch unzulässig, weil S für einen ungenannten Dritten handelt?", False,
                   ["**Nein!** Einsprechen kann jedermann (Art. 99 Abs. 1 EPÜ), auch ein Strohmann im Auftrag eines Dritten. Unzulässig wäre der "
                    "Einspruch nur bei missbräuchlicher Gesetzesumgehung, etwa wenn S in Wahrheit für den Patentinhaber handelte (G 3/97)."],
                   merke="Der Strohmann darf einsprechen, nur nicht für den Inhaber.", titel="Strohmann", cases=["epc_g_3_97"], step=_ES + ".2"),
             frage("Ist der Einspruch wirksam eingelegt?", False,
                   ["**Nein!** Die Einspruchsfrist endete am 4.3.2026 (Art. 99 Abs. 1 Satz 1 EPÜ, R. 131 Abs. 4 EPÜ). Der Einspruch gilt erst mit "
                    "der Gebühr als eingelegt (Art. 99 Abs. 1 Satz 2 EPÜ); nach der verspäteten Zahlung gilt er als nicht eingelegt (Richtlinien "
                    "D-IV, 1.2.1). Weiterbehandlung kann nur der Anmelder beantragen (Art. 121 Abs. 1 EPÜ), Wiedereinsetzung in die Einspruchsfrist gibt "
                    "es nicht (Richtlinien D-III, 1)."],
                   merke="Ohne Gebühr in der Frist gibt es keinen Einspruch.", titel="Frist und Gebühr", level=2,
                   norms=["R. 131 Abs. 4 EPÜ"], concepts=["epc_fristen"], step=_ES + ".3"),
             frage("Könnte P selbst Einspruch gegen sein Patent einlegen, um einen zu weiten Anspruch loszuwerden?", False,
                   ["**Nein!** Der Patentinhaber ist nicht „jedermann“ im Sinne des Art. 99 Abs. 1 EPÜ (G 9/93). Zur Selbstbeschränkung dient "
                    "das Beschränkungsverfahren nach Art. 105a EPÜ."],
                   merke="Gegen das eigene Patent: Beschränkung statt Einspruch.", titel="Einspruch des Inhabers",
                   norms=["Art. 105a EPÜ"], cases=["epc_g_9_93"], concepts=["epc_beschraenkung"], step=_ES + ".2"),
             frage("Ist ein Einspruch dann überhaupt noch statthaft?", True,
                   ["**Ja!** Einspruch kann auch eingelegt werden, wenn das Patent in allen benannten Staaten erloschen ist (R. 75 EPÜ). Das "
                    "Erlöschen wirkt nur für die Zukunft, der Widerruf von Anfang an (Art. 68 EPÜ); Ansprüche aus der Zeit davor können fortbestehen "
                    "(Richtlinien D-I, 2)."],
                   merke="Auch ein erloschenes Patent kann angegriffen werden.", titel="Einspruch nach Erlöschen", level=2,
                   abwandlung="P hat das Patent schon vor dem Einspruch in allen benannten Staaten verfallen lassen.",
                   norms=["R. 75 EPÜ", "Art. 68 EPÜ"], step=_ES + ".1"),
            ],
            abschnitt="Art. 99 Abs. 1 EPÜ: Einsprechender, Frist, Gebühr", level=1, concepts=["epc_einspruch"], norms=["Art. 99 Abs. 1 EPÜ"]),
        *fallkette("e01n99-2", "Zwei Einsprechende, eine Gebühr",
            "Luca, italienischer Staatsangehöriger mit Wohnsitz in Brasilien, und Marco, wohnhaft in Mailand, legen in der Einspruchsfrist "
            "gemeinsam Einspruch gegen EP-Q ein. Die Schrift ist italienisch, von beiden unterschrieben und nennt Umfang, Gründe, Tatsachen und "
            "Beweismittel. Sie zahlen eine Einspruchsgebühr.",
            [frage("Genügt eine einzige Einspruchsgebühr?", True,
                   ["**Ja!** Ein von mehreren Personen gemeinsam eingelegter Einspruch ist mit einer Gebühr zulässig (G 3/99; Richtlinien D-III, 2). "
                    "Im ganzen Verfahren muss klar sein, wer zur Gruppe gehört; Verfahrenshandlungen nimmt der gemeinsame Vertreter vor "
                    "(R. 151 Abs. 1 EPÜ)."],
                   merke="Gemeinsamer Einspruch: eine Gebühr, ein gemeinsamer Vertreter.", titel="Gemeinsamer Einspruch",
                   norms=["R. 151 Abs. 1 EPÜ"], cases=["epc_g_3_99"], step=_ES + ".2"),
             frage("Durften die beiden den Einspruch auf Italienisch einreichen?", True,
                   ["**Ja!** Marco wohnt in Italien, Luca ist Italiener mit Wohnsitz im Ausland; beide dürfen Italienisch verwenden (Art. 14 Abs. 4 EPÜ). "
                    "Die Übersetzung in eine Amtssprache des EPA ist binnen eines Monats oder bis zum Ende der Einspruchsfrist nachzureichen, je "
                    "nachdem, was später abläuft (R. 6 Abs. 2 EPÜ)."],
                   merke="Italiener im Ausland dürfen Italienisch einreichen, mit Übersetzung.", titel="Sprache", level=2,
                   norms=["Art. 14 Abs. 4 EPÜ", "R. 6 Abs. 2 EPÜ"], concepts=["epc_sprachen"]),
             frage("Muss Luca einen zugelassenen Vertreter bestellen?", True,
                   ["**Ja!** Wer weder Wohnsitz noch Sitz in einem Vertragsstaat hat, muss vertreten sein (Art. 133 Abs. 2 EPÜ); die "
                    "Staatsangehörigkeit hilft nicht. Der Mangel ist auf Aufforderung in der gesetzten Frist behebbar (R. 77 Abs. 2 EPÜ); der Vertreter "
                    "muss die Einspruchsschrift auch unterzeichnen oder genehmigen (Richtlinien D-IV, 1.2.2.2)."],
                   merke="Wohnsitz außerhalb der Vertragsstaaten: Vertreter nötig, Mangel heilbar.", titel="Vertretung", level=2,
                   norms=["Art. 133 Abs. 2 EPÜ", "R. 77 Abs. 2 EPÜ"], concepts=["epc_vertretung"], step=_ES + ".2"),
             frage("Werden die beiden aufgefordert, die Tatsachen und Beweismittel nachzureichen?", False,
                   ["**Nein!** Die Angaben nach R. 76 Abs. 2 lit. c EPÜ müssen bis zum Ablauf der Einspruchsfrist vorliegen. Fehlen sie dann noch, "
                    "verwirft die Einspruchsabteilung den Einspruch ohne Aufforderung als unzulässig (R. 77 Abs. 1 EPÜ). Eine Mängelaufforderung "
                    "gibt es nur für die übrigen Mängel (R. 77 Abs. 2 EPÜ)."],
                   merke="Gründe, Tatsachen, Beweismittel: nur bis Fristende heilbar.", titel="Substantiierung", level=2,
                   abwandlung="Die Einspruchsschrift nennt keine Tatsachen und Beweismittel; die beiden wollen sie nach Ablauf der Einspruchsfrist liefern.",
                   norms=["R. 76 Abs. 2 EPÜ", "R. 77 Abs. 1 EPÜ"], step=_ES + ".4"),
            ],
            abschnitt="R. 76 und R. 77 EPÜ: Inhalt und Mängel", level=1, concepts=["epc_einspruch"], norms=["R. 76 EPÜ", "R. 77 EPÜ"]),
        *fallkette("e01n99-3", "Der nicht angegriffene Anspruch",
            "EP-N enthält den unabhängigen Anspruch 1 (A), den abhängigen Anspruch 2 (A+B) und den unabhängigen Anspruch 3 (D). Die "
            "Einsprechende O greift nur Anspruch 1 an, wegen fehlender Neuheit gegenüber D1. Nach Ablauf der Einspruchsfrist legt sie D2 vor, "
            "das D offenbart. Der Inhaber verteidigt Anspruch 1 zusammen mit dem Merkmal B.",
            [frage("Prüft die Einspruchsabteilung Anspruch 3 anhand von D2?", False,
                   ["**Nein!** Die Erklärung zum Umfang des Einspruchs (R. 76 Abs. 2 lit. c EPÜ) begrenzt die Prüfungsbefugnis; nicht angegriffene "
                    "unabhängige Ansprüche werden nicht geprüft (G 9/91). D2 ist für Anspruch 3 deshalb unbeachtlich, auch wenn es prima facie "
                    "relevant ist."],
                   merke="Der Umfang des Einspruchs begrenzt die Prüfung.", titel="Umfang des Einspruchs", level=2,
                   norms=["R. 76 Abs. 2 EPÜ"], cases=["epc_g_9_91"], step=_ES + ".5"),
             frage("Kann O einwenden, der neue Anspruch 1 sei unklar, weil schon der erteilte Anspruch 2 unklar war?", False,
                   ["**Nein!** Geänderte Ansprüche werden auf Klarheit (Art. 84 EPÜ) nur geprüft, soweit die Änderung den Mangel einführt. Die "
                    "bloße Übernahme eines erteilten abhängigen Anspruchs genügt dafür nicht (G 3/14)."],
                   merke="Klarheit nur, soweit die Änderung sie verursacht.", titel="Klarheit geänderter Ansprüche", level=2,
                   norms=["Art. 84 EPÜ", "Art. 101 Abs. 3 EPÜ"], cases=["epc_g_3_14"], step=_ES + ".5"),
             frage("Hätte O die Unklarheit des erteilten Anspruchs 2 als Einspruchsgrund geltend machen können?", False,
                   ["**Nein!** Art. 100 EPÜ zählt die Einspruchsgründe abschließend auf: fehlende Patentierbarkeit, mangelnde Ausführbarkeit, "
                    "unzulässige Erweiterung. Mangelnde Klarheit gehört nicht dazu. Nicht vorgebrachte Gründe des Art. 100 EPÜ prüft die "
                    "Einspruchsabteilung nur ausnahmsweise, wenn sie prima facie durchgreifen (G 10/91)."],
                   merke="Art. 84 EPÜ ist kein Einspruchsgrund.", titel="Einspruchsgründe", cases=["epc_g_10_91"], step=_ES + ".5"),
            ],
            abschnitt="Art. 100 und 101 EPÜ: Gründe und Prüfungsumfang", level=2, concepts=["epc_einspruchsgruende"], norms=["Art. 100 EPÜ", "Art. 101 EPÜ"]),
        *fallkette("e01n99-4", "Der verkaufte Geschäftsbereich",
            "Die Firma E hat gegen das Patent EP-R Einspruch eingelegt, um ihren Geschäftsbereich Pumpen zu schützen. Nach Ablauf der "
            "Einspruchsfrist verkauft E diesen Geschäftsbereich an F; der Vertrag überträgt ausdrücklich auch den Einspruch. Ein Dokument nach "
            "Art. 54 Abs. 3 EPÜ nimmt Anspruch 1 offensichtlich vorweg.",
            [frage("Wird F Einsprechende?", True,
                   ["**Ja!** Der Einspruch ist nicht frei übertragbar (G 2/04), geht aber mit dem Geschäftsbereich über, in dessen Interesse er "
                    "eingelegt wurde (G 4/88). F muss den Übergang durch Urkunden belegen; das EPA prüft ihn in jedem Stadium von Amts wegen "
                    "(T 1178/04)."],
                   merke="Der Einspruch folgt dem Geschäftsbereich, nicht dem Vertrag allein.", titel="Übergang des Einspruchs", level=2,
                   cases=["epc_g_4_88", "epc_g_2_04", "epc_t_1178_04"], step=_ES + ".2"),
             frage("Endet das Einspruchsverfahren damit?", False,
                   ["**Nein!** Die Einspruchsabteilung kann das Verfahren nach Rücknahme des Einspruchs von Amts wegen fortsetzen "
                    "(R. 84 Abs. 2 Satz 2 EPÜ). Sie tut das, wenn ein Widerruf oder eine Beschränkung ohne weitere Mitwirkung und ohne aufwendige "
                    "Ermittlungen wahrscheinlich ist, hier wegen der offensichtlichen Vorwegnahme (Richtlinien D-VII, 5.2 und 5.3)."],
                   merke="Rücknahme des Einspruchs beendet das Verfahren nicht zwingend.", titel="Fortsetzung von Amts wegen",
                   abwandlung="F nimmt den Einspruch kurz darauf zurück.", norms=["R. 84 Abs. 2 EPÜ"], step=_ES + ".6"),
             frage("Setzt die Beschwerdekammer das Verfahren fort?", False,
                   ["**Nein!** Nimmt der Einsprechende, der einziger Beschwerdeführer ist, den Einspruch zurück, endet das Beschwerdeverfahren sofort, "
                    "gleich wie die Kammer die Rechtslage sieht (G 8/93). Die Zurückweisung des Einspruchs wird rechtskräftig; den vorweggenommenen "
                    "Anspruch 1 kann der Inhaber nur noch im Beschränkungsverfahren aufgeben (Art. 105a EPÜ)."],
                   merke="In der Beschwerde gibt es keine Fortsetzung von Amts wegen.", titel="Rücknahme in der Beschwerde", level=3,
                   abwandlung="Die Rücknahme erfolgt erst in der Beschwerde: Die Einspruchsabteilung hatte den Einspruch zurückgewiesen, F als einzige Beschwerde eingelegt.",
                   norms=["Art. 105a EPÜ"], cases=["epc_g_8_93"], concepts=["epc_beschwerde"]),
            ],
            abschnitt="R. 84 EPÜ: Einsprechendenstellung und Fortsetzung", level=2, concepts=["epc_einsprechendenstellung"], norms=["R. 84 EPÜ"]),
        *fallkette("e01n99-5", "Die Verletzungsklage während des Einspruchs",
            "Gegen EP-B der Firma B läuft ein Einspruch der Firma C, gestützt nur auf Art. 100 lit. c EPÜ. Die Einspruchsfrist ist abgelaufen. "
            "Am 2.3.2026 erhebt B gegen D Klage wegen Verletzung von EP-B. D besitzt ein Dokument nach Art. 54 Abs. 3 EPÜ, das Anspruch 1 "
            "vorwegnimmt.",
            [frage("Bis wann kann D dem Einspruchsverfahren beitreten?", 1,
                   ["**Bis 2.6.2026.** Der Beitritt ist binnen drei Monaten nach Erhebung der Verletzungsklage zu erklären (Art. 105 Abs. 1 EPÜ, "
                    "R. 89 Abs. 1 EPÜ), schriftlich und begründet; er gilt erst mit Zahlung der Einspruchsgebühr als erklärt (R. 89 Abs. 2 EPÜ)."],
                   optionen=["2.4.2026", "2.6.2026", "2.9.2026", "gar nicht mehr, weil die Einspruchsfrist abgelaufen ist"],
                   merke="Beitritt: drei Monate ab Klage, mit Einspruchsgebühr.", titel="Beitrittsfrist",
                   norms=["R. 89 EPÜ"], concepts=["epc_fristen"], step=_ES + ".6"),
             frage("Darf D den Beitritt auf fehlende Neuheit stützen, obwohl C diesen Grund nicht geltend gemacht hat?", True,
                   ["**Ja!** Ein zulässiger Beitritt wird als Einspruch behandelt (Art. 105 Abs. 2 EPÜ) und kann auf jeden Einspruchsgrund des "
                    "Art. 100 EPÜ gestützt werden (G 1/94; Richtlinien D-VII, 6). D macht also Art. 100 lit. a EPÜ mit Art. 54 Abs. 3 EPÜ geltend."],
                   merke="Der Beitretende hat alle Einspruchsgründe.", titel="Gründe des Beitretenden", level=2,
                   norms=["Art. 100 EPÜ"], cases=["epc_g_1_94"], concepts=["epc_einspruchsgruende"], step=_ES + ".6"),
             frage("Wird das Beschwerdeverfahren mit D fortgesetzt?", False,
                   ["**Nein!** Der Beitritt ist auch im Beschwerdeverfahren zulässig (G 1/94), der Beitretende erlangt dort aber keine Stellung als "
                    "Beschwerdeführer. Nach Rücknahme aller Beschwerden endet das Verfahren (G 2/24)."],
                   merke="Wer erst in der Beschwerde beitritt, hängt an den Beschwerden der anderen.", titel="Beitritt in der Beschwerde", level=3,
                   abwandlung="Die Klage wird erst erhoben, als der Fall bei der Beschwerdekammer liegt; D tritt dort bei. Dann nimmt C als einzige Beschwerdeführerin die Beschwerde zurück.",
                   cases=["epc_g_2_24", "epc_g_1_94"], concepts=["epc_beschwerde"]),
            ],
            abschnitt="Art. 105 EPÜ: Beitritt", level=2, concepts=["epc_beitritt"], norms=["Art. 105 EPÜ", "R. 89 EPÜ"]),
    ]),
    # ================================================================== Art. 105a bis 105c EPÜ
    dict(id="e01n105a", order=10510, titel="Art. 105a bis 105c EPÜ, R. 90 bis 96 EPÜ: Beschränkung und Widerruf", einheiten=[
        intro("e01n105a-0", "Das Werkzeug des Inhabers",
              "Die Beschränkung ist in Paper D der Weg des Patentinhabers, wenn der Einspruch nicht mehr hilft (2021 Q6, 2022 Q6, 2023 Q3, "
              "2024 Q4). Der Antrag ist **jederzeit nach der Erteilung** möglich, auch nach Erlöschen des Patents, aber nicht, solange ein "
              "Einspruchsverfahren anhängig ist (Art. 105a EPÜ). Ein später eingelegter Einspruch hat Vorrang vor der Beschränkung, nicht vor dem "
              "Widerruf (R. 93 EPÜ; Richtlinien D-X, 7.1). Die Prüfungsabteilung prüft nur, ob wirklich beschränkt wird und ob Art. 84 EPÜ und Art. 123 Abs. 2 und 3 EPÜ "
              "eingehalten sind (R. 95 Abs. 2 EPÜ), nicht die Patentierbarkeit. Die Entscheidung wirkt für alle Vertragsstaaten und von Anfang an "
              "(Art. 105b Abs. 3 EPÜ, Art. 68 EPÜ).",
              concepts=["epc_beschraenkung", "epc_schutzbereichserweiterung", "epc_einspruch"],
              norms=["Art. 105a EPÜ", "Art. 105b EPÜ", "Art. 105c EPÜ", "R. 92 EPÜ", "R. 93 EPÜ", "R. 95 EPÜ"],
              distinctions=["d_epc_angriffe_nach_erteilung"], abschnitt="Überblick"),
        *fallkette("e01n105a-1", "Die späte Einsicht",
            "Das Patent EP-L der Firma L wurde 2019 erteilt; Einspruch wurde nicht eingelegt. 2026 findet L eine Vorveröffentlichung, die "
            "Anspruch 1 vorwegnimmt, nicht aber den abhängigen Anspruch 2. L will die Ansprüche 1 und 2 zusammenfassen.",
            [frage("Kann L das Patent noch beim EPA beschränken lassen?", True,
                   ["**Ja!** Der Antrag ist an keine Frist gebunden: Er ist jederzeit nach der Erteilung möglich, auch nach einem Einspruchsverfahren "
                    "(Art. 105a Abs. 1 EPÜ; Richtlinien D-X, 1). Er gilt erst mit Zahlung der Beschränkungsgebühr als gestellt."],
                   merke="Beschränkung: keine Frist, aber Gebühr.", titel="Zeitpunkt"),
             frage("Was muss L dem Antrag nicht beifügen?", 2,
                   ["**Die Begründung der Neuheit.** R. 92 Abs. 2 EPÜ verlangt Angaben zum Antragsteller, die Nummer des Patents mit der Liste der "
                    "Staaten, in denen es wirksam ist, und die vollständige Fassung der geänderten Ansprüche. Warum beschränkt wird, prüft das EPA "
                    "nicht (Richtlinien D-X, 4.3.4)."],
                   optionen=["die vollständige Fassung der geänderten Ansprüche", "die Liste der Staaten, in denen das Patent wirksam geworden ist",
                             "eine Begründung, warum der beschränkte Anspruch gegenüber der Vorveröffentlichung neu ist", "Angaben zur Person von L"],
                   merke="Der Antrag braucht Ansprüche, keine Begründung.", titel="Antragserfordernisse", level=2, norms=["R. 92 Abs. 2 EPÜ"]),
             frage("Prüft die Prüfungsabteilung, ob der beschränkte Anspruch gegenüber der Vorveröffentlichung neu ist?", False,
                   ["**Nein!** Sie prüft nur, ob die Änderung eine Beschränkung ist und Art. 84 EPÜ sowie Art. 123 Abs. 2 und 3 EPÜ genügt "
                    "(R. 95 Abs. 2 EPÜ). Ob L sein Ziel erreicht, bleibt offen (Richtlinien D-X, 4.3.4); das Risiko trägt L."],
                   merke="Keine Prüfung der Patentierbarkeit im Beschränkungsverfahren.", titel="Prüfungsumfang", level=2,
                   norms=["R. 95 Abs. 2 EPÜ", "Art. 84 EPÜ", "Art. 123 Abs. 2 EPÜ", "Art. 123 Abs. 3 EPÜ"]),
             frage("Kann L trotzdem noch beschränken?", True,
                   ["**Ja!** Die Beschränkung ist auch nach Erlöschen oder Ablauf des Patents möglich (Richtlinien D-X, 1). Sie kann sich lohnen, "
                    "weil sie nach Art. 68 EPÜ von Anfang an wirkt und damit auch Ansprüche aus der Zeit vor dem Erlöschen erfasst."],
                   merke="Auch ein erloschenes Patent lässt sich beschränken.", titel="Nach Erlöschen", level=2,
                   abwandlung="L hat die Jahresgebühren nicht mehr gezahlt; das Patent ist in allen Staaten erloschen.", norms=["Art. 68 EPÜ"]),
            ],
            abschnitt="Art. 105a Abs. 1 EPÜ: Antrag", level=1, concepts=["epc_beschraenkung"], norms=["Art. 105a Abs. 1 EPÜ"]),
        *fallkette("e01n105a-2", "Einspruch und Beschränkung kreuzen sich",
            "Der Hinweis auf die Erteilung von EP-M wird am 7.1.2026 bekannt gemacht. Die Inhaberin M beantragt am 2.3.2026 die Beschränkung "
            "und zahlt die Gebühr. Am 8.4.2026 legt W zulässig Einspruch ein.",
            [frage("War der Antrag vom 2.3.2026 zulässig, obwohl die Einspruchsfrist noch lief?", True,
                   ["**Ja!** Ausgeschlossen ist der Antrag nur, solange ein Einspruchsverfahren **anhängig** ist (Art. 105a Abs. 2 EPÜ, "
                    "R. 93 Abs. 1 EPÜ). Am 2.3.2026 hatte niemand Einspruch eingelegt; die laufende Einspruchsfrist schadet nicht."],
                   merke="Nur ein anhängiger Einspruch sperrt den Antrag.", titel="Laufende Einspruchsfrist"),
             frage("Läuft das Beschränkungsverfahren nach dem Einspruch weiter?", False,
                   ["**Nein!** Die Prüfungsabteilung stellt das Beschränkungsverfahren ein und ordnet die Rückzahlung der Beschränkungsgebühr an "
                    "(R. 93 Abs. 2 EPÜ). M kann ihre Änderungen im Einspruchsverfahren einreichen (R. 80 EPÜ)."],
                   merke="Der Einspruch verdrängt die Beschränkung.", titel="Vorrang des Einspruchs", norms=["R. 93 Abs. 2 EPÜ", "R. 80 EPÜ"],
                   concepts=["epc_einspruch"]),
             frage("Kann M während des Einspruchsverfahrens einen neuen Beschränkungsantrag stellen?", False,
                   ["**Nein!** Ein solcher Antrag gilt als nicht eingereicht; die Gebühr wird erstattet (R. 93 Abs. 1 EPÜ; Richtlinien D-X, 2.1). "
                    "Erst nach Abschluss des Einspruchsverfahrens ist der Weg wieder frei."],
                   merke="Während des Einspruchs: Änderungen nur dort.", titel="Antrag im Einspruch", level=2, norms=["R. 93 Abs. 1 EPÜ"]),
             frage("Wird auch das Widerrufsverfahren wegen des Einspruchs eingestellt?", False,
                   ["**Nein!** R. 93 Abs. 2 EPÜ gilt nur für die Beschränkung. Das Widerrufsverfahren läuft weiter; wird das Patent widerrufen, endet "
                    "der Einspruch. Erst wenn der Widerrufsantrag zurückgenommen, verworfen oder als nicht gestellt behandelt wird, geht der "
                    "Einspruch weiter (Richtlinien D-X, 7.1)."],
                   merke="Der Widerruf hat Vorrang vor dem Einspruch, die Beschränkung nicht.", titel="Widerruf statt Beschränkung", level=3,
                   abwandlung="M hatte am 2.3.2026 nicht die Beschränkung, sondern den Widerruf des Patents beantragt."),
            ],
            abschnitt="Art. 105a Abs. 2 EPÜ und R. 93 EPÜ: Vorrang des Einspruchs", level=2, concepts=["epc_beschraenkung"],
            norms=["Art. 105a Abs. 2 EPÜ", "R. 93 EPÜ"]),
        *fallkette("e01n105a-3", "Das ältere österreichische Recht",
            "Anspruch 1 von EP-S lautet „Getränk mit 2 bis 8 % Fruchtsaft“; die Beschreibung offenbart 2 bis 8 % Apfelsaft. Eine ältere "
            "österreichische Anmeldung, erst nach dem Anmeldetag von EP-S veröffentlicht, zeigt ein Getränk mit 4 % Traubensaft. Die Inhaberin "
            "will nur für Österreich beschränken auf „Getränk mit 2 bis 8 % Apfelsaft“.",
            [frage("Darf die Inhaberin im Beschränkungsverfahren eigene Ansprüche für Österreich einreichen?", True,
                   ["**Ja!** Wegen eines älteren nationalen Rechts (Art. 139 Abs. 2 EPÜ) darf das Patent für diesen Staat unterschiedliche Ansprüche "
                    "enthalten (R. 138 EPÜ). Die Inhaberin muss dem EPA das ältere Recht mitteilen; sonst wird der Antrag zurückgewiesen "
                    "(Richtlinien D-X, 10.1)."],
                   merke="Nationales älteres Recht: eigene Ansprüche für diesen Staat.", titel="Unterschiedliche Ansprüche",
                   norms=["R. 138 EPÜ", "Art. 139 Abs. 2 EPÜ"]),
             frage("Ist der vorgeschlagene Anspruch gewährbar?", False,
                   ["**Nein!** Die Obergrenze von 8 % gilt jetzt nur noch für Apfelsaft. Ein Getränk mit 5 % Apfelsaft und 5 % Traubensaft fiele unter "
                    "den neuen, nicht aber unter den erteilten Anspruch; der Schutzbereich wird erweitert (Art. 123 Abs. 3 EPÜ, R. 95 Abs. 2 EPÜ). "
                    "Die Prüfungsabteilung gibt einmal Gelegenheit zur Nachbesserung."],
                   merke="Eine scheinbare Beschränkung kann den Schutzbereich erweitern.", titel="Erweiterung des Schutzbereichs", level=3,
                   norms=["Art. 123 Abs. 3 EPÜ", "R. 95 Abs. 2 EPÜ"], concepts=["epc_schutzbereichserweiterung"],
                   ),
             frage("Darf die Inhaberin dann nur für Österreich beschränken?", False,
                   ["**Nein!** Ältere europäische Anmeldungen sind seit dem EPÜ 2000 für alle Vertragsstaaten Stand der Technik, unabhängig von den "
                    "Benennungen. Unterschiedliche Ansprüche lassen sich darauf bei Anmeldungen ab dem 13.12.2007 nicht stützen (Richtlinien D-X, 10.1)."],
                   merke="Art. 54 Abs. 3 EPÜ wirkt für alle Staaten gleich.", titel="Ältere europäische Anmeldung", level=2,
                   abwandlung="Das ältere Recht ist keine österreichische, sondern eine ältere europäische Anmeldung, die Österreich benennt.",
                   norms=["Art. 54 Abs. 3 EPÜ"], concepts=["epc_aeltere_rechte"]),
            ],
            abschnitt="R. 95 und R. 138 EPÜ: Prüfung und unterschiedliche Ansprüche", level=2, concepts=["epc_beschraenkung"], norms=["R. 95 EPÜ"]),
        *fallkette("e01n105a-4", "Der Anspruch, den der Einspruch nicht erfasste",
            "Im Einspruchsverfahren gegen EP-T war nur Anspruch 1 angegriffen; das Patent wurde mit geändertem Anspruch 1 rechtskräftig "
            "aufrechterhalten. Den unabhängigen Anspruch 3 nimmt ein Dokument nach Art. 54 Abs. 3 EPÜ vorweg. Die Inhaberin T will Anspruch 3 "
            "streichen.",
            [frage("Kann T jetzt ein Beschränkungsverfahren einleiten?", True,
                   ["**Ja!** Das Einspruchsverfahren ist abgeschlossen, Art. 105a Abs. 2 EPÜ steht nicht mehr entgegen. Gegenstand ist das Patent in "
                    "der im Einspruch geänderten Fassung (R. 90 EPÜ). Die Streichung eines Anspruchs verringert den Schutzbereich und ist eine "
                    "Beschränkung (Richtlinien D-X, 4.3.1)."],
                   merke="Nach dem Einspruch repariert die Beschränkung, was dort nicht geprüft wurde.", titel="Beschränkung nach Einspruch",
                   norms=["R. 90 EPÜ", "Art. 105a Abs. 2 EPÜ"], cases=["epc_g_9_91"]),
             frage("Wirkt die Beschränkung nur für die Zukunft?", False,
                   ["**Nein!** Soweit das Patent beschränkt wird, gelten seine Wirkungen als von Anfang an nicht eingetreten (Art. 68 EPÜ). Die "
                    "Entscheidung erfasst das Patent für alle Vertragsstaaten und wird mit der Bekanntmachung des Hinweises im Patentblatt wirksam "
                    "(Art. 105b Abs. 3 EPÜ)."],
                   merke="Beschränkung wirkt ex tunc und für alle Staaten.", titel="Wirkung", norms=["Art. 68 EPÜ", "Art. 105b Abs. 3 EPÜ"]),
             frage("Muss T noch etwas tun, wenn die Prüfungsabteilung mitteilt, dass sie dem Antrag stattgeben will?", True,
                   ["**Ja!** T muss binnen drei Monaten Übersetzungen der geänderten Ansprüche in die beiden anderen Amtssprachen einreichen "
                    "(R. 95 Abs. 3 EPÜ); versäumt sie das, kann sie es binnen zwei Monaten nach der Mitteilung darüber nachholen "
                    "(R. 82 Abs. 3 Satz 1 EPÜ). Dann beschränkt das EPA das Patent und veröffentlicht die geänderte Patentschrift (Art. 105c EPÜ)."],
                   merke="Am Ende: Übersetzungen der Ansprüche in drei Monaten.", titel="Abschluss", level=2,
                   norms=["R. 95 Abs. 3 EPÜ", "R. 82 Abs. 3 EPÜ", "Art. 105c EPÜ"]),
            ],
            abschnitt="Art. 105b und 105c EPÜ: Entscheidung und Wirkung", level=2, concepts=["epc_beschraenkung"], norms=["Art. 105b EPÜ"]),
    ]),
    # ================================================================== Art. 106 bis 112a EPÜ
    dict(id="e01n108", order=10600, titel="Art. 106 bis 112a EPÜ: Beschwerde und Überprüfungsantrag", einheiten=[
        intro("e01n108-0", "Fristen, Gebühr, Berechtigung",
              "Paper D fragt zur Beschwerde vor allem nach **Frist und Gebühr** (Art. 108 EPÜ), nach der **Rückzahlung** der Beschwerdegebühr "
              "(R. 103 EPÜ), nach der **Beschwerdeberechtigung** (Art. 107 EPÜ) und nach Rechtsbehelfen bei versäumter Frist (2016 Q1, 2018 Q4, "
              "2022 Q6, 2023 Q4). Die Beschwerdefrist ist von der Weiterbehandlung ausgeschlossen (Art. 121 Abs. 4 EPÜ); Wiedereinsetzung gibt es "
              "für Anmelder und Inhaber, für den Einsprechenden nur in die Begründungsfrist (G 1/86). R. 103 EPÜ staffelt die Rückzahlung nach dem "
              "Zeitpunkt der Rücknahme (100, 75, 50 oder 25 %). Gegen Entscheidungen der Kammern bleibt nur der Überprüfungsantrag (Art. 112a EPÜ).",
              concepts=["epc_beschwerde", "epc_ueberpruefung", "epc_wiedereinsetzung"],
              norms=["Art. 106 EPÜ", "Art. 107 EPÜ", "Art. 108 EPÜ", "Art. 109 EPÜ", "R. 103 EPÜ", "Art. 112a EPÜ"], abschnitt="Überblick"),
        schema("e01n108-0s", "Prüfungsschema Beschwerde", "epc_schema_beschwerde", abschnitt="Überblick"),
        *fallkette("e01n108-1", "Die Zurückweisung im Juni",
            "Die Prüfungsabteilung weist die Anmeldung von A in der mündlichen Verhandlung vom 9.6.2026 zurück. Die schriftliche Entscheidung ist "
            "auf den 23.6.2026 datiert und geht A am 26.6.2026 zu.",
            [frage("Bis wann muss A Beschwerde einlegen und die Gebühr zahlen?", 1,
                   ["**Bis 24.8.2026.** Die Frist beträgt zwei Monate nach Zustellung der schriftlichen Entscheidung (Art. 108 Satz 1 EPÜ). Sie gilt "
                    "als am 23.6.2026 zugestellt, weil sie binnen sieben Tagen zuging (R. 126 Abs. 2 EPÜ). Der 23.8.2026 ist ein Sonntag; die Frist "
                    "endet am Montag (R. 134 Abs. 1 EPÜ)."],
                   optionen=["9.8.2026", "24.8.2026", "26.8.2026", "3.9.2026"], merke="Maßgeblich ist die schriftliche Entscheidung, nicht die Verkündung.",
                   titel="Beschwerdefrist", norms=["R. 126 Abs. 2 EPÜ", "R. 134 Abs. 1 EPÜ"], concepts=["epc_fristen", "epc_zustellung"],
                   step=_BS + ".3"),
             frage("Bis wann muss die Beschwerdebegründung eingehen?", 1,
                   ["**Bis 23.10.2026.** Die Begründungsfrist beträgt vier Monate nach Zustellung der Entscheidung (Art. 108 Satz 3 EPÜ). Die "
                    "Verschiebung der Beschwerdefrist nach R. 134 Abs. 1 EPÜ wirkt nicht fort; der 23.10.2026 ist ein Freitag."],
                   optionen=["23.9.2026", "23.10.2026", "24.10.2026", "24.12.2026"], merke="Vier Monate ab Zustellung, nicht ab Einlegung.",
                   titel="Begründungsfrist", level=2, concepts=["epc_fristen"], step=_BS + ".4"),
             frage("Ist die Beschwerde dann unzulässig?", False,
                   ["**Nein,** sie gilt als **nicht eingelegt**, weil die Beschwerdeschrift nicht in der Frist einging; die Gebühr wird "
                    "zurückgezahlt (G 1/18). Weiterbehandlung ist für die Frist des Art. 108 EPÜ ausgeschlossen (Art. 121 Abs. 4 EPÜ); A bleibt nur "
                    "die Wiedereinsetzung (Art. 122 EPÜ)."],
                   merke="Schrift und Gebühr: beide in der Frist, sonst keine Beschwerde.", titel="Verspätete Beschwerdeschrift", level=2,
                   abwandlung="A zahlt die Gebühr am 20.8.2026, reicht die Beschwerdeschrift aber erst am 25.8.2026 ein.",
                   norms=["Art. 121 Abs. 4 EPÜ", "Art. 122 EPÜ"], cases=["epc_g_1_18"], concepts=["epc_weiterbehandlung"], step=_BS + ".3"),
            ],
            abschnitt="Art. 108 EPÜ: Frist, Gebühr, Begründung", level=1, concepts=["epc_beschwerde"], norms=["Art. 108 EPÜ"]),
        *fallkette("e01n108-2", "Die zurückgenommene Beschwerde",
            "B legt am 10.8.2026 fristgerecht Beschwerde gegen die Zurückweisung seiner Anmeldung ein und zahlt die Gebühr. Die Frist für die "
            "Beschwerdebegründung läuft bis 23.10.2026. Am 1.9.2026 nimmt B die Beschwerde zurück, ohne sie begründet zu haben.",
            [frage("In welcher Höhe wird die Beschwerdegebühr zurückgezahlt?", 0,
                   ["**In voller Höhe.** B hat die Beschwerde vor Einreichung der Begründung und vor Ablauf der Begründungsfrist zurückgenommen "
                    "(R. 103 Abs. 1 lit. b EPÜ)."],
                   optionen=["in voller Höhe", "zu 75 %", "zu 50 %", "gar nicht"], merke="Rücknahme vor der Begründung: volle Rückzahlung.",
                   titel="Rücknahme vor Begründung", norms=["R. 103 Abs. 1 EPÜ"], step=_BS + ".5"),
             frage("Wie viel erhält B, wenn er die Beschwerde drei Wochen nach Zustellung dieser Mitteilung zurücknimmt?", 1,
                   ["**75 %.** Die Rücknahme erfolgt in Erwiderung auf die Mitteilung, dass die Kammer die inhaltliche Prüfung aufnehmen will, "
                    "binnen zwei Monaten ab deren Zustellung (R. 103 Abs. 2 EPÜ). Treffen mehrere Sätze zu, gilt der höhere (R. 103 Abs. 5 EPÜ)."],
                   optionen=["in voller Höhe", "zu 75 %", "zu 50 %", "gar nicht"], merke="Ankündigung der Sachprüfung: zwei Monate für 75 %.",
                   titel="Rücknahme nach Ankündigung", level=2,
                   abwandlung="B reicht die Begründung rechtzeitig ein. Später teilt die Kammer mit, dass sie die inhaltliche Prüfung aufnehmen will.",
                   norms=["R. 103 Abs. 2 EPÜ", "R. 103 Abs. 5 EPÜ"], step=_BS + ".5"),
             frage("Und wenn B erst vier Monate nach dieser Mitteilung zurücknimmt; eine mündliche Verhandlung ist nicht anberaumt, eine Frist "
                   "zur Stellungnahme nicht gesetzt?", 2,
                   ["**50 %.** Die Begründungsfrist ist abgelaufen, die Zweimonatsfrist des R. 103 Abs. 2 EPÜ auch. Ohne Termin und ohne Aufforderung "
                    "zur Stellungnahme genügt für 50 % die Rücknahme vor Erlass der Entscheidung (R. 103 Abs. 3 lit. c EPÜ)."],
                   optionen=["in voller Höhe", "zu 75 %", "zu 50 %", "zu 25 %"], merke="Später zurückgenommen: 50 % bis zur Entscheidung, sonst 25 %.",
                   titel="Spätere Rücknahme", level=3, norms=["R. 103 Abs. 3 EPÜ"], step=_BS + ".5"),
            ],
            abschnitt="R. 103 EPÜ: Rückzahlung der Beschwerdegebühr", level=2, concepts=["epc_beschwerde", "epc_gebuehrenzahlung"], norms=["R. 103 EPÜ"]),
        *fallkette("e01n108-3", "Das übersehene Schreiben",
            "Die Prüfungsabteilung weist die Anmeldung von C zurück. Einen rechtzeitig eingereichten Hilfsantrag, der alle Einwände ausräumt, "
            "hat sie nicht berücksichtigt, weil er nicht zur Akte gelangt war. C legt Beschwerde ein, begründet sie und beantragt die "
            "Rückzahlung der Beschwerdegebühr.",
            [frage("Muss die Prüfungsabteilung der Beschwerde abhelfen?", True,
                   ["**Ja!** Hält das Organ, dessen Entscheidung angefochten ist, die Beschwerde für zulässig und begründet, muss es abhelfen "
                    "(Art. 109 Abs. 1 EPÜ), binnen drei Monaten nach Eingang der Begründung (Art. 109 Abs. 2 EPÜ). Ein übersehenes, rechtzeitig "
                    "eingereichtes Schriftstück ist ein typischer Abhilfegrund (Richtlinien E-XI, 7.1)."],
                   merke="Einseitiges Verfahren: Abhilfe binnen drei Monaten.", titel="Abhilfe", norms=["Art. 109 Abs. 1 EPÜ", "Art. 109 Abs. 2 EPÜ"],
                   step=_BS + ".5"),
             frage("Darf die Prüfungsabteilung abhelfen und den Rückzahlungsantrag zugleich zurückweisen?", False,
                   ["**Nein!** Sie ordnet die Rückzahlung an, wenn sie sie wegen eines wesentlichen Verfahrensmangels für billig hält "
                    "(R. 103 Abs. 1 lit. a EPÜ, R. 103 Abs. 6 EPÜ). Hält sie sie nicht für billig, legt sie den Antrag der Beschwerdekammer vor; "
                    "zurückweisen darf sie ihn nicht (G 3/03)."],
                   merke="Über die Ablehnung der Rückzahlung entscheidet die Kammer.", titel="Rückzahlung bei Abhilfe", level=2,
                   norms=["R. 103 Abs. 1 EPÜ", "R. 103 Abs. 6 EPÜ"], cases=["epc_g_3_03"], step=_BS + ".5"),
             frage("Darf die Einspruchsabteilung abhelfen?", False,
                   ["**Nein!** Abhilfe ist ausgeschlossen, wenn dem Beschwerdeführer ein anderer Beteiligter gegenübersteht "
                    "(Art. 109 Abs. 1 Satz 2 EPÜ). Die Einspruchsabteilung legt die Beschwerde der Kammer vor. Ausnahme: Alle Einsprüche sind "
                    "zurückgenommen (Richtlinien E-XI, 7.1)."],
                   merke="Zweiseitiges Verfahren: keine Abhilfe.", titel="Keine Abhilfe im Einspruch", level=2,
                   abwandlung="Statt einer Anmeldung geht es um ein Patent, das die Einspruchsabteilung widerrufen hat; der Einsprechende ist am Verfahren beteiligt.",
                   step=_BS + ".5"),
            ],
            abschnitt="Art. 109 EPÜ: Abhilfe", level=2, concepts=["epc_beschwerde"], norms=["Art. 109 EPÜ"]),
        *fallkette("e01n108-4", "Beide sind beschwert",
            "Die Einspruchsabteilung hält das Patent von P in geändertem Umfang aufrecht (Art. 101 Abs. 3 lit. a EPÜ). P wollte das Patent wie "
            "erteilt, die Einsprechende O den Widerruf. Nur O legt Beschwerde ein; ihr Vertreter nennt in der Beschwerdeschrift versehentlich "
            "die Muttergesellschaft Q als Beschwerdeführerin.",
            [frage("Kann P im Beschwerdeverfahren beantragen, das Patent wie erteilt aufrechtzuerhalten?", False,
                   ["**Nein!** Ohne eigene Beschwerde ist P nur Beteiligte (Art. 107 Satz 2 EPÜ). Ist die Einsprechende alleinige "
                    "Beschwerdeführerin, darf sie nicht schlechter gestellt werden; P verteidigt nur die aufrechterhaltene Fassung, ausnahmsweise "
                    "mit einschränkenden Änderungen (G 1/99)."],
                   merke="Wer nicht selbst Beschwerde einlegt, kann nicht mehr verlangen.", titel="Verbot der Schlechterstellung", level=2,
                   cases=["epc_g_1_99"], step=_BS + ".2"),
             frage("Ist die Beschwerde verloren, weil Q nicht beschwert ist?", False,
                   ["**Nein!** Der Name des Beschwerdeführers kann nach R. 101 Abs. 2 EPÜ berichtigt werden, wenn die wirkliche Absicht, für O "
                    "Beschwerde einzulegen, aus den Akten oder durch Beweise feststellbar ist (G 1/12; R. 139 EPÜ). O sollte Auftrag und Versehen "
                    "belegen."],
                   merke="Falscher Beschwerdeführer: Berichtigung nach R. 101 Abs. 2 EPÜ.", titel="Berichtigung des Beschwerdeführers", level=2,
                   norms=["R. 101 Abs. 2 EPÜ", "R. 139 EPÜ"], cases=["epc_g_1_12"], concepts=["epc_berichtigung"], step=_BS + ".4"),
             frage("Hätte O Wiedereinsetzung beantragen können, wenn sie die Beschwerdefrist trotz aller Sorgfalt versäumt hätte?", False,
                   ["**Nein!** Wiedereinsetzung steht nach Art. 122 Abs. 1 EPÜ Anmelder und Inhaber zu; in die Beschwerdefrist kann der Einsprechende "
                    "nicht wiedereingesetzt werden (T 210/89; Richtlinien E-VIII, 3.1.2). Hat er Beschwerde eingelegt, ist Wiedereinsetzung in die "
                    "Begründungsfrist möglich (G 1/86). P als Inhaberin hätte sie beantragen können."],
                   merke="Einsprechender: Wiedereinsetzung nur in die Begründungsfrist.", titel="Wiedereinsetzung des Einsprechenden", level=3,
                   norms=["Art. 122 Abs. 1 EPÜ"], cases=["epc_t_210_89", "epc_g_1_86"], concepts=["epc_wiedereinsetzung"], step=_FV + ".4.1"),
            ],
            abschnitt="Art. 107 EPÜ: Berechtigung und Beteiligung", level=2, concepts=["epc_beschwerde"], norms=["Art. 107 EPÜ"]),
        *fallkette("e01n108-5", "Das Dokument aus der Verhandlung",
            "Die Beschwerdekammer weist die Beschwerde von D zurück und stützt sich auf ein Dokument, das sie erst in der mündlichen Verhandlung "
            "eingeführt hat, ohne D Gelegenheit zur Stellungnahme zu geben. D rügt das sofort; die Kammer weist die Rüge zurück. Die "
            "schriftliche Entscheidung ist auf den 14.9.2026 datiert.",
            [frage("Kann D die Überprüfung durch die Große Beschwerdekammer beantragen?", True,
                   ["**Ja!** Ein schwerwiegender Verstoß gegen das rechtliche Gehör (Art. 113 EPÜ) ist ein Überprüfungsgrund "
                    "(Art. 112a Abs. 2 lit. c EPÜ). D hat den Mangel im Beschwerdeverfahren gerügt, wie R. 106 EPÜ verlangt. Eine bloß falsche "
                    "Sachentscheidung genügt nicht."],
                   merke="Überprüfung nur bei schweren Verfahrensmängeln, nach Rüge.", titel="Überprüfungsgrund",
                   norms=["Art. 112a Abs. 2 EPÜ", "Art. 113 EPÜ", "R. 106 EPÜ"]),
             frage("Bis wann muss D den Antrag stellen und die Gebühr zahlen?", 1,
                   ["**Bis 16.11.2026.** Die Frist beträgt zwei Monate nach Zustellung der Entscheidung (Art. 112a Abs. 4 EPÜ); der 14.11.2026 ist ein "
                    "Samstag (R. 134 Abs. 1 EPÜ). Der Antrag gilt erst mit der Gebühr als gestellt und muss die Gründe enthalten (R. 107 EPÜ)."],
                   optionen=["14.11.2026", "16.11.2026", "14.1.2027", "14.9.2031"], merke="Überprüfungsantrag: zwei Monate, mit Gebühr und Begründung.",
                   titel="Antragsfrist", level=2, norms=["Art. 112a Abs. 4 EPÜ", "R. 107 EPÜ", "R. 134 Abs. 1 EPÜ"], concepts=["epc_fristen"]),
             frage("Kann D eine versäumte Antragsfrist mit der Weiterbehandlung retten?", False,
                   ["**Nein!** Die Frist des Art. 112a Abs. 4 EPÜ ist von der Weiterbehandlung ausgeschlossen (Art. 121 Abs. 4 EPÜ). Möglich ist "
                    "die Wiedereinsetzung, beantragt binnen zwei Monaten nach Fristablauf (R. 136 Abs. 1 Satz 2 EPÜ). Der Antrag hat keine "
                    "aufschiebende Wirkung (Art. 112a Abs. 3 EPÜ)."],
                   merke="Wie bei der Priorität: Wiedereinsetzung binnen zwei Monaten nach Fristablauf.", titel="Versäumte Antragsfrist", level=2,
                   norms=["Art. 121 Abs. 4 EPÜ", "R. 136 Abs. 1 EPÜ", "Art. 112a Abs. 3 EPÜ"], concepts=["epc_wiedereinsetzung"],
                   step=_FV + ".4.2"),
            ],
            abschnitt="Art. 112a EPÜ: Überprüfungsantrag", level=2, concepts=["epc_ueberpruefung"], norms=["Art. 112a EPÜ"]),
    ]),
    # ================================================================== Art. 150 bis 152 EPÜ (internationale Phase)
    dict(id="e01n150", order=15000, titel="Art. 150 bis 152 EPÜ und PCT: die internationale Phase", einheiten=[
        intro("e01n150-0", "Das EPA als PCT-Behörde",
              "Zehn Paper-D-Fragen von 2015 bis 2025 spielen ganz oder teilweise in der internationalen Phase (2015 Q3, 2016 Q2, 2017 Q5, 2018 Q1, "
              "2019 Q3, 2021 Q5, 2023 Q2 und Q5, 2024 Q1, 2025 Q5). Das EPA ist dort Anmeldeamt, Internationale Recherchenbehörde, Behörde für "
              "die ergänzende Recherche und für die vorläufige Prüfung (Art. 151 EPÜ, Art. 152 EPÜ); der PCT geht dem EPÜ vor "
              "(Art. 150 Abs. 2 EPÜ). Typische Fragen: Ist das EPA als Anmeldeamt zuständig? Bleibt der Anmeldetag, wenn Teile fehlen? Bis wann "
              "lässt sich eine Priorität hinzufügen oder wiederherstellen? Welche Fristen gelten für ergänzende Recherche, Antrag auf "
              "vorläufige Prüfung und Änderungen?",
              concepts=["epc_pct_international", "epc_euro_pct"], norms=["Art. 150 EPÜ", "Art. 151 EPÜ", "Art. 152 EPÜ"], abschnitt="Überblick"),
        *fallkette("e01n150-1", "Die Portugiesin in Brasilien",
            "Ana, portugiesische Staatsangehörige mit Wohnsitz in Brasilien, und die brasilianische Firma Tecno wollen gemeinsam eine "
            "internationale Anmeldung auf Englisch beim EPA einreichen. Ana ist zugleich die Erfinderin.",
            [frage("Ist das EPA als Anmeldeamt zuständig?", True,
                   ["**Ja!** Es genügt, dass ein Anmelder Staatsangehöriger oder Ansässiger eines EPÜ-Vertragsstaats ist (R. 19.1 PCT, "
                    "R. 157 Abs. 1 EPÜ); Ana ist Portugiesin. Die Anmeldung ist zudem auf Englisch abgefasst (R. 157 Abs. 2 EPÜ; Richtlinien "
                    "PCT-EPA A-II, 2)."],
                   merke="Ein Anmelder aus einem EPÜ-Staat genügt.", titel="Zuständigkeit", norms=["R. 157 EPÜ"]),
             frage("Bleibt das EPA zuständig, wenn die Anmeldung auf Portugiesisch eingereicht wird?", False,
                   ["**Nein!** Als Anmeldeamt nimmt das EPA nur Deutsch, Englisch oder Französisch an (R. 157 Abs. 2 EPÜ). Es leitet die Anmeldung "
                    "an das Internationale Büro als Anmeldeamt weiter; als Eingangstag gilt der Tag des Eingangs beim EPA (R. 19.4 PCT)."],
                   merke="Falsche Sprache: Weiterleitung an das Internationale Büro, Tag bleibt.", titel="Sprache", level=2,
                   norms=["R. 157 EPÜ"], concepts=["epc_sprachen"]),
             frage("Ist das EPA jetzt als Anmeldeamt zuständig?", False,
                   ["**Nein!** Wer nur als Erfinder genannt ist, ist kein Anmelder; seine Staatsangehörigkeit zählt nicht (Richtlinien PCT-EPA A-II, 2). "
                    "Tecno ist weder Staatsangehörige noch Ansässige eines EPÜ-Staats. Das EPA leitet die Anmeldung an das Internationale Büro weiter "
                    "(R. 19.4 PCT)."],
                   merke="Der Erfinder allein begründet keine Zuständigkeit.", titel="Nur Erfinderin", level=2,
                   abwandlung="Ana wird im Antrag nur als Erfinderin genannt; Anmelderin ist allein Tecno."),
            ],
            abschnitt="Art. 151 EPÜ: das EPA als Anmeldeamt", level=1, concepts=["epc_pct_international"], norms=["Art. 151 EPÜ"]),
        *fallkette("e01n150-2", "Die fehlende Seite",
            "F reicht am letzten Tag des Prioritätsjahres die internationale Anmeldung PCT-F mit dem Formblatt PCT/RO/101 beim EPA ein und "
            "beansprucht die Priorität der französischen Anmeldung FR-F. Eine Woche später bemerkt F, dass die zweite Seite der Ansprüche fehlt. "
            "FR-F enthält sie wortgleich.",
            [frage("Kann F die Seite nachreichen, ohne den Anmeldetag zu verlieren?", True,
                   ["**Ja,** durch Einbeziehung durch Verweis: Das Formblatt enthält die Erklärung nach R. 4.18 PCT, und der fehlende Teil steht "
                    "vollständig in FR-F. Bestätigt F die Einbeziehung fristgerecht (R. 20.6 PCT), bleibt der Anmeldetag (Richtlinien PCT-EPA A-II, 5)."],
                   merke="Fehlender Teil im Prioritätsdokument: Einbeziehung ohne Datumsverlust.", titel="Einbeziehung durch Verweis",
                   concepts=["epc_fehlende_teile", "epc_anmeldetag"]),
             frage("Ändert sich der Anmeldetag, wenn der nachgereichte Teil nicht in FR-F steht?", True,
                   ["**Ja!** Ohne Grundlage im Prioritätsdokument kann F fehlende Teile nur nach R. 20.5 PCT nachreichen; Anmeldetag wird dann der Tag "
                    "ihres Eingangs (Richtlinien PCT-EPA A-II, 5). Er liegt hier nach dem Ende des Prioritätsjahres."],
                   merke="Ohne Grundlage in der Priorität wandert der Anmeldetag.", titel="Nachreichen ohne Grundlage", level=2,
                   concepts=["epc_fehlende_teile"]),
             frage("Kann F einen offensichtlichen Schreibfehler in Anspruch 3 berichtigen lassen?", True,
                   ["**Ja,** nach R. 91.1 PCT, wenn Fehler und Berichtigung für den Fachmann offensichtlich sind. Für Beschreibung, Ansprüche und "
                    "Zeichnungen entscheidet die Recherchen- oder Prüfungsbehörde, für den Antrag das Anmeldeamt; der Antrag ist binnen 26 Monaten ab "
                    "dem Prioritätstag zu stellen (Richtlinien PCT-EPA H-IV, 2.1 und 2.2)."],
                   merke="Offensichtliche Fehler: R. 91.1 PCT, 26 Monate.", titel="Berichtigung", level=2, concepts=["epc_berichtigung"]),
             frage("Kann F trotzdem den ursprünglichen Eingangstag als Anmeldetag behalten?", True,
                   ["**Ja!** Ohne Ansprüche fehlt eine Voraussetzung des Art. 11 PCT. Auch ein ganzes Element lässt sich aber durch Verweis einbeziehen, "
                    "wenn es vollständig im Prioritätsdokument steht und F das fristgerecht bestätigt (R. 20.6 PCT). Anders als nach R. 40 Abs. 1 EPÜ "
                    "braucht der PCT-Anmeldetag Ansprüche."],
                   merke="PCT: ohne Ansprüche kein Anmeldetag, außer per Verweis.", titel="Keine Ansprüche", level=3,
                   abwandlung="F hat überhaupt keine Ansprüche eingereicht.", norms=["R. 40 Abs. 1 EPÜ"], concepts=["epc_anmeldetag"]),
            ],
            abschnitt="Art. 11 PCT: Anmeldetag und fehlende Teile", level=2, concepts=["epc_pct_international"], norms=["Art. 151 EPÜ"]),
        *fallkette("e01n150-3", "Die vergessene zweite Priorität",
            "G reicht am Samstag, 8.3.2025, elektronisch die französische Anmeldung FR2 ein und am 20.3.2025 FR1. Am Montag, 9.3.2026, reicht G "
            "beim EPA die internationale Anmeldung PCT-G ein und beansprucht nur FR1. FR2 hat G vergessen.",
            [frage("Liegt PCT-G für FR2 noch innerhalb des Prioritätsjahres?", True,
                   ["**Ja!** Das Prioritätsjahr endete am Sonntag, 8.3.2026. Ist das Amt an diesem Tag geschlossen, verlängert sich die Frist auf den "
                    "nächsten Tag, an dem es geöffnet ist (R. 80.5 PCT; Richtlinien PCT-EPA A-VI, 1.2)."],
                   merke="Fristende am Wochenende: nächster Arbeitstag, auch für das Prioritätsjahr.", titel="Prioritätsjahr",
                   concepts=["epc_fristen"]),
             frage("Bis wann kann G den Prioritätsanspruch für FR2 hinzufügen?", 1,
                   ["**Bis 9.7.2026.** Maßgeblich sind 16 Monate ab dem Prioritätstag; ändert er sich, gilt die zuerst ablaufende Frist, hier 16 Monate "
                    "ab FR2 (8.7.2026). Jedenfalls reichen aber vier Monate ab dem internationalen Anmeldetag (R. 26bis.1 PCT; Richtlinien PCT-EPA "
                    "A-VI, 1.4.1)."],
                   optionen=["8.7.2026", "9.7.2026", "20.7.2026", "9.5.2026"], merke="Hinzufügen: 16 Monate, mindestens vier Monate ab Anmeldetag.",
                   titel="Prioritätsanspruch hinzufügen", level=3),
             frage("Bis wann muss G danach in die europäische Phase eintreten?", 0,
                   ["**Bis 8.10.2027.** Die 31 Monate rechnen ab dem frühesten Prioritätstag (R. 159 Abs. 1 EPÜ), mit dem Hinzufügen also ab FR2. Der "
                    "8.10.2027 ist ein Freitag."],
                   optionen=["8.10.2027", "20.10.2027", "9.10.2028", "8.9.2027"], merke="Neue frühere Priorität, frühere Eintrittsfrist.",
                   titel="Folge für die 31-Monatsfrist", level=2, norms=["R. 159 Abs. 1 EPÜ"], concepts=["epc_euro_pct"]),
            ],
            abschnitt="R. 26bis PCT: Prioritätsanspruch", level=2, concepts=["epc_prioritaet", "epc_pct_international"], norms=["Art. 150 EPÜ"]),
        *fallkette("e01n150-4", "Fünf Tage zu spät",
            "H reicht am 10.6.2025 die US-Anmeldung US-H ein. Wegen eines einmaligen Versehens einer erfahrenen Assistentin in einem sonst "
            "zuverlässigen Fristensystem geht die internationale Anmeldung PCT-H mit Anspruch auf diese Priorität erst am 15.6.2026 beim EPA als "
            "Anmeldeamt ein.",
            [frage("Ist der Prioritätsanspruch in der internationalen Phase nichtig?", False,
                   ["**Nein!** PCT-H ging innerhalb von zwei Monaten nach Ablauf des Prioritätsjahres (10.6.2026) ein. Der Anspruch gilt in der "
                    "internationalen Phase nicht als nichtig und bleibt Grundlage der Fristberechnung (R. 26bis.2 PCT; Richtlinien PCT-EPA A-VI, 1.5)."],
                   merke="Bis zwei Monate zu spät: Priorität bleibt für die Fristen.", titel="Kein nichtiger Anspruch", level=2),
             frage("Kann H die Wiederherstellung beim EPA als Anmeldeamt erreichen?", True,
                   ["**Ja!** Antrag mit Begründung und Gebühr binnen zwei Monaten nach Ablauf des Prioritätsjahres, also bis 10.8.2026 "
                    "(R. 26bis.3 PCT). Das EPA wendet nur den Maßstab der gebotenen Sorgfalt an, wie bei Art. 122 EPÜ; ein einmaliges Versehen in einem "
                    "sonst zuverlässigen System genügt (Richtlinien PCT-EPA A-VI, 1.5)."],
                   merke="EPA als Anmeldeamt: Wiederherstellung nur bei gebotener Sorgfalt.", titel="Wiederherstellung",
                   norms=["Art. 122 EPÜ"], concepts=["epc_wiedereinsetzung"]),
             frage("Muss H beim Eintritt in die europäische Phase erneut die Wiederherstellung beantragen?", False,
                   ["**Nein!** Stellt das EPA als Anmeldeamt die Priorität nach dem Sorgfaltsmaßstab wieder her, wirkt das auch vor dem EPA als "
                    "Bestimmungsamt (R. 49ter.1 PCT; Richtlinien A-XV, 5)."],
                   merke="Sorgfaltsmaßstab beim Anmeldeamt: bindet das EPA als Bestimmungsamt.", titel="Wirkung in der europäischen Phase", level=2,
                   concepts=["epc_euro_pct"]),
             frage("Wirkt diese Wiederherstellung vor dem EPA?", False,
                   ["**Nein!** Das EPA erkennt nur Wiederherstellungen nach dem Sorgfaltsmaßstab an. H muss binnen eines Monats nach Ablauf der "
                    "31-Monatsfrist beim EPA als Bestimmungsamt erneut einen begründeten Antrag stellen und die Gebühr zahlen (R. 49ter.2 PCT; "
                    "Richtlinien A-XV, 5)."],
                   merke="„Unabsichtlich“ genügt dem EPA nicht.", titel="Unabsichtlichkeit genügt nicht", level=3,
                   abwandlung="H reicht PCT-H beim US-Amt ein; dieses stellt die Priorität nur nach dem Maßstab der Unabsichtlichkeit wieder her.",
                   norms=["R. 159 Abs. 1 EPÜ"], concepts=["epc_euro_pct"]),
            ],
            abschnitt="R. 26bis.3 PCT: Wiederherstellung der Priorität", level=2, concepts=["epc_prioritaet", "epc_pct_international"],
            norms=["Art. 151 EPÜ"]),
        *fallkette("e01n150-5", "Erfindung D soll geprüft werden",
            "I reicht am 4.8.2025 ohne Priorität die internationale Anmeldung PCT-I auf Englisch beim schwedischen Amt ein, das auch Internationale "
            "Recherchenbehörde ist. PCT-I beansprucht die uneinheitlichen Erfindungen C und D. Das schwedische Amt recherchiert nur C, weil I "
            "keine zusätzliche Gebühr zahlt. I will D vom EPA prüfen lassen.",
            [frage("Kann das EPA als Behörde für die vorläufige Prüfung D prüfen, obwohl D nicht recherchiert ist?", False,
                   ["**Nein!** Das EPA als Behörde für die vorläufige Prüfung prüft keine Ansprüche, zu denen keine Recherche durchgeführt wurde "
                    "(R. 66.1 PCT; Richtlinien PCT-EPA C-IV, 1.1). Zuständig wäre das EPA, weil das schwedische Amt recherchiert hat (Richtlinien PCT-EPA C-II, 2)."],
                   merke="Keine Prüfung ohne Recherche.", titel="Prüfung ohne Recherche", level=2, norms=["Art. 152 EPÜ"],
                   concepts=["epc_einheitlichkeit"]),
             frage("Bis wann kann I beim Internationalen Büro eine ergänzende internationale Recherche zu D durch das EPA beantragen?", 0,
                   ["**Bis 4.6.2027.** Der Antrag ist binnen 22 Monaten ab dem Prioritätstag, hier dem Anmeldetag, zu stellen (R. 45bis.1 PCT). I gibt "
                    "an, dass D recherchiert werden soll; das EPA folgt dem, wenn es die Uneinheitlichkeit ebenso sieht (Richtlinien PCT-EPA B-XII, 10.3)."],
                   optionen=["4.6.2027", "4.8.2027", "4.2.2027", "4.12.2026"], merke="Ergänzende Recherche: 22 Monate, beim Internationalen Büro.",
                   titel="Ergänzende Recherche", level=2, norms=["Art. 152 EPÜ"], concepts=["epc_einheitlichkeit"]),
             frage("Kann I mit Änderungen nach Art. 19 PCT auch die Beschreibung ändern?", False,
                   ["**Nein!** Art. 19 PCT erlaubt nach Erhalt des Recherchenberichts nur Änderungen der Ansprüche, beim Internationalen Büro. "
                    "Beschreibung und Zeichnungen lassen sich erst in der vorläufigen Prüfung nach Art. 34 PCT ändern (Richtlinien PCT-EPA H-I, 3)."],
                   merke="Art. 19 PCT: nur Ansprüche; Art. 34 PCT: alles.", titel="Änderungen", level=1),
             frage("Muss I den Antrag auf vorläufige Prüfung spätestens 22 Monate nach dem Prioritätstag stellen?", False,
                   ["**Nein,** nicht zwingend: Maßgeblich ist die später ablaufende von zwei Fristen, drei Monate nach Übermittlung des "
                    "Recherchenberichts oder 22 Monate ab dem Prioritätstag (R. 54bis.1 PCT). Ein verspäteter Antrag gilt als nicht gestellt "
                    "(Richtlinien PCT-EPA C-II, 1.1)."],
                   merke="Antrag auf vorläufige Prüfung: die später ablaufende Frist zählt.", titel="Antrag auf vorläufige Prüfung", level=2,
                   concepts=["epc_fristen"]),
            ],
            abschnitt="R. 45bis und R. 54bis PCT: ergänzende Recherche, vorläufige Prüfung, Änderungen", level=2, concepts=["epc_pct_international"],
            norms=["Art. 152 EPÜ"]),
    ]),
    # ================================================================== Art. 153 EPÜ, R. 159 bis 165 EPÜ
    dict(id="e01n153", order=15300, titel="Art. 153 EPÜ, R. 159 bis 165 EPÜ: Euro-PCT", einheiten=[
        intro("e01n153-0", "31 Monate und was danach kommt",
              "Der Eintritt einer PCT-Anmeldung in die europäische Phase gehört zum Kernstoff von Paper D (2016 Q3, 2017 Q1, 2021 Q2, 2022 Q3, "
              "2025 Q1). Eine internationale Anmeldung mit Anmeldetag wirkt als europäische Anmeldung (Art. 153 Abs. 2 EPÜ). Bearbeitet wird sie "
              "aber erst, wenn der Anmelder binnen **31 Monaten** ab dem frühesten Prioritätstag die Handlungen der R. 159 Abs. 1 EPÜ vornimmt, "
              "oder früher auf ausdrücklichen Antrag (Art. 23 Abs. 2 PCT). Versäumnisse heilt die Weiterbehandlung (R. 160 EPÜ). Nach dem Eintritt "
              "folgen R. 161 und R. 162 EPÜ, bei Uneinheitlichkeit R. 164 EPÜ. Eine Teilanmeldung setzt den wirksamen Eintritt voraus (J 18/09).",
              concepts=["epc_euro_pct", "epc_einheitlichkeit", "epc_weiterbehandlung"],
              norms=["Art. 153 EPÜ", "R. 159 EPÜ", "R. 160 EPÜ", "R. 161 EPÜ", "R. 162 EPÜ", "R. 164 EPÜ"], cases=["epc_j_18_09"],
              abschnitt="Überblick"),
        schema("e01n153-0s", "Prüfungsschema Euro-PCT", "epc_schema_euro_pct", abschnitt="Überblick"),
        *fallkette("e01n153-1", "Die japanische PCT-Anmeldung",
            "K reicht am 9.4.2025 eine japanische Anmeldung ein und am 7.4.2026 unter deren Priorität die internationale Anmeldung PCT-K auf "
            "Japanisch beim japanischen Amt. PCT-K wird auf Japanisch veröffentlicht. K will ein europäisches Patent.",
            [frage("Bis wann muss K die Handlungen nach R. 159 Abs. 1 EPÜ vornehmen?", 1,
                   ["**Bis 9.11.2027.** Die Frist beträgt 31 Monate ab dem Prioritätstag, nicht ab dem internationalen Anmeldetag "
                    "(R. 159 Abs. 1 EPÜ, R. 131 Abs. 4 EPÜ). Der 9.11.2027 ist ein Dienstag."],
                   optionen=["9.10.2027", "9.11.2027", "7.11.2028", "7.11.2027"], merke="31 Monate ab dem frühesten Prioritätstag.",
                   titel="31-Monatsfrist", norms=["R. 131 Abs. 4 EPÜ"], concepts=["epc_fristen"], step=_EP + ".1"),
             frage("Muss K eine Übersetzung einreichen?", True,
                   ["**Ja!** PCT-K ist nicht in einer Amtssprache des EPA veröffentlicht. K muss eine Übersetzung ins Deutsche, Englische oder "
                    "Französische einreichen (Art. 153 Abs. 4 EPÜ, R. 159 Abs. 1 lit. a EPÜ); diese Sprache wird Verfahrenssprache. Daneben zahlt K "
                    "die fälligen Gebühren und stellt den Prüfungsantrag (R. 159 Abs. 1 EPÜ)."],
                   merke="Nicht in Amtssprache veröffentlicht: Übersetzung binnen 31 Monaten.", titel="Übersetzung",
                   norms=["Art. 153 Abs. 4 EPÜ"], concepts=["epc_sprachen"], step=_EP + ".2"),
             frage("K lässt die Frist verstreichen; das EPA teilt mit, die Anmeldung gelte als zurückgenommen. Kann K das heilen?", True,
                   ["**Ja,** mit der Weiterbehandlung: binnen zwei Monaten nach der Mitteilung (R. 160 Abs. 2 EPÜ, R. 112 Abs. 1 EPÜ) die "
                    "Weiterbehandlungsgebühr zahlen und Übersetzung, Gebühren und Prüfungsantrag nachholen (Art. 121 EPÜ, R. 135 Abs. 1 EPÜ; "
                    "Richtlinien A-XIII, 3.3)."],
                   merke="Versäumter Eintritt: Weiterbehandlung.", titel="Versäumnis", level=2,
                   norms=["R. 160 EPÜ", "Art. 121 EPÜ", "R. 135 Abs. 1 EPÜ"], concepts=["epc_weiterbehandlung"], step=_EP + ".3"),
             frage("K zahlt nur die Anmeldegebühr und reicht nie eine Übersetzung ein. Ist PCT-K älteres Recht nach Art. 54 Abs. 3 EPÜ gegen "
                   "spätere europäische Anmeldungen?", False,
                   ["**Nein!** Als Stand der Technik nach Art. 54 Abs. 3 EPÜ gilt die Euro-PCT-Anmeldung nur, wenn die Übersetzung nach "
                    "Art. 153 Abs. 4 EPÜ vorliegt **und** die Anmeldegebühr gezahlt ist (Art. 153 Abs. 5 EPÜ, R. 165 EPÜ). Bei japanischer "
                    "Veröffentlichung genügt die Zahlung allein nicht."],
                   merke="R. 165 EPÜ: Übersetzung und Anmeldegebühr.", titel="Älteres Recht", level=3,
                   norms=["Art. 153 Abs. 5 EPÜ", "R. 165 EPÜ", "Art. 54 Abs. 3 EPÜ"], concepts=["epc_aeltere_rechte"], step=_EP + ".4"),
            ],
            abschnitt="R. 159 Abs. 1 EPÜ und R. 160 EPÜ: Eintritt und Versäumnis", level=1, concepts=["epc_euro_pct"], norms=["R. 159 Abs. 1 EPÜ"]),
        *fallkette("e01n153-2", "Russisch und eilig",
            "R reicht am 3.2.2025 ohne Priorität die internationale Anmeldung PCT-R auf Russisch beim russischen Amt ein; sie wird am 13.8.2026 "
            "mit dem Recherchenbericht auf Russisch veröffentlicht. Am 15.10.2026 beantragt R beim EPA ausdrücklich die sofortige Bearbeitung und "
            "zahlt Anmelde- und Recherchengebühr.",
            [frage("Ist der Antrag am 15.10.2026 wirksam?", False,
                   ["**Nein!** Die vorzeitige Bearbeitung (Art. 23 Abs. 2 PCT, Art. 40 Abs. 2 PCT) wird erst wirksam, wenn die Erfordernisse der "
                    "R. 159 Abs. 1 EPÜ erfüllt sind, als liefe die 31-Monatsfrist an diesem Tag ab. Die Übersetzung nach Art. 153 Abs. 4 EPÜ ist stets "
                    "nötig; sie fehlt (Richtlinien A-XII, 7.1)."],
                   merke="Vorzeitige Bearbeitung: Übersetzung, Anmelde- und gegebenenfalls Recherchengebühr immer.", titel="Wirksamkeit des Antrags", level=2,
                   norms=["Art. 153 Abs. 4 EPÜ"], step=_EP + ".1"),
             frage("Muss R mit dem Antrag auch den Prüfungsantrag stellen?", False,
                   ["**Nein,** nicht am 15.10.2026: Die Frist nach R. 70 Abs. 1 EPÜ läuft noch; sie endet sechs Monate nach Veröffentlichung des "
                    "internationalen Recherchenberichts (Art. 153 Abs. 6 EPÜ). Prüfungsantrag, Benennungs- und Jahresgebühr sind nur nötig, wenn ihre "
                    "Fristen schon abgelaufen sind (R. 159 Abs. 1 EPÜ; Richtlinien A-XII, 7.1)."],
                   merke="Nur bereits abgelaufene Fristen sind sofort zu erfüllen.", titel="Prüfungsantrag", level=3,
                   norms=["R. 70 Abs. 1 EPÜ", "Art. 153 Abs. 6 EPÜ"], step=_EP + ".2"),
             frage("Kann R ab diesem Tag eine Teilanmeldung einreichen?", True,
                   ["**Ja!** Mit der wirksamen vorzeitigen Bearbeitung ist die Anmeldung vor dem EPA anhängig; ab diesem Tag ist eine Teilanmeldung "
                    "möglich (Richtlinien A-XIII, 9.1.2). Vor dem wirksamen Eintritt ist sie es nicht (J 18/09)."],
                   merke="Teilanmeldung erst nach wirksamem Eintritt.", titel="Teilanmeldung", level=2,
                   abwandlung="R reicht die Übersetzung nach; der Antrag wird wirksam.",
                   norms=["R. 36 Abs. 1 EPÜ"], cases=["epc_j_18_09"], concepts=["epc_teilanmeldung", "epc_anhaengigkeit"]),
            ],
            abschnitt="Art. 23 Abs. 2 PCT: vorzeitige Bearbeitung", level=2, concepts=["epc_euro_pct"], norms=["Art. 153 EPÜ"]),
        *fallkette("e01n153-3", "Zwei Erfindungen, eine Recherche",
            "U reicht PCT-U beim EPA als Anmeldeamt ein. Das EPA als Internationale Recherchenbehörde hält die Erfindungen X und Y für "
            "uneinheitlich; U zahlt keine zusätzliche Recherchengebühr, recherchiert wird nur X. Beim Eintritt in die europäische Phase richtet U "
            "die Ansprüche nur auf Y.",
            [frage("Erstellt das EPA einen ergänzenden europäischen Recherchenbericht?", False,
                   ["**Nein!** War das EPA Internationale Recherchenbehörde, entfällt der ergänzende europäische Recherchenbericht "
                    "(Art. 153 Abs. 7 EPÜ; Richtlinien B-II, 4.3.1). Eine Recherchengebühr nach R. 159 Abs. 1 lit. e EPÜ fällt nicht an."],
                   merke="EPA als ISA: keine ergänzende europäische Recherche.", titel="Ergänzende Recherche",
                   norms=["Art. 153 Abs. 7 EPÜ"], step=_EP + ".2"),
             frage("Prüft die Prüfungsabteilung Y ohne weitere Gebühr?", False,
                   ["**Nein!** Für Y liegt keine Recherche des EPA vor. Die Prüfungsabteilung fordert U auf, binnen zwei Monaten eine Recherchengebühr "
                    "für Y zu zahlen (R. 164 Abs. 2 lit. a EPÜ). Zahlt U, wird Y recherchiert und geprüft; sonst muss U auf X beschränken "
                    "(R. 164 Abs. 2 EPÜ)."],
                   merke="Nicht recherchierte Erfindung: Gebühr nach R. 164 Abs. 2 EPÜ.", titel="Nicht recherchierte Erfindung", level=2,
                   norms=["R. 164 Abs. 2 EPÜ"], step=_EP + ".4"),
             frage("Kann U Y trotzdem weiterverfolgen, wenn er die Gebühr nicht zahlt?", True,
                   ["**Ja,** mit einer Teilanmeldung (Art. 76 EPÜ), solange die Euro-PCT-Anmeldung anhängig ist; dort wird Y gegen eine eigene "
                    "Recherchengebühr recherchiert. Die Euro-PCT-Anmeldung selbst bleibt auf X beschränkt."],
                   merke="Uneinheitlich: Teilanmeldung für den Rest.", titel="Teilanmeldung", level=2,
                   norms=["Art. 76 EPÜ"], concepts=["epc_teilanmeldung"]),
             frage("Gilt dann für Y dasselbe?", True,
                   ["**Ja!** Auch nach einer ergänzenden internationalen Recherche durch das EPA entfällt der ergänzende europäische Recherchenbericht "
                    "(Richtlinien B-II, 4.3.1). R. 164 Abs. 2 EPÜ erfasst ausdrücklich auch Erfindungen, die das EPA als Behörde für die ergänzende "
                    "Recherche nicht recherchiert hat."],
                   merke="EPA als SISA steht dem EPA als ISA gleich.", titel="EPA als Behörde für die ergänzende Recherche", level=3,
                   abwandlung="Internationale Recherchenbehörde war das chinesische Amt; das EPA hat als Behörde für die ergänzende Recherche nur X recherchiert.",
                   norms=["R. 164 Abs. 2 EPÜ"], step=_EP + ".4"),
            ],
            abschnitt="R. 164 EPÜ: Einheitlichkeit", level=2, concepts=["epc_einheitlichkeit", "epc_euro_pct"], norms=["R. 164 EPÜ"]),
        *fallkette("e01n153-4", "Der negative Bescheid",
            "V reicht PCT-V auf Englisch beim EPA ein; das EPA als Internationale Recherchenbehörde verneint im schriftlichen Bescheid die "
            "Neuheit. V leitet mit 22 Ansprüchen die europäische Phase ein und zahlt keine Anspruchsgebühren. Das EPA erlässt die Mitteilung nach "
            "R. 161 Abs. 1 EPÜ und R. 162 EPÜ.",
            [frage("Muss V auf den schriftlichen Bescheid reagieren?", True,
                   ["**Ja!** Hat das EPA als Internationale Recherchenbehörde Mängel festgestellt, muss V binnen sechs Monaten nach der Mitteilung "
                    "Stellung nehmen oder ändern. Tut er keines von beiden, gilt die Anmeldung als zurückgenommen (R. 161 Abs. 1 EPÜ); dagegen hilft "
                    "die Weiterbehandlung."],
                   merke="Negativer WO-ISA des EPA: Pflichterwiderung in sechs Monaten.", titel="Erwiderung nach R. 161 EPÜ", level=2,
                   norms=["R. 161 Abs. 1 EPÜ"], step=_EP + ".4"),
             frage("Muss V Anspruchsgebühren für sieben Ansprüche zahlen, wenn er innerhalb der Sechsmonatsfrist auf 15 Ansprüche beschränkt?", False,
                   ["**Nein!** Nicht gezahlte Anspruchsgebühren können noch in der Frist nach R. 161 Abs. 1 EPÜ gezahlt werden; reicht V darin "
                    "geänderte Ansprüche ein, berechnen sie sich nach diesen (R. 162 Abs. 2 EPÜ). Bei 15 Ansprüchen fällt keine an. Nicht gezahlte "
                    "Gebühren gelten als Verzicht auf den Anspruch (R. 162 Abs. 4 EPÜ)."],
                   merke="Anspruchsgebühren nach der Fassung am Ende der Sechsmonatsfrist.", titel="Anspruchsgebühren", level=2,
                   norms=["R. 162 Abs. 2 EPÜ", "R. 162 Abs. 4 EPÜ"], step=_EP + ".4"),
             frage("Kann V beim Eintritt eine französische Übersetzung einreichen, damit das Verfahren auf Französisch geführt wird?", False,
                   ["**Nein!** PCT-V ist auf Englisch veröffentlicht; Englisch ist Verfahrenssprache. Eine Übersetzung in eine andere Amtssprache ist "
                    "nicht vorgesehen (G 4/08; Art. 14 Abs. 3 EPÜ)."],
                   merke="In Amtssprache veröffentlicht: diese Sprache bleibt.", titel="Verfahrenssprache", level=2,
                   norms=["Art. 14 Abs. 3 EPÜ"], cases=["epc_g_4_08"], concepts=["epc_sprachen"], step=_EP + ".2"),
            ],
            abschnitt="R. 161 und R. 162 EPÜ: nach dem Eintritt", level=2, concepts=["epc_euro_pct"], norms=["R. 161 EPÜ", "R. 162 EPÜ"]),
        *fallkette("e01n153-5", "Die zurückgenommene Priorität",
            "B reicht am 12.11.2024 die europäische Anmeldung EP-B ein. Am 12.11.2025 reichen die Deutschen A und B gemeinsam PCT-AB beim EPA ein "
            "und beanspruchen die Priorität von EP-B. Am 2.3.2026 wollen sie den Eintritt in die europäische Phase so weit wie möglich "
            "hinausschieben.",
            [frage("Können A und B den Eintritt verschieben, indem sie den Prioritätsanspruch zurücknehmen?", True,
                   ["**Ja!** Die Rücknahme ist bis 30 Monate nach dem Prioritätstag möglich (R. 90bis.3 PCT). Noch nicht abgelaufene Fristen rechnen "
                    "dann vom neuen Prioritätstag, hier dem Anmeldetag: Die 31-Monatsfrist (R. 159 Abs. 1 EPÜ) endet erst am 12.6.2028 statt im Juni "
                    "2027 (Richtlinien PCT-EPA A-IV, 2.4)."],
                   merke="Priorität zurücknehmen verschiebt alle offenen Fristen.", titel="Rücknahme der Priorität", level=2,
                   norms=["R. 159 Abs. 1 EPÜ"], step=_EP + ".1"),
             frage("Genügt es, wenn B allein die Rücknahme erklärt?", False,
                   ["**Nein!** Die Rücknahme müssen alle Anmelder unterschreiben, oder ein bestellter Anwalt oder gemeinsamer Vertreter. Der nur "
                    "fiktive gemeinsame Vertreter (der erstgenannte Anmelder) genügt nicht (R. 90bis.5 PCT; Richtlinien PCT-EPA A-IV, 2.1)."],
                   merke="Rücknahmen: alle Anmelder unterschreiben.", titel="Unterschrift", level=2, concepts=["epc_vertretung"]),
             frage("Kann EP-B der Euro-PCT-Anmeldung nach der Rücknahme der Priorität schaden?", True,
                   ["**Ja!** EP-B wird um Mai 2026 veröffentlicht und ist dann gegenüber PCT-AB, deren maßgeblicher Tag jetzt der 12.11.2025 ist, "
                    "Stand der Technik nach Art. 54 Abs. 3 EPÜ. B sollte EP-B vor Abschluss der technischen Vorbereitungen für die Veröffentlichung "
                    "zurücknehmen."],
                   merke="Ohne Priorität wird die eigene Erstanmeldung zum älteren Recht.", titel="Eigene ältere Anmeldung", level=3,
                   norms=["Art. 54 Abs. 3 EPÜ"], concepts=["epc_aeltere_rechte", "epc_prioritaet"]),
             frage("Wirkt die Rücknahme der Priorität dann noch für die europäische Phase?", False,
                   ["**Nein!** Mit der wirksamen vorzeitigen Bearbeitung endet die internationale Phase gegenüber dem EPA; eine spätere Rücknahme "
                    "nach R. 90bis PCT bleibt dort ohne Wirkung (R. 90bis.6 PCT; Richtlinien A-XII, 7.1)."],
                   merke="Nach wirksamem Eintritt helfen PCT-Rücknahmen in Europa nicht mehr.", titel="Nach vorzeitiger Bearbeitung", level=3,
                   abwandlung="A und B hatten vorher schon wirksam die vorzeitige Bearbeitung beim EPA beantragt.", step=_EP + ".1"),
            ],
            abschnitt="Art. 153 EPÜ: Priorität und Eintrittszeitpunkt", level=2, concepts=["epc_euro_pct", "epc_prioritaet"], norms=["Art. 153 EPÜ"]),
    ]),
]
