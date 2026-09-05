# -*- coding: utf-8 -*-
def intro(id, titel, text, concepts=(), norms=(), cases=()):
    return dict(id=id, typ="intro", titel=titel, text=text, concepts=list(concepts), norms=list(norms), cases=list(cases))


def schema(id, titel, schema_id, text=""):
    return dict(id=id, typ="schema", titel=titel, schema=schema_id, text=text, concepts=[], norms=[], cases=[])


def fall(id, titel, sachverhalt, frage, antwort, loesung, merke="", level=1, concepts=(), norms=(), cases=(), step=None):
    """antwort: True/False. loesung: Liste von Absätzen (Markdown-Fett mit **...**)."""
    return dict(id=id, typ="fall", titel=titel, sachverhalt=sachverhalt, frage=frage, antwort=antwort,
                loesung=list(loesung), merke=merke, level=level, concepts=list(concepts), norms=list(norms),
                cases=list(cases), step=step)


def mc(id, titel, frage, optionen, richtig, loesung, sachverhalt="", merke="", level=1, concepts=(), norms=(), cases=(), step=None):
    """optionen: Liste von Strings; richtig: Index der richtigen Option."""
    return dict(id=id, typ="mc", titel=titel, sachverhalt=sachverhalt, frage=frage, optionen=list(optionen), richtig=richtig,
                loesung=list(loesung), merke=merke, level=level, concepts=list(concepts), norms=list(norms),
                cases=list(cases), step=step)
