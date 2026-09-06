# -*- coding: utf-8 -*-
"""Erzeugt die fallbasierte Lernapp docs/kurse/index.html (Jurafuchs-artiges Format)
sowie data/kurse.json."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from knowledge.gesetze import js_source  # noqa: E402
from knowledge.kurse import KURSE  # noqa: E402

TEMPLATE = ROOT / "src" / "templates" / "kurs.html"
GRAPH = ROOT / "graph" / "markenrecht_graph.json"
OUT = ROOT / "docs" / "kurse" / "index.html"
DATA = ROOT / "data" / "kurse.json"


def embed(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def reduced_graph(graph):
    """Nur die Knoten, die die Kursapp für Inline-Karten braucht."""
    keep_types = {"concept", "case", "norm", "schema", "step", "distinction"}
    nodes = []
    for n in graph["nodes"]:
        if n["type"] not in keep_types:
            continue
        n = dict(n)
        if n["type"] == "norm":
            n.pop("text", None)
        nodes.append(n)
    ids = {n["id"] for n in nodes}
    edges = [e for e in graph["edges"] if e["source"] in ids and e["target"] in ids]
    return dict(nodes=nodes, edges=edges)


def build():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    DATA.write_text(json.dumps(KURSE, ensure_ascii=False, indent=1), encoding="utf-8")
    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("__KURSE__", embed(KURSE))
            .replace("__GRAPH__", embed(reduced_graph(graph)))
            .replace("__LAWJS__", js_source()))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    n = sum(len(k["einheiten"]) for kurs in KURSE for k in kurs["kapitel"])
    print(f"Kursapp: {len(KURSE)} Kurse, {n} Einheiten -> {OUT.relative_to(ROOT)} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    build()
