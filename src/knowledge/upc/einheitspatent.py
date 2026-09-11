# -*- coding: utf-8 -*-
"""Rechtsgrundlagen des Einheitspatents (europäisches Patent mit einheitlicher Wirkung).

Vier weitere `eunorm`-Familien neben EPGÜ und VerfO; Wortlaut aus data/up_*.json (tools/fetch_upc.py, epo.org):
  EPatVO       Verordnung (EU) Nr. 1257/2012 (Einheitspatent), Art. 1–18, Zitat `Art. 3 Abs. 1 EPatVO`
  EPatÜVO  Verordnung (EU) Nr. 1260/2012 (Übersetzungsregelungen), Art. 1–7, Zitat `Art. 6 EPatÜVO`
  DOEPS        Durchführungsordnung zum einheitlichen Patentschutz (engl. UPR), Regeln 1–24, Zitat `R. 6 Abs. 1 DOEPS`
  GebOEPS      Gebührenordnung zum einheitlichen Patentschutz (engl. RFeesUPP), Art. 1–7, Zitat `Art. 3 GebOEPS`
Dazu die UP-Richtlinien des EPA (Ausgabe April 2026, data/up_richtlinien.json aus der Tabelle UPLegaltext) als
`source`-Knoten (Provider „UP-Richtlinien“, Teile und Abschnitte bis zur zweiten Ebene, Seiten-ID `uprl:2.4`) und die
EPA-Informationsseiten zum Einheitspatent (Provider „epo.org Einheitspatent“, `upinfo:cost`); Begriffe verweisen über
`quellen` darauf. Die Texte stammen aus der RheinIP-Datenbank (Spiegel von epo.org/de/legal/guidelines-up und
epo.org/de/applying/european/unitary/unitary-patent); `fetch_upc.py` schreibt sie nach data/.

Brücken: `entspricht` (Artikel -> Artikel gleicher Funktion in EPGÜ/EPatVO), `bezug` (Regel/Gebührenvorschrift -> die
Vorschrift, die sie durchführt); beide werden in build_graph.py als Kanten `entspricht` bzw. `konkretisiert` angelegt.
"""
import json
from pathlib import Path

from .upca import schoen

_DATA = Path(__file__).resolve().parents[3] / "data"

UP_RL_URL = "https://www.epo.org/de/legal/guidelines-up/2026/"
UP_RL_PDF = "https://link.epo.org/web/legal/guidelines-up/de-up-guidelines-2026-hyperlinked.pdf"
UP_RL_STAND = "Ausgabe April 2026, in Kraft seit 1.4.2026 (ABl. EPA 2026, A6); jährliche Überarbeitung, Stand 1.12.2025"
EPO_UP_URL = "https://www.epo.org/de/applying/european/unitary/unitary-patent"

# ------------------------------------------------------------------ Hinweise und Brücken je Vorschrift
HINWEISE_EPATVO = {
    1: "Verstärkte Zusammenarbeit nach Art. 20 EUV: 25 Mitgliedstaaten (alle außer Spanien und Kroatien). Die Verordnung ist ein „besonderes Übereinkommen“ im Sinne von Art. 142 EPÜ.",
    2: "„Teilnehmender Mitgliedstaat“ ist nur ein an der Verstärkten Zusammenarbeit beteiligter EU-Staat; wirken kann das Einheitspatent aber nur dort, wo das EPGÜ bei Eintragung in Kraft ist (Art. 18 Abs. 2).",
    3: "Voraussetzung: Erteilung mit denselben Ansprüchen für alle teilnehmenden Mitgliedstaaten (Abs. 1; R. 5 Abs. 2 DOEPS). Einheitlicher Charakter (Abs. 2): Beschränkung, Übertragung, Nichtigerklärung und Erlöschen nur für alle Staaten zugleich, Lizenzen auch für Teilgebiete.",
    4: "Wirksam am Tag der Bekanntmachung des Erteilungshinweises im Europäischen Patentblatt, also rückwirkend zur Eintragung. Abs. 2: Die Mitgliedstaaten sorgen dafür, dass das europäische Patent für sie nicht daneben als nationales Patent wirkt.",
    5: "Das materielle Recht (Verletzungshandlungen, Beschränkungen) steht nicht in der Verordnung, sondern über die Verweisung des Abs. 3 im nationalen Recht des Staates nach Art. 7 – und damit für alle Vertragsmitgliedstaaten in Art. 25 bis 30 EPGÜ.",
    6: "Unionsweite Erschöpfung; wortgleich mit Art. 29 EPGÜ.",
    7: "Kollisionsnorm für das Einheitspatent als Gegenstand des Vermögens: Recht des teilnehmenden Mitgliedstaats, in dem der Anmelder am Anmeldetag Wohnsitz oder Hauptniederlassung hatte, hilfsweise eine Niederlassung (R. 16 Abs. 1 lit. w DOEPS), sonst deutsches Recht (Abs. 3, Sitz der EPO).",
    8: "Lizenzbereitschaftserklärung gegenüber dem EPA; Vertragslizenz kraft Gesetzes (Abs. 2). Folge: 15 % Ermäßigung der Jahresgebühren (R. 12 DOEPS, Art. 3 GebOEPS); die angemessene Vergütung bestimmt das EPG (Art. 32 Abs. 1 lit. h EPGÜ).",
    9: "Aufgabenkatalog des EPA nach Art. 143 EPÜ: Anträge auf einheitliche Wirkung (lit. a, g), Register (lit. b), Lizenzbereitschaft (lit. c), Übersetzungen (lit. d), Jahresgebühren (lit. e, f), Kompensation (lit. f). Abs. 3: Klagen gegen EPA-Entscheidungen zum EPG (Art. 32 Abs. 1 lit. i EPGÜ).",
    11: "Eine einzige Jahresgebühr an das EPA, fällig ab dem Folgejahr des Erteilungshinweises; Zahlung ohne Vertreterzwang. Durchführung in R. 13 DOEPS.",
    12: "Grundsätze der Gebührenhöhe (progressiv, kostendeckend, KMU-freundlich); tatsächlich festgesetzt als Summe der vier validierungsstärksten Staaten von 2015 („True Top 4“) in Art. 2 GebOEPS.",
    13: "Das EPA behält 50 % der Jahresgebühren, der Rest wird nach einem Schlüssel des Engeren Ausschusses an die teilnehmenden Mitgliedstaaten verteilt.",
    18: "In Kraft seit 20.1.2013, anwendbar seit 1.6.2023 (Inkrafttreten des EPGÜ). Abs. 2: einheitliche Wirkung nur für Staaten, in denen das EPGÜ bei Eintragung in Kraft ist – Grundlage der „Generationen“ von Einheitspatenten (17 Staaten ab 1.6.2023, 18 mit Rumänien ab 1.9.2024).",
}
ENTSPRICHT_EPATVO = {
    2: ["Art. 2 EPGÜ"],
    3: ["Art. 3 EPGÜ"],
    5: ["Art. 25 EPGÜ", "Art. 26 EPGÜ", "Art. 27 EPGÜ"],
    6: ["Art. 29 EPGÜ"],
    8: ["Art. 32 EPGÜ"],
    9: ["Art. 32 EPGÜ", "Art. 66 EPGÜ"],
    18: ["Art. 89 EPGÜ"],
}
HINWEISE_UEBERSVO = {
    3: "Grundsatz: Nach Veröffentlichung der Patentschrift in der EPA-Verfahrenssprache (mit Ansprüchen in den beiden anderen Amtssprachen, Art. 14 Abs. 6 EPÜ) sind keine weiteren Übersetzungen erforderlich – sobald die Übergangszeit des Art. 6 abgelaufen ist.",
    4: "Übersetzung im Streitfall auf Kosten des Inhabers: auf Verlangen des mutmaßlichen Verletzers in eine Amtssprache des Verletzungs- oder Sitzstaats (Abs. 1), auf Anforderung des Gerichts in die Verfahrenssprache (Abs. 2). Abs. 4: gutgläubige KMU und natürliche Personen vor Erhalt der Übersetzung – zu berücksichtigen beim Schadensersatz (Art. 68 EPGÜ).",
    5: "Kompensation der Übersetzungskosten in der Anmeldephase für KMU, natürliche Personen, Organisationen ohne Gewinnerzielungsabsicht, Hochschulen und öffentliche Forschungseinrichtungen mit Sitz in der EU, die in einer anderen EU-Amtssprache als Deutsch, Englisch oder Französisch angemeldet haben; Pauschale 500 EUR (R. 8 bis 11 DOEPS, Art. 4 GebOEPS).",
    6: "Übergangszeit von sechs Jahren ab 1.6.2023, verlängerbar bis höchstens zwölf Jahre: Mit dem Antrag auf einheitliche Wirkung ist eine vollständige Übersetzung der Patentschrift einzureichen – ins Englische bei Verfahrenssprache Deutsch oder Französisch, in eine andere EU-Amtssprache bei Verfahrenssprache Englisch (R. 6 Abs. 2 lit. d DOEPS). Nur Information, keine Rechtswirkung (Abs. 2).",
}
ENTSPRICHT_UEBERSVO = {
    4: ["Art. 68 EPGÜ"],
}
HINWEISE_DOEPS = {
    1: "Gegenstand: Verfahren vor dem EPA nach beiden Verordnungen. Abs. 1: Das EPA ist bei Klagen gegen die Abteilung für den einheitlichen Patentschutz an die Entscheidungen des EPG gebunden.",
    3: "Grundlage der UP-Richtlinien: Der Präsident des EPA erlässt nach R. 3 DOEPS i.V.m. Art. 10 Abs. 2 lit. a EPÜ die Verwaltungsvorschriften für die Abteilung für den einheitlichen Patentschutz (UP-Richtlinien, Ausgabe April 2026).",
    4: "Die Abteilung für den einheitlichen Patentschutz ist eine eigene Abteilung des EPA; jede Entscheidung trifft ein rechtskundiges Mitglied (Abs. 3).",
    5: "Anspruchsberechtigung: Antrag durch den Inhaber (Abs. 1); Erteilung mit denselben Ansprüchen für alle 25 teilnehmenden Mitgliedstaaten (Abs. 2 lit. a) – deshalb keine einheitliche Wirkung bei zurückgenommener Benennung oder bei Anmeldungen vor dem 1.3.2007 (Beitritt Maltas). Abs. 2 lit. b (seit 15.11.2024): keine einheitliche Wirkung für sanktionierte Inhaber (14. EU-Sanktionspaket).",
    6: "Die Klausurnorm des Einheitspatents: Frist ein Monat ab Bekanntmachung des Erteilungshinweises, nicht verlängerbar, aber wiedereinsetzbar (R. 22 Abs. 2: zwei Monate ab Fristablauf). Schriftlich, in der Verfahrenssprache, Formblatt 7000; Inhalt nach Abs. 2 einschließlich der Übersetzung nach Art. 6 EPatÜVO. Ein früher Antrag nach der Erteilungsentscheidung ist möglich (Formblatt 2006A).",
    7: "Prüfung: Eintragung und Mitteilung des Eintragungstags (Abs. 1, Formblatt 7030); beabsichtigte Zurückweisung mit rechtlichem Gehör (Abs. 2, Art. 113 Abs. 1 EPÜ); Mängel nach R. 6 Abs. 2 binnen einer nicht verlängerbaren Monatsfrist behebbar (Abs. 3), für die es keine Wiedereinsetzung gibt (R. 22 Abs. 6; EPG-BerG Bodycap/EPA).",
    8: "Kompensation: Anmeldung in einer anderen EU-Amtssprache als Deutsch, Englisch, Französisch (Abs. 1); Berechtigte: KMU (Empfehlung 2003/361/EG), natürliche Personen, Organisationen ohne Gewinnerzielungsabsicht, Hochschulen, öffentliche Forschungseinrichtungen mit Sitz in der EU (Abs. 2); bei mehreren Inhabern oder Rechtsübergang müssen alle die Kriterien erfüllen (Abs. 3, 4); auch Euro-PCT-Anmeldungen (Abs. 5).",
    9: "Der Antrag auf Kompensation ist zusammen mit dem Antrag auf einheitliche Wirkung zu stellen (Kästchen im Formblatt 7000) und enthält eine Erklärung über den Status des Inhabers.",
    10: "Gewährung erst nach Eintragung der einheitlichen Wirkung (Abs. 1), danach unwiderruflich (Abs. 2). Bei Zweifeln Beweismittel (Abs. 3); bei unrichtiger Erklärung Rückzahlung plus Verwaltungsgebühr von 50 % (Abs. 4, Art. 4 Abs. 2 GebOEPS), sonst Erlöschen (R. 14).",
    11: "Pauschalbetrag nach Art. 4 Abs. 1 GebOEPS: 500 EUR; ausgezahlt wie eine Rückerstattung.",
    12: "Lizenzbereitschaft: Erklärung beim EPA (Formblatt 7001), gebührenfrei eingetragen; nicht möglich bei eingetragener ausschließlicher Lizenz (Abs. 3); danach keine ausschließliche Lizenz mehr eintragbar (Abs. 4). Rücknahme nur gegen Rückzahlung der gesamten Ermäßigung (Abs. 2).",
    13: "Jahresgebühren an das EPA, fällig am letzten Tag des Monats, der dem Anmeldemonat entspricht (Abs. 2, wie R. 51 Abs. 1 EPÜ); frühestens drei Monate vorher zahlbar; Nachfrist sechs Monate mit Zuschlag von 50 % (Abs. 3, Art. 2 Abs. 1 Nr. 2 GebOEPS), berechnet „von Ultimo zu Ultimo“. Abs. 4 und 5: dreimonatige Sicherheitsfrist ohne Zuschlag nach Zustellung der Eintragungsmitteilung; Gebühren zwischen Erteilung und Mitteilung werden erst mit der Mitteilung fällig.",
    14: "Erlöschen bei Nichtzahlung rückwirkend auf den Fälligkeitstag (Abs. 2); die Feststellung des Rechtsverlusts (R. 112 EPÜ) kann durch Entscheidung überprüft und diese vor dem EPG angefochten werden. Wiedereinsetzung nach R. 22 möglich (ein Jahr ab Ende der Nachfrist).",
    15: "Das Register für den einheitlichen Patentschutz ist gesonderter, aber integrierter Teil des Europäischen Patentregisters (Art. 127 EPÜ); Einheitspatente tragen dort den Code „C0“.",
    16: "Registerinhalt: unter anderem Eintragungstag der einheitlichen Wirkung, territorialer Geltungsbereich (lit. g), Rechtsübergänge und Lizenzen (lit. j), Lizenzzusagen gegenüber Normungsgremien (lit. k), Unterbrechung (lit. u) und die freiwillige Angabe der Niederlassung am Anmeldetag für Art. 7 EPatVO (lit. w).",
    17: "Eigener Teil des Europäischen Patentblatts für Einheitspatente (Abs. 1); Beschlüsse und Mitteilungen zum Einheitspatent im Amtsblatt des EPA (Abs. 2).",
    18: "Das EPA veröffentlicht die nach Art. 6 EPatÜVO eingereichten Übersetzungen – ohne inhaltliche Prüfung, weil sie keine Rechtswirkung haben.",
    20: "Generalverweisung auf das EPÜ: Vertretung (Art. 133, 134 EPÜ), rechtliches Gehör (Art. 113 EPÜ), Zustellung (R. 125 ff. EPÜ), Fristenberechnung (R. 131, 134 EPÜ), Unterbrechung (R. 142 EPÜ), Rechtsübergänge und Lizenzen (R. 22 bis 24 EPÜ). Abs. 4: Fristen der Abteilung zwischen einem und vier Monaten, nicht verlängerbar; keine Weiterbehandlung (R. 135 EPÜ).",
    21: "Mündliche Verhandlung auf Antrag oder von Amts wegen (Abs. 1), im Verfahren über den Antrag auf einheitliche Wirkung nur auf Antrag des Inhabers und bei Sachdienlichkeit (Abs. 2); nicht öffentlich (Abs. 3).",
    22: "Wiedereinsetzung (Maßstab: alle gebotene Sorgfalt, Rechtsprechung zu Art. 122 EPÜ): für die Frist des R. 6 Abs. 1 binnen zwei Monaten ab Fristablauf ohne Rücksicht auf den Wegfall des Hindernisses (Abs. 2), sonst zwei Monate ab Wegfall, höchstens ein Jahr; Gebühr nach Art. 2 Abs. 2 GebOEPS. Ausgeschlossen für die Wiedereinsetzungsfrist selbst und die Mängelfrist des R. 7 Abs. 3 (Abs. 6).",
    23: "Rechtsbehelf: Klage vor dem EPG gegen Entscheidungen der Abteilung für den einheitlichen Patentschutz (Art. 32 Abs. 1 lit. i, Art. 66 EPGÜ) – zwei Monate nach R. 88 VerfO, bei Zurückweisung des Antrags auf einheitliche Wirkung drei Wochen nach R. 97 VerfO (beschleunigtes Verfahren vor dem Eilrichter).",
    24: "Abhilfe durch das EPA binnen zwei Monaten, wenn das EPG die Klage für zulässig hält (R. 91 VerfO) – nicht im Verfahren nach R. 97 VerfO, das als lex specialis keine Abhilfe kennt (R. 85 Abs. 2 VerfO; EPG-BerG Bodycap/EPA).",
}
BEZUG_DOEPS = {
    1: ["Art. 9 EPatVO"], 2: ["Art. 9 EPatVO"], 4: ["Art. 9 EPatVO"],
    5: ["Art. 3 EPatVO", "Art. 9 EPatVO"], 6: ["Art. 9 EPatVO", "Art. 6 EPatÜVO"], 7: ["Art. 4 EPatVO", "Art. 9 EPatVO"],
    8: ["Art. 5 EPatÜVO"], 9: ["Art. 5 EPatÜVO"], 10: ["Art. 5 EPatÜVO"], 11: ["Art. 5 EPatÜVO"],
    12: ["Art. 8 EPatVO"], 13: ["Art. 11 EPatVO", "Art. 12 EPatVO"], 14: ["Art. 3 EPatVO", "Art. 9 EPatVO"],
    15: ["Art. 2 EPatVO", "Art. 9 EPatVO"], 16: ["Art. 9 EPatVO", "Art. 7 EPatVO"], 17: ["Art. 9 EPatVO"], 18: ["Art. 6 EPatÜVO", "Art. 9 EPatVO"],
    19: ["Art. 9 EPatVO"], 20: ["Art. 9 EPatVO"], 22: ["Art. 9 EPatVO"],
    23: ["Art. 9 EPatVO", "Art. 32 EPGÜ", "Art. 66 EPGÜ", "R. 88 VerfO", "R. 97 VerfO"], 24: ["Art. 66 EPGÜ", "R. 91 VerfO"],
}
HINWEISE_GEBOEPS = {
    1: "Die GebOEPS regelt nur die Gebühren des Einheitspatentverfahrens; für die Zahlung gilt im Übrigen die Gebührenordnung zum EPÜ (Art. 6).",
    2: "Die Gebührentabelle: Jahresgebühren vom 2. Jahr (35 EUR) bis zum 20. Jahr (4 855 EUR), zusammen 35 555 EUR über die volle Laufzeit („True Top 4“: Summe der Jahresgebühren der vier 2015 validierungsstärksten Staaten); Zuschlagsgebühr 50 % (Abs. 1 Nr. 2); Wiedereinsetzungsgebühr (Abs. 2). Maßgeblich ist der am Zahlungstag geltende Betrag.",
    3: "Ermäßigung um 15 % bei Lizenzbereitschaftserklärung (R. 12 DOEPS); der Zuschlag bei verspäteter Zahlung wird aus der ermäßigten Gebühr berechnet.",
    4: "Kompensation von Übersetzungskosten: Pauschale 500 EUR (Abs. 1); bei unrichtiger Erklärung Rückzahlung zuzüglich Verwaltungsgebühr von 50 % (Abs. 2, R. 10 Abs. 4 DOEPS).",
    5: "Vom Präsidenten festgesetzte Gebühren, etwa für die Eintragung von Rechtsübergängen und Lizenzen (entfällt bei Antrag über MyEPO).",
    6: "Verweisung auf die Gebührenordnung zum EPÜ: Zahlungsarten, Fälligkeit, laufendes Konto; Jahresgebühren kann jedermann ohne Vertreter wirksam zahlen.",
    7: "Überprüfung der Jahresgebührenhöhe durch den Engeren Ausschuss und Bericht über KMU und andere begünstigte Einheiten.",
}
BEZUG_GEBOEPS = {
    2: ["R. 13 DOEPS", "R. 22 DOEPS", "Art. 11 EPatVO", "Art. 12 EPatVO"],
    3: ["R. 12 DOEPS", "Art. 8 EPatVO"],
    4: ["R. 10 DOEPS", "R. 11 DOEPS", "Art. 5 EPatÜVO"],
    5: ["R. 20 DOEPS"], 6: ["R. 20 DOEPS"], 7: ["Art. 12 EPatVO", "Art. 16 EPatVO"],
}

_FAM = [
    dict(key="epatvo", datei="up_epatvo.json", kurz="EPatVO", aliase=(), zitat="Art.", hinweise=HINWEISE_EPATVO, entspricht=ENTSPRICHT_EPATVO, bezug={},
         titel="Verordnung (EU) Nr. 1257/2012 über das Einheitspatent (EPatVO)", gesetz="Verordnung (EU) Nr. 1257/2012 (EPatVO)",
         url_pdf="https://www.epo.org/xx/legal/up-upc/2022/de/eu20121257_20221201_de.pdf", celex="https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1257",
         hinweis="Amtlicher deutscher Wortlaut der Verordnung (EU) Nr. 1257/2012 (epo.org, Rechtstexte zum Einheitspatentsystem); englische Fassung je Artikel verlinkt."),
    dict(key="epatuevo", datei="up_epatuevo.json", kurz="EPatÜVO", aliase=("EPatÜbersVO",), zitat="Art.", hinweise=HINWEISE_UEBERSVO, entspricht=ENTSPRICHT_UEBERSVO, bezug={},
         titel="Verordnung (EU) Nr. 1260/2012 über die Übersetzungsregelungen (EPatÜVO)", gesetz="Verordnung (EU) Nr. 1260/2012 (EPatÜVO)",
         url_pdf="https://www.epo.org/xx/legal/up-upc/2022/de/eu20121260_20221201_de.pdf", celex="https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1260",
         hinweis="Amtlicher deutscher Wortlaut der Verordnung (EU) Nr. 1260/2012 (epo.org); englische Fassung je Artikel verlinkt."),
    dict(key="doeps", datei="up_doeps.json", kurz="DOEPS", aliase=("UPR",), zitat="R.", hinweise=HINWEISE_DOEPS, entspricht={}, bezug=BEZUG_DOEPS,
         titel="Durchführungsordnung zum einheitlichen Patentschutz (DOEPS)", gesetz="DOEPS (Beschluss des Engeren Ausschusses SC/D 1/15, zuletzt geändert 9.10.2025)",
         url_pdf="https://www.epo.org/xx/legal/up-upc/2022/de/up_rules_2022_20221201_de.pdf", celex=None,
         hinweis="Deutscher Wortlaut der Durchführungsordnung zum einheitlichen Patentschutz (epo.org, fortlaufend aktualisierte HTML-Sammlung); englische Regeltitel hinterlegt."),
    dict(key="gebeps", datei="up_gebeps.json", kurz="GebOEPS", aliase=("GebEPS", "RFeesUPP"), zitat="Art.", hinweise=HINWEISE_GEBOEPS, entspricht={}, bezug=BEZUG_GEBOEPS,
         titel="Gebührenordnung zum einheitlichen Patentschutz (GebOEPS)", gesetz="GebOEPS (Beschluss des Engeren Ausschusses SC/D 2/15, zuletzt geändert 9.10.2025)",
         url_pdf="https://www.epo.org/xx/legal/up-upc/2022/de/up_fees_2022_20221201_de.pdf", celex=None,
         hinweis="Deutscher Wortlaut der Gebührenordnung zum einheitlichen Patentschutz (epo.org); Jahresgebührentabelle in Art. 2."),
]


def _absaetze(raw):
    out = []
    for a in raw:
        nr, text = None, a
        if a.startswith("(") and ")" in a[:5]:
            nr, text = a[1:a.index(")")], a[a.index(")") + 1:].strip()
        out.append(dict(nr=nr, text=text))
    return out


FAMILIEN = []
META = {}
for _f in _FAM:
    _j = json.loads((_DATA / _f["datei"]).read_text(encoding="utf-8"))
    META[_f["key"]] = _j["meta"]
    arts = []
    for _a in _j["artikel"]:
        kapitel = schoen(_a["teil"]) if _a["teil"] else (schoen(_a["kapitel"]) if _a["kapitel"] else "Allgemeines")
        abschnitt = schoen(_a["kapitel"]) if _a["teil"] and _a["kapitel"] else None
        arts.append(dict(
            nr=str(_a["nr"]), titel=_a["titel"], titel_en=_a["titel_en"], kapitel=kapitel, abschnitt=abschnitt,
            absaetze=_absaetze(_a["absaetze"]), absaetze_en=_absaetze(_a["absaetze_en"]),
            umsetzung=[], umsetzung_weitere={}, concepts=[], cases=[],
            entspricht=_f["entspricht"].get(_a["nr"], []), bezug=_f["bezug"].get(_a["nr"], []),
            hinweis=_f["hinweise"].get(_a["nr"], ""), url=_a["url"], url_en=_a["url_en"],
        ))
    FAMILIEN.append(dict(key=_f["key"], kurz=_f["kurz"], aliase=_f["aliase"], titel=_f["titel"], gesetz=_f["gesetz"], artikel=arts,
                         erwaegungsgruende=[], url=_j["meta"]["quelle"], url_pdf=_f["url_pdf"], celex=_f["celex"], paraphrase=False,
                         zitat=_f["zitat"], hinweis=_f["hinweis"]))

# ------------------------------------------------------------------ UP-Richtlinien (Ausgabe April 2026) und EPA-Informationsseiten als Quellen
_RL_JSON = json.loads((_DATA / "up_richtlinien.json").read_text(encoding="utf-8"))
RL_META = _RL_JSON["meta"]
_RL_BY_ID = {a["id"]: a for a in _RL_JSON["abschnitte"]}


def _rl(page, nr, title, summary):
    """Kuratierte Zusammenfassung eines Abschnitts; URL und englischer Titel aus den Daten."""
    sec = page.split(":")[1].replace(".", "_")
    a = _RL_BY_ID.get(sec, {})
    return dict(page=page, title="UP-Richtlinien %s %s" % (nr, title), title_en=a.get("titel_en", ""), summary=summary,
                url=a.get("url") or UP_RL_URL + "section_%s.html" % sec, provider="UP-Richtlinien")


def _kurz(text, n=260):
    text = text.strip()
    if len(text) <= n:
        return text
    cut = text[:n]
    return cut[:max(cut.rfind(". "), cut.rfind("; "), n - 60) + 1].strip() + " …"


UP_RICHTLINIEN = [
    _rl("uprl:1", "Teil 1:", "Allgemeines", "Rechtsrahmen (EPatVO, EPatÜVO, DOEPS, GebOEPS), Rolle des EPG, territorialer Geltungsbereich und Generationen von Einheitspatenten, Abteilung für den einheitlichen Patentschutz."),
    _rl("uprl:1.5", "1.5:", "Territorialer Geltungsbereich des Einheitspatents", "17 Staaten ab 1.6.2023, 18 mit Rumänien ab 1.9.2024; der Geltungsbereich einer Generation bleibt für die gesamte Laufzeit gleich; Verschiebung der Eintragung bei bevorstehendem Beitritt (ABl. EPA 2024, A61)."),
    _rl("uprl:2", "Teil 2:", "Der Antrag auf einheitliche Wirkung", "Anspruchsberechtigung nach R. 5 Abs. 2 DOEPS, Form und Monatsfrist, Antragsteller, Angaben, Sprache, Unterschrift, Übersetzung, Prüfung, Eintragung, Zurückweisung und Zurücknahme."),
    _rl("uprl:2.4", "2.4:", "Prüfung des Antrags auf einheitliche Wirkung", "Eintragung bei erfüllten Erfordernissen; Mängel nach R. 6 Abs. 2 DOEPS binnen nicht verlängerbarer Monatsfrist ohne Wiedereinsetzung; beabsichtigte Zurückweisung mit Gelegenheit zur Stellungnahme."),
    _rl("uprl:3", "Teil 3:", "Gebühren", "Gebührenarten der GebOEPS, Zahlungsarten, Fälligkeit der Jahresgebühren, frühe Zahlung, sechsmonatige Nachfrist mit 50 % Zuschlag, Erlöschen, dreimonatige Sicherheitsfrist nach R. 13 Abs. 4 DOEPS."),
    _rl("uprl:3.10", "3.10:", "Zusätzliche Frist von sechs Monaten für die Entrichtung der Jahresgebühren", "Nachfrist mit Zuschlag von 50 % (Art. 2 Abs. 1 Nr. 2 GebOEPS); Berechnung von Ultimo zu Ultimo; Erinnerung des EPA nur als Service."),
    _rl("uprl:4", "Teil 4:", "Kompensationssystem", "Anspruchskriterien (Sitz in der EU, Kategorien nach R. 8 Abs. 2 DOEPS, Anmeldesprache), Antrag zusammen mit dem Antrag auf einheitliche Wirkung, Prüfung, Zurückweisung, Zweifel an der Erklärung."),
    _rl("uprl:5", "Teil 5:", "Wiedereinsetzung in den vorigen Stand", "Anwendungsbereich (verspäteter Antrag auf einheitliche Wirkung, Jahresgebühren), Zulässigkeit (Fristen des R. 22 DOEPS), Begründetheit (alle gebotene Sorgfalt), Entscheidung."),
    _rl("uprl:6", "Teil 6:", "Unterbrechung und Wiederaufnahme des Verfahrens; Aussetzung des Eintragungsverfahrens", "R. 20 Abs. 2 lit. i DOEPS i.V.m. R. 142 EPÜ; Aussetzung durch den Präsidenten nach R. 3 DOEPS (Beispiel: EU-Sanktionspaket 2024)."),
    _rl("uprl:7", "Teil 7:", "Eintragung von Namens- und Adressänderungen, Rechtsübergängen, Lizenzen und anderen Rechten", "Übertragung nur für alle Staaten, Lizenzen auch für Teilgebiete, ausschließliche Lizenz und Lizenzbereitschaft, Lizenzzusagen gegenüber Normungsgremien, Erfinderdaten."),
    _rl("uprl:7.5", "7.5:", "Erklärung über die Lizenzbereitschaft", "Formblatt 7001, gebührenfrei; 15 % Ermäßigung der Jahresgebühren; ausgeschlossen bei eingetragener ausschließlicher Lizenz; Zurücknahme nur gegen Rückzahlung der Ermäßigung."),
    _rl("uprl:8", "Teil 8:", "Verfahren vor der Abteilung für den einheitlichen Patentschutz", "Einreichung, Vertretung (EPÜ-Regeln), Unterschrift, Sprachen, Zustellung, Fristen (ein bis vier Monate, nicht verlängerbar), mündliche Verhandlung, Register und Akteneinsicht, Rechtsmittel."),
    _rl("uprl:8.9", "8.9:", "Rechtsmittel", "Klage vor dem EPG nach R. 23 DOEPS: zwei Monate (R. 88 VerfO), bei Zurückweisung des Antrags auf einheitliche Wirkung drei Wochen (R. 97 VerfO); Abhilfe nach R. 24 DOEPS nur außerhalb des R.-97-Verfahrens (UPC_CoA_796/2025)."),
]
# Übrige Abschnitte bis zur zweiten Ebene (1.1, 2.3, 3.7 …) mit dem Anfang des Richtlinientexts als Zusammenfassung; Sachregister (Teil 9) nicht
_kuratiert = {w["page"] for w in UP_RICHTLINIEN}
for _a in _RL_JSON["abschnitte"]:
    if _a["id"].count("_") > 1 or _a["id"].startswith("9") or ("uprl:" + _a["id"].replace("_", ".")) in _kuratiert:
        continue
    _nr = _a["nr"].rstrip(".")
    UP_RICHTLINIEN.append(dict(page="uprl:" + _a["id"].replace("_", "."), title="UP-Richtlinien %s %s" % (("Teil %s:" % _nr) if "." not in _nr else _nr + ":", _a["titel"]),
                               title_en=_a["titel_en"], summary=_kurz(_a["text"]) or _a["titel"], url=_a["url"], provider="UP-Richtlinien"))
UP_RICHTLINIEN.sort(key=lambda w: [int(x) for x in w["page"].split(":")[1].split(".")])
# EPA-Informationsseiten (epo.org/de/applying/european/unitary/unitary-patent/*)
UP_INFO = [dict(page="upinfo:" + i["id"], title="EPA: " + i["titel"], title_en=i["titel_en"], summary=_kurz(i["text"], 300), url=i["url"], provider="epo.org Einheitspatent")
           for i in _RL_JSON["info"] if i["id"] != "introductory-brochures"]
QUELLEN = UP_RICHTLINIEN + UP_INFO
