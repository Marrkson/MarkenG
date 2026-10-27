# -*- coding: utf-8 -*-
"""Leitentscheidungen der Beschwerdekammern des EPA (Große Beschwerdekammer, Juristische und Technische Beschwerdekammern).

Quelle: Tabelle BoaDecision der RheinIP-Datenbank (data/epc_decisions.json). Jede Entscheidung wird beim Import gegen den Korpus
geprüft (Aktenzeichen und Datum); URL kommt aus der Datenbank (deutsche Fassung, wenn es eine gibt). `kern` fasst den Leitsatz in
eigenen Worten zusammen. Gerichte: GBK (Große Beschwerdekammer), JBK (Juristische Beschwerdekammer), TBK (Technische Beschwerdekammer).
Zitierweise in `norms`: `Art. 54 Abs. 3 EPÜ`, `R. 36 Abs. 1 EPÜ`.
"""
from . import entscheidungen as _k

_GERICHT = {"G": "GBK", "J": "JBK", "T": "TBK", "R": "GBK"}


def eb(id, name, az, date, kern, norms=(), concepts=(), tags=()):
    rec = _k.by_az(az, date)
    if rec is None:
        raise ValueError(f"Entscheidung {az} vom {date} ({name}) nicht im Korpus data/epc_decisions.json")
    court = _GERICHT[az[0]]
    fund = f"{court}, {'Entscheidung' if az[0] != 'G' else 'Entscheidung/Stellungnahme'} vom {date[8:]}.{date[5:7]}.{date[:4]} – {az}"
    return dict(id=id, name=f"{az} – {name}", court=court, date=date, az=az, fundstelle=fund, norms=list(norms), concepts=list(concepts),
                kern=kern, tags=list(tags), url=rec.get("url_de") or rec["url"], url_en=rec["url"])


CASES = [
    # ------------------------------------------------------------------ Stand der Technik, Neuheit
    eb("epc_g_1_92", "Öffentliche Zugänglichkeit", "G 1/92", "1992-12-18",
       "Die chemische Zusammensetzung eines Erzeugnisses gehört zum Stand der Technik, wenn das Erzeugnis selbst öffentlich zugänglich ist und "
       "der Fachmann es analysieren und reproduzieren kann; ein besonderer Anlass zur Analyse ist nicht nötig.",
       norms=["Art. 54 Abs. 2 EPÜ"], concepts=["epc_stand_der_technik"], tags=["Neuheit", "Stand der Technik"]),
    eb("epc_g_1_23", "Auf den Markt gebrachtes Erzeugnis", "G 1/23", "2025-07-02",
       "Ein vor dem Anmeldetag in Verkehr gebrachtes Erzeugnis gehört zum Stand der Technik, auch wenn der Fachmann seine Zusammensetzung oder "
       "innere Struktur nicht analysieren und reproduzieren konnte; öffentlich zugängliche technische Informationen über das Erzeugnis gehören "
       "ebenfalls dazu. G 1/92 ist insoweit präzisiert.",
       norms=["Art. 54 Abs. 2 EPÜ"], concepts=["epc_stand_der_technik"], tags=["Neuheit", "Stand der Technik"]),
    eb("epc_g_2_08", "Dosierungsanleitung", "G 2/08", "2010-02-19",
       "Art. 54 Abs. 5 EPÜ erlaubt den Schutz eines bekannten Arzneimittels für eine andere therapeutische Behandlung derselben Krankheit, auch "
       "wenn das einzige neue Merkmal eine Dosierungsanleitung ist. Ansprüche im schweizerischen Format sind für solche Erfindungen nicht mehr zulässig.",
       norms=["Art. 54 Abs. 5 EPÜ", "Art. 53 EPÜ"], concepts=["epc_medizinische_indikation"], tags=["Neuheit", "Medizinische Indikation"]),
    eb("epc_g_3_98", "Sechsmonatsfrist", "G 3/98", "2000-07-12",
       "Die Frist von sechs Monaten für unschädliche Offenbarungen nach Art. 55 Abs. 1 EPÜ berechnet sich vom Tag der tatsächlichen Einreichung "
       "der europäischen Anmeldung; der Prioritätstag zählt nicht.",
       norms=["Art. 55 Abs. 1 EPÜ"], concepts=["epc_unschaedliche_offenbarung"], tags=["Neuheit"]),
    eb("epc_g_3_93", "Prioritätsintervall", "G 3/93", "1994-08-16",
       "Eine im Prioritätsintervall veröffentlichte Druckschrift mit demselben Inhalt wie das Prioritätsdokument ist Stand der Technik nach "
       "Art. 54 Abs. 2 EPÜ, soweit der Prioritätsanspruch unwirksam ist, auch wenn er nur deshalb unwirksam ist, weil nicht dieselbe Erfindung vorliegt.",
       norms=["Art. 54 Abs. 2 EPÜ", "Art. 89 EPÜ"], concepts=["epc_prioritaet", "epc_stand_der_technik"], tags=["Priorität", "Neuheit"]),
    # ------------------------------------------------------------------ Priorität
    eb("epc_g_2_98", "Dieselbe Erfindung", "G 2/98", "2001-05-31",
       "Die Priorität ist für einen Anspruch nur anzuerkennen, wenn der Fachmann dessen Gegenstand unter Heranziehung des allgemeinen Fachwissens "
       "unmittelbar und eindeutig der früheren Anmeldung als Ganzes entnehmen kann.",
       norms=["Art. 87 Abs. 1 EPÜ", "Art. 88 EPÜ"], concepts=["epc_prioritaet"], tags=["Priorität"]),
    eb("epc_g_1_15", "Teilpriorität", "G 1/15", "2016-11-29",
       "Ein generischer „ODER“-Anspruch hat Anspruch auf Teilpriorität für die alternativen Gegenstände, die im Prioritätsdokument erstmals, "
       "unmittelbar oder zumindest implizit, eindeutig und ausführbar offenbart sind; weitere Bedingungen gibt es nicht.",
       norms=["Art. 87 Abs. 1 EPÜ", "Art. 88 Abs. 2 EPÜ", "Art. 88 Abs. 3 EPÜ"], concepts=["epc_prioritaet", "epc_teilprioritaet"], tags=["Priorität"]),
    eb("epc_g_1_22", "Prioritätsberechtigung", "G 1/22", "2023-10-10",
       "Das EPA prüft selbst, ob der Anmelder zur Inanspruchnahme der Priorität berechtigt ist. Nach dem autonomen Recht des EPÜ besteht eine "
       "widerlegbare Vermutung der Berechtigung, auch bei PCT-Anmeldungen und wenn Prioritäts- und Nachanmelder nicht identisch sind; eine "
       "gemeinsame PCT-Anmeldung von A und B begründet eine stillschweigende Übereinkunft zur Nutzung der Priorität.",
       norms=["Art. 87 Abs. 1 EPÜ", "Art. 88 Abs. 1 EPÜ"], concepts=["epc_prioritaet"], tags=["Priorität"]),
    # ------------------------------------------------------------------ Änderungen, Disclaimer, Berichtigung
    eb("epc_g_1_03", "Disclaimer (nicht offenbart)", "G 1/03", "2004-04-08",
       "Ein in der ursprünglichen Anmeldung nicht offenbarter Disclaimer kann nach Art. 123 Abs. 2 EPÜ zulässig sein, wenn er die Neuheit "
       "gegenüber Stand der Technik nach Art. 54 Abs. 3 EPÜ oder einer zufälligen Vorwegnahme wiederherstellt oder Gegenstände ausklammert, die "
       "aus nichttechnischen Gründen ausgeschlossen sind; er darf nicht mehr ausschließen als nötig.",
       norms=["Art. 123 Abs. 2 EPÜ", "Art. 54 Abs. 3 EPÜ"], concepts=["epc_disclaimer", "epc_unzulaessige_erweiterung"], tags=["Änderungen"]),
    eb("epc_g_2_10", "Disclaimer (offenbart)", "G 2/10", "2011-08-30",
       "Klammert ein Disclaimer einen ursprünglich offenbarten Gegenstand aus, verstößt die Änderung gegen Art. 123 Abs. 2 EPÜ, wenn der "
       "verbleibende Gegenstand nicht unmittelbar und eindeutig ursprünglich offenbart ist (Goldstandard).",
       norms=["Art. 123 Abs. 2 EPÜ"], concepts=["epc_disclaimer", "epc_unzulaessige_erweiterung"], tags=["Änderungen"]),
    eb("epc_g_1_16", "Disclaimer III", "G 1/16", "2017-12-18",
       "Für nicht offenbarte Disclaimer gelten allein die Kriterien aus G 1/03; der Disclaimer darf keinen technischen Beitrag leisten und für "
       "erfinderische Tätigkeit oder Ausführbarkeit nicht relevant werden. Der Goldstandard aus G 2/10 gilt für ihn nicht.",
       norms=["Art. 123 Abs. 2 EPÜ"], concepts=["epc_disclaimer"], tags=["Änderungen"]),
    eb("epc_g_1_93", "Beschränkendes Merkmal", "G 1/93", "1994-02-02",
       "Enthält ein Patent ein unzulässig erweiterndes, aber den Schutzbereich beschränkendes Merkmal, kann es weder unverändert bleiben "
       "(Art. 100 lit. c EPÜ) noch durch Streichung des Merkmals gerettet werden (Art. 123 Abs. 3 EPÜ) – die „unentrinnbare Falle“. Ein Merkmal "
       "ohne technischen Beitrag, das nur den Schutz einschränkt, gilt nicht als unzulässige Erweiterung.",
       norms=["Art. 123 Abs. 2 EPÜ", "Art. 123 Abs. 3 EPÜ", "Art. 100 EPÜ"], concepts=["epc_unzulaessige_erweiterung", "epc_schutzbereichserweiterung"], tags=["Änderungen", "Einspruch"]),
    eb("epc_g_2_88", "Kategoriewechsel", "G 2/88", "1989-12-11",
       "Ein Wechsel der Anspruchskategorie im Einspruchsverfahren verstößt nicht gegen Art. 123 Abs. 3 EPÜ, wenn er den Schutzbereich nicht "
       "erweitert; der Wechsel vom Stoffanspruch zum Verwendungsanspruch ist zulässig.",
       norms=["Art. 123 Abs. 3 EPÜ", "Art. 69 EPÜ"], concepts=["epc_schutzbereichserweiterung"], tags=["Änderungen", "Einspruch"]),
    eb("epc_g_3_89", "Berichtigung der Offenbarung", "G 3/89", "1992-11-19",
       "Beschreibung, Ansprüche und Zeichnungen dürfen nach R. 139 EPÜ nur berichtigt werden, wenn der Fachmann den Fehler und die richtige "
       "Fassung den ursprünglichen Unterlagen unmittelbar und eindeutig entnimmt; die Berichtigung ist feststellend und keine Erweiterung.",
       norms=["R. 139 EPÜ", "Art. 123 Abs. 2 EPÜ"], concepts=["epc_berichtigung"], tags=["Berichtigung"]),
    eb("epc_g_1_10", "Berichtigung des Patents", "G 1/10", "2012-07-23",
       "R. 140 EPÜ erlaubt nur die Berichtigung von Fehlern in Entscheidungen, nicht des Wortlauts des erteilten Patents; ein solcher Antrag des "
       "Inhabers ist zu jedem Zeitpunkt unzulässig. Fehler in der Druckfassung müssen vor Erteilung (R. 71 Abs. 3 EPÜ) gerügt werden.",
       norms=["R. 140 EPÜ", "R. 139 EPÜ", "R. 71 Abs. 3 EPÜ"], concepts=["epc_berichtigung", "epc_erteilung"], tags=["Berichtigung", "Erteilung"]),
    eb("epc_g_1_24", "Auslegung der Ansprüche", "G 1/24", "2025-06-18",
       "Die Ansprüche sind Ausgangspunkt der Prüfung der Patentierbarkeit; Beschreibung und Zeichnungen sind bei ihrer Auslegung stets "
       "heranzuziehen, nicht erst, wenn ein Anspruch für sich genommen unklar ist.",
       norms=["Art. 69 EPÜ", "Art. 84 EPÜ"], concepts=["epc_anspruchsauslegung"], tags=["Auslegung"]),
    eb("epc_g_1_25", "Anpassung der Beschreibung", "G 1/25", "2026-09-03",
       "Werden die Ansprüche im Verfahren vor dem EPA geändert und entsteht dadurch ein Widerspruch zur Beschreibung, der zu einem Verstoß gegen "
       "Art. 52 bis 57 EPÜ, Art. 76 Abs. 1 EPÜ, Art. 83 EPÜ, Art. 84 EPÜ oder Art. 123 Abs. 2, 3 EPÜ führt, ist die Beschreibung anzupassen.",
       norms=["Art. 84 EPÜ", "Art. 123 Abs. 2 EPÜ"], concepts=["epc_anspruchsauslegung"], tags=["Änderungen", "Prüfung"]),
    # ------------------------------------------------------------------ Teilanmeldung, Doppelpatentierung
    eb("epc_g_1_05", "Teilanmeldung mit Erweiterung", "G 1/05", "2007-06-28",
       "Eine Teilanmeldung, die bei Einreichung über den Inhalt der Stammanmeldung hinausgeht, kann später noch so geändert werden, dass sie "
       "Art. 76 Abs. 1 EPÜ genügt, auch wenn die Stammanmeldung nicht mehr anhängig ist; sie erhält dann Anmeldetag und Priorität der Stammanmeldung.",
       norms=["Art. 76 Abs. 1 EPÜ"], concepts=["epc_teilanmeldung"], tags=["Teilanmeldung"]),
    eb("epc_g_1_06", "Kette von Teilanmeldungen", "G 1/06", "2007-06-28",
       "Bei einer Kette von Teilanmeldungen muss sich die gesamte Offenbarung jeder Teilanmeldung unmittelbar und eindeutig aus jeder "
       "vorangehenden Anmeldung in der ursprünglich eingereichten Fassung ableiten lassen.",
       norms=["Art. 76 Abs. 1 EPÜ"], concepts=["epc_teilanmeldung"], tags=["Teilanmeldung"]),
    eb("epc_g_1_09", "Anhängigkeit nach Zurückweisung", "G 1/09", "2010-09-27",
       "Eine zurückgewiesene Anmeldung bleibt ohne Beschwerde bis zum Ablauf der Beschwerdefrist anhängig; bis dahin kann eine Teilanmeldung "
       "eingereicht werden (R. 36 Abs. 1 EPÜ).",
       norms=["R. 36 Abs. 1 EPÜ", "Art. 108 EPÜ"], concepts=["epc_teilanmeldung", "epc_anhaengigkeit"], tags=["Teilanmeldung"]),
    eb("epc_j_4_11", "Keine Anhängigkeit während der Wiedereinsetzungsfrist", "J 4/11", "2011-11-25",
       "Eine wegen Nichtzahlung einer Jahresgebühr als zurückgenommen geltende Anmeldung ist während der Frist für den Wiedereinsetzungsantrag "
       "und nach dessen Zurückweisung nicht anhängig; eine Teilanmeldung kann in dieser Zeit nicht eingereicht werden.",
       norms=["R. 36 Abs. 1 EPÜ", "Art. 122 EPÜ", "Art. 86 Abs. 1 EPÜ"], concepts=["epc_teilanmeldung", "epc_anhaengigkeit"], tags=["Teilanmeldung", "Wiedereinsetzung"]),
    eb("epc_j_18_09", "Euro-PCT ohne Eintritt nicht anhängig", "J 18/09", "2010-09-01",
       "Eine internationale Anmeldung, für die die Handlungen zum Eintritt in die europäische Phase nicht vorgenommen wurden, ist vor dem EPA "
       "nicht anhängig; zu ihr kann keine Teilanmeldung nach R. 36 Abs. 1 EPÜ eingereicht werden.",
       norms=["R. 36 Abs. 1 EPÜ", "Art. 153 EPÜ", "R. 159 EPÜ"], concepts=["epc_teilanmeldung", "epc_euro_pct"], tags=["Teilanmeldung", "Euro-PCT"]),
    eb("epc_g_4_19", "Doppelpatentierung", "G 4/19", "2021-06-22",
       "Eine Anmeldung kann nach Art. 97 Abs. 2 und Art. 125 EPÜ zurückgewiesen werden, wenn sie denselben Gegenstand beansprucht wie ein "
       "demselben Anmelder bereits erteiltes europäisches Patent, gleich ob es sich um parallele, Stamm-, Teil- oder Prioritätsanmeldungen handelt.",
       norms=["Art. 97 Abs. 2 EPÜ", "Art. 125 EPÜ", "Art. 76 Abs. 1 EPÜ"], concepts=["epc_teilanmeldung"], tags=["Teilanmeldung", "Prüfung"]),
    # ------------------------------------------------------------------ Einspruch
    eb("epc_g_9_91", "Umfang der Prüfungsbefugnis", "G 9/91", "1993-03-31",
       "Die Einspruchsabteilung und die Kammer prüfen nur in dem Umfang, in dem das Patent angegriffen ist; abhängige Ansprüche eines "
       "gefallenen unabhängigen Anspruchs dürfen geprüft werden, wenn ihre Gültigkeit prima facie zweifelhaft ist.",
       norms=["Art. 101 EPÜ", "R. 76 Abs. 2 EPÜ"], concepts=["epc_einspruch"], tags=["Einspruch"]),
    eb("epc_g_10_91", "Neue Einspruchsgründe", "G 10/91", "1993-03-31",
       "Die Einspruchsabteilung prüft grundsätzlich nur die vorgebrachten Gründe, ausnahmsweise weitere, die prima facie entgegenstehen; im "
       "Beschwerdeverfahren dürfen neue Einspruchsgründe nur mit Einverständnis des Inhabers geprüft werden.",
       norms=["Art. 100 EPÜ", "Art. 114 Abs. 1 EPÜ"], concepts=["epc_einspruch", "epc_einspruchsgruende"], tags=["Einspruch", "Beschwerde"]),
    eb("epc_g_3_14", "Klarheit geänderter Ansprüche", "G 3/14", "2015-03-24",
       "Im Einspruchsverfahren sind geänderte Ansprüche auf Klarheit (Art. 84 EPÜ) nur zu prüfen, soweit gerade die Änderung den Mangel "
       "herbeiführt; die bloße Kombination erteilter Ansprüche genügt dafür nicht.",
       norms=["Art. 101 Abs. 3 EPÜ", "Art. 84 EPÜ"], concepts=["epc_einspruch", "epc_einspruchsgruende"], tags=["Einspruch"]),
    eb("epc_g_4_88", "Übertragung des Einspruchs", "G 4/88", "1989-04-24",
       "Ein anhängiger Einspruch kann zusammen mit dem Geschäftsbereich des Einsprechenden, auf den er sich bezieht, auf einen Dritten "
       "übertragen werden.",
       norms=["Art. 99 EPÜ"], concepts=["epc_einsprechendenstellung"], tags=["Einspruch"]),
    eb("epc_g_2_04", "Keine freie Übertragbarkeit", "G 2/04", "2005-05-25",
       "Die Stellung als Einsprechender ist nicht frei übertragbar; eine Tochtergesellschaft, deren Aktien veräußert werden, nimmt sie nicht mit. "
       "Bei berechtigter Unsicherheit darf die Beschwerde hilfsweise im Namen einer anderen Person eingelegt werden.",
       norms=["Art. 99 EPÜ", "Art. 107 EPÜ"], concepts=["epc_einsprechendenstellung"], tags=["Einspruch", "Beschwerde"]),
    eb("epc_g_3_97", "Einspruch in fremdem Auftrag", "G 3/97", "1999-01-21",
       "Ein Einspruch ist nicht schon deshalb unzulässig, weil der Einsprechende für einen Dritten handelt (Strohmann); unzulässig ist er bei "
       "missbräuchlicher Gesetzesumgehung, etwa im Auftrag des Patentinhabers.",
       norms=["Art. 99 Abs. 1 EPÜ"], concepts=["epc_einspruch"], tags=["Einspruch"]),
    eb("epc_g_9_93", "Einspruch des Inhabers", "G 9/93", "1994-07-06",
       "Der Patentinhaber kann gegen sein eigenes europäisches Patent keinen Einspruch einlegen (Aufgabe von G 1/84); zur Beschränkung dient seit "
       "2007 Art. 105a EPÜ.",
       norms=["Art. 99 Abs. 1 EPÜ", "Art. 105a EPÜ"], concepts=["epc_einspruch", "epc_beschraenkung"], tags=["Einspruch"]),
    eb("epc_g_3_99", "Gemeinsamer Einspruch", "G 3/99", "2002-02-18",
       "Ein von mehreren Personen gemeinsam eingelegter Einspruch ist mit einer Einspruchsgebühr zulässig; die Beschwerde muss dann der "
       "gemeinsame Vertreter einlegen (R. 151 EPÜ).",
       norms=["Art. 99 Abs. 1 EPÜ", "R. 151 Abs. 1 EPÜ"], concepts=["epc_einspruch", "epc_vertretung"], tags=["Einspruch", "Vertretung"]),
    eb("epc_g_1_13", "Wiederaufgelebter Einsprechender", "G 1/13", "2014-11-25",
       "Erlischt ein einsprechendes Unternehmen und lebt es nach nationalem Recht rückwirkend wieder auf, muss das EPA die Rückwirkung "
       "anerkennen und das Verfahren mit ihm fortsetzen.",
       norms=["Art. 99 EPÜ", "R. 84 EPÜ"], concepts=["epc_einsprechendenstellung"], tags=["Einspruch"]),
    eb("epc_g_2_24", "Beitretender ohne Beschwerdeführerstellung", "G 2/24", "2025-09-25",
       "Werden alle Beschwerden zurückgenommen, kann das Beschwerdeverfahren nicht mit einem Dritten fortgesetzt werden, der erst im "
       "Beschwerdeverfahren nach Art. 105 EPÜ beigetreten ist; er erlangt keine Stellung als Beschwerdeführer.",
       norms=["Art. 105 EPÜ", "Art. 107 EPÜ"], concepts=["epc_beitritt", "epc_beschwerde"], tags=["Einspruch", "Beschwerde"]),
    # ------------------------------------------------------------------ Beschwerde
    eb("epc_g_1_18", "Beschwerde ohne fristgerechte Gebühr", "G 1/18", "2019-07-18",
       "Wird die Beschwerdeschrift oder die Beschwerdegebühr nach Ablauf der Zweimonatsfrist des Art. 108 Satz 1 EPÜ eingereicht bzw. entrichtet, "
       "gilt die Beschwerde als nicht eingelegt (nicht: unzulässig); die Gebühr wird von Amts wegen zurückgezahlt.",
       norms=["Art. 108 EPÜ"], concepts=["epc_beschwerde"], tags=["Beschwerde"]),
    eb("epc_g_1_12", "Berichtigung des Beschwerdeführers", "G 1/12", "2014-04-30",
       "Ist in der Beschwerdeschrift versehentlich die falsche Person als Beschwerdeführer genannt, kann der Name nach R. 101 Abs. 2 EPÜ "
       "berichtigt werden, wenn die Erfordernisse der R. 101 Abs. 1 EPÜ erfüllt sind; es gilt freie Beweiswürdigung.",
       norms=["R. 101 Abs. 2 EPÜ", "R. 99 Abs. 1 EPÜ", "R. 139 EPÜ"], concepts=["epc_beschwerde", "epc_berichtigung"], tags=["Beschwerde"]),
    eb("epc_g_1_99", "Reformatio in peius", "G 1/99", "2001-04-02",
       "Ist der Einsprechende alleiniger Beschwerdeführer, darf er durch die Entscheidung nicht schlechter gestellt werden; ausnahmsweise darf "
       "der Inhaber Änderungen vornehmen, um einen Widerruf infolge einer unzulässigen Änderung abzuwenden.",
       norms=["Art. 107 EPÜ", "Art. 111 EPÜ"], concepts=["epc_beschwerde"], tags=["Beschwerde"]),
    eb("epc_g_3_03", "Rückzahlung bei Abhilfe", "G 3/03", "2005-01-28",
       "Hilft die erste Instanz der Beschwerde ab, ist sie nicht befugt, einen Antrag auf Rückzahlung der Beschwerdegebühr zurückzuweisen; "
       "darüber entscheidet die Beschwerdekammer.",
       norms=["Art. 109 Abs. 1 EPÜ", "R. 103 EPÜ"], concepts=["epc_beschwerde"], tags=["Beschwerde"]),
    eb("epc_g_2_97", "Treu und Glauben", "G 2/97", "1998-11-12",
       "Der Vertrauensschutz verpflichtet die Kammer nicht, einen Beschwerdeführer auf eine noch ausstehende Beschwerdegebühr hinzuweisen, "
       "wenn nichts darauf hindeutet, dass er die Frist versehentlich versäumen wird.",
       norms=["Art. 108 EPÜ"], concepts=["epc_beschwerde", "epc_vertrauensschutz"], tags=["Beschwerde"]),
    # ------------------------------------------------------------------ Rechtsbehelfe bei Fristversäumnis
    eb("epc_j_5_80", "Sorgfalt des Vertreters", "J 5/80", "1981-07-07",
       "Wiedereinsetzung setzt voraus, dass auch der Vertreter die gebotene Sorgfalt beachtet hat. Fehler einer Hilfsperson werden ihm nicht "
       "zugerechnet, wenn er sie sorgfältig ausgewählt, eingewiesen und überwacht hat.",
       norms=["Art. 122 Abs. 1 EPÜ"], concepts=["epc_wiedereinsetzung"], tags=["Wiedereinsetzung"]),
    eb("epc_g_1_86", "Wiedereinsetzung des Einsprechenden", "G 1/86", "1987-06-24",
       "Art. 122 EPÜ gilt nicht nur für Anmelder und Inhaber: Ein Einsprechender als Beschwerdeführer kann in die versäumte Frist für die "
       "Beschwerdebegründung wiedereingesetzt werden.",
       norms=["Art. 122 Abs. 1 EPÜ", "Art. 108 EPÜ"], concepts=["epc_wiedereinsetzung", "epc_beschwerde"], tags=["Wiedereinsetzung", "Beschwerde"]),
    eb("epc_j_6_22", "Vollständige Begründung des Wiedereinsetzungsantrags", "J 6/22", "2023-07-26",
       "Der Wiedereinsetzungsantrag muss alle Gründe und Beweismittel sofort vollständig angeben; nachträgliches Vorbringen ist ausgeschlossen. "
       "Ein Recht auf mündliche Verhandlung besteht nicht unbegrenzt.",
       norms=["Art. 122 EPÜ", "R. 136 Abs. 2 EPÜ"], concepts=["epc_wiedereinsetzung"], tags=["Wiedereinsetzung"]),
    eb("epc_j_10_20", "Vertrauen auf Fristverlängerung", "J 10/20", "2021-01-22",
       "Auf Mitteilungen des EPA über Fristverlängerungen nach R. 134 Abs. 4 EPÜ dürfen sich Beteiligte verlassen, auch wenn tatsächlich keine "
       "allgemeine Störung des Postverkehrs vorlag (Vertrauensschutz).",
       norms=["R. 134 EPÜ"], concepts=["epc_fristen", "epc_vertrauensschutz"], tags=["Fristen"]),
    # ------------------------------------------------------------------ Berechtigung, Sprache, Euro-PCT
    eb("epc_j_14_19", "Aussetzung nur vor Erteilung", "J 14/19", "2021-04-19",
       "Die Voraussetzungen der Aussetzung nach R. 14 Abs. 1 EPÜ müssen vor dem Hinweis auf die Erteilung nachgewiesen werden; wann das nationale "
       "Verfahren eingeleitet ist, richtet sich nach dem Prozessrecht des angerufenen Gerichts.",
       norms=["R. 14 Abs. 1 EPÜ", "Art. 61 Abs. 1 EPÜ"], concepts=["epc_vindikation"], tags=["Berechtigung"]),
    eb("epc_g_4_08", "Verfahrenssprache bei Euro-PCT", "G 4/08", "2010-02-16",
       "Ist eine PCT-Anmeldung in einer Amtssprache des EPA eingereicht und veröffentlicht, kann beim Eintritt in die europäische Phase keine "
       "Übersetzung in eine andere Amtssprache eingereicht werden; das EPA verwendet im schriftlichen Verfahren nur die Verfahrenssprache.",
       norms=["Art. 14 Abs. 3 EPÜ", "Art. 153 EPÜ", "R. 159 Abs. 1 EPÜ"], concepts=["epc_sprachen", "epc_euro_pct"], tags=["Sprache", "Euro-PCT"]),
]
