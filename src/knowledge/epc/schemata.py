# -*- coding: utf-8 -*-
"""Prüfungsschemata zum Verfahren vor dem EPA (Paper D). Schritt-IDs: step:<schema>.<n>.<m> (Kurse verweisen darauf)."""
from ..schemata import step

K = "EPÜ: Fristen und Rechtsbehelfe"

SCHEMATA = [
    dict(
        id="epc_schema_fristversaeumnis", label="Versäumte Frist vor dem EPA: Rechtsfolge und Rechtsbehelf", kategorie=K,
        beschreibung="Das Grundraster fast jeder Paper-D-Frage: Frist berechnen, Rechtsfolge feststellen, dann in fester Reihenfolge prüfen, ob "
                     "Weiterbehandlung möglich ist, sonst Wiedereinsetzung, und ob andere Wege (Entscheidung nach R. 112 Abs. 2 EPÜ, "
                     "Fristverlängerung, Vertrauensschutz, neue Anmeldung) helfen.",
        norms=["Art. 120 EPÜ", "Art. 121 EPÜ", "Art. 122 EPÜ", "R. 131 EPÜ", "R. 135 EPÜ", "R. 136 EPÜ"],
        steps=[
            step("1. Frist bestimmen (Art. 120 EPÜ, R. 131 EPÜ)", children=[
                step("1. Auslösendes Ereignis und Dauer", "Zustellung (R. 126 Abs. 2 EPÜ, R. 127 Abs. 2 EPÜ: Datum des Schriftstücks), Anmelde- oder "
                     "Prioritätstag, Hinweis im Patentblatt; Dauer aus Übereinkommen, Ausführungsordnung oder Bescheid.",
                     concepts=["epc_fristen", "epc_zustellung"], norms=["R. 131 Abs. 2 EPÜ", "R. 126 Abs. 2 EPÜ"]),
                step("2. Fristende berechnen (R. 131 Abs. 4 EPÜ)", "Monatsfrist endet am Tag mit derselben Zahl, sonst am Monatsletzten; Ketten "
                     "von Fristen jeweils vom ursprünglichen Ereignis rechnen.", concepts=["epc_fristen"], norms=["R. 131 Abs. 4 EPÜ"]),
                step("3. Verlängerung (R. 134 EPÜ)", "Annahmestelle geschlossen oder elektronische Einreichung nicht verfügbar: nächster Tag, an dem alle "
                     "Annahmestellen offen sind (R. 134 Abs. 1 EPÜ); allgemeine Störung der Post (R. 134 Abs. 2 EPÜ); außerordentliches Ereignis in den "
                     "letzten zehn Tagen (R. 134 Abs. 5 EPÜ).", concepts=["epc_fristen"], norms=["R. 134 EPÜ"], cases=["epc_j_10_20"]),
            ]),
            step("2. Rechtsfolge der Versäumung", "Rücknahmefiktion (z. B. Art. 86 Abs. 1, Art. 94 Abs. 4 EPÜ, R. 71 Abs. 7 EPÜ), Verlust eines Rechts "
                 "(Priorität R. 53 Abs. 3 EPÜ), Schriftstück gilt als nicht eingereicht; Mitteilung nach R. 112 Abs. 1 EPÜ.",
                 concepts=["epc_rechtsverlust"], norms=["R. 112 Abs. 1 EPÜ"]),
            step("3. Weiterbehandlung (Art. 121 EPÜ, R. 135 EPÜ)", children=[
                step("1. Statthaft?", "Frist gegenüber dem EPA, versäumt vom Anmelder; nicht ausgeschlossen nach Art. 121 Abs. 4 EPÜ oder R. 135 Abs. 2 EPÜ.",
                     concepts=["epc_weiterbehandlung"], norms=["Art. 121 Abs. 4 EPÜ", "R. 135 Abs. 2 EPÜ"]),
                step("2. Frist: zwei Monate nach der Mitteilung (R. 135 Abs. 1 EPÜ)", "Mitteilung über die Fristversäumung oder den Rechtsverlust; "
                     "Fristende nach R. 131 EPÜ berechnen.", concepts=["epc_weiterbehandlung"], norms=["R. 135 Abs. 1 EPÜ"]),
                step("3. Gebühr zahlen und versäumte Handlung nachholen", "Der Antrag gilt erst mit Zahlung als gestellt; ohne nachgeholte Handlung "
                     "ist er unzulässig. Kein Verschulden zu prüfen.", concepts=["epc_weiterbehandlung"], norms=["R. 135 Abs. 1 EPÜ"]),
            ]),
            step("4. Wiedereinsetzung (Art. 122 EPÜ, R. 136 EPÜ)", children=[
                step("1. Statthaft?", "Nur wenn keine Weiterbehandlung möglich ist (R. 136 Abs. 3 EPÜ); unmittelbarer Rechtsverlust; Anmelder, Inhaber, "
                     "ausnahmsweise Einsprechender (G 1/86).", concepts=["epc_wiedereinsetzung"], norms=["R. 136 Abs. 3 EPÜ", "Art. 122 Abs. 1 EPÜ"], cases=["epc_g_1_86"]),
                step("2. Frist (R. 136 Abs. 1 EPÜ)", "Zwei Monate nach Wegfall des Hindernisses, spätestens ein Jahr nach Ablauf der versäumten Frist; "
                     "Prioritätsfrist und Überprüfungsfrist: zwei Monate nach deren Ablauf.", concepts=["epc_wiedereinsetzung"], norms=["R. 136 Abs. 1 EPÜ"]),
                step("3. Form: Antrag, Gebühr, Begründung, Handlung nachholen (R. 136 Abs. 1, 2 EPÜ)", "Alle Gründe und Beweismittel sofort (J 6/22).",
                     concepts=["epc_wiedereinsetzung"], norms=["R. 136 Abs. 2 EPÜ"], cases=["epc_j_6_22"]),
                step("4. Begründet: alle gebotene Sorgfalt", "Isoliertes Versehen in einem sonst funktionierenden Fristensystem; Sorgfalt von Anmelder, "
                     "Vertreter und Hilfspersonen (J 5/80).", concepts=["epc_wiedereinsetzung"], norms=["Art. 122 Abs. 1 EPÜ"], cases=["epc_j_5_80"]),
            ]),
            step("5. Andere Wege", "Beschwerdefähige Entscheidung beantragen, wenn der Rechtsverlust bestritten wird (R. 112 Abs. 2 EPÜ); Teilanmeldung, "
                 "solange die Anmeldung anhängig ist; neue Anmeldung (ohne Priorität, wenn deren Frist abgelaufen ist); Vertrauensschutz.",
                 concepts=["epc_rechtsverlust", "epc_teilanmeldung", "epc_vertrauensschutz"], norms=["R. 112 Abs. 2 EPÜ", "R. 36 Abs. 1 EPÜ"]),
        ]),
    dict(
        id="epc_schema_stand_der_technik", label="Neuheit in Paper D: wirksamer Tag und Stand der Technik", kategorie="EPÜ: Stand der Technik und Patentierbarkeit",
        beschreibung="Für jeden Anspruch zuerst den wirksamen Tag bestimmen (Priorität, Teilpriorität), dann jedes Dokument einordnen: Art. 54 Abs. 2 "
                     "oder Abs. 3 EPÜ oder gar kein Stand der Technik, schließlich Abhilfen prüfen.",
        norms=["Art. 54 EPÜ", "Art. 55 EPÜ", "Art. 87 EPÜ", "Art. 89 EPÜ"],
        steps=[
            step("1. Wirksamer Tag je Anspruch (Art. 89 EPÜ)", children=[
                step("1. Prioritätsvoraussetzungen", "Erste Anmeldung (Art. 87 Abs. 4 EPÜ), PVÜ-/WTO-Staat, Frist zwölf Monate, dieselbe Erfindung (G 2/98), "
                     "Berechtigung (G 1/22), Erklärung (R. 52 EPÜ).", concepts=["epc_prioritaet"], norms=["Art. 87 Abs. 1 EPÜ", "Art. 87 Abs. 4 EPÜ", "R. 52 EPÜ"],
                     cases=["epc_g_2_98", "epc_g_1_22"]),
                step("2. Teilpriorität (Art. 88 Abs. 3 EPÜ, G 1/15)", "Generische Ansprüche aufspalten: offenbarter Teil am Prioritätstag, Rest am Anmeldetag.",
                     concepts=["epc_teilprioritaet"], norms=["Art. 88 Abs. 3 EPÜ"], cases=["epc_g_1_15"]),
            ]),
            step("2. Dokumente einordnen", children=[
                step("1. Art. 54 Abs. 2 EPÜ", "Vor dem wirksamen Tag öffentlich zugänglich, gleich wo und in welcher Sprache; auch eigene Veröffentlichungen.",
                     concepts=["epc_stand_der_technik"], norms=["Art. 54 Abs. 2 EPÜ"], cases=["epc_g_1_92", "epc_g_3_93"]),
                step("2. Art. 54 Abs. 3 EPÜ", "Ältere europäische (oder Euro-PCT nach R. 165 EPÜ) Anmeldung, früherer wirksamer Tag, Veröffentlichung am oder nach dem "
                     "maßgeblichen Tag; nur Neuheit.", concepts=["epc_aeltere_rechte"], norms=["Art. 54 Abs. 3 EPÜ", "R. 165 EPÜ"]),
                step("3. Kein Stand der Technik", "Nach dem wirksamen Tag veröffentlicht und nicht Art. 54 Abs. 3 EPÜ; nationale ältere Rechte (Art. 139 Abs. 2 EPÜ); "
                     "unschädliche Offenbarung (Art. 55 EPÜ).", concepts=["epc_unschaedliche_offenbarung"], norms=["Art. 55 EPÜ", "Art. 139 Abs. 2 EPÜ"]),
            ]),
            step("3. Abhilfen", "Disclaimer gegen Art. 54 Abs. 3 EPÜ (G 1/03), Teilanmeldung oder Beschränkung auf den prioritätsberechtigten Teil, "
                 "Wiedereinsetzung in die Prioritätsfrist, Einspruch gegen das ältere Patent.",
                 concepts=["epc_disclaimer", "epc_teilanmeldung"], norms=["Art. 123 Abs. 2 EPÜ"], cases=["epc_g_1_03"]),
        ]),
    dict(
        id="epc_schema_einspruch", label="Einspruch: Zulässigkeit und Begründetheit (Art. 99 bis 101 EPÜ)", kategorie="EPÜ: Einspruch, Beschränkung, Beschwerde",
        beschreibung="Zulässigkeit in der Reihenfolge der Mängelprüfung nach R. 77 EPÜ, dann die Begründetheit; daneben Beitritt und Fortsetzung von Amts wegen.",
        norms=["Art. 99 EPÜ", "Art. 100 EPÜ", "Art. 101 EPÜ", "R. 76 EPÜ", "R. 77 EPÜ"],
        steps=[
            step("1. Statthaftigkeit", "Erteiltes europäisches Patent; auch nach Verzicht oder Erlöschen (R. 75 EPÜ); kein anhängiges Beschränkungsverfahren hindert.",
                 concepts=["epc_einspruch"], norms=["Art. 99 Abs. 1 EPÜ", "R. 75 EPÜ"]),
            step("2. Einsprechender", "Jeder Dritte, auch Strohmann (G 3/97), nicht der Inhaber (G 9/93); mehrere gemeinsam mit einer Gebühr (G 3/99); "
                 "Vertretung nach Art. 133 Abs. 2 EPÜ.", concepts=["epc_einspruch", "epc_vertretung"], norms=["Art. 99 Abs. 1 EPÜ", "Art. 133 Abs. 2 EPÜ"],
                 cases=["epc_g_3_97", "epc_g_9_93", "epc_g_3_99"]),
            step("3. Frist und Gebühr (Art. 99 Abs. 1 EPÜ)", "Neun Monate nach dem Hinweis auf die Erteilung; Gebühr in derselben Frist, sonst gilt der Einspruch "
                 "als nicht eingelegt; keine Weiterbehandlung (kein Anmelder), keine Wiedereinsetzung für den Einsprechenden.",
                 concepts=["epc_einspruch"], norms=["Art. 99 Abs. 1 EPÜ"]),
            step("4. Inhalt (R. 76 Abs. 2 EPÜ)", "Angaben zum Einsprechenden, zum Patent, Umfang, Gründe, Tatsachen und Beweismittel; Mängel nach R. 77 EPÜ "
                 "teils nur binnen der Einspruchsfrist behebbar.", concepts=["epc_einspruch"], norms=["R. 76 Abs. 2 EPÜ", "R. 77 EPÜ"], cases=["epc_g_9_91"]),
            step("5. Begründetheit (Art. 100, 101 EPÜ)", "Nur die Gründe des Art. 100 EPÜ; Prüfungsumfang G 9/91, G 10/91; geänderte Ansprüche: Art. 84 EPÜ nur "
                 "soweit durch die Änderung (G 3/14), Art. 123 Abs. 2, 3 EPÜ.", concepts=["epc_einspruchsgruende"], norms=["Art. 100 EPÜ", "Art. 101 Abs. 3 EPÜ"],
                 cases=["epc_g_10_91", "epc_g_3_14"]),
            step("6. Beitritt und Fortsetzung", "Beitritt des vermeintlichen Verletzers binnen drei Monaten (Art. 105 EPÜ, R. 89 EPÜ); Fortsetzung von Amts wegen "
                 "nach Rücknahme oder Tod (R. 84 EPÜ).", concepts=["epc_beitritt", "epc_einsprechendenstellung"], norms=["Art. 105 EPÜ", "R. 84 EPÜ"], cases=["epc_g_2_24"]),
        ]),
    dict(
        id="epc_schema_beschwerde", label="Beschwerde: Zulässigkeit (Art. 106 bis 108 EPÜ)", kategorie="EPÜ: Einspruch, Beschränkung, Beschwerde",
        beschreibung="Prüfung der Zulässigkeit einer Beschwerde in der Reihenfolge der R. 101 EPÜ, mit Abhilfe und Rückzahlung der Gebühr.",
        norms=["Art. 106 EPÜ", "Art. 107 EPÜ", "Art. 108 EPÜ", "R. 99 EPÜ", "R. 101 EPÜ"],
        steps=[
            step("1. Beschwerdefähige Entscheidung (Art. 106 EPÜ)", "Entscheidung der Eingangsstelle, Prüfungs-, Einspruchs- oder Rechtsabteilung; "
                 "Zwischenentscheidungen nur zusammen mit der Endentscheidung, außer die Beschwerde ist gesondert zugelassen (Art. 106 Abs. 2 EPÜ).",
                 concepts=["epc_beschwerde"], norms=["Art. 106 EPÜ"]),
            step("2. Beschwerdeberechtigung (Art. 107 EPÜ)", "Beteiligter, der beschwert ist; übrige Beteiligte sind am Verfahren beteiligt. Der Beitretende "
                 "der Beschwerdeinstanz ist kein Beschwerdeführer (G 2/24).", concepts=["epc_beschwerde"], norms=["Art. 107 EPÜ"], cases=["epc_g_2_24"]),
            step("3. Frist und Gebühr (Art. 108 Satz 1, 2 EPÜ)", "Zwei Monate nach Zustellung; beides fristgerecht, sonst gilt die Beschwerde als nicht "
                 "eingelegt (G 1/18).", concepts=["epc_beschwerde"], norms=["Art. 108 EPÜ"], cases=["epc_g_1_18"]),
            step("4. Form und Begründung (R. 99 EPÜ, Art. 108 Satz 3 EPÜ)", "Name und Anschrift des Beschwerdeführers (Berichtigung R. 101 Abs. 2 EPÜ, G 1/12), "
                 "angefochtene Entscheidung, Antrag; Begründung binnen vier Monaten.", concepts=["epc_beschwerde"], norms=["R. 99 EPÜ", "R. 101 EPÜ"],
                 cases=["epc_g_1_12"]),
            step("5. Abhilfe und Rückzahlung (Art. 109 EPÜ, R. 103 EPÜ)", "Abhilfe nur im einseitigen Verfahren; Rückzahlung der Beschwerdegebühr nach R. 103 EPÜ "
                 "(Zuständigkeit G 3/03).", concepts=["epc_beschwerde"], norms=["Art. 109 EPÜ", "R. 103 EPÜ"], cases=["epc_g_3_03"]),
        ]),
    dict(
        id="epc_schema_euro_pct", label="Euro-PCT: Eintritt in die europäische Phase (R. 159 EPÜ)", kategorie="EPÜ: Euro-PCT und PCT",
        beschreibung="Die 31-Monatsfrist und die Handlungen der R. 159 Abs. 1 EPÜ, die Folgen ihrer Versäumung und das Verfahren nach dem Eintritt.",
        norms=["Art. 153 EPÜ", "R. 159 EPÜ", "R. 160 EPÜ", "R. 161 EPÜ", "R. 164 EPÜ"],
        steps=[
            step("1. Frist: 31 Monate ab Anmelde- oder frühestem Prioritätstag (R. 159 Abs. 1 EPÜ)", "Fristberechnung nach R. 131 EPÜ; vorzeitige Bearbeitung "
                 "auf ausdrücklichen Antrag (Art. 23 Abs. 2 PCT).", concepts=["epc_euro_pct"], norms=["R. 159 Abs. 1 EPÜ"]),
            step("2. Handlungen (R. 159 Abs. 1 lit. a bis h EPÜ)", "Übersetzung, Unterlagen angeben, Anmeldegebühr, Benennungsgebühr, Recherchengebühr, "
                 "Prüfungsantrag, Jahresgebühr für das dritte Jahr, Ausstellungsbescheinigung.", concepts=["epc_euro_pct"], norms=["R. 159 Abs. 1 EPÜ"], cases=["epc_g_4_08"]),
            step("3. Versäumung (R. 160 EPÜ)", "Rücknahmefiktion bzw. Benennung als zurückgenommen; Mitteilung nach R. 112 Abs. 1 EPÜ, dann Weiterbehandlung; "
                 "Übersetzung fehlt: ebenfalls Weiterbehandlung.", concepts=["epc_euro_pct", "epc_weiterbehandlung"], norms=["R. 160 EPÜ", "Art. 121 EPÜ"]),
            step("4. Nach dem Eintritt", "Aufforderung nach R. 161 EPÜ (Stellungnahme/Änderungen binnen sechs Monaten), Anspruchsgebühren R. 162 EPÜ, "
                 "Uneinheitlichkeit R. 164 EPÜ, Stand der Technik nach Art. 54 Abs. 3 EPÜ über R. 165 EPÜ.",
                 concepts=["epc_euro_pct", "epc_einheitlichkeit"], norms=["R. 161 EPÜ", "R. 162 EPÜ", "R. 164 EPÜ", "R. 165 EPÜ"]),
        ]),
    dict(
        id="epc_schema_teilanmeldung", label="Teilanmeldung: Voraussetzungen und Gebühren (Art. 76 EPÜ, R. 36 EPÜ)", kategorie="EPÜ: Anmeldung, Anmeldetag, Priorität, Änderungen",
        beschreibung="Wann eine Teilanmeldung noch möglich ist, wo und in welcher Sprache sie einzureichen ist, welchen Inhalt sie haben darf und welche Gebühren anfallen.",
        norms=["Art. 76 EPÜ", "R. 36 EPÜ"],
        steps=[
            step("1. Anhängige Stammanmeldung (R. 36 Abs. 1 EPÜ)", "Bis zum Tag vor dem Hinweis auf die Erteilung; nach Zurückweisung bis zum Ablauf der "
                 "Beschwerdefrist (G 1/09); nicht während der Wiedereinsetzungsfrist nach Rechtsverlust (J 4/11); Euro-PCT erst nach Eintritt (J 18/09).",
                 concepts=["epc_anhaengigkeit"], norms=["R. 36 Abs. 1 EPÜ"], cases=["epc_g_1_09", "epc_j_4_11", "epc_j_18_09"]),
            step("2. Anmelder, Ort, Sprache (R. 36 Abs. 2 EPÜ)", "Anmelder der Stammanmeldung; Einreichung beim EPA in München, Den Haag oder Berlin; "
                 "Verfahrenssprache der Stammanmeldung bzw. deren Originalsprache mit Übersetzung.", concepts=["epc_teilanmeldung"], norms=["R. 36 Abs. 2 EPÜ"]),
            step("3. Inhalt (Art. 76 Abs. 1 EPÜ)", "Nicht über die Stammanmeldung hinaus (G 1/05); bei Ketten über keine Vorgängerin hinaus (G 1/06); keine "
                 "Doppelpatentierung (G 4/19).", concepts=["epc_teilanmeldung", "epc_unzulaessige_erweiterung"], norms=["Art. 76 Abs. 1 EPÜ"],
                 cases=["epc_g_1_05", "epc_g_1_06", "epc_g_4_19"]),
            step("4. Gebühren", "Anmelde- und Recherchengebühr binnen eines Monats (R. 36 Abs. 3 EPÜ), Benennungsgebühr nach R. 36 Abs. 4 EPÜ, "
                 "rückständige Jahresgebühren binnen vier Monaten (R. 51 Abs. 3 EPÜ).", concepts=["epc_teilanmeldung", "epc_jahresgebuehren"],
                 norms=["R. 36 Abs. 3 EPÜ", "R. 36 Abs. 4 EPÜ", "R. 51 Abs. 3 EPÜ"]),
        ]),
]
