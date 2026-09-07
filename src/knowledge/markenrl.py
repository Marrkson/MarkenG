# -*- coding: utf-8 -*-
"""Richtlinie (EU) 2015/2436 zur Angleichung der Rechtsvorschriften der Mitgliedstaaten
über die Marken (Markenrechtsrichtlinie, MarkenRL), ABl. L 336 vom 23.12.2015, S. 1.

HINWEIS: Der amtliche Wortlaut (EUR-Lex, CELEX 32015L2436) war aus der Build-Umgebung
nicht abrufbar (Netzwerksperre). Die Artikel sind deshalb als inhaltlich vollständige,
aber PARAPHRASIERTE Zusammenfassungen je Absatz erfasst, nicht als Zitat. Für Zitate
den Wortlaut auf EUR-Lex prüfen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2436

Felder je Artikel:
  nr, titel, kapitel, abschnitt
  absaetze    Liste [(nr, Paraphrase)]
  umsetzung   MarkenG-Vorschriften, die den Artikel umsetzen
  concepts    Begriffs-IDs (concepts.py)
  cases       Entscheidungs-IDs (cases.py)
  hinweis     Lern-/Klausurhinweis, insbes. Änderungen durch das MaMoG 2019
"""

CELEX = "32015L2436"
URL = "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:" + CELEX
URL_PDF = "https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:" + CELEX

K1 = "Kapitel 1 – Allgemeine Bestimmungen"
K2 = "Kapitel 2 – Materielles Markenrecht"
K3 = "Kapitel 3 – Verfahren"
K4 = "Kapitel 4 – Verwaltungszusammenarbeit"
K5 = "Kapitel 5 – Schlussbestimmungen"


def art(nr, titel, kapitel, abschnitt, absaetze, umsetzung=(), concepts=(), cases=(), hinweis=""):
    return dict(nr=str(nr), titel=titel, kapitel=kapitel, abschnitt=abschnitt,
                absaetze=[dict(nr=str(a), text=t) for a, t in absaetze],
                umsetzung=list(umsetzung), concepts=list(concepts), cases=list(cases), hinweis=hinweis)


ARTIKEL = [
    # ---------------- Kapitel 1 ----------------
    art(1, "Anwendungsbereich", K1, None, [
        (None, "Die Richtlinie gilt für alle Individual-, Garantie-, Gewährleistungs- und Kollektivmarken für Waren oder Dienstleistungen, die in einem Mitgliedstaat oder beim Benelux-Amt eingetragen oder angemeldet sind oder mit Wirkung für einen Mitgliedstaat international registriert wurden.")],
        umsetzung=["§ 1"], concepts=["markenrl", "marke"],
        hinweis="Nicht harmonisiert sind Benutzungsmarken (§ 4 Nr. 2 MarkenG) und geschäftliche Bezeichnungen (§ 5 MarkenG); insoweit bleibt das nationale Recht frei."),
    art(2, "Begriffsbestimmungen", K1, None, [
        ("a", "„Amt“ ist die für die Eintragung von Marken zuständige zentrale Behörde für den gewerblichen Rechtsschutz des Mitgliedstaats oder das Benelux-Amt für geistiges Eigentum."),
        ("b", "„Register“ ist das von einem Amt geführte Markenregister.")],
        umsetzung=["§ 56", "§ 41"], concepts=["markenrl"]),

    # ---------------- Kapitel 2, Abschnitt 1 ----------------
    art(3, "Markenformen", K2, "Abschnitt 1 – Markenformen", [
        (None, "Marken können alle Zeichen sein, insbesondere Wörter einschließlich Personennamen, Abbildungen, Buchstaben, Zahlen, Farben, die Form der Ware oder ihrer Verpackung sowie Klänge, sofern sie (a) geeignet sind, Waren oder Dienstleistungen eines Unternehmens von denen anderer zu unterscheiden, und (b) im Register so dargestellt werden können, dass Behörden und Publikum den Schutzgegenstand klar und eindeutig bestimmen können.")],
        umsetzung=["§ 3 Abs. 1", "§ 8 Abs. 1"], concepts=["markenfaehigkeit", "darstellbarkeit", "farbmarke", "formmarke"], cases=["eugh_libertel"],
        hinweis="Aufgabe des Erfordernisses der graphischen Darstellbarkeit (Sieckmann-Kriterien bleiben Maßstab). Umsetzung im MaMoG: § 8 Abs. 1 MarkenG neu gefasst; Klang-, Bewegungs-, Multimedia- und Hologrammmarken ausdrücklich zulässig."),

    # ---------------- Kapitel 2, Abschnitt 2 ----------------
    art(4, "Absolute Eintragungshindernisse oder Ungültigkeitsgründe", K2, "Abschnitt 2 – Eintragungshindernisse und Ungültigkeitsgründe", [
        ("1", "Von der Eintragung ausgeschlossen bzw. für ungültig zu erklären sind: (a) nicht markenfähige Zeichen; (b) Marken ohne Unterscheidungskraft; (c) ausschließlich beschreibende Angaben (Art, Beschaffenheit, Menge, Bestimmung, Wert, geographische Herkunft, Zeit der Herstellung, sonstige Merkmale); (d) im allgemeinen Sprachgebrauch oder in redlichen Verkehrsgepflogenheiten üblich gewordene Zeichen; (e) Zeichen, die ausschließlich aus der Form oder einem anderen charakteristischen Merkmal bestehen, die durch die Art der Ware bedingt, zur Erreichung einer technischen Wirkung erforderlich sind oder der Ware einen wesentlichen Wert verleihen; (f) Verstoß gegen öffentliche Ordnung oder gute Sitten; (g) Täuschungseignung; (h) Hoheitszeichen nach Art. 6ter PVÜ ohne Genehmigung; (i) Ursprungsbezeichnungen und geographische Angaben; (j) traditionelle Weinbezeichnungen; (k) garantiert traditionelle Spezialitäten; (l) frühere Sortenbezeichnungen."),
        ("2", "Eine Marke ist für ungültig zu erklären, wenn der Anmelder bei der Anmeldung bösgläubig war; die Mitgliedstaaten können Bösgläubigkeit auch als Eintragungshindernis vorsehen."),
        ("3", "Fakultative Gründe der Mitgliedstaaten: Verbot der Benutzung nach anderem Recht; Zeichen von hoher symbolischer Bedeutung, insbesondere religiöse Symbole; Abzeichen, Embleme und Wappen jenseits von Art. 6ter PVÜ."),
        ("4", "Die Hindernisse nach Abs. 1 lit. b, c und d greifen nicht, wenn die Marke vor dem Anmeldetag infolge Benutzung Unterscheidungskraft erlangt hat; die Ungültigerklärung ist ausgeschlossen, wenn die Unterscheidungskraft vor dem Antrag erlangt wurde."),
        ("5", "Die Mitgliedstaaten können vorsehen, dass Abs. 4 auch gilt, wenn die Unterscheidungskraft erst nach dem Anmeldetag, aber vor der Eintragung erlangt wurde.")],
        umsetzung=["§ 3 Abs. 2", "§ 8 Abs. 2", "§ 8 Abs. 3", "§ 50"], concepts=["absolute_schutzhindernisse", "unterscheidungskraft", "freihaltebeduerfnis", "uebliche_bezeichnung", "formausschluss", "taeuschung", "boesglaeubigkeit", "verkehrsdurchsetzung"],
        cases=["eugh_chiemsee", "eugh_philips_remington", "bgh_black_friday", "bgh_ritter_sport"],
        hinweis="Neu gegenüber RL 2008/95: Formausschluss auch für „andere charakteristische Merkmale“ (§ 3 Abs. 2 MarkenG), Bösgläubigkeit als zwingender Ungültigkeitsgrund (§ 8 Abs. 2 Nr. 14 MarkenG), Schutz von Ursprungsbezeichnungen, Weinbezeichnungen, Spezialitäten und Sortenbezeichnungen (§ 8 Abs. 2 Nr. 9 bis 13 MarkenG)."),
    art(5, "Relative Eintragungshindernisse oder Ungültigkeitsgründe", K2, "Abschnitt 2 – Eintragungshindernisse und Ungültigkeitsgründe", [
        ("1", "Ausgeschlossen oder ungültig ist eine Marke, (a) die mit einer älteren Marke identisch ist und für identische Waren angemeldet wurde, oder (b) wenn wegen Identität oder Ähnlichkeit mit der älteren Marke und der Waren für das Publikum Verwechslungsgefahr besteht, einschließlich der Gefahr gedanklicher Verbindung."),
        ("2", "„Ältere Marken“ sind: Unionsmarken, nationale und Benelux-Marken, international registrierte Marken mit Wirkung im Mitgliedstaat oder in der Union, jeweils mit früherem Anmeldetag (auch Priorität), Unionsmarken mit Seniorität, Anmeldungen solcher Marken vorbehaltlich ihrer Eintragung sowie notorisch bekannte Marken im Sinne des Art. 6bis PVÜ."),
        ("3", "Ferner ausgeschlossen oder ungültig: (a) Marken, die einer älteren, im Mitgliedstaat oder in der Union bekannten Marke identisch oder ähnlich sind, wenn die Benutzung deren Unterscheidungskraft oder Wertschätzung ohne rechtfertigenden Grund unlauter ausnutzen oder beeinträchtigen würde, und zwar unabhängig davon, ob die Waren identisch, ähnlich oder unähnlich sind; (b) Agentenmarken, die ein Agent oder Vertreter ohne Zustimmung des Inhabers auf eigenen Namen anmeldet; (c) Marken, die mit einer älteren Ursprungsbezeichnung oder geographischen Angabe kollidieren."),
        ("4", "Fakultative Gründe der Mitgliedstaaten: ältere Benutzungsmarken oder sonstige im Verkehr benutzte Kennzeichen, die ein Verbietungsrecht gewähren; sonstige ältere Rechte wie Name, Bildnis, Urheberrecht, gewerbliche Schutzrechte; Verwechslungsgefahr mit einer im Ausland benutzten Marke bei bösgläubiger Anmeldung."),
        ("5", "Keine Zurückweisung oder Ungültigerklärung, wenn der Inhaber des älteren Rechts der Eintragung zustimmt."),
        ("6", "Mitgliedstaaten können abweichend vorsehen, dass vor Inkrafttreten der Umsetzungsvorschriften der RL 89/104/EWG geltende Gründe weiter anwendbar sind.")],
        umsetzung=["§ 9", "§ 10", "§ 11", "§ 12", "§ 13", "§ 42", "§ 51", "§ 125b"], concepts=["relative_schutzhindernisse", "verwechslungsgefahr", "doppelidentitaet", "relative_schutzhindernis_bekannt", "bekanntheit_union", "prioritaet"],
        cases=["eugh_sabel_puma", "eugh_canon", "eugh_thomson_life", "bgh_springender_pudel", "eugh_iron_smith"],
        hinweis="Der Bekanntheitsschutz im Register ist jetzt zwingend und gilt ausdrücklich auch bei identischen und ähnlichen Waren; § 9 Abs. 1 Nr. 3 MarkenG wurde entsprechend geändert (Streichung von „nicht ähnlich“)."),
    art(6, "Nachträgliche Feststellung der Ungültigkeit oder des Verfalls einer Marke", K2, "Abschnitt 2 – Eintragungshindernisse und Ungültigkeitsgründe", [
        (None, "Wurde für eine Unionsmarke die Seniorität einer nationalen Marke in Anspruch genommen, auf die verzichtet wurde oder die erloschen ist, kann die Ungültigkeit oder der Verfall dieser nationalen Marke nachträglich festgestellt werden, sofern die Voraussetzungen schon im Zeitpunkt des Verzichts oder Erlöschens vorlagen; die Seniorität entfällt dann.")],
        umsetzung=["§ 125c"], concepts=["senioritaet", "unionsmarke"]),
    art(7, "Eintragungshindernisse und Ungültigkeitsgründe nur für einen Teil der Waren oder Dienstleistungen", K2, "Abschnitt 2 – Eintragungshindernisse und Ungültigkeitsgründe", [
        (None, "Liegt ein Hindernis nur für einen Teil der Waren oder Dienstleistungen vor, wird die Marke nur für diesen Teil zurückgewiesen oder für ungültig erklärt.")],
        umsetzung=["§ 37 Abs. 5", "§ 51 Abs. 5", "§ 50"], concepts=["absolute_schutzhindernisse", "nichtigkeit"]),
    art(8, "Fehlende Unterscheidungskraft oder Bekanntheit einer älteren Marke als Hindernis für die Nichtigerklärung einer eingetragenen Marke", K2, "Abschnitt 2 – Eintragungshindernisse und Ungültigkeitsgründe", [
        (None, "Ein Antrag auf Nichtigerklärung aufgrund einer älteren Marke ist erfolglos, wenn er am Anmelde- oder Prioritätstag der jüngeren Marke erfolglos gewesen wäre, weil (a) die ältere Marke damals nach Art. 4 Abs. 1 lit. b, c oder d für ungültig erklärt werden konnte und noch keine Unterscheidungskraft erlangt hatte, (b) noch keine Verwechslungsgefahr bestand, weil die ältere Marke noch nicht hinreichend unterscheidungskräftig war, oder (c) die ältere Marke noch nicht bekannt war.")],
        umsetzung=["§ 51 Abs. 3", "§ 51 Abs. 4", "§ 22"], concepts=["koexistenz_22", "relative_schutzhindernis_bekannt", "kennzeichnungskraft"],
        hinweis="Maßgeblicher Zeitpunkt für Kennzeichnungskraft und Bekanntheit der älteren Marke ist der Prioritätstag der jüngeren Marke (§ 51 Abs. 3, Abs. 4 S. 2 MarkenG)."),
    art(9, "Verwirkung durch Duldung", K2, "Abschnitt 2 – Eintragungshindernisse und Ungültigkeitsgründe", [
        ("1", "Hat der Inhaber einer älteren Marke die Benutzung einer jüngeren eingetragenen Marke fünf aufeinanderfolgende Jahre in Kenntnis geduldet, kann er weder die Nichtigkeit der jüngeren Marke geltend machen noch ihrer Benutzung widersprechen, es sei denn, die jüngere Marke wurde bösgläubig angemeldet."),
        ("2", "Die Mitgliedstaaten können dies auf sonstige ältere Rechte nach Art. 5 Abs. 4 lit. a und b erstrecken."),
        ("3", "Auch der Inhaber der jüngeren Marke kann sich der Benutzung des älteren Rechts nicht widersetzen, obwohl dieses nicht mehr gegen die jüngere Marke geltend gemacht werden kann.")],
        umsetzung=["§ 21", "§ 51 Abs. 2"], concepts=["verwirkung"], cases=["bgh_hard_rock_cafe"]),

    # ---------------- Kapitel 2, Abschnitt 3 ----------------
    art(10, "Rechte aus der Marke", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        ("1", "Die Eintragung gewährt dem Inhaber ein ausschließliches Recht."),
        ("2", "Unbeschadet älterer Rechte kann der Inhaber Dritten verbieten, ohne seine Zustimmung im geschäftlichen Verkehr für Waren oder Dienstleistungen ein Zeichen zu benutzen, (a) das mit der Marke identisch ist und für identische Waren benutzt wird; (b) das mit der Marke identisch oder ähnlich ist und für identische oder ähnliche Waren benutzt wird, wenn Verwechslungsgefahr einschließlich der Gefahr gedanklicher Verbindung besteht; (c) das mit der Marke identisch oder ähnlich ist, wenn die Marke im Mitgliedstaat bekannt ist und die Benutzung ihre Unterscheidungskraft oder Wertschätzung ohne rechtfertigenden Grund unlauter ausnutzt oder beeinträchtigt, unabhängig von der Waren(un)ähnlichkeit."),
        ("3", "Verboten werden können insbesondere: (a) Anbringen auf Waren oder Verpackungen; (b) Anbieten, Inverkehrbringen, Besitz zu diesen Zwecken, Anbieten oder Erbringen von Dienstleistungen; (c) Einfuhr oder Ausfuhr; (d) Benutzung als Handelsname oder Unternehmensbezeichnung oder als Teil davon; (e) Benutzung in Geschäftspapieren und Werbung; (f) Benutzung in vergleichender Werbung entgegen der RL 2006/114/EG."),
        ("4", "Der Inhaber kann verhindern, dass Dritte Waren aus Drittstaaten, die ohne Zustimmung mit einer identischen (oder in wesentlichen Aspekten nicht unterscheidbaren) Marke versehen sind, in den Mitgliedstaat verbringen, ohne sie dort in den Verkehr zu bringen (Transit); das Recht erlischt, wenn der Anmelder oder Besitzer im Verletzungsverfahren nachweist, dass der Inhaber im Bestimmungsland die Vermarktung nicht verbieten könnte."),
        ("5", "Konnte nach dem Recht des Mitgliedstaats die Benutzung vor Inkrafttreten der Umsetzungsvorschriften der RL 89/104/EWG nicht verboten werden, kann sie auch jetzt nicht verboten werden."),
        ("6", "Die Absätze 1, 2, 3 und 5 lassen Vorschriften über den Schutz gegen Benutzung zu anderen Zwecken als der Unterscheidung von Waren unberührt, wenn die Benutzung die Unterscheidungskraft oder Wertschätzung unlauter ausnutzt oder beeinträchtigt.")],
        umsetzung=["§ 14 Abs. 1", "§ 14 Abs. 2", "§ 14 Abs. 3", "§ 14a", "§ 15"], concepts=["doppelidentitaet", "verwechslungsgefahr", "bekannte_marke", "markenmaessige_benutzung", "markenfunktionen", "transit", "firmenmaessiger_gebrauch"],
        cases=["eugh_arsenal", "eugh_loreal_bellure", "eugh_google_france", "eugh_celine", "eugh_general_motors", "eugh_intel"],
        hinweis="Kern der Harmonisierung. Neu: Transitverbot (§ 14a MarkenG), Benutzung als Unternehmensbezeichnung ausdrücklich als Verletzungshandlung (§ 14 Abs. 3 Nr. 5), Bekanntheitsschutz zwingend und für alle Waren (§ 14 Abs. 2 Nr. 3). Die Funktionenlehre des EuGH (Herkunfts-, Werbe-, Investitionsfunktion) ist Auslegung dieses Artikels."),
    art(11, "Recht, Vorbereitungshandlungen im Zusammenhang mit der Benutzung von Aufmachungen oder anderen Kennzeichnungsmitteln zu verbieten", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        (None, "Besteht die Gefahr, dass Aufmachungen, Verpackungen, Etiketten, Anhänger, Sicherheits- oder Echtheitshinweise, auf denen die Marke angebracht ist, für Waren benutzt werden und dies eine Verletzung wäre, kann der Inhaber verbieten: (a) das Anbringen der Marke auf solchen Kennzeichnungsmitteln, (b) das Anbieten, Inverkehrbringen, Besitzen, Ein- oder Ausführen solcher Kennzeichnungsmittel.")],
        umsetzung=["§ 14 Abs. 4"], concepts=["vorbereitungshandlungen"],
        hinweis="Vorverlagerung des Schutzes gegen Produktpiraterie; § 14 Abs. 4 MarkenG wurde um Sicherheits- und Echtheitshinweise erweitert."),
    art(12, "Wiedergabe von Marken in Wörterbüchern", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        (None, "Erweckt die Wiedergabe einer Marke in einem Wörterbuch, Lexikon oder ähnlichen Nachschlagewerk den Eindruck, es handle sich um eine Gattungsbezeichnung, muss der Verleger auf Verlangen des Inhabers unverzüglich, bei Druckwerken spätestens in der nächsten Auflage, kenntlich machen, dass es sich um eine eingetragene Marke handelt.")],
        umsetzung=["§ 16"], concepts=["uebliche_bezeichnung", "nachschlagewerke"]),
    art(13, "Untersagung der Benutzung einer Marke, die für einen Agenten oder Vertreter eingetragen ist", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        ("1", "Wurde eine Marke ohne Zustimmung des Inhabers auf den Namen seines Agenten oder Vertreters eingetragen, kann der Inhaber der Benutzung widersprechen, es sei denn, der Agent rechtfertigt seine Handlung; außerdem kann er die Übertragung der Eintragung auf sich verlangen."),
        ("2", "Das Recht besteht nur, wenn der Agent oder Vertreter die Handlung nicht rechtfertigen kann.")],
        umsetzung=["§ 11", "§ 17"], concepts=["agentenmarke"]),
    art(14, "Beschränkung der Wirkungen der Marke", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        ("1", "Die Marke gewährt nicht das Recht, Dritten zu verbieten, im geschäftlichen Verkehr zu benutzen: (a) den Namen oder die Anschrift des Dritten, wenn dieser eine natürliche Person ist; (b) Zeichen ohne Unterscheidungskraft oder Angaben über Art, Beschaffenheit, Menge, Bestimmung, Wert, geographische Herkunft, Zeit der Herstellung oder andere Merkmale; (c) die Marke zu Zwecken der Identifizierung oder zum Verweis auf Waren des Inhabers, insbesondere wenn dies als Hinweis auf die Bestimmung einer Ware als Zubehör oder Ersatzteil notwendig ist."),
        ("2", "Abs. 1 gilt nur, wenn die Benutzung den anständigen Gepflogenheiten in Gewerbe oder Handel entspricht."),
        ("3", "Die Marke gewährt nicht das Recht, einem Dritten die Benutzung eines älteren Rechts von örtlicher Bedeutung zu verbieten, wenn dieses Recht nach dem Recht des Mitgliedstaats anerkannt ist, in den Grenzen des Gebiets, in dem es anerkannt ist.")],
        umsetzung=["§ 23"], concepts=["schranke_23", "ersatzteilhinweis", "gleichnamigkeit"], cases=["eugh_gillette", "bgh_kuehlergrill", "bgh_staubsaugerfiltertueten"],
        hinweis="Neu: Die Namensschranke gilt nur noch für natürliche Personen (§ 23 Abs. 1 Nr. 1 MarkenG); die referierende Benutzung („zu Zwecken der Identifizierung oder des Verweises“) ist ausdrücklich privilegiert."),
    art(15, "Erschöpfung des Rechts aus der Marke", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        ("1", "Die Marke gewährt nicht das Recht, die Benutzung für Waren zu verbieten, die unter dieser Marke vom Inhaber oder mit seiner Zustimmung in der Union in den Verkehr gebracht worden sind."),
        ("2", "Abs. 1 gilt nicht, wenn berechtigte Gründe es rechtfertigen, dass der Inhaber sich dem weiteren Vertrieb widersetzt, insbesondere wenn der Zustand der Waren nach dem Inverkehrbringen verändert oder verschlechtert ist.")],
        umsetzung=["§ 24"], concepts=["erschoepfung", "berechtigte_gruende", "beweislast_erschoepfung", "umverpackung"], cases=["eugh_van_doren", "eugh_bms", "eugh_dior_evora"],
        hinweis="Unionsweite (EWR-weite) Erschöpfung; keine internationale Erschöpfung (EuGH Silhouette). Die Beweislastregeln (Van Doren) und die BMS-Kriterien konkretisieren Abs. 1 und 2."),
    art(16, "Benutzung der Marke", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        ("1", "Hat der Inhaber die Marke binnen fünf Jahren nach Abschluss des Eintragungsverfahrens nicht ernsthaft im Mitgliedstaat für die eingetragenen Waren benutzt oder die Benutzung fünf Jahre ausgesetzt, unterliegt die Marke den Beschränkungen und Sanktionen der Art. 17, 19 Abs. 1, 44 Abs. 1 und 2 sowie 46 Abs. 3 und 4, sofern keine berechtigten Gründe vorliegen."),
        ("2", "Sieht ein Mitgliedstaat ein Widerspruchsverfahren nach der Eintragung vor, beginnt die Fünfjahresfrist mit dem Tag, ab dem kein Widerspruch mehr möglich ist oder das Widerspruchsverfahren abgeschlossen ist."),
        ("3", "Bei international registrierten Marken mit Wirkung im Mitgliedstaat beginnt die Frist mit dem Tag, ab dem die Marke nicht mehr zurückgewiesen oder ihr nicht mehr widersprochen werden kann, bzw. mit Abschluss des Verfahrens."),
        ("4", "Der Tag des Fristbeginns wird im Register vermerkt."),
        ("5", "Als Benutzung gilt auch (a) die Benutzung in einer nur in unwesentlichen Bestandteilen abweichenden Form, die den kennzeichnenden Charakter nicht verändert, unabhängig davon, ob die abweichende Form ebenfalls eingetragen ist, und (b) das Anbringen der Marke auf Waren oder Verpackungen ausschließlich für den Export."),
        ("6", "Die Benutzung mit Zustimmung des Inhabers gilt als Benutzung durch den Inhaber.")],
        umsetzung=["§ 26", "§ 25", "§ 115", "§ 116", "§ 117"], concepts=["rechtserhaltende_benutzung", "ernsthafte_benutzung", "abweichende_form", "benutzungsschonfrist", "ir_benutzungsschonfrist"], cases=["eugh_ansul", "bgh_voodoo", "bgh_dorzo", "bgh_probiotik"],
        hinweis="Die Schonfrist beginnt jetzt mit dem Abschluss des Widerspruchsverfahrens (§ 26 Abs. 5 MarkenG neu); Benutzung in abweichender Form ist auch dann rechtserhaltend, wenn die abweichende Form selbst eingetragen ist (§ 26 Abs. 3 S. 2)."),
    art(17, "Einrede der Nichtbenutzung in Verletzungsverfahren", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        (None, "Der Inhaber kann die Benutzung eines Zeichens nur verbieten, soweit seine Rechte zum Zeitpunkt der Klageerhebung nicht nach Art. 19 für verfallen erklärt werden könnten; auf Verlangen des Beklagten muss der Inhaber nachweisen, dass die Marke in den fünf Jahren vor Klageerhebung ernsthaft benutzt wurde oder berechtigte Gründe vorliegen, sofern die Schonfrist bei Klageerhebung abgelaufen war.")],
        umsetzung=["§ 25"], concepts=["nichtbenutzungseinrede"], cases=["bgh_voodoo"]),
    art(18, "Zwischenrecht des Inhabers einer später eingetragenen Marke als Einwand in Verletzungsverfahren", K2, "Abschnitt 3 – Rechte aus der Marke und Beschränkungen", [
        ("1", "Der Inhaber kann die Benutzung einer später eingetragenen Marke nicht verbieten, wenn diese jüngere Marke nach Art. 8, Art. 9 Abs. 1 oder 2 oder Art. 46 Abs. 3 nicht für ungültig erklärt werden könnte."),
        ("2", "Ebenso nicht, wenn die jüngere Unionsmarke nach Art. 53 Abs. 1, 3 oder 4, Art. 54 Abs. 1 oder 2 oder Art. 57 Abs. 2 UMV nicht für nichtig erklärt werden könnte."),
        ("3", "Kann der Inhaber der älteren Marke die Benutzung der jüngeren Marke danach nicht verbieten, kann auch deren Inhaber die Benutzung der älteren Marke nicht verbieten, obwohl diese nicht mehr gegen die jüngere geltend gemacht werden kann.")],
        umsetzung=["§ 22"], concepts=["koexistenz_22"],
        hinweis="Übernahme des unionsmarkenrechtlichen Zwischenrechts (Art. 16 UMV) in das nationale Recht; § 22 MarkenG wurde neu gefasst."),

    # ---------------- Kapitel 2, Abschnitt 4 ----------------
    art(19, "Nichtbenutzung als Verfallsgrund", K2, "Abschnitt 4 – Verfall", [
        ("1", "Eine Marke wird für verfallen erklärt, wenn sie innerhalb von fünf aufeinanderfolgenden Jahren nicht ernsthaft im Mitgliedstaat für die eingetragenen Waren benutzt wurde und keine berechtigten Gründe vorliegen."),
        ("2", "Der Verfall kann nicht geltend gemacht werden, wenn die Benutzung zwischen Ablauf der fünf Jahre und Antragstellung ernsthaft begonnen oder wieder aufgenommen wurde."),
        ("3", "Eine Aufnahme oder Wiederaufnahme innerhalb von drei Monaten vor Antragstellung, frühestens nach Ablauf der fünf Jahre, bleibt unberücksichtigt, wenn die Vorbereitungen erst begannen, nachdem der Inhaber vom möglichen Antrag Kenntnis erlangt hatte.")],
        umsetzung=["§ 49 Abs. 1"], concepts=["verfall", "benutzungsschonfrist", "ernsthafte_benutzung"], cases=["eugh_ansul", "bgh_voodoo"]),
    art(20, "Entwicklung zu einer gebräuchlichen Bezeichnung oder irreführende Angabe als Verfallsgrund", K2, "Abschnitt 4 – Verfall", [
        (None, "Eine Marke wird für verfallen erklärt, wenn sie nach der Eintragung (a) infolge des Verhaltens oder der Untätigkeit des Inhabers zur gebräuchlichen Bezeichnung einer Ware oder Dienstleistung geworden ist, für die sie eingetragen ist, oder (b) infolge ihrer Benutzung durch den Inhaber oder mit seiner Zustimmung geeignet ist, das Publikum insbesondere über Art, Beschaffenheit oder geographische Herkunft irrezuführen.")],
        umsetzung=["§ 49 Abs. 2"], concepts=["uebliche_bezeichnung", "taeuschung", "verfall"], cases=["bgh_tuev_ii"]),
    art(21, "Verfall nur für einen Teil der Waren oder Dienstleistungen", K2, "Abschnitt 4 – Verfall", [
        (None, "Liegt ein Verfallsgrund nur für einen Teil der Waren oder Dienstleistungen vor, wird die Marke nur für diesen Teil für verfallen erklärt.")],
        umsetzung=["§ 49 Abs. 3"], concepts=["verfall"]),

    # ---------------- Kapitel 2, Abschnitt 5 ----------------
    art(22, "Rechtsübergang eingetragener Marken", K2, "Abschnitt 5 – Marken als Gegenstand des Vermögens", [
        ("1", "Die Marke kann unabhängig vom Unternehmen für alle oder einen Teil der Waren übertragen werden."),
        ("2", "Der Übergang des gesamten Unternehmens erfasst die Marke, sofern nichts anderes vereinbart ist oder sich aus den Umständen ergibt."),
        ("3", "Die Mitgliedstaaten sehen Verfahren zur Eintragung des Rechtsübergangs im Register vor.")],
        umsetzung=["§ 27"], concepts=["lizenz", "aktivlegitimation"]),
    art(23, "Dingliche Rechte", K2, "Abschnitt 5 – Marken als Gegenstand des Vermögens", [
        ("1", "Die Marke kann unabhängig vom Unternehmen verpfändet oder Gegenstand eines sonstigen dinglichen Rechts sein."),
        ("2", "Die Mitgliedstaaten sehen Verfahren zur Eintragung dinglicher Rechte im Register vor.")],
        umsetzung=["§ 29"], concepts=[]),
    art(24, "Zwangsvollstreckung", K2, "Abschnitt 5 – Marken als Gegenstand des Vermögens", [
        ("1", "Die Marke kann Gegenstand von Maßnahmen der Zwangsvollstreckung sein."),
        ("2", "Die Mitgliedstaaten sehen Verfahren zur Eintragung der Zwangsvollstreckung im Register vor.")],
        umsetzung=["§ 29"], concepts=[]),
    art(25, "Lizenz", K2, "Abschnitt 5 – Marken als Gegenstand des Vermögens", [
        ("1", "Die Marke kann für alle oder einen Teil der Waren und für das gesamte Gebiet oder einen Teil des Mitgliedstaats Gegenstand ausschließlicher oder nicht ausschließlicher Lizenzen sein."),
        ("2", "Der Inhaber kann die Marke gegen einen Lizenznehmer geltend machen, der gegen Bestimmungen des Lizenzvertrags über Dauer, Form der Benutzung, Art der Waren, Gebiet oder Qualität verstößt."),
        ("3", "Der Lizenznehmer kann Verletzungsklage nur mit Zustimmung des Inhabers erheben; der ausschließliche Lizenznehmer auch ohne Zustimmung, wenn der Inhaber nach förmlicher Aufforderung nicht innerhalb angemessener Frist selbst klagt."),
        ("4", "Jeder Lizenznehmer kann einer Verletzungsklage des Inhabers beitreten, um eigenen Schaden geltend zu machen."),
        ("5", "Die Mitgliedstaaten sehen Verfahren zur Eintragung von Lizenzen im Register vor.")],
        umsetzung=["§ 30"], concepts=["lizenz", "erschoepfung"], cases=["bgh_converse_ii"],
        hinweis="Abs. 2 ist der unionsrechtliche Hintergrund des § 30 Abs. 2 MarkenG: Ein Lizenzverstoß in diesen Punkten schließt die Zustimmung und damit die Erschöpfung aus (EuGH Copad, BGH Converse II)."),
    art(26, "Anmeldung einer Marke als Gegenstand des Vermögens", K2, "Abschnitt 5 – Marken als Gegenstand des Vermögens", [
        (None, "Die Art. 22 bis 25 gelten auch für Markenanmeldungen.")],
        umsetzung=["§ 31"], concepts=[]),

    # ---------------- Kapitel 2, Abschnitt 6 ----------------
    art(27, "Begriffsbestimmungen", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("a", "„Garantie- oder Gewährleistungsmarke“: Marke, die geeignet ist, Waren oder Dienstleistungen, für die der Inhaber Material, Herstellungsart, Qualität, Genauigkeit oder andere Eigenschaften gewährleistet, von nicht gewährleisteten zu unterscheiden."),
        ("b", "„Kollektivmarke“: Marke, die geeignet ist, Waren oder Dienstleistungen der Mitglieder eines Verbands von denen anderer Unternehmen zu unterscheiden.")],
        umsetzung=["§ 97", "§ 106a"], concepts=["kollektivmarke"]),
    art(28, "Garantie- oder Gewährleistungsmarken", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("1", "Die Mitgliedstaaten können die Eintragung von Garantie- oder Gewährleistungsmarken vorsehen."),
        ("2", "Anmelden kann jede natürliche oder juristische Person einschließlich Einrichtungen des öffentlichen Rechts, sofern sie keine Waren der gewährleisteten Art selbst anbietet."),
        ("3", "Abweichend von Art. 4 Abs. 1 lit. c können beschreibende Herkunftsangaben Gewährleistungsmarken sein; der Inhaber kann Dritten die redliche Benutzung solcher Angaben nicht verbieten."),
        ("4", "Die Mitgliedstaaten können zusätzliche Verfalls- und Ungültigkeitsgründe vorsehen."),
        ("5", "Die Benutzung durch eine berechtigte Person gilt als rechtserhaltend.")],
        umsetzung=["§ 106a", "§ 106b", "§ 106c", "§ 106d"], concepts=["kollektivmarke"], cases=["bgh_oeko_test_ii"],
        hinweis="Deutschland hat die Option genutzt: Gewährleistungsmarke seit dem MaMoG in §§ 106a ff. MarkenG (Prüf- und Gütesiegel)."),
    art(29, "Kollektivmarken", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("1", "Die Mitgliedstaaten sehen die Eintragung von Kollektivmarken vor."),
        ("2", "Anmelden können Verbände von Herstellern, Erzeugern, Dienstleistern oder Händlern mit Rechtsfähigkeit sowie juristische Personen des öffentlichen Rechts."),
        ("3", "Abweichend von Art. 4 Abs. 1 lit. c können geographische Herkunftsangaben Kollektivmarken sein; der Inhaber kann Dritten die redliche Benutzung, insbesondere durch ortsansässige Berechtigte, nicht verbieten.")],
        umsetzung=["§ 97", "§ 98", "§ 99", "§ 100"], concepts=["kollektivmarke", "geographische_herkunftsangabe"]),
    art(30, "Satzung der Kollektivmarke", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("1", "Der Anmelder legt dem Amt die Markensatzung vor."),
        ("2", "Die Satzung nennt die zur Benutzung befugten Personen, die Voraussetzungen der Mitgliedschaft und der Benutzung sowie Sanktionen; bei geographischen Angaben muss jeder Ortsansässige, der die Voraussetzungen erfüllt, Mitglied werden können.")],
        umsetzung=["§ 102"], concepts=["kollektivmarke"]),
    art(31, "Zurückweisung der Anmeldung", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("1", "Neben den Gründen der Art. 4 und 5 wird die Anmeldung zurückgewiesen, wenn Art. 27 lit. b, 29 oder 30 nicht erfüllt sind oder die Satzung gegen die öffentliche Ordnung oder die guten Sitten verstößt."),
        ("2", "Zurückweisung auch, wenn das Publikum über Charakter oder Bedeutung der Marke irregeführt werden kann, insbesondere wenn sie nicht als Kollektivmarke erscheint."),
        ("3", "Die Anmeldung wird nicht zurückgewiesen, wenn der Anmelder die Satzung so ändert, dass die Voraussetzungen erfüllt sind.")],
        umsetzung=["§ 103"], concepts=["kollektivmarke"]),
    art(32, "Benutzung von Kollektivmarken", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        (None, "Art. 16 ist erfüllt, wenn eine zur Benutzung befugte Person die Kollektivmarke ernsthaft benutzt.")],
        umsetzung=["§ 100 Abs. 2"], concepts=["kollektivmarke", "rechtserhaltende_benutzung"]),
    art(33, "Änderung der Satzung der Kollektivmarke", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("1", "Der Inhaber legt jede geänderte Satzung dem Amt vor."),
        ("2", "Die Änderung wird im Register vermerkt, sofern sie den Anforderungen des Art. 30 entspricht und keinen Zurückweisungsgrund nach Art. 31 begründet."),
        ("3", "Die Änderung wird erst mit dem Registervermerk wirksam.")],
        umsetzung=["§ 104"], concepts=["kollektivmarke"]),
    art(34, "Klagebefugnis", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        ("1", "Art. 25 Abs. 3 und 4 gelten für zur Benutzung Befugte entsprechend."),
        ("2", "Der Inhaber kann im Namen der Benutzungsberechtigten Ersatz des Schadens verlangen, der diesen durch unberechtigte Benutzung entstanden ist.")],
        umsetzung=["§ 101", "§ 106c"], concepts=["kollektivmarke", "schadensersatz"]),
    art(35, "Zusätzliche Verfallsgründe", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        (None, "Zusätzlich zu Art. 19 und 20 wird die Kollektivmarke für verfallen erklärt, wenn (a) der Inhaber keine angemessenen Maßnahmen gegen satzungswidrige Benutzung trifft, (b) die Benutzung durch Befugte das Publikum nach Art. 31 Abs. 2 irreführen kann, oder (c) eine Satzungsänderung entgegen Art. 33 Abs. 2 im Register vermerkt wurde, es sei denn, der Inhaber erfüllt die Anforderungen durch erneute Änderung.")],
        umsetzung=["§ 105", "§ 106g"], concepts=["kollektivmarke", "verfall"]),
    art(36, "Zusätzliche Ungültigkeitsgründe", K2, "Abschnitt 6 – Garantie- oder Gewährleistungsmarken und Kollektivmarken", [
        (None, "Zusätzlich zu Art. 4 und 5 wird eine entgegen Art. 31 eingetragene Kollektivmarke für ungültig erklärt, es sei denn, der Inhaber erfüllt die Anforderungen durch Satzungsänderung.")],
        umsetzung=["§ 106", "§ 106h"], concepts=["kollektivmarke", "nichtigkeit"]),

    # ---------------- Kapitel 3 ----------------
    art(37, "Anmeldeerfordernisse", K3, "Abschnitt 1 – Anmeldung und Eintragung", [
        ("1", "Die Anmeldung enthält mindestens: (a) einen Antrag auf Eintragung, (b) Angaben zur Identität des Anmelders, (c) das Verzeichnis der Waren und Dienstleistungen, (d) eine Wiedergabe der Marke nach Art. 3 lit. b."),
        ("2", "Die Anmeldung unterliegt einer Gebühr.")],
        umsetzung=["§ 32"], concepts=["entstehung_markenschutz", "darstellbarkeit"]),
    art(38, "Anmeldetag", K3, "Abschnitt 1 – Anmeldung und Eintragung", [
        ("1", "Anmeldetag ist der Tag, an dem die Unterlagen nach Art. 37 Abs. 1 beim Amt eingereicht werden."),
        ("2", "Die Mitgliedstaaten können die Zuerkennung des Anmeldetags zusätzlich von der Zahlung der Gebühr abhängig machen.")],
        umsetzung=["§ 33"], concepts=["prioritaet", "entstehung_markenschutz"]),
    art(39, "Bezeichnung und Klassifizierung von Waren und Dienstleistungen", K3, "Abschnitt 1 – Anmeldung und Eintragung", [
        ("1", "Die Waren und Dienstleistungen werden nach der Nizza-Klassifikation klassifiziert."),
        ("2", "Sie sind so klar und eindeutig anzugeben, dass Behörden und Wirtschaftsteilnehmer den Schutzumfang bestimmen können."),
        ("3", "Zulässig sind die allgemeinen Begriffe der Klassenüberschriften, sofern sie hinreichend klar sind."),
        ("4", "Zu unklare Angaben weist das Amt zurück, wenn der Anmelder nicht binnen Frist nachbessert."),
        ("5", "Allgemeine Begriffe, einschließlich der Klassenüberschriften, umfassen nur die Waren und Dienstleistungen, die eindeutig von ihrer wörtlichen Bedeutung erfasst sind (Klarstellung nach EuGH IP Translator)."),
        ("6", "Bei Klassenüberschriften wird nicht vermutet, dass alle Waren der Klasse beansprucht sind."),
        ("7", "Waren gelten nicht schon deshalb als ähnlich, weil sie derselben Klasse angehören, und nicht als unähnlich, weil sie verschiedenen Klassen angehören.")],
        umsetzung=["§ 32 Abs. 3", "§ 9 Abs. 3", "§ 65"], concepts=["klassifizierung", "warenaehnlichkeit"],
        hinweis="Abs. 7 entspricht § 9 Abs. 3 MarkenG; Abs. 5 kodifiziert die IP-Translator-Rechtsprechung (EuGH C-307/10)."),
    art(40, "Bemerkungen Dritter", K3, "Abschnitt 1 – Anmeldung und Eintragung", [
        ("1", "Die Mitgliedstaaten können vorsehen, dass Dritte vor der Eintragung schriftliche Bemerkungen zu absoluten Eintragungshindernissen einreichen, ohne am Verfahren beteiligt zu werden."),
        ("2", "Bei Kollektiv- und Gewährleistungsmarken können sich Bemerkungen auch auf Art. 31 beziehen.")],
        umsetzung=["§ 37 Abs. 6"], concepts=["absolute_schutzhindernisse"]),
    art(41, "Teilung von Anmeldungen und Eintragungen", K3, "Abschnitt 1 – Anmeldung und Eintragung", [
        (None, "Der Anmelder oder Inhaber kann die Anmeldung oder Eintragung in zwei oder mehr Teile teilen.")],
        umsetzung=["§ 40", "§ 46"], concepts=[]),
    art(42, "Klassengebühren", K3, "Abschnitt 1 – Anmeldung und Eintragung", [
        (None, "Die Mitgliedstaaten können für Anmeldung und Verlängerung eine zusätzliche Gebühr je Klasse jenseits der ersten Klasse vorsehen.")],
        umsetzung=["§ 32 Abs. 4"], concepts=[]),
    art(43, "Widerspruchsverfahren", K3, "Abschnitt 2 – Verfahren für Widerspruch, Verfall und Nichtigkeit", [
        ("1", "Die Mitgliedstaaten sehen ein effizientes und zügiges Verwaltungsverfahren vor, mit dem gegen die Anmeldung auf Grundlage der Gründe des Art. 5 Widerspruch erhoben werden kann."),
        ("2", "Widerspruch kann zumindest der Inhaber einer älteren Marke nach Art. 5 Abs. 2 und Abs. 3 lit. a sowie der Berechtigte einer Ursprungsbezeichnung erheben; ein Widerspruch kann auf mehrere ältere Rechte desselben Inhabers gestützt werden und sich gegen einen Teil der Waren richten."),
        ("3", "Den Parteien wird auf gemeinsamen Antrag eine Frist von mindestens zwei Monaten für eine gütliche Einigung eingeräumt (Cooling-off).")],
        umsetzung=["§ 42"], concepts=["widerspruch", "relative_schutzhindernisse"],
        hinweis="Umsetzung: § 42 Abs. 2 (Widerspruchsberechtigte, jetzt auch bekannte Marken ausdrücklich), Abs. 3 (mehrere ältere Rechte), Abs. 4 (Cooling-off von mindestens zwei Monaten)."),
    art(44, "Nichtbenutzung als Einrede im Widerspruchsverfahren", K3, "Abschnitt 2 – Verfahren für Widerspruch, Verfall und Nichtigkeit", [
        ("1", "War die Schonfrist der älteren Marke am Anmelde- oder Prioritätstag der jüngeren Marke abgelaufen, muss der Widersprechende auf Verlangen des Anmelders nachweisen, dass die ältere Marke in den fünf Jahren vor diesem Tag ernsthaft benutzt wurde oder berechtigte Gründe vorlagen; sonst wird der Widerspruch zurückgewiesen."),
        ("2", "Bei nur teilweiser Benutzung gilt die ältere Marke für die Prüfung nur für die benutzten Waren als eingetragen."),
        ("3", "Bei älteren Unionsmarken bestimmt sich die ernsthafte Benutzung nach Art. 15 (jetzt Art. 18) UMV.")],
        umsetzung=["§ 43 Abs. 1", "§ 125b"], concepts=["nichtbenutzungseinrede", "benutzung_union"], cases=["eugh_leno_merken"],
        hinweis="Maßgeblicher Fünfjahreszeitraum ist der vor dem Anmelde-/Prioritätstag der jüngeren Marke (§ 43 Abs. 1 S. 1 MarkenG neu)."),
    art(45, "Verfahren zur Erklärung des Verfalls oder der Nichtigkeit", K3, "Abschnitt 2 – Verfahren für Widerspruch, Verfall und Nichtigkeit", [
        ("1", "Unbeschadet gerichtlicher Verfahren sehen die Mitgliedstaaten ein effizientes und zügiges Verwaltungsverfahren vor den Ämtern für die Erklärung des Verfalls oder der Nichtigkeit vor."),
        ("2", "Das Verfahren muss Verfall nach Art. 19 und 20 sowie Nichtigkeit nach Art. 4 und 5 ermöglichen."),
        ("3", "Antragsbefugt sind mindestens: (a) bei Verfall und absoluten Ungültigkeitsgründen jede natürliche oder juristische Person sowie Verbände; (b) bei relativen Gründen die Inhaber der älteren Rechte."),
        ("4", "Der Antrag kann sich gegen einen Teil der Waren richten."),
        ("5", "Er kann auf mehrere ältere Rechte desselben Inhabers gestützt werden."),
        ("6", "Bei Nichtigkeit aufgrund einer Unionsmarke gilt für deren Benutzung Art. 15 (jetzt Art. 18) UMV.")],
        umsetzung=["§ 53", "§ 54", "§ 55"], concepts=["verfall", "nichtigkeit", "verwaltungsverfahren_loeschung"],
        hinweis="Umsetzungsfrist bis 14. Januar 2023 (Art. 54 Abs. 1 UAbs. 2). Deutschland: seit 1.5.2020 vollständiges Verfalls- und Nichtigkeitsverfahren vor dem DPMA (§ 53 MarkenG), daneben Klage nach § 55 nur noch für Verfall und relative Nichtigkeit."),
    art(46, "Nichtbenutzung als Einrede in Verfahren zur Erklärung der Nichtigkeit", K3, "Abschnitt 2 – Verfahren für Widerspruch, Verfall und Nichtigkeit", [
        ("1", "Der Inhaber der jüngeren Marke kann verlangen, dass der Antragsteller die ernsthafte Benutzung seiner älteren Marke in den fünf Jahren vor Antragstellung nachweist, wenn deren Schonfrist bei Antragstellung abgelaufen war."),
        ("2", "War die Schonfrist bereits am Anmelde- oder Prioritätstag der jüngeren Marke abgelaufen, muss zusätzlich die Benutzung in den fünf Jahren vor diesem Tag nachgewiesen werden."),
        ("3", "Ohne Nachweis wird der Antrag zurückgewiesen."),
        ("4", "Bei teilweiser Benutzung gilt die ältere Marke nur für die benutzten Waren als eingetragen."),
        ("5", "Bei älteren Unionsmarken gilt Art. 15 (jetzt Art. 18) UMV.")],
        umsetzung=["§ 53 Abs. 6", "§ 55 Abs. 3", "§ 125b"], concepts=["nichtbenutzungseinrede", "nichtigkeit"]),
    art(47, "Wirkungen des Verfalls und der Nichtigkeit", K3, "Abschnitt 2 – Verfahren für Widerspruch, Verfall und Nichtigkeit", [
        ("1", "Bei Verfall gelten die Wirkungen der Marke ab dem Tag der Antragstellung als nicht mehr eingetreten; auf Antrag kann ein früherer Zeitpunkt festgesetzt werden, zu dem der Verfallsgrund eintrat."),
        ("2", "Bei Nichtigkeit gelten die Wirkungen der Marke als von Anfang an nicht eingetreten.")],
        umsetzung=["§ 52"], concepts=["verfall", "nichtigkeit"]),
    art(48, "Schutzdauer", K3, "Abschnitt 3 – Schutzdauer und Verlängerung", [
        ("1", "Die Schutzdauer beträgt zehn Jahre ab dem Anmeldetag."),
        ("2", "Sie kann um jeweils zehn Jahre verlängert werden.")],
        umsetzung=["§ 47 Abs. 1", "§ 47 Abs. 2"], concepts=["schutzdauer"]),
    art(49, "Verlängerung", K3, "Abschnitt 3 – Schutzdauer und Verlängerung", [
        ("1", "Die Verlängerung erfolgt auf Antrag des Inhabers oder eines Bevollmächtigten gegen Gebühr; die Mitgliedstaaten können die Gebührenzahlung als Antrag gelten lassen."),
        ("2", "Das Amt unterrichtet den Inhaber mindestens sechs Monate vor Ablauf; eine unterbliebene Unterrichtung begründet keine Haftung."),
        ("3", "Antrag und Gebühr müssen innerhalb von mindestens sechs Monaten vor Ablauf eingehen; nachträglich innerhalb weiterer sechs Monate gegen Zuschlag."),
        ("4", "Die Verlängerung kann auf einen Teil der Waren beschränkt werden."),
        ("5", "Sie wird am Tag nach Ablauf der Schutzdauer wirksam und im Register vermerkt.")],
        umsetzung=["§ 47 Abs. 3", "§ 47 Abs. 4", "§ 47 Abs. 5"], concepts=["schutzdauer"],
        hinweis="Schutzdauer und Verlängerungsfristen laufen jetzt ab dem Anmeldetag, nicht mehr ab dem Monatsende (§ 47 MarkenG neu)."),
    art(50, "Kommunikation mit dem Amt", K3, "Abschnitt 4 – Kommunikation mit dem Amt", [
        (None, "Die Verfahrensbeteiligten oder ihre Vertreter geben eine amtliche Anschrift für die amtliche Kommunikation an; die Mitgliedstaaten können verlangen, dass sie im EWR liegt.")],
        umsetzung=["§ 96", "§ 94"], concepts=[]),

    # ---------------- Kapitel 4 ----------------
    art(51, "Zusammenarbeit im Bereich der Eintragung und Verwaltung von Marken", K4, None, [
        (None, "Die Ämter arbeiten untereinander und mit dem EUIPO zusammen, um Verfahren und Instrumente zu harmonisieren und Ergebnisse zu vereinheitlichen.")],
        umsetzung=["§ 65a"], concepts=["markenrl"]),
    art(52, "Zusammenarbeit in anderen Bereichen", K4, None, [
        (None, "Die Ämter können mit dem EUIPO auch in anderen Tätigkeitsbereichen zusammenarbeiten, etwa bei Sensibilisierung und Bekämpfung von Verletzungen.")],
        umsetzung=["§ 65a"], concepts=["markenrl"]),

    # ---------------- Kapitel 5 ----------------
    art(53, "Datenschutz", K5, None, [(None, "Für die Verarbeitung personenbezogener Daten gilt das nationale Datenschutzrecht in Umsetzung der RL 95/46/EG (heute DSGVO).")],
        umsetzung=["§ 62a"], concepts=[]),
    art(54, "Umsetzung", K5, None, [
        ("1", "Die Mitgliedstaaten setzen die Art. 3 bis 6, 8 bis 14, 16, 17, 18, 22 bis 39, 41 und 43 bis 50 bis zum 14. Januar 2019 um; Art. 45 bis zum 14. Januar 2023."),
        ("2", "Sie teilen der Kommission den Wortlaut der Umsetzungsvorschriften mit.")],
        umsetzung=["§ 158"], concepts=["markenrl"],
        hinweis="Deutschland: Markenrechtsmodernisierungsgesetz (MaMoG) vom 11.12.2018, BGBl. I S. 2357, in Kraft seit 14.1.2019; Verfalls-/Nichtigkeitsverfahren vor dem DPMA seit 1.5.2020."),
    art(55, "Aufhebung", K5, None, [(None, "Die Richtlinie 2008/95/EG wird mit Wirkung vom 15. Januar 2019 aufgehoben; Verweise gelten als Verweise auf diese Richtlinie (Entsprechungstabelle in Anhang).")],
        umsetzung=[], concepts=["markenrl"]),
    art(56, "Inkrafttreten", K5, None, [(None, "Die Richtlinie tritt am zwanzigsten Tag nach ihrer Veröffentlichung im Amtsblatt in Kraft; Art. 1, 7, 15, 19, 20, 21 und 54 bis 57 gelten ab dem 15. Januar 2019.")],
        umsetzung=[], concepts=["markenrl"]),
    art(57, "Adressaten", K5, None, [(None, "Die Richtlinie ist an die Mitgliedstaaten gerichtet.")],
        umsetzung=[], concepts=["markenrl"]),
]

# Ausgewählte Erwägungsgründe (paraphrasiert), die Auslegung und Lernstoff prägen.
ERWAEGUNGSGRUENDE = [
    dict(nr="1-3", text="Neufassung der RL 2008/95/EG; Ziel ist die weitere Angleichung des nationalen Markenrechts an das Unionsmarkensystem, weil verbleibende Unterschiede Hindernisse für den freien Warenverkehr und Wettbewerbsverzerrungen begründen."),
    dict(nr="5-9", text="Koexistenz und Ausgleich der nationalen Marken und der Unionsmarke; nationale Marken bleiben für Unternehmen wichtig, die keinen unionsweiten Schutz wollen. Die Harmonisierung erfasst nun auch Verfahrensregeln, nicht nur das materielle Recht."),
    dict(nr="13", text="Aufgabe der graphischen Darstellbarkeit: Die Darstellung muss klar, eindeutig, in sich abgeschlossen, leicht zugänglich, verständlich, dauerhaft und objektiv sein (Sieckmann-Kriterien), kann aber jede geeignete Technologie nutzen."),
    dict(nr="16", text="Der Schutz der eingetragenen Marke dient insbesondere der Gewährleistung der Herkunftsfunktion; bei Doppelidentität ist er absolut, bei Ähnlichkeit ist die Verwechslungsgefahr die spezifische Schutzvoraussetzung."),
    dict(nr="17-18", text="Die Beurteilung der Verwechslungsgefahr hängt von zahlreichen Faktoren ab: Bekanntheit der Marke, gedankliche Verbindung, Grad der Ähnlichkeit von Zeichen und Waren. Eine Verletzung setzt Benutzung zur Unterscheidung von Waren voraus; Benutzung als Handelsname ist erfasst, wenn sie Warenbezug hat."),
    dict(nr="19-20", text="Rechtssicherheit: Die Rechte aus der jüngeren Marke sollen nicht gegenüber älteren Marken bestehen, die im Prioritätszeitpunkt der jüngeren Marke nicht durchsetzbar waren (Zwischenrecht)."),
    dict(nr="21-22", text="Zollrechtliche Durchsetzung: Der Inhaber soll gegen rechtsverletzende Waren im Transit vorgehen können, ohne die legitime Durchfuhr von Generika oder Waren, die im Bestimmungsland nicht verletzen, zu behindern."),
    dict(nr="25-26", text="Vorverlagerung des Schutzes auf Vorbereitungshandlungen (Etiketten, Verpackungen, Echtheitshinweise), um Produktpiraterie effektiver zu bekämpfen."),
    dict(nr="27", text="Die ausschließlichen Rechte sollen redliche Benutzungen nicht verhindern: Nutzung des eigenen Namens natürlicher Personen, beschreibende Angaben, referierende Benutzung (Zubehör, Ersatzteile, vergleichende Werbung), Meinungs- und Kunstfreiheit; Maßstab sind die anständigen Gepflogenheiten."),
    dict(nr="28", text="Unionsweite Erschöpfung: Der Inhaber darf den Weitervertrieb von Waren, die er selbst oder mit seiner Zustimmung in der Union in Verkehr gebracht hat, nicht verbieten, es sei denn, berechtigte Gründe liegen vor."),
    dict(nr="31-32", text="Benutzungszwang: Eingetragene Marken müssen tatsächlich benutzt werden; nicht benutzte Marken sollen für verfallen erklärt werden können und in Widerspruchs- und Nichtigkeitsverfahren nicht durchgreifen. Die Nichtbenutzungseinrede soll auch im Verletzungsprozess möglich sein."),
    dict(nr="35-37", text="Kollektiv- und Gewährleistungsmarken: Einführung eines gemeinsamen Rahmens; Gewährleistungsmarken bleiben fakultativ."),
    dict(nr="38-40", text="Verfahrensrechtliche Angleichung: Klassifizierung nach IP Translator, Widerspruchsverfahren, verwaltungsbehördliche Verfalls- und Nichtigkeitsverfahren zur Entlastung der Gerichte."),
    dict(nr="41-44", text="Verwaltungszusammenarbeit der Ämter mit dem EUIPO; Einhaltung der Grundrechte der Charta; Umsetzungspflichten."),
]

ARTIKEL_INDEX = {a["nr"]: a for a in ARTIKEL}
