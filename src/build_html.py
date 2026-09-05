# -*- coding: utf-8 -*-
"""Erzeugt die eigenständige HTML-Lernapp docs/index.html aus Graph und Karteikarten."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "src" / "templates" / "app.html"
GRAPH = ROOT / "graph" / "markenrecht_graph.json"
CARDS = ROOT / "flashcards" / "karteikarten.json"
OUT = ROOT / "docs" / "index.html"


def embed(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def build():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    cards = json.loads(CARDS.read_text(encoding="utf-8"))
    # Für die HTML-App reichen die Kartenfelder ohne Redundanz
    html = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", embed(graph)).replace("__CARDS__", embed(cards))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"HTML -> {OUT.relative_to(ROOT)} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    build()
