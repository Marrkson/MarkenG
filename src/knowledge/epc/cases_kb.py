# -*- coding: utf-8 -*-
"""Weitere Leitentscheidungen für Kapitel des Kurses e01 (Modul _e01_b.py); Helfer und Prüfung gegen den Korpus wie cases.py."""
from .cases import eb  # noqa: F401

# J 4/91 (epc_j_4_91) steht in cases_kc.py und wird auch von _e01_b.py genutzt.
CASES = [
    eb("epc_g_11_91", "Berichtigung der Offenbarung (Parallelfall)", "G 11/91", "1992-11-19",
       "Wie G 3/89: Beschreibung, Ansprüche und Zeichnungen dürfen nach R. 139 EPÜ nur in dem Rahmen berichtigt werden, den der Fachmann den "
       "ursprünglich eingereichten Unterlagen mit seinem allgemeinen Fachwissen unmittelbar und eindeutig entnimmt. Das allgemeine Fachwissen "
       "kann mit jedem geeigneten Beweismittel belegt werden.",
       norms=["R. 139 EPÜ", "Art. 123 Abs. 2 EPÜ"], concepts=["epc_berichtigung"], tags=["Berichtigung"]),
]
