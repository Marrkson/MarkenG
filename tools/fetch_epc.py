#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quellen für das Wissenspaket EPÜ (Europäisches Patentübereinkommen) beschaffen und unter data/ ablegen.

Erzeugt (alle mitversioniert, damit `build.py` weder Netz noch Datenbank braucht):
  data/epc.json            EPÜ: Artikel und Regeln der Ausführungsordnung, deutsch und englisch, mit Teil/Kapitel und den
                           Fußnoten (Hinweise auf Entscheidungen der Großen Beschwerdekammer und Fundstellen im Amtsblatt).
                           Englisch: RheinIP-Datenbank, Tabelle EPOLegaltext (type epc, Spiegel von epo.org/en/legal/epc/2020).
                           Deutsch: fehlt in der Datenbank, deshalb epo.org/de/legal/epc/2020/<a54|r71>.html (Cache
                           ~/.cache/ipelico/epc/de/); die Gliederung (Teile, Kapitel, Titel) kommt aus dem Menü dieser Seiten.
  data/epc_decisions.json  Entscheidungen der Beschwerdekammern (Tabelle BoaDecision): alle G-, J- und R-Sachen sowie die T-Sachen
                           der Verteilerschlüssel A, B und C, ohne Volltext; Zählung der zitierten Artikel und Regeln über alle
                           Entscheidungen (auch Verteiler D) für den Zitierzähler je Vorschrift.
  data/epc_guidelines.json Richtlinien für die Prüfung im EPA (Ausgabe 2026) abschnittsweise: Titel, Randverweise (Rechtsgrundlagen am
                           Rand), im Text zitierte Artikel/Regeln/Entscheidungen, Textanfang (EPOLegaltext, type gl).
  data/epc_oj.json         Amtsblatt des EPA seit 2008 (EPÜ 2000): Beschlüsse des Präsidenten und des Verwaltungsrats, Mitteilungen
                           des EPA, Entscheidungen der Kammern, mit den zitierten Artikeln und Regeln (EPOLegaltext, type oj).
  data/eqe_d1.json         Prüfungsfragen der EQE Paper D, Teil 1 (2015 bis 2025) mit Thema, Punkten und den Rechtsgrundlagen
                           der Musterlösungen (aus ~/github/EQEAnalysis/paper_D/output/D1_all_questions.json; ohne Fragetext).

Aufruf:  python3 tools/fetch_epc.py [--no-net] [--no-db] [--nur texte,boa,gl,oj,eqe]
Postgres-Zugang: POSTGRES_LOGIN aus ~/github/RheinIP/.env, nur lesend.
"""
import collections
import concurrent.futures
import html as htmlmod
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path.home() / ".cache" / "ipelico" / "epc"
UA = {"User-Agent": "Mozilla/5.0 (IPelico fetch_epc)"}
EPC_URL = "https://www.epo.org/%s/legal/epc/2020/%s.html"
EQE_D1 = Path.home() / "github" / "EQEAnalysis" / "paper_D" / "output" / "D1_all_questions.json"


def fetch(url, target, net=True):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 1000:
        return target.read_text(encoding="utf-8")
    if not net:
        raise SystemExit("fehlt im Cache und --no-net gesetzt: %s" % url)
    data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
    target.write_bytes(data)
    return data.decode("utf-8")


def _db_cursor():
    import psycopg2
    if "POSTGRES_LOGIN" not in os.environ:
        for ln in (Path.home() / "github" / "RheinIP" / ".env").read_text().splitlines():
            if ln.startswith("POSTGRES_LOGIN="):
                os.environ["POSTGRES_LOGIN"] = ln.split("=", 1)[1].strip().strip('"')
    conn = psycopg2.connect(os.environ["POSTGRES_LOGIN"], connect_timeout=30)
    conn.set_session(readonly=True)
    return conn.cursor()


def _ws(s):
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:)\]])", r"\1", s)
    return re.sub(r"([(\[])\s+", r"\1", s)


# ---------------------------------------------------------------- EPÜ: Gliederung aus dem Menü der deutschen Seiten
_MENU = re.compile(r"var oMenu = (\[.*?\]);\s*</script>", re.S)
_SLUG = re.compile(r"/legal/epc/2020/([ar]\d+[a-z]?)\.html$")


def gliederung(html):
    """{slug: dict(titel, teil, kapitel)} aus dem Menü (Artikel: Teil/Kapitel; Regeln: Teil/Kapitel der Ausführungsordnung)."""
    menu = json.loads(_MENU.search(html).group(1))
    out = {}

    def walk(items, teil, kapitel, depth):
        for it in items:
            name, url = it[0], it[1]
            kids = it[3] if len(it) > 3 else []
            m = _SLUG.search(url)
            if m:
                titel = re.sub(r"^(?:Artikel|Regel|Article|Rule)\s\d+[a-z]?\s–\s", "", name.replace("\xa0", " "))
                out[m.group(1)] = dict(titel=titel, teil=teil, kapitel=kapitel)
            if re.match(r"^[A-ZÄÖÜ][a-zäöü]+ter Teil|^Erster Teil|^Dritter Teil|^Achter Teil|^Part [IVX]+\b", name):
                walk(kids, name, "", depth + 1)
            elif name.startswith(("Kapitel", "Chapter")):
                walk(kids, teil, name, depth + 1)
            else:
                walk(kids, teil, kapitel, depth + 1)
    walk(menu, "", "", 0)
    return out


# ---------------------------------------------------------------- EPÜ: deutscher Wortlaut (HTML)
_P = re.compile(r"<p\b([^>]*)>(.*?)</p>", re.S)
_NR = re.compile(r"^\((\d+[a-z]?)\)\s*")
_SUB = re.compile(r"^(?:\(([a-z]|[ivx]+)\)|([a-z])\))\s")


def _strip(fragment):
    f = re.sub(r'<span class="hidden">.*?</span>', "", fragment, flags=re.S)
    f = re.sub(r'<span class="(?:Del|Deleted|Old|deleted)\b[^"]*"[^>]*>.*?</span>', "", f, flags=re.S)
    # Fußnotenverweise samt Kommas zwischen aufeinanderfolgenden Verweisen („d)<sup>207</sup>, <sup>208</sup>“) entfernen
    f = re.sub(r'<a [^>]*class="FootnoteRef"[^>]*>.*?</a>', "\x00", f, flags=re.S)
    f = re.sub(r"\x00(?:\s|<[^>]+>|,)*(?=\x00)", "", f).replace("\x00", "")
    f = re.sub(r"<sup>.*?</sup>", "", f, flags=re.S)
    f = re.sub(r"<br\s*/?>", " ", f)
    return _ws(htmlmod.unescape(re.sub(r"<[^>]+>", "", f)).replace("\xa0", " "))


def parse_de(html):
    """Absätze [{nr, text}] und Fußnoten [{nr, text}] einer Artikel- oder Regelseite."""
    i = html.find('class="epolegal-content"')
    if i < 0:
        raise ValueError("kein epolegal-content")
    j = html.find("DOC4NET2-noteseparator", i)
    k = html.find("</div>\n</div>", i)
    body = html[i:j if j > 0 else (k if k > 0 else len(html))]
    absaetze = []
    for attrs, inner in _P.findall(body):
        if "Deleted" in attrs:
            continue
        t = _strip(inner)
        if not t:
            continue
        m = _NR.match(t)
        if m:
            absaetze.append(dict(nr=m.group(1), text=t[m.end():]))
        elif absaetze and (_SUB.match(t) or t.startswith(("– ", "- ", "und", "oder", "and", "or")) or "prefixed" not in attrs):
            absaetze[-1]["text"] += "\n" + t
        else:
            absaetze.append(dict(nr=None, text=t))
    fn = []
    if j > 0:
        for attrs, inner in _P.findall(html[j:j + 200000]):
            if "FootnoteText" not in attrs:
                break
            m = re.search(r"<sup>(\d+)</sup>", inner)
            fn.append(dict(nr=int(m.group(1)) if m else None, text=_strip(inner)))
    return absaetze, fn


# ---------------------------------------------------------------- EPÜ: englischer Wortlaut (Datenbank, zeilenweise)
_LINK_PREV = re.compile(r"(?:paragraphs?|Articles?|Rules?|items?|sub-paragraphs?|and|or|to|,)$", re.I)


def parse_en(text, slug, fussnoten):
    """DB-Text einer Seite (Zeilen wie auf epo.org) -> (titel, kapitel, absätze). Fußnotennummern (aus der deutschen Seite bekannt)
    werden aus dem Fließtext entfernt, der Fußnotenblock am Ende abgeschnitten."""
    lines = [x.replace("\xa0", " ").strip() for x in text.split("\n")]
    kapitel = lines[0] if lines else ""
    head = ("Article " if slug[0] == "a" else "Rule ") + slug[1:]
    try:
        h = lines.index(head)
    except ValueError:
        return "", kapitel, []
    rest = [x for x in lines[h + 1:] if x != ""]
    fnr = {str(f["nr"]) for f in fussnoten if f.get("nr")}
    # Fußnotenblock: ab der ersten Fußnotennummer, auf die der Fußnotentext folgt, bis zum Ende (Rückwärtssuche)
    if fussnoten:
        first = str(fussnoten[0]["nr"])
        for k in range(len(rest) - 1, -1, -1):
            if rest[k] == first and k + 1 < len(rest) and not re.fullmatch(r"\d+|,", rest[k + 1]):
                rest = rest[:k]
                break
    # Titel: nach Fußnotenverweisen im Kopf („42“, „,“, „43“)
    t = 0
    while t < len(rest) and (rest[t] in fnr or rest[t] == ","):
        t += 1
    titel = rest[t] if t < len(rest) else ""
    body = rest[t + 1:]
    clean = []
    for x in body:
        if x in fnr and not (clean and _LINK_PREV.search(clean[-1])):
            continue
        if x == "," and clean and clean[-1] in fnr:
            continue
        clean.append(x)
    absaetze, cur = [], None
    for x in clean:
        m = re.fullmatch(r"\((\d+[a-z]?)\)", x)
        if m:
            cur = dict(nr=m.group(1), parts=[])
            absaetze.append(cur)
            continue
        if cur is None:
            cur = dict(nr=None, parts=[])
            absaetze.append(cur)
        if re.fullmatch(r"\(([a-z]|[ivx]+)\)", x):
            cur["parts"].append("\n" + x)
        else:
            cur["parts"].append(x)
    out = []
    for a in absaetze:
        s = " ".join(a["parts"]).replace(" \n", "\n")
        s = "\n".join(_ws(p) for p in s.split("\n"))
        out.append(dict(nr=a["nr"], text=s.strip()))
    return titel, kapitel, [a for a in out if a["text"]]


_G = re.compile(r"\bG \d+/\d{2}\b")
_OJ = re.compile(r"(?:ABl\.|OJ) EPA? (\d{4}), (A?\d+)")


def build_texte(net, db):
    rows = {}
    if db:
        cur = _db_cursor()
        cur.execute("""select url, text from "EPOLegaltext" where type='epc' and url ~ '/epc/2020/[a-z]+[0-9]*[a-z]*\\.html$'""")
        for url, text in cur.fetchall():
            rows[url.rsplit("/", 1)[1][:-5]] = text
        (CACHE / "en_db.json").parent.mkdir(parents=True, exist_ok=True)
        (CACHE / "en_db.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
    else:
        rows = json.loads((CACHE / "en_db.json").read_text(encoding="utf-8"))
    slugs = sorted((s for s in rows if re.fullmatch(r"[ar]\d+[a-z]?", s)),
                   key=lambda s: (s[0], int(re.match(r"\d+", s[1:]).group(0)), s[1:]))
    def load(lang):
        with concurrent.futures.ThreadPoolExecutor(6) as ex:
            return dict(zip(slugs, ex.map(lambda s: fetch(EPC_URL % (lang, s), CACHE / lang / (s + ".html"), net), slugs)))
    pages, pages_en = load("de"), load("en")
    glied, glied_en = gliederung(pages["a1"]), gliederung(pages_en["a1"])
    artikel, regeln, warn = [], [], []
    for s in slugs:
        absaetze, fn = parse_de(pages[s])
        absaetze_en, fn_en = parse_de(pages_en[s])
        # Kontrolle gegen den Datenbanktext (dort sind Änderungsmarkierungen alt/neu zusammengezogen, deshalb nur Absatzzahl)
        _, _, db_en = parse_en(rows[s], s, fn)
        g, ge = glied.get(s, {}), glied_en.get(s, {})
        if not g or not ge:
            warn.append("%s: nicht im Menü" % s)
        for name, other in (("englisch (epo.org)", absaetze_en), ("englisch (Datenbank)", db_en)):
            if len([a for a in absaetze if a["nr"]]) != len([a for a in other if a["nr"]]):
                warn.append("%s: %d Absätze deutsch, %d %s" % (s, len(absaetze), len(other), name))
        rec = dict(nr=s[1:], titel=g.get("titel", ""), titel_en=ge.get("titel", ""), teil=g.get("teil", ""), teil_en=ge.get("teil", ""),
                   kapitel=g.get("kapitel", ""), kapitel_en=ge.get("kapitel", ""),
                   absaetze=absaetze, absaetze_en=absaetze_en, fussnoten=[f["text"] for f in fn], fussnoten_en=[f["text"] for f in fn_en],
                   grosse_kammer=sorted(set(_G.findall(" ".join(f["text"] for f in fn))), key=lambda x: (int(x.split("/")[1]) % 100 < 70, x)),
                   amtsblatt=sorted({"%s, %s" % m for m in _OJ.findall(" ".join(f["text"] for f in fn))}),
                   url=EPC_URL % ("de", s), url_en=EPC_URL % ("en", s))
        (artikel if s[0] == "a" else regeln).append(rec)
    meta = dict(titel="Europäisches Patentübereinkommen (EPÜ)", kurz="EPÜ", stand="17. Auflage (EPÜ 2000, Stand der fortlaufend aktualisierten Fassung auf epo.org)",
                quelle_en="epo.org/en/legal/epc/2020; die RheinIP-Datenbank (EPOLegaltext, type epc) enthält den englischen Text, zieht aber bei "
                          "geänderten Vorschriften alte und neue Fassung zusammen (Änderungsmarkierungen), deshalb nur Kontrolle der Absatzzahl",
                quelle_de="epo.org/de/legal/epc/2020 (nicht in der Datenbank)", warnungen=warn)
    return dict(meta=meta, artikel=artikel, regeln=regeln)


# ---------------------------------------------------------------- Zitate in Texten der Kammern, Richtlinien, Amtsblatt, EQE
_PROV = re.compile(r"(?:Art\.?|Article|Rule|R\.)\s*(\d+[a-z]?)(?:\([^)]*\))*")


def az_norm(s):
    """'T 0641/00' -> 'T 641/00'"""
    m = re.match(r"([A-Z])\s*0*(\d+)/(\d{2})", s.strip())
    return "%s %s/%s" % m.groups() if m else s.strip()


def boa_prov(x):
    """Eintrag aus BoaDecision.relevantLegalProv -> (familie, nummer) oder None. Familien: a, r (EPÜ 2000), rpba, rfees, pct_a, pct_r."""
    x = x.strip()
    if re.search(r"1973|EPC1973", x):
        return None
    m = re.match(r"EPC2000_(Art|R)_0*(\d+[a-z]?)", x) or re.match(r"RPBA_\d{4}_(Art)_0*(\d+)", x)
    if m:
        return ("rpba" if x.startswith("RPBA") else ("a" if m.group(1) == "Art" else "r"), m.group(2))
    m = re.match(r"(European Patent Convention|EPC|Rules of procedure of the Boards of Appeal(?: 20\d\d)?|Rules relating to fees|Patent Cooperation Treaty)\s+(Art|R)\.?\s*(\d+[a-z]?)", x)
    if not m:
        return None
    law, kind, nr = m.groups()
    if law.startswith("Rules of procedure"):
        return ("rpba", nr)
    if law.startswith("Rules relating"):
        return ("rfees", nr)
    if law.startswith("Patent"):
        return ("pct_" + ("a" if kind == "Art" else "r"), nr)
    return ("a" if kind == "Art" else "r", nr)


def _br(s):
    if isinstance(s, list):
        s = "<br />".join(x for x in s if x)
    return _ws(re.sub(r"<br\s*/?>", " · ", s or "")).strip(" ·")


def build_boa(gl_cited=()):
    cur = _db_cursor()
    cur.execute('''select "caseNumber", "decisionDate", distribution, board, "applicationTitle", headword, keywords, catchword, headnote, url,
                   "decisionType", language, "isTranslation", "relevantLegalProv", "applicantName", "opponentName" from "BoaDecision"''')
    orig, trans = {}, collections.defaultdict(list)
    for row in cur.fetchall():
        key = (az_norm(row[0]), row[1].date().isoformat() if row[1] else "")
        if row[12]:
            trans[key].append(row)
        else:
            orig.setdefault(key, row)
    zit = collections.Counter()
    out = []
    for key, r in orig.items():
        az, datum = key
        provs = sorted({p for p in (boa_prov(x) for x in (r[13] or [])) if p}, key=lambda p: (p[0], int(re.match(r"\d+", p[1]).group(0)), p[1]))
        for fam, nr in provs:
            zit["%s%s" % (fam, nr)] += 1
        keep = (r[2] in ("A", "B", "C")) or az[0] in "GJR" or az in gl_cited
        if not keep:
            continue
        de = next((t for t in trans.get(key, []) if re.search(r"d[pxu]\d$", t[9] or "")), None)
        rec = dict(az=az, datum=datum, kammer=r[3] or ("GBK" if az[0] == "G" else ""), verteiler=r[2] or "", titel=_ws(r[4] or "")[:160], stichwort=_ws(r[5] or ""),
                   schlagworte=_br(r[6])[:500], leitsatz=_br(r[7] or r[8])[:1500], url=r[9] or "",
                   typ=r[10] or "", sprache=r[11] or "", anmelder=_ws(r[14] or "")[:80],
                   a=[nr for f, nr in provs if f == "a"], r=[nr for f, nr in provs if f == "r"], rpba=[nr for f, nr in provs if f == "rpba"],
                   rfees=[nr for f, nr in provs if f == "rfees"])
        if de is not None:
            rec.update(url_de=de[9] or "", leitsatz_de=_br(de[7] or de[8])[:1500], schlagworte_de=_br(de[6])[:500])
        out.append(rec)
    out.sort(key=lambda e: (e["datum"], e["az"]))
    meta = dict(quelle="RheinIP-Datenbank, Tabelle BoaDecision (Entscheidungen der Beschwerdekammern des EPA, epo.org)", anzahl=len(out),
                gesamt=len(orig), zeitraum=[out[0]["datum"], out[-1]["datum"]] if out else None,
                auswahl="alle Entscheidungen der Großen Beschwerdekammer (G), der Juristischen Beschwerdekammer (J) und Überprüfungsanträge (R), "
                        "die T-Entscheidungen der Verteilerschlüssel A, B und C sowie jede in den Richtlinien zitierte Entscheidung",
                hinweis="Zitierte Vorschriften aus dem Feld „Relevant legal provisions“ der Entscheidung (EPÜ 2000; Zitate des EPÜ 1973 bleiben "
                        "außer Betracht); Zählung `zitiert` über alle Entscheidungen einschließlich Verteiler D.",
                zitiert=dict(sorted(zit.items())))
    return dict(meta=meta, entscheidungen=out)


_GL_REF = re.compile(r"^([a-h]|k)_([ivx]+)(?:_(\d+(?:_\d+)*))?$")


def gl_ref(slug):
    """'e_viii_2' -> 'E-VIII, 2'; 'a_ii_5_1' -> 'A-II, 5.1'; 'e_viii' -> 'E-VIII'"""
    m = _GL_REF.match(slug)
    if not m:
        return None
    teil, kap, abs_ = m.groups()
    return "%s-%s" % (teil.upper(), kap.upper()) + (", " + abs_.replace("_", ".") if abs_ else "")


def zitate(text, default="EPC"):
    """Artikel/Regeln im Fließtext mit Gesetz: {('EPC','a','54'), ('EPC','r','56a'), ('PCT','r','80.2'), ('RFees','a','14')}.
    Das Gesetz ist das nächste Kürzel im selben Satzteil; fehlt es, gilt `default` (Regeln mit Punkt: PCT)."""
    out = set()
    for clause in re.split(r";|\.\s+(?=[A-Z(])|\n", text):
        for m in re.finditer(r"\b(Articles?|Art\.|Rules?|R\.)\s*((?:\d+(?:bis|ter|quater|[a-z])?(?:\.\d+)?(?:\([^)]{1,6}\))*(?:\s*(?:,|and|or|to|-|–)\s*)?)+)", clause):
            kind = "a" if m.group(1).startswith("Art") else "r"
            after = clause[m.end():m.end() + 60]
            law = re.match(r"\s*(?:EPC|RFees|PCT|RPBA|RRF|UPR|EPC 1973)\b", after)
            nxt = re.search(r"\b(EPC 1973|EPC|RFees|PCT|RPBA|UPR)\b", after)
            lawname = (law.group(0).strip() if law else (nxt.group(1) if nxt and not re.search(r"\b(?:Art|Rule)", after[:nxt.start()]) else None))
            for nr in re.findall(r"(?<![\d(])(\d+(?:bis|ter|quater|[a-z])?(?:\.\d+)?)(?![\d)])", re.sub(r"\([^)]*\)", "", m.group(2))):
                ln = lawname or ("PCT" if "." in nr else default)
                if ln == "EPC 1973" or ln is None:
                    continue
                if ln == "EPC" and "." in nr:
                    continue
                out.add((ln, kind, nr))
    return out


def build_gl():
    cur = _db_cursor()
    cur.execute("select url, text from \"EPOLegaltext\" where type='gl' and url like '%/guidelines-epc/2026/%'")
    out = []
    for url, text in cur.fetchall():
        slug = url.rsplit("/", 1)[1][:-5]
        ref = gl_ref(slug)
        if not ref:
            continue
        lines = [x.replace("\xa0", " ").strip() for x in text.split("\n")]
        try:
            h = lines.index("Overview") + 1
        except ValueError:
            h = 1
        body = [x for x in lines[h:] if x]
        titel = body[0] if body else ""
        rand = []
        while body and re.match(r"^(?:Art\.|Article|Rule|Rules|R\.)\s?\d", body[-1]) and len(body[-1]) < 40:
            rand.insert(0, body.pop())
        flat = _ws(" ".join(body[1:]))
        z = zitate(flat)
        rz = zitate(" ; ".join(rand))
        dec = sorted({az_norm(m) for m in re.findall(r"\b[TJGR] \d{1,4}/\d{2}\b", flat)})
        out.append(dict(id=slug, ref=ref, titel=titel, rand=rand,
                        a=sorted({n for l, k, n in z | rz if l == "EPC" and k == "a"}, key=lambda n: (int(re.match(r"\d+", n).group(0)), n)),
                        r=sorted({n for l, k, n in z | rz if l == "EPC" and k == "r"}, key=lambda n: (int(re.match(r"\d+", n).group(0)), n)),
                        ra=[n for l, k, n in sorted(rz) if l == "EPC" and k == "a"], rr=[n for l, k, n in sorted(rz) if l == "EPC" and k == "r"],
                        entscheidungen=dec, anfang=flat[:400], zeichen=len(flat),
                        url=url, url_de=url.replace("/en/legal/", "/de/legal/")))
    out.sort(key=lambda g: [int(x) if x.isdigit() else x for x in re.split(r"[_]", g["id"])])
    meta = dict(titel="Richtlinien für die Prüfung im Europäischen Patentamt", ausgabe="März 2026", url="https://www.epo.org/de/legal/guidelines-epc/2026/index.html",
                quelle="RheinIP-Datenbank, Tabelle EPOLegaltext (type gl, englische Fassung 2026)", anzahl=len(out),
                hinweis="`rand` sind die Rechtsgrundlagen am Rand des Abschnitts, `a`/`r` alle im Abschnitt zitierten EPÜ-Artikel und -Regeln.")
    return dict(meta=meta, abschnitte=out)


_OJ_KEEP = ("EUROPEAN PATENT OFFICE", "ADMINISTRATIVE COUNCIL", "BOARDS OF APPEAL", "ENLARGED BOARD OF APPEAL", "INTERNATIONAL TREATIES",
            "EUROPEAN PATENT ORGANISATION")
_OJ_DROP = re.compile(r"Composition of|List of professional representatives|held its \d+|Patent Prosecution Highway|closed in \d{4}|"
                      r"Representation$|Information from the Contracting|Membership|Election|Appointment", re.I)
_MONATE = {m: i + 1 for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])}


def build_oj():
    cur = _db_cursor()
    cur.execute("select url, text from \"EPOLegaltext\" where type='oj' and url ~ 'official-journal/(200[89]|20[12][0-9])/'")
    out = []
    for url, text in cur.fetchall():
        lines = [x.replace("\xa0", " ").strip() for x in text.split("\n") if x.strip()]
        if not lines or lines[0] not in _OJ_KEEP:
            continue
        cand = [x for x in lines[1:6] if re.match(r"^(Decision|Notice|Information|Guidance|Amendment|Rules|Agreement|Arrangements|Fees|Supplementary)", x) and len(x) > 25]
        titel = cand[0] if cand else (lines[2] if len(lines) > 2 else lines[1])
        if _OJ_DROP.search(titel):
            continue
        m = re.search(r"official-journal/(\d{4})/(\d{2})/([ap])(\d+)", url)
        if not m:
            continue
        jahr, monat, art, nr = m.groups()
        fund = "%s, %s" % (jahr, ("A" + nr) if art == "a" else nr)
        dm = re.search(r"dated (\d{1,2}) (%s) (\d{4})" % "|".join(_MONATE), titel)
        datum = "%s-%02d-%02d" % (dm.group(3), _MONATE[dm.group(2)], int(dm.group(1))) if dm else "%s-%s-01" % (jahr, monat)
        flat = _ws(" ".join(lines[1:]))
        z = zitate(flat, default=None)
        a = sorted({n for l, k, n in z if l == "EPC" and k == "a"}, key=lambda n: (int(re.match(r"\d+", n).group(0)), n))
        r = sorted({n for l, k, n in z if l == "EPC" and k == "r"}, key=lambda n: (int(re.match(r"\d+", n).group(0)), n))
        if not a and not r:
            continue
        out.append(dict(fundstelle=fund, datum=datum, rubrik=lines[0], titel=titel[:300], a=a, r=r,
                        rfees=sorted({n for l, k, n in z if l == "RFees"}), entscheidungen=sorted({az_norm(x) for x in re.findall(r"\b[GJ] \d{1,2}/\d{2}\b", flat)}),
                        url=url, url_de=url.replace("/en/legal/", "/de/legal/")))
    out.sort(key=lambda o: o["datum"])
    meta = dict(titel="Amtsblatt des Europäischen Patentamts", quelle="RheinIP-Datenbank, Tabelle EPOLegaltext (type oj, englische Fassung)",
                zeitraum=[out[0]["datum"], out[-1]["datum"]] if out else None, anzahl=len(out),
                auswahl="Beschlüsse des Präsidenten und des Verwaltungsrats, Mitteilungen des EPA und Entscheidungen der Kammern seit 2008, "
                        "die mindestens einen Artikel oder eine Regel des EPÜ nennen")
    return dict(meta=meta, ausgaben=out)


def build_eqe():
    if not EQE_D1.exists():
        print("EQE: %s fehlt, data/eqe_d1.json bleibt unverändert" % EQE_D1)
        return None
    raw = json.loads(EQE_D1.read_text(encoding="utf-8"))
    out = []
    for q in raw:
        jur = q.get("jurisdiction", "")
        default = "EPC" if jur == "EPC" else None
        z = zitate((q.get("legal_basis") or "") + " ; " + (q.get("core_answer_logic") or ""), default=default)
        nums = lambda law, kind: sorted({n for l, k, n in z if l == law and k == kind}, key=lambda n: [int(x) if x.isdigit() else x for x in re.findall(r"\d+|\D+", n)])
        out.append(dict(jahr=q["year"], nr=str(q["question_number"]), punkte=q.get("points_awarded"), thema=q.get("topic", ""), recht=jur,
                        rechtsgrundlage=q.get("legal_basis", ""), a=nums("EPC", "a"), r=nums("EPC", "r"), pct_a=nums("PCT", "a"), pct_r=nums("PCT", "r"),
                        rfees=nums("RFees", "a"),
                        entscheidungen=sorted({az_norm(x) for x in re.findall(r"\bG\s?\d{1,2}/\d{2}\b", (q.get("legal_basis") or "") + " " + (q.get("core_answer_logic") or ""))})))
    out.sort(key=lambda q: (q["jahr"], q["nr"]))
    rang = collections.Counter()
    for q in out:
        for n in q["a"]:
            rang["a" + n] += 1
        for n in q["r"]:
            rang["r" + n] += 1
    meta = dict(titel="EQE Paper D, Teil 1 (Rechtsfragen)", quelle="Prüfungsaufgaben und Prüferberichte der EQE 2015 bis 2025 (EPA), ausgewertet in "
                "~/github/EQEAnalysis (paper_D/output/D1_all_questions.json); hier ohne Fragetext", jahre=sorted({q["jahr"] for q in out}),
                fragen=len(out), rang=dict(rang.most_common()))
    return dict(meta=meta, fragen=out)


def main():
    net = "--no-net" not in sys.argv
    db = "--no-db" not in sys.argv
    nur = set(sys.argv[sys.argv.index("--nur") + 1].split(",")) if "--nur" in sys.argv else {"texte", "boa", "gl", "oj", "eqe"}
    if "texte" in nur:
        d = build_texte(net, db)
        (DATA / "epc.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print("epc.json: %d Artikel, %d Regeln" % (len(d["artikel"]), len(d["regeln"])))
        for w in d["meta"]["warnungen"]:
            print("  Hinweis:", w)
    gl_cited = set()
    if "gl" in nur:
        g = build_gl()
        (DATA / "epc_guidelines.json").write_text(json.dumps(g, ensure_ascii=False, indent=0), encoding="utf-8")
        print("epc_guidelines.json: %d Abschnitte" % len(g["abschnitte"]))
    if (DATA / "epc_guidelines.json").exists():
        gl_cited = {az for x in json.loads((DATA / "epc_guidelines.json").read_text())["abschnitte"] for az in x["entscheidungen"]}
    if "boa" in nur:
        b = build_boa(gl_cited)
        (DATA / "epc_decisions.json").write_text(json.dumps(b, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print("epc_decisions.json: %d von %d Entscheidungen" % (b["meta"]["anzahl"], b["meta"]["gesamt"]))
    if "oj" in nur:
        o = build_oj()
        (DATA / "epc_oj.json").write_text(json.dumps(o, ensure_ascii=False, indent=0), encoding="utf-8")
        print("epc_oj.json: %d Ausgaben %s" % (len(o["ausgaben"]), o["meta"]["zeitraum"]))
    if "eqe" in nur:
        q = build_eqe()
        if q:
            (DATA / "eqe_d1.json").write_text(json.dumps(q, ensure_ascii=False, indent=1), encoding="utf-8")
            print("eqe_d1.json: %d Fragen, Rang: %s" % (len(q["fragen"]), list(q["meta"]["rang"].items())[:25]))


if __name__ == "__main__":
    main()
