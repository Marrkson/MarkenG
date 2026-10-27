# -*- coding: utf-8 -*-
"""Europäisches Patentübereinkommen (EPÜ): Artikel und Regeln der Ausführungsordnung als zwei Normfamilien.

Wortlaut aus data/epc.json (tools/fetch_epc.py: deutsch und englisch von epo.org, Kontrolle gegen die RheinIP-Datenbank).
Zitierform: `Art. 54 Abs. 3 EPÜ` (Familie `epc`), `R. 71 Abs. 3 EPÜ` (Familie `epcr`); englisch `Art. 54(3) EPC`, `R. 71(3) EPC`.
Beide Familien teilen das Kürzel EPÜ; build_graph unterscheidet sie am Zitatkopf (`Art.` oder `R.`, gesetze.RULE_NORM_KEYS).

Jede Vorschrift trägt neben dem Wortlaut die Anreicherung, in der Reihenfolge, in der man eine Vorschrift erschließt:
  `zitiert`     Zahl der Entscheidungen der Beschwerdekammern, die sie als einschlägige Vorschrift nennen (data/epc_decisions.json),
  `gl`          Abschnitte der Richtlinien für die Prüfung (2026), die sie am Rand oder im Text zitieren (data/epc_guidelines.json),
  `oj`          Beschlüsse und Mitteilungen im Amtsblatt seit 2008, die sie nennen (data/epc_oj.json), dazu die Fußnoten des EPÜ,
  `eqe`         Zahl der Fragen der EQE Paper D, Teil 1 (2015 bis 2025), deren Musterlösung sie heranzieht (data/eqe_d1.json),
  `hinweis`     Lern- und Klausurhinweis (HINWEISE unten).
"""
import json
import re
from pathlib import Path

_DATA = Path(__file__).resolve().parents[3] / "data"
_JSON = json.loads((_DATA / "epc.json").read_text(encoding="utf-8"))
META = _JSON["meta"]
_GL = json.loads((_DATA / "epc_guidelines.json").read_text(encoding="utf-8"))
_OJ = json.loads((_DATA / "epc_oj.json").read_text(encoding="utf-8"))
_EQE = json.loads((_DATA / "eqe_d1.json").read_text(encoding="utf-8"))
GL_META, OJ_META, EQE_META = _GL["meta"], _OJ["meta"], _EQE["meta"]
GL_BY_ID = {g["id"]: g for g in _GL["abschnitte"]}
OJ_BY_REF = {o["fundstelle"]: o for o in _OJ["ausgaben"]}

KURZ = "EPÜ"
TITEL = "Europäisches Patentübereinkommen (EPÜ 2000)"
GESETZ = "EPÜ (Übereinkommen über die Erteilung europäischer Patente, Fassung 2000)"
GESETZ_AO = "Ausführungsordnung zum EPÜ"
URL = "https://www.epo.org/de/legal/epc/2020/index.html"
URL_PDF = "https://www.epo.org/de/legal/epc/2020/convention.html"
GL_URL = GL_META["url"]

# Lern- und Klausurhinweise je Vorschrift (Schlüssel: "a54" für Artikel, "r71" für Regeln). Jedes Zitat mit Gesetz.
HINWEISE = {
    "a14": "Amtssprachen Deutsch, Englisch, Französisch. Anmeldung in jeder Sprache möglich, Übersetzung binnen zwei Monaten (R. 6 Abs. 1 EPÜ); "
           "die Übersetzung kann bis zum Ende des Verfahrens mit dem Original in Übereinstimmung gebracht werden (Art. 14 Abs. 2 EPÜ). "
           "Sprachenermäßigung von 30 % auf Anmelde- und Prüfungsgebühr bei Einreichung in einer zugelassenen Nichtamtssprache für "
           "KMU (einschließlich Kleinstunternehmen), natürliche Personen, Organisationen ohne Gewinnerzielungsabsicht, Hochschulen und öffentliche "
           "Forschungseinrichtungen aus diesem Staat (R. 7a Abs. 1 EPÜ, Art. 14 Abs. 1 GebO).",
    "a54": "Klausurnorm Nr. 1 in Paper D. Abs. 2: alles, was vor dem Anmeldetag (bei wirksamer Priorität: Prioritätstag, Art. 89 EPÜ) öffentlich "
           "zugänglich war. Abs. 3: ältere europäische Anmeldungen nur für die Neuheit (nicht Art. 56 EPÜ), Inhalt in der ursprünglich eingereichten "
           "Fassung, Veröffentlichung am oder nach dem Anmeldetag; Euro-PCT-Anmeldungen nur bei Anmeldegebühr und Übersetzung (Art. 153 Abs. 5 EPÜ, R. 165 EPÜ). "
           "Abs. 4, 5: erste und weitere medizinische Indikation.",
    "a55": "Unschädliche Offenbarung nur bei offensichtlichem Missbrauch oder anerkannter Ausstellung, und nur, wenn sie höchstens sechs Monate vor "
           "der Einreichung erfolgte; maßgeblich ist der tatsächliche Anmeldetag, nicht der Prioritätstag (G 3/98, G 2/99).",
    "a60": "Recht auf das europäische Patent: Erfinder oder Rechtsnachfolger; im Verfahren vor dem EPA gilt der Anmelder als berechtigt (Abs. 3). "
           "Streit über die Berechtigung entscheiden die nationalen Gerichte (Anerkennungsprotokoll), nicht das EPA.",
    "a61": "Nach rechtskräftiger nationaler Entscheidung kann der Berechtigte binnen drei Monaten die Anmeldung weiterverfolgen, eine neue Anmeldung "
           "einreichen oder die Zurückweisung beantragen (R. 16 EPÜ); Aussetzung des Erteilungsverfahrens nach R. 14 EPÜ.",
    "a65": "Übersetzungserfordernis nur noch in Staaten, die das Londoner Übereinkommen nicht oder nur teilweise anwenden. Wird einheitliche Wirkung "
           "eingetragen (Antrag nach R. 6 DOEPS), entfällt die Validierung in den teilnehmenden Staaten; Übersetzungen richten sich dann nur nach Art. 6 EPatÜVO.",
    "a76": "Teilanmeldung: unmittelbar beim EPA, für jede anhängige frühere Anmeldung (R. 36 Abs. 1 EPÜ), nur Gegenstand, der nicht über die "
           "Stammanmeldung hinausgeht (G 1/05, G 1/06); sie erhält Anmeldetag und Priorität der Stammanmeldung. Anhängig bis zum Tag vor dem "
           "Hinweis auf die Erteilung bzw. bis zum Ablauf der Beschwerdefrist nach Zurückweisung (G 1/09).",
    "a80": "Anmeldetag nach R. 40 Abs. 1 EPÜ: Hinweis, dass ein Patent beantragt wird, Angaben zur Identität des Anmelders, Beschreibung oder "
           "Bezugnahme auf eine früher eingereichte Anmeldung. Ansprüche sind für den Anmeldetag nicht nötig (R. 58 EPÜ).",
    "a86": "Jahresgebühren ab dem dritten Jahr, gerechnet vom Anmeldetag; fällig am letzten Tag des Monats, in dem sich der Anmeldetag jährt "
           "(R. 51 Abs. 1 EPÜ). Nachfrist sechs Monate mit Zuschlag (R. 51 Abs. 2 EPÜ). Nach dem Hinweis auf die Erteilung an die nationalen Ämter.",
    "a87": "Priorität: erste Anmeldung in oder für einen PVÜ-/WTO-Staat, dieselbe Erfindung (G 2/98), zwölf Monate (nicht weiterbehandlungs-, "
           "aber wiedereinsetzungsfähig nach R. 136 Abs. 1 EPÜ). Teilpriorität für generische Ansprüche (G 1/15); widerlegbare Vermutung der "
           "Prioritätsberechtigung (G 1/22, G 2/22).",
    "a88": "Prioritätserklärung möglichst bei Einreichung, spätestens binnen 16 Monaten ab dem frühesten Prioritätstag (R. 52 Abs. 2 EPÜ); Berichtigung "
           "binnen 16 Monaten, jedenfalls bis vier Monate nach dem Anmeldetag (R. 52 Abs. 3 EPÜ). Abschrift und Übersetzung der Prioritätsanmeldung nach R. 53 EPÜ.",
    "a94": "Prüfungsantrag bis sechs Monate nach dem Hinweis auf die Veröffentlichung des Recherchenberichts (R. 70 Abs. 1 EPÜ); Bescheide nach "
           "Art. 94 Abs. 3 EPÜ; Fristversäumnis führt zur Rücknahmefiktion (Art. 94 Abs. 4 EPÜ), Abhilfe: Weiterbehandlung.",
    "a97": "Erteilung erst nach Einverständnis mit der Fassung (R. 71 Abs. 3 bis 5 EPÜ); Wirkung ab dem Tag der Bekanntmachung des Hinweises "
           "im Europäischen Patentblatt (Abs. 3) – ab da laufen Einspruchsfrist (Art. 99 EPÜ) und die Frist für den Antrag auf einheitliche Wirkung.",
    "a99": "Einspruch binnen neun Monaten nach Bekanntmachung des Hinweises auf die Erteilung, schriftlich und begründet, Einspruchsgebühr; jeder "
           "Dritte, auch ein Strohmann (G 3/97), nicht der Inhaber selbst (G 9/93). Wirkt für alle benannten Staaten; Einheitspatent eingeschlossen.",
    "a100": "Abschließende Einspruchsgründe: mangelnde Patentierbarkeit (Art. 52 bis 57 EPÜ), mangelnde Ausführbarkeit, unzulässige Erweiterung. "
            "Klarheit (Art. 84 EPÜ) ist kein Einspruchsgrund; geänderte Ansprüche werden auf Klarheit nur geprüft, soweit die Änderung sie aufwirft (G 3/14).",
    "a101": "Prüfung des Einspruchs; Umfang durch den Einspruch begrenzt (G 9/91), neue Einspruchsgründe im Beschwerdeverfahren nur mit Zustimmung des Inhabers (G 10/91). "
            "Aufrechterhaltung in geändertem Umfang nach R. 82 EPÜ.",
    "a105": "Beitritt des vermeintlichen Patentverletzers binnen drei Monaten, nachdem die Verletzungsklage gegen ihn oder seine negative "
            "Feststellungsklage (nach einer Unterlassungsaufforderung) erhoben wurde (R. 89 Abs. 1 EPÜ); auch im "
            "Beschwerdeverfahren, dort aber ohne eigene Beschwerdeführerstellung (G 2/24).",
    "a105a": "Beschränkung oder Widerruf auf Antrag des Inhabers jederzeit nach der Erteilung, aber nicht, solange ein Einspruch anhängig ist "
             "(Abs. 2); Gebühr, Antrag nach R. 92 EPÜ, Mängelbeseitigung R. 94 EPÜ.",
    "a108": "Beschwerde binnen zwei Monaten nach Zustellung der Entscheidung, Beschwerdegebühr in derselben Frist, Begründung binnen vier Monaten. "
            "Ohne fristgerechte Gebühr gilt die Beschwerde als nicht eingelegt (G 1/18). Frist nicht weiterbehandlungsfähig (Art. 121 Abs. 4 EPÜ).",
    "a112a": "Überprüfungsantrag gegen Entscheidungen der Beschwerdekammern nur bei schwerwiegenden Verfahrensmängeln oder Straftaten; zwei Monate, "
             "Gebühr; der Antrag hat keine aufschiebende Wirkung (Art. 112a Abs. 3 EPÜ).",
    "a115": "Einwendungen Dritter: nach Veröffentlichung, schriftlich und begründet, ohne Gebühr; der Dritte wird nicht Beteiligter (Art. 115 EPÜ, R. 114 EPÜ).",
    "a121": "Weiterbehandlung ist der Standardbehelf bei versäumten Fristen gegenüber dem EPA: Antrag durch Gebührenzahlung binnen zwei Monaten nach "
            "der Mitteilung über den Rechtsverlust, versäumte Handlung nachholen (R. 135 Abs. 1 EPÜ). Ausgeschlossen: Prioritätsfrist, Beschwerdefrist, "
            "Überprüfungsantrag und die Fristen in R. 135 Abs. 2 EPÜ.",
    "a122": "Wiedereinsetzung nur bei Wahrung aller nach den Umständen gebotenen Sorgfalt; zwei Monate nach Wegfall des Hindernisses, spätestens ein Jahr "
            "nach Fristablauf (R. 136 Abs. 1 EPÜ); für die Prioritätsfrist zwei Monate nach deren Ablauf. Vorrang hat die Weiterbehandlung (R. 136 Abs. 3 EPÜ).",
    "a123": "Abs. 2: keine Änderung über den Inhalt der ursprünglichen Anmeldung hinaus (Goldstandard: unmittelbar und eindeutig offenbart; "
            "Disclaimer nach G 1/03, G 2/10, G 1/16). Abs. 3: nach Erteilung keine Erweiterung des Schutzbereichs; Kollision beider Absätze (G 1/93).",
    "a133": "Vertretungszwang nur für Beteiligte ohne Wohnsitz oder Sitz in einem Vertragsstaat (Abs. 2), ausgenommen die Einreichung der Anmeldung; "
            "Beteiligte mit Sitz in einem Vertragsstaat können durch Angestellte mit Vollmacht handeln (Abs. 3). Vollmachten: R. 152 EPÜ.",
    "a153": "Euro-PCT: Das EPA ist Bestimmungsamt und ausgewähltes Amt. Eintritt in die europäische Phase binnen 31 Monaten (R. 159 Abs. 1 EPÜ); "
            "die internationale Anmeldung gilt als europäische Anmeldung, als Stand der Technik nach Art. 54 Abs. 3 EPÜ aber nur, wenn die Voraussetzungen "
            "des Art. 153 Abs. 3 oder 4 EPÜ und der R. 165 EPÜ (Anmeldegebühr, gegebenenfalls Übersetzung) erfüllt sind (Art. 153 Abs. 5 EPÜ).",
    "r6": "Übersetzung einer Anmeldung in Nichtamtssprache binnen zwei Monaten (Abs. 1), keine Weiterbehandlung (R. 135 Abs. 2 EPÜ). "
          "Die Gebührenermäßigung der früheren Abs. 3 und 4 steht heute in R. 7a EPÜ und Art. 14 GebO.",
    "r36": "Teilanmeldung zu jeder anhängigen früheren Anmeldung; in der Verfahrenssprache der Stammanmeldung oder deren Originalsprache mit "
           "Übersetzung binnen zwei Monaten (Abs. 2); Anmelde- und Recherchengebühr binnen eines Monats (Abs. 3); fällige Jahresgebühren binnen vier Monaten "
           "ohne Zuschlag (R. 51 Abs. 3 EPÜ).",
    "r40": "Anmeldetag: Hinweis auf Patentantrag, Identität des Anmelders, Beschreibung oder Bezugnahme. Bei Bezugnahme beglaubigte Abschrift "
           "binnen zwei Monaten (Abs. 3).",
    "r51": "Fälligkeit am letzten Tag des Monats; Zahlung mit Zuschlag binnen sechs Monaten nach Fälligkeit (Abs. 2). Keine Weiterbehandlung für "
           "die Frist nach Abs. 2 (R. 135 Abs. 2 EPÜ), aber Wiedereinsetzung.",
    "r56": "Fehlende Teile oder Zeichnungen: Nachreichung binnen zwei Monaten; Neudatierung, außer die Teile sind vollständig in der Priorität "
           "enthalten (Abs. 3) – dann bleibt der Anmeldetag.",
    "r56a": "Seit 1.11.2022: fälschlich eingereichte Anmeldungsunterlagen können durch richtige ersetzt werden; Neudatierung, außer die richtigen "
            "Unterlagen sind vollständig in der Priorität enthalten (Abs. 4).",
    "r58": "Mängelbeseitigung nach der Eingangsprüfung, insbesondere fehlende Ansprüche binnen zwei Monaten (R. 58 EPÜ).",
    "r70": "Prüfungsantrag binnen sechs Monaten nach dem Hinweis auf die Veröffentlichung des europäischen Recherchenberichts; Aufrechterhaltungs"
           "erklärung nach Abs. 2, Stellungnahme zum Recherchenbericht nach R. 70a EPÜ.",
    "r71": "R. 71 Abs. 3 EPÜ: Mitteilung der für die Erteilung vorgesehenen Fassung; vier Monate für Erteilungsgebühr und Übersetzung der Ansprüche "
           "(Einverständnis). Änderungen oder Berichtigungen innerhalb der Frist führen zu einem neuen Bescheid (Abs. 6). Versäumnis: Rücknahmefiktion (Abs. 7), "
           "Weiterbehandlung möglich.",
    "r112": "Feststellung eines Rechtsverlusts; binnen zwei Monaten kann eine beschwerdefähige Entscheidung beantragt werden (Abs. 2). Die Mitteilung "
            "setzt die Frist der Weiterbehandlung in Gang.",
    "r126": "Seit 1.11.2023 keine Zehn-Tage-Fiktion mehr: Das Schriftstück gilt als an dem Tag zugestellt, auf den es datiert ist, es sei denn, es ist "
            "nicht zugegangen. Weist das EPA einen Zugang mehr als sieben Tage nach dem Datum nach, verlängert sich die Frist um die überschießenden Tage "
            "(Abs. 2). Entsprechend für elektronische Zustellungen (R. 127 Abs. 2 EPÜ).",
    "r131": "Fristberechnung: Monatsfristen enden am Tag des späteren Monats mit derselben Zahl wie das auslösende Ereignis; fehlt dieser Tag, am letzten "
            "Tag des Monats (Abs. 4).",
    "r134": "Fristverlängerung, wenn eine Annahmestelle des EPA am Fristende geschlossen ist oder die Post allgemein unterbrochen ist (Abs. 1, 2); "
            "Abs. 5: Nachweis bei Störungen des Postverkehrs.",
    "r135": "Antrag durch Zahlung der Weiterbehandlungsgebühr binnen zwei Monaten nach der Mitteilung, versäumte Handlung in derselben Frist nachholen. "
            "Ausgeschlossen (Abs. 2): die Fristen des Art. 121 Abs. 4 EPÜ sowie u. a. R. 6 Abs. 1, R. 36 Abs. 2, R. 40 Abs. 3, R. 51 Abs. 2 bis 5, "
            "R. 52 Abs. 2 und 3, R. 55, R. 56, R. 58, R. 64, R. 112 Abs. 2 und R. 164 Abs. 1 und 2 EPÜ – dort hilft nur die Wiedereinsetzung.",
    "r136": "Wiedereinsetzungsantrag schriftlich und begründet, Gebühr, versäumte Handlung nachholen (Abs. 2); ausgeschlossen sind Fristen, für die "
            "Weiterbehandlung möglich ist, und die Wiedereinsetzungsfrist selbst (Abs. 3).",
    "r137": "Änderungen vor Erhalt des Recherchenberichts nur unter R. 137 Abs. 1 EPÜ, danach einmal mit Erwiderung auf den Recherchenbericht (R. 161, R. 70a EPÜ) "
            "aus eigenem Antrieb, später nur mit Zustimmung (Abs. 3); keine Ansprüche auf nicht recherchierte Gegenstände (Abs. 5).",
    "r139": "Berichtigung sprachlicher Fehler, Schreibfehler und Unrichtigkeiten; in Beschreibung, Ansprüchen und Zeichnungen nur, wenn die Berichtigung "
            "offensichtlich ist (G 3/89, G 11/91). Berichtigung der Prioritätserklärung nach R. 52 Abs. 3 EPÜ.",
    "r151": "Ohne Bezeichnung gilt der im Antrag erstgenannte Anmelder als gemeinsamer Vertreter; muss einer der Anmelder einen zugelassenen Vertreter "
            "bestellen, ist dieser gemeinsamer Vertreter, sofern nicht der Erstgenannte selbst einen bestellt hat (Abs. 1). Gilt ebenso für gemeinsame "
            "Einsprechende und Inhaber.",
    "r159": "31 Monate ab Anmelde- bzw. Prioritätstag für Übersetzung, Angabe der Unterlagen, Anmeldegebühr, Benennungs- und Recherchengebühr, "
            "Prüfungsantrag und ggf. Jahresgebühr. Versäumnis: Rücknahmefiktion (R. 160 EPÜ), Weiterbehandlung.",
    "r161": "Nach Eintritt: Aufforderung zur Stellungnahme oder Änderung binnen sechs Monaten (Abs. 1), Änderungen vor der ergänzenden Recherche (Abs. 2).",
    "r164": "Uneinheitlichkeit in der europäischen Phase: ergänzende Recherche nur der ersten Erfindung, weitere Recherchengebühren nach Abs. 1; bei EPA als "
            "ISA oder SISA: Recherche nicht recherchierter Erfindungen in der Prüfung gegen Gebühr (Abs. 2).",
}

# Kapitelüberschriften der Richtlinien (Teil-Kapitel) für die Liste je Vorschrift
_GL_ORDER = {g["id"]: i for i, g in enumerate(_GL["abschnitte"])}


def _num(n):
    m = re.match(r"(\d+)(.*)", n)
    return (int(m.group(1)), m.group(2))


def _gl_fuer(kind, nr):
    """Abschnitte der Richtlinien, die die Vorschrift nennen: zuerst die mit Randverweis, dann im Text zitierend; Unterabschnitte mit eigenem
    Randverweis vor dem Oberabschnitt; höchstens 12."""
    rand, text = [], []
    for g in _GL["abschnitte"]:
        if nr in (g["ra"] if kind == "a" else g["rr"]):
            rand.append(g)
        elif nr in (g["a"] if kind == "a" else g["r"]):
            text.append(g)
    sel = rand[:12] + text[:max(0, 12 - len(rand))]
    sel.sort(key=lambda g: _GL_ORDER[g["id"]])
    return [dict(id=g["id"], ref=g["ref"], titel=re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", g["titel"]), rand=g in rand) for g in sel], len(rand) + len(text)


def _oj_fuer(kind, nr):
    hits = [o for o in _OJ["ausgaben"] if nr in (o["a"] if kind == "a" else o["r"])]
    hits.sort(key=lambda o: o["datum"], reverse=True)
    return [dict(ref=o["fundstelle"], datum=o["datum"], titel=o["titel"], url=o["url_de"]) for o in hits[:8]], len(hits)


def _eqe_fuer(kind, nr):
    return [dict(jahr=q["jahr"], nr=q["nr"], thema=q["thema"]) for q in _EQE["fragen"] if nr in (q["a"] if kind == "a" else q["r"])]


def _vorschrift(rec, kind):
    nr = rec["nr"]
    gl, gl_n = _gl_fuer(kind, nr)
    oj, oj_n = _oj_fuer(kind, nr)
    gestrichen = not rec["absaetze"]
    return dict(
        nr=nr, titel=rec["titel"] or ("(gestrichen)" if gestrichen else ""), titel_en=rec["titel_en"],
        kapitel=rec["teil"], abschnitt=rec["kapitel"] or None,
        absaetze=rec["absaetze"] or [dict(nr=None, text="(gestrichen)")],
        hinweis=HINWEISE.get(kind + nr, ""), umsetzung=[], concepts=[], cases=[],
        url=rec["url"], url_en=rec["url_en"], order=_num(nr)[0] * 10 + (ord(_num(nr)[1][:1]) - 96 if _num(nr)[1] else 0),
        gl=gl, gl_n=gl_n, oj=oj, oj_n=oj_n, eqe=_eqe_fuer(kind, nr),
        grosse_kammer=rec["grosse_kammer"], amtsblatt=rec["amtsblatt"], gestrichen=gestrichen,
    )


ARTIKEL = [_vorschrift(a, "a") for a in _JSON["artikel"]]
REGELN = [_vorschrift(r, "r") for r in _JSON["regeln"]]
_HINWEIS_KEYS = {("a" if k[0] == "a" else "r") + x["nr"] for k, liste in (("a", ARTIKEL), ("r", REGELN)) for x in liste}
_fehlt = sorted(set(HINWEISE) - _HINWEIS_KEYS)
if _fehlt:
    raise SystemExit("epc/texte.py: HINWEISE für unbekannte Vorschriften: " + ", ".join(_fehlt))

_COMMON = dict(kurz=KURZ, erwaegungsgruende=[], url=URL, url_pdf=URL_PDF, paraphrase=False, korpus="epa")
FAMILIEN = [
    dict(key="epc", titel=TITEL, gesetz=GESETZ, artikel=ARTIKEL, zitat="Art.",
         hinweis="Amtlicher deutscher Wortlaut des EPÜ 2000 (epo.org); englischer Titel und Link je Artikel. Angereichert mit den "
                 "Entscheidungen der Beschwerdekammern, den Richtlinien für die Prüfung (2026) und dem Amtsblatt.", **_COMMON),
    dict(key="epcr", titel="Ausführungsordnung zum EPÜ", gesetz=GESETZ_AO, artikel=REGELN, zitat="R.",
         hinweis="Amtlicher deutscher Wortlaut der Ausführungsordnung zum EPÜ (epo.org), Stand der fortlaufend aktualisierten Fassung.", **_COMMON),
]
