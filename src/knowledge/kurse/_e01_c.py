# -*- coding: utf-8 -*-
"""Kapitel des Normkurses e01 (siehe e01_epue_paper_d.py): Art. 51 EPÜ mit der Gebührenordnung, Art. 94, 97 EPÜ (Prüfung und Erteilung),
Art. 120 EPÜ (Fristen und Zustellung), Art. 122 EPÜ (Wiedereinsetzung) und Art. 133, 134 EPÜ (Vertretung). `order` = Artikel × 100.
Stand: Richtlinien 2026, R. 126, R. 127 EPÜ in der Fassung seit 1.11.2023 (keine Zehn-Tage-Fiktion), R. 7a EPÜ seit 1.4.2024."""
from ._helpers import intro, schema, frage, fallkette  # noqa: F401

_FV = "step:epc_schema_fristversaeumnis"
_TA = "step:epc_schema_teilanmeldung"
_EU = "step:epc_schema_euro_pct"
_ES = "step:epc_schema_einspruch"
_BS = "step:epc_schema_beschwerde"

KAPITEL = [
    # ================================================================== Art. 51 EPÜ und Gebührenordnung
    dict(id="e01n51", order=5100, titel="Art. 51 EPÜ und GebO: Gebühren zahlen, ermäßigen, zurückerhalten", einheiten=[
        intro("e01n51-0", "Wann ist gezahlt, was wird ermäßigt, was kommt zurück?",
              "Art. 51 EPÜ erlaubt dem EPA, Gebühren zu erheben; Höhe und Zahlungsweise regelt die Gebührenordnung (Art. 51 Abs. 4 EPÜ). Paper D "
              "fragt danach in Fallgestaltungen: 2017 (Sprachenermäßigung einer Hochschule, leeres laufendes Konto), 2019 (verspätet aufgefülltes "
              "Konto), 2021 (Rückerstattung von Recherchen- und Prüfungsgebühr) und 2025 (automatische Abbuchung). Ältere Musterlösungen sind "
              "teils überholt: Die Ermäßigungen stehen seit 1.4.2024 in **R. 7a EPÜ**, mit einer neuen Regelung für Kleinstunternehmen; bei "
              "Banküberweisungen gibt es keinen Zuschlag für Aufträge in den letzten zehn Tagen mehr (Art. 7 Abs. 3 GebO); für laufende Konten "
              "gilt eine eigene Sicherheitsvorschrift (Richtlinien A-X, 6.2.2).",
              concepts=["epc_gebuehrenzahlung", "epc_sprachen"], norms=["Art. 51 EPÜ", "R. 7a EPÜ", "R. 7b EPÜ"], abschnitt="Überblick"),
        *fallkette("e01n51-1", "Die Überweisung am letzten Tag",
            "Die Frist für Ns Prüfungsgebühr endet am Montag, 14.9.2026. N erteilt seiner Bank in Wien am 14.9.2026 den Überweisungsauftrag. "
            "Der Betrag wird dem Konto des EPA am 16.9.2026 gutgeschrieben.",
            [frage("Welcher Tag gilt grundsätzlich als Zahlungstag?", 2,
                   ["**Der 16.9.2026.** Als Zahlungstag gilt der Tag, an dem der Betrag auf einem Bankkonto des EPA gutgeschrieben wird "
                    "(Art. 7 Abs. 1 GebO). Die Überweisung ist der Grundfall (Art. 5 Abs. 1 GebO); daneben stehen laufendes Konto, Kreditkarte "
                    "und Umbuchung einer Rückerstattung (Richtlinien A-X, 2)."],
                   optionen=["14.9.2026, der Tag des Auftrags", "15.9.2026, der Tag der Abbuchung bei N", "16.9.2026, der Tag der Gutschrift beim EPA",
                             "Der Tag, an dem das EPA die Zahlung verbucht"],
                   merke="Gezahlt ist, wenn das Geld auf dem Konto des EPA ankommt.", titel="Zahlungstag"),
             frage("Gilt die Frist trotzdem als gewahrt?", True,
                   ["**Ja!** Die Frist gilt als eingehalten, wenn N nachweist, dass er innerhalb der Frist in einem Vertragsstaat den "
                    "Überweisungsauftrag ordnungsgemäß erteilt hat (Art. 7 Abs. 3 GebO); den Nachweis kann das EPA verlangen (Art. 7 Abs. 4 GebO). "
                    "Einen Zuschlag für Aufträge in den letzten zehn Tagen der Frist gibt es nicht mehr."],
                   merke="Auftrag an eine Bank im Vertragsstaat innerhalb der Frist genügt.", titel="Sicherung bei Banküberweisung", level=2),
             frage("Gilt die Frist auch dann als gewahrt?", False,
                   ["**Nein!** Art. 7 Abs. 3 GebO verlangt, dass der Auftrag in einem Vertragsstaat erteilt wird. Mit der Gutschrift am 16.9.2026 "
                    "ist die Frist versäumt; die Anmeldung gilt als zurückgenommen (Art. 94 Abs. 2 EPÜ). N bleibt die Weiterbehandlung (Art. 121 EPÜ)."],
                   merke="Bankauftrag außerhalb der Vertragsstaaten: keine Sicherung.", titel="Bank außerhalb Europas", level=2,
                   abwandlung="N erteilt den Auftrag am 14.9.2026 bei seiner Bank in New York.", norms=["Art. 94 Abs. 2 EPÜ"]),
            ],
            abschnitt="Art. 7 GebO: Zahlungstag", level=1, concepts=["epc_gebuehrenzahlung"], norms=["Art. 51 Abs. 4 EPÜ"]),
        *fallkette("e01n51-2", "Das leere laufende Konto",
            "O hat für seine Anmeldung einen Auftrag zur automatischen Abbuchung von seinem laufenden Konto beim EPA erteilt. Am 13.11.2026, "
            "dem letzten Tag für die Prüfungsgebühr, ist das Konto nicht gedeckt. O hatte am 12.11.2026 eine SEPA-Überweisung zum Auffüllen "
            "veranlasst; sie wird am 16.11.2026 gutgeschrieben.",
            [frage("Gilt die Prüfungsgebühr als am 13.11.2026 gezahlt?", False,
                   ["**Nein!** Reicht das Guthaben nicht, gilt die Zahlung erst an dem Tag als bewirkt, an dem das Konto ausreichend aufgefüllt ist, "
                    "hier am 16.11.2026 (Richtlinien A-X, 4.2.4). Bis dahin werden auch keine weiteren Abbuchungsaufträge ausgeführt."],
                   merke="Ungedecktes Konto: gezahlt erst mit dem Auffüllen.", titel="Ungedecktes Konto"),
             frage("Kann O die Frist trotzdem ohne Weiterbehandlung retten?", True,
                   ["**Ja,** über die Sicherheitsvorschrift für laufende Konten: Die Frist gilt als gewahrt, wenn O nachweist, dass er die Auffüllung "
                    "per SEPA-Überweisung mindestens einen Tag vor Fristablauf veranlasst hat (Richtlinien A-X, 6.2.2). Nach einer Mitteilung über den "
                    "Rechtsverlust beantragt O eine Entscheidung nach R. 112 Abs. 2 EPÜ, hilfsweise Weiterbehandlung (Richtlinien A-X, 6.2.5)."],
                   merke="SEPA einen Tag vorher, SEPA Instant am letzten Tag, sonst drei Tage vorher.", titel="Sicherheitsvorschrift", level=2,
                   norms=["R. 112 Abs. 2 EPÜ"], concepts=["epc_rechtsverlust"]),
             frage("Kann O den Abbuchungsauftrag auf die Prüfungsgebühr beschränken?", False,
                   ["**Nein!** Ein automatischer Abbuchungsauftrag erfasst alle Gebühren seines Typs im Verfahren und kann nicht auf einzelne "
                    "Gebühren beschränkt werden. Es gibt nur drei Typen: alle Gebühren, alle außer Jahresgebühren oder nur Jahresgebühren "
                    "(Richtlinien A-X, 4.3)."],
                   merke="Automatische Abbuchung: alles oder nichts je Typ.", titel="Umfang der automatischen Abbuchung"),
            ],
            abschnitt="Art. 5 GebO: laufendes Konto und automatische Abbuchung", level=2, concepts=["epc_gebuehrenzahlung"], norms=["Art. 51 Abs. 4 EPÜ"]),
        *fallkette("e01n51-3", "Die Hochschule aus Portugal",
            "Eine portugiesische Hochschule H will eine europäische Anmeldung mit der Priorität ihrer portugiesischen Anmeldung einreichen. "
            "Eine englische Übersetzung liegt vor. In den fünf Jahren davor hat H zwei europäische Anmeldungen eingereicht.",
            [frage("Erhält H die Ermäßigung der Anmeldegebühr, wenn sie die Anmeldung gleich auf Englisch einreicht?", False,
                   ["**Nein!** Die Sprachenermäßigung nach R. 7a Abs. 1 EPÜ setzt voraus, dass die Anmeldung, jedenfalls die Beschreibung, in einer "
                    "zugelassenen Nichtamtssprache eingereicht wird (Richtlinien A-X, 9.3.2). H reicht auf Portugiesisch ein und die englische "
                    "Übersetzung danach oder gleichzeitig, nicht früher (Richtlinien A-X, 9.3.1)."],
                   merke="Sprachenermäßigung nur bei Einreichung in der eigenen Nichtamtssprache.", titel="Sprachenermäßigung",
                   norms=["R. 7a Abs. 1 EPÜ", "Art. 14 Abs. 4 EPÜ"], concepts=["epc_sprachen"]),
             frage("Kann H auch die Recherchengebühr ermäßigt zahlen?", True,
                   ["**Ja,** aber nicht wegen der Sprache: R. 7a Abs. 1 EPÜ betrifft nur Anmelde- und Prüfungsgebühr. Als Hochschule mit weniger als "
                    "fünf Anmeldungen in fünf Jahren fällt H zusätzlich unter R. 7a Abs. 3 EPÜ und R. 7a Abs. 4 EPÜ; diese Ermäßigung um 30 % "
                    "erfasst auch die Recherchengebühr (Art. 14 Abs. 1 GebO)."],
                   merke="Hochschulen können beide Ermäßigungen nutzen.", titel="Regelung für kleinere Einheiten", level=2,
                   norms=["R. 7a Abs. 3 EPÜ", "R. 7a Abs. 4 EPÜ"]),
             frage("Werden beide Ermäßigungen bei der Anmeldegebühr zusammen angewandt?", True,
                   ["**Ja!** Greifen mehrere Ermäßigungen für dieselbe Gebühr, werden sie nacheinander berechnet (Art. 14 Abs. 3 GebO; Richtlinien "
                    "A-X, 9.2). H muss spätestens mit der ersten ermäßigten Zahlung erklären, dass sie anspruchsberechtigt ist (R. 7b Abs. 1 EPÜ)."],
                   merke="Mehrere Ermäßigungen: nacheinander, Erklärung bei der ersten Zahlung.", titel="Zusammentreffen", level=3,
                   norms=["R. 7b Abs. 1 EPÜ"]),
            ],
            abschnitt="R. 7a Abs. 1 und 2 EPÜ: Sprachenermäßigung", level=2, concepts=["epc_gebuehrenzahlung"], norms=["R. 7a EPÜ"]),
        *fallkette("e01n51-4", "Das Start-up aus Boston",
            "Q Inc. mit Sitz in Boston hat acht Beschäftigte und einen Jahresumsatz von 1 Mio. EUR. Sie reicht eine europäische Anmeldung auf "
            "Englisch ein; in den fünf Jahren davor hat sie zwei europäische Anmeldungen eingereicht.",
            [frage("Kann Q trotz ihres Sitzes in den USA Gebührenermäßigungen erhalten?", True,
                   ["**Ja!** Die Ermäßigung für Kleinstunternehmen, natürliche Personen, Hochschulen und ähnliche Einrichtungen nach R. 7a Abs. 3 EPÜ "
                    "gilt unabhängig von Staatsangehörigkeit und Sitz (Richtlinien A-X, 9.4.1). Mit weniger als zehn Beschäftigten und höchstens "
                    "2 Mio. EUR Umsatz ist Q ein Kleinstunternehmen."],
                   merke="Kleinstunternehmen weltweit, Sprachenermäßigung nur für Europa.", titel="Anspruchsberechtigung"),
             frage("Wird auch die Jahresgebühr für die Anmeldung ermäßigt?", True,
                   ["**Ja!** R. 7a Abs. 3 EPÜ erfasst Anmelde-, Recherchen-, Prüfungs-, Benennungs- und Erteilungsgebühr sowie die Jahresgebühren "
                    "für europäische Patentanmeldungen, jeweils um 30 % (Art. 14 Abs. 1 GebO). Ein mittleres Unternehmen, das kein "
                    "Kleinstunternehmen ist, erhält diese Ermäßigung nicht."],
                   merke="Sechs Gebühren, darunter die Jahresgebühren der Anmeldung.", titel="Erfasste Gebühren", concepts=["epc_jahresgebuehren"]),
             frage("Bleibt es bei der Ermäßigung?", False,
                   ["**Nein!** Ausgeschlossen ist, wer innerhalb von fünf Jahren vor dem Anmeldetag fünf oder mehr europäische oder Euro-PCT-Anmeldungen "
                    "eingereicht hat (R. 7a Abs. 4 EPÜ). Hat Q schon ermäßigt gezahlt, fordert das EPA den Fehlbetrag binnen zwei Monaten an "
                    "(Richtlinien A-X, 9.4.3)."],
                   merke="Fünf Anmeldungen in fünf Jahren beenden die Ermäßigung.", titel="Obergrenze", level=2,
                   abwandlung="Q hat in den fünf Jahren vor dem Anmeldetag fünf europäische Anmeldungen eingereicht.", norms=["R. 7a Abs. 4 EPÜ"]),
            ],
            abschnitt="R. 7a Abs. 3 und 4 EPÜ: Kleinstunternehmen", level=1, concepts=["epc_gebuehrenzahlung"], norms=["R. 7a Abs. 3 EPÜ"]),
        *fallkette("e01n51-5", "Zwei Anmeldungen, die niemand mehr will",
            "R hat für EP-1 und EP-2 bei Einreichung Recherchen- und Prüfungsgebühr gezahlt. Zu EP-1 fordert das EPA nach R. 58 EPÜ Ansprüche an; "
            "die Recherche hat nicht begonnen. Für EP-2 hat R auf die Aufforderung nach R. 70 Abs. 2 EPÜ verzichtet; mit dem Recherchenbericht "
            "kam ein erster Bescheid der Prüfungsabteilung.",
            [frage("Erhält R bei Rücknahme von EP-1 die Recherchengebühr voll zurück?", True,
                   ["**Ja!** Die Recherchengebühr wird voll erstattet, wenn die Anmeldung zurückgenommen wird, bevor das EPA mit dem Recherchenbericht "
                    "begonnen hat (Art. 9 Abs. 1 GebO). Den Beginn der Recherche zeigt das Formblatt 1704 in der Akte (Richtlinien A-X, 10.2.1)."],
                   merke="Recherche nicht begonnen: Recherchengebühr voll zurück.", titel="Recherchengebühr"),
             frage("Erhält R auch die Prüfungsgebühr für EP-1 voll zurück?", True,
                   ["**Ja!** Wird die Anmeldung vor Beginn der Sachprüfung zurückgenommen, zurückgewiesen oder gilt sie als zurückgenommen, wird die "
                    "Prüfungsgebühr voll erstattet (Art. 11 lit. a GebO; Richtlinien A-VI, 2.5)."],
                   merke="Vor der Sachprüfung: Prüfungsgebühr voll zurück.", titel="Prüfungsgebühr vor der Sachprüfung"),
             frage("Kann R für EP-2 noch Gebühren zurückerhalten?", True,
                   ["**Ja,** die Hälfte der Prüfungsgebühr, wenn R EP-2 vor Ablauf der Frist zur Erwiderung auf den ersten Bescheid der "
                    "Prüfungsabteilung nach Art. 94 Abs. 3 EPÜ zurücknimmt (Art. 11 lit. b GebO). Die Recherchengebühr bleibt beim EPA, weil die "
                    "Recherche durchgeführt ist (Art. 9 Abs. 1 GebO)."],
                   merke="Nach Beginn der Sachprüfung: 50 % bis zum Ablauf der ersten Bescheidsfrist.", titel="Hälftige Erstattung", level=2,
                   concepts=["epc_pruefungsverfahren"]),
             frage("Darf R eine Rücknahme davon abhängig machen, dass die Prüfungsgebühr voll erstattet wird?", True,
                   ["**Ja!** Wer unsicher ist, ob die Sachprüfung schon begonnen hat, kann die Anmeldung unter der Bedingung der vollen "
                    "Rückerstattung zurücknehmen (Richtlinien A-VI, 2.5). Den Beginn der Sachprüfung zeigt das Formblatt 2095 in der Akte."],
                   merke="Bedingte Rücknahme sichert die volle Erstattung.", titel="Bedingte Rücknahme", level=3),
            ],
            abschnitt="Art. 9 und 11 GebO: Rückerstattung", level=2, concepts=["epc_gebuehrenzahlung"], norms=["Art. 51 EPÜ"]),
    ]),
    # ================================================================== Art. 94, 97 EPÜ, R. 70, R. 71 EPÜ
    dict(id="e01n94", order=9400, titel="Art. 94, 97 EPÜ, R. 70, R. 71 EPÜ: Prüfung und Erteilung", einheiten=[
        intro("e01n94-0", "Vom Prüfungsantrag bis zum Hinweis auf die Erteilung",
              "Prüfung und Erteilung bilden in Paper D den Rahmen vieler Fristfragen: 2018 (Änderung nach dem Einverständnis), 2022 (Berichtigung "
              "auf die Mitteilung nach R. 71 Abs. 3 EPÜ), 2023 (nicht recherchierte Erfindung) und 2025 (Erteilung nach Zurückverweisung). Der "
              "Ablauf: **Prüfungsantrag** mit Gebühr binnen sechs Monaten nach dem Hinweis auf den Recherchenbericht (Art. 94 Abs. 1 EPÜ, "
              "R. 70 Abs. 1 EPÜ), zugleich Erwiderung auf eine negative Stellungnahme (R. 70a Abs. 1 EPÜ); **Bescheide** nach Art. 94 Abs. 3 EPÜ; "
              "**Mitteilung nach R. 71 Abs. 3 EPÜ** mit vier Monaten für Gebühren und Übersetzungen oder für einen Änderungsantrag nach "
              "R. 71 Abs. 6 EPÜ; wirksam wird die Erteilung mit dem Hinweis im Patentblatt (Art. 97 Abs. 3 EPÜ).",
              concepts=["epc_pruefungsverfahren", "epc_erteilung"],
              norms=["Art. 94 EPÜ", "Art. 97 EPÜ", "R. 70 EPÜ", "R. 70a EPÜ", "R. 71 EPÜ"], abschnitt="Überblick"),
        *fallkette("e01n94-1", "Der Recherchenbericht mit Einwänden",
            "A reicht im März 2025 die Anmeldung EP-A mit dem Formblatt 1001 ein und zahlt nur Anmelde- und Recherchengebühr. Am 13.5.2026 "
            "weist das Europäische Patentblatt auf die Veröffentlichung des Recherchenberichts hin. Die Stellungnahme zur Recherche hält "
            "Anspruch 1 für nicht neu.",
            [frage("Bis wann muss A die Prüfung beantragen?", 1,
                   ["**Bis 13.11.2026.** Die Frist beträgt sechs Monate ab dem Hinweis im Patentblatt (R. 70 Abs. 1 EPÜ). Den schriftlichen Antrag "
                    "enthält schon das Formblatt 1001; er gilt aber erst mit Zahlung der Prüfungsgebühr als gestellt (Art. 94 Abs. 1 EPÜ; "
                    "Richtlinien A-VI, 2.2)."],
                   optionen=["13.8.2026", "13.11.2026", "23.11.2026", "Sechs Monate nach der Mitteilung nach R. 69 EPÜ"],
                   merke="Prüfungsantrag gleich Formblatt plus Gebühr, sechs Monate ab Hinweis auf den Recherchenbericht.", titel="Frist für den Prüfungsantrag",
                   norms=["R. 70 Abs. 1 EPÜ", "Art. 94 Abs. 1 EPÜ"], step=_FV + ".1.1"),
             frage("Muss A innerhalb derselben Frist auch auf die Stellungnahme zur Recherche erwidern?", True,
                   ["**Ja!** Ist die Stellungnahme negativ, ist innerhalb der Frist nach R. 70 Abs. 1 EPÜ zu erwidern (R. 70a Abs. 1 EPÜ), sonst gilt "
                    "die Anmeldung als zurückgenommen (R. 70a Abs. 3 EPÜ). Ein bloßer Antrag auf mündliche Verhandlung oder pauschaler Widerspruch "
                    "ist keine Erwiderung (Richtlinien B-XI, 8)."],
                   merke="Negative Stellungnahme zur Recherche: Erwiderung ist Pflicht.", titel="Erwiderung auf die Stellungnahme",
                   norms=["R. 70a Abs. 1 EPÜ", "R. 70a Abs. 3 EPÜ"]),
             frage("A zahlt bis 13.11.2026 weder Prüfungs- noch Benennungsgebühr und erwidert nicht. Genügt eine Weiterbehandlungsgebühr?", False,
                   ["**Nein!** A hat drei voneinander unabhängige Handlungen versäumt, jede mit eigener Rechtsfolge (Art. 94 Abs. 2 EPÜ, "
                    "R. 39 Abs. 2 EPÜ und R. 70a Abs. 3 EPÜ). Für jede ist eine Weiterbehandlungsgebühr zu zahlen und die Handlung nachzuholen "
                    "(R. 135 Abs. 1 EPÜ; Richtlinien E-VIII, 2)."],
                   merke="Unabhängige Handlungen, unabhängige Weiterbehandlungsgebühren.", titel="Mehrere versäumte Handlungen", level=2,
                   norms=["R. 39 Abs. 2 EPÜ", "R. 135 Abs. 1 EPÜ"], concepts=["epc_weiterbehandlung"], step=_FV + ".3.3"),
            ],
            abschnitt="Art. 94 Abs. 1 und 2 EPÜ: Prüfungsantrag", level=1, concepts=["epc_pruefungsverfahren"], norms=["Art. 94 Abs. 2 EPÜ"]),
        *fallkette("e01n94-2", "Die zweite Erfindung aus der PCT-Phase",
            "Das EPA hat als Internationale Recherchenbehörde zur PCT-Anmeldung von B nur die erste von zwei Erfindungen recherchiert; B zahlte "
            "keine zusätzliche Recherchengebühr. In der europäischen Phase gibt es keine ergänzende Recherche. B richtet die Ansprüche nun auf "
            "die zweite Erfindung.",
            [frage("Kann B für die zweite Erfindung noch eine Recherche erhalten?", True,
                   ["**Ja!** Die Prüfungsabteilung fordert B auf, für jede nicht recherchierte Erfindung binnen zwei Monaten eine Recherchengebühr zu "
                    "zahlen (R. 164 Abs. 2 lit. a EPÜ). Das Ergebnis übersendet sie mit einem Bescheid nach Art. 94 Abs. 3 EPÜ oder mit der "
                    "Mitteilung nach R. 71 Abs. 3 EPÜ (R. 164 Abs. 2 lit. b EPÜ)."],
                   merke="EPA als ISA, Erfindung nicht recherchiert: Gebühr nach R. 164 Abs. 2 EPÜ.", titel="Recherche in der Prüfung", step=_EU + ".4"),
             frage("B versäumt die Zweimonatsfrist. Kann B Weiterbehandlung beantragen?", False,
                   ["**Nein!** Die Frist nach R. 164 Abs. 2 EPÜ ist von der Weiterbehandlung ausgeschlossen (R. 135 Abs. 2 EPÜ) und nicht "
                    "verlängerbar (Richtlinien C-III, 3.1). B muss die Anmeldung auf eine recherchierte Erfindung beschränken "
                    "(R. 164 Abs. 2 EPÜ; Richtlinien C-III, 3.2.1)."],
                   merke="R. 164 Abs. 2 EPÜ: keine Weiterbehandlung.", titel="Versäumte Recherchengebühr", level=2,
                   norms=["R. 135 Abs. 2 EPÜ"], concepts=["epc_weiterbehandlung"], step=_FV + ".3.1"),
             frage("Ist die zweite Erfindung damit für B verloren?", False,
                   ["**Nein!** Nicht recherchierte Gegenstände kann B in einer Teilanmeldung weiterverfolgen, solange die Anmeldung anhängig ist "
                    "(Art. 76 Abs. 1 EPÜ, R. 36 Abs. 1 EPÜ; Richtlinien C-III, 3.3). Für die Teilanmeldung fällt eine eigene Recherchengebühr an "
                    "(R. 36 Abs. 3 EPÜ)."],
                   merke="Nicht recherchiert: Teilanmeldung statt Prüfung in der Stammanmeldung.", titel="Ausweg Teilanmeldung", level=2,
                   norms=["R. 36 Abs. 1 EPÜ"], concepts=["epc_teilanmeldung"], step=_TA + ".1"),
            ],
            abschnitt="Art. 94 Abs. 3 EPÜ: nur recherchierte Erfindungen", level=2, concepts=["epc_einheitlichkeit", "epc_euro_pct"],
            norms=["R. 164 Abs. 2 EPÜ", "Art. 94 Abs. 3 EPÜ"]),
        *fallkette("e01n94-3", "Die Mitteilung über die Erteilungsabsicht",
            "C hat EP-C auf Englisch mit 15 Ansprüchen eingereicht; in der Prüfung sind es 17 geworden. Die Mitteilung nach R. 71 Abs. 3 EPÜ "
            "ist auf den 15.6.2026 datiert. C will möglichst bald ein Patent, hat aber in Anspruch 3 einen offensichtlichen Schreibfehler entdeckt.",
            [frage("Wann endet die Frist für die Antwort auf die Mitteilung?", 1,
                   ["**Am 15.10.2026.** Die Frist beträgt vier Monate (R. 71 Abs. 3 EPÜ). Die Mitteilung gilt als an dem Tag zugestellt, auf den sie "
                    "datiert ist (R. 126 Abs. 2 EPÜ, R. 127 Abs. 2 EPÜ); zehn Tage wie in älteren Musterlösungen kommen nicht mehr hinzu."],
                   optionen=["15.8.2026", "15.10.2026", "25.10.2026", "15.12.2026"],
                   merke="R. 71 Abs. 3 EPÜ: vier Monate ab dem Datum der Mitteilung.", titel="Frist", concepts=["epc_fristen"]),
             frage("Würde es genügen, die Erteilungsgebühr zu zahlen und die Ansprüche ins Deutsche und Französische zu übersetzen?", False,
                   ["**Nein!** Für den 16. und 17. Anspruch sind Anspruchsgebühren zu zahlen (R. 71 Abs. 4 EPÜ). Erst wenn alle Gebühren gezahlt und "
                    "die Übersetzungen eingereicht sind, gilt das Einverständnis mit der Fassung als erklärt (R. 71 Abs. 5 EPÜ); fehlt etwas, gilt die "
                    "Anmeldung als zurückgenommen (R. 71 Abs. 7 EPÜ)."],
                   merke="Einverständnis: Erteilungsgebühr, Anspruchsgebühren, Übersetzungen.", titel="Einverständnis",
                   norms=["R. 71 Abs. 4 EPÜ", "R. 71 Abs. 5 EPÜ", "R. 71 Abs. 7 EPÜ"]),
             frage("Muss C Gebühren zahlen und Übersetzungen einreichen, wenn er fristgerecht die Berichtigung des Schreibfehlers beantragt?", False,
                   ["**Nein!** Auf einen begründeten Berichtigungsantrag erlässt die Prüfungsabteilung bei Zustimmung eine neue Mitteilung nach "
                    "R. 71 Abs. 3 EPÜ, sonst nimmt sie die Prüfung wieder auf (R. 71 Abs. 6 EPÜ). Gebühren und Übersetzungen sind erst auf die neue "
                    "Mitteilung fällig (Richtlinien C-V, 4.1); die Begründung sollte R. 139 EPÜ darlegen (Richtlinien C-V, 4.3)."],
                   merke="Änderungs- oder Berichtigungsantrag ersetzt die Zahlung auf die erste Mitteilung.", titel="Berichtigung", level=2,
                   norms=["R. 71 Abs. 6 EPÜ", "R. 139 EPÜ"], concepts=["epc_berichtigung"]),
            ],
            abschnitt="R. 71 Abs. 3 EPÜ: Mitteilung über die Erteilungsabsicht", level=1, concepts=["epc_erteilung"], norms=["R. 71 Abs. 3 EPÜ"]),
        *fallkette("e01n94-4", "Der späte Fund nach dem Einverständnis",
            "D hat auf die Mitteilung nach R. 71 Abs. 3 EPÜ alle Gebühren gezahlt und die Übersetzungen eingereicht. Zwei Wochen später erfährt "
            "er von einer älteren europäischen Anmeldung, die Anspruch 1 die Neuheit nimmt, nicht aber dem abhängigen Anspruch 2. Der "
            "Erteilungsbeschluss ist noch nicht ergangen.",
            [frage("Kann D noch die Streichung von Anspruch 1 erreichen?", True,
                   ["**Ja!** Bis zur Entscheidung über die Erteilung kann die Prüfungsabteilung das Prüfungsverfahren wieder aufnehmen "
                    "(R. 71a Abs. 2 EPÜ), und zwar bis zur Abgabe der Entscheidung an die interne Poststelle (G 12/91). Änderungen nach dem "
                    "Einverständnis lässt sie nur ausnahmsweise zu (R. 137 Abs. 3 EPÜ); eine rasch prüfbare, gewährbare Streichung spricht dafür "
                    "(Richtlinien H-II, 2.6)."],
                   merke="Bis zur Abgabe an die Poststelle ist die Erteilung nicht endgültig.", titel="Änderung nach dem Einverständnis", level=2,
                   norms=["R. 71a Abs. 2 EPÜ", "R. 137 Abs. 3 EPÜ"], cases=["epc_g_12_91"]),
             frage("Wird das Patent mit dem Datum des Erteilungsbeschlusses wirksam?", False,
                   ["**Nein!** Die Entscheidung über die Erteilung wird erst an dem Tag wirksam, an dem der Hinweis auf die Erteilung im Europäischen "
                    "Patentblatt bekannt gemacht wird (Art. 97 Abs. 3 EPÜ). Ab diesem Tag läuft auch die Einspruchsfrist (Art. 99 Abs. 1 EPÜ)."],
                   merke="Wirksam mit dem Hinweis im Patentblatt.", titel="Wirksamwerden", norms=["Art. 97 Abs. 3 EPÜ", "Art. 99 Abs. 1 EPÜ"]),
             frage("Kann D noch am Tag des Hinweises auf die Erteilung eine Teilanmeldung einreichen?", False,
                   ["**Nein!** Die Anmeldung ist nur bis zum Tag vor dem Hinweis auf die Erteilung anhängig; R. 134 EPÜ verlängert das nicht "
                    "(Richtlinien A-IV, 1.1.1). Die Teilanmeldung muss spätestens am Vortag eingehen (R. 36 Abs. 1 EPÜ)."],
                   merke="Teilanmeldung spätestens am Tag vor dem Hinweis auf die Erteilung.", titel="Letzter Tag für die Teilanmeldung", level=2,
                   norms=["R. 36 Abs. 1 EPÜ"], concepts=["epc_anhaengigkeit", "epc_teilanmeldung"], step=_TA + ".1"),
            ],
            abschnitt="Art. 97 EPÜ: Erteilungsbeschluss und Wirksamkeit", level=1, concepts=["epc_erteilung"], norms=["Art. 97 EPÜ"]),
        *fallkette("e01n94-5", "Erteilung nach Zurückverweisung",
            "Die Prüfungsabteilung hatte EP-E zurückgewiesen. Die Beschwerdekammer verweist die Sache zur Erteilung in einer von ihr abschließend "
            "festgelegten Fassung zurück. Auf die Mitteilung nach R. 71 Abs. 3 EPÜ beantragt E nur einen zusätzlichen abhängigen Anspruch und "
            "zahlt nichts. Das EPA teilt einen Rechtsverlust mit.",
            [frage("Hätte die Prüfungsabteilung eine neue Mitteilung nach R. 71 Abs. 3 EPÜ erlassen müssen?", False,
                   ["**Nein!** Die Prüfungsabteilung ist an die Entscheidung der Kammer gebunden (Art. 111 Abs. 2 EPÜ); das Verfahren nach "
                    "R. 71 Abs. 6 EPÜ ist daher nicht anwendbar. Der Änderungsantrag ersetzt die Zahlung nicht, und die Anmeldung gilt als "
                    "zurückgenommen (R. 71 Abs. 7 EPÜ; Richtlinien E-XI, 9)."],
                   merke="Fassung von der Kammer festgelegt: kein Änderungsantrag nach R. 71 Abs. 6 EPÜ.", titel="Bindung an die Kammer",
                   norms=["Art. 111 Abs. 2 EPÜ", "R. 71 Abs. 7 EPÜ"], concepts=["epc_beschwerde"]),
             frage("Kann E den zusätzlichen Anspruch noch in einem Patent erhalten?", True,
                   ["**Ja,** über eine Teilanmeldung. Dazu muss EP-E erst wieder anhängig werden: Weiterbehandlung binnen zwei Monaten nach der "
                    "Mitteilung mit Gebühr, Erteilungsgebühr und Übersetzungen der Fassung der Kammer (Art. 121 EPÜ, R. 135 Abs. 1 EPÜ). Danach "
                    "Teilanmeldung mit dem Zusatzanspruch (R. 36 Abs. 1 EPÜ), ohne Doppelpatentierung (G 4/19)."],
                   merke="Erst Weiterbehandlung, dann Teilanmeldung.", titel="Ausweg", level=3,
                   norms=["R. 135 Abs. 1 EPÜ", "R. 36 Abs. 1 EPÜ"], cases=["epc_g_4_19"], concepts=["epc_weiterbehandlung", "epc_teilanmeldung"],
                   step=_FV + ".5"),
            ],
            abschnitt="R. 71 Abs. 6 und 7 EPÜ: nach der Beschwerde", level=3, concepts=["epc_erteilung"], norms=["R. 71 Abs. 6 EPÜ"]),
    ]),
    # ================================================================== Art. 120 EPÜ, R. 126, R. 127, R. 131, R. 134 EPÜ
    dict(id="e01n120", order=12000, titel="Art. 120 EPÜ, R. 126, R. 127, R. 131, R. 134 EPÜ: Fristen und Zustellung", einheiten=[
        intro("e01n120-0", "Rechnen ohne zehn Tage",
              "Fast jede Paper-D-Frage verlangt eine Fristberechnung, ausdrücklich etwa 2016, 2019 und 2022. Art. 120 EPÜ verweist auf die "
              "Ausführungsordnung: Ereignis bestimmen (R. 131 Abs. 2 EPÜ), Monatsfrist am Tag mit derselben Zahl oder am Monatsletzten enden "
              "lassen (R. 131 Abs. 4 EPÜ), dann verlängern, wenn eine Annahmestelle geschlossen oder die Post gestört ist (R. 134 EPÜ). "
              "**Achtung, neues Recht:** Seit 1.11.2023 gilt ein Schriftstück als an dem Tag zugestellt, auf den es datiert ist "
              "(R. 126 Abs. 2 EPÜ, R. 127 Abs. 2 EPÜ). Die Zehn-Tage-Regel älterer Musterlösungen ist abgeschafft; geht ein Schriftstück mehr als "
              "sieben Tage nach seinem Datum zu, verlängert sich die Frist nur um die überschießenden Tage.",
              concepts=["epc_fristen", "epc_zustellung"], norms=["Art. 120 EPÜ", "R. 126 EPÜ", "R. 127 EPÜ", "R. 131 EPÜ", "R. 134 EPÜ"],
              abschnitt="Überblick"),
        *fallkette("e01n120-1", "Die Zurückweisung in der Mailbox",
            "Die Prüfungsabteilung weist die Anmeldung von F zurück. Die Entscheidung ist auf den 3.6.2026 datiert und wird elektronisch in die "
            "MyEPO-Mailbox von Fs Vertreterin zugestellt. Diese öffnet die Mailbox erst am 5.6.2026.",
            [frage("Wann gilt die Entscheidung als zugestellt?", 0,
                   ["**Am 3.6.2026.** Das elektronische Dokument gilt als an dem Tag zugestellt, auf den es datiert ist (R. 127 Abs. 2 EPÜ). Auf das "
                    "Öffnen der Mailbox kommt es nicht an; eine Zehn-Tage-Fiktion gibt es seit 1.11.2023 nicht mehr (Richtlinien E-II, 2.3)."],
                   optionen=["3.6.2026", "5.6.2026", "10.6.2026", "13.6.2026"],
                   merke="Zugestellt am Datum des Schriftstücks.", titel="Zustellung", norms=["R. 127 Abs. 2 EPÜ"], step=_FV + ".1.1"),
             frage("Bis wann muss F Beschwerde einlegen und die Beschwerdegebühr zahlen?", 0,
                   ["**Bis 3.8.2026.** Die Beschwerdefrist beträgt zwei Monate nach Zustellung (Art. 108 Satz 1 EPÜ) und endet am Tag mit derselben "
                    "Zahl (R. 131 Abs. 4 EPÜ). Der 3.8.2026 ist ein Montag."],
                   optionen=["3.8.2026", "5.8.2026", "13.8.2026", "3.10.2026"],
                   merke="Beschwerde: zwei Monate ab Zustellung.", titel="Beschwerdefrist", norms=["Art. 108 EPÜ", "R. 131 Abs. 4 EPÜ"],
                   concepts=["epc_beschwerde"], step=_BS + ".3"),
             frage("Läuft die Frist für die Beschwerdebegründung ab der Einlegung der Beschwerde?", False,
                   ["**Nein!** Die Begründung ist innerhalb von vier Monaten nach Zustellung der Entscheidung einzureichen (Art. 108 Satz 3 EPÜ). Die "
                    "Frist endet am 3.10.2026, einem Samstag, und verlängert sich auf Montag, 5.10.2026 (R. 134 Abs. 1 EPÜ)."],
                   merke="Begründung: vier Monate ab Zustellung, nicht ab Einlegung.", titel="Begründungsfrist", level=2,
                   norms=["Art. 108 EPÜ", "R. 134 Abs. 1 EPÜ"], concepts=["epc_beschwerde"], step=_FV + ".1.3"),
             frage("Verlängert sich die Beschwerdefrist?", True,
                   ["**Ja,** um zwei Tage bis 5.8.2026. Geht ein Schriftstück nachweislich mehr als sieben Tage nach seinem Datum zu, läuft die Frist "
                    "um die überschießenden Tage später ab (R. 126 Abs. 2 EPÜ). Der 12.6. liegt neun Tage nach dem 3.6., also zwei Tage zu viel."],
                   merke="Sieben Tage sind gedeckt, jeder weitere Tag verlängert.", titel="Verspäteter Zugang", level=2,
                   abwandlung="Die Entscheidung wird per Einschreiben versandt und geht nachweislich erst am 12.6.2026 zu.",
                   norms=["R. 126 Abs. 2 EPÜ"]),
            ],
            abschnitt="R. 126 und R. 127 EPÜ: Zustellung", level=1, concepts=["epc_zustellung", "epc_fristen"], norms=["R. 126 Abs. 2 EPÜ"]),
        *fallkette("e01n120-2", "Der Bescheid vom Monatsende",
            "Die Prüfungsabteilung erlässt einen Bescheid nach Art. 94 Abs. 3 EPÜ, datiert auf den 31.10.2025, mit einer Frist von vier "
            "Monaten. G braucht für Vergleichsversuche mehr Zeit.",
            [frage("Wann endet die Frist?", 1,
                   ["**Am 2.3.2026.** Der Februar hat keinen 31. Tag; die Frist endet am Monatsletzten, dem 28.2.2026 (R. 131 Abs. 4 EPÜ). Das ist "
                    "ein Samstag, an dem die Annahmestellen geschlossen sind; die Frist erstreckt sich auf Montag, 2.3.2026 (R. 134 Abs. 1 EPÜ)."],
                   optionen=["28.2.2026", "2.3.2026", "3.3.2026", "10.3.2026"],
                   merke="Monatsletzter, dann Wochenende prüfen.", titel="Monatsende", norms=["R. 131 Abs. 4 EPÜ", "R. 134 Abs. 1 EPÜ"],
                   step=_FV + ".1.2"),
             frage("G beantragt am 20.2.2026 ohne Begründung eine Verlängerung um zwei Monate. Bis wann läuft die verlängerte Frist?", 0,
                   ["**Bis 30.4.2026.** Vom EPA bestimmte Fristen können auf Antrag vor Ablauf verlängert werden (R. 132 Abs. 2 EPÜ). Die verlängerte "
                    "Frist wird vom Beginn der ursprünglichen Frist an berechnet: sechs Monate ab 31.10.2025. Bis zu zwei Monate und insgesamt "
                    "höchstens sechs Monate werden in der Regel auch ohne Gründe gewährt (Richtlinien E-VIII, 1.6.1)."],
                   optionen=["30.4.2026", "2.5.2026", "4.5.2026", "28.4.2026"],
                   merke="Verlängerung rechnet vom ursprünglichen Fristbeginn.", titel="Verlängerung nach R. 132 EPÜ", level=2,
                   norms=["R. 132 Abs. 2 EPÜ"]),
             frage("Endet die Frist für die Zahlung mit Zuschlagsgebühr erst am 1.12.2026?", False,
                   ["**Nein!** Die Sechsmonatsfrist des R. 51 Abs. 2 EPÜ beginnt am Fälligkeitstag, auch wenn er ein Sonntag ist, und läuft von "
                    "Monatsende zu Monatsende (J 4/91; Richtlinien A-X, 5.2.4). Sie endet am 30.11.2026, einem Montag; R. 134 EPÜ greift nur für "
                    "ihr Ende."],
                   merke="Fristenketten: Die Verlängerung einer Frist verschiebt den Beginn der nächsten nicht.", titel="Fristenkette Jahresgebühr",
                   level=3, abwandlung="Die Jahresgebühr für Gs Anmeldung war am 31.5.2026, einem Sonntag, fällig; G hat sie nicht gezahlt.",
                   norms=["R. 51 Abs. 2 EPÜ", "R. 131 Abs. 2 EPÜ"], cases=["epc_j_4_91"], concepts=["epc_jahresgebuehren"]),
            ],
            abschnitt="R. 131 und R. 132 EPÜ: Berechnung und Verlängerung", level=1, concepts=["epc_fristen"], norms=["R. 131 EPÜ"]),
        *fallkette("e01n120-3", "Koningsdag",
            "Die Frist für Hs Erwiderung läuft am Montag, 27.4.2026, ab. An diesem Tag ist die Annahmestelle Den Haag wegen des Koningsdag "
            "geschlossen; München und Berlin sind geöffnet. H reicht die Erwiderung am 28.4.2026 online ein.",
            [frage("Ist die Erwiderung rechtzeitig?", True,
                   ["**Ja!** Ist auch nur eine der Annahmestellen in München, Den Haag oder Berlin geschlossen, erstreckt sich die Frist auf den "
                    "nächsten Tag, an dem alle geöffnet sind (R. 134 Abs. 1 EPÜ, R. 35 Abs. 1 EPÜ). Wo und wie H einreicht, spielt keine Rolle; die "
                    "Schließtage veröffentlicht das EPA im Amtsblatt."],
                   merke="Eine geschlossene Annahmestelle verlängert für alle.", titel="Schließtag einer Annahmestelle", step=_FV + ".1.3"),
             frage("Kann H die europäische Anmeldung am 28.4.2026 noch mit Priorität einreichen?", True,
                   ["**Ja!** R. 134 EPÜ gilt für alle Fristen des Übereinkommens, auch für die Prioritätsfrist des Art. 87 Abs. 1 EPÜ, die "
                    "Einspruchsfrist und die Frist für den Eintritt in die europäische Phase (Richtlinien E-VIII, 1.6.2.3)."],
                   merke="Auch die Prioritätsfrist wird nach R. 134 EPÜ verlängert.", titel="Prioritätsfrist", level=2,
                   abwandlung="Am 27.4.2026 endet die Prioritätsfrist für Hs Nachanmeldung.",
                   norms=["Art. 87 Abs. 1 EPÜ"], concepts=["epc_prioritaet"]),
             frage("Verlängert sich die Frist, wenn alle Annahmestellen geöffnet sind, die Online-Einreichung aber wegen angekündigter Wartung "
                   "fünf Stunden ausfällt?", True,
                   ["**Ja!** R. 134 Abs. 1 Satz 2 EPÜ gilt entsprechend, wenn eine zugelassene Einrichtung zur elektronischen Einreichung nicht "
                    "verfügbar ist. Bei geplanter Wartung greift das ab vier Stunden; kürzere, mindestens zwei Arbeitstage vorher angekündigte "
                    "Ausfälle verlängern nicht (Richtlinien E-VIII, 1.6.2.1)."],
                   merke="Ausfall der Online-Einreichung zählt wie eine geschlossene Annahmestelle.", titel="Ausfall der Online-Einreichung", level=2),
            ],
            abschnitt="R. 134 Abs. 1 EPÜ: geschlossene Annahmestellen", level=1, concepts=["epc_fristen"], norms=["R. 134 Abs. 1 EPÜ"]),
        *fallkette("e01n120-4", "Die Störung der Post",
            "Die Frist für Js Beschwerdebegründung läuft am 15.9.2026 ab. Js Vertreter hat seinen Geschäftssitz im Vertragsstaat P. Das EPA macht "
            "bekannt, dass die Postzustellung in P vom 10.9. bis 21.9.2026 allgemein gestört war.",
            [frage("Bis wann kann J die Begründung einreichen?", 2,
                   ["**Bis 22.9.2026.** Läuft eine Frist während einer allgemeinen Störung der Post in einem Vertragsstaat ab, erstreckt sie sich für "
                    "Beteiligte mit Wohnsitz oder Vertreter in diesem Staat auf den ersten Tag nach dem Ende der Störung (R. 134 Abs. 2 EPÜ). Beginn "
                    "und Ende macht das EPA bekannt (R. 134 Abs. 4 EPÜ)."],
                   optionen=["15.9.2026", "21.9.2026", "22.9.2026", "28.9.2026"],
                   merke="Allgemeine Störung: Frist bis zum ersten Tag nach ihrem Ende.", titel="Allgemeine Störung", step=_FV + ".1.3"),
             frage("Darf J sich auf die bekannt gemachte Verlängerung verlassen?", True,
                   ["**Ja!** Beteiligte müssen Bekanntmachungen nach R. 134 Abs. 4 EPÜ nicht ohne Anlass hinterfragen. Nach dem Grundsatz des "
                    "Vertrauensschutzes dürfen sie sich darauf verlassen, auch wenn tatsächlich keine allgemeine Störung vorlag (J 10/20)."],
                   merke="Auf Bekanntmachungen des EPA darf man sich verlassen.", titel="Vertrauensschutz", level=2,
                   abwandlung="Später zeigt sich, dass die Post in P normal lief; die Bekanntmachung beruhte auf einer Fehleinschätzung.",
                   cases=["epc_j_10_20"], concepts=["epc_vertrauensschutz"]),
             frage("Kann die Begründung als rechtzeitig gelten?", True,
                   ["**Ja,** auf Antrag mit Nachweis (R. 134 Abs. 5 EPÜ): Ein außergewöhnliches Ereignis störte die Post am Ort des Vertreters an einem "
                    "der letzten zehn Tage vor Fristablauf, und J hat spätestens am fünften Tag nach dem Ende der Störung, dem 25.9.2026, versandt "
                    "(Richtlinien E-VIII, 1.6.2.2)."],
                   merke="Einzelne Störung: Nachweis, letzte zehn Tage, Versand binnen fünf Tagen.", titel="Störung im Einzelfall", level=3,
                   abwandlung="Es gibt keine Bekanntmachung. Ein Hochwasser legt vom 11.9. bis 20.9.2026 die Post am Kanzleisitz lahm; J versendet die "
                              "Begründung am 24.9.2026.",
                   norms=["R. 134 Abs. 5 EPÜ"]),
            ],
            abschnitt="R. 134 Abs. 2 und 5 EPÜ: Störungen", level=2, concepts=["epc_fristen"], norms=["R. 134 Abs. 2 EPÜ"]),
    ]),
    # ================================================================== Art. 122 EPÜ, R. 136 EPÜ
    dict(id="e01n122", order=12200, titel="Art. 122 EPÜ, R. 136 EPÜ: Wiedereinsetzung", einheiten=[
        intro("e01n122-0", "Der Rettungsweg mit Verschuldensprüfung",
              "Die Wiedereinsetzung hilft, wenn die Weiterbehandlung ausgeschlossen oder ihre Frist schon abgelaufen ist (R. 136 Abs. 3 EPÜ). "
              "Paper D fragt sie regelmäßig: 2015 und 2021 die Prioritätsfrist, 2018 die Beschwerdefrist von Inhaber und Einsprechendem, 2022 und "
              "2024 die versäumte Weiterbehandlungsfrist. Zu prüfen sind: **Statthaftigkeit** (unmittelbarer Rechtsverlust, Anmelder oder "
              "Inhaber), **Frist** (zwei Monate nach Wegfall des Hindernisses, höchstens ein Jahr; Priorität: zwei Monate nach Fristablauf, "
              "R. 136 Abs. 1 EPÜ), **Form** (Gebühr, Begründung, versäumte Handlung, R. 136 Abs. 2 EPÜ) und **alle gebotene Sorgfalt** "
              "(Art. 122 Abs. 1 EPÜ). Gutgläubige Benutzer im Zwischenzeitraum schützt Art. 122 Abs. 5 EPÜ.",
              concepts=["epc_wiedereinsetzung", "epc_weiterbehandlung"], norms=["Art. 122 EPÜ", "R. 136 EPÜ"],
              distinctions=["d_epc_weiterbehandlung_wiedereinsetzung"], abschnitt="Überblick"),
        *fallkette("e01n122-1", "Die übersehene Rechtsverlustmitteilung",
            "K hat auf einen Bescheid nach Art. 94 Abs. 3 EPÜ nicht geantwortet. Die Mitteilung über den Rechtsverlust nach R. 112 Abs. 1 EPÜ ist "
            "auf den 2.3.2026 datiert. Trotz aller gebotenen Sorgfalt erfährt K erst am 8.6.2026 von ihr.",
            [frage("Kann K Wiedereinsetzung in die Frist zur Erwiderung auf den Bescheid beantragen?", False,
                   ["**Nein!** Für diese Frist gibt es die Weiterbehandlung; solche Fristen sind von der Wiedereinsetzung ausgeschlossen "
                    "(R. 136 Abs. 3 EPÜ). Versäumt ist aber auch die Weiterbehandlungsfrist, die am 4.5.2026 ablief (der 2.5. war ein Samstag). In "
                    "**diese** Frist kann K Wiedereinsetzung beantragen (Richtlinien E-VIII, 3.1.1)."],
                   merke="Wiedereinsetzung in die Weiterbehandlungsfrist, nicht in die Ausgangsfrist.", titel="Welche Frist?", level=2,
                   norms=["R. 136 Abs. 3 EPÜ", "R. 135 Abs. 1 EPÜ"], step=_FV + ".4.1"),
             frage("Bis wann muss K den Antrag stellen?", 2,
                   ["**Bis 10.8.2026.** Die Frist beträgt zwei Monate nach Wegfall des Hindernisses, hier der Kenntnis am 8.6.2026 "
                    "(R. 136 Abs. 1 EPÜ). Der 8.8.2026 ist ein Samstag, daher Montag (R. 134 Abs. 1 EPÜ). Die Grenze von einem Jahr nach Ablauf der "
                    "versäumten Frist ist gewahrt."],
                   optionen=["4.5.2026", "8.8.2026", "10.8.2026", "4.5.2027"],
                   merke="Zwei Monate ab Wegfall des Hindernisses, höchstens ein Jahr.", titel="Antragsfrist", level=2,
                   norms=["R. 136 Abs. 1 EPÜ"], step=_FV + ".4.2"),
             frage("Genügt es, bis dahin den Antrag zu stellen und die Wiedereinsetzungsgebühr zu zahlen?", False,
                   ["**Nein!** Der Antrag ist zu begründen, die Tatsachen sind glaubhaft zu machen, und zwar sofort vollständig (R. 136 Abs. 2 EPÜ; "
                    "J 6/22). Nachzuholen ist die versäumte Handlung: der Weiterbehandlungsantrag mit Gebühr und Erwiderung auf den Bescheid "
                    "(R. 135 Abs. 1 EPÜ)."],
                   merke="Gebühr, Begründung und versäumte Handlung, alles in der Antragsfrist.", titel="Form", norms=["R. 136 Abs. 2 EPÜ"],
                   cases=["epc_j_6_22"], step=_FV + ".4.3"),
             frage("Eine Jahresgebühr wäre in der Zwischenzeit fällig geworden. Muss K sie schon mit dem Antrag zahlen?", False,
                   ["**Nein!** Eine Jahresgebühr, die zwischen Rechtsverlust und Zustellung der Entscheidung über die Wiedereinsetzung fällig geworden "
                    "wäre, wird erst mit dieser Zustellung fällig und kann binnen vier Monaten danach ohne Zuschlag gezahlt werden "
                    "(R. 51 Abs. 4 EPÜ)."],
                   merke="Jahresgebühren nach dem Rechtsverlust: fällig erst mit der Wiedereinsetzung.", titel="Jahresgebühren", level=3,
                   norms=["R. 51 Abs. 4 EPÜ"], concepts=["epc_jahresgebuehren"]),
            ],
            abschnitt="R. 136 Abs. 1 bis 3 EPÜ: Statthaftigkeit, Frist und Form", level=2, concepts=["epc_wiedereinsetzung"],
            norms=["Art. 122 Abs. 1 EPÜ", "R. 136 EPÜ"]),
        *fallkette("e01n122-2", "Die Assistentin und der Fristenkalender",
            "Die Prüfungsabteilung weist Ls Anmeldung mit Entscheidung vom 9.3.2026 zurück. Vertreterin M lässt Fristen von einer erfahrenen, "
            "sorgfältig ausgewählten und regelmäßig kontrollierten Assistentin eintragen. Diese vergisst ausnahmsweise die Beschwerdefrist; M "
            "bemerkt das am 15.6.2026.",
            [frage("Steht der Fehler der Assistentin der Wiedereinsetzung in die Beschwerdefrist entgegen?", False,
                   ["**Nein!** Routineaufgaben wie das Notieren von Fristen darf der Vertreter delegieren. Fehler der Hilfsperson werden ihm nicht "
                    "zugerechnet, wenn er sie sorgfältig ausgewählt, eingewiesen und überwacht hat (J 5/80; Richtlinien E-VIII, 3.2). Ein isoliertes "
                    "Versehen in einem sonst zuverlässigen System genügt."],
                   merke="Hilfspersonen: Auswahl, Einweisung, Überwachung.", titel="Fehler der Hilfsperson", cases=["epc_j_5_80"],
                   step=_FV + ".4.4"),
             frage("Genügt im Antrag der Satz, es liege ein isoliertes Versehen in einem gut funktionierenden System vor?", False,
                   ["**Nein!** Der Antrag muss die konkreten Tatsachen nennen: die Ursache, wann sie eintrat und wegfiel und wie das Fristensystem "
                    "arbeitet (R. 136 Abs. 2 EPÜ; Richtlinien E-VIII, 3.1.4). Nach Ablauf der Antragsfrist darf M nur noch erläutern, keine neuen "
                    "Tatsachen nachschieben (J 6/22)."],
                   merke="Allgemeine Formeln sind keine Begründung.", titel="Begründung", level=2, norms=["R. 136 Abs. 2 EPÜ"],
                   cases=["epc_j_6_22"], step=_FV + ".4.3"),
             frage("Kann M sich auf ein isoliertes Versehen in einem zuverlässigen System berufen?", False,
                   ["**Nein,** in der Regel nicht. Die Rechtsprechung zum isolierten Versehen hilft nicht über ein eigenes Versäumnis des Vertreters "
                    "hinweg, wenn keine besonderen Umstände vorliegen (T 1095/06). Vom Vertreter selbst wird die volle Sorgfalt verlangt."],
                   merke="Eigenes Versäumnis des Vertreters wiegt schwerer.", titel="Eigener Fehler des Vertreters", level=3,
                   abwandlung="M hatte die Frist selbst notiert, die fertige Beschwerdeschrift aber zu versenden vergessen.",
                   cases=["epc_t_1095_06"]),
            ],
            abschnitt="Art. 122 Abs. 1 EPÜ: alle gebotene Sorgfalt", level=2, concepts=["epc_wiedereinsetzung"], norms=["Art. 122 Abs. 1 EPÜ"]),
        *fallkette("e01n122-3", "Beide Seiten verpassen die Beschwerde",
            "Die Einspruchsabteilung hält Ns Patent in geänderter Fassung aufrecht. Inhaber N und Einsprechender O sind beide beschwert. Wegen "
            "isolierter Versehen legt keiner Beschwerde ein; beide bemerken das nach Ablauf der Beschwerdefrist.",
            [frage("Kann N Wiedereinsetzung in die Beschwerdefrist beantragen?", True,
                   ["**Ja!** Art. 122 Abs. 1 EPÜ steht dem Patentinhaber offen. Die Beschwerdefrist ist von der Weiterbehandlung ausgeschlossen "
                    "(Art. 121 Abs. 4 EPÜ), also ist die Wiedereinsetzung der richtige Behelf. Innerhalb der Antragsfrist legt N Beschwerde ein und "
                    "zahlt die Beschwerdegebühr (R. 136 Abs. 2 EPÜ)."],
                   merke="Beschwerdefrist: nur Wiedereinsetzung.", titel="Patentinhaber", norms=["Art. 121 Abs. 4 EPÜ"], step=_FV + ".4.1"),
             frage("Kann auch O Wiedereinsetzung in die Frist zur Einlegung der Beschwerde beantragen?", False,
                   ["**Nein!** Art. 122 Abs. 1 EPÜ nennt nur Anmelder und Patentinhaber. Ein Einsprechender, der keine Beschwerde eingelegt hat, kann "
                    "nicht in die Beschwerdefrist wiedereingesetzt werden (T 210/89; Richtlinien E-VIII, 3.1.2)."],
                   merke="Einsprechender: keine Wiedereinsetzung in die Beschwerdefrist.", titel="Einsprechender und Beschwerdefrist", level=2,
                   cases=["epc_t_210_89"], concepts=["epc_einspruch"]),
             frage("Kann O jetzt Wiedereinsetzung beantragen?", True,
                   ["**Ja!** Ein Einsprechender, der Beschwerde eingelegt hat, kann in die Frist für die Beschwerdebegründung wiedereingesetzt "
                    "werden (G 1/86). Ausgeschlossen bleibt nur die Frist zur Einlegung der Beschwerde (T 210/89; Richtlinien E-VIII, 3.1.2)."],
                   merke="Einsprechender: Wiedereinsetzung nur in die Begründungsfrist.", titel="Einsprechender und Begründungsfrist", level=2,
                   abwandlung="O hat rechtzeitig Beschwerde eingelegt, aber die Frist für die Begründung versäumt.",
                   cases=["epc_g_1_86"]),
            ],
            abschnitt="Art. 122 Abs. 1 EPÜ: wer Wiedereinsetzung beantragen kann", level=2, concepts=["epc_wiedereinsetzung", "epc_beschwerde"],
            norms=["Art. 122 Abs. 1 EPÜ", "Art. 108 EPÜ"]),
        *fallkette("e01n122-4", "Die vergessene Jahresgebühr und der Nachahmer",
            "Die Jahresgebühr für Ps veröffentlichte Anmeldung war am 31.3.2026 fällig. P zahlt sie versehentlich weder dann noch mit Zuschlag "
            "bis 30.9.2026. Q beginnt im November 2026 in Deutschland, einem benannten Staat, gutgläubig mit der Herstellung der Erfindung. "
            "Später wird P wiedereingesetzt.",
            [frage("Hätte P schon im April 2026 Wiedereinsetzung in die Frist des R. 51 Abs. 1 EPÜ beantragen können?", False,
                   ["**Nein!** Das Versäumen des Fälligkeitstags führt nicht unmittelbar zu einem Rechtsverlust, weil die Zahlung mit Zuschlag noch "
                    "möglich ist (R. 51 Abs. 2 EPÜ; Richtlinien E-VIII, 3.1.1). Wiedereinsetzung kommt erst für die Nachfrist in Betracht, die am "
                    "30.9.2026 ablief."],
                   merke="Kein unmittelbarer Rechtsverlust, keine Wiedereinsetzung.", titel="Unmittelbarer Rechtsverlust",
                   norms=["R. 51 Abs. 2 EPÜ"], concepts=["epc_jahresgebuehren"], step=_FV + ".4.1"),
             frage("Muss P mit dem Antrag die Jahresgebühr samt Zuschlagsgebühr zahlen?", True,
                   ["**Ja!** Die versäumte Handlung ist innerhalb der Antragsfrist nachzuholen (R. 136 Abs. 2 EPÜ); versäumt ist die Zahlung der "
                    "Jahresgebühr mit Zuschlag. Hinzu kommt die Gebühr für die Wiedereinsetzung (R. 136 Abs. 1 EPÜ)."],
                   merke="Versäumte Handlung: Jahresgebühr mit Zuschlag.", titel="Versäumte Handlung", step=_FV + ".4.3"),
             frage("Darf Q nach der Wiedereinsetzung weiter herstellen?", True,
                   ["**Ja!** Wer in einem benannten Staat zwischen dem Rechtsverlust und der Bekanntmachung des Hinweises auf die Wiedereinsetzung "
                    "die Erfindung gutgläubig in Benutzung genommen hat, darf sie in seinem Betrieb oder für dessen Bedürfnisse unentgeltlich weiter "
                    "benutzen (Art. 122 Abs. 5 EPÜ). Der Rechtsverlust trat mit Ablauf des 30.9.2026 ein."],
                   merke="Zwischenbenutzer behalten ein Weiterbenutzungsrecht.", titel="Weiterbenutzungsrecht", level=2,
                   norms=["Art. 122 Abs. 5 EPÜ"]),
            ],
            abschnitt="Art. 122 Abs. 5 EPÜ: Folgen der Wiedereinsetzung", level=2, concepts=["epc_wiedereinsetzung"], norms=["Art. 122 EPÜ"]),
        *fallkette("e01n122-5", "Krank in der Prioritätsfrist",
            "R, ein Einzelerfinder mit Wohnsitz in München, meldet am 15.4.2025 beim DPMA an. Ab 1.4.2026 ist er plötzlich schwer erkrankt und "
            "kann nicht handeln; einen Vertreter hat er nicht. Am 20.4.2026 reicht er die europäische Anmeldung mit der deutschen Priorität ein.",
            [frage("Bis wann muss R Wiedereinsetzung in die Prioritätsfrist beantragen?", 0,
                   ["**Bis 15.6.2026.** Bei der Prioritätsfrist läuft die Antragsfrist zwei Monate nach deren Ablauf (R. 136 Abs. 1 Satz 2 EPÜ), nicht "
                    "ab Wegfall des Hindernisses. Die Prioritätsfrist endete am 15.4.2026 (Art. 87 Abs. 1 EPÜ)."],
                   optionen=["15.6.2026", "20.6.2026", "22.6.2026", "15.4.2027"],
                   merke="Priorität: zwei Monate nach Ablauf der Prioritätsfrist.", titel="Antragsfrist bei der Priorität",
                   norms=["R. 136 Abs. 1 EPÜ", "Art. 87 Abs. 1 EPÜ"], step=_FV + ".4.2"),
             frage("Kann eine plötzliche schwere Erkrankung die Wiedereinsetzung tragen?", True,
                   ["**Ja,** als außergewöhnlicher Umstand (Richtlinien E-VIII, 3.2). R muss aber zeigen, dass er auch sonst alle gebotene Sorgfalt "
                    "beachtet hat, etwa dass er eine Vertretung nicht organisieren konnte. Maßstab ist die Sorgfalt nach den gegebenen Umständen "
                    "(Art. 122 Abs. 1 EPÜ)."],
                   merke="Außergewöhnliche Umstände: Krankheit ja, aber Vorsorge zeigen.", titel="Außergewöhnliche Umstände", level=2,
                   step=_FV + ".4.4"),
             frage("Wird die europäische Anmeldung unwirksam, wenn die Wiedereinsetzung scheitert?", False,
                   ["**Nein!** Sie behält ihren Anmeldetag 20.4.2026, nur ohne Priorität. Maßgeblicher Tag für den Stand der Technik ist dann der "
                    "Anmeldetag; alles, was vorher öffentlich zugänglich war, steht ihr entgegen (Art. 89 EPÜ, Art. 54 Abs. 2 EPÜ)."],
                   merke="Ohne Priorität zählt der Anmeldetag.", titel="Folge des Scheiterns", level=1,
                   norms=["Art. 89 EPÜ", "Art. 54 Abs. 2 EPÜ"], concepts=["epc_stand_der_technik"]),
            ],
            abschnitt="R. 136 Abs. 1 Satz 2 EPÜ: Prioritätsfrist", level=2, concepts=["epc_wiedereinsetzung", "epc_prioritaet"],
            norms=["Art. 122 Abs. 1 EPÜ"]),
    ]),
    # ================================================================== Art. 133, 134 EPÜ, R. 151, R. 152 EPÜ
    dict(id="e01n133", order=13300, titel="Art. 133, 134 EPÜ, R. 151, R. 152 EPÜ: Vertretung", einheiten=[
        intro("e01n133-0", "Wohnsitz entscheidet, nicht Staatsangehörigkeit",
              "Vertretungsfragen stecken in Paper D in Sachverhalten mit Beteiligten außerhalb Europas: 2017 (US-Erwerber des Patents im "
              "Einspruch), 2018 (argentinischer Erfinder reicht selbst ein) und 2024 (gemeinsamer Einspruch mit einem Einsprechenden in Mexiko). "
              "Niemand muss sich vertreten lassen (Art. 133 Abs. 1 EPÜ), außer wer **weder Wohnsitz noch Sitz** in einem Vertragsstaat hat "
              "(Art. 133 Abs. 2 EPÜ); die Staatsangehörigkeit zählt nicht. Die Anmeldung darf jeder selbst einreichen. Angestellte handeln für "
              "ihren Arbeitgeber (Art. 133 Abs. 3 EPÜ), Rechtsanwälte nach Art. 134 Abs. 8 EPÜ. Mehrere Beteiligte handeln durch einen "
              "gemeinsamen Vertreter (R. 151 EPÜ); fehlt eine verlangte Vollmacht, gelten Handlungen als nicht erfolgt (R. 152 Abs. 6 EPÜ).",
              concepts=["epc_vertretung"], norms=["Art. 133 EPÜ", "Art. 134 EPÜ", "R. 151 EPÜ", "R. 152 EPÜ"], abschnitt="Überblick"),
        *fallkette("e01n133-1", "Der Erfinder aus Brasilien",
            "S wohnt in Brasilien. Er reicht die europäische Anmeldung EP-S selbst online ein und zahlt Anmelde- und Recherchengebühr von seinem "
            "Konto. Das EPA fordert ihn auf, einen zugelassenen Vertreter zu bestellen.",
            [frage("War die Einreichung durch S selbst wirksam?", True,
                   ["**Ja!** Art. 133 Abs. 2 EPÜ nimmt die Einreichung der Anmeldung vom Vertretungszwang aus. Dazu gehören alle Handlungen, die zur "
                    "Zuerkennung des Anmeldetags führen (Richtlinien A-VIII, 1.1)."],
                   merke="Einreichen darf jeder selbst.", titel="Einreichung"),
             frage("Durfte S die Gebühren selbst zahlen?", True,
                   ["**Ja!** Gebühren kann jede Person wirksam zahlen (Richtlinien A-X, 1). Auf den Vertretungszwang kommt es dafür nicht an."],
                   merke="Zahlen darf jeder.", titel="Gebührenzahlung", concepts=["epc_gebuehrenzahlung"]),
             frage("Darf S selbst auf die Stellungnahme zur Recherche erwidern?", False,
                   ["**Nein!** Alle anderen Handlungen muss S durch einen zugelassenen Vertreter vornehmen (Art. 133 Abs. 2 EPÜ). Eine eigene Eingabe "
                    "behandelt das EPA wie ein nicht wirksam unterzeichnetes Schriftstück und fordert zur Unterschrift durch einen Berechtigten auf "
                    "(R. 50 Abs. 3 EPÜ; Richtlinien A-VIII, 3.1)."],
                   merke="Nach der Einreichung handelt nur noch der Vertreter.", titel="Weitere Handlungen", level=2, norms=["R. 50 Abs. 3 EPÜ"]),
             frage("Kann S Weiterbehandlung beantragen?", False,
                   ["**Nein!** Die Frist nach R. 58 EPÜ zur Bestellung eines Vertreters ist von der Weiterbehandlung ausgeschlossen "
                    "(R. 135 Abs. 2 EPÜ); die Anmeldung wird zurückgewiesen (Art. 90 Abs. 5 EPÜ; Richtlinien A-III, 16.2)."],
                   merke="Kein Vertreter bestellt: Zurückweisung ohne Weiterbehandlung.", titel="Kein Vertreter bestellt", level=2,
                   abwandlung="S bestellt innerhalb der gesetzten Frist keinen Vertreter.",
                   norms=["R. 58 EPÜ", "R. 135 Abs. 2 EPÜ", "Art. 90 Abs. 5 EPÜ"], concepts=["epc_weiterbehandlung"], step=_FV + ".3.1"),
            ],
            abschnitt="Art. 133 Abs. 2 EPÜ: Vertretungszwang", level=1, concepts=["epc_vertretung"], norms=["Art. 133 Abs. 2 EPÜ"]),
        *fallkette("e01n133-2", "Der gemeinsame Einspruch",
            "T, wohnhaft in Italien, und U, italienischer Staatsangehöriger mit Wohnsitz in Kanada, legen gemeinsam Einspruch ein; T ist zuerst "
            "genannt. Beide unterschreiben, eine Einspruchsgebühr wird gezahlt. Auf Aufforderung bestellt U die zugelassene Vertreterin V; T "
            "bestellt niemanden.",
            [frage("Genügt eine Einspruchsgebühr für beide?", True,
                   ["**Ja!** Ein von mehreren Personen gemeinsam eingelegter Einspruch ist mit nur einer Einspruchsgebühr zulässig (G 3/99)."],
                   merke="Gemeinsamer Einspruch: eine Gebühr.", titel="Eine Gebühr", cases=["epc_g_3_99"], step=_ES + ".2"),
             frage("Musste U einen Vertreter bestellen, obwohl er Italiener ist?", True,
                   ["**Ja!** Art. 133 Abs. 2 EPÜ knüpft an Wohnsitz oder Sitz an, nicht an die Staatsangehörigkeit. Die Vertreterin muss den Einspruch "
                    "zudem unterzeichnen oder genehmigen (Richtlinien D-IV, 1.2.2.2)."],
                   merke="Maßgeblich ist der Wohnsitz.", titel="Staatsangehörigkeit", norms=["Art. 133 Abs. 2 EPÜ"], step=_ES + ".2"),
             frage("Wer ist gemeinsamer Vertreter?", 1,
                   ["**V.** Grundsätzlich gilt der zuerst Genannte als gemeinsamer Vertreter. Ist aber ein Beteiligter vertretungspflichtig, gilt "
                    "sein zugelassener Vertreter als gemeinsamer Vertreter, sofern der zuerst Genannte keinen bestellt hat (R. 151 Abs. 1 EPÜ). Das "
                    "gilt auch für gemeinsam Einsprechende."],
                   optionen=["T als zuerst Genannter", "V, die Vertreterin von U", "T und V gemeinsam", "Ein vom EPA bestimmter Vertreter"],
                   merke="Pflichtvertreter verdrängt den zuerst Genannten ohne Vertreter.", titel="Gemeinsamer Vertreter", level=2,
                   norms=["R. 151 Abs. 1 EPÜ"]),
             frage("Kann T später allein Beschwerde gegen die Entscheidung einlegen?", False,
                   ["**Nein!** Bei gemeinsam Einsprechenden muss der gemeinsame Vertreter die Beschwerde einlegen. Legt ein Nichtberechtigter sie ein, "
                    "gilt sie als nicht ordnungsgemäß unterzeichnet, und der gemeinsame Vertreter wird zur Unterschrift aufgefordert (G 3/99)."],
                   merke="Gemeinsame Einsprechende handeln durch den gemeinsamen Vertreter.", titel="Beschwerde", level=3,
                   concepts=["epc_beschwerde"]),
            ],
            abschnitt="R. 151 EPÜ: gemeinsamer Vertreter", level=2, concepts=["epc_vertretung", "epc_einspruch"], norms=["R. 151 EPÜ"],
            cases=["epc_g_3_99"]),
        *fallkette("e01n133-3", "Der Patentingenieur",
            "Die W GmbH mit Sitz in Stuttgart lässt ihre Anmeldung von ihrem angestellten Patentingenieur X betreuen, der kein zugelassener "
            "Vertreter ist. X erwidert auf einen Bescheid, ohne eine Vollmacht einzureichen. Die Muttergesellschaft von W hat ihren Sitz in den USA.",
            [frage("Darf X für W handeln?", True,
                   ["**Ja!** Personen mit Sitz in einem Vertragsstaat können durch einen Angestellten handeln, der kein zugelassener Vertreter sein "
                    "muss (Art. 133 Abs. 3 EPÜ). Der Angestellte braucht aber stets eine unterzeichnete Vollmacht oder die Nummer einer registrierten "
                    "allgemeinen Vollmacht (Richtlinien A-VIII, 1.7)."],
                   merke="Angestellte: ohne Zulassung, aber immer mit Vollmacht.", titel="Angestellter", norms=["Art. 133 Abs. 3 EPÜ"]),
             frage("X reicht die Vollmacht auch innerhalb der vom EPA gesetzten Frist nicht ein. Bleibt die Erwiderung wirksam?", False,
                   ["**Nein!** Wird eine vorgeschriebene Vollmacht nicht rechtzeitig eingereicht, gelten die Handlungen des Vertreters außer der "
                    "Einreichung der Anmeldung als nicht erfolgt (R. 152 Abs. 6 EPÜ). Ist die Bescheidsfrist abgelaufen, gilt die Anmeldung als "
                    "zurückgenommen (Art. 94 Abs. 4 EPÜ)."],
                   merke="Keine Vollmacht: Handlungen gelten als nicht erfolgt.", titel="Fehlende Vollmacht", level=2,
                   norms=["R. 152 Abs. 2 EPÜ", "R. 152 Abs. 6 EPÜ", "Art. 94 Abs. 4 EPÜ"]),
             frage("Kann X auch Anmeldungen der US-Muttergesellschaft betreuen?", False,
                   ["**Nein!** Die Muttergesellschaft hat keinen Sitz in einem Vertragsstaat und muss durch einen zugelassenen Vertreter handeln "
                    "(Art. 133 Abs. 2 EPÜ). Ein Angestellter, der nicht in der Liste der zugelassenen Vertreter steht, genügt nicht "
                    "(Art. 134 Abs. 1 EPÜ)."],
                   merke="Vertretungspflichtige brauchen einen zugelassenen Vertreter.", titel="Muttergesellschaft", level=2,
                   norms=["Art. 133 Abs. 2 EPÜ", "Art. 134 Abs. 1 EPÜ"]),
            ],
            abschnitt="Art. 133 Abs. 3 EPÜ, R. 152 EPÜ: Angestellte und Vollmacht", level=1, concepts=["epc_vertretung"],
            norms=["R. 152 EPÜ"]),
        *fallkette("e01n133-4", "Der Inhaberwechsel vor der mündlichen Verhandlung",
            "Inhaberin des Patents ist die US-Firma Alpha, im Einspruchsverfahren vertreten durch die zugelassene Vertreterin Berg. Alpha "
            "überträgt das Patent auf die US-Firma Beta; Berg zeigt dem EPA das Ende ihrer Vollmacht an. Schriftsätze zur mündlichen Verhandlung "
            "können bis 7.10.2026 eingereicht werden.",
            [frage("Kann Beta die geänderten Ansprüche selbst einreichen?", False,
                   ["**Nein!** Beta hat keinen Sitz in einem Vertragsstaat und muss durch einen zugelassenen Vertreter handeln (Art. 133 Abs. 2 EPÜ). "
                    "Zudem wird der Rechtsübergang dem EPA gegenüber erst wirksam, wenn er mit Dokumenten nachgewiesen ist (R. 22 Abs. 3 EPÜ, "
                    "R. 85 EPÜ)."],
                   merke="Neuer Inhaber außerhalb Europas: Vertreter bestellen, Übergang nachweisen.", titel="Neuer Inhaber",
                   norms=["Art. 133 Abs. 2 EPÜ", "R. 22 Abs. 3 EPÜ", "R. 85 EPÜ"]),
             frage("Darf Beta statt eines zugelassenen Vertreters einen in Deutschland zugelassenen Rechtsanwalt beauftragen?", True,
                   ["**Ja!** Ein Rechtsanwalt, der in einem Vertragsstaat zugelassen ist und dort seinen Geschäftssitz hat, kann wie ein zugelassener "
                    "Vertreter vertreten, soweit er in diesem Staat in Patentsachen vertreten darf (Art. 134 Abs. 8 EPÜ). In der Liste der "
                    "zugelassenen Vertreter steht er nicht (Richtlinien A-VIII, 1.3)."],
                   merke="Rechtsanwälte vertreten im Umfang ihrer nationalen Befugnis.", titel="Rechtsanwalt", level=2,
                   norms=["Art. 134 Abs. 8 EPÜ"]),
             frage("Muss die neu bestellte zugelassene Vertreterin Clausen eine unterzeichnete Vollmacht einreichen?", False,
                   ["**Nein,** in der Regel nicht. Zugelassene Vertreter müssen eine Vollmacht nur in besonderen Fällen einreichen, etwa bei einem "
                    "Vertreterwechsel, ohne dass der bisherige Vertreter das Erlöschen angezeigt hat (R. 152 Abs. 1 EPÜ; Richtlinien A-VIII, 1.7). "
                    "Berg hat das Erlöschen angezeigt."],
                   merke="Zugelassene Vertreter: Vollmacht nur ausnahmsweise.", titel="Vollmacht des neuen Vertreters", level=2,
                   norms=["R. 152 Abs. 1 EPÜ"]),
             frage("Muss Clausen jetzt eine Vollmacht einreichen?", True,
                   ["**Ja!** Beim Vertreterwechsel ohne Anzeige des Erlöschens durch den bisherigen Vertreter verlangt das EPA eine unterzeichnete "
                    "Vollmacht (Richtlinien A-VIII, 1.7). Bis zur Anzeige gilt der bisherige Vertreter als bevollmächtigt (R. 152 Abs. 8 EPÜ)."],
                   merke="Ohne Anzeige des Erlöschens gilt der alte Vertreter fort.", titel="Wechsel ohne Anzeige", level=3,
                   abwandlung="Berg hatte das Ende ihrer Vollmacht nicht angezeigt.", norms=["R. 152 Abs. 8 EPÜ"]),
            ],
            abschnitt="Art. 134 EPÜ, R. 152 EPÜ: Vertreterwechsel", level=2, concepts=["epc_vertretung"], norms=["Art. 134 EPÜ"]),
    ]),
]
