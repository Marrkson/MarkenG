# -*- coding: utf-8 -*-
"""Übereinkommen über ein Einheitliches Patentgericht (EPGÜ, engl. UPCA), ABl. C 175 vom 20.6.2013, S. 1.

Wortlaut aus data/upca.json (deutsche und englische Fassung, epo.org). Hier nur die Anreicherung:
`entspricht` verknüpft Artikel mit den Vorschriften der Durchsetzungsrichtlinie 2004/48/EG, die sie
für das EPG umsetzen (Kante `entspricht`, Tabelle ENTSPRECHUNG_DISTINCTION); `hinweis` trägt den
Lern-/Klausurhinweis. Begriffe und Entscheidungen hängen über ihre eigenen `norms`-Felder am Artikel.
"""
import json
from pathlib import Path

from ..gesetze import qualify

_KLEIN = {"und", "der", "des", "die", "das", "oder", "zur", "zum", "von", "vor", "dem", "den", "mit", "bei", "im", "in", "an", "auf", "für", "durch", "nach", "über", "aus", "als", "ohne", "eines", "einer", "sowie"}
_GROSS = {"epgü", "epg", "epa", "epü", "eu", "esz", "cms"}


def schoen(s):
    """'KAPITEL VI – INTERNATIONALE UND SONSTIGE ZUSTÄNDIGKEIT' -> 'Kapitel VI – Internationale und sonstige Zuständigkeit'
    (Überschriften der Quelltexte sind in Versalien; für Listen und Kärtchen lesbarer)."""
    out, satzanfang = [], True
    for w in s.split(" "):
        lw = w.lower()
        if not w:
            continue
        if w in ("–", "-"):
            out.append(w); satzanfang = True
            continue
        if lw.rstrip(".,") in _GROSS or all(c in "ivxlc" for c in lw):
            out.append(w.upper())
        elif not satzanfang and lw in _KLEIN:
            out.append(lw)
        elif not satzanfang and lw in {"sonstige", "allgemeine", "internationale", "institutionelle", "vorläufige", "gemeinsame", "besondere", "schriftliches", "mündliches", "elektronische", "erster", "sonstiger", "einstweilige"}:
            out.append(lw)  # Adjektive in der Mitte klein (Deutsch), Substantive bleiben groß
        else:
            out.append(w[:1].upper() + w[1:].lower())
        satzanfang = False
    return " ".join(out)

KURZ = "EPGÜ"
ALIASE = ("UPCA",)
TITEL = "Übereinkommen über ein Einheitliches Patentgericht (EPGÜ)"
GESETZ = "EPGÜ (ABl. C 175/1 vom 20.6.2013)"
URL = "https://www.epo.org/de/legal/up-upc/2022/upca.html"
URL_PDF = "https://www.epo.org/xx/legal/up-upc/2022/de/upc_agreement_2022_20221201_de.pdf"
CELEX_URL = "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:42013A0620(01)"

_DATA = Path(__file__).resolve().parents[3] / "data" / "upca.json"

# EPGÜ-Artikel -> Artikel der Durchsetzungsrichtlinie, den er für das EPG umsetzt
ENTSPRICHT = {
    42: ["Art. 3 DurchsetzungsRL"],
    47: ["Art. 4 DurchsetzungsRL"],
    58: ["Art. 6 DurchsetzungsRL"],
    59: ["Art. 6 DurchsetzungsRL"],
    60: ["Art. 7 DurchsetzungsRL"],
    61: ["Art. 9 DurchsetzungsRL"],
    62: ["Art. 9 DurchsetzungsRL"],
    63: ["Art. 11 DurchsetzungsRL"],
    64: ["Art. 10 DurchsetzungsRL"],
    67: ["Art. 8 DurchsetzungsRL"],
    68: ["Art. 13 DurchsetzungsRL"],
    69: ["Art. 14 DurchsetzungsRL"],
    80: ["Art. 15 DurchsetzungsRL"],
}

HINWEISE = {
    1: "Das EPG ist ein gemeinsames Gericht der Vertragsmitgliedstaaten, kein Unionsorgan; es unterliegt aber denselben unionsrechtlichen Pflichten wie nationale Gerichte (Art. 20 bis 23).",
    2: "Begriffe merken: „Vertragsmitgliedstaat“ (nur EU-Staaten, die das EPGÜ ratifiziert haben), „europäisches Patent mit einheitlicher Wirkung“ und „europäisches Patent“ (Bündelpatent, soweit nicht opt-out).",
    3: "Sachlicher Geltungsbereich: Einheitspatente, ESZ, europäische Bündelpatente (auch vor dem 1.6.2023 erteilte) und Anmeldungen – jeweils ohne Opt-out (Art. 83 Abs. 3).",
    7: "Gericht erster Instanz = Zentralkammer (Sitz Paris; Abteilungen München und Mailand) + Lokal- und Regionalkammern. Zuweisung der Nichtigkeitsklagen nach IPC-Klassen (Anhang II).",
    8: "Multinationale Besetzung: Lokalkammer drei rechtlich qualifizierte Richter; technisch qualifizierter Richter auf Antrag oder bei Widerklage auf Nichtigerklärung (Abs. 5) aus dem Richterpool (Art. 18).",
    24: "Rechtsquellen in Rangfolge: Unionsrecht, EPGÜ, EPÜ, sonstige internationale Übereinkünfte, nationales Recht (über Abs. 2 bestimmt nach Rom II/EU-Recht).",
    25: "Verletzungshandlungen entsprechen § 9 PatG; das EPG legt die Begriffe („Anbieten“) autonom aus (EPG-BerG Belkin/Philips).",
    26: "Mittelbare Verletzung wie § 10 PatG; Verwendungsbestimmung aus objektiven Umständen (EPG-BerG Onward/Niche).",
    27: "Schrankenkatalog inkl. Bolar (lit. d), Landwirteprivileg, Schiffe/Luftfahrzeuge, Dekompilierung, Züchtung (lit. c).",
    28: "Vorbenutzungsrecht besteht nur nach dem jeweiligen nationalen Recht und nur für dessen Gebiet.",
    31: "Internationale Zuständigkeit richtet sich nach Brüssel-Ia-VO (Art. 71a bis 71d) bzw. Lugano-Übereinkommen; das EPG ist „Gericht eines Mitgliedstaats“.",
    32: "Abschließender Katalog der ausschließlichen Zuständigkeiten; alles andere bleibt bei nationalen Gerichten (Abs. 2).",
    33: "Die Klausurnorm: Verletzungsort oder Beklagtensitz (Abs. 1), Sperre paralleler Klagen (Abs. 2), drei Optionen bei Widerklage auf Nichtigerklärung (Abs. 3), Nichtigkeitsklage zur Zentralkammer (Abs. 4), Aussetzung bei EPA-Verfahren (Abs. 10).",
    34: "Entscheidungen wirken für das Gebiet aller Vertragsmitgliedstaaten, für die das Patent Wirkung hat.",
    42: "Verhältnismäßigkeit und Fairness als Leitprinzipien; Umsetzung von Art. 3 DurchsetzungsRL.",
    47: "Parteifähigkeit/Klagebefugnis: Inhaber, ausschließlicher Lizenznehmer (Abs. 2), einfacher Lizenznehmer nur mit Zustimmung (Abs. 3); Nichtigkeitsklage kann „jede Person“ erheben (Abs. 6).",
    48: "Vertretung durch Anwälte oder europäische Patentanwälte mit EPLC; kein Vertretungszwang für Entscheidungsträger der Partei (EPG-BerG Suinno/Microsoft).",
    49: "Verfahrenssprache erster Instanz: Amtssprache der Kammer (Abs. 1), zusätzlich bestimmte EPA-Sprachen (Abs. 2), auf Vereinbarung oder Antrag die Patentsprache (Abs. 3 bis 5).",
    52: "Drei Verfahrensabschnitte: schriftliches Verfahren, Zwischenverfahren, mündliches Verfahren.",
    54: "Beweislast trägt, wer sich auf Tatsachen beruft; Ausnahme Art. 55 (Verfahrenspatent, Beweislastumkehr).",
    56: "Allgemeine Befugnisse: Anordnungen unter Bedingungen, Sicherheitsleistung, rechtliches Gehör vor Anordnungen zu Lasten einer Partei.",
    58: "Schutz vertraulicher Informationen; konkretisiert in R. 262A VerfO (Vertraulichkeitskreis, mindestens eine natürliche Person je Partei).",
    59: "Anordnung der Beweisvorlage („discovery light“); konkretisiert in R. 190 VerfO; keine Ausforschung.",
    60: "Beweissicherung und Besichtigung („saisie“): R. 192 bis 199 VerfO; auch ex parte; Sicherheitsleistung und Schadensersatz bei Aufhebung (Abs. 8).",
    62: "Einstweilige Maßnahmen: „hinreichende Sicherheit“ (Abs. 4, R. 211.2 VerfO), Interessenabwägung, Dringlichkeit (R. 211.4), Sicherheitsleistung, Schadensersatz bei Aufhebung (Abs. 5).",
    63: "Unterlassungsanordnung gegen Verletzer und Mittelspersonen; Zwangsgeld; nicht auf bereits begangene Handlungen beschränkt (EPG-BerG Dyson/Dreame).",
    65: "Nichtigkeitsgründe nur nach Art. 138 Abs. 1 und Art. 139 Abs. 2 EPÜ; teilweise Nichtigerklärung (Abs. 3); Wirkung ex tunc (Abs. 4).",
    68: "Schadensersatz nur bei Verschulden (wusste oder hätte wissen müssen); Berechnung: Schaden, Verletzergewinn oder Lizenzanalogie (Abs. 3); kein Strafschadensersatz (Abs. 2).",
    69: "Kosten trägt die unterliegende Partei bis zur Obergrenze; Prozesskostensicherheit nur gegen den Antragsteller (Abs. 4, EPG-BerG Hefei/Grundfos).",
    73: "Berufung gegen Endentscheidungen (Abs. 1, zwei Monate) und bestimmte Anordnungen (Abs. 2 lit. a, 15 Tage); sonstige Anordnungen nur mit Zulassung (Abs. 2 lit. b).",
    74: "Berufung hat grundsätzlich keine aufschiebende Wirkung (Ausnahme: Nichtigkeitsklage); Anordnung auf Antrag nach R. 223 VerfO.",
    76: "Dispositionsmaxime (Abs. 1) und Beibringungsgrundsatz (Abs. 2): Das Gericht entscheidet nur über die gestellten Anträge und nur auf Grundlage des Parteivorbringens.",
    82: "Vollstreckung nach dem Recht des Vollstreckungsstaats, Anordnung des Gerichts gilt als vollstreckbarer Titel; Zwangsgeld an das Gericht (Abs. 4).",
    83: "Übergangszeit sieben Jahre (verlängerbar): Wahlrecht für nationale Gerichte (Abs. 1) und Opt-out (Abs. 3), Rücknahme des Opt-out (Abs. 4).",
    89: "Inkrafttreten am 1. Juni 2023 (nach Ratifikation durch Deutschland); Voraussetzung: 13 Staaten inkl. der drei mit den meisten EP-Wirkungen im Jahr vor der Unterzeichnung.",
}


def _load():
    return json.loads(_DATA.read_text(encoding="utf-8"))


def _absaetze(raw):
    out = []
    for a in raw:
        nr = None
        text = a
        if a.startswith("(") and ")" in a[:5]:
            nr, text = a[1:a.index(")")], a[a.index(")") + 1:].strip()
        out.append(dict(nr=nr, text=text))
    return out


_JSON = _load()
META = _JSON["meta"]
ARTIKEL = []
for _a in _JSON["artikel"]:
    ARTIKEL.append(dict(
        nr=str(_a["nr"]), titel=_a["titel"], titel_en=_a["titel_en"],
        kapitel=schoen(_a["teil"]),
        abschnitt=(schoen(_a["kapitel"]) if _a["kapitel"] else None),
        absaetze=_absaetze(_a["absaetze"]), absaetze_en=_absaetze(_a["absaetze_en"]),
        umsetzung=[], umsetzung_weitere={}, concepts=[], cases=[],
        entspricht=ENTSPRICHT.get(_a["nr"], []), hinweis=HINWEISE.get(_a["nr"], ""), url=_a["url"], url_en=_a["url_en"],
    ))
ERWAEGUNGSGRUENDE = []

# Entsprechungstabelle EPGÜ <-> Durchsetzungsrichtlinie <-> deutsche Umsetzung (Anzeige in Kurs 10 und Navigator)
ENTSPRECHUNG_DISTINCTION = dict(
    id="d_upc_entsprechung_durchsetzungsrl",
    label="Durchsetzungsrichtlinie: Umsetzung im EPGÜ, in der VerfO und im deutschen Recht",
    concepts=["upc_durchsetzungsrl_bezug", "upc_einstweilige_massnahmen", "upc_beweissicherung", "upc_schadensersatz"],
    frage="Welche Vorschrift des EPGÜ und der VerfO entspricht welchem Artikel der Durchsetzungsrichtlinie 2004/48/EG, und wo steht die deutsche Umsetzung?",
    kriterien=[
        "Art. 3 – Allgemeine Verpflichtung (fair, verhältnismäßig, abschreckend)",
        "Art. 4 – Antragsbefugte (Inhaber, Lizenznehmer)",
        "Art. 6 – Beweise / Vorlage von Beweismitteln",
        "Art. 7 – Maßnahmen zur Beweissicherung",
        "Art. 8 – Recht auf Auskunft",
        "Art. 9 – Einstweilige Maßnahmen und Sicherungsmaßnahmen",
        "Art. 10 – Abhilfemaßnahmen (Rückruf, Entfernung, Vernichtung)",
        "Art. 11 – Gerichtliche Anordnungen (Unterlassung, Mittelspersonen)",
        "Art. 13 – Schadensersatz",
        "Art. 14 – Prozesskosten",
        "Art. 15 – Veröffentlichung von Gerichtsentscheidungen",
    ],
    spalten=["EPGÜ", "VerfO", "MarkenG", "PatG"],
    rows=[
        ["Art. 42 EPGÜ (Verhältnismäßigkeit und Fairness); Präambel VerfO Nr. 2 bis 5", "R. 1 VerfO", "§ 19c MarkenG (Verhältnismäßigkeit) und allgemeine Grundsätze", qualify("§ 140a Abs. 4, § 140b Abs. 4, § 139 Abs. 1 S. 3", "PatG")],
        ["Art. 47 EPGÜ (Parteien: Inhaber, ausschließlicher Lizenznehmer, einfacher Lizenznehmer mit Zustimmung)", "R. 13.1(g) VerfO", "§ 30 Abs. 3 MarkenG", qualify("§ 15 Abs. 2, § 139", "PatG")],
        ["Art. 59 EPGÜ (Anordnung der Beweisvorlage), Art. 58 EPGÜ (Vertraulichkeit)", "R. 190 VerfO, R. 262A VerfO", "§ 19a MarkenG", qualify("§ 140c", "PatG")],
        ["Art. 60 EPGÜ (Beweissicherung, Besichtigung, Arrest)", "R. 192 bis 199 VerfO", "§ 19a MarkenG i.V.m. §§ 485 ff. ZPO", qualify("§ 140c", "PatG") + " i.V.m. §§ 485 ff. ZPO"],
        ["Art. 67 EPGÜ (Anordnung zur Auskunftserteilung)", "R. 191 VerfO", "§ 19 MarkenG", qualify("§ 140b", "PatG")],
        ["Art. 62 EPGÜ (einstweilige Maßnahmen), Art. 61 EPGÜ (Arrest, Kontensperre)", "R. 205 bis 213 VerfO", "§§ 935 ff. ZPO, § 19 Abs. 7 MarkenG", "§§ 935 ff. ZPO, " + qualify("§ 140b Abs. 7", "PatG")],
        ["Art. 64 EPGÜ (Abhilfemaßnahmen)", "R. 118 VerfO", "§ 18 MarkenG", qualify("§ 140a", "PatG")],
        ["Art. 63 EPGÜ (Unterlassungsanordnung, Zwangsgeld)", "R. 118, R. 354 VerfO", "§ 14 Abs. 5 MarkenG, § 890 ZPO", qualify("§ 139 Abs. 1", "PatG") + ", § 890 ZPO"],
        ["Art. 68 EPGÜ (Schadensersatz, drei Berechnungsarten)", "R. 118.1, R. 125 bis 131 VerfO", "§ 14 Abs. 6 MarkenG", qualify("§ 139 Abs. 2", "PatG")],
        ["Art. 69 EPGÜ (Kosten, Obergrenzen, Prozesskostensicherheit)", "R. 150 bis 158, R. 370 VerfO", "§§ 91 ff. ZPO, § 142 MarkenG (Streitwertbegünstigung)", "§§ 91 ff. ZPO, " + qualify("§ 144", "PatG")],
        ["Art. 80 EPGÜ (Veröffentlichung der Entscheidung)", "R. 118.1 VerfO", "§ 19c MarkenG", qualify("§ 140e", "PatG")],
    ],
    merksatz="Die Durchsetzungsrichtlinie ist der gemeinsame Nenner: Was im MarkenG die §§ 18 bis 19c und im PatG die §§ 140a bis 140e regeln, steht für das EPG in Art. 56 bis 69 und 80 EPGÜ.",
)
