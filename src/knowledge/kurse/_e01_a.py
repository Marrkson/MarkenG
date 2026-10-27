# -*- coding: utf-8 -*-
"""Kapitel des Normkurses e01 (siehe e01_epue_paper_d.py): Art. 14 EPÜ (Sprachen), Art. 60, 61 EPÜ (Recht auf das Patent), Art. 64, 65 EPÜ
(Validierung und Einheitspatent), Art. 76 EPÜ (Teilanmeldung) und Art. 80 EPÜ (Anmeldetag, fehlende Teile). `order` = Artikel × 100."""
from ._helpers import intro, schema, frage, fallkette

_FV = "step:epc_schema_fristversaeumnis"
_TA = "step:epc_schema_teilanmeldung"

KAPITEL = [
    # ================================================================== Art. 14 EPÜ, R. 3, R. 6, R. 7a EPÜ
    dict(id="e01n14", order=1400, titel="Art. 14 EPÜ, R. 3, R. 6 EPÜ: Sprachen und Übersetzungen", einheiten=[
        intro("e01n14-0", "Jede Sprache, aber dann übersetzen",
              "Vor dem EPA darf man in **jeder Sprache** anmelden; die Übersetzung in eine Amtssprache folgt binnen zwei Monaten (Art. 14 Abs. 2 EPÜ, "
              "R. 6 Abs. 1 EPÜ) und bestimmt die **Verfahrenssprache** (Art. 14 Abs. 3 EPÜ). Paper D fragt danach in vielen Varianten: "
              "Berichtigung einer fehlerhaften Übersetzung (2015), Sprachenermäßigung für eine portugiesische Hochschule (2017), Teilanmeldung in "
              "der falschen Sprache (2021), Sprache einer PCT-Anmeldung (2024) und ein Einspruch auf Spanisch nach Art. 14 Abs. 4 EPÜ (2024). "
              "Merkposten: Übersetzungsfristen sind von der Weiterbehandlung ausgeschlossen, und die Verfahrenssprache lässt sich nicht wechseln (G 4/08).",
              concepts=["epc_sprachen", "epc_gebuehrenzahlung"], norms=["Art. 14 EPÜ", "R. 3 EPÜ", "R. 6 EPÜ", "R. 7a EPÜ"], cases=["epc_g_4_08"],
              abschnitt="Überblick"),
        *fallkette("e01n14-1", "Die Anmeldung auf Japanisch",
            "Die N. K. mit Sitz in Osaka reicht am Montag, 9.3.2026, beim EPA eine europäische Anmeldung auf Japanisch ein, ohne Priorität. Eine "
            "englische Übersetzung soll später folgen.",
            [frage("Erhält die Anmeldung einen Anmeldetag, obwohl sie nicht in einer Amtssprache des EPA abgefasst ist?", True,
                   ["**Ja!** Eine europäische Anmeldung kann in jeder Sprache eingereicht werden (Art. 14 Abs. 2 EPÜ). Die Sprache gehört nicht zu den "
                    "Erfordernissen des Anmeldetags (R. 40 Abs. 1 EPÜ); die Übersetzung wird erst in der Formalprüfung verlangt (R. 57 EPÜ)."],
                   merke="Jede Sprache wahrt den Anmeldetag.", titel="Einreichung in jeder Sprache",
                   norms=["R. 40 Abs. 1 EPÜ", "R. 57 EPÜ"], concepts=["epc_anmeldetag"]),
             frage("Bis wann muss N. K. die Übersetzung einreichen?", 2,
                   ["**Bis 11.5.2026.** Die Frist beträgt zwei Monate nach Einreichung der Anmeldung (R. 6 Abs. 1 EPÜ) und endet rechnerisch am "
                    "Samstag, 9.5.2026 (R. 131 Abs. 4 EPÜ). Sie verlängert sich auf den nächsten Tag, an dem das EPA Schriftstücke annimmt "
                    "(R. 134 Abs. 1 EPÜ)."],
                   optionen=["9.4.2026", "9.5.2026", "11.5.2026", "9.6.2026"], merke="Übersetzung: zwei Monate ab Einreichung.",
                   titel="Übersetzungsfrist", norms=["R. 6 Abs. 1 EPÜ", "R. 131 Abs. 4 EPÜ", "R. 134 Abs. 1 EPÜ"], concepts=["epc_fristen"], level=2),
             frage("N. K. versäumt die Frist und auch die zwei Monate der Aufforderung nach R. 58 EPÜ. Kann sie Weiterbehandlung beantragen?", False,
                   ["**Nein!** Die Anmeldung gilt als zurückgenommen (Art. 14 Abs. 2 Satz 3 EPÜ). Die Fristen nach R. 6 Abs. 1 EPÜ und R. 58 EPÜ "
                    "sind von der Weiterbehandlung ausgeschlossen (R. 135 Abs. 2 EPÜ). Möglich bleibt die Wiedereinsetzung in die Frist nach "
                    "R. 58 EPÜ (Art. 122 EPÜ; Richtlinien A-III, 14)."],
                   merke="Übersetzung vergessen: nur Wiedereinsetzung.", titel="Fehlende Übersetzung",
                   norms=["R. 58 EPÜ", "R. 135 Abs. 2 EPÜ", "Art. 122 EPÜ"], concepts=["epc_weiterbehandlung", "epc_wiedereinsetzung"],
                   step=_FV + ".3.1", level=2),
             frage("N. K. reicht die englische Übersetzung rechtzeitig ein. Darf sie später geänderte Ansprüche auf Deutsch einreichen?", False,
                   ["**Nein!** Durch die Übersetzung ist Englisch Verfahrenssprache geworden (Art. 14 Abs. 3 EPÜ). Änderungen der Anmeldung sind in "
                    "der Verfahrenssprache einzureichen (R. 3 Abs. 2 EPÜ). Sonstige Schriftsätze darf sie in jeder Amtssprache abfassen (R. 3 Abs. 1 EPÜ)."],
                   merke="Änderungen nur in der Verfahrenssprache.", titel="Sprache der Änderungen",
                   norms=["Art. 14 Abs. 3 EPÜ", "R. 3 Abs. 2 EPÜ"]),
            ],
            abschnitt="Abs. 2, 3: Einreichung, Übersetzung, Verfahrenssprache", level=1, concepts=["epc_sprachen"],
            norms=["Art. 14 Abs. 2 EPÜ", "R. 6 Abs. 1 EPÜ"]),
        *fallkette("e01n14-2", "Mikrometer oder Millimeter",
            "L reicht EP-L1 auf Koreanisch mit fristgerechter englischer Übersetzung und EP-L2 unmittelbar auf Englisch ein. In beiden englischen "
            "Texten steht in Anspruch 1 „5 mm“; der koreanische Text von EP-L1 und die koreanische Prioritätsanmeldung lauten „5 µm“. Aus den "
            "englischen Texten allein ist der Fehler nicht erkennbar.",
            [frage("Kann L in EP-L1 „mm“ durch „µm“ ersetzen?", True,
                   ["**Ja!** Die Übersetzung kann während des gesamten Verfahrens mit der Anmeldung in der ursprünglich eingereichten Fassung in "
                    "Übereinstimmung gebracht werden (Art. 14 Abs. 2 Satz 2 EPÜ). Ursprünglich eingereichte Fassung ist der koreanische Text "
                    "(Art. 70 Abs. 2 EPÜ); er lautet „5 µm“, die Korrektur erweitert also nichts."],
                   merke="Bei Einreichung in einer Nichtamtssprache ist das Original der Maßstab.", titel="Übersetzung angleichen",
                   norms=["Art. 70 Abs. 2 EPÜ"]),
             frage("Kann L den Fehler in EP-L2 nach R. 139 EPÜ unter Hinweis auf die Prioritätsanmeldung berichtigen?", False,
                   ["**Nein!** EP-L2 wurde auf Englisch eingereicht; der englische Text ist die ursprüngliche Fassung. Bei Ansprüchen müssen Fehler "
                    "und Berichtigung den ursprünglichen Unterlagen sofort zu entnehmen sein (R. 139 EPÜ, G 3/89); Prioritätsunterlagen dürfen "
                    "dafür nicht herangezogen werden (Richtlinien H-VI, 2.2.1). Hier ist der Fehler nicht erkennbar."],
                   merke="Prioritätsunterlagen helfen bei R. 139 EPÜ nicht.", titel="Berichtigung nach R. 139 EPÜ", level=2,
                   norms=["R. 139 EPÜ"], cases=["epc_g_3_89"], concepts=["epc_berichtigung"]),
            ],
            abschnitt="Abs. 2: Übersetzung und ursprüngliche Fassung", level=2, concepts=["epc_sprachen"], norms=["Art. 14 Abs. 2 EPÜ"]),
        *fallkette("e01n14-3", "Die PCT-Anmeldung auf Deutsch",
            "Die US-Firma Q reicht eine internationale Anmeldung auf Deutsch ein; sie wird auf Deutsch veröffentlicht. Beim Eintritt in die "
            "europäische Phase möchte Q das Verfahren vor dem EPA auf Englisch führen.",
            [frage("Kann Q beim Eintritt eine englische Übersetzung einreichen und so Englisch zur Verfahrenssprache machen?", False,
                   ["**Nein!** Ist die internationale Anmeldung in einer Amtssprache des EPA eingereicht und veröffentlicht, bleibt diese Sprache "
                    "Verfahrenssprache; eine Übersetzung in eine andere Amtssprache ist nicht möglich (G 4/08, Art. 14 Abs. 3 EPÜ). Das EPA verwendet "
                    "im schriftlichen Verfahren nur die Verfahrenssprache."],
                   merke="Die Verfahrenssprache lässt sich nicht wechseln.", titel="Kein Sprachwechsel", cases=["epc_g_4_08"],
                   concepts=["epc_euro_pct"]),
             frage("Darf Q seine Erwiderungen auf Bescheide auf Englisch schreiben?", True,
                   ["**Ja!** Im schriftlichen Verfahren kann sich jeder Beteiligte jeder Amtssprache des EPA bedienen (R. 3 Abs. 1 EPÜ). Geänderte "
                    "Ansprüche und Beschreibungsseiten muss Q aber auf Deutsch einreichen (R. 3 Abs. 2 EPÜ)."],
                   merke="Schriftsätze in jeder Amtssprache, Änderungen in der Verfahrenssprache.", titel="Sprache der Schriftsätze",
                   norms=["R. 3 Abs. 1 EPÜ", "R. 3 Abs. 2 EPÜ"]),
            ],
            abschnitt="Abs. 3: Verfahrenssprache", level=2, concepts=["epc_sprachen"], norms=["Art. 14 Abs. 3 EPÜ"]),
        *fallkette("e01n14-4", "Der Einspruch auf Italienisch",
            "Die Einspruchsfrist gegen das Patent EP-P (Verfahrenssprache Deutsch) endet am Montag, 14.9.2026. Am 3.8.2026 legen die italienische "
            "Staatsangehörige M mit Wohnsitz in München und die O S.r.l. mit Sitz in Mailand gemeinsam Einspruch auf Italienisch ein und zahlen die Gebühr.",
            [frage("Durften M und O den Einspruch auf Italienisch einreichen?", True,
                   ["**Ja!** Personen mit Sitz in einem Vertragsstaat, dessen Amtssprache nicht Deutsch, Englisch oder Französisch ist (O in Italien), "
                    "und Angehörige dieses Staats mit Wohnsitz im Ausland (M) dürfen fristgebundene Schriftstücke in einer Amtssprache dieses Staats "
                    "einreichen (Art. 14 Abs. 4 Satz 1 EPÜ)."],
                   merke="Zugelassene Nichtamtssprache: Sitz im Staat oder seine Staatsangehörigkeit genügt.", titel="Berechtigte Personen"),
             frage("Bis wann muss die Übersetzung eingehen?", 1,
                   ["**Bis 14.9.2026.** Grundsätzlich gilt ein Monat nach Einreichung des Schriftstücks (R. 6 Abs. 2 Satz 1 EPÜ), hier also bis "
                    "3.9.2026. Bei einem Einspruch genügt die Einreichung bis zum Ende der Einspruchsfrist, wenn diese später abläuft "
                    "(R. 6 Abs. 2 Satz 3 EPÜ)."],
                   optionen=["3.9.2026", "14.9.2026", "3.10.2026", "Zwei Monate nach einer Aufforderung des EPA"],
                   merke="Einspruch: Übersetzung bis zum Ende der Einspruchsfrist, wenn diese später endet.", titel="Übersetzungsfrist",
                   norms=["R. 6 Abs. 2 EPÜ"], concepts=["epc_fristen"], level=2),
             frage("Muss die Übersetzung in der Verfahrenssprache Deutsch abgefasst sein?", False,
                   ["**Nein!** Die Übersetzung nach Art. 14 Abs. 4 EPÜ kann in jeder Amtssprache des EPA eingereicht werden (R. 3 Abs. 1 Satz 2 EPÜ), "
                    "also auch auf Englisch oder Französisch."],
                   merke="Übersetzung in jede Amtssprache.", titel="Sprache der Übersetzung", norms=["R. 3 Abs. 1 EPÜ"]),
             frage("Ist der Einspruch dann wirksam eingelegt?", False,
                   ["**Nein!** Wird eine vorgeschriebene Übersetzung nicht rechtzeitig eingereicht, gilt das Schriftstück als nicht eingereicht "
                    "(Art. 14 Abs. 4 Satz 3 EPÜ). Weiterbehandlung steht nur dem Anmelder offen (Art. 121 Abs. 1 EPÜ), und die Einspruchsfrist ist abgelaufen."],
                   merke="Übersetzung zu spät: Einspruch gilt als nicht eingereicht.", titel="Verspätete Übersetzung",
                   abwandlung="Die Übersetzung geht erst am 15.9.2026 ein.", norms=["Art. 121 Abs. 1 EPÜ"], concepts=["epc_einspruch"], level=2),
            ],
            abschnitt="Abs. 4: zugelassene Nichtamtssprachen", level=1, concepts=["epc_sprachen"], norms=["Art. 14 Abs. 4 EPÜ", "R. 6 Abs. 2 EPÜ"]),
        *fallkette("e01n14-5", "Die Universität aus Porto",
            "Die Universität U mit Sitz in Porto hat noch nie eine europäische Anmeldung eingereicht. Sie will eine Erfindung anmelden, deren "
            "Beschreibung auf Portugiesisch vorliegt; eine englische Übersetzung ist fertig. U möchte möglichst wenig Gebühren zahlen.",
            [frage("Wie erhält U die Sprachenermäßigung der Anmeldegebühr?", 2,
                   ["**Beschreibung auf Portugiesisch, Übersetzung nicht früher, Erklärung.** Die Ermäßigung setzt eine Anmeldung in einer "
                    "zugelassenen Nichtamtssprache voraus (R. 7a Abs. 1 EPÜ, Art. 14 Abs. 1 GebO); maßgeblich ist die Beschreibung, nicht der "
                    "Erteilungsantrag (Richtlinien A-X, 9.3.2). Hochschulen sind berechtigt (R. 7a Abs. 2 EPÜ); ihren Status muss U ausdrücklich erklären."],
                   optionen=["Anmeldung auf Englisch einreichen und erklären, eine Hochschule zu sein",
                             "Nur den Erteilungsantrag auf Portugiesisch einreichen",
                             "Mindestens die Beschreibung auf Portugiesisch einreichen, die Übersetzung nicht früher, und den Status erklären",
                             "Die portugiesische Fassung nach der englischen nachreichen"],
                   merke="Sprachenermäßigung: Beschreibung in der zugelassenen Nichtamtssprache.", titel="Sprachenermäßigung",
                   norms=["R. 7a Abs. 1 EPÜ", "R. 7a Abs. 2 EPÜ"]),
             frage("Wird nach der Sprachenregelung auch die Recherchengebühr ermäßigt?", False,
                   ["**Nein!** R. 7a Abs. 1 EPÜ ermäßigt nur Anmelde- und Prüfungsgebühr. U erhält aber die Ermäßigung für Kleinsteinheiten, die "
                    "auch die Recherchengebühr erfasst (R. 7a Abs. 3 EPÜ): Hochschulen gehören dazu, und U hat keine fünf Anmeldungen in fünf Jahren "
                    "eingereicht (R. 7a Abs. 4 EPÜ). Beide Ermäßigungen werden nacheinander angewandt (Richtlinien A-X, 9.2)."],
                   merke="Sprachenregelung: Anmelde- und Prüfungsgebühr; Kleinsteinheiten: auch Recherche, Benennung, Erteilung, Jahresgebühren.",
                   titel="Ermäßigung für Kleinsteinheiten", norms=["R. 7a Abs. 3 EPÜ", "R. 7a Abs. 4 EPÜ"], level=2),
             frage("Erhält das Unternehmen eine Ermäßigung der Recherchengebühr?", False,
                   ["**Nein!** Als kleines oder mittleres Unternehmen erhält es nur die Sprachenermäßigung (R. 7a Abs. 2 EPÜ). R. 7a Abs. 3 EPÜ gilt "
                    "nur für Kleinstunternehmen, natürliche Personen, Organisationen ohne Gewinnerzielungsabsicht, Hochschulen und öffentliche "
                    "Forschungseinrichtungen; andere KMU sind ausgeschlossen (Richtlinien A-X, 9.4.1)."],
                   merke="KMU, die keine Kleinstunternehmen sind: nur Sprachenermäßigung.", titel="Abwandlung: mittleres Unternehmen",
                   abwandlung="Anmelderin ist statt U ein portugiesisches Unternehmen mit 120 Beschäftigten.", norms=["R. 7a Abs. 3 EPÜ"], level=2),
            ],
            abschnitt="R. 7a EPÜ: Gebührenermäßigungen", level=2, concepts=["epc_gebuehrenzahlung", "epc_sprachen"], norms=["R. 7a EPÜ"]),
    ]),
    # ================================================================== Art. 60, 61 EPÜ, R. 14 bis 16 EPÜ
    dict(id="e01n61", order=6100, titel="Art. 60, 61 EPÜ, R. 14 bis 16 EPÜ: Recht auf das Patent", einheiten=[
        intro("e01n61-0", "Wem gehört die Erfindung?",
              "Über das Recht auf das Patent entscheidet nicht das EPA, sondern ein nationales Gericht; vor dem EPA gilt der Anmelder als berechtigt "
              "(Art. 60 Abs. 3 EPÜ). Das EPÜ sichert den wahren Berechtigten aber ab: Weist er seine Klage nach, wird das Erteilungsverfahren "
              "**ausgesetzt** (R. 14 Abs. 1 EPÜ), Fristen außer den Jahresgebührenfristen werden gehemmt (R. 14 Abs. 4 EPÜ), und der Anmelder darf "
              "nicht zurücknehmen (R. 15 EPÜ). Nach rechtskräftigem Urteil hat der Berechtigte **drei Monate** für die Wege des Art. 61 Abs. 1 EPÜ "
              "(R. 16 Abs. 1 EPÜ). Paper D 2019 fragte die ganze Kette ab, bis zur Teilanmeldung nach Fortsetzung des Verfahrens.",
              concepts=["epc_vindikation"], norms=["Art. 60 EPÜ", "Art. 61 EPÜ", "R. 14 EPÜ", "R. 15 EPÜ", "R. 16 EPÜ"], cases=["epc_j_14_19"],
              abschnitt="Überblick"),
        *fallkette("e01n61-1", "Der Streit zieht sich",
            "J klagt 2024 vor einem nationalen Gericht gegen die Anmelderin K auf Zuerkennung des Anspruchs auf Erteilung; das EPA setzt das "
            "Erteilungsverfahren am 3.6.2024 aus. Das Gerichtsverfahren ist 2026 noch nicht abgeschlossen. K drängt auf Erteilung.",
            [frage("Kann das EPA selbst entscheiden, ob K oder J berechtigt ist?", False,
                   ["**Nein!** Im Verfahren vor dem EPA gilt der Anmelder als berechtigt, das Recht auf das Patent geltend zu machen (Art. 60 Abs. 3 EPÜ). "
                    "Über den Anspruch auf Erteilung entscheiden die nationalen Gerichte; ihre Entscheidungen werden nach dem Anerkennungsprotokoll "
                    "anerkannt, das Bestandteil des Übereinkommens ist (Art. 164 Abs. 1 EPÜ)."],
                   merke="Das EPA prüft die Berechtigung nicht.", titel="Keine Prüfung der Berechtigung", norms=["Art. 60 Abs. 3 EPÜ", "Art. 164 Abs. 1 EPÜ"]),
             frage("Muss das EPA mit der Fortsetzung bis zum Ende des Gerichtsverfahrens warten?", False,
                   ["**Nein!** Das EPA kann einen Zeitpunkt festsetzen, zu dem es das Erteilungsverfahren ohne Rücksicht auf den Stand des nationalen "
                    "Verfahrens fortsetzen will. Ist bis dahin keine rechtskräftige Entscheidung nachgewiesen, kann es fortsetzen (R. 14 Abs. 3 EPÜ)."],
                   merke="Das EPA muss nicht unbegrenzt warten.", titel="Fortsetzung ohne Urteil", norms=["R. 14 Abs. 3 EPÜ"], level=2),
             frage("Bei der Aussetzung liefen von der Frist für den Prüfungsantrag noch drei Wochen. Bleiben K nach der Fortsetzung nur drei Wochen?", False,
                   ["**Nein!** Der noch nicht verstrichene Teil der Frist beginnt am Tag der Fortsetzung zu laufen; die verbleibende Frist beträgt "
                    "jedoch mindestens zwei Monate (R. 14 Abs. 4 EPÜ)."],
                   merke="Nach der Fortsetzung bleiben mindestens zwei Monate.", titel="Restfrist", norms=["R. 14 Abs. 4 EPÜ", "R. 70 Abs. 1 EPÜ"],
                   concepts=["epc_fristen"], level=2),
            ],
            abschnitt="Art. 60 Abs. 3 EPÜ, R. 14 Abs. 3, 4 EPÜ: Berechtigung und Fortsetzung", level=1, concepts=["epc_vindikation"],
            norms=["Art. 60 Abs. 3 EPÜ", "R. 14 EPÜ"]),
        *fallkette("e01n61-2", "Die Klage kurz vor der Erteilung",
            "Die Anmeldung EP-A von A ist veröffentlicht. Am 5.10.2026 erlässt die Prüfungsabteilung die Mitteilung nach R. 71 Abs. 3 EPÜ. B hat vor "
            "einem zuständigen deutschen Gericht gegen A geklagt, um den Anspruch auf Erteilung zugesprochen zu bekommen. Am 26.10.2026 reicht B "
            "den Nachweis der Klageerhebung beim EPA ein.",
            [frage("Wird das Erteilungsverfahren ausgesetzt, obwohl A widerspricht?", True,
                   ["**Ja!** Weist ein Dritter nach, dass er ein Verfahren mit dem Ziel einer Entscheidung nach Art. 61 Abs. 1 EPÜ eingeleitet hat, wird "
                    "ausgesetzt (R. 14 Abs. 1 EPÜ); nur B könnte der Fortsetzung zustimmen. Die Anmeldung ist veröffentlicht, und der Nachweis liegt "
                    "vor dem Hinweis auf die Erteilung (J 14/19)."],
                   merke="Aussetzung: Nachweis der Klage, nach Veröffentlichung, vor dem Erteilungshinweis.", titel="Aussetzung",
                   norms=["R. 14 Abs. 1 EPÜ"], cases=["epc_j_14_19"]),
             frage("Läuft die Frist nach R. 71 Abs. 3 EPÜ während der Aussetzung weiter?", False,
                   ["**Nein!** Alle am Tag der Aussetzung laufenden Fristen werden gehemmt; nach der Fortsetzung läuft der Rest, mindestens aber zwei "
                    "Monate (R. 14 Abs. 4 EPÜ). Die Aussetzung wirkt ab Eingang des Nachweises, hier ab 26.10.2026 (Richtlinien A-IV, 2.2.2)."],
                   merke="Gehemmt, nicht neu: Rest der Frist, mindestens zwei Monate.", titel="Hemmung der Fristen",
                   norms=["R. 14 Abs. 4 EPÜ", "R. 71 Abs. 3 EPÜ"], concepts=["epc_fristen"], cases=["epc_j_9_12"]),
             frage("Müssen während der Aussetzung Jahresgebühren gezahlt werden?", True,
                   ["**Ja!** Die Fristen zur Zahlung der Jahresgebühren sind von der Hemmung ausgenommen (R. 14 Abs. 4 EPÜ). Zahlt A nicht, sollte B "
                    "zahlen; Gebühren kann jeder wirksam entrichten (Richtlinien A-X, 1). Sonst gilt die Anmeldung als zurückgenommen (Art. 86 Abs. 1 EPÜ)."],
                   merke="Jahresgebühren laufen trotz Aussetzung weiter.", titel="Jahresgebühren", level=2,
                   norms=["Art. 86 Abs. 1 EPÜ"], concepts=["epc_jahresgebuehren"]),
             frage("Kann A die Anmeldung während der Aussetzung zurücknehmen, um B das Verfahren zu entziehen?", False,
                   ["**Nein!** Von dem Tag, an dem der Dritte die Klage nachweist, bis zur Fortsetzung des Verfahrens darf weder die Anmeldung noch die "
                    "Benennung eines Vertragsstaats zurückgenommen werden (R. 15 EPÜ)."],
                   merke="Während der Aussetzung keine Rücknahme.", titel="Rücknahmesperre", norms=["R. 15 EPÜ"]),
            ],
            abschnitt="R. 14, 15 EPÜ: Aussetzung", level=1, concepts=["epc_vindikation"], norms=["R. 14 Abs. 1 EPÜ"]),
        *fallkette("e01n61-3", "Die Teilanmeldung während der Aussetzung",
            "Die Anmeldung EP-G von G beschreibt die Erfindungen X und Y und beansprucht X. H weist am 4.5.2026 beim EPA nach, dass er auf "
            "Zuerkennung des Anspruchs auf Erteilung geklagt hat. Am 12.5.2026 reicht G eine Teilanmeldung für Y ein; die Mitteilung über die "
            "Aussetzung erhält G erst am 20.5.2026.",
            [frage("Ist die Teilanmeldung wirksam eingereicht?", False,
                   ["**Nein!** Die Aussetzung wirkt ab Eingang des Nachweises, hier ab 4.5.2026, auch wenn G die Mitteilung erst später erhält "
                    "(J 9/12). Während der Aussetzung bleibt der Status quo gewahrt; eine Teilanmeldung kann nicht eingereicht werden "
                    "(J 20/05; Richtlinien A-IV, 2.2.3)."],
                   merke="Die Aussetzung sperrt Teilanmeldungen ab Eingang des Nachweises.", titel="Teilanmeldung gesperrt",
                   cases=["epc_j_9_12", "epc_j_20_05"], step=_TA + ".1"),
             frage("H obsiegt rechtskräftig und verfolgt EP-G nach Art. 61 Abs. 1 lit. a EPÜ weiter. Kann H nach der Fortsetzung die Teilanmeldung "
                   "für Y einreichen?", True,
                   ["**Ja!** Mit der Erklärung nach Art. 61 Abs. 1 lit. a EPÜ tritt H an die Stelle von G. Als Anmelder kann H zu der fortgesetzten, "
                    "anhängigen Anmeldung eine Teilanmeldung einreichen (R. 36 Abs. 1 EPÜ); G kann es nicht mehr."],
                   merke="Nach der Fortsetzung teilt der neue Anmelder.", titel="Teilanmeldung nach Fortsetzung", level=2,
                   norms=["Art. 61 Abs. 1 EPÜ", "R. 36 Abs. 1 EPÜ"], step=_TA + ".2"),
            ],
            abschnitt="R. 14 EPÜ: Wirkungen der Aussetzung", level=2, concepts=["epc_vindikation", "epc_teilanmeldung"], norms=["R. 14 Abs. 1 EPÜ"]),
        *fallkette("e01n61-4", "Das rechtskräftige Urteil",
            "Ein Landgericht spricht C den Anspruch auf Erteilung des europäischen Patents aus der Anmeldung EP-D von D für alle benannten Staaten "
            "zu. Das Urteil ist seit Montag, 15.6.2026, rechtskräftig. Das Erteilungsverfahren vor dem EPA ist seit 2025 ausgesetzt.",
            [frage("Kann C die Anmeldung EP-D als eigene Anmeldung weiterverfolgen?", True,
                   ["**Ja!** Der Berechtigte kann die Anmeldung anstelle des Anmelders als eigene weiterverfolgen (Art. 61 Abs. 1 lit. a EPÜ). C erklärt "
                    "dies schriftlich; das Verfahren wird in dem Stand fortgesetzt, in dem es ausgesetzt wurde (Richtlinien A-IV, 2.4). Alternativ: neue "
                    "Anmeldung (lit. b) oder Zurückweisung (lit. c)."],
                   merke="Art. 61 Abs. 1 EPÜ: weiterverfolgen, neu anmelden oder zurückweisen lassen.", titel="Weiterverfolgen"),
             frage("Bis wann muss C von einem der Rechtsbehelfe Gebrauch machen?", 1,
                   ["**Bis 15.9.2026.** Die Rechtsbehelfe des Art. 61 Abs. 1 EPÜ stehen nur binnen drei Monaten nach Rechtskraft offen "
                    "(R. 16 Abs. 1 lit. a EPÜ); Weiterbehandlung ist ausgeschlossen (R. 135 Abs. 2 EPÜ). Vorher setzt das EPA das Verfahren ohne "
                    "Antrag von C nicht fort (R. 14 Abs. 2 EPÜ)."],
                   optionen=["15.7.2026", "15.9.2026", "15.12.2026", "15.6.2027"], merke="Drei Monate ab Rechtskraft.", titel="Frist",
                   norms=["R. 16 Abs. 1 EPÜ", "R. 14 Abs. 2 EPÜ", "R. 135 Abs. 2 EPÜ"], concepts=["epc_fristen"], level=2),
             frage("Kann C noch nach Art. 61 Abs. 1 EPÜ vorgehen?", False,
                   ["**Nein!** Die Rechtsbehelfe setzen voraus, dass das europäische Patent noch nicht erteilt ist (R. 16 Abs. 1 lit. b EPÜ). C bleibt "
                    "das nationale Recht: Übertragung des Patents oder Nichtigkeit, weil D nicht berechtigt ist (Art. 138 Abs. 1 lit. e EPÜ)."],
                   merke="Nach der Erteilung hilft Art. 61 EPÜ nicht mehr.", titel="Abwandlung: Patent erteilt",
                   abwandlung="C hatte keine Aussetzung erwirkt; EP-D wurde erteilt, bevor das Urteil rechtskräftig wurde.",
                   norms=["R. 16 Abs. 1 EPÜ", "Art. 138 Abs. 1 EPÜ"], level=2),
            ],
            abschnitt="Art. 61 Abs. 1 EPÜ, R. 16 EPÜ: Rechtsbehelfe", level=1, concepts=["epc_vindikation"], norms=["Art. 61 Abs. 1 EPÜ", "R. 16 Abs. 1 EPÜ"]),
        *fallkette("e01n61-5", "Die zurückgenommene Anmeldung",
            "E reicht 2024 die Anmeldung EP-E über eine Erfindung ein, die in Wahrheit F gemacht hat. Ende 2025 nimmt E die Anmeldung zurück, bevor "
            "F klagt. Später spricht ein Gericht F rechtskräftig den Anspruch auf Erteilung eines europäischen Patents für diese Erfindung zu.",
            [frage("Kann F eine neue Anmeldung nach Art. 61 Abs. 1 lit. b EPÜ einreichen, obwohl EP-E nicht mehr anhängig ist?", True,
                   ["**Ja!** Es ist keine Voraussetzung, dass die ursprüngliche Anmeldung bei Einreichung der neuen Anmeldung noch anhängig ist "
                    "(G 3/92). F muss aber die drei Monate nach Rechtskraft einhalten (R. 16 Abs. 1 lit. a EPÜ)."],
                   merke="Die Art.-61-Anmeldung braucht keine anhängige Ursprungsanmeldung.", titel="Neue Anmeldung", cases=["epc_g_3_92"],
                   norms=["R. 16 Abs. 1 EPÜ"]),
             frage("Erhält die neue Anmeldung den Anmeldetag von EP-E?", True,
                   ["**Ja,** soweit sie nicht über den Inhalt von EP-E in der ursprünglich eingereichten Fassung hinausgeht: Art. 76 Abs. 1 EPÜ gilt "
                    "entsprechend (Art. 61 Abs. 2 EPÜ). F reicht sie unmittelbar beim EPA ein und zahlt Anmelde- und Recherchengebühr binnen eines "
                    "Monats (R. 17 Abs. 2 EPÜ)."],
                   merke="Die neue Anmeldung wird wie eine Teilanmeldung behandelt.", titel="Anmeldetag", level=2,
                   norms=["Art. 61 Abs. 2 EPÜ", "Art. 76 Abs. 1 EPÜ", "R. 17 Abs. 2 EPÜ"], concepts=["epc_teilanmeldung"]),
             frage("Muss F für die neue Anmeldung Jahresgebühren für die zurückliegenden Jahre nachzahlen?", False,
                   ["**Nein!** Für das Jahr, in dem die neue Anmeldung eingereicht wird, und für die vorhergehenden Jahre sind keine Jahresgebühren zu "
                    "entrichten (R. 51 Abs. 6 EPÜ). Insoweit unterscheidet sie sich von der Teilanmeldung (R. 51 Abs. 3 EPÜ)."],
                   merke="Keine rückständigen Jahresgebühren für die Art.-61-Anmeldung.", titel="Jahresgebühren", level=3,
                   norms=["R. 51 Abs. 6 EPÜ", "R. 51 Abs. 3 EPÜ"], concepts=["epc_jahresgebuehren"]),
            ],
            abschnitt="Art. 61 Abs. 1 lit. b, Abs. 2 EPÜ: neue Anmeldung", level=2, concepts=["epc_vindikation"],
            norms=["Art. 61 Abs. 1 EPÜ", "Art. 61 Abs. 2 EPÜ"]),
    ]),
    # ================================================================== Art. 64, 65 EPÜ
    dict(id="e01n65", order=6500, titel="Art. 64, 65 EPÜ: Validierung und Einheitspatent", einheiten=[
        intro("e01n65-0", "Nach der Erteilung: Bündel oder Einheitspatent",
              "Mit dem Hinweis auf die Erteilung wirkt das europäische Patent in jedem benannten Staat wie ein nationales Patent (Art. 64 Abs. 1 EPÜ). "
              "Was dafür noch zu tun ist, bestimmt jeder Staat: eine Übersetzung nach Art. 65 EPÜ, soweit er nicht nach dem Londoner Übereinkommen "
              "darauf verzichtet, und Jahresgebühren an das nationale Amt (Art. 141 EPÜ). Für die teilnehmenden EU-Staaten gibt es stattdessen das "
              "**Einheitspatent**: Antrag binnen **eines Monats** nach dem Erteilungshinweis (R. 6 Abs. 1 DOEPS). Paper D 2024 fragte genau diese "
              "Kombination ab: Vereinigtes Königreich, Polen und Einheitspatent für einen Anmelder aus Marokko.",
              concepts=["epc_validierung", "upc_antrag_einheitliche_wirkung"], norms=["Art. 64 EPÜ", "Art. 65 EPÜ", "Art. 141 EPÜ", "R. 6 DOEPS"],
              abschnitt="Überblick"),
        *fallkette("e01n65-1", "Das Verfahren und sein Erzeugnis",
            "Das europäische Patent EP-H von H schützt ein Verfahren zur Herstellung des Stoffs S. Der Erteilungsbeschluss datiert vom 6.8.2026, der "
            "Hinweis auf die Erteilung wird am 2.9.2026 bekannt gemacht. W stellt S in Frankreich mit dem Verfahren her und verkauft S in Deutschland.",
            [frage("Ab wann gewährt EP-H die Rechte aus dem Patent?", 1,
                   ["**Ab 2.9.2026.** Das Patent gewährt die Rechte ab dem Tag der Bekanntmachung des Hinweises auf die Erteilung (Art. 64 Abs. 1 EPÜ); "
                    "an diesem Tag wird auch der Erteilungsbeschluss wirksam (Art. 97 Abs. 3 EPÜ). Vorher besteht nur der einstweilige Schutz der "
                    "veröffentlichten Anmeldung (Art. 67 EPÜ)."],
                   optionen=["6.8.2026", "2.9.2026", "Ab Einreichung der Übersetzungen", "Ab Ablauf der Einspruchsfrist"],
                   merke="Maßgeblich ist der Hinweis auf die Erteilung im Patentblatt.", titel="Beginn der Wirkung",
                   norms=["Art. 97 Abs. 3 EPÜ", "Art. 67 EPÜ"], concepts=["epc_erteilung"]),
             frage("Kann H gegen den Verkauf von S in Deutschland vorgehen, obwohl dort nicht das Verfahren benutzt wird?", True,
                   ["**Ja!** Ist Gegenstand des Patents ein Verfahren, erstreckt sich der Schutz auch auf die durch das Verfahren unmittelbar "
                    "hergestellten Erzeugnisse (Art. 64 Abs. 2 EPÜ). Der Verkauf von S berührt den deutschen Teil von EP-H."],
                   merke="Verfahrensschutz erfasst das unmittelbare Erzeugnis.", titel="Unmittelbares Verfahrenserzeugnis", norms=["Art. 64 Abs. 2 EPÜ"]),
             frage("Richtet sich die Frage, ob W das Patent verletzt, nach dem EPÜ?", False,
                   ["**Nein!** Eine Verletzung des europäischen Patents wird nach nationalem Recht behandelt (Art. 64 Abs. 3 EPÜ). Das EPÜ legt nur fest, "
                    "dass sich der Schutzbereich nach den Ansprüchen bestimmt (Art. 69 EPÜ)."],
                   merke="Verletzung: nationales Recht; Schutzbereich: Art. 69 EPÜ.", titel="Verletzung", level=2,
                   norms=["Art. 64 Abs. 3 EPÜ", "Art. 69 EPÜ"], concepts=["epc_anspruchsauslegung"]),
            ],
            abschnitt="Art. 64 EPÜ: Wirkung des Patents", level=1, concepts=["epc_validierung"], norms=["Art. 64 Abs. 1 EPÜ"]),
        *fallkette("e01n65-2", "Vom Vereinigten Königreich bis Marokko",
            "Die J S.A. mit Sitz in Marokko erhält das europäische Patent EP-J auf Französisch; der Hinweis auf die Erteilung wird am Mittwoch, "
            "2.9.2026, bekannt gemacht. J will Schutz im Vereinigten Königreich, in Polen und in Marokko. Eine Validierungsgebühr für Marokko hat J nie gezahlt.",
            [frage("Muss J für das Vereinigte Königreich eine Übersetzung einreichen?", False,
                   ["**Nein!** Das Vereinigte Königreich hat als Partei des Londoner Übereinkommens auf Übersetzungen nach Art. 65 Abs. 1 EPÜ verzichtet; "
                    "es hat mit Englisch eine Amtssprache des EPA. Das Patent wirkt dort ohne weitere Handlung (Art. 64 Abs. 1 EPÜ)."],
                   merke="Staaten des Londoner Übereinkommens mit EPA-Amtssprache verlangen keine Übersetzung.", titel="Londoner Übereinkommen"),
             frage("Bis wann muss J die polnische Übersetzung einreichen, wenn Polen keine längere Frist vorsieht?", 1,
                   ["**Bis 2.12.2026.** Polen ist nicht Partei des Londoner Übereinkommens und verlangt eine Übersetzung (Art. 65 Abs. 1 EPÜ). Die Frist "
                    "endet drei Monate nach dem Hinweis auf die Erteilung. Versäumt J sie, kann Polen die Wirkungen als von Anfang an nicht "
                    "eingetreten behandeln (Art. 65 Abs. 3 EPÜ)."],
                   optionen=["2.10.2026", "2.12.2026", "2.3.2027", "Polen verlangt keine Übersetzung"],
                   merke="Art. 65 EPÜ: drei Monate ab Erteilungshinweis.", titel="Übersetzung für Polen",
                   norms=["Art. 65 Abs. 1 EPÜ", "Art. 65 Abs. 3 EPÜ"], concepts=["epc_fristen"], level=2),
             frage("Kann J den Schutz in Marokko jetzt noch durch Zahlung der Validierungsgebühr erlangen?", False,
                   ["**Nein!** Die Validierungsgebühr war binnen sechs Monaten nach dem Hinweis auf die Veröffentlichung des Recherchenberichts zu "
                    "zahlen, mit Zuschlag noch zwei Monate danach (Richtlinien A-III, 12.2). Wiedereinsetzung gibt es nicht; die Validierung richtet "
                    "sich nach nationalem Recht, nicht nach dem EPÜ (Richtlinien A-III, 12.1)."],
                   merke="Validierungsstaaten: Gebühr in der Anmeldephase, keine Wiedereinsetzung.", titel="Validierungsstaat", level=2),
            ],
            abschnitt="Art. 65 EPÜ: Übersetzungen und Validierung", level=1, concepts=["epc_validierung"], norms=["Art. 65 EPÜ"]),
        *fallkette("e01n65-3", "Der Antrag auf einheitliche Wirkung",
            "Für das europäische Patent EP-K von K wird der Hinweis auf die Erteilung am Mittwoch, 7.10.2026, bekannt gemacht. Verfahrenssprache ist "
            "Deutsch; die Ansprüche sind für alle Staaten gleich. K will ein Einheitspatent und zusätzlich Schutz in Spanien.",
            [frage("Bis wann muss K den Antrag auf einheitliche Wirkung stellen?", 2,
                   ["**Bis 9.11.2026.** Der Antrag ist spätestens einen Monat nach Bekanntmachung des Hinweises auf die Erteilung beim EPA zu stellen "
                    "(R. 6 Abs. 1 DOEPS). Die Frist endet am Samstag, 7.11.2026, und verlängert sich auf Montag (R. 134 Abs. 1 EPÜ, entsprechend "
                    "anwendbar nach R. 20 Abs. 2 DOEPS)."],
                   optionen=["7.10.2026", "7.11.2026", "9.11.2026", "7.1.2027"], merke="Einheitliche Wirkung: ein Monat ab Erteilungshinweis.",
                   titel="Antragsfrist", norms=["R. 6 Abs. 1 DOEPS", "R. 20 Abs. 2 DOEPS", "R. 134 Abs. 1 EPÜ"], concepts=["epc_fristen"]),
             frage("Genügt ein Antrag auf Deutsch ohne Übersetzung der Patentschrift?", False,
                   ["**Nein!** Der Antrag ist schriftlich in der Verfahrenssprache zu stellen, hier Deutsch. Während der Übergangszeit muss er eine "
                    "vollständige Übersetzung der Patentschrift ins Englische enthalten (R. 6 Abs. 2 DOEPS, Art. 6 Abs. 1 EPatÜVO). Fehlt sie, fordert "
                    "das EPA zur Behebung binnen eines Monats auf (R. 7 Abs. 3 DOEPS)."],
                   merke="Antrag in der Verfahrenssprache, Übersetzung ins Englische oder aus dem Englischen.", titel="Inhalt des Antrags",
                   norms=["R. 6 Abs. 2 DOEPS", "R. 7 Abs. 3 DOEPS", "Art. 6 Abs. 1 EPatÜVO"], concepts=["upc_up_uebersetzung"], level=2),
             frage("K versäumt die Monatsfrist. Kann K Weiterbehandlung beantragen?", False,
                   ["**Nein!** Art. 121 EPÜ gehört nicht zu den Vorschriften, die R. 20 Abs. 1 DOEPS für entsprechend anwendbar erklärt. Möglich ist "
                    "nur die Wiedereinsetzung, zu beantragen binnen zwei Monaten nach Ablauf der versäumten Frist (R. 22 Abs. 2 DOEPS)."],
                   merke="Antragsfrist versäumt: Wiedereinsetzung binnen zwei Monaten, keine Weiterbehandlung.", titel="Fristversäumnis",
                   norms=["R. 20 Abs. 1 DOEPS", "R. 22 Abs. 2 DOEPS"], concepts=["epc_wiedereinsetzung"], level=3),
             frage("Erstreckt sich das Einheitspatent auch auf Spanien?", False,
                   ["**Nein!** Einheitliche Wirkung besteht nur in den teilnehmenden Mitgliedstaaten, in denen das Einheitliche Patentgericht am Tag "
                    "der Eintragung ausschließlich zuständig ist (Art. 18 Abs. 2 EPatVO). Spanien nimmt nicht teil; dort muss K das europäische Patent "
                    "nach Art. 65 EPÜ und nationalem Recht validieren."],
                   merke="Einheitspatent und nationale Validierung lassen sich kombinieren.", titel="Räumlicher Umfang", level=2,
                   norms=["Art. 18 Abs. 2 EPatVO", "Art. 65 EPÜ"]),
            ],
            abschnitt="Einheitspatent: R. 6 DOEPS", level=2, concepts=["upc_antrag_einheitliche_wirkung", "epc_validierung"], norms=["R. 6 DOEPS"]),
        *fallkette("e01n65-4", "Die Jahresgebühren nach der Erteilung",
            "Die Anmeldung von L wurde am 15.11.2021 eingereicht. Der Hinweis auf die Erteilung wird am 7.10.2026 bekannt gemacht. L validiert das "
            "Patent in Polen und lässt für die teilnehmenden Staaten die einheitliche Wirkung eintragen.",
            [frage("Zahlt L die am 30.11.2025 fällige Jahresgebühr für das fünfte Jahr an das EPA?", True,
                   ["**Ja!** Die Pflicht zur Zahlung von Jahresgebühren an das EPA endet mit der Gebühr für das Jahr, in dem der Hinweis auf die "
                    "Erteilung bekannt gemacht wird (Art. 86 Abs. 2 EPÜ). Der 7.10.2026 fällt in das fünfte Jahr (15.11.2025 bis 14.11.2026)."],
                   merke="An das EPA: bis einschließlich zum Jahr des Erteilungshinweises.", titel="Letzte Jahresgebühr an das EPA",
                   norms=["Art. 86 Abs. 2 EPÜ"]),
             frage("Muss L für Polen einen Zuschlag zahlen, wenn er die am 30.11.2026 fällige Gebühr für das sechste Jahr am 4.12.2026 zahlt?", False,
                   ["**Nein!** Nationale Jahresgebühren, die binnen zwei Monaten nach dem Erteilungshinweis fällig werden, gelten als wirksam entrichtet, "
                    "wenn sie innerhalb dieser Frist gezahlt werden, hier bis 7.12.2026; ein Zuschlag wird nicht erhoben (Art. 141 Abs. 2 EPÜ)."],
                   merke="Art. 141 Abs. 2 EPÜ: zwei Monate Schonfrist nach der Erteilung.", titel="Nationale Jahresgebühr",
                   norms=["Art. 141 Abs. 1 EPÜ", "Art. 141 Abs. 2 EPÜ"], level=2),
             frage("Zahlt L die Jahresgebühren für das Einheitspatent an die nationalen Ämter?", False,
                   ["**Nein!** Jahresgebühren für das Einheitspatent sind an das EPA zu entrichten, einmal für alle teilnehmenden Staaten "
                    "(R. 13 Abs. 1 DOEPS). Wäre eine Gebühr zwischen Erteilungshinweis und Mitteilung über die Eintragung fällig geworden, wird sie "
                    "erst mit dieser Mitteilung fällig und ist binnen drei Monaten zuschlagsfrei zahlbar (R. 13 Abs. 5 DOEPS)."],
                   merke="Einheitspatent: Jahresgebühren an das EPA.", titel="Jahresgebühren Einheitspatent", level=2,
                   norms=["R. 13 Abs. 1 DOEPS", "R. 13 Abs. 5 DOEPS"], concepts=["upc_up_jahresgebuehren"]),
            ],
            abschnitt="Art. 86 Abs. 2 EPÜ, Art. 141 EPÜ: Jahresgebühren", level=2, concepts=["epc_jahresgebuehren", "epc_validierung"],
            norms=["Art. 86 Abs. 2 EPÜ", "Art. 141 EPÜ"]),
    ]),
    # ================================================================== Art. 76 EPÜ, R. 36 EPÜ
    dict(id="e01n76", order=7600, titel="Art. 76 EPÜ, R. 36 EPÜ: Teilanmeldung", einheiten=[
        intro("e01n76-0", "Solange die Stammanmeldung lebt",
              "Die Teilanmeldung ist in Paper D das Universalwerkzeug: für eine zweite Erfindung (2021), für nicht recherchierte Gegenstände (2023), "
              "für einen zusätzlichen Anspruch nach der Zurückverweisung (2025) oder nach Fortsetzung eines ausgesetzten Verfahrens (2019). Vier "
              "Prüfungspunkte: Ist die Stammanmeldung **anhängig** (R. 36 Abs. 1 EPÜ, G 1/09)? Stimmt die **Sprache** (R. 36 Abs. 2 EPÜ)? Geht der "
              "**Inhalt** nicht über die Stammanmeldung hinaus (Art. 76 Abs. 1 EPÜ)? Sind die **Gebühren** gezahlt, auch rückständige "
              "Jahresgebühren (R. 36 Abs. 3 EPÜ, R. 51 Abs. 3 EPÜ)?",
              concepts=["epc_teilanmeldung", "epc_anhaengigkeit"], norms=["Art. 76 EPÜ", "R. 36 EPÜ"], cases=["epc_g_1_09"], abschnitt="Überblick"),
        schema("e01n76-0s", "Prüfungsschema Teilanmeldung", "epc_schema_teilanmeldung", abschnitt="Überblick"),
        *fallkette("e01n76-1", "Drei Anmeldungen, drei Stichtage",
            "S hat drei europäische Anmeldungen. Für EP-1 wird der Hinweis auf die Erteilung am Mittwoch, 7.10.2026, bekannt gemacht. EP-2 wurde mit "
            "Entscheidung vom 9.9.2026 zurückgewiesen; S legt keine Beschwerde ein. Für EP-3 ist die am 30.4.2026 fällige Jahresgebühr unbezahlt, die "
            "Nachfrist mit Zuschlag läuft noch.",
            [frage("Kann S am 7.10.2026 noch eine Teilanmeldung zu EP-1 einreichen?", False,
                   ["**Nein!** Die Anmeldung ist bis zum Tag vor dem Hinweis auf die Erteilung anhängig, an diesem Tag nicht mehr (Richtlinien A-IV, "
                    "1.1.1); R. 134 EPÜ verlängert das nicht. Letzte Gelegenheit war der 6.10.2026."],
                   merke="Erteilungshinweis: Teilanmeldung spätestens am Vortag.", titel="Erteilung", norms=["Art. 97 Abs. 3 EPÜ"]),
             frage("Kann S am 5.11.2026 noch eine Teilanmeldung zu EP-2 einreichen?", True,
                   ["**Ja!** Eine zurückgewiesene Anmeldung bleibt ohne Beschwerde bis zum Ablauf der Beschwerdefrist anhängig (G 1/09). Die Frist "
                    "beträgt zwei Monate nach Zustellung (Art. 108 EPÜ); die Entscheidung gilt als am 9.9.2026 zugestellt (R. 126 Abs. 2 EPÜ, "
                    "R. 127 Abs. 2 EPÜ), die Frist endet am 9.11.2026."],
                   merke="Zurückweisung: anhängig bis zum Ende der Beschwerdefrist.", titel="Zurückweisung", cases=["epc_g_1_09"],
                   norms=["Art. 108 EPÜ", "R. 126 Abs. 2 EPÜ"], level=2),
             frage("Kann S jetzt eine Teilanmeldung zu EP-3 einreichen, obwohl S die Jahresgebühr nicht mehr zahlen will?", True,
                   ["**Ja!** Wird eine Jahresgebühr nicht bei Fälligkeit gezahlt, bleibt die Anmeldung bis zum Ende der Nachfrist nach R. 51 Abs. 2 EPÜ "
                    "anhängig, auch wenn die Gebühr am Ende nicht gezahlt wird (Richtlinien A-IV, 1.1.1). Erst mit Ablauf der Nachfrist gilt sie als "
                    "zurückgenommen (Art. 86 Abs. 1 EPÜ)."],
                   merke="Während der Nachfrist bleibt die Anmeldung anhängig.", titel="Unbezahlte Jahresgebühr", level=2,
                   norms=["R. 51 Abs. 2 EPÜ", "Art. 86 Abs. 1 EPÜ"], concepts=["epc_jahresgebuehren"]),
            ],
            abschnitt="R. 36 Abs. 1 EPÜ: anhängige Stammanmeldung", level=1, concepts=["epc_anhaengigkeit", "epc_teilanmeldung"],
            norms=["R. 36 Abs. 1 EPÜ"], step=_TA + ".1"),
        *fallkette("e01n76-2", "Die Teilanmeldung auf Französisch",
            "Die englischsprachige Anmeldung EP-T von T, eingereicht am 10.4.2023, beschreibt die Erfindungen X und Y; recherchiert und beansprucht "
            "ist nur X. Auf einen Bescheid vom 2.6.2026 mit viermonatiger Frist antwortet T nicht. Am 25.9.2026 reicht T eine Teilanmeldung für Y "
            "auf Französisch ein.",
            [frage("Ist die Teilanmeldung wirksam?", False,
                   ["**Nein!** Eine Teilanmeldung zu einer Anmeldung in einer Amtssprache ist in deren Verfahrenssprache einzureichen, hier Englisch "
                    "(R. 36 Abs. 2 EPÜ). Eine nachgereichte Übersetzung oder eine Berichtigung nach R. 139 EPÜ heilt das nicht (J 13/14). Anhängig "
                    "war EP-T am 25.9.2026 noch."],
                   merke="Teilanmeldung: in der Verfahrenssprache der Stammanmeldung.", titel="Falsche Sprache",
                   norms=["R. 36 Abs. 2 EPÜ"], cases=["epc_j_13_14"], concepts=["epc_sprachen"], step=_TA + ".2"),
             frage("Die Bescheidsfrist ist am 2.10.2026 abgelaufen. Ist eine am 27.10.2026 auf Englisch eingereichte Teilanmeldung wirksam, wenn T den Rechtsverlust nicht behebt?", False,
                   ["**Nein!** Mit Fristablauf gilt EP-T als zurückgenommen (Art. 94 Abs. 4 EPÜ) und ist nicht mehr anhängig. Wirksam wird die "
                    "Teilanmeldung erst, wenn T Weiterbehandlung beantragt: Gebühr zahlen und auf den Bescheid erwidern (Art. 121 EPÜ, R. 135 Abs. 1 EPÜ). "
                    "Dann gilt EP-T als durchgehend anhängig (Richtlinien A-IV, 1.1.1)."],
                   merke="Ohne Behebung des Rechtsverlusts keine wirksame Teilanmeldung.", titel="Weiterbehandlung der Stammanmeldung", level=2,
                   norms=["Art. 94 Abs. 4 EPÜ", "Art. 121 EPÜ", "R. 135 Abs. 1 EPÜ"], concepts=["epc_weiterbehandlung", "epc_anhaengigkeit"],
                   step=_TA + ".1"),
             frage("Muss T für die neue Teilanmeldung auch Jahresgebühren zahlen?", True,
                   ["**Ja!** Die für EP-T schon fälligen Jahresgebühren für das dritte und vierte Jahr (fällig am 30.4.2025 und 30.4.2026) sind auch für "
                    "die Teilanmeldung zu entrichten. Sie werden mit deren Einreichung fällig und können binnen vier Monaten ohne Zuschlag gezahlt "
                    "werden (R. 51 Abs. 3 EPÜ). Anmelde- und Recherchengebühr: binnen eines Monats (R. 36 Abs. 3 EPÜ)."],
                   merke="Rückständige Jahresgebühren: vier Monate ab Einreichung der Teilanmeldung.", titel="Gebühren der Teilanmeldung", level=2,
                   norms=["R. 51 Abs. 3 EPÜ", "R. 36 Abs. 3 EPÜ"], concepts=["epc_jahresgebuehren"], step=_TA + ".4"),
            ],
            abschnitt="R. 36 Abs. 2, 3 EPÜ: Sprache und Gebühren", level=2, concepts=["epc_teilanmeldung"], norms=["R. 36 Abs. 2 EPÜ"]),
        *fallkette("e01n76-3", "Die Kette",
            "Die Stammanmeldung EP-1 beschreibt eine Pumpe mit den Merkmalen A und B, wobei B als unverzichtbar dargestellt ist, und eine Ausführung "
            "mit dem Zusatz C. Die Teilanmeldung EP-2 übernimmt die Beschreibung ohne die Ausführung mit C und beansprucht A allein. EP-1 ist "
            "inzwischen erteilt.",
            [frage("Ist EP-2 verloren, weil sie über EP-1 hinausgeht und EP-1 nicht mehr anhängig ist?", False,
                   ["**Nein!** Eine Teilanmeldung, die bei Einreichung über die Stammanmeldung hinausgeht, kann noch so geändert werden, dass sie "
                    "Art. 76 Abs. 1 EPÜ genügt, auch wenn die Stammanmeldung nicht mehr anhängig ist (G 1/05). Wird der Anspruch auf A und B "
                    "beschränkt, erhält EP-2 Anmeldetag und Priorität von EP-1."],
                   merke="Eine Erweiterung der Teilanmeldung ist heilbar.", titel="Heilung durch Änderung", cases=["epc_g_1_05"],
                   concepts=["epc_unzulaessige_erweiterung"]),
             frage("Aus EP-2 wird die Teilanmeldung EP-3 abgezweigt, die A, B und C beansprucht. Ist das zulässig?", False,
                   ["**Nein!** In einer Kette muss sich der Inhalt jeder Teilanmeldung aus jeder vorangehenden Anmeldung in der ursprünglich "
                    "eingereichten Fassung ableiten lassen (G 1/06). C fehlt in EP-2; dass EP-1 es offenbart, genügt nicht."],
                   merke="Jede Generation ist ein Filter.", titel="Kette von Teilanmeldungen", cases=["epc_g_1_06"], level=2),
             frage("Kommt es für die Einreichung von EP-3 darauf an, ob EP-1 noch anhängig ist?", False,
                   ["**Nein!** Bei einer Teilanmeldung zu einer Teilanmeldung genügt, dass die unmittelbar vorangehende Anmeldung, hier EP-2, anhängig "
                    "ist (Richtlinien A-IV, 1.1.1). Für EP-3 als Teilanmeldung der zweiten Generation fällt eine Zusatzgebühr als Teil der "
                    "Anmeldegebühr an (R. 38 Abs. 4 EPÜ)."],
                   merke="Maßgeblich ist die direkte Vorgängerin.", titel="Anhängigkeit in der Kette", level=2,
                   norms=["R. 36 Abs. 1 EPÜ", "R. 38 Abs. 4 EPÜ"], concepts=["epc_anhaengigkeit"], step=_TA + ".1"),
            ],
            abschnitt="Art. 76 Abs. 1 EPÜ: Inhalt und Ketten", level=2, concepts=["epc_teilanmeldung"], norms=["Art. 76 Abs. 1 EPÜ"], step=_TA + ".3"),
        *fallkette("e01n76-4", "Das nicht recherchierte Ventil",
            "Die Anmeldung EP-U von U beschreibt ein Ventil mit den Merkmalen E und F und ein davon unabhängiges Ventil G. Recherchiert und "
            "beansprucht ist nur G. Die Erteilung steht bevor; U möchte auch E und F schützen und für G einen weiteren abhängigen Anspruch erhalten.",
            [frage("Kann U die Ansprüche von EP-U auf E und F umstellen?", False,
                   ["**Nein!** Geänderte Ansprüche dürfen sich nicht auf nicht recherchierte Gegenstände beziehen, die mit der ursprünglich "
                    "beanspruchten Erfindung nicht durch eine allgemeine erfinderische Idee verbunden sind (R. 137 Abs. 5 EPÜ). Der Weg ist eine "
                    "Teilanmeldung, solange EP-U anhängig ist; für sie ist eine eigene Recherchengebühr binnen eines Monats zu zahlen (R. 36 Abs. 3 EPÜ)."],
                   merke="Nicht recherchiert: in die Teilanmeldung.", titel="Nicht recherchierter Gegenstand",
                   norms=["R. 137 Abs. 5 EPÜ", "R. 36 Abs. 3 EPÜ"], concepts=["epc_einheitlichkeit"], step=_TA + ".4"),
             frage("Wann ist die Benennungsgebühr für die Teilanmeldung zu zahlen?", 2,
                   ["**Binnen sechs Monaten nach dem Hinweis auf die Veröffentlichung des Recherchenberichts zur Teilanmeldung** (R. 36 Abs. 4 EPÜ). "
                    "Benannt sind die Staaten, die in EP-U bei Einreichung der Teilanmeldung benannt sind (Art. 76 Abs. 2 EPÜ). Bei Versäumnis hilft "
                    "die Weiterbehandlung (Richtlinien A-IV, 1.4.1)."],
                   optionen=["Mit der Einreichung", "Binnen eines Monats nach Einreichung",
                             "Binnen sechs Monaten nach dem Hinweis auf die Veröffentlichung des Recherchenberichts zur Teilanmeldung",
                             "Gar nicht, sie ist mit der Gebühr für EP-U bezahlt"],
                   merke="Benennungsgebühr der Teilanmeldung: an ihren eigenen Recherchenbericht geknüpft.", titel="Benennungsgebühr", level=2,
                   norms=["R. 36 Abs. 4 EPÜ", "Art. 76 Abs. 2 EPÜ"], step=_TA + ".4"),
             frage("U reicht eine zweite Teilanmeldung mit denselben Ansprüchen auf G und dem zusätzlichen abhängigen Anspruch ein. Kann sie neben "
                   "EP-U zum Patent führen?", False,
                   ["**Nein!** Eine Anmeldung kann zurückgewiesen werden, wenn sie denselben Gegenstand beansprucht wie ein demselben Anmelder "
                    "erteiltes europäisches Patent, auch im Verhältnis von Stamm- und Teilanmeldung (G 4/19). U sollte EP-U nach Einreichung der "
                    "Teilanmeldung, aber vor dem Hinweis auf die Erteilung zurücknehmen."],
                   merke="Dieselben Ansprüche gibt es nur einmal.", titel="Doppelpatentierung", cases=["epc_g_4_19"], level=3,
                   norms=["Art. 97 Abs. 2 EPÜ", "Art. 125 EPÜ"], step=_TA + ".3"),
            ],
            abschnitt="Art. 76 Abs. 1, 2 EPÜ: Teilanmeldung als Werkzeug", level=2, concepts=["epc_teilanmeldung"], norms=["Art. 76 Abs. 1 EPÜ"]),
    ]),
    # ================================================================== Art. 80 EPÜ, R. 40, R. 56, R. 56a, R. 58 EPÜ
    dict(id="e01n80", order=8000, titel="Art. 80 EPÜ, R. 40, R. 56, R. 56a, R. 58 EPÜ: Anmeldetag und fehlende Teile", einheiten=[
        intro("e01n80-0", "Was ein Anmeldetag braucht",
              "Für den Anmeldetag genügen drei Dinge: ein Hinweis, dass ein europäisches Patent beantragt wird, Angaben zum Anmelder und eine "
              "Beschreibung oder die Bezugnahme auf eine frühere Anmeldung (Art. 80 EPÜ, R. 40 Abs. 1 EPÜ). Ansprüche, Gebühren und eine Amtssprache "
              "sind nicht nötig. Paper D prüft vor allem, was danach geschieht: fehlende Teile oder Zeichnungen (R. 56 EPÜ, 2015 und 2018), falsch "
              "eingereichte Unterlagen (R. 56a EPÜ, 2025), fehlende Ansprüche (R. 58 EPÜ, 2019) und die Einreichung durch Bezugnahme (2017). Die "
              "Neudatierung kann die Prioritätsfrist sprengen; deshalb zählen die Rettung über die Priorität und die Rücknahme.",
              concepts=["epc_anmeldetag", "epc_fehlende_teile"], norms=["Art. 80 EPÜ", "R. 40 EPÜ", "R. 56 EPÜ", "R. 56a EPÜ", "R. 58 EPÜ"],
              distinctions=["d_epc_r56_r56a_r139"], abschnitt="Überblick"),
        *fallkette("e01n80-1", "Die beschädigten Anhänge",
            "Heute, am letzten Tag des Prioritätsjahrs, soll Vertreterin V für einen japanischen Kollegen eine europäische Anmeldung mit der Priorität "
            "der japanischen Anmeldung JP 4711 einreichen. Die Anhänge mit dem Anmeldungstext und den Angaben zum Anmelder lassen sich nicht öffnen; "
            "der Kollege ist heute nicht erreichbar.",
            [frage("Kann V ohne den Namen des Anmelders einen Anmeldetag erhalten?", True,
                   ["**Ja!** R. 40 Abs. 1 lit. b EPÜ verlangt Angaben, die es erlauben, die Identität des Anmelders festzustellen **oder** mit ihm "
                    "Kontakt aufzunehmen. Name und Anschrift des Vertreters genügen (Richtlinien A-II, 4.1.2)."],
                   merke="Kontaktdaten genügen für den Anmeldetag.", titel="Angaben zum Anmelder", norms=["R. 40 Abs. 1 EPÜ"]),
             frage("Wie ersetzt V die fehlende Beschreibung?", 1,
                   ["**Durch Bezugnahme auf JP 4711.** Statt einer Beschreibung genügt die Bezugnahme auf eine früher eingereichte Anmeldung "
                    "(R. 40 Abs. 1 lit. c EPÜ). Sie muss Anmeldetag, Nummer und Amt angeben und zum Ausdruck bringen, dass sie Beschreibung und "
                    "Zeichnungen ersetzt (R. 40 Abs. 2 EPÜ)."],
                   optionen=["Gar nicht; ohne Beschreibung gibt es keinen Anmeldetag",
                             "Durch Bezugnahme auf JP 4711 mit Anmeldetag, Nummer, Amt und der Erklärung, dass sie Beschreibung und Zeichnungen ersetzt",
                             "Durch Ansprüche, die V aus dem Gedächtnis formuliert", "Durch einen Antrag auf Fristverlängerung"],
                   merke="Bezugnahme: Tag, Nummer, Amt, Ersetzungserklärung.", titel="Einreichung durch Bezugnahme", norms=["R. 40 Abs. 2 EPÜ"], level=2),
             frage("Ist der Anmeldetag verloren, wenn V die beglaubigte Abschrift von JP 4711 nicht binnen zwei Monaten einreicht?", False,
                   ["**Nein!** Abschrift und Übersetzung sind binnen zwei Monaten einzureichen (R. 40 Abs. 3 EPÜ). Fehlt die Abschrift, fordert das EPA "
                    "nach R. 55 EPÜ auf; geht sie binnen zwei Monaten nach dieser Mitteilung ein, bleibt der ursprüngliche Anmeldetag (Richtlinien "
                    "A-II, 4.1.5). Eine Abschrift genügt zugleich für die Priorität."],
                   merke="Bezugnahme: Abschrift binnen zwei Monaten, notfalls nach Aufforderung.", titel="Beglaubigte Abschrift", level=3,
                   norms=["R. 40 Abs. 3 EPÜ", "R. 55 EPÜ"]),
            ],
            abschnitt="R. 40 EPÜ: Erfordernisse des Anmeldetags", level=1, concepts=["epc_anmeldetag"], norms=["Art. 80 EPÜ", "R. 40 EPÜ"]),
        *fallkette("e01n80-2", "Ansprüche und Zeichnungen, aber keine Beschreibung",
            "Z, ein in Argentinien wohnender Erfinder, reicht am Montag, 2.2.2026, online eine europäische Anmeldung auf Spanisch ein, ohne "
            "Priorität. Sie enthält nur Ansprüche und Zeichnungen. Die Beschreibung reicht Z am 16.2.2026 nach.",
            [frage("Ist der 2.2.2026 der Anmeldetag?", False,
                   ["**Nein!** Ohne Beschreibung oder Bezugnahme ist R. 40 Abs. 1 lit. c EPÜ nicht erfüllt. Anmeldetag ist der Tag, an dem alle "
                    "Erfordernisse vorliegen, hier der 16.2.2026 (Richtlinien A-II, 4.1.5). R. 56 EPÜ greift nicht: Es fehlten nicht Teile der "
                    "Beschreibung, sondern die ganze."],
                   merke="Keine Beschreibung: Anmeldetag erst mit ihr.", titel="Fehlende Beschreibung"),
             frage("Musste Z schon für die Einreichung einen zugelassenen Vertreter bestellen?", False,
                   ["**Nein!** Wer weder Wohnsitz noch Sitz in einem Vertragsstaat hat, muss sich vertreten lassen, ausgenommen die Einreichung der "
                    "Anmeldung (Art. 133 Abs. 2 EPÜ). Für alle weiteren Handlungen braucht Z einen zugelassenen Vertreter."],
                   merke="Einreichen darf jeder selbst.", titel="Vertretung", norms=["Art. 133 Abs. 2 EPÜ"], concepts=["epc_vertretung"], level=2),
            ],
            abschnitt="R. 40 Abs. 1 lit. c EPÜ: Beschreibung", level=1, concepts=["epc_anmeldetag"], norms=["R. 40 Abs. 1 EPÜ"]),
        *fallkette("e01n80-3", "Die vergessenen Zeichnungen",
            "W reicht am Freitag, 13.3.2026, dem letzten Tag des Prioritätsjahrs, EP-W1 mit der Priorität GB-1 und EP-W2 mit der Priorität GB-2 ein. "
            "In EP-W1 fehlen die Zeichnungen, auf die die Beschreibung verweist; GB-1 enthält sie identisch. Am 20.3.2026 reicht W sie nach, für "
            "EP-W2 außerdem neu gezeichnete Figuren, die GB-2 nicht enthält.",
            [frage("Kann EP-W1 den Anmeldetag 13.3.2026 behalten?", True,
                   ["**Ja!** Die Zeichnungen sind vollständig in GB-1 enthalten, deren Priorität am Anmeldetag beansprucht war. W muss bis 13.5.2026 "
                    "beantragen, sie auf die Priorität zu stützen, eine Abschrift einreichen (falls nicht nach R. 53 Abs. 2 EPÜ verfügbar) und angeben, "
                    "wo sie in GB-1 stehen (R. 56 Abs. 3 EPÜ)."],
                   merke="In der Priorität enthalten: Der Anmeldetag bleibt.", titel="Rettung über die Priorität", norms=["R. 56 Abs. 3 EPÜ"]),
             frage("Behält EP-W2 die Priorität von GB-2?", False,
                   ["**Nein!** Die Figuren sind nicht in GB-2 enthalten; der Anmeldetag wird auf den 20.3.2026 neu festgesetzt (R. 56 Abs. 2 EPÜ). Er liegt "
                    "damit nach Ablauf der zwölf Monate (Art. 87 Abs. 1 EPÜ); der Prioritätsanspruch ist unwirksam."],
                   merke="Neudatierung kann die Priorität kosten.", titel="Neudatierung", norms=["R. 56 Abs. 2 EPÜ", "Art. 87 Abs. 1 EPÜ"],
                   concepts=["epc_prioritaet"], level=2),
             frage("Kann W für EP-W2 den Anmeldetag 13.3.2026 zurückgewinnen?", True,
                   ["**Ja,** durch Rücknahme der nachgereichten Figuren binnen eines Monats nach der Mitteilung über die Neudatierung (R. 56 Abs. 6 EPÜ). "
                    "Die Neufestsetzung gilt dann als nicht erfolgt, die Bezugnahmen auf die Figuren gelten als gestrichen (R. 56 Abs. 4 EPÜ). Die "
                    "Figuren sind dann nicht Teil der Anmeldung."],
                   merke="Rücknahme: alter Tag, aber ohne die Teile.", titel="Rücknahme der Teile", norms=["R. 56 Abs. 6 EPÜ", "R. 56 Abs. 4 EPÜ"], level=2),
             frage("Kann W Weiterbehandlung beantragen, wenn er die Monatsfrist verpasst?", False,
                   ["**Nein!** Die Fristen nach R. 56 EPÜ sind von der Weiterbehandlung ausgeschlossen (R. 135 Abs. 2 EPÜ). In Betracht kommt nur die "
                    "Wiedereinsetzung (Art. 122 EPÜ)."],
                   merke="R. 56 EPÜ: keine Weiterbehandlung.", titel="Keine Weiterbehandlung", norms=["R. 135 Abs. 2 EPÜ"],
                   concepts=["epc_weiterbehandlung"], step=_FV + ".3.1", level=2),
            ],
            abschnitt="R. 56 EPÜ: fehlende Teile und Zeichnungen", level=1, concepts=["epc_fehlende_teile"], norms=["R. 56 EPÜ"]),
        *fallkette("e01n80-4", "Die falsche Datei",
            "Y reicht am Donnerstag, 15.1.2026, EP-Y1 unter Inanspruchnahme der Priorität der italienischen Anmeldung IT-Y über die Erfindung A ein. "
            "Versehentlich lädt sie Beschreibung und Ansprüche einer anderen Anmeldung über die Erfindung B hoch. A wurde im Prioritätsintervall in "
            "einer Zeitschrift veröffentlicht. Am 2.3.2026 bemerkt Y den Fehler.",
            [frage("Bis wann muss Y die richtigen Unterlagen einreichen, um den Anmeldetag zu behalten?", 2,
                   ["**Bis 16.3.2026.** Die Frist beträgt zwei Monate nach dem Anmeldetag (R. 56a Abs. 3 EPÜ) und endet am Sonntag, 15.3.2026, verlängert "
                    "auf Montag (R. 134 Abs. 1 EPÜ). In derselben Frist muss Y beantragen, die Unterlagen auf IT-Y zu stützen, Abschrift und Übersetzung "
                    "einreichen und angeben, wo sie enthalten sind (R. 56a Abs. 4 EPÜ)."],
                   optionen=["15.2.2026", "15.3.2026", "16.3.2026", "2.5.2026"],
                   merke="Fälschlich eingereicht: zwei Monate, Rettung über die Priorität.", titel="Frist und Rettung",
                   norms=["R. 56a Abs. 3 EPÜ", "R. 56a Abs. 4 EPÜ", "R. 134 Abs. 1 EPÜ"], concepts=["epc_fristen"]),
             frage("Verschwinden die Unterlagen über B dann aus EP-Y1?", False,
                   ["**Nein!** Bleibt der Anmeldetag nach R. 56a Abs. 4 EPÜ erhalten, werden die richtigen Unterlagen aufgenommen, und die falschen "
                    "verbleiben in der Anmeldung. Entfernen lassen sie sich nur durch Änderung im Rahmen von Art. 123 Abs. 2 EPÜ (Richtlinien A-II, 6.4). "
                    "Nach Veröffentlichung können sie einer späteren Anmeldung über B als älteres Recht entgegenstehen (Art. 54 Abs. 3 EPÜ)."],
                   merke="Die Priorität rettet den Tag, aber die falschen Unterlagen bleiben.", titel="Falsche Unterlagen bleiben", level=2,
                   norms=["R. 56a Abs. 4 EPÜ", "Art. 54 Abs. 3 EPÜ"], concepts=["epc_aeltere_rechte"]),
             frage("Bleibt es beim Anmeldetag 15.1.2026, wenn Y die richtigen Unterlagen am 2.3.2026 einreicht?", False,
                   ["**Nein!** Ohne Prioritätsanspruch am Anmeldetag gibt es keine Rettung über R. 56a Abs. 4 EPÜ (Richtlinien A-II, 6.4.1). Der "
                    "Anmeldetag wird auf den 2.3.2026 neu festgesetzt, die falschen Unterlagen gelten als nicht eingereicht (R. 56a Abs. 3 EPÜ)."],
                   merke="Ohne Prioritätsanspruch am Anmeldetag: Neudatierung.", titel="Abwandlung: keine Priorität",
                   abwandlung="EP-Y1 beanspruchte bei Einreichung keine Priorität.", norms=["R. 56a Abs. 3 EPÜ"], level=2),
            ],
            abschnitt="R. 56a EPÜ: fälschlich eingereichte Unterlagen", level=2, concepts=["epc_fehlende_teile"], norms=["R. 56a EPÜ"]),
        *fallkette("e01n80-5", "Die Anmeldung ohne Ansprüche",
            "X reicht am letzten Tag des Prioritätsjahrs EP-X mit der Priorität der deutschen Anmeldung DE-1 ein. Die Beschreibung stimmt mit DE-1 "
            "überein und beschreibt nur Kapseln aus Aluminium; die Ansprüche von DE-1 betreffen Kapseln aus Aluminium und aus Metall. X vergisst die "
            "Ansprüche. Im Prioritätsintervall erschien ein Artikel über beide.",
            [frage("Erhält EP-X einen Anmeldetag?", True,
                   ["**Ja!** Ansprüche sind kein Erfordernis des Anmeldetags (R. 40 Abs. 1 EPÜ). X kann sie aus eigenem Antrieb nachreichen oder auf "
                    "die Aufforderung des EPA binnen zwei Monaten (R. 57 EPÜ, R. 58 EPÜ; Richtlinien A-III, 15)."],
                   merke="Ohne Ansprüche gibt es einen Anmeldetag.", titel="Anmeldetag ohne Ansprüche", norms=["R. 40 Abs. 1 EPÜ", "R. 57 EPÜ"],
                   concepts=["epc_anmeldetag"]),
             frage("Darf X einen Anspruch auf Kapseln aus Metall nachreichen?", False,
                   ["**Nein!** Nachgereichte Ansprüche brauchen eine Grundlage in Beschreibung und Zeichnungen am Anmeldetag (Art. 123 Abs. 2 EPÜ); "
                    "die Beschreibung offenbart nur Aluminium, die Ansprüche von DE-1 zählen nicht. Ein Anspruch auf Aluminiumkapseln genießt die "
                    "Priorität; der Artikel ist für ihn kein Stand der Technik."],
                   merke="Nachgereichte Ansprüche: Grundlage nur in der eingereichten Beschreibung.", titel="Inhalt der Ansprüche", level=2,
                   norms=["Art. 123 Abs. 2 EPÜ"], concepts=["epc_unzulaessige_erweiterung", "epc_prioritaet"]),
             frage("X reicht auch auf die Aufforderung keine Ansprüche ein. Kann X Weiterbehandlung beantragen?", False,
                   ["**Nein!** Die Anmeldung wird zurückgewiesen (Art. 90 Abs. 5 EPÜ). Die Frist nach R. 58 EPÜ ist von der Weiterbehandlung "
                    "ausgeschlossen (R. 135 Abs. 2 EPÜ); möglich sind Wiedereinsetzung oder Beschwerde (Richtlinien A-III, 15)."],
                   merke="Keine Ansprüche: Zurückweisung, keine Weiterbehandlung.", titel="Versäumte Frist", level=2,
                   norms=["Art. 90 Abs. 5 EPÜ", "R. 135 Abs. 2 EPÜ"], concepts=["epc_weiterbehandlung"], step=_FV + ".3.1"),
            ],
            abschnitt="R. 57, 58 EPÜ: fehlende Ansprüche", level=2, concepts=["epc_anmeldetag"], norms=["R. 58 EPÜ"]),
    ]),
]
