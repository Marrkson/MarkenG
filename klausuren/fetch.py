#!/usr/bin/env python3
"""Lädt von kandidatentreff.de (Seite "Patentanwaltsprüfung (schriftlich)") alle PDFs der
Klausur "Nichttechnische Schutzrechte" (NS) samt Lösungshinweisen herunter und extrahiert den Text.

Aufruf:  python3 klausuren/fetch.py            (schreibt nach klausuren/pdf, klausuren/text, klausuren/source)
Benötigt: pdftotext (poppler-utils). Läuft lokal oder im GitHub-Actions-Workflow fetch-klausuren.yml.
"""
import csv
import html
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

SOURCE = "https://kandidatentreff.de/2018/03/patentanwaltspruefung-schriftlich/"
ROOT = Path(__file__).resolve().parent
PDF = ROOT / "pdf"
TXT = ROOT / "text"
SRC = ROOT / "source"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) MarkenG-Klausurarchiv/1.0"}
NS_RE = re.compile(r"(^|[^A-Za-z])NS([^A-Za-z]|$)")


def get(url, binary=False, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                data = r.read()
                return data if binary else data.decode(r.headers.get_content_charset() or "utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            print(f"  Versuch {i+1} fehlgeschlagen: {url}: {e}")
            time.sleep(2 ** i)
    return None


class Links(HTMLParser):
    """Sammelt (href, Linktext, umgebender Tabellenzeilentext)."""

    def __init__(self):
        super().__init__()
        self.links, self._href, self._text, self._row = [], None, [], []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []
        if tag == "tr":
            self._row = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)
        self._row.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append((self._href, " ".join("".join(self._text).split()), len(self.rows)))
            self._href = None
        if tag == "tr":
            self.rows.append(" ".join(" ".join(self._row).split()))


def is_ns(url, text, row):
    name = urllib.parse.unquote(url.rsplit("/", 1)[-1])
    hay = f"{name} {text} {row}"
    return bool(NS_RE.search(name)) or "nichttechn" in hay.lower() or bool(NS_RE.search(f"{text} {row}"))


def main():
    for d in (PDF, TXT, SRC):
        d.mkdir(parents=True, exist_ok=True)
    print("Lade", SOURCE)
    page = get(SOURCE)
    if page is None:
        sys.exit("Seite nicht erreichbar")
    (SRC / "patentanwaltspruefung-schriftlich.html").write_text(page, encoding="utf-8")
    p = Links()
    p.feed(page)
    rows = p.rows
    all_links, ns_links = [], []
    for href, text, rowidx in p.links:
        url = urllib.parse.urljoin(SOURCE, html.unescape(href))
        row = rows[rowidx] if rowidx < len(rows) else ""
        all_links.append((url, text, row))
        if url.lower().endswith(".pdf") and is_ns(url, text, row):
            ns_links.append((url, text, row))
    with open(SRC / "links.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["url", "linktext", "tabellenzeile"])
        w.writerows(all_links)
    print(f"{len(all_links)} Links, davon {len(ns_links)} NS-PDFs")
    manifest = [["datei", "url", "linktext", "tabellenzeile", "bytes", "status"]]
    seen = set()
    for url, text, row in ns_links:
        name = urllib.parse.unquote(url.rsplit("/", 1)[-1])
        if name in seen:
            continue
        seen.add(name)
        dest = PDF / name
        print("Lade", url)
        data = get(url, binary=True)
        if data is None or not data.startswith(b"%PDF"):
            manifest.append([name, url, text, row, 0, "FEHLER"])
            continue
        dest.write_bytes(data)
        txt = TXT / (dest.stem + ".txt")
        r = subprocess.run(["pdftotext", "-layout", str(dest), str(txt)], capture_output=True, text=True)
        status = "ok" if r.returncode == 0 and txt.exists() and txt.stat().st_size > 200 else f"pdftotext: {r.stderr.strip()[:120] or 'kein Text (Scan?)'}"
        manifest.append([name, url, text, row, len(data), status])
    with open(ROOT / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(manifest)
    print("\n".join(",".join(map(str, m)) for m in manifest))


if __name__ == "__main__":
    main()
