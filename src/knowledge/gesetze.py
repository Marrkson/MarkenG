# -*- coding: utf-8 -*-
"""Verlinkung von Gesetzeszitaten auf gesetze-im-internet.de.

Erkennt Zitate wie „§ 14 Abs. 2 Nr. 2 MarkenG“, „§§ 9 bis 13“, „§§ 23/24“,
„§ 242 BGB“ oder „Art. 5 Abs. 3 GG“ in Fließtext und hängt einen Link an.

Fehlt die Gesetzesangabe, gilt das MarkenG als Bezugsgesetz (Projektkontext).
Zitate, deren Gesetz nicht auf gesetze-im-internet.de steht (UMV, MarkenRL,
PMMA, PVÜ), bleiben bewusst unverlinkt.

Dieses Modul ist die einzige Quelle der Verlinkungsregeln: `linkify` erzeugt
Markdown und HTML für die Exporte, `js_source` die wortgleiche JavaScript-
Fassung für die beiden Web-Apps.
"""
import json
import re

BASE = "https://www.gesetze-im-internet.de/"

# Abkürzung -> (Slug auf gesetze-im-internet.de, Zitierweise "§" oder "Art.")
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
    "TMG": ("tmg", "§"),
    "GKG": ("gkg_2004", "§"),
    "MarkenV": ("markenv_2004", "§"),
    "DPMAV": ("dpmav", "§"),
    "PAO": ("pao", "§"),
    "StGB": ("stgb", "§"),
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
    "VwZG": ("vwzg", "§"),
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
}

DEFAULT_LAW = "MarkenG"
# Unionsrecht: nicht auf gesetze-im-internet.de, aber auf EUR-Lex (Link auf das Gesamtdokument).
EU_LAWS = {
    "MarkenRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2436",
    "DurchsetzungsRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004L0048R(01)",
    "UMV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1001",
    "AEUV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016E/TXT",
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
    "GebEPS": "https://www.epo.org/de/legal/up-upc/2022/upf.html",
    "RFeesUPP": "https://www.epo.org/de/legal/up-upc/2022/upf.html",
    # Designrecht: Richtlinie 98/71/EG (bis 9.12.2027), Richtlinie (EU) 2024/2823 (Neufassung) und die Verordnung über
    # Unionsgeschmacksmuster (VO (EG) Nr. 6/2002, konsolidiert; weiter „GGV“ zitiert, auch UGMV)
    "DesignRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31998L0071",
    "DesignRL 2024": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L2823",
    "GGV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02002R0006-20260701",
    "UGMV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02002R0006-20260701",
    "GGV-DV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32002R2245",
    "HMA": "https://www.wipo.int/treaties/de/registration/hague/",
}
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
_ROMAN_HEAD = re.compile(r"^Art\.\s*([IVX]+)\s*§")
# Ohne verlinkbare Fundstelle: nie verlinken.
UNLINKED = ("GMV", "PMMA", "MMA", "PVÜ", "TRIPS", "EUV", "DSGVO", "EPÜ", "ERVDPMAV", "PatAnwAPrV", "GV", "GRCh", "GeschmMG")

_ABBR = "|".join(sorted(list(LAWS) + list(EU_LAWS) + list(UNLINKED), key=len, reverse=True))
# Gruppen: 1 Zitatkopf (auch „R.“/„Regel“/„Rule“ für die VerfO), 2 Nummern (Ketten „9 bis 13“, „146 ff.“, Regeln
# „262A“, „19.1“, „262.1(b)“), 3 Untergliederung (Abs., Nr., S., lit., jeweils mit Ketten „S. 3 bis 5“, „lit. a bis d“), 4 Gesetz
_PATTERN = (
    r"(Art\.\s*[IVX]+\s*§|§§|§|Art\.|\bR\.|\bRegel|\bRule)\s*"
    r"(\d+[a-zA-Z]?(?:\.\d+)*(?:\([a-z0-9]+\))*(?:\s*(?:bis|,|und|ff\.|f\.|/|-|–)\s*\d+[a-zA-Z]?(?:\.\d+)*(?:\([a-z0-9]+\))*)*(?:\s*f{1,2}\.)?)"
    r"((?:\s+(?:Abs\.|Absatz|Nr\.|Nummer|Satz|S\.|lit\.|Halbsatz|Alt\.)\s*[\w§]+(?:\s*(?:bis|und|,|/|–|-)\s*(?:\d+[a-z]?|[a-z])(?![\w.]))*)*)"
    r"(?:\s+(" + _ABBR + r"))?"
)
CITATION = re.compile(_PATTERN)
_NUM = re.compile(r"\d+[a-z]?")


def qualify(text, law):
    """Hängt an Zitate ohne Gesetzesangabe das Gesetz an, damit `linkify` sie richtig zuordnet.

    qualify('§ 140b, § 139 Abs. 1 S. 3 bis 5', 'PatG') -> '§ 140b PatG, § 139 Abs. 1 S. 3 bis 5 PatG'
    Zitate, die bereits ein Gesetz nennen, und unbekannte Gesetze bleiben unverändert.
    """
    if law not in LAWS and law not in EU_LAWS:
        return text
    out, pos = [], 0
    for m in CITATION.finditer(text):
        if m.group(4):
            continue
        out.append(text[pos:m.end()] + " " + law)
        pos = m.end()
    return "".join(out) + text[pos:]


def url_for(nummer, law=DEFAULT_LAW, artikel=None):
    """URL der Einzelvorschrift, oder None, wenn das Gesetz nicht verlinkbar ist.
    `artikel`: römische Artikelnummer beim IntPatÜG (Art. II § 6 -> intpat_bkg/art_ii__6.html)."""
    entry = LAWS.get(law)
    if not entry:
        return None
    slug, kind = entry
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


def linkify(text, fmt="html", escape=None):
    """Ersetzt Gesetzeszitate durch Links.

    fmt="html"     -> <a href="…" class="lawlink">§ 14 MarkenG</a>
    fmt="markdown" -> [§ 14 MarkenG](…)
    escape         -> optionale Funktion für den Text außerhalb der Zitate
    """
    def repl(m):
        head, nums, law = m.group(1), m.group(2), m.group(4)
        label = m.group(0)
        if law in UNLINKED:
            return label
        if law in EU_LAWS:
            return _link(None, law, label, fmt)
        rm = _ROMAN_HEAD.match(head)
        if rm:  # Art. II § 6 IntPatÜG
            found = _NUM.findall(nums)
            return _link(found[0], law, label, fmt, rm.group(1)) if law in LAWS and found else label
        if head in RULE_HEADS or (head == "Art." and law != "GG"):
            return label
        target = law or DEFAULT_LAW
        if target not in LAWS:
            return label
        found = _NUM.findall(nums)
        if not found:
            return label
        if head == "§§" and len(found) > 1:
            rest, out, pos = label[len(head):], head, 0
            for n in found:
                i = rest.index(n, pos)
                out += rest[pos:i] + _link(n, target, n, fmt)
                pos = i + len(n)
            return out + rest[pos:]
        return _link(found[0], target, label, fmt)

    parts, last = [], 0
    for m in CITATION.finditer(text):
        chunk = text[last:m.start()]
        parts.append(escape(chunk) if escape else chunk)
        parts.append(repl(m))
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
        "eu": EU_LAWS,
        "default": DEFAULT_LAW,
        "eukeys": EU_NORM_KEYS,
        "dekeys": DE_NORM_KEYS,
        "ruleheads": list(RULE_HEADS),
    }


JS_TEMPLATE = """
// ---- Gesetzeslinks auf gesetze-im-internet.de (erzeugt aus src/knowledge/gesetze.py) ----
const LAW = __LAWDATA__;
const LAWABBR = Object.keys(LAW.laws).concat(Object.keys(LAW.eu), LAW.unlinked).sort((a, b) => b.length - a.length).join('|');
const CITE = new RegExp(__PATTERN__, 'g');
function lawUrl(num, law){ const e = LAW.laws[law]; if(!e) return null;
  return LAW.base + e.slug + '/' + (e.kind === 'Art.' ? 'art_' + num + '.html' : '__' + num + '.html'); }
function lawA(href, label){ var eu = href.indexOf('eur-lex') >= 0, upc = href.indexOf('unifiedpatentcourt') >= 0, epo = href.indexOf('epo.org') >= 0;
  return '<a href="' + href + '" target="_blank" rel="noopener" class="lawlink"'
  + ' title="' + (upc ? 'Verfahrensordnung des EPG (PDF)' : epo ? 'Auf epo.org nachlesen' : eu ? 'Auf EUR-Lex nachlesen' : 'Auf gesetze-im-internet.de nachlesen') + '">' + label + '</a>'; }
function lawifyText(s){
  return s.replace(CITE, function(m, head, nums, sub, law){
    if(law && LAW.unlinked.indexOf(law) >= 0) return m;
    if(law && LAW.eu[law]) return lawA(LAW.eu[law], m);
    if(LAW.ruleheads.indexOf(head) >= 0 || (head === 'Art.' && law !== 'GG')) return m;
    var target = law || LAW.default; if(!LAW.laws[target]) return m;
    var found = nums.match(NUMRE) || []; if(!found.length) return m;
    if(head === '\\u00a7\\u00a7' && found.length > 1){
      var rest = m.slice(head.length), o = head, pos = 0;
      for(var i = 0; i < found.length; i++){ var n = found[i], at = rest.indexOf(n, pos);
        o += rest.slice(pos, at) + lawA(lawUrl(n, target), n); pos = at + n.length; }
      return o + rest.slice(pos);
    }
    var href = lawUrl(found[0], target); return href ? lawA(href, m) : m;
  });
}
function lawify(html){ if(html == null) return ''; var s = String(html);
  if(s.indexOf('class="lawlink"') >= 0) return s;
  return s.split(/(<[^>]*>)/).map(function(p, i){ return i % 2 ? p : lawifyText(p); }).join(''); }
"""


def js_source():
    """JavaScript-Fassung der Verlinkung: gleiche Tabelle, gleiches Muster."""
    js_pattern = json.dumps(_PATTERN)                       # Backslashes/Quotes korrekt escapen
    js_pattern = js_pattern.replace("(" + _ABBR + ")", '(" + LAWABBR + ")')
    return (JS_TEMPLATE
            .replace("__LAWDATA__", json.dumps(js_table(), ensure_ascii=False))
            .replace("__PATTERN__", js_pattern)
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
    ]
    for p in proben:
        print(linkify(p, "markdown"))
    print(qualify("§ 140b, § 139 Abs. 1 S. 3 bis 5, § 140a Abs. 1 bis 4; § 9 Abs. 2 (§§ 24a bis 24e GebrMG)", "PatG"))
