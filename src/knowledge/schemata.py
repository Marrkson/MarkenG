# -*- coding: utf-8 -*-
"""Prüfungsschemata (Klausur-/Gutachtenaufbau) als Bäume.

Jeder Schritt: dict(label, text?, concepts=[...], norms=[...], cases=[...], children=[...]).
Begriffe in `concepts` werden in der HTML-Ansicht inline (aufklappbar) angezeigt.
"""

def step(label, text="", concepts=None, norms=None, cases=None, children=None, hinweis=""):
    return dict(label=label, text=text, concepts=concepts or [], norms=norms or [],
                cases=cases or [], children=children or [], hinweis=hinweis)


SCHEMATA = [
    dict(
        id="schema_markenverletzung",
        label="Unterlassungsanspruch wegen Markenverletzung (§ 14 Abs. 2, 5 MarkenG)",
        kategorie="Verletzung",
        beschreibung="Zentrales Klausurschema: Anspruch des Markeninhabers gegen den Verletzer auf Unterlassung. Schadensersatz (§ 14 Abs. 6) und Annexansprüche (§§ 18, 19) bauen auf dem gleichen Tatbestand auf.",
        norms=["§ 14"],
        steps=[
            step("A. Anspruchsgrundlage", "§ 14 Abs. 5 S. 1 i.V.m. Abs. 2 Nr. 1, 2 oder 3 MarkenG.", norms=["§ 14 Abs. 5"]),
            step("B. Schutzfähige Marke des Anspruchstellers", concepts=["marke", "entstehung_markenschutz", "aktivlegitimation"], children=[
                step("1. Bestehen des Markenschutzes", "Eintragung (§ 4 Nr. 1), Verkehrsgeltung (§ 4 Nr. 2) oder notorische Bekanntheit (§ 4 Nr. 3). Bei der eingetragenen Marke ist das Verletzungsgericht an die Eintragung gebunden – absolute Schutzhindernisse werden nicht geprüft (Einwand nur über Löschungsverfahren/Widerklage, ggf. Aussetzung).",
                     concepts=["entstehung_markenschutz", "verkehrsgeltung", "notorische_bekanntheit"], norms=["§ 4"], cases=["bgh_langenscheidt_gelb"]),
                step("2. Aktivlegitimation", "Markeninhaber (§ 28 Abs. 1 Vermutung) oder Lizenznehmer mit Zustimmung (§ 30 Abs. 3).", concepts=["aktivlegitimation", "lizenz"], norms=["§ 28", "§ 30 Abs. 3"]),
                step("3. Zeitrang / Priorität", "Die Klagemarke muss gegenüber dem angegriffenen Zeichen prioritätsälter sein (§ 6); der Beklagte kann ein eigenes älteres Recht einwenden.", concepts=["prioritaet"], norms=["§ 6"]),
            ]),
            step("C. Verletzungshandlung (§ 14 Abs. 2)", children=[
                step("1. Benutzung im geschäftlichen Verkehr", concepts=["geschaeftlicher_verkehr"], norms=["§ 14 Abs. 2"]),
                step("2. Ohne Zustimmung des Markeninhabers", "Zustimmung z.B. durch Lizenz (§ 30); Grenzen des § 30 Abs. 2 beachten.", concepts=["lizenz"]),
                step("3. Benutzungshandlung", "Benutzung für Waren/Dienstleistungen, insbesondere die Handlungen des § 14 Abs. 3 (Anbringen, Anbieten, Inverkehrbringen, Ein-/Ausfuhr, Verwendung in Geschäftspapieren und Werbung, Verwendung als Handelsname) und Vorbereitungshandlungen nach § 14 Abs. 4.", norms=["§ 14 Abs. 3", "§ 14 Abs. 4"]),
                step("4. Markenmäßige (rechtsverletzende) Benutzung", "Beeinträchtigung einer Markenfunktion, insbesondere der Herkunftsfunktion: Der Verkehr versteht das Zeichen als Herkunftshinweis. Abgrenzung zur rein beschreibenden, dekorativen oder firmenmäßigen Verwendung.",
                     concepts=["markenmaessige_benutzung", "herkunftsfunktion", "markenfunktionen", "firmenmaessiger_gebrauch", "keyword_advertising"],
                     cases=["eugh_arsenal", "bgh_opel_blitz_ii", "bgh_sam", "bgh_damen_hose_mo", "bgh_fruehstuecks_drink_ii", "eugh_google_france"]),
                step("5. Kollisionstatbestand", children=[
                    step("a) § 14 Abs. 2 Nr. 1 – Doppelidentität", "Zeichenidentität + Waren-/Dienstleistungsidentität. Keine Verwechslungsgefahr erforderlich; Beeinträchtigung irgendeiner Markenfunktion genügt.",
                         concepts=["doppelidentitaet", "markenfunktionen"], norms=["§ 14 Abs. 2 Nr. 1"], cases=["eugh_loreal_bellure", "bgh_kuehlergrill", "bgh_grosse_inspektion"]),
                    step("b) § 14 Abs. 2 Nr. 2 – Verwechslungsgefahr", "Zeichenidentität/-ähnlichkeit + Waren-/Dienstleistungsidentität/-ähnlichkeit + Verwechslungsgefahr (siehe eigenes Schema).",
                         concepts=["verwechslungsgefahr", "wechselwirkung"], norms=["§ 14 Abs. 2 Nr. 2"], cases=["eugh_sabel_puma", "eugh_canon", "bgh_culinaria"]),
                    step("c) § 14 Abs. 2 Nr. 3 – Bekanntheitsschutz", "Bekannte Marke + Zeichenidentität/-ähnlichkeit + gedankliche Verknüpfung + Ausnutzung/Beeinträchtigung der Unterscheidungskraft oder Wertschätzung + ohne rechtfertigenden Grund in unlauterer Weise (siehe eigenes Schema).",
                         concepts=["bekannte_marke", "gedankliche_verknuepfung", "unlauterkeit"], norms=["§ 14 Abs. 2 Nr. 3"], cases=["bgh_otto_cap", "bgh_lila_postkarte"]),
                ]),
            ]),
            step("D. Keine Schranken / Einwendungen", children=[
                step("1. § 23 – Namen, beschreibende Angaben, Bestimmungshinweis", concepts=["schranke_23", "ersatzteilhinweis", "gleichnamigkeit"], norms=["§ 23"], cases=["eugh_gillette", "bgh_staubsaugerfiltertueten", "bgh_kuehlergrill"]),
                step("2. § 24 – Erschöpfung", concepts=["erschoepfung", "berechtigte_gruende", "beweislast_erschoepfung"], norms=["§ 24"], cases=["eugh_van_doren", "bgh_stuessy_ii", "eugh_bms"]),
                step("3. § 25 – Einrede der Nichtbenutzung", "Nach Ablauf der Benutzungsschonfrist: Inhaber muss rechtserhaltende Benutzung nachweisen (§ 26).", concepts=["nichtbenutzungseinrede", "rechtserhaltende_benutzung", "benutzungsschonfrist"], norms=["§ 25", "§ 26"], cases=["bgh_voodoo"]),
                step("4. § 21 – Verwirkung; § 22 – Bestandskraft jüngerer Marke", concepts=["verwirkung"], norms=["§ 21", "§ 22"], cases=["bgh_hard_rock_cafe"]),
                step("5. Älteres Recht des Beklagten (§ 6) / Löschungsreife der Klagemarke", "Einrede des besseren Zeitrangs; Löschungsreife der Klagemarke wegen Verfalls (§ 49) oder Nichtigkeit (§§ 50, 51) – im Verletzungsprozess über Widerklage bzw. § 52.", concepts=["prioritaet", "verfall", "nichtigkeit"], norms=["§ 6", "§ 49", "§ 50", "§ 51", "§ 52"]),
                step("6. Verjährung (§ 20)", concepts=["verjaehrung"], norms=["§ 20"]),
            ]),
            step("E. Rechtsfolge: Unterlassung (§ 14 Abs. 5)", "Wiederholungsgefahr (vermutet nach Verletzung; Wegfall nur durch strafbewehrte Unterlassungserklärung) oder Erstbegehungsgefahr (§ 14 Abs. 5 S. 2). Kein Verschulden erforderlich. Passivlegitimation: Täter, Teilnehmer, Störer.",
                 concepts=["unterlassungsanspruch", "stoererhaftung"], norms=["§ 14 Abs. 5"], cases=["bgh_internet_versteigerung_ii", "bgh_kinderhochstuehle"]),
            step("F. Weitere Ansprüche", children=[
                step("Schadensersatz (§ 14 Abs. 6)", "Zusätzlich: Verschulden (Vorsatz/Fahrlässigkeit). Dreifache Schadensberechnung: konkreter Schaden, Verletzergewinn, Lizenzanalogie. Haftung für Angestellte/Beauftragte (§ 14 Abs. 7).", concepts=["schadensersatz", "lizenzanalogie"], norms=["§ 14 Abs. 6", "§ 14 Abs. 7"], cases=["bgh_btk"]),
                step("Vernichtung/Rückruf (§ 18), Auskunft (§ 19), Vorlage (§ 19a), Urteilsbekanntmachung (§ 19c)", concepts=["vernichtung_auskunft"], norms=["§ 18", "§ 19", "§ 19a", "§ 19c"]),
                step("Bereicherung (§ 812 BGB), GoA; Ansprüche aus anderen Vorschriften (§ 19d): UWG, § 12 BGB", concepts=["verhaeltnis_uwg"], norms=["§ 19d", "§ 2"]),
            ]),
        ],
    ),
    dict(
        id="schema_verwechslungsgefahr",
        label="Verwechslungsgefahr (§ 14 Abs. 2 Nr. 2 / § 9 Abs. 1 Nr. 2 MarkenG)",
        kategorie="Verletzung",
        beschreibung="Umfassende Beurteilung aller Umstände des Einzelfalls unter Berücksichtigung der Wechselwirkung zwischen Waren-/Dienstleistungsähnlichkeit, Kennzeichnungskraft der älteren Marke und Zeichenähnlichkeit.",
        norms=["§ 14 Abs. 2 Nr. 2", "§ 9 Abs. 1 Nr. 2"],
        steps=[
            step("1. Maßgebliche Verkehrskreise und Aufmerksamkeitsgrad", "Normal informierter, angemessen aufmerksamer und verständiger Durchschnittsverbraucher der konkreten Waren; bei gespaltener Verkehrsauffassung genügt Verwechslungsgefahr in einer Gruppe.",
                 concepts=["durchschnittsverbraucher"], cases=["eugh_lloyd", "bgh_maalox"]),
            step("2. Waren-/Dienstleistungsidentität oder -ähnlichkeit", "Registerlage der Klagemarke vs. konkret benutzte Waren. Faktoren: Art, Verwendungszweck, Nutzung, Konkurrenz-/Ergänzungsverhältnis, Herstellungsstätten, Vertriebswege. Bei absoluter Unähnlichkeit: Ende der Prüfung (ggf. Nr. 3).",
                 concepts=["warenaehnlichkeit"], cases=["eugh_canon", "bgh_desperados"]),
            step("3. Kennzeichnungskraft der älteren Marke", "Originäre Kennzeichnungskraft (Eigenart des Zeichens; beschreibende Anklänge schwächen) → Steigerung durch Benutzung/Bekanntheit → Schwächung durch Drittzeichen. Ergebnis: sehr gering / gering / durchschnittlich / erhöht / sehr hoch. Bei verkehrsdurchgesetzten Marken: regelmäßig durchschnittlich.",
                 concepts=["kennzeichnungskraft", "verkehrsdurchsetzung"], cases=["bgh_culinaria", "bgh_kinder_ii", "bgh_lacoste_krokodil"]),
            step("4. Zeichenidentität oder -ähnlichkeit", children=[
                step("a) Gesamteindruck", "Vergleich der Zeichen in ihrer Gesamtheit aus dem Erinnerungsbild; keine zergliedernde Betrachtung.", concepts=["gesamteindruck"], cases=["eugh_sabel_puma"]),
                step("b) Prägung durch einzelne Bestandteile", "Prägetheorie: Ein Bestandteil prägt, wenn die anderen zurücktreten; beschreibende Bestandteile prägen nicht; bekannte Herstellerangaben treten regelmäßig zurück.", concepts=["praegetheorie"], cases=["bgh_springende_raubkatze", "bgh_metrobus"]),
                step("c) Ähnlichkeit nach Klang, Bild, Sinngehalt", "Ähnlichkeit in einer Richtung genügt; Neutralisierung klanglicher Ähnlichkeit durch abweichenden Sinngehalt möglich. Wortmarke vs. 3D-Gestaltung: nur begriffliche Ähnlichkeit.", concepts=["zeichenaehnlichkeit"], cases=["bgh_goldbaeren", "bgh_ips_isp", "bgh_maalox"]),
                step("d) Selbständig kennzeichnende Stellung", "Übernahme der älteren Marke in ein zusammengesetztes Zeichen (THOMSON LIFE) – Ausnahmefall, besondere Umstände erforderlich.", concepts=["selbstaendig_kennzeichnende_stellung"], cases=["eugh_thomson_life", "bgh_culinaria", "bgh_interconnect"]),
            ]),
            step("5. Gesamtabwägung (Wechselwirkung)", "Geringere Warenähnlichkeit kann durch höhere Zeichenähnlichkeit oder erhöhte Kennzeichnungskraft ausgeglichen werden und umgekehrt.", concepts=["wechselwirkung"], cases=["eugh_canon", "bgh_culinaria"]),
            step("6. Art der Verwechslungsgefahr", "Unmittelbar (Zeichen werden verwechselt) – mittelbar (Serienzeichen, gemeinsamer Stammbestandteil) – im weiteren Sinne (Annahme wirtschaftlicher/organisatorischer Verbindungen; Ausnahme, besondere Umstände).",
                 concepts=["verwechslungsgefahr_weiterer_sinn", "serienmarke"], cases=["bgh_mustang", "bgh_volkswagen_volksinspektion"]),
        ],
    ),
    dict(
        id="schema_bekanntheitsschutz",
        label="Bekanntheitsschutz (§ 14 Abs. 2 Nr. 3 MarkenG)",
        kategorie="Verletzung",
        beschreibung="Erweiterter Schutz bekannter Marken über die Herkunftsfunktion hinaus – auch außerhalb des Ähnlichkeitsbereichs der Waren und ohne Verwechslungsgefahr.",
        norms=["§ 14 Abs. 2 Nr. 3", "§ 9 Abs. 1 Nr. 3"],
        steps=[
            step("1. Bekannte Marke im Inland", "Bekanntheit bei einem bedeutenden Teil des von den Waren/Dienstleistungen angesprochenen Publikums; keine festen Prozentsätze; Faktoren: Marktanteil, Intensität, Dauer, Werbeaufwand. Maßgeblicher Zeitpunkt: Kollisionszeitpunkt (Verletzung) bzw. Anmeldetag des jüngeren Zeichens.",
                 concepts=["bekannte_marke"], cases=["eugh_general_motors", "bgh_tuev_ii"]),
            step("2. Zeichenidentität oder -ähnlichkeit", "Gleiche Maßstäbe wie bei Nr. 2, aber es genügt ein Grad der Ähnlichkeit, der zur gedanklichen Verknüpfung führt.", concepts=["zeichenaehnlichkeit"], cases=["bgh_goldbaeren", "bgh_springender_pudel"]),
            step("3. Benutzung für Waren/Dienstleistungen (auch bei Identität/Ähnlichkeit)", "Nach richtlinienkonformer Auslegung auch im Ähnlichkeitsbereich anwendbar (OTTO Cap). Markenmäßige Benutzung: gedankliche Verknüpfung genügt; Beeinträchtigung der Herkunftsfunktion nicht erforderlich.", concepts=["markenmaessige_benutzung"], cases=["bgh_otto_cap", "bgh_lila_postkarte"]),
            step("4. Gedankliche Verknüpfung", "Der Verkehr bringt das Zeichen mit der bekannten Marke in Verbindung (Assoziation), ohne sie zu verwechseln. Notwendige, aber nicht hinreichende Voraussetzung.", concepts=["gedankliche_verknuepfung"], cases=["eugh_intel", "bgh_metrobus"]),
            step("5. Eingriffstatbestand (eine Alternative genügt)", children=[
                step("a) Ausnutzung der Unterscheidungskraft (Aufmerksamkeitsausbeutung)", concepts=["ausnutzung_unterscheidungskraft"], cases=["bgh_otto_cap", "bgh_springender_pudel"]),
                step("b) Ausnutzung der Wertschätzung (Rufausbeutung, Imagetransfer)", concepts=["ausnutzung_wertschaetzung"], cases=["eugh_loreal_bellure", "bgh_oeko_test_ii"]),
                step("c) Beeinträchtigung der Unterscheidungskraft (Verwässerung)", "Nachweis der (Gefahr einer) Änderung des wirtschaftlichen Verhaltens der Verbraucher (Intel).", concepts=["verwaesserung"], cases=["eugh_intel"]),
                step("d) Beeinträchtigung der Wertschätzung (Rufschädigung/Verunglimpfung)", concepts=["rufschaedigung"], cases=["bgh_lila_postkarte"]),
            ]),
            step("6. Ohne rechtfertigenden Grund in unlauterer Weise", "Umfassende Interessenabwägung; Grundrechte (Kunst-, Meinungsfreiheit), zulässige vergleichende Werbung, Alternativangebot bei Keyword-Werbung als rechtfertigende Gründe.", concepts=["unlauterkeit"], cases=["bgh_lila_postkarte", "eugh_interflora", "eugh_loreal_bellure"]),
            step("7. Keine Schranken (§§ 23, 24)", concepts=["schranke_23", "erschoepfung"], cases=["bgh_tuev_ii"]),
        ],
    ),
    dict(
        id="schema_eintragungsfaehigkeit",
        label="Schutzfähigkeit / Eintragungsfähigkeit einer Marke (§§ 3, 7, 8 MarkenG)",
        kategorie="Schutzvoraussetzungen",
        beschreibung="Prüfung im Eintragungsverfahren (§§ 36, 37) und im Nichtigkeitsverfahren (§ 50). Reihenfolge: Markenfähigkeit → Inhaberschaft → Darstellbarkeit → absolute Schutzhindernisse → Verkehrsdurchsetzung.",
        norms=["§ 3", "§ 7", "§ 8", "§ 37", "§ 50"],
        steps=[
            step("1. Markenfähigkeit (§ 3 Abs. 1)", "Abstrakte Unterscheidungseignung des Zeichens (losgelöst von den konkreten Waren). Nur ausnahmsweise zu verneinen.", concepts=["markenfaehigkeit"], cases=["eugh_libertel"]),
            step("2. Kein Formausschluss (§ 3 Abs. 2)", "Form/charakteristisches Merkmal durch Art der Ware bedingt (Nr. 1), technisch erforderlich (Nr. 2) oder wertverleihend (Nr. 3)? Nicht durch Verkehrsdurchsetzung überwindbar.", concepts=["formausschluss", "formmarke"], cases=["bgh_ritter_sport", "bgh_bodenduebel", "eugh_philips_remington"]),
            step("3. Inhaberschaft (§ 7)", "Natürliche Personen, juristische Personen, rechtsfähige Personengesellschaften.", norms=["§ 7"]),
            step("4. Darstellbarkeit im Register (§ 8 Abs. 1)", "Klare und eindeutige Bestimmbarkeit des Schutzgegenstands (Sieckmann-Kriterien); graphische Darstellbarkeit nicht mehr erforderlich.", concepts=["darstellbarkeit"]),
            step("5. Keine absoluten Schutzhindernisse (§ 8 Abs. 2)", concepts=["absolute_schutzhindernisse"], children=[
                step("Nr. 1 – Fehlende Unterscheidungskraft", "Konkrete Eignung als Herkunftshinweis für die beanspruchten Waren; großzügiger Maßstab; alle praktisch bedeutsamen Verwendungsformen; Sicht des Durchschnittsverbrauchers im Anmeldezeitpunkt.", concepts=["unterscheidungskraft", "verwendungsformen"], cases=["bgh_hot", "bgh_darferdas_ii", "bgh_link_economy", "bgh_for_you", "bgh_pippi_langstrumpf"]),
                step("Nr. 2 – Freihaltebedürfnis an beschreibenden Angaben", "Kann die Angabe zur Beschreibung von Merkmalen der Waren dienen (auch künftig)? Allgemeininteresse der Mitbewerber.", concepts=["freihaltebeduerfnis"], cases=["bgh_black_friday", "eugh_chiemsee"]),
                step("Nr. 3 – Üblich gewordene Bezeichnungen", concepts=["uebliche_bezeichnung"]),
                step("Nr. 4 – Täuschungseignung (nur wenn ersichtlich, § 37 Abs. 3)", concepts=["taeuschung"]),
                step("Nr. 5 – Verstoß gegen öffentliche Ordnung / gute Sitten", norms=["§ 8 Abs. 2 Nr. 5"]),
                step("Nr. 6-8 – Hoheitszeichen, amtliche Prüfzeichen, Kennzeichen internationaler Organisationen", norms=["§ 8 Abs. 2 Nr. 6", "§ 8 Abs. 2 Nr. 7", "§ 8 Abs. 2 Nr. 8"]),
                step("Nr. 9-13 – Sonstige gesetzliche Verbote, geschützte Ursprungsbezeichnungen, traditionelle Bezeichnungen, Sortenbezeichnungen", norms=["§ 8 Abs. 2 Nr. 9"]),
                step("Nr. 14 – Bösgläubige Anmeldung (nur wenn ersichtlich, § 37 Abs. 3)", concepts=["boesglaeubigkeit"], cases=["bgh_glueckspilz", "bgh_eros"]),
            ]),
            step("6. Überwindung von Nr. 1-3 durch Verkehrsdurchsetzung (§ 8 Abs. 3)", "Durchsetzung in den beteiligten Verkehrskreisen vor dem Anmeldetag; Richtwert mind. 50 % Zuordnung; Nachweis v.a. durch demoskopisches Gutachten.", concepts=["verkehrsdurchsetzung"], cases=["eugh_chiemsee", "bgh_test", "bgh_nivea_blau", "bgh_rocher_kugel"]),
            step("7. Verfahren", "Prüfung von Amts wegen (§ 37); Zurückweisung; Beschwerde BPatG (§ 66); Rechtsbeschwerde BGH (§ 83). Nach Eintragung: Nichtigkeit § 50 (Feststellungslast beim Antragsteller; Zehnjahresfrist für Nr. 1-3).", concepts=["nichtigkeit"], norms=["§ 37", "§ 66", "§ 83", "§ 50"], cases=["bgh_smartbook", "bgh_sparkassen_rot"]),
        ],
    ),
    dict(
        id="schema_schranke_23",
        label="Schranke des § 23 MarkenG (Namen, beschreibende Angaben, Bestimmungshinweis)",
        kategorie="Schranken",
        beschreibung="Einwendung des Verletzers: Auch eine an sich tatbestandsmäßige Benutzung kann nicht untersagt werden, wenn sie einer der drei Fallgruppen unterfällt und den anständigen Gepflogenheiten entspricht.",
        norms=["§ 23"],
        steps=[
            step("1. Tatbestand des § 14 Abs. 2 erfüllt", "§ 23 ist erst zu prüfen, wenn eine rechtsverletzende Benutzung vorliegt (bei rein beschreibender Verwendung fehlt bereits die markenmäßige Benutzung).", concepts=["markenmaessige_benutzung"]),
            step("2. Fallgruppe", children=[
                step("Nr. 1 – Name oder Anschrift des Dritten", "Nur natürliche Personen (nach MaMoG). Recht der Gleichnamigen.", concepts=["gleichnamigkeit"], cases=["bgh_peek_cloppenburg"]),
                step("Nr. 2 – Zeichen ohne Unterscheidungskraft / beschreibende Angaben", "Benutzung von Angaben über Art, Beschaffenheit, Bestimmung usw. – auch wenn sie mit einer (verkehrsdurchgesetzten) Marke identisch sind.", concepts=["freihaltebeduerfnis", "schranke_23"], cases=["bgh_tuev_ii"]),
                step("Nr. 3 – Bestimmungshinweis (Zubehör, Ersatzteile, Kompatibilität)", "Benutzung muss notwendig sein: praktisch einziges Mittel, um über die Bestimmung zu informieren (Gillette). Wortmarke statt Logo; keine Emblem-Nachbildung.", concepts=["ersatzteilhinweis"], cases=["eugh_gillette", "bgh_staubsaugerfiltertueten", "bgh_kuehlergrill", "bgh_grosse_inspektion"]),
            ]),
            step("3. Anständige Gepflogenheiten in Gewerbe oder Handel (§ 23 Abs. 2)", "Verstoß, wenn (a) eine geschäftliche Verbindung zum Markeninhaber suggeriert wird, (b) die Unterscheidungskraft/Wertschätzung unlauter ausgenutzt wird, (c) die Marke herabgesetzt wird oder (d) die eigene Ware als Imitation dargestellt wird. Die Eigenmarke muss im Vordergrund stehen.", concepts=["schranke_23"], cases=["eugh_gillette", "bgh_staubsaugerfiltertueten"]),
        ],
    ),
    dict(
        id="schema_erschoepfung",
        label="Erschöpfung (§ 24 MarkenG)",
        kategorie="Schranken",
        beschreibung="Einwendung gegen Ansprüche wegen des Weitervertriebs von Originalware.",
        norms=["§ 24"],
        steps=[
            step("1. Originalware (Echtheit)", "Die konkrete Ware wurde vom Markeninhaber oder mit seiner Zustimmung mit der Marke versehen. Bei Bestreiten: Beweislast beim Beklagten (Converse I).", concepts=["beweislast_erschoepfung"], cases=["bgh_converse_i"]),
            step("2. Inverkehrbringen im Inland, in der EU oder im EWR", "Übertragung der tatsächlichen Verfügungsgewalt mit Verwertungsmöglichkeit innerhalb des EWR. Keine internationale Erschöpfung: Ware aus Drittstaaten ist nicht erschöpft.", concepts=["erschoepfung"], cases=["eugh_van_doren", "bgh_stuessy_ii"]),
            step("3. Durch den Inhaber oder mit seiner Zustimmung", "Zustimmung durch Lizenz; Verstoß des Lizenznehmers gegen § 30 Abs. 2 = ohne Zustimmung (Converse II). Beweislast grundsätzlich beim Beklagten; Umkehr bei ausschließlichem Vertriebssystem und Marktabschottungsgefahr.", concepts=["lizenz", "beweislast_erschoepfung"], cases=["bgh_converse_ii", "eugh_van_doren"]),
            step("4. Keine berechtigten Gründe (§ 24 Abs. 2)", "Veränderung/Verschlechterung der Ware; Umverpacken nur nach den BMS-Kriterien; erhebliche Rufschädigung durch Werbung (Dior/Evora); Suggestion einer Vertragshändlerbeziehung.", concepts=["berechtigte_gruende", "umverpackung"], cases=["eugh_bms", "eugh_dior_evora"]),
            step("5. Reichweite", "Erschöpfung erfasst Weitervertrieb und Werbung für die konkreten Warenstücke; nicht die Verwendung der Marke für andere Waren oder als Unternehmenskennzeichen.", concepts=["erschoepfung"]),
        ],
    ),
    dict(
        id="schema_benutzungszwang",
        label="Rechtserhaltende Benutzung und Verfall (§§ 25, 26, 49 MarkenG)",
        kategorie="Benutzungszwang",
        beschreibung="Prüfung der Nichtbenutzungseinrede (§ 25 im Verletzungsprozess, § 43 Abs. 1 im Widerspruchsverfahren) und des Verfallsantrags (§ 49 Abs. 1).",
        norms=["§ 25", "§ 26", "§ 49"],
        steps=[
            step("1. Ablauf der Benutzungsschonfrist", "Fünf Jahre seit Eintragung bzw. seit Abschluss des Widerspruchsverfahrens (§ 26 Abs. 5). Vorher ist die Einrede unbeachtlich.", concepts=["benutzungsschonfrist"]),
            step("2. Maßgeblicher Fünfjahreszeitraum", "§ 25 Abs. 2: fünf Jahre vor Klageerhebung (und ggf. vor Schluss der mündlichen Verhandlung); § 49 Abs. 1: ununterbrochene fünf Jahre vor dem Löschungsantrag; Heilung durch Benutzungsaufnahme (§ 49 Abs. 1 S. 2, 3).", concepts=["nichtbenutzungseinrede", "verfall"]),
            step("3. Voraussetzungen der rechtserhaltenden Benutzung (§ 26)", children=[
                step("a) Ernsthafte Benutzung", "Benutzung entsprechend der Hauptfunktion zur Erschließung/Sicherung eines Absatzmarkts; keine Scheinbenutzung; kein Mindestumfang.", concepts=["ernsthafte_benutzung"], cases=["eugh_ansul", "bgh_voodoo"]),
                step("b) Benutzung als Marke (funktionsgemäß)", "Der Verkehr muss die Verwendung als Herkunftshinweis für die Waren verstehen; rein firmenmäßige oder beschreibende Verwendung genügt nicht (aber: LOTTOCARD).", concepts=["rechtserhaltende_benutzung", "markenmaessige_benutzung"], cases=["bgh_lottocard"]),
                step("c) Für die eingetragenen Waren/Dienstleistungen", "Teilbenutzung: Bei Oberbegriffen bleibt der Schutz für die Untergruppe erhalten, der die benutzten Waren angehören (Integrationsfrage, § 49 Abs. 3).", norms=["§ 49 Abs. 3"]),
                step("d) Im Inland", "Auch Anbringen auf Waren/Verpackungen allein für den Export genügt (§ 26 Abs. 4).", norms=["§ 26 Abs. 1", "§ 26 Abs. 4"]),
                step("e) Durch den Inhaber oder mit seiner Zustimmung (§ 26 Abs. 2)", "Lizenznehmer, Konzernunternehmen.", concepts=["lizenz"]),
                step("f) In eingetragener oder nur unwesentlich abweichender Form (§ 26 Abs. 3)", "Kennzeichnender Charakter darf nicht verändert werden; unschädliche Zusätze vs. Verschmelzung zu neuem Gesamtzeichen.", concepts=["abweichende_form"], cases=["bgh_probiotik", "bgh_dorzo"]),
            ]),
            step("4. Berechtigte Gründe für die Nichtbenutzung", "Hindernisse außerhalb des Einflussbereichs des Inhabers (z.B. Zulassungsverfahren, Einfuhrverbote), nicht bloße wirtschaftliche Schwierigkeiten.", norms=["§ 26 Abs. 1"]),
            step("5. Beweis-/Glaubhaftmachungslast", "Verletzungsprozess: voller Beweis durch den Markeninhaber; Widerspruchsverfahren: Glaubhaftmachung (§ 43 Abs. 1); Verfallsverfahren: Inhaber muss Benutzung darlegen (§ 53 Abs. 5, § 55 Abs. 3).", concepts=["nichtbenutzungseinrede"], norms=["§ 43 Abs. 1", "§ 53", "§ 55"], cases=["bgh_voodoo"]),
            step("6. Rechtsfolge", "Einrede: Ansprüche ausgeschlossen (§ 25). Verfall: Löschung mit Wirkung ab Antrag oder früherem Verfallszeitpunkt (§ 52 Abs. 1).", concepts=["verfall"], norms=["§ 52"]),
        ],
    ),
    dict(
        id="schema_unternehmenskennzeichen",
        label="Schutz geschäftlicher Bezeichnungen (§§ 5, 15 MarkenG)",
        kategorie="Geschäftliche Bezeichnungen",
        beschreibung="Unterlassungsanspruch aus § 15 Abs. 4 i.V.m. Abs. 2 (Verwechslungsgefahr) oder Abs. 3 (bekannte geschäftliche Bezeichnung).",
        norms=["§ 5", "§ 15"],
        steps=[
            step("1. Schutzfähige geschäftliche Bezeichnung (§ 5)", children=[
                step("a) Unternehmenskennzeichen (§ 5 Abs. 2)", "Name, Firma, besondere Geschäftsbezeichnung; Firmenschlagwort/-bestandteil; Domain. Entstehung: Benutzungsaufnahme im Inland + originäre Unterscheidungskraft, sonst Verkehrsgeltung (§ 5 Abs. 2 S. 2 für Geschäftsabzeichen).", concepts=["unternehmenskennzeichen", "firmenschlagwort", "domain"], cases=["bgh_soco_de", "bgh_defacto", "bgh_baumann_ii"]),
                step("b) Werktitel (§ 5 Abs. 3)", "Titelschutzfähiges Werk (Druckschrift, Film, Ton, Bühne, Software, App, Website); Unterscheidungskraft (abgesenkter Maßstab bei Verkehrsgewöhnung); Benutzungsaufnahme / Titelschutzanzeige.", concepts=["werktitel"], cases=["bgh_wetter_de", "bgh_das_omen"]),
            ]),
            step("2. Priorität (§ 6)", "Zeitpunkt der Benutzungsaufnahme bzw. des Erwerbs der Verkehrsgeltung; Vergleich mit dem Zeitrang des angegriffenen Zeichens.", concepts=["prioritaet"]),
            step("3. Verletzungshandlung (§ 15 Abs. 2)", "Unbefugte Benutzung im geschäftlichen Verkehr in einer Weise, die geeignet ist, Verwechslungen hervorzurufen: Wechselwirkung von Branchennähe, Kennzeichnungskraft und Zeichenähnlichkeit. Kennzeichenmäßige Benutzung erforderlich.", concepts=["branchennaehe", "kennzeichnungskraft", "zeichenaehnlichkeit", "verwechslungsgefahr"], cases=["bgh_defacto", "bgh_augsburger_puppenkiste"]),
            step("4. Alternativ: Bekannte geschäftliche Bezeichnung (§ 15 Abs. 3)", "Parallel zu § 14 Abs. 2 Nr. 3: Ausnutzung/Beeinträchtigung der Unterscheidungskraft oder Wertschätzung ohne rechtfertigenden Grund.", concepts=["bekannte_marke"]),
            step("5. Schranken", "§ 23 (insb. Gleichnamigkeit), § 21 Verwirkung, § 20 Verjährung; Recht der Gleichnamigen bei redlichem Namensgebrauch.", concepts=["gleichnamigkeit", "verwirkung"], cases=["bgh_peek_cloppenburg", "bgh_shell_de"]),
            step("6. Rechtsfolgen (§ 15 Abs. 4-6)", "Unterlassung, Schadensersatz bei Verschulden, Haftung für Angestellte; §§ 18, 19 entsprechend.", concepts=["unterlassungsanspruch", "schadensersatz"]),
        ],
    ),
    dict(
        id="schema_widerspruch",
        label="Widerspruchsverfahren (§§ 42, 43 MarkenG) und relative Schutzhindernisse (§ 9)",
        kategorie="Verfahren",
        beschreibung="Registerrechtliche Kollisionsprüfung nach Eintragung der jüngeren Marke.",
        norms=["§ 42", "§ 43", "§ 9"],
        steps=[
            step("1. Zulässigkeit des Widerspruchs", "Frist: drei Monate ab Veröffentlichung der Eintragung (§ 42 Abs. 1); Widerspruchsberechtigung: Inhaber eines in § 42 Abs. 2 genannten älteren Rechts (Marke, notorisch bekannte Marke, Benutzungsmarke/geschäftliche Bezeichnung, Ursprungsbezeichnung); Gebühr.", concepts=["widerspruch", "relative_schutzhindernisse"]),
            step("2. Einrede der Nichtbenutzung (§ 43 Abs. 1)", "Wenn die Widerspruchsmarke seit mehr als fünf Jahren eingetragen ist: Glaubhaftmachung der rechtserhaltenden Benutzung; nur die glaubhaft gemachten Waren werden berücksichtigt (§ 43 Abs. 1 S. 3).", concepts=["nichtbenutzungseinrede", "rechtserhaltende_benutzung"]),
            step("3. Begründetheit: Kollisionstatbestand des § 9 Abs. 1", children=[
                step("Nr. 1 – Identität von Marke und Waren", concepts=["doppelidentitaet"]),
                step("Nr. 2 – Verwechslungsgefahr (Registerlage)", "Vergleich nach den Verzeichnissen beider Marken; sonst wie § 14 Abs. 2 Nr. 2.", concepts=["verwechslungsgefahr", "wechselwirkung"], cases=["bgh_maalox", "bgh_desperados", "bgh_culinaria"]),
                step("Nr. 3 – Bekannte ältere Marke", concepts=["bekannte_marke"], cases=["bgh_springender_pudel"]),
            ]),
            step("4. Entscheidung und Rechtsmittel", "Löschung der jüngeren Marke ganz oder teilweise (§ 43 Abs. 2); Beschwerde zum BPatG (§ 66), Rechtsbeschwerde zum BGH (§ 83); alternativ Nichtigkeitsverfahren nach § 51 (auch mit Rechten aus § 13) vor DPMA (§ 53) oder Gericht (§ 55).", concepts=["nichtigkeit"], norms=["§ 43 Abs. 2", "§ 51", "§ 53", "§ 55", "§ 66", "§ 83"]),
        ],
    ),
    dict(
        id="schema_loeschung",
        label="Löschung eingetragener Marken: Verfall (§ 49) und Nichtigkeit (§§ 50, 51)",
        kategorie="Verfahren",
        beschreibung="Angriffe gegen den Bestand einer eingetragenen Marke.",
        norms=["§ 49", "§ 50", "§ 51", "§ 52", "§ 53", "§ 55"],
        steps=[
            step("1. Verfall (§ 49) – ex nunc, Popularantrag", children=[
                step("Abs. 1 – Nichtbenutzung über fünf Jahre", concepts=["verfall", "rechtserhaltende_benutzung", "benutzungsschonfrist"], cases=["bgh_voodoo"]),
                step("Abs. 2 Nr. 1 – Entwicklung zur gebräuchlichen Bezeichnung infolge Verhaltens/Untätigkeit des Inhabers", concepts=["uebliche_bezeichnung"], cases=["bgh_tuev_ii"]),
                step("Abs. 2 Nr. 2 – Täuschungseignung infolge der Benutzung", concepts=["taeuschung"]),
                step("Abs. 2 Nr. 3 – Wegfall der Inhabervoraussetzungen (§ 7)", norms=["§ 7"]),
            ]),
            step("2. Nichtigkeit wegen absoluter Schutzhindernisse (§ 50) – ex tunc, Popularantrag", "Verstoß gegen §§ 3, 7, 8 im Anmeldezeitpunkt; bei § 8 Abs. 2 Nr. 1-3 muss das Hindernis noch im Entscheidungszeitpunkt fortbestehen und der Antrag innerhalb von zehn Jahren gestellt werden (§ 50 Abs. 2). Feststellungslast: Antragsteller.", concepts=["nichtigkeit", "absolute_schutzhindernisse", "boesglaeubigkeit"], cases=["bgh_smartbook", "bgh_sparkassen_rot", "bgh_black_friday", "bgh_ritter_sport", "bgh_test"]),
            step("3. Nichtigkeit wegen älterer Rechte (§ 51) – ex tunc, nur Inhaber des älteren Rechts", "Kollision nach §§ 9-13; Ausschluss bei Verwirkung (§ 51 Abs. 2), Zustimmung (§ 51 Abs. 3) und Löschungsreife des älteren Rechts (§ 51 Abs. 4).", concepts=["nichtigkeit", "relative_schutzhindernisse", "verwirkung"], cases=["bgh_springender_pudel"]),
            step("4. Verfahren", "Antrag beim DPMA (§ 53; bei Widerspruch des Inhabers Weiterführung als kontradiktorisches Verfahren) oder Klage vor dem Landgericht (§ 55; für § 50 seit MaMoG nur DPMA). Wirkung: § 52.", concepts=["verfall", "nichtigkeit"], norms=["§ 52", "§ 53", "§ 55"]),
        ],
    ),
    dict(
        id="schema_entstehung",
        label="Entstehung und Erlöschen des Markenschutzes (§§ 4, 32 ff., 47 ff.)",
        kategorie="Grundlagen",
        beschreibung="Lebenszyklus einer Marke vom Erwerb bis zum Erlöschen.",
        norms=["§ 4", "§ 32", "§ 33", "§ 47", "§ 48"],
        steps=[
            step("1. Entstehung (§ 4)", children=[
                step("Nr. 1 – Eintragung", "Anmeldung (§ 32: Antrag, Wiedergabe, Waren-/Dienstleistungsverzeichnis) → Anmeldetag (§ 33) → Prüfung (§§ 36, 37) → Eintragung und Veröffentlichung (§ 41) → Widerspruchsfrist (§ 42).", concepts=["entstehung_markenschutz", "absolute_schutzhindernisse"], norms=["§ 32", "§ 33", "§ 36", "§ 37", "§ 41"]),
                step("Nr. 2 – Verkehrsgeltung durch Benutzung", concepts=["verkehrsgeltung"]),
                step("Nr. 3 – Notorische Bekanntheit", concepts=["notorische_bekanntheit"]),
            ]),
            step("2. Zeitrang (§ 6) und Priorität (§§ 34, 35)", "Anmeldetag; ausländische Priorität (PVÜ, 6 Monate); Ausstellungspriorität.", concepts=["prioritaet"]),
            step("3. Schutzdauer und Verlängerung (§ 47)", "Zehn Jahre ab Anmeldetag, beliebig oft um zehn Jahre verlängerbar durch Gebührenzahlung.", norms=["§ 47"]),
            step("4. Marke als Vermögensgegenstand (§§ 27-31)", "Rechtsübergang (§ 27), Vermutung der Inhaberschaft (§ 28), dingliche Rechte/Zwangsvollstreckung (§ 29), Lizenzen (§ 30).", concepts=["lizenz", "aktivlegitimation"], norms=["§ 27", "§ 28", "§ 29", "§ 30"]),
            step("5. Erlöschen", "Verzicht (§ 48), Nichtverlängerung (§ 47 Abs. 6), Verfall (§ 49), Nichtigkeit (§§ 50, 51), Löschung im Widerspruchsverfahren (§ 43 Abs. 2).", concepts=["verfall", "nichtigkeit"], norms=["§ 48", "§ 47"]),
        ],
    ),
]

SCHEMA_INDEX = {s["id"]: s for s in SCHEMATA}
