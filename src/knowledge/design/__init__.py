# -*- coding: utf-8 -*-
"""Wissenspaket Designrecht: DesignG und DesignV (amtlicher Wortlaut), Richtlinie 98/71/EG, Richtlinie (EU) 2024/2823 und die
Verordnung (EG) Nr. 6/2002 über Unionsgeschmacksmuster (GGV, konsolidiert), Begriffe, Prüfungsschemata, Abgrenzungen,
Leitentscheidungen (BGH I. Zivilsenat, BPatG, EuGH/EuG) und der Entscheidungskorpus der Design-Beschwerde- und
Nichtigkeitssachen des BPatG sowie der designrechtlichen BGH-Rechtsprechung aus der RheinIP-Datenbank.

Normtexte: data/designg.json, designv.json, designrl.json, designrl2024.json, ggv.json; Entscheidungen: data/design_decisions.json
(alles erzeugt von tools/fetch_design.py). IDs sind mit `des_` bzw. `d_des_` präfixiert.
Zitierweise in `norms`-Feldern: `§ 2 Abs. 3 DesignG`, `§ 7 DesignV`, `Art. 5 DesignRL`, `Art. 19 DesignRL 2024`, `Art. 8 Abs. 1 GGV`.
"""
from .concepts import CONCEPTS  # noqa: F401
from .cases import CASES  # noqa: F401
from .schemata import SCHEMATA  # noqa: F401
from .distinctions import DISTINCTIONS  # noqa: F401
from . import gesetze_texte, eurecht, entscheidungen  # noqa: F401
