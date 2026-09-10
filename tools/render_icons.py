# -*- coding: utf-8 -*-
"""Rendert die App-Icons (Homescreen, Favicon) aus src/templates/ipelico/logo/ipelico-badge.svg.
  python3 tools/render_icons.py     (braucht Python-Playwright mit Chromium)
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

LOGO = Path(__file__).resolve().parent.parent / "src" / "templates" / "ipelico" / "logo"
badge = (LOGO / "ipelico-badge.svg").read_text()
full = badge.replace('rx="24"', 'rx="0"')   # iOS und Android runden selbst
SIZES = {"apple-touch-icon.png": (full, 180), "icon-192.png": (full, 192), "icon-512.png": (full, 512),
         "favicon-32.png": (badge, 32), "favicon-16.png": (badge, 16)}
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, (svg, s) in SIZES.items():
        html = f'<body style="margin:0;background:transparent"><div style="width:{s}px;height:{s}px">{svg.replace("<svg ", f"<svg width={s} height={s} ", 1)}</div></body>'
        pg = b.new_page(viewport={"width": s, "height": s}); pg.set_content(html)
        pg.screenshot(path=str(LOGO / name), omit_background=True); pg.close(); print(name)
    b.close()
