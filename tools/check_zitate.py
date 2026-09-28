#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prüft alle Gesetzeszitate der Inhalte so, wie die Apps sie verlinken (src/knowledge/gesetze.py: resolve/href_for).

Geprüft wird
  1. unbekannte Normen in `norms=[…]`/`umsetzung=[…]` (Graph),
  2. Zitate ohne Gesetzesangabe in Inhalten der Pakete Patent, Design und EPG (dort gibt es kein Kontextgesetz),
  3. ob der Paragraph/Artikel im geltenden Gesetz existiert und nicht weggefallen ist,
  4. ob zitierte Absätze („Abs. 3“) und Nummern/Buchstaben („Nr. 2“, „lit. c“) im Normtext vorkommen,
  5. welche Zitate unverlinkt bleiben (unbekanntes Gesetz).
Normtexte: data/*.json (MarkenG, PatG, PatV, IntPatÜG, PatKostG, DesignG, DesignV) und für alle übrigen Gesetze der
gesetze-im-internet-XML im Cache ~/.cache/ipelico/gesetze/ (mit --net nachladen).

Aufruf:  python3 tools/check_zitate.py [--net] [--paket marken|patent|design|upc|texte] [--alle] [--json DATEI]
Ausgabe: Befunde je Knoten; Exit-Code 1 bei Fehlern (Warnungen: unverlinkte Zitate, fehlende Normtexte).
"""
import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

import build_graph  # noqa: E402
import fetch_patent  # noqa: E402
from knowledge.gesetze import LAWS, EU_LAWS, ARTICLE_URLS, DEFAULT_LAW, RULE_HEADS, G_HEAD, G_NUMS, G_SUB, _ROMAN_HEAD, resolve, href_for, _NUM  # noqa: E402
from knowledge.kurse import KURSE  # noqa: E402
from knowledge.klausur import DATA as KLAUSUR  # noqa: E402

CACHE = Path.home() / ".cache" / "ipelico" / "gesetze"
LOCAL = {"MarkenG": "markeng", "PatG": "patg", "PatV": "patv", "IntPatÜG": "intpatueg", "IntPatÜbkG": "intpatueg",
         "PatKostG": "patkostg", "DesignG": "designg", "DesignV": "designv"}
PAKET_LAW = {"marken": DEFAULT_LAW, "patent": None, "design": None, "upc": None}
SKIP_KEYS = {"url", "url_pdf", "url_en", "id", "icon", "farbe", "concepts", "cases", "distinctions", "norms", "related",
             "ipwiki", "quellen", "tags", "az", "date", "court", "fundstelle", "rl", "korpus", "type", "schema", "step",
             "umsetzung", "entspricht", "bezug", "typ", "level", "order", "gebiet"}


# ------------------------------------------------------------------ Normtexte
def _xml_law(abbr, net):
    slug = LAWS[abbr][0]
    target = CACHE / (slug + ".json")
    if target.exists():
        return json.loads(target.read_text())
    if not net:
        return None
    raw = urllib.request.urlopen(urllib.request.Request(fetch_patent.BASE + slug + "/xml.zip", headers=fetch_patent.UA), timeout=60).read()
    zf = zipfile.ZipFile(io.BytesIO(raw))
    xml = zf.read([n for n in zf.namelist() if n.endswith(".xml")][0]).decode("utf-8")
    out = {}
    for _, body in re.findall(r"<norm (.*?)>(.*?)</norm>", xml, re.S):
        enbez = fetch_patent._clean(fetch_patent._inner("enbez", body))
        m = re.match(r"^(?:§|Art\.?)\s*(\d+[a-z]*)$", enbez)
        if not m:
            continue
        key = m.group(1)
        # Artikelgesetze mit Paragraphen (EGBGB: „Art. 229 § 6“): Schlüssel „229 6“ wie beim IntPatÜG („II 6“)
        ga = re.match(r"^Art\.?\s+([IVX]+|\d+)$", fetch_patent._clean(fetch_patent._inner("gliederungsbez", body)))
        if enbez.startswith("§") and ga and LAWS[abbr][1] == "Art.":
            key = ga.group(1) + " " + key
        ab = fetch_patent.parse_norm(body)
        out[key] = dict(titel=fetch_patent._clean(fetch_patent._inner("titel", body)), abs=[a["nr"] for a in ab],
                               absaetze=ab)
    CACHE.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, ensure_ascii=False))
    return out


def load_texts(net):
    texts = {}
    for abbr in LAWS:
        if abbr in LOCAL:
            d = json.loads((ROOT / "data" / (LOCAL[abbr] + ".json")).read_text())
            texts[abbr] = {(p.get("nummer") or p.get("nr")): dict(titel=p["titel"], abs=[a["nr"] for a in p["absaetze"]], absaetze=p["absaetze"])
                           for p in d["paragraphen"]}
        else:
            try:
                texts[abbr] = _xml_law(abbr, net)
            except Exception as e:  # noqa: BLE001
                print("Normtext nicht ladbar:", abbr, e, file=sys.stderr)
                texts[abbr] = None
    return texts


# ------------------------------------------------------------------ Struktur eines Zitats
_SUB = re.compile(r"(Abs\.|Absatz|Nr\.|Nummer|lit\.|Buchst\.)\s*(\d+[a-z]?|[a-z](?![\w]))((?:\s*(?:,|und|bis|/|–|-)\s*(?:\d+[a-z]?|[a-z])(?![\w.]))*)")


def _subparts(sub):
    """„Abs. 2 Nr. 3, 4 S. 1“ -> [("abs", ["2"]), ("nr", ["3", "4"])] (Ketten: nur Endpunkte bei „bis“)."""
    out = []
    for kind, first, rest in _SUB.findall(sub or ""):
        vals = [first] + re.findall(r"\d+[a-z]?|\b[a-z]\b", rest)
        out.append(({"Abs.": "abs", "Absatz": "abs", "Nr.": "nr", "Nummer": "nr", "lit.": "lit", "Buchst.": "lit"}[kind], vals))
    return out


def _has_item(text, val, kind):
    if kind == "nr":
        return re.search(r"(?m)^\s*%s\.(?:\s|$)" % re.escape(val), text) is not None
    return re.search(r"(?m)^\s*%s\)" % re.escape(val), text) is not None


def check_structure(m, law, texts):
    """Liste von Befunden (Text) für ein Zitat mit Gesetz aus LAWS."""
    t = texts.get(law)
    if t is None:
        return []
    head, nums, sub = m.group(G_HEAD), m.group(G_NUMS), m.group(G_SUB)
    if head in RULE_HEADS or (head == "Art." and LAWS[law][1] != "Art."):
        return []
    roman = _ROMAN_HEAD.match(head)
    found = _NUM.findall(nums)
    probs = []
    for i, n in enumerate(found):
        key = (roman.group(1) + " § " + n) if roman else n
        if law in ("IntPatÜG", "IntPatÜbkG") and not roman:
            continue
        p = t.get(key) if not roman else t.get(key) or t.get(roman.group(1) + " " + n)
        if p is None:
            probs.append("%s %s %s existiert nicht" % ("§" if LAWS[law][1] == "§" else "Art.", key, law))
            continue
        if "(weggefallen)" in (p["titel"] or "") or (p["absaetze"] and p["absaetze"][0]["text"].strip() in ("(weggefallen)", "-")):
            probs.append("%s %s ist weggefallen" % (key, law))
            continue
        if i:  # Untergliederung gehört nur zum ersten Paragraphen
            continue
        parts = _subparts(sub)
        cur = p["absaetze"]
        for kind, vals in parts:
            if kind == "abs":
                have = [a["nr"] for a in p["absaetze"]]
                miss = [v for v in vals if v not in have]
                if miss:
                    probs.append("%s %s: Abs. %s gibt es nicht (Absätze: %s)" % (key, law, ", ".join(miss), ", ".join(x for x in have if x) or "keine"))
                    break
                cur = [a for a in p["absaetze"] if a["nr"] in vals]
            else:
                text = "\n".join(a["text"] for a in cur)
                miss = [v for v in vals if not _has_item(text, v, kind)]
                if miss:
                    probs.append("%s %s%s: %s %s nicht gefunden" % (key, law, "" if cur is p["absaetze"] else " (im zitierten Absatz)",
                                                                   "Nr." if kind == "nr" else "lit.", ", ".join(miss)))
                    break
    return probs


# ------------------------------------------------------------------ Inhalte einsammeln
def _paket_of_id(nid, node=None):
    s = nid.split(":", 1)[1] if ":" in nid else nid
    for pre, pk in (("d_pat_", "patent"), ("pat_", "patent"), ("d_des_", "design"), ("des_", "design"), ("d_upc_", "upc"), ("upc_", "upc")):
        if s.startswith(pre):
            return pk
    if node is not None and node.get("type") == "source" and node.get("provider") not in (None, "IPWiki"):
        return "upc"
    return "marken"


def _hinweis_law(n):
    """wie hinweisLaw() in den Apps"""
    return "MarkenG" if n.get("rl") == "markenrl" else _norm_law(n)


def _norm_law(n):
    """wie normLaw() in den Apps"""
    return n["kurz"] if n.get("kurz") in LAWS or n.get("kurz") in EU_LAWS or n.get("kurz") in ARTICLE_URLS else None


def items(graph):
    """(paket, knoten, feld, text, kontextgesetz) für alle Texte der Apps."""
    nodes = {n["id"]: n for n in graph["nodes"]}
    parent = {e["target"]: e["source"] for e in graph["edges"] if e["relation"] in ("has_unit", "has_chapter", "has_step")}

    def paket(nid):
        n = nodes[nid]
        while nid in parent and n["type"] in ("unit", "chapter", "step"):
            nid = parent[nid]
            n = nodes[nid]
        if n["type"] == "course":
            return {"k": "marken", "p": "patent", "d": "design", "u": "upc"}[n["id"].split(":")[1][0]]
        return _paket_of_id(nid, n)

    def walk(v, path, emit):
        if isinstance(v, str):
            emit(path, v)
        elif isinstance(v, list):
            for x in v:
                walk(x, path, emit)
        elif isinstance(v, dict):
            for k, x in v.items():
                if k not in SKIP_KEYS:
                    walk(x, (path + "." if path else "") + k, emit)

    out = []
    for n in graph["nodes"]:
        if n["type"] in ("norm", "eunorm"):
            law = "MarkenG" if n["type"] == "norm" else _norm_law(n)
            pk = "texte"
            for f in ("absaetze", "text"):
                walk(n.get(f), f, lambda p, s: out.append((pk, n["id"], p, s, law)))
            walk(n.get("hinweis"), "hinweis", lambda p, s: out.append((pk, n["id"], p, s, "MarkenG" if n["type"] == "norm" else _hinweis_law(n))))
            for k, s in (n.get("umsetzung_weitere") or {}).items():
                out.append((pk, n["id"], "umsetzung_weitere." + k, s, k if k in LAWS else None))
            continue
        if n["type"] in ("unit", "chapter", "course"):
            continue  # Kursinhalte kommen vollständig aus KURSE
        pk = paket(n["id"])
        walk({k: v for k, v in n.items() if k not in ("label",) or n["type"] != "case"}, "",
             lambda p, s: out.append((pk, n["id"], p, s, PAKET_LAW[pk])))
    for k in KURSE:
        pk = {"k": "marken", "p": "patent", "d": "design", "u": "upc"}[k["id"][0]]
        walk({x: y for x, y in k.items() if x != "kapitel"}, "", lambda p, s: out.append((pk, "course:" + k["id"], p, s, PAKET_LAW[pk])))
        for c in k["kapitel"]:
            walk({x: y for x, y in c.items() if x != "einheiten"}, "", lambda p, s: out.append((pk, "chapter:" + c["id"], p, s, PAKET_LAW[pk])))
            for u in c["einheiten"]:
                walk(u, "", lambda p, s: out.append((pk, "unit:" + u["id"], p, s, PAKET_LAW[pk])))
    walk(KLAUSUR, "", lambda p, s: out.append(("marken", "klausur", p, s, DEFAULT_LAW)))
    for f, key, pk in (("patent_entscheidungen.json", "ls", "patent"), ("design_entscheidungen.json", "ls", "design"),
                       ("upc_entscheidungen.json", "leitsatz", "upc")):
        d = json.loads((ROOT / "docs" / f).read_text())
        for e in d.get("entscheidungen", []):
            if e.get(key):
                out.append(("leitsaetze", "%s %s" % (e.get("g", ""), e.get("az", "")), key, e[key], None))
    return out


def update_paragraphen(texts):
    """data/gesetze_paragraphen.json: bestehende (nicht weggefallene) Vorschriften je Gesetz für den Link-Filter der Apps."""
    out = {}
    for abbr, t in sorted(texts.items()):
        if not t:
            continue
        keys = [k.replace(" § ", " ") for k, p in t.items()
                if "(weggefallen)" not in (p["titel"] or "") and not (p["absaetze"] and p["absaetze"][0]["text"].strip() in ("(weggefallen)", "-"))]
        out[abbr] = sorted(set(keys), key=lambda k: (len(k), k))
    target = ROOT / "data" / "gesetze_paragraphen.json"
    target.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n")
    print("->", target.relative_to(ROOT), sum(len(v) for v in out.values()), "Vorschriften in", len(out), "Gesetzen")


def main():
    net = "--net" in sys.argv
    alle = "--alle" in sys.argv
    only = sys.argv[sys.argv.index("--paket") + 1] if "--paket" in sys.argv else None
    unknown = []
    graph = build_graph.build(write=False, unknown=unknown)
    texts = load_texts(net)
    if "--update" in sys.argv:
        update_paragraphen(texts)
    befunde = []  # (schwere, paket, knoten, feld, zitat, befund, umgebung)
    for src, ref in unknown:
        if only and _paket_of_id(src) != only:
            continue
        befunde.append(("FEHLER", _paket_of_id(src), src, "norms", ref, "unbekannte Norm (Graph)", ""))
    seen = set()
    for pk, nid, field, text, ctx in items(graph):
        if only and pk != only:
            continue
        for m, law, how in resolve(text, ctx):
            around = text[max(0, m.start() - 60):m.end() + 30].replace("\n", " ")
            key = (nid, field, m.start(), text[:40])
            if key in seen:
                continue
            seen.add(key)
            cite = m.group(0)
            if how == "alte Fassung":
                continue
            href = href_for(m, law)
            content = pk in ("marken", "patent", "design", "upc")
            if law == "":
                befunde.append(("WARNUNG", pk, nid, field, cite, "nicht verlinkbares Gesetz", around))
                continue
            if not law or (how == "kontext" and href is None):
                befunde.append(("FEHLER" if content else "WARNUNG", pk, nid, field, cite, "Gesetzesangabe fehlt", around))
                continue
            probs = check_structure(m, law, texts) if law in LAWS else []
            for p in probs:
                if pk in ("texte", "leitsaetze") and ("gibt es nicht" in p or "nicht gefunden" in p):
                    continue  # amtlicher Wortlaut/Leitsatz: Untergliederung älterer Fassungen nicht beanstanden
                # Amtliche Texte und Leitsätze zitieren zu Recht aufgehobene Vorschriften (§ 177 PAO, § 125e MarkenG a.F.);
                # sie bleiben unverlinkt (kein 404) und sind kein Fehler unserer Inhalte
                befunde.append(("WARNUNG" if pk in ("texte", "leitsaetze") else "FEHLER", pk, nid, field, cite,
                                p + ("" if how == "genannt" else " [Gesetz aus %s]" % how), around))
            if href is None and not probs:
                befunde.append(("FEHLER" if content else "WARNUNG", pk, nid, field, cite, "kein Link (%s)" % law, around))
            if alle:
                befunde.append(("INFO", pk, nid, field, cite, "%s (%s) -> %s" % (law, how, href_for(m, law)), around))
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(befunde, ensure_ascii=False, indent=0))
    fehler = [b for b in befunde if b[0] == "FEHLER"]
    for b in befunde:
        if b[0] != "INFO":
            print("%s [%s] %s (%s): %s – %s\n    …%s…" % b)
    print("\n%d Fehler, %d Warnungen" % (len(fehler), sum(1 for b in befunde if b[0] == "WARNUNG")))
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
