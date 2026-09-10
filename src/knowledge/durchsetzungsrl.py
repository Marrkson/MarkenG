# -*- coding: utf-8 -*-
"""Richtlinie 2004/48/EG des Europäischen Parlaments und des Rates vom 29. April 2004 zur
Durchsetzung der Rechte des geistigen Eigentums (Durchsetzungsrichtlinie, DurchsetzungsRL;
„Enforcement-Richtlinie“), ABl. L 157 vom 30.4.2004, S. 45, berichtigte Fassung ABl. L 195
vom 2.6.2004, S. 16.

Anders als bei der MarkenRL lag der amtliche deutsche Wortlaut beim Erstellen vor (Berichtigung
ABl. L 195, geladen über den EU-Cellar, s. PLAYBOOK Abschnitt 1). Die Absätze sind deshalb im
WORTLAUT erfasst; Buchstabenaufzählungen sind in den Absatztext eingerückt, Fußnoten weggelassen.

Felder je Artikel:
  nr, titel, kapitel, abschnitt
  absaetze           Liste [(nr, Text)]
  umsetzung          MarkenG-Vorschriften, die den Artikel umsetzen (werden im Graphen verknüpft)
  umsetzung_weitere  dict Gesetz -> Vorschriften in den übrigen Gesetzen des gewerblichen
                     Rechtsschutzes und im allgemeinen Recht (nur Text, in Apps und Karten angezeigt)
  concepts, cases    Begriffs- und Entscheidungs-IDs
  hinweis            Lern-/Klausurhinweis
"""

CELEX = "32004L0048"
URL = "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004L0048R(01)"
URL_PDF = "https://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2004:195:0016:0025:de:PDF"
from .gesetze import qualify  # Zitate ohne Gesetzesangabe erhalten das Gesetz der Spalte ("§ 140b" -> "§ 140b PatG")

KURZ = "DurchsetzungsRL"
TITEL = "Richtlinie 2004/48/EG (Durchsetzungsrichtlinie)"
GESETZ = "Richtlinie 2004/48/EG"

K1 = "Kapitel I – Ziel und Anwendungsbereich"
K2 = "Kapitel II – Maßnahmen, Verfahren und Rechtsbehelfe"
K3 = "Kapitel III – Sanktionen der Mitgliedstaaten"
K4 = "Kapitel IV – Verhaltenskodizes und Verwaltungszusammenarbeit"
K5 = "Kapitel V – Schlussbestimmungen"
A1 = "Abschnitt 1 – Allgemeine Bestimmungen"
A2 = "Abschnitt 2 – Beweise"
A3 = "Abschnitt 3 – Recht auf Auskunft"
A4 = "Abschnitt 4 – Einstweilige Maßnahmen und Sicherungsmaßnahmen"
A5 = "Abschnitt 5 – Maßnahmen aufgrund einer Sachentscheidung"
A6 = "Abschnitt 6 – Schadensersatz und Rechtskosten"
A7 = "Abschnitt 7 – Veröffentlichung"

# Reihenfolge der Spalten in der Umsetzungstabelle
GESETZE = ["MarkenG", "PatG", "GebrMG", "DesignG", "UrhG", "HalblSchG", "SortSchG", "Allgemeines Recht"]


def art(nr, titel, kapitel, abschnitt, absaetze, umsetzung=(), weitere=None, concepts=(), cases=(), hinweis=""):
    return dict(nr=str(nr), titel=titel, kapitel=kapitel, abschnitt=abschnitt,
                absaetze=[dict(nr=(str(a) if a is not None else None), text=t) for a, t in absaetze],
                umsetzung=list(umsetzung), umsetzung_weitere={law: qualify(t, law) for law, t in (weitere or {}).items()},
                concepts=list(concepts), cases=list(cases), hinweis=hinweis)


ARTIKEL = [
    # ---------------- Kapitel I ----------------
    art(1, "Gegenstand", K1, None, [
        (None, "Diese Richtlinie betrifft die Maßnahmen, Verfahren und Rechtsbehelfe, die erforderlich sind, um die Durchsetzung der Rechte des geistigen Eigentums sicherzustellen. Im Sinne dieser Richtlinie umfasst der Begriff „Rechte des geistigen Eigentums“ auch die gewerblichen Schutzrechte.")],
        umsetzung=["§ 18", "§ 19", "§ 19a", "§ 19b", "§ 19c"],
        weitere={"PatG": "§§ 139 bis 140e", "GebrMG": "§§ 24 bis 24e", "DesignG": "§§ 42 bis 47", "UrhG": "§§ 97 bis 103", "HalblSchG": "§ 9", "SortSchG": "§§ 37 bis 37e",
                 "Allgemeines Recht": "ZPO (einstweiliger Rechtsschutz, Kosten), BGB (Bereicherung, GoA)"},
        concepts=["durchsetzungsrl"],
        hinweis="Die Richtlinie harmonisiert nicht das materielle Recht (das tun MarkenRL, UMV, DesignRL usw.), sondern die zivilrechtliche Durchsetzung aller Schutzrechte. Deutschland hat sie mit einem Artikelgesetz (Durchsetzungsgesetz vom 7.7.2008, BGBl. I S. 1191, in Kraft seit 1.9.2008) gleichlautend in MarkenG, PatG, GebrMG, DesignG, UrhG, HalblSchG und SortSchG umgesetzt."),
    art(2, "Anwendungsbereich", K1, None, [
        ("1", "Unbeschadet etwaiger Instrumente in den Rechtsvorschriften der Gemeinschaft oder der Mitgliedstaaten, die für die Rechtsinhaber günstiger sind, finden die in dieser Richtlinie vorgesehenen Maßnahmen, Verfahren und Rechtsbehelfe gemäß Artikel 3 auf jede Verletzung von Rechten des geistigen Eigentums, die im Gemeinschaftsrecht und/oder im innerstaatlichen Recht des betreffenden Mitgliedstaats vorgesehen sind, Anwendung."),
        ("2", "Diese Richtlinie gilt unbeschadet der besonderen Bestimmungen zur Gewährleistung der Rechte und Ausnahmen, die in der Gemeinschaftsgesetzgebung auf dem Gebiet des Urheberrechts und der verwandten Schutzrechte vorgesehen sind, namentlich in der Richtlinie 91/250/EWG, insbesondere in Artikel 7, und der Richtlinie 2001/29/EG, insbesondere in den Artikeln 2 bis 6 und Artikel 8."),
        ("3", "Diese Richtlinie berührt nicht: a) die gemeinschaftlichen Bestimmungen zum materiellen Recht auf dem Gebiet des geistigen Eigentums, die Richtlinie 95/46/EG, die Richtlinie 1999/93/EG und die Richtlinie 2000/31/EG im Allgemeinen und insbesondere deren Artikel 12 bis 15; b) die sich aus internationalen Übereinkünften für die Mitgliedstaaten ergebenden Verpflichtungen, insbesondere solche aus dem TRIPS-Übereinkommen, einschließlich solcher betreffend strafrechtliche Verfahren und Strafen; c) innerstaatliche Vorschriften der Mitgliedstaaten betreffend strafrechtliche Verfahren und Strafen bei Verletzung von Rechten des geistigen Eigentums.")],
        umsetzung=["§ 19d", "§ 5"],
        weitere={"PatG": "§ 141a", "GebrMG": "§ 24g", "DesignG": "§ 50", "UrhG": "§ 102a", "HalblSchG": "§ 9 Abs. 4", "SortSchG": "§ 37g",
                 "Allgemeines Recht": "UWG, §§ 823, 826, 812 BGB, GoA bleiben unberührt (Mindestharmonisierung)"},
        concepts=["durchsetzungsrl", "verhaeltnis_uwg"], cases=["eugh_otk"],
        hinweis="Abs. 1 macht die Richtlinie zur Mindestharmonisierung: Strengere nationale Sanktionen (etwa eine pauschale doppelte Lizenzgebühr) sind zulässig (EuGH OTK). Erfasst sind auch rein national geschützte Rechte wie Unternehmenskennzeichen (§ 5 MarkenG) und Benutzungsmarken."),

    # ---------------- Kapitel II, Abschnitt 1 ----------------
    art(3, "Allgemeine Verpflichtung", K2, A1, [
        ("1", "Die Mitgliedstaaten sehen die Maßnahmen, Verfahren und Rechtsbehelfe vor, die zur Durchsetzung der Rechte des geistigen Eigentums, auf die diese Richtlinie abstellt, erforderlich sind. Diese Maßnahmen, Verfahren und Rechtsbehelfe müssen fair und gerecht sein, außerdem dürfen sie nicht unnötig kompliziert oder kostspielig sein und keine unangemessenen Fristen oder ungerechtfertigten Verzögerungen mit sich bringen."),
        ("2", "Diese Maßnahmen, Verfahren und Rechtsbehelfe müssen darüber hinaus wirksam, verhältnismäßig und abschreckend sein und so angewendet werden, dass die Einrichtung von Schranken für den rechtmäßigen Handel vermieden wird und die Gewähr gegen ihren Missbrauch gegeben ist.")],
        umsetzung=["§ 18 Abs. 3", "§ 19 Abs. 4", "§ 19a Abs. 2", "§ 19b Abs. 2"],
        weitere={"PatG": "§ 139 Abs. 1 S. 3 bis 5 (Verhältnismäßigkeit des Unterlassungsanspruchs), § 140a Abs. 4, § 140b Abs. 4, § 140c Abs. 2", "GebrMG": "§ 24 Abs. 1 S. 3 bis 5, § 24a Abs. 3, § 24b Abs. 4, § 24c Abs. 2",
                 "DesignG": "§ 43 Abs. 4, § 46 Abs. 4, § 46a Abs. 2", "UrhG": "§ 98 Abs. 4, § 101 Abs. 4, § 101a Abs. 2", "HalblSchG": "§ 9 Abs. 2 i.V.m. §§ 24a bis 24c GebrMG", "SortSchG": "§ 37a Abs. 3, § 37b Abs. 4, § 37c Abs. 2",
                 "Allgemeines Recht": "§ 242 BGB; Auslegungsmaßstab für alle Durchsetzungsnormen"},
        concepts=["durchsetzungsrl", "gewerbliches_ausmass"], cases=["eugh_novatext", "eugh_mircom", "eugh_loreal_ebay"],
        hinweis="Art. 3 ist die Generalklausel der Richtlinie. Der EuGH zieht sie zur Auslegung jeder Einzelnorm heran: Kostenerstattung nur für zumutbare und angemessene Kosten (NovaText), Missbrauchskontrolle bei Auskunftsanträgen (Mircom), keine allgemeine Überwachungspflicht für Mittelspersonen (L'Oréal/eBay). Im deutschen Recht spiegeln die Verhältnismäßigkeitsvorbehalte der §§ 18 Abs. 3, 19 Abs. 4, 19a Abs. 2, 19b Abs. 2 MarkenG Abs. 2 wider."),
    art(4, "Zur Beantragung der Maßnahmen, Verfahren und Rechtsbehelfe befugte Personen", K2, A1, [
        (None, "Die Mitgliedstaaten räumen den folgenden Personen das Recht ein, die in diesem Kapitel vorgesehenen Maßnahmen, Verfahren und Rechtsbehelfe zu beantragen: a) den Inhabern der Rechte des geistigen Eigentums im Einklang mit den Bestimmungen des anwendbaren Rechts, b) allen anderen Personen, die zur Nutzung solcher Rechte befugt sind, insbesondere Lizenznehmern, soweit dies nach den Bestimmungen des anwendbaren Rechts zulässig ist und mit ihnen im Einklang steht, c) Verwertungsgesellschaften mit ordnungsgemäß anerkannter Befugnis zur Vertretung von Inhabern von Rechten des geistigen Eigentums, soweit dies nach den Bestimmungen des anwendbaren Rechts zulässig ist und mit ihnen im Einklang steht, d) Berufsorganisationen mit ordnungsgemäß anerkannter Befugnis zur Vertretung von Inhabern von Rechten des geistigen Eigentums, soweit dies nach den Bestimmungen des anwendbaren Rechts zulässig ist und mit ihnen im Einklang steht.")],
        umsetzung=["§ 14 Abs. 1", "§ 28 Abs. 1", "§ 30 Abs. 3", "§ 30 Abs. 4"],
        weitere={"PatG": "§ 139 („Verletzter“); Lizenz § 15 Abs. 2, Klagebefugnis des ausschließlichen Lizenznehmers nach der Rechtsprechung", "GebrMG": "§ 24; Lizenz § 22 Abs. 2", "DesignG": "§ 42 Abs. 1 („Rechtsinhaber oder anderer Berechtigter“); § 31 Abs. 3, 4 (Lizenznehmer)",
                 "UrhG": "§ 97 („Verletzter“); Verwertungsgesellschaften nach dem VGG", "HalblSchG": "§ 9 Abs. 1", "SortSchG": "§ 37 Abs. 1; Nutzungsrechte § 11 Abs. 2",
                 "Allgemeines Recht": "Prozessstandschaft, Abtretung (auch Zessionar ist Inhaber: EuGH Mircom)"},
        concepts=["aktivlegitimation", "lizenz"], cases=["eugh_mircom"],
        hinweis="Die Richtlinie überlässt dem nationalen Recht, ob und wann Lizenznehmer klagen dürfen („soweit dies nach dem anwendbaren Recht zulässig ist“). § 30 Abs. 3 MarkenG: Zustimmung des Inhabers, ausnahmsweise eigenes Klagerecht des ausschließlichen Lizenznehmers nach förmlicher Aufforderung; Abs. 4: Beitritt zur Geltendmachung eigenen Schadens."),
    art(5, "Urheber- oder Inhabervermutung", K2, A1, [
        (None, "Zum Zwecke der Anwendung der in dieser Richtlinie vorgesehenen Maßnahmen, Verfahren und Rechtsbehelfe gilt Folgendes: a) Damit der Urheber eines Werkes der Literatur und Kunst mangels Gegenbeweises als solcher gilt und infolgedessen Verletzungsverfahren anstrengen kann, genügt es, dass sein Name in der üblichen Weise auf dem Werkstück angegeben ist. b) Die Bestimmung des Buchstabens a) gilt entsprechend für Inhaber von dem Urheberrecht verwandten Schutzrechten in Bezug auf ihre Schutzgegenstände.")],
        umsetzung=["§ 28 Abs. 1"],
        weitere={"PatG": "– (Registerfiktion § 30 Abs. 3)", "GebrMG": "–", "DesignG": "–", "UrhG": "§ 10 (Vermutung der Urheber- und Rechtsinhaberschaft)", "HalblSchG": "–", "SortSchG": "–",
                 "Allgemeines Recht": "nur für Urheberrecht und verwandte Schutzrechte vorgeschrieben"},
        concepts=["aktivlegitimation"],
        hinweis="Für Registerrechte braucht es keine Namensvermutung: Die Eintragung begründet die Vermutung der Inhaberschaft (§ 28 Abs. 1 MarkenG). Art. 5 ist deshalb allein im UrhG (§ 10) umgesetzt."),

    # ---------------- Kapitel II, Abschnitt 2 ----------------
    art(6, "Beweise", K2, A2, [
        ("1", "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte auf Antrag einer Partei, die alle vernünftigerweise verfügbaren Beweismittel zur hinreichenden Begründung ihrer Ansprüche vorgelegt und die in der Verfügungsgewalt der gegnerischen Partei befindlichen Beweismittel zur Begründung ihrer Ansprüche bezeichnet hat, die Vorlage dieser Beweismittel durch die gegnerische Partei anordnen können, sofern der Schutz vertraulicher Informationen gewährleistet wird. Für die Zwecke dieses Absatzes können die Mitgliedstaaten vorsehen, dass eine angemessen große Auswahl aus einer erheblichen Anzahl von Kopien eines Werks oder eines anderen geschützten Gegenstands von den zuständigen Gerichten als glaubhafter Nachweis angesehen wird."),
        ("2", "Im Falle einer in gewerblichem Ausmaß begangenen Rechtsverletzung räumen die Mitgliedstaaten den zuständigen Gerichten unter den gleichen Voraussetzungen die Möglichkeit ein, in geeigneten Fällen auf Antrag einer Partei die Übermittlung von in der Verfügungsgewalt der gegnerischen Partei befindlichen Bank-, Finanz- oder Handelsunterlagen anzuordnen, sofern der Schutz vertraulicher Informationen gewährleistet wird.")],
        umsetzung=["§ 19a Abs. 1"],
        weitere={"PatG": "§ 140c Abs. 1", "GebrMG": "§ 24c Abs. 1", "DesignG": "§ 46a Abs. 1", "UrhG": "§ 101a Abs. 1", "HalblSchG": "§ 9 Abs. 2 i.V.m. § 24c GebrMG", "SortSchG": "§ 37c Abs. 1",
                 "Allgemeines Recht": "§§ 142, 144 ZPO (Anordnung der Urkundenvorlage und des Augenscheins), § 809 BGB"},
        concepts=["vorlage_besichtigung", "gewerbliches_ausmass"], cases=["bgh_faxkarte"],
        hinweis="Deutschland hat Art. 6 und 7 als materiellen Anspruch ausgestaltet (§ 19a MarkenG: Vorlage einer Urkunde, Besichtigung einer Sache; bei gewerblichem Ausmaß auch Bank-, Finanz-, Handelsunterlagen), nicht als bloße prozessuale Anordnungsbefugnis. Voraussetzung ist „hinreichende Wahrscheinlichkeit“ der Verletzung, nicht ihr Nachweis."),
    art(7, "Maßnahmen zur Beweissicherung", K2, A2, [
        ("1", "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte selbst vor Einleitung eines Verfahrens in der Sache auf Antrag einer Partei, die alle vernünftigerweise verfügbaren Beweismittel zur Begründung ihrer Ansprüche, dass ihre Rechte an geistigem Eigentum verletzt worden sind oder verletzt zu werden drohen, vorgelegt hat, schnelle und wirksame einstweilige Maßnahmen zur Sicherung der rechtserheblichen Beweismittel hinsichtlich der behaupteten Verletzung anordnen können, sofern der Schutz vertraulicher Informationen gewährleistet wird. Derartige Maßnahmen können die ausführliche Beschreibung mit oder ohne Einbehaltung von Mustern oder die dingliche Beschlagnahme der rechtsverletzenden Ware sowie gegebenenfalls der für die Herstellung und/oder den Vertrieb dieser Waren notwendigen Werkstoffe und Geräte und der zugehörigen Unterlagen umfassen. Diese Maßnahmen werden gegebenenfalls ohne Anhörung der anderen Partei getroffen, insbesondere dann, wenn durch eine Verzögerung dem Rechtsinhaber wahrscheinlich ein nicht wieder gutzumachender Schaden entstünde, oder wenn nachweislich die Gefahr besteht, dass Beweise vernichtet werden. Wenn Maßnahmen zur Beweissicherung ohne Anhörung der anderen Partei getroffen wurden, sind die betroffenen Parteien spätestens unverzüglich nach der Vollziehung der Maßnahmen davon in Kenntnis zu setzen. Auf Antrag der betroffenen Parteien findet eine Prüfung, die das Recht zur Stellungnahme einschließt, mit dem Ziel statt, innerhalb einer angemessenen Frist nach der Mitteilung der Maßnahmen zu entscheiden, ob diese abgeändert, aufgehoben oder bestätigt werden sollen."),
        ("2", "Die Mitgliedstaaten stellen sicher, dass die Maßnahmen zur Beweissicherung an die Stellung einer angemessenen Kaution oder entsprechenden Sicherheit durch den Antragsteller geknüpft werden können, um eine Entschädigung des Antragsgegners wie in Absatz 4 vorgesehen sicherzustellen."),
        ("3", "Die Mitgliedstaaten stellen sicher, dass die Maßnahmen zur Beweissicherung auf Antrag des Antragsgegners unbeschadet etwaiger Schadensersatzforderungen aufgehoben oder auf andere Weise außer Kraft gesetzt werden, wenn der Antragsteller nicht innerhalb einer angemessenen Frist — die entweder von dem die Maßnahmen anordnenden Gericht festgelegt wird, sofern dies nach dem Recht des Mitgliedstaats zulässig ist, oder, wenn es nicht zu einer solchen Festlegung kommt, 20 Arbeitstage oder 31 Kalendertage, wobei der längere der beiden Zeiträume gilt, nicht überschreitet — bei dem zuständigen Gericht das Verfahren einleitet, das zu einer Sachentscheidung führt."),
        ("4", "Werden Maßnahmen zur Beweissicherung aufgehoben oder werden sie auf Grund einer Handlung oder Unterlassung des Antragstellers hinfällig, oder wird in der Folge festgestellt, dass keine Verletzung oder drohende Verletzung eines Rechts des geistigen Eigentums vorlag, so sind die Gerichte befugt, auf Antrag des Antragsgegners anzuordnen, dass der Antragsteller dem Antragsgegner angemessenen Ersatz für durch diese Maßnahmen entstandenen Schaden zu leisten hat."),
        ("5", "Die Mitgliedstaaten können Maßnahmen zum Schutz der Identität von Zeugen ergreifen.")],
        umsetzung=["§ 19a Abs. 3", "§ 19a Abs. 5"],
        weitere={"PatG": "§ 140c Abs. 3, Abs. 5", "GebrMG": "§ 24c Abs. 3, Abs. 5", "DesignG": "§ 46a Abs. 3, Abs. 5", "UrhG": "§ 101a Abs. 3, Abs. 5", "HalblSchG": "§ 9 Abs. 2 i.V.m. § 24c GebrMG", "SortSchG": "§ 37c Abs. 3, Abs. 5",
                 "Allgemeines Recht": "§§ 485 ff. ZPO (selbständiges Beweisverfahren); §§ 935 ff. ZPO, § 937 Abs. 2 ZPO, § 921 ZPO, § 926 ZPO, § 945 ZPO"},
        concepts=["vorlage_besichtigung", "einstweilige_verfuegung"], cases=["bgh_faxkarte"],
        hinweis="Umsetzung als einstweilige Verfügung auf Vorlage oder Duldung der Besichtigung (§ 19a Abs. 3), auch ohne Anhörung, mit Geheimnisschutz („Düsseldorfer Verfahren“: Besichtigung durch einen zur Verschwiegenheit verpflichteten Sachverständigen). Abs. 4 entspricht § 19a Abs. 5 (verschuldensunabhängiger Schadensersatz, wenn keine Verletzung vorlag) und allgemein § 945 ZPO."),

    # ---------------- Kapitel II, Abschnitt 3 ----------------
    art(8, "Recht auf Auskunft", K2, A3, [
        ("1", "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte im Zusammenhang mit einem Verfahren wegen Verletzung eines Rechts des geistigen Eigentums auf einen begründeten und die Verhältnismäßigkeit wahrenden Antrag des Klägers hin anordnen können, dass Auskünfte über den Ursprung und die Vertriebswege von Waren oder Dienstleistungen, die ein Recht des geistigen Eigentums verletzen, von dem Verletzer und/oder jeder anderen Person erteilt werden, die a) nachweislich rechtsverletzende Ware in gewerblichem Ausmaß in ihrem Besitz hatte, b) nachweislich rechtsverletzende Dienstleistungen in gewerblichem Ausmaß in Anspruch nahm, c) nachweislich für rechtsverletzende Tätigkeiten genutzte Dienstleistungen in gewerblichem Ausmaß erbrachte, oder d) nach den Angaben einer in Buchstabe a), b) oder c) genannten Person an der Herstellung, Erzeugung oder am Vertrieb solcher Waren bzw. an der Erbringung solcher Dienstleistungen beteiligt war."),
        ("2", "Die Auskünfte nach Absatz 1 erstrecken sich, soweit angebracht, auf a) die Namen und Adressen der Hersteller, Erzeuger, Vertreiber, Lieferer und anderer Vorbesitzer der Waren oder Dienstleistungen sowie der gewerblichen Abnehmer und Verkaufsstellen, für die sie bestimmt waren; b) Angaben über die Mengen der hergestellten, erzeugten, ausgelieferten, erhaltenen oder bestellten Waren und über die Preise, die für die betreffenden Waren oder Dienstleistungen gezahlt wurden."),
        ("3", "Die Absätze 1 und 2 gelten unbeschadet anderer gesetzlicher Bestimmungen, die a) dem Rechtsinhaber weiter gehende Auskunftsrechte einräumen, b) die Verwendung der gemäß diesem Artikel erteilten Auskünfte in straf- oder zivilrechtlichen Verfahren regeln, c) die Haftung wegen Missbrauchs des Auskunftsrechts regeln, d) die Verweigerung von Auskünften zulassen, mit denen die in Absatz 1 genannte Person gezwungen würde, ihre Beteiligung oder die Beteiligung enger Verwandter an einer Verletzung eines Rechts des geistigen Eigentums zuzugeben, oder e) den Schutz der Vertraulichkeit von Informationsquellen oder die Verarbeitung personenbezogener Daten regeln.")],
        umsetzung=["§ 19", "§ 19 Abs. 2", "§ 19 Abs. 3", "§ 19 Abs. 7", "§ 19 Abs. 9"],
        weitere={"PatG": "§ 140b", "GebrMG": "§ 24b", "DesignG": "§ 46", "UrhG": "§ 101 (Abs. 1: Anspruch gegen den Verletzer nur bei gewerblichem Ausmaß)", "HalblSchG": "§ 9 Abs. 2 i.V.m. § 24b GebrMG", "SortSchG": "§ 37b",
                 "Allgemeines Recht": "§ 242 BGB (unselbständige Auskunft zur Bezifferung); §§ 383 bis 385 ZPO (Zeugnisverweigerung = Abs. 3 lit. d)"},
        concepts=["drittauskunft", "vernichtung_auskunft", "gewerbliches_ausmass"],
        cases=["eugh_coty_stadtsparkasse", "bgh_davidoff_hot_water_ii", "eugh_constantin_film", "eugh_new_wave", "eugh_promusicae", "eugh_mircom"],
        hinweis="Kernstück der Richtlinie. Zuordnung: Abs. 1 lit. a bis d = § 19 Abs. 2 S. 1 Nr. 1 bis 4 MarkenG (Drittauskunft bei offensichtlicher Verletzung oder nach Klageerhebung); Abs. 2 = § 19 Abs. 3; Abs. 3 lit. d = Zeugnisverweigerungsrecht (§§ 383 bis 385 ZPO); Abs. 3 lit. e = Richtervorbehalt für Verkehrsdaten (§ 19 Abs. 9). „Adressen“ meint nur die Postanschrift (Constantin Film); das Bankgeheimnis rechtfertigt keine pauschale Verweigerung (Coty, Davidoff Hot Water II); der Anspruch kann auch in einem gesonderten Verfahren nach dem Verletzungsprozess verfolgt werden (NEW WAVE)."),

    # ---------------- Kapitel II, Abschnitt 4 ----------------
    art(9, "Einstweilige Maßnahmen und Sicherungsmaßnahmen", K2, A4, [
        ("1", "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte die Möglichkeit haben, auf Antrag des Antragstellers a) gegen den angeblichen Verletzer eine einstweilige Maßnahme anzuordnen, um eine drohende Verletzung eines Rechts des geistigen Eigentums zu verhindern oder einstweilig und, sofern die einzelstaatlichen Rechtsvorschriften dies vorsehen, in geeigneten Fällen unter Verhängung von Zwangsgeldern die Fortsetzung angeblicher Verletzungen dieses Rechts zu untersagen oder die Fortsetzung an die Stellung von Sicherheiten zu knüpfen, die die Entschädigung des Rechtsinhabers sicherstellen sollen; eine einstweilige Maßnahme kann unter den gleichen Voraussetzungen auch gegen eine Mittelsperson angeordnet werden, deren Dienste von einem Dritten zwecks Verletzung eines Rechts des geistigen Eigentums in Anspruch genommen werden; Anordnungen gegen Mittelspersonen, deren Dienste von einem Dritten zwecks Verletzung eines Urheberrechts oder eines verwandten Schutzrechts in Anspruch genommen werden, fallen unter die Richtlinie 2001/29/EG; b) die Beschlagnahme oder Herausgabe der Waren, bei denen der Verdacht auf Verletzung eines Rechts des geistigen Eigentums besteht, anzuordnen, um deren Inverkehrbringen und Umlauf auf den Vertriebswegen zu verhindern."),
        ("2", "Im Falle von Rechtsverletzungen in gewerblichem Ausmaß stellen die Mitgliedstaaten sicher, dass die zuständigen Gerichte die Möglichkeit haben, die vorsorgliche Beschlagnahme beweglichen und unbeweglichen Vermögens des angeblichen Verletzers einschließlich der Sperrung seiner Bankkonten und der Beschlagnahme sonstiger Vermögenswerte anzuordnen, wenn die geschädigte Partei glaubhaft macht, dass die Erfüllung ihrer Schadensersatzforderung fraglich ist. Zu diesem Zweck können die zuständigen Behörden die Übermittlung von Bank-, Finanz- oder Handelsunterlagen oder einen geeigneten Zugang zu den entsprechenden Unterlagen anordnen."),
        ("3", "Im Falle der Maßnahmen nach den Absätzen 1 und 2 müssen die Gerichte befugt sein, dem Antragsteller aufzuerlegen, alle vernünftigerweise verfügbaren Beweise vorzulegen, um sich mit ausreichender Sicherheit davon überzeugen zu können, dass der Antragsteller der Rechtsinhaber ist und dass das Recht des Antragstellers verletzt wird oder dass eine solche Verletzung droht."),
        ("4", "Die Mitgliedstaaten stellen sicher, dass die einstweiligen Maßnahmen nach den Absätzen 1 und 2 in geeigneten Fällen ohne Anhörung der anderen Partei angeordnet werden können, insbesondere dann, wenn durch eine Verzögerung dem Rechtsinhaber ein nicht wieder gutzumachender Schaden entstehen würde. In diesem Fall sind die Parteien spätestens unverzüglich nach der Vollziehung der Maßnahmen davon in Kenntnis zu setzen. Auf Antrag des Antragsgegners findet eine Prüfung, die das Recht zur Stellungnahme einschließt, mit dem Ziel statt, innerhalb einer angemessenen Frist nach der Mitteilung der Maßnahmen zu entscheiden, ob diese abgeändert, aufgehoben oder bestätigt werden sollen."),
        ("5", "Die Mitgliedstaaten stellen sicher, dass die einstweiligen Maßnahmen nach den Absätzen 1 und 2 auf Antrag des Antragsgegners aufgehoben oder auf andere Weise außer Kraft gesetzt werden, wenn der Antragsteller nicht innerhalb einer angemessenen Frist — die entweder von dem die Maßnahmen anordnenden Gericht festgelegt wird, sofern dies nach dem Recht des Mitgliedstaats zulässig ist, oder, wenn es nicht zu einer solchen Festlegung kommt, 20 Arbeitstage oder 31 Kalendertage, wobei der längere der beiden Zeiträume gilt, nicht überschreitet — bei dem zuständigen Gericht das Verfahren einleitet, das zu einer Sachentscheidung führt."),
        ("6", "Die zuständigen Gerichte können die einstweiligen Maßnahmen nach den Absätzen 1 und 2 an die Stellung einer angemessenen Kaution oder die Leistung einer entsprechenden Sicherheit durch den Antragsteller knüpfen, um eine etwaige Entschädigung des Antragsgegners gemäß Absatz 7 sicherzustellen."),
        ("7", "Werden einstweilige Maßnahmen aufgehoben oder werden sie auf Grund einer Handlung oder Unterlassung des Antragstellers hinfällig, oder wird in der Folge festgestellt, dass keine Verletzung oder drohende Verletzung eines Rechts des geistigen Eigentums vorlag, so sind die Gerichte befugt, auf Antrag des Antragsgegners anzuordnen, dass der Antragsteller dem Antragsgegner angemessenen Ersatz für durch diese Maßnahmen entstandenen Schaden zu leisten hat.")],
        umsetzung=["§ 140 Abs. 3", "§ 19b", "§ 19 Abs. 7", "§ 19a Abs. 3"],
        weitere={"PatG": "§ 140d (Sicherung); keine Dringlichkeitsvermutung", "GebrMG": "§ 24d", "DesignG": "§ 46b", "UrhG": "§ 101b", "HalblSchG": "§ 9 Abs. 2 i.V.m. § 24d GebrMG", "SortSchG": "§ 37d",
                 "Allgemeines Recht": "§§ 935 ff. ZPO (Abs. 1 lit. a), § 938 Abs. 2 ZPO Sequestration (lit. b), §§ 916 ff. ZPO dinglicher Arrest (Abs. 2), § 920 Abs. 2 ZPO Glaubhaftmachung (Abs. 3), § 937 Abs. 2 ZPO (Abs. 4), § 926 ZPO (Abs. 5), § 921 ZPO (Abs. 6), § 945 ZPO (Abs. 7)"},
        concepts=["einstweilige_verfuegung", "sicherung_schadensersatz", "mittelsperson_anordnung"], cases=["eugh_bayer_richter", "eugh_tommy_hilfiger"],
        hinweis="Der Eilrechtsschutz läuft in Deutschland über die ZPO; das MarkenG ergänzt nur die Dringlichkeitsvermutung des § 140 Abs. 3 (Unterlassung; erst seit dem MaMoG 2019, nicht richtliniengetrieben), die Eilauskunft (§ 19 Abs. 7) und die Vorlageverfügung (§ 19a Abs. 3). Abs. 2 (Kontosperre, Unterlagen) = § 19b MarkenG plus Arrest. Abs. 7 = § 945 ZPO, der verschuldensunabhängig haftet und damit über die Richtlinie hinausgeht (EuGH Bayer/Richter: „angemessener Ersatz“ erlaubt die Berücksichtigung eigenen Risikos des Antragsgegners)."),

    # ---------------- Kapitel II, Abschnitt 5 ----------------
    art(10, "Abhilfemaßnahmen", K2, A5, [
        ("1", "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte auf Antrag des Antragstellers anordnen können, dass in Bezug auf Waren, die nach ihren Feststellungen ein Recht des geistigen Eigentums verletzen, und gegebenenfalls in Bezug auf Materialien und Geräte, die vorwiegend zur Schaffung oder Herstellung dieser Waren gedient haben, unbeschadet etwaiger Schadensersatzansprüche des Rechtsinhabers aus der Verletzung sowie ohne Entschädigung irgendwelcher Art geeignete Maßnahmen getroffen werden. Zu diesen Maßnahmen gehören a) der Rückruf aus den Vertriebswegen, b) das endgültige Entfernen aus den Vertriebswegen oder c) die Vernichtung."),
        ("2", "Die Gerichte ordnen an, dass die betreffenden Maßnahmen auf Kosten des Verletzers durchgeführt werden, es sei denn, es werden besondere Gründe geltend gemacht, die dagegen sprechen."),
        ("3", "Bei der Prüfung eines Antrags auf Anordnung von Abhilfemaßnahmen sind die Notwendigkeit eines angemessenen Verhältnisses zwischen der Schwere der Verletzung und den angeordneten Abhilfemaßnahmen sowie die Interessen Dritter zu berücksichtigen.")],
        umsetzung=["§ 18", "§ 18 Abs. 1", "§ 18 Abs. 2", "§ 18 Abs. 3"],
        weitere={"PatG": "§ 140a Abs. 1 bis 4", "GebrMG": "§ 24a", "DesignG": "§ 43 (Abs. 3: Überlassung gegen Vergütung)", "UrhG": "§ 98 (Abs. 3: Überlassung)", "HalblSchG": "§ 9 Abs. 2 i.V.m. § 24a GebrMG", "SortSchG": "§ 37a",
                 "Allgemeines Recht": "Beseitigungsanspruch (§ 1004 BGB analog); Vollstreckung §§ 883, 887 ZPO"},
        concepts=["vernichtung_auskunft"],
        hinweis="Abs. 1 lit. a und b sind der Rückruf- und Entfernungsanspruch des § 18 Abs. 2 MarkenG (neu seit 2008), lit. c der Vernichtungsanspruch des § 18 Abs. 1; Abs. 3 ist der Verhältnismäßigkeitsvorbehalt des § 18 Abs. 3 einschließlich der Interessen Dritter (etwa gutgläubiger Abnehmer). Kein Verschulden erforderlich."),
    art(11, "Gerichtliche Anordnungen", K2, A5, [
        (None, "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte bei Feststellung einer Verletzung eines Rechts des geistigen Eigentums eine Anordnung gegen den Verletzer erlassen können, die ihm die weitere Verletzung des betreffenden Rechts untersagt. Sofern dies nach dem Recht eines Mitgliedstaats vorgesehen ist, werden im Falle einer Missachtung dieser Anordnung in geeigneten Fällen Zwangsgelder verhängt, um die Einhaltung der Anordnung zu gewährleisten. Unbeschadet des Artikels 8 Absatz 3 der Richtlinie 2001/29/EG stellen die Mitgliedstaaten ferner sicher, dass die Rechtsinhaber eine Anordnung gegen Mittelspersonen beantragen können, deren Dienste von einem Dritten zwecks Verletzung eines Rechts des geistigen Eigentums in Anspruch genommen werden.")],
        umsetzung=["§ 14 Abs. 5", "§ 15 Abs. 4"],
        weitere={"PatG": "§ 139 Abs. 1", "GebrMG": "§ 24 Abs. 1", "DesignG": "§ 42 Abs. 1", "UrhG": "§ 97 Abs. 1", "HalblSchG": "§ 9 Abs. 1 S. 1", "SortSchG": "§ 37 Abs. 1",
                 "Allgemeines Recht": "§ 890 ZPO (Ordnungsgeld, Ordnungshaft); Störerhaftung nach der Rechtsprechung des BGH für Mittelspersonen"},
        concepts=["unterlassungsanspruch", "mittelsperson_anordnung", "stoererhaftung"],
        cases=["eugh_loreal_ebay", "eugh_tommy_hilfiger", "bgh_internet_versteigerung_ii", "bgh_kinderhochstuehle"],
        hinweis="Satz 1 = Unterlassungsanspruch (§ 14 Abs. 5), Satz 2 = Vollstreckung über § 890 ZPO. Satz 3 verlangt Anordnungen gegen Mittelspersonen unabhängig von deren eigener Haftung; Deutschland erfüllt das mit der Störerhaftung (Unterlassung ohne Verschulden bei Verletzung zumutbarer Prüfpflichten). Die Anordnung muss auch künftige gleichartige Verletzungen verhindern, darf aber keine allgemeine Überwachungspflicht begründen (L'Oréal/eBay); Mittelsperson kann auch der Betreiber einer physischen Markthalle sein (Tommy Hilfiger)."),
    art(12, "Ersatzmaßnahmen", K2, A5, [
        (None, "Die Mitgliedstaaten können vorsehen, dass die zuständigen Gerichte in entsprechenden Fällen und auf Antrag der Person, der die in diesem Abschnitt vorgesehenen Maßnahmen auferlegt werden könnten, anordnen können, dass anstelle der Anwendung der genannten Maßnahmen eine Abfindung an die geschädigte Partei zu zahlen ist, sofern die betreffende Person weder vorsätzlich noch fahrlässig gehandelt hat, ihr aus der Durchführung der betreffenden Maßnahmen ein unverhältnismäßig großer Schaden entstehen würde und die Zahlung einer Abfindung an die geschädigte Partei als angemessene Entschädigung erscheint.")],
        umsetzung=[],
        weitere={"MarkenG": "nicht genutzt", "PatG": "nicht genutzt (aber § 139 Abs. 1 S. 3, 4: Ausgleich in Geld bei unverhältnismäßiger Härte)", "GebrMG": "nicht genutzt (§ 24 Abs. 1 S. 3, 4)", "DesignG": "§ 45 (Entschädigung)", "UrhG": "§ 100 (Entschädigung)", "HalblSchG": "–", "SortSchG": "–",
                 "Allgemeines Recht": "fakultativ (Erwägungsgrund 25)"},
        concepts=["vernichtung_auskunft"],
        hinweis="Fakultative Regelung; Deutschland hat sie nur im DesignG (§ 45) und UrhG (§ 100) umgesetzt: Der schuldlose Verletzer kann Unterlassung und Vernichtung durch eine Geldentschädigung in Höhe der angemessenen Vergütung abwenden. Im MarkenG gibt es diese Option nicht."),

    # ---------------- Kapitel II, Abschnitt 6 ----------------
    art(13, "Schadensersatz", K2, A6, [
        ("1", "Die Mitgliedstaaten stellen sicher, dass die zuständigen Gerichte auf Antrag der geschädigten Partei anordnen, dass der Verletzer, der wusste oder vernünftigerweise hätte wissen müssen, dass er eine Verletzungshandlung vornahm, dem Rechtsinhaber zum Ausgleich des von diesem wegen der Rechtsverletzung erlittenen tatsächlichen Schadens angemessenen Schadensersatz zu leisten hat. Bei der Festsetzung des Schadensersatzes verfahren die Gerichte wie folgt: a) Sie berücksichtigen alle in Frage kommenden Aspekte, wie die negativen wirtschaftlichen Auswirkungen, einschließlich der Gewinneinbußen für die geschädigte Partei und der zu Unrecht erzielten Gewinne des Verletzers, sowie in geeigneten Fällen auch andere als die rein wirtschaftlichen Faktoren, wie den immateriellen Schaden für den Rechtsinhaber, oder b) sie können stattdessen in geeigneten Fällen den Schadensersatz als Pauschalbetrag festsetzen, und zwar auf der Grundlage von Faktoren wie mindestens dem Betrag der Vergütung oder Gebühr, die der Verletzer hätte entrichten müssen, wenn er die Erlaubnis zur Nutzung des betreffenden Rechts des geistigen Eigentums eingeholt hätte."),
        ("2", "Für Fälle, in denen der Verletzer eine Verletzungshandlung vorgenommen hat, ohne dass er dies wusste oder vernünftigerweise hätte wissen müssen, können die Mitgliedstaaten die Möglichkeit vorsehen, dass die Gerichte die Herausgabe der Gewinne oder die Zahlung von Schadensersatz anordnen, dessen Höhe im Voraus festgesetzt werden kann.")],
        umsetzung=["§ 14 Abs. 6", "§ 15 Abs. 5", "§ 17 Abs. 2"],
        weitere={"PatG": "§ 139 Abs. 2", "GebrMG": "§ 24 Abs. 2", "DesignG": "§ 42 Abs. 2", "UrhG": "§ 97 Abs. 2 (S. 4: immaterieller Schaden)", "HalblSchG": "§ 9 Abs. 1 S. 2, 3", "SortSchG": "§ 37 Abs. 2",
                 "Allgemeines Recht": "Abs. 2: Eingriffskondiktion § 812 Abs. 1 S. 1 Alt. 2 BGB; § 852 BGB über § 20 S. 2 MarkenG"},
        concepts=["schadensersatz", "lizenzanalogie"], cases=["eugh_liffers", "eugh_otk", "bgh_btk"],
        hinweis="Das Durchsetzungsgesetz hat die dreifache Schadensberechnung in allen Schutzrechtsgesetzen kodifiziert (§ 14 Abs. 6 S. 2: Verletzergewinn, S. 3: Lizenzanalogie). Verschulden bleibt Voraussetzung („wusste oder hätte wissen müssen“). Der Pauschalbetrag nach lit. b ist eine Untergrenze („mindestens“), immaterieller Schaden kann hinzukommen (Liffers); strengere nationale Regeln wie die doppelte Lizenzgebühr sind zulässig (OTK). Für den schuldlosen Verletzer (Abs. 2) greift in Deutschland die Eingriffskondiktion."),
    art(14, "Prozesskosten", K2, A6, [
        (None, "Die Mitgliedstaaten stellen sicher, dass die Prozesskosten und sonstigen Kosten der obsiegenden Partei in der Regel, soweit sie zumutbar und angemessen sind, von der unterlegenen Partei getragen werden, sofern Billigkeitsgründe dem nicht entgegenstehen.")],
        umsetzung=["§ 140 Abs. 4", "§ 142"],
        weitere={"PatG": "§ 143 Abs. 3 (Patentanwaltskosten), § 144 (Streitwertbegünstigung)", "GebrMG": "§ 27 Abs. 3", "DesignG": "§ 52 Abs. 4", "UrhG": "§ 97a Abs. 3 (Abmahnkosten, Deckelung des Gegenstandswerts)", "HalblSchG": "–", "SortSchG": "–",
                 "Allgemeines Recht": "§§ 91 ff. ZPO, RVG; Abmahnkosten aus GoA (§§ 677, 683, 670 BGB) und als Schadensersatz"},
        concepts=["prozesskosten_erstattung"], cases=["eugh_novatext", "bgh_kosten_patentanwalt_vii", "eugh_koch_media", "eugh_united_video"],
        hinweis="Klausurklassiker seit 2022: § 140 Abs. 3 MarkenG a.F. (heute Abs. 4) ließ Patentanwaltskosten in Kennzeichenstreitsachen stets erstatten; das verstößt gegen Art. 3 und 14 (EuGH NovaText). Der BGH legt die Norm seither richtlinienkonform aus: Erstattung nur, wenn die Mitwirkung zur zweckentsprechenden Rechtsverfolgung notwendig war (Kosten des Patentanwalts VII). Auch Abmahnkosten sind „sonstige Kosten“ (Koch Media); Pauschal- und Höchstsätze sind zulässig, wenn ein erheblicher und angemessener Teil erstattet wird (United Video Properties)."),

    # ---------------- Kapitel II, Abschnitt 7 ----------------
    art(15, "Veröffentlichung von Gerichtsentscheidungen", K2, A7, [
        (None, "Die Mitgliedstaaten stellen sicher, dass die Gerichte bei Verfahren wegen Verletzung von Rechten des geistigen Eigentums auf Antrag des Antragstellers und auf Kosten des Verletzers geeignete Maßnahmen zur Verbreitung von Informationen über die betreffende Entscheidung, einschließlich der Bekanntmachung und der vollständigen oder teilweisen Veröffentlichung, anordnen können. Die Mitgliedstaaten können andere, den besonderen Umständen angemessene Zusatzmaßnahmen, einschließlich öffentlichkeitswirksamer Anzeigen, vorsehen.")],
        umsetzung=["§ 19c"],
        weitere={"PatG": "§ 140e", "GebrMG": "§ 24e", "DesignG": "§ 47", "UrhG": "§ 103", "HalblSchG": "§ 9 Abs. 2 i.V.m. § 24e GebrMG", "SortSchG": "§ 37e",
                 "Allgemeines Recht": "strafrechtlich § 143 Abs. 6 MarkenG; § 12 Abs. 3 UWG a.F. (Vorbild)"},
        concepts=["urteilsbekanntmachung"],
        hinweis="§ 19c: Befugnis der obsiegenden Partei (auch des Beklagten) bei berechtigtem Interesse; Art und Umfang bestimmt das Urteil; Erlöschen drei Monate nach Rechtskraft; nicht vorläufig vollstreckbar. Wortgleich in allen Schutzrechtsgesetzen."),

    # ---------------- Kapitel III ----------------
    art(16, "Sanktionen der Mitgliedstaaten", K3, None, [
        (None, "Unbeschadet der in dieser Richtlinie vorgesehenen zivil- und verwaltungsrechtlichen Maßnahmen, Verfahren und Rechtsbehelfe können die Mitgliedstaaten in Fällen von Verletzungen von Rechten des geistigen Eigentums andere angemessene Sanktionen vorsehen.")],
        umsetzung=["§ 143", "§ 143a", "§ 144", "§ 146"],
        weitere={"PatG": "§ 142 (Strafvorschrift); §§ 142a, 142b (Zollbeschlagnahme)", "GebrMG": "§ 25; §§ 25a, 25b", "DesignG": "§ 51; §§ 55 ff.", "UrhG": "§§ 106 bis 111a; § 111b", "HalblSchG": "§ 10; § 9 Abs. 2 i.V.m. §§ 25a, 25b GebrMG", "SortSchG": "§ 39; § 40a",
                 "Allgemeines Recht": "Verordnung (EU) Nr. 608/2013 (Grenzbeschlagnahme); Art. 61 TRIPS"},
        concepts=["transit"],
        hinweis="Strafrecht und Grenzbeschlagnahme sind nicht Gegenstand der Richtlinie (Art. 2 Abs. 3 lit. b, c); Art. 16 stellt nur klar, dass sie daneben zulässig bleiben. Die Grenzbeschlagnahme ist unionsrechtlich in der VO (EU) Nr. 608/2013 geregelt, § 146 MarkenG gilt subsidiär."),

    # ---------------- Kapitel IV ----------------
    art(17, "Verhaltenskodizes", K4, None, [
        (None, "Die Mitgliedstaaten wirken darauf hin, dass a) die Unternehmens- und Berufsverbände oder -organisationen auf Gemeinschaftsebene Verhaltenskodizes ausarbeiten, die zum Schutz der Rechte des geistigen Eigentums beitragen, insbesondere indem die Anbringung eines Codes auf optischen Speicherplatten empfohlen wird, der den Ort ihrer Herstellung erkennen lässt; b) der Kommission die Entwürfe innerstaatlicher oder gemeinschaftsweiter Verhaltenskodizes und etwaige Gutachten über deren Anwendung übermittelt werden.")],
        umsetzung=[], weitere={"Allgemeines Recht": "keine gesetzliche Umsetzung erforderlich"}, concepts=["durchsetzungsrl"]),
    art(18, "Bewertung", K4, None, [
        ("1", "Jeder Mitgliedstaat legt der Kommission drei Jahre nach Ablauf der in Artikel 20 Absatz 1 genannten Frist einen Bericht über die Umsetzung dieser Richtlinie vor. Anhand dieser Berichte erstellt die Kommission einen Bericht über die Anwendung dieser Richtlinie, einschließlich einer Bewertung der Wirksamkeit der ergriffenen Maßnahmen sowie einer Bewertung der Auswirkungen der Richtlinie auf die Innovation und die Entwicklung der Informationsgesellschaft. Dieser Bericht wird dem Europäischen Parlament, dem Rat und dem Europäischen Wirtschafts- und Sozialausschuss vorgelegt. Soweit erforderlich, legt die Kommission unter Berücksichtigung der Entwicklung des Gemeinschaftsrechts zusammen mit dem Bericht Vorschläge zur Änderung dieser Richtlinie vor."),
        ("2", "Die Mitgliedstaaten lassen der Kommission bei der Erstellung des in Absatz 1 Unterabsatz 2 genannten Berichts jede benötigte Hilfe und Unterstützung zukommen.")],
        umsetzung=[], weitere={"Allgemeines Recht": "Bericht der Kommission KOM(2010) 779; Leitlinien zur Auslegung COM(2017) 708"}, concepts=["durchsetzungsrl"],
        hinweis="Die Leitlinien der Kommission von 2017 (COM(2017) 708) fassen die EuGH-Rechtsprechung zu Art. 3, 6 bis 11 und 13, 14 zusammen und sind eine gute Lernquelle."),
    art(19, "Informationsaustausch und Korrespondenzstellen", K4, None, [
        (None, "Zur Förderung der Zusammenarbeit, einschließlich des Informationsaustauschs, der Mitgliedstaaten untereinander sowie zwischen den Mitgliedstaaten und der Kommission benennt jeder Mitgliedstaat mindestens eine nationale Korrespondenzstelle für alle die Durchführung der in dieser Richtlinie vorgesehenen Maßnahmen betreffenden Fragen. Jeder Mitgliedstaat teilt die Kontaktadressen seiner Korrespondenzstelle(n) den anderen Mitgliedstaaten und der Kommission mit.")],
        umsetzung=[], weitere={"Allgemeines Recht": "Verwaltungspraxis (BMJ)"}, concepts=["durchsetzungsrl"]),

    # ---------------- Kapitel V ----------------
    art(20, "Umsetzung", K5, None, [
        ("1", "Die Mitgliedstaaten setzen die Rechts- und Verwaltungsvorschriften in Kraft, die erforderlich sind, um dieser Richtlinie spätestens ab dem 29. April 2006 nachzukommen. Sie setzen die Kommission unverzüglich davon in Kenntnis. Wenn die Mitgliedstaaten diese Vorschriften erlassen, nehmen sie in den Vorschriften selbst oder durch einen Hinweis bei der amtlichen Veröffentlichung auf diese Richtlinie Bezug. Die Mitgliedstaaten regeln die Einzelheiten der Bezugnahme."),
        ("2", "Die Mitgliedstaaten teilen der Kommission den Wortlaut der innerstaatlichen Rechtsvorschriften mit, die sie auf dem unter diese Richtlinie fallenden Gebiet erlassen.")],
        umsetzung=[],
        weitere={"Allgemeines Recht": "Gesetz zur Verbesserung der Durchsetzung von Rechten des geistigen Eigentums vom 7.7.2008 (BGBl. I S. 1191), in Kraft seit 1.9.2008 – Artikelgesetz für PatG, GebrMG, MarkenG, HalblSchG, UrhG, DesignG und SortSchG"},
        concepts=["durchsetzungsrl"],
        hinweis="Deutschland hat die Frist (29.4.2006) um mehr als zwei Jahre verfehlt; in der Zwischenzeit galt richtlinienkonforme Auslegung des bestehenden Rechts (etwa § 242 BGB für Auskunft, § 809 BGB für Besichtigung)."),
    art(21, "Inkrafttreten", K5, None, [(None, "Diese Richtlinie tritt am zwanzigsten Tag nach ihrer Veröffentlichung im Amtsblatt der Europäischen Union in Kraft.")],
        umsetzung=[], weitere={}, concepts=["durchsetzungsrl"],
        hinweis="Veröffentlicht am 30.4.2004 (ABl. L 157, S. 45); wegen Fehlern in der Erstveröffentlichung wurde der gesamte Text am 2.6.2004 berichtigt neu bekannt gemacht (ABl. L 195, S. 16). Zitiert wird die berichtigte Fassung."),
    art(22, "Adressaten", K5, None, [(None, "Diese Richtlinie ist an die Mitgliedstaaten gerichtet.")],
        umsetzung=[], weitere={}, concepts=["durchsetzungsrl"]),
]

# Ausgewählte Erwägungsgründe (Wortlaut, teils gekürzt), die die Auslegung prägen.
ERWAEGUNGSGRUENDE = [
    dict(nr="3", text="Ohne wirksame Instrumente zur Durchsetzung der Rechte des geistigen Eigentums werden jedoch Innovation und kreatives Schaffen gebremst und Investitionen verhindert. Daher ist darauf zu achten, dass das materielle Recht auf dem Gebiet des geistigen Eigentums, das heute weitgehend Teil des gemeinschaftlichen Besitzstands ist, in der Gemeinschaft wirksam angewandt wird."),
    dict(nr="7", text="Aus den Sondierungen der Kommission hat sich ergeben, dass ungeachtet des TRIPS-Übereinkommens weiterhin zwischen den Mitgliedstaaten große Unterschiede bei den Instrumenten zur Durchsetzung bestehen: bei einstweiligen Maßnahmen zur Beweissicherung, bei der Berechnung von Schadensersatz, bei Verfahren zur Beendigung von Verstößen. In einigen Mitgliedstaaten stehen Maßnahmen wie das Auskunftsrecht und der Rückruf rechtsverletzender Ware vom Markt auf Kosten des Verletzers nicht zur Verfügung."),
    dict(nr="10", text="Mit dieser Richtlinie sollen diese Rechtsvorschriften einander angenähert werden, um ein hohes, gleichwertiges und homogenes Schutzniveau für geistiges Eigentum im Binnenmarkt zu gewährleisten."),
    dict(nr="13", text="Der Anwendungsbereich dieser Richtlinie muss so breit wie möglich gewählt werden, damit er alle Rechte des geistigen Eigentums erfasst, die den diesbezüglichen Gemeinschaftsvorschriften und/oder den Rechtsvorschriften der jeweiligen Mitgliedstaaten unterliegen. Dieses Erfordernis hindert die Mitgliedstaaten jedoch nicht daran, die Bestimmungen dieser Richtlinie bei Bedarf zu innerstaatlichen Zwecken auf Handlungen auszuweiten, die den unlauteren Wettbewerb einschließlich der Produktpiraterie oder vergleichbare Tätigkeiten betreffen."),
    dict(nr="14", text="Nur bei in gewerblichem Ausmaß vorgenommenen Rechtsverletzungen müssen die Maßnahmen nach Artikel 6 Absatz 2, Artikel 8 Absatz 1 und Artikel 9 Absatz 2 angewandt werden. Unbeschadet davon können die Mitgliedstaaten diese Maßnahmen auch bei anderen Rechtsverletzungen anwenden. In gewerblichem Ausmaß vorgenommene Rechtsverletzungen zeichnen sich dadurch aus, dass sie zwecks Erlangung eines unmittelbaren oder mittelbaren wirtschaftlichen oder kommerziellen Vorteils vorgenommen werden; dies schließt in der Regel Handlungen aus, die in gutem Glauben von Endverbrauchern vorgenommen werden."),
    dict(nr="17", text="Die in dieser Richtlinie vorgesehenen Maßnahmen, Verfahren und Rechtsbehelfe sollten in jedem Einzelfall so bestimmt werden, dass den spezifischen Merkmalen dieses Falles, einschließlich der Sonderaspekte jedes Rechts an geistigem Eigentum und gegebenenfalls des vorsätzlichen oder nicht vorsätzlichen Charakters der Rechtsverletzung gebührend Rechnung getragen wird."),
    dict(nr="20", text="Da Beweismittel für die Feststellung einer Verletzung von zentraler Bedeutung sind, muss sichergestellt werden, dass wirksame Mittel zur Vorlage, zur Erlangung und zur Sicherung von Beweismitteln zur Verfügung stehen. Die Verfahren sollten den Rechten der Verteidigung Rechnung tragen und die erforderlichen Sicherheiten einschließlich des Schutzes vertraulicher Informationen bieten. Bei in gewerblichem Ausmaß vorgenommenen Rechtsverletzungen ist es ferner wichtig, dass die Gerichte gegebenenfalls die Übergabe von Bank-, Finanz- und Handelsunterlagen anordnen können."),
    dict(nr="21", text="In einigen Mitgliedstaaten gibt es andere Maßnahmen zur Sicherstellung eines hohen Schutzniveaus; diese sollten in allen Mitgliedstaaten verfügbar sein. Dies gilt für das Recht auf Auskunft über die Herkunft rechtsverletzender Waren und Dienstleistungen, über die Vertriebswege sowie über die Identität Dritter, die an der Rechtsverletzung beteiligt sind."),
    dict(nr="22", text="Ferner sind einstweilige Maßnahmen unabdingbar, die unter Wahrung des Anspruchs auf rechtliches Gehör und der Verhältnismäßigkeit sowie vorbehaltlich der Sicherheiten, die erforderlich sind, um dem Antragsgegner im Falle eines ungerechtfertigten Antrags den entstandenen Schaden zu ersetzen, die unverzügliche Beendigung der Verletzung ermöglichen, ohne dass eine Entscheidung in der Sache abgewartet werden muss."),
    dict(nr="23", text="Unbeschadet anderer verfügbarer Maßnahmen sollten Rechtsinhaber die Möglichkeit haben, eine gerichtliche Anordnung gegen eine Mittelsperson zu beantragen, deren Dienste von einem Dritten dazu genutzt werden, das gewerbliche Schutzrecht des Rechtsinhabers zu verletzen. Die Voraussetzungen und Verfahren für derartige Anordnungen sollten Gegenstand der einzelstaatlichen Rechtsvorschriften bleiben."),
    dict(nr="24", text="Die Maßnahmen sollten Verbotsmaßnahmen beinhalten, die eine erneute Verletzung verhindern. Darüber hinaus sollten Abhilfemaßnahmen vorgesehen werden, deren Kosten dem Verletzer angelastet werden und die beinhalten können, dass Waren, durch die ein Recht verletzt wird, und gegebenenfalls auch die Materialien und Geräte, die vorwiegend zu ihrer Herstellung gedient haben, zurückgerufen, endgültig aus den Vertriebswegen entfernt oder vernichtet werden. Diese Abhilfemaßnahmen sollten den Interessen Dritter, insbesondere der in gutem Glauben handelnden Verbraucher und privaten Parteien, Rechnung tragen."),
    dict(nr="25", text="In Fällen, in denen eine Rechtsverletzung weder vorsätzlich noch fahrlässig erfolgt ist und die Abhilfemaßnahmen oder gerichtlichen Anordnungen unangemessen wären, sollten die Mitgliedstaaten die Möglichkeit vorsehen können, dass als Ersatzmaßnahme die Zahlung einer Abfindung an den Geschädigten angeordnet wird."),
    dict(nr="26", text="Um den Schaden auszugleichen, den ein Verletzer verursacht hat, der wusste oder vernünftigerweise hätte wissen müssen, dass er eine Verletzungshandlung vornahm, sollten bei der Festsetzung des Schadensersatzes alle einschlägigen Aspekte berücksichtigt werden, wie Gewinneinbußen des Rechtsinhabers oder zu Unrecht erzielte Gewinne des Verletzers sowie gegebenenfalls der immaterielle Schaden. Ersatzweise, etwa wenn die Höhe des tatsächlichen Schadens schwierig zu beziffern wäre, kann die Höhe des Schadens aus Kriterien wie der Vergütung abgeleitet werden, die der Verletzer hätte entrichten müssen, wenn er die Erlaubnis zur Nutzung eingeholt hätte. Bezweckt wird dabei nicht die Einführung einer Verpflichtung zu einem als Strafe angelegten Schadensersatz, sondern eine Ausgleichsentschädigung auf objektiver Grundlage unter Berücksichtigung der Kosten des Rechtsinhabers, z. B. für die Feststellung der Rechtsverletzung und ihrer Verursacher."),
    dict(nr="27", text="Die Entscheidungen in Verfahren wegen Verletzungen von Rechten des geistigen Eigentums sollten veröffentlicht werden, um künftige Verletzer abzuschrecken und zur Sensibilisierung der breiten Öffentlichkeit beizutragen."),
    dict(nr="32", text="Diese Richtlinie steht im Einklang mit den Grundrechten und Grundsätzen der Charta der Grundrechte der Europäischen Union. In besonderer Weise soll sie im Einklang mit Artikel 17 Absatz 2 der Charta die uneingeschränkte Achtung geistigen Eigentums sicherstellen."),
]

# Umsetzungstabelle: Artikel -> Vorschriften in allen Gesetzen des gewerblichen Rechtsschutzes.
# Reihenfolge der Spalten wie GESETZE; für die Abgrenzungs-Ansicht als distinction exportiert.
UMSETZUNG = [
    ("Art. 2 Abs. 1 – Günstigere Vorschriften bleiben unberührt (Mindestharmonisierung)",
     ["§ 19d", "§ 141a", "§ 24g", "§ 50", "§ 102a", "§ 9 Abs. 4", "§ 37g", "UWG, §§ 823, 826, 812 BGB, GoA (EuGH OTK: strengere Regeln zulässig)"]),
    ("Art. 3 – Allgemeine Verpflichtung: fair, wirksam, verhältnismäßig, abschreckend, kein Missbrauch",
     ["§ 18 Abs. 3, § 19 Abs. 4, § 19a Abs. 2, § 19b Abs. 2", "§ 139 Abs. 1 S. 3 bis 5, § 140a Abs. 4, § 140b Abs. 4, § 140c Abs. 2", "§ 24 Abs. 1 S. 3 bis 5, § 24a Abs. 3, § 24b Abs. 4, § 24c Abs. 2", "§ 43 Abs. 4, § 46 Abs. 4, § 46a Abs. 2", "§ 98 Abs. 4, § 101 Abs. 4, § 101a Abs. 2", "§ 9 Abs. 2 (§§ 24a bis 24c GebrMG)", "§ 37a Abs. 3, § 37b Abs. 4, § 37c Abs. 2", "§ 242 BGB; Auslegungsmaßstab für alle Durchsetzungsnormen (EuGH NovaText, Mircom)"]),
    ("Art. 4 – Antragsbefugte: Inhaber, Lizenznehmer, Verwertungsgesellschaften, Verbände",
     ["§ 14 Abs. 1, § 28 Abs. 1; Lizenznehmer § 30 Abs. 3, 4", "§ 139 („Verletzter“); Lizenz § 15 Abs. 2", "§ 24; Lizenz § 22 Abs. 2", "§ 42 Abs. 1; Lizenznehmer § 31 Abs. 3, 4", "§ 97; Verwertungsgesellschaften nach VGG", "§ 9 Abs. 1", "§ 37 Abs. 1; § 11 Abs. 2", "Prozessstandschaft, Abtretung (EuGH Mircom)"]),
    ("Art. 5 – Urheber- oder Inhabervermutung",
     ["– (Registervermutung § 28 Abs. 1)", "– (§ 30 Abs. 3)", "–", "–", "§ 10", "–", "–", "nur Urheberrecht und verwandte Schutzrechte"]),
    ("Art. 6 – Beweise: Vorlage von Beweismitteln, Bank-, Finanz- und Handelsunterlagen",
     ["§ 19a Abs. 1", "§ 140c Abs. 1", "§ 24c Abs. 1", "§ 46a Abs. 1", "§ 101a Abs. 1", "§ 9 Abs. 2 (§ 24c GebrMG)", "§ 37c Abs. 1", "§§ 142, 144 ZPO; § 809 BGB"]),
    ("Art. 7 – Beweissicherung: einstweilige Maßnahmen, ohne Anhörung, Schadensersatz bei Aufhebung",
     ["§ 19a Abs. 3, Abs. 5", "§ 140c Abs. 3, Abs. 5", "§ 24c Abs. 3, Abs. 5", "§ 46a Abs. 3, Abs. 5", "§ 101a Abs. 3, Abs. 5", "§ 9 Abs. 2 (§ 24c GebrMG)", "§ 37c Abs. 3, Abs. 5", "§§ 485 ff. ZPO; §§ 935 ff. ZPO, § 937 Abs. 2 ZPO, § 945 ZPO"]),
    ("Art. 8 – Recht auf Auskunft: Verletzer und Dritte; Namen, Adressen, Mengen, Preise",
     ["§ 19 (Abs. 2 Nr. 1 bis 4 = Art. 8 Abs. 1 lit. a bis d; Abs. 3 = Art. 8 Abs. 2; Abs. 9 Verkehrsdaten)", "§ 140b", "§ 24b", "§ 46", "§ 101 (Abs. 1: nur bei gewerblichem Ausmaß)", "§ 9 Abs. 2 (§ 24b GebrMG)", "§ 37b", "§ 242 BGB; §§ 383 bis 385 ZPO (= Art. 8 Abs. 3 lit. d)"]),
    ("Art. 9 Abs. 1 – Einstweilige Maßnahmen: Unterlassung, auch gegen Mittelspersonen; Beschlagnahme",
     ["§ 140 Abs. 3 (Dringlichkeitsvermutung, seit MaMoG 2019); § 19 Abs. 7, § 19a Abs. 3", "§§ 935 ff. ZPO (keine Dringlichkeitsvermutung)", "§§ 935 ff. ZPO", "§§ 935 ff. ZPO", "§§ 935 ff. ZPO", "§§ 935 ff. ZPO", "§§ 935 ff. ZPO", "§§ 935, 938, 940 ZPO; Sequestration § 938 Abs. 2 ZPO; Störerhaftung"]),
    ("Art. 9 Abs. 2 – Sicherung von Schadensersatz: Vermögensbeschlagnahme, Kontosperre, Unterlagen",
     ["§ 19b", "§ 140d", "§ 24d", "§ 46b", "§ 101b", "§ 9 Abs. 2 (§ 24d GebrMG)", "§ 37d", "dinglicher Arrest §§ 916 ff. ZPO"]),
    ("Art. 9 Abs. 3 bis 7 – Eilverfahren: Glaubhaftmachung, ohne Anhörung, Hauptsachefrist, Sicherheit, Schadensersatz",
     ["–", "–", "–", "–", "–", "–", "–", "§ 920 Abs. 2 ZPO, § 936 ZPO; § 937 Abs. 2 ZPO; § 926 ZPO; § 921 ZPO; § 945 ZPO (verschuldensunabhängig; EuGH Bayer/Richter)"]),
    ("Art. 10 – Abhilfemaßnahmen: Rückruf, endgültiges Entfernen, Vernichtung; Verhältnismäßigkeit",
     ["§ 18 Abs. 1 (Vernichtung), Abs. 2 (Rückruf, Entfernen), Abs. 3 (Verhältnismäßigkeit)", "§ 140a Abs. 1 bis 4", "§ 24a", "§ 43 (Abs. 3: Überlassung)", "§ 98 (Abs. 3: Überlassung)", "§ 9 Abs. 2 (§ 24a GebrMG)", "§ 37a", "§ 1004 BGB analog; Vollstreckung §§ 883, 887 ZPO"]),
    ("Art. 11 – Gerichtliche Anordnungen: Unterlassung, Zwangsgeld, Anordnung gegen Mittelspersonen",
     ["§ 14 Abs. 5, § 15 Abs. 4; Störerhaftung", "§ 139 Abs. 1", "§ 24 Abs. 1", "§ 42 Abs. 1", "§ 97 Abs. 1", "§ 9 Abs. 1 S. 1", "§ 37 Abs. 1", "§ 890 ZPO; Störerhaftung (BGH); Providerhaftung nach dem DDG"]),
    ("Art. 12 – Ersatzmaßnahmen: Abfindung statt Rückruf und Vernichtung bei schuldloser Verletzung",
     ["nicht genutzt", "nicht genutzt (§ 139 Abs. 1 S. 3, 4: Geldausgleich bei Härte)", "nicht genutzt (§ 24 Abs. 1 S. 3, 4)", "§ 45 (Entschädigung)", "§ 100 (Entschädigung)", "–", "–", "fakultativ (Erwägungsgrund 25)"]),
    ("Art. 13 – Schadensersatz: Verschulden; Verletzergewinn, immaterieller Schaden; Pauschale nach Lizenzgebühr",
     ["§ 14 Abs. 6 (S. 2 Verletzergewinn, S. 3 Lizenzanalogie), § 15 Abs. 5, § 17 Abs. 2 S. 2", "§ 139 Abs. 2", "§ 24 Abs. 2", "§ 42 Abs. 2", "§ 97 Abs. 2 (S. 4: immaterieller Schaden)", "§ 9 Abs. 1 S. 2, 3", "§ 37 Abs. 2", "Abs. 2: § 812 Abs. 1 S. 1 Alt. 2 BGB; § 852 BGB (§ 20 S. 2 MarkenG)"]),
    ("Art. 14 – Prozesskosten: zumutbare und angemessene Kosten trägt der Unterlegene",
     ["§ 140 Abs. 4 (Patentanwaltskosten; nur bei Notwendigkeit: EuGH NovaText, BGH Kosten des Patentanwalts VII); § 142", "§ 143 Abs. 3; § 144", "§ 27 Abs. 3", "§ 52 Abs. 4", "§ 97a Abs. 3 (Abmahnkosten; EuGH Koch Media)", "–", "–", "§§ 91 ff. ZPO; RVG; Abmahnkosten aus GoA"]),
    ("Art. 15 – Veröffentlichung von Gerichtsentscheidungen",
     ["§ 19c", "§ 140e", "§ 24e", "§ 47", "§ 103", "§ 9 Abs. 2 (§ 24e GebrMG)", "§ 37e", "Befugnis erlischt drei Monate nach Rechtskraft; nicht vorläufig vollstreckbar"]),
    ("Art. 16 – Sanktionen der Mitgliedstaaten: Strafrecht, Grenzbeschlagnahme",
     ["§§ 143, 143a, 144; §§ 146 bis 151", "§ 142; §§ 142a, 142b", "§ 25; §§ 25a, 25b", "§ 51; §§ 55 ff.", "§§ 106 bis 111a; § 111b", "§ 10; § 9 Abs. 2 (§§ 25a, 25b GebrMG)", "§ 39; § 40a", "VO (EU) Nr. 608/2013; Art. 61 TRIPS"]),
    ("Nicht harmonisiert: Verjährung; Haftung des Betriebsinhabers",
     ["§ 20 (BGB, § 852 BGB); § 14 Abs. 7", "§ 141", "§ 24f", "§ 49; § 44", "§ 102; § 99", "§ 9 Abs. 3", "§ 37f", "§§ 195, 199 BGB; § 852 BGB (Restschadensersatz, zehn Jahre)"]),
    ("Art. 20 – Umsetzungsfrist 29.4.2006",
     ["–", "–", "–", "–", "–", "–", "–", "Durchsetzungsgesetz vom 7.7.2008 (BGBl. I S. 1191), in Kraft 1.9.2008, als Artikelgesetz für alle sieben Gesetze"]),
]

UMSETZUNG_DISTINCTION = dict(
    id="d_durchsetzungsrl_umsetzung",
    label="Umsetzungstabelle: Durchsetzungsrichtlinie 2004/48/EG in allen Gesetzen des gewerblichen Rechtsschutzes",
    concepts=["durchsetzungsrl", "vernichtung_auskunft", "drittauskunft", "vorlage_besichtigung", "prozesskosten_erstattung"],
    frage="Welcher Artikel der Durchsetzungsrichtlinie steckt in welcher Vorschrift des MarkenG, PatG, GebrMG, DesignG, UrhG, HalblSchG und SortSchG?",
    kriterien=[k for k, _ in UMSETZUNG],
    spalten=list(GESETZE),
    rows=[[qualify(cell, law) for cell, law in zip(r, GESETZE)] for _, r in UMSETZUNG],
    merksatz="Ein Muster, sieben Gesetze: Vernichtung/Rückruf – Auskunft – Vorlage/Besichtigung – Sicherung – Urteilsbekanntmachung stehen überall in derselben Reihenfolge (§§ 18 bis 19c MarkenG = §§ 140a bis 140e PatG = §§ 24a bis 24e GebrMG = §§ 43, 46 bis 47 DesignG = §§ 98, 101 bis 103 UrhG = §§ 37a bis 37e SortSchG; HalblSchG verweist auf das GebrMG).",
)

ARTIKEL_INDEX = {a["nr"]: a for a in ARTIKEL}
