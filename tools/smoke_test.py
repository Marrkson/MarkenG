# -*- coding: utf-8 -*-
"""Rauchtest für IPelico (docs/index.html) über einen lokalen HTTP-Server.

  (cd docs && python3 -m http.server 8791 &) ; python3 tools/smoke_test.py [http://localhost:8791/]

Prüft: keine pageerror, alle <use>-Referenzen lösen auf, keine leeren Chip-Zeilen, Gesetzeslinks mit href,
Antwortfluss inkl. Tastatur, Cookie-Kompatibilität mit dem alten Format, Theme-Umschaltung.
"""
import json, sys
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8791/"
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg); print("FEHLER", msg)


with sync_playwright() as pw:
    b = pw.chromium.launch()
    ctx = b.new_context(viewport={"width": 390, "height": 844})
    pg = ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(BASE + "#/"); pg.wait_for_timeout(500)
    kurse = pg.evaluate("JSON.parse(document.getElementById('kurse-data').textContent).map(k=>({id:k.id,units:k.kapitel.flatMap(c=>c.einheiten.map(e=>({id:e.id,typ:e.typ})))}))")
    units = [u for k in kurse for u in k["units"]]
    routes = ["#/", "#/wdh", "#/profil", "#/didaktik", "#/ende/k04a"] + [f"#/kurs/{k['id']}" for k in kurse]
    sample = [u for u in units if u["typ"] in ("intro", "schema")] + units[::7]
    routes += [f"#/lernen/{u['id']}" for u in sample]
    for r in routes:
        pg.goto(BASE + r); pg.wait_for_timeout(120)
        missing = pg.evaluate("[...document.querySelectorAll('use')].map(u=>u.getAttribute('href')).filter(h=>!document.querySelector(h))")
        check(not missing, f"{r}: fehlende Symbole {missing[:3]}")
        empty = pg.evaluate("[...document.querySelectorAll('.chips')].filter(c=>!c.children.length).length")
        check(empty == 0, f"{r}: leere Chip-Zeilen")
        bad_links = pg.evaluate("[...document.querySelectorAll('a.lawlink')].filter(a=>!a.getAttribute('href')).length")
        check(bad_links == 0, f"{r}: Gesetzeslinks ohne href")
    # Antwortfluss: Klick, Chip öffnen, Enter
    fall = next(u for u in units if u["typ"] == "fall")
    pg.goto(BASE + f"#/lernen/{fall['id']}"); pg.wait_for_timeout(200)
    pg.click(".ans"); pg.wait_for_timeout(200)
    check(pg.is_visible("#result"), "Ergebnis nicht sichtbar")
    check(pg.query_selector("#result .btn") is not None, "Weiter-Button fehlt")
    chip = pg.query_selector("#result .chip[data-node]")
    if chip:
        chip.click(); pg.wait_for_timeout(150)
        check(pg.query_selector("#result .inline") is not None, "Inline-Karte öffnet nicht")
    before = pg.url; pg.keyboard.press("Enter"); pg.wait_for_timeout(200)
    check(pg.url != before, "Enter führt nicht weiter")
    mc = next((u for u in units if u["typ"] == "mc"), None)
    if mc:
        pg.goto(BASE + f"#/lernen/{mc['id']}"); pg.wait_for_timeout(200); pg.keyboard.press("2"); pg.wait_for_timeout(150)
        check(pg.is_visible("#result"), "MC-Tastatur 2 ohne Ergebnis")
    check(pg.evaluate("document.cookie.includes('mgk_p=')"), "Cookie mgk_p nicht gesetzt")
    # Cookie-Kompatibilität (altes Format) und Theme
    ctx2 = b.new_context(viewport={"width": 390, "height": 844}); pg2 = ctx2.new_page()
    pg2.goto(BASE); pg2.evaluate("document.cookie='mgk_p=k01a-2.1.20300.2; path=/'; document.cookie='mgk_m=20300,3,5,120,k01a-2,1; path=/'")
    pg2.goto(BASE + "#/profil"); pg2.reload(); pg2.wait_for_timeout(300)
    check("120" in pg2.inner_text(".ecard"), "XP aus altem Cookie nicht übernommen")
    check(pg2.is_hidden("#notice"), "Hinweis trotz ack sichtbar")
    pg2.click("#theme button[data-t=dark]"); pg2.wait_for_timeout(100)
    check(pg2.evaluate("document.documentElement.dataset.theme") == "dark", "Dunkel-Theme nicht gesetzt")
    check(pg2.evaluate("localStorage.getItem('mgk_theme')") == "dark", "mgk_theme nicht gespeichert")
    pg2.click("#theme button[data-t=system]"); pg2.wait_for_timeout(100)
    check(pg2.evaluate("localStorage.getItem('mgk_theme')") is None, "System löscht mgk_theme nicht")
    check(not errs, f"pageerror: {errs[:3]}")
    b.close()
print(f"{len(routes)} Routen geprüft,", "OK" if not fails else f"{len(fails)} Fehler")
sys.exit(1 if fails else 0)
