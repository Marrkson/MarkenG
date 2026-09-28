# -*- coding: utf-8 -*-
"""Baut den Wissensgraphen zum deutschen Markenrecht.

Knoten-Typen:
  norm         Paragraph des MarkenG (Volltext aus data/markeng.json)
  concept      Begriff / Definition
  schema       Prüfungsschema
  step         Prüfungsschritt (Baum unter einem Schema)
  case         Gerichtsentscheidung (BGH/EuGH)
  distinction  Abgrenzung mehrerer Begriffe
  source       IPWiki-Artikel

Kanten (source -> target, relation):
  concept  -[defined_in]->     norm
  concept  -[related_to]->     concept
  concept  -[illustrated_by]-> case
  concept  -[documented_in]->  source
  case     -[interprets]->     norm
  schema   -[has_step]->       step        (order)
  step     -[has_step]->       step        (order)
  step     -[next_step]->      step
  step     -[uses_concept]->   concept
  step     -[cites]->          case
  step     -[applies]->        norm
  schema   -[applies]->        norm
  distinction -[contrasts]->   concept
  course   -[has_chapter]->    chapter     (order)
  chapter  -[has_unit]->       unit        (order)
  unit     -[trains]->         concept
  unit     -[cites]->          case
  unit     -[applies]->        norm
  unit     -[covers]->         step | schema
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from knowledge.cases import CASES  # noqa: E402
from knowledge.concepts import CONCEPTS  # noqa: E402
from knowledge.distinctions import DISTINCTIONS  # noqa: E402
from knowledge.ipwiki import IPWIKI, IPWIKI_BASE  # noqa: E402
from knowledge.schemata import SCHEMATA  # noqa: E402
from knowledge.kurse import KURSE  # noqa: E402
from knowledge import markenrl, durchsetzungsrl  # noqa: E402
from knowledge import upc  # noqa: E402  (zweites Wissenspaket: EPGÜ, VerfO, EPG-Entscheidungen)
from knowledge import patent  # noqa: E402  (drittes Wissenspaket: PatG, PatV, IntPatÜG, PatKostG, BPatG-/BGH-Rechtsprechung)
from knowledge import design  # noqa: E402  (viertes Wissenspaket: DesignG, DesignV, DesignRL, GGV, Design-Rechtsprechung)
from knowledge.gesetze import EU_NORM_KEYS, DE_NORM_KEYS, RULE_HEADS  # noqa: E402

# Alle Wissenspakete in einem Graphen; IDs des UPC-Pakets sind mit upc_ / d_upc_, die des Patentpakets mit pat_ / d_pat_,
# die des Designpakets mit des_ / d_des_ präfixiert.
CASES = CASES + upc.CASES + patent.CASES + design.CASES
CONCEPTS = CONCEPTS + upc.CONCEPTS + patent.CONCEPTS + design.CONCEPTS
DISTINCTIONS = DISTINCTIONS + upc.DISTINCTIONS + patent.DISTINCTIONS + design.DISTINCTIONS
SCHEMATA = SCHEMATA + upc.SCHEMATA + patent.SCHEMATA + design.SCHEMATA

STATUTE = ROOT / "data" / "markeng.json"
OUT = ROOT / "graph" / "markenrecht_graph.json"

# EU-Richtlinien: Knoten-IDs `eunorm:<key>:<nr>`, Zitierform `Art. <nr> … <kurz>`
RICHTLINIEN = [
    dict(key="markenrl", kurz="MarkenRL", titel="Markenrechtsrichtlinie (EU) 2015/2436", gesetz="Richtlinie (EU) 2015/2436",
         artikel=markenrl.ARTIKEL, erwaegungsgruende=markenrl.ERWAEGUNGSGRUENDE, url=markenrl.URL, url_pdf=markenrl.URL_PDF, paraphrase=True,
         hinweis="Artikel der Richtlinie (EU) 2015/2436 sind als Paraphrase erfasst (amtlicher Wortlaut aus der Build-Umgebung nicht abrufbar)."),
    dict(key="durchsetzungsrl", kurz="DurchsetzungsRL", titel="Durchsetzungsrichtlinie 2004/48/EG", gesetz="Richtlinie 2004/48/EG",
         artikel=durchsetzungsrl.ARTIKEL, erwaegungsgruende=durchsetzungsrl.ERWAEGUNGSGRUENDE, url=durchsetzungsrl.URL, url_pdf=durchsetzungsrl.URL_PDF, paraphrase=False,
         hinweis="Artikel der Richtlinie 2004/48/EG im amtlichen Wortlaut der berichtigten Fassung (ABl. L 195 vom 2.6.2004, S. 16); Buchstabenaufzählungen in den Absatztext eingerückt."),
    # Einheitliches Patentgericht: Übereinkommen und Verfahrensordnung als weitere „eunorm“-Familien (Zitierform Art. 33 EPGÜ, R. 19 VerfO)
    dict(key="upca", kurz=upc.upca.KURZ, titel=upc.upca.TITEL, gesetz=upc.upca.GESETZ, artikel=upc.upca.ARTIKEL,
         erwaegungsgruende=upc.upca.ERWAEGUNGSGRUENDE, url=upc.upca.URL, url_pdf=upc.upca.URL_PDF, paraphrase=False, zitat="Art.",
         hinweis="Amtlicher deutscher Wortlaut des EPGÜ (epo.org, Fassung 2022); englischer Titel und Wortlaut je Artikel hinterlegt."),
    dict(key="rop", kurz=upc.rop.KURZ, titel=upc.rop.TITEL, gesetz=upc.rop.GESETZ, artikel=upc.rop.REGELN,
         erwaegungsgruende=upc.rop.ERWAEGUNGSGRUENDE, url=upc.rop.URL, url_pdf=upc.rop.URL_PDF, paraphrase=False, zitat="R.",
         hinweis="Deutscher Wortlaut der konsolidierten Verfahrensordnung (unifiedpatentcourt.org, Änderungen vom 4.11.2025 in Kraft seit 1.1.2026); Präambel als Sammelknoten."),
    # Einheitspatent: EPatVO, EPatÜVO, DOEPS, GebOEPS (src/knowledge/upc/einheitspatent.py; Zitierform Art. 3 EPatVO, R. 6 DOEPS)
    *upc.einheitspatent.FAMILIEN,
    # Patentrecht: PatG, PatV, IntPatÜG, PatKostG als deutsche Normfamilien (src/knowledge/patent/gesetze_texte.py; Zitierform § 3 PatG, Art. II § 6 IntPatÜG)
    *patent.gesetze_texte.FAMILIEN,
    # Designrecht: DesignG, DesignV (deutsche Normfamilien, Zitierform § 2 DesignG), Richtlinie 98/71/EG, Richtlinie (EU) 2024/2823 und
    # die Verordnung über Unionsgeschmacksmuster (Zitierform Art. 5 DesignRL, Art. 19 DesignRL 2024, Art. 8 GGV)
    *design.gesetze_texte.FAMILIEN,
    *design.eurecht.FAMILIEN,
]
RL_BY_KURZ = {r["kurz"]: r["key"] for r in RICHTLINIEN}
RL_BY_KURZ.update({k: v for k, v in EU_NORM_KEYS.items() if v in {r["key"] for r in RICHTLINIEN}})
RL_ZITAT = {r["key"]: r.get("zitat", "Art.") for r in RICHTLINIEN}
_DE_KEYS = {k: v for k, v in DE_NORM_KEYS.items() if v in {r["key"] for r in RICHTLINIEN}}
_ART_KEYS = [k for k, v in RL_BY_KURZ.items() if RL_ZITAT[v] == "Art." and k not in _DE_KEYS]
_RULE_KEYS = [k for k, v in RL_BY_KURZ.items() if RL_ZITAT[v] == "R."]

NORM_RE = re.compile(r"§ (\d+[a-z]?)")
EUNORM_RE = re.compile(r"Art\. (\d+[a-z]?)(?: .*)? (" + "|".join(_ART_KEYS) + r")$")
RULE_RE = re.compile(r"(?:" + "|".join(re.escape(h) for h in RULE_HEADS) + r") (\d+[A-Za-z]?)(?:\.\d+)*(?:\([a-z0-9]+\))*(?: .*)? (" + "|".join(_RULE_KEYS) + r")$")
DENORM_RE = re.compile(r"§ (\d+[a-z]?)(?: .*)? (" + "|".join(_DE_KEYS) + r")$")
ROMAN_RE = re.compile(r"Art\. ([IVX]+)(?: § (\d+[a-z]?))?(?: .*)? (" + "|".join(_DE_KEYS) + r")$")
ANLAGE_RE = re.compile(r"Anlage(?: (\d+))? (" + "|".join(_DE_KEYS) + r")$")


def norm_id(ref: str) -> str:
    """'§ 14 Abs. 2 Nr. 2' -> 'norm:§14'; 'Art. 10 Abs. 2 MarkenRL' -> 'eunorm:markenrl:10';
    'Art. 8 Abs. 3 lit. e DurchsetzungsRL' -> 'eunorm:durchsetzungsrl:8'; 'Art. 33 Abs. 1 EPGÜ' -> 'eunorm:upca:33';
    'R. 262A.1 VerfO' / 'Rule 19 RoP' -> 'eunorm:rop:262A' / 'eunorm:rop:19';
    '§ 3 Abs. 1 PatG' -> 'eunorm:patg:3'; 'Art. II § 6 Abs. 1 Nr. 3 IntPatÜG' -> 'eunorm:intpatueg:II§6'; 'Anlage PatKostG' -> 'eunorm:patkostg:anlage'"""
    m = DENORM_RE.match(ref)
    if m:
        return f"eunorm:{_DE_KEYS[m.group(2)]}:{m.group(1)}"
    m = ROMAN_RE.match(ref)
    if m:
        return f"eunorm:{_DE_KEYS[m.group(3)]}:{m.group(1)}" + (f"§{m.group(2)}" if m.group(2) else "")
    m = ANLAGE_RE.match(ref)
    if m:
        return f"eunorm:{_DE_KEYS[m.group(2)]}:anlage" + (f"_{m.group(1)}" if m.group(1) else "")
    m = EUNORM_RE.match(ref)
    if m:
        return f"eunorm:{RL_BY_KURZ[m.group(2)]}:{m.group(1)}"
    m = RULE_RE.match(ref)
    if m:
        return f"eunorm:{RL_BY_KURZ[m.group(2)]}:{m.group(1).upper()}"
    m = NORM_RE.match(ref)
    if not m:
        raise ValueError(ref)
    return f"norm:§{m.group(1)}"


def case_url(c):
    if c.get("url"):
        return c["url"]
    d, m, y = c["date"].split("-")[::-1]
    az = c["az"].replace(" ", "+")
    return (f"https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht={c['court']}"
            f"&Datum={d}.{m}.{y}&Aktenzeichen={az}")


def build(write=True, unknown=None):
    """Baut den Graphen; `write=False` nur im Speicher (tools/check_zitate.py). `unknown`: Liste, in der unbekannte
    Normzitate gesammelt werden, statt den Build abzubrechen."""
    statute = json.loads(STATUTE.read_text(encoding="utf-8"))
    nodes, edges = [], []
    seen = set()

    def add_node(n):
        if n["id"] in seen:
            raise ValueError("doppelte Knoten-ID " + n["id"])
        seen.add(n["id"])
        nodes.append(n)

    def add_edge(s, t, rel, **attrs):
        edges.append(dict(source=s, target=t, relation=rel, **attrs))

    # --- Normen ---
    for p in statute["paragraphen"]:
        add_node(dict(id=f"norm:§{p['nummer']}", type="norm", label=f"{p['id']} MarkenG", titel=p["titel"],
                      nummer=p["nummer"], teil=p["teil"], abschnitt=p["abschnitt"],
                      absaetze=p["absaetze"], text=p["text"],
                      url=f"https://www.gesetze-im-internet.de/markeng/__{p['nummer']}.html"))
    # --- EU-Richtlinien (MarkenRL, DurchsetzungsRL) ---
    zitiert = upc.entscheidungen.zitierungen()
    zitiert_pat = patent.entscheidungen.zitierungen()
    zitiert_des = design.entscheidungen.zitierungen()
    for rl in RICHTLINIEN:
        zitat = rl.get("zitat", "Art.")
        common = dict(type="eunorm", rl=rl["key"], kurz=rl["kurz"], gesetz=rl["gesetz"], url=rl["url"], url_pdf=rl["url_pdf"], paraphrase=rl["paraphrase"], zitat=zitat)
        if rl.get("korpus"):
            common["korpus"] = rl["korpus"]  # Entscheidungskorpus für Zitierzähler und Rechtsprechungsansicht (patent)
        for a in rl["artikel"]:
            nid = f"eunorm:{rl['key']}:{a['nr'].replace(' ', '')}"
            node = dict(id=nid, label=a.get("label") or f"{zitat} {a['nr']} {rl['kurz']}", titel=a["titel"],
                        nummer=a["nr"], kapitel=a["kapitel"], abschnitt=a["abschnitt"], absaetze=a["absaetze"], hinweis=a["hinweis"],
                        umsetzung_weitere=a.get("umsetzung_weitere", {}), **common)
            for extra in ("titel_en", "url_en", "order"):  # englischer Wortlaut nur per Link (url_en), sonst verdoppelt sich die App-Größe
                if a.get(extra):
                    node[extra] = a[extra]
            if a.get("url"):
                node["url"] = a["url"]
            if rl["key"] in ("upca", "rop"):
                node["zitiert"] = zitiert.get(nid, 0)
            if rl.get("korpus") == "patent":
                node["zitiert"] = zitiert_pat.get(nid, 0)
            if rl.get("korpus") == "design":
                node["zitiert"] = zitiert_des.get(nid, 0)
            add_node(node)
        if rl["erwaegungsgruende"]:
            add_node(dict(id=f"eunorm:{rl['key']}:erwaegungsgruende", label=("Präambel " if zitat == "R." else "Erwägungsgründe ") + rl["kurz"],
                          titel="Präambel" if zitat == "R." else "Erwägungsgründe (Auswahl)",
                          nummer="0", kapitel="Präambel", abschnitt=None,
                          absaetze=[dict(nr=e["nr"], text=e["text"]) for e in rl["erwaegungsgruende"]], hinweis="", umsetzung_weitere={}, **common))
    norm_ids = {n["id"] for n in nodes}

    def fehler(msg, src, ref):
        if unknown is None:
            raise ValueError(msg)
        unknown.append((src, ref))
    # PatG und DesignG setzen die Durchsetzungsrichtlinie um: Kanten aus durchsetzungsrl.umsetzung_weitere (nur Zitate, keine Verneinungen)
    for gesetz, key in (("PatG", "patg"), ("DesignG", "designg")):
        for a in durchsetzungsrl.ARTIKEL:
            txt = a.get("umsetzung_weitere", {}).get(gesetz, "")
            if not txt or txt.startswith(("–", "nicht")):
                continue
            for nr in dict.fromkeys(re.findall(r"§ (\d+[a-z]?)", txt)):
                nid = f"eunorm:{key}:{nr}"
                if nid not in norm_ids:
                    fehler(f"Unbekannte {gesetz}-Umsetzungsnorm § {nr} bei Art. {a['nr']} DurchsetzungsRL", f"eunorm:durchsetzungsrl:{a['nr']}", f"§ {nr} {gesetz}")
                    continue
                add_edge(nid, f"eunorm:durchsetzungsrl:{a['nr']}", "implements", ref=f"§ {nr} {gesetz}")
    for rl in RICHTLINIEN:
        for a in rl["artikel"]:
            aid = f"eunorm:{rl['key']}:{a['nr'].replace(' ', '')}"
            ref_label = a.get("label") or f"Art. {a['nr']} {rl['kurz']}"
            for ref in a["umsetzung"]:
                nid = norm_id(ref)
                if nid not in norm_ids:
                    fehler(f"Unbekannte Umsetzungsnorm {ref} bei {ref_label}", aid, ref)
                    continue
                add_edge(nid, aid, "implements", ref=ref)
            for c in a["concepts"]:
                add_edge(f"concept:{c}", aid, "defined_in", ref=ref_label)
            for c in a["cases"]:
                add_edge(f"case:{c}", aid, "interprets", ref=ref_label)
            # EPGÜ-Artikel -> Artikel der Durchsetzungsrichtlinie, den er für das EPG umsetzt
            for ref in a.get("entspricht", []):
                nid = norm_id(ref)
                if nid not in norm_ids:
                    fehler(f"Unbekannte Entsprechung {ref} bei {ref_label}", aid, ref)
                    continue
                add_edge(aid, nid, "entspricht", ref=ref)
            # VerfO-Regel -> EPGÜ-Artikel („Bezug zum Übereinkommen“)
            for ref in a.get("bezug", []):
                nid = norm_id(ref)
                if nid not in norm_ids:
                    fehler(f"Unbekannter Bezug {ref} bei {ref_label}", aid, ref)
                    continue
                add_edge(aid, nid, "konkretisiert", ref=ref)

    def link_norms(src, refs, rel):
        for r in refs:
            nid = norm_id(r)
            if nid not in norm_ids:
                fehler(f"Unbekannte Norm {r} in {src}", src, r)
                continue
            add_edge(src, nid, rel, ref=r)

    # --- IPWiki-Quellen ---
    for w in IPWIKI:
        add_node(dict(id=f"source:{w['page']}", type="source", label=w["title"], summary=w["summary"],
                      url=IPWIKI_BASE + w["page"], provider="IPWiki"))
    # UP-Richtlinien des EPA (Ausgabe April 2026) und EPA-Informationsseiten zum Einheitspatent als Quellen der Einheitspatent-Begriffe
    for w in upc.einheitspatent.QUELLEN:
        add_node(dict(id=f"source:{w['page']}", type="source", label=w["title"], summary=w["summary"], url=w["url"], provider=w["provider"],
                      **({"titel_en": w["title_en"]} if w.get("title_en") else {})))

    # --- Entscheidungen ---
    for c in CASES:
        add_node(dict(id=f"case:{c['id']}", type="case", label=f"{c['court']} – {c['name']}", name=c["name"],
                      court=c["court"], date=c["date"], az=c["az"], fundstelle=c["fundstelle"],
                      kern=c["kern"], tags=c["tags"], url=case_url(c)))
        link_norms(f"case:{c['id']}", c["norms"], "interprets")

    # --- Begriffe ---
    for c in CONCEPTS:
        add_node(dict(id=f"concept:{c['id']}", type="concept", label=c["label"], kategorie=c["kategorie"],
                      definition=c["definition"], erlaeuterung=c["erlaeuterung"]))
        link_norms(f"concept:{c['id']}", c["norms"], "defined_in")
        for r in c["related"]:
            add_edge(f"concept:{c['id']}", f"concept:{r}", "related_to")
        for k in c["cases"]:
            add_edge(f"concept:{c['id']}", f"case:{k}", "illustrated_by")
        for w in c["ipwiki"] + c.get("quellen", []):
            add_edge(f"concept:{c['id']}", f"source:{w}", "documented_in")
    for c in CASES:  # Rückrichtung aus der Entscheidungsperspektive
        for k in c["concepts"]:
            e = (f"concept:{k}", f"case:{c['id']}")
            if not any(x["source"] == e[0] and x["target"] == e[1] for x in edges):
                add_edge(e[0], e[1], "illustrated_by")

    # --- Abgrenzungen ---
    for d in DISTINCTIONS:
        add_node(dict(id=f"distinction:{d['id']}", type="distinction", label=d["label"], frage=d["frage"],
                      kriterien=d["kriterien"], spalten=d["spalten"], rows=d["rows"], merksatz=d["merksatz"]))
        for k in d["concepts"]:
            add_edge(f"distinction:{d['id']}", f"concept:{k}", "contrasts")

    # --- Schemata ---
    def add_steps(parent_id, steps, prefix):
        prev = None
        for i, st in enumerate(steps, 1):
            sid = f"{prefix}.{i}"
            add_node(dict(id=sid, type="step", label=st["label"], text=st["text"], hinweis=st["hinweis"], order=i))
            add_edge(parent_id, sid, "has_step", order=i)
            if prev:
                add_edge(prev, sid, "next_step")
            prev = sid
            for k in st["concepts"]:
                add_edge(sid, f"concept:{k}", "uses_concept")
            for k in st["cases"]:
                add_edge(sid, f"case:{k}", "cites")
            link_norms(sid, st["norms"], "applies")
            add_steps(sid, st["children"], sid)

    for s in SCHEMATA:
        sid = f"schema:{s['id']}"
        add_node(dict(id=sid, type="schema", label=s["label"], kategorie=s["kategorie"], beschreibung=s["beschreibung"]))
        link_norms(sid, s["norms"], "applies")
        add_steps(sid, s["steps"], f"step:{s['id']}")

    # --- Kurse (fallbasierte Lerneinheiten) ---
    for i, k in enumerate(KURSE, 1):
        kid = f"course:{k['id']}"
        add_node(dict(id=kid, type="course", label=k["titel"], untertitel=k["untertitel"], beschreibung=k["beschreibung"], gebiet=k.get("gebiet"), order=i))
        for j, kap in enumerate(k["kapitel"], 1):
            cid = f"chapter:{kap['id']}"
            add_node(dict(id=cid, type="chapter", label=kap["titel"], order=j))
            add_edge(kid, cid, "has_chapter", order=j)
            for m, e in enumerate(kap["einheiten"], 1):
                uid = f"unit:{e['id']}"
                add_node(dict(id=uid, type="unit", label=e["titel"], typ=e["typ"], level=e.get("level", 0),
                              frage=e.get("frage", ""), order=m))
                add_edge(cid, uid, "has_unit", order=m)
                for c in e["concepts"]:
                    add_edge(uid, f"concept:{c}", "trains")
                for c in e["cases"]:
                    add_edge(uid, f"case:{c}", "cites")
                link_norms(uid, e["norms"], "applies")
                if e.get("step"):
                    add_edge(uid, e["step"], "covers")
                for d in e.get("distinctions", []):
                    add_edge(uid, f"distinction:{d}", "covers")
                if e["typ"] == "schema":
                    add_edge(uid, f"schema:{e['schema']}", "covers")

    # Doppelte Kanten entfernen (z.B. Begriff -> Artikel aus beiden Richtungen erfasst)
    seen_e, dedup = set(), []
    for e in edges:
        key = (e["source"], e["target"], e["relation"], e.get("ref"))
        if key in seen_e:
            continue
        seen_e.add(key)
        dedup.append(e)
    edges[:] = dedup

    # Validierung
    ids = {n["id"] for n in nodes}
    for e in edges:
        for k in ("source", "target"):
            if e[k] not in ids:
                fehler(f"Kante verweist auf unbekannten Knoten: {e}", e["source"], e["target"])

    graph = dict(
        meta=dict(
            titel="Wissensgraph Markenrecht (MarkenG), Patentrecht (PatG, PatV, IntPatÜG, PatKostG), Designrecht (DesignG, DesignV, GGV) und Einheitliches Patentgericht (EPGÜ, VerfO)",
            beschreibung="Normen, Begriffe, Prüfungsschemata, Abgrenzungen und Leitentscheidungen zum deutschen Marken-, Patent- und Designrecht sowie zum Verfahren vor dem Einheitlichen Patentgericht; verbunden über die Durchsetzungsrichtlinie 2004/48/EG, die Designrichtlinie und das IntPatÜG.",
            patent=dict(entscheidungen=patent.entscheidungen.META["anzahl"], bpatg=patent.entscheidungen.META["bpatg"], bgh=patent.entscheidungen.META["bgh"],
                        zeitraum=patent.entscheidungen.META["zeitraum"], quelle=patent.entscheidungen.META["quelle"],
                        stand={k: v.get("stand", []) for k, v in patent.gesetze_texte.META.items()}),
            design=dict(entscheidungen=design.entscheidungen.META["anzahl"], bpatg=design.entscheidungen.META["bpatg"], bgh=design.entscheidungen.META["bgh"],
                        zeitraum=design.entscheidungen.META["zeitraum"], quelle=design.entscheidungen.META["quelle"],
                        stand={k: v.get("stand", []) for k, v in design.gesetze_texte.META.items()}, eu_stand=design.eurecht.STAND),
            upc=dict(entscheidungen=upc.entscheidungen.META["anzahl"], zeitraum=upc.entscheidungen.META["zeitraum"], quelle=upc.entscheidungen.META["quelle"],
                     upca_stand=upc.upca.META["stand"], rop_stand=upc.rop.META["stand"][:160],
                     einheitspatent_stand=upc.einheitspatent.META["doeps"]["stand"], einheitspatent_quelle=upc.einheitspatent.META["doeps"].get("quelle_db", ""),
                     up_richtlinien=upc.einheitspatent.UP_RL_STAND, up_richtlinien_quelle=upc.einheitspatent.RL_META.get("quelle_db", ""),
                     up_richtlinien_url=upc.einheitspatent.UP_RL_URL, up_richtlinien_pdf=upc.einheitspatent.UP_RL_PDF),
            markenrl=dict(quelle=markenrl.URL, hinweis=RICHTLINIEN[0]["hinweis"]),
            richtlinien=[dict(key=r["key"], kurz=r["kurz"], titel=r["titel"], gesetz=r["gesetz"], quelle=r["url"], pdf=r["url_pdf"],
                              paraphrase=r["paraphrase"], hinweis=r["hinweis"], artikel=len(r["artikel"])) for r in RICHTLINIEN],
            gesetz_quelle=statute["quelle"], gesetz_stand=statute["meta"],
            statistik={t: sum(1 for n in nodes if n["type"] == t) for t in
                       ["norm", "eunorm", "concept", "schema", "step", "case", "distinction", "source", "course", "chapter", "unit"]},
            kanten=len(edges),
        ),
        nodes=nodes, edges=edges,
    )
    if not write:
        return graph
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(graph, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Graph:", graph["meta"]["statistik"], "Kanten:", len(edges), "->", OUT.relative_to(ROOT))
    return graph


if __name__ == "__main__":
    build()
