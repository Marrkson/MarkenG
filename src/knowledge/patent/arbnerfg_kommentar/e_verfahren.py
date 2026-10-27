# -*- coding: utf-8 -*-
"""Kommentar zum ArbnErfG, Teil e_verfahren: §§ 27 bis 42 (siehe __init__.py)."""
from ._helfer import rn, ea, SST, BGH, BPATG  # noqa: F401

KOMMENTAR = {
    "42": [
        rn("Hochschulbegriff", "Hochschule im Sinne des § 42 ArbnErfG ist jede Einrichtung, die nach Landesrecht staatliche Hochschule ist. Ein "
           "Universitätsklinikum gehört unabhängig von seiner Rechtsform dazu, weil Forschung, Lehre und Krankenversorgung dort verfassungsrechtlich "
           "geboten verzahnt sind. Beschäftigte sind alle, die dort arbeiten: Beamte und Angestellte, wissenschaftliches, technisches und sonstiges Personal.",
           belege=[("Arb.Erf. 12/23", "2026-06-16")]),
        rn("30 % der Einnahmen", "Für Hochschulbeschäftigte bestimmt sich die Höhe der Vergütung ausnahmslos nach § 42 Nr. 4 ArbnErfG, nicht nach "
           "§ 9 Abs. 2 ArbnErfG: Es gibt weder Erfindungswert noch Anteilsfaktor. Einnahmen sind alle geldwerten Vorteile, die der Hochschule aus der "
           "Verwertung zufließen, auch ein ersparter betrieblicher Nutzen; ihn über einen „Umrechnungsfaktor“ (Lizenzsatz) zu kürzen, ist systemwidrig.",
           belege=[("Arb.Erf. 12/23", "2026-06-16")], absatz="Nr. 4"),
    ],
}

CASES = [
    ea("arb_sst_hochschulklinikum", "Hochschulklinikum", SST, "2026-06-16", "Arb.Erf. 12/23",
       "Ein Universitätsklinikum ist Hochschule im Sinne des § 42 ArbnErfG; Beschäftigte ist das gesamte Personal. Die Vergütung richtet sich "
       "ausschließlich nach § 42 Nr. 4 ArbnErfG (30 % der Einnahmen); dazu zählen alle geldwerten Vorteile aus der Verwertung, auch ein "
       "erfasster betrieblicher Nutzen, ohne Kürzung durch einen Umrechnungsfaktor.",
       norms=["§ 42 ArbnErfG", "§ 9 Abs. 1 ArbnErfG"], concepts=["arb_hochschulerfindung", "arb_verguetungsanspruch"], tags=["Hochschule", "Vergütung"]),
]
