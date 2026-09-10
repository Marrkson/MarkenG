# -*- coding: utf-8 -*-
"""Erzeugt die IPelico-Icons mit Gemini und vektorisiert sie.

  python3 tools/gen_assets.py gen   [--only a,b] [--force]   Rohbilder nach tools/gen_raw/icons/*.png
  python3 tools/gen_assets.py trace [--only a,b]             PNG -> src/templates/ipelico/icons/ic-*.svg (potrace)

Voraussetzungen: GEMINI_API_KEY in .env, Pillow, potrace (brew install potrace).
Stil: dicke Linie in der Sprache des Zeichens (src/templates/ipelico/logo/ipelico-mark.svg), einfarbig,
Farbe kommt aus dem CSS (currentColor). Die fünf Tab-/Feier-Icons enthalten den Pelikan.
"""
import base64, json, re, subprocess, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "src" / "templates" / "ipelico"
RAW = ROOT / "tools" / "gen_raw" / "icons"
STYLE_REF = ASSETS / "ref" / "icons-T1.png"      # Stilblatt (dicke Linie)
LOGO_REF = ASSETS / "ref" / "logo-mark.png"      # Zeichen als Bild (für Pelikan-Icons)
MODEL = "gemini-3-pro-image"

STYLE = ("Single icon in exactly the style of the reference sheet: thick monoline strokes (about one tenth of the icon "
         "size), rounded caps and joins, geometric construction from circles, straight strokes and arcs, no fills except "
         "where stated, no outlines around strokes, no gradients, no shadow, no text, no frame, no container. Single "
         "vivid blue #1482e3 on a pure white edge-to-edge background, centered, the icon fills about 70 percent of the canvas.")
PELICAN = ("The pelican mark from the second reference image (ring head, straight beak, pouch arc) must appear exactly "
           "as drawn, same stroke weight as the rest.")

# name: (Prompt, mit Pelikan?)
ICONS = {
    # Tableiste und Feier (mit Pelikan)
    "tab-kurse": ("a simple house outline (roof and walls, no door, no window) with the pelican mark centered inside, mark about half the house height", True),
    "tab-wdh": ("the pelican mark with one circular arrow around it (repeat)", True),
    "tab-profil": ("the pelican mark centered inside a plain circle, with clear space between mark and circle, nothing else", True),
    "tab-konzept": ("an open book (two pages) drawn in the same monoline, with the pelican mark small and centered above it, not touching", True),
    "feier": ("the pelican mark inside a laurel wreath (achievement)", True),
    # Aktionen
    "zurueck": ("a chevron pointing left", False), "weiter": ("an arrow pointing right", False),
    "schliessen": ("a cross (X)", False), "menu": ("three horizontal lines", False),
    "extern": ("an arrow pointing out of the top right corner of a rounded square", False),
    "suche": ("a magnifying glass", False), "einstellungen": ("a gear with six teeth", False),
    # Einheitentypen
    "fall": ("a briefcase", False), "quiz": ("a question mark inside a speech bubble", False),
    "intro": ("the letter i inside a circle", False), "schema": ("a hierarchy: one box above two boxes connected by lines", False),
    # Status
    "richtig": ("a checkmark", False), "falsch": ("a cross inside a circle", False), "offen": ("an empty circle", False),
    "streak": ("a flame", False), "punkte": ("a five-pointed star", False), "faellig": ("a clock face", False),
    # Wissensboxen
    "merke": ("a bookmark ribbon", False), "definition": ("an open book", False), "tipp": ("a light bulb", False),
    "sachverhalt": ("a document sheet with a folded corner and two text lines", False),
    "loesung": ("a checkmark inside a rounded square", False),
    # Chips
    "begriff": ("a closed book seen from the front", False), "norm": ("the section sign §", False),
    "richtlinie": ("a circle of small dots like the EU stars", False), "entscheidung": ("a judge's gavel", False),
    "pruefungspunkt": ("a numbered list: three short lines each with a small circle in front", False),
    "tabelle": ("a table grid of two columns and two rows", False),
    # Kurse
    "marke": ("a price tag with a small circle (the ® idea) on it", False), "register": ("a clipboard with three lines", False),
    "verletzung": ("a shield with a lightning bolt", False), "verwechslung": ("a balance scale", False),
    "bekanntheit": ("a simple five-pointed star outline, nothing else", False), "schranken": ("a road barrier gate", False),
    "loeschung": ("a trash can", False), "bezeichnungen": ("a small shop front with an awning", False),
    "rechtsfolgen": ("a judge gavel with its block, nothing else", False), "union": ("a globe with meridians", False),
    "klausur": ("a diagonal pencil, nothing else", False), "zulaessigkeit": ("a staircase of three steps as one stepped line rising from bottom left to top right", False),
    "durchsetzung": ("a magnifying glass whose lens contains a single short horizontal line, nothing else", False),
    # Profil
    "hell": ("a sun", False), "dunkel": ("a crescent moon", False), "system": ("a computer monitor", False),
    "datenschutz": ("a shield with a checkmark", False),
}


def api_key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("GEMINI_API_KEY fehlt in .env")


def gen(prompt, out, refs=(), retries=4):
    parts = [{"inlineData": {"mimeType": "image/png", "data": base64.b64encode(Path(r).read_bytes()).decode()}} for r in refs]
    parts.append({"text": prompt})
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "1:1", "imageSize": "1K"}}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={api_key()}"
    for attempt in range(retries):
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                d = json.load(resp)
        except (urllib.error.HTTPError, TimeoutError, OSError) as e:
            code = getattr(e, "code", None)
            print("Fehler", code or type(e).__name__, out.name, file=sys.stderr)
            if attempt < retries - 1 and (code in (None, 429, 500, 503)):
                time.sleep(10 * (attempt + 1)); continue
            raise
        for p in d.get("candidates", [{}])[0].get("content", {}).get("parts", []):
            if "inlineData" in p:
                out.write_bytes(base64.b64decode(p["inlineData"]["data"])); return out
        print("keine Bilddaten:", out.name, json.dumps(d)[:200], file=sys.stderr); time.sleep(5)
    raise RuntimeError("keine Bilddaten für " + out.name)


def job_gen(name, force):
    raw = RAW / f"{name}.png"
    if raw.exists() and not force:
        return
    desc, pel = ICONS[name]
    refs = [STYLE_REF, LOGO_REF] if pel else [STYLE_REF]
    gen(f"{STYLE} Icon: {desc}. {PELICAN if pel else ''}", raw, refs=refs)


def trace(name):
    """Blau auf Weiß -> Schwarzweißmaske -> potrace -> SVG mit fill=currentColor, viewBox 0 0 24 24."""
    raw = RAW / f"{name}.png"
    img = Image.open(raw).convert("RGB")
    # Alles, was deutlich nicht weiß ist, wird schwarz
    mask = img.convert("L").point(lambda v: 0 if v < 200 else 255)
    bbox = Image.eval(mask, lambda v: 255 - v).getbbox()
    if not bbox:
        raise RuntimeError(f"leeres Icon {name}")
    glyph = mask.crop(bbox)
    side = max(glyph.size); m = int(side * 0.10)
    canvas = Image.new("L", (side + 2 * m, side + 2 * m), 255)
    canvas.paste(glyph, ((canvas.width - glyph.width) // 2, (canvas.height - glyph.height) // 2))
    canvas = canvas.resize((480, 480), Image.LANCZOS).point(lambda v: 0 if v < 128 else 255)
    pbm = raw.with_suffix(".pbm"); canvas.save(pbm)
    svg_tmp = raw.with_suffix(".trace.svg")
    subprocess.run(["potrace", str(pbm), "-s", "-o", str(svg_tmp), "--flat", "-t", "8", "-a", "1.2", "-O", "0.4",
                    "-W", "24pt", "-H", "24pt"], check=True)
    svg = svg_tmp.read_text()
    # potrace: <g transform="translate(0,24) scale(0.05,-0.05)"> <path d="..."/> </g>
    tr = re.search(r'<g transform="([^"]+)"', svg).group(1)
    paths = "".join(f'<path d="{d}"/>' for d in re.findall(r'<path d="([^"]+)"', svg))
    out = ASSETS / "icons" / f"ic-{name}.svg"
    out.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><g transform="{tr}">{paths}</g></svg>\n')
    pbm.unlink(); svg_tmp.unlink()
    return out


def main():
    args = sys.argv[1:]
    mode = args[0] if args and not args[0].startswith("--") else "gen"
    force = "--force" in args
    only = set(args[args.index("--only") + 1].split(",")) if "--only" in args else None
    names = [n for n in ICONS if not only or n in only]
    RAW.mkdir(parents=True, exist_ok=True); (ASSETS / "icons").mkdir(parents=True, exist_ok=True)
    errors = []
    if mode == "gen":
        def run(n):
            try:
                job_gen(n, force); print("ok", n, flush=True)
            except Exception as e:
                errors.append((n, str(e))); print("FEHLER", n, e, flush=True)
        with ThreadPoolExecutor(max_workers=3) as ex:
            list(ex.map(run, names))
    elif mode == "trace":
        for n in names:
            try:
                trace(n); print("svg", n, flush=True)
            except Exception as e:
                errors.append((n, str(e))); print("FEHLER", n, e, flush=True)
    if errors:
        print("\nFehlgeschlagen:", errors); sys.exit(1)


if __name__ == "__main__":
    main()
