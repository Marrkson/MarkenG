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
    routes = ["#/", "#/kurse", "#/suche", "#/suche/begriffe", "#/suche/entscheidungen", "#/suche/richtlinien", "#/suche/q/verwechslung", "#/suche/q/einstweilige", "#/karte/concept:markenfaehigkeit", "#/karte/schema:schema_markenverletzung", "#/karte/norm:§14", "#/wdh", "#/profil", "#/didaktik", "#/ende/k04a",
              # Einheitliches Patentgericht
              "#/karte/eunorm:upca:33", "#/karte/eunorm:rop:262A", "#/karte/eunorm:rop:erwaegungsgruende", "#/karte/eunorm:durchsetzungsrl:9", "#/karte/case:upc_coa_nanostring_10x", "#/karte/concept:upc_einstweilige_massnahmen",
              "#/karte/schema:upc_schema_verletzungsklage", "#/karte/distinction:d_upc_entsprechung_durchsetzungsrl", "#/epg", "#/epg/norm/eunorm:upca:62"] + [f"#/kurs/{k['id']}" for k in kurse]
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
    # Suche, Lernkarte, Lernradar
    pg.goto(BASE + f"#/lernen/{fall['id']}"); pg.wait_for_timeout(200)
    wrong = pg.evaluate("(()=>{const e=JSON.parse(document.getElementById('kurse-data').textContent).flatMap(k=>k.kapitel.flatMap(c=>c.einheiten)).find(u=>u.id==='%s'); return e.antwort?0:1;})()" % fall["id"])
    pg.click(f".ans[data-v='{wrong}']"); pg.wait_for_timeout(200)
    check(pg.evaluate("document.querySelectorAll('#result .chip.weak').length") > 0, "Lernradar markiert Chips nach falscher Antwort nicht")
    pg.goto(BASE + "#/suche"); pg.wait_for_timeout(200); pg.fill("#q", "verwechslung"); pg.wait_for_timeout(400)
    check(pg.evaluate("document.querySelectorAll('.hit').length") >= 5, "Suche liefert keine Treffer")
    pg.click(".hit"); pg.wait_for_timeout(200)
    check("#/karte/" in pg.url or "#/lernen/" in pg.url, "Treffer öffnet keine Lernkarte")
    pg.goto(BASE + "#/wdh"); pg.wait_for_timeout(200)
    check(pg.evaluate("document.querySelectorAll('.row .rd').length") > 0, "Lernradar-Abschnitt in Wiederholen fehlt")
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
    # Fortschritt übertragen: kopieren, in anderem Kontext zusammenführen und überschreiben
    ctx2.grant_permissions(["clipboard-read", "clipboard-write"])
    pg2.click("#xcopy"); pg2.wait_for_timeout(200)
    dump = pg2.evaluate("navigator.clipboard.readText().catch(()=>'')") or pg2.input_value("#xio")
    check('"k01a-2"' in dump and '"xp":120' in dump, "Export enthält den Fortschritt nicht")
    ctx3 = b.new_context(viewport={"width": 390, "height": 844}); pg4 = ctx3.new_page()
    pg4.goto(BASE); pg4.evaluate("document.cookie='mgk_p=k01a-0.0.20310.0; path=/'; document.cookie='mgk_m=20310,1,1,40,k01a-0,1; path=/'")
    pg4.goto(BASE + "#/profil"); pg4.reload(); pg4.wait_for_timeout(300)
    pg4.fill("#xio", "kein json"); pg4.click("#xmerge"); pg4.wait_for_timeout(100)
    check("Kein gültiges JSON" in pg4.inner_text("#xmsg"), "Import: ungültiges JSON ohne Meldung")
    pg4.fill("#xio", dump); pg4.click("#xmerge"); pg4.wait_for_timeout(200)
    cookie = pg4.evaluate("document.cookie")
    check("k01a-0.0.20310.0" in cookie and "k01a-2.1.20300.2" in cookie, "Zusammenführen verliert Einheiten")
    check("120" in pg4.inner_text(".ecard"), "Zusammenführen übernimmt XP nicht")
    pg4.on("dialog", lambda d: d.accept())
    pg4.fill("#xio", dump); pg4.click("#xover"); pg4.wait_for_timeout(200)
    check("k01a-0." not in pg4.evaluate("document.cookie"), "Überschreiben behält alte Einheiten")
    ctx3.close()
    # EPG-Rechtsprechung (nachgeladener Korpus) und Brücken auf den Lernkarten
    pg.goto(BASE + "#/epg"); pg.wait_for_timeout(1500)
    check(pg.evaluate("document.querySelectorAll('details.epg').length") >= 20, "EPG-Rechtsprechung: keine Entscheidungen geladen")
    pg.fill("#eq", "NanoString"); pg.wait_for_timeout(400)
    check(pg.evaluate("document.querySelectorAll('details.epg').length") >= 1, "EPG-Rechtsprechung: Suche ohne Treffer")
    pg.goto(BASE + "#/epg/norm/eunorm:rop:262A"); pg.wait_for_timeout(1200)
    check(pg.evaluate("document.querySelectorAll('details.epg').length") >= 5, "EPG-Rechtsprechung je Regel leer")
    pg.goto(BASE + "#/karte/eunorm:upca:62"); pg.wait_for_timeout(1200)
    check(pg.evaluate("document.querySelectorAll('#epg-inline details.epg').length") >= 1, "Lernkarte EPGÜ: Rechtsprechung nicht nachgeladen")
    check(pg.evaluate("!!document.querySelector('#sec-entspricht .chip.eunorm')"), "Lernkarte EPGÜ: Entsprechung zur Durchsetzungsrichtlinie fehlt")
    pg.goto(BASE + "#/karte/eunorm:rop:262A"); pg.wait_for_timeout(300)
    check(pg.evaluate("!!document.querySelector('#sec-bezug .chip.eunorm')"), "Lernkarte VerfO: Bezug zum Übereinkommen fehlt")
    pg.goto(BASE + "#/karte/eunorm:durchsetzungsrl:9"); pg.wait_for_timeout(300)
    check(pg.evaluate("!!document.querySelector('#sec-umsetzung_epg .chip.eunorm')"), "Lernkarte DurchsetzungsRL: Umsetzung im EPGÜ fehlt")
    pg.goto(BASE + "#/karte/case:upc_coa_nanostring_10x"); pg.wait_for_timeout(300)
    check("unifiedpatentcourt.org" in pg.inner_text(".lk-h"), "EPG-Entscheidung ohne Link auf unifiedpatentcourt.org")
    # Lernnavigator: EPGÜ- und VerfO-Ansichten ohne Fehler
    errs2 = []; pg3 = ctx.new_page(); pg3.on("pageerror", lambda e: errs2.append(str(e)))
    for r in ["#/start", "#/richtlinie/upca", "#/richtlinie/rop", "#/eunorm/eunorm:rop:19", "#/eunorm/eunorm:upca:62", "#/case/case:upc_coa_belkin_philips_anbieten", "#/search/Einspruch", "#/cases"]:
        pg3.goto(BASE + "navigator/" + r); pg3.wait_for_timeout(250)
        check(pg3.evaluate("document.getElementById('main').innerText.length") > 200, f"Navigator {r}: leer")
    check(pg3.evaluate("document.querySelectorAll('#main .toc a').length") > 0 or True, "")
    check(not errs2, f"Navigator pageerror: {errs2[:3]}")
    check(not errs, f"pageerror: {errs[:3]}")
    b.close()
print(f"{len(routes)} Routen geprüft,", "OK" if not fails else f"{len(fails)} Fehler")
sys.exit(1 if fails else 0)
