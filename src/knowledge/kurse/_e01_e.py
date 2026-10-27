# -*- coding: utf-8 -*-
"""Kapitel des Normkurses e01 (siehe e01_epue_paper_d.py): Art. 54, 55 EPÜ (Neuheit, Stand der Technik) und Art. 121 EPÜ mit R. 135 EPÜ
(Weiterbehandlung) – die beiden in Paper D am häufigsten herangezogenen Vorschriften. `order` = Artikel × 100."""
from ._helpers import intro, schema, frage, fallkette

_SDT = "step:epc_schema_stand_der_technik"
_FV = "step:epc_schema_fristversaeumnis"

KAPITEL = [
    # ================================================================== Art. 54, 55 EPÜ
    dict(id="e01n54", order=5400, titel="Art. 54, 55 EPÜ: Neuheit und Stand der Technik", einheiten=[
        intro("e01n54-0", "Der wirksame Tag entscheidet",
              "Art. 54 EPÜ ist die in Paper D am häufigsten herangezogene Vorschrift (15 der 54 Fragen 2015 bis 2025). Gefragt wird fast nie, ob "
              "ein Dokument die Erfindung offenbart, sondern **ob es überhaupt Stand der Technik ist**. Dafür zuerst je Anspruch den wirksamen Tag "
              "bestimmen (Priorität, Art. 89 EPÜ), dann jedes Dokument einordnen: vorveröffentlicht nach **Art. 54 Abs. 2 EPÜ**, ältere europäische "
              "Anmeldung nach **Art. 54 Abs. 3 EPÜ** (nur Neuheit) oder gar kein Stand der Technik. Art. 55 EPÜ nimmt Missbrauch und anerkannte "
              "Ausstellungen aus, nicht eigene Veröffentlichungen.",
              concepts=["epc_stand_der_technik", "epc_aeltere_rechte", "epc_unschaedliche_offenbarung"],
              norms=["Art. 54 Abs. 2 EPÜ", "Art. 54 Abs. 3 EPÜ", "Art. 55 EPÜ", "Art. 89 EPÜ"], distinctions=["d_epc_54_2_54_3"], abschnitt="Überblick"),
        schema("e01n54-0s", "Prüfungsschema Stand der Technik", "epc_schema_stand_der_technik", abschnitt="Überblick"),
        *fallkette("e01n54-1", "Der Fachartikel im Prioritätsintervall",
            "A reicht am 3.3.2025 eine deutsche Anmeldung für das Verfahren X ein und veröffentlicht am 2.6.2025 einen Fachartikel über X. Am "
            "3.3.2026 reicht A eine europäische Anmeldung unter Inanspruchnahme der deutschen Priorität ein. Anspruch 1 betrifft X, Anspruch 2 "
            "X mit dem Merkmal Y, das nur die europäische Anmeldung beschreibt.",
            [frage("Ist der Fachartikel Stand der Technik für Anspruch 1?", False,
                   ["**Nein!** Anspruch 1 genießt die Priorität vom 3.3.2025: erste Anmeldung, dieselbe Erfindung, Frist von zwölf Monaten gewahrt "
                    "(Art. 87 Abs. 1 EPÜ). Der Prioritätstag gilt als Anmeldetag (Art. 89 EPÜ); der Artikel vom 2.6.2025 ist danach erschienen."],
                   merke="Wirksame Priorität verlegt den Stichtag auf den Prioritätstag.", titel="Wirksamer Tag Anspruch 1",
                   norms=["Art. 87 Abs. 1 EPÜ", "Art. 89 EPÜ"], concepts=["epc_prioritaet"], step=_SDT + ".1.1"),
             frage("Ist der Fachartikel Stand der Technik nach Art. 54 Abs. 2 EPÜ für Anspruch 2?", True,
                   ["**Ja!** X mit Y ist in der deutschen Anmeldung nicht offenbart; für Anspruch 2 gilt der Anmeldetag 3.3.2026 (G 2/98). Der Artikel "
                    "war davor öffentlich zugänglich, also Stand der Technik für Neuheit und erfinderische Tätigkeit (G 3/93)."],
                   merke="Ohne Priorität schadet auch die eigene Veröffentlichung im Intervall.", titel="Wirksamer Tag Anspruch 2",
                   cases=["epc_g_2_98", "epc_g_3_93"], step=_SDT + ".2.1", level=2),
             frage("Kann A sich für Anspruch 2 auf Art. 55 EPÜ berufen?", False,
                   ["**Nein!** Art. 55 Abs. 1 EPÜ erfasst nur offensichtlichen Missbrauch und Zurschaustellung auf anerkannten Ausstellungen. Eine "
                    "eigene Veröffentlichung fällt nicht darunter; zudem lag sie mehr als sechs Monate vor der Einreichung (G 3/98)."],
                   merke="Das EPÜ kennt keine Neuheitsschonfrist für eigene Veröffentlichungen.", titel="Unschädliche Offenbarung",
                   norms=["Art. 55 Abs. 1 EPÜ"], cases=["epc_g_3_98"], concepts=["epc_unschaedliche_offenbarung"], step=_SDT + ".2.3"),
            ],
            abschnitt="Abs. 2: vorveröffentlichter Stand der Technik", level=1, concepts=["epc_stand_der_technik"], norms=["Art. 54 Abs. 2 EPÜ"]),
        *fallkette("e01n54-2", "Die ältere Anmeldung des Wettbewerbers",
            "B reicht am 10.1.2025 die europäische Anmeldung EP-B ein; die Beschreibung offenbart X, die Ansprüche betreffen Z. EP-B wird am "
            "10.7.2026 veröffentlicht. A reicht am 5.5.2025 ohne Priorität EP-A mit einem Anspruch auf X ein.",
            [frage("Ist EP-B Stand der Technik für EP-A?", True,
                   ["**Ja,** nach Art. 54 Abs. 3 EPÜ: EP-B wurde vor dem Anmeldetag von EP-A eingereicht und danach veröffentlicht. Maßgeblich ist der "
                    "**gesamte Inhalt** in der ursprünglich eingereichten Fassung, also auch die Beschreibung."],
                   merke="Art. 54 Abs. 3 EPÜ: ganzer Inhalt wie eingereicht, nicht nur die Ansprüche.", titel="Älteres Recht", step=_SDT + ".2.2"),
             frage("Kann EP-B auch gegen die erfinderische Tätigkeit von EP-A eingewandt werden?", False,
                   ["**Nein!** Ältere Rechte nach Art. 54 Abs. 3 EPÜ bleiben bei der erfinderischen Tätigkeit außer Betracht (Art. 56 Satz 2 EPÜ)."],
                   merke="Abs. 3 nur für die Neuheit.", titel="Erfinderische Tätigkeit", norms=["Art. 56 EPÜ"]),
             frage("Darf A die Neuheit mit einem in der Anmeldung nicht offenbarten Disclaimer wiederherstellen?", True,
                   ["**Ja!** Ein nicht offenbarter Disclaimer ist nach G 1/03 zulässig, um einen Anspruch gegenüber Stand der Technik nach "
                    "Art. 54 Abs. 3 EPÜ abzugrenzen; er darf nicht mehr ausschließen als nötig und keinen technischen Beitrag leisten (G 1/16)."],
                   merke="Gegen Art. 54 Abs. 3 EPÜ hilft der nicht offenbarte Disclaimer.", titel="Disclaimer", level=2,
                   norms=["Art. 123 Abs. 2 EPÜ"], cases=["epc_g_1_03", "epc_g_1_16"], concepts=["epc_disclaimer"], step=_SDT + ".3"),
             frage("Ist EP-B noch Stand der Technik, wenn B die Anmeldung so rechtzeitig zurücknimmt, dass sie nie veröffentlicht wird?", False,
                   ["**Nein!** Art. 54 Abs. 3 EPÜ verlangt, dass die ältere Anmeldung am oder nach dem Anmeldetag **veröffentlicht** wurde. Ohne "
                    "Veröffentlichung entsteht kein älteres Recht."],
                   merke="Keine Veröffentlichung, kein älteres Recht.", titel="Rücknahme vor Veröffentlichung",
                   abwandlung="B nimmt EP-B vor Abschluss der technischen Vorbereitungen für die Veröffentlichung zurück."),
            ],
            abschnitt="Abs. 3: ältere europäische Anmeldungen", level=1, concepts=["epc_aeltere_rechte"], norms=["Art. 54 Abs. 3 EPÜ"]),
        *fallkette("e01n54-3", "Die PCT-Anmeldung, die nie nach Europa kam",
            "C reicht am 1.2.2024 die internationale Anmeldung PCT-C ein, die X offenbart; sie wird am 1.8.2025 auf Englisch veröffentlicht. C "
            "nimmt keine Handlungen nach R. 159 EPÜ vor. A reicht am 1.3.2024 eine europäische Anmeldung mit einem Anspruch auf X ein.",
            [frage("Ist PCT-C Stand der Technik nach Art. 54 Abs. 3 EPÜ für die Anmeldung von A?", False,
                   ["**Nein!** Eine Euro-PCT-Anmeldung gilt nur dann als Stand der Technik nach Art. 54 Abs. 3 EPÜ, wenn die Anmeldegebühr gezahlt und "
                    "gegebenenfalls die Übersetzung eingereicht ist (Art. 153 Abs. 5 EPÜ, R. 165 EPÜ). C hat beides unterlassen."],
                   merke="Euro-PCT als älteres Recht nur mit Anmeldegebühr (R. 165 EPÜ).", titel="Euro-PCT als älteres Recht",
                   norms=["Art. 153 Abs. 5 EPÜ", "R. 165 EPÜ"], concepts=["epc_euro_pct"], step=_SDT + ".2.2"),
             frage("Ist die Veröffentlichung von PCT-C vom 1.8.2025 Stand der Technik nach Art. 54 Abs. 2 EPÜ?", False,
                   ["**Nein!** Sie erschien nach dem Anmeldetag von A (1.3.2024). Art. 54 Abs. 2 EPÜ erfasst nur, was **vor** dem maßgeblichen Tag "
                    "öffentlich zugänglich war."],
                   merke="Nach dem Stichtag veröffentlicht: nur über Abs. 3 relevant.", titel="Keine Vorveröffentlichung", step=_SDT + ".2.3"),
             frage("Ändert sich das, wenn C die Anmeldegebühr nach R. 159 Abs. 1 EPÜ zahlt?", True,
                   ["**Ja!** Mit der Anmeldegebühr (Übersetzung entbehrlich, da Englisch) sind die Voraussetzungen der R. 165 EPÜ erfüllt; PCT-C wird "
                    "rückwirkend zum älteren Recht nach Art. 54 Abs. 3 EPÜ gegen die Anmeldung von A."],
                   merke="Der Eintritt in die europäische Phase macht die PCT-Anmeldung zum älteren Recht.", titel="Abwandlung: Eintritt", level=2,
                   abwandlung="C leitet fristgerecht die europäische Phase ein und zahlt die Anmeldegebühr."),
            ],
            abschnitt="Abs. 3: Euro-PCT-Anmeldungen", level=2, concepts=["epc_aeltere_rechte", "epc_euro_pct"], norms=["Art. 54 Abs. 3 EPÜ"]),
        *fallkette("e01n54-4", "Das Dichtungsmaterial im Handel",
            "D verkauft seit 2020 ein Dichtungsmaterial für Solarmodule. Seine Zusammensetzung lässt sich mit den Mitteln vor dem Anmeldetag nicht "
            "vollständig analysieren und nicht nachbauen. E meldet 2023 genau diese Zusammensetzung an und meint, das Produkt gehöre nicht zum "
            "Stand der Technik.",
            [frage("Gehört das verkaufte Produkt zum Stand der Technik, obwohl es nicht reproduzierbar war?", True,
                   ["**Ja!** Ein vor dem Anmeldetag in Verkehr gebrachtes Erzeugnis kann nicht allein deshalb aus dem Stand der Technik ausgeschlossen "
                    "werden, weil der Fachmann seine Zusammensetzung nicht analysieren und reproduzieren konnte (G 1/23, Präzisierung von G 1/92)."],
                   merke="Verkauft ist öffentlich zugänglich – auch ohne Reproduzierbarkeit.", titel="In Verkehr gebrachtes Erzeugnis",
                   cases=["epc_g_1_23", "epc_g_1_92"]),
             frage("Gehören auch die öffentlich zugänglichen Datenblätter des Produkts zum Stand der Technik?", True,
                   ["**Ja!** Technische Informationen über das Erzeugnis, die vor dem Anmeldetag öffentlich zugänglich waren, sind Stand der Technik, "
                    "unabhängig davon, ob das Erzeugnis selbst analysierbar war (G 1/23)."],
                   merke="Auch Informationen über das Produkt zählen.", titel="Informationen über das Produkt", cases=["epc_g_1_23"]),
            ],
            abschnitt="Abs. 2: öffentliche Zugänglichkeit", level=2, concepts=["epc_stand_der_technik"], norms=["Art. 54 Abs. 2 EPÜ"]),
        *fallkette("e01n54-5", "Einmal wöchentlich statt täglich",
            "Der Wirkstoff W ist zur Behandlung der Krankheit K mit 10 mg täglich bekannt. F entdeckt, dass 50 mg einmal wöchentlich bei K "
            "besser verträglich sind, und will das schützen lassen.",
            [frage("Kann F einen Anspruch auf W zur Verwendung bei K mit der neuen Dosierung erhalten, obwohl Wirkstoff und Krankheit bekannt sind?", True,
                   ["**Ja!** Art. 54 Abs. 5 EPÜ schließt den Schutz eines bekannten Arzneimittels für eine **andere therapeutische Behandlung derselben "
                    "Krankheit** nicht aus; die Neuheit kann allein in einer Dosierungsanleitung liegen (G 2/08)."],
                   merke="Neue Dosierung kann eine weitere medizinische Indikation sein.", titel="Weitere Indikation",
                   cases=["epc_g_2_08"], concepts=["epc_medizinische_indikation"]),
             frage("Darf F den Anspruch im schweizerischen Format („Verwendung von W zur Herstellung eines Arzneimittels zur Behandlung von K“) fassen?", False,
                   ["**Nein!** Wird die Neuheit nur durch die neue therapeutische Verwendung begründet, ist das schweizerische Anspruchsformat seit "
                    "G 2/08 nicht mehr zulässig; richtig ist der zweckgebundene Stoffanspruch „W zur Verwendung bei …“ (Art. 54 Abs. 5 EPÜ)."],
                   merke="Zweckgebundener Stoffanspruch statt Swiss-type.", titel="Anspruchsformat", level=2, cases=["epc_g_2_08"]),
            ],
            abschnitt="Abs. 4, 5: medizinische Indikationen", level=2, concepts=["epc_medizinische_indikation"],
            norms=["Art. 54 Abs. 4 EPÜ", "Art. 54 Abs. 5 EPÜ"]),
    ]),
    # ================================================================== Art. 121 EPÜ, R. 135 EPÜ
    dict(id="e01n121", order=12100, titel="Art. 121 EPÜ, R. 135 EPÜ: Weiterbehandlung", einheiten=[
        intro("e01n121-0", "Der Standardbehelf bei versäumten Fristen",
              "Hat der Anmelder eine Frist gegenüber dem EPA versäumt, ist die **Weiterbehandlung** der erste Gedanke: Gebühr zahlen und versäumte "
              "Handlung nachholen, binnen **zwei Monaten nach der Mitteilung** über den Rechtsverlust (R. 135 Abs. 1 EPÜ); ein Verschulden ist "
              "nicht zu prüfen. Paper D fragt vor allem die **Ausschlüsse** ab: Art. 121 Abs. 4 EPÜ (Priorität, Beschwerde, Überprüfung, die "
              "Behelfsfristen selbst) und die Liste der R. 135 Abs. 2 EPÜ. Dort hilft nur die Wiedereinsetzung (Art. 122 EPÜ).",
              concepts=["epc_weiterbehandlung", "epc_wiedereinsetzung", "epc_rechtsverlust"],
              norms=["Art. 121 EPÜ", "R. 135 EPÜ"], distinctions=["d_epc_weiterbehandlung_wiedereinsetzung"], abschnitt="Überblick"),
        schema("e01n121-0s", "Prüfungsschema versäumte Frist", "epc_schema_fristversaeumnis", abschnitt="Überblick"),
        *fallkette("e01n121-1", "Der liegengebliebene Bescheid",
            "Die Prüfungsabteilung erlässt am 10.2.2026 einen Bescheid nach Art. 94 Abs. 3 EPÜ mit einer Frist von vier Monaten. Der Anmelder G "
            "antwortet nicht. Das EPA erlässt eine vom 15.7.2026 datierte Mitteilung nach R. 112 Abs. 1 EPÜ, die Anmeldung gelte als zurückgenommen.",
            [frage("Kann G Weiterbehandlung beantragen?", True,
                   ["**Ja!** Die Frist zur Erwiderung auf einen Bescheid ist eine Frist gegenüber dem EPA (Art. 94 Abs. 4 EPÜ) und weder in "
                    "Art. 121 Abs. 4 EPÜ noch in R. 135 Abs. 2 EPÜ ausgeschlossen."],
                   merke="Bescheidsfristen sind weiterbehandlungsfähig.", titel="Statthaftigkeit", norms=["Art. 94 Abs. 4 EPÜ"], step=_FV + ".3.1"),
             frage("Bis wann muss G den Antrag stellen?", 1,
                   ["**Bis 15.9.2026.** Die Frist beträgt zwei Monate nach der Mitteilung über den Rechtsverlust (R. 135 Abs. 1 EPÜ). Die Mitteilung gilt "
                    "als am 15.7.2026 zugestellt (R. 126 Abs. 2 EPÜ); die Frist endet am Tag mit derselben Zahl (R. 131 Abs. 4 EPÜ)."],
                   optionen=["10.8.2026", "15.9.2026", "25.9.2026", "15.10.2026"], merke="Zwei Monate ab Mitteilung, ohne Zehn-Tage-Zuschlag.",
                   titel="Antragsfrist", norms=["R. 135 Abs. 1 EPÜ", "R. 131 Abs. 4 EPÜ", "R. 126 Abs. 2 EPÜ"], concepts=["epc_fristen"], step=_FV + ".3.2", level=2),
             frage("Genügt es, innerhalb der Frist nur die Weiterbehandlungsgebühr zu zahlen und die Erwiderung später einzureichen?", False,
                   ["**Nein!** Die versäumte Handlung ist innerhalb der Antragsfrist nachzuholen (R. 135 Abs. 1 Satz 2 EPÜ). Fehlt die Erwiderung bei "
                    "Fristablauf, ist der Antrag unzulässig."],
                   merke="Gebühr und versäumte Handlung – beides in der Frist.", titel="Nachholen der Handlung", step=_FV + ".3.3"),
            ],
            abschnitt="Abs. 1: Voraussetzungen", level=1, concepts=["epc_weiterbehandlung"], norms=["Art. 121 Abs. 1 EPÜ", "R. 135 Abs. 1 EPÜ"]),
        *fallkette("e01n121-2", "Zwei Tage zu spät",
            "H reicht am 3.3.2025 eine US-Anmeldung ein. Wegen eines Kalenderfehlers reicht er die europäische Nachanmeldung erst am 5.3.2026 ein "
            "und beansprucht die US-Priorität.",
            [frage("Kann H die Prioritätsfrist mit der Weiterbehandlung retten?", False,
                   ["**Nein!** Die Frist des Art. 87 Abs. 1 EPÜ ist von der Weiterbehandlung ausdrücklich ausgeschlossen (Art. 121 Abs. 4 EPÜ)."],
                   merke="Prioritätsfrist: keine Weiterbehandlung.", titel="Ausschluss nach Art. 121 Abs. 4 EPÜ", norms=["Art. 121 Abs. 4 EPÜ", "Art. 87 Abs. 1 EPÜ"],
                   step=_FV + ".3.1"),
             frage("Bleibt H ein anderer Weg?", True,
                   ["**Ja,** die Wiedereinsetzung in die Prioritätsfrist: Antrag binnen zwei Monaten nach deren Ablauf, wegen des Sonntags bis 4.5.2026 "
                    "(R. 134 Abs. 1 EPÜ), mit Gebühr und Begründung (R. 136 Abs. 1 EPÜ). Begründet ist er nur, wenn H trotz aller gebotenen Sorgfalt verhindert war (Art. 122 Abs. 1 EPÜ)."],
                   merke="Priorität verpasst: Wiedereinsetzung binnen zwei Monaten nach Fristablauf.", titel="Wiedereinsetzung",
                   norms=["Art. 122 Abs. 1 EPÜ", "R. 136 Abs. 1 EPÜ"], concepts=["epc_wiedereinsetzung", "epc_prioritaet"], step=_FV + ".4.2", level=2),
            ],
            abschnitt="Art. 121 Abs. 4 EPÜ: ausgeschlossene Fristen", level=1, concepts=["epc_weiterbehandlung"], norms=["Art. 121 Abs. 4 EPÜ"]),
        *fallkette("e01n121-3", "Die vergessene Jahresgebühr",
            "Die Jahresgebühr für das dritte Jahr der Anmeldung von J war am 31.1.2026 fällig. J zahlt weder sie noch die Zuschlagsgebühr bis zum "
            "31.7.2026. Das EPA teilt ihm danach mit, die Anmeldung gelte als zurückgenommen.",
            [frage("Kann J Weiterbehandlung beantragen?", False,
                   ["**Nein!** Die Nachfrist für Jahresgebühren mit Zuschlag (R. 51 Abs. 2 EPÜ) gehört zu den in R. 135 Abs. 2 EPÜ ausgeschlossenen Fristen."],
                   merke="Jahresgebühren: keine Weiterbehandlung.", titel="Ausschluss nach R. 135 Abs. 2 EPÜ", norms=["R. 135 Abs. 2 EPÜ", "R. 51 Abs. 2 EPÜ"],
                   concepts=["epc_jahresgebuehren"], step=_FV + ".3.1"),
             frage("Kann J während der laufenden Wiedereinsetzungsfrist noch eine Teilanmeldung einreichen?", False,
                   ["**Nein!** Eine als zurückgenommen geltende Anmeldung ist während der Frist für den Wiedereinsetzungsantrag nicht anhängig "
                    "(J 4/11); erst eine erfolgreiche Wiedereinsetzung stellt die Anhängigkeit wieder her (R. 36 Abs. 1 EPÜ)."],
                   merke="Keine Teilanmeldung aus einer erloschenen Anmeldung.", titel="Teilanmeldung", level=3,
                   norms=["R. 36 Abs. 1 EPÜ"], cases=["epc_j_4_11"], concepts=["epc_anhaengigkeit"], step=_FV + ".5"),
            ],
            abschnitt="R. 135 Abs. 2 EPÜ: ausgeschlossene Fristen", level=2, concepts=["epc_weiterbehandlung", "epc_jahresgebuehren"], norms=["R. 135 Abs. 2 EPÜ"]),
        *fallkette("e01n121-4", "Die Erteilungsgebühr",
            "K erhält die Mitteilung nach R. 71 Abs. 3 EPÜ, versäumt aber die Frist von vier Monaten für die Erteilungsgebühr und die Übersetzung "
            "der Ansprüche. Das EPA teilt mit, die Anmeldung gelte als zurückgenommen (R. 71 Abs. 7 EPÜ).",
            [frage("Kann K Weiterbehandlung beantragen?", True,
                   ["**Ja!** Die Frist nach R. 71 Abs. 3 EPÜ ist nicht ausgeschlossen. K zahlt binnen zwei Monaten nach der Mitteilung die "
                    "Weiterbehandlungsgebühr und holt Erteilungsgebühr und Übersetzung nach (R. 135 Abs. 1 EPÜ)."],
                   merke="R. 71 Abs. 3 EPÜ: Weiterbehandlung möglich.", titel="Statthaftigkeit", norms=["R. 71 Abs. 3 EPÜ", "R. 71 Abs. 7 EPÜ"],
                   concepts=["epc_erteilung"], step=_FV + ".3.1"),
             frage("Kann K mit der Weiterbehandlung zugleich Änderungen der Ansprüche einreichen?", True,
                   ["**Ja,** als versäumte Handlung gilt dann der Änderungs- oder Berichtigungsantrag nach R. 71 Abs. 6 EPÜ; die Prüfungsabteilung "
                    "erlässt bei Zustimmung eine neue Mitteilung nach R. 71 Abs. 3 EPÜ, sonst nimmt sie die Prüfung wieder auf (Richtlinien C-V, 3)."],
                   merke="Auch mit der Weiterbehandlung kann man noch ändern.", titel="Änderungen", level=3,
                   norms=["R. 71 Abs. 6 EPÜ"], concepts=["epc_erteilung"]),
            ],
            abschnitt="Abs. 1: Voraussetzungen", level=2, concepts=["epc_weiterbehandlung"], norms=["Art. 121 Abs. 1 EPÜ", "R. 135 Abs. 1 EPÜ"]),
    ]),
]
