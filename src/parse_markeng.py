"""Parst den Markdown-Gesetzestext des MarkenG (Spiegel von gesetze-im-internet.de
im Repository bundestag/gesetze) in eine strukturierte JSON-Datei.

Ausgabe: data/markeng.json mit einer Liste aller Paragraphen inkl. Gliederung
(Teil / Abschnitt), Überschrift, Absätzen und Volltext.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "markeng.md"
OUT = ROOT / "data" / "markeng.json"

HEADING = re.compile(r"^(#{2,4}) (.+?)\s*$")
PARA = re.compile(r"^§ (\d+[a-z]?) (.+)$")
ABSATZ = re.compile(r"^\((\d+[a-z]?)\) ")


def clean(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_absaetze(body: str):
    """Teilt den Paragraphentext in Absätze (1), (2) ... auf."""
    lines = body.split("\n")
    absaetze = []
    current = {"nr": None, "text": []}
    for line in lines:
        m = ABSATZ.match(line)
        if m:
            if current["text"]:
                absaetze.append(current)
            current = {"nr": m.group(1), "text": [line[m.end():]]}
        else:
            current["text"].append(line)
    if current["text"]:
        absaetze.append(current)
    result = []
    for a in absaetze:
        txt = clean("\n".join(a["text"]))
        if txt:
            result.append({"nr": a["nr"], "text": txt})
    return result


def parse():
    md = SRC.read_text(encoding="utf-8")
    lines = md.split("\n")
    meta = {}
    sections = []
    teil = abschnitt = None
    cur = None
    buf = []
    in_front = True

    def flush():
        nonlocal cur, buf
        if cur is not None:
            body = clean("\n".join(buf))
            cur["absaetze"] = split_absaetze(body)
            cur["text"] = body
            sections.append(cur)
        cur, buf = None, []

    for line in lines:
        m = HEADING.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2).strip()
            if title.startswith("Teil "):
                flush()
                teil = title
                abschnitt = None
                continue
            if title.startswith("Abschnitt "):
                flush()
                abschnitt = title
                continue
            pm = PARA.match(title)
            if pm:
                flush()
                in_front = False
                cur = {
                    "id": f"§ {pm.group(1)}",
                    "nummer": pm.group(1),
                    "titel": pm.group(2).strip(),
                    "teil": teil,
                    "abschnitt": abschnitt,
                }
                continue
        if in_front:
            mm = re.match(r"^(Ausfertigungsdatum|Fundstelle|Zuletzt geändert durch|Stand)$", line.strip())
            if mm:
                meta["_key"] = mm.group(1)
            elif line.startswith(":   ") and meta.get("_key"):
                meta[meta.pop("_key")] = line[4:].strip()
            continue
        if cur is not None:
            buf.append(line)
    flush()
    meta.pop("_key", None)
    out = {
        "gesetz": "Gesetz über den Schutz von Marken und sonstigen Kennzeichen (Markengesetz - MarkenG)",
        "quelle": "https://www.gesetze-im-internet.de/markeng/ (Spiegel: https://github.com/bundestag/gesetze/blob/master/m/markeng/index.md)",
        "meta": meta,
        "paragraphen": sections,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(sections)} Paragraphen -> {OUT.relative_to(ROOT)}")
    return out


if __name__ == "__main__":
    parse()
