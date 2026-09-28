#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quellen für das Wissenspaket Patentrecht beschaffen (Netz + Postgres) und als JSON unter data/ ablegen.

Erzeugt (alle mitversioniert, damit `build.py` ohne Netz und ohne Datenbank läuft):
  data/patg.json               Patentgesetz (PatG), alle Paragraphen mit Abschnittsgliederung, Absätzen und Volltext
  data/patv.json               Patentverordnung (PatV) einschließlich Anlagen
  data/intpatueg.json          Gesetz über internationale Patentübereinkommen (IntPatÜG, amtlich IntPatÜbkG): Art. I bis XI,
                               die Paragraphen der Art. II (EPÜ), III (PCT) und XI (Übergang) mit Artikelpräfix („II § 6“)
  data/patkostg.json           Patentkostengesetz (PatKostG) mit dem Gebührenverzeichnis (Anlage zu § 2 Abs. 1) als Tabellenzeilen
  data/patent_decisions.json   Entscheidungen des BPatG (Nichtigkeitssenate, Technische und Juristische Beschwerdesenate,
                               Gebrauchsmuster-Beschwerdesenat) und des BGH (X. und Xa. Zivilsenat sowie andere Senate, soweit sie
                               Patentgesetze zitieren) aus der RheinIP-Datenbank: Metadaten, Entscheidungsname, Leitsatz,
                               zitierte Normen (PatG, PatV, IntPatÜG, PatKostG, GebrMG, ArbnErfG, EPÜ) mit Auslegungsmarkierung.
                               Volltexte werden nicht versioniert.

Quelle der Gesetzestexte: gesetze-im-internet.de, XML-Fassung (`<slug>/xml.zip`). Die Datenbank enthält PatG, PatKostG und IntPatÜG
zwar ebenfalls (Tabelle DeLegalProvision), aber ohne Abschnittsgliederung und ohne Absatztrennung und die PatV gar nicht; deshalb
kommt der Normtext aus dem XML, die Datenbank liefert die Rechtsprechung.

Aufruf:  python3 tools/fetch_patent.py [--no-net] [--no-db]
Zwischenstände (XML-Zips) liegen in ~/.cache/ipelico/patent/. Postgres-Zugang: POSTGRES_LOGIN aus ~/github/RheinIP/.env.
"""
import collections
import html as htmlmod
import io
import json
import os
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path.home() / ".cache" / "ipelico" / "patent"
UA = {"User-Agent": "Mozilla/5.0 (IPelico fetch_patent)"}
BASE = "https://www.gesetze-im-internet.de/"

GESETZE = [
    dict(key="patg", slug="patg", kurz="PatG", datei="patg.json"),
    dict(key="patv", slug="patv", kurz="PatV", datei="patv.json"),
    dict(key="intpatueg", slug="intpat_bkg", kurz="IntPatÜG", datei="intpatueg.json"),
    dict(key="patkostg", slug="patkostg", kurz="PatKostG", datei="patkostg.json"),
]


def fetch_zip(slug, net):
    target = CACHE / (slug + ".zip")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 1000:
        return target.read_bytes()
    if not net:
        raise SystemExit("fehlt im Cache und --no-net gesetzt: %s" % slug)
    data = urllib.request.urlopen(urllib.request.Request(BASE + slug + "/xml.zip", headers=UA), timeout=60).read()
    target.write_bytes(data)
    return data


# ---------------------------------------------------------------- XML -> Text
_TAG = re.compile(r"<[^>]+>")


def _inner(tag, s, flags=re.S):
    m = re.search(r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), s, flags)
    return m.group(1) if m else ""


def _clean(s):
    s = htmlmod.unescape(_TAG.sub("", s)).replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", s).strip()


def _dl(s):
    """<DL><DT>1.</DT><DD><LA>Text</LA></DD>…</DL> -> Zeilen „1. Text“ (verschachtelt einrücken).
    DD-Inhalte werden mit Tiefenzählung abgegrenzt, damit verschachtelte Listen („5. … a) … b) …“) erhalten bleiben."""
    out, pos = [], 0
    while True:
        m = re.compile(r"<DT>(.*?)</DT>\s*<DD[^>]*>", re.S).search(s, pos)
        if not m:
            break
        depth, i = 1, m.end()
        for t in re.compile(r"<(/?)DD\b[^>]*>").finditer(s, m.end()):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                i = t.start()
                pos = t.end()
                break
        else:
            pos = len(s)
            i = len(s)
        out.append(_clean(m.group(1)) + " " + _content(s[m.end():i]).replace("\n", "\n   "))
    return "\n".join(out)


def _table(s):
    rows = []
    for row in re.findall(r"<row\b[^>]*>(.*?)</row>", s, re.S):
        cells = [_content(c).replace("\n", " ") for c in re.findall(r"<entry\b[^>]*>(.*?)</entry>", row, re.S)]
        cells = [c for c in cells if c]
        if cells:
            rows.append(" | ".join(cells))
    return "\n".join(rows)


def _content(s):
    """Inhalt eines P/DD/entry-Elements: Listen und Tabellen werden zu Zeilen, Rest zu Fließtext."""
    s = re.sub(r"<noindex>.*?</noindex>", "", s, flags=re.S)
    s = re.sub(r"<FnR\b[^>]*/>|<FnR\b.*?</FnR>", "", s, flags=re.S)
    parts, pos = [], 0
    while True:
        m = re.compile(r"<(DL|table)\b[^>]*>").search(s, pos)
        if not m:
            break
        depth, end = 1, len(s)   # verschachtelte Listen: bis zum passenden schließenden Tag
        for t in re.compile(r"<(/?)%s\b[^>]*>" % m.group(1)).finditer(s, m.end()):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                end = t.end()
                break
        parts.append(_clean(s[pos:m.start()]))
        parts.append(_dl(s[m.start():end]) if m.group(1) == "DL" else _table(s[m.start():end]))
        pos = end
    parts.append(_clean(s[pos:]))
    return "\n".join(p for p in parts if p).strip()


_ABS = re.compile(r"^\((\d+[a-z]?)\)\s*")


def parse_norm(body):
    content = _inner("Content", _inner("textdaten", body))
    paras = re.findall(r"<P\b[^>]*>(.*?)</P>", content, re.S) or ([content] if content.strip() else [])
    absaetze, cur = [], None
    for p in paras:
        t = _content(p)
        if not t:
            continue
        m = _ABS.match(t)
        if m:
            if cur:
                absaetze.append(cur)
            cur = dict(nr=m.group(1), text=t[m.end():])
        elif cur:
            cur["text"] += "\n" + t
        else:
            cur = dict(nr=None, text=t)
    if cur:
        absaetze.append(cur)
    return absaetze


ROMAN = re.compile(r"^Art ([IVX]+)(?: (?:bis|u\.) ([IVX]+))?$")


def parse_gesetz(g, net):
    raw = fetch_zip(g["slug"], net)
    zf = zipfile.ZipFile(io.BytesIO(raw))
    name = [n for n in zf.namelist() if n.endswith(".xml")][0]
    xml = zf.read(name).decode("utf-8")
    head = xml[:8000]
    meta = dict(
        jurabk=_clean(_inner("jurabk", head)), gesetz=_clean(_inner("langue", head)),
        ausfertigung=_clean(_inner("ausfertigung-datum", head)),
        stand=[_clean(s) for s in re.findall(r"<standkommentar>(.*?)</standkommentar>", head)],
        builddate=re.search(r'builddate="(\d+)"', head).group(1),
        quelle=BASE + g["slug"] + "/", quelle_xml=BASE + g["slug"] + "/xml.zip",
    )
    dok = re.search(r'doknr="(BJNR\d+)"', head).group(1)
    abschnitte = {}   # Kennzahl -> Titel
    paragraphen = []
    cur_teil = cur_abschnitt = None  # PatG, PatV: Paragraphen tragen keine Gliederungseinheit, sie folgen der letzten Überschrift
    for attrs, body in re.findall(r"<norm (.*?)>(.*?)</norm>", xml, re.S):
        doknr = re.search(r'doknr="(\w+)"', attrs).group(1)
        enbez = _clean(_inner("enbez", body))
        kz = _clean(_inner("gliederungskennzahl", body))
        gbez = _clean(_inner("gliederungsbez", body))
        gtit = _clean(_inner("gliederungstitel", body))
        titel = _clean(_inner("titel", body).replace("<BR/>", " "))
        if kz and gbez and gbez != "-":
            abschnitte.setdefault(kz, (gbez + (" " + gtit if gtit else "")).strip())
            if not enbez:
                if len(kz) > 3:
                    cur_abschnitt = abschnitte[kz]
                else:
                    cur_teil, cur_abschnitt = abschnitte[kz], None
        if enbez in ("Eingangsformel", "Inhaltsübersicht") or (not enbez and g["key"] != "intpatueg"):
            continue
        # Gliederung: Abschnitt (3-stellige Kennzahl) und Unterabschnitt (6-stellig)
        teil, abschnitt = cur_teil, cur_abschnitt
        if kz and enbez:
            teil = abschnitte.get(kz[:3])
            abschnitt = abschnitte.get(kz) if len(kz) > 3 else None
        if g["key"] == "intpatueg":
            m = ROMAN.match(gbez or "")
            art = m.group(1) if m else None
            if not enbez:  # Art. I, VII, X: Artikel ohne Paragraphen (Text direkt am Gliederungsknoten)
                if not art or m.group(2) or not parse_norm(body):
                    continue
                nr, label, titel, url = art, "Art. " + art, gtit, BASE + g["slug"] + "/" + dok + ".html#" + doknr
                teil, abschnitt = "Art. " + art + (" – " + gtit if gtit else ""), None
            else:
                nr = art + " " + enbez
                label = "Art. " + nr
                teil = "Art. " + art + (" – " + gtit if gtit else "")
                url = BASE + g["slug"] + "/art_%s__%s.html" % (art.lower(), enbez.replace("§ ", ""))
        elif enbez.startswith("§"):
            nr = enbez.replace("§ ", "")
            label, url = enbez, BASE + g["slug"] + "/__%s.html" % nr
        elif enbez.startswith("Anlage"):
            nr = enbez.lower().replace(" ", "_")
            label, url = enbez, BASE + g["slug"] + "/%s.html" % nr
        else:
            continue
        absaetze = parse_norm(body)
        if not absaetze and "(weggefallen)" not in titel:
            absaetze = [dict(nr=None, text=titel or "(weggefallen)")]
        paragraphen.append(dict(nr=nr, label=label, titel=titel, teil=teil, abschnitt=abschnitt,
                                absaetze=absaetze, text="\n".join((("(%s) " % a["nr"]) if a["nr"] else "") + a["text"] for a in absaetze),
                                url=url, doknr=doknr))
    return dict(gesetz=meta["gesetz"], kurz=g["kurz"], meta=meta, paragraphen=paragraphen)


# ---------------------------------------------------------------- Rechtsprechung (Postgres)
def _db_cursor():
    from dotenv import load_dotenv
    import psycopg2
    load_dotenv(Path.home() / "github" / "RheinIP" / ".env")
    conn = psycopg2.connect(os.environ["POSTGRES_LOGIN"], connect_timeout=30)
    conn.set_session(readonly=True)
    return conn.cursor()


LAW_KEYS = {"PatG": "patg", "PatV": "patv", "IntPatÜG": "intpatueg", "PatKostG": "patkostg", "GebrMG": "gebrmg", "ArbEG": "arbnerfg", "EPÜ": "epue"}
SENAT_KURZ = {
    "Nichtigkeitssenat": "Nichtigkeitssenat", "Technischer-Beschwerdesenat": "Technischer Beschwerdesenat",
    "Juristischer-Beschwerdesenat": "Juristischer Beschwerdesenat", "Juristischer Beschwerde- und Nichtigkeitssenat": "Juristischer Beschwerde- und Nichtigkeitssenat",
    "Gebrauchsmuster-Beschwerdesenat": "Gebrauchsmuster-Beschwerdesenat",
}
VERFAHREN = [  # (Muster im Aktenzeichen, Verfahrensart)
    (r"\bNi\b", "Nichtigkeitsklage"), (r"\bZR\b", "Revision/Berufung"), (r"\bZB\b", "Rechtsbeschwerde"), (r"\bLi\b", "Zwangslizenz"),
    (r"\bW \(pat\)", "Beschwerde"), (r"\bZA\b", "Sonstiges"),
]


def _ws(s):
    return re.sub(r"\s+", " ", (s or "").strip())


def _leitsatz(s):
    s = (s or "").strip()
    s = re.sub(r"^(Leitsatz|Leitsätze|Parallelentscheidung:[^\n]*)\s*:?\s*\n", "", s, flags=re.I)
    s = re.sub(r"[ \t]*\n[ \t]*", " ", s)
    return re.sub(r"\s{2,}", " ", s)[:1500]


def _name(s):
    s = _ws(s)
    s = re.sub(r"^(Name Entscheidung|Entscheidung|Bezeichnung)\s*:?\s*", "", s, flags=re.I)
    return s.strip(" „“\"'")[:120]


def _verfahren(az, typ, gericht):
    for pat, v in VERFAHREN:
        if re.search(pat, az or ""):
            if v == "Beschwerde" and gericht == "BPatG":
                return "Einspruchsbeschwerde" if "Einspruch" in (typ or "") else "Beschwerde"
            return v
    return "Sonstiges"


def build_decisions():
    cur = _db_cursor()
    # Normzitate je Entscheidung (Tabelle DeCourtNorm: Gesetz, Paragraph, Absatz, Auslegung)
    cur.execute('select "decisionId", law, paragraph, bool_or(interpreted), sum(mentions) from "DeCourtNorm" '
                'where law = any(%s) group by 1, 2, 3', (list(LAW_KEYS),))
    zit = collections.defaultdict(lambda: collections.defaultdict(dict))
    for did, law, par, interp, ment in cur.fetchall():
        if not par:
            continue
        p = ("II " + par if not par.startswith("I") else par) if law == "IntPatÜG" else par
        zit[did][LAW_KEYS[law]][p] = dict(i=bool(interp), m=int(ment or 0))
    out = []
    cur.execute('select id, url, "fileNumber", ecli, senate, "senateType", topic, category, "decisionType", "caseType", "caseName", norms, '
                '"decisionDate", headnote from "BpatgDecision" where category in (\'patent\', \'utility_model\') order by "decisionDate", "fileNumber"')
    for row in cur.fetchall():
        did, url, az, ecli, senat, styp, topic, cat, dtyp, ctyp, name, norms, date, head = row
        out.append(dict(id=did, gericht="BPatG", az=_ws(az), ecli=ecli or "", senat=_ws(senat), senat_typ=SENAT_KURZ.get(styp or "", styp or "–"),
                        typ=dtyp or "", verfahren=_verfahren(az, ctyp, "BPatG"), sache=_ws(ctyp)[:160], name=_name(name), gebiet=cat,
                        datum=date.date().isoformat() if date else None, leitsatz=_leitsatz(head), normen_text=_ws("; ".join(norms or []))[:300],
                        url=url, zitate=zit.get(did, {})))
    cur.execute('select d.id, d.url, d."fileNumber", d.ecli, d.senate, d.category, d."decisionType", d."caseType", d."caseName", d.norms, d."decisionDate", d.headnote '
                'from "BghDecision" d where d.senate in (\'X. Zivilsenat\', \'Xa. Zivilsenat\') or d.category in (\'patent\', \'utility_model\') '
                'or exists (select 1 from "DeCourtNorm" n where n."decisionId" = d.id and n.law = any(%s)) order by d."decisionDate", d."fileNumber"',
                (["PatG", "PatV", "IntPatÜG", "PatKostG", "GebrMG", "ArbEG"],))
    for row in cur.fetchall():
        did, url, az, ecli, senat, cat, dtyp, ctyp, name, norms, date, head = row
        patentnah = cat in ("patent", "utility_model") or any(k in zit.get(did, {}) for k in ("patg", "patv", "intpatueg", "patkostg", "gebrmg", "arbnerfg"))
        if not patentnah:
            continue  # X. ZS entscheidet auch Reise-, Werkvertrags- und Vergaberecht; das bleibt draußen
        out.append(dict(id=did, gericht="BGH", az=_ws(az), ecli=ecli or "", senat=_ws(senat), senat_typ=_ws(senat),
                        typ=dtyp or "", verfahren=_verfahren(az, ctyp, "BGH"), sache=_ws(ctyp)[:160], name=_name(name), gebiet=cat,
                        datum=date.date().isoformat() if date else None, leitsatz=_leitsatz(head), normen_text=_ws("; ".join(norms or []))[:300],
                        url=url, zitate=zit.get(did, {})))
    out.sort(key=lambda e: (e["datum"] or "", e["az"]))
    stat = collections.Counter(e["gericht"] for e in out)
    daten = sorted(e["datum"] for e in out if e["datum"])
    meta = dict(quelle="RheinIP-Datenbank, Tabellen BpatgDecision und BghDecision (Scrape der Entscheidungsdatenbanken von bundespatentgericht.de und bundesgerichtshof.de), Normzitate aus DeCourtNorm",
                anzahl=len(out), bpatg=stat["BPatG"], bgh=stat["BGH"], mit_leitsatz=sum(1 for e in out if e["leitsatz"]),
                zeitraum=[daten[0], daten[-1]] if daten else None,
                hinweis="Leitsätze und Entscheidungsnamen stammen aus den veröffentlichten Entscheidungen (nur ein Teil trägt einen Leitsatz). "
                        "Normzitate sind maschinell aus dem Volltext erkannt (Kennzeichen i = die Entscheidung legt die Norm aus, nicht nur Erwähnung); "
                        "Paragraphen des IntPatÜG werden ohne Artikelangabe erfasst und Art. II zugeordnet (Art. III wird selten zitiert).")
    return dict(meta=meta, entscheidungen=out)


def main():
    net = "--no-net" not in sys.argv
    for g in GESETZE:
        d = parse_gesetz(g, net)
        (DATA / g["datei"]).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print("%s: %d Vorschriften; %s" % (g["datei"], len(d["paragraphen"]), "; ".join(d["meta"]["stand"])[:100]))
    if "--no-db" not in sys.argv:
        d = build_decisions()
        (DATA / "patent_decisions.json").write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")
        print("patent_decisions.json:", {k: v for k, v in d["meta"].items() if k != "hinweis"})
    else:
        print("patent_decisions.json unverändert (--no-db)")


if __name__ == "__main__":
    main()
