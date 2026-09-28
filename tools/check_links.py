#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ruft jeden Gesetzeslink, den die Apps erzeugen, einmal ab und prüft, ob die Zielseite existiert und die richtige
Vorschrift zeigt (gesetze-im-internet.de: Überschrift „§ 14 …“ bzw. „Art 5 …“; epo.org: Artikel/Regel).

Quellen der Links: alle Texte aus tools/check_zitate.py (Inhalte, Normtexte, Leitsätze) über gesetze.resolve/href_for sowie
die url-Felder der Norm-Knoten. EUR-Lex beantwortet automatisierte Abrufe mit einer Bot-Prüfung (202) und wird nur
gezählt, nicht geprüft.

Aufruf:  python3 tools/check_links.py [--json DATEI]      (Netz nötig; ca. 8 parallele Abrufe)
"""
import concurrent.futures as cf
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

import build_graph  # noqa: E402
import check_zitate  # noqa: E402
from knowledge.gesetze import resolve, href_for  # noqa: E402

# epo.org, echr.coe.int, wto.org und unifiedpatentcourt.org beantworten Skript-Kennungen mit 403; deshalb Browser-Kennung
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36 IPelico-Linkpruefung"}


def collect():
    graph = build_graph.build(write=False, unknown=[])
    links = defaultdict(set)   # url -> {(knoten, zitat)}
    for _, nid, _, text, ctx in check_zitate.items(graph):
        for m, law, _ in resolve(text, ctx):
            u = href_for(m, law)
            if u:
                links[u].add((nid, m.group(0)))
    for n in graph["nodes"]:
        if n["type"] in ("norm", "eunorm") and n.get("url"):
            links[n["url"]].add((n["id"], n["label"]))
    return links


def fetch(url):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                body = r.read(400000)
                return r.status, body.decode("latin-1" if "gesetze-im-internet" in url else "utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, ""
        except Exception as e:  # noqa: BLE001
            err = str(e)
            time.sleep(1 + attempt)
    return 0, err


def expected_heading(url):
    """gesetze-im-internet: .../__14a.html -> '§ 14a', .../art_5.html -> 'Art 5', art_ii__6 -> '§ 6' (Art. II IntPatÜG)."""
    m = re.search(r"/(?:art_[ivx]+)?__(\d+[a-z]*)\.html$", url)
    if m:
        return "§ " + m.group(1)
    m = re.search(r"/art_(\d+[a-z]*)\.html$", url)
    if m:
        return "Art " + m.group(1)
    return None


def check(url):
    if "eur-lex.europa.eu" in url:
        return url, "übersprungen (EUR-Lex-Botschutz)", None
    status, body = fetch(url)
    if status != 200:
        return url, "HTTP %s" % status, None
    heading = None
    if "gesetze-im-internet.de" in url:
        m = re.search(r'<span class="jnenbez">(.*?)</span>', body)
        t = re.search(r'<span class="jnentitel">(.*?)</span>', body)
        heading = html.unescape(re.sub(r"<[^>]+>", "", (m.group(1) if m else "") + " " + (t.group(1) if t else ""))).strip()
        exp = expected_heading(url)
        got = (m and html.unescape(m.group(1)).replace("\xa0", " ").strip()) or ""
        if exp and got.replace("Art.", "Art") != exp:
            return url, "falsche Seite (erwartet %s, gefunden %r)" % (exp, got), heading
        if "(weggefallen)" in heading or "weggefallen" in (t.group(1) if t else ""):
            return url, "weggefallen", heading   # Seite existiert; als Ziel eines Zitats ein Fehler, als url eines Norm-Knotens nicht
    return url, "ok", heading


def main():
    links = collect()
    print(len(links), "verschiedene Links", file=sys.stderr)
    results = {}
    with cf.ThreadPoolExecutor(8) as ex:
        for url, status, heading in ex.map(check, sorted(links)):
            results[url] = (status, heading)
    def is_bad(u, r):
        if r[0] == "ok" or r[0].startswith("übersprungen"):
            return False
        if r[0] == "weggefallen":   # nur beanstanden, wenn ein Zitat (nicht bloß der Norm-Knoten selbst) dorthin zeigt
            return any(not nid.startswith(("norm:", "eunorm:")) for nid, _ in links[u])
        return True
    bad = {u: r for u, r in results.items() if is_bad(u, r)}
    by_host = defaultdict(lambda: defaultdict(int))
    for u, (st, _) in results.items():
        by_host[re.sub(r"^https?://([^/]+)/.*$", r"\1", u)][st.split(" (")[0]] += 1
    for h, c in sorted(by_host.items()):
        print(h, dict(c))
    for u, (st, hd) in sorted(bad.items()):
        refs = sorted(links[u])[:4]
        print("FEHLER", st, u, "| z. B.", "; ".join("%s: %s" % r for r in refs))
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(
            {u: dict(status=r[0], ueberschrift=r[1], stellen=sorted(links[u])) for u, r in results.items()}, ensure_ascii=False, indent=0))
    print("\n%d Links geprüft, %d fehlerhaft" % (len(results), len(bad)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
