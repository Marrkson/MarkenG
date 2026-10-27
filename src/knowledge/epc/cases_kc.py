# -*- coding: utf-8 -*-
"""Weitere Leitentscheidungen für Kapitel des Kurses e01 (Modul _e01_c.py); Helfer und Prüfung gegen den Korpus wie cases.py."""
from .cases import eb  # noqa: F401

CASES = [
    eb("epc_g_12_91", "Abschluss des schriftlichen Verfahrens", "G 12/91", "1993-12-17",
       "Im schriftlichen Verfahren ist das Verfahren zum Erlass einer Entscheidung mit dem Tag abgeschlossen, an dem die Formalprüfungsstelle "
       "die Entscheidung an die interne Poststelle des EPA zur Zustellung abgibt. Bis dahin kann das Organ Eingaben der Beteiligten noch berücksichtigen.",
       norms=["Art. 97 Abs. 1 EPÜ", "R. 71a Abs. 2 EPÜ"], concepts=["epc_erteilung", "epc_pruefungsverfahren"], tags=["Prüfung", "Erteilung"]),
    eb("epc_t_210_89", "Keine Wiedereinsetzung des Einsprechenden in die Beschwerdefrist", "T 210/89", "1989-10-20",
       "Ein Einsprechender, der die Frist zur Einlegung der Beschwerde versäumt hat, kann nicht nach Art. 122 EPÜ in den vorigen Stand eingesetzt "
       "werden. Anders liegt es nur, wenn er Beschwerde eingelegt, aber die Begründungsfrist versäumt hat (G 1/86).",
       norms=["Art. 122 Abs. 1 EPÜ", "Art. 108 EPÜ"], concepts=["epc_wiedereinsetzung", "epc_beschwerde"], tags=["Wiedereinsetzung", "Beschwerde"]),
    eb("epc_t_1095_06", "Eigenes Versäumnis des Vertreters", "T 1095/06", "2008-05-07",
       "Die Rechtsprechung zum isolierten Versehen in einem sonst zuverlässigen Fristensystem hilft nicht über ein eigenes Versäumnis des "
       "zugelassenen Vertreters hinweg, wenn keine besonderen Umstände vorliegen. Die Bedeutung der Anmeldung für den Anmelder spricht nicht für die Wiedereinsetzung.",
       norms=["Art. 122 Abs. 1 EPÜ"], concepts=["epc_wiedereinsetzung", "epc_vertretung"], tags=["Wiedereinsetzung"]),
    eb("epc_j_4_91", "Nachfrist für Jahresgebühren von Monatsende zu Monatsende", "J 4/91", "1991-10-22",
       "Die Sechsmonatsfrist zur Zahlung einer Jahresgebühr mit Zuschlag endet am letzten Tag des sechsten Monats nach Fälligkeit. Sie beginnt am "
       "Fälligkeitstag auch dann, wenn das EPA an diesem Tag geschlossen ist; eine Verlängerung des Fälligkeitstags verschiebt ihr Ende nicht.",
       norms=["R. 51 Abs. 2 EPÜ", "R. 134 Abs. 1 EPÜ"], concepts=["epc_jahresgebuehren", "epc_fristen"], tags=["Jahresgebühren", "Fristen"]),
]
