"""Klausuren TS/NS/RP1/RP2 (2018-II bis 2023-III) -> eine JSON je Klausurart, Bilder als PNG.

Text:   Textebene der PDFs (pdftotext -layout, je Seite).
Bilder: eingebettete Bilder ab MIN_PX (ohne DPMA-Logo, ohne einfarbige Flächen, Transparenzmaske angewandt) als
        <typ>/bilder/<id>/<id>_S<seite>_B<nr>.png; OCR mit tesseract deu+eng.
Seiten: jede Seite mit Bild oder Vektorzeichnung zusätzlich als <id>_S<seite>_seite.png (150 dpi).
Aufruf: python3 tools/klausuren_json.py klausuren <tessdata-dir mit deu/eng.traineddata> <tmp-dir>
        (deu.traineddata aus github.com/tesseract-ocr/tessdata_best)
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageStat

KL, TESS, WORK = (Path(a) for a in sys.argv[1:4])
OUT = KL / "json"
TYPEN = {
    "TS": "Technische Schutzrechte",
    "NS": "Nichttechnische Schutzrechte",
    "RP1": "Rechtspraxis 1",
    "RP2": "Rechtspraxis 2",
}
TERMINE = [(2018, "II"), (2018, "III")] + [(j, t) for j in range(2019, 2024) for t in ("I", "II", "III")]
MIN_PX = 64
# Zeichnungen als Vektorgrafik (pdfimages findet sie nicht); per SVG-Pfadanalyse gesucht, visuell bestätigt
VEKTOR = {("PAP-2022-I-TS", 9): "Figur 1 als Vektorzeichnung"}
BASE = "https://kandidatentreff.de/pdfspeicher/PAP/"
SEITE = "https://kandidatentreff.de/2018/03/patentanwaltspruefung-schriftlich/"
MONATE = r"Januar|Februar|M[äa]rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember"


def run(*cmd):
    return subprocess.run([str(c) for c in cmd], capture_output=True, text=True, check=True).stdout


def clean(t):
    t = t.replace("\f", "")
    t = re.sub(r"[ \t]+\n", "\n", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def ocr(png):
    r = subprocess.run(["tesseract", str(png), "-", "-l", "deu+eng", "--psm", "3", "--tessdata-dir", str(TESS)],
                       capture_output=True, text=True)
    t = clean(r.stdout)
    return t if len(re.findall(r"[A-Za-zÄÖÜäöüß0-9]", t)) >= 3 else ""


def bilder(pdf, page, stem, ziel):
    """Exportiert die relevanten Bilder einer Seite; gibt JSON-Einträge zurück."""
    wd = WORK / stem
    shutil.rmtree(wd, ignore_errors=True)
    wd.mkdir(parents=True)
    rows = [l.split() for l in run("pdfimages", "-f", page, "-l", page, "-list", pdf).splitlines()[2:]]
    run("pdfimages", "-f", page, "-l", page, "-png", pdf, wd / "img")
    res, gesehen = [], set()
    for i, r in enumerate(rows):
        num, typ, w, h, obj = int(r[1]), r[2], int(r[3]), int(r[4]), r[10]
        if typ != "image" or w < MIN_PX or h < MIN_PX or obj in gesehen:
            continue
        gesehen.add(obj)
        src = wd / f"img-{num:03d}.png"
        if not src.exists():
            continue
        im = Image.open(src)
        if i + 1 < len(rows) and rows[i + 1][2] == "smask":
            m = wd / f"img-{int(rows[i + 1][1]):03d}.png"
            if m.exists():
                mask = Image.open(m).convert("L").resize(im.size)
                bg = Image.new("RGB", im.size, "white")
                bg.paste(im.convert("RGB"), mask=mask)
                im = bg
        lo, hi = im.convert("L").getextrema()
        if hi - lo < 30 or ImageStat.Stat(im.convert("L")).stddev[0] < 4:  # Fläche/Linie ohne Inhalt
            continue
        tmp = wd / f"x-{num}.png"
        im.save(tmp)
        text = ocr(tmp)
        if page == 1 and "Markenamt" in text and len(text) < 60:  # DPMA-Logo auf dem Deckblatt
            continue
        nr = len(res) + 1
        name = f"{stem}_S{page:02d}_B{nr:02d}.png"
        ziel.mkdir(parents=True, exist_ok=True)
        shutil.copy(tmp, ziel / name)
        e = {"datei": str((ziel / name).relative_to(KL)), "breite": im.width, "hoehe": im.height}
        if text:
            e["ocr"] = text
            if "kalender" in text.lower() or len(re.findall(MONATE, text, re.I)) >= 3:
                e["hinweis"] = "Kalenderblatt; OCR der Tageszahlen unzuverlässig, für Fristen das Bild ansehen"
        res.append(e)
    return res


def dokument(pdf, art, kid, ziel):
    n = int(re.search(r"Pages:\s+(\d+)", run("pdfinfo", pdf)).group(1))
    stem = pdf.stem
    seiten = []
    for p in range(1, n + 1):
        s = {"seite": p, "text": clean(run("pdftotext", "-f", p, "-l", p, "-layout", pdf, "-"))}
        b = bilder(pdf, p, stem, ziel)
        if b:
            s["bilder"] = b
        vek = VEKTOR.get((stem, p))
        if vek:
            s["vektorgrafik"] = vek
        if b or vek:
            ziel.mkdir(parents=True, exist_ok=True)
            run("pdftoppm", "-q", "-r", 150, "-png", "-f", p, "-l", p, "-singlefile", pdf, ziel / f"{stem}_S{p:02d}_seite")
            s["seitenbild"] = str((ziel / f"{stem}_S{p:02d}_seite.png").relative_to(KL))
        seiten.append(s)
    return {"art": art, "datei": str(pdf.relative_to(KL)), "url": BASE + pdf.name, "seitenzahl": n, "seiten": seiten}


def kopf(text):
    m = re.search(r"Prüfungsaufgabe gem\.\s*(§[^\n]+?PatAnwAPrV)\s*\n\s*([^\n]+)", text)
    b = re.search(r"Bearbeitungszeit[^\n]*", text)
    t = re.search(r"Bestehend aus[^\n;]*", text)
    return {
        "rechtsgrundlage": m.group(1).strip() if m else None,
        "titel_deckblatt": m.group(2).strip() if m else None,
        "aufbau": t.group(0).strip() if t else None,
        "bearbeitungszeit": b.group(0).split(":", 1)[-1].strip() if b else None,
    }


OUT.mkdir(parents=True, exist_ok=True)
for typ, name in TYPEN.items():
    d = KL / typ.lower()
    shutil.rmtree(d / "bilder", ignore_errors=True)
    klausuren = []
    for jahr, termin in TERMINE:
        kid = f"PAP-{jahr}-{termin}-{typ}"
        pdf = d / f"{kid}.pdf"
        if not pdf.exists():
            print("FEHLT", pdf)
            continue
        ziel = d / "bilder" / kid
        docs = [dokument(pdf, "Aufgabe", kid, ziel)]
        anl = d / f"{kid}-Anlage.pdf"
        if anl.exists():
            docs.append(dokument(anl, "Anlage", kid, ziel))
        voll = "\n\n".join(
            s["text"] + "".join(f"\n\n[Bild {Path(b['datei']).name}, OCR]\n{b['ocr']}" for b in s.get("bilder", []) if b.get("ocr"))
            for doc in docs for s in doc["seiten"]
        )
        p1 = docs[0]["seiten"]
        klausuren.append({
            "id": kid, "jahr": jahr, "termin": termin, "typ": typ,
            **kopf(p1[0]["text"] + "\n" + (p1[1]["text"] if len(p1) > 1 else "")),
            "bilderordner": str(ziel.relative_to(KL)) if ziel.exists() else None,
            "dokumente": docs,
            "volltext": voll,
        })
        nb = sum(len(s.get("bilder", [])) for doc in docs for s in doc["seiten"])
        ns = sum("seitenbild" in s for doc in docs for s in doc["seiten"])
        print(f"{kid}: {sum(x['seitenzahl'] for x in docs)} S., {len(voll)} Zeichen, {nb} Bilder, {ns} Seitenbilder")
    out = {
        "typ": typ,
        "bezeichnung": name,
        "zeitraum": "2018-II bis 2023-III",
        "quelle": SEITE,
        "stand": "2026-11-14",
        "methode": "Text aus der Textebene der PDFs (pdftotext -layout). Eingebettete Bilder ab "
                   f"{MIN_PX} px (ohne DPMA-Logo) als PNG unter {typ.lower()}/bilder/<id>/<id>_S<seite>_B<nr>.png, "
                   "OCR mit tesseract 5 (deu+eng, tessdata_best) im Feld ocr. Jede Seite mit Bild oder Vektorzeichnung "
                   "zusätzlich als <id>_S<seite>_seite.png (150 dpi). Pfade relativ zu klausuren/. "
                   "Nur Aufgaben, keine Lösungshinweise.",
        "anzahl": len(klausuren),
        "klausuren": klausuren,
    }
    (OUT / f"klausuren_{typ.lower()}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
