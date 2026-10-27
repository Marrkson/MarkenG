# -*- coding: utf-8 -*-
"""Englische Fassung des EPG-Pakets für IPelico (docs/en/): nur das Gebiet „upc“, Kurse u01–u10 mit Graph.

Übersetzt wird nur Text; Struktur (IDs, Antworten, Verweise) kommt immer aus dem deutschen Paket. Die Übersetzungen
liegen als JSON neben dieser Datei:
  u01.json … u10.json      Kurse: Schlüssel `kurs:<id>`, `kapitel:<id>`, `einheit:<id>`, `gruppe:<fallkette>`
  knoten_begriffe.json     Begriffe (`concept:…`) und Kategorien (`kategorie:<deutsch>`, auch für Schemata)
  knoten_entscheidungen.json  kuratierte Entscheidungen (`case:…`: name, kern)
  knoten_schemata.json     Prüfungsschemata und -punkte (`schema:…`, `step:…`)
  knoten_tabellen.json     Abgrenzungstabellen (`distinction:…`)
  knoten_normen.json       Hinweise an EPGÜ/VerfO/EPatVO/…/IPRED (`eunorm:…`: hinweis) und Quellen (`source:…`)
Jeder Eintrag trägt `_de`, den Hash der deutschen Felder, aus denen er übersetzt wurde (`tools/i18n_en.py`):
fehlt ein Eintrag, bricht der Build ab; weicht der Hash ab (deutscher Text geändert), meldet er „veraltet“.
Normtexte sind nicht übersetzt, sondern amtlich englisch: data/upca.json, up_*.json (`absaetze_en`), data/upc_rop.json
(`absaetze_en`, Fassung 2022) und data/durchsetzungsrl_en.json (Cellar).

Zitierform im englischen Text: `Art. 33(1)(a) UPCA`, `R. 19.1 RoP`, `Art. 3(1) UPReg`, `Art. 6 TranslReg`, `R. 6(1) UPR`,
`Art. 2 RFeesUPP`, `Art. 8 IPRED`, `Art. 69 EPC`, deutsche Gesetze unverändert (`§ 139 PatG`).
"""
import copy
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[3] / "data"

KURS_FIELDS = ("titel", "untertitel", "beschreibung", "reihe")
KAPITEL_FIELDS = ("titel",)
UNIT_FIELDS = ("titel", "text", "sachverhalt", "frage", "optionen", "loesung", "merke", "abwandlung", "abschnitt")
GRUPPE_FIELDS = ("titel", "sachverhalt")
NODE_FIELDS = {"concept": ("label", "definition", "erlaeuterung"), "case": ("name", "kern"), "schema": ("label", "beschreibung"),
               "step": ("label", "text", "hinweis"), "distinction": ("label", "frage", "kriterien", "spalten", "rows", "merksatz"),
               "eunorm": ("hinweis",), "source": ("label", "summary")}
NODE_FILE = {"concept": "knoten_begriffe", "case": "knoten_entscheidungen", "schema": "knoten_schemata", "step": "knoten_schemata",
             "distinction": "knoten_tabellen", "eunorm": "knoten_normen", "source": "knoten_normen"}
FAMILIEN = ("upca", "rop", "epatvo", "epatuevo", "doeps", "gebeps", "durchsetzungsrl")

# Normfamilien: Kürzel, Titel und Quelle der englischen Fassung
FAM_EN = {
    "upca": dict(kurz="UPCA", gesetz="Agreement on a Unified Patent Court (UPCA, OJ C 175/1 of 20.6.2013)", datei="upca.json"),
    "rop": dict(kurz="RoP", gesetz="Rules of Procedure of the Unified Patent Court (RoP)", datei="upc_rop.json"),
    "epatvo": dict(kurz="UPReg", gesetz="Regulation (EU) No 1257/2012 on unitary patent protection (UPReg)", datei="up_epatvo.json"),
    "epatuevo": dict(kurz="TranslReg", gesetz="Regulation (EU) No 1260/2012 on translation arrangements (TranslReg)", datei="up_epatuevo.json"),
    "doeps": dict(kurz="UPR", gesetz="Rules relating to Unitary Patent Protection (UPR)", datei="up_doeps.json"),
    "gebeps": dict(kurz="RFeesUPP", gesetz="Rules relating to Fees for Unitary Patent Protection (RFeesUPP)", datei="up_gebeps.json"),
    "durchsetzungsrl": dict(kurz="IPRED", gesetz="Directive 2004/48/EC on the enforcement of intellectual property rights (IPRED)", datei="durchsetzungsrl_en.json"),
}
LAW_EN = {"EPGÜ": "UPCA", "VerfO": "RoP", "EPatVO": "UPReg", "EPatÜVO": "TranslReg", "EPatÜbersVO": "TranslReg", "DOEPS": "UPR",
          "GebOEPS": "RFeesUPP", "DurchsetzungsRL": "IPRED", "EPÜ": "EPC", "AEUV": "TFEU", "EUV": "TEU", "GRCh": "CFR", "EMRK": "ECHR",
          "Brüssel-Ia-VO": "Brussels Ia Regulation", "EPG-Satzung": "UPC Statute"}

ORTE = {"München": "Munich", "Düsseldorf": "Düsseldorf", "Mannheim": "Mannheim", "Hamburg": "Hamburg", "Paris": "Paris", "Mailand": "Milan",
        "Den Haag": "The Hague", "Brüssel": "Brussels", "Wien": "Vienna", "Lissabon": "Lisbon", "Kopenhagen": "Copenhagen"}


def court_en(c):
    """'EPG-BerG' -> 'UPC CoA', 'EPG LK München' -> 'UPC LD Munich', 'EPG ZK Paris' -> 'UPC CD Paris'"""
    if c == "EPG-BerG":
        return "UPC CoA"
    m = re.fullmatch(r"EPG (LK|ZK|RK) (.+)", c)
    if m:
        return "UPC %s %s" % ({"LK": "LD", "ZK": "CD", "RK": "RD"}[m.group(1)], ORTE.get(m.group(2), m.group(2)))
    raise SystemExit("Gericht ohne englische Bezeichnung: %r (knowledge/upc/en/__init__.py court_en)" % c)


def kammer_en(k):
    """Kammern des Entscheidungskorpus (entscheidungen.division_kurz) auf Englisch."""
    if k == "Berufungsgericht":
        return "Court of Appeal"
    if k == "Regionalkammer Nordisch-Baltisch":
        return "Nordic-Baltic Regional Division"
    for de, en in (("Lokalkammer ", "Local Division "), ("Zentralkammer ", "Central Division ")):
        if k.startswith(de):
            return en + ORTE.get(k[len(de):], k[len(de):])
    return k


_ABS = re.compile(r" (?:Abs\.|lit\.|Nr\.|Buchst\.) (\w+)")


def ref_en(r):
    """Normverweis der Einheiten (deutsche Zitierform) in die englische: 'Art. 33 Abs. 1 lit. a EPGÜ' -> 'Art. 33(1)(a) UPCA'."""
    head, law = r.rsplit(" ", 1)
    head = re.sub(r" (?:S\.|Satz|UAbs\.|Unterabs\.|Alt\.|Hs\.) \d+", "", head)
    head = _ABS.sub(r"(\1)", head).replace("Anlage", "Annex").replace("Anhang", "Annex")
    return head + " " + LAW_EN.get(law, law)


def label_en(n):
    """Kurzbezeichnung eines Normknotens: 'Art. 33 EPGÜ' -> 'Art. 33 UPCA', 'R. 19 VerfO' -> 'R. 19 RoP'."""
    head = n["label"].rsplit(" ", 1)[0]
    return head + " " + FAM_EN[n["rl"]]["kurz"]


def de_hash(fields):
    return hashlib.sha1(json.dumps(fields, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:10]


def _pick(obj, names):
    return {f: obj[f] for f in names if obj.get(f) not in (None, "", [], {})}


# ------------------------------------------------------------------ deutsche Quellen
def upc_kurse(kurse):
    return [k for k in kurse if k["gebiet"] == "upc"]


def _in_paket(n):
    s = n["id"].split(":", 1)[1]
    if n["type"] in ("unit", "chapter", "course"):
        return False
    if n["type"] == "eunorm":
        return n.get("rl") in FAMILIEN
    if n["type"] == "source":
        return s.startswith(("uprl:", "upinfo:"))
    return s.startswith(("upc_", "d_upc_"))


def knoten_ids(graph, kurse):
    """Knoten der englischen App: das EPG-Paket, die Durchsetzungsrichtlinie und alles, worauf die EPG-Einheiten verweisen."""
    ids = {n["id"] for n in graph["nodes"] if _in_paket(n)}
    for k in upc_kurse(kurse):
        for c in k["kapitel"]:
            for e in c["einheiten"]:
                ids |= {"concept:" + x for x in e.get("concepts", [])} | {"case:" + x for x in e.get("cases", [])}
                ids |= {"distinction:" + x for x in e.get("distinctions", [])}
                if e.get("schema"):
                    ids.add("schema:" + e["schema"])
                if e.get("step"):
                    ids.add(e["step"])
    return ids


def quellen(kurse, graph):
    """{datei: {schlüssel: {feld: deutscher Text, '_de': hash}}} – das, was übersetzt sein muss."""
    out = {}

    def put(datei, key, fields):
        if fields:
            out.setdefault(datei, {})[key] = dict(fields, _de=de_hash(fields))

    for k in upc_kurse(kurse):
        d = k["id"]
        put(d, "kurs:" + k["id"], _pick(k, KURS_FIELDS))
        for c in k["kapitel"]:
            put(d, "kapitel:" + c["id"], _pick(c, KAPITEL_FIELDS))
            for e in c["einheiten"]:
                if e.get("gruppe"):
                    put(d, "gruppe:" + e["gruppe"]["id"], _pick(e["gruppe"], GRUPPE_FIELDS))
                put(d, "einheit:" + e["id"], _pick(e, UNIT_FIELDS))
    ids = knoten_ids(graph, kurse)
    for n in graph["nodes"]:
        if n["id"] not in ids:
            continue
        put(NODE_FILE[n["type"]], n["id"], _pick(n, NODE_FIELDS[n["type"]]))
        if n.get("kategorie"):
            put("knoten_begriffe", "kategorie:" + n["kategorie"], {"kategorie": n["kategorie"]})
    return out


# ------------------------------------------------------------------ Übersetzungen laden und prüfen
def laden():
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(HERE.glob("*.json"))}


def pruefen(src, tr):
    """(fehlend, veraltet, ueberzaehlig, formfehler) als Listen 'datei: schlüssel …'."""
    fehlt, alt, extra, form = [], [], [], []
    for datei, entries in src.items():
        have = tr.get(datei, {})
        for key, de in entries.items():
            en = have.get(key)
            if en is None:
                fehlt.append("%s: %s" % (datei, key))
                continue
            if en.get("_de") != de["_de"]:
                alt.append("%s: %s" % (datei, key))
            for f, v in de.items():
                if f == "_de":
                    continue
                w = en.get(f)
                if w in (None, "", []):
                    form.append("%s: %s.%s fehlt" % (datei, key, f))
                elif type(w) is not type(v):
                    form.append("%s: %s.%s hat den falschen Typ" % (datei, key, f))
                elif f in ("optionen", "kriterien", "spalten") and len(w) != len(v):
                    form.append("%s: %s.%s: %d statt %d Einträge" % (datei, key, f, len(w), len(v)))
                elif f == "rows" and [len(r) for r in w] != [len(r) for r in v]:
                    form.append("%s: %s.rows: Maße weichen ab" % (datei, key))
        extra += ["%s: %s" % (datei, key) for key in have if key not in entries]
    return fehlt, alt, extra, form


def _tr(tr):
    flat = {}
    for entries in tr.values():
        flat.update(entries)
    return flat


def _apply(obj, en, names):
    for f in names:
        if obj.get(f) not in (None, "", [], {}):
            obj[f] = en[f]


def kurse_en(kurse, tr):
    t = _tr(tr)
    out = copy.deepcopy(upc_kurse(kurse))
    for k in out:
        _apply(k, t["kurs:" + k["id"]], KURS_FIELDS)
        for c in k["kapitel"]:
            _apply(c, t["kapitel:" + c["id"]], KAPITEL_FIELDS)
            for e in c["einheiten"]:
                _apply(e, t["einheit:" + e["id"]], UNIT_FIELDS)
                if e.get("gruppe"):
                    _apply(e["gruppe"], t["gruppe:" + e["gruppe"]["id"]], GRUPPE_FIELDS)
                e["norms"] = [ref_en(r) for r in e.get("norms", [])]
    return out


_GROSS_EN = {"UPC", "EPO", "EU", "CMS", "EPC", "PCT", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV"}


def satz_en(s):
    """'CHAPTER VI – INTERNATIONAL JURISDICTION AND COMPETENCE' -> 'Chapter VI – International jurisdiction and competence'"""
    if not s or s.upper() != s:
        return s or ""
    out, anfang = [], True
    for w in s.split(" "):
        core = w.strip(".,()")
        if w in ("–", "-"):
            out.append(w); anfang = True
            continue
        out.append(w if core in _GROSS_EN or re.fullmatch(r"\d+[A-Z]?", core) else (w[:1] + w[1:].lower() if anfang else w.lower()))
        anfang = False
    return " ".join(out)


def _absaetze_en(raw):
    """'(1) …' (EPGÜ, Verordnungen, DOEPS) oder '1. …' (VerfO) -> [{nr, text}]"""
    out = []
    for a in raw:
        m = re.match(r"^\((\d+[a-z]?)\)\s+(.*)$", a) or re.match(r"^(\d{1,2})\.\s+(.*)$", a)
        out.append(dict(nr=m.group(1), text=m.group(2)) if m else dict(nr=None, text=a))
    return out


def _fam_texte():
    """{(rl, nummer): englischer Artikel/Regel} aus den Datendateien."""
    out = {}
    for rl, f in FAM_EN.items():
        d = json.loads((DATA / f["datei"]).read_text(encoding="utf-8"))
        for a in d.get("artikel") or d.get("regeln"):
            out[(rl, str(a["nr"]).upper())] = a
        erw = d.get("erwaegungsgruende_en") or d.get("praeambel_en")  # Erwägungsgründe/Präambel als Sammelknoten
        if erw:
            out[(rl, "ERWAEGUNGSGRUENDE")] = dict(titel_en="Preamble" if rl == "rop" else "Recitals",
                                                  absaetze_en=[dict(nr=str(e["nr"]), text=e["text"]) for e in erw])
    return out


def graph_en(graph, kurse, tr):
    """Der reduzierte Graph der App, beschränkt auf die EPG-Knoten und ins Englische gesetzt."""
    t = _tr(tr)
    ids = knoten_ids(graph, kurse)
    texte = _fam_texte()
    nodes = []
    for n in graph["nodes"]:
        if n["id"] not in ids:
            continue
        n = copy.deepcopy(n)
        if n["type"] in NODE_FIELDS:
            en = t.get(n["id"], {})
            _apply(n, en, NODE_FIELDS[n["type"]])
        if n.get("kategorie"):
            n["kategorie"] = t["kategorie:" + n["kategorie"]]["kategorie"]
        if n["type"] == "case":
            n["court"] = court_en(n["court"])
            n["label"] = n["court"] + " – " + n["name"]
            n["fundstelle"] = re.sub(r"^EPG\b", "UPC", n.get("fundstelle") or "")
        elif n["type"] == "eunorm":
            sammel = n["id"].endswith(":erwaegungsgruende")
            a = texte.get((n["rl"], "ERWAEGUNGSGRUENDE" if sammel else str(n["nummer"]).upper()))
            if a is None or not (a.get("absaetze_en") or a.get("absaetze")):
                raise SystemExit("kein englischer Wortlaut für %s (data/%s)" % (n["id"], FAM_EN[n["rl"]]["datei"]))
            f = FAM_EN[n["rl"]]
            raw = a.get("absaetze_en") or a["absaetze"]
            n.update(label=(a["titel_en"] + " " + f["kurz"]) if sammel else label_en(n), kurz=f["kurz"], gesetz=f["gesetz"], titel=a.get("titel_en") or a["titel"],
                     absaetze=raw if sammel else _absaetze_en(raw),
                     kapitel=satz_en(a.get("teil_en") or a.get("kapitel_en") or ""), abschnitt=satz_en(a.get("abschnitt_en") or a.get("kapitel_en") or ""))
            if n["kapitel"] == n["abschnitt"]:
                n["kapitel"] = ""
            n["url"] = a.get("url_en") or n.get("url_en") or n["url"]
            if a.get("hinweis_en"):  # Abweichung der englischen Fassung (VerfO 2022 gegenüber der konsolidierten Fassung)
                n["hinweis"] = (n.get("hinweis", "") + " " if n.get("hinweis") else "") + a["hinweis_en"]
            for x in ("titel_en", "url_en", "umsetzung_weitere", "url_pdf"):
                n.pop(x, None)
        elif n["type"] == "source":
            n["url"] = n.get("url_en") or n["url"].replace("epo.org/de/", "epo.org/en/")
            n["provider"] = {"UP-Richtlinien": "Guidelines for Unitary Patent Protection", "epo.org Einheitspatent": "epo.org Unitary Patent"}.get(n.get("provider"), n.get("provider"))
        nodes.append(n)
    keep = {n["id"] for n in nodes}
    edges = [dict(e, ref=ref_en(e["ref"])) if e.get("ref") and " " in e["ref"] else e
             for e in graph["edges"] if e["source"] in keep and e["target"] in keep]
    return dict(nodes=nodes, edges=edges)


def gebiete_en(gebiete):
    g = copy.deepcopy([x for x in gebiete if x["id"] == "upc"])
    g[0].update(kurz="UPC", titel="Unified Patent Court (UPCA, RoP)",
                beschreibung="Structure and jurisdiction of the UPC, infringement and revocation actions, provisional measures, evidence, "
                             "remedies, appeal and the Unitary Patent – with the case law of the Court of Appeal.")
    return g


def bauen(kurse, gebiete, graph):
    """Englische Kurse, Gebiete und Graph; bricht ab, wenn Übersetzungen fehlen oder nicht passen."""
    src, tr = quellen(kurse, graph), laden()
    fehlt, alt, extra, form = pruefen(src, tr)
    if fehlt or form:
        raise SystemExit("Englische Fassung (src/knowledge/upc/en/) unvollständig – python3 tools/i18n_en.py status\n  "
                         + "\n  ".join((fehlt + form)[:40]) + ("\n  …" if len(fehlt + form) > 40 else ""))
    if alt:
        print("Hinweis: %d englische Einträge veraltet (deutscher Text geändert), z. B. %s – tools/i18n_en.py status" % (len(alt), alt[0]))
    return kurse_en(kurse, tr), gebiete_en(gebiete), graph_en(graph, kurse, tr)
