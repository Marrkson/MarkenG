# -*- coding: utf-8 -*-
"""Begriffe zum EPÜ (Verfahren vor dem EPA). Felder wie knowledge/concepts.py; `norms` in der Zitierweise `Art. 54 Abs. 3 EPÜ`,
`R. 71 Abs. 3 EPÜ`; `quellen` verweisen auf Abschnitte der Richtlinien für die Prüfung (`epagl:e_viii_2`, quellen.py).
Gebührenordnung (`Art. 14 Abs. 1 GebO`) und PCT (`R. 80.2 PCT`) nur im Fließtext, sie sind keine Graphknoten."""


def c(id, label, kategorie, definition, erlaeuterung, norms=(), cases=(), related=(), gl=()):
    return dict(id=id, label=label, kategorie=kategorie, definition=definition, erlaeuterung=erlaeuterung,
                norms=list(norms), cases=list(cases), ipwiki=[], related=list(related), quellen=["epagl:" + g for g in gl])


S, A, E, F, B, P, G = ("EPÜ: Stand der Technik und Patentierbarkeit", "EPÜ: Anmeldung, Anmeldetag, Priorität, Änderungen",
                       "EPÜ: Recherche, Prüfung und Erteilung", "EPÜ: Fristen und Rechtsbehelfe", "EPÜ: Einspruch, Beschränkung, Beschwerde",
                       "EPÜ: Euro-PCT und PCT", "EPÜ: Sprachen, Gebühren, Vertretung")

CONCEPTS = [
    # ------------------------------------------------------------------ Stand der Technik
    c("epc_stand_der_technik", "Stand der Technik (Art. 54 Abs. 2 EPÜ)", S,
      "Den Stand der Technik bildet alles, was vor dem Anmeldetag (bei wirksamer Priorität: dem Prioritätstag, Art. 89 EPÜ) der Öffentlichkeit "
      "durch schriftliche oder mündliche Beschreibung, durch Benutzung oder in sonstiger Weise zugänglich gemacht worden ist (Art. 54 Abs. 2 EPÜ).",
      "Öffentlich ist, was ein nicht zur Geheimhaltung verpflichteter Dritter zur Kenntnis nehmen konnte. In Verkehr gebrachte Erzeugnisse gehören "
      "mit ihrer Zusammensetzung zum Stand der Technik (G 1/92), auch wenn sie nicht analysierbar sind (G 1/23). Veröffentlichungen im "
      "Prioritätsintervall schaden, soweit die Priorität unwirksam ist (G 3/93). Klausurtechnik: für jeden Anspruch den wirksamen Tag bestimmen, "
      "dann jedes Dokument einordnen (Art. 54 Abs. 2 EPÜ, Art. 54 Abs. 3 EPÜ oder gar nicht).",
      norms=["Art. 54 Abs. 2 EPÜ", "Art. 89 EPÜ"], cases=["epc_g_1_92", "epc_g_1_23", "epc_g_3_93"],
      related=["epc_aeltere_rechte", "epc_prioritaet", "epc_unschaedliche_offenbarung"], gl=["g_iv_1", "g_iv_3"]),
    c("epc_aeltere_rechte", "Ältere europäische Anmeldungen (Art. 54 Abs. 3 EPÜ)", S,
      "Als Stand der Technik gilt auch der Inhalt europäischer Anmeldungen in der ursprünglich eingereichten Fassung, deren Anmeldetag (oder "
      "wirksamer Prioritätstag) vor dem maßgeblichen Tag liegt und die an oder nach diesem Tag veröffentlicht werden (Art. 54 Abs. 3 EPÜ).",
      "Nur für die Neuheit, nie für die erfinderische Tätigkeit (Art. 56 Satz 2 EPÜ). Maßgeblich ist der Gesamtinhalt der Anmeldung, nicht die "
      "Ansprüche; die spätere Rücknahme schadet nicht, wenn die Veröffentlichung erfolgt ist. Seit dem EPÜ 2000 kommt es nicht mehr auf "
      "gemeinsam benannte Staaten an. Euro-PCT-Anmeldungen zählen nur, wenn Anmeldegebühr und gegebenenfalls Übersetzung vorliegen "
      "(Art. 153 Abs. 5 EPÜ, R. 165 EPÜ). Nationale ältere Rechte sind kein Stand der Technik im Verfahren vor dem EPA (Art. 139 Abs. 2 EPÜ). "
      "Abgrenzung durch Disclaimer (G 1/03) möglich.",
      norms=["Art. 54 Abs. 3 EPÜ", "Art. 56 EPÜ", "Art. 153 Abs. 5 EPÜ", "R. 165 EPÜ"], cases=["epc_g_1_03"],
      related=["epc_stand_der_technik", "epc_disclaimer", "epc_euro_pct"], gl=["g_iv_5", "g_iv_5_1", "g_iv_5_2"]),
    c("epc_unschaedliche_offenbarung", "Unschädliche Offenbarung (Art. 55 EPÜ)", S,
      "Eine Offenbarung bleibt außer Betracht, wenn sie höchstens sechs Monate vor Einreichung der europäischen Anmeldung erfolgte und auf einem "
      "offensichtlichen Missbrauch zum Nachteil des Anmelders oder auf einer Zurschaustellung auf einer anerkannten Ausstellung beruht (Art. 55 EPÜ).",
      "Die Frist berechnet sich vom tatsächlichen Anmeldetag, nicht vom Prioritätstag (G 3/98). Bei Ausstellungen Angabe bei Einreichung und "
      "Bescheinigung binnen vier Monaten (R. 25 EPÜ). Eigene Veröffentlichungen des Anmelders (Fachartikel, Messe ohne Anerkennung) sind nie "
      "unschädlich – eine Neuheitsschonfrist kennt das EPÜ nicht.",
      norms=["Art. 55 Abs. 1 EPÜ", "R. 25 EPÜ"], cases=["epc_g_3_98"], related=["epc_stand_der_technik"], gl=["b_vi_5_5"]),
    c("epc_medizinische_indikation", "Erste und weitere medizinische Indikation (Art. 54 Abs. 4, 5 EPÜ)", S,
      "Bekannte Stoffe sind für die Anwendung in einem Verfahren nach Art. 53 lit. c EPÜ patentierbar, wenn diese Anwendung nicht zum Stand der "
      "Technik gehört (Abs. 4, erste Indikation), und für jede weitere spezifische Anwendung (Abs. 5).",
      "Anspruchsformat: „Stoff X zur Verwendung bei der Behandlung von Y“ (zweckgebundener Stoffschutz). Auch eine neue Dosierungsanleitung kann "
      "die Neuheit begründen (G 2/08); das schweizerische Anspruchsformat ist seither ausgeschlossen. Verfahren zur Behandlung selbst bleiben "
      "nach Art. 53 lit. c EPÜ ausgeschlossen.",
      norms=["Art. 54 Abs. 4 EPÜ", "Art. 54 Abs. 5 EPÜ", "Art. 53 EPÜ"], cases=["epc_g_2_08"], related=["epc_stand_der_technik"], gl=["g_vi_6"]),
    c("epc_anspruchsauslegung", "Auslegung der Ansprüche (Art. 69 EPÜ)", S,
      "Der Schutzbereich wird durch die Ansprüche bestimmt; Beschreibung und Zeichnungen sind zur Auslegung heranzuziehen (Art. 69 Abs. 1 EPÜ "
      "mit Auslegungsprotokoll). Das gilt auch bei der Prüfung der Patentierbarkeit (G 1/24).",
      "Die Ansprüche sind Ausgangspunkt, Beschreibung und Zeichnungen werden stets herangezogen, nicht nur bei Unklarheit (G 1/24). Werden "
      "Ansprüche geändert und führt ein Widerspruch zur Beschreibung dazu, dass Art. 84 EPÜ oder andere Erfordernisse nicht erfüllt sind, ist die "
      "Beschreibung anzupassen (G 1/25).",
      norms=["Art. 69 EPÜ", "Art. 84 EPÜ"], cases=["epc_g_1_24", "epc_g_1_25"], related=["epc_schutzbereichserweiterung"], gl=["f_iv_4"]),
    # ------------------------------------------------------------------ Anmeldung, Anmeldetag, Priorität, Änderungen
    c("epc_anmeldetag", "Anmeldetag (Art. 80 EPÜ, R. 40 EPÜ)", A,
      "Anmeldetag ist der Tag, an dem die Unterlagen einen Hinweis auf den Patentantrag, Angaben zur Identität des Anmelders und eine "
      "Beschreibung oder die Bezugnahme auf eine früher eingereichte Anmeldung enthalten (Art. 80 EPÜ, R. 40 Abs. 1 EPÜ).",
      "Ansprüche, Gebühren und Amtssprache sind für den Anmeldetag nicht nötig: Ansprüche können binnen zwei Monaten nachgereicht werden "
      "(R. 58 EPÜ), Übersetzung binnen zwei Monaten (R. 6 Abs. 1 EPÜ), Anmelde- und Recherchengebühr binnen eines Monats (R. 38 Abs. 1 EPÜ). "
      "Bei Bezugnahme: beglaubigte Abschrift binnen zwei Monaten (R. 40 Abs. 3 EPÜ). Fehlende Teile verschieben den Anmeldetag (R. 56 EPÜ).",
      norms=["Art. 80 EPÜ", "R. 40 Abs. 1 EPÜ", "R. 40 Abs. 3 EPÜ", "R. 58 EPÜ"], related=["epc_fehlende_teile", "epc_sprachen"], gl=["a_ii_4_1"]),
    c("epc_fehlende_teile", "Fehlende und fälschlich eingereichte Teile (R. 56, R. 56a EPÜ)", A,
      "Fehlende Teile der Beschreibung oder fehlende Zeichnungen (R. 56 EPÜ) und fälschlich eingereichte Unterlagen (R. 56a EPÜ) können binnen "
      "zwei Monaten nach dem Anmeldetag oder nach Aufforderung nachgereicht werden; der Anmeldetag wird dann neu festgesetzt.",
      "Ausnahme: Die Teile sind vollständig in der beanspruchten Priorität enthalten und der Anmelder beantragt dies fristgerecht mit Abschrift "
      "(und Übersetzung) – dann bleibt der Anmeldetag (R. 56 Abs. 3 EPÜ, R. 56a Abs. 4 EPÜ). Gegen die Neudatierung hilft die Rücknahme der "
      "nachgereichten Teile binnen eines Monats (R. 56 Abs. 6 EPÜ). Neudatierung kann die Prioritätsfrist sprengen. Keine Weiterbehandlung "
      "(R. 135 Abs. 2 EPÜ). Fehlende Ansprüche fallen nicht unter R. 56 EPÜ, sondern unter R. 58 EPÜ.",
      norms=["R. 56 EPÜ", "R. 56a EPÜ", "R. 58 EPÜ"], related=["epc_anmeldetag", "epc_prioritaet"], gl=["a_ii_5", "a_ii_6"]),
    c("epc_prioritaet", "Priorität (Art. 87 bis 89 EPÜ)", A,
      "Wer in oder für einen Verbandsstaat der PVÜ oder ein WTO-Mitglied eine Anmeldung ordnungsgemäß eingereicht hat, genießt für die "
      "europäische Nachanmeldung derselben Erfindung binnen zwölf Monaten ein Prioritätsrecht (Art. 87 Abs. 1 EPÜ); der Prioritätstag gilt "
      "als Anmeldetag für Art. 54 Abs. 2, 3 und Art. 60 Abs. 2 EPÜ (Art. 89 EPÜ).",
      "Voraussetzungen: erste Anmeldung (Art. 87 Abs. 4 EPÜ: eine jüngere gilt nur als erste, wenn die ältere vor ihrer Einreichung ohne "
      "öffentliche Einsicht und ohne Rechte zurückgenommen wurde und nicht Grundlage einer Priorität war), dieselbe Erfindung (G 2/98), "
      "Berechtigung (widerlegbar vermutet, G 1/22). Erklärung, Abschrift, Übersetzung nach R. 52, R. 53 EPÜ. Mehrfach- und Teilprioritäten sind "
      "zulässig (Art. 88 Abs. 2, 3 EPÜ; G 1/15). Prioritätsfrist: keine Weiterbehandlung, aber Wiedereinsetzung binnen zwei Monaten (R. 136 Abs. 1 EPÜ).",
      norms=["Art. 87 Abs. 1 EPÜ", "Art. 87 Abs. 4 EPÜ", "Art. 88 EPÜ", "Art. 89 EPÜ", "R. 52 EPÜ", "R. 53 EPÜ"],
      cases=["epc_g_2_98", "epc_g_1_15", "epc_g_1_22", "epc_g_3_93"], related=["epc_teilprioritaet", "epc_stand_der_technik", "epc_wiedereinsetzung"],
      gl=["a_iii_6", "a_iii_6_6", "f_vi_1"]),
    c("epc_teilprioritaet", "Teilpriorität (G 1/15)", A,
      "Ein generischer „ODER“-Anspruch kann für den Teil, der im Prioritätsdokument eindeutig und ausführbar offenbart ist, die Priorität "
      "beanspruchen, für den Rest nicht (Art. 88 Abs. 3 EPÜ; G 1/15).",
      "Klausurtechnik: Anspruch gedanklich in den prioritätsberechtigten Teil (Prioritätstag) und den Rest (Anmeldetag) aufspalten; ein im "
      "Intervall veröffentlichtes Dokument schadet nur dem Rest. Die eigene Prioritätsanmeldung wird so nicht zum „giftigen“ Stand der Technik.",
      norms=["Art. 88 Abs. 2 EPÜ", "Art. 88 Abs. 3 EPÜ"], cases=["epc_g_1_15"], related=["epc_prioritaet"], gl=["f_vi_2_4"]),
    c("epc_teilanmeldung", "Teilanmeldung (Art. 76 EPÜ, R. 36 EPÜ)", A,
      "Eine Teilanmeldung kann zu jeder anhängigen früheren europäischen Anmeldung unmittelbar beim EPA eingereicht werden; sie gilt als am "
      "Anmeldetag der Stammanmeldung eingereicht und genießt deren Priorität, soweit sie nicht über deren Inhalt hinausgeht (Art. 76 Abs. 1 EPÜ, "
      "R. 36 Abs. 1 EPÜ).",
      "Anhängig ist die Stammanmeldung bis zum Tag vor dem Hinweis auf die Erteilung, nach Zurückweisung bis zum Ablauf der Beschwerdefrist "
      "(G 1/09), nicht aber während einer laufenden Wiedereinsetzungsfrist nach Rechtsverlust (J 4/11). Bei Ketten muss jede Generation den Inhalt "
      "jeder Vorgängerin wahren (G 1/06). Gebühren: Anmelde- und Recherchengebühr binnen eines Monats (R. 36 Abs. 3 EPÜ), Zusatzgebühr ab "
      "der zweiten Generation (Art. 2 Abs. 1 Nr. 1b GebO), rückständige Jahresgebühren binnen vier Monaten (R. 51 Abs. 3 EPÜ). Doppelpatentierung "
      "ist ausgeschlossen (G 4/19).",
      norms=["Art. 76 Abs. 1 EPÜ", "R. 36 EPÜ", "R. 51 Abs. 3 EPÜ"], cases=["epc_g_1_05", "epc_g_1_06", "epc_g_1_09", "epc_j_4_11", "epc_g_4_19", "epc_j_18_09"],
      related=["epc_anhaengigkeit", "epc_unzulaessige_erweiterung"], gl=["a_iv_1", "a_iv_1_2", "a_iv_1_3", "c_ix_1"]),
    c("epc_anhaengigkeit", "Anhängigkeit der Anmeldung", A,
      "Eine Anmeldung ist anhängig, solange über sie noch entschieden werden kann: bis zum Tag vor dem Hinweis auf die Erteilung, nach Zurückweisung "
      "bis zum Ablauf der Beschwerdefrist oder bis zum Ende des Beschwerdeverfahrens, nach Rücknahmefiktion während der Weiterbehandlungsfrist.",
      "Wichtig für Teilanmeldungen (R. 36 Abs. 1 EPÜ). Während der Weiterbehandlungsfrist ist die Anmeldung anhängig, wenn die Weiterbehandlung "
      "dann tatsächlich beantragt wird; nach Ablauf aller Fristen nur bei erfolgreicher Wiedereinsetzung rückwirkend (J 4/11). Eine Euro-PCT-"
      "Anmeldung ist erst nach Eintritt in die europäische Phase anhängig (J 18/09).",
      norms=["R. 36 Abs. 1 EPÜ", "Art. 97 EPÜ"], cases=["epc_g_1_09", "epc_j_4_11", "epc_j_18_09"], related=["epc_teilanmeldung"], gl=["a_iv_1_1"]),
    c("epc_vindikation", "Recht auf das Patent und Vindikation (Art. 60, 61 EPÜ)", A,
      "Das Recht auf das europäische Patent hat der Erfinder oder sein Rechtsnachfolger (Art. 60 Abs. 1 EPÜ). Ist durch rechtskräftige "
      "Entscheidung ein Dritter als berechtigt anerkannt, kann er die Anmeldung als eigene weiterverfolgen, eine neue Anmeldung einreichen oder "
      "die Zurückweisung beantragen (Art. 61 Abs. 1 EPÜ).",
      "Zuständig für den Streit sind die nationalen Gerichte (Anerkennungsprotokoll). Das EPA setzt das Erteilungsverfahren auf Nachweis der "
      "Klageerhebung aus (R. 14 Abs. 1 EPÜ, nicht vor Veröffentlichung und nur vor dem Hinweis auf die Erteilung, J 14/19); laufende Fristen außer "
      "den Jahresgebührenfristen werden gehemmt (R. 14 Abs. 4 EPÜ). Rechtsbehelfe binnen drei Monaten ab Rechtskraft (R. 16 Abs. 1 EPÜ). "
      "Die neue Anmeldung nach Art. 61 Abs. 1 lit. b EPÜ erhält den Anmeldetag der ursprünglichen.",
      norms=["Art. 60 Abs. 1 EPÜ", "Art. 61 Abs. 1 EPÜ", "R. 14 EPÜ", "R. 16 EPÜ"], cases=["epc_j_14_19"], related=["epc_teilanmeldung"],
      gl=["a_iv_2_2", "a_iv_2_4", "c_ix_2_3"]),
    c("epc_unzulaessige_erweiterung", "Unzulässige Erweiterung (Art. 123 Abs. 2 EPÜ)", A,
      "Anmeldung und Patent dürfen nicht so geändert werden, dass ihr Gegenstand über den Inhalt der Anmeldung in der ursprünglich eingereichten "
      "Fassung hinausgeht (Art. 123 Abs. 2 EPÜ).",
      "Maßstab ist, was der Fachmann den ursprünglichen Unterlagen unmittelbar und eindeutig entnimmt (Goldstandard, G 2/10). Typische Fehler: "
      "Zwischenverallgemeinerung, Auswahl aus zwei Listen, Streichung als wesentlich offenbarter Merkmale. Disclaimer nach G 1/03, G 1/16. "
      "Für Teilanmeldungen gilt derselbe Maßstab gegenüber der Stammanmeldung (Art. 76 Abs. 1 EPÜ). Einspruchs- und Nichtigkeitsgrund "
      "(Art. 100 lit. c EPÜ, Art. 138 Abs. 1 lit. c EPÜ).",
      norms=["Art. 123 Abs. 2 EPÜ", "Art. 76 Abs. 1 EPÜ", "Art. 100 EPÜ"], cases=["epc_g_2_10", "epc_g_1_03", "epc_g_1_93"],
      related=["epc_disclaimer", "epc_schutzbereichserweiterung", "epc_berichtigung"], gl=["h_iv_2", "h_v_3"]),
    c("epc_disclaimer", "Disclaimer", A,
      "Ein Disclaimer nimmt einen Teil des beanspruchten Gegenstands ausdrücklich aus. Ein ursprünglich nicht offenbarter Disclaimer ist nur "
      "zulässig, um die Neuheit gegenüber Art. 54 Abs. 3 EPÜ oder einer zufälligen Vorwegnahme wiederherzustellen oder aus nichttechnischen "
      "Gründen Ausgeschlossenes zu entfernen (G 1/03, G 1/16).",
      "Er darf nicht mehr ausnehmen als nötig und keinen technischen Beitrag leisten. Ein offenbarter Disclaimer (Ausklammern einer ursprünglich "
      "beschriebenen Ausführungsform) unterliegt dem Goldstandard: Der verbleibende Gegenstand muss ursprünglich offenbart sein (G 2/10).",
      norms=["Art. 123 Abs. 2 EPÜ", "Art. 54 Abs. 3 EPÜ"], cases=["epc_g_1_03", "epc_g_2_10", "epc_g_1_16"],
      related=["epc_unzulaessige_erweiterung", "epc_aeltere_rechte"], gl=["h_v_4"]),
    c("epc_schutzbereichserweiterung", "Erweiterung des Schutzbereichs (Art. 123 Abs. 3 EPÜ)", A,
      "Das erteilte Patent darf im Einspruchs-, Beschränkungs- oder Beschwerdeverfahren nicht so geändert werden, dass sein Schutzbereich "
      "erweitert wird (Art. 123 Abs. 3 EPÜ).",
      "Maßstab ist der Schutzbereich nach Art. 69 EPÜ. Kategoriewechsel kann zulässig sein (Stoff → Verwendung, G 2/88). Kollision mit Abs. 2 "
      "(unentrinnbare Falle): Ein unzulässig aufgenommenes beschränkendes Merkmal kann nicht gestrichen werden (G 1/93). Einspruchsgrund ist "
      "Abs. 3 nicht, wohl aber Nichtigkeitsgrund (Art. 138 Abs. 1 lit. d EPÜ).",
      norms=["Art. 123 Abs. 3 EPÜ", "Art. 69 EPÜ", "Art. 138 Abs. 1 EPÜ"], cases=["epc_g_2_88", "epc_g_1_93"],
      related=["epc_unzulaessige_erweiterung", "epc_beschraenkung"], gl=["h_iv_3"]),
    c("epc_berichtigung", "Berichtigung von Fehlern (R. 139, R. 140 EPÜ)", A,
      "Sprachliche Fehler, Schreibfehler und Unrichtigkeiten in beim EPA eingereichten Unterlagen können auf Antrag berichtigt werden; in "
      "Beschreibung, Ansprüchen und Zeichnungen nur, wenn die Berichtigung offensichtlich ist (R. 139 EPÜ). Fehler in Entscheidungen berichtigt "
      "R. 140 EPÜ.",
      "Offensichtlich heißt: Fehler und Berichtigung ergeben sich unmittelbar und eindeutig aus den ursprünglichen Unterlagen (G 3/89, G 11/91). "
      "Die Prioritätserklärung wird nach der Sonderregel R. 52 Abs. 3 EPÜ berichtigt; die falsche Bezeichnung des Beschwerdeführers nach "
      "R. 101 Abs. 2 EPÜ (G 1/12). Der Wortlaut des erteilten Patents ist über R. 140 EPÜ nicht korrigierbar (G 1/10). Die Übersetzung "
      "kann jederzeit an das Original angepasst werden (Art. 14 Abs. 2 EPÜ).",
      norms=["R. 139 EPÜ", "R. 140 EPÜ", "R. 52 Abs. 3 EPÜ", "Art. 14 Abs. 2 EPÜ"], cases=["epc_g_3_89", "epc_g_1_10", "epc_g_1_12"],
      related=["epc_unzulaessige_erweiterung", "epc_erteilung"], gl=["a_v_3", "h_vi_2"]),
    # ------------------------------------------------------------------ Recherche, Prüfung, Erteilung
    c("epc_einheitlichkeit", "Einheitlichkeit und Recherche (Art. 82 EPÜ, R. 64, R. 164 EPÜ)", E,
      "Die Anmeldung darf nur eine Erfindung oder eine Gruppe von Erfindungen mit einem einzigen allgemeinen erfinderischen Gedanken enthalten "
      "(Art. 82 EPÜ). Bei Uneinheitlichkeit recherchiert das EPA die erste Erfindung und fordert für weitere Recherchengebühren an (R. 64 EPÜ).",
      "In der Prüfung werden nur recherchierte Erfindungen weiterverfolgt (R. 137 Abs. 5 EPÜ); für die übrigen bleiben Teilanmeldungen. "
      "Euro-PCT: ergänzende Recherche der ersten Erfindung mit Aufforderung zu weiteren Gebühren (R. 164 Abs. 1 EPÜ); war das EPA ISA, kann es "
      "in der Prüfung zur Zahlung für nicht recherchierte Erfindungen auffordern (R. 164 Abs. 2 EPÜ). Keine Weiterbehandlung (R. 135 Abs. 2 EPÜ).",
      norms=["Art. 82 EPÜ", "R. 64 EPÜ", "R. 164 EPÜ", "R. 137 Abs. 5 EPÜ"], related=["epc_teilanmeldung", "epc_euro_pct"], gl=["b_vii_2", "b_vii_2_3", "c_iii_3"]),
    c("epc_pruefungsverfahren", "Prüfungsverfahren (Art. 94 EPÜ, R. 70, R. 71 EPÜ)", E,
      "Die Prüfungsabteilung prüft auf schriftlichen Antrag (Prüfungsgebühr), ob Anmeldung und Erfindung den Erfordernissen des EPÜ genügen; "
      "Mängel teilt sie in Bescheiden nach Art. 94 Abs. 3 EPÜ mit.",
      "Prüfungsantrag binnen sechs Monaten nach dem Hinweis auf die Veröffentlichung des Recherchenberichts (R. 70 Abs. 1 EPÜ), Stellungnahme zur "
      "Recherche (R. 70a EPÜ). Versäumte Erwiderung auf einen Bescheid: Rücknahmefiktion (Art. 94 Abs. 4 EPÜ), Weiterbehandlung. Änderungen "
      "aus eigenem Antrieb nur einmal mit der Erwiderung auf den Recherchenbericht, danach mit Zustimmung (R. 137 Abs. 2, 3 EPÜ).",
      norms=["Art. 94 EPÜ", "R. 70 EPÜ", "R. 70a EPÜ", "R. 137 EPÜ"], related=["epc_erteilung", "epc_weiterbehandlung"], gl=["a_vi_2_2", "c_vi_1"]),
    c("epc_erteilung", "Erteilung (R. 71 Abs. 3 EPÜ, Art. 97 EPÜ)", E,
      "Vor der Erteilung teilt die Prüfungsabteilung die vorgesehene Fassung mit und fordert binnen vier Monaten zur Zahlung der Erteilungsgebühr "
      "und zur Übersetzung der Ansprüche in die beiden anderen Amtssprachen auf (R. 71 Abs. 3 EPÜ); dies gilt als Einverständnis (Abs. 5).",
      "Änderungs- oder Berichtigungswünsche innerhalb der Frist: neuer Bescheid nach Abs. 3 oder Wiederaufnahme der Prüfung (R. 71 Abs. 6 EPÜ); "
      "Versäumnis: Rücknahmefiktion (Abs. 7), Weiterbehandlung. Die Erteilung wird mit dem Hinweis im Europäischen Patentblatt wirksam "
      "(Art. 97 Abs. 3 EPÜ); ab diesem Tag laufen Einspruchsfrist, Frist für den Antrag auf einheitliche Wirkung und nationale Validierung. "
      "Fehler im erteilten Text sind danach nicht mehr korrigierbar (G 1/10).",
      norms=["R. 71 Abs. 3 EPÜ", "R. 71 Abs. 6 EPÜ", "Art. 97 Abs. 3 EPÜ"], cases=["epc_g_1_10"], related=["epc_pruefungsverfahren", "epc_validierung"],
      gl=["c_v_2", "c_v_4", "c_v_8"]),
    c("epc_einwendungen_dritter", "Einwendungen Dritter (Art. 115 EPÜ)", E,
      "Nach Veröffentlichung der Anmeldung kann jeder Dritte Einwendungen gegen die Patentierbarkeit erheben; er wird dadurch nicht Beteiligter "
      "(Art. 115 EPÜ, R. 114 EPÜ).",
      "Schriftlich, in einer Amtssprache, mit Begründung; gebührenfrei. Auch Klarheit und andere Mängel können gerügt werden; sie werden im "
      "Prüfungs- und Einspruchsverfahren berücksichtigt. Im PCT gibt es das Gegenstück in der internationalen Phase (bis 28 Monate ab Priorität).",
      norms=["Art. 115 EPÜ", "R. 114 EPÜ"], related=["epc_einspruch"], gl=["e_vi_3"]),
    c("epc_jahresgebuehren", "Jahresgebühren (Art. 86 EPÜ, R. 51 EPÜ)", E,
      "Für die europäische Anmeldung sind ab dem dritten Jahr Jahresgebühren an das EPA zu zahlen, jeweils fällig am letzten Tag des Monats, in den "
      "der Jahrestag des Anmeldetags fällt (Art. 86 Abs. 1 EPÜ, R. 51 Abs. 1 EPÜ).",
      "Nachfrist sechs Monate mit Zuschlagsgebühr (R. 51 Abs. 2 EPÜ); erst mit ihrem Ablauf gilt die Anmeldung als zurückgenommen. Keine "
      "Weiterbehandlung, nur Wiedereinsetzung. Vorauszahlung frühestens sechs (drittes Jahr) bzw. drei Monate vor Fälligkeit. Teilanmeldung: "
      "rückständige Gebühren binnen vier Monaten ohne Zuschlag (R. 51 Abs. 3 EPÜ). Nach dem Hinweis auf die Erteilung zahlen Inhaber an die "
      "nationalen Ämter bzw. beim Einheitspatent an das EPA.",
      norms=["Art. 86 Abs. 1 EPÜ", "R. 51 EPÜ"], cases=["epc_j_4_11"], related=["epc_wiedereinsetzung", "epc_gebuehrenzahlung"], gl=["a_x_5_2_4"]),
    # ------------------------------------------------------------------ Fristen und Rechtsbehelfe
    c("epc_fristen", "Fristberechnung (R. 131, R. 134 EPÜ)", F,
      "Fristen beginnen mit dem auslösenden Ereignis (Zustellung, Anmeldetag); Monatsfristen enden im maßgeblichen späteren Monat an dem Tag mit "
      "derselben Zahl, fehlt er, am letzten Tag des Monats (R. 131 Abs. 2, 4 EPÜ). Ist das EPA am letzten Tag geschlossen, läuft die Frist am "
      "nächsten Arbeitstag ab (R. 134 Abs. 1 EPÜ).",
      "Zustellung: Das Schriftstück gilt als an seinem Datum zugestellt (R. 126 Abs. 2 EPÜ, R. 127 Abs. 2 EPÜ, seit 1.11.2023 ohne Zehn-Tage-"
      "Fiktion). Verlängerung auch bei nicht verfügbaren elektronischen Einreichungswegen (R. 134 Abs. 1 Satz 2 EPÜ) und bei allgemeiner Störung des "
      "Postverkehrs (R. 134 Abs. 2 EPÜ); außerordentliche Ereignisse in den letzten zehn Tagen vor Fristablauf nach R. 134 Abs. 5 EPÜ. "
      "Klausurschema: Ereignis → Dauer → Rohdatum → R. 134 EPÜ → Behelf (Weiterbehandlung, Wiedereinsetzung).",
      norms=["R. 131 EPÜ", "R. 134 EPÜ", "R. 126 EPÜ", "Art. 120 EPÜ"], cases=["epc_j_10_20"], related=["epc_zustellung", "epc_weiterbehandlung"],
      gl=["e_viii_1_4", "e_viii_1_6"]),
    c("epc_zustellung", "Zustellung (R. 125 bis 130 EPÜ)", F,
      "Das EPA stellt elektronisch, durch die Post oder durch Übergabe zu; an einen bestellten Vertreter wird zugestellt (R. 130 EPÜ). Zugestellte "
      "Schriftstücke gelten an dem Tag als zugestellt, auf den sie datiert sind (R. 126 Abs. 2 EPÜ, R. 127 Abs. 2 EPÜ).",
      "Seit 1.11.2023 gilt die frühere Zehn-Tage-Regel nicht mehr; nur wenn das EPA einen Zugang mehr als sieben Tage nach dem Datum nachweist, "
      "verschiebt sich das Fristende um die überschießenden Tage. Ist das Schriftstück nicht zugegangen, ist die Zustellung unwirksam.",
      norms=["R. 126 Abs. 2 EPÜ", "R. 127 EPÜ", "R. 130 EPÜ"], related=["epc_fristen"], gl=["e_ii_2_3", "e_ii_2_4"]),
    c("epc_rechtsverlust", "Rechtsverlust und Entscheidung darüber (R. 112 EPÜ)", F,
      "Tritt ein Rechtsverlust ohne Entscheidung ein (z. B. Rücknahmefiktion), teilt das EPA ihn mit; der Betroffene kann binnen zwei Monaten eine "
      "beschwerdefähige Entscheidung beantragen (R. 112 Abs. 1, 2 EPÜ).",
      "Die Mitteilung nach R. 112 Abs. 1 EPÜ setzt in der Regel die Weiterbehandlungsfrist in Gang (R. 135 Abs. 1 EPÜ). Der Antrag nach Abs. 2 ist "
      "der richtige Weg, wenn der Rechtsverlust bestritten wird (z. B. Zahlung war rechtzeitig); die Frist nach Abs. 2 ist nicht "
      "weiterbehandlungsfähig.",
      norms=["R. 112 EPÜ", "R. 135 Abs. 1 EPÜ"], related=["epc_weiterbehandlung", "epc_wiedereinsetzung"], gl=["e_viii_1_9"]),
    c("epc_weiterbehandlung", "Weiterbehandlung (Art. 121 EPÜ, R. 135 EPÜ)", F,
      "Hat der Anmelder eine Frist gegenüber dem EPA versäumt, wird die Anmeldung auf Antrag weiterbehandelt; der Antrag ist durch Zahlung der "
      "Gebühr binnen zwei Monaten nach der Mitteilung über die Fristversäumung oder den Rechtsverlust zu stellen, die versäumte Handlung ist "
      "nachzuholen (Art. 121 Abs. 1 EPÜ, R. 135 Abs. 1 EPÜ).",
      "Kein Verschulden nötig. Ausgeschlossen: Prioritätsfrist, Beschwerde- und Überprüfungsfrist, Weiterbehandlungs- und Wiedereinsetzungsfrist "
      "(Art. 121 Abs. 4 EPÜ) sowie die Fristen der R. 135 Abs. 2 EPÜ, u. a. für Übersetzung (R. 6 Abs. 1 EPÜ), Sprache der Teilanmeldung "
      "(R. 36 Abs. 2 EPÜ), Jahresgebühren mit Zuschlag (R. 51 Abs. 2 EPÜ), Priorität (R. 52 Abs. 2 EPÜ), fehlende Teile (R. 56 EPÜ, R. 58 EPÜ), "
      "Recherchengebühren (R. 64 EPÜ, R. 164 EPÜ) und die Entscheidung nach R. 112 Abs. 2 EPÜ. Nur für den Anmelder, nicht nach Erteilung.",
      norms=["Art. 121 EPÜ", "R. 135 EPÜ"], related=["epc_wiedereinsetzung", "epc_rechtsverlust", "epc_fristen"], gl=["e_viii_2"]),
    c("epc_wiedereinsetzung", "Wiedereinsetzung (Art. 122 EPÜ, R. 136 EPÜ)", F,
      "Wer trotz Beachtung aller nach den gegebenen Umständen gebotenen Sorgfalt verhindert war, eine Frist gegenüber dem EPA einzuhalten, wird "
      "auf Antrag wieder eingesetzt, wenn die Versäumung den Rechtsverlust unmittelbar zur Folge hat (Art. 122 Abs. 1 EPÜ).",
      "Antrag schriftlich binnen zwei Monaten nach Wegfall des Hindernisses, spätestens ein Jahr nach Fristablauf; für Prioritäts- und "
      "Überprüfungsfrist binnen zwei Monaten nach deren Ablauf; Gebühr, Begründung mit Glaubhaftmachung, versäumte Handlung nachholen "
      "(R. 136 Abs. 1, 2 EPÜ). Subsidiär: ausgeschlossen, wo Weiterbehandlung möglich ist (R. 136 Abs. 3 EPÜ). Sorgfalt des Vertreters und "
      "seines Hilfspersonals (J 5/80). Der Einsprechende nur in die Frist zur Beschwerdebegründung (G 1/86). Weiterbenutzungsrecht Dritter: Art. 122 Abs. 5 EPÜ.",
      norms=["Art. 122 EPÜ", "R. 136 EPÜ"], cases=["epc_j_5_80", "epc_g_1_86", "epc_j_6_22", "epc_j_4_11"],
      related=["epc_weiterbehandlung", "epc_fristen"], gl=["e_viii_3", "e_viii_3_1", "e_viii_3_2"]),
    c("epc_vertrauensschutz", "Vertrauensschutz (Treu und Glauben)", F,
      "Das EPA muss Erklärungen und Auskünfte, die es gibt, gegen sich gelten lassen; Beteiligte dürfen darauf vertrauen, dass ihnen aus "
      "irreführenden Mitteilungen des Amts kein Nachteil entsteht.",
      "Keine allgemeine Hinweispflicht auf Mängel, die der Beteiligte selbst erkennen muss (G 2/97); wohl aber bei leicht erkennbaren Mängeln, "
      "die noch rechtzeitig behoben werden können. Veröffentlichte Fristverlängerungen gelten zugunsten aller (J 10/20).",
      norms=["R. 134 EPÜ"], cases=["epc_g_2_97", "epc_j_10_20"], related=["epc_fristen"]),
    # ------------------------------------------------------------------ Einspruch, Beschränkung, Beschwerde
    c("epc_einspruch", "Einspruch (Art. 99 bis 101 EPÜ)", B,
      "Innerhalb von neun Monaten nach Bekanntmachung des Hinweises auf die Erteilung kann jeder Dritte beim EPA Einspruch einlegen; er ist "
      "schriftlich einzureichen und zu begründen und gilt erst als eingelegt, wenn die Einspruchsgebühr entrichtet ist (Art. 99 Abs. 1 EPÜ).",
      "Inhalt: R. 76 Abs. 2 EPÜ (Einsprechender, Patent, Umfang, Gründe, Tatsachen und Beweismittel); Mängel nach R. 77 EPÜ. Der Inhaber selbst "
      "kann nicht einsprechen (G 9/93), ein Strohmann schon (G 3/97); gemeinsamer Einspruch mit einer Gebühr (G 3/99). Wirkt für alle "
      "benannten Staaten und auch nach Verzicht oder Erlöschen (R. 75 EPÜ). Prüfungsumfang: G 9/91, G 10/91. Nach Verzicht oder Erlöschen des Patents "
      "nur auf Antrag des Einsprechenden binnen zwei Monaten (R. 84 Abs. 1 EPÜ), nach Tod des Einsprechenden oder Rücknahme des Einspruchs auch "
      "von Amts wegen (R. 84 Abs. 2 EPÜ). Entscheidung: Widerruf, Zurückweisung oder Aufrechterhaltung in geändertem Umfang (Art. 101 EPÜ).",
      norms=["Art. 99 EPÜ", "Art. 100 EPÜ", "Art. 101 EPÜ", "R. 75 EPÜ", "R. 76 EPÜ", "R. 84 EPÜ"],
      cases=["epc_g_9_93", "epc_g_3_97", "epc_g_3_99", "epc_g_9_91", "epc_g_10_91", "epc_g_3_14"],
      related=["epc_einspruchsgruende", "epc_einsprechendenstellung", "epc_beitritt", "epc_beschwerde"], gl=["d_i_4", "d_iii_1", "d_iii_6", "d_vii_5"]),
    c("epc_einspruchsgruende", "Einspruchsgründe (Art. 100 EPÜ)", B,
      "Der Einspruch kann nur darauf gestützt werden, dass der Gegenstand nicht patentierbar ist (Art. 52 bis 57 EPÜ), die Erfindung nicht "
      "ausführbar offenbart ist oder der Gegenstand über den Inhalt der ursprünglichen Anmeldung hinausgeht (Art. 100 EPÜ).",
      "Kein Einspruchsgrund: Klarheit (Art. 84 EPÜ), Einheitlichkeit, Priorität als solche, widerrechtliche Entnahme (nationale Gerichte). "
      "Geänderte Ansprüche werden auf Klarheit nur geprüft, soweit die Änderung den Mangel verursacht (G 3/14). Neue Gründe im "
      "Beschwerdeverfahren nur mit Zustimmung des Inhabers (G 10/91).",
      norms=["Art. 100 EPÜ", "Art. 84 EPÜ", "Art. 101 Abs. 3 EPÜ"], cases=["epc_g_10_91", "epc_g_3_14"], related=["epc_einspruch"], gl=["d_iii_5", "d_v_2_2"]),
    c("epc_einsprechendenstellung", "Stellung als Einsprechender", B,
      "Einsprechender ist, wer im Einspruch genannt ist; die Stellung ist nicht frei übertragbar, geht aber mit dem Geschäftsbereich, auf den sich "
      "der Einspruch bezieht, und im Erbfall über (G 4/88, G 2/04).",
      "Erlischt der Einsprechende, kann das EPA das Verfahren von Amts wegen fortsetzen (R. 84 Abs. 2 EPÜ); lebt er nach nationalem Recht "
      "rückwirkend wieder auf, wird es mit ihm fortgesetzt (G 1/13). Nachweis des Übergangs durch Urkunden.",
      norms=["Art. 99 EPÜ", "R. 84 EPÜ"], cases=["epc_g_4_88", "epc_g_2_04", "epc_g_1_13"], related=["epc_einspruch"], gl=["d_i_6"]),
    c("epc_beitritt", "Beitritt des vermeintlichen Verletzers (Art. 105 EPÜ)", B,
      "Wer wegen Verletzung des Patents verklagt ist oder eine negative Feststellungsklage nach Unterlassungsaufforderung erhoben hat, kann dem "
      "anhängigen Einspruchsverfahren binnen drei Monaten nach Klageerhebung beitreten; der Beitritt gilt als Einspruch (Art. 105 EPÜ, R. 89 EPÜ).",
      "Schriftlich, begründet, mit Einspruchsgebühr. Beitritt auch während des Beschwerdeverfahrens; dort erlangt der Beitretende aber keine "
      "Stellung als Beschwerdeführer: Nehmen alle Beschwerdeführer zurück, endet das Verfahren (G 2/24).",
      norms=["Art. 105 EPÜ", "R. 89 EPÜ"], cases=["epc_g_2_24"], related=["epc_einspruch", "epc_beschwerde"], gl=["d_i_5", "d_vii_6"]),
    c("epc_beschraenkung", "Beschränkung und Widerruf (Art. 105a bis 105c EPÜ)", B,
      "Der Inhaber kann jederzeit nach der Erteilung beim EPA beantragen, sein Patent zu widerrufen oder durch Änderung der Ansprüche zu "
      "beschränken; der Antrag ist unzulässig, solange ein Einspruchsverfahren anhängig ist (Art. 105a EPÜ).",
      "Antrag nach R. 92 EPÜ mit Gebühr; Prüfung nur auf Klarheit, Beschränkung, Art. 123 Abs. 2, 3 EPÜ (R. 95 Abs. 2 EPÜ), nicht auf "
      "Patentierbarkeit. Ein späterer Einspruch beendet das Beschränkungsverfahren (R. 93 Abs. 2 EPÜ). Wirkung ex tunc für alle Staaten "
      "(Art. 105b Abs. 3 EPÜ). Unterschiedliche Ansprüche für verschiedene Staaten sind möglich (R. 138 EPÜ).",
      norms=["Art. 105a EPÜ", "Art. 105b EPÜ", "R. 92 EPÜ", "R. 93 EPÜ", "R. 95 EPÜ"], cases=["epc_g_9_93"],
      related=["epc_schutzbereichserweiterung", "epc_einspruch"], gl=["d_x", "d_x_4", "d_x_7_1"]),
    c("epc_beschwerde", "Beschwerde (Art. 106 bis 112 EPÜ)", B,
      "Entscheidungen der Eingangsstelle, der Prüfungs- und Einspruchsabteilungen und der Rechtsabteilung sind mit der Beschwerde anfechtbar "
      "(Art. 106 Abs. 1 EPÜ); beschwerdeberechtigt ist, wer durch die Entscheidung beschwert ist (Art. 107 EPÜ).",
      "Beschwerdeschrift und Gebühr binnen zwei Monaten nach Zustellung, Begründung binnen vier Monaten (Art. 108 EPÜ); ohne fristgerechte "
      "Gebühr gilt sie als nicht eingelegt (G 1/18). Keine Weiterbehandlung (Art. 121 Abs. 4 EPÜ); Wiedereinsetzung für Anmelder "
      "und Inhaber, für den Einsprechenden nur in die Begründungsfrist (G 1/86). Abhilfe im einseitigen Verfahren (Art. 109 EPÜ). Verbot der Schlechterstellung (G 1/99). Rückzahlung der "
      "Gebühr nach R. 103 EPÜ (Rücknahme vor Begründung: voll). Aufschiebende Wirkung (Art. 106 Abs. 1 Satz 2 EPÜ). Verfahrensordnung: VOBK.",
      norms=["Art. 106 EPÜ", "Art. 107 EPÜ", "Art. 108 EPÜ", "Art. 109 EPÜ", "R. 99 EPÜ", "R. 101 EPÜ", "R. 103 EPÜ"],
      cases=["epc_g_1_18", "epc_g_1_12", "epc_g_1_99", "epc_g_3_03", "epc_g_2_97", "epc_g_1_86", "epc_g_2_24"],
      related=["epc_einspruch", "epc_ueberpruefung"], gl=["e_xi_5", "e_xi_6", "e_xi_7"]),
    c("epc_ueberpruefung", "Überprüfungsantrag (Art. 112a EPÜ)", B,
      "Gegen Entscheidungen der Beschwerdekammern kann ein Beteiligter, der beschwert ist, bei der Großen Beschwerdekammer Überprüfung "
      "beantragen, gestützt auf schwerwiegende Verfahrensmängel (insbesondere Verletzung des rechtlichen Gehörs) oder Straftaten (Art. 112a EPÜ).",
      "Frist zwei Monate ab Zustellung (bei Straftat ab Feststellung, spätestens fünf Jahre), Gebühr, Begründung (R. 107 EPÜ); der Mangel muss im "
      "Beschwerdeverfahren gerügt worden sein (R. 106 EPÜ). Keine aufschiebende Wirkung. Keine Weiterbehandlung, Wiedereinsetzung binnen zwei "
      "Monaten nach Fristablauf (R. 136 Abs. 1 EPÜ).",
      norms=["Art. 112a EPÜ", "R. 104 EPÜ", "R. 106 EPÜ", "R. 107 EPÜ"], related=["epc_beschwerde"], gl=["e_xi_5"]),
    # ------------------------------------------------------------------ Euro-PCT und PCT
    c("epc_euro_pct", "Euro-PCT-Anmeldung (Art. 153 EPÜ, R. 159 EPÜ)", P,
      "Eine internationale Anmeldung, für die das EPA Bestimmungsamt oder ausgewähltes Amt ist, gilt als europäische Anmeldung (Art. 153 Abs. 2 EPÜ). "
      "Der Anmelder muss binnen 31 Monaten ab Anmelde- oder Prioritätstag die Handlungen der R. 159 Abs. 1 EPÜ vornehmen.",
      "Handlungen: Übersetzung, Angabe der Unterlagen, Anmeldegebühr, Benennungsgebühr, Recherchengebühr (ergänzende Recherche), Prüfungsantrag, "
      "ggf. Jahresgebühr. Versäumnis: Rücknahmefiktion (R. 160 EPÜ), Weiterbehandlung. Vorzeitige Bearbeitung auf Antrag (Art. 23 Abs. 2 PCT, "
      "Art. 40 Abs. 2 PCT). Sprache: keine neue Übersetzung, wenn in Amtssprache veröffentlicht (G 4/08). Nach Eintritt R. 161, R. 162 EPÜ, "
      "Uneinheitlichkeit R. 164 EPÜ. Teilanmeldung erst nach Eintritt (J 18/09). Stand der Technik nach Art. 54 Abs. 3 EPÜ nur mit R. 165 EPÜ.",
      norms=["Art. 153 EPÜ", "R. 159 EPÜ", "R. 160 EPÜ", "R. 161 EPÜ", "R. 164 EPÜ", "R. 165 EPÜ"], cases=["epc_g_4_08", "epc_j_18_09"],
      related=["epc_pct_international", "epc_einheitlichkeit", "epc_aeltere_rechte"], gl=["c_ii_1_2", "b_vii_2_3", "g_iv_5_2"]),
    c("epc_pct_international", "Internationale Phase vor dem EPA (PCT)", P,
      "Das EPA ist Anmeldeamt, Internationale Recherchenbehörde, Behörde für die ergänzende Recherche und Behörde für die internationale "
      "vorläufige Prüfung (Art. 151, Art. 152 EPÜ).",
      "Klausurstoff: zuständiges Anmeldeamt (R. 19.1 PCT; EPA für Staatsangehörige und Ansässige der EPÜ-Staaten), Anmeldetag und fehlende "
      "Bestandteile (Art. 11 PCT, R. 20 PCT, Einbeziehung durch Verweis R. 4.18 PCT), Prioritätsberichtigung (R. 26bis PCT), Wiederherstellung "
      "der Priorität (R. 26bis.3 PCT: Sorgfaltsmaßstab beim EPA), Änderungen (Art. 19, Art. 34 PCT), ergänzende Recherche (R. 45bis PCT), "
      "Antrag auf vorläufige Prüfung (R. 54bis PCT), Fristberechnung (R. 80 PCT) und Berichtigung (R. 91 PCT).",
      norms=["Art. 150 EPÜ", "Art. 151 EPÜ", "Art. 152 EPÜ"], related=["epc_euro_pct"]),
    # ------------------------------------------------------------------ Sprachen, Gebühren, Vertretung
    c("epc_sprachen", "Sprachen (Art. 14 EPÜ, R. 3, R. 6 EPÜ)", G,
      "Amtssprachen des EPA sind Deutsch, Englisch und Französisch; die Anmeldung kann in jeder Sprache eingereicht werden, ist dann aber binnen "
      "zwei Monaten in eine Amtssprache zu übersetzen, die Verfahrenssprache wird (Art. 14 Abs. 1 bis 3 EPÜ, R. 6 Abs. 1 EPÜ).",
      "Fristgebundene Schriftstücke dürfen Berechtigte nach Art. 14 Abs. 4 EPÜ in ihrer Landessprache einreichen (Übersetzung binnen eines Monats, "
      "R. 6 Abs. 2 EPÜ). Sprachenermäßigung von 30 % auf Anmelde- und Prüfungsgebühr bei Einreichung in einer zugelassenen Nichtamtssprache für "
      "KMU (einschließlich Kleinstunternehmen), natürliche Personen, Organisationen ohne Gewinnerzielungsabsicht, Hochschulen und öffentliche Forschungseinrichtungen mit Sitz in diesem Staat (R. 7a Abs. 1 EPÜ, "
      "Art. 14 Abs. 1 GebO); daneben seit 1.4.2024 die sprachunabhängige Ermäßigung für Kleinstunternehmen (R. 7a Abs. 3 EPÜ). Im schriftlichen "
      "Verfahren jede Amtssprache (R. 3 Abs. 1 EPÜ). Fehlt die Übersetzung: Rücknahmefiktion, keine Weiterbehandlung, Wiedereinsetzung.",
      norms=["Art. 14 EPÜ", "R. 3 EPÜ", "R. 6 EPÜ"], cases=["epc_g_4_08"], related=["epc_gebuehrenzahlung", "epc_anmeldetag"],
      gl=["a_vii_1", "a_vii_2", "a_vii_3_2", "a_x_9_3"]),
    c("epc_gebuehrenzahlung", "Gebühren: Zahlung, Ermäßigung, Rückerstattung", G,
      "Gebühren werden durch Überweisung auf ein Bankkonto des EPA oder durch Abbuchung von einem laufenden Konto beim EPA entrichtet; als "
      "Tag der Zahlung gilt grundsätzlich der Tag der Gutschrift (Art. 5, Art. 7 Abs. 1 GebO).",
      "Verspätete Überweisung gilt als rechtzeitig, wenn die Zahlung innerhalb der Frist in einem Vertragsstaat bei einer Bank veranlasst wurde "
      "(Art. 7 Abs. 3, 4 GebO). Laufendes Konto und automatische Abbuchung nach den Vorschriften über das laufende Konto (VLK); bei fehlender "
      "Deckung schützt eine rechtzeitig veranlasste Auffüllung. Ermäßigungen: Sprachenregelung und Kleinstunternehmen (R. 7a EPÜ, Art. 14 GebO). "
      "Rückerstattung der Prüfungsgebühr voll bei Rücknahme vor Beginn der Sachprüfung, zu 50 % danach bis zum Ablauf der Frist für die Erwiderung "
      "auf den ersten Bescheid nach Art. 94 Abs. 3 EPÜ (Art. 11 GebO). Beträge stets an der aktuellen Gebührenordnung prüfen.",
      norms=["Art. 51 EPÜ"], related=["epc_jahresgebuehren", "epc_sprachen"], gl=["a_x_2", "a_x_4", "a_x_9", "a_x_10", "a_vi_2_5"]),
    c("epc_vertretung", "Vertretung (Art. 133, 134 EPÜ)", G,
      "Niemand muss sich vor dem EPA vertreten lassen, außer Beteiligte ohne Wohnsitz oder Sitz in einem Vertragsstaat; sie müssen außer für "
      "die Einreichung der Anmeldung einen zugelassenen Vertreter bestellen (Art. 133 Abs. 1, 2 EPÜ).",
      "Beteiligte mit Sitz in einem Vertragsstaat können durch Angestellte handeln (Art. 133 Abs. 3 EPÜ). Gemeinsamer Vertreter mehrerer "
      "Anmelder oder Einsprechender: R. 151 EPÜ. Vollmachten: R. 152 EPÜ; Handlungen eines nicht bevollmächtigten Vertreters gelten als nicht "
      "erfolgt (Abs. 6). Zustellungen an den Vertreter (R. 130 EPÜ). Vertretung durch Rechtsanwälte: Art. 134 Abs. 8 EPÜ.",
      norms=["Art. 133 EPÜ", "Art. 134 EPÜ", "R. 151 EPÜ", "R. 152 EPÜ"], cases=["epc_g_3_99"], related=["epc_einspruch"], gl=["a_viii_1", "a_viii_1_2"]),
    c("epc_validierung", "Validierung und Einheitspatent (Art. 65 EPÜ)", G,
      "Nach der Erteilung entfaltet das europäische Patent in jedem benannten Staat die Wirkung eines nationalen Patents (Art. 64 EPÜ); ein "
      "Staat kann eine Übersetzung verlangen (Art. 65 EPÜ), die meisten verzichten darauf nach dem Londoner Übereinkommen.",
      "Für die teilnehmenden EU-Staaten kann binnen eines Monats nach dem Hinweis auf die Erteilung einheitliche Wirkung beantragt werden "
      "(R. 6 DOEPS); dann keine Validierung in diesen Staaten. Erstreckungs- und Validierungsstaaten außerhalb des EPÜ: Gebühren binnen sechs "
      "Monaten nach dem Hinweis auf die Veröffentlichung des Recherchenberichts.",
      norms=["Art. 64 EPÜ", "Art. 65 EPÜ"], related=["epc_erteilung"], gl=["c_v_2_1", "a_iii_12"]),
]
