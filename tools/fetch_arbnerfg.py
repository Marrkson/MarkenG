#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quellen für das Arbeitnehmererfinderrecht beschaffen (Netz + Postgres) und als JSON unter data/ ablegen.

Erzeugt (alle mitversioniert, damit `build.py` ohne Netz und ohne Datenbank läuft):
  data/arbnerfg.json            Gesetz über Arbeitnehmererfindungen (ArbnErfG, in der Praxis „ArbEG“), alle Paragraphen mit
                                Abschnittsgliederung und Absätzen (gesetze-im-internet.de, XML; Parser aus fetch_patent.py)
  data/arbnerfg_vergrl.json     Richtlinien für die Vergütung von Arbeitnehmererfindungen im privaten Dienst vom 20.7.1959,
                                geändert am 1.9.1983 (PDF von dpma.de), Nummern 1 bis 43 mit Gliederung
  data/arbnerfg_decisions.json  Einigungsvorschläge, Beschlüsse und Zwischenbescheide der Schiedsstelle nach dem ArbEG beim DPMA
                                (Tabelle SchiedsstelleDecision, 2000 bis heute) sowie die Entscheidungen des BGH und des BPatG,
                                die das ArbEG zitieren (BghDecision, BpatgDecision, DeCourtNorm): Metadaten, Leitsatz, Schlagworte,
                                zitierte Vorschriften (ArbnErfG je Paragraph mit Absätzen, Vergütungsrichtlinien je Nummer)

Normzitate: Die Schiedsstelle steht nicht in DeCourtNorm. Deshalb werden die Zitate aller Entscheidungen aus dem Volltext gezählt
(Zitaterkenner aus src/knowledge/gesetze.py, Ketten wie „§§ 9, 12 ArbEG“ eingeschlossen); als „ausgelegt“ gilt eine Vorschrift,
die in der amtlichen Normenkette der Entscheidung (Spalte norms) oder im Leitsatz steht, beim BGH zusätzlich DeCourtNorm.interpreted.

Für den Kommentar (src/knowledge/patent/arbnerfg_kommentar.py) schreibt das Skript je Paragraph die Textstellen, die ihn zitieren,
nach ~/.cache/ipelico/arbnerfg/passagen.json (nicht versioniert; Volltexte bleiben außerhalb des Repos).

Die Datenbank enthält das ArbEG auch in DeLegalProvision, aber ohne Gliederung, ohne Absatztrennung und im Stand 2022; die
Vergütungsrichtlinien fehlen dort ganz (sie stehen auch nicht auf gesetze-im-internet.de). Deshalb XML und DPMA-PDF für die Texte,
Datenbank für die Entscheidungen.

Aufruf:  python3 tools/fetch_arbnerfg.py [--no-net] [--no-db]
Zwischenstände (XML-Zip, PDF, Volltexte) liegen in ~/.cache/ipelico/arbnerfg/. Postgres-Zugang: POSTGRES_LOGIN aus ~/github/RheinIP/.env.
"""
import collections
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import fetch_patent as fp  # noqa: E402  (XML-Parser für gesetze-im-internet.de und Datenbankzugang)
from knowledge import gesetze  # noqa: E402  (Zitaterkenner)

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path.home() / ".cache" / "ipelico" / "arbnerfg"
fp.CACHE = CACHE
UA = {"User-Agent": "Mozilla/5.0 (IPelico fetch_arbnerfg)"}

GESETZ = dict(key="arbnerfg", slug="arbnerfg", kurz="ArbnErfG", datei="arbnerfg.json")
VERGRL_URL = "https://www.dpma.de/docs/dpma/richtlinienfuerdieverguetungvonarbeitnehmererfindungen.pdf"

# Gliederung der Vergütungsrichtlinien (Inhaltsverzeichnis des Originals): (erste Nummer, Teil, Abschnitt)
VERGRL_GLIEDERUNG = [
    (1, "Einleitung", None),
    (3, "Erster Teil: Erfindungswert", "A. I. Betrieblich benutzte Erfindungen – Allgemeines"),
    (6, "Erster Teil: Erfindungswert", "A. I. 2. Ermittlung des Erfindungswertes nach der Lizenzanalogie"),
    (12, "Erster Teil: Erfindungswert", "A. I. 3. Ermittlung des Erfindungswertes nach dem erfassbaren betrieblichen Nutzen"),
    (13, "Erster Teil: Erfindungswert", "A. I. 4. Schätzung"),
    (14, "Erster Teil: Erfindungswert", "A. II. Lizenz-, Kauf- und Austauschverträge"),
    (18, "Erster Teil: Erfindungswert", "A. III. Sperrpatente"),
    (19, "Erster Teil: Erfindungswert", "A. IV. Schutzrechtskomplexe"),
    (20, "Erster Teil: Erfindungswert", "A. V. Nicht verwertete Erfindungen"),
    (25, "Erster Teil: Erfindungswert", "A. VI. Besonderheiten"),
    (28, "Erster Teil: Erfindungswert", "B. Gebrauchsmusterfähige Erfindungen"),
    (29, "Erster Teil: Erfindungswert", "C. Technische Verbesserungsvorschläge (§ 20 Abs. 1)"),
    (30, "Zweiter Teil: Anteilsfaktor", None),
    (38, "Zweiter Teil: Anteilsfaktor", "Wegfall der Vergütung"),
    (39, "Dritter Teil: Die rechnerische Ermittlung der Vergütung", "I. Formel"),
    (40, "Dritter Teil: Die rechnerische Ermittlung der Vergütung", "II. Art der Zahlung der Vergütung"),
    (42, "Dritter Teil: Die rechnerische Ermittlung der Vergütung", "III. Die für die Berechnung der Vergütung maßgebende Zeit"),
]
# Stichwort je Nummer (redaktionell, aus dem Inhaltsverzeichnis und dem Text)
VERGRL_TITEL = {
    "1": "Zweck: Anhaltspunkte, keine verbindlichen Vorschriften", "2": "Aufbau: Erfindungswert × Anteilsfaktor; kein doppelter Ansatz",
    "3": "Drei Methoden: Lizenzanalogie, erfassbarer Nutzen, Schätzung", "4": "Andere Analogiemethoden (Kaufpreisanalogie)",
    "5": "Wahl der Methode", "6": "Lizenzanalogie: Vergleichbarkeit", "7": "Bezugsgröße: Umsatz oder Erzeugung",
    "8": "Gesamtvorrichtung oder wertbeeinflusster Teil", "9": "Erhöhung oder Ermäßigung des Lizenzsatzes",
    "10": "Übliche Lizenzsätze je Industriezweig", "11": "Abstaffelung bei hohen Umsätzen", "12": "Erfassbarer betrieblicher Nutzen",
    "13": "Schätzung", "14": "Lizenzvergabe: Nettolizenzeinnahme", "15": "Lizenzeinnahmen: Abzüge und Umrechnung",
    "16": "Verkauf der Erfindung", "17": "Austauschverträge", "18": "Sperrpatente", "19": "Schutzrechtskomplexe",
    "20": "Nicht verwertete Erfindungen", "21": "Vorrats- und Ausbaupatente", "22": "Nicht verwertbare Erfindungen",
    "23": "Verwertbarkeit noch nicht feststellbar", "24": "Verwertbarkeit nicht ausgenutzt", "25": "Beschränkte Inanspruchnahme",
    "26": "Absatz im Ausland, ausländische Schutzrechte", "27": "Betriebsgeheime Erfindungen (§ 17)",
    "28": "Gebrauchsmusterfähige Erfindungen", "29": "Technische Verbesserungsvorschläge", "30": "Anteilsfaktor: Grundsatz",
    "31": "Stellung der Aufgabe (Wertzahl a)", "32": "Lösung der Aufgabe (Wertzahl b)", "33": "Aufgaben und Stellung im Betrieb (Wertzahl c)",
    "34": "Gruppen der Arbeitnehmer", "35": "Leitende Angestellte", "36": "Wertzahl c: Abweichungen",
    "37": "Tabelle des Anteilsfaktors", "38": "Wegfall der Vergütung", "39": "Formel V = E × A",
    "40": "Laufende Zahlung oder Gesamtabfindung", "41": "Zahlungsweise", "42": "Maßgebende Zeit: Dauer", "43": "Vergütung nach Ablauf",
}


# Gesperrt gesetzte Überschriften der Nr. 3, 11 und 39 („E r m i t t l u n g d e s …“): Wortgrenzen sind im PDF nicht erkennbar
SPERRSATZ = {
    "E r m i t t l u n g d e s E r f i n d u n g s w e r t e s n a c h d e r L i z e n z a n a - l o g i e (N u m m e r 6 ff.)":
        "Ermittlung des Erfindungswertes nach der Lizenzanalogie (Nummer 6 ff.):",
    "E r m i t t l u n g d e s E r f i n d u n g s w e r t e s n a c h d e m e r f a ß b a r e n b e t r i e b l i c h e n N u t z e n ( N u m m e r 12)":
        "Ermittlung des Erfindungswertes nach dem erfaßbaren betrieblichen Nutzen (Nummer 12):",
    "S c h ä t z u n g d e s E r f i n d u n g s w e r t e s ( N u m m e r 13)": "Schätzung des Erfindungswertes (Nummer 13):",
    "B e i s p i e l :": "Beispiel:",
}


def fetch(url, target, net):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 1000:
        return target.read_bytes()
    if not net:
        raise SystemExit("fehlt im Cache und --no-net gesetzt: %s" % target.name)
    data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
    target.write_bytes(data)
    return data


def _dehyph(s):
    """Silbentrennung der PDF-Zeilen auflösen („Ar-\\n beitnehmer“ -> „Arbeitnehmer“), Bindestrich vor Großbuchstaben behalten."""
    s = re.sub(r"(\w)-[ \t]*\n[ \t]*(?=[a-zäöüß])", r"\1", s)
    s = re.sub(r"(\w)-[ \t]*\n[ \t]*(?=[A-ZÄÖÜ])", r"\1-", s)
    return s


def _despace(s):
    """Gesperrte Schrift („E r m i t t l u n g d e s“) zusammenziehen; Wortgrenzen sind dort doppelte Leerzeichen oder fehlen."""
    def fix(m):
        return m.group(0).replace(" ", "")
    return re.sub(r"(?<!\S)(?:[A-Za-zÄÖÜäöüß] ){3,}[A-Za-zÄÖÜäöüß](?!\S)", fix, s)


# ---------------------------------------------------------------- Vergütungsrichtlinien (PDF)
def parse_vergrl(net):
    pdf = CACHE / "vergrl.pdf"
    fetch(VERGRL_URL, pdf, net)
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    start = txt.index("Einleitung", txt.index("folgende Richtlinien"))
    txt = txt[start:]
    for k, v in SPERRSATZ.items():
        txt = re.sub(r"\s+".join(re.escape(w) for w in k.split()), v, txt)
    lines = []
    for ln in txt.split("\n"):
        ln = ln.replace("\f", "")
        if re.fullmatch(r"\d{1,2}", ln.strip()):
            continue   # Seitenzahl
        lines.append(ln)
    # Zwischenüberschriften der Gliederung sind Blöcke zwischen Leerzeilen, deren Zeilen alle weit eingerückt (zentriert) sind;
    # Tabellenzeilen (Nr. 11, 37) beginnen dagegen links. Solche Blöcke werden entfernt.
    blocks, keep = [], []
    for ln in lines + [""]:
        if ln.strip():
            blocks.append(ln)
            continue
        if blocks and not all(len(b) - len(b.lstrip()) >= 6 and not re.match(r"\s*\(\d", b) and "=" not in b for b in blocks):
            keep.extend(blocks)
        blocks = []
        keep.append("")
    nummern, cur = [], None
    for ln in keep:
        m = re.match(r"^\s*\((\d{1,2})\)\s+(.*)$", ln)
        if m and (cur is None or int(m.group(1)) == int(cur["nr"]) + 1):
            if cur:
                nummern.append(cur)
            cur = dict(nr=m.group(1), zeilen=[m.group(2)])
        elif cur:
            cur["zeilen"].append(ln.strip())
    if cur:
        nummern.append(cur)
    out = []
    for n in nummern:
        zeilen = n["zeilen"]
        body = _dehyph("\n".join(zeilen))
        body = _despace(body)
        abs_ = [re.sub(r"[ \t]+", " ", re.sub(r"\s*\n\s*", " ", p)).strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        abs_ = [re.sub(r"\s+(?:Erster|Zweiter|Dritter) Teil$", "", a) for a in abs_ if not re.fullmatch(r"(?:\d\.|[A-C]\.) [^.]{5,90}|(?:Erster|Zweiter|Dritter) Teil", a)]
        nr = int(n["nr"])
        teil, abschnitt = next((t, a) for first, t, a in reversed(VERGRL_GLIEDERUNG) if nr >= first)
        out.append(dict(nr=n["nr"], titel=VERGRL_TITEL.get(n["nr"], ""), teil=teil, abschnitt=abschnitt, absaetze=abs_,
                        url=VERGRL_URL))
    # Seite je Nummer (für den Link #page=n): erste Seite, auf der „(n)“ am Zeilenanfang steht
    seiten = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout.split("\f")
    for o in out:
        o["seite"] = next((i + 1 for i, sv in enumerate(seiten) if i > 1 and re.search(r"^\s*\(%s\)\s" % o["nr"], sv, re.M)), 1)
        o["url"] = "%s#page=%d" % (VERGRL_URL, o["seite"])
    if [o["nr"] for o in out] != [str(i) for i in range(1, 44)]:
        raise SystemExit("Vergütungsrichtlinien: Nummern 1 bis 43 erwartet, gefunden %s" % [o["nr"] for o in out])
    meta = dict(titel="Richtlinien für die Vergütung von Arbeitnehmererfindungen im privaten Dienst",
                stand="vom 20. Juli 1959 (Beilage zum BAnz. Nr. 156 vom 18.8.1959), geändert durch die Richtlinie vom 1. September 1983 (BAnz. Nr. 169, S. 9994); "
                      "nach den Richtlinien vom 1.12.1960 (BAnz. Nr. 237) entsprechend anwendbar auf Arbeitnehmer im öffentlichen Dienst, Beamte und Soldaten",
                quelle=VERGRL_URL, rechtsgrundlage="§ 11 ArbnErfG",
                hinweis="Die Richtlinien sind keine Rechtsnormen, sondern Anhaltspunkte für die angemessene Vergütung (Nr. 1); Beträge noch in DM.")
    return dict(meta=meta, nummern=out)


# ---------------------------------------------------------------- Zitate im Volltext
VRL_RE = re.compile(r"(?:\bRL|Richtlinien?|Vergütungsrichtlinien?|RLn|VergRL)\s*(?:1959\s*)?(?:Nrn?\.|Nummern?|Rn\.)\s*(\d{1,2})"
                    r"((?:\s*(?:,|und|bis|-|–)\s*\d{1,2}(?![\d.]))*)")
_ABS = re.compile(r"(?:Abs\.|Absatz)\s*(\d+)")
_NR = re.compile(r"^\s*(?:Nr\.|Nummer)\s*(\d+)")


def _clean_text(s):
    s = (s or "").replace("\xa0", " ").replace("\r", "")
    s = _dehyph(s)
    s = re.sub(r"(?<=\w)-\s+(?=[a-zäöüß]{2,})", "", s)   # „qualifi-zierter“ aus einspaltigem Fließtext
    return s


def zitate_arbnerfg(text):
    """[(paragraph, absatz|None, start, end)] aller ArbnErfG-Zitate im Text (Kettenglieder einzeln)."""
    out = []
    for m, law, _ in gesetze.resolve(text, None):
        if law != "ArbnErfG" or not m.group(gesetze.G_HEAD).startswith("§"):
            continue
        nums = m.group(gesetze.G_NUMS)
        found = gesetze._NUM.findall(nums)
        if " bis " in nums and len(found) == 2 and found[0].isdigit() and found[1].isdigit() and int(found[1]) - int(found[0]) <= 6:
            found = [str(i) for i in range(int(found[0]), int(found[1]) + 1)]
        sub = m.group(gesetze.G_SUB) or ""
        am = _ABS.search(sub)
        nr = _NR.match(sub)
        for i, p in enumerate(found):
            ab = (am.group(1) if am else (("Nr. " + nr.group(1)) if nr else None)) if i == 0 else None
            out.append((p, ab, m.start(), m.end()))
    return out


def zitate_vrl(text):
    out = []
    for m in VRL_RE.finditer(text):
        nums = [m.group(1)] + re.findall(r"\d{1,2}", m.group(2) or "")
        for n in nums:
            if 1 <= int(n) <= 43:
                out.append((n, m.start(), m.end()))
    return out


def _passage(text, start, end, width=700):
    """Absatz um eine Fundstelle (Leerzeilen trennen Absätze), auf `width` Zeichen um das Zitat gekürzt."""
    a = text.rfind("\n\n", 0, start)
    b = text.find("\n\n", end)
    a = 0 if a < 0 else a + 2
    b = len(text) if b < 0 else b
    if b - a > width:
        a = max(a, start - width // 2)
        b = min(b, end + width // 2)
    p = re.sub(r"\s+", " ", text[a:b]).strip()
    return p


# ---------------------------------------------------------------- Entscheidungen (Postgres)
def _normen_aus_liste(norms):
    """Amtliche Normenkette („§§ 5, 6, 7 ArbEG“, „§ 12 Abs. 3 ArbEG“) -> {paragraph}, VergRL-Nummern."""
    pars, vrl = set(), set()
    for s in norms or []:
        s = s.replace("ArbnErfG", "ArbEG").replace("ArbNErfG", "ArbEG")
        if "ArbEG" in s:
            pars.update(p for p, *_ in zitate_arbnerfg(s))
            # „§ 5, 6, 7 ArbEG“ (Einzel-§ mit Kette) erkennt der Zitaterkenner nur teilweise
            m = re.match(r"^\s*§§?\s*([\d\s,a-z]+?)\s*(?:Abs\.|ArbEG)", s)
            if m:
                pars.update(re.findall(r"\d+[a-z]?", m.group(1)))
        for n, *_ in zitate_vrl(s):
            vrl.add(n)
    return pars, vrl


def build_decisions():
    cur = fp._db_cursor()
    out, volltexte = [], {}
    # 1. Schiedsstelle
    cur.execute('select id, url, "fileNumber", "decisionType", "publicationForm", norms, keywords, headnote, "decisionDate", "decisionText" '
                'from "SchiedsstelleDecision" order by "decisionDate", "fileNumber"')
    for did, url, az, dtyp, pform, norms, kw, head, date, text in cur.fetchall():
        out.append(dict(id=did, gericht="Schiedsstelle", az=fp._ws(az), ecli="", senat="Schiedsstelle nach dem ArbEG beim DPMA",
                        senat_typ="Schiedsstelle", typ=dtyp or "", verfahren="Schiedsverfahren", form=pform or "", name="",
                        schlagworte=fp._ws(kw)[:400], datum=date.date().isoformat() if date else None,
                        leitsatz=fp._leitsatz(head), normen=list(norms or []), url=url))
        volltexte[did] = _clean_text(text)
    # 2. BGH und BPatG: Entscheidungen, die das ArbEG nennen (Volltext) oder in DeCourtNorm mit ArbEG geführt sind
    cur.execute('select "decisionId", paragraph, bool_or(interpreted) from "DeCourtNorm" where law = %s group by 1, 2', ("ArbEG",))
    dcn = collections.defaultdict(dict)
    for did, par, interp in cur.fetchall():
        if par:
            dcn[did][par] = bool(interp)
    rx = r"(ArbEG|ArbNErfG|ArbnErfG|Arbeitnehmererfindungsgesetz|Gesetz(es)? über Arbeitnehmererfindungen)"
    cur.execute('select id, url, "fileNumber", ecli, senate, "decisionType", "caseName", norms, "decisionDate", headnote, "decisionText" '
                'from "BghDecision" where "decisionText" ~ %s or id = any(%s) order by "decisionDate"', (rx, list(dcn)))
    for did, url, az, ecli, senat, dtyp, name, norms, date, head, text in cur.fetchall():
        out.append(dict(id=did, gericht="BGH", az=fp._ws(az), ecli=ecli or "", senat=fp._ws(senat), senat_typ=fp._ws(senat), typ=dtyp or "",
                        verfahren=fp._verfahren(az, "", "BGH"), form="", name=fp._name(name), schlagworte="",
                        datum=date.date().isoformat() if date else None, leitsatz=fp._leitsatz(head), normen=list(norms or []), url=url))
        volltexte[did] = _clean_text(text)
    cur.execute('select id, url, "fileNumber", ecli, senate, "senateType", "decisionType", "caseType", "caseName", norms, "decisionDate", headnote, "decisionText" '
                'from "BpatgDecision" where "decisionText" ~ %s or id = any(%s) order by "decisionDate"', (rx, list(dcn)))
    for did, url, az, ecli, senat, styp, dtyp, ctyp, name, norms, date, head, text in cur.fetchall():
        out.append(dict(id=did, gericht="BPatG", az=fp._ws(az), ecli=ecli or "", senat=fp._ws(senat), senat_typ=fp.SENAT_KURZ.get(styp or "", styp or "–"),
                        typ=dtyp or "", verfahren=fp._verfahren(az, ctyp, "BPatG"), form="", name=fp._name(name), schlagworte="",
                        datum=date.date().isoformat() if date else None, leitsatz=fp._leitsatz(head), normen=list(norms or []), url=url))
        volltexte[did] = _clean_text(text)
    # 3. Zitate zählen, Passagen sammeln
    passagen = collections.defaultdict(list)    # paragraph -> [{az, datum, gericht, abs, text}]
    passagen_vrl = collections.defaultdict(list)
    behalten = []
    for e in out:
        text = volltexte.get(e["id"], "")
        ausgelegt, vrl_ausgelegt = _normen_aus_liste(e["normen"])
        for p, *_ in zitate_arbnerfg(e["leitsatz"] + " " + e["schlagworte"]):
            ausgelegt.add(p)
        for p, i in dcn.get(e["id"], {}).items():
            if i:
                ausgelegt.add(p)
        z = collections.defaultdict(lambda: dict(i=False, m=0, abs={}))
        seen = set()
        for p, ab, s, t in zitate_arbnerfg(text):
            z[p]["m"] += 1
            if ab:
                z[p]["abs"][ab] = z[p]["abs"].get(ab, 0) + 1
            key = (p, s // 400)
            if key not in seen and len([x for x in passagen[p] if x["id"] == e["id"]]) < 6:
                seen.add(key)
                passagen[p].append(dict(id=e["id"], az=e["az"], datum=e["datum"], gericht=e["gericht"], abs=ab, text=_passage(text, s, t)))
        for p in ausgelegt:
            z[p]["i"] = True
        vz = collections.Counter(n for n, *_ in zitate_vrl(text))
        for n, s, t in zitate_vrl(text):
            if len([x for x in passagen_vrl[n] if x["id"] == e["id"]]) < 3:
                passagen_vrl[n].append(dict(id=e["id"], az=e["az"], datum=e["datum"], gericht=e["gericht"], text=_passage(text, s, t, 500)))
        e["zitate"] = {"arbnerfg": {p: dict(i=v["i"], m=v["m"], **({"abs": v["abs"]} if v["abs"] else {})) for p, v in z.items() if v["m"] or v["i"]}}
        if vz or vrl_ausgelegt:
            e["zitate"]["vergrl"] = {n: dict(i=n in vrl_ausgelegt, m=vz.get(n, 0)) for n in set(vz) | vrl_ausgelegt}
        e["normen_text"] = fp._ws("; ".join(e.pop("normen")))[:300]
        if e["gericht"] != "Schiedsstelle" and not e["zitate"]["arbnerfg"]:
            continue   # BGH/BPatG nur mit echtem ArbEG-Zitat („Arbeitnehmererfindungsgesetz“ in der Langform zählt über den Erkenner)
        behalten.append(e)
    behalten.sort(key=lambda e: (e["datum"] or "", e["az"]))
    stat = collections.Counter(e["gericht"] for e in behalten)
    daten = sorted(e["datum"] for e in behalten if e["datum"])
    meta = dict(quelle="RheinIP-Datenbank, Tabellen SchiedsstelleDecision (Veröffentlichungen der Schiedsstelle nach dem ArbEG, dpma.de), BghDecision und BpatgDecision; Normzitate aus dem Volltext",
                anzahl=len(behalten), schiedsstelle=stat["Schiedsstelle"], bgh=stat["BGH"], bpatg=stat["BPatG"],
                mit_leitsatz=sum(1 for e in behalten if e["leitsatz"]), zeitraum=[daten[0], daten[-1]] if daten else None,
                hinweis="Die Schiedsstelle veröffentlicht ausgewählte Einigungsvorschläge in bearbeiteter oder gekürzter Fassung. Normzitate sind maschinell aus dem "
                        "Volltext erkannt; „ausgelegt“ heißt: Die Vorschrift steht in der Normenkette, im Leitsatz oder in den Schlagworten der Entscheidung. "
                        "„RL Nr. n“ meint die Vergütungsrichtlinien von 1959.")
    pas = dict(arbnerfg={p: v for p, v in passagen.items()}, vergrl={n: v for n, v in passagen_vrl.items()})
    return dict(meta=meta, entscheidungen=[{k: v for k, v in e.items() if k != "id"} | {"id": e["id"]} for e in behalten]), pas


def main():
    net = "--no-net" not in sys.argv
    d = fp.parse_gesetz(GESETZ, net)
    (DATA / GESETZ["datei"]).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%s: %d Vorschriften; %s" % (GESETZ["datei"], len(d["paragraphen"]), "; ".join(d["meta"]["stand"])[:100]))
    v = parse_vergrl(net)
    (DATA / "arbnerfg_vergrl.json").write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    print("arbnerfg_vergrl.json: %d Nummern" % len(v["nummern"]))
    if "--no-db" not in sys.argv:
        d, pas = build_decisions()
        (DATA / "arbnerfg_decisions.json").write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")
        (CACHE / "passagen.json").write_text(json.dumps(pas, ensure_ascii=False, indent=0), encoding="utf-8")
        print("arbnerfg_decisions.json:", {k: v for k, v in d["meta"].items() if k != "hinweis"})
    else:
        print("arbnerfg_decisions.json unverändert (--no-db)")


if __name__ == "__main__":
    main()
