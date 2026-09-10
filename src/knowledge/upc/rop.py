# -*- coding: utf-8 -*-
"""Verfahrensordnung des Einheitlichen Patentgerichts (VerfO, engl. Rules of Procedure, RoP).

Wortlaut aus data/upc_rop.json (deutsche konsolidierte Fassung, englische Regeltitel). Jede Regel
kennt ihren „Bezug zum Übereinkommen“ (Kante `konkretisiert` -> EPGÜ-Artikel). Präambel als
Sammelknoten (Nr. 0), weil die Grundsätze (Verhältnismäßigkeit, Fairness, front-loaded, Nr. 7)
in der Rechtsprechung des Berufungsgerichts ständig zitiert werden.
"""
import json
import re
from pathlib import Path

from .upca import schoen

KURZ = "VerfO"
ALIASE = ("RoP",)
TITEL = "Verfahrensordnung des Einheitlichen Patentgerichts (VerfO)"
GESETZ = "Verfahrensordnung des EPG (Beschluss des Verwaltungsausschusses vom 8.7.2022, geändert am 4.11.2025)"
_DATA = Path(__file__).resolve().parents[3] / "data" / "upc_rop.json"

HINWEISE = {
    "5": "Opt-out: Antrag beim Kanzler für alle Inhaber, wirksam mit Eintragung; unwirksam, wenn bereits Klage beim EPG anhängig war (R. 5.6); Rücknahme nur, wenn noch keine nationale Klage (R. 5.8).",
    "9": "Fallmanagement-Generalklausel: Fristverlängerung (Abs. 3) nur ausnahmsweise; das Gericht kann Vorbringen als unbeachtlich behandeln (Abs. 2).",
    "13": "Klageschrift: Inhalt lit. a bis q, insbesondere Kammerwahl (i), Angriffsmerkmale (m), Beweismittel (n); Anlagen sind gleichzeitig hochzuladen (R. 13.2).",
    "19": "Einspruch (Preliminary objection) binnen eines Monats; abschließender Katalog (Zuständigkeit, Kammer, Sprache); Versäumnis = Anerkennung (Abs. 7).",
    "23": "Klageerwiderung drei Monate nach Zustellung; ist die Nichtigkeit einzuwenden, muss die Widerklage darin enthalten sein (R. 25).",
    "30": "Änderung des Patents: Hilfsanträge in angemessener Zahl (Abs. 1 lit. c); spätere Änderungen nur mit Erlaubnis (Abs. 2).",
    "37": "Entscheidung der Lokalkammer über die drei Optionen des Art. 33 Abs. 3 EPGÜ nach Abschluss des schriftlichen Verfahrens.",
    "118": "Entscheidung in der Sache: Anordnungen, Zwangsgeld, Sicherheitsleistung, Aussetzung bei parallelem EPA-Verfahren (Abs. 2), Vollstreckbarkeit (Abs. 8).",
    "150": "Kostenentscheidung als gesondertes Verfahren nach der Hauptsacheentscheidung; Antrag binnen eines Monats (R. 151).",
    "158": "Prozesskostensicherheit: Gefährdung der Erstattung oder Vollstreckungsschwierigkeiten; Beweislast beim Antragsteller (EPG-BerG Aarke/SodaStream).",
    "190": "Beweisvorlage nach Art. 59 EPGÜ für substantiierte, bestrittene Tatsachen; keine Ausforschung.",
    "192": "Antrag auf Beweissicherung: Angaben, Beweismittel, Offenlegungspflicht bei ex parte (Abs. 3, EPG-BerG Ecovacs/Roborock).",
    "206": "Antrag auf einstweilige Maßnahmen: Angaben zu Rechtsbestand, Verletzung, Dringlichkeit; Schutzschrift nach R. 207 ist zu berücksichtigen.",
    "207": "Schutzschrift: sechs Monate wirksam, verlängerbar; wird dem Antragsteller erst nach Antragstellung mitgeteilt.",
    "209": "Verfahrensgang bei einstweiligen Maßnahmen: Anhörung des Gegners oder ex parte (Abs. 1 lit. c), Prüfung der Dringlichkeit (Abs. 2 lit. b).",
    "211": "Entscheidung: hinreichende Sicherheit (Abs. 2 – überwiegend wahrscheinlich, EPG-BerG NanoString/10x), Interessenabwägung (Abs. 3), unangemessene Verzögerung (Abs. 4), Sicherheitsleistung (Abs. 5).",
    "220": "Berufung: gegen Endentscheidungen und aufgezählte Anordnungen (Abs. 1), sonst nur mit Zulassung (Abs. 2) oder nach Ermessensüberprüfung (Abs. 3, 4).",
    "222": "Berufungsgegenstand: neue Tatsachen und Beweismittel nur ausnahmsweise (Abs. 2); Ermessen des Berufungsgerichts.",
    "223": "Aufschiebende Wirkung nur auf Antrag und bei außergewöhnlichen Umständen; Antrag muss vollständig sein (EPG-BerG Amycel).",
    "224": "Berufungsfrist: zwei Monate (Endentscheidung) bzw. 15 Tage (Anordnungen) ab Zustellung der begründeten Entscheidung.",
    "262": "Öffentlichkeit des Registers; Zugang zu Schriftsätzen und Beweismitteln nur auf begründeten Antrag (Abs. 1 lit. b).",
    "262A": "Schutz vertraulicher Informationen: Antrag bei Einreichung, Vertraulichkeitskreis mit mindestens einer natürlichen Person je Partei (Abs. 6), Interessenabwägung.",
    "263": "Klageänderung nur mit Erlaubnis; Ablehnung, wenn die Änderung mit angemessener Sorgfalt früher hätte erfolgen können (Abs. 2).",
    "265": "Rücknahme der Klage; Gebührenerstattung nach R. 370.9 (seit 1.1.2026: 50 % vor Abschluss des schriftlichen Verfahrens).",
    "295": "Aussetzungsgründe: u.a. paralleles EPA-Einspruchsverfahren mit baldiger Entscheidung (lit. a), Vorabentscheidung des EuGH (lit. c), Vergleichsverhandlungen (lit. i).",
    "333": "Überprüfung verfahrensleitender Anordnungen des Berichterstatters durch den Spruchkörper; Antrag binnen 15 Tagen.",
    "354": "Vollstreckung: Anordnungen sofort vollstreckbar; Zwangsgeld (Abs. 3, 4); Sicherheitsleistung; Aufhebung wirkt zurück (EPG-BerG Kodak/Fujifilm).",
    "370": "Gerichtsgebühren: Festgebühr plus streitwertabhängige Gebühr (Verletzungsklage, Widerklage, einstweilige Maßnahmen, Berufung); KMU-Ermäßigung (Abs. 8); Erstattung (Abs. 9).",
}


def _absaetze(raw):
    out = []
    for a in raw:
        m = re.match(r"^(\d{1,2})\.\s+(.*)$", a)
        out.append(dict(nr=m.group(1), text=m.group(2)) if m else dict(nr=None, text=a))
    return out


_JSON = json.loads(_DATA.read_text(encoding="utf-8"))
META = _JSON["meta"]
URL = META["quelle"]
URL_PDF = META["quelle"]
REGELN = []
for _r in _JSON["regeln"]:
    _kap = " / ".join(schoen(x) for x in (_r["kapitel"], _r["abschnitt"]) if x)
    REGELN.append(dict(
        nr=_r["nr"], titel=_r["titel"], titel_en=_r["titel_en"],
        kapitel=(schoen(_r["teil"]) if _r["teil"] else "Anwendung und Auslegung der Verfahrensordnung"), abschnitt=_kap or None,
        absaetze=_absaetze(_r["absaetze"]), umsetzung=[], umsetzung_weitere={}, concepts=[], cases=[],
        bezug=[f"Art. {n} EPGÜ" for n in _r["bezug"]], hinweis=HINWEISE.get(_r["nr"], ""), url=_r["url"],
    ))
ARTIKEL = REGELN
ERWAEGUNGSGRUENDE = [dict(nr=str(p["nr"]), text=p["text"]) for p in _JSON.get("praeambel", [])]
