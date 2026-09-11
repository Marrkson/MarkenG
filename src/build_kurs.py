# -*- coding: utf-8 -*-
"""Erzeugt IPelico, die fallbasierte Lernapp docs/index.html (Startseite), und data/kurse.json.
Bettet zusätzlich die Rechtsgebiete (__GEBIETE__, kurse/gebiete.py) ein.

Bettet ein: Kurse (__KURSE__), den reduzierten Graphen (__GRAPH__), das Verlinkungs-JavaScript
(__LAWJS__), das SVG-Sprite aus src/templates/ipelico/ (__SPRITE__: Icons und Zeichen) sowie die
Schriften als @font-face (__FONTS__). Die Datei bleibt ohne externe Ressourcen lauffähig.
"""
import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from knowledge.gesetze import js_source  # noqa: E402
from knowledge.kurse import KURSE, GEBIETE  # noqa: E402
from knowledge.upc import entscheidungen as upc_entscheidungen  # noqa: E402

TEMPLATE = ROOT / "src" / "templates" / "kurs.html"
ASSETS = ROOT / "src" / "templates" / "ipelico"
GRAPH = ROOT / "graph" / "markenrecht_graph.json"
OUT = ROOT / "docs" / "index.html"
EPG_DB = ROOT / "docs" / "upc_entscheidungen.json"  # Entscheidungskorpus des EPG, von IPelico nachgeladen (#/epg)
DATA = ROOT / "data" / "kurse.json"

# Icons, die das Template verwendet; fehlt eines im Sprite, bricht der Build ab.
REQUIRED_ICONS = [
    "tab-kurse", "tab-wdh", "tab-profil", "tab-konzept", "feier",
    "zurueck", "weiter", "schliessen", "extern", "suche", "einstellungen",
    "fall", "quiz", "intro", "schema", "richtig", "falsch", "offen", "streak", "punkte", "faellig",
    "merke", "definition", "tipp", "sachverhalt", "loesung",
    "begriff", "norm", "richtlinie", "entscheidung", "pruefungspunkt", "tabelle",
    "hell", "dunkel", "system", "datenschutz", "loeschung",
]
FONTS = [  # (Datei, family, weight)
    ("IBMPlexSans-var.woff2", "IBM Plex Sans", "400 700"),
    ("IBMPlexMono-500.woff2", "IBM Plex Mono", "500"),
]


def embed(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def reduced_graph(graph):
    """Nur die Knoten, die die Kursapp für Inline-Karten braucht."""
    keep_types = {"concept", "case", "norm", "eunorm", "schema", "step", "distinction", "source"}
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


SVG_RE = re.compile(r"<svg\b([^>]*)>(.*)</svg>", re.S)


def to_symbol(svg_text, sid):
    m = SVG_RE.search(svg_text)
    if not m:
        raise SystemExit(f"kein <svg> in {sid}")
    attrs, body = m.group(1), m.group(2)
    vb = re.search(r'viewBox="([^"]+)"', attrs)
    keep = " ".join(re.findall(r'(?:fill|stroke|stroke-width|stroke-linecap|stroke-linejoin)="[^"]*"', attrs))
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
    body = re.sub(r'\bid="([^"]+)"', lambda x: f'id="{sid}-{x.group(1)}"', body)
    body = re.sub(r"url\(#([^)]+)\)", lambda x: f"url(#{sid}-{x.group(1)})", body)
    return f'<symbol id="{sid}" viewBox="{vb.group(1) if vb else "0 0 24 24"}" {keep}>{body}</symbol>'


def sprite():
    syms, ids = [], set()
    for sub in ("icons", "logo"):
        for f in sorted((ASSETS / sub).glob("*.svg")):
            sid = f.stem
            if sid in ids:
                raise SystemExit(f"doppelte Symbol-ID {sid}")
            ids.add(sid)
            syms.append(to_symbol(f.read_text(encoding="utf-8"), sid))
    missing = [n for n in REQUIRED_ICONS if f"ic-{n}" not in ids]
    if missing or "ipelico-mark" not in ids:
        raise SystemExit(f"Sprite unvollständig, fehlt: {missing + ([] if 'ipelico-mark' in ids else ['ipelico-mark'])}")
    # Nicht display:none: Chrome wendet Masken und Verläufe aus unsichtbaren SVGs nicht an (Aussparung „IP“ im Zeichen)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true" focusable="false" '
            'style="position:absolute;width:0;height:0;overflow:hidden">' + "".join(syms) + "</svg>")


def fonts_css():
    rules = []
    for fname, family, weight in FONTS:
        p = ASSETS / "fonts" / fname
        if not p.exists():
            raise SystemExit(f"Schrift fehlt: {p}")
        b64 = base64.b64encode(p.read_bytes()).decode()
        rules.append(f"@font-face{{font-family:\"{family}\";font-style:normal;font-weight:{weight};font-display:swap;"
                     f"src:url(data:font/woff2;base64,{b64}) format(\"woff2\")}}")
    return "\n".join(rules)


def favicon():
    p = ASSETS / "logo" / "ipelico-badge.svg"
    return "data:image/svg+xml;base64," + base64.b64encode(p.read_bytes()).decode()


APP_ICONS = ["apple-touch-icon.png", "icon-192.png", "icon-512.png", "icon-maskable-512.png", "favicon-32.png", "favicon-16.png", "favicon.ico"]


def app_icons():
    """PNG-Icons (Homescreen, Favicon) und Web-Manifest nach docs/ kopieren; PNGs entstehen aus dem Badge."""
    for name in APP_ICONS:
        src = ASSETS / "logo" / name
        if not src.exists():
            raise SystemExit(f"App-Icon fehlt: {src} (Rendern: siehe PLAYBOOK 6)")
        (OUT.parent / name).write_bytes(src.read_bytes())
    manifest = {
        "name": "IPelico – Markenrecht und EPG in Fällen", "short_name": "IPelico", "start_url": "./", "scope": "./",
        "display": "standalone", "background_color": "#f3f5f9", "theme_color": "#1482e3", "lang": "de",
        "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                  {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                  {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
    }
    (OUT.parent / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")


def build():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    DATA.write_text(json.dumps(KURSE, ensure_ascii=False, indent=1), encoding="utf-8")
    sp = sprite()
    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("__KURSE__", embed(KURSE))
            .replace("__GEBIETE__", embed(GEBIETE))
            .replace("__GRAPH__", embed(reduced_graph(graph)))
            .replace("__LAWJS__", js_source())
            .replace("__SPRITE__", sp)
            .replace("__FONTS__", fonts_css())
            .replace("__FAVICON__", favicon()))
    for ph in ("__KURSE__", "__GEBIETE__", "__GRAPH__", "__LAWJS__", "__SPRITE__", "__FONTS__", "__FAVICON__"):
        if ph in html:
            raise SystemExit(f"Platzhalter {ph} nicht ersetzt")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    epg = upc_entscheidungen.kompakt()
    EPG_DB.write_text(json.dumps(epg, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"EPG-Rechtsprechung: {epg['meta']['anzahl']} Entscheidungen -> {EPG_DB.relative_to(ROOT)} ({EPG_DB.stat().st_size/1024:.0f} KB)")
    app_icons()
    n = sum(len(k["einheiten"]) for kurs in KURSE for k in kurs["kapitel"])
    print(f"IPelico: {len(KURSE)} Kurse, {n} Einheiten, Sprite {len(sp)/1024:.0f} KB -> "
          f"{OUT.relative_to(ROOT)} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    build()
