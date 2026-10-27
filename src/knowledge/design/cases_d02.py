# -*- coding: utf-8 -*-
"""Weitere Leitentscheidungen für den Normkurs d02 (DesignG nach Vorschriften): BGH/BPatG geprüft gegen data/design_decisions.json
(Helfer `e`), EuGH/EuG per Websuche verifiziert (Helfer `eu`). IDs mit Präfix `des_`."""
from .cases import e, eu, BGH, BPATG, EUGH, EUG  # noqa: F401

CASES = [
    # ------------------------------------------------------------------ Offenbarung und nicht eingetragenes Muster
    e("des_bgh_gebaeckpresse", "Gebäckpresse", BGH, "2008-10-09", "I ZR 126/06",
      "Ein nicht eingetragenes Gemeinschaftsgeschmacksmuster entsteht nur, wenn das Muster der Öffentlichkeit erstmals innerhalb der "
      "Union zugänglich gemacht wird; eine Veröffentlichung außerhalb der Union (hier: im chinesischen Musterregister) genügt nicht, auch "
      "wenn die Fachkreise in der Union sie kennen konnten (Art. 11 GGV). Dieselbe Veröffentlichung kann aber nach Art. 7 GGV "
      "neuheitsschädlich sein, wenn sie den in der Union tätigen Fachkreisen im normalen Geschäftsverlauf bekannt sein konnte.",
      norms=["Art. 11 GGV", "Art. 7 GGV", "Art. 5 GGV", "§ 5 DesignG"],
      concepts=["des_ggm_nicht_eingetragen", "des_offenbarung", "des_neuheit"], tags=["Nicht eingetragenes Muster", "Offenbarung", "Drittstaat"],
      fundstelle="BGH, Urteil vom 09.10.2008 – I ZR 126/06 – Gebäckpresse (GRUR 2009, 79)"),
    # ------------------------------------------------------------------ Recht auf das Design
    eu("des_eugh_feia", "FEIA/Cul de Sac (Auftragsentwurf)", EUGH, "2009-07-02", "C-32/08", "GRUR 2009, 867",
       "Die Arbeitgeberregel des Art. 14 Abs. 3 GGV gilt nicht für Geschmacksmuster, die im Auftrag eines Dritten entworfen werden. Das "
       "Recht auf das Gemeinschaftsgeschmacksmuster steht dann nach Art. 14 Abs. 1 GGV dem Entwerfer zu, sofern es nicht vertraglich auf "
       "einen Rechtsnachfolger übertragen wurde. Für das eingetragene Design gilt dasselbe: § 7 Abs. 2 DesignG erfasst nur Arbeitnehmer.",
       norms=["Art. 14 GGV", "§ 7 DesignG"], concepts=["des_entwerfer_recht", "des_arbeitnehmerdesign"], tags=["Inhaberschaft", "Auftragsentwurf"]),
    # ------------------------------------------------------------------ Nichtigkeitsverfahren: Kosten und Gegenstandswert
    e("des_bpatg_emblemhalterung", "Kühlergitter-Emblemhalterung", BPATG, "2025-02-20", "30 W (pat) 801/22",
      "Willigt die Designinhaberin innerhalb der Widerspruchsfrist in die Löschung ein (§ 33 Abs. 6 DesignG), steht das einem sofortigen "
      "Anerkenntnis gleich; über § 34a Abs. 5 DesignG und § 84 Abs. 2 PatG ist der Rechtsgedanke des § 93 ZPO anwendbar. Die Kosten trägt "
      "dann der Antragsteller, wenn er die Inhaberin nicht zuvor unter Angabe der Nichtigkeitsgründe und mit Frist zum Verzicht aufgefordert "
      "hat. Die bloße Berufung auf das Design in der Antwort auf eine markenrechtliche Abmahnung macht die Aufforderung nicht entbehrlich.",
      norms=["§ 34a Abs. 5 DesignG", "§ 33 Abs. 6 DesignG", "§ 34a Abs. 2 DesignG", "§ 84 PatG"],
      concepts=["des_nichtigkeitsverfahren_dpma", "des_nichtigkeit"], tags=["Nichtigkeitsverfahren", "Kosten", "Verzichtsaufforderung"]),
    e("des_bgh_gegenstandswert_sporthelm", "Gegenstandswert Sporthelm", BGH, "2020-05-28", "I ZB 25/18",
      "Der Gegenstandswert im Designnichtigkeitsverfahren ist nach billigem Ermessen zu bestimmen (heute § 34a Abs. 6 DesignG mit § 23 Abs. 3 "
      "Satz 2 RVG). Maßgeblich ist das wirtschaftliche Interesse des Designinhabers an der Aufrechterhaltung seines Designs; im Regelfall "
      "entspricht ein Wert von 50.000 € billigem Ermessen.",
      norms=["§ 34a Abs. 6 DesignG"], concepts=["des_nichtigkeitsverfahren_dpma"], tags=["Nichtigkeitsverfahren", "Gegenstandswert"],
      fundstelle="BGH, Beschluss vom 28.05.2020 – I ZB 25/18 – Gegenstandswert Sporthelm (GRUR 2020, 1016)"),
    # ------------------------------------------------------------------ Aktivlegitimation, Schadensersatz, Folgeansprüche
    eu("des_eugh_thomas_philipps", "Thomas Philipps/Grüne Welle (Lizenznehmer)", EUGH, "2016-06-22", "C-419/15", "GRUR 2016, 1163",
       "Der Lizenznehmer kann Ansprüche wegen Verletzung eines eingetragenen Gemeinschaftsgeschmacksmusters geltend machen, auch wenn die "
       "Lizenz nicht im Register eingetragen ist (Art. 33 Abs. 2 GGV). In einem Verletzungsverfahren, das er nach Art. 32 Abs. 3 GGV selbst "
       "anhängig macht, kann er Ersatz seines eigenen Schadens verlangen.",
       norms=["Art. 32 GGV", "Art. 33 GGV", "§ 31 DesignG"], concepts=["des_lizenz", "des_schadensersatz"], tags=["Lizenz", "Aktivlegitimation"]),
    e("des_bgh_gemeinkostenanteil", "Gemeinkostenanteil", BGH, "2000-11-02", "I ZR 246/98",
      "Wird Schadensersatz als Herausgabe des Verletzergewinns verlangt, dürfen Gemeinkosten nur abgezogen werden, wenn und soweit sie "
      "ausnahmsweise den schutzrechtsverletzenden Gegenständen unmittelbar zugerechnet werden können. Der Verletzer kann nicht einwenden, "
      "der Gewinn beruhe teilweise auf eigenen Vertriebsleistungen. Die zum Geschmacksmustergesetz a.F. ergangene Entscheidung prägt die "
      "Berechnung nach § 42 Abs. 2 Satz 2 DesignG bis heute.",
      norms=["§ 42 Abs. 2 DesignG"], concepts=["des_schadensersatz"], tags=["Schadensersatz", "Verletzergewinn"]),
    e("des_bgh_windsor_estate", "Windsor Estate", BGH, "2007-07-19", "I ZR 93/04",
      "Der Schadensersatzanspruch aus einer Schutzrechtsverletzung und der Auskunftsanspruch zu seiner Bezifferung sind zeitlich nicht auf "
      "die Zeit ab der ersten nachgewiesenen Verletzungshandlung begrenzt (Aufgabe von BGH Gaby). Zum Markenrecht ergangen, gilt der Satz "
      "für alle Schutzrechte mit gleich gebauten Ansprüchen, auch für § 42 Abs. 2 DesignG.",
      norms=["§ 42 Abs. 2 DesignG", "§ 46 DesignG"], concepts=["des_schadensersatz", "des_auskunft"], tags=["Schadensersatz", "Auskunft", "Markenrecht"]),
    e("des_bgh_wundversorgung", "Produkte zur Wundversorgung", BGH, "2017-10-11", "I ZB 96/16",
      "Ein Unterlassungsgebot, das einen fortdauernden Störungszustand betrifft, verpflichtet mangels abweichender Anhaltspunkte auch zu "
      "möglichen und zumutbaren Handlungen zur Beseitigung, auch in einer einstweiligen Verfügung. Im Verfügungsverfahren muss der Schuldner "
      "ausgelieferte Ware nicht zurückrufen, seine Abnehmer aber auffordern, sie vorläufig nicht weiterzuvertreiben. Zum Markenrecht ergangen; "
      "übertragbar auf § 42 Abs. 1 und § 43 Abs. 2 DesignG.",
      norms=["§ 42 Abs. 1 DesignG", "§ 43 Abs. 2 DesignG"], concepts=["des_unterlassung", "des_vernichtung_rueckruf"], tags=["Unterlassung", "Rückruf", "Einstweilige Verfügung"],
      fundstelle="BGH, Beschluss vom 11.10.2017 – I ZB 96/16 – Produkte zur Wundversorgung (GRUR 2018, 292)"),
    e("des_bgh_alles_kann_besser_werden", "Alles kann besser werden", BGH, "2012-04-19", "I ZB 80/11",
      "Der Auskunftsanspruch gegen Dritte, die in gewerblichem Ausmaß für rechtsverletzende Tätigkeiten genutzte Dienstleistungen erbringen "
      "(hier § 101 Abs. 2 Satz 1 Nr. 3 UrhG), setzt nicht voraus, dass die Rechtsverletzung selbst ein gewerbliches Ausmaß hat. Die Vorschrift "
      "ist wortgleich mit § 46 Abs. 2 Satz 1 Nr. 3 DesignG.",
      norms=["§ 46 Abs. 2 DesignG"], concepts=["des_auskunft"], tags=["Auskunft", "Drittauskunft", "Urheberrecht"]),
    e("des_bgh_pierre_cardin", "PIERRE CARDIN", BGH, "2024-02-22", "I ZR 217/22",
      "Die Befugnis zur Urteilsbekanntmachung (§ 19c MarkenG) kann der obsiegenden Partei nicht nur bei Unterlassungsklagen, sondern auch bei "
      "Klagen auf Auskunft, Rechnungslegung und Feststellung der Schadensersatzpflicht zugesprochen werden. Das berechtigte Interesse steht "
      "unter dem Vorbehalt der Verhältnismäßigkeit; einzustellen sind unter anderem der Zeitablauf seit der Verletzung und die Marktverwirrung. "
      "§ 47 DesignG ist gleich gefasst.",
      norms=["§ 47 DesignG", "§ 19c MarkenG"], concepts=["des_schadensersatz"], tags=["Urteilsbekanntmachung", "Markenrecht"]),
]
