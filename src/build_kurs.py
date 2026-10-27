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
from knowledge.patent import entscheidungen as pat_entscheidungen  # noqa: E402
from knowledge.design import entscheidungen as des_entscheidungen  # noqa: E402
from knowledge.patent import arbnerfg_entscheidungen as arb_entscheidungen  # noqa: E402
from knowledge.epc import entscheidungen as boa_entscheidungen  # noqa: E402
from knowledge.upc import en as upc_en  # noqa: E402
from knowledge.upc.en import ui as ui_en  # noqa: E402

TEMPLATE = ROOT / "src" / "templates" / "kurs.html"
SW = ROOT / "src" / "templates" / "sw.js"  # Service Worker nur für Web Push (Erinnerung), wird unverändert nach docs/ kopiert
VAPID = ROOT / "data" / "push_vapid_public.txt"  # öffentlicher VAPID-Schlüssel (__VAPID__); fehlt er, bleibt die Erinnerung aus
PUSH_API = ROOT / "data" / "push_api.txt"  # URL des Cloudflare Workers push/ (__PUSH_API__), ohne Schrägstrich am Ende
ASSETS = ROOT / "src" / "templates" / "ipelico"
GRAPH = ROOT / "graph" / "markenrecht_graph.json"
OUT = ROOT / "docs" / "index.html"
EPG_DB = ROOT / "docs" / "upc_entscheidungen.json"  # Entscheidungskorpus des EPG, von IPelico nachgeladen (#/epg)
PAT_DB = ROOT / "docs" / "patent_entscheidungen.json"  # Entscheidungskorpus BPatG/BGH, nachgeladen (#/bpatg)
DES_DB = ROOT / "docs" / "design_entscheidungen.json"  # Entscheidungskorpus Designsachen BPatG/BGH, nachgeladen (#/bpatg/design)
ARB_DB = ROOT / "docs" / "arbnerfg_entscheidungen.json"  # Schiedsstelle nach dem ArbEG und BGH, nachgeladen (#/bpatg/arbnerfg)
BOA_DB = ROOT / "docs" / "boa_entscheidungen.json"  # Beschwerdekammern des EPA (G, J, R, T mit Verteiler A bis C), nachgeladen (#/boa)
DATA = ROOT / "data" / "kurse.json"
OUT_EN = ROOT / "docs" / "en" / "index.html"  # englische App: nur das Gebiet EPG (knowledge/upc/en, PLAYBOOK 17)

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


def vapid_public():
    if not VAPID.exists():
        print("Hinweis: data/push_vapid_public.txt fehlt, Erinnerung bleibt ausgeschaltet (PLAYBOOK 14)")
        return ""
    key = VAPID.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[A-Za-z0-9_-]{80,100}", key):
        raise SystemExit("data/push_vapid_public.txt: kein base64url-kodierter P-256-Schlüssel")
    return key


def push_api():
    if not PUSH_API.exists():
        print("Hinweis: data/push_api.txt fehlt, Erinnerung bleibt ausgeschaltet (PLAYBOOK 14)")
        return ""
    url = PUSH_API.read_text(encoding="utf-8").strip().rstrip("/")
    if not re.fullmatch(r"https://[A-Za-z0-9.-]+(?::\d+)?(?:/[A-Za-z0-9._~-]+)*", url):
        raise SystemExit(f"data/push_api.txt: keine https-URL ohne Abfrage: {url!r}")
    return url


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


# Wörter, an denen deutsche Reste in der englischen Oberfläche auffallen (nur Warnung; der Rauchtest prüft den sichtbaren Text)
_DE_RESTE = re.compile(r"[äöüÄÖÜß]|\b(?:und|nicht|oder|Fälle|Einheiten|gelöst|fällig|Kurs|Kurse|Weiter|Zurück|Lernkarte|Tagesziel|Entscheidungen)\b")


def _ersetzen(html, paare, wo):
    fehlt = []
    for de, en in paare:
        if de not in html:
            fehlt.append(de[:110])
        html = html.replace(de, en)
    if fehlt:
        raise SystemExit(f"{wo}: {len(fehlt)} Ersetzungen treffen nicht mehr (Template geändert?):\n  " + "\n  ".join(map(repr, fehlt)))
    return html


def _reste(html):
    """Zeilen des englischen Templates (ohne Kommentare und eingebettete Daten), die noch deutsch aussehen."""
    code = re.sub(r"/\*.*?\*/", "", html, flags=re.S)
    out = []
    for ln in code.split("\n"):
        ln = re.sub(r"(^|\s)//.*$", "", ln)
        if _DE_RESTE.search(ln) and "__" not in ln and not any(t in ln for t in ui_en.TOT):
            out.append(ln.strip()[:120])
    return out


def build_en(graph, template):
    """docs/en/index.html: dieselbe App mit englischer Oberfläche (ui.py) und dem englischen EPG-Paket (knowledge/upc/en)."""
    kurse, gebiete, g = upc_en.bauen(KURSE, GEBIETE, reduced_graph(graph))
    html = _ersetzen(template, ui_en.STRUKTUR, "ui.STRUKTUR")
    reste = _reste(_ersetzen(html, ui_en.TEXTE, "ui.TEXTE"))
    html = _ersetzen(html, ui_en.TEXTE, "ui.TEXTE")
    epg = json.loads(EPG_DB.read_text(encoding="utf-8"))
    kammern = {k: upc_en.kammer_en(k) for k in sorted({e["kammer"] for e in epg["entscheidungen"]})}
    html = (html.replace("__KAMMERN__", embed(kammern))
            .replace("__KURSE__", embed(kurse)).replace("__GEBIETE__", embed(gebiete)).replace("__GRAPH__", embed(g))
            .replace("__LAWJS__", _ersetzen(js_source(), ui_en.LAWJS, "ui.LAWJS"))
            .replace("__SPRITE__", sprite()).replace("__FONTS__", fonts_css()).replace("__FAVICON__", favicon())
            .replace("__VAPID__", vapid_public()).replace("__PUSH_API__", push_api()))
    for ph in ("__KURSE__", "__GEBIETE__", "__GRAPH__", "__LAWJS__", "__SPRITE__", "__FONTS__", "__FAVICON__", "__VAPID__", "__PUSH_API__", "__KAMMERN__"):
        if ph in html:
            raise SystemExit(f"Platzhalter {ph} in docs/en nicht ersetzt")
    OUT_EN.parent.mkdir(parents=True, exist_ok=True)
    OUT_EN.write_text(html, encoding="utf-8")
    manifest = {
        "name": "IPelico – The Unified Patent Court in cases", "short_name": "IPelico UPC", "start_url": "./", "scope": "./",
        "display": "standalone", "background_color": "#f3f5f9", "theme_color": "#1482e3", "lang": "en",
        "icons": [{"src": "../icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                  {"src": "../icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                  {"src": "../icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
    }
    (OUT_EN.parent / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(len(c["einheiten"]) for k in kurse for c in k["kapitel"])
    print(f"IPelico (englisch): {len(kurse)} Kurse, {n} Einheiten, {len(g['nodes'])} Knoten -> {OUT_EN.relative_to(ROOT)} ({OUT_EN.stat().st_size/1024:.0f} KB)")
    if reste:
        print(f"Hinweis: {len(reste)} Zeilen der englischen Oberfläche sehen noch deutsch aus (src/knowledge/upc/en/ui.py), z. B.:\n  " + "\n  ".join(reste[:12]))


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
            .replace("__FAVICON__", favicon())
            .replace("__VAPID__", vapid_public())
            .replace("__PUSH_API__", push_api()))
    for ph in ("__KURSE__", "__GEBIETE__", "__GRAPH__", "__LAWJS__", "__SPRITE__", "__FONTS__", "__FAVICON__", "__VAPID__", "__PUSH_API__"):
        if ph in html:
            raise SystemExit(f"Platzhalter {ph} nicht ersetzt")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    (OUT.parent / "sw.js").write_text(SW.read_text(encoding="utf-8"), encoding="utf-8")
    epg = upc_entscheidungen.kompakt()
    EPG_DB.write_text(json.dumps(epg, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"EPG-Rechtsprechung: {epg['meta']['anzahl']} Entscheidungen -> {EPG_DB.relative_to(ROOT)} ({EPG_DB.stat().st_size/1024:.0f} KB)")
    pat = pat_entscheidungen.kompakt()
    PAT_DB.write_text(json.dumps(pat, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"BPatG/BGH-Rechtsprechung: {pat['meta']['anzahl']} Entscheidungen -> {PAT_DB.relative_to(ROOT)} ({PAT_DB.stat().st_size/1024:.0f} KB)")
    des = des_entscheidungen.kompakt()
    DES_DB.write_text(json.dumps(des, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Design-Rechtsprechung: {des['meta']['anzahl']} Entscheidungen -> {DES_DB.relative_to(ROOT)} ({DES_DB.stat().st_size/1024:.0f} KB)")
    arb = arb_entscheidungen.kompakt()
    ARB_DB.write_text(json.dumps(arb, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"ArbnErfG-Rechtsprechung: {arb['meta']['anzahl']} Entscheidungen -> {ARB_DB.relative_to(ROOT)} ({ARB_DB.stat().st_size/1024:.0f} KB)")
    boa = boa_entscheidungen.kompakt()
    BOA_DB.write_text(json.dumps(boa, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Beschwerdekammern EPA: {boa['meta']['anzahl']} Entscheidungen -> {BOA_DB.relative_to(ROOT)} ({BOA_DB.stat().st_size/1024:.0f} KB)")
    app_icons()
    build_en(graph, TEMPLATE.read_text(encoding="utf-8"))
    n = sum(len(k["einheiten"]) for kurs in KURSE for k in kurs["kapitel"])
    print(f"IPelico: {len(KURSE)} Kurse, {n} Einheiten, Sprite {len(sp)/1024:.0f} KB -> "
          f"{OUT.relative_to(ROOT)} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    build()
