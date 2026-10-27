# -*- coding: utf-8 -*-
"""Bausteine der Lerneinheiten. `distinctions` verweist auf Abgrenzungstabellen (distinctions.py);
bei Intro-Einheiten werden sie direkt unter dem Text als Tabelle angezeigt. `abschnitt` gliedert ein Kapitel in
Unterkapitel (Absatz oder Tatbestandsmerkmal, z. B. „Abs. 2: Schadensersatz“); die App setzt eine Zwischenüberschrift,
sobald er wechselt. `fallkette` ist das Jurafuchs-Format: ein kurzer Sachverhalt, danach mehrere Fragen."""


def _ab(e, abschnitt):
    if abschnitt:
        e["abschnitt"] = abschnitt
    return e


def intro(id, titel, text, concepts=(), norms=(), cases=(), distinctions=(), abschnitt=""):
    return _ab(dict(id=id, typ="intro", titel=titel, text=text, concepts=list(concepts), norms=list(norms), cases=list(cases),
                    distinctions=list(distinctions)), abschnitt)


def schema(id, titel, schema_id, text="", abschnitt=""):
    return _ab(dict(id=id, typ="schema", titel=titel, schema=schema_id, text=text, concepts=[], norms=[], cases=[], distinctions=[]), abschnitt)


def fall(id, titel, sachverhalt, frage, antwort, loesung, merke="", level=1, concepts=(), norms=(), cases=(), step=None, distinctions=(), abschnitt=""):
    """antwort: True/False. loesung: Liste von Absätzen (Markdown-Fett mit **...**)."""
    return _ab(dict(id=id, typ="fall", titel=titel, sachverhalt=sachverhalt, frage=frage, antwort=antwort,
                    loesung=list(loesung), merke=merke, level=level, concepts=list(concepts), norms=list(norms),
                    cases=list(cases), step=step, distinctions=list(distinctions)), abschnitt)


def mc(id, titel, frage, optionen, richtig, loesung, sachverhalt="", merke="", level=1, concepts=(), norms=(), cases=(), step=None, distinctions=(), abschnitt=""):
    """optionen: Liste von Strings; richtig: Index der richtigen Option."""
    return _ab(dict(id=id, typ="mc", titel=titel, sachverhalt=sachverhalt, frage=frage, optionen=list(optionen), richtig=richtig,
                    loesung=list(loesung), merke=merke, level=level, concepts=list(concepts), norms=list(norms),
                    cases=list(cases), step=step, distinctions=list(distinctions)), abschnitt)


def frage(frage, antwort, loesung, merke="", titel="", abwandlung="", optionen=None, level=None, concepts=(), norms=(), cases=(), step=None):
    """Ein Schritt einer Fallkette, genau ein Prüfungspunkt. antwort: True/False (Ja/Nein) oder, mit `optionen`, der Index der
    richtigen Option. `abwandlung`: ein Satz, der den Sachverhalt für diese und die folgenden Fragen ändert („Wie wäre es, wenn …“)."""
    return dict(frage=frage, antwort=antwort, loesung=list(loesung), merke=merke, titel=titel, abwandlung=abwandlung,
                optionen=list(optionen) if optionen else None, level=level, concepts=list(concepts), norms=list(norms),
                cases=list(cases), step=step)


def _merge(*ls):
    out = []
    for l in ls:
        out += [x for x in l if x not in out]
    return out


def fallkette(id, titel, sachverhalt, fragen, abschnitt="", level=1, concepts=(), norms=(), cases=(), step=None):
    """Jurafuchs-Format: ein kurzer Sachverhalt (zwei bis vier Sätze), danach zwei bis sechs Fragen, die den Fall Prüfungspunkt
    für Prüfungspunkt lösen. Ergibt eine Liste von Einheiten (IDs `<id>a`, `<id>b`, …), die in der Kapitelliste unter dem
    Falltitel zusammenstehen; jede Frage wird einzeln bewertet und wiederholt. Verwendung: `einheiten=[intro(…), *fallkette(…)]`."""
    if not 2 <= len(fragen) <= 6:
        raise SystemExit(f"Fallkette {id}: {len(fragen)} Fragen (erlaubt: 2 bis 6)")
    gruppe = dict(id=id, titel=titel, sachverhalt=sachverhalt, n=len(fragen))
    out = []
    for i, q in enumerate(fragen):
        common = dict(merke=q["merke"], level=q["level"] or level, concepts=_merge(q["concepts"], concepts), norms=_merge(q["norms"], norms),
                      cases=_merge(q["cases"], cases), step=q["step"] or step, abschnitt=abschnitt)
        uid, t = f"{id}{chr(97 + i)}", q["titel"] or q["frage"]
        if q["optionen"]:
            e = mc(uid, t, q["frage"], q["optionen"], q["antwort"], q["loesung"], **common)
        else:
            e = fall(uid, t, "", q["frage"], bool(q["antwort"]), q["loesung"], **common)
        e.update(gruppe=gruppe, schritt=i + 1)
        if q["abwandlung"]:
            e["abwandlung"] = q["abwandlung"]
        out.append(e)
    return out
