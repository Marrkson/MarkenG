# -*- coding: utf-8 -*-
"""Erzeugt Lernkarteikarten aus dem Wissensgraphen.

Ausgaben (flashcards/):
  karteikarten.json   strukturierte Karten (für die HTML-App; Gesetzeszitate werden
                      dort beim Rendern verlinkt)
  karteikarten.csv    Anki-Import (Tab-getrennt: Vorderseite, Rückseite, Tags);
                      Gesetzeszitate als HTML-Links auf gesetze-im-internet.de
  karteikarten.md     lesbare Markdown-Fassung mit Links auf gesetze-im-internet.de

Kartentypen:
  definition      Begriff -> Definition
  begriff         Definition -> Begriff (Umkehrkarte)
  schema          Prüfungsschema -> Gliederung
  schema_step     Prüfungspunkt -> Unterpunkte
  abgrenzung      Abgrenzungsfrage -> Vergleichstabelle + Merksatz
  entscheidung    Entscheidung -> Kernaussage
  entscheidung_r  Kernaussage -> Entscheidungsname (Umkehrkarte)
  norm            Paragraph -> Regelungsinhalt
  eunorm          Artikel der MarkenRL -> Inhalt und Umsetzung im MarkenG
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from knowledge.gesetze import linkify  # noqa: E402
GRAPH = ROOT / "graph" / "markenrecht_graph.json"
OUTDIR = ROOT / "flashcards"


def load_graph():
    return json.loads(GRAPH.read_text(encoding="utf-8"))


def index(graph):
    by_id = {n["id"]: n for n in graph["nodes"]}
    out, inc = {}, {}
    for e in graph["edges"]:
        out.setdefault(e["source"], []).append(e)
        inc.setdefault(e["target"], []).append(e)
    return by_id, out, inc


def children(out, nid):
    return sorted([e for e in out.get(nid, []) if e["relation"] == "has_step"], key=lambda e: e["order"])


def outline(by_id, out, nid, depth=0, max_depth=2):
    lines = []
    for e in children(out, nid):
        st = by_id[e["target"]]
        lines.append("  " * depth + "- " + st["label"])
        if depth < max_depth:
            lines.extend(outline(by_id, out, st["id"], depth + 1, max_depth))
    return lines


def generate(graph):
    by_id, out, inc = index(graph)
    cards = []

    def add(typ, front, back, tags, node, extra=None):
        c = dict(id=f"card:{typ}:{node}", typ=typ, front=front, back=back, tags=tags, node=node)
        if extra:
            c.update(extra)
        cards.append(c)

    # Begriffe
    for n in graph["nodes"]:
        if n["type"] != "concept":
            continue
        norms = [e["ref"] for e in out.get(n["id"], []) if e["relation"] == "defined_in"]
        cases = [by_id[e["target"]] for e in out.get(n["id"], []) if e["relation"] == "illustrated_by"]
        back = n["definition"]
        if norms:
            back += "\n\nNormen: " + ", ".join(norms) + " MarkenG"
        if cases:
            back += "\n\nRechtsprechung: " + "; ".join(f"{c['court']} {c['name']} ({c['az']})" for c in cases[:4])
        add("definition", f"Definiere: {n['label']}", back, ["Begriff", n["kategorie"]], n["id"],
            dict(erlaeuterung=n["erlaeuterung"]))
        add("begriff", f"Welcher Begriff wird so definiert?\n\n{n['definition']}", n["label"], ["Begriff", "Umkehr", n["kategorie"]], n["id"])

    # Schemata
    for n in graph["nodes"]:
        if n["type"] != "schema":
            continue
        add("schema", f"Prüfungsschema: {n['label']}", "\n".join(outline(by_id, out, n["id"])), ["Prüfungsschema", n["kategorie"]], n["id"])
    for n in graph["nodes"]:
        if n["type"] != "step":
            continue
        kids = children(out, n["id"])
        if len(kids) >= 2:
            schema_id = n["id"].split(".")[0].replace("step:", "schema:")
            schema = by_id.get(schema_id)
            front = f"{n['label']}\n({schema['label'] if schema else ''})\n\nWelche Punkte sind hier zu prüfen?"
            back = "\n".join(outline(by_id, out, n["id"], 0, 1))
            if n.get("text"):
                back += "\n\n" + n["text"]
            add("schema_step", front, back, ["Prüfungsschema", "Prüfungspunkt"], n["id"])

    # Abgrenzungen
    for n in graph["nodes"]:
        if n["type"] != "distinction":
            continue
        lines = []
        for krit, row in zip(n["kriterien"], n["rows"]):
            cells = [f"{sp}: {val}" for sp, val in zip(n["spalten"], row) if val]
            lines.append(f"• {krit} — " + " | ".join(cells))
        back = "\n".join(lines) + "\n\nMerksatz: " + n["merksatz"]
        add("abgrenzung", n["frage"] + f"\n({n['label']})", back, ["Abgrenzung"], n["id"])

    # Entscheidungen
    for n in graph["nodes"]:
        if n["type"] != "case":
            continue
        norms = sorted({e["ref"] for e in out.get(n["id"], []) if e["relation"] == "interprets"})
        front = f"{n['court']} „{n['name']}“ ({n['az']}, {n['date'][:4]}) – Kernaussage?"
        back = n["kern"] + (f"\n\nNormen: {', '.join(norms)} MarkenG" if norms else "") + (f"\nFundstelle: {n['fundstelle']}" if n.get("fundstelle") else "")
        add("entscheidung", front, back, ["Rechtsprechung", n["court"]] + n["tags"], n["id"])
        add("entscheidung_r", f"Welche Entscheidung ({n['court']}) steht für folgenden Grundsatz?\n\n{n['kern']}", f"{n['court']} „{n['name']}“ – {n['az']} ({n['date'][:4]}), {n['fundstelle']}", ["Rechtsprechung", "Umkehr", n["court"]] + n["tags"], n["id"])

    # Normen (nur solche, die von Begriffen/Schemata verwendet werden)
    used = {}
    for e in graph["edges"]:
        if e["relation"] in ("defined_in", "applies") and e["target"].startswith("norm:"):
            used.setdefault(e["target"], set()).add(e["source"])
    for nid in sorted(used, key=lambda x: (len(by_id[x]["nummer"].rstrip("abcdefghi")), by_id[x]["nummer"])):
        n = by_id[nid]
        first = n["absaetze"][0]["text"] if n["absaetze"] else n["text"]
        first = first if len(first) <= 700 else first[:700] + " …"
        concepts = [by_id[s]["label"] for s in used[nid] if s.startswith("concept:")]
        back = f"{n['titel']}\n\n{first}"
        if concepts:
            back += "\n\nZugehörige Begriffe: " + ", ".join(sorted(concepts)[:8])
        add("norm", f"Was regelt {n['label']}?", back, ["Gesetz"], nid)

    # Markenrechtsrichtlinie: Artikel -> Inhalt und Umsetzung
    for n in graph["nodes"]:
        if n["type"] != "eunorm" or n["nummer"] == "0":
            continue
        umsetzung = [e["ref"] for e in inc.get(n["id"], []) if e["relation"] == "implements"]
        first = n["absaetze"][0]["text"] if n["absaetze"] else ""
        first = first if len(first) <= 600 else first[:600] + " …"
        back = f"{n['titel']}\n\n{first}"
        if umsetzung:
            back += "\n\nUmgesetzt in: " + ", ".join(sorted(set(umsetzung))) + " MarkenG"
        weitere = [f"{law}: {ref}" for law, ref in n.get("umsetzung_weitere", {}).items() if law != "MarkenG"]
        if weitere:
            back += "\n\nWeitere Gesetze: " + "; ".join(weitere)
        if n.get("hinweis"):
            back += "\n\nHinweis: " + n["hinweis"]
        add("eunorm", f"Was regelt {n['label']} und welche Vorschrift des MarkenG setzt ihn um?", back, ["Richtlinie", "EU", n.get("kurz", "")], n["id"])
    return cards


def write(cards):
    OUTDIR.mkdir(exist_ok=True)
    (OUTDIR / "karteikarten.json").write_text(json.dumps(cards, ensure_ascii=False, indent=1), encoding="utf-8")
    with (OUTDIR / "karteikarten.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        for c in cards:
            front = linkify(c["front"], "html").replace("\n", "<br>")
            back = linkify(c["back"], "html").replace("\n", "<br>")
            w.writerow([front, back, " ".join(t.replace(" ", "_") for t in c["tags"])])
    md = ["# Karteikarten Markenrecht", "", f"{len(cards)} Karten, generiert aus graph/markenrecht_graph.json.", ""]
    current = None
    for c in cards:
        if c["typ"] != current:
            current = c["typ"]
            md += [f"## {current}", ""]
        md += [f"**F:** {linkify(c['front'], 'markdown')}", "",
               f"**A:** {linkify(c['back'], 'markdown')}", "",
               f"*Tags: {', '.join(c['tags'])}*", "", "---", ""]
    (OUTDIR / "karteikarten.md").write_text("\n".join(md), encoding="utf-8")
    from collections import Counter
    print(f"{len(cards)} Karteikarten -> {OUTDIR.relative_to(ROOT)}/ ", dict(Counter(c["typ"] for c in cards)))


if __name__ == "__main__":
    write(generate(load_graph()))
