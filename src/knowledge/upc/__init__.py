# -*- coding: utf-8 -*-
"""Wissenspaket Einheitliches Patentgericht (EPG/UPC): EPGÜ, Verfahrensordnung, Entscheidungen,
Begriffe, Prüfungsschemata und Abgrenzungen. Die Normtexte kommen aus data/upca.json und
data/upc_rop.json, die Entscheidungsdaten aus data/upc_decisions.json (erzeugt von tools/fetch_upc.py).

IDs sind mit `upc_` bzw. `d_upc_` präfixiert, damit sie neben dem Markenrecht im selben Graphen leben.
Zitierweise in `norms`-Feldern: `Art. 33 Abs. 1 EPGÜ`, `R. 19.1 VerfO` (auch `UPCA`/`RoP`).
"""
from .concepts import CONCEPTS  # noqa: F401
from .cases import CASES  # noqa: F401
from .schemata import SCHEMATA  # noqa: F401
from .distinctions import DISTINCTIONS  # noqa: F401
from . import upca, rop, entscheidungen  # noqa: F401
