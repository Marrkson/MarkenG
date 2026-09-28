# -*- coding: utf-8 -*-
"""Verlinkung von Gesetzeszitaten auf gesetze-im-internet.de.

Erkennt Zitate wie „§ 14 Abs. 2 Nr. 2 MarkenG“, „§§ 9 bis 13“, „§§ 23/24“,
„§ 242 BGB“, „Art. 5 Abs. 3 GG“ oder die Langform der Gesetzestexte
(„§ 125 des Patentgesetzes“, „§ 91 der Zivilprozessordnung“) und hängt einen Link an.

Welches Gesetz gilt, wenn ein Zitat keine Gesetzesangabe trägt:
  1. Ketten: „§ 4, § 1 Nr. 4 DesignG“ oder „§ 81 Absatz 6 und § 125 des Patentgesetzes“ – Zitate, die nur durch
     „,“, „und“, „oder“, „sowie“, „bzw.“ verbunden sind, übernehmen das Gesetz des letzten Glieds.
  2. Sonst das Kontextgesetz (`law`): im Normtext eines Gesetzes dieses Gesetz („dieses Gesetzes“ ebenso), in den
     Inhalten des Markenpakets das MarkenG. Inhalte der Pakete Patent, Design und EPG müssen jedes Zitat mit Gesetz
     schreiben; `tools/check_zitate.py` bricht sonst ab.
Nennt ein Zitat ein Gesetz, das hier nicht verlinkbar ist (unbekannte Abkürzung, „des Warenzeichengesetzes“), bleibt es
unverlinkt; es fällt nie auf das Kontextgesetz zurück.

Dieses Modul ist die einzige Quelle der Verlinkungsregeln: `linkify` erzeugt
Markdown und HTML für die Exporte, `js_source` die wortgleiche JavaScript-
Fassung für die beiden Web-Apps.
"""
import json
import re

BASE = "https://www.gesetze-im-internet.de/"

# Abkürzung -> (Slug auf gesetze-im-internet.de, Zitierweise "§" oder "Art."); Slugs am 28.09.2026 geprüft (index.html = 200)
LAWS = {
    "MarkenG": ("markeng", "§"),
    "BGB": ("bgb", "§"),
    "UWG": ("uwg_2004", "§"),
    "ZPO": ("zpo", "§"),
    "GG": ("gg", "Art."),
    "UrhG": ("urhg", "§"),
    "PatG": ("patg", "§"),
    "DesignG": ("geschmmg_2004", "§"),
    "DesignV": ("designv", "§"),
    "GebrMG": ("gebrmg", "§"),
    "HGB": ("hgb", "§"),
    "GKG": ("gkg_2004", "§"),
    "MarkenV": ("markenv_2004", "§"),
    "DPMAV": ("dpmav_2004", "§"),
    "PAO": ("patanwo", "§"),
    "StGB": ("stgb", "§"),
    "StPO": ("stpo", "§"),
    "OWiG": ("owig_1968", "§"),
    "GWB": ("gwb", "§"),
    "PatKostG": ("patkostg", "§"),
    "PatKostZV": ("patkostzv_2004", "§"),
    "PatV": ("patv", "§"),
    # IntPatÜG (amtlich IntPatÜbkG): Paragraphen der Art. II, III und XI werden als „Art. II § 6 IntPatÜG“ zitiert
    # und liegen unter intpat_bkg/art_ii__6.html (siehe url_for).
    "IntPatÜG": ("intpat_bkg", "§"),
    "IntPatÜbkG": ("intpat_bkg", "§"),
    "GmbHG": ("gmbhg", "§"),
    "FamFG": ("famfg", "§"),
    "VwZG": ("vwzg_2005", "§"),
    "VwVfG": ("vwvfg", "§"),
    "GVG": ("gvg", "§"),
    "InsO": ("inso", "§"),
    "PartGG": ("partgg", "§"),
    "AktG": ("aktg", "§"),
    "RVG": ("rvg", "§"),
    "RPflG": ("rpflg_1969", "§"),
    "HalblSchG": ("halblschg", "§"),
    "SortSchG": ("sortschg_1985", "§"),
    "VGG": ("vgg", "§"),
    "DDG": ("ddg", "§"),
    "ArbnErfG": ("arbnerfg", "§"),
    "EGBGB": ("bgbeg", "Art."),
    "AO": ("ao_1977", "§"),
    "TKG": ("tkg_2021", "§"),
    "LPartG": ("lpartg", "§"),
    "BRAO": ("brao", "§"),
    "ErstrG": ("erstrg", "§"),
    "JBeitrG": ("jbeitro", "§"),
    "GNotKG": ("gnotkg", "§"),
    "JVEG": ("jveg", "§"),
    "UKlaG": ("uklag", "§"),
    "KunstUrhG": ("kunsturhg", "§"),
    "GeschGehG": ("geschgehg", "§"),
    "PatAnwAPrV": ("patanwaprv", "§"),
    "ERVDPMAV": ("ervdpmav_2026", "§"),
    "RDG": ("rdg", "§"),
    "EuPAG": ("eupag", "§"),
    "AMG": ("amg_1976", "§"),
}
# Schreibweisen in Entscheidungen und Normenketten -> Abkürzung der Tabellen
ALIASES = {"ArbNErfG": "ArbnErfG", "ArbEG": "ArbnErfG", "EPC": "EPÜ", "TFEU": "AEUV", "EPGVerfO": "VerfO", "UPCS": "EPG-Satzung",
           "EuGVVO": "Brüssel-Ia-VO", "Brüssel Ia-VO": "Brüssel-Ia-VO", "GbmG": "GebrMG",
           "EPG": "EPGÜ", "EU-GRCh": "GRCh", "RpfG": "RPflG"}

# Gesetze ohne Einzelseiten je Artikel (Link auf das Gesamtdokument); Paragraphen wie „Art. 229 § 6“ haben eigene Seiten
WHOLE_DOC = {"EGBGB": "BJNR006049896.html"}

# Langformen in Gesetzestexten („§ 125 des Patentgesetzes“) -> Abkürzung; None = nicht verlinkbar (aufgehobenes Gesetz)
LONG_LAWS = {
    "des Patentgesetzes": "PatG", "des Markengesetzes": "MarkenG", "des Designgesetzes": "DesignG",
    "des Gebrauchsmustergesetzes": "GebrMG", "des Patentkostengesetzes": "PatKostG",
    "der Zivilprozessordnung": "ZPO", "der Zivilprozeßordnung": "ZPO",
    "des Bürgerlichen Gesetzbuchs": "BGB", "des Bürgerlichen Gesetzbuches": "BGB",
    "des Einführungsgesetzes zum Bürgerlichen Gesetzbuche": "EGBGB",
    "des Handelsgesetzbuchs": "HGB", "des Handelsgesetzbuches": "HGB",
    "des Strafgesetzbuchs": "StGB", "des Strafgesetzbuches": "StGB",
    "der Strafprozessordnung": "StPO", "der Strafprozeßordnung": "StPO",
    "des Gesetzes über Ordnungswidrigkeiten": "OWiG",
    "des Gerichtsverfassungsgesetzes": "GVG", "des Gerichtskostengesetzes": "GKG",
    "des Rechtsanwaltsvergütungsgesetzes": "RVG", "des Rechtspflegergesetzes": "RPflG",
    "des Urheberrechtsgesetzes": "UrhG", "des Gesetzes gegen den unlauteren Wettbewerb": "UWG",
    "des Gesetzes gegen Wettbewerbsbeschränkungen": "GWB",
    "der Patentanwaltsordnung": "PAO", "der Bundesrechtsanwaltsordnung": "BRAO",
    "der Insolvenzordnung": "InsO", "der Abgabenordnung": "AO", "des Aktiengesetzes": "AktG",
    "des Verwaltungszustellungsgesetzes": "VwZG", "des Verwaltungsverfahrensgesetzes": "VwVfG",
    "des Telekommunikationsgesetzes": "TKG", "des Lebenspartnerschaftsgesetzes": "LPartG",
    "des Erstreckungsgesetzes": "ErstrG", "der Justizbeitreibungsordnung": "JBeitrG", "des Justizbeitreibungsgesetzes": "JBeitrG",
    "des Halbleiterschutzgesetzes": "HalblSchG", "des Sortenschutzgesetzes": "SortSchG",
    "des Gesetzes über internationale Patentübereinkommen": "IntPatÜG", "des Arbeitnehmererfindungsgesetzes": "ArbnErfG",
    "des Gesetzes über Arbeitnehmererfindungen": "ArbnErfG", "des Grundgesetzes": "GG", "der DPMA-Verordnung": "DPMAV",
    "des Digitale-Dienste-Gesetzes": "DDG", "des Gerichts- und Notarkostengesetzes": "GNotKG",
    "des Justizvergütungs- und -entschädigungsgesetzes": "JVEG",
    "der Durchführungsordnung zum einheitlichen Patentschutz": "DOEPS",
    "des Geschmacksmustergesetzes": None, "des Warenzeichengesetzes": None,
}
SELF_LAW = ("dieses Gesetzes", "dieser Verordnung")

# Bestehende Paragraphen/Artikel je Gesetz (data/gesetze_paragraphen.json, erzeugt von tools/check_zitate.py --net --update):
# Zitate auf nicht (mehr) existierende Vorschriften werden nicht verlinkt, damit kein Link ins Leere (404) führt.
try:
    PARAGRAPHEN = json.loads((__import__("pathlib").Path(__file__).resolve().parents[2] / "data" / "gesetze_paragraphen.json").read_text())
except FileNotFoundError:
    PARAGRAPHEN = {}

DEFAULT_LAW = "MarkenG"  # nur Inhalte des Markenpakets und der MarkenG-Normtext; alle anderen Aufrufer übergeben `law`
# Unionsrecht und Staatsverträge: nicht auf gesetze-im-internet.de; Link auf das Gesamtdokument (EUR-Lex, WIPO, WTO).
EU_LAWS = {
    "MarkenRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2436",
    "DurchsetzungsRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004L0048R(01)",
    "UMV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1001",
    "GMV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32009R0207",
    "AEUV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016E/TXT",
    "EUV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016M/TXT",
    "GRCh": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016P/TXT",
    "DSGVO": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679",
    "PVÜ": "https://www.wipo.int/treaties/en/ip/paris/",
    "PMMA": "https://www.wipo.int/treaties/en/registration/madrid_protocol/",
    "MMA": "https://www.wipo.int/treaties/en/registration/madrid/",
    "TRIPS": "https://www.wto.org/english/docs_e/legal_e/27-trips_01_e.htm",
    # Einheitliches Patentgericht: Übereinkommen (EUR-Lex) und Verfahrensordnung (unifiedpatentcourt.org, PDF)
    "EPGÜ": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:42013A0620(01)",
    "UPCA": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:42013A0620(01)",
    "VerfO": "https://www.unifiedpatentcourt.org/sites/default/files/upc_documents/Consolidated%20Rules%20of%20Procedure%20UPC_DE.pdf",
    "RoP": "https://www.unifiedpatentcourt.org/sites/default/files/upc_documents/Consolidated%20Rules%20of%20Procedure%20UPC_DE.pdf",
    # Einheitspatent: Verordnungen (EUR-Lex), Durchführungs- und Gebührenordnung (epo.org, Rechtstexte zum Einheitspatentsystem)
    "EPatVO": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1257",
    "EPatÜVO": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1260",
    "EPatÜbersVO": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1260",
    "DOEPS": "https://www.epo.org/de/legal/up-upc/2022/upr.html",
    "UPR": "https://www.epo.org/de/legal/up-upc/2022/upr.html",
    "GebOEPS": "https://www.epo.org/de/legal/up-upc/2022/upf.html",
    "GebEPS": "https://www.epo.org/de/legal/up-upc/2022/upf.html",
    "RFeesUPP": "https://www.epo.org/de/legal/up-upc/2022/upf.html",
    # Designrecht: Richtlinie 98/71/EG (bis 9.12.2027), Richtlinie (EU) 2024/2823 (Neufassung) und die Verordnung über
    # Unionsgeschmacksmuster (VO (EG) Nr. 6/2002, konsolidiert; weiter „GGV“ zitiert, auch UGMV)
    "DesignRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31998L0071",
    "DesignRL 2024": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L2823",
    "GGV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02002R0006-20260701",
    "UGMV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02002R0006-20260701",
    "GGV-DV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32002R2245",
    "HMA": "https://www.wipo.int/treaties/en/registration/hague/",
    "EPG-Satzung": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:42013A0620(01)",
    "Brüssel-Ia-VO": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1215",
    "Rom-II-VO": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32007R0864",
    "EMRK": "https://www.echr.coe.int/documents/d/echr/convention_deu",
    "PCT": "https://www.wipo.int/pct/en/texts/articles/atoc.html",
}
# Einzelvorschriften mit eigener Seite außerhalb von gesetze-im-internet.de: EPÜ-Artikel und Regeln der Ausführungsordnung
# auf epo.org („Art. 54 EPÜ“ -> a54.html, „R. 71 EPÜ“ -> r71.html).
ARTICLE_URLS = {"EPÜ": ("https://www.epo.org/de/legal/epc/2020/a%s.html", "https://www.epo.org/de/legal/epc/2020/r%s.html")}
# EPÜ-Artikel mit Buchstabenzusatz, die es wirklich gibt („Art. 53c“ in Leitsätzen meint Art. 53 lit. c und bleibt unverlinkt)
ARTICLE_LETTERED = {"EPÜ": ("105a", "105b", "105c", "112a", "134a", "149a")}
# Zitierkürzel -> Schlüssel des Richtlinien-/Übereinkommensknotens im Graphen (eunorm:<key>:<nr>); Aliase erlaubt.
EU_NORM_KEYS = {"MarkenRL": "markenrl", "DurchsetzungsRL": "durchsetzungsrl", "EPGÜ": "upca", "UPCA": "upca", "VerfO": "rop", "RoP": "rop",
                "EPatVO": "epatvo", "EPatÜVO": "epatuevo", "EPatÜbersVO": "epatuevo", "DOEPS": "doeps", "UPR": "doeps",
                "GebOEPS": "gebeps", "GebEPS": "gebeps", "RFeesUPP": "gebeps",
                "DesignRL": "designrl", "DesignRL 2024": "designrl2024", "GGV": "ggv", "UGMV": "ggv"}
# Zitatköpfe für Regeln (VerfO, DOEPS): „R. 19.1 VerfO“, „Regel 262A VerfO“, „Rule 19 RoP“, „R. 6 Abs. 1 DOEPS“; ohne Gesetzesangabe nie verlinken.
RULE_HEADS = ("R.", "Regel", "Rule")
# Deutsche Gesetze, die als eigene Normfamilien im Graphen liegen (eunorm:<key>:<nr>): `§ 3 PatG` -> eunorm:patg:3
DE_NORM_KEYS = {"PatG": "patg", "PatV": "patv", "IntPatÜG": "intpatueg", "IntPatÜbkG": "intpatueg", "PatKostG": "patkostg",
                "DesignG": "designg", "DesignV": "designv"}
# „Art. II § 6 IntPatÜG“, „Art. 229 § 6 EGBGB“ (Artikelgesetze mit Paragraphen): Seite art_ii__6.html bzw. art_229__6.html
_ROMAN_HEAD = re.compile(r"^(?:Art\.|Artikel)\s*([IVX]+|\d+)\s*§")
# Ohne verlinkbare Fundstelle (aufgehoben): nie verlinken, nie auf das Kontextgesetz zurückfallen.
UNLINKED = ("GeschmMG", "WZG", "TMG", "EPÜ 1973")

_KNOWN = list(LAWS) + list(EU_LAWS) + list(ARTICLE_URLS) + list(UNLINKED) + list(ALIASES)
_ABBR = "|".join(re.escape(k) for k in sorted(_KNOWN, key=len, reverse=True))
_LETTERS = "A-Za-zÄÖÜäöüß"
# Langform: bekannte Namen zuerst, dann jede andere Gesetzes-/Verordnungsbezeichnung im Genitiv (nicht verlinkbar)
_LONG = ("|".join(re.escape(k) for k in sorted(list(LONG_LAWS) + list(SELF_LAW), key=len, reverse=True))
         + r"|(?:des|der)\s+[A-ZÄÖÜ][" + _LETTERS + r"-]*(?:gesetzes|gesetzbuchs|gesetzbuches|gesetzbuche|ordnung|verordnung)(?![" + _LETTERS + r"])"
         + r"|des\s+Gesetzes\s+(?:über|gegen|zur|zum|zu)\s[" + _LETTERS + r"\s-]{3,60}?(?=[\s,.;)])")
# Unbekannte Gesetzesabkürzung nach dem Zitat („§ 5 WZG“, „§ 3 MaMoG“): nicht verlinken statt Kontextgesetz.
# Nicht als Gesetz gelten Währungen und Sammelbegriffe (EUR, EU, EG).
_FOREIGN = r"(?!(?:EUR|EU|EG)(?![" + _LETTERS + r"]))[A-ZÄÖÜ][a-zäöüß]*[A-ZÄÖÜ][" + _LETTERS + r"-]*(?![" + _LETTERS + r"])"
# Zusätze an Artikelnummern der Staatsverträge („Art. 6bis PVÜ“, „Art. 9quinquies PMMA“) oder Buchstabe („§ 19a“, „R. 262A“)
_SUFFIX = r"(?:bis|ter|quater|quinquies|sexies|septies|octies|[a-zA-Z])?"
_PAREN = r"(?:\s?\([a-z0-9]{1,4}\))*"   # „R. 262.1(b)“, „Art. 76 (1) UPCA“, „Abs. 1 (b)“
_SUBKEYS = r"Abs\.|Absatz|UAbs\.|Unterabs\.|Unterabsatz|Nr\.|Nummer|Satz|S\.|lit\.|Buchst\.?|Buchstabe|Halbsatz|Halbs\.|Hs\.|Alt\.|Var\."
# Gruppen (G_*): Gesetz vor dem Zitat (Normenkette der Leitsätze „PatG § 9 Nr. 1, § 139“), Zitatkopf (auch „R.“/„Regel“/„Rule“),
# Nummern (Ketten „9 bis 13“, „146 ff.“, Regeln „262A“, „19.1“, „262.1(b)“), Untergliederung (Abs., Nr., S., lit., mit Ketten
# „S. 3 bis 5“), Gesetzesabkürzung, Langform („des Patentgesetzes“, „dieses Gesetzes“), unbekannte Abkürzung
G_PRE, G_HEAD, G_NUMS, G_SUB, G_LAW, G_LONG, G_FOREIGN = 1, 2, 3, 4, 5, 6, 7
_PATTERN = (
    r"(?:(?<![" + _LETTERS + r"])(" + _ABBR + r")\s+(?=§|Art\.))?"
    r"((?:Art\.|Artikel)\s*(?:[IVX]+|\d+)\s*§|§§|§|Art\.|\bR\.|\bRegel|\bRule)\s*"
    r"(\d+" + _SUFFIX + r"(?:\.\d+)*" + _PAREN + r"(?:\s*(?:bis|,|und|ff\.|f\.|/|-|–)\s*\d+" + _SUFFIX + r"(?:\.\d+)*" + _PAREN + r")*(?:\s*f{1,2}\.)?(?: [A-I](?= ))?)"
    r"((?:(?:,|\s+und|\s+oder|\s+sowie)?\s+(?:" + _SUBKEYS + r")\s*[0-9A-Za-z_ÄÖÜäöüß§]+" + _PAREN + r"(?:\s*(?:bis|und|,|/|–|-)\s*(?:\d+[a-z]?|[a-z])" + _PAREN + r"(?![0-9A-Za-z_ÄÖÜäöüß.]))*)*)"
    r"(?:\s+(" + _ABBR + r")(?![" + _LETTERS + r"])|\s+(" + _LONG + r")|\s+(" + _FOREIGN + r"))?"
)
CITATION = re.compile(_PATTERN)
_NUM = re.compile(r"\d+[a-z]?")
_CHAIN = re.compile(r"\s*(?:,|und|oder|sowie|bzw\.)\s*(?:(?:die|der|den|des|dem)\s+)?")
_LONG_NAMES = re.compile("|".join(re.escape(k) for k in sorted(LONG_LAWS, key=len, reverse=True)))
FOREIGN = ""  # Marker: Zitat nennt ein nicht verlinkbares Gesetz
_ABBR_BEFORE = re.compile(r"(?<![" + _LETTERS + r"])(" + _ABBR + r")\s*\(\s*$")
_ALT = re.compile(r"\s*\(?a\.\s?F\.")


def _abbr(a):
    a = ALIASES.get(a, a)
    return FOREIGN if a in UNLINKED else a


def _named(m, law):
    """Gesetz, das das Zitat selbst nennt: Abkürzung, Langform („dieses Gesetzes“ = Kontextgesetz), FOREIGN, oder None."""
    if m.group(G_LAW):
        return _abbr(m.group(G_LAW))
    if m.group(G_LONG):
        lf = re.sub(r"\s+", " ", m.group(G_LONG))
        if lf in SELF_LAW:
            return law or FOREIGN
        return LONG_LAWS.get(lf) or FOREIGN
    if m.group(G_FOREIGN):
        return FOREIGN
    if m.group(G_PRE):
        return _abbr(m.group(G_PRE))
    return None


def _paren_law(text, m):
    """„die Vorschriften der Zivilprozessordnung über Zustellungen (§§ 166 bis 190)“: Zitat in Klammern ohne Gesetz übernimmt
    die zuletzt im selben Satz genannte Langform."""
    before = text[max(0, m.start() - 400):m.start()]
    if not before.rstrip().endswith("("):
        return None
    ab = _ABBR_BEFORE.search(before)   # „im MarkenG (§ 18)“, „UrhG (§ 98 Abs. 3)“
    if ab:
        return _abbr(ab.group(1)) or None
    before = re.split(r"[.;:]\s+(?=[A-ZÄÖÜ(])|\n", before)[-1]
    found = _LONG_NAMES.findall(before)
    return LONG_LAWS.get(found[-1]) if found else None


def resolve(text, law=DEFAULT_LAW):
    """Alle Zitate in `text` mit dem Gesetz, das für sie gilt: [(match, gesetz, herkunft)].
    herkunft: "genannt" (Zitat nennt das Gesetz), "kette-vor" (Normenkette mit vorangestelltem Gesetz: „PatG § 9 Nr. 1, § 139“),
    "kette" (Gesetz am Kettenende: „§ 4, § 1 Nr. 4 DesignG“), "satz" (Langform im selben Satz vor der Klammer),
    "kontext" (Kontextgesetz `law`)."""
    ms = list(CITATION.finditer(text))
    n = len(ms)
    out = [None] * n
    # 1. Normenketten mit vorangestelltem Gesetz (Leitsätze). Ein Gesetz zwischen zwei Zitaten gehört zum folgenden:
    #    „PatG §§ 59 Abs. 1, 123 Abs. 1 PatKostG § 6“ -> § 6 PatKostG.
    carry, state = {}, None
    for i, m in enumerate(ms):
        pre = _abbr(m.group(G_PRE)) if m.group(G_PRE) else carry.get(i)
        if pre is not None:
            state, how = pre, "genannt"
        elif state is not None and _CHAIN.fullmatch(text[ms[i - 1].end():m.start()]):
            how = "kette-vor"
        else:
            state = None
            continue
        out[i] = (m, state, how)
        if m.group(G_LAW) and i + 1 < n and not ms[i + 1].group(G_PRE) and not text[m.end():ms[i + 1].start()].strip():
            carry[i + 1] = _abbr(m.group(G_LAW))
    # 2. Gesetz hinter dem Zitat; Kettenglieder davor übernehmen es („§ 4, § 1 Nr. 4 DesignG“)
    for i in range(n - 1, -1, -1):
        if out[i] is not None:
            continue
        m = ms[i]
        named = _named(m, law)
        if named is not None:
            out[i] = (m, named, "genannt")
        elif i + 1 < n and out[i + 1] is not None and out[i + 1][2] in ("genannt", "kette") and not ms[i + 1].group(G_PRE) \
                and (i + 1) not in carry and _CHAIN.fullmatch(text[m.end():ms[i + 1].start()]):
            out[i] = (m, out[i + 1][1], "kette")
    # 3. Klammerzitat nach einer Langform im selben Satz, sonst Kontextgesetz
    for i, m in enumerate(ms):
        if out[i] is None:
            pl = _paren_law(text, m)
            out[i] = (m, pl, "satz") if pl else (m, law, "kontext")
    # 4. Alte Fassung („§ 125b MarkenG a.F.“): nie auf die heutige Vorschrift gleicher Nummer verlinken
    for i, m in enumerate(ms):
        if _ALT.match(text, m.end()):
            out[i] = (m, FOREIGN, "alte Fassung")
    return out


def qualify(text, law):
    """Hängt an Zitate ohne Gesetzesangabe das Gesetz an, damit `linkify` sie richtig zuordnet.

    qualify('§ 140b, § 139 Abs. 1 S. 3 bis 5', 'PatG') -> '§ 140b PatG, § 139 Abs. 1 S. 3 bis 5 PatG'
    Zitate, die bereits ein Gesetz nennen (auch über eine Kette), und unbekannte Gesetze bleiben unverändert.
    """
    if law not in LAWS and law not in EU_LAWS:
        return text
    out, pos = [], 0
    for m, _, how in resolve(text, None):
        if how != "kontext":
            continue
        out.append(text[pos:m.end()] + " " + law)
        pos = m.end()
    return "".join(out) + text[pos:]


def url_for(nummer, law=DEFAULT_LAW, artikel=None):
    """URL der Einzelvorschrift, oder None, wenn das Gesetz nicht verlinkbar ist oder die Vorschrift dort nicht existiert.
    `artikel`: römische Artikelnummer beim IntPatÜG (Art. II § 6 -> intpat_bkg/art_ii__6.html)."""
    entry = LAWS.get(law)
    if not entry:
        return None
    slug, kind = entry
    if law in WHOLE_DOC and not artikel:   # EGBGB: nur die Paragraphen der Art. 224/229 haben eigene Seiten, sonst Gesamtdokument
        return BASE + slug + "/" + WHOLE_DOC[law]
    known = PARAGRAPHEN.get(law)
    if known is not None and (artikel + " " + nummer if artikel else nummer) not in known:
        return None
    if artikel:
        return BASE + slug + "/art_%s__%s.html" % (artikel.lower(), nummer)
    datei = "art_%s.html" % nummer if kind == "Art." else "__%s.html" % nummer
    return BASE + slug + "/" + datei


def _link(nummer, law, label, fmt, artikel=None):
    href = EU_LAWS.get(law) or url_for(nummer, law, artikel)
    if not href:
        return label
    if fmt == "markdown":
        return "[%s](%s)" % (label, href)
    return '<a href="%s" target="_blank" rel="noopener" class="lawlink">%s</a>' % (href, label)


def href_for(m, law):
    """Ziel-URL eines Zitats (für Prüfskripte); None = nicht verlinkt."""
    head, nums = m.group(G_HEAD), m.group(G_NUMS)
    if not law:
        return None
    if law in EU_LAWS:
        return EU_LAWS[law] if not head.startswith("§") else None   # Unionsrecht/Staatsverträge haben keine Paragraphen
    found = _NUM.findall(nums)
    if law in ARTICLE_URLS:
        if not found or head == "§" or head == "§§":
            return None
        if head not in RULE_HEADS and not found[0].isdigit() and found[0] not in ARTICLE_LETTERED.get(law, ()):
            return None
        return ARTICLE_URLS[law][1 if head in RULE_HEADS else 0] % found[0]
    rm = _ROMAN_HEAD.match(head)
    if rm:
        return url_for(found[0], law, rm.group(1)) if law in LAWS and found else None
    if head in RULE_HEADS or (head == "Art." and LAWS.get(law, ("", ""))[1] != "Art."):
        return None
    return url_for(found[0], law) if found else None


def linkify(text, fmt="html", escape=None, law=DEFAULT_LAW):
    """Ersetzt Gesetzeszitate durch Links.

    fmt="html"     -> <a href="…" class="lawlink">§ 14 MarkenG</a>
    fmt="markdown" -> [§ 14 MarkenG](…)
    escape         -> optionale Funktion für den Text außerhalb der Zitate
    law            -> Kontextgesetz für Zitate ohne Gesetzesangabe (Normtext: das Gesetz selbst)
    """
    def repl(m, target):
        head, nums = m.group(G_HEAD), m.group(G_NUMS)
        label = m.group(0)
        href = href_for(m, target)
        if not href:
            return label
        found = _NUM.findall(nums)
        if head == "§§" and len(found) > 1 and target in LAWS:
            k = m.start(G_HEAD) - m.start() + len(head)
            rest, out, pos = label[k:], label[:k], 0
            for n in found:
                i = rest.index(n, pos)
                out += rest[pos:i] + (_link(n, target, n, fmt) if url_for(n, target) else n)
                pos = i + len(n)
            return out + rest[pos:]
        if fmt == "markdown":
            return "[%s](%s)" % (label, href)
        return '<a href="%s" target="_blank" rel="noopener" class="lawlink">%s</a>' % (href, label)

    parts, last = [], 0
    for m, target, _ in resolve(text, law):
        chunk = text[last:m.start()]
        parts.append(escape(chunk) if escape else chunk)
        parts.append(repl(m, target))
        last = m.end()
    tail = text[last:]
    parts.append(escape(tail) if escape else tail)
    return "".join(parts)


def js_table():
    """Tabelle für die HTML-Apps."""
    return {
        "base": BASE,
        "laws": {k: {"slug": v[0], "kind": v[1]} for k, v in LAWS.items()},
        "unlinked": list(UNLINKED),
        "aliases": ALIASES,
        "eu": EU_LAWS,
        "article": {k: list(v) for k, v in ARTICLE_URLS.items()},
        "long": LONG_LAWS,
        "self": list(SELF_LAW),
        "default": DEFAULT_LAW,
        "eukeys": EU_NORM_KEYS,
        "dekeys": DE_NORM_KEYS,
        "ruleheads": list(RULE_HEADS),
        "paras": PARAGRAPHEN,
        "wholedoc": WHOLE_DOC,
        "lettered": {k: list(v) for k, v in ARTICLE_LETTERED.items()},
        "g": dict(pre=G_PRE, head=G_HEAD, nums=G_NUMS, sub=G_SUB, law=G_LAW, long=G_LONG, foreign=G_FOREIGN),
    }


JS_TEMPLATE = """
// ---- Gesetzeslinks (erzeugt aus src/knowledge/gesetze.py; gleiche Regeln wie resolve/href_for/linkify dort) ----
const LAW = __LAWDATA__;
const CITE = new RegExp(__PATTERN__, 'g');
const LAWCHAIN = new RegExp('^(?:' + __CHAIN__ + ')$');
const LAWROMAN = new RegExp(__ROMAN__);
const LAWLONGNAMES = new RegExp(__LONGNAMES__, 'g');
const LG = LAW.g;
const LAWALT = new RegExp('^' + __ALT__);
const LAWABBRBEFORE = new RegExp(__ABBRBEFORE__);
function lawUrl(num, law, art){ const e = LAW.laws[law]; if(!e) return null;
  if(LAW.wholedoc[law] && !art) return LAW.base + e.slug + '/' + LAW.wholedoc[law];
  const k = LAW.paras[law]; if(k && k.indexOf(art ? art + ' ' + num : num) < 0) return null;
  if(art) return LAW.base + e.slug + '/art_' + art.toLowerCase() + '__' + num + '.html';
  return LAW.base + e.slug + '/' + (e.kind === 'Art.' ? 'art_' + num + '.html' : '__' + num + '.html'); }
function lawA(href, label){ var eu = href.indexOf('eur-lex') >= 0, upc = href.indexOf('unifiedpatentcourt') >= 0, epo = href.indexOf('epo.org') >= 0,
  intl = href.indexOf('wipo.int') >= 0 || href.indexOf('wto.org') >= 0 || href.indexOf('echr.coe.int') >= 0;
  return '<a href="' + href + '" target="_blank" rel="noopener" class="lawlink"'
  + ' title="' + (upc ? 'Verfahrensordnung des EPG (PDF)' : epo ? 'Auf epo.org nachlesen' : eu ? 'Auf EUR-Lex nachlesen' : intl ? 'Vertragstext nachlesen' : 'Auf gesetze-im-internet.de nachlesen') + '">' + label + '</a>'; }
function lawAbbr(a){ a = LAW.aliases[a] || a; return LAW.unlinked.indexOf(a) >= 0 ? '' : a; }
function lawNamed(m, ctx){
  if(m[LG.law]) return lawAbbr(m[LG.law]);
  if(m[LG.long]){ var lf = m[LG.long].replace(/\\s+/g, ' '); if(LAW.self.indexOf(lf) >= 0) return ctx || ''; return LAW.long[lf] || ''; }
  if(m[LG.foreign]) return '';
  if(m[LG.pre]) return lawAbbr(m[LG.pre]);
  return null; }
function lawParen(s, m){ var before = s.slice(Math.max(0, m.index - 400), m.index);
  if(!/\\($/.test(before.replace(/\\s+$/, ''))) return null;
  var ab = before.match(LAWABBRBEFORE); if(ab) return lawAbbr(ab[1]) || null;
  before = before.split(/[.;:]\\s+(?=[A-ZÄÖÜ(])|\\n/).pop();
  var f = before.match(LAWLONGNAMES); return f ? LAW.long[f[f.length - 1]] || null : null; }
function lawResolve(s, ctx){
  var ms = [], m, i, n; CITE.lastIndex = 0;
  while((m = CITE.exec(s))){ ms.push(m); if(!m[0]) CITE.lastIndex++; }
  n = ms.length;
  var out = new Array(n), carry = {}, state = null, gap = function(a, b){ return LAWCHAIN.test(s.slice(a.index + a[0].length, b.index)); };
  for(i = 0; i < n; i++){ m = ms[i]; var pre = m[LG.pre] ? lawAbbr(m[LG.pre]) : (i in carry ? carry[i] : null), how;
    if(pre !== null){ state = pre; how = 'genannt'; }
    else if(state !== null && gap(ms[i - 1], m)) how = 'kette-vor';
    else { state = null; continue; }
    out[i] = [m, state, how];
    if(m[LG.law] && i + 1 < n && !ms[i + 1][LG.pre] && !s.slice(m.index + m[0].length, ms[i + 1].index).trim()) carry[i + 1] = lawAbbr(m[LG.law]); }
  for(i = n - 1; i >= 0; i--){ if(out[i]) continue; m = ms[i]; var named = lawNamed(m, ctx);
    if(named !== null) out[i] = [m, named, 'genannt'];
    else if(i + 1 < n && out[i + 1] && (out[i + 1][2] === 'genannt' || out[i + 1][2] === 'kette') && !ms[i + 1][LG.pre] && !((i + 1) in carry) && gap(m, ms[i + 1])) out[i] = [m, out[i + 1][1], 'kette']; }
  for(i = 0; i < n; i++) if(!out[i]){ var pl = lawParen(s, ms[i]); out[i] = pl ? [ms[i], pl, 'satz'] : [ms[i], ctx, 'kontext']; }
  for(i = 0; i < n; i++) if(LAWALT.test(s.slice(ms[i].index + ms[i][0].length, ms[i].index + ms[i][0].length + 8))) out[i] = [ms[i], '', 'alte Fassung'];
  return out; }
function lawHref(m, law){
  var head = m[LG.head], found = m[LG.nums].match(NUMRE) || [];
  if(!law) return null;
  if(LAW.eu[law]) return head.charAt(0) === '\u00a7' ? null : LAW.eu[law];
  if(LAW.article[law]){ if(!found.length || head.charAt(0) === '\\u00a7') return null;
    if(LAW.ruleheads.indexOf(head) < 0 && !/^\\d+$/.test(found[0]) && (LAW.lettered[law] || []).indexOf(found[0]) < 0) return null;
    return LAW.article[law][LAW.ruleheads.indexOf(head) >= 0 ? 1 : 0].replace('%s', found[0]); }
  var rm = head.match(LAWROMAN);
  if(rm) return LAW.laws[law] && found.length ? lawUrl(found[0], law, rm[1]) : null;
  if(LAW.ruleheads.indexOf(head) >= 0 || (head === 'Art.' && !(LAW.laws[law] && LAW.laws[law].kind === 'Art.'))) return null;
  return found.length ? lawUrl(found[0], law) : null; }
function lawifyText(s, ctx){
  var o = '', last = 0, rs = lawResolve(s, ctx);
  for(var j = 0; j < rs.length; j++){ var m = rs[j][0], law = rs[j][1], label = m[0], href = lawHref(m, law);
    o += s.slice(last, m.index); last = m.index + label.length;
    if(!href){ o += label; continue; }
    var found = m[LG.nums].match(NUMRE) || [], head = m[LG.head];
    if(head === '\\u00a7\\u00a7' && found.length > 1 && LAW.laws[law]){
      var k = label.indexOf(head) + head.length, rest = label.slice(k), x = label.slice(0, k), pos = 0;
      for(var i = 0; i < found.length; i++){ var n = found[i], at = rest.indexOf(n, pos);
        var u = lawUrl(n, law); x += rest.slice(pos, at) + (u ? lawA(u, n) : n); pos = at + n.length; }
      o += x + rest.slice(pos);
    } else o += lawA(href, label); }
  return o + s.slice(last); }
// ctx: Gesetz für Zitate ohne Gesetzesangabe (Normtext: das Gesetz selbst); ohne Angabe das MarkenG (Markenpaket), '' = keins
function lawify(html, ctx){ if(html == null) return ''; var s = String(html); if(ctx === undefined) ctx = LAW.default;
  if(s.indexOf('class="lawlink"') >= 0) return s;
  return s.split(/(<[^>]*>)/).map(function(p, i){ return i % 2 ? p : lawifyText(p, ctx); }).join(''); }
"""


def js_source():
    """JavaScript-Fassung der Verlinkung: gleiche Tabelle, gleiches Muster."""
    return (JS_TEMPLATE
            .replace("__LAWDATA__", json.dumps(js_table(), ensure_ascii=False))
            .replace("__PATTERN__", json.dumps(_PATTERN))
            .replace("__CHAIN__", json.dumps(_CHAIN.pattern))
            .replace("__ROMAN__", json.dumps(_ROMAN_HEAD.pattern))
            .replace("__LONGNAMES__", json.dumps(_LONG_NAMES.pattern))
            .replace("__ALT__", json.dumps(_ALT.pattern))
            .replace("__ABBRBEFORE__", json.dumps(_ABBR_BEFORE.pattern))
            .replace("NUMRE", json.dumps(_NUM.pattern).join(["new RegExp(", ", 'g')"])))


if __name__ == "__main__":
    proben = [
        "Nach § 14 Abs. 2 Nr. 2 MarkenG besteht Verwechslungsgefahr.",
        "Die §§ 9 bis 13 regeln relative Schutzhindernisse; §§ 3, 7, 8 die Eintragung.",
        "Schranken der §§ 23/24, Verfahren der §§ 112-125, Löschung §§ 49–52.",
        "Verwirkung nach § 21 Abs. 4 i.V.m. § 242 BGB; Kunstfreiheit Art. 5 Abs. 3 GG.",
        "Art. 9 Abs. 2 lit. c UMV entspricht § 14 Abs. 2 Nr. 3; Art. 6 PMMA bleibt frei; Art. 10 Abs. 2 MarkenRL ist der Ursprung.",
        "Streitwert nach § 51 GKG, Zuständigkeit § 140, Aussetzung § 148 ZPO.",
        "Einspruch nach R. 19.1 VerfO, Vertraulichkeit R. 262A VerfO, Zugang R. 262.1(b) RoP; Art. 33 Abs. 1 lit. a EPGÜ; Rule 19 RoP; Nr. 2 bleibt frei; R. 19 ohne Gesetz bleibt frei.",
        "Nichtigkeit nach Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Gebühr § 6 Abs. 1 PatKostG, Form § 9 PatV, Art. I IntPatÜG bleibt frei.",
        "Bauelemente (Abs. 3, 4 = § 4, § 1 Nr. 4 DesignG); Neuheit Art. 54 EPÜ, Zustellung R. 125 ff. EPÜ; Art. 6bis PVÜ; § 5 WZG bleibt frei.",
    ]
    for p in proben:
        print(linkify(p, "markdown"))
    print(linkify("§ 81 Absatz 6 und § 125 des Patentgesetzes gelten entsprechend; § 38 dieses Gesetzes; § 3 des Warenzeichengesetzes.",
                  "markdown", law="DesignG"))
    print(qualify("§ 140b, § 139 Abs. 1 S. 3 bis 5, § 140a Abs. 1 bis 4; § 9 Abs. 2 (§§ 24a bis 24e GebrMG)", "PatG"))
