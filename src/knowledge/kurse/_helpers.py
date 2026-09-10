# -*- coding: utf-8 -*-
"""Bausteine der Lerneinheiten. `distinctions` verweist auf Abgrenzungstabellen (distinctions.py);
bei Intro-Einheiten werden sie direkt unter dem Text als Tabelle angezeigt."""


def intro(id, titel, text, concepts=(), norms=(), cases=(), distinctions=()):
    return dict(id=id, typ="intro", titel=titel, text=text, concepts=list(concepts), norms=list(norms), cases=list(cases),
                distinctions=list(distinctions))


def schema(id, titel, schema_id, text=""):
    return dict(id=id, typ="schema", titel=titel, schema=schema_id, text=text, concepts=[], norms=[], cases=[], distinctions=[])


def fall(id, titel, sachverhalt, frage, antwort, loesung, merke="", level=1, concepts=(), norms=(), cases=(), step=None, distinctions=()):
    """antwort: True/False. loesung: Liste von Absätzen (Markdown-Fett mit **...**)."""
    return dict(id=id, typ="fall", titel=titel, sachverhalt=sachverhalt, frage=frage, antwort=antwort,
                loesung=list(loesung), merke=merke, level=level, concepts=list(concepts), norms=list(norms),
                cases=list(cases), step=step, distinctions=list(distinctions))


def mc(id, titel, frage, optionen, richtig, loesung, sachverhalt="", merke="", level=1, concepts=(), norms=(), cases=(), step=None, distinctions=()):
    """optionen: Liste von Strings; richtig: Index der richtigen Option."""
    return dict(id=id, typ="mc", titel=titel, sachverhalt=sachverhalt, frage=frage, optionen=list(optionen), richtig=richtig,
                loesung=list(loesung), merke=merke, level=level, concepts=list(concepts), norms=list(norms),
                cases=list(cases), step=step, distinctions=list(distinctions))
