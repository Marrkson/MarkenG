# -*- coding: utf-8 -*-
"""Richtlinien für die Prüfung von Patentanmeldungen (Prüfungsrichtlinien) des DPMA als Quellen des Patentpakets.

Die Richtlinien sind eine Verwaltungsvorschrift des DPMA und keine Norm: Sie binden die Prüfungsstellen, nicht die Gerichte.
Deshalb sind ihre Abschnitte wie die UP-Richtlinien des EPA `source`-Knoten (Provider „DPMA-Prüfungsrichtlinien“, Seiten-ID
`prl:2.3.3.3`); Begriffe verweisen mit `quellen=["prl:2.4.1"]` darauf (Zuordnung in BEGRIFF_QUELLEN, concepts.py wendet sie an).
Text: data/dpma_pruefungsrichtlinien.json (tools/fetch_pruefungsrichtlinien.py aus dem Formular P 2796 des DPMA); die
kuratierten Zusammenfassungen unten fassen den Abschnitt in eigenen Worten zusammen, die übrigen Abschnitte tragen den Anfang
des amtlichen Wortlauts. Neue Ausgabe: PDF im Cache löschen, Skript laufen lassen, Abschnittsnummern der Kuratierung prüfen.
"""
import json
import re
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data" / "dpma_pruefungsrichtlinien.json"
_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
ABSCHNITTE = _JSON["abschnitte"]
STAND = "Ausgabe vom %s (%s)" % (META["stand"], META["formular"])
URL = META["quelle"]
PROVIDER = "DPMA-Prüfungsrichtlinien"
_BY_NR = {a["nr"]: a for a in ABSCHNITTE if a["nr"]}


def _url(a):
    return "%s#page=%d" % (URL, a["seite"])


def _kurz(text, n=300):
    """Anfang des amtlichen Wortlauts bis zum letzten Satzende vor n Zeichen (kein abgeschnittenes Zitat), ohne Fußnotenzeichen."""
    text = re.sub(r"\s*\[\d+\]", "", text.replace("\n", " ")).strip()
    if len(text) <= n:
        return text
    ende = [m.end() for m in re.finditer(r"\.(?=\s+[A-ZÄÖÜ])", text[:n])
            if not re.search(r"(?:\b(?:Abs|Nr|Art|vgl|bzw|ggf|sog|[A-Za-z])|\d)\.$", text[:m.end()])]
    if not ende:  # kein Satzende in Reichweite: ganzen ersten Satz nehmen, damit kein Zitat abgeschnitten wird
        m = re.search(r"(?<![A-Za-z0-9]{1}\b)\.(?=\s+[A-ZÄÖÜ])", text[n:])
        return text[:n + m.end()] + " …" if m else text
    return text[:ende[-1]] + " …"


# Kuratierte Zusammenfassungen (Abschnittsnummer -> Text); Fristen und Fundstellen aus dem Wortlaut der Richtlinien
KURATIERT = {
    "1.1": "Anmeldetag ist der Tag, an dem Name des Anmelders, Erteilungsantrag und eine dem Anschein nach als Beschreibung anzusehende Unterlage eingegangen sind (§ 35 Abs. 1 PatG). Werden die Mindesterfordernisse nacheinander erfüllt, zählt der letzte Eingang; fehlen sie, wird nicht zurückgewiesen, sondern durch Beschluss festgestellt, dass keine rechtswirksame Anmeldung vorliegt. Nachgereichte Zeichnungen oder Beschreibungsteile verschieben den Anmeldetag (§ 35 Abs. 2, 3 PatG).",
    "1.2": "Die Offensichtlichkeitsprüfung beschränkt sich auf die in § 42 PatG genannten Erfordernisse: offensichtliche Mängel nach §§ 34, 36, 37 und 38 PatG (Aufforderung zur Beseitigung) und offensichtlich fehlende Erfindung, gewerbliche Anwendbarkeit oder ein Patentierungsausschluss (§ 42 Abs. 2 PatG); Zurückweisung nach § 42 Abs. 3 PatG nur nach rechtlichem Gehör.",
    "1.3": "Die Offensichtlichkeitsprüfung führen die fachlich zuständigen Patentprüfer durch; die formelle Bearbeitung obliegt Beamten des gehobenen und mittleren Dienstes und vergleichbaren Tarifbeschäftigten (§ 27 Abs. 5 PatG in Verbindung mit der Wahrnehmungsverordnung).",
    "1.4": "Offensichtlich ist ein Mangel, den die Prüfungsstelle ohne weitere Sachprüfung zweifelsfrei erkennt; nicht sofort verfügbares Material und Nachforschungen bleiben außer Betracht. Rechtsfragen zählen dazu, wenn gesicherte Rechtsprechung sie klar beantwortet. Neuheit und erfinderische Tätigkeit werden in der Offensichtlichkeitsprüfung nicht geprüft.",
    "1.5": "Katalog formeller Mängel: unvollständiger Erteilungsantrag, unklare Anmelderbezeichnung, fehlender Zustellungsbevollmächtigter bei mehreren Anmeldern, fehlende Unterlagen nach §§ 34 und 36 PatG, fehlende Vollmacht nichtanwaltlicher Vertreter (§ 15 Abs. 4 DPMAV), ungenaue Bezeichnung, fehlende Erfinderbenennung (§ 37 PatG).",
    "1.5.1": "Die Erfinderbenennung ist binnen 15 Monaten nach dem Anmelde- oder Prioritätstag einzureichen (§ 37 Abs. 1 PatG); bei außergewöhnlichen Umständen Fristverlängerung (§ 37 Abs. 2 PatG). Der Anmelder als Alleinerfinder braucht kein gesondertes Schriftstück, außer bei Antrag auf Nichtnennung.",
    "1.5.3": "Verstöße gegen die PatV kann die Prüfungsstelle bis zum Beginn des Prüfungsverfahrens unbeanstandet lassen (§ 42 Abs. 1 S. 2 PatG). Gerügt werden in der Offensichtlichkeitsprüfung nur Mängel, die den Druck der Offenlegungsschrift behindern oder eine sachgerechte Recherche verhindern; an die Lesbarkeit ist ein strenger Maßstab anzulegen.",
    "1.6.3": "Die Ausschlussgründe des § 42 Abs. 2 Nr. 3 PatG verweisen auf § 1a Abs. 1 PatG, § 2 PatG und § 2a Abs. 1 PatG. Ein Verstoß gegen die öffentliche Ordnung liegt nicht bei jedem Gesetzesverstoß vor, sondern nur, wenn tragende Grundsätze der Rechts- und Sittenordnung betroffen sind; bloße Vertriebsbeschränkungen hindern die Erteilung nicht (Art. 4quater PVÜ).",
    "1.7": "In der Offensichtlichkeitsprüfung wird Uneinheitlichkeit nur gerügt, wenn mehrere Erfindungen offensichtlich nichts miteinander zu tun haben. Sie ist zu verneinen, wenn sich eine technisch sinnvolle, einheitliche Aufgabe angeben lässt, zu deren Lösung alle Teile der Anmeldung erforderlich oder dienlich sind.",
    "1.8": "Keine offensichtlichen Mängel: Aktenvermerk. Sonst Mängelrüge mit Frist; ein weiterer Bescheid nur ausnahmsweise. Die abschließende Entscheidung soll spätestens vier Monate nach dem Anmeldetag ergehen, damit die Offenlegungsschrift mit berichtigten Unterlagen gedruckt werden kann.",
    "1.11": "Die Frist zur Erwiderung auf Sachbescheide kann in der Offensichtlichkeitsprüfung von vier auf zwei Monate abgekürzt werden, wenn die Prüfung sonst nicht vor der Offenlegung abgeschlossen werden kann.",
    "1.12": "Die Offenlegungsschrift erscheint nach 18 Monaten (§ 31 Abs. 2 Nr. 2 PatG) grundsätzlich mit den ursprünglichen Unterlagen, auch während eines Beschwerdeverfahrens. Sie unterbleibt, wenn die Patentschrift schon veröffentlicht ist (§ 32 Abs. 2 S. 2 PatG); ordnungs- oder sittenwidrige Bestandteile können weggelassen werden (§ 32 Abs. 2 S. 3 PatG). Unaufgefordert eingereichte neue Unterlagen werden nicht verwendet.",
    "2.1": "Prüfungsantrag durch Anmelder oder Dritte binnen sieben Jahren ab Einreichung (§ 44 Abs. 2 PatG); Prüfungsgebühr drei Monate ab Antragstellung, längstens bis zum Ablauf der Siebenjahresfrist. Der Dritte wird nicht Verfahrensbeteiligter, erhält keine Bescheide, kann aber Akteneinsicht nehmen. Spätere Anträge gelten als nicht gestellt; die Rücknahme des Antrags beendet das Verfahren nicht (§ 44 Abs. 5 PatG).",
    "2.3.1": "Bearbeitung grundsätzlich in der Reihenfolge des Eingangs der Prüfungsanträge und Erwiderungen. Bevorzugt: erteilungsreife Anmeldungen, zurückweisungsreife Anmeldungen und Fälle, in denen die Erwiderung die mitgeteilten Mängel erkennbar nicht ausräumt.",
    "2.3.2": "Auf begründeten Beschleunigungsantrag wird das Verfahren vordringlich betrieben, wenn die sonst zu erwartende Dauer zu erheblichen Nachteilen führen würde; der Antrag gilt grundsätzlich nur für die nächste Verfahrenshandlung.",
    "2.3.3": "Geprüft wird, ob die Anmeldung den §§ 34, 37 und 38 PatG genügt und der Gegenstand nach den §§ 1 bis 5 PatG patentfähig ist. Zuerst ist der Anspruch aus der Sicht des Fachmanns auszulegen (BGH Polymerschaum); dann wird recherchiert und auf die im Gesetz genannten Zurückweisungsgründe geprüft. Mangelnde „Klarheit“ als einziger Zurückweisungsgrund ohne Auslegung und Recherche soll unterbleiben.",
    "2.3.3.1": "Ausführbar offenbart ist die Erfindung, wenn der Fachmann sie mit Fachwissen und Fachkönnen erfolgreich ausführen kann (§ 34 Abs. 4 PatG; BGH Klammernahtgerät). Ein ausführbarer Weg genügt (BGH Taxol), zumutbare Versuche schaden nicht. Die Zusammenfassung gehört nicht zur Offenbarung (§ 36 PatG). Grenzen: nur aufgabenhafte Mittel und spekulativ weite Bereichsangaben (BGH Thermoplastische Zusammensetzung).",
    "2.3.3.2": "Vor der Prüfung der Patentfähigkeit ist der maßgebliche Fachmann zu definieren; aus seiner Sicht wird der Sinngehalt der Anspruchsmerkmale ausgelegt, Beschreibung und Zeichnungen sind heranzuziehen (§ 14 S. 2 PatG; BPatG Batterieüberwachungsgerät, BGH Brieflocher).",
    "2.3.3.2.1": "Technizität: Lehre zum planmäßigen Handeln unter Einsatz beherrschbarer Naturkräfte; menschliche Verstandestätigkeit schadet nicht. Die Einstufung eines Merkmals als nichttechnisch ist zu begründen. Der Katalog des § 1 Abs. 3 PatG schließt nur „als solche“ aus (§ 1 Abs. 4 PatG). Ansprüche mit technischen und nichttechnischen Merkmalen sind zugänglich, nichttechnische Merkmale bleiben bei § 4 PatG außer Acht. Mehrstufige Verfahren mit einer chirurgischen, therapeutischen oder diagnostischen Stufe sind insgesamt ausgeschlossen (§ 2a Abs. 1 Nr. 2 PatG).",
    "2.3.3.2.2": "Stand der Technik ist alles vor dem Zeitrang öffentlich Zugängliche (§ 3 Abs. 1 PatG), dazu der gesamte Offenbarungsgehalt älterer, nachveröffentlichter nationaler, europäischer und internationaler Anmeldungen (§ 3 Abs. 2 PatG). Unschädlich sind Missbrauch und amtlich anerkannte Ausstellungen in den sechs Monaten vor der Anmeldung (§ 3 Abs. 5 PatG); die Ausstellung ist bei der Anmeldung anzugeben, die Bescheinigung binnen vier Monaten vorzulegen.",
    "2.3.3.2.3": "Neuheit im Einzelvergleich: neuheitsschädlich ist nur eine Entgegenhaltung, der alle Merkmale unmittelbar und eindeutig zu entnehmen sind, einschließlich des selbstverständlich Mitgelesenen, ohne Ergänzung aus dem Fachwissen (BGH Olanzapin, Proteintrennung). Eine ältere Anmeldung bleibt Stand der Technik, auch wenn sie nach der Veröffentlichung wegfällt (BGH PALplus); ihr Inhalt darf dem jüngeren Anmelder erst nach ihrer Offenlegung mitgeteilt werden.",
    "2.3.3.2.4": "Naheliegen verlangt Können und Veranlassung: Das Bekannte muss dem Fachmann Anlass oder Anregung gegeben haben (BGH Einteilige Öse); generelle Lösungsmittel des Fachwissens genügen nur bei erkennbar passender Ausgangslage (BGH Farbversorgungssystem, Kinderbett). Fachmann ist der Entwickler, nicht der Anwender, gegebenenfalls ein Team. Hilfskriterien sind nur Anlass zu kritischer Prüfung; Aggregation und beliebige Auswahl sind nicht erfinderisch; ältere Anmeldungen bleiben außer Betracht (§ 4 S. 2 PatG); keine zergliedernde und keine rückschauende Betrachtung.",
    "2.3.3.2.6": "Recherchiert wird die in den Ansprüchen angegebene Erfindung, für alle unabhängigen und abhängigen Ansprüche möglichst in einem Arbeitsgang vor dem Erstbescheid; vor Ablauf von sechs Monaten nach dem Anmeldetag kann Stand der Technik systemseitig fehlen. Der Anmelder hat auf Verlangen den ihm bekannten Stand der Technik anzugeben (§ 34 Abs. 7 PatG); Hinweise Dritter werden dem Anmelder übersandt und von Amts wegen berücksichtigt.",
    "2.3.3.3": "Änderungen sind bis zum Erteilungsbeschluss zulässig, soweit sie den Gegenstand nicht erweitern (§ 38 PatG); vor dem Prüfungsantrag nur Berichtigungen, Mängelbeseitigung und Anspruchsänderungen. Maßstab ist, was der Fachmann den ursprünglichen Unterlagen unmittelbar und eindeutig als zur Erfindung gehörend entnimmt (BGH Fälschungssicheres Dokument); die Ansprüche dürfen innerhalb dieser Grenze auch weiter gefasst werden. „Enthält“ offenbart nicht ohne weiteres „besteht aus“ (BGH Reifenabdichtmittel). Wird die Erweiterung nicht gestrichen, ist die Anmeldung insgesamt zurückzuweisen.",
    "2.3.3.4": "Einheitlichkeit nach § 34 Abs. 5 PatG; die Beanstandung ist konkret zu begründen und mit einer Stellungnahme zur Patentfähigkeit zu verbinden. Die Ausscheidungsanmeldung entsteht mit Eingang der Ausscheidungserklärung und wird in der Verfahrenslage der Stammanmeldung weitergeführt; Anmeldegebühr, gegebenenfalls Prüfungsgebühr und Jahresgebühren werden fällig. § 39 PatG gilt für die Ausscheidung nicht entsprechend.",
    "2.3.3.5": "Die freie Teilung ist jederzeit bis zum Ablauf der Beschwerdefrist gegen den Erteilungsbeschluss möglich (BGH Graustufenbild). Zeitrang und Priorität bleiben erhalten. Unterlagen und Gebühren binnen drei Monaten nach der Teilungserklärung, sonst gilt sie als nicht abgegeben (§ 39 Abs. 3 PatG).",
    "2.3.3.6": "Ansprüche einteilig oder zweiteilig (§ 9 Abs. 1 PatV); geprüft wird stets der gesamte Anspruch. Der Oberbegriff muss nicht vom „nächsten“ Stand der Technik ausgehen. Product-by-process-Ansprüche, fakultative Merkmale und Zweck- oder Funktionsangaben sind zulässig; Zweckangaben im Sachanspruch verlangen objektive Eignung (BGH Gurtstraffer). Unteransprüche mit Kategoriewechsel sind gesondert zu prüfen. Kategorien: Erzeugnis und Verfahren (Herstellungs-, Arbeitsverfahren, Verwendung).",
    "2.3.3.7.1": "Innere Priorität: Nachanmeldung binnen zwölf Monaten (§ 40 Abs. 1 PatG), Prioritätserklärung mit Aktenzeichen binnen zwei Monaten (§ 40 Abs. 4 PatG); die anhängige frühere Patentanmeldung gilt als zurückgenommen (§ 40 Abs. 5 PatG), bei Inanspruchnahme für eine PCT-Anmeldung erst nach Art. III § 4 Abs. 4 IntPatÜG. Über die förmliche Wirksamkeit kann vorab entschieden werden.",
    "2.3.3.7.2": "Äußere Priorität: Angaben und Abschrift vor Ablauf des 16. Monats nach dem Prioritätstag (§ 41 Abs. 1 PatG). Die materielle Berechtigung wird nur geprüft, wenn entscheidungserhebliches Material im Prioritätsintervall liegt, und ohne Zwischenentscheidung. Dieselbe Erfindung verlangt die Offenbarung der Merkmalskombination als Ganzes; Merkmale verschiedener Priorität lassen sich nicht in einem Anspruch kombinieren (BGH Luftverteiler).",
    "2.4": "Bescheide bereiten Erteilung oder Zurückweisung vor und sollen auch positive Anregungen geben. Entgegenhaltungen sind mit Textstellen im Merkmalsvergleich zu erörtern, nicht pauschal; bei fehlender erfinderischer Tätigkeit ist die Veranlassung des Fachmanns darzulegen. Druckschriften werden zu Beginn nummeriert aufgelistet, die Nummern gelten im ganzen Verfahren.",
    "2.4.1": "Der erste Bescheid soll bei früh gestelltem Prüfungsantrag vier Monate vor Ablauf des Prioritätsjahres zugestellt sein. Er definiert den Fachmann, teilt Auslegung und Annahmen mit, nimmt zu allen beanspruchten Gegenständen Stellung und verbindet Formmängel mit der vollständigen Sachprüfung; Uneinheitlichkeit ist schon hier zu rügen.",
    "2.4.2": "Ein zweiter Sachbescheid soll in der Regel der letzte sein; die Anhörung hat Vorrang vor weiteren Bescheiden. Die Prüfungsstelle ändert eine begründete Auffassung nur auf überzeugende Gegendarstellung oder bei neuer Sach- oder Rechtslage, auch nach einem Prüferwechsel.",
    "2.5": "Regelfristen: ein Monat für Formmängel, vier Monate für Sachbescheide; bis zu zwölf Monate (auch wiederholt), wenn die Priorität in einer anhängigen europäischen Anmeldung mit Benennung Deutschlands beansprucht wird. Erste Fristverlängerung bei kurzer Begründung, weitere bei ausreichender Begründung. Nach Fristablauf oder Antrag auf Entscheidung nach Aktenlage kann sofort entschieden werden. Gesetzliche Fristen bleiben unberührt.",
    "2.6.1": "Der Anmelder ist auf Antrag zu hören (§ 46 Abs. 1 PatG); Dritte nur mit seinem Einverständnis. Niederschrift über den wesentlichen Gang und alle rechtserheblichen Erklärungen (§ 46 Abs. 2 PatG). Am Ende soll in der Regel ein Beschluss verkündet werden (§ 47 Abs. 1 S. 3 PatG); Rücksprachebedarf des Vertreters ist kein Aufschubgrund. An den verkündeten Beschluss ist das Amt gebunden; spätere Schriftsätze bleiben außer bei Abhilfe unberücksichtigt.",
    "2.6.3": "Telefonate klären Fragen, die keinen Bescheid erfordern (Fassung der Beschreibung, Zweifelsfragen zu neuen Unterlagen, Reinschriften); sie ersetzen weder Sachbescheide noch Anhörungen und sind durch Aktenvermerk festzuhalten.",
    "2.6.4": "Anhörung und Vernehmung im Wege der Bild- und Tonübertragung in entsprechender Anwendung des § 128a ZPO (§ 46 Abs. 1 S. 2 PatG), auf Antrag oder von Amts wegen; die Entscheidung darüber ist unanfechtbar.",
    "2.7.1": "Nach Einigung über die Ansprüche muss der Anmelder die Beschreibung anpassen (§ 10 PatV), auf Verlangen den Stand der Technik angeben (§ 34 Abs. 7 PatG), Reinschriften einreichen (§ 15 Abs. 1 PatV) und die Offenbarungsstellen der Änderungen nennen (§ 15 Abs. 3 PatV). Änderungsverlangen sind auf das Notwendige zu beschränken, um unzulässige Erweiterungen zu vermeiden.",
    "2.7.2": "Für die sprachliche Fassung ist der Anmelder verantwortlich; die Prüfungsstelle redigiert nicht, wenn die Unterlagen klar und vertretbar sind. Telefonisch vereinbarte Änderungen sind schriftlich zu bestätigen. Nach Verkündung oder Abgabe des Erteilungsbeschlusses an den Versand sind Änderungen nur noch bei Abhilfe möglich.",
    "2.8": "Beschluss ist jede abschließende Regelung, die Rechte der Beteiligten berühren kann, unabhängig von der Form. Aufbau: Rubrum, Tenor, Tatbestand, Entscheidungsgründe. Begründung entbehrlich, wenn nur der Anmelder beteiligt ist und seinem Antrag stattgegeben wird (§ 47 Abs. 1 S. 4 PatG). Rechtsmittelbelehrung nach § 47 Abs. 2 PatG; fehlt sie oder ist sie unrichtig, Beschwerde binnen eines Jahres. Wirksam mit Verkündung oder Zustellung.",
    "2.8.1": "Erteilung, wenn die Anmeldung den §§ 34, 37 und 38 PatG genügt und der Gegenstand nach den §§ 1 bis 5 PatG patentfähig ist (§ 49 Abs. 1 PatG). Der Erteilungsbeschluss kann auch bei Rechtswidrigkeit nicht widerrufen werden; die Wirkungen treten mit der Veröffentlichung im Patentblatt ein (§ 58 Abs. 1 PatG).",
    "2.8.2": "Zurückweisung bei fehlender Patentfähigkeit oder nicht beseitigten Mängeln (§ 48 PatG), auch bei Antrag auf Entscheidung nach Aktenlage nur aus Gründen, die dem Anmelder vorher mitgeteilt wurden (§ 42 Abs. 3 S. 2 PatG).",
    "2.9": "Beschwerde binnen eines Monats beim DPMA (§ 73 Abs. 2 PatG), Gebühr in derselben Frist, sonst gilt sie als nicht eingelegt (§ 6 PatKostG). Abhilfe nur bei zulässiger und begründeter Beschwerde im einseitigen Verfahren (§ 73 Abs. 3, 4 PatG); sonst Vorlage an das Bundespatentgericht ohne sachliche Stellungnahme. Rückzahlung der Beschwerdegebühr bei offensichtlichem Amtsfehler oder unzweckmäßiger Verfahrensführung.",
    "3.1.1": "Biotechnologische Erfindungen sind patentfähig (§ 2a Abs. 3 PatG; Umsetzung der Richtlinie 98/44/EG zum 28.2.2005). Die Hinterlegung biologischen Materials ergänzt die Offenbarung nach § 34 Abs. 4 PatG (§ 1 BioMatHintV); beim Anspruch auf das mikrobiologische Verfahren selbst ersetzt sie nicht den Nachweis der Wiederholbarkeit (BGH Tollwutvirus). Hinterlegung nach dem Budapester Vertrag erfordert keine gesonderte Freigabeerklärung.",
    "3.1.2.1": "Hinterlegung spätestens am Anmelde- oder Prioritätstag bei einer anerkannten Hinterlegungsstelle (§ 1 Abs. 1 BioMatHintV, § 2 BioMatHintV).",
    "3.1.2.2": "Die ursprünglichen Unterlagen müssen die bekannten Merkmale des Materials, die Hinterlegungsstelle und das Aktenzeichen nennen; das Aktenzeichen kann bei eindeutiger Zuordnung binnen 16 Monaten nach dem Anmelde- oder Prioritätstag nachgereicht werden (§ 3 Abs. 1 BioMatHintV).",
    "3.1.2.3": "Aufbewahrung fünf Jahre ab dem letzten Probenantrag, mindestens fünf Jahre über die längste Schutzdauer hinaus (§ 7 BioMatHintV); nach dem Budapester Vertrag mindestens 30 Jahre ab Hinterlegung.",
    "3.1.2.4": "Zugang zu Proben gestuft (§ 5 BioMatHintV): bis zur Offenlegung nur Hinterleger, DPMA und Berechtigte; ab Offenlegung jedermann, auf Antrag des Hinterlegers nur über einen unabhängigen Sachverständigen (Expertenlösung); nach Erteilung jedermann. Der Empfänger verpflichtet sich, die Probe nicht weiterzugeben und nur zu Versuchszwecken zu verwenden (§ 6 BioMatHintV).",
    "3.2": "Programmbezogene (computerimplementierte) Erfindungen setzen zur Ausführung einen Computer, ein Netzwerk oder eine programmierbare Vorrichtung ein und weisen mindestens ein Merkmal auf, das ganz oder teilweise mit einem Programm realisiert wird.",
    "3.2.2": "Die Gegenstände des § 1 Abs. 3 PatG sind nur als solche ausgeschlossen (§ 1 Abs. 4 PatG). Der Ausschluss kommt im Allgemeinen nur für Verfahren in Betracht, nicht für Vorrichtungen.",
    "3.2.3": "Dreistufige Prüfung: (1) Technizität nach § 1 Abs. 1 PatG, (2) Ausschluss nach § 1 Abs. 3, 4 PatG anhand der Frage, ob ein konkretes technisches Problem mit technischen Mitteln gelöst wird, (3) Neuheit und erfinderische Tätigkeit nur anhand der Anweisungen, die diese Lösung bestimmen oder beeinflussen. Die ersten beiden Stufen sind Grobsichtung ohne Stand der Technik; auch bei scheinbarem Ausschluss soll recherchiert werden. Eine feste Prüfungsreihenfolge ist nicht vorgeschrieben.",
    "3.2.3.1": "Erste Stufe: Technizität liegt vor, wenn das Verfahren die Nutzung von Komponenten einer Datenverarbeitungsanlage zumindest implizit lehrt; die Geräte müssen im Anspruch nicht genannt sein. Eine programmtechnisch eingerichtete Vorrichtung ist stets technisch (BGH Sprachanalyseeinrichtung). Nichttechnische Merkmale daneben schaden nicht.",
    "3.2.3.2": "Zweite Stufe: Löst wenigstens ein Teil der Lehre ein konkretes technisches Problem mit technischen Mitteln? Das Problem ergibt sich aus dem, was die Erfindung tatsächlich leistet (BGH Gelenkanordnung); Vorgaben des Auftraggebers gehören zum Problem. Technische Mittel: modifizierte Gerätekomponenten, durch äußere technische Gegebenheiten bestimmter Programmablauf, Rücksicht auf die Gegebenheiten der Anlage. Beispiele dafür und dagegen aus der Rechtsprechung (Steuerungseinrichtung, Flugzeugzustand, Bildstrom; Rentabilitätsermittlung, Webseitenanzeige, Anbieten interaktiver Hilfe).",
    "3.2.3.3": "Dritte Stufe: Neuheit und erfinderische Tätigkeit der Lösung; nur Anweisungen, die die Lösung des technischen Problems mit technischen Mitteln bestimmen oder beeinflussen, stützen § 4 PatG. Außer Betracht bleiben Datenauswahl, auch wenn sie Rechenschritte spart (BGH Routenplanung), und der Inhalt wiedergegebener Information (BGH Wiedergabe topografischer Informationen, Fahrzeugnavigationssystem).",
    "3.2.4": "Anmeldungen in deutscher Fachsprache mit üblichen fremdsprachigen Fachausdrücken; Datenfluss- und Programmablaufpläne sind zulässig, kurze Programmauszüge in einer genau bezeichneten Programmiersprache zur Verdeutlichung ebenfalls.",
    "3.3": "KI-bezogene Erfindungen betreffen Grundlagen (Hardware-Architekturen, Algorithmen, Modelle, Lernverfahren) oder Anwendungen. Etablierte Rechtsprechung fehlt; wegen der Nähe zu programmbezogenen Erfindungen wird deren Prüfung einschließlich des dreistufigen Ansatzes regelmäßig übertragen.",
    "4": "Akteneinsicht für jedermann nach § 31 PatG, auch über das Internet (§ 31 Abs. 3a PatG, DPMAregister), nur für veröffentlichte Anmeldungen; ausgeschlossen bei entgegenstehender Rechtsvorschrift, überwiegendem Datenschutzinteresse oder ordnungs- und sittenwidrigen Inhalten (§ 31 Abs. 3b PatG). Nichtpatentliteratur wird aus urheberrechtlichen Gründen nur auf schriftlichen Antrag zugänglich gemacht.",
}
_unbekannt = sorted(set(KURATIERT) - set(_BY_NR))
if _unbekannt:
    raise SystemExit("patent/richtlinien.py: kuratierte Abschnitte fehlen in data/dpma_pruefungsrichtlinien.json: " + ", ".join(_unbekannt))


def _summary(a):
    if a["nr"] in KURATIERT:
        return KURATIERT[a["nr"]]
    if a["text"]:
        return _kurz(a["text"])
    kinder = [b for b in ABSCHNITTE if b["nr"].startswith(a["nr"] + ".") and b["ebene"] == a["ebene"] + 1]
    return "Gliederungsabschnitt mit den Unterabschnitten: " + "; ".join("%s %s" % (b["nr"], b["titel"]) for b in kinder) + "."


QUELLEN = [dict(page="prl:" + a["nr"], title="Prüfungsrichtlinien %s %s" % (a["nr"], a["titel"]), summary=_summary(a), url=_url(a),
                provider=PROVIDER, seite=a["seite"], kuratiert=a["nr"] in KURATIERT)
           for a in ABSCHNITTE if a["nr"]]
QUELLEN.insert(0, dict(page="prl:0", title="Prüfungsrichtlinien: Vorbemerkung und Rechtsgrundlagen",
                       summary="Die Richtlinien vom %s ersetzen die Fassung vom 6. Mai 2025. Sie enthalten die Grundsätze des Prüfungsverfahrens vor dem DPMA "
                               "(Offensichtlichkeitsprüfung, Recherche, Bescheid, Erteilung, Zurückweisung) und sollen eine einheitliche und zügige Behandlung sichern; "
                               "Besonderheiten des Einzelfalls und die aktuelle Rechtsprechung gehen vor. Rechtsrahmen: PatG, PatV, DPMAV, Wahrnehmungsverordnung, "
                               "PatKostG, PatKostZV, DPMA-Verwaltungskostenverordnung, ERVDPMAV, EAPatV und VwZG." % META["stand"],
                       url=URL + "#page=5", provider=PROVIDER, seite=5, kuratiert=True))
SEITEN = {w["page"] for w in QUELLEN}

# Begriff -> Abschnitte der Richtlinien (Kante documented_in); concepts.py hängt sie an `quellen`
BEGRIFF_QUELLEN = {
    "pat_pruefungsrichtlinien": ["prl:0", "prl:2.3.3"],
    "pat_offensichtlichkeitspruefung": ["prl:1.2", "prl:1.4", "prl:1.5", "prl:1.8"],
    "pat_pruefungsantrag": ["prl:2.1", "prl:2.2"],
    "pat_pruefungsbescheid": ["prl:2.4", "prl:2.4.1", "prl:2.4.2", "prl:2.5"],
    "pat_anhoerung": ["prl:2.6.1", "prl:2.6.3", "prl:2.6.4"],
    "pat_einheitlichkeit": ["prl:1.7", "prl:2.3.3.4"],
    "pat_beschluss_pruefungsstelle": ["prl:2.8", "prl:2.8.1", "prl:2.8.2"],
    "pat_abhilfe": ["prl:2.9"],
    "pat_hilfskriterien": ["prl:2.3.3.2.4"],
    "pat_patentkategorie": ["prl:2.3.3.6"],
    "pat_hinterlegung": ["prl:3.1.1", "prl:3.1.2.1", "prl:3.1.2.2", "prl:3.1.2.3", "prl:3.1.2.4"],
    "pat_dreistufige_pruefung": ["prl:3.2.3", "prl:3.2.3.1", "prl:3.2.3.2", "prl:3.2.3.3"],
    "pat_ki_erfindung": ["prl:3.3"],
    "pat_recherche_pruefung": ["prl:2.3.3.2.6"],
    "pat_erteilungsreife_unterlagen": ["prl:2.7.1", "prl:2.7.2"],
    # bestehende Begriffe
    "pat_pruefungsverfahren": ["prl:2.1", "prl:2.3.3", "prl:2.4"],
    "pat_anmeldetag": ["prl:1.1"],
    "pat_erfinderbenennung": ["prl:1.5.1"],
    "pat_akteneinsicht": ["prl:1.12", "prl:4"],
    "pat_ausfuehrbarkeit": ["prl:2.3.3.1"],
    "pat_technizitaet": ["prl:2.3.3.2.1", "prl:3.2.1"],
    "pat_programme": ["prl:3.2", "prl:3.2.2", "prl:3.2.3"],
    "pat_biotech": ["prl:1.6.3", "prl:3.1.1"],
    "pat_therapeutische_verfahren": ["prl:1.6.2", "prl:2.3.3.2.1"],
    "pat_neuheit": ["prl:2.3.3.2.2", "prl:2.3.3.2.3"],
    "pat_offenbarung": ["prl:2.3.3.2.3", "prl:2.3.3.3"],
    "pat_zweite_indikation": ["prl:2.3.3.2.3"],
    "pat_erfinderische_taetigkeit": ["prl:2.3.3.2.4"],
    "pat_fachmann": ["prl:2.3.3.2", "prl:2.3.3.2.4"],
    "pat_aufgabe_loesung": ["prl:3.2.3.2"],
    "pat_gewerbliche_anwendbarkeit": ["prl:2.3.3.2.5"],
    "pat_auslegung": ["prl:2.3.3", "prl:2.3.3.2"],
    "pat_unzulaessige_erweiterung": ["prl:2.3.3.3"],
    "pat_teilung": ["prl:2.3.3.4", "prl:2.3.3.5"],
    "pat_patentanspruch": ["prl:2.3.3.6"],
    "pat_zweckangabe": ["prl:2.3.3.6"],
    "pat_prioritaet": ["prl:2.3.3.7.1", "prl:2.3.3.7.2"],
    "pat_beschreibung": ["prl:2.7.1"],
    "pat_beschwerde": ["prl:2.9"],
    "pat_rechtliches_gehoer": ["prl:2.8.2", "prl:2.6.1"],
}
_falsch = sorted({p for v in BEGRIFF_QUELLEN.values() for p in v} - SEITEN)
if _falsch:
    raise SystemExit("patent/richtlinien.py: unbekannte Abschnitte in BEGRIFF_QUELLEN: " + ", ".join(_falsch))
