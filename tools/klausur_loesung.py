#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lösungen der Klausuren TS/NS/RP1/RP2 in Lösungssprache: Prüfung und Darstellung.

Ablage:  klausuren/loesungen/<typ>/<id>.json  (z. B. klausuren/loesungen/ts/PAP-2018-III-TS.json; nicht versioniert)
Aufruf:  python3 tools/klausur_loesung.py check <datei.json> [...]   Schema, Zitate, Entscheidungen, Wochentage
         python3 tools/klausur_loesung.py check --alle
         python3 tools/klausur_loesung.py render [ziel]               Seiten nach klausuren/loesungen/site/

Lösungssprache (Schema der JSON-Datei)
--------------------------------------
{
  "id": "PAP-2018-III-TS", "typ": "TS",
  "titel": "kurzer Falltitel", "thema": "ein Satz: Problemschwerpunkte",
  "zeittafel": [{"datum": "Do 15.01.2009", "ereignis": "...", "bedeutung": "..."}],
  "fristen":   [{"frist": "...", "norm": "...", "berechnung": "...", "verschiebung": "...", "ende": "Fr 15.01.2010, ..."}],
  "vorbemerkung": "optional (Merkmalsgliederung, Auslegung des Sachverhalts)",
  "fragen": [{
     "nr": "1a", "aufgabe": "wörtlicher Fragetext",
     "pruefungen": [{
        "agl": "Nichtigkeitsklage gegen den DE-Teil", "normen": ["Art. II § 6 Abs. 1 IntPatÜG", "§ 81 Abs. 1 S. 1 PatG"],
        "hinweis": "optional",
        "bloecke": [{"titel": "A · Zulässigkeit", "hinweis": "optional",
                     "v": [{"k": "V1", "titel": "Zuständigkeit", "normen": ["§ 81 Abs. 4 S. 1 PatG"],
                            "def": "Definition mit Quelle", "sub": "Subsumtion", "erg": "+",
                            "unter": [ ...gleiche Struktur, k = "V1.1" ... ]}]}],
        "ergebnis": "Ergebnis dieser Prüfung"}],
     "notizen": ["optional"],
     "ergebnis": "Ergebnis der Frage"}],
  "abgleich": "Abgleich mit Lösungshinweis oder zugrunde liegender Entscheidung (leer, wenn keiner)",
  "rechtsstand": "Abweichungen zwischen dem Recht zur Zeit der Klausur und heute (leer, wenn keine)",
  "entscheidungen": [{"az": "X ZR 49/12", "gericht": "BGH", "datum": "2013-04-16", "name": "Fahrzeugscheibe",
                      "quelle": "korpus" | "https://… (per WebSearch geprüft)"}],
  "normtexte_extern": ["BGB §§ 187, 188, 193 (gesetze-im-internet.de)"]
}
erg: "+" erfüllt, "-" nicht erfüllt, "+?" voraussichtlich erfüllt, "?" offen, "" Gliederungspunkt ohne eigenes Ergebnis.
Jede Voraussetzung so formulieren, dass "+" für die AGL spricht. Gesetzeszitate immer mit Gesetz („§ 9 Abs. 1 Nr. 2 MarkenG“).
Fristen immer mit drei Normen (Frist, Berechnung, Verschiebung) und Wochentag des Endes („Fr 15.01.2010“).
Jedes Aktenzeichen im Text muss in "entscheidungen" stehen; "korpus" nur, wenn es in einem lokalen Korpus steht.
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

KL = ROOT / "klausuren"
LOE = KL / "loesungen"
TYPEN = {"TS": "Technische Schutzrechte", "NS": "Nichttechnische Schutzrechte", "RP1": "Rechtspraxis 1", "RP2": "Rechtspraxis 2"}
ERG = {"+": "(+)", "-": "(–)", "+?": "(+)?", "?": "(?)", "": ""}
WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

# ------------------------------------------------------------------ Aktenzeichen
AZ_PATTERNS = [
    r"\b[IVX]{1,4}a? Z[RBA] \(?\w*\)? ?\d+/\d{2}\b",          # BGH: X ZR 49/12, I ZB 44/14, X ZB 22/07, Xa ZB 20/08
    r"\b[IVX]{1,4}a? Z[RBA] \d+/\d{2}\b",
    r"\b\d{1,2} W \(pat\) \d+/\d{2}\b",                         # BPatG Beschwerde
    r"\b\d{1,2} Ni \d+/\d{2}(?: \((?:EP|EU)\))?",              # BPatG Nichtigkeit
    r"\b\d{1,2} ZA \(pat\) \d+/\d{2}\b",
    r"\bArb\.? ?Erf\. \d+/\d{2}\b",                             # Schiedsstelle
    r"\b[GTJRW] \d{1,4}/\d{2}\b",                               # EPA-Beschwerdekammern
    r"\bC-\d{1,3}/\d{2}\b", r"\bT-\d{1,3}/\d{2}\b",             # EuGH, EuG
    r"\bR \d{1,4}/\d{4}-\d\b",                                  # EUIPO-Beschwerdekammern
    r"\b\d{1,2}[a-z]? O \d+/\d{2}\b",                           # LG
    r"\b(?:I-)?\d{1,2} U \d+/\d{2}\b",                          # OLG
    r"\bUPC[_-][A-Z]{3}[_-]\d+/\d{4}\b", r"\b(?:App|ORD|ACT)_\d+/\d{4}\b",
]
AZ_RE = re.compile("|".join("(?:%s)" % p for p in AZ_PATTERNS))


def _norm_az(s):
    s = re.sub(r"\s+", " ", s.strip())
    s = s.replace("Arb.Erf.", "Arb.Erf.").replace("ArbErf.", "Arb.Erf.")
    return re.sub(r"\b([GTJRW]) 0+(\d)", r"\1 \2", s)   # T 0641/00 -> T 641/00


def korpus_index():
    idx = {}
    for f, key in (("patent_decisions", "az"), ("design_decisions", "az"), ("arbnerfg_decisions", "az"),
                   ("epc_decisions", "az"), ("upc_decisions", "docket")):
        d = json.loads((ROOT / "data" / (f + ".json")).read_text(encoding="utf-8"))
        for e in (d["entscheidungen"] if isinstance(d, dict) else d):
            az = e.get(key)
            if az:
                idx.setdefault(_norm_az(az), []).append((f, e.get("datum") or e.get("date") or "", e.get("name") or ""))
    # in den Wissenspaketen bereits verifizierte Entscheidungen (Marken: per WebSearch geprüft, PLAYBOOK)
    # Formate: dict(… date="2009-07-09", az="I ZB 88/07"), e("…", "Name", BGH, "2009-01-20", "X ZB 22/07"), eb("…", "…", "G 1/22", "2023-10-10")
    for p in [ROOT / "src/knowledge/cases.py", *sorted((ROOT / "src/knowledge").rglob("cases*.py"))]:
        for line in p.read_text(encoding="utf-8").splitlines():
            dates = re.findall(r'"(\d{4}-\d{2}-\d{2})"', line)
            if len(dates) != 1:
                continue
            for q in re.findall(r'"([^"]{3,60})"', line):
                for az in AZ_RE.findall(q):
                    idx.setdefault(_norm_az(az), []).append((p.stem, dates[0], ""))
    return idx


# ------------------------------------------------------------------ Prüfung
def _walk_strings(v, path=""):
    if isinstance(v, str):
        yield path, v
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from _walk_strings(x, "%s[%d]" % (path, i))
    elif isinstance(v, dict):
        for k, x in v.items():
            if k in ("entscheidungen", "normtexte_extern", "id", "typ", "erg", "k"):
                continue
            yield from _walk_strings(x, (path + "." if path else "") + k)


def _schema(d):
    errs = []
    for k in ("id", "typ", "titel", "thema", "fragen", "entscheidungen"):
        if k not in d:
            errs.append("Feld fehlt: " + k)
    if d.get("typ") not in TYPEN:
        errs.append("typ muss TS, NS, RP1 oder RP2 sein")

    def v_check(v, where):
        for k in ("k", "titel", "erg"):
            if k not in v:
                errs.append("%s: Feld %s fehlt" % (where, k))
        if v.get("erg") not in ERG:
            errs.append("%s: erg %r ungültig (erlaubt: + - +? ? leer)" % (where, v.get("erg")))
        if v.get("erg") and not v.get("normen") and not v.get("unter"):
            errs.append("%s (%s): Voraussetzung mit Ergebnis ohne normen" % (where, v.get("titel")))
        for i, u in enumerate(v.get("unter", [])):
            v_check(u, "%s.unter[%d]" % (where, i))

    for i, f in enumerate(d.get("fragen", [])):
        w = "fragen[%d]" % i
        for k in ("nr", "aufgabe", "pruefungen", "ergebnis"):
            if k not in f:
                errs.append("%s: Feld %s fehlt" % (w, k))
        for j, p in enumerate(f.get("pruefungen", [])):
            wp = "%s.pruefungen[%d]" % (w, j)
            if not p.get("agl") or not p.get("normen"):
                errs.append("%s: agl und normen erforderlich" % wp)
            for b_i, b in enumerate(p.get("bloecke", [])):
                for v_i, v in enumerate(b.get("v", [])):
                    v_check(v, "%s.bloecke[%d].v[%d]" % (wp, b_i, v_i))
    for i, fr in enumerate(d.get("fristen", [])):
        for k in ("frist", "norm", "berechnung", "verschiebung", "ende"):
            if not fr.get(k):
                errs.append("fristen[%d]: Feld %s fehlt oder leer (Fristen immer mit Berechnung und Verschiebung)" % (i, k))
    for i, e in enumerate(d.get("entscheidungen", [])):
        for k in ("az", "gericht", "datum", "quelle"):
            if not e.get(k):
                errs.append("entscheidungen[%d]: Feld %s fehlt" % (i, k))
    return errs


def _zitate(d):
    import check_zitate as cz
    from knowledge.gesetze import resolve, href_for, LAWS
    texts = cz.load_texts(False)
    errs, warns = [], []
    for path, s in _walk_strings(d):
        for m, law, how in resolve(s, None):
            cite = m.group(0)
            if how == "alte Fassung":
                continue
            around = s[max(0, m.start() - 40):m.end() + 20].replace("\n", " ")
            if law == "":
                warns.append("%s: nicht verlinkbares Gesetz: %s  …%s…" % (path, cite, around))
                continue
            if not law:
                errs.append("%s: Gesetzesangabe fehlt: %s  …%s…" % (path, cite, around))
                continue
            probs = cz.check_structure(m, law, texts) if law in LAWS else (cz.check_epc(m) if law == "EPÜ" else [])
            for p in probs:
                errs.append("%s: %s  …%s…" % (path, p, around))
            if href_for(m, law) is None and not probs:
                warns.append("%s: kein Link (%s): %s" % (path, law, cite))
    return errs, warns


def _entscheidungen(d, idx):
    errs = []
    listed = {_norm_az(e.get("az", "")): e for e in d.get("entscheidungen", [])}
    for path, s in _walk_strings(d):
        for az in AZ_RE.findall(s):
            if _norm_az(az) not in listed:
                errs.append("%s: Aktenzeichen %s steht nicht in entscheidungen" % (path, az))
    for az, e in listed.items():
        hits = idx.get(az)
        if e.get("quelle") == "korpus":
            if not hits:
                errs.append("entscheidungen: %s als korpus angegeben, aber in keinem lokalen Korpus" % az)
            elif e.get("datum") and not any(h[1][:10] == e["datum"][:10] for h in hits):
                errs.append("entscheidungen: %s Datum %s passt nicht zum Korpus (%s)" % (az, e["datum"], ", ".join(sorted({h[1] for h in hits}))))
        elif not str(e.get("quelle", "")).startswith("http"):
            errs.append("entscheidungen: %s braucht quelle 'korpus' oder eine URL der WebSearch-Prüfung" % az)
    return errs


def _wochentage(d):
    errs = []
    for path, s in _walk_strings(d):
        for m in re.finditer(r"\b(Mo|Di|Mi|Do|Fr|Sa|So),? (\d{1,2})\.(\d{1,2})\.(\d{4})\b", s):
            try:
                wd = WT[date(int(m.group(4)), int(m.group(3)), int(m.group(2))).weekday()]
            except ValueError:
                errs.append("%s: ungültiges Datum %s" % (path, m.group(0)))
                continue
            if wd != m.group(1):
                errs.append("%s: %s ist ein %s, kein %s" % (path, m.group(0)[3:].strip(), wd, m.group(1)))
    return errs


def check(paths):
    idx = korpus_index()
    total = 0
    for p in paths:
        d = json.loads(Path(p).read_text(encoding="utf-8"))
        errs = _schema(d)
        z_err, z_warn = _zitate(d)
        errs += z_err + _entscheidungen(d, idx) + _wochentage(d)
        total += len(errs)
        print("== %s: %d Fehler, %d Warnungen" % (p, len(errs), len(z_warn)))
        for e in errs:
            print("  FEHLER  " + e)
        for w in z_warn:
            print("  WARNUNG " + w)
    return total


# ------------------------------------------------------------------ Darstellung
def _klausuren():
    out = {}
    for t in TYPEN:
        d = json.loads((KL / "json" / ("klausuren_%s.json" % t.lower())).read_text(encoding="utf-8"))
        for k in d["klausuren"]:
            out[k["id"]] = k
    return out


def _linkify(s):
    from knowledge.gesetze import linkify
    return linkify(s, fmt="html", escape=html.escape, law=None)


def _render_v(v, depth=0):
    erg = v.get("erg", "")
    cls = {"+": "plus", "+?": "plus", "-": "minus", "?": "open"}.get(erg, "")
    normen = " ".join('<span class="n">%s</span>' % _linkify(n) for n in v.get("normen", []))
    d = '<span class="def">%s</span>' % _linkify(v["def"]) if v.get("def") else ""
    out = ['<div class="v%s"><div class="vk">%s</div><div class="vb"><b>%s</b> %s%s</div><div class="vs">%s</div><div class="vr %s">%s</div></div>'
           % (" sub" * (depth > 0), html.escape(v["k"]), html.escape(v["titel"]), normen, d,
              _linkify(v.get("sub", "")), cls, ERG.get(erg, ""))]
    for u in v.get("unter", []):
        out.append(_render_v(u, depth + 1))
    return "\n".join(out)


def _render_exam(sol, exam, bilder):
    from string import Template
    rows = []
    # Sachverhalt: Volltext der Klausur links, Zeittafel und Fristen rechts
    left = '<div class="qlabel">Sachverhalt (Volltext)</div><div class="volltext">%s</div>' % html.escape(exam["volltext"])
    if bilder:
        left += '<div class="bilder">' + "".join(
            '<a href="../%s" target="_blank" rel="noopener"><img src="../%s" alt="%s" loading="lazy"></a>' % (b, b, html.escape(Path(b).stem)) for b in bilder) + "</div>"
    right = []
    if sol.get("zeittafel"):
        right.append('<div class="table-wrap"><table><tr><th>Datum</th><th>Ereignis</th><th>Bedeutung</th></tr>%s</table></div>' % "".join(
            "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (html.escape(z["datum"]), _linkify(z["ereignis"]), _linkify(z.get("bedeutung", ""))) for z in sol["zeittafel"]))
    if sol.get("fristen"):
        right.append('<div class="table-wrap"><table><tr><th>Frist</th><th>Norm</th><th>Berechnung</th><th>Verschiebung</th><th>Ende</th></tr>%s</table></div>' % "".join(
            "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % tuple(_linkify(f[k]) for k in ("frist", "norm", "berechnung", "verschiebung", "ende")) for f in sol["fristen"]))
    if sol.get("vorbemerkung"):
        right.append('<p class="note-line">%s</p>' % _linkify(sol["vorbemerkung"]))
    rows.append((left, "\n".join(right) or "<p class='note-line'>–</p>"))
    for f in sol["fragen"]:
        l = '<div class="qlabel">Frage %s</div><p class="aufgabe">%s</p>' % (html.escape(f["nr"]), html.escape(f["aufgabe"]))
        r = []
        for p in f["pruefungen"]:
            r.append('<div class="agl"><span class="k">AGL</span><b>%s</b>%s</div>' % (
                html.escape(p["agl"]), "".join('<span class="n">%s</span>' % _linkify(n) for n in p["normen"])))
            if p.get("hinweis"):
                r.append('<p class="note-line">%s</p>' % _linkify(p["hinweis"]))
            for b in p.get("bloecke", []):
                r.append('<div class="lvl">%s%s</div>' % (html.escape(b["titel"]), (' <span class="def nd">%s</span>' % _linkify(b["hinweis"])) if b.get("hinweis") else ""))
                r.extend(_render_v(v) for v in b.get("v", []))
            if p.get("ergebnis"):
                r.append('<div class="erg sm"><div class="vk">⇒</div><div>%s</div></div>' % _linkify(p["ergebnis"]))
        for n in f.get("notizen", []):
            r.append('<p class="note-line">%s</p>' % _linkify(n))
        r.append('<div class="erg"><div class="vk">⇒</div><div><b>Ergebnis %s:</b> %s</div></div>' % (html.escape(f["nr"]), _linkify(f["ergebnis"])))
        rows.append((l, "\n".join(r)))
    body = "\n".join('<div class="task">%s</div><div class="sol">%s</div>' % lr for lr in rows)
    notes = []
    if sol.get("abgleich"):
        notes.append('<div class="note"><h2>Abgleich</h2><p>%s</p></div>' % _linkify(sol["abgleich"]))
    if sol.get("rechtsstand"):
        notes.append('<div class="note"><h2>Rechtsstand</h2><p>%s</p></div>' % _linkify(sol["rechtsstand"]))
    ent = "".join("<li>%s %s, %s%s – %s</li>" % (html.escape(e["gericht"]), html.escape(e["az"]), html.escape(e["datum"]),
                                                 (" „%s“" % html.escape(e["name"])) if e.get("name") else "",
                                                 "Korpus" if e["quelle"] == "korpus" else '<a href="%s" target="_blank" rel="noopener">Web</a>' % html.escape(e["quelle"]))
                  for e in sol.get("entscheidungen", []))
    ext = "".join("<li>%s</li>" % html.escape(x) for x in sol.get("normtexte_extern", []))
    notes.append('<div class="note"><h2>Entscheidungen</h2><ul>%s</ul>%s</div>' % (ent or "<li>keine</li>", ("<h2>Normtexte extern</h2><ul>%s</ul>" % ext) if ext else ""))
    tpl = Template((Path(__file__).parent / "klausur_loesung_template.html").read_text(encoding="utf-8"))
    return tpl.substitute(title=html.escape("%s %s" % (sol["typ"], exam["id"].split("-")[2] + "/" + exam["id"].split("-")[1])),
                          eyebrow=html.escape("Patentanwaltsprüfung %s/%s · %s" % (exam["termin"], exam["jahr"], TYPEN[sol["typ"]])),
                          h1=html.escape(sol["titel"]), lede=_linkify(sol["thema"]), body=body, notes="\n".join(notes))


def render(target):
    import shutil
    target = Path(target)
    exams = _klausuren()
    (target / "k").mkdir(parents=True, exist_ok=True)
    rows = []
    for t in TYPEN:
        for p in sorted((LOE / t.lower()).glob("PAP-*.json")):
            sol = json.loads(p.read_text(encoding="utf-8"))
            exam = exams[sol["id"]]
            bilder = []
            for doc in exam["dokumente"]:
                for s in doc["seiten"]:
                    for b in s.get("bilder", []):
                        src = KL / b["datei"]
                        dst = target / "img" / src.name
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            from PIL import Image
                            im = Image.open(src)
                            im.thumbnail((900, 900))
                            im.save(dst, optimize=True)
                        except Exception:  # noqa: BLE001
                            shutil.copy(src, dst)
                        bilder.append("img/" + src.name)
            (target / "k" / (sol["id"] + ".html")).write_text(_render_exam(sol, exam, bilder), encoding="utf-8")
            n_v = sum(1 for _ in re.finditer(r'"erg"', p.read_text(encoding="utf-8")))
            rows.append((t, sol["id"], exam["termin"], exam["jahr"], sol["titel"], sol["thema"], len(sol["fragen"]), n_v))
    (target / "index.html").write_text(_render_index(rows, exams), encoding="utf-8")
    print(len(rows), "Lösungen ->", target)
    return rows


def _render_index(rows, exams):
    """Startseite (Hauptseite des Artifacts: ohne doctype, das Skelett ergänzt der Host)."""
    have = {r[1]: r for r in rows}
    css = (Path(__file__).parent / "klausur_loesung_template.html").read_text(encoding="utf-8")
    css = css[css.index("<style>"):css.index("</style>") + 8]
    parts = ['<title>Klausurlösungen Patentanwaltsprüfung</title>', '<meta name="claude:viewport-fit-sides" content="cover">',
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap">',
             css, """<style>
.typ { background: var(--paper); border: 1px solid var(--line); border-radius: 10px; padding: 14px 18px; display: grid; gap: 8px; }
.typ h2 { font: 600 19px/1.2 var(--f-display); margin: 0; }
.ex { display: grid; grid-template-columns: 6.5em minmax(0, 1fr); gap: 2px 14px; padding: 8px 0; border-top: 1px solid var(--line); text-decoration: none; color: var(--ink); }
.ex:hover b { color: var(--accent); }
.ex .t { font: 600 13px/1.4 var(--f-mono); color: var(--accent); }
.ex .th { grid-column: 2; font-size: 13px; color: var(--muted); }
.ex.missing { opacity: .55; }
</style>""", '<div class="wrap"><header><div class="eyebrow">Patentanwaltsprüfung · schriftlich · II/2018 bis III/2023</div>',
             '<h1>Klausurlösungen in Lösungssprache</h1><p class="lede">Je Klausur Aufgabe und Lösung nebeneinander: Anspruchsgrundlage, Voraussetzungen mit Norm und Definition, Subsumtion, Ergebnis; Fristen mit Berechnung und Verschiebung. Normen und Entscheidungen automatisch gegen die Korpora geprüft.</p>',
             '<div class="legend">%d von %d Klausuren gelöst</div></header>' % (len(rows), len(exams))]
    for t, name in TYPEN.items():
        parts.append('<section class="typ"><h2>%s · %s</h2>' % (t, name))
        for eid in sorted((e for e in exams if exams[e]["typ"] == t), key=lambda e: (exams[e]["jahr"], len(exams[e]["termin"]))):
            ex = exams[eid]
            label = "%s/%s" % (ex["termin"], ex["jahr"])
            if eid in have:
                r = have[eid]
                parts.append('<a class="ex" href="k/%s.html"><span class="t">%s</span><b>%s</b><span class="th">%s</span></a>'
                             % (eid, label, html.escape(r[4]), html.escape(r[5])))
            else:
                parts.append('<div class="ex missing"><span class="t">%s</span><span>noch keine Lösung</span></div>' % label)
        parts.append("</section>")
    parts.append("</div>")
    return "\n".join(parts)


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("check", "render"):
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == "check":
        files = sorted(str(p) for p in LOE.glob("*/PAP-*.json")) if "--alle" in sys.argv else sys.argv[2:]
        sys.exit(1 if check(files) else 0)
    render(sys.argv[2] if len(sys.argv) > 2 else LOE / "site")
