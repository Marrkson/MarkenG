# -*- coding: utf-8 -*-
"""Arbeitnehmererfinderrecht: Gesetz über Arbeitnehmererfindungen (ArbnErfG, in der Praxis „ArbEG“) als Normfamilie des
Patentpakets, die Vergütungsrichtlinien von 1959 als Quellen und der Kommentar aus der Rechtsprechung.

Wortlaut: data/arbnerfg.json (gesetze-im-internet.de, XML; tools/fetch_arbnerfg.py). Knoten `eunorm:arbnerfg:<nr>`, Zitierform
`§ 9 Abs. 2 ArbnErfG` (Alias `ArbEG`). Jede Vorschrift trägt `kommentar` (Randnummern aus arbnerfg_kommentar, jede mit Belegen aus
dem Korpus der Schiedsstelle und des BGH) und `korpus="arbnerfg"` (Zitierliste aus data/arbnerfg_decisions.json).

Die Richtlinien für die Vergütung von Arbeitnehmererfindungen im privaten Dienst (20.7.1959, geändert 1.9.1983; § 11 ArbnErfG) sind
keine Rechtsnorm, sondern Anhaltspunkte (Nr. 1). Deshalb sind ihre 43 Nummern wie die Prüfungsrichtlinien des DPMA `source`-Knoten
(Provider „Vergütungsrichtlinien“, Seiten-ID `vrl:30`, URL auf die Seite im PDF von dpma.de); Begriffe verweisen mit
`quellen=["vrl:30"]` darauf. Im Text werden sie „RL Nr. 30“ zitiert (kein Gesetzeszitat, wird nicht verlinkt).
"""
import json
import re
from pathlib import Path

from .arbnerfg_kommentar import KOMMENTAR

_DATA = Path(__file__).resolve().parents[3] / "data"
_J = json.loads((_DATA / "arbnerfg.json").read_text(encoding="utf-8"))
_V = json.loads((_DATA / "arbnerfg_vergrl.json").read_text(encoding="utf-8"))
META = _J["meta"]
VERGRL_META = _V["meta"]
VERGRL = {n["nr"]: n for n in _V["nummern"]}

# Lern- und Klausurhinweise je Vorschrift (kurz; der Kommentar trägt die Auslegung)
HINWEISE = {
    "4": "Diensterfindung = gebundene Erfindung (Abs. 2): aus der Tätigkeit im Betrieb entstanden (Nr. 1) oder maßgeblich auf Erfahrungen oder Arbeiten des Betriebs beruhend (Nr. 2), jeweils während der Dauer des Arbeitsverhältnisses. Alles andere ist freie Erfindung (Abs. 3) mit Mitteilungs- und Anbietungspflicht (§§ 18, 19 ArbnErfG).",
    "5": "Meldung gesondert, in Textform, als Erfindungsmeldung kenntlich, unverzüglich (Abs. 1). Mängel muss der Arbeitgeber binnen zwei Monaten beanstanden, sonst gilt die Meldung als ordnungsgemäß (Abs. 3); erst die ordnungsgemäße Meldung setzt die Frist des § 6 Abs. 2 ArbnErfG in Gang.",
    "6": "Seit 1.10.2009 Inanspruchnahmefiktion: Gibt der Arbeitgeber die Diensterfindung nicht binnen vier Monaten nach Eingang der ordnungsgemäßen Meldung in Textform frei, gilt sie als in Anspruch genommen (Abs. 2). Für vorher gemeldete Erfindungen gilt altes Recht (§ 43 Abs. 3 ArbnErfG): schriftliche, fristgebundene Inanspruchnahmeerklärung, beschränkte oder unbeschränkte Inanspruchnahme.",
    "9": "Anspruchsgrundlage der Erfindervergütung. Vergütung = Erfindungswert × Anteilsfaktor (RL Nr. 39); Erfindungswert meist nach der Lizenzanalogie (RL Nr. 6 ff.), Anteilsfaktor aus Stellung der Aufgabe, Lösung und Stellung im Betrieb (RL Nr. 30 ff.). Auskunft und Rechnungslegung aus § 242 BGB.",
    "12": "Feststellung durch Vereinbarung (Abs. 1), sonst Festsetzung durch begründete Erklärung in Textform, spätestens drei Monate nach Erteilung (Abs. 3); Widerspruch binnen zwei Monaten in Textform, sonst verbindlich (Abs. 4). Anpassung bei wesentlich geänderten Umständen (Abs. 6), Rückzahlung nie.",
    "13": "Der Arbeitgeber muss die gemeldete Diensterfindung unverzüglich im Inland anmelden (Abs. 1); Ausnahmen in Abs. 2 (Freigabe, Zustimmung, Betriebsgeheimnis nach § 17 ArbnErfG). Versäumt er es, kann der Arbeitnehmer nach Fristsetzung selbst anmelden (Abs. 3).",
    "16": "Aufgabe von Anmeldung oder Schutzrecht vor Erfüllung des Vergütungsanspruchs: erst dem Arbeitnehmer mitteilen und auf Verlangen übertragen (Abs. 1, 2); Vorbehalt eines nichtausschließlichen Benutzungsrechts gegen angemessene Vergütung (Abs. 3).",
    "20": "Qualifizierter technischer Verbesserungsvorschlag (Vorzugsstellung wie ein Schutzrecht): Vergütung, sobald der Arbeitgeber ihn verwertet; §§ 9 und 12 ArbnErfG gelten sinngemäß (Abs. 1). Einfache Verbesserungsvorschläge: Tarifvertrag oder Betriebsvereinbarung (Abs. 2).",
    "22": "Unabdingbar zuungunsten des Arbeitnehmers; Vereinbarungen nach der Meldung (Diensterfindung) oder Mitteilung (freie Erfindung, Verbesserungsvorschlag) sind zulässig, stehen aber unter § 23 ArbnErfG.",
    "23": "Vereinbarungen nach § 22 S. 2 ArbnErfG und Festsetzungen sind unwirksam, soweit sie in erheblichem Maße unbillig sind (Abs. 1); geltend zu machen durch Erklärung in Textform bis spätestens sechs Monate nach Ende des Arbeitsverhältnisses (Abs. 2).",
    "28": "In allen Streitfällen auf Grund des ArbnErfG kann die Schiedsstelle beim DPMA angerufen werden; Ziel ist eine gütliche Einigung (Einigungsvorschlag, § 34 ArbnErfG).",
    "34": "Der Einigungsvorschlag gilt als angenommen und wird verbindlich, wenn nicht binnen eines Monats nach Zustellung schriftlich widersprochen wird (Abs. 3).",
    "37": "Klage erst nach einem Verfahren vor der Schiedsstelle (Abs. 1), außer in den Fällen des Abs. 2 (u. a. Ausscheiden des Arbeitnehmers, sechs Monate seit Anrufung, Verzicht beider Parteien nach Entstehen des Streits).",
    "42": "Hochschulerfinder: Publikationsfreiheit nach Anzeige (Nr. 1), negative Publikationsfreiheit (Nr. 2), Benutzungsrecht für Lehre und Forschung (Nr. 3), Vergütung pauschal 30 % der Verwertungseinnahmen (Nr. 4).",
    "43": "Übergangsrecht: Auf Erfindungen, die vor dem 1.10.2009 gemeldet wurden, ist das ArbnErfG in der bis dahin geltenden Fassung anzuwenden (Abs. 3); die Schiedsstelle prüft deshalb stets zuerst den Meldezeitpunkt.",
}


def _titel(p):
    return p["titel"] or ""


ARTIKEL = []
for _i, _p in enumerate(_J["paragraphen"]):
    nr = _p["nr"]
    ARTIKEL.append(dict(
        nr=nr, label=_p["label"] + " ArbnErfG", titel=_titel(_p), kapitel=re.sub(r"\s+", " ", _p["teil"] or "Allgemeines"),
        abschnitt=re.sub(r"\s+", " ", _p["abschnitt"]) if _p["abschnitt"] else None,
        absaetze=[dict(nr=a["nr"], text=a["text"]) for a in _p["absaetze"]], order=_i + 1,
        umsetzung=[], umsetzung_weitere={}, concepts=[], cases=[], entspricht=[], bezug=[],
        hinweis=HINWEISE.get(nr, ""), url=_p["url"], kommentar=KOMMENTAR.get(nr, []),
    ))
_UNBEKANNT = set(KOMMENTAR) - {a["nr"] for a in ARTIKEL}
if _UNBEKANNT:
    raise ValueError(f"Kommentar zu unbekannten Paragraphen des ArbnErfG: {sorted(_UNBEKANNT)}")

FAMILIE = dict(key="arbnerfg", kurz="ArbnErfG", aliase=("ArbEG", "ArbNErfG"), titel="Gesetz über Arbeitnehmererfindungen (ArbnErfG)",
               gesetz="ArbnErfG (Gesetz über Arbeitnehmererfindungen vom 25.7.1957, zuletzt geändert 7.7.2021)", artikel=ARTIKEL,
               erwaegungsgruende=[], url=META["quelle"], url_pdf=META["quelle_xml"], paraphrase=False, zitat="§",
               hinweis="Amtlicher Wortlaut von gesetze-im-internet.de (XML); in Entscheidungen meist „ArbEG“ zitiert. Kommentar je Vorschrift "
                       "aus den Einigungsvorschlägen der Schiedsstelle beim DPMA und der Rechtsprechung des BGH.",
               stand="; ".join(META["stand"]), korpus="arbnerfg")

# ------------------------------------------------------------------ Vergütungsrichtlinien als Quellen
PROVIDER = "Vergütungsrichtlinien"
VERGRL_STAND = "Richtlinien vom 20.7.1959, geändert 1.9.1983"
QUELLEN = [dict(page=f"vrl:{n['nr']}", title=f"RL Nr. {n['nr']}: {n['titel']}", url=n["url"], provider=PROVIDER,
                summary=" ".join(n["absaetze"]))
           for n in _V["nummern"]]
# Begriff -> Nummern der Richtlinien (concepts_arb.c() hängt sie als `quellen` an)
BEGRIFF_QUELLEN = {
    "arb_verguetungsanspruch": ["vrl:1", "vrl:2", "vrl:39"],
    "arb_erfindungswert": ["vrl:3", "vrl:5", "vrl:12", "vrl:13", "vrl:14", "vrl:16", "vrl:20", "vrl:24"],
    "arb_lizenzanalogie": ["vrl:6", "vrl:7", "vrl:8", "vrl:9", "vrl:10", "vrl:11"],
    "arb_anteilsfaktor": ["vrl:30", "vrl:31", "vrl:32", "vrl:33", "vrl:34", "vrl:35", "vrl:37"],
    "arb_tvv": ["vrl:29"],
    "arb_festsetzung": ["vrl:40", "vrl:41"],
    "arb_vorratspatent": ["vrl:18", "vrl:21", "vrl:22", "vrl:23"],
}
for _k, _v in BEGRIFF_QUELLEN.items():
    for _q in _v:
        if _q[4:] not in VERGRL:
            raise ValueError(f"Unbekannte Nummer der Vergütungsrichtlinien {_q} bei {_k}")
