#!/usr/bin/env python3
"""Baut alle Artefakte neu: Gesetz parsen -> Graph -> Karteikarten -> HTML."""
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
for script in ["parse_markeng", "build_graph", "build_flashcards", "build_html"]:
    runpy.run_path(str(ROOT / "src" / f"{script}.py"), run_name="__main__")
