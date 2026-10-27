# -*- coding: utf-8 -*-
"""Wissenspaket EPÜ: Europäisches Patentübereinkommen und Ausführungsordnung mit Begriffen, Prüfungsschemata, Abgrenzungen,
Leitentscheidungen der Beschwerdekammern und dem Entscheidungskorpus der Kammern aus der RheinIP-Datenbank, angereichert mit den
Richtlinien für die Prüfung (2026), dem Amtsblatt und den Fragen der EQE Paper D.

Normtexte: data/epc.json; Entscheidungen: data/epc_decisions.json; Richtlinien: data/epc_guidelines.json; Amtsblatt: data/epc_oj.json;
EQE: data/eqe_d1.json (alles von tools/fetch_epc.py). IDs sind mit `epc_` bzw. `d_epc_` präfixiert.
Zitierweise in `norms`-Feldern: `Art. 54 Abs. 3 EPÜ`, `R. 71 Abs. 3 EPÜ`.
"""
from .concepts import CONCEPTS  # noqa: F401
from .cases import CASES as _CASES
from . import cases_ka, cases_kb, cases_kc, cases_kd
CASES = _CASES + cases_ka.CASES + cases_kb.CASES + cases_kc.CASES + cases_kd.CASES
from .schemata import SCHEMATA  # noqa: F401
from .distinctions import DISTINCTIONS  # noqa: F401
from . import texte, entscheidungen, quellen  # noqa: F401
