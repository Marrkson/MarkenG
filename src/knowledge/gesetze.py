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
    "GebrMG": ("gebrmg", "§"),
    "HGB": ("hgb", "§"),
    "TMG": ("tmg", "§"),
    "GKG": ("gkg_2004", "§"),
    "MarkenV": ("markenv_2004", "§"),
    "DPMAV": ("dpmav", "§"),
    "PAO": ("pao", "§"),
    "StGB": ("stgb", "§"),
    "GWB": ("gwb", "§"),
}

DEFAULT_LAW = "MarkenG"
# Unionsrecht: nicht auf gesetze-im-internet.de, aber auf EUR-Lex (Link auf das Gesamtdokument).
EU_LAWS = {
    "MarkenRL": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2436",
    "UMV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1001",
    "AEUV": "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016E/TXT",
}
# Ohne verlinkbare Fundstelle: nie verlinken.
UNLINKED = ("GMV", "PMMA", "MMA", "PVÜ", "TRIPS", "EUV", "DSGVO", "GGV", "EPÜ")

_ABBR = "|".join(sorted(list(LAWS) + list(EU_LAWS) + list(UNLINKED), key=len, reverse=True))
_PATTERN = (
    r"(§§|§|Art\.)\s*"
    r"(\d+[a-z]?(?:\s*(?:bis|,|und|ff\.|f\.|/|-|–)\s*\d+[a-z]?)*)"
    r"((?:\s+(?:Abs\.|Absatz|Nr\.|Nummer|Satz|S\.|lit\.|Halbsatz|Alt\.)\s*[\w§]+)*)"
    r"(?:\s+(" + _ABBR + r"))?"
)
CITATION = re.compile(_PATTERN)
_NUM = re.compile(r"\d+[a-z]?")


def url_for(nummer, law=DEFAULT_LAW):
    """URL der Einzelvorschrift, oder None, wenn das Gesetz nicht verlinkbar ist."""
    entry = LAWS.get(law)
    if not entry:
        return None
    slug, kind = entry
    datei = "art_%s.html" % nummer if kind == "Art." else "__%s.html" % nummer
    return BASE + slug + "/" + datei


def _link(nummer, law, label, fmt):
    href = EU_LAWS.get(law) or url_for(nummer, law)
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
        if head == "Art." and law != "GG":
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
    }


JS_TEMPLATE = """
// ---- Gesetzeslinks auf gesetze-im-internet.de (erzeugt aus src/knowledge/gesetze.py) ----
const LAW = __LAWDATA__;
const LAWABBR = Object.keys(LAW.laws).concat(Object.keys(LAW.eu), LAW.unlinked).sort((a, b) => b.length - a.length).join('|');
const CITE = new RegExp(__PATTERN__, 'g');
function lawUrl(num, law){ const e = LAW.laws[law]; if(!e) return null;
  return LAW.base + e.slug + '/' + (e.kind === 'Art.' ? 'art_' + num + '.html' : '__' + num + '.html'); }
function lawA(href, label){ var eu = href.indexOf('eur-lex') >= 0;
  return '<a href="' + href + '" target="_blank" rel="noopener" class="lawlink"'
  + ' title="' + (eu ? 'Auf EUR-Lex nachlesen' : 'Auf gesetze-im-internet.de nachlesen') + '">' + label + '</a>'; }
function lawifyText(s){
  return s.replace(CITE, function(m, head, nums, sub, law){
    if(law && LAW.unlinked.indexOf(law) >= 0) return m;
    if(law && LAW.eu[law]) return lawA(LAW.eu[law], m);
    if(head === 'Art.' && law !== 'GG') return m;
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
    ]
    for p in proben:
        print(linkify(p, "markdown"))
