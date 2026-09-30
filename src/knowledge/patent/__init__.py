# -*- coding: utf-8 -*-
"""Wissenspaket Patentrecht: PatG, PatV, IntPatÜG, PatKostG mit Begriffen, Prüfungsschemata, Abgrenzungen,
Leitentscheidungen (BGH X./Xa. Zivilsenat, BPatG) und dem Entscheidungskorpus der Nichtigkeits- und
Beschwerdesenate des BPatG sowie der patentrechtlichen BGH-Rechtsprechung aus der RheinIP-Datenbank.

Normtexte: data/patg.json, patv.json, intpatueg.json, patkostg.json; Entscheidungen: data/patent_decisions.json
(beides erzeugt von tools/fetch_patent.py); Prüfungsrichtlinien des DPMA als Quellen: data/dpma_pruefungsrichtlinien.json
(tools/fetch_pruefungsrichtlinien.py, Modul richtlinien.py). IDs sind mit `pat_` bzw. `d_pat_` präfixiert.
Zitierweise in `norms`-Feldern: `§ 3 Abs. 1 PatG`, `§ 9 PatV`, `Art. II § 6 Abs. 1 Nr. 3 IntPatÜG`, `§ 6 PatKostG`, `Anlage PatKostG`.
"""
from .concepts import CONCEPTS  # noqa: F401
from .cases import CASES  # noqa: F401
from .schemata import SCHEMATA  # noqa: F401
from .distinctions import DISTINCTIONS  # noqa: F401
from . import gesetze_texte, entscheidungen, richtlinien  # noqa: F401
