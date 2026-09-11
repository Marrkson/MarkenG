#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quellen für das Wissenspaket UPC beschaffen (Netz + Postgres) und als JSON unter data/ ablegen.

Erzeugt (alle mitversioniert, damit `build.py` ohne Netz und ohne Datenbank läuft):
  data/upca.json           Übereinkommen über ein Einheitliches Patentgericht (EPGÜ/UPCA), Art. 1–89,
                           deutscher und englischer Wortlaut von epo.org (Fassung 2022)
  data/upc_rop.json        Verfahrensordnung (VerfO/RoP), deutscher Wortlaut, konsolidierte Fassung
                           (Stand laut Deckblatt), englische Regeltitel; je Regel „Bezug zum Übereinkommen“
  data/upc_decisions.json  Alle Entscheidungen und Anordnungen aus der Tabelle UpcDecision (RheinIP-Datenbank):
                           Metadaten, Leitsätze/Schlagworte (aus dem Volltext extrahiert), zitierte Artikel
                           und Regeln (Zählung im Volltext). Volltexte werden nicht versioniert.
  data/up_epatvo.json      Verordnung (EU) Nr. 1257/2012 (Einheitspatent, EPatVO), Art. 1–18, deutsch und englisch (epo.org)
  data/up_epatuevo.json    Verordnung (EU) Nr. 1260/2012 (Übersetzungsregelungen, EPatÜVO), Art. 1–7
  data/up_doeps.json       Durchführungsordnung zum einheitlichen Patentschutz (DOEPS, engl. UPR), Regeln 1–24
  data/up_gebeps.json     Gebührenordnung zum einheitlichen Patentschutz (GebOEPS, engl. RFeesUPP), Art. 1–7
                           (Quelle: RheinIP-Datenbank, Tabelle UPLegaltext, instrument epatvo/epatuevo/doeps/gebeps, deutsch und englisch,
                           Spiegel der fortlaufend aktualisierten HTML-Sammlung „Rechtstexte zum Einheitspatentsystem“ auf epo.org;
                           ohne Datenbank (--no-db) direkt von epo.org bzw. aus dem Cache)
  data/up_richtlinien.json UP-Richtlinien (Richtlinien für das Einheitspatent, Ausgabe 2026) abschnittsweise und die EPA-Informationsseiten
                           zum Einheitspatent (epo.org/de/applying/european/unitary/unitary-patent/*), deutsch mit englischen Titeln
                           (UPLegaltext, instrument up-gl und up-info; nur aus der Datenbank, mit --no-db bleibt die Datei unverändert)

Aufruf:  python3 tools/fetch_upc.py [--no-net] [--no-db]
Zwischenstände (HTML, PDF) liegen in ~/.cache/ipelico/upc/. Postgres-Zugang: POSTGRES_LOGIN aus
~/github/RheinIP/.env (wie script/utils/db_utils.py dort).
"""
import collections
import html as htmlmod
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path.home() / ".cache" / "ipelico" / "upc"
UA = {"User-Agent": "Mozilla/5.0 (IPelico fetch_upc)"}
ROP_PDF = {
    "de": "https://www.unifiedpatentcourt.org/sites/default/files/upc_documents/Consolidated%20Rules%20of%20Procedure%20UPC_DE.pdf",
    "en": "https://www.unifiedpatentcourt.org/sites/default/files/upc_documents/rop_en_25_july_2022_final_consolidated_published_on_website.pdf",
}
UPCA_URL = "https://www.epo.org/%s/legal/up-upc/2022/upca_%d.html"
UPCA_ARTICLES = 89


def fetch(url, target, net=True):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 1000:
        return target.read_bytes()
    if not net:
        raise SystemExit("fehlt im Cache und --no-net gesetzt: %s" % url)
    data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
    target.write_bytes(data)
    return data


# ---------------------------------------------------------------- UPCA (epo.org, HTML je Artikel)
_MAIN = re.compile(r"<main\b.*?</main>", re.S)
_MENU = re.compile(r'\["(TEIL [IVX]+ – [^"]+)","/de/legal/up-upc/2022/upca_p[^"]*","",\[(.*?)\]\]\](?=,\["TEIL|\]\]\])', re.S)


def _lines(html):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", html, flags=re.S)
    t = re.sub(r"<[^>]+>", "\n", t)
    t = htmlmod.unescape(t).replace("\xa0", " ")
    return [ln for ln in (re.sub(r"\s+", " ", x).strip() for x in t.split("\n")) if ln]


def parse_upca_page(html, nr, lang):
    m = _MAIN.search(html)
    lines = _lines(m.group(0) if m else html)
    art = ("Artikel" if lang == "de" else "Article") + " %d" % nr
    ueb = "Übersicht" if lang == "de" else "Overview"
    i = None
    for k, ln in enumerate(lines):
        if ln == art and k > 0 and lines[k - 1] == ueb:
            i = k
            break
    if i is None:
        raise SystemExit("Artikel %d (%s): Textblock nicht gefunden" % (nr, lang))
    kapitel = lines[i - 2] if re.match(r"(KAPITEL|CHAPTER)\b", lines[i - 2]) else ""
    titel = lines[i + 1]
    body = []
    for ln in lines[i + 2:]:
        if ln in ("Weiter", "Zurück", "Next", "Previous", "Show modifications") or ln.startswith("Drucken") or ln.startswith("Print"):
            break
        body.append(ln)
    absaetze, cur = [], ""
    for ln in body:
        if re.fullmatch(r"\(\d+\)", ln):
            if cur.strip():
                absaetze.append(cur.strip())
            cur = ln + " "
            continue
        cur += ln + " "
    if cur.strip():
        absaetze.append(cur.strip())
    absaetze = [re.sub(r"\s+([,.;:)])", r"\1", re.sub(r"\(\s+", "(", a)) for a in absaetze]
    return dict(nr=nr, titel=titel, kapitel=kapitel, absaetze=absaetze)


def parse_teile(html):
    """Teil-Überschriften aus dem Inhaltsverzeichnis (oMenu-Skript) je Artikelnummer."""
    teile = {}
    for m in re.finditer(r'\["(TEIL [IVX]+ – [^"]+)","/de/legal/up-upc/2022/upca_p', html):
        start = m.start()
        nxt = re.search(r'\["TEIL [IVX]+ – ', html[m.end():])
        chunk = html[start: m.end() + nxt.start()] if nxt else html[start:start + 60000]
        for a in re.findall(r"upca_(\d+)\.html", chunk):
            teile.setdefault(int(a), m.group(1))
    return teile


def build_upca(net):
    de, en = {}, {}
    teile = {}
    for nr in range(1, UPCA_ARTICLES + 1):
        for lang, store in (("de", de), ("en", en)):
            raw = fetch(UPCA_URL % (lang, nr), CACHE / "upca_html" / ("%s_%d.html" % (lang, nr)), net).decode("utf-8", "replace")
            store[nr] = parse_upca_page(raw, nr, lang)
            if lang == "de" and not teile:
                teile = parse_teile(raw)
    arts = []
    for nr in range(1, UPCA_ARTICLES + 1):
        d, e = de[nr], en[nr]
        arts.append(dict(nr=nr, titel=d["titel"], titel_en=e["titel"], teil=teile.get(nr, ""), kapitel=d["kapitel"], kapitel_en=e["kapitel"],
                         absaetze=d["absaetze"], absaetze_en=e["absaetze"],
                         url=UPCA_URL % ("de", nr), url_en=UPCA_URL % ("en", nr)))
    meta = dict(titel="Übereinkommen über ein Einheitliches Patentgericht (EPGÜ, UPCA)", kurz="UPCA",
                quelle="https://www.epo.org/de/legal/up-upc/2022/index.html", stand="Fassung 2022 (epo.org, Rechtstexte Einheitspatent und EPG)",
                hinweis="Amtlicher Wortlaut; deutsche, englische und französische Fassung sind gleichermaßen verbindlich (Art. 88 UPCA).")
    return dict(meta=meta, artikel=arts)


# ---------------------------------------------------------------- Einheitspatent: EPatVO, EPatÜVO, DOEPS, GebOEPS (epo.org, HTML je Artikel/Regel)
EPO_URL = "https://www.epo.org/%s/legal/up-upc/2022/%s_%d.html"
_HEAD = re.compile(r"^(Artikel|Article|Regel|Rule)\s+(\d+)(?:\s+(.+))?$")
UP_TEXTE = [
    dict(key="epatvo", prefix="eu20121257", n=18, kopf=("Artikel", "Article"), datei="up_epatvo.json", kurz="EPatVO",
         titel="Verordnung (EU) Nr. 1257/2012 über die Umsetzung der Verstärkten Zusammenarbeit im Bereich der Schaffung eines einheitlichen Patentschutzes (EPatVO)",
         hinweis="Amtlicher Wortlaut (ABl. EU L 361 vom 31.12.2012, S. 1; ABl. EPA 2013, 111); in Kraft seit 20.1.2013, anwendbar seit 1.6.2023 (Art. 18)."),
    dict(key="epatuevo", prefix="eu20121260", n=7, kopf=("Artikel", "Article"), datei="up_epatuevo.json", kurz="EPatÜVO",
         titel="Verordnung (EU) Nr. 1260/2012 über die Umsetzung der Verstärkten Zusammenarbeit im Bereich der Schaffung eines einheitlichen Patentschutzes im Hinblick auf die anzuwendenden Übersetzungsregelungen (EPatÜVO)",
         hinweis="Amtlicher Wortlaut (ABl. EU L 361 vom 31.12.2012, S. 89; ABl. EPA 2013, 132); in Kraft seit 20.1.2013, anwendbar seit 1.6.2023 (Art. 7)."),
    dict(key="doeps", prefix="upr", n=24, kopf=("Regel", "Rule"), datei="up_doeps.json", kurz="DOEPS",
         titel="Durchführungsordnung zum einheitlichen Patentschutz (DOEPS)",
         hinweis="Beschluss des Engeren Ausschusses des Verwaltungsrats vom 15.12.2015 (SC/D 1/15), zuletzt geändert durch Beschluss vom 9.10.2025 (laut epo.org, HTML-Sammlung Rechtstexte zum Einheitspatentsystem)."),
    dict(key="gebeps", prefix="upf", n=7, kopf=("Artikel", "Article"), datei="up_gebeps.json", kurz="GebOEPS",
         titel="Gebührenordnung zum einheitlichen Patentschutz (GebOEPS)",
         hinweis="Beschluss des Engeren Ausschusses des Verwaltungsrats vom 15.12.2015 (SC/D 2/15), zuletzt geändert durch Beschluss vom 9.10.2025 (laut epo.org); Jahresgebührenbeträge stehen in Art. 2."),
]


def parse_epo_page(html, nr, lang, kopf):
    m = _MAIN.search(html)
    return parse_epo_lines(_lines(m.group(0) if m else html), nr, lang, kopf)


def parse_epo_lines(lines, nr, lang, kopf):
    """Artikel-/Regelseite der epo.org-Sammlung (als Zeilen, aus HTML oder aus UPLegaltext.text): Kapitelzeile, Kopf
    („Artikel 3“ oder „Article 4 Title“), Titel, Absätze. Absatzmarken sind „(1)“ (EPGÜ, DOEPS) oder „1.“ (EU-Verordnungen,
    englische Fassung); Buchstabenpunkte bleiben im Absatztext."""
    lines = [ln for ln in (re.sub(r"\s+", " ", x.replace("\xa0", " ")).strip() for x in lines) if ln]
    ueb = "Übersicht" if lang == "de" else "Overview"
    i, head = None, None
    for k, ln in enumerate(lines):
        h = _HEAD.match(ln)
        if h and h.group(1) == kopf and int(h.group(2)) == nr and k > 0 and lines[k - 1] == ueb:
            i, head = k, h
            break
    if i is None:
        raise SystemExit("%s %d (%s): Textblock nicht gefunden" % (kopf, nr, lang))
    kapitel = lines[i - 2] if re.match(r"(KAPITEL|CHAPTER)\b", lines[i - 2]) else ""
    if head.group(3):
        titel, start = head.group(3).strip(), i + 1
    else:
        titel, start = lines[i + 1], i + 2
    body = []
    for ln in lines[start:]:
        if ln in ("Weiter", "Zurück", "Next", "Previous", "Show modifications") or ln.startswith("Drucken") or ln.startswith("Print"):
            break
        body.append(ln)
    absaetze, cur = [], ""
    for ln in body:
        if re.fullmatch(r"\(\d+\)", ln) or re.fullmatch(r"\d+\.", ln):
            if cur.strip():
                absaetze.append(cur.strip())
            cur = ("(%s) " % ln.strip("().")) if ln.endswith(".") else ln + " "
            continue
        cur += ln + " "
    if cur.strip():
        absaetze.append(cur.strip())
    absaetze = [re.sub(r"\s+([,.;:)])", r"\1", re.sub(r"\(\s+", "(", a)) for a in absaetze]
    return dict(nr=nr, titel=titel, kapitel=kapitel, absaetze=absaetze)


def parse_teile_prefix(html, prefix):
    """Teil-Überschriften (TEIL I – …) aus dem Inhaltsverzeichnis je Nummer; leer bei Texten ohne Teile (Verordnungen, GebOEPS)."""
    teile = {}
    html = html.replace("\xa0", " ").replace("\u200d", "")  # Menü schreibt „TEIL I“ mit geschütztem Leerzeichen, „NR. 1257“ mit Zero-Width-Joiner
    for m in re.finditer(r'\["(TEIL [IVX]+ – [^"]+)","/de/legal/up-upc/2022/' + re.escape(prefix) + r'_p', html):
        start = m.start()
        nxt = re.search(r'\["TEIL [IVX]+ – ', html[m.end():])
        chunk = html[start: m.end() + nxt.start()] if nxt else html[start:start + 60000]
        for a in re.findall(re.escape(prefix) + r"_(\d+)\.html", chunk):
            teile.setdefault(int(a), re.sub(r"\s+", " ", m.group(1)))
    return teile


def parse_teile_index(text):
    """Teil-Überschrift je Regel/Artikel aus dem Inhaltsverzeichnis (UPLegaltext, sectionId index): Zeilen „TEIL II – …“,
    darunter „Regel 5“ / „Artikel 3“ als eigene Zeilen."""
    teile, cur = {}, ""
    for ln in text.replace("\xa0", " ").replace("\u200d", "").split("\n"):
        ln = re.sub(r"\s+", " ", ln).strip()
        if ln.startswith("TEIL "):
            cur = ln
        m = re.fullmatch(r"(?:Regel|Artikel) (\d+)", ln)
        if m and cur:
            teile.setdefault(int(m.group(1)), cur)
    return teile


def up_db_rows():
    """Alle Zeilen der Tabelle UPLegaltext: {(instrument, lang, sectionId): dict(text, url, titel, stand)}."""
    cur = _db_cursor()
    cur.execute('select instrument, lang, "sectionId", text, url, "documentTitle", "updatedAt" from "UPLegaltext"')
    return {(i, l, sec): dict(text=t or "", url=u, titel=d or "", stand=up.date().isoformat() if up else "") for i, l, sec, t, u, d, up in cur.fetchall()}


def build_up_text(t, net, db=None):
    """Aus der Datenbank (UPLegaltext, Vorrang) oder von epo.org (HTML-Cache)."""
    de, en, teile, urls = {}, {}, {}, {}
    sec = "r" if t["kopf"][0] == "Regel" else "a"
    stand = ""
    for nr in range(1, t["n"] + 1):
        for lang, store, kopf in (("de", de, t["kopf"][0]), ("en", en, t["kopf"][1])):
            row = db.get((t["key"], lang, "%s%d" % (sec, nr))) if db else None
            if row:
                store[nr] = parse_epo_lines(row["text"].split("\n"), nr, lang, kopf)
                urls[(lang, nr)] = row["url"]
                stand = max(stand, row["stand"])
            else:
                raw = fetch(EPO_URL % (lang, t["prefix"], nr), CACHE / "up_html" / ("%s_%s_%d.html" % (t["prefix"], lang, nr)), net).decode("utf-8", "replace")
                store[nr] = parse_epo_page(raw, nr, lang, kopf)
                urls[(lang, nr)] = EPO_URL % (lang, t["prefix"], nr)
                if lang == "de" and not teile:
                    teile = parse_teile_prefix(raw, t["prefix"])
    if db and (t["key"], "de", "index") in db:
        teile = parse_teile_index(db[(t["key"], "de", "index")]["text"]) or teile
    arts = []
    for nr in range(1, t["n"] + 1):
        d, e = de[nr], en[nr]
        arts.append(dict(nr=nr, titel=d["titel"], titel_en=e["titel"], teil=teile.get(nr, ""), kapitel=d["kapitel"], kapitel_en=e["kapitel"],
                         absaetze=d["absaetze"], absaetze_en=e["absaetze"], url=urls[("de", nr)], url_en=urls[("en", nr)]))
    quelle_db = "RheinIP-Datenbank, Tabelle UPLegaltext (Spiegel von epo.org, Stand %s)" % stand if stand else "epo.org (HTML-Sammlung, ohne Datenbank abgerufen)"
    meta = dict(titel=t["titel"], kurz=t["kurz"], zitat=t["kopf"][0], quelle="https://www.epo.org/de/legal/up-upc/2022/%s.html" % t["prefix"],
                quelle_db=quelle_db, stand="HTML-Sammlung „Rechtstexte zum Einheitspatentsystem“ (epo.org, fortlaufend aktualisiert); %s" % quelle_db, hinweis=t["hinweis"])
    return dict(meta=meta, artikel=arts)


def _gl_text(text):
    """Abschnittstext der UP-Richtlinien: erste Zeile ist die Überschrift; Zeilenumbrüche der Zitate wieder zusammenziehen."""
    lines = [re.sub(r"\s+", " ", x.replace("\xa0", " ")).strip() for x in text.split("\n")]
    lines = [x for x in lines if x and x not in ("Zurück", "Weiter", "Previous", "Next")]
    head = lines[0] if lines else ""
    body = " ".join(lines[1:])
    body = re.sub(r"\s+([,.;:)])", r"\1", re.sub(r"\(\s+", "(", body))
    return head, body


def build_up_richtlinien(db):
    """UP-Richtlinien (up-gl) abschnittsweise und EPA-Informationsseiten (up-info), deutsch; englische Titel und URLs dazu."""
    abschnitte, info, stand = [], [], ""
    for (inst, lang, sec), row in sorted(db.items(), key=lambda kv: (kv[0][0], [int(x) if x.isdigit() else x for x in kv[0][2].split("_")])):
        if lang != "de" or inst not in ("up-gl", "up-info"):
            continue
        en = db.get((inst, "en", sec)) or {}
        head, body = _gl_text(row["text"])
        head_en = _gl_text(en["text"])[0] if en else ""
        stand = max(stand, row["stand"])
        if inst == "up-gl":
            m = re.match(r"([\d.]+)\.?\s+(.*)", head)
            nr, titel = (m.group(1), m.group(2)) if m else (sec.replace("_", "."), head)
            abschnitte.append(dict(id=sec, nr=nr, titel=titel, titel_en=re.sub(r"^[\d.]+\s+", "", head_en), url=row["url"], url_en=en.get("url", ""), text=body))
        else:
            lines = [x for x in _gl_text(row["text"])]
            abschnitte_txt = row["text"].split("\n")
            # Informationsseiten: Titel = erste Zeile nach den Navigationszeilen (Einheitspatent & …, Einheitspatent, Übersicht)
            body_lines = [re.sub(r"\s+", " ", x.replace("\xa0", " ")).strip() for x in abschnitte_txt]
            body_lines = [x for x in body_lines if x][3:]
            info.append(dict(id=sec, titel=body_lines[0] if body_lines else sec, titel_en=(re.sub(r"\s+", " ", (en.get("text", "").split("\n") + ["", "", "", ""])[3]).strip() if en else ""),
                             url=row["url"], url_en=en.get("url", ""), text=" ".join(body_lines[1:])))
    meta = dict(titel="Richtlinien für das Einheitspatent (UP-Richtlinien), Ausgabe April 2026, und EPA-Informationsseiten zum Einheitspatent",
                quelle="https://www.epo.org/de/legal/guidelines-up", quelle_info="https://www.epo.org/de/applying/european/unitary/unitary-patent",
                quelle_db="RheinIP-Datenbank, Tabelle UPLegaltext (instrument up-gl, up-info; Spiegel von epo.org, Stand %s)" % stand,
                stand="Ausgabe April 2026 (in Kraft seit 1.4.2026, ABl. EPA 2026, A6); Informationsseiten Stand Juni 2026", hinweis="Nur deutscher Text; englische Titel und URLs je Abschnitt.")
    return dict(meta=meta, abschnitte=abschnitte, info=info)


# ---------------------------------------------------------------- Verfahrensordnung (PDF -> pdftotext)
_FOOT = re.compile(r"^\s*\d+\s*\|\s*(S e i t e|P a g e)\s*$")


def _pdf_lines(pdf):
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True).stdout.decode("utf-8")
    return [ln.replace("\f", "").rstrip() for ln in txt.split("\n") if not _FOOT.match(ln.replace("\f", ""))]


def parse_rop(lines, lang):
    rule_re = re.compile(r"^(Regel|Rule)\s+(\d+\s?[A-C]?)\s+[–-]\s+(.+)$" if True else "")
    bezug_re = re.compile(r"^(Bezug zum Übereinkommen|Relation with Agreement)\s*:\s*(.+)$")
    head_re = re.compile(r"^(TEIL|PART|KAPITEL|CHAPTER|ABSCHNITT|SECTION)\b.*$")
    # Hauptteil beginnt nach dem Inhaltsverzeichnis mit der Präambel
    starts = [i for i, ln in enumerate(lines) if re.match(r"^\s*(PRÄAMBEL|PREAMBLE)\s*$", ln)]
    start = starts[-1] if starts else 0
    rules, cur = [], None
    praeambel = []
    teil = kapitel = abschnitt = ""
    pending = None  # Überschrift, die auf der nächsten Zeile weitergehen kann (Zeilenumbruch im PDF)
    head_at = -9
    para_re = re.compile(r"^(\d{1,2})\.\s+(.*)$")
    for i, raw in enumerate(lines[start:]):
        ln = raw.strip()
        if not ln:
            if cur is not None:
                cur["_blank"] = True
            continue
        m = rule_re.match(ln)
        caps = ln.upper() == ln and len(ln) > 3 and not para_re.match(ln) and re.search(r"[A-ZÄÖÜ]{3}", ln)
        if caps and not m and not head_re.match(ln):
            # Versalzeile ohne TEIL/KAPITEL/ABSCHNITT: Fortsetzung einer umgebrochenen Überschrift (direkt folgende Zeile)
            # oder eigene Zwischenüberschrift (nach Leerzeile)
            unvollstaendig = pending and i == head_at + 1
            if unvollstaendig:
                head_at = i
                if pending in ("TEIL", "PART"):
                    teil += " " + ln
                elif pending in ("KAPITEL", "CHAPTER"):
                    kapitel += " " + ln
                else:
                    abschnitt += " " + ln
            else:
                abschnitt = ln
                pending = "ABSCHNITT"
                head_at = i
            continue
        pending = None
        if cur is None and not m and not head_re.match(ln) and not re.match(r"^\s*(PRÄAMBEL|PREAMBLE)\s*$", ln):
            p = para_re.match(ln)
            if p:
                praeambel.append(dict(nr=int(p.group(1)), text=p.group(2)))
            elif praeambel:
                praeambel[-1]["text"] += " " + ln
            continue
        if m:
            cur = dict(nr=m.group(2).replace(" ", ""), titel=m.group(3).strip(), teil=teil, kapitel=kapitel, abschnitt=abschnitt,
                       absaetze=[], bezug=[], _title_open=True, _blank=False)
            rules.append(cur)
            continue
        h = head_re.match(ln)
        if h and ln.upper() == ln and len(ln) > 6:
            key = h.group(1)
            if key in ("TEIL", "PART"):
                teil, kapitel, abschnitt = ln, "", ""
            elif key in ("KAPITEL", "CHAPTER"):
                kapitel, abschnitt = ln, ""
            else:
                abschnitt = ln
            pending = key
            head_at = i
            continue
        if cur is None:
            continue
        b = bezug_re.match(ln)
        if b:
            cur["bezug"] = sorted({int(x) for x in re.findall(r"(\d+)", re.sub(r"\(\d+\)", "", b.group(2)))})
            continue
        if cur["_title_open"] and not cur["_blank"] and not para_re.match(ln):
            cur["titel"] += " " + ln           # umgebrochener Regeltitel
            continue
        cur["_title_open"] = False
        p = para_re.match(ln)
        if p and (not cur["absaetze"] or int(p.group(1)) == len(cur["absaetze"]) + 1):
            cur["absaetze"].append(ln)
        elif cur["absaetze"]:
            cur["absaetze"][-1] += " " + ln
        else:
            cur["absaetze"].append(ln)
    for r in rules:
        r.pop("_title_open"); r.pop("_blank")
        r["absaetze"] = [re.sub(r"\s{2,}", " ", a) for a in r["absaetze"]]
    for p in praeambel:
        p["text"] = re.sub(r"\s{2,}", " ", p["text"])
    return rules, praeambel


def build_rop(net):
    de, praeambel = parse_rop(_pdf_lines(Path(fetch(ROP_PDF["de"], CACHE / "rop_de.pdf", net) and CACHE / "rop_de.pdf")), "de")
    en, _ = parse_rop(_pdf_lines(Path(fetch(ROP_PDF["en"], CACHE / "rop_en.pdf", net) and CACHE / "rop_en.pdf")), "en")
    en_by = {r["nr"].upper(): r for r in en}
    for r in de:
        r["nr"] = r["nr"].upper()
        e = en_by.get(r["nr"])
        r["titel_en"] = e["titel"] if e else ""
        r["url"] = ROP_PDF["de"]
    head = subprocess.run(["pdftotext", "-l", "1", str(CACHE / "rop_de.pdf"), "-"], check=True, capture_output=True).stdout.decode()
    stand = " ".join(re.sub(r"\s+", " ", head).split())[:400]
    meta = dict(titel="Verfahrensordnung des Einheitlichen Patentgerichts (VerfO, RoP)", kurz="RoP", quelle=ROP_PDF["de"], quelle_en=ROP_PDF["en"],
                stand=stand, hinweis="Deutscher Wortlaut der konsolidierten Fassung (unifiedpatentcourt.org); englische Regeltitel aus der Fassung vom 25.07.2022.")
    return dict(meta=meta, praeambel=praeambel, regeln=de)


# ---------------------------------------------------------------- Entscheidungen (Postgres, RheinIP)
_LABEL = r"(?:HEADNOTES?|LEITSATZ|LEITSÄTZE|LEITSAETZE|ORIENTIERUNGSS[ÄA]TZE?|KERNAUSSAGEN|SOMMAIRE|MASSIME|KERNPUNTEN)"
_KEYL = r"(?:KEYWORDS?|KEY WORDS|SCHLAGWORTE|SCHLAGWÖRTER|STICHWORTE|STICHWÖRTER|MOTS[- ]CL[ÉE]S|PAROLE CHIAVE|TREFWOORDEN)"
_STOP = r"\n\s*(?:[A-ZÄÖÜ][A-ZÄÖÜ0-9 /()\-–,.]{5,}:|CLAIMANT|KLÄGER|APPLICANT|ANTRAGSTELLER|BERUFUNGS|APPELLANT|PARTIES|PARTEIEN|DEMANDEUR|RICORRENTE|EISER|PATENT|STREITPATENT|LANGUAGE|VERFAHRENSSPRACHE|DECIDING|PANEL|SPRUCHKÖRPER)"
HEAD = re.compile(_LABEL + r"\s*:?\s*\n(.*?)(?=\n\s*" + _KEYL + "|" + _STOP + r"|\Z)", re.S)
KEYS = re.compile(_KEYL + r"\s*:?\s*\n(.*?)(?=" + _STOP + r"|\n\s*\n\s*\n)", re.S)
ART = re.compile(r"\bArt(?:icle|ikel|icolo|\.)?\s*(\d{1,2})\s*(?:\(\d\))?\s*(?:UPCA|EPGÜ|AJUB|of the (?:UPC )?Agreement|des (?:EPG-)?Übereinkommens)", re.I)
RULE = re.compile(r"\bR(?:ule|egel|ègle|egola|\.)?\s*(\d{1,3}\s?[A-Ca-c]?)(?:\.\d+)?(?:\s*\(\w\))?\s*(?:RoP|VerfO|RdP|RP|ROP|of the Rules of Procedure|der Verfahrensordnung)", re.I)


def _clean(s):
    s = re.sub(r"[ \t]*\n[ \t]*", " ", s.strip())
    return re.sub(r"\s{2,}", " ", s)


def _db_cursor():
    from dotenv import load_dotenv
    import psycopg2
    load_dotenv(Path.home() / "github" / "RheinIP" / ".env")
    conn = psycopg2.connect(os.environ["POSTGRES_LOGIN"], connect_timeout=30)
    conn.set_session(readonly=True)
    return conn.cursor()


def build_decisions():
    cur = _db_cursor()
    cur.execute('select docket, "decisionType", "decisionDate", division, language, claimant, respondent, patent, url, "decisionText" '
                'from "UpcDecision" order by "decisionDate", docket')
    out = []
    for docket, typ, date, div, lang, cl, resp, pat, url, txt in cur.fetchall():
        txt = txt or ""
        head = HEAD.search(txt[:25000])
        keys = KEYS.search(txt[:25000])
        arts = collections.Counter(int(a) for a in ART.findall(txt) if 1 <= int(a) <= 89)
        rules = collections.Counter(x.replace(" ", "").upper() for x in RULE.findall(txt))
        out.append(dict(docket=docket, typ=typ or "", date=date.date().isoformat() if date else None, division=div or "", lang=lang or "",
                        claimant=(cl or "")[:200], respondent=(resp or "")[:200], patent=pat or "", url=url,
                        headnote=_clean(head.group(1))[:3000] if head else "", keywords=_clean(keys.group(1))[:600] if keys else "",
                        upca=dict(arts.most_common()), rop=dict(rules.most_common()), chars=len(txt)))
    meta = dict(quelle="RheinIP-Datenbank, Tabelle UpcDecision (Scrape von unifiedpatentcourt.org)", anzahl=len(out),
                mit_leitsatz=sum(1 for o in out if o["headnote"]), zeitraum=[out[0]["date"], out[-1]["date"]] if out else None,
                hinweis="Leitsätze und Schlagworte stammen aus den Entscheidungen selbst (Abschnitte LEITSATZ/HEADNOTES, SCHLAGWORTE/KEYWORDS); "
                        "Zitate sind Zählungen im Volltext.")
    return dict(meta=meta, entscheidungen=out)


def main():
    net = "--no-net" not in sys.argv
    if "--no-db" not in sys.argv:
        d = build_decisions()
        (DATA / "upc_decisions.json").write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")
        print("upc_decisions.json:", d["meta"])
    u = build_upca(net)
    (DATA / "upca.json").write_text(json.dumps(u, ensure_ascii=False, indent=1), encoding="utf-8")
    print("upca.json: %d Artikel" % len(u["artikel"]))
    r = build_rop(net)
    (DATA / "upc_rop.json").write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    print("upc_rop.json: %d Regeln; Stand: %s" % (len(r["regeln"]), r["meta"]["stand"][:120]))
    db = None if "--no-db" in sys.argv else up_db_rows()
    for t in UP_TEXTE:
        d = build_up_text(t, net, db)
        (DATA / t["datei"]).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print("%s: %d %s (%s)" % (t["datei"], len(d["artikel"]), "Regeln" if t["kopf"][0] == "Regel" else "Artikel", d["meta"]["quelle_db"][:60]))
    if db:
        g = build_up_richtlinien(db)
        (DATA / "up_richtlinien.json").write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8")
        print("up_richtlinien.json: %d Abschnitte, %d Informationsseiten" % (len(g["abschnitte"]), len(g["info"])))
    else:
        print("up_richtlinien.json unverändert (--no-db)")


if __name__ == "__main__":
    main()
