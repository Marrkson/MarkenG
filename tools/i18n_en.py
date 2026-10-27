#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Englische Fassung des EPG-Pakets pflegen (src/knowledge/upc/en/, PLAYBOOK Abschnitt 17).

  python3 tools/i18n_en.py status            fehlende, veraltete, überzählige und formfehlerhafte Einträge je Datei
  python3 tools/i18n_en.py export DIR [--nur-offen]
                                            deutsche Quelltexte je Übersetzungsdatei nach DIR/<datei>.json (mit `_de`-Hash);
                                            --nur-offen: nur fehlende und veraltete Einträge
  python3 tools/i18n_en.py check DATEI       eine Übersetzungsdatei prüfen (Form, Vollständigkeit, englische Zitate mit Link)
  python3 tools/i18n_en.py stamp DATEI …     `_de` der genannten Einträge (datei:schlüssel) auf den aktuellen deutschen Stand setzen,
                                            nachdem die englische Fassung geprüft und angepasst wurde; `stamp --alle` für alle
Der Graph muss gebaut sein (python3 build.py oder src/build_graph.py).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from knowledge.kurse import KURSE  # noqa: E402
from knowledge.upc import en  # noqa: E402

GRAPH = ROOT / "graph" / "markenrecht_graph.json"


def main():
    args = sys.argv[1:]
    cmd = args[0] if args else "status"
    src = en.quellen(KURSE, json.loads(GRAPH.read_text(encoding="utf-8")))
    tr = en.laden()
    fehlt, alt, extra, form = en.pruefen(src, tr)
    if cmd == "status":
        for datei in sorted(src):
            n = len(src[datei])
            f = sum(1 for x in fehlt if x.startswith(datei + ":"))
            a = sum(1 for x in alt if x.startswith(datei + ":"))
            print("%-26s %4d Einträge, %4d fehlen, %3d veraltet" % (datei, n, f, a))
        for title, lst in (("Formfehler", form), ("Veraltet", alt), ("Überzählig", extra)):
            if lst:
                print("\n%s (%d):\n  %s" % (title, len(lst), "\n  ".join(lst[:60])))
        sys.exit(1 if fehlt or form else 0)
    if cmd == "export":
        out = Path(args[1])
        out.mkdir(parents=True, exist_ok=True)
        offen = set(fehlt) | set(alt)
        for datei, entries in src.items():
            if "--nur-offen" in args:
                entries = {k: v for k, v in entries.items() if "%s: %s" % (datei, k) in offen}
            if entries:
                (out / (datei + ".json")).write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
                print(out / (datei + ".json"), len(entries))
        return
    if cmd == "check":
        # eine Datei prüfen: Vollständigkeit, Form, Zitate (jedes Zitat mit Gesetz und Link, wie lawify in der App)
        from knowledge.gesetze import resolve, href_for, ALIASES
        datei = Path(args[1]).stem
        probs = [x for x in fehlt + form if x.startswith(datei + ":")] + [x for x in extra if x.startswith(datei + ":")]
        for key, e in tr.get(datei, {}).items():
            # Hinweise an Normen: Kontextgesetz ist die Norm selbst (wie hinweisLaw in der App)
            ctx = ALIASES.get(en.FAM_EN[key.split(":")[1]]["kurz"], en.FAM_EN[key.split(":")[1]]["kurz"]) if key.startswith("eunorm:") else None

            def walk(v, f):
                if isinstance(v, str):
                    for m, law, how in resolve(v, ctx):
                        if not law or href_for(m, law) is None:
                            probs.append("%s: %s.%s: Zitat ohne Gesetz/Link: %r …%s…" % (datei, key, f, m.group(0), v[max(0, m.start() - 40):m.end() + 20]))
                    if re.search(r"\b(?:EPGÜ|VerfO|EPatVO|EPatÜVO|DOEPS|GebOEPS|DurchsetzungsRL|EPÜ|Abs\.|lit\.)", v):
                        probs.append("%s: %s.%s: deutsche Zitierform: …%s…" % (datei, key, f, v[:80]))
                elif isinstance(v, list):
                    for x in v:
                        walk(x, f)
            for f, v in e.items():
                if f != "_de":
                    walk(v, f)
        print("\n".join(probs) or "%s: in Ordnung (%d Einträge)" % (datei, len(tr.get(datei, {}))))
        sys.exit(1 if probs else 0)
    if cmd == "stamp":
        ziel = None if "--alle" in args else {a for a in args[1:]}
        for datei, entries in tr.items():
            changed = 0
            for key, e in entries.items():
                de = src.get(datei, {}).get(key)
                if de and e.get("_de") != de["_de"] and (ziel is None or "%s:%s" % (datei, key) in ziel):
                    e["_de"] = de["_de"]
                    changed += 1
            if changed:
                (en.HERE / (datei + ".json")).write_text(json.dumps(entries, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
                print(datei, changed, "gestempelt")
        return
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
