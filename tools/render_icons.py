# -*- coding: utf-8 -*-
"""Rendert die App-Icons (Homescreen, Favicon) aus src/templates/ipelico/logo/ipelico-badge.svg.
  python3 tools/render_icons.py     (braucht Python-Playwright mit Chromium)
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

LOGO = Path(__file__).resolve().parent.parent / "src" / "templates" / "ipelico" / "logo"
badge = (LOGO / "ipelico-badge.svg").read_text()
full = badge.replace('rx="24"', 'rx="0"')   # iOS und Android runden selbst
# maskable: Android schneidet bis zu 20 % je Seite ab; das Zeichen bleibt in der sicheren Mitte (Skalierung .6)
maskable = full.replace('transform="translate(8 8) scale(.84)"', 'transform="translate(20 20) scale(.6)"')
SIZES = {"apple-touch-icon.png": (full, 180), "icon-192.png": (full, 192), "icon-512.png": (full, 512),
         "icon-maskable-512.png": (maskable, 512),
         "favicon-48.png": (badge, 48), "favicon-32.png": (badge, 32), "favicon-16.png": (badge, 16)}
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, (svg, s) in SIZES.items():
        html = f'<body style="margin:0;background:transparent"><div style="width:{s}px;height:{s}px">{svg.replace("<svg ", f"<svg width={s} height={s} ", 1)}</div></body>'
        pg = b.new_page(viewport={"width": s, "height": s}); pg.set_content(html)
        pg.screenshot(path=str(LOGO / name), omit_background=True); pg.close(); print(name)
    b.close()
# favicon.ico mit 16, 32 und 48 px (Browser ohne SVG/PNG-Favicon, GitHub Pages, Lesezeichen)
from PIL import Image
frames = [Image.open(LOGO / f"favicon-{n}.png").convert("RGBA") for n in (48, 32, 16)]
frames[0].save(LOGO / "favicon.ico", format="ICO", sizes=[(48, 48), (32, 32), (16, 16)], append_images=frames[1:])
print("favicon.ico")
