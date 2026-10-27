# -*- coding: utf-8 -*-
"""Fallbasierte Kurse zum MarkenG im Stil einer Microlearning-App.

Struktur: Rechtsgebiet (gebiete.py) -> Kurs -> Kapitel -> Lerneinheiten.
Einheitentypen:
  intro       Einführung/Systematik (kein Quiz)
  schema      Prüfungsschema aus dem Graphen (kein Quiz)
  fall        Mini-Fall mit Ja/Nein-Frage
  mc          Multiple Choice (eine richtige Option)
Fallketten (`_helpers.fallkette`) sind Folgen von fall/mc-Einheiten mit gemeinsamem Sachverhalt (`gruppe`).
Kurse mit `kompakt=True` und alle Fallketten unterliegen den Längengrenzen in LIMITS (Jurafuchs-Maß: in einer Minute
gelesen); der Import bricht ab, wenn eine Einheit sie überschreitet. `kompakt="fragen"` (EPG-Kurse) begrenzt nur die Fragen,
nicht die Einführungen.
Jede Einheit verweist auf Begriffe, Normen, Entscheidungen und ggf. einen Prüfungspunkt des Graphen.
"""
from . import k01_grundlagen, k02_schutzfaehigkeit, k03_verletzung, k04_verwechslung, k05_bekanntheit
from . import k06_schranken, k07_benutzung_loeschung, k08_bezeichnungen, k09_rechtsfolgen, k10_eu_ir, k11_markenrl
from . import k12_klausurtraining, k13_zulaessigkeit, k14_durchsetzungsrl
from . import p00_technische_schutzrechte, p01_klausurtraining_ts, p02_pruefungsrichtlinien  # Patentrecht: Grundkurs, Klausurtraining TS, Prüfungsrichtlinien
from .gebiete import GEBIETE, GEBIET_IDS  # noqa: F401
import importlib as _importlib
import re as _re
import pkgutil as _pkgutil

KURSE = [m.KURS for m in (k01_grundlagen, k02_schutzfaehigkeit, k03_verletzung, k04_verwechslung, k05_bekanntheit,
                          k06_schranken, k07_benutzung_loeschung, k08_bezeichnungen, k09_rechtsfolgen, k10_eu_ir, k11_markenrl,
                          k14_durchsetzungsrl, k12_klausurtraining, k13_zulaessigkeit, p00_technische_schutzrechte, p02_pruefungsrichtlinien, p01_klausurtraining_ts)]

# Kurse zum Einheitlichen Patentgericht (u01_*.py …), zum Designrecht (d01_*.py …) und weitere Patentkurse (p03_*.py …) werden
# automatisch eingesammelt (Reihenfolge nach Kurs-ID).
_AUTO = [_importlib.import_module(f"{__name__}.{m.name}").KURS for m in _pkgutil.iter_modules(__path__)
         if m.name[:1] in ("u", "d", "p") and m.name[1:3].isdigit() and int(m.name[1:3]) >= (3 if m.name[0] == "p" else 0)]
KURSE += sorted(_AUTO, key=lambda k: k["id"])
_ids = [k["id"] for k in KURSE]
if len(_ids) != len(set(_ids)):
    raise SystemExit("doppelte Kurs-IDs: " + ", ".join(sorted({i for i in _ids if _ids.count(i) > 1})))

for _k in KURSE:
    if _k.get("gebiet") not in GEBIET_IDS:
        raise SystemExit(f"Kurs {_k['id']}: gebiet={_k.get('gebiet')!r} ist nicht in kurse/gebiete.py registriert")


# Längengrenzen in Wörtern (Fallketten und Kurse mit kompakt=True)
LIMITS = dict(sachverhalt=70, frage=35, loesung=90, abwandlung=35, option=30, intro=130, merke=30)


def _w(s):
    return len(_re.findall(r"\w+", s or ""))


def _laengen():
    fehler = []
    for k in KURSE:
        for kap in k["kapitel"]:
            for e in kap["einheiten"]:
                if not (k.get("kompakt") or e.get("gruppe")):
                    continue
                n = dict(sachverhalt=_w(e["gruppe"]["sachverhalt"] if e.get("gruppe") else e.get("sachverhalt")), frage=_w(e.get("frage")),
                         loesung=sum(_w(x) for x in e.get("loesung", [])), abwandlung=_w(e.get("abwandlung")), merke=_w(e.get("merke")),
                         option=max([_w(o) for o in e.get("optionen", [])] or [0]),
                         intro=_w(e.get("text")) if e["typ"] in ("intro", "schema") and k.get("kompakt") is True else 0)
                fehler += [f"{e['id']}: {f} {v} Wörter (max. {LIMITS[f]})" for f, v in n.items() if v > LIMITS[f]]
    if fehler:
        raise SystemExit("Einheiten zu lang:\n  " + "\n  ".join(fehler))


_laengen()


def alle_einheiten():
    for k in KURSE:
        for kap in k["kapitel"]:
            for e in kap["einheiten"]:
                yield k, kap, e
