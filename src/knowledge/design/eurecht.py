# -*- coding: utf-8 -*-
"""Unionsrecht des Designpakets als `eunorm`-Familien (build_graph.RICHTLINIEN):

  designrl      Richtlinie 98/71/EG über den rechtlichen Schutz von Mustern und Modellen (amtlicher Wortlaut, data/designrl.json;
                Cellar-PDF des Amtsblatts). `umsetzung` = DesignG-Vorschriften (Kante `implements` DesignG -> Richtlinie). Gilt bis 9.12.2027.
  designrl2024  Richtlinie (EU) 2024/2823 (Neufassung; data/designrl2024.json, Cellar-XHTML). Noch nicht umgesetzt; `entspricht` zeigt auf
                den Vorgängerartikel der Richtlinie 98/71/EG, `hinweis` nennt die Neuerungen.
  ggv           Verordnung (EG) Nr. 6/2002 über Unionsgeschmacksmuster, konsolidiert zum 1.7.2026 (data/ggv.json, Cellar-XHTML; enthält die
                Änderungen der Verordnung (EU) 2024/2822). Zitierform weiter „GGV“ (Alias UGMV). Entsprechungen DesignG -> GGV stehen in
                gesetze_texte.ENTSPRICHT_DESIGNG.

Zitierformen in `norms`-Feldern: `Art. 5 DesignRL`, `Art. 19 DesignRL 2024`, `Art. 8 Abs. 1 GGV`.
"""
import json
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data"

# ------------------------------------------------------------------ Richtlinie 98/71/EG: Umsetzung im DesignG und Hinweise
UMSETZUNG_DESIGNRL = {
    "1": ["§ 1 DesignG"], "2": ["§ 66 DesignG"], "3": ["§ 2 Abs. 1 DesignG", "§ 4 DesignG", "§ 1 DesignG", "§ 27 Abs. 1 DesignG"],
    "4": ["§ 2 Abs. 2 DesignG"], "5": ["§ 2 Abs. 3 DesignG"], "6": ["§ 5 DesignG", "§ 6 DesignG"], "7": ["§ 3 Abs. 1 DesignG", "§ 3 Abs. 2 DesignG"],
    "8": ["§ 3 Abs. 1 DesignG"], "9": ["§ 38 Abs. 2 DesignG"], "10": ["§ 27 Abs. 2 DesignG", "§ 28 DesignG"], "11": ["§ 18 DesignG", "§ 33 DesignG", "§ 34 DesignG", "§ 35 DesignG"],
    "12": ["§ 38 Abs. 1 DesignG"], "13": ["§ 40 DesignG"], "14": ["§ 73 DesignG", "§ 40a DesignG"], "15": ["§ 48 DesignG"], "16": ["§ 50 DesignG"], "17": ["§ 50 DesignG"],
}
HINWEISE_DESIGNRL = {
    "1": "Begriffe Muster, Erzeugnis, komplexes Erzeugnis: wörtlich in § 1 DesignG übernommen (dort „Design“ statt „Muster“). Computerprogramme sind keine Erzeugnisse, grafische Symbole und Schriftbilder schon.",
    "2": "Anwendungsbereich: nationale Registermuster, Benelux-Muster und internationale Eintragungen mit Wirkung für einen Mitgliedstaat; das Gemeinschaftsgeschmacksmuster regelt die GGV parallel und weitgehend wortgleich.",
    "3": "Schutz nur durch Eintragung (kein nationales nicht eingetragenes Design; dafür Art. 11 GGV); Schutzvoraussetzungen Neuheit und Eigenart; Bauelemente nur bei Sichtbarkeit bei bestimmungsgemäßer Verwendung (Abs. 3, 4 = § 4, § 1 Nr. 4 DesignG; EuGH Monz/Büchel).",
    "4": "Neuheit: kein identisches Muster vor dem Anmelde- oder Prioritätstag zugänglich gemacht; unwesentliche Einzelheiten unschädlich. § 2 Abs. 2 DesignG.",
    "5": "Eigenart: anderer Gesamteindruck beim informierten Benutzer, Gestaltungsfreiheit berücksichtigen. § 2 Abs. 3 DesignG. EuGH PepsiCo (informierter Benutzer), Karen Millen (Einzelvergleich, keine Merkmalskombination aus mehreren Mustern).",
    "6": "Offenbarung mit Fachkreisklausel und Vertraulichkeitsvorbehalt (Abs. 1 = § 5 DesignG); Neuheitsschonfrist zwölf Monate (Abs. 2 = § 6 DesignG); missbräuchliche Offenbarung (Abs. 3). EuGH Gautzsch/Duna zur Offenbarung außerhalb der Union.",
    "7": "Technisch bedingte Merkmale (Abs. 1), Verbindungselemente (Abs. 2), modulare Systeme (Abs. 3) = § 3 Abs. 1 Nr. 1, 2, Abs. 2 DesignG. EuGH DOCERAM: objektiver Maßstab; EuG Lego zu Abs. 3.",
    "8": "Ordre public und gute Sitten = § 3 Abs. 1 Nr. 3 DesignG.",
    "9": "Schutzumfang: jedes Muster ohne anderen Gesamteindruck, Gestaltungsfreiheit berücksichtigen = § 38 Abs. 2 DesignG. Spiegelbild der Eigenart (Art. 5): Was Eigenart begründet, bestimmt den Schutzumfang (BGH Untersetzer).",
    "10": "Schutzdauer: Fünfjahresabschnitte bis 25 Jahre ab Anmeldung = § 27 Abs. 2, § 28 DesignG.",
    "11": "Nichtigkeitsgründe und Eintragungshindernisse: zwingende (Abs. 1: kein Muster, fehlende Schutzvoraussetzungen, Nichtberechtigung, älteres Muster) und fakultative (Abs. 2: Zeichen, Urheberrecht, Hoheitszeichen); Antragsbefugnis (Abs. 3 bis 5); Aufrechterhaltung in geänderter Form (Abs. 7). Umsetzung in §§ 18, 33, 34, 35 DesignG; Deutschland hat alle fakultativen Gründe übernommen.",
    "12": "Rechte aus dem Muster: ausschließliches Benutzungsrecht mit Beispielskatalog = § 38 Abs. 1 DesignG.",
    "13": "Schranken: privat, Versuche, Zitat und Lehre, Schiffe und Luftfahrzeuge = § 40 DesignG. EuGH Nintendo/BigBen zur Zitierschranke.",
    "14": "Übergangsbestimmung „freeze plus“: Mitgliedstaaten behalten ihre Regeln zur Reparatur komplexer Erzeugnisse bei und dürfen sie nur liberalisieren. Deutschland hatte keine Reparaturklausel (voller Ersatzteilschutz, § 73 Abs. 1 DesignG für Altfälle) und hat sie erst 2020 mit § 40a DesignG eingeführt; die Richtlinie (EU) 2024/2823 macht sie mit Art. 19 zwingend.",
    "15": "Erschöpfung im Binnenmarkt = § 48 DesignG (EWR-weit, keine internationale Erschöpfung).",
    "16": "Verhältnis zu anderen Schutzformen: nicht eingetragene Rechte, Marken, Patente, Gebrauchsmuster, unlauterer Wettbewerb, Haftungsrecht bleiben unberührt = § 50 DesignG.",
    "17": "Kumulation mit dem Urheberrecht: Muster sind auch urheberrechtlich schutzfähig; Schutzumfang und Voraussetzungen (Originalität) bestimmt der Mitgliedstaat. EuGH Cofemel und Brompton: Werkbegriff des Unionsrechts, keine erhöhte Gestaltungshöhe; BGH Geburtstagszug (Aufgabe der Stufentheorie). = § 50 DesignG.",
    "18": "Revisionsklausel: führte über den Vorschlag von 2004 (Reparaturklausel) und die Evaluierung 2020 schließlich zur Neufassung durch die Richtlinie (EU) 2024/2823.",
    "19": "Umsetzungsfrist 28.10.2001; Deutschland setzte mit dem Geschmacksmusterreformgesetz vom 12.3.2004 (in Kraft 1.6.2004) um. Für Altmuster gelten die alten Schutzvoraussetzungen (§ 72 Abs. 2 DesignG).",
}

# ------------------------------------------------------------------ Richtlinie (EU) 2024/2823: Vorgängerartikel und Neuerungen
ENTSPRICHT_DESIGNRL2024 = {
    "1": ["Art. 2 DesignRL"], "2": ["Art. 1 DesignRL"], "3": ["Art. 3 DesignRL"], "4": ["Art. 4 DesignRL"], "5": ["Art. 5 DesignRL"], "6": ["Art. 6 DesignRL"],
    "7": ["Art. 7 DesignRL"], "8": ["Art. 8 DesignRL"], "9": ["Art. 9 DesignRL"], "10": ["Art. 10 DesignRL"], "13": ["Art. 11 DesignRL"], "14": ["Art. 11 DesignRL"],
    "16": ["Art. 12 DesignRL"], "18": ["Art. 13 DesignRL"], "19": ["Art. 14 DesignRL"], "20": ["Art. 15 DesignRL"], "22": ["Art. 16 DesignRL"], "23": ["Art. 17 DesignRL"],
    "36": ["Art. 19 DesignRL"], "38": ["Art. 20 DesignRL"], "39": ["Art. 21 DesignRL"],
}
HINWEISE_DESIGNRL2024 = {
    "1": "Anwendungsbereich wie bisher; die Neufassung erfasst ausdrücklich auch die Anmeldungen.",
    "2": "Neue Begriffe: „Design“ statt „Muster“, erstmals ausdrücklich auch Bewegung, Übergänge und Animation als Merkmale (Nr. 3: Erscheinungsform „einschließlich der Bewegung, des Übergangs oder jeder anderen Art von Animation“); Erzeugnis umfasst auch nicht körperliche Gegenstände, grafische Benutzeroberflächen und räumliche Anordnungen (Nr. 4). Muss bis 9.12.2027 in § 1 DesignG umgesetzt werden.",
    "3": "Schutzvoraussetzungen unverändert (Neuheit, Eigenart, Sichtbarkeit von Bauelementen); Begriff „übliche Verwendung“ statt „bestimmungsgemäße Verwendung“. Erwägungsgründe stellen klar, dass Merkmale nicht in jedem Moment sichtbar sein müssen.",
    "7": "Technische Bedingtheit unverändert; Erwägungsgrund 16 übernimmt EuGH DOCERAM (objektive Prüfung, Mehrheit-der-Formen ist nur ein Indiz).",
    "15": "Neu: Gegenstand des Schutzes sind die in der Anmeldung sichtbar wiedergegebenen Merkmale (bisher nur § 37 DesignG national, jetzt harmonisiert).",
    "16": "Rechte aus dem Design: neu ausdrücklich das Erstellen, Herunterladen, Kopieren und Weitergeben von Dateien zur Herstellung des Erzeugnisses (3D-Druck, Abs. 2 lit. d) und das Verbot der Durchfuhr von Waren aus Drittstaaten (Abs. 3) wie im Markenrecht.",
    "17": "Vermutung der Rechtsgültigkeit des eingetragenen Designs (bisher nur § 39 DesignG national).",
    "18": "Schranken: neu ausdrücklich Handlungen zur Identifizierung oder Bezugnahme (Referenznutzung, Abs. 1 lit. d) sowie Kommentar, Kritik und Parodie (lit. e), jeweils unter dem Vorbehalt der Lauterkeit.",
    "19": "Reparaturklausel wird zwingend für alle Mitgliedstaaten: kein Schutz für formgebundene Bauelemente („must match“), die allein zur Reparatur des komplexen Erzeugnisses verwendet werden; Unterrichtungspflicht über den Ursprung (Abs. 2); Bestandsschutz für vor dem 8.12.2024 angemeldete Designs bis 9.12.2032 (Abs. 4). Deutschland: § 40a DesignG (seit 2020) genügt im Kern; § 73 Abs. 2 DesignG muss mit dem Enddatum 2032 harmonisiert werden. Vorbild Art. 20a GGV.",
    "20": "Erschöpfung unverändert (unionsweit).",
    "21": "Neu harmonisiert: Vorbenutzungsrecht (bisher § 41 DesignG national, Art. 22 GGV).",
    "23": "Kumulation mit dem Urheberrecht: Werk, wenn die urheberrechtlichen Voraussetzungen erfüllt sind (Kodifikation von EuGH Cofemel).",
    "24": "Eintragungssymbol: Ⓓ (D im Kreis) darf als Hinweis auf den Designschutz verwendet werden.",
    "26": "Darstellung des Designs: jede Form der visuellen Wiedergabe einschließlich Video und 3D-Modellen; Ämter müssen digitale Darstellungen akzeptieren; Verzicht auf Schutz einzelner sichtbarer Merkmale möglich (Disclaimer).",
    "27": "Sammelanmeldungen ohne Bindung an eine Warenklasse (so schon § 12 DesignG seit 2014); Obergrenze bleibt dem nationalen Recht überlassen (Deutschland: 100).",
    "30": "Aufschiebung der Bekanntmachung: mindestens 30 Monate ab Anmeldetag (§ 21 DesignG entspricht).",
    "31": "Nichtigkeitsverfahren: Mitgliedstaaten müssen ein effizientes Verwaltungsverfahren beim Amt vorsehen (in Deutschland seit 2014: § 34a DesignG).",
    "36": "Umsetzungsfrist 9.12.2027; die Richtlinie 98/71/EG wird mit diesem Tag aufgehoben (Art. 37).",
}

# ------------------------------------------------------------------ GGV: Hinweise zu den Kernvorschriften
HINWEISE_GGV = {
    "1": "Zwei Schutzformen mit einheitlicher Wirkung in der ganzen Union (Abs. 3): nicht eingetragenes Unionsgeschmacksmuster kraft Offenbarung (Abs. 2 lit. a) und eingetragenes durch Eintragung beim EUIPO (lit. b). Seit 1.5.2025 „Unionsgeschmacksmuster“ statt „Gemeinschaftsgeschmacksmuster“ (Verordnung (EU) 2024/2822).",
    "3": "Begriffe Geschmacksmuster, Erzeugnis, komplexes Erzeugnis wie § 1 DesignG; seit der Reform 2024 einschließlich Bewegung und Animation sowie nicht körperlicher Erzeugnisse.",
    "4": "Schutzvoraussetzungen Neuheit und Eigenart; Bauelemente nur bei Sichtbarkeit bei bestimmungsgemäßer Verwendung (Abs. 2, 3) = § 2 Abs. 1, § 4 DesignG.",
    "5": "Neuheit: getrennte Stichtage für nicht eingetragene (erste Offenbarung) und eingetragene Muster (Anmelde- oder Prioritätstag) = § 2 Abs. 2 DesignG.",
    "6": "Eigenart = § 2 Abs. 3 DesignG. EuGH Karen Millen: Vergleich mit einzelnen vorbekannten Mustern, nicht mit einer Kombination; PepsiCo: informierter Benutzer.",
    "7": "Offenbarung mit Fachkreisklausel (EuGH Gautzsch/Duna), Neuheitsschonfrist zwölf Monate (Abs. 2) = §§ 5, 6 DesignG. Für das nicht eingetragene Muster entsteht der Schutz erst mit Offenbarung in der Union (Art. 11; EuGH Gautzsch: Offenbarung außerhalb der Union genügt nicht für die Entstehung).",
    "8": "Technisch bedingte Merkmale (EuGH DOCERAM), Verbindungselemente, modulare Systeme (EuG Lego) = § 3 Abs. 1 Nr. 1, 2, Abs. 2 DesignG.",
    "10": "Schutzumfang wie § 38 Abs. 2 DesignG; Gestaltungsfreiheit und Musterdichte bestimmen die Reichweite.",
    "11": "Nicht eingetragenes Unionsgeschmacksmuster: drei Jahre ab erster Offenbarung in der Union; Schutz nur gegen Nachahmung (Art. 19 Abs. 4). EuGH Ferrari/Mansory: Offenbarung eines Gesamterzeugnisses kann Teile davon als eigenes Muster offenbaren, wenn sie klar erkennbar sind.",
    "12": "Schutzdauer des eingetragenen Musters: fünf Jahre, verlängerbar bis 25 Jahre ab Anmeldetag (§ 27 Abs. 2 DesignG).",
    "14": "Recht auf das Unionsgeschmacksmuster: Entwerfer oder Rechtsnachfolger; Arbeitnehmermuster dem Arbeitgeber, sofern nicht anders vereinbart oder nationales Recht anderes bestimmt (Abs. 3) = § 7 DesignG.",
    "15": "Vindikation gegen den Nichtberechtigten binnen drei Jahren ab Bekanntmachung, außer bei Bösgläubigkeit = § 9 DesignG.",
    "18a": "Gegenstand des Schutzes: die in der Anmeldung sichtbar wiedergegebenen Merkmale (neu 2024; § 37 DesignG).",
    "19": "Rechte aus dem Muster: eingetragen = objektives Verbotsrecht (Abs. 1, 2, seit 2024 auch 3D-Druck-Dateien, Abs. 2 lit. d, und Durchfuhr, Abs. 3); nicht eingetragen = nur gegen Nachahmung, mit Vermutung, wenn der Entwerfer das Muster kennen konnte (Abs. 4). Während der Aufschiebung nur Nachahmungsschutz (Abs. 5) = § 38 DesignG.",
    "20": "Schranken wie § 40 DesignG, seit 2024 zusätzlich Referenznutzung sowie Kommentar, Kritik und Parodie (Abs. 1 lit. d, e). EuGH Nintendo/BigBen zur Zitierschranke.",
    "20a": "Reparaturklausel (ersetzt die Übergangsregelung des Art. 110 GGV a.F.): kein Schutz für formgebundene Bauelemente zur Reparatur komplexer Erzeugnisse; Unterrichtung der Verbraucher; Sorgfaltspflichten des Herstellers (EuGH Acacia/Audi und Porsche: keine Beschränkung auf formgebundene Teile nach Art. 110 GGV a.F., aber Hinweis- und Sorgfaltspflichten). Nationales Pendant § 40a DesignG.",
    "21": "Erschöpfung unionsweit = § 48 DesignG.",
    "22": "Vorbenutzungsrecht = § 41 DesignG.",
    "24": "Nichtigerklärung: eingetragenes Muster durch das EUIPO (Antrag, Art. 52) oder auf Widerklage vor dem Unionsgeschmacksmustergericht; nicht eingetragenes nur durch das Unionsgeschmacksmustergericht auf Klage oder Widerklage (Abs. 3), daneben Einrede (Art. 85 Abs. 2).",
    "25": "Nichtigkeitsgründe: kein Muster, Art. 4 bis 9 nicht erfüllt, Nichtberechtigung, älteres Muster, Zeichen mit Unterscheidungskraft, Urheberrecht, Hoheitszeichen; Antragsbefugnis (Abs. 2 bis 5). Die Aufrechterhaltung in geänderter Form (Abs. 6 a.F.) hat die Reform 2024 gestrichen. = § 33 DesignG.",
    "36": "Erfordernisse der Anmeldung beim EUIPO: Antrag, Anmelder, Wiedergabe, Erzeugnisangabe; Erzeugnisangabe ohne Einfluss auf den Schutzumfang (Abs. 6) = § 11 DesignG.",
    "37": "Sammelanmeldung ohne Klassenbindung (seit 2024; zuvor Einheitlichkeit der Klasse), Obergrenze 50 Muster = § 12 DesignG (100).",
    "38": "Anmeldetag = Eingang der Mindestunterlagen beim Amt = § 13 DesignG.",
    "41": "Priorität nach der PVÜ: sechs Monate = § 14 DesignG.",
    "47": "Eintragungshindernisse, die das EUIPO prüft: kein Muster, Verstoß gegen ordre public = § 18 DesignG; keine Prüfung der Neuheit und Eigenart.",
    "50": "Aufschiebung der Bekanntmachung um 30 Monate = § 21 DesignG.",
    "52": "Antrag auf Nichtigerklärung beim EUIPO: jedermann für absolute Gründe, Rechtsinhaber für relative = § 34 DesignG.",
    "80": "Unionsgeschmacksmustergerichte der Mitgliedstaaten (Deutschland: Landgerichte, § 63 DesignG) für Verletzungsklagen und Nichtigkeitswiderklagen.",
    "81": "Ausschließliche Zuständigkeit der Unionsgeschmacksmustergerichte für Verletzungsklagen, negative Feststellungsklagen und Nichtigkeitswiderklagen (auch beim nicht eingetragenen Muster).",
    "82": "Internationale Zuständigkeit: Wohnsitz oder Niederlassung des Beklagten, hilfsweise des Klägers, hilfsweise Spanien (Sitz des EUIPO); alternativ Verletzungsort (Abs. 5) mit auf den Staat beschränkter Reichweite (Art. 83 Abs. 2).",
    "83": "Reichweite: Sitzgerichtsstand unionsweit, Verletzungsortgerichtsstand nur für den eigenen Staat. EuGH Nintendo/BigBen: bei mehreren Beklagten im Gerichtsstand der Streitgenossenschaft unionsweite Anordnungen.",
    "84": "Widerklage auf Nichtigerklärung nur auf die Gründe des Art. 25; Popularwiderklage bei absoluten Gründen.",
    "85": "Vermutung der Rechtsgültigkeit: eingetragenes Muster nur durch Widerklage angreifbar (Abs. 1); nicht eingetragenes: Kläger muss Offenbarung und Eigenart darlegen, Beklagter kann Nichtigkeit einredeweise geltend machen (Abs. 2; EuGH Karen Millen). = § 39, § 52a DesignG.",
    "88": "Anwendbares Recht: die Verordnung, ergänzend das nationale Recht des Gerichtsstaats einschließlich IPR (Abs. 2). EuGH Acacia/BMW: für Folgeansprüche (Auskunft, Schadensersatz, Vernichtung) gilt über Art. 8 Abs. 2 Rom-II-VO das Recht des Staates, in dem die Verletzungshandlung begangen wurde; bei Klage im Verletzungsstaat also dessen Recht (§ 62a DesignG).",
    "89": "Sanktionen: Unterlassung direkt aus der Verordnung, Durchsetzung mit den Zwangsmitteln des nationalen Rechts (Abs. 1); weitere Maßnahmen wie Beschlagnahme und Vernichtung nach dem anwendbaren Recht (Abs. 2; bis 30.4.2025 Abs. 1 lit. b bis d a.F.) = § 62a DesignG mit §§ 42 ff. DesignG.",
    "90": "Einstweilige Maßnahmen bei den Gerichten aller Mitgliedstaaten; unionsweite Wirkung nur beim nach Art. 82 Abs. 1 bis 4 zuständigen Gericht (Abs. 3).",
    "96": "Verhältnis zu anderen Schutzformen (nationales Design, Marke, Patent, Urheberrecht, unlauterer Wettbewerb) = § 50 DesignG; Kumulation mit dem Urheberrecht (Abs. 2; EuGH Cofemel).",
    "106a": "Internationale Eintragungen nach der Genfer Akte des Haager Abkommens mit Benennung der EU wirken wie Anmeldungen beim EUIPO; Schutzverweigerung binnen sechs Monaten (Art. 106e).",
    "110a": "Erweiterung der Union: Muster gelten auch in neuen Mitgliedstaaten; kein Angriff wegen dort älterer Rechte, Weiterbenutzung dort möglich.",
}

_FAM = [
    dict(key="designrl", datei="designrl.json", kurz="DesignRL", aliase=(), hinweise=HINWEISE_DESIGNRL, umsetzung=UMSETZUNG_DESIGNRL, entspricht={},
         titel="Richtlinie 98/71/EG (DesignRL)",
         hinweis="Amtlicher Wortlaut der Richtlinie 98/71/EG (ABl. L 289 vom 28.10.1998, S. 28; Cellar-PDF, zweispaltiger Satz zusammengeführt). Gilt bis zur Aufhebung am 9.12.2027 durch die Richtlinie (EU) 2024/2823; das DesignG setzt sie um."),
    dict(key="designrl2024", datei="designrl2024.json", kurz="DesignRL 2024", aliase=(), hinweise=HINWEISE_DESIGNRL2024, umsetzung={}, entspricht=ENTSPRICHT_DESIGNRL2024,
         titel="Richtlinie (EU) 2024/2823 (DesignRL 2024)",
         hinweis="Amtlicher Wortlaut der Neufassung (ABl. L, 2024/2823 vom 18.11.2024; Cellar-XHTML). Umsetzungsfrist 9.12.2027; das DesignG ist im September 2026 noch nicht angepasst, `entspricht` zeigt auf den Vorgängerartikel der Richtlinie 98/71/EG."),
    dict(key="ggv", datei="ggv.json", kurz="GGV", aliase=("UGMV",), hinweise=HINWEISE_GGV, umsetzung={}, entspricht={},
         titel="Verordnung (EG) Nr. 6/2002 über Unionsgeschmacksmuster (GGV)",
         hinweis="Konsolidierte Fassung vom 1.7.2026 (Cellar-XHTML; Änderungsmarken entfernt), einschließlich der Verordnung (EU) 2024/2822, die seit 1.5.2025 gilt (Teile seit 1.7.2026). Erwägungsgründe sind in der konsolidierten Fassung nicht enthalten."),
]

FAMILIEN = []
STAND = {}
for _f in _FAM:
    _j = json.loads((_DATA / _f["datei"]).read_text(encoding="utf-8"))
    STAND[_f["key"]] = _j["meta"]["stand"]
    arts = []
    for _i, _a in enumerate(_j["artikel"]):
        nr = _a["nr"]
        arts.append(dict(
            nr=nr, label=f"Art. {nr} {_f['kurz']}", titel=_a["titel"], kapitel=_a["kapitel"], abschnitt=_a["abschnitt"],
            absaetze=[dict(nr=x["nr"], text=x["text"]) for x in _a["absaetze"]], order=_i + 1,
            umsetzung=_f["umsetzung"].get(nr, []), umsetzung_weitere={}, concepts=[], cases=[],
            entspricht=_f["entspricht"].get(nr, []), bezug=[], hinweis=_f["hinweise"].get(nr, ""),
        ))
    FAMILIEN.append(dict(key=_f["key"], kurz=_f["kurz"], aliase=_f["aliase"], titel=_f["titel"], gesetz=_j["gesetz"], artikel=arts,
                         erwaegungsgruende=[dict(nr=e["nr"], text=e["text"]) for e in _j["erwaegungsgruende"]],
                         url=_j["meta"]["quelle"], url_pdf=_j["meta"]["quelle_pdf"], paraphrase=False, zitat="Art.", hinweis=_f["hinweis"], stand=_j["meta"]["stand"]))
