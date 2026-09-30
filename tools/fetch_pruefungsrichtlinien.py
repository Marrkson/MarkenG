#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Richtlinien für die Prüfung von Patentanmeldungen (Prüfungsrichtlinien) des DPMA laden und als JSON unter data/ ablegen.

Erzeugt (mitversioniert, damit `build.py` ohne Netz läuft):
  data/dpma_pruefungsrichtlinien.json   Abschnitte der Richtlinien (Nummer, Titel, Ebene, Seite, Text, Fußnoten) im amtlichen Wortlaut

Quelle ist das Formular P 2796 des DPMA (https://www.dpma.de/docs/formulare/patent/p2796.pdf). Die RheinIP-Datenbank enthält
die Richtlinien nicht (EPOLegaltext `gl` sind die Prüfungsrichtlinien des EPA), deshalb Netzabruf. Das PDF ist zweispaltig:
jede Seite wird links und rechts der Seitenmitte getrennt extrahiert (`pdftotext -layout -x/-W`, wie die Richtlinie 98/71/EG in
fetch_design.py), Seitenzahlen und Fußnotenblöcke werden abgetrennt, Silbentrennungen aufgelöst. Überschriften werden am
Inhaltsverzeichnis (Seiten 2 bis 4) erkannt; die Titel stammen von dort.

Aufruf:  python3 tools/fetch_pruefungsrichtlinien.py [--no-net]
Zwischenstand (PDF) liegt in ~/.cache/ipelico/patent/p2796.pdf; für eine neue Ausgabe die Datei löschen und ohne --no-net laufen lassen.
"""
import datetime
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path.home() / ".cache" / "ipelico" / "patent"
UA = {"User-Agent": "Mozilla/5.0 (IPelico fetch_pruefungsrichtlinien)"}
URL = "https://www.dpma.de/docs/formulare/patent/p2796.pdf"
MITTE = 298  # Seitenmitte in Punkt (A4: 595 pt)


def fetch_pdf(net):
    target = CACHE / "p2796.pdf"
    if target.exists():
        return target
    if not net:
        raise SystemExit("PDF fehlt im Cache (%s); ohne --no-net aufrufen" % target)
    CACHE.mkdir(parents=True, exist_ok=True)
    raw = urllib.request.urlopen(urllib.request.Request(URL, headers=UA), timeout=60).read()
    if not raw.startswith(b"%PDF"):
        raise SystemExit("Antwort von %s ist kein PDF" % URL)
    target.write_bytes(raw)
    return target


def _pdftotext(pdf, *args):
    return subprocess.run(["pdftotext", *args, str(pdf), "-"], check=True, capture_output=True).stdout.decode("utf-8")


def _seiten(pdf):
    m = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True).stdout.decode())
    return int(m.group(1))


def _ws(s):
    return re.sub(r"\s+", " ", s).strip()


def _join(lines):
    """Zeilen zu Fließtext: Silbentrennung am Zeilenende auflösen, Aufzählungen und Absätze (Leerzeile) erhalten."""
    out, buf = [], ""
    for ln in lines + [""]:
        ln = ln.strip()
        if not ln:
            if buf:
                out.append(buf)
                buf = ""
            continue
        if re.match(r"^(?:[a-z]\)|\d\)|•|-)(?:\s|$)", ln) and buf:
            out.append(buf)
            buf = ""
        if buf.endswith("-") and re.match(r"^[a-zäöüß]", ln) and not re.match(r"^(?:und|oder|bzw\.)\s", ln) and len(buf) > 1 and buf[-2].isalpha():
            buf = buf[:-1] + ln
        elif buf.endswith("­"):
            buf = buf[:-1] + ln
        else:
            buf = (buf + " " + ln) if buf else ln
    return [_ws(p.replace("­", "-")) for p in out if _ws(p)]


# ------------------------------------------------------------------ Inhaltsverzeichnis
def inhaltsverzeichnis(pdf):
    """[(nr, titel, seite)] aus den Seiten 2 bis 4; mehrzeilige Einträge werden bis zur Zeile mit Führungspunkten gesammelt."""
    txt = _pdftotext(pdf, "-f", "2", "-l", "4", "-layout")
    out, buf = [], ""
    for ln in txt.splitlines():
        ln = ln.strip()
        if not ln or re.fullmatch(r"\d+", ln) or ln == "Inhaltsverzeichnis":
            continue
        buf = (buf + " " + ln) if buf else ln
        m = re.match(r"^(.*?)\s*\.{4,}\s*(\d+)$", buf)
        if not m:
            continue
        kopf, seite = _ws(m.group(1)), int(m.group(2))
        n = re.match(r"^((?:\d+\.)+)\s+(.*)$", kopf)
        out.append((n.group(1).rstrip(".") if n else "", n.group(2) if n else kopf, seite))
        buf = ""
    return out


# ------------------------------------------------------------------ Text
_FN = re.compile(r"^\s*(\d{1,3})\s+(?=vgl\.|BGH\b|BPatG\b)")
_FN_TEXT = re.compile(r"^\s*(?:vgl\.|BGH\b|BPatG\b)")


def spalte(pdf, seite, x):
    """(Textzeilen, Fußnotenzeilen) einer Spalte. Der Fußnotenblock beginnt mit der ersten Zeile „<Nr.> BGH/BPatG/vgl. …“ oder,
    wenn pdftotext die Nummern abgesetzt hat, mit einer Zeile, die mit BGH/BPatG/vgl. beginnt, nach dem letzten Satzende."""
    raw = _pdftotext(pdf, "-f", str(seite), "-l", str(seite), "-layout", "-x", str(x), "-y", "0", "-W", str(MITTE), "-H", "842")
    lines = [ln.rstrip() for ln in raw.replace("\f", "").splitlines()]
    while lines and (not lines[0].strip() or re.fullmatch(r"\s*\d{1,2}\s*", lines[0])):
        lines.pop(0)  # Seitenzahl im Kopf (steht mittig und landet zerteilt in beiden Spalten)
    start = None
    for i, ln in enumerate(lines):
        if _FN.match(ln) or (_FN_TEXT.match(ln) and i and not lines[i - 1].strip()):
            start = i
            break
    text = lines if start is None else lines[:start]
    while text and not text[-1].strip():
        text.pop()  # Leerzeilen am Spaltenende sind kein Absatzende
    return text, ([] if start is None else lines[start:])


def fussnoten(lines):
    """{nr: text} aus einem Fußnotenblock."""
    out, nr = {}, None
    for ln in lines:
        m = re.match(r"^\s*(\d{1,3})\s+(.*)$", ln)
        if m and (nr is None or int(m.group(1)) > nr):
            nr = int(m.group(1))
            out[nr] = m.group(2).strip()
        elif nr is not None and ln.strip():
            out[nr] = _join([out[nr], ln])[0]
    return out


def _norm(s):
    return re.sub(r"[^a-zäöüß0-9§]", "", s.lower().replace("­", ""))


def abschnitte(pdf, toc):
    nummern = {nr: (titel, seite) for nr, titel, seite in toc if nr}
    ohne_nr = {titel: seite for nr, titel, seite in toc if not nr}
    erste = min(s for _, _, s in toc)
    letzte = ohne_nr.get("Abkürzungen", _seiten(pdf) + 1) - 1
    secs, cur, fns = [], None, {}

    def neu(nr, titel, seite):
        nonlocal cur
        cur = dict(nr=nr, titel=titel, ebene=nr.count(".") + 1 if nr else 1, seite=seite, zeilen=[])
        secs.append(cur)

    for seite in range(erste, letzte + 1):
        for x in (0, MITTE):
            lines, fn = spalte(pdf, seite, x)
            fns.update(fussnoten(fn))
            i = 0
            while i < len(lines):
                ln = lines[i].strip()
                m = re.match(r"^((?:\d+\.)+)\s+(\S.*)$", ln)
                nr = m.group(1).rstrip(".") if m else None
                if nr in nummern and not any(s["nr"] == nr for s in secs):
                    soll, kopf = _norm(nummern[nr][0]), m.group(2)
                    while _norm(kopf) != soll and soll.startswith(_norm(kopf)) and i + 1 < len(lines):
                        i += 1
                        kopf += " " + lines[i].strip()
                    neu(nr, nummern[nr][0], seite)
                elif ln in ohne_nr and ohne_nr[ln] == seite and not any(s["titel"] == ln for s in secs):
                    neu("", ln, seite)
                elif cur is not None:
                    cur["zeilen"].append(lines[i])
                i += 1
            letzte_zeile = next((z.strip() for z in reversed(cur["zeilen"]) if z.strip()), "") if cur is not None else ""
            if cur is not None and re.search(r"[.:;!?“]\s*\d{0,3}$", letzte_zeile):
                cur["zeilen"].append("")  # Absatzende am Spaltenende; sonst läuft der Satz in der nächsten Spalte weiter
    fehlend = sorted(set(nummern) - {s["nr"] for s in secs})
    if fehlend:
        raise SystemExit("Abschnitte aus dem Inhaltsverzeichnis nicht im Text gefunden: " + ", ".join(fehlend))

    # Fußnotenzeichen im Text („… zu bestimmen sind. 7“) in eckige Klammern setzen und die Fußnoten dem Abschnitt zuordnen.
    # Als Fußnotenzeichen gilt nur die nächste erwartete Nummer, nicht nach „Abs.“, „von“ usw. und nicht vor „Monaten“, „Jahren“ usw.
    erwartet = 1
    davor = re.compile(r"(?:Abs\.|Nr\.|Art\.|Satz|Nummer|Ziffer|Regel|§|§§|von|auf|bis|ab|als|nach|vom|und|oder|innerhalb|mindestens|spätestens|Klasse|\d,)$")
    danach = re.compile(r"^\s*(?:Monat|Jahr|Tag|Woche|Prozent|%|Abs\.|Nr\.|bis\s+\d|und\s+\d|\d|[A-ZÄÖÜ][A-Za-zÄÖÜäöü]*[A-Z][A-Za-z]*\b)")
    for s in secs:
        absaetze, eigene = _join(s.pop("zeilen")), []
        for k, a in enumerate(absaetze):
            def repl(m):
                nonlocal erwartet
                n = int(m.group(2))
                if n in fns and erwartet <= n <= erwartet + 2 and not davor.search(a[:m.end(1)]) and not danach.match(a[m.end(2):]):
                    erwartet = n + 1
                    eigene.append(n)
                    return "%s [%d]" % (m.group(1), n)
                return m.group(0)
            absaetze[k] = re.sub(r"(\S) (\d{1,3})(?=\s|$)", repl, a)
        s["text"] = "\n".join(absaetze)
        s["fussnoten"] = [dict(nr=n, text=fns[n]) for n in eigene]
    return secs, fns


def main():
    net = "--no-net" not in sys.argv
    pdf = fetch_pdf(net)
    toc = inhaltsverzeichnis(pdf)
    secs, fns = abschnitte(pdf, toc)
    kopf = _ws(_pdftotext(pdf, "-f", "1", "-l", "1"))
    stand = re.search(r"vom\s+(\d{1,2}\.\s*\S+\s+\d{4})", kopf)
    formular = re.search(r"P\s*2796/[\d.]+(?:\s*\(\d+\))?", kopf)
    zugeordnet = sum(len(s["fussnoten"]) for s in secs)
    out = dict(
        meta=dict(titel="Richtlinien für die Prüfung von Patentanmeldungen (Prüfungsrichtlinien)", herausgeber="Deutsches Patent- und Markenamt",
                  stand=stand.group(1) if stand else "", formular=_ws(formular.group(0)) if formular else "P 2796", quelle=URL,
                  abgerufen=datetime.date.fromtimestamp(pdf.stat().st_mtime).isoformat(), seiten=_seiten(pdf), abschnitte=len(secs),
                  fussnoten=len(fns), fussnoten_zugeordnet=zugeordnet,
                  hinweis="Amtlicher Wortlaut aus dem PDF (zweispaltig, je Spalte extrahiert); Fußnotenzeichen stehen als [n] im Text. "
                          "Verwaltungsvorschrift ohne Gesetzeskraft: bindet die Prüfungsstellen, nicht die Gerichte."),
        abschnitte=secs)
    DATA.mkdir(exist_ok=True)
    (DATA / "dpma_pruefungsrichtlinien.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("data/dpma_pruefungsrichtlinien.json: %d Abschnitte, Stand %s, %d Fußnoten (%d im Text zugeordnet)"
          % (len(secs), out["meta"]["stand"], len(fns), zugeordnet))


if __name__ == "__main__":
    main()
