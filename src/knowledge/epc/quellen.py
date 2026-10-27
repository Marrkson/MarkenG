# -*- coding: utf-8 -*-
"""Richtlinien für die Prüfung im EPA (Ausgabe März 2026) als `source`-Knoten der EPÜ-Begriffe (`quellen=["epagl:e_viii_2"]`).

Quelle: data/epc_guidelines.json (EPOLegaltext, type gl, englische Fassung). Die Datenbank enthält die Richtlinien nur auf Englisch;
deshalb tragen die Knoten einen deutschen Titel (TITEL unten, Hand) und als Zusammenfassung die Randverweise und die zitierten
Entscheidungen des Abschnitts, verlinkt auf die deutsche Seite epo.org/de/legal/guidelines-epc/2026/<id>.html. Die englische App
setzt Titel und Zusammenfassung aus dem englischen Original (`titel_en`, `summary_en`), eine Übersetzung ist nicht nötig.
Jede Vorschrift (texte.py) listet daneben selbst die Abschnitte, die sie zitieren (`gl`).
"""
import re

from .concepts import CONCEPTS
from .texte import GL_BY_ID, GL_META

PROVIDER = "EPA-Richtlinien"
STAND = "Richtlinien für die Prüfung im EPA, Ausgabe März 2026"

TITEL = {
    "a_ii_4_1": "Mindesterfordernisse für die Zuerkennung eines Anmeldetags", "a_ii_5": "Nachreichen fehlender Zeichnungen oder Teile der Beschreibung",
    "a_ii_6": "Berichtigung fälschlich eingereichter Anmeldungsunterlagen", "a_iii_6": "Prioritätsanspruch", "a_iii_6_6": "Prioritätsfrist",
    "a_iii_12": "Erstreckung und Validierung", "a_iv_1": "Europäische Teilanmeldungen", "a_iv_1_1": "Teilanmeldungen: Allgemeines (Anhängigkeit)",
    "a_iv_1_2": "Anmeldetag und Priorität der Teilanmeldung", "a_iv_1_3": "Einreichung einer Teilanmeldung",
    "a_iv_2_2": "Aussetzung des Erteilungsverfahrens", "a_iv_2_4": "Weiterverfolgung der Anmeldung durch einen Dritten",
    "a_v_3": "Berichtigung von Fehlern in eingereichten Unterlagen", "a_vi_2_2": "Frist für den Prüfungsantrag", "a_vi_2_5": "Rückerstattung der Prüfungsgebühr",
    "a_vii_1": "Zulässige Sprachen bei Einreichung", "a_vii_2": "Verfahrenssprache", "a_vii_3_2": "Zugelassene Nichtamtssprachen",
    "a_viii_1": "Vertretung", "a_viii_1_2": "Vertretung durch zugelassene Vertreter", "a_x_2": "Zahlungsarten", "a_x_4": "Tag der Zahlung",
    "a_x_5_2_4": "Fälligkeit der Jahresgebühren", "a_x_9": "Gebührenermäßigungen", "a_x_9_3": "Ermäßigung nach der Sprachenregelung",
    "a_x_10": "Rückerstattung von Gebühren", "b_vi_5_5": "Unschädliche Offenbarungen", "b_vii_2": "Verfahren bei mangelnder Einheitlichkeit",
    "b_vii_2_3": "Ergänzende europäische Recherche bei Uneinheitlichkeit", "c_ii_1_2": "Euro-PCT-Anmeldungen: Prüfungsantrag",
    "c_iii_3": "Einheitlichkeit in der Prüfung", "c_ix_1": "Teilanmeldungen in der Prüfung", "c_ix_2_3": "Teilweise Berechtigung",
    "c_v_2": "Einverständnis mit der Fassung – Erteilung", "c_v_2_1": "Antrag auf einheitliche Wirkung", "c_v_4": "Änderungen oder Berichtigungen nach R. 71 Abs. 3 EPÜ",
    "c_v_8": "Weiterbehandlung im Erteilungsstadium", "c_vi_1": "Fristen für Erwiderungen auf Bescheide", "d_i_4": "Einspruchsberechtigung",
    "d_i_5": "Beitritt des vermeintlichen Patentverletzers", "d_i_6": "Beteiligte am Einspruchsverfahren", "d_iii_1": "Einspruchsfrist",
    "d_iii_5": "Einspruchsgründe", "d_iii_6": "Inhalt der Einspruchsschrift", "d_v_2_2": "Prüfung der Einspruchsgründe",
    "d_vii_5": "Fortsetzung des Einspruchsverfahrens (R. 84 EPÜ)", "d_vii_6": "Beitritt im Einspruchsverfahren",
    "d_x": "Beschränkungs- und Widerrufsverfahren", "d_x_4": "Sachprüfung im Beschränkungsverfahren", "d_x_7_1": "Vorrang des Einspruchsverfahrens",
    "e_ii_2_3": "Elektronische Zustellung", "e_ii_2_4": "Zustellung durch Postdienste", "e_vi_3": "Einwendungen Dritter",
    "e_viii_1_4": "Fristberechnung", "e_viii_1_6": "Fristverlängerung", "e_viii_1_9": "Rechtsverlust", "e_viii_2": "Weiterbehandlung",
    "e_viii_3": "Wiedereinsetzung in den vorigen Stand", "e_viii_3_1": "Zulässigkeit des Wiedereinsetzungsantrags", "e_viii_3_2": "Begründetheit des Wiedereinsetzungsantrags",
    "e_xi_5": "Beschwerdeberechtigte und Beteiligte", "e_xi_6": "Frist und Form der Beschwerde", "e_xi_7": "Abhilfe",
    "f_iv_4": "Klarheit und Auslegung der Ansprüche", "f_vi_1": "Prioritätsrecht", "f_vi_2_4": "Beispiele zur Bestimmung des Prioritätstags",
    "g_iv_1": "Stand der Technik: Begriff", "g_iv_3": "Anmeldetag oder Prioritätstag als maßgeblicher Tag", "g_iv_5": "Kollision mit älteren europäischen Anmeldungen",
    "g_iv_5_1": "Stand der Technik nach Art. 54 Abs. 3 EPÜ", "g_iv_5_2": "Euro-PCT-Anmeldungen als ältere Rechte", "g_vi_6": "Prüfung der Neuheit (medizinische Verwendung)",
    "h_iv_2": "Zulässigkeit von Änderungen nach Art. 123 Abs. 2 EPÜ", "h_iv_3": "Zulässigkeit von Änderungen nach Art. 123 Abs. 3 EPÜ",
    "h_v_3": "Änderungen in den Ansprüchen", "h_v_4": "Disclaimer", "h_vi_2": "Berichtigung von Fehlern in Unterlagen",
}


def _kurz(liste, n=8):
    return ", ".join(liste[:n]) + (" …" if len(liste) > n else "")


def _rand_de(r):
    """'Art. 90(1)' -> 'Art. 90 Abs. 1 EPÜ', 'Rule 56(4)(a)' -> 'R. 56 Abs. 4 lit. a EPÜ', 'Art. 11 RFees' -> 'Art. 11 GebO'."""
    m = re.match(r"^(Art\.|Article|Rules?|R\.)\s*(\d+[a-z]?)((?:\(\w+\))*)(.*)$", r)
    if not m:
        return r
    head = "Art." if m.group(1).startswith("Art") else "R."
    parts = re.findall(r"\((\w+)\)", m.group(3))
    sub = "".join((" Abs. " if x[0].isdigit() else " lit. ") + x for x in parts[:2])
    law = "GebO" if "RFees" in m.group(4) else ("PCT" if "PCT" in m.group(4) else "EPÜ")
    return f"{head} {m.group(2)}{sub} {law}"


def _rand_en(r):
    m = re.match(r"^(Art\.|Article|Rules?|R\.)\s*(\d+[a-z]?)((?:\(\w+\))*)(.*)$", r)
    if not m:
        return r
    head = "Art." if m.group(1).startswith("Art") else "R."
    law = "RFees" if "RFees" in m.group(4) else ("PCT" if "PCT" in m.group(4) else "EPC")
    return f"{head} {m.group(2)}{m.group(3)} {law}"


def _knoten(gid):
    g = GL_BY_ID.get(gid)
    if g is None:
        raise SystemExit(f"epc/quellen.py: Richtlinienabschnitt {gid} nicht in data/epc_guidelines.json")
    if gid not in TITEL:
        raise SystemExit(f"epc/quellen.py: deutscher Titel für {gid} ({g['ref']}) fehlt in TITEL")
    titel_en = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", g["titel"]).strip()
    rand = [_rand_de(r) for r in g["rand"]]
    teile = []
    if rand:
        teile.append("Rechtsgrundlagen am Rand: " + _kurz(rand))
    if g["entscheidungen"]:
        teile.append("zitierte Entscheidungen: " + _kurz(g["entscheidungen"]))
    teile_en = []
    if g["rand"]:
        teile_en.append("Legal basis in the margin: " + _kurz([_rand_en(r) for r in g["rand"]]))
    if g["entscheidungen"]:
        teile_en.append("decisions cited: " + _kurz(g["entscheidungen"]))
    return dict(page="epagl:" + gid, title=f"Richtlinien {g['ref']}: {TITEL[gid]}", title_en=f"Guidelines {g['ref']}: {titel_en}",
                summary=("; ".join(teile) + ". " if teile else "") + STAND + ".",
                summary_en=("; ".join(teile_en) + ". " if teile_en else "") + "Guidelines for Examination in the EPO, March 2026.",
                url=g["url_de"], url_en=g["url"], provider=PROVIDER)


_IDS = list(dict.fromkeys(q.split(":", 1)[1] for c in CONCEPTS for q in c["quellen"] if q.startswith("epagl:")))
QUELLEN = [_knoten(g) for g in _IDS]
URL = GL_META["url"]
