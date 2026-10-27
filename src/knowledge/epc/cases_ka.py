# -*- coding: utf-8 -*-
"""Weitere Leitentscheidungen für Kapitel des Kurses e01 (Modul _e01_a.py); Helfer und Prüfung gegen den Korpus wie cases.py."""
from .cases import eb  # noqa: F401

CASES = [
    eb("epc_j_13_14", "Teilanmeldung in falscher Sprache", "J 13/14", "2016-12-13",
       "Eine Teilanmeldung zu einer in einer Amtssprache eingereichten Anmeldung muss in deren Verfahrenssprache eingereicht werden. Wird sie in "
       "einer anderen Sprache eingereicht, lässt sich der Mangel weder durch eine Übersetzung noch durch Berichtigung nach R. 139 EPÜ oder "
       "Änderung beheben; sie wird nicht als Teilanmeldung behandelt.",
       norms=["Art. 76 Abs. 1 EPÜ", "R. 36 Abs. 2 EPÜ", "Art. 14 EPÜ"], concepts=["epc_teilanmeldung", "epc_sprachen"],
       tags=["Teilanmeldung", "Sprache"]),
    eb("epc_j_20_05", "Keine Teilanmeldung während der Aussetzung", "J 20/05", "2007-09-06",
       "Solange das Erteilungsverfahren wegen eines Vindikationsverfahrens ausgesetzt ist, kann der Anmelder keine Teilanmeldung zu dieser "
       "Anmeldung einreichen; eine solche Anmeldung wird nicht als Teilanmeldung behandelt.",
       norms=["R. 14 Abs. 1 EPÜ", "R. 36 Abs. 1 EPÜ", "Art. 76 Abs. 1 EPÜ"], concepts=["epc_vindikation", "epc_teilanmeldung"],
       tags=["Berechtigung", "Teilanmeldung"]),
    eb("epc_j_9_12", "Aussetzung ab Eingang des Nachweises", "J 9/12", "2013-06-28",
       "Die Aussetzung nach R. 14 Abs. 1 EPÜ wirkt ab dem Tag, an dem der Nachweis der Klageerhebung beim EPA eingeht, nicht erst ab der "
       "Mitteilung an den Anmelder. Eine danach, aber vor dieser Mitteilung eingereichte Teilanmeldung ist nicht als Teilanmeldung zu behandeln.",
       norms=["R. 14 Abs. 1 EPÜ", "R. 36 Abs. 1 EPÜ", "Art. 61 Abs. 1 EPÜ"], concepts=["epc_vindikation", "epc_teilanmeldung"],
       tags=["Berechtigung", "Teilanmeldung"]),
    eb("epc_g_3_92", "Neue Anmeldung des Berechtigten", "G 3/92", "1994-06-13",
       "Ist einem anderen als dem Anmelder durch rechtskräftige Entscheidung eines nationalen Gerichts der Anspruch auf Erteilung zugesprochen "
       "worden, kann er nach Art. 61 Abs. 1 lit. b EPÜ eine neue Anmeldung für dieselbe Erfindung einreichen, auch wenn die ursprüngliche "
       "Anmeldung des Nichtberechtigten nicht mehr anhängig ist.",
       norms=["Art. 61 Abs. 1 EPÜ", "Art. 61 Abs. 2 EPÜ"], concepts=["epc_vindikation"], tags=["Berechtigung"]),
]
