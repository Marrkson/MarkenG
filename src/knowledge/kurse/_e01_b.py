# -*- coding: utf-8 -*-
"""Kapitel des Normkurses e01 (siehe e01_epue_paper_d.py): Art. 86 EPÜ mit R. 51 EPÜ (Jahresgebühren), Art. 87 bis 89 EPÜ mit R. 52,
R. 53 EPÜ (Priorität), Art. 114, 115 EPÜ (Ermittlung von Amts wegen, Einwendungen Dritter), Art. 123 EPÜ mit R. 137 EPÜ (Änderungen)
und R. 139, R. 140 EPÜ (Berichtigung von Fehlern). `order` = Artikel × 100; R. 139 EPÜ steht hinter Art. 123 EPÜ."""
from ._helpers import intro, schema, frage, fallkette  # noqa: F401

_FV = "step:epc_schema_fristversaeumnis"
_SDT = "step:epc_schema_stand_der_technik"
_TA = "step:epc_schema_teilanmeldung"
_EINS = "step:epc_schema_einspruch"
_BESCHW = "step:epc_schema_beschwerde"

KAPITEL = [
    # ================================================================== Art. 86 EPÜ, R. 51 EPÜ
    dict(id="e01n86", order=8600, titel="Art. 86 EPÜ, R. 51 EPÜ: Jahresgebühren", einheiten=[
        intro("e01n86-0", "Fälligkeit, Nachfrist, Rechtsverlust",
              "Jahresgebühren tauchen in Paper D fast immer als Nebenfrage auf: 2022 nach einer Wiedereinsetzung (Frage 1) und kurz vor der "
              "Erteilung (Frage 2), 2025 beim automatischen Abbuchungsauftrag (Frage 4). Das Gerüst: Gebühren ab dem **dritten Jahr**, fällig am "
              "**letzten Tag des Monats**, in dem sich der Anmeldetag jährt (R. 51 Abs. 1 EPÜ); Nachfrist von sechs Monaten mit Zuschlag "
              "(R. 51 Abs. 2 EPÜ), erst danach gilt die Anmeldung als zurückgenommen (Art. 86 Abs. 1 EPÜ). Keine Weiterbehandlung, nur "
              "Wiedereinsetzung. Sonderregeln gelten für Teilanmeldungen (R. 51 Abs. 3 EPÜ) und nach Wiedereinsetzung (R. 51 Abs. 4 EPÜ); "
              "nach der Erteilung kassieren die Staaten (Art. 141 EPÜ), beim Einheitspatent das EPA.",
              concepts=["epc_jahresgebuehren", "epc_gebuehrenzahlung", "epc_rechtsverlust"],
              norms=["Art. 86 EPÜ", "R. 51 EPÜ", "Art. 141 EPÜ"], cases=["epc_j_4_91"], abschnitt="Überblick"),
        *fallkette("e01n86-1", "Zu früh gezahlt",
            "A reicht am 14.3.2024 eine europäische Patentanmeldung ein. Ihre Buchhaltung will alle Jahresgebühren möglichst früh zahlen und "
            "überweist die Jahresgebühr für das dritte Jahr am 15.9.2025.",
            [frage("Wann ist die Jahresgebühr für das dritte Jahr fällig?", 1,
                   ["**Am 31.3.2026.** Jahresgebühren sind für das kommende Jahr am letzten Tag des Monats fällig, in den der Jahrestag des Anmeldetags fällt "
                    "(R. 51 Abs. 1 Satz 1 EPÜ). Das dritte Jahr beginnt am 14.3.2026; die Gebühr wird zum Monatsende fällig (Art. 86 Abs. 1 EPÜ)."],
                   optionen=["14.3.2026", "31.3.2026", "14.3.2027", "31.3.2027"], merke="Fällig am Monatsletzten des Jahrestags.",
                   titel="Fälligkeit", norms=["R. 51 Abs. 1 EPÜ", "Art. 86 Abs. 1 EPÜ"]),
             frage("Ist die Zahlung vom 15.9.2025 wirksam?", False,
                   ["**Nein!** Die Gebühr für das dritte Jahr kann frühestens sechs Monate vor Fälligkeit wirksam gezahlt werden (R. 51 Abs. 1 Satz 2 EPÜ), "
                    "also ab 30.9.2025. Eine frühere Zahlung ist unwirksam; das EPA erstattet sie (Richtlinien A-X, 5.2.4)."],
                   merke="Drittes Jahr: höchstens sechs Monate im Voraus.", titel="Frühester Zahltag", level=2),
             frage("Kann A die Jahresgebühr für das vierte Jahr schon im Oktober 2026 zahlen?", False,
                   ["**Nein!** Alle Jahresgebühren außer der dritten können frühestens drei Monate vor Fälligkeit wirksam gezahlt werden "
                    "(R. 51 Abs. 1 Satz 3 EPÜ). Die vierte Gebühr ist am 31.3.2027 fällig."],
                   merke="Ab dem vierten Jahr: höchstens drei Monate im Voraus.", titel="Spätere Jahresgebühren"),
            ],
            abschnitt="R. 51 Abs. 1 EPÜ: Fälligkeit und Vorauszahlung", level=1, concepts=["epc_jahresgebuehren", "epc_gebuehrenzahlung"],
            norms=["R. 51 Abs. 1 EPÜ"]),
        *fallkette("e01n86-2", "Die Nachfrist",
            "B reicht am 12.9.2023 eine europäische Patentanmeldung ein. Die Jahresgebühr für das dritte Jahr wird am 30.9.2025 fällig; B zahlt "
            "sie nicht.",
            [frage("Bis wann kann B die Gebühr noch mit Zuschlagsgebühr zahlen?", 2,
                   ["**Bis 31.3.2026.** Die Nachfrist beträgt sechs Monate nach Fälligkeit (R. 51 Abs. 2 Satz 1 EPÜ). Sie läuft von Ultimo zu Ultimo, "
                    "endet also am letzten Tag des sechsten Monats (J 4/91; Richtlinien A-X, 5.2.4)."],
                   optionen=["30.12.2025", "30.3.2026", "31.3.2026", "30.9.2026"], merke="Nachfrist: vom Monatsletzten zum Monatsletzten.",
                   titel="Ende der Nachfrist", cases=["epc_j_4_91"], concepts=["epc_fristen"], level=2),
             frage("Gilt die Anmeldung schon am 1.10.2025 als zurückgenommen?", False,
                   ["**Nein!** Die Rücknahmefiktion des Art. 86 Abs. 1 EPÜ tritt erst mit Ablauf der Sechsmonatsfrist ein (R. 51 Abs. 2 Satz 2 EPÜ)."],
                   merke="Rechtsverlust erst mit Ablauf der Nachfrist.", titel="Zeitpunkt des Rechtsverlusts", concepts=["epc_rechtsverlust"],
                   step=_FV + ".2"),
             frage("Kann B am 16.3.2026 noch eine Teilanmeldung einreichen?", True,
                   ["**Ja!** Bis zum Ablauf der Nachfrist ist die Anmeldung anhängig; zu jeder anhängigen früheren Anmeldung kann eine Teilanmeldung "
                    "eingereicht werden (R. 36 Abs. 1 EPÜ)."],
                   merke="Während der Nachfrist ist die Anmeldung noch anhängig.", titel="Teilanmeldung in der Nachfrist",
                   norms=["R. 36 Abs. 1 EPÜ"], concepts=["epc_anhaengigkeit", "epc_teilanmeldung"], step=_TA + ".1"),
             frage("B zahlt auch bis 31.3.2026 nicht. Bleibt ihm nur die Wiedereinsetzung?", True,
                   ["**Ja!** Die Weiterbehandlung ist für R. 51 Abs. 2 EPÜ ausgeschlossen (R. 135 Abs. 2 EPÜ). Wiedereinsetzung setzt alle gebotene "
                    "Sorgfalt voraus (Art. 122 Abs. 1 EPÜ). Der Antrag ist spätestens ein Jahr nach Ablauf der "
                    "Nachfrist zu stellen (R. 136 Abs. 1 EPÜ)."],
                   merke="Jahresgebühr verpasst: nur Wiedereinsetzung.", titel="Rechtsbehelf", norms=["R. 135 Abs. 2 EPÜ", "Art. 122 Abs. 1 EPÜ"],
                   concepts=["epc_wiedereinsetzung"], step=_FV + ".4.1", level=2),
            ],
            abschnitt="R. 51 Abs. 2 EPÜ: Nachfrist und Rechtsverlust", level=1, concepts=["epc_jahresgebuehren"],
            norms=["R. 51 Abs. 2 EPÜ", "Art. 86 Abs. 1 EPÜ"]),
        *fallkette("e01n86-3", "Die späte Teilanmeldung",
            "Die Stammanmeldung von C wurde am 15.4.2021 eingereicht; alle Jahresgebühren sind bezahlt. Am 3.3.2026 reicht C eine Teilanmeldung ein.",
            [frage("Welche Jahresgebühren werden für die Teilanmeldung mit ihrer Einreichung fällig?", 2,
                   ["**Die für das dritte bis fünfte Jahr.** Gebühren, die für die Stammanmeldung bis zur Einreichung fällig geworden sind, sind auch für "
                    "die Teilanmeldung zu zahlen und werden mit deren Einreichung fällig (R. 51 Abs. 3 Satz 1 EPÜ). Die Jahre zählen ab dem Anmeldetag "
                    "der Stammanmeldung (Art. 76 Abs. 1 EPÜ)."],
                   optionen=["Keine, die Teilanmeldung beginnt mit dem ersten Jahr", "Nur die für das fünfte Jahr",
                             "Die für das dritte bis fünfte Jahr", "Die für das dritte bis sechste Jahr"],
                   merke="Die Teilanmeldung erbt das Alter der Stammanmeldung.", titel="Nachzuzahlende Gebühren",
                   norms=["R. 51 Abs. 3 EPÜ", "Art. 76 Abs. 1 EPÜ"], step=_TA + ".4"),
             frage("Kann C die am 30.4.2026 fällige Gebühr für das sechste Jahr noch am 3.7.2026 ohne Zuschlag zahlen?", True,
                   ["**Ja!** Eine Jahresgebühr, die bis zum Ablauf von vier Monaten nach Einreichung der Teilanmeldung fällig wird, kann wie die "
                    "nachzuzahlenden Gebühren innerhalb dieser Frist ohne Zuschlag gezahlt werden (R. 51 Abs. 3 Satz 2 EPÜ). Die Frist endet am 3.7.2026."],
                   merke="Vier Monate ohne Zuschlag – auch für die neu fällig werdende Gebühr.", titel="Viermonatsfrist", level=2),
             frage("Bis wann kann C die Gebühr für das fünfte Jahr mit Zuschlag zahlen, wenn er die vier Monate verpasst?", 1,
                   ["**Bis 3.9.2026.** R. 51 Abs. 2 EPÜ ist anzuwenden (R. 51 Abs. 3 Satz 3 EPÜ): sechs Monate nach Fälligkeit, und fällig wurde die "
                    "Gebühr am Tag der Einreichung (Richtlinien A-IV, 1.4.3)."],
                   optionen=["3.7.2026", "3.9.2026", "30.9.2026", "31.10.2026"], merke="Nachfrist ab Einreichung der Teilanmeldung.",
                   titel="Nachfrist bei Teilanmeldung", level=3),
            ],
            abschnitt="R. 51 Abs. 3 EPÜ: Teilanmeldung", level=2, concepts=["epc_jahresgebuehren", "epc_teilanmeldung"], norms=["R. 51 Abs. 3 EPÜ"]),
        *fallkette("e01n86-4", "Jahresgebühren nach der Wiedereinsetzung",
            "Die Anmeldung von D (Anmeldetag 18.3.2021) gilt als zurückgenommen, weil die Frist für die Erwiderung auf einen Bescheid am 15.1.2026 "
            "ablief. D erhält Wiedereinsetzung in die Frist für die Weiterbehandlung; die Entscheidung wird am 9.10.2026 zugestellt. Die Gebühr für "
            "das sechste Jahr ist unbezahlt.",
            [frage("Musste D die am 31.3.2026 fällige Gebühr bis 30.9.2026 mit Zuschlag zahlen, um die Anmeldung zu retten?", False,
                   ["**Nein!** Eine Jahresgebühr, die zwischen dem Eintritt des Rechtsverlusts (15.1.2026) und der Zustellung der Entscheidung über die "
                    "Wiedereinsetzung fällig geworden wäre, wird erst am Tag der Zustellung fällig (R. 51 Abs. 4 lit. a EPÜ)."],
                   merke="Während des Rechtsverlusts wird keine Jahresgebühr fällig.", titel="Verschobene Fälligkeit", concepts=["epc_wiedereinsetzung"]),
             frage("Bis wann kann D die Gebühr ohne Zuschlag zahlen?", 0,
                   ["**Bis 9.2.2027.** Die verschobene Gebühr kann innerhalb von vier Monaten nach Zustellung der Entscheidung ohne Zuschlag gezahlt "
                    "werden (R. 51 Abs. 4 lit. a EPÜ); danach gilt die Nachfrist von sechs Monaten mit Zuschlag (R. 51 Abs. 2 EPÜ)."],
                   optionen=["9.2.2027", "9.4.2027", "31.3.2027", "30.9.2026"], merke="Nach Wiedereinsetzung: vier Monate ohne Zuschlag.",
                   titel="Zahlungsfrist", level=2),
             frage("Kann D eine schon am 31.10.2025 fällige, noch unbezahlte Gebühr nach dem 30.4.2026 wirksam zahlen?", True,
                   ["**Ja!** War die Gebühr beim Rechtsverlust schon fällig, die Nachfrist aber noch offen, kann sie binnen sechs Monaten nach Zustellung "
                    "der Entscheidung über die Wiedereinsetzung gezahlt werden, zusammen mit der Zuschlagsgebühr (R. 51 Abs. 4 lit. b EPÜ)."],
                   merke="Laufende Nachfrist: sechs Monate nach Zustellung, mit Zuschlag.", titel="Laufende Nachfrist", level=3,
                   abwandlung="Der Anmeldetag war der 20.10.2020; die Gebühr für das sechste Jahr war am 31.10.2025 fällig."),
            ],
            abschnitt="R. 51 Abs. 4 EPÜ: nach Wiedereinsetzung", level=2, concepts=["epc_jahresgebuehren", "epc_wiedereinsetzung"],
            norms=["R. 51 Abs. 4 EPÜ"]),
        *fallkette("e01n86-5", "Nach der Erteilung",
            "Die Anmeldung von E wurde am 12.5.2021 eingereicht. Der Hinweis auf die Erteilung wird am 6.5.2026 im Europäischen Patentblatt "
            "bekannt gemacht. Die Gebühr für das sechste Jahr wäre am 31.5.2026 fällig.",
            [frage("Muss E die Gebühr für das sechste Jahr an das EPA zahlen?", False,
                   ["**Nein!** Die Zahlungspflicht gegenüber dem EPA endet mit der Gebühr für das Jahr, in dem der Hinweis auf die Erteilung bekannt "
                    "gemacht wird (Art. 86 Abs. 2 EPÜ). Das fünfte Jahr läuft bis 11.5.2026; ab dem sechsten Jahr erheben die Vertragsstaaten die "
                    "Gebühren (Art. 141 Abs. 1 EPÜ)."],
                   merke="Maßgeblich ist das Patentjahr der Erteilungsbekanntmachung.", titel="Letzte Gebühr an das EPA",
                   norms=["Art. 86 Abs. 2 EPÜ", "Art. 141 Abs. 1 EPÜ"], concepts=["epc_validierung"]),
             frage("Kann E die nationale Gebühr für das sechste Jahr noch am 3.7.2026 ohne Zuschlag zahlen?", True,
                   ["**Ja!** Wird eine Jahresgebühr innerhalb von zwei Monaten nach der Bekanntmachung des Hinweises auf die Erteilung fällig, gilt sie "
                    "als wirksam gezahlt, wenn sie innerhalb dieser Frist gezahlt wird; ein nationaler Zuschlag wird nicht erhoben (Art. 141 Abs. 2 EPÜ). "
                    "Die Frist endet am 6.7.2026."],
                   merke="Zwei Monate Schonfrist nach der Erteilung.", titel="Schonfrist", norms=["Art. 141 Abs. 2 EPÜ"], level=2),
             frage("An wen zahlt E die Jahresgebühren, wenn E für das Patent einheitliche Wirkung erhält?", 1,
                   ["**An das EPA.** Für Patente mit einheitlicher Wirkung sind Jahresgebühren und Zuschlagsgebühren an die Europäische "
                    "Patentorganisation, also an das EPA, zu zahlen (Art. 11 Abs. 1 EPatVO, R. 13 Abs. 1 DOEPS)."],
                   optionen=["An jedes teilnehmende nationale Amt", "An das EPA", "An das Einheitliche Patentgericht"],
                   merke="Einheitspatent: eine Jahresgebühr an das EPA.", titel="Einheitspatent",
                   norms=["Art. 11 Abs. 1 EPatVO", "R. 13 Abs. 1 DOEPS"]),
            ],
            abschnitt="Art. 86 Abs. 2 EPÜ: nach der Erteilung", level=2, concepts=["epc_jahresgebuehren"], norms=["Art. 86 Abs. 2 EPÜ"]),
    ]),
    # ================================================================== Art. 87 bis 89 EPÜ, R. 52, R. 53 EPÜ
    dict(id="e01n87", order=8700, titel="Art. 87 bis 89 EPÜ, R. 52, R. 53 EPÜ: Priorität", einheiten=[
        intro("e01n87-0", "Ohne wirksame Priorität kein Prioritätstag",
              "Kaum ein Paper D kommt ohne Priorität aus: Sie bestimmt, welches Dokument Stand der Technik ist (Art. 89 EPÜ). Geprüft werden "
              "**erste Anmeldung** (2019 Frage 4, Art. 87 Abs. 4 EPÜ), **dieselbe Erfindung** (2017 Frage 4, G 2/98), **Teilpriorität** "
              "(2021 Frage 4, 2022 Frage 5, G 1/15), die Wirksamkeit des Prioritätsdokuments (2022 Frage 4), Erklärung, Abschrift und Übersetzung "
              "(R. 52, R. 53 EPÜ; 2015 Frage 2, 2025 Frage 2) und die Rücknahme einer Priorität, um Fristen hinauszuschieben (2025 Frage 1). Die "
              "Prioritätsfrist selbst ist nur über die Wiedereinsetzung zu retten; die Berechtigung wird nach G 1/22 vermutet.",
              concepts=["epc_prioritaet", "epc_teilprioritaet", "epc_stand_der_technik"],
              norms=["Art. 87 EPÜ", "Art. 88 EPÜ", "Art. 89 EPÜ", "R. 52 EPÜ", "R. 53 EPÜ"], cases=["epc_g_2_98", "epc_g_1_15", "epc_g_1_22"],
              abschnitt="Überblick"),
        *fallkette("e01n87-1", "Die zweite Anmeldung in Korea",
            "E reicht am 5.2.2024 eine kanadische Anmeldung CA für die Vorrichtung V ein; sie wird am 6.8.2025 veröffentlicht. Am 4.11.2024 "
            "meldet E die Vorrichtung V in Korea an (KR). Am 3.11.2025 reicht E eine europäische Anmeldung für V ein und beansprucht die "
            "Priorität von KR.",
            [frage("Ist KR eine erste Anmeldung im Sinne des Art. 87 Abs. 1 EPÜ?", False,
                   ["**Nein!** E hatte V schon mit CA angemeldet. Art. 87 Abs. 4 EPÜ hilft nicht: CA wurde in einem anderen Staat eingereicht, nicht "
                    "zurückgenommen und später veröffentlicht. Die Priorität ist unwirksam, auch ohne Prüfung des Inhalts von KR (Richtlinien F-VI, 1.4)."],
                   merke="Priorität nur aus der ersten Anmeldung desselben Anmelders.", titel="Erste Anmeldung", step=_SDT + ".1.1"),
             frage("Ist CA Stand der Technik für die europäische Anmeldung?", True,
                   ["**Ja,** nach Art. 54 Abs. 2 EPÜ: Ohne wirksame Priorität ist der Anmeldetag 3.11.2025 maßgeblich (Art. 89 EPÜ greift nicht), "
                    "und CA war seit 6.8.2025 öffentlich zugänglich. Der Anspruch auf V ist nicht neu."],
                   merke="Unwirksame Priorität: die eigene Voranmeldung wird zum Stand der Technik.", titel="Folge für die Neuheit",
                   norms=["Art. 54 Abs. 2 EPÜ"], concepts=["epc_stand_der_technik"], step=_SDT + ".2.1"),
             frage("Ist KR dann eine erste Anmeldung?", True,
                   ["**Ja!** Eine jüngere Anmeldung in demselben Staat gilt als erste Anmeldung, wenn die ältere bis zu ihrer Einreichung ohne "
                    "Veröffentlichung, ohne verbleibende Rechte und ohne Prioritätsbeanspruchung zurückgenommen wurde (Art. 87 Abs. 4 EPÜ)."],
                   merke="Art. 87 Abs. 4 EPÜ: gleicher Staat, spurlos zurückgenommen.", titel="Abwandlung: zurückgenommene Voranmeldung", level=2,
                   abwandlung="Statt CA hatte E am 5.2.2024 in Korea KR0 eingereicht und vor Einreichung von KR unveröffentlicht, ohne verbleibende "
                              "Rechte und ohne Prioritätsbeanspruchung zurückgenommen."),
            ],
            abschnitt="Art. 87 Abs. 1, 4 EPÜ: erste Anmeldung", level=1, concepts=["epc_prioritaet"], norms=["Art. 87 Abs. 1 EPÜ", "Art. 87 Abs. 4 EPÜ"]),
        *fallkette("e01n87-2", "Stahl oder Metall",
            "F reicht am 8.4.2025 eine US-Anmeldung ein, die eine Schraube aus Stahl offenbart. Am 10.10.2025 erscheint ein Fachaufsatz über eine "
            "Schraube aus Aluminium. Am 7.4.2026 reicht F eine europäische Anmeldung mit Prioritätsanspruch ein; Anspruch 1 lautet "
            "„Schraube aus Metall“.",
            [frage("Genießt Anspruch 1 insgesamt die Priorität vom 8.4.2025?", False,
                   ["**Nein!** Dieselbe Erfindung liegt nur vor, soweit der Fachmann den Gegenstand des Anspruchs unmittelbar und eindeutig der "
                    "früheren Anmeldung als Ganzes entnimmt (G 2/98). Die US-Anmeldung offenbart nur Stahl, nicht Metall allgemein."],
                   merke="Priorität nur für das, was das Prioritätsdokument unmittelbar und eindeutig offenbart.", titel="Dieselbe Erfindung",
                   cases=["epc_g_2_98"]),
             frage("Kann Anspruch 1 teilweise die Priorität genießen?", True,
                   ["**Ja!** Ein generischer „Oder“-Anspruch hat Teilpriorität für die Alternative, die im Prioritätsdokument erstmals, unmittelbar oder "
                    "implizit, eindeutig und ausführbar offenbart ist (G 1/15; Art. 88 Abs. 3 EPÜ). Für Stahl gilt der 8.4.2025, für alle anderen "
                    "Metalle der 7.4.2026."],
                   merke="Gedanklich aufspalten: Stahl mit Priorität, Rest ohne.", titel="Teilpriorität", norms=["Art. 88 Abs. 3 EPÜ"],
                   cases=["epc_g_1_15"], concepts=["epc_teilprioritaet"], step=_SDT + ".1.2", level=2),
             frage("Nimmt der Fachaufsatz Anspruch 1 die Neuheit?", True,
                   ["**Ja!** Für den Teil ohne Priorität ist der Aufsatz Stand der Technik nach Art. 54 Abs. 2 EPÜ, und Aluminium fällt in diesen Teil. "
                    "F muss den Anspruch auf Stahl oder auf andere nicht vorweggenommene Metalle beschränken."],
                   merke="Der Zwischenstand trifft den Teil ohne Priorität.", titel="Zwischenveröffentlichung", norms=["Art. 54 Abs. 2 EPÜ"], level=2),
             frage("Nimmt der Fachaufsatz Anspruch 1 dann die Neuheit?", False,
                   ["**Nein!** Für den Stahl-Teil gilt der Prioritätstag, der Aufsatz ist dafür kein Stand der Technik (Art. 89 EPÜ). Den Teil ohne "
                    "Priorität (andere Metalle) nimmt eine Stahlschraube nicht vorweg (G 1/15; Richtlinien F-VI, 1.5)."],
                   merke="Teilpriorität schützt gerade das, was im Intervall veröffentlicht wurde.", titel="Abwandlung: Stahl im Aufsatz", level=3,
                   abwandlung="Der Fachaufsatz vom 10.10.2025 beschreibt eine Schraube aus Stahl."),
            ],
            abschnitt="Art. 87 Abs. 1, Art. 88 Abs. 3 EPÜ: dieselbe Erfindung", level=2, concepts=["epc_prioritaet", "epc_teilprioritaet"],
            norms=["Art. 87 Abs. 1 EPÜ", "Art. 89 EPÜ"]),
        *fallkette("e01n87-3", "Die japanische Priorität",
            "G reicht am 2.3.2026 eine europäische Anmeldung ein und beansprucht die Priorität einer japanischen Anmeldung JP vom 3.3.2025. Im "
            "Antrag steht versehentlich der 20.2.2025; das EPA weist darauf hin, die Priorität liege außerhalb der Zwölfmonatsfrist.",
            [frage("Bis wann kann G das Datum berichtigen?", 1,
                   ["**Bis 2.7.2026.** Maßgeblich ist die früher ablaufende der Fristen von 16 Monaten ab dem alten (20.6.2026) und dem berichtigten "
                    "Prioritätstag (3.7.2026), mindestens aber vier Monate nach dem Anmeldetag (R. 52 Abs. 3 EPÜ; Richtlinien A-III, 6.5.2)."],
                   optionen=["22.6.2026", "2.7.2026", "3.7.2026", "2.3.2027"], merke="Berichtigung: mindestens vier Monate ab Anmeldetag.",
                   titel="Berichtigung der Prioritätserklärung", norms=["R. 52 Abs. 3 EPÜ"], level=3),
             frage("Muss G innerhalb von 16 Monaten unaufgefordert eine Übersetzung von JP einreichen?", False,
                   ["**Nein!** Innerhalb von 16 Monaten ist nur die Abschrift einzureichen, soweit sie dem EPA nicht ohnehin zugänglich ist (R. 53 Abs. 1, 2 EPÜ). "
                    "Eine Übersetzung verlangt das EPA nur, wenn die Wirksamkeit der Priorität für die Patentierbarkeit relevant ist (R. 53 Abs. 3 EPÜ)."],
                   merke="Übersetzung des Prioritätsdokuments nur auf Aufforderung.", titel="Übersetzung", norms=["R. 53 Abs. 1 EPÜ", "R. 53 Abs. 3 EPÜ"]),
             frage("G lässt die Frist für die angeforderte Übersetzung in der Prüfung verstreichen. Ist die Priorität endgültig verloren?", False,
                   ["**Nein!** Der Prioritätsanspruch erlischt zwar (R. 53 Abs. 3 Satz 4 EPÜ). Im Prüfungsverfahren ist aber Weiterbehandlung möglich, "
                    "R. 53 EPÜ steht nicht in R. 135 Abs. 2 EPÜ. Im Einspruchsverfahren bleibt dem Inhaber nur die Wiedereinsetzung (Richtlinien A-III, 6.8.3)."],
                   merke="Versäumte Übersetzung: Weiterbehandlung in der Prüfung.", titel="Versäumte Übersetzung", norms=["R. 135 Abs. 2 EPÜ"],
                   concepts=["epc_weiterbehandlung"], level=2),
             frage("Kann G die Priorität noch retten?", True,
                   ["**Ja,** durch Wiedereinsetzung in die Prioritätsfrist: Antrag binnen zwei Monaten nach deren Ablauf, also bis 20.4.2026 (R. 136 Abs. 1 "
                    "Satz 2 EPÜ); die europäische Anmeldung liegt in diesem Zeitraum. G muss alle gebotene Sorgfalt darlegen (Art. 122 Abs. 1 EPÜ; "
                    "Richtlinien A-III, 6.6)."],
                   merke="Prioritätsfrist: Wiedereinsetzung binnen zwei Monaten, Nachanmeldung im selben Zeitraum.", titel="Abwandlung: Frist verpasst",
                   norms=["Art. 122 Abs. 1 EPÜ", "R. 136 Abs. 1 EPÜ"], concepts=["epc_wiedereinsetzung"], step=_FV + ".4.2", level=2,
                   abwandlung="JP wurde tatsächlich am 20.2.2025 eingereicht; G hat die Prioritätsfrist durch ein isoliertes Versehen versäumt."),
            ],
            abschnitt="R. 52, R. 53 EPÜ: Erklärung, Abschrift, Übersetzung", level=2, concepts=["epc_prioritaet"],
            norms=["Art. 88 Abs. 1 EPÜ", "R. 52 EPÜ", "R. 53 EPÜ"]),
        *fallkette("e01n87-4", "Zwei Prioritäten",
            "H reicht am 8.6.2026 eine europäische Anmeldung ein und beansprucht zwei Prioritäten: P1 vom 10.6.2025 offenbart das Merkmal A, P2 vom "
            "9.9.2025 das Merkmal B. Anspruch 1 lautet „A oder B“, Anspruch 2 „A und B in Kombination“.",
            [frage("Kann Anspruch 1 beide Prioritäten genießen?", True,
                   ["**Ja!** Für einen Patentanspruch können mehrere Prioritäten in Anspruch genommen werden (Art. 88 Abs. 2 Satz 2 EPÜ). Die "
                    "Alternative A erhält den 10.6.2025, die Alternative B den 9.9.2025 (Richtlinien F-VI, 1.5)."],
                   merke="Alternativen in einem Anspruch können verschiedene Prioritätstage haben.", titel="Mehrere Prioritäten"),
             frage("Genießt Anspruch 2 die Priorität von P2?", False,
                   ["**Nein!** Die Kombination A und B offenbart keines der Prioritätsdokumente. Prioritätsdokumente dürfen nicht mosaikartig "
                    "zusammengesetzt werden; maßgeblich ist der Anmeldetag 8.6.2026 (Art. 88 Abs. 3 EPÜ; Richtlinien F-VI, 1.5)."],
                   merke="Kein Mosaik aus Prioritätsdokumenten.", titel="Kombination", norms=["Art. 88 Abs. 3 EPÜ"], level=2),
             frage("H nimmt P1 vor Abschluss der technischen Vorbereitungen für die Veröffentlichung zurück. Wann wird die Anmeldung veröffentlicht?", 1,
                   ["**Nach dem 9.3.2027.** Veröffentlicht wird 18 Monate nach dem frühesten verbleibenden Prioritätstag (Art. 93 Abs. 1 lit. a EPÜ). "
                    "Auch vom Prioritätstag abhängige Fristen laufen ab P2, soweit sie noch nicht abgelaufen sind (Richtlinien F-VI, 3.5, E-VIII, 1.5)."],
                   optionen=["Nach dem 10.12.2026", "Nach dem 9.3.2027", "Nach dem 8.12.2027"],
                   merke="Rücknahme der frühesten Priorität verschiebt Veröffentlichung und Fristen.", titel="Rücknahme einer Priorität",
                   norms=["Art. 93 Abs. 1 EPÜ"], level=2),
            ],
            abschnitt="Art. 88 Abs. 2 EPÜ: mehrere Prioritäten", level=2, concepts=["epc_prioritaet"], norms=["Art. 88 Abs. 2 EPÜ"]),
        *fallkette("e01n87-5", "Die Erfinderin und die GmbH",
            "Die Erfinderin K reicht am 6.11.2024 allein eine US-Anmeldung ein. Am 5.11.2025 reichen K (für die USA) und die L-GmbH (für alle "
            "übrigen Staaten) gemeinsam eine PCT-Anmeldung mit der US-Priorität ein. Im europäischen Einspruchsverfahren bestreitet ein Einsprechender "
            "die Prioritätsberechtigung der L-GmbH.",
            [frage("Darf sich die L-GmbH auf die Priorität stützen, obwohl sie die US-Anmeldung nicht eingereicht hat?", True,
                   ["**Ja!** Wer die Priorität nach Art. 88 Abs. 1 EPÜ beansprucht, gilt widerleglich als berechtigt, auch wenn Prioritäts- und "
                    "Nachanmelder verschieden sind. Die gemeinsame PCT-Anmeldung begründet eine stillschweigende Abrede, dass die L-GmbH die Priorität "
                    "nutzen darf (G 1/22)."],
                   merke="Gemeinsame PCT-Anmeldung: Abrede zur Nutzung der Priorität wird vermutet.", titel="Prioritätsberechtigung"),
             frage("Wer muss im Einspruch was beweisen?", 2,
                   ["**Der Einsprechende muss die Vermutung widerlegen.** Das EPA ist für die Prioritätsberechtigung zuständig. Die Vermutung fällt nur "
                    "bei erheblichen tatsächlichen Anhaltspunkten gegen die Abrede (G 1/22)."],
                   optionen=["Die L-GmbH muss eine schriftliche Übertragung vor dem 5.11.2025 nachweisen",
                             "Niemand: Für die Berechtigung sind nur nationale Gerichte zuständig",
                             "Der Einsprechende muss die Vermutung der Berechtigung widerlegen"],
                   merke="Die Beweislast trägt, wer die Berechtigung bestreitet.", titel="Beweislast", level=2,
                   concepts=["epc_einspruch"]),
            ],
            abschnitt="Art. 87 Abs. 1 EPÜ: Berechtigung", level=2, concepts=["epc_prioritaet"], norms=["Art. 87 Abs. 1 EPÜ", "Art. 88 Abs. 1 EPÜ"],
            cases=["epc_g_1_22"]),
    ]),
    # ================================================================== Art. 114, 115 EPÜ
    dict(id="e01n115", order=11500, titel="Art. 114, 115 EPÜ: Einwendungen Dritter und Ermittlung von Amts wegen", einheiten=[
        intro("e01n115-0", "Der Dritte als Hinweisgeber",
              "Wer gegen eine fremde Anmeldung vorgehen will, ohne Beteiligter zu werden, erhebt **Einwendungen Dritter** (Art. 115 EPÜ): nach "
              "Veröffentlichung, schriftlich, in einer Amtssprache, begründet, ohne Gebühr, auch anonym (R. 114 EPÜ). Paper D fragt danach, ob "
              "Einwendungen den Erteilungsbeschluss noch aufhalten (2018 Frage 5) und welche Einwände zulässig sind, etwa mangelnde Klarheit "
              "(2019 Frage 2). Möglich wird das durch die **Ermittlung von Amts wegen** (Art. 114 Abs. 1 EPÜ). Art. 114 Abs. 2 EPÜ erlaubt dem Amt, "
              "verspätetes Vorbringen zurückzuweisen.",
              concepts=["epc_einwendungen_dritter", "epc_pruefungsverfahren", "epc_einspruch"],
              norms=["Art. 114 EPÜ", "Art. 115 EPÜ", "R. 114 EPÜ"], distinctions=["d_epc_angriffe_nach_erteilung"], abschnitt="Überblick"),
        *fallkette("e01n115-1", "Der Wettbewerber will anonym bleiben",
            "Die europäische Anmeldung von N ist veröffentlicht und in der Prüfung. Der Wettbewerber M besitzt eine japanische Patentschrift, die "
            "Anspruch 1 vorwegnimmt, und hält Anspruch 2 für unklar. M will nicht, dass N von seinem Vorgehen erfährt.",
            [frage("Kann M Einwendungen erheben, ohne seinen Namen zu nennen?", True,
                   ["**Ja!** Einwendungen Dritter können anonym eingereicht werden (Richtlinien E-VI, 3). Sie werden N mitgeteilt, der dazu Stellung "
                    "nehmen kann (R. 114 Abs. 2 EPÜ)."],
                   merke="Einwendungen Dritter: auch anonym.", titel="Anonymität"),
             frage("Darf M die japanische Patentschrift im Original einreichen?", True,
                   ["**Ja!** Die Einwendungen selbst sind in einer Amtssprache abzufassen und zu begründen (R. 114 Abs. 1 EPÜ). Beweismittel wie "
                    "Druckschriften können in jeder Sprache eingereicht werden; das EPA kann eine Übersetzung anfordern (Richtlinien E-VI, 3)."],
                   merke="Schriftsatz in Amtssprache, Belege in jeder Sprache.", titel="Sprache", norms=["R. 114 Abs. 1 EPÜ"], concepts=["epc_sprachen"],
                   level=2),
             frage("Kann M auch die mangelnde Klarheit von Anspruch 2 rügen?", True,
                   ["**Ja!** Art. 115 EPÜ nennt die Patentierbarkeit, das EPA berücksichtigt aber auch Einwände zu Klarheit (Art. 84 EPÜ), "
                    "Ausführbarkeit und unzulässigen Änderungen (Richtlinien E-VI, 3)."],
                   merke="Auch Klarheit kann Gegenstand von Einwendungen sein.", titel="Gegenstand", norms=["Art. 84 EPÜ"]),
             frage("Kann M schon jetzt Einwendungen erheben?", False,
                   ["**Nein!** Einwendungen sind erst nach Veröffentlichung der europäischen Patentanmeldung möglich (Art. 115 Satz 1 EPÜ)."],
                   merke="Erst die Veröffentlichung öffnet Art. 115 EPÜ.", titel="Abwandlung: noch nicht veröffentlicht",
                   abwandlung="Die Anmeldung von N ist noch nicht veröffentlicht; M kennt sie aus einer Lizenzverhandlung."),
            ],
            abschnitt="Art. 115 EPÜ: wer, wann, wie", level=1, concepts=["epc_einwendungen_dritter"], norms=["Art. 115 EPÜ", "R. 114 EPÜ"]),
        *fallkette("e01n115-2", "Kurz vor der Erteilung",
            "P hat auf die Mitteilung nach R. 71 Abs. 3 EPÜ hin die Gebühren gezahlt und die Übersetzungen eingereicht. Danach reicht Q Einwendungen "
            "mit einer älteren europäischen Anmeldung ein, die Anspruch 1 vorwegnimmt. Der Erteilungsbeschluss ist noch nicht an die Poststelle abgegeben.",
            [frage("Muss die Prüfungsabteilung die Einwendungen noch berücksichtigen?", True,
                   ["**Ja!** Einwendungen, die nach der Mitteilung nach R. 71 Abs. 3 EPÜ, aber vor Abgabe des Erteilungsbeschlusses an die Poststelle "
                    "eingehen, werden geprüft; sind sie relevant, nimmt die Prüfungsabteilung die Prüfung wieder auf (Richtlinien E-VI, 3)."],
                   merke="Bis zur Abgabe an die Poststelle zählt jede Einwendung.", titel="Nach dem Einverständnis", norms=["R. 71 Abs. 3 EPÜ"],
                   concepts=["epc_erteilung"]),
             frage("Werden die Einwendungen dann noch berücksichtigt?", False,
                   ["**Nein!** Mit der Abgabe an die Poststelle ist das schriftliche Verfahren abgeschlossen (G 12/91). Später eingehende Einwendungen "
                    "kommen ungeprüft zur Akte (Richtlinien E-VI, 3)."],
                   merke="Nach Abgabe an die Poststelle: nur noch zur Akte.", titel="Abwandlung: Beschluss abgegeben", level=2,
                   abwandlung="Die Einwendungen gehen einen Tag nach Abgabe des Erteilungsbeschlusses an die Poststelle ein."),
             frage("Kann Q gegen den Erteilungsbeschluss Beschwerde einlegen?", False,
                   ["**Nein!** Der Dritte ist am Verfahren nicht beteiligt (Art. 115 Satz 2 EPÜ); beschwerdeberechtigt sind nur Beteiligte "
                    "(Art. 107 EPÜ). Q bleibt der Einspruch binnen neun Monaten nach dem Hinweis auf die Erteilung (Art. 99 Abs. 1 EPÜ)."],
                   merke="Kein Beteiligter, keine Beschwerde – aber Einspruch.", titel="Rechtsstellung", norms=["Art. 107 EPÜ", "Art. 99 Abs. 1 EPÜ"],
                   concepts=["epc_beschwerde", "epc_einspruch"], step=_BESCHW + ".2"),
            ],
            abschnitt="Art. 115 EPÜ: Berücksichtigung und Rechtsstellung", level=2, concepts=["epc_einwendungen_dritter"], norms=["Art. 115 EPÜ"]),
        *fallkette("e01n115-3", "Einwendungen gegen das erteilte Patent",
            "Das Patent von R ist erteilt; die Einspruchsfrist läuft, ein Einspruch ist noch nicht eingelegt. S reicht Einwendungen ein: R habe die "
            "Erfindung vor dem Anmeldetag auf einer Hausmesse gezeigt. Belege fügt S nicht bei.",
            [frage("Berücksichtigt das EPA die Einwendungen jetzt?", False,
                   ["**Nein!** Einwendungen, die eingehen, solange kein Verfahren anhängig ist, bleiben unberücksichtigt. Sie werden berücksichtigt, "
                    "wenn wieder ein Verfahren anhängig wird, etwa ein Einspruch oder eine Beschränkung (Richtlinien E-VI, 3)."],
                   merke="Einwendungen brauchen ein anhängiges Verfahren.", titel="Kein anhängiges Verfahren", concepts=["epc_anhaengigkeit"]),
             frage("Muss die Einspruchsabteilung die Vorbenutzung zugrunde legen, wenn R sie bestreitet?", False,
                   ["**Nein!** Behaupteter Stand der Technik, der nicht aus einem Dokument folgt, etwa eine Benutzung, wird nur berücksichtigt, wenn er "
                    "unbestritten oder ohne vernünftigen Zweifel nachgewiesen ist (Richtlinien E-VI, 3)."],
                   merke="Vorbenutzung aus Einwendungen: unbestritten oder bewiesen.", titel="Abwandlung: Vorbenutzung", level=2,
                   abwandlung="Inzwischen hat ein Dritter Einspruch eingelegt; die Einwendungen von S liegen der Einspruchsabteilung vor."),
            ],
            abschnitt="Art. 115 EPÜ: nach der Erteilung", level=2, concepts=["epc_einwendungen_dritter", "epc_einspruch"], norms=["Art. 115 EPÜ"]),
        *fallkette("e01n115-4", "Amtsermittlung im Einspruch",
            "T legt gegen das Patent von U Einspruch ein und stützt ihn nur auf mangelnde Neuheit gegenüber D1. Die Einspruchsabteilung hält die "
            "Ansprüche zudem für unzulässig erweitert.",
            [frage("Darf die Einspruchsabteilung den nicht geltend gemachten Einspruchsgrund der unzulässigen Erweiterung prüfen?", True,
                   ["**Ja,** ausnahmsweise: Nach Art. 114 Abs. 1 EPÜ darf sie über den Einspruch hinausgehen, wenn der neue Grund prima facie der "
                    "Aufrechterhaltung entgegensteht (G 10/91; Richtlinien E-VI, 2.1)."],
                   merke="Neuer Einspruchsgrund von Amts wegen nur bei prima facie Relevanz.", titel="Neuer Einspruchsgrund",
                   norms=["Art. 100 EPÜ"], cases=["epc_g_10_91", "epc_g_9_91"], step=_EINS + ".5", level=2),
             frage("Muss die Einspruchsabteilung ein Dokument berücksichtigen, das T erst in der mündlichen Verhandlung vorlegt?", False,
                   ["**Nein!** Verspätet vorgebrachte Tatsachen und Beweismittel braucht das EPA nicht zu berücksichtigen (Art. 114 Abs. 2 EPÜ). Es "
                    "lässt sie nur zu, wenn sie prima facie relevant sind, also die Entscheidung ändern würden (Richtlinien E-VI, 2)."],
                   merke="Verspätet: zugelassen nur bei prima facie Relevanz.", titel="Verspätetes Vorbringen", norms=["Art. 114 Abs. 2 EPÜ"]),
             frage("Kann die Einspruchsabteilung das Verfahren fortsetzen, wenn T den Einspruch zurücknimmt?", True,
                   ["**Ja!** Das Einspruchsverfahren kann nach Rücknahme des Einspruchs von Amts wegen fortgesetzt werden (R. 84 Abs. 2 Satz 2 EPÜ); "
                    "das folgt aus der Amtsermittlung (Art. 114 Abs. 1 EPÜ)."],
                   merke="Der Einspruch gehört nach Einlegung nicht mehr allein dem Einsprechenden.", titel="Rücknahme des Einspruchs",
                   norms=["R. 84 Abs. 2 EPÜ"], step=_EINS + ".6"),
             frage("Kann T den neuen Einspruchsgrund erst im Beschwerdeverfahren einführen, wenn U widerspricht?", False,
                   ["**Nein!** Neue Einspruchsgründe dürfen im Beschwerdeverfahren nur mit Einverständnis des Patentinhabers geprüft werden (G 10/91)."],
                   merke="Beschwerde: neuer Einspruchsgrund nur mit Zustimmung des Inhabers.", titel="Beschwerdeverfahren", level=3,
                   cases=["epc_g_10_91"], concepts=["epc_beschwerde"]),
            ],
            abschnitt="Art. 114 EPÜ: Amtsermittlung und Verspätung", level=2, concepts=["epc_einspruch"],
            norms=["Art. 114 Abs. 1 EPÜ", "Art. 114 Abs. 2 EPÜ"]),
    ]),
    # ================================================================== Art. 123 EPÜ, R. 137 EPÜ
    dict(id="e01n123", order=12300, titel="Art. 123 EPÜ: Änderungen", einheiten=[
        intro("e01n123-0", "Wann, was, wie weit",
              "Art. 123 EPÜ beantwortet drei Fragen. **Wann** darf geändert werden (Abs. 1 mit R. 137 EPÜ)? **Was** darf hinein: nur, was die "
              "Anmeldung ursprünglich unmittelbar und eindeutig offenbart (Abs. 2, Goldstandard nach G 2/10). **Wie weit** nach der Erteilung: "
              "keine Erweiterung des Schutzbereichs (Abs. 3). Paper D prüft Zwischenverallgemeinerung und nicht recherchierte Gegenstände (2023 "
              "Frage 1), Verwendungsansprüche (2023 Frage 6, G 2/88), Abs. 3 in der Beschränkung (2021 Frage 6) und Änderungen im Einspruch "
              "(2018 Frage 2). Dazu kommen Disclaimer (G 1/03, G 2/10, G 1/16), die Falle aus G 1/93 und die Anpassung der Beschreibung (G 1/25).",
              concepts=["epc_unzulaessige_erweiterung", "epc_schutzbereichserweiterung", "epc_disclaimer"],
              norms=["Art. 123 EPÜ", "R. 137 EPÜ"], cases=["epc_g_2_10", "epc_g_1_93"], distinctions=["d_epc_123_2_123_3"], abschnitt="Überblick"),
        *fallkette("e01n123-1", "Wann darf geändert werden?",
            "V reicht direkt beim EPA eine Anmeldung mit Ansprüchen auf die Vorrichtung A ein. Die Beschreibung schildert außerdem ein Verfahren mit "
            "den Merkmalen E und F, das mit A keine gemeinsame erfinderische Idee teilt und nicht recherchiert wird.",
            [frage("Darf V die Ansprüche ändern, bevor er den Recherchenbericht erhalten hat?", False,
                   ["**Nein!** Vor Erhalt des europäischen Recherchenberichts darf der Anmelder Beschreibung, Ansprüche und Zeichnungen nicht ändern, "
                    "sofern nichts anderes bestimmt ist (R. 137 Abs. 1 EPÜ)."],
                   merke="Vor dem Recherchenbericht keine Änderungen.", titel="Vor der Recherche", norms=["R. 137 Abs. 1 EPÜ"]),
             frage("Darf V mit seiner Erwiderung auf die Stellungnahme zur Recherche von sich aus ändern?", True,
                   ["**Ja!** Mit der Erwiderung auf die Mitteilung nach R. 70a EPÜ kann der Anmelder von sich aus ändern (R. 137 Abs. 2 EPÜ; "
                    "Art. 123 Abs. 1 Satz 2 EPÜ). Spätere Änderungen bedürfen der Zustimmung der Prüfungsabteilung (R. 137 Abs. 3 EPÜ)."],
                   merke="Einmal von sich aus, danach mit Zustimmung.", titel="Nach der Recherche", norms=["R. 137 Abs. 2 EPÜ", "R. 137 Abs. 3 EPÜ"]),
             frage("Darf V die Ansprüche durch Ansprüche auf das Verfahren mit E und F ersetzen?", False,
                   ["**Nein!** Geänderte Ansprüche dürfen sich nicht auf nicht recherchierte Gegenstände beziehen, die mit der ursprünglich beanspruchten "
                    "Erfindung nicht durch eine allgemeine erfinderische Idee verbunden sind (R. 137 Abs. 5 EPÜ). V muss dafür eine Teilanmeldung "
                    "einreichen, solange die Anmeldung anhängig ist (Art. 76 EPÜ, R. 36 Abs. 1 EPÜ)."],
                   merke="Nicht recherchiert und uneinheitlich: Teilanmeldung.", titel="Nicht recherchierter Gegenstand",
                   norms=["R. 137 Abs. 5 EPÜ", "Art. 76 EPÜ"], concepts=["epc_einheitlichkeit", "epc_teilanmeldung"], level=2),
             frage("Hat V nach seinem Einverständnis mit der Fassung nach R. 71 Abs. 3 EPÜ noch ein Recht auf weitere Änderungen?", False,
                   ["**Nein!** Danach lässt die Prüfungsabteilung Änderungen nur nach Ermessen zu (R. 137 Abs. 3 EPÜ), in der Regel nur geringfügige, "
                    "die keine Wiederaufnahme der Prüfung erfordern (G 7/93; Richtlinien H-II, 2.6)."],
                   merke="Nach dem Einverständnis entscheidet das Ermessen.", titel="Nach der Mitteilung nach R. 71 Abs. 3 EPÜ",
                   norms=["R. 71 Abs. 3 EPÜ"], concepts=["epc_erteilung"], level=2),
            ],
            abschnitt="Abs. 1: Zeitpunkt (R. 137 EPÜ)", level=1, concepts=["epc_pruefungsverfahren"], norms=["Art. 123 Abs. 1 EPÜ", "R. 137 EPÜ"]),
        *fallkette("e01n123-2", "Das herausgelöste Merkmal",
            "Die Anmeldung von W beschreibt nur ein Ausführungsbeispiel: einen Filter mit Gehäuse G, Membran M und Halterung H, die M im Gehäuse "
            "festklemmt. Es heißt dort, der Filter könne „vorzugsweise“ einen Drucksensor S haben. Anspruch 1 lautet „Filter mit Gehäuse G“.",
            [frage("Welcher Maßstab gilt für Änderungen nach Art. 123 Abs. 2 EPÜ?", 2,
                   ["**Unmittelbare und eindeutige Offenbarung.** Zulässig ist nur, was der Fachmann unter Heranziehung des allgemeinen Fachwissens der "
                    "Anmeldung in der ursprünglichen Fassung unmittelbar und eindeutig entnimmt, ausdrücklich oder implizit (Goldstandard, G 2/10)."],
                   optionen=["Was dem Fachmann angesichts der Anmeldung naheliegt", "Was durch den Wortlaut der Anmeldung gestützt wird",
                             "Was der Fachmann der Anmeldung unmittelbar und eindeutig entnimmt"],
                   merke="Goldstandard: unmittelbar und eindeutig offenbart.", titel="Maßstab", cases=["epc_g_2_10"]),
             frage("Darf W die Membran M ohne die Halterung H in Anspruch 1 aufnehmen?", False,
                   ["**Nein!** Ein Merkmal darf nur aus einem Ausführungsbeispiel herausgelöst werden, wenn es mit den übrigen Merkmalen nicht "
                    "strukturell und funktionell verknüpft ist. M und H wirken zusammen; M allein wäre eine unzulässige Zwischenverallgemeinerung "
                    "(Richtlinien H-V, 3.2.1)."],
                   merke="Verknüpfte Merkmale nur gemeinsam.", titel="Zwischenverallgemeinerung", level=2),
             frage("Darf W den Drucksensor S allein in Anspruch 1 aufnehmen?", True,
                   ["**Ja!** S ist allgemein als bevorzugt beschrieben und nicht mit M oder H verknüpft. Die Offenbarung rechtfertigt, S isoliert mit "
                    "dem Gehäuse zu kombinieren (Art. 123 Abs. 2 EPÜ; Richtlinien H-V, 3.2.1)."],
                   merke="Unabhängiges, allgemein beschriebenes Merkmal: isoliert aufnehmbar.", titel="Unabhängiges Merkmal"),
             frage("Muss W die Beschreibung anpassen, wenn sie S weiter als bloß bevorzugt darstellt und der Anspruch dadurch unklar wird?", True,
                   ["**Ja!** Führt eine Anspruchsänderung zu einem Widerspruch mit der Beschreibung, wegen dessen etwa Art. 84 EPÜ nicht erfüllt ist, "
                    "ist die Beschreibung anzupassen (G 1/25)."],
                   merke="Widerspruch mit Folgen für Art. 84 EPÜ: Beschreibung anpassen.", titel="Anpassung der Beschreibung", level=2,
                   norms=["Art. 84 EPÜ"], cases=["epc_g_1_25"]),
            ],
            abschnitt="Abs. 2: Goldstandard und Zwischenverallgemeinerung", level=2, concepts=["epc_unzulaessige_erweiterung"],
            norms=["Art. 123 Abs. 2 EPÜ"]),
        *fallkette("e01n123-3", "Der Disclaimer",
            "Anspruch 1 der Anmeldung von X betrifft einen Klebstoff mit 1 bis 10 % Harz Z; die Anmeldung erwähnt keinen bestimmten Wert. Ein vor "
            "dem Anmeldetag veröffentlichter Aufsatz über Klebstoffe für denselben Zweck offenbart einen Klebstoff mit 5 % Z.",
            [frage("Darf X die Neuheit durch den nicht offenbarten Disclaimer „ausgenommen 5 % Z“ herstellen?", False,
                   ["**Nein!** Ein nicht offenbarter Disclaimer darf gegenüber Art. 54 Abs. 2 EPÜ nur eine **zufällige** Vorwegnahme ausklammern "
                    "(G 1/03). Ein Aufsatz über denselben Zweck ist nicht zufällig; X muss sich auf andere Weise abgrenzen."],
                   merke="Gegen echten Stand der Technik hilft kein nicht offenbarter Disclaimer.", titel="Nicht zufällige Vorwegnahme",
                   norms=["Art. 54 Abs. 2 EPÜ"], cases=["epc_g_1_03"]),
             frage("Ist der Disclaimer jetzt zulässig?", True,
                   ["**Ja!** Eine Vorwegnahme ist zufällig, wenn sie so fernab liegt, dass der Fachmann sie nicht berücksichtigt hätte. Der Disclaimer "
                    "darf keinen technischen Beitrag leisten (G 1/03, G 1/16)."],
                   merke="Zufällige Vorwegnahme: Disclaimer zulässig.", titel="Abwandlung: zufällige Vorwegnahme", level=2, cases=["epc_g_1_16"],
                   abwandlung="Der Aufsatz betrifft ein Gleitmittel für Bohrköpfe, in dem Z zufällig mit 5 % vorkommt."),
             frage("Darf X stattdessen „ausgenommen 4 bis 6 % Z“ ausklammern?", False,
                   ["**Nein!** Der Disclaimer darf nicht mehr ausschließen, als nötig ist, um die Neuheit wiederherzustellen (G 1/16, G 1/03)."],
                   merke="Disclaimer: so eng wie die Vorwegnahme.", titel="Umfang", cases=["epc_g_1_16"]),
             frage("Ist der Disclaimer allein deshalb zulässig, weil die Anmeldung den ausgeklammerten Wert nennt?", False,
                   ["**Nein!** Auch ein offenbarter Disclaimer verstößt gegen Art. 123 Abs. 2 EPÜ, wenn der **verbleibende** Gegenstand nicht unmittelbar "
                    "und eindeutig offenbart ist (G 2/10)."],
                   merke="Beim offenbarten Disclaimer zählt der Rest.", titel="Abwandlung: offenbarter Disclaimer", level=3, cases=["epc_g_2_10"],
                   abwandlung="Die Anmeldung nennt 5 % Z ausdrücklich als ein Beispiel."),
            ],
            abschnitt="Abs. 2: Disclaimer", level=2, concepts=["epc_disclaimer", "epc_unzulaessige_erweiterung"], norms=["Art. 123 Abs. 2 EPÜ"]),
        *fallkette("e01n123-4", "Rindfleisch statt Fleisch",
            "Anspruch 1 des erteilten Patents von Y lautet „Lebensmittel, enthaltend 1 bis 5 % Fleisch“; die Beschreibung nennt Rindfleisch. Y "
            "beantragt die Beschränkung auf „Lebensmittel, enthaltend 1 bis 5 % Rindfleisch“.",
            [frage("Ist die Änderung mit Art. 123 Abs. 3 EPÜ vereinbar?", False,
                   ["**Nein!** Ein Lebensmittel mit 3 % Rind- und 3 % Schweinefleisch fiele unter den neuen Anspruch, aber nicht unter den erteilten "
                    "(6 % Fleisch). Das Engführen eines Bestandteils einer offenen Zusammensetzung kann den Schutz erweitern (Richtlinien H-IV, 3.4; "
                    "T 287/11)."],
                   merke="Engere Komponente in offener Zusammensetzung kann den Schutz erweitern.", titel="Versteckte Erweiterung", level=3,
                   norms=["Art. 105a EPÜ"], concepts=["epc_beschraenkung"]),
             frage("Wäre „1 bis 5 % Fleisch, wobei das Fleisch Rindfleisch ist“ zulässig?", True,
                   ["**Ja!** Die Fleischmenge insgesamt bleibt auf 1 bis 5 % begrenzt, zusätzlich muss es Rindfleisch sein; jede Ausführungsform fällt "
                    "auch unter den erteilten Anspruch (Art. 123 Abs. 3 EPÜ, Art. 69 EPÜ)."],
                   merke="Echte Beschränkung: zusätzliches Merkmal, alte Grenze bleibt.", titel="Zulässige Fassung", level=2, norms=["Art. 69 EPÜ"]),
             frage("Darf Y im Einspruch „Zusatzstoff S“ in „Verwendung von S zur Konservierung von Lebensmitteln“ ändern?", True,
                   ["**Ja!** Der Wechsel vom Stoffanspruch zum Verwendungsanspruch für einen bestimmten Zweck erweitert den Schutzbereich nicht (G 2/88). "
                    "Umgekehrt, von der Verwendung zum Stoff, wäre er unzulässig."],
                   merke="Vom Stoff zur Verwendung: zulässig.", titel="Kategoriewechsel", level=2, cases=["epc_g_2_88"],
                   abwandlung="Ein anderes Patent von Y beansprucht „Zusatzstoff S“; es ist mit Einspruch angegriffen."),
            ],
            abschnitt="Abs. 3: Schutzbereich nach der Erteilung", level=2, concepts=["epc_schutzbereichserweiterung"],
            norms=["Art. 123 Abs. 3 EPÜ"]),
        *fallkette("e01n123-5", "Die unentrinnbare Falle",
            "In der Prüfung fügte Z in Anspruch 1 das Merkmal „Gehäuse aus Kunststoff“ ein; die Anmeldung nannte nur ein Gehäuse aus Polyamid. "
            "Das Patent wird erteilt. Ein Einsprechender stützt sich auf Art. 100 lit. c EPÜ.",
            [frage("Kann das Patent unverändert aufrechterhalten werden?", False,
                   ["**Nein!** „Kunststoff“ geht über die ursprüngliche Offenbarung hinaus (Art. 123 Abs. 2 EPÜ); der Einspruchsgrund nach "
                    "Art. 100 lit. c EPÜ steht der Aufrechterhaltung entgegen (G 1/93)."],
                   merke="Unzulässige Erweiterung im erteilten Anspruch: Einspruchsgrund.", titel="Unverändert", norms=["Art. 100 EPÜ"],
                   step=_EINS + ".5"),
             frage("Kann Z das Merkmal einfach streichen?", False,
                   ["**Nein!** Die Streichung des beschränkenden Merkmals würde den Schutzbereich erweitern (Art. 123 Abs. 3 EPÜ). Das ist die "
                    "Falle aus G 1/93."],
                   merke="Streichen verletzt Abs. 3, Behalten Abs. 2.", titel="Streichung", level=2),
             frage("Kann Z „Kunststoff“ durch „Polyamid“ ersetzen?", True,
                   ["**Ja!** Polyamid ist ursprünglich offenbart und enger als Kunststoff. Wenn die Anmeldung eine Grundlage für den Austausch bietet "
                    "und der Schutzbereich nicht erweitert wird, kann das Patent aufrechterhalten werden (G 1/93; Richtlinien H-IV, 3.5)."],
                   merke="Ausweg: durch ein offenbartes, engeres Merkmal ersetzen.", titel="Ersetzung", level=2),
             frage("Kann das Patent mit diesem Merkmal aufrechterhalten werden?", True,
                   ["**Ja!** Ein nicht offenbartes Merkmal, das keinen technischen Beitrag leistet und nur einen Teil des Gegenstands vom Schutz "
                    "ausnimmt, ist keine unzulässige Erweiterung (G 1/93, Leitsatz 2)."],
                   merke="Ohne technischen Beitrag schadet das Merkmal nicht.", titel="Abwandlung: kein technischer Beitrag", level=3,
                   abwandlung="Das eingefügte Merkmal trägt technisch nichts zur Erfindung bei und nimmt nur einen Teil des ursprünglich "
                              "beanspruchten Gegenstands vom Schutz aus."),
            ],
            abschnitt="Abs. 2 und 3: Kollision", level=2, concepts=["epc_unzulaessige_erweiterung", "epc_schutzbereichserweiterung", "epc_einspruch"],
            norms=["Art. 123 Abs. 2 EPÜ", "Art. 123 Abs. 3 EPÜ"], cases=["epc_g_1_93"]),
    ]),
    # ================================================================== R. 139, R. 140 EPÜ
    dict(id="e01n139", order=12350, titel="R. 139, R. 140 EPÜ: Berichtigung von Fehlern", einheiten=[
        intro("e01n139-0", "Berichtigen ist nicht Ändern",
              "R. 139 EPÜ erlaubt, sprachliche Fehler, Schreibfehler und Unrichtigkeiten in eingereichten Unterlagen zu berichtigen. In Beschreibung, "
              "Ansprüchen und Zeichnungen muss die Berichtigung **offensichtlich** sein: Fehler und Korrektur sind den ursprünglichen Unterlagen selbst "
              "zu entnehmen, nicht dem Prioritätsdokument (G 3/89, G 11/91). Paper D fragt danach bei Übersetzungsfehlern (2015 Frage 4), bei Fehlern "
              "in der Fassung nach R. 71 Abs. 3 EPÜ (2022 Frage 2) und beim falschen Namen in der Beschwerdeschrift (2023 Frage 4, G 1/12). "
              "R. 140 EPÜ betrifft nur Entscheidungen, nie den Text des erteilten Patents (G 1/10).",
              concepts=["epc_berichtigung"], norms=["R. 139 EPÜ", "R. 140 EPÜ"],
              cases=["epc_g_3_89", "epc_g_11_91", "epc_g_1_10", "epc_g_1_12"], distinctions=["d_epc_r56_r56a_r139"], abschnitt="Überblick"),
        *fallkette("e01n139-1", "Copyright statt Mikrometer",
            "AA reicht EP-1 auf Japanisch mit englischer Übersetzung und EP-2 auf Englisch ein; beide beanspruchen eine japanische Priorität. In der "
            "Übersetzung von EP-1 und in EP-2 steht „©“ statt „µm“. Der japanische Text von EP-1 und das Prioritätsdokument nennen richtig „µm“; der "
            "Zusammenhang im englischen Text lässt die Korrektur nicht erkennen.",
            [frage("Kann AA den Fehler in der Übersetzung von EP-1 beheben?", True,
                   ["**Ja!** Die Übersetzung kann während des gesamten Verfahrens mit der Anmeldung in der ursprünglich eingereichten Fassung, hier dem "
                    "japanischen Text, in Übereinstimmung gebracht werden (Art. 14 Abs. 2 Satz 2 EPÜ). Auf die Offensichtlichkeit kommt es nicht an."],
                   merke="Maßstab für Übersetzungsfehler ist das Original, nicht R. 139 EPÜ.", titel="Fehler in der Übersetzung",
                   norms=["Art. 14 Abs. 2 EPÜ", "R. 7 EPÜ"], concepts=["epc_sprachen"]),
             frage("Kann AA den Fehler in EP-2 nach R. 139 EPÜ berichtigen?", False,
                   ["**Nein!** Fehler und Korrektur müssen sofort aus den ursprünglich eingereichten Unterlagen erkennbar sein (R. 139 Satz 2 EPÜ). Das "
                    "Prioritätsdokument darf dafür nicht herangezogen werden (G 3/89, G 11/91; Richtlinien H-VI, 2.2.1)."],
                   merke="Das Prioritätsdokument beweist keine offensichtliche Unrichtigkeit.", titel="Fehler im Original", level=2),
             frage("Kann AA den Fehler in EP-2 dann berichtigen?", True,
                   ["**Ja!** Erkennt der Fachmann aus der Anmeldung selbst, dass ein Fehler vorliegt und nur „µm“ gemeint sein kann, ist die Berichtigung "
                    "zulässig. Sie wirkt feststellend und verletzt Art. 123 Abs. 2 EPÜ nicht (G 3/89)."],
                   merke="Fehler und Korrektur aus der Anmeldung selbst: berichtigungsfähig.", titel="Abwandlung: erkennbarer Fehler",
                   norms=["Art. 123 Abs. 2 EPÜ"],
                   abwandlung="Aus Tabellen und Maßangaben in EP-2 ergibt sich eindeutig, dass nur „µm“ gemeint sein kann."),
            ],
            abschnitt="R. 139 Satz 2 EPÜ: Beschreibung, Ansprüche, Zeichnungen", level=2, concepts=["epc_berichtigung"],
            norms=["R. 139 EPÜ"], cases=["epc_g_3_89", "epc_g_11_91"]),
        *fallkette("e01n139-2", "Der Schreibfehler in der Druckfassung",
            "BB erhält eine Mitteilung nach R. 71 Abs. 3 EPÜ vom 14.9.2026. In Anspruch 4 steht „Polyetylen“; dass „Polyethylen“ gemeint ist, liegt "
            "auf der Hand.",
            [frage("Kann BB den Fehler noch vor der Erteilung berichtigen lassen?", True,
                   ["**Ja!** BB beantragt innerhalb der Viermonatsfrist begründet die Berichtigung (R. 71 Abs. 6 EPÜ, R. 139 Satz 2 EPÜ). Stimmt die "
                    "Prüfungsabteilung zu, erlässt sie eine neue Mitteilung nach R. 71 Abs. 3 EPÜ (Richtlinien C-V, 4.3)."],
                   merke="Fehler in der Druckfassung: vor der Erteilung rügen.", titel="Vor der Erteilung", norms=["R. 71 Abs. 6 EPÜ"],
                   concepts=["epc_erteilung"]),
             frage("Kann BB den Wortlaut des erteilten Patents nach R. 140 EPÜ berichtigen lassen?", False,
                   ["**Nein!** R. 140 EPÜ dient nicht der Berichtigung des Wortlauts eines Patents; ein solcher Antrag des Inhabers ist jederzeit "
                    "unzulässig, auch im Einspruch (G 1/10). Die Verantwortung für den gebilligten Text trägt der Anmelder."],
                   merke="R. 140 EPÜ heilt keine Fehler im gebilligten Text.", titel="Abwandlung: nach der Erteilung", level=2, cases=["epc_g_1_10"],
                   abwandlung="BB übersieht den Fehler, billigt die Fassung, und das Patent wird erteilt."),
             frage("Kann das berichtigt werden?", True,
                   ["**Ja!** Weicht die veröffentlichte Patentschrift vom Druckexemplar ab, auf dem die Erteilung beruht, liegt ein Fehler bei der "
                    "Veröffentlichung vor; er kann jederzeit berichtigt werden (Richtlinien H-VI, 6)."],
                   merke="Druckfehler der Veröffentlichung: jederzeit berichtigungsfähig.", titel="Abwandlung: Fehler bei der Veröffentlichung",
                   abwandlung="Anders als im Ausgangsfall war das gebilligte Druckexemplar fehlerfrei; erst die veröffentlichte Patentschrift "
                              "enthält „Polyetylen“."),
             frage("Kann ein Schreibfehler im Namen der Inhaberin im Erteilungsbeschluss nach R. 140 EPÜ berichtigt werden?", True,
                   ["**Ja!** Bibliografische Daten im Erteilungsbeschluss, die offensichtlich nicht dem Willen der Prüfungsabteilung entsprechen, sind "
                    "nach R. 140 EPÜ berichtigungsfähig, solange keine andere Person bezeichnet wird (Richtlinien H-VI, 3.2)."],
                   merke="R. 140 EPÜ: Fehler in Entscheidungen, etwa bibliografische Daten.", titel="Fehler in der Entscheidung", level=2,
                   norms=["R. 140 EPÜ"]),
            ],
            abschnitt="R. 139, R. 140 EPÜ: vor und nach der Erteilung", level=2, concepts=["epc_berichtigung"], norms=["R. 139 EPÜ", "R. 140 EPÜ"]),
        *fallkette("e01n139-3", "Die falsche Gesellschaft",
            "Das Patent wurde von der CC-AG auf die DD-GmbH umgeschrieben; die Umschreibung ist eingetragen. Die Einspruchsabteilung widerruft das "
            "Patent. Der Vertreter legt fristgerecht Beschwerde ein, nennt aber versehentlich die CC-AG als Beschwerdeführerin; beauftragt hatte "
            "ihn die DD-GmbH.",
            [frage("Ist die Beschwerde der CC-AG zulässig?", False,
                   ["**Nein!** Beschwerde einlegen kann nur, wer am Verfahren beteiligt und durch die Entscheidung beschwert ist (Art. 107 EPÜ). Die "
                    "CC-AG ist nach der eingetragenen Umschreibung nicht mehr Beteiligte."],
                   merke="Beschwerdeberechtigt ist nur der beschwerte Beteiligte.", titel="Beschwerdeberechtigung", norms=["Art. 107 EPÜ"],
                   step=_BESCHW + ".2"),
             frage("Kann der Name der Beschwerdeführerin in DD-GmbH berichtigt werden?", True,
                   ["**Ja!** War es die wirkliche Absicht, die Beschwerde für die DD-GmbH einzulegen, kann der Name nach R. 101 Abs. 2 EPÜ und "
                    "R. 139 Satz 1 EPÜ berichtigt werden. Es gilt freie Beweiswürdigung; der Auftrag der DD-GmbH ist das Beweismittel (G 1/12)."],
                   merke="Falscher Name in der Beschwerdeschrift: berichtigungsfähig bei nachweisbarer Absicht.", titel="Berichtigung des Namens",
                   norms=["R. 101 Abs. 2 EPÜ", "R. 99 Abs. 1 EPÜ"], cases=["epc_g_1_12"], step=_BESCHW + ".4", level=2),
             frage("Kann der Name auch dann berichtigt werden?", False,
                   ["**Nein!** Die Berichtigung soll ausdrücken, was bei Einlegung tatsächlich gewollt war. Eine spätere Meinungsänderung macht die "
                    "damalige Angabe nicht zum Fehler (G 1/12)."],
                   merke="Berichtigt wird ein Irrtum, nicht ein Sinneswandel.", titel="Abwandlung: Sinneswandel", level=3, cases=["epc_g_1_12"],
                   abwandlung="Die CC-AG wollte die Beschwerde bewusst selbst einlegen; erst später soll die DD-GmbH Beschwerdeführerin sein."),
            ],
            abschnitt="R. 139 Satz 1 EPÜ: Verfahrenserklärungen", level=2, concepts=["epc_berichtigung", "epc_beschwerde"], norms=["R. 139 EPÜ"]),
        *fallkette("e01n139-4", "Die vergessene Priorität",
            "EE reicht am 5.5.2025 eine europäische Anmeldung für die Merkmale A und B ein und beansprucht die Priorität von P2 vom 2.9.2024, "
            "die B offenbart. Die ältere Anmeldung P1 vom 6.5.2024, die A offenbart, vergisst sie anzugeben.",
            [frage("Kann EE die Priorität von P1 im Juli 2025 noch hinzufügen?", True,
                   ["**Ja!** Die Prioritätserklärung kann innerhalb von 16 Monaten nach dem frühesten beanspruchten Prioritätstag abgegeben werden "
                    "(R. 52 Abs. 2 EPÜ); verschiebt die neue Priorität diesen Tag, rechnet die Frist ab P1 (Richtlinien A-III, 6.5.1)."],
                   merke="Priorität nachtragen: R. 52 Abs. 2 EPÜ, nicht R. 139 EPÜ.", titel="Nachträgliche Prioritätserklärung",
                   norms=["R. 52 Abs. 2 EPÜ"], concepts=["epc_prioritaet"]),
             frage("Kann EE P1 jetzt noch nach R. 139 EPÜ einfügen lassen?", False,
                   ["**Nein,** grundsätzlich nicht: Nach Ablauf der Fristen der R. 52 EPÜ und der Veröffentlichung schützt das EPA das Vertrauen der "
                    "Öffentlichkeit. Eine Ausnahme gilt nur, wenn der Fehler aus der veröffentlichten Anmeldung selbst ersichtlich ist (J 6/91; "
                    "Richtlinien A-V, 3)."],
                   merke="Nach Veröffentlichung: Prioritätsberichtigung nur bei offenkundigem Fehler.", titel="Abwandlung: nach Veröffentlichung",
                   level=3, norms=["R. 52 Abs. 3 EPÜ"],
                   abwandlung="EE bemerkt das Versäumnis erst im April 2026, nach der Veröffentlichung; die Anmeldung lässt den Fehler nicht erkennen."),
            ],
            abschnitt="R. 139 Satz 1 EPÜ: Prioritätsangaben", level=2, concepts=["epc_berichtigung", "epc_prioritaet"], norms=["R. 139 EPÜ"]),
    ]),
]
