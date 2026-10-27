# -*- coding: utf-8 -*-
"""Weitere Leitentscheidungen für Kapitel des Kurses e01 (Modul _e01_d.py); Helfer und Prüfung gegen den Korpus wie cases.py."""
from .cases import eb  # noqa: F401

CASES = [
    eb("epc_g_1_94", "Beitritt im Beschwerdeverfahren", "G 1/94", "1994-05-11",
       "Der vermeintliche Patentverletzer kann auch noch während eines anhängigen Beschwerdeverfahrens nach Art. 105 EPÜ beitreten. Er darf "
       "seinen Beitritt auf jeden Einspruchsgrund des Art. 100 EPÜ stützen, auch auf einen, den der Einsprechende nicht geltend gemacht hat.",
       norms=["Art. 105 EPÜ", "Art. 100 EPÜ"], concepts=["epc_beitritt"], tags=["Einspruch", "Beschwerde"]),
    eb("epc_g_8_93", "Rücknahme des Einspruchs in der Beschwerde", "G 8/93", "1994-06-13",
       "Nimmt der Einsprechende, der einziger Beschwerdeführer ist, seinen Einspruch zurück, endet das Beschwerdeverfahren sofort. Auf die "
       "Zustimmung des Patentinhabers oder die Meinung der Kammer zur Rechtsbeständigkeit des Patents kommt es nicht an.",
       norms=["Art. 107 EPÜ", "R. 84 Abs. 2 EPÜ"], concepts=["epc_beschwerde", "epc_einsprechendenstellung"], tags=["Einspruch", "Beschwerde"]),
    eb("epc_t_1178_04", "Prüfung der Einsprechendenstellung von Amts wegen", "T 1178/04", "2007-02-27",
       "Das EPA prüft die Stellung als Einsprechender in jedem Verfahrensstadium von Amts wegen. Das gilt auch für die Wirksamkeit einer "
       "behaupteten Übertragung des Einspruchs auf einen neuen Beteiligten.",
       norms=["Art. 99 EPÜ"], concepts=["epc_einsprechendenstellung"], tags=["Einspruch"]),
]
