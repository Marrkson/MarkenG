# -*- coding: utf-8 -*-
"""Fallbasierte Kurse zum MarkenG im Stil einer Microlearning-App.

Struktur: Kurs -> Kapitel -> Lerneinheiten.
Einheitentypen:
  intro       Einführung/Systematik (kein Quiz)
  schema      Prüfungsschema aus dem Graphen (kein Quiz)
  fall        Mini-Fall mit Ja/Nein-Frage
  mc          Multiple Choice (eine richtige Option)
Jede Einheit verweist auf Begriffe, Normen, Entscheidungen und ggf. einen Prüfungspunkt des Graphen.
"""
from . import k01_grundlagen, k02_schutzfaehigkeit, k03_verletzung, k04_verwechslung, k05_bekanntheit
from . import k06_schranken, k07_benutzung_loeschung, k08_bezeichnungen, k09_rechtsfolgen, k10_eu_ir, k11_markenrl

KURSE = [m.KURS for m in (k01_grundlagen, k02_schutzfaehigkeit, k03_verletzung, k04_verwechslung, k05_bekanntheit,
                          k06_schranken, k07_benutzung_loeschung, k08_bezeichnungen, k09_rechtsfolgen, k10_eu_ir, k11_markenrl)]


def alle_einheiten():
    for k in KURSE:
        for kap in k["kapitel"]:
            for e in kap["einheiten"]:
                yield k, kap, e
