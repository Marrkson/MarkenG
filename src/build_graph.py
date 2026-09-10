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
]
RL_BY_KURZ = {r["kurz"]: r["key"] for r in RICHTLINIEN}

NORM_RE = re.compile(r"§ (\d+[a-z]?)")
EUNORM_RE = re.compile(r"Art\. (\d+[a-z]?)(?: .*)? (" + "|".join(RL_BY_KURZ) + r")$")


def norm_id(ref: str) -> str:
    """'§ 14 Abs. 2 Nr. 2' -> 'norm:§14'; 'Art. 10 Abs. 2 MarkenRL' -> 'eunorm:markenrl:10';
    'Art. 8 Abs. 3 lit. e DurchsetzungsRL' -> 'eunorm:durchsetzungsrl:8'"""
    m = EUNORM_RE.match(ref)
    if m:
        return f"eunorm:{RL_BY_KURZ[m.group(2)]}:{m.group(1)}"
    m = NORM_RE.match(ref)
    if not m:
        raise ValueError(ref)
    return f"norm:§{m.group(1)}"


def case_url(c):
    d, m, y = c["date"].split("-")[::-1]
    az = c["az"].replace(" ", "+")
    return (f"https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht={c['court']}"
            f"&Datum={d}.{m}.{y}&Aktenzeichen={az}")


def build():
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
    for rl in RICHTLINIEN:
        common = dict(type="eunorm", rl=rl["key"], kurz=rl["kurz"], gesetz=rl["gesetz"], url=rl["url"], url_pdf=rl["url_pdf"], paraphrase=rl["paraphrase"])
        for a in rl["artikel"]:
            add_node(dict(id=f"eunorm:{rl['key']}:{a['nr']}", label=f"Art. {a['nr']} {rl['kurz']}", titel=a["titel"],
                          nummer=a["nr"], kapitel=a["kapitel"], abschnitt=a["abschnitt"], absaetze=a["absaetze"], hinweis=a["hinweis"],
                          umsetzung_weitere=a.get("umsetzung_weitere", {}), **common))
        add_node(dict(id=f"eunorm:{rl['key']}:erwaegungsgruende", label=f"Erwägungsgründe {rl['kurz']}", titel="Erwägungsgründe (Auswahl)",
                      nummer="0", kapitel="Präambel", abschnitt=None,
                      absaetze=[dict(nr=e["nr"], text=e["text"]) for e in rl["erwaegungsgruende"]], hinweis="", umsetzung_weitere={}, **common))
    norm_ids = {n["id"] for n in nodes}
    for rl in RICHTLINIEN:
        for a in rl["artikel"]:
            aid = f"eunorm:{rl['key']}:{a['nr']}"
            ref_label = f"Art. {a['nr']} {rl['kurz']}"
            for ref in a["umsetzung"]:
                nid = norm_id(ref)
                if nid not in norm_ids:
                    raise ValueError(f"Unbekannte Umsetzungsnorm {ref} bei {ref_label}")
                add_edge(nid, aid, "implements", ref=ref)
            for c in a["concepts"]:
                add_edge(f"concept:{c}", aid, "defined_in", ref=ref_label)
            for c in a["cases"]:
                add_edge(f"case:{c}", aid, "interprets", ref=ref_label)

    def link_norms(src, refs, rel):
        for r in refs:
            nid = norm_id(r)
            if nid not in norm_ids:
                raise ValueError(f"Unbekannte Norm {r} in {src}")
            add_edge(src, nid, rel, ref=r)

    # --- IPWiki-Quellen ---
    for w in IPWIKI:
        add_node(dict(id=f"source:{w['page']}", type="source", label=w["title"], summary=w["summary"],
                      url=IPWIKI_BASE + w["page"], provider="IPWiki"))

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
        for w in c["ipwiki"]:
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
        add_node(dict(id=kid, type="course", label=k["titel"], untertitel=k["untertitel"], beschreibung=k["beschreibung"], order=i))
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
                raise ValueError(f"Kante verweist auf unbekannten Knoten: {e}")

    graph = dict(
        meta=dict(
            titel="Wissensgraph Markenrecht (MarkenG)",
            beschreibung="Normen, Begriffe, Prüfungsschemata, Abgrenzungen und Leitentscheidungen zum deutschen Markenrecht.",
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
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(graph, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Graph:", graph["meta"]["statistik"], "Kanten:", len(edges), "->", OUT.relative_to(ROOT))
    return graph


if __name__ == "__main__":
    build()
