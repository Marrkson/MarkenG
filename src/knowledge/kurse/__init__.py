# -*- coding: utf-8 -*-
"""Fallbasierte Kurse zum MarkenG im Stil einer Microlearning-App.

Struktur: Rechtsgebiet (gebiete.py) -> Kurs -> Kapitel -> Lerneinheiten.
Einheitentypen:
  intro       Einführung/Systematik (kein Quiz)
  schema      Prüfungsschema aus dem Graphen (kein Quiz)
  fall        Mini-Fall mit Ja/Nein-Frage
  mc          Multiple Choice (eine richtige Option)
Jede Einheit verweist auf Begriffe, Normen, Entscheidungen und ggf. einen Prüfungspunkt des Graphen.
"""
from . import k01_grundlagen, k02_schutzfaehigkeit, k03_verletzung, k04_verwechslung, k05_bekanntheit
from . import k06_schranken, k07_benutzung_loeschung, k08_bezeichnungen, k09_rechtsfolgen, k10_eu_ir, k11_markenrl
from . import k12_klausurtraining, k13_zulaessigkeit, k14_durchsetzungsrl
from .gebiete import GEBIETE, GEBIET_IDS  # noqa: F401
import importlib as _importlib
import pkgutil as _pkgutil

KURSE = [m.KURS for m in (k01_grundlagen, k02_schutzfaehigkeit, k03_verletzung, k04_verwechslung, k05_bekanntheit,
                          k06_schranken, k07_benutzung_loeschung, k08_bezeichnungen, k09_rechtsfolgen, k10_eu_ir, k11_markenrl,
                          k14_durchsetzungsrl, k12_klausurtraining, k13_zulaessigkeit)]

# Kurse zum Einheitlichen Patentgericht: Module u01_*.py … werden automatisch eingesammelt (Reihenfolge nach Kurs-ID).
_UPC = [_importlib.import_module(f"{__name__}.{m.name}").KURS for m in _pkgutil.iter_modules(__path__) if m.name[:1] == "u" and m.name[1:3].isdigit()]
KURSE += sorted(_UPC, key=lambda k: k["id"])
_ids = [k["id"] for k in KURSE]
if len(_ids) != len(set(_ids)):
    raise SystemExit("doppelte Kurs-IDs: " + ", ".join(sorted({i for i in _ids if _ids.count(i) > 1})))

for _k in KURSE:
    if _k.get("gebiet") not in GEBIET_IDS:
        raise SystemExit(f"Kurs {_k['id']}: gebiet={_k.get('gebiet')!r} ist nicht in kurse/gebiete.py registriert")


def alle_einheiten():
    for k in KURSE:
        for kap in k["kapitel"]:
            for e in kap["einheiten"]:
                yield k, kap, e
