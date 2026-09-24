# -*- coding: utf-8 -*-
"""Normtexte des Wissenspakets Patentrecht: PatG, PatV, IntPatÜG (amtlich IntPatÜbkG) und PatKostG.

Wortlaut aus data/patg.json, patv.json, intpatueg.json, patkostg.json (gesetze-im-internet.de, XML; erzeugt von
tools/fetch_patent.py). Die vier Gesetze sind wie EPGÜ und VerfO als Normfamilien registriert (build_graph.RICHTLINIEN,
Knoten `eunorm:<key>:<nr>`), Zitierform in `norms`-Feldern: `§ 3 Abs. 1 PatG`, `§ 9 PatV`, `Art. II § 6 Abs. 1 Nr. 3 IntPatÜG`,
`§ 6 Abs. 1 PatKostG`, `Anlage PatKostG` (Gebührenverzeichnis).

Hier nur die Anreicherung: `PATG_TITEL` (das PatG trägt keine amtlichen Paragraphenüberschriften), `HINWEISE_*` (Lern- und
Klausurhinweis je Vorschrift), `BEZUG_*` (Kante `konkretisiert`: PatV, PatKostG und IntPatÜG zeigen auf die PatG-Vorschrift,
die sie ausfüllen) und `ENTSPRICHT_*` (Kante `entspricht`: Vorschriften gleicher Funktion im EPGÜ oder in der EPatVO).
Die Umsetzung der Durchsetzungsrichtlinie im PatG (`implements`) erzeugt build_graph aus durchsetzungsrl.umsetzung_weitere.
"""
import json
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data"

# ------------------------------------------------------------------ PatG: Stichworte je Paragraph (amtlich ohne Überschrift)
PATG_TITEL = {
    "1": "Patentfähige Erfindungen; Ausschlüsse (Entdeckungen, Programme, Wiedergabe von Informationen)",
    "1a": "Biotechnologische Erfindungen: menschlicher Körper, Gensequenzen", "2": "Ausschluss: öffentliche Ordnung, gute Sitten, Klonen, Keimbahn, Embryonen",
    "2a": "Ausschluss: Pflanzensorten, Tierrassen, im Wesentlichen biologische Verfahren; Begriffsbestimmungen",
    "3": "Neuheit, Stand der Technik, ältere Anmeldungen, Neuheitsschonfrist, zweite medizinische Indikation", "4": "Erfinderische Tätigkeit",
    "5": "Gewerbliche Anwendbarkeit", "6": "Recht auf das Patent; Erfinder, Miterfinder, Doppelerfindung", "7": "Anmelder gilt als Berechtigter; Einspruch des Verletzten",
    "8": "Widerrechtliche Entnahme: Anspruch auf Abtretung oder Übertragung (Vindikation)",
    "9": "Wirkung des Patents: Herstellen, Anbieten, Inverkehrbringen, Gebrauchen, Einführen, Besitzen; Verfahren, unmittelbares Verfahrenserzeugnis",
    "9a": "Schutz für biologisches Material und Verfahren mit biologischem Material", "9b": "Reichweite bei Vermehrung biologischen Materials",
    "9c": "Landwirteprivileg: Nachbau, Nutztiere; kein Schutz beim zufälligen Eintrag", "10": "Mittelbare Patentverletzung",
    "11": "Schranken: Privatbereich, Versuche, Bolar, Einzelzubereitung, Schiffe, Luftfahrzeuge, Züchtung", "12": "Vorbenutzungsrecht",
    "13": "Staatsbenutzungsanordnung (Bundesregierung, öffentliche Wohlfahrt, Sicherheit)", "14": "Schutzbereich: Patentansprüche, Beschreibung und Zeichnungen zur Auslegung",
    "15": "Übertragung, Vererbung, Lizenz; Sukzessionsschutz", "16": "Laufzeit: 20 Jahre ab Anmeldetag", "16a": "Ergänzende Schutzzertifikate",
    "17": "Jahresgebühren", "20": "Erlöschen: Verzicht, verspätete Erfinderbenennung, Nichtzahlung der Jahresgebühr",
    "21": "Widerrufsgründe: fehlende Patentfähigkeit, mangelnde Ausführbarkeit, widerrechtliche Entnahme, unzulässige Erweiterung",
    "22": "Nichtigkeitsgründe (Widerrufsgründe und Erweiterung des Schutzbereichs)", "23": "Lizenzbereitschaftserklärung: halbe Jahresgebühren, Vergütung",
    "24": "Zwangslizenz: öffentliches Interesse, Bemühen um Lizenz, abhängige Erfindung, Nichtausübung", "25": "Inlandsvertreter",
    "26": "Deutsches Patent- und Markenamt: Organisation, Prüfungsstellen, Patentabteilungen", "26a": "Weiterbildung, Aufgabenwahrnehmung durch Beamte",
    "27": "Prüfungsstellen und Patentabteilungen: Zuständigkeit und Besetzung", "28": "Datenverarbeitung im Verfahren", "29": "Verfahrenskostenhilfe (Verweis), Ausschließung und Ablehnung",
    "29a": "Elektronische Verfahren, Verordnungsermächtigung", "30": "Register: Eintragungen, Registerfiktion (Abs. 3), Lizenzbereitschaft, Umschreibung",
    "31": "Akteneinsicht", "31a": "Datenschutz", "32": "Veröffentlichungen: Patentschrift, Offenlegungsschrift, Patentblatt, Register",
    "33": "Entschädigungsanspruch aus der offengelegten Anmeldung", "34": "Anmeldung: Einheitlichkeit, Erfordernisse, Anmeldetag, Ausscheidung",
    "34a": "Angabe der geografischen Herkunft biologischen Materials", "35": "Anmeldetag, fremdsprachige Anmeldung, Übersetzungsfrist", "35a": "Fehlende Teile der Beschreibung, Zeichnungen",
    "36": "Zusammenfassung", "37": "Erfinderbenennung, Nachfrist", "38": "Änderungen der Anmeldung; keine Erweiterung des Gegenstands", "39": "Teilung der Anmeldung",
    "40": "Innere Priorität (zwölf Monate, deutsche Voranmeldung)", "41": "Ausländische Priorität (PVÜ), Prioritätserklärung, Nachweis", "42": "Offensichtlichkeitsprüfung, Mängelbeseitigung, Zurückweisung",
    "43": "Rechercheantrag", "44": "Prüfungsantrag (sieben Jahre), Antragsberechtigung", "45": "Prüfung: Zurückweisung bei Mängeln, Unterrichtung", "46": "Ermittlungen, Anhörung, Beweisaufnahme",
    "47": "Beschlüsse: Begründung, Zustellung, Rechtsmittelbelehrung", "48": "Zurückweisung der Anmeldung", "49": "Erteilung des Patents, Veröffentlichung im Patentblatt",
    "49a": "Ergänzendes Schutzzertifikat: Antrag, Prüfung, Erteilung", "50": "Geheimhaltung: Staatsgeheimnis, Anordnung", "51": "Anhörung im Geheimhaltungsverfahren",
    "52": "Ausländische Anmeldung geheimhaltungsbedürftiger Erfindungen", "53": "Aufhebung der Geheimhaltungsanordnung", "54": "Verwahrung geheimer Patente", "55": "Entschädigung bei Geheimhaltung",
    "56": "Zuständige oberste Bundesbehörde", "57": "Geheimhaltung: Mitteilungspflichten", "58": "Veröffentlichung der Erteilung, Wirkungseintritt, Rücknahmefiktion",
    "59": "Einspruch: neun Monate, Widerrufsgründe, Begründung, Beitritt", "60": "Teilung im Einspruchsverfahren, Verzicht, Beschränkung", "61": "Entscheidung über den Einspruch, Aufrechterhaltung, Antrag an das Patentgericht",
    "62": "Kostenentscheidung im Einspruchsverfahren", "63": "Erfindernennung, Berichtigung", "64": "Beschränkung und Widerruf auf Antrag des Patentinhabers",
    "65": "Bundespatentgericht: Sitz, Aufgaben, Besetzung", "66": "Beschwerde- und Nichtigkeitssenate, Besetzung", "67": "Zuständigkeit der Senate", "68": "Richter: Stellung, Ernennung",
    "69": "Öffentlichkeit der Verhandlung, Ausschluss", "70": "Präsidium, Geschäftsverteilung", "71": "Rechtsstellung der Richter, Vertretung", "72": "Wissenschaftliche Mitarbeiter, Geschäftsstelle",
    "73": "Beschwerde: Statthaftigkeit, Monatsfrist, Abhilfe", "74": "Beschwerdeberechtigte, Beteiligte", "75": "Aufschiebende Wirkung, Ausnahmen", "76": "Beschwerdeschrift, Erklärung des Präsidenten des DPMA",
    "77": "Beitritt des Präsidenten des DPMA", "78": "Mündliche Verhandlung", "79": "Entscheidung über die Beschwerde, Zurückverweisung", "80": "Kosten des Beschwerdeverfahrens",
    "81": "Nichtigkeitsklage: Klageberechtigung, Zwangslizenzklage, Klagesperre bei laufendem Einspruch, Klageschrift, Sicherheitsleistung",
    "82": "Zustellung der Klage, Widerspruchsfrist, Entscheidung ohne mündliche Verhandlung bei Säumnis", "83": "Qualifizierter Hinweis, Fristsetzung, Zurückweisung verspäteten Vorbringens",
    "84": "Urteil, Kostenentscheidung (§§ 91 ff. ZPO), Billigkeit", "85": "Einstweilige Verfügung im Zwangslizenzverfahren", "85a": "Beschleunigte Zwangslizenz bei Pandemien",
    "86": "Kostenfestsetzung, Vollstreckung", "87": "Amtsermittlung, Aufklärung, Beweisaufnahme", "88": "Rechtshilfe, Amtshilfe", "89": "Ladung, Verhandlung ohne Beteiligte",
    "90": "Verhandlungsleitung, Fragerecht", "91": "Sitzungspolizei (Verweis auf GVG)", "92": "Protokoll", "93": "Urteil und Beschlüsse: Begründung, Zustellung, Verkündung",
    "94": "Ausfertigung, Zustellung von Entscheidungen", "95": "Berichtigung von Urteilen und Beschlüssen", "96": "Berichtigung des Tatbestands",
    "97": "Vertretung vor dem Patentgericht, Bevollmächtigte", "98": "Zustellungen", "99": "Anwendung der ZPO, Akteneinsicht, Rechtsmittel",
    "100": "Rechtsbeschwerde: Zulassung, absolute Rechtsbeschwerdegründe", "101": "Rechtsbeschwerdeberechtigte, Anschlussrechtsbeschwerde", "102": "Frist, Form, Begründung der Rechtsbeschwerde",
    "103": "Prüfung der Zulässigkeit, Verwerfung", "104": "Mündliche Verhandlung vor dem BGH", "105": "Anwendung der Vorschriften über die Revision", "106": "Vertretung, Zustellung", "107": "Entscheidung und Zurückverweisung",
    "108": "Entscheidungsgründe, Bindung des Patentgerichts", "109": "Kosten der Rechtsbeschwerde", "110": "Berufung gegen Nichtigkeitsurteile: Monatsfrist, Begründung",
    "111": "Berufungsbegründung: Anträge, Berufungsgründe", "112": "Anschlussberufung", "113": "Berufungssenat, Vorbereitung", "114": "Zurückweisung der Berufung", "115": "Vorbereitung der mündlichen Verhandlung",
    "116": "Prüfungsumfang, Bindung an Anträge, neue Verteidigung", "117": "Neue Angriffs- und Verteidigungsmittel (Präklusion)", "118": "Urteil des BGH, Zurückverweisung", "119": "Berufung: Verweis auf ZPO",
    "120": "Verfahren vor dem BGH bei Beschwerden", "121": "Streitwert im Nichtigkeitsverfahren, Kostenentscheidung", "122": "Gemeinsame Vorschriften: Vertretung vor dem BGH",
    "122a": "Erstattung von Patentanwaltskosten", "123": "Wiedereinsetzung in den vorigen Stand", "123a": "Weiterbehandlung der Anmeldung", "124": "Wahrheitspflicht der Beteiligten",
    "125": "Zeugen und Sachverständige, Beweisaufnahme", "125a": "Elektronische Dokumente, elektronische Akte", "126": "Amtssprache Deutsch, Übersetzungen", "127": "Zustellungen (VwZG), Zustellung an Vertreter",
    "128": "Rechtshilfe der Gerichte für das DPMA", "128a": "Videoverhandlung", "128b": "Elektronische Akteneinsicht", "129": "Verfahrenskostenhilfe: Anwendung der ZPO",
    "130": "Verfahrenskostenhilfe im Erteilungsverfahren, hinreichende Erfolgsaussicht", "131": "Verfahrenskostenhilfe im Einspruchsverfahren", "132": "Verfahrenskostenhilfe im Nichtigkeits- und Zwangslizenzverfahren",
    "133": "Beiordnung eines Vertreters", "134": "Antragsverfahren, Entscheidung über Verfahrenskostenhilfe", "135": "Beiordnung: Vergütung, Ausländer", "136": "Anwendung der ZPO-Vorschriften über Prozesskostenhilfe",
    "137": "Verfahrenskostenhilfe: Aufhebung, Rückzahlung", "138": "Beschwerde in Verfahrenskostenhilfesachen", "139": "Unterlassung, Schadensersatz, Verhältnismäßigkeit, Verletzergewinn, Lizenzanalogie",
    "140": "Verjährung (Verweis auf BGB), Restschadensersatz", "140a": "Vernichtung, Rückruf, Entfernen aus den Vertriebswegen", "140b": "Auskunft und Drittauskunft",
    "140c": "Vorlage und Besichtigung", "140d": "Sicherung von Schadensersatzansprüchen", "140e": "Urteilsbekanntmachung", "141": "Verjährung der Ansprüche, Herausgabe des Erlangten",
    "141a": "Verhältnis zur Zollverordnung", "142": "Strafvorschriften", "142a": "Beschlagnahme durch die Zollbehörden", "142b": "Zollverordnung: Verfahren, Kosten", "143": "Patentstreitkammern, Konzentration, Patentanwaltskosten",
    "144": "Streitwertbegünstigung", "145": "Klagekonzentration: gleichartige Handlungen", "145a": "Gebrauchsmuster, Abzweigung (Verweis)", "146": "Patentberühmung: Auskunft",
    "147": "Übergangsvorschriften",
}

# ------------------------------------------------------------------ Hinweise (Lern- und Klausurhinweis je Vorschrift)
HINWEISE_PATG = {
    "1": "Zentralnorm der Patentfähigkeit: Erfindung auf allen Gebieten der Technik (Abs. 1), Negativkatalog (Abs. 3) nur „als solche“ (Abs. 4). Prüfungsreihenfolge: Technizität, Ausschluss, Neuheit (§ 3), erfinderische Tätigkeit (§ 4), gewerbliche Anwendbarkeit (§ 5). Bei Programmen: technischer Beitrag zur Lösung eines technischen Problems (BGH Webseitenanzeige, Dynamische Dokumentengenerierung).",
    "1a": "Umsetzung der Biopatentrichtlinie 98/44/EG: Der menschliche Körper und die bloße Entdeckung eines Gens sind nicht patentierbar (Abs. 1); isolierte Sequenzen mit angegebener Funktion schon (Abs. 2, 3); Zweckbindung bei menschlichen Gensequenzen (Abs. 4).",
    "2": "Ordre public und gute Sitten; Verstoß liegt nicht schon in einem Verbot durch Gesetz (Abs. 1 S. 2). Abs. 2 nennt die absoluten Ausschlüsse (Klonen, Keimbahn, Embryonen, Tierleiden).",
    "2a": "Pflanzensorten und Tierrassen sind ausgeschlossen (Sortenschutz), nicht aber Pflanzen und Tiere, wenn die Ausführung technisch nicht auf eine Sorte beschränkt ist (Abs. 2 Nr. 1). „Im Wesentlichen biologische Verfahren“ sind Kreuzung und Selektion.",
    "3": "Absoluter, weltweiter Neuheitsbegriff (Abs. 1). Ältere, nachveröffentlichte Anmeldungen zählen nur für die Neuheit, nicht für § 4 (Abs. 2). Neuheitsschonfrist sechs Monate nur bei offensichtlichem Missbrauch oder amtlicher Ausstellung (Abs. 5), keine allgemeine Schonfrist. Zweite medizinische Indikation als zweckgebundener Stoffschutz (Abs. 4). Offenbarungsbegriff: BGH Olanzapin.",
    "4": "Naheliegen aus der Sicht des Fachmanns am Anmeldetag; Aufgabe-Lösungs-Ansatz ist Hilfsmittel, nicht Gesetz. Der Fachmann braucht eine Veranlassung, den Stand der Technik weiterzuentwickeln (BGH Fischbissanzeiger, Kinderbett); allgemeines Fachwissen allein genügt nicht (BGH Airbag-Auslösesteuerung).",
    "5": "Gewerbliche Anwendbarkeit fehlt fast nie; praktisch relevant nur bei Verfahren zur chirurgischen oder therapeutischen Behandlung (Abs. 2 Nr. 1 i.V.m. § 2a Abs. 1 Nr. 2: seit 2005 Patentierungsausschluss, nicht mehr fehlende gewerbliche Anwendbarkeit).",
    "6": "Erfinderprinzip: Das Recht auf das Patent steht dem Erfinder zu, Ausnahme § 7 ArbnErfG (Inanspruchnahme durch den Arbeitgeber). Bei Doppelerfindung gilt das Prioritätsprinzip (S. 3).",
    "7": "Der Anmelder gilt im Verfahren vor dem DPMA als berechtigt (formelle Berechtigung); die materielle Berechtigung wird nur im Einspruch (§ 21 Abs. 1 Nr. 3) oder mit der Vindikationsklage (§ 8) geklärt. Abs. 2: zwei Jahre nach Erteilung ist der Einspruch wegen widerrechtlicher Entnahme ausgeschlossen, es sei denn, der Inhaber war bösgläubig.",
    "8": "Vindikation: Der Verletzte kann Abtretung der Anmeldung oder Übertragung des Patents verlangen; Frist zwei Jahre nach Erteilung, außer bei Bösgläubigkeit (S. 3, 4). Alternativ Einspruch (§ 21 Abs. 1 Nr. 3) und danach Nachanmeldung mit Priorität (§ 7 Abs. 2).",
    "9": "Erzeugnisansprüche (S. 2 Nr. 1), Verfahrensansprüche (Nr. 2) und der Schutz des unmittelbaren Verfahrenserzeugnisses (Nr. 3). Ausschließlichkeitsrecht mit Verbotswirkung; Verletzungshandlungen sind abschließend aufgezählt. Erschöpfung ist ungeschrieben (BGH Palettenbehälter II: bestimmungsgemäßer Gebrauch vs. Neuherstellung).",
    "10": "Mittelbare Verletzung: Anbieten oder Liefern von Mitteln, die sich auf ein wesentliches Element der Erfindung beziehen, an Nichtberechtigte, wenn der Anbieter weiß oder es offensichtlich ist, dass die Mittel zur Benutzung bestimmt sind (Abs. 1). Doppelter Inlandsbezug. Allgemein im Handel erhältliche Erzeugnisse nur bei bewusster Veranlassung (Abs. 2). BGH Flügelradzähler.",
    "11": "Schranken abschließend: Privatbereich, Versuche (auch klinische Versuche zur Gewinnung von Erkenntnissen über den Erfindungsgegenstand: BGH Klinische Versuche I und II), Bolar-Ausnahme (Nr. 2b), Einzelzubereitung in Apotheken, Schiffe und Luftfahrzeuge (PVÜ Art. 5ter).",
    "12": "Vorbenutzungsrecht: Erfindungsbesitz und Benutzung oder Veranstaltungen im Inland zum Prioritätstag; nur mit dem Betrieb übertragbar (Abs. 1 S. 3); kein Vorbenutzungsrecht bei widerrechtlicher Entnahme vom Anmelder (Abs. 1 S. 2).",
    "13": "Benutzungsanordnung im Interesse der öffentlichen Wohlfahrt oder Sicherheit; Entschädigung; praktisch bedeutungslos, aber Klausurklassiker neben der Zwangslizenz (§ 24).",
    "14": "Schutzbereich wird durch die Patentansprüche bestimmt; Beschreibung und Zeichnungen sind heranzuziehen. Parallel zu Art. 69 EPÜ und dem Auslegungsprotokoll. Äquivalenz nach den drei Schneidmesser-Fragen (Gleichwirkung, Auffindbarkeit, Gleichwertigkeit); Auswahlentscheidung: BGH Okklusionsvorrichtung, Pemetrexed.",
    "15": "Anmeldung und Patent sind übertragbar und lizenzierbar. Ausschließliche und einfache Lizenz; Sukzessionsschutz (Abs. 3): Rechtsübergang lässt Lizenzen unberührt. Der ausschließliche Lizenznehmer ist aus eigenem Recht klagebefugt, der einfache nur mit Ermächtigung.",
    "16": "Laufzeit 20 Jahre ab dem Tag nach der Anmeldung; Verlängerung nur über ergänzende Schutzzertifikate (§ 16a). Wirkungen der Anmeldung: Entschädigung ab Offenlegung (§ 33), volle Wirkung ab Erteilungsveröffentlichung (§ 58).",
    "16a": "Ergänzende Schutzzertifikate nach den Verordnungen (EG) Nr. 469/2009 (Arzneimittel) und (EG) Nr. 1610/96 (Pflanzenschutzmittel): bis zu fünf Jahre (plus sechs Monate pädiatrisch); Verfahren § 49a, Gebühren Nr. 311 500 ff. und 312 210 ff. der Anlage zum PatKostG.",
    "17": "Jahresgebühren ab dem dritten Jahr, gerechnet vom Anmeldetag; Fälligkeit am letzten Tag des Monats, der dem Anmeldemonat entspricht (§ 3 Abs. 2 PatKostG), Zahlungsfrist und Verspätungszuschlag nach § 7 PatKostG; Nichtzahlung führt zum Erlöschen (§ 20 Abs. 1 Nr. 3).",
    "20": "Erlöschen durch Verzicht (Nr. 1), fehlende Erfinderbenennung nach Fristsetzung (Nr. 2) oder Nichtzahlung der Jahresgebühr mit Zuschlag (Nr. 3); dann Wiedereinsetzung (§ 123) binnen zwei Monaten nach Wegfall des Hindernisses, spätestens ein Jahr nach Fristablauf.",
    "21": "Widerrufsgründe des Einspruchs: fehlende Patentfähigkeit (Nr. 1: §§ 1 bis 5), mangelnde Ausführbarkeit (Nr. 2), widerrechtliche Entnahme (Nr. 3, nur der Verletzte), unzulässige Erweiterung (Nr. 4). Teilwiderruf durch Beschränkung (Abs. 2). Der Katalog ist abschließend: mangelnde Klarheit ist kein Widerrufsgrund (BGH Fugenband zur Nichtigkeit).",
    "22": "Nichtigkeitsgründe = Widerrufsgründe des § 21 plus Erweiterung des Schutzbereichs (Abs. 1). Für europäische Patente gilt Art. II § 6 IntPatÜG mit denselben Gründen aus Art. 138 EPÜ. Verteidigung mit beschränkten Ansprüchen (Abs. 2 i.V.m. § 21 Abs. 2).",
    "23": "Lizenzbereitschaft: Erklärung gegenüber dem DPMA, Jahresgebühren halbieren sich (Abs. 1), jeder darf gegen angemessene Vergütung benutzen (Abs. 3), Vergütung setzt die Patentabteilung fest (Abs. 4). Rücknahme nur, solange keine Benutzungsanzeige (Abs. 7). Ausgeschlossen bei eingetragener ausschließlicher Lizenz (Abs. 2).",
    "24": "Zwangslizenz durch das Patentgericht (§ 81): erfolgloses Bemühen um eine Lizenz zu angemessenen Bedingungen und öffentliches Interesse (Abs. 1); abhängige Erfindung mit wichtigem technischen Fortschritt (Abs. 2); Nichtausübung (Abs. 5). Einstweilige Verfügung nach § 85. BGH Raltegravir, Alirocumab: Bemühen und öffentliches Interesse im Einzelfall.",
    "25": "Wer im Inland weder Wohnsitz noch Sitz noch Niederlassung hat, kann nur mit Inlandsvertreter (Patent- oder Rechtsanwalt) am Verfahren teilnehmen; Verstoß führt zur Zurückweisung nach Fristsetzung.",
    "30": "Register mit Legitimationswirkung: Nach Abs. 3 S. 2 gilt der Eingetragene als Berechtigter im Verfahren vor dem DPMA und dem Patentgericht (Registerfiktion); Umschreibung nur auf Antrag mit Nachweis. Lizenzbereitschaft, ausschließliche Lizenzen und Erlöschen werden vermerkt.",
    "33": "Entschädigungsanspruch aus der offengelegten Anmeldung gegen den, der den Gegenstand benutzt, obwohl er wusste oder wissen musste, dass es sich um eine Patentanmeldung handelt; kein Unterlassungsanspruch vor Erteilung. Für europäische Anmeldungen: Art. II § 1 IntPatÜG.",
    "34": "Anmeldeerfordernisse: Antrag, Ansprüche, Beschreibung, Zeichnungen, Zusammenfassung (Abs. 3), Einheitlichkeit (Abs. 5), Ausführbarkeit (Abs. 4); Ausscheidung bei Uneinheitlichkeit (Abs. 5 i.V.m. § 39). Form und Inhalt regelt die PatV (Abs. 6). Anmeldetag nach § 35.",
    "35": "Anmeldetag: Eingang von Erteilungsantrag, Angaben zum Anmelder und einer Beschreibung (auch fremdsprachig, auch Verweis auf frühere Anmeldung). Übersetzung binnen drei (englisch/französisch: zwölf) Monaten, sonst gilt die Anmeldung als zurückgenommen (Abs. 2). Zeichnungen: § 35a.",
    "37": "Erfinderbenennung binnen 15 Monaten ab Anmeldetag bzw. Prioritätstag; Nachfrist gegen Gebühr; ohne Benennung keine Erteilung (§ 20 Abs. 1 Nr. 2 für spätere Fälle). Erfinderpersönlichkeitsrecht: Nennung in Patentschrift und Register (§ 63).",
    "38": "Änderungen bis zum Prüfungsantrag frei, danach nur zur Mängelbeseitigung; nie über den Inhalt der ursprünglichen Anmeldung hinaus (S. 1 Hs. 2). Unzulässige Erweiterung = Widerrufs- und Nichtigkeitsgrund (§ 21 Abs. 1 Nr. 4); Maßstab: unmittelbar und eindeutig offenbart (BGH Hubgliedertor, Winkelmesseinrichtung).",
    "39": "Teilung jederzeit bis zur Erteilung; die Teilanmeldung behält Anmeldetag und Priorität; für die Teilanmeldung sind die Gebühren nachzuzahlen (Abs. 2). Teilungserklärung ist unwiderruflich (Abs. 3). Abgrenzung: Ausscheidung (§ 34 Abs. 5) und Teilung im Einspruch (§ 60).",
    "40": "Innere Priorität: binnen zwölf Monaten Nachanmeldung derselben Erfindung mit dem Zeitrang der ersten deutschen Anmeldung; die frühere Anmeldung gilt mit der Prioritätserklärung als zurückgenommen (Abs. 5). Für Gebrauchsmuster gilt § 40 über § 6 GebrMG.",
    "41": "Ausländische Priorität nach PVÜ: Erklärung mit Zeit, Land und Aktenzeichen binnen 16 Monaten ab Prioritätstag, Prioritätsbeleg auf Aufforderung; Versäumung führt zum Verlust des Prioritätsanspruchs (Abs. 1 S. 4). Wiedereinsetzung in die Prioritätsfrist selbst ist ausgeschlossen (§ 123 Abs. 1 S. 2).",
    "42": "Offensichtlichkeitsprüfung: formale Mängel (§ 34 Abs. 3 bis 5, § 36, § 37) und offensichtlich fehlende Patentfähigkeit (§§ 1 bis 5); Fristsetzung, dann Zurückweisung nach § 48. Unabhängig vom Prüfungsantrag.",
    "43": "Rechercheantrag (Gebühr Nr. 311 200: 300 EUR): Ermittlung des Stands der Technik ohne Prüfung; von jedermann stellbar; Gebühr wird auf die spätere Prüfungsgebühr angerechnet (Nr. 311 300).",
    "44": "Prüfungsantrag binnen sieben Jahren ab Anmeldetag, von jedem Dritten stellbar (Abs. 2); ohne Antrag gilt die Anmeldung als zurückgenommen (Abs. 4). Gebühr Nr. 311 400 (350 EUR, nach Recherche 150 EUR); Zahlungsfrist drei Monate nach Fälligkeit (§ 6 PatKostG).",
    "45": "Prüfungsverfahren: Beanstandung, Bescheid mit Fristsetzung, Gelegenheit zur Äußerung; die Prüfungsstelle darf nur mit Gründen zurückweisen, zu denen der Anmelder gehört wurde (§ 48 i.V.m. § 42 Abs. 3, rechtliches Gehör).",
    "48": "Zurückweisung der Anmeldung durch Beschluss; Rechtsbehelf: Beschwerde binnen eines Monats (§ 73) oder Weiterbehandlung nach § 123a bei Fristversäumung. Teilzurückweisung bei Haupt- und Hilfsanträgen: BPatG Teilbeschluss.",
    "49": "Erteilungsbeschluss, wenn die Anmeldung den Erfordernissen genügt und die Erfindung patentfähig ist; Veröffentlichung im Patentblatt (§ 58) mit Beginn der Einspruchsfrist und der vollen Wirkung.",
    "58": "Mit der Veröffentlichung der Erteilung treten die Wirkungen des Patents ein (Abs. 1 S. 3) und beginnt die Einspruchsfrist (§ 59). Wird auf das Patent verzichtet oder erlischt es, bleibt die Anmeldung bestehen (Abs. 2). Rücknahmefiktion bei Nichtzahlung der Erteilungsgebühr entfällt seit 2004 (Gebührenfreiheit der Erteilung).",
    "59": "Einspruch: neun Monate nach Veröffentlichung der Erteilung, schriftlich, begründet (Tatsachen im Einzelnen), nur auf Widerrufsgründe des § 21 gestützt; jedermann (bei Nr. 3 nur der Verletzte); Gebühr 200 EUR (Nr. 313 600). Beitritt des Verletzungsbeklagten (Abs. 2). Zuständigkeit Patentabteilung; Verfahren vor dem Patentgericht nach § 61 Abs. 2 nur noch für Altfälle. BGH Ratschenschlüssel (Beitritt bei einstweiliger Verfügung).",
    "60": "Im Einspruchsverfahren kann das Patent geteilt werden (Abs. 1); die Teilung ist unwiderruflich. BGH Sammelhefter: Teilungserklärung braucht keinen gegenständlich bestimmten Teil.",
    "61": "Entscheidung der Patentabteilung: Widerruf, Aufrechterhaltung (auch beschränkt); Abs. 2 (Antrag auf gerichtliche Entscheidung) gilt für Einsprüche bis 2006 und ist als § 61 Abs. 2 n.F. seit 2020 für Sonderfälle wieder eingeführt (Gebühr Nr. 400 000). Beschwerde nach § 73 zum Technischen Beschwerdesenat.",
    "62": "Kosten im Einspruchsverfahren trägt jeder selbst; abweichende Kostenentscheidung nur aus Billigkeit (etwa bei unbegründetem Einspruch mit offensichtlich aussichtsloser Begründung).",
    "63": "Erfindernennung in Patentschrift, Register und Veröffentlichungen; Berichtigung auf Antrag mit Zustimmung; Verzicht des Erfinders auf Nennung ist zulässig (Abs. 1 S. 3), nicht aber ein Vorausverzicht auf das Recht selbst.",
    "64": "Beschränkung oder Widerruf auf Antrag des Patentinhabers (Zentrales Beschränkungsverfahren, Gebühr Nr. 313 700); Wirkung ex tunc (Abs. 3 i.V.m. § 21 Abs. 3). Praktisch wichtig zur Sicherung des Rechtsbestands vor einer Nichtigkeitsklage.",
    "65": "Bundespatentgericht in München: Beschwerden gegen Beschlüsse des DPMA, Nichtigkeits- und Zwangslizenzklagen (§ 81). Senate: Technische und Juristische Beschwerdesenate, Nichtigkeitssenate (§ 66), Marken- und Gebrauchsmuster-Beschwerdesenate.",
    "66": "Besetzung: Beschwerdesenate in Patentsachen mit einem rechtskundigen und zwei technischen Richtern (Abs. 1 Nr. 1), Nichtigkeitssenate mit zwei rechtskundigen und drei technischen Richtern (Abs. 1 Nr. 2), Juristischer Beschwerdesenat mit drei rechtskundigen Richtern.",
    "73": "Beschwerde gegen Beschlüsse der Prüfungsstellen und Patentabteilungen; Frist ein Monat ab Zustellung; Gebühr Nr. 401 100 (500 EUR), 401 300 (200 EUR); Abhilfe binnen eines Monats (Abs. 3), sonst Vorlage. Fristversäumung: Wiedereinsetzung (§ 123). Gebührenzahlung binnen der Beschwerdefrist (§ 6 Abs. 1 S. 1 PatKostG), sonst gilt die Beschwerde als nicht eingelegt (§ 6 Abs. 2 PatKostG).",
    "74": "Beschwerdeberechtigt sind die Beteiligten des Verfahrens vor dem DPMA; im Einspruchsverfahren auch der Einsprechende; Beschwer erforderlich.",
    "75": "Beschwerde hat aufschiebende Wirkung (Abs. 1), nicht gegen Beschlüsse, die eine Prüfung nach § 42 oder die Zurückweisung der Anmeldung betreffen, soweit Sicherheitsleistung angeordnet ist; Ausnahme Geheimhaltung.",
    "79": "Das Patentgericht entscheidet durch Beschluss in der Sache selbst oder verweist zurück (Abs. 3), etwa bei fehlender Sachaufklärung oder Verletzung des rechtlichen Gehörs. Im Einspruchsbeschwerdeverfahren keine neuen Widerrufsgründe von Amts wegen (BGH Ventileinrichtung).",
    "80": "Kosten des Beschwerdeverfahrens: grundsätzlich jeder Beteiligte selbst; Auferlegung nach Billigkeit (Abs. 1); Rückzahlung der Beschwerdegebühr (Abs. 3), etwa bei Verfahrensfehlern des DPMA. Streitwertfestsetzung (Abs. 2).",
    "81": "Nichtigkeitsklage vor dem BPatG (Abs. 1): Popularklage, keine Klagebefugnis nötig (außer Nr. 3: nur der Verletzte); während eines laufenden Einspruchs unzulässig (Abs. 2). Ausländische Kläger: Sicherheitsleistung (Abs. 6). Verletzungs- und Nichtigkeitsverfahren sind getrennt (Trennungsprinzip); Aussetzung des Verletzungsprozesses nach § 148 ZPO (BGH Klimaschrank, Adalimumab). Rechtsmissbrauch: BGH Benutzerauthentifizierung.",
    "82": "Widerspruch des Beklagten binnen eines Monats nach Zustellung (verlängerbar); ohne Widerspruch entscheidet das Gericht ohne mündliche Verhandlung und legt das Klagevorbringen als zugestanden zugrunde (Abs. 2). Vertretung durch Patentanwalt oder Rechtsanwalt nicht zwingend, Kostenerstattung nach § 84 Abs. 2.",
    "83": "Qualifizierter Hinweis (Abs. 1) mit Fristsetzung (Abs. 2) und Präklusion verspäteten Vorbringens (Abs. 4): seit 2009 Herzstück des Nichtigkeitsverfahrens; das Berufungsgericht ist an die Präklusion gebunden (§ 117). BGH Walzstraße: Hinweis, Fristsetzung, Verspätung.",
    "84": "Urteil; Kosten nach §§ 91 ff. ZPO (Abs. 2), Billigkeitskorrektur nur bei Verteidigung mit erst im Verfahren beschränkten Ansprüchen. Bei Nichtigerklärung: Wirkung ex tunc und inter omnes (§ 22 Abs. 2 i.V.m. § 21 Abs. 3).",
    "85": "Einstweilige Verfügung im Zwangslizenzverfahren bei Glaubhaftmachung der Voraussetzungen des § 24 und Dringlichkeit im öffentlichen Interesse (BGH Raltegravir: Isentress); Gebühr Nr. 402 300.",
    "99": "Anwendung der ZPO im Verfahren vor dem Patentgericht (Abs. 1), Akteneinsicht (Abs. 3), keine Anfechtung von Zwischenentscheidungen (Abs. 2). Grundlage für Nebenintervention (§ 66 ZPO: BGH Carvedilol, Pemetrexed II) und Restitution.",
    "100": "Rechtsbeschwerde zum BGH nur bei Zulassung durch das Patentgericht (Abs. 1, 2) oder bei absoluten Rechtsbeschwerdegründen (Abs. 3: Besetzung, Ausschließung, rechtliches Gehör, Vertretung, Öffentlichkeit, fehlende Gründe). Frist ein Monat (§ 102); Anwaltszwang vor dem BGH (§ 102 Abs. 5).",
    "110": "Berufung gegen Urteile der Nichtigkeitssenate zum BGH (X. Zivilsenat) binnen eines Monats, Begründung binnen drei Monaten; kein zweiter Tatsachenrichter im klassischen Sinn: neue Angriffs- und Verteidigungsmittel nur nach § 117 (Präklusion).",
    "116": "Prüfungsumfang der Berufung: Anträge und Berufungsgründe; hilfsweise Verteidigung mit geänderten Ansprüchen nur bei Sachdienlichkeit (Abs. 2), etwa wenn das Patentgericht seinen Hinweis erst in der Verhandlung geändert hat (BGH Fahrzeugscheibe II).",
    "117": "Neue Angriffs- und Verteidigungsmittel nur unter den Voraussetzungen des § 531 Abs. 2 ZPO; nach § 83 Abs. 4 zurückgewiesenes Vorbringen bleibt ausgeschlossen (§ 117 S. 2).",
    "121": "Streitwert des Nichtigkeitsverfahrens: gemeiner Wert des Patents bei Klageerhebung plus Schadensersatz (Regel: Verletzungsstreitwert plus 25 %); Gebühr 4,5 Gebühren nach Nr. 402 100 der Anlage zum PatKostG; Streitwertbegünstigung § 144 gilt entsprechend (Abs. 2).",
    "123": "Wiedereinsetzung: unverschuldete Versäumung einer Frist mit Rechtsnachteil; Antrag binnen zwei Monaten nach Wegfall des Hindernisses mit Begründung und Nachholung der Handlung, spätestens ein Jahr nach Fristablauf (Abs. 2). Ausgeschlossen: Einspruchsfrist, Prioritätsfrist, Nachfrist der Erfinderbenennung (Abs. 1 S. 2). Verschulden des Vertreters wird zugerechnet (§ 85 Abs. 2 ZPO). Nach Wiedereinsetzung Zwischenbenutzungsrecht (Abs. 5).",
    "123a": "Weiterbehandlung: Bei Zurückweisung der Anmeldung wegen versäumter Frist genügt Antrag mit Nachholung der Handlung und Gebühr (100 EUR, Nr. 313 000) binnen eines Monats nach Zustellung; kein Verschuldensmaßstab. Nur für die Anmeldung, nicht für Einspruch oder Beschwerde. BPatG Weiterbehandlung II: Nachholung innerhalb der Monatsfrist.",
    "126": "Amtssprache Deutsch; fremdsprachige Schriftstücke sind unbeachtlich, wenn keine Übersetzung nachgereicht wird; § 35 Abs. 2 für die Anmeldung, PatV § 14 für Belege.",
    "139": "Unterlassung (Abs. 1) bei Wiederholungs- oder Erstbegehungsgefahr, verschuldensunabhängig; Verhältnismäßigkeitseinwand seit 2021 (Abs. 1 S. 3, 4) mit Ausgleich in Geld. Schadensersatz bei Verschulden (Abs. 2) nach Wahl: konkreter Schaden, Verletzergewinn, Lizenzanalogie. Verjährung nach § 141. Klagebefugnis des Lizenznehmers: § 15 Abs. 2.",
    "140a": "Vernichtung, Rückruf und endgültiges Entfernen aus den Vertriebswegen; Ausschluss bei Unverhältnismäßigkeit (Abs. 4). Umsetzung von Art. 10 DurchsetzungsRL.",
    "140b": "Auskunft über Herkunft und Vertriebsweg (Abs. 1), Drittauskunft bei offensichtlicher Verletzung (Abs. 2), Umfang (Abs. 3), Unverhältnismäßigkeit (Abs. 4), einstweilige Verfügung (Abs. 7). Daneben der unselbständige Rechnungslegungsanspruch aus § 242 BGB zur Bezifferung des Schadensersatzes.",
    "140c": "Vorlage und Besichtigung bei hinreichender Wahrscheinlichkeit der Verletzung (Abs. 1), auch im Wege der einstweiligen Verfügung (Abs. 3) mit Geheimnisschutz (Abs. 1 S. 3); Düsseldorfer Praxis: Besichtigung durch Sachverständigen mit Verschwiegenheitspflicht. Umsetzung von Art. 6, 7 DurchsetzungsRL; BGH Faxkarte (§ 809 BGB) als Vorläufer.",
    "140e": "Urteilsbekanntmachung auf Antrag der obsiegenden Partei bei berechtigtem Interesse; Umsetzung von Art. 15 DurchsetzungsRL.",
    "141": "Verjährung der Verletzungsansprüche nach den §§ 194 ff. BGB (drei Jahre ab Kenntnis, zehn Jahre absolut); danach Restschadensersatz nach Bereicherungsrecht (S. 2 i.V.m. § 852 BGB).",
    "142": "Strafbarkeit der vorsätzlichen Patentverletzung (Abs. 1), gewerbsmäßig bis fünf Jahre (Abs. 2); Antragsdelikt (Abs. 4); Einziehung (Abs. 5); Bekanntmachung der Verurteilung (Abs. 6).",
    "143": "Patentstreitsachen vor den Landgerichten ohne Rücksicht auf den Streitwert (Abs. 1), Konzentration durch Landesverordnung (Abs. 2: Düsseldorf, Mannheim, München u.a.); Erstattung der Patentanwaltskosten (Abs. 3) neben dem Rechtsanwalt.",
    "144": "Streitwertbegünstigung: Auf Antrag zahlt eine Partei, deren wirtschaftliche Lage durch die vollen Kosten erheblich gefährdet würde, Gebühren nach einem angepassten Teilstreitwert; Antrag vor Verhandlung zur Hauptsache; gilt entsprechend im Nichtigkeitsverfahren (§ 121 Abs. 2).",
    "145": "Klagekonzentration: Wer wegen Verletzung eines Patents Klage erhoben hat, kann wegen derselben oder gleichartiger Handlung aus einem anderen Patent nur klagen, wenn er ohne Verschulden nicht schon in der ersten Klage darauf stützen konnte. BGH Raffvorhang: gleichartig nur bei zusätzlichen oder abgewandelten Merkmalen.",
    "146": "Patentberühmung: Wer Gegenstände mit einer Bezeichnung versieht, die den Eindruck eines Patentschutzes erweckt, muss jedem mit berechtigtem Interesse Auskunft über das Patent geben; keine Patentberühmung ist der Hinweis „Patent angemeldet“ bei laufender Anmeldung.",
}

HINWEISE_PATV = {
    "1": "Die PatV regelt Form und Inhalt der Anmeldung (§ 34 Abs. 6 PatG) und der sonstigen Eingaben; sie ergänzt die DPMAV (allgemeine Verfahrensfragen, Vertreter, Fristen) und die ERVDPMAV (elektronischer Rechtsverkehr).",
    "3": "Anmeldung und Zusammenfassung sind schriftlich einzureichen; elektronisch nach der ERVDPMAV. Anlage 2 enthält die Standards für Zeichnungen (§ 12).",
    "4": "Der Erteilungsantrag: amtliches Formblatt, Bezeichnung der Erfindung, Angaben zum Anmelder, Antrag auf Prüfung oder Recherche, Prioritätsangaben; der Antrag muss den Willen zur Patenterteilung erkennen lassen (Anmeldetag nach § 35 Abs. 1 PatG).",
    "5": "Anmeldungsunterlagen: Ansprüche (§ 9), Beschreibung (§ 10), Zeichnungen (§ 12), Zusammenfassung (§ 13), Sequenzprotokoll (§ 11); Reihenfolge und Blattzählung nach § 6.",
    "6": "Formerfordernisse: DIN A4, Ränder, einseitig, Zeilenabstand; keine Änderungen von Hand; Blätter fortlaufend nummerieren. Formmängel werden im Offensichtlichkeitsverfahren (§ 42 PatG) beanstandet.",
    "7": "Erfinderbenennung nach § 37 PatG: gesonderte Erklärung mit Name und Anschrift jedes Erfinders und Angabe, wie das Recht auf den Anmelder übergegangen ist (etwa Inanspruchnahme nach § 6 ArbnErfG).",
    "8": "Nichtnennung des Erfinders auf dessen Antrag (§ 63 Abs. 1 S. 3 PatG): Erklärung des Erfinders, jederzeit widerruflich.",
    "9": "Patentansprüche: Was unter Schutz gestellt werden soll; ein- oder zweiteilige Fassung (Oberbegriff und kennzeichnender Teil, Abs. 1), Bezugszeichen, keine Verweisung auf die Beschreibung „wie beschrieben“ (Abs. 5), nebengeordnete und Unteransprüche (Abs. 3, 4). Der Anspruch bestimmt den Schutzbereich (§ 14 PatG).",
    "10": "Beschreibung: technisches Gebiet, Stand der Technik, Aufgabe (Problem), Lösung, Vorteile, Ausführungsbeispiele, gewerbliche Anwendbarkeit (Abs. 2); die Aufgabe darf nicht mit Lösungsmerkmalen formuliert werden. Unzulässiges Vorbringen (Abs. 4: Herabsetzung Dritter) wird gestrichen.",
    "11": "Nukleotid- und Aminosäuresequenzen sind in einem Sequenzprotokoll nach dem WIPO-Standard ST.26 darzustellen (§§ 11a, 11b für Einreichung und Nachreichung).",
    "12": "Zeichnungen: Standards in Anlage 2 (Ränder, Linien, Bezugszeichen, keine Beschriftung außer Stichworten); Fotos nur, wenn Zeichnungen unmöglich sind.",
    "13": "Zusammenfassung (§ 36 PatG): Titel, Kurzfassung des Offenbarten mit Aufgabe, Lösung, Verwendung, bis zu 1 500 Zeichen, eine Figur; dient nur der technischen Information, nicht der Auslegung (§ 36 Abs. 2 PatG).",
    "14": "Fremdsprachige Dokumente: deutsche Übersetzung, beglaubigt durch Rechts- oder Patentanwalt oder öffentlich beglaubigt (§ 17), auf Anforderung; Anmeldungsübersetzung nach § 35 Abs. 2 PatG.",
    "15": "Nachgereichte Unterlagen (§ 35a PatG, fehlende Teile): Einreichung binnen der Fristen der PatG; Bezugnahme auf die Prioritätsanmeldung möglich, wenn die Teile darin vollständig enthalten sind.",
    "16": "Modelle und Proben nur auf Verlangen des DPMA; biologisches Material durch Hinterlegung nach § 34 Abs. 8 PatG bei einer anerkannten Hinterlegungsstelle (Budapester Vertrag).",
    "19": "Form der Einreichung sonstiger Eingaben (Einspruch, Anträge): schriftlich, unterschrieben; elektronische Einreichung über DPMAdirekt nach der ERVDPMAV.",
    "20": "Ergänzende Schutzzertifikate: Antrag auf Erteilung (§ 49a PatG) mit Angaben zur Genehmigung für das Inverkehrbringen, zum Grundpatent und zum Erzeugnis; Laufzeitverlängerung (pädiatrisch) nach § 21.",
}

HINWEISE_INTPATUEG = {
    "I": "Zustimmungsgesetz zum Straßburger Übereinkommen (1963), zum PCT (1970) und zum EPÜ (1973); Art. II und III enthalten das nationale Ausführungsrecht, das in Klausuren als „IntPatÜG“ zitiert wird (amtliche Abkürzung IntPatÜbkG).",
    "II § 1": "Entschädigungsanspruch aus der veröffentlichten europäischen Anmeldung wie § 33 PatG, aber erst ab Veröffentlichung einer deutschen Übersetzung der Ansprüche oder Zugang an den Benutzer (Abs. 1); Art. 67 EPÜ.",
    "II § 2": "Veröffentlichung von Übersetzungen der Patentansprüche europäischer Anmeldungen durch das DPMA auf Antrag (Gebühr Nr. 313 800); Voraussetzung des Entschädigungsanspruchs nach § 1.",
    "II § 3": "Übersetzungserfordernis für europäische Patente nach Art. 65 EPÜ; für Patente mit Erteilungshinweis ab 1.5.2008 durch das Londoner Übereinkommen entfallen (Art. XI § 4). BPatG Ethylenische Hauptketten: Übergangsfrage. Gebührenpflichtige Übermittlung von Informationen an das EPA.",
    "II § 4": "Einreichung europäischer Anmeldungen beim DPMA (Art. 75 Abs. 1 lit. b EPÜ) und Weiterleitung; Pflicht zur Inlandsanmeldung bei geheimhaltungsbedürftigen Erfindungen (§ 52 PatG entsprechend).",
    "II § 5": "Anspruch gegen den nichtberechtigten Anmelder einer europäischen Anmeldung wie § 8 PatG (Abtretung der Anmeldung; Art. 61 EPÜ).",
    "II § 6": "Nichtigkeit des deutschen Teils eines europäischen Patents: Gründe abschließend nach Art. 138 Abs. 1 EPÜ (Abs. 1 Nr. 1 bis 5), Verfahren nach §§ 81 ff. PatG; beschränkte Verteidigung (Abs. 3). Zuständig bleiben die deutschen Gerichte, solange nicht das EPG ausschließlich zuständig ist (Opt-out, Übergangszeit nach Art. 83 EPGÜ). Klarheit ist kein Nichtigkeitsgrund (BGH Fugenband). Die meistzitierte Vorschrift des Gesetzes in der BPatG-Rechtsprechung.",
    "II § 6a": "Ergänzende Schutzzertifikate auf der Grundlage europäischer Patente: Nichtigkeit nach Art. 15 VO (EG) Nr. 469/2009 im Verfahren nach § 81 PatG.",
    "II § 7": "Jahresgebühren für europäische Patente an das DPMA nach § 17 PatG und PatKostG, beginnend mit dem Jahr, das auf das Jahr des Erteilungshinweises folgt (Art. 141 EPÜ).",
    "II § 8": "Verbot des Doppelschutzes: Ein deutsches Patent für dieselbe Erfindung desselben Erfinders mit gleichem Zeitrang verliert seine Wirkung, soweit ein europäisches Patent mit Wirkung für Deutschland erteilt ist, ab Ablauf der Einspruchsfrist bzw. rechtskräftigem Abschluss des Einspruchs (Abs. 1). Seit 2023 gilt das nicht mehr, wenn das europäische Patent dem EPG unterliegt (§ 18: Doppelschutz zulässig, Einrede der doppelten Inanspruchnahme).",
    "II § 9": "Umwandlung einer europäischen Anmeldung in eine deutsche Anmeldung (Art. 135 EPÜ) bei Rücknahmefiktion wegen Übersetzungsfristversäumung; Gebühr wie Anmeldung; Übersetzung binnen drei Monaten.",
    "II § 10": "Zuständigkeit der Gerichte für Klagen aus europäischen Patenten wie für deutsche Patente (§ 143 PatG); Anerkennungsprotokoll zum EPÜ für Vindikationsstreitigkeiten.",
    "II § 15": "Nationale Vorschriften für das europäische Patent mit einheitlicher Wirkung: Das Einheitspatent gilt im Inland wie ein europäisches Patent, soweit die EPatVO nichts anderes bestimmt; §§ 6 bis 9 sind nicht anzuwenden (keine nationale Nichtigkeit, keine Jahresgebühren an das DPMA, keine Umwandlung).",
    "II § 16": "Zwangslizenz am Einheitspatent nach § 24 PatG mit Wirkung für Deutschland (Art. 32 Abs. 1 EPGÜ nennt Zwangslizenzen nicht: nationale Gerichte bleiben zuständig).",
    "II § 17": "Verzicht auf das Einheitspatent nur einheitlich gegenüber dem EPA; ein nationaler Teilverzicht ist ausgeschlossen (Art. 3 Abs. 2 EPatVO).",
    "II § 18": "Doppelschutz seit 1.6.2023: Ein deutsches Patent bleibt neben einem europäischen Patent oder Einheitspatent bestehen, wenn das europäische Patent dem EPG unterliegt (Abs. 1). Einrede der doppelten Inanspruchnahme (Abs. 2): Wer wegen derselben Handlung bereits vor dem EPG in Anspruch genommen wurde, kann die Klage aus dem deutschen Patent abwehren.",
    "II § 19": "Vollstreckung aus Entscheidungen des EPG im Inland nach der ZPO (Art. 82 EPGÜ): Vollstreckungsklausel durch den Rechtspfleger des Landgerichts, Vollstreckungsabwehrklage nach § 767 ZPO beim EPG.",
    "II § 20": "Beitreibung von Geldforderungen des EPG (Zwangsgelder, Gebühren) im Inland nach der Justizbeitreibungsordnung.",
    "III § 1": "Das DPMA als Anmeldeamt für internationale Anmeldungen (Art. 10 PCT): Übermittlungsgebühr (Nr. 313 900), Weiterleitung an das Internationale Büro; Anmelder mit Sitz oder Staatsangehörigkeit in Deutschland.",
    "III § 2": "Geheimhaltungsbedürftige internationale Anmeldungen: Prüfung nach §§ 50 ff. PatG vor der Weiterleitung.",
    "III § 4": "Das DPMA als Bestimmungsamt: Nationale Phase binnen 30 Monaten ab Priorität mit Übersetzung und nationaler Gebühr (Nr. 311 150); ohne fristgerechten Eintritt gilt die Wirkung der Anmeldung als beendet. BPatG Nationale Gebühr einer internationalen Anmeldung: Fälligkeit nach § 3 Abs. 1 PatKostG.",
    "III § 5": "Weiterbehandlung als nationale Anmeldung (Art. 25 PCT) nach Fehlern des Anmeldeamts oder des Internationalen Büros.",
    "III § 6": "Das DPMA als ausgewähltes Amt (Kapitel II PCT, internationale vorläufige Prüfung): Fristen für den Eintritt in die nationale Phase.",
    "III § 8": "Wirkung der internationalen Veröffentlichung: Entschädigungsanspruch nach § 33 PatG erst mit Veröffentlichung einer deutschen Übersetzung durch das DPMA.",
    "XI § 4": "Übergang zum Londoner Übereinkommen: Für europäische Patente mit Erteilungshinweis ab 1.5.2008 entfällt das Übersetzungserfordernis des Art. II § 3.",
}

HINWEISE_PATKOSTG = {
    "1": "Gilt für alle Gebühren und Auslagen des DPMA und des BPatG (Patente, Gebrauchsmuster, Marken, Designs, Topografien); Verfahrenskostenfreiheit nur, wo das Gesetz sie vorsieht. Ermächtigung für die PatKostZV (Zahlungsformen und Zahlungstag).",
    "2": "Höhe nach dem Gebührenverzeichnis (Anlage); im Klageverfahren (Nichtigkeit, Zwangslizenz) Wertgebühren nach dem Streitwert (Abs. 2: 4,5 Gebühren nach § 34 GKG). Streitwertfestsetzung im Nichtigkeitsverfahren nach § 121 PatG.",
    "3": "Fälligkeit: mit Einreichung der Anmeldung, des Antrags oder des Rechtsbehelfs (Abs. 1); Jahresgebühren am letzten Tag des Monats, der durch seine Benennung dem Monat des Anmeldetags entspricht (Abs. 2). Wertgebühren mit Einreichung der Klage. Von der Fälligkeit laufen die Zahlungsfristen der §§ 6, 7.",
    "4": "Kostenschuldner ist, wer die Amtshandlung beantragt oder das Verfahren einleitet; mehrere haften als Gesamtschuldner; Jahresgebühren kann jeder zahlen (Dritter, Lizenznehmer).",
    "5": "Vorauszahlung und Vorschuss: Bei Klagen vor dem BPatG wird die Gebühr für das Verfahren im Allgemeinen vorab fällig; ohne Zahlung binnen der gesetzten Frist wird die Klage nicht zugestellt (§ 81 Abs. 5 PatG i.V.m. Abs. 2).",
    "6": "Zahlungsfrist drei Monate ab Fälligkeit für Anmeldungs-, Prüfungs- und Antragsgebühren (Abs. 1 S. 1); für Rechtsbehelfe (Einspruch, Beschwerde, Erinnerung) gilt die Rechtsbehelfsfrist (Abs. 1 S. 2). Folge der Nichtzahlung: Anmeldung gilt als zurückgenommen, Antrag als nicht gestellt, Rechtsbehelf als nicht erhoben (Abs. 2). Häufigster Klausurfehler: Beschwerde ohne Gebühr binnen Monatsfrist. BPatG Einspruchsgebühren bei gemeinsamem Einspruch.",
    "7": "Jahresgebühren: Zahlung bis zum Ablauf des zweiten Monats nach Fälligkeit ohne Zuschlag, danach bis zum Ablauf des sechsten Monats mit Verspätungszuschlag von 50 EUR (Abs. 1); Nichtzahlung führt zum Erlöschen (§ 20 Abs. 1 Nr. 3 PatG). Vorauszahlung der nächsten Jahresgebühr bis ein Jahr vor Fälligkeit (Abs. 2). BPatG Sägeblatt: Insolvenzeröffnung unterbricht die Zahlungsfrist nicht.",
    "8": "Kostenansatz durch das DPMA oder das BPatG (Kostenbeamter); Rechtsbehelf: Erinnerung und Beschwerde nach § 11.",
    "9": "Kosten, die bei richtiger Sachbehandlung nicht entstanden wären, werden nicht erhoben; Grundlage für die Rückzahlung von Beschwerdegebühren bei Verfahrensfehlern (§ 80 Abs. 3 PatG).",
    "10": "Rückzahlung gezahlter Gebühren, wenn die Handlung nicht vorgenommen wird oder die Zahlung ohne Rechtsgrund erfolgte (Abs. 1); Wegfall der Jahresgebühr bei Rücknahme der Anmeldung oder Verzicht vor Fälligkeit (Abs. 2). BPatG Jahresgebühren: keine Rückzahlung mit Rechtsgrund entrichteter Gebühren.",
    "11": "Erinnerung gegen den Kostenansatz beim DPMA, Beschwerde zum BPatG (Juristischer Beschwerdesenat); Rechtspfleger beim BPatG.",
    "12": "Verjährung der Kostenforderungen und Erstattungsansprüche nach vier Jahren (§ 5 GKG entsprechend); keine Verzinsung.",
    "14": "Übergangsrecht zum 1.1.2002 (Inkrafttreten des PatKostG); für Klausuren nur noch selten relevant, aber § 13 (bisherige Gebührensätze bei früherer Fälligkeit) erklärt, warum bei Altpatenten der Gebührenstand am Fälligkeitstag maßgeblich ist.",
    "anlage": "Gebührenverzeichnis (Stand nach dem Gesetz vom 11.1.2026): Anmeldung elektronisch 40 EUR (Nr. 311 000, Papier 1,5-fach), Recherche 300 EUR (311 200), Prüfung 350 EUR bzw. 150 EUR nach Recherche (311 400, 311 300), Jahresgebühren 3. Jahr 70 EUR bis 20. Jahr 2 030 EUR (312 030 ff., halbiert bei Lizenzbereitschaft, Zuschlag 50 EUR), Weiterbehandlung 100 EUR (313 000), Einspruch 200 EUR (313 600), Beschwerde 500 EUR (401 100) bzw. 200 EUR in anderen Fällen (401 300), Nichtigkeitsklage 4,5 Wertgebühren (402 100). Gebrauchsmuster: Anmeldung 30 EUR, Löschung 300 EUR. Beträge in Klausuren immer am Verzeichnis prüfen; maßgeblich ist der bei Fälligkeit geltende Satz (§ 13).",
}

# ------------------------------------------------------------------ Brücken
# PatV -> PatG (Kante `konkretisiert`): welche Vorschrift des PatG die Verordnung ausfüllt
BEZUG_PATV = {
    "1": ["§ 34 Abs. 6 PatG"], "3": ["§ 34 Abs. 3 PatG", "§ 36 PatG"], "4": ["§ 34 Abs. 3 Nr. 1 PatG", "§ 35 Abs. 1 PatG"], "5": ["§ 34 Abs. 3 PatG"],
    "6": ["§ 34 Abs. 6 PatG"], "7": ["§ 37 PatG"], "8": ["§ 63 Abs. 1 PatG"], "9": ["§ 34 Abs. 3 Nr. 3 PatG", "§ 14 PatG"], "10": ["§ 34 Abs. 3 Nr. 4 PatG", "§ 34 Abs. 4 PatG"],
    "11": ["§ 34 Abs. 3 PatG"], "11a": ["§ 34 Abs. 3 PatG"], "11b": ["§ 38 PatG"], "12": ["§ 34 Abs. 3 Nr. 5 PatG", "§ 35a PatG"], "13": ["§ 36 PatG"],
    "14": ["§ 126 PatG", "§ 35 Abs. 2 PatG"], "15": ["§ 35a PatG"], "16": ["§ 34 Abs. 8 PatG"], "19": ["§ 59 Abs. 1 PatG"], "20": ["§ 49a PatG", "§ 16a PatG"], "21": ["§ 49a PatG"],
}
# PatKostG -> PatG
BEZUG_PATKOSTG = {
    "2": ["§ 121 PatG"], "3": ["§ 17 PatG", "§ 44 PatG", "§ 59 Abs. 1 PatG"], "5": ["§ 81 Abs. 5 PatG"], "6": ["§ 44 Abs. 4 PatG", "§ 59 Abs. 1 PatG", "§ 73 Abs. 2 PatG", "§ 39 Abs. 2 PatG"],
    "7": ["§ 17 PatG", "§ 20 Abs. 1 Nr. 3 PatG", "§ 23 Abs. 1 PatG"], "9": ["§ 80 Abs. 3 PatG"], "10": ["§ 17 PatG"], "anlage": ["§ 17 PatG", "§ 43 PatG", "§ 44 PatG", "§ 59 PatG", "§ 73 PatG", "§ 81 PatG", "§ 123a PatG"],
}
# IntPatÜG -> PatG
BEZUG_INTPATUEG = {
    "II § 1": ["§ 33 PatG"], "II § 5": ["§ 8 PatG"], "II § 6": ["§ 21 PatG", "§ 22 PatG", "§ 81 PatG"], "II § 6a": ["§ 16a PatG", "§ 49a PatG"], "II § 7": ["§ 17 PatG"],
    "II § 8": ["§ 20 PatG"], "II § 9": ["§ 34 PatG", "§ 35 PatG"], "II § 10": ["§ 143 PatG"], "II § 16": ["§ 24 PatG", "§ 81 PatG"], "II § 18": ["§ 139 PatG"],
    "III § 1": ["§ 34 PatG"], "III § 2": ["§ 50 PatG"], "III § 4": ["§ 34 PatG", "§ 35 PatG", "§ 44 PatG"], "III § 8": ["§ 33 PatG"],
}
# IntPatÜG -> EPGÜ / EPatVO (Kante `entspricht`: Vorschrift gleicher Funktion)
ENTSPRICHT_INTPATUEG = {
    "II § 15": ["Art. 3 EPatVO", "Art. 4 EPatVO"], "II § 17": ["Art. 3 EPatVO"], "II § 18": ["Art. 83 EPGÜ"], "II § 19": ["Art. 82 EPGÜ"], "II § 20": ["Art. 82 EPGÜ"],
}
# PatG -> EPGÜ (Kante `entspricht`): materielles Verletzungsrecht und Rechtsfolgen
ENTSPRICHT_PATG = {
    "9": ["Art. 25 EPGÜ"], "10": ["Art. 26 EPGÜ"], "11": ["Art. 27 EPGÜ"], "12": ["Art. 28 EPGÜ"], "22": ["Art. 65 EPGÜ"], "24": ["Art. 32 Abs. 1 EPGÜ"],
    "139": ["Art. 63 EPGÜ", "Art. 68 EPGÜ"], "140a": ["Art. 64 EPGÜ"], "140b": ["Art. 67 EPGÜ"], "140c": ["Art. 59 EPGÜ", "Art. 60 EPGÜ"], "140d": ["Art. 61 EPGÜ"], "140e": ["Art. 80 EPGÜ"], "144": ["Art. 69 EPGÜ"],
}

_FAM = [
    dict(key="patg", datei="patg.json", kurz="PatG", aliase=(), hinweise=HINWEISE_PATG, titel_map=PATG_TITEL, bezug={}, entspricht=ENTSPRICHT_PATG,
         titel="Patentgesetz (PatG)", gesetz="PatG (Neufassung 1980, zuletzt geändert 20.5.2026)",
         hinweis="Amtlicher Wortlaut von gesetze-im-internet.de (XML-Fassung); das PatG trägt keine Paragraphenüberschriften, die Stichworte sind redaktionell."),
    dict(key="patv", datei="patv.json", kurz="PatV", aliase=(), hinweise=HINWEISE_PATV, titel_map={}, bezug=BEZUG_PATV, entspricht={},
         titel="Patentverordnung (PatV)", gesetz="PatV (Verordnung zum Verfahren in Patentsachen vor dem DPMA, zuletzt geändert 14.6.2022)",
         hinweis="Amtlicher Wortlaut von gesetze-im-internet.de; Anlage 2 (Zeichnungsstandards) als Vorschrift erfasst."),
    dict(key="intpatueg", datei="intpatueg.json", kurz="IntPatÜG", aliase=("IntPatÜbkG",), hinweise=HINWEISE_INTPATUEG, titel_map={}, bezug=BEZUG_INTPATUEG, entspricht=ENTSPRICHT_INTPATUEG,
         titel="Gesetz über internationale Patentübereinkommen (IntPatÜG)", gesetz="IntPatÜbkG (Zustimmungs- und Ausführungsgesetz zu EPÜ und PCT, zuletzt geändert 20.8.2021)",
         hinweis="Amtlicher Wortlaut von gesetze-im-internet.de; Zitierform Art. II § 6 IntPatÜG (amtliche Abkürzung IntPatÜbkG); Art. I, VII und X als eigene Vorschriften."),
    dict(key="patkostg", datei="patkostg.json", kurz="PatKostG", aliase=(), hinweise=HINWEISE_PATKOSTG, titel_map={}, bezug=BEZUG_PATKOSTG, entspricht={},
         titel="Patentkostengesetz (PatKostG)", gesetz="PatKostG (Gesetz über die Kosten des DPMA und des BPatG, zuletzt geändert 11.1.2026)",
         hinweis="Amtlicher Wortlaut von gesetze-im-internet.de; das Gebührenverzeichnis (Anlage zu § 2 Abs. 1) ist zeilenweise erfasst (Nummer | Tatbestand | Gebühr)."),
]

FAMILIEN = []
META = {}
for _f in _FAM:
    _j = json.loads((_DATA / _f["datei"]).read_text(encoding="utf-8"))
    META[_f["key"]] = _j["meta"]
    arts = []
    for _i, _p in enumerate(_j["paragraphen"]):
        nr = _p["nr"]
        arts.append(dict(
            nr=nr, label=_p["label"] + " " + _f["kurz"], titel=_p["titel"] or _f["titel_map"].get(nr, ""), kapitel=_p["teil"] or "Allgemeines", abschnitt=_p["abschnitt"],
            absaetze=[dict(nr=a["nr"], text=a["text"]) for a in _p["absaetze"]], order=_i + 1,
            umsetzung=[], umsetzung_weitere={}, concepts=[], cases=[],
            entspricht=_f["entspricht"].get(nr, []), bezug=_f["bezug"].get(nr, []), hinweis=_f["hinweise"].get(nr, ""), url=_p["url"],
        ))
    FAMILIEN.append(dict(key=_f["key"], kurz=_f["kurz"], aliase=_f["aliase"], titel=_f["titel"], gesetz=_f["gesetz"], artikel=arts,
                         erwaegungsgruende=[], url=_j["meta"]["quelle"], url_pdf=_j["meta"]["quelle_xml"], paraphrase=False,
                         zitat="Art." if _f["key"] == "intpatueg" else "§", hinweis=_f["hinweis"], stand="; ".join(_j["meta"]["stand"]), korpus="patent"))
