#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rangliste der Vorschriften nach Auslegungen in der Rechtsprechung: Grundlage für die Gliederung der Normkurse.

Je Gesetz (PatG, GebrMG, DesignG, EPGÜ, VerfO) und je Paragraph/Absatz bzw. Artikel/Regel: Zahl der Entscheidungen, die die
Vorschrift auslegen (`ausgelegt`), die sie nennen (`genannt`), davon BGH bzw. EPG-Berufungsgericht, und die führenden
Entscheidungen mit Leitsatz (BGH/Berufungsgericht zuerst, dann neueste). Kapitel und Unterkapitel eines Normkurses folgen den
oberen Plätzen dieser Liste (PLAYBOOK Abschnitt 15).

Quellen: Tabelle DeCourtNorm der RheinIP-Datenbank (Absatzebene, `interpreted`) mit BghDecision/BpatgDecision; ohne Datenbank
(--no-db) die Paragraphenzählung aus data/patent_decisions.json und data/design_decisions.json. EPG: data/upc_decisions.json
(Zitatzählung je Artikel/Regel, keine Absatzebene).

Aufruf:  python3 tools/norm_ranking.py [--no-db] [--top 40]     Ausgabe: data/norm_ranking.json
"""
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "norm_ranking.json"
sys.path.insert(0, str(ROOT / "tools"))

DE_LAWS = {"PatG": "patg", "GebrMG": "gebrmg", "DesignG": "designg", "GeschmMG": "designg"}  # GeschmMG ab 2004 = DesignG (gleiche Zählung)
N_BEISPIELE = 8


def _de_db(top):
    from fetch_patent import _db_cursor
    cur = _db_cursor()
    cur.execute('''
        with n as (
          select n."decisionId" did, case when n.law = 'GeschmMG' then 'DesignG' else n.law end law, n.paragraph par, coalesce(n.absatz, '') abs,
                 bool_or(n.interpreted) i
          from "DeCourtNorm" n where n.law = any(%s) and n.paragraph is not null group by 1, 2, 3, 4),
        d as (
          select id, 'BGH' gericht, "fileNumber" az, "decisionDate" datum, "caseName" name, headnote, url from "BghDecision"
          union all
          select id, 'BPatG', "fileNumber", "decisionDate", "caseName", headnote, url from "BpatgDecision")
        select n.did, n.law, n.par, n.abs, n.i, d.gericht, d.az, d.datum, d.name, d.headnote, d.url
        from n join d on d.id = n.did''', (list(DE_LAWS),))
    stats = collections.defaultdict(lambda: dict(ausgelegt=0, genannt=0, bgh=0, beispiele=[]))
    seen = set()
    for did, law, par, abs_, interp, gericht, az, datum, name, head, url in sorted(cur.fetchall(), key=lambda r: not r[4]):
        for key in {(law, par, ""), (law, par, abs_)}:  # Paragraph gesamt und je Absatz, jede Entscheidung einmal
            if (did,) + key in seen:
                continue
            seen.add((did,) + key)
            s = stats[key]
            s["genannt"] += 1
            if interp:
                s["ausgelegt"] += 1
                s["bgh"] += gericht == "BGH"
                if head and head.strip():
                    s["beispiele"].append(dict(gericht=gericht, az=" ".join(az.split()), datum=datum.date().isoformat() if datum else None,
                                               name=" ".join((name or "").split())[:80], leitsatz=" ".join(head.split())[:400], url=url))
    out = collections.defaultdict(list)
    for (law, par, abs_), s in stats.items():
        bsp = sorted(s.pop("beispiele"), key=lambda b: (b["gericht"] != "BGH", -(int((b["datum"] or "0000")[:4]))))
        out[law].append(dict(norm=f"§ {par}" + (f" Abs. {abs_}" if abs_ else "") + f" {law}", par=par, absatz=abs_, **s, beispiele=bsp[:N_BEISPIELE]))
    return {law: sorted(v, key=lambda r: -r["ausgelegt"])[:top * 2] for law, v in out.items()}


def _de_json(top):
    out = collections.defaultdict(list)
    for f in ("patent_decisions.json", "design_decisions.json"):
        stats = collections.defaultdict(lambda: dict(ausgelegt=0, genannt=0, bgh=0, beispiele=[]))
        for e in json.loads((ROOT / "data" / f).read_text())["entscheidungen"]:
            for key, ps in (e.get("zitate") or {}).items():
                law = {v: k for k, v in DE_LAWS.items() if k != "GeschmMG"}.get(key)
                if not law:
                    continue
                for par, v in ps.items():
                    s = stats[(law, par)]
                    s["genannt"] += 1
                    if v["i"]:
                        s["ausgelegt"] += 1
                        s["bgh"] += e["gericht"] == "BGH"
                        if e.get("leitsatz"):
                            s["beispiele"].append(dict(gericht=e["gericht"], az=e["az"], datum=e["datum"], name=e.get("name", ""),
                                                       leitsatz=e["leitsatz"][:400], url=e["url"]))
        for (law, par), s in stats.items():
            bsp = sorted(s.pop("beispiele"), key=lambda b: (b["gericht"] != "BGH", -(int((b["datum"] or "0000")[:4]))))
            out[law].append(dict(norm=f"§ {par} {law}", par=par, absatz="", **s, beispiele=bsp[:N_BEISPIELE]))
    return {law: sorted(v, key=lambda r: -r["ausgelegt"])[:top] for law, v in out.items()}


def _upc(top):
    d = json.loads((ROOT / "data" / "upc_decisions.json").read_text())["entscheidungen"]
    out = {}
    for key, law, kopf in (("upca", "EPGÜ", "Art."), ("rop", "VerfO", "R.")):
        stats = collections.defaultdict(lambda: dict(ausgelegt=0, genannt=0, bgh=0, beispiele=[]))
        for e in d:
            coa = "Court of Appeal" in (e.get("division") or "")
            for nr, n in (e.get(key) or {}).items():
                s = stats[nr]
                s["genannt"] += 1
                s["ausgelegt"] += n >= 3  # mehrfach zitiert ≈ erörtert (die EPG-Daten kennen kein `interpreted`)
                s["bgh"] += coa
                if e.get("headnote"):
                    s["beispiele"].append(dict(gericht="EPG-BerG" if coa else e.get("division", ""), az=e["docket"], datum=e["date"], name=f"{e.get('claimant', '')}/{e.get('respondent', '')}"[:80],
                                               leitsatz=" ".join(e["headnote"].split())[:400], url=e["url"], n=n))
        rows = []
        for nr, s in stats.items():
            bsp = sorted(s.pop("beispiele"), key=lambda b: (b["gericht"] != "EPG-BerG", -b["n"], b["datum"] or ""))
            rows.append(dict(norm=f"{kopf} {nr} {law}", par=nr, absatz="", **s, beispiele=bsp[:N_BEISPIELE]))
        out[law] = sorted(rows, key=lambda r: (-r["genannt"]))[:top]
    return out


def main():
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 40
    de = _de_json(top) if "--no-db" in sys.argv else _de_db(top)
    data = dict(meta=dict(hinweis="ausgelegt = Entscheidungen, die die Vorschrift auslegen (DeCourtNorm.interpreted; EPG: mindestens dreimal zitiert); "
                                  "bgh = davon BGH bzw. EPG-Berufungsgericht", quelle="RheinIP-Datenbank" if "--no-db" not in sys.argv else "data/*_decisions.json"),
                **de, **_upc(top))
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    for law in ("PatG", "GebrMG", "DesignG", "EPGÜ", "VerfO"):
        print(f"{law:8} " + ", ".join(f"{r['norm'].rsplit(' ', 1)[0]} ({r['ausgelegt']})" for r in data.get(law, [])[:15]))
    print(f"-> {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
