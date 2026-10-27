# -*- coding: utf-8 -*-
"""Normkurs Designrecht im Jurafuchs-Format: ein Kapitel je Vorschrift des DesignG (mit den Parallelnormen der GGV),
Unterkapitel (`abschnitt`) je Absatz oder Tatbestandsmerkmal, darin kurze Fallketten mit Abwandlungen.
Auswahl nach data/norm_ranking.json (tools/norm_ranking.py) und den Anspruchsgrundlagen der Verletzungsklage.

Die Fälle folgen den Leitentscheidungen in design/cases.py und design/cases_d02.py (BGH/BPatG gegen den Korpus geprüft, EuGH/EuG per
Websuche verifiziert); Fallketten ohne `cases` sind Lehrfälle. Der Überblickskurs d01 bleibt die Einführung; d02 geht Vorschrift für
Vorschrift in die Tiefe und stellt dort, wo d01 eine Entscheidung schon nutzt, andere Prüfungspunkte derselben Entscheidung in den Vordergrund."""
from ._helpers import intro, schema, fall, mc, frage, fallkette  # noqa: F401

SF = "step:des_schema_schutzfaehigkeit"
VL = "step:des_schema_designverletzung"
NV = "step:des_schema_nichtigkeitsverfahren"
UG = "step:des_schema_unionsgeschmacksmuster"

KAPITEL = [
    # ================================================================== § 1 DesignG (mit § 4)
    dict(id="d02n1", titel="§ 1 DesignG: Design, Erzeugnis, Bauelement (mit § 4 DesignG)", einheiten=[
        intro("d02n1-0", "Die Begriffe, an denen jede Prüfung beginnt",
              "§ 1 DesignG definiert die Grundbegriffe. **Design** ist die zwei- oder dreidimensionale Erscheinungsform eines ganzen Erzeugnisses "
              "oder eines Teils davon (Nr. 1). **Erzeugnis** ist jeder industrielle oder handwerkliche Gegenstand einschließlich Verpackung, "
              "grafischer Symbole und typografischer Schriftzeichen; ein Computerprogramm ist keines (Nr. 2). Ein **komplexes Erzeugnis** besteht "
              "aus ersetzbaren Bauelementen (Nr. 3); **bestimmungsgemäße Verwendung** ist die Verwendung durch den Endbenutzer ohne Instandhaltung, "
              "Wartung und Reparatur (Nr. 4). § 4 DesignG knüpft daran an: Ein Bauelement ist nur schutzfähig, soweit es eingebaut sichtbar bleibt "
              "und gerade seine sichtbaren Merkmale neu sind und Eigenart haben. Fehlt schon ein Design, weist das DPMA die Anmeldung zurück "
              "(§ 18 DesignG); eine Eintragung ist nichtig (§ 33 Abs. 1 Nr. 1 DesignG).",
              norms=["§ 1 DesignG", "§ 4 DesignG", "§ 18 DesignG", "§ 33 Abs. 1 DesignG"], concepts=["des_design_begriff", "des_erzeugnis"],
              abschnitt="Überblick"),
        *fallkette("d02n1-1", "Icon, App und Schachtel",
            "Die Softwarefirma S hat für ihre Kalender-App ein farbiges App-Icon entworfen und für den Handel eine auffällige Schachtel, in der "
            "eine Download-Karte steckt. S möchte Designschutz für das Icon, die Schachtel und „die App selbst“.",
            [frage("Ist das App-Icon ein Erzeugnis im Sinne von § 1 Nr. 2 DesignG?", True,
                   ["**Ja!** Erzeugnis ist jeder industrielle oder handwerkliche Gegenstand, ausdrücklich einschließlich **grafischer Symbole** "
                    "(§ 1 Nr. 2 DesignG). Das Icon ist ein grafisches Symbol; seine Erscheinungsform aus Linien, Konturen und Farben ist ein Design "
                    "im Sinne von § 1 Nr. 1 DesignG."],
                   merke="Grafische Symbole und Schriftzeichen sind Erzeugnisse.", titel="Grafisches Symbol"),
             frage("Was davon ist **kein** Erzeugnis im Sinne von § 1 Nr. 2 DesignG?", 2,
                   ["**Das Computerprogramm.** § 1 Nr. 2 Halbs. 2 DesignG nimmt Computerprogramme ausdrücklich aus. Verpackung und typografische "
                    "Schriftzeichen nennt die Vorschrift dagegen ausdrücklich als Erzeugnisse. S kann also die sichtbare Gestaltung (Icon, Schachtel) "
                    "schützen, nicht den Code oder die Funktion der App."],
                   optionen=["Die Schachtel für die Download-Karte", "Das App-Icon", "Das Computerprogramm der App", "Eine eigens entworfene Schrift für die App"],
                   merke="Designschutz erfasst Erscheinungsformen, nie Programme oder Funktionen.", titel="Kein Erzeugnis"),
            ],
            abschnitt="Nr. 1 und 2: Design und Erzeugnis", level=1, concepts=["des_erzeugnis", "des_design_begriff"], norms=["§ 1 DesignG"],
            step=f"{SF}.2.1"),
        *fallkette("d02n1-2", "Die Front des Rennwagens (Front kit)",
            "Ferrari stellt einen Rennwagen mit Pressefotos des ganzen Fahrzeugs vor; Abbildungen einzelner Teile veröffentlicht es nicht. Der "
            "Tuner M verkauft Bausätze, mit denen ein Serienmodell die markante V-förmige Front des Rennwagens erhält. Ferrari beruft sich auf "
            "ein nicht eingetragenes Gemeinschaftsgeschmacksmuster an der Front.",
            [frage("Kann die Erscheinungsform eines bloßen Teils eines Erzeugnisses ein Design sein?", True,
                   ["**Ja!** Design ist die Erscheinungsform eines ganzen Erzeugnisses „oder eines Teils davon“ (§ 1 Nr. 1 DesignG, Art. 3 GGV). "
                    "Schutzgegenstand kann deshalb auch die Front eines Fahrzeugs sein, ohne dass das ganze Fahrzeug geschützt ist."],
                   merke="Auch Teile eines Erzeugnisses sind Designs.", titel="Teil eines Erzeugnisses"),
             frage("Genügen die Fotos des ganzen Fahrzeugs, um ein Design an der Front zu offenbaren?", True,
                   ["**Ja**, wenn die Erscheinungsform des Teils auf den Abbildungen **eindeutig erkennbar** ist (EuGH Ferrari). Eine gesonderte "
                    "Veröffentlichung des Teils ist nicht nötig."],
                   merke="Das Gesamtbild offenbart den Teil, wenn er eindeutig erkennbar ist.", titel="Offenbarung durch das Ganze", level=2,
                   norms=["Art. 11 GGV"]),
             frage("Ist damit jeder beliebige Ausschnitt der Fahrzeugfront schutzfähig?", False,
                   ["**Nein!** Der Teil muss ein sichtbarer, durch Linien, Konturen, Farben, Gestalt oder Oberflächenstruktur **klar abgegrenzter "
                    "Teilbereich** sein, der einen eigenen Gesamteindruck hervorruft und nicht völlig in der Gesamtform aufgeht (BGH Front kit II). "
                    "Nur dann kann er Eigenart haben."],
                   merke="Teildesign: klar abgegrenzt, eigener Gesamteindruck.", titel="Abgegrenzter Teilbereich", level=2),
            ],
            abschnitt="Nr. 1: Teil eines Erzeugnisses", level=2, concepts=["des_design_begriff", "des_ggm_nicht_eingetragen"],
            norms=["§ 1 DesignG", "Art. 3 GGV"], cases=["des_eugh_ferrari", "des_bgh_front_kit_ii"], step=f"{SF}.2.1"),
        *fallkette("d02n1-3", "Die Sattelunterseite",
            "B hat ein Design für einen Fahrradsattel eingetragen; neu und eigenartig ist nur die Gestaltung der Unterseite. M beantragt beim DPMA "
            "die Feststellung der Nichtigkeit: Am montierten Sattel sehe man die Unterseite beim Fahren nicht.",
            [frage("Ist das Fahrrad ein komplexes Erzeugnis und der Sattel eines seiner Bauelemente?", True,
                   ["**Ja!** Ein komplexes Erzeugnis besteht aus mehreren Bauelementen, die sich ersetzen lassen, so dass es auseinander- und wieder "
                    "zusammengebaut werden kann (§ 1 Nr. 3 DesignG). Der Sattel lässt sich abnehmen und austauschen. Damit greift § 4 DesignG: "
                    "Schutzfähig ist nur, was eingebaut bei bestimmungsgemäßer Verwendung sichtbar bleibt."],
                   merke="Bauelement eines komplexen Erzeugnisses: Prüfung über § 4 DesignG.", titel="Komplexes Erzeugnis"),
             frage("Muss die Unterseite während der Fahrt ständig sichtbar sein?", False,
                   ["**Nein!** Das Bauelement muss nicht in jedem Moment der Benutzung sichtbar sein. Maßgeblich ist die Sicht des Endbenutzers und "
                    "eines **außenstehenden Beobachters** bei bestimmungsgemäßer Verwendung; dazu gehören auch Abstellen, Aufbewahren und Transport "
                    "des Fahrrads (EuGH Monz, BGH Sattelunterseite II)."],
                   merke="Sichtbarkeit: Endbenutzer und Beobachter, nicht in jedem Moment.", titel="Sichtbarkeit beim Gebrauch", level=2),
             frage("Zählt es, dass die Unterseite beim Austausch des Sattels in der Werkstatt zu sehen ist?", False,
                   ["**Nein!** Instandhaltung, Wartung und Reparatur gehören nicht zur bestimmungsgemäßen Verwendung (§ 1 Nr. 4 DesignG). "
                    "Sichtbarkeit allein beim Aus- und Einbauen begründet keinen Schutz."],
                   merke="Werkstatt zählt nicht: § 1 Nr. 4 DesignG.", titel="Wartung und Reparatur"),
             frage("Bleibt das Design schutzfähig, selbst wenn die Unterseite am Fahrrad nie sichtbar wäre?", True,
                   ["**Ja!** Lässt sich das Bauelement mehreren komplexen Erzeugnissen zuordnen, greift § 4 DesignG nur, wenn es bei **keiner** "
                    "bestimmungsgemäßen Verwendung sichtbar bleibt. Es genügt, dass die neuen und eigenartigen Merkmale bei einem der Erzeugnisse "
                    "sichtbar sind (BPatG Sattelunterseite II)."],
                   abwandlung="Der Sattel passt auch auf Motorräder; dort ist seine Unterseite beim Abstellen gut zu sehen.",
                   merke="Mehrere komplexe Erzeugnisse: eines mit Sichtbarkeit genügt.", titel="Mehrere komplexe Erzeugnisse", level=3,
                   cases=["des_bpatg_sattelunterseite_ii"]),
            ],
            abschnitt="Nr. 3, 4 und § 4 DesignG: Bauelemente", level=2, concepts=["des_bauelement_sichtbarkeit", "des_erzeugnis"],
            norms=["§ 1 DesignG", "§ 4 DesignG"], cases=["des_eugh_monz", "des_bgh_sattelunterseite_ii"], step=f"{SF}.2.2"),
        *fallkette("d02n1-4", "Der Ansaugkrümmer",
            "Zulieferer Z hat ein Design für einen Ansaugkrümmer eingetragen, der im Motorraum eines Pkw verbaut wird. Zu sehen ist der Krümmer "
            "nur bei geöffneter Motorhaube, etwa beim Ölwechsel in der Werkstatt. Nachbauer N bietet baugleiche Krümmer an.",
            [frage("Bleibt der Krümmer bei bestimmungsgemäßer Verwendung des Pkw sichtbar?", False,
                   ["**Nein!** Bestimmungsgemäß ist die Verwendung durch den Endbenutzer, also Fahren, Parken, Beladen; Instandhaltung und Wartung "
                    "wie ein Ölwechsel sind ausgenommen (§ 1 Nr. 4 DesignG). Sichtbar ist der Krümmer nur bei solchen Arbeiten."],
                   merke="Unter der Haube verbaut heißt: nicht sichtbar im Sinne von § 4 DesignG.", titel="Verbautes Bauelement"),
             frage("Kann das eingetragene Design des Z dann neu sein und Eigenart haben?", False,
                   ["**Nein!** Nach § 4 DesignG gilt ein Design an einem Bauelement nur dann als neu und eigenartig, wenn das eingebaute Bauelement "
                    "sichtbar bleibt und gerade seine sichtbaren Merkmale die Voraussetzungen erfüllen. Das Design ist nach § 33 Abs. 1 Nr. 2 DesignG "
                    "nichtig; N kann die Feststellung beim DPMA beantragen (§ 34 S. 1 DesignG)."],
                   merke="Unsichtbares Bauelement: weder neu noch eigenartig, also nichtig.", titel="Rechtsfolge des § 4 DesignG", level=2,
                   norms=["§ 33 Abs. 1 DesignG", "§ 34 DesignG"]),
             frage("Rettet es Z, dass der Krümmer im Ersatzteilkarton im Laden gut zu sehen ist?", False,
                   ["**Nein!** § 4 DesignG fragt nach der Sichtbarkeit des Bauelements, wenn es **in das komplexe Erzeugnis eingefügt** ist, bei "
                    "dessen bestimmungsgemäßer Verwendung. Wie das Einzelteil im Handel aussieht, ist dafür ohne Bedeutung."],
                   abwandlung="Z verkauft den Krümmer auch einzeln als Ersatzteil in einem Karton mit Sichtfenster.",
                   merke="Maßstab ist das eingebaute Teil, nicht die Ladentheke.", titel="Sichtbarkeit im Handel", level=2),
            ],
            abschnitt="Nr. 3, 4 und § 4 DesignG: Bauelemente", level=1, concepts=["des_bauelement_sichtbarkeit"],
            norms=["§ 4 DesignG", "§ 1 DesignG"], step=f"{SF}.2.2"),
    ]),
    # ================================================================== § 2 Abs. 2 DesignG (mit §§ 5, 6)
    dict(id="d02n2a2", titel="§ 2 Abs. 2 DesignG: Neuheit (mit §§ 5, 6 DesignG)", einheiten=[
        intro("d02n2a2-0", "Neuheit in vier Schritten",
              "Ein Design ist **neu**, wenn vor dem Anmeldetag kein identisches Design offenbart worden ist; identisch sind Designs, deren Merkmale "
              "sich nur in **unwesentlichen Einzelheiten** unterscheiden (§ 2 Abs. 2 DesignG). Prüfung: (1) maßgeblicher Tag, Anmelde- oder "
              "Prioritätstag (§ 13 Abs. 2 DesignG); (2) Offenbarung der Entgegenhaltung (§ 5 DesignG): bekannt gemacht, ausgestellt, im Verkehr "
              "verwendet oder sonst zugänglich gemacht, es sei denn, die in der Union tätigen Fachkreise konnten sie im normalen Geschäftsverlauf "
              "nicht kennen; vertrauliche Mitteilungen zählen nicht; (3) Neuheitsschonfrist: Offenbarungen des Entwerfers in den zwölf Monaten vor "
              "dem Anmeldetag bleiben außer Betracht (§ 6 DesignG); (4) Einzelvergleich. Das DPMA prüft die Neuheit bei der Anmeldung nicht; "
              "sie wird im Nichtigkeitsverfahren geprüft (§ 33 Abs. 1 Nr. 2 DesignG).",
              norms=["§ 2 Abs. 2 DesignG", "§ 5 DesignG", "§ 6 DesignG", "§ 13 Abs. 2 DesignG"],
              concepts=["des_neuheit", "des_offenbarung", "des_neuheitsschonfrist"], abschnitt="Überblick"),
        *fallkette("d02n2a2-1", "Die vertrauliche Vorführung",
            "Möbeldesigner M zeigt den Prototyp eines Sessels im Januar einem Hersteller, mit dem er eine Geheimhaltung vereinbart hat. Im März "
            "schickt M Fotos des Sessels ohne Vorbehalt an zwanzig Möbelhändler in mehreren EU-Staaten. Erst im Juni des Folgejahres meldet er "
            "den Sessel als Design an.",
            [frage("Ist der Sessel durch die Vorführung beim Hersteller offenbart worden?", False,
                   ["**Nein!** Ein Design gilt nicht als offenbart, wenn es einem Dritten nur unter der ausdrücklichen oder stillschweigenden "
                    "Bedingung der **Vertraulichkeit** bekannt gemacht wurde (§ 5 S. 2 DesignG)."],
                   merke="Vertrauliche Mitteilung ist keine Offenbarung.", titel="Vertraulichkeit"),
             frage("Kann der Versand der Fotos an die Händler eine Offenbarung sein?", True,
                   ["**Ja!** Auch die Verteilung von Abbildungen an Händler kann ein Design den in der Union tätigen Fachkreisen im normalen "
                    "Geschäftsverlauf bekannt machen (EuGH Gautzsch). Ob das im Einzelfall so ist, ist Tatfrage. Ein Vertraulichkeitsvorbehalt fehlt "
                    "hier. Da zwischen März und der Anmeldung mehr als zwölf Monate liegen, hilft auch § 6 DesignG nicht."],
                   merke="Abbildungen an Händler können offenbaren; Tatfrage.", titel="Händlerversand", level=2, cases=["des_eugh_gautzsch"]),
             frage("Wann bleibt eine Offenbarung nach § 5 S. 1 DesignG außer Betracht, obwohl das ältere Design zugänglich war?", 1,
                   ["**Wenn die Fachkreise es nicht kennen konnten.** Maßgeblich ist, ob die in der Union tätigen Fachkreise des betreffenden "
                    "Sektors das Design im normalen Geschäftsverlauf vor dem Anmeldetag kennen konnten (§ 5 S. 1 DesignG). Der Ort der Offenbarung "
                    "ist für sich gleichgültig (BGH Gebäckpresse), ebenso die Erzeugnisart des älteren Designs (EuGH Easy Sanitary) und seine "
                    "Eintragung."],
                   optionen=["Wenn sie außerhalb der Union stattfand", "Wenn die Fachkreise des Sektors in der Union sie im normalen Geschäftsverlauf nicht kennen konnten",
                             "Wenn das ältere Design für eine andere Erzeugnisart bestimmt war", "Wenn das ältere Design nie eingetragen wurde"],
                   merke="Fachkreisklausel: entscheidend ist die Kenntnismöglichkeit der Fachkreise in der Union.", titel="Fachkreisklausel", level=2,
                   cases=["des_bgh_gebaeckpresse", "des_eugh_easy_sanitary"]),
            ],
            abschnitt="§ 5 DesignG: Offenbarung", level=1, concepts=["des_offenbarung", "des_formenschatz"], norms=["§ 5 DesignG"], step=f"{SF}.4.2"),
        *fallkette("d02n2a2-2", "Die verlängerte Limousine",
            "Karosseriebauer A meldet am 1. März ein Design für eine verlängerte Limousine an; bekannt gemacht wird es im Juni. Wettbewerber B "
            "meldet am 1. Mai eine fast gleiche Limousine an, ohne von A zu wissen.",
            [frage("Nimmt die frühere Anmeldung des A dem Design des B die Neuheit?", False,
                   ["**Nein!** Die bloße Anmeldung macht ein Design der Öffentlichkeit noch nicht zugänglich; erst die Bekanntmachung oder eine "
                    "sonstige Offenbarung zählt zum Formenschatz (BGH Verlängerte Limousinen). Am 1. Mai war das Design des A nicht offenbart, "
                    "§ 2 Abs. 2 DesignG steht dem Design des B nicht entgegen."],
                   merke="Anmeldung ist noch keine Offenbarung.", titel="Anmeldung als Offenbarung?", level=2),
             frage("Kann A trotzdem gegen das Design des B vorgehen?", True,
                   ["**Ja!** Fällt ein Design in den Schutzumfang eines eingetragenen Designs mit älterem Zeitrang, wird es für nichtig erklärt, auch "
                    "wenn das ältere erst nach dem Anmeldetag des jüngeren offenbart wurde (§ 33 Abs. 2 Nr. 2 DesignG). Den Antrag kann nur A als "
                    "Inhaber stellen (§ 34 S. 2 DesignG)."],
                   merke="Nachveröffentlichtes älteres Design: relativer Nichtigkeitsgrund, nicht Neuheitsschädlichkeit.", titel="Älteres Recht",
                   level=2, norms=["§ 33 Abs. 2 DesignG", "§ 34 DesignG"]),
            ],
            abschnitt="§ 5 DesignG: Offenbarung", level=2, concepts=["des_offenbarung", "des_neuheit", "des_nichtigkeit"], norms=["§ 2 Abs. 2 DesignG", "§ 5 DesignG"],
            cases=["des_bgh_verlaengerte_limousinen"], step=f"{SF}.4.2"),
        *fallkette("d02n2a2-3", "Die Leuchte von der Messe",
            "Designerin D stellt im April 2025 eine neue Stehleuchte auf einer Möbelmesse in Mailand aus. Im Februar 2026 meldet sie die Leuchte "
            "beim DPMA als Design an. Ihr Konkurrent K hält das Design für nicht neu.",
            [frage("Ist die Ausstellung auf der Messe eine Offenbarung im Sinne von § 5 DesignG?", True,
                   ["**Ja!** Ausstellen ist ein Regelbeispiel der Offenbarung (§ 5 S. 1 DesignG). Eine internationale Fachmesse in der Union "
                    "können die Fachkreise im normalen Geschäftsverlauf kennen."],
                   merke="Ausstellen ist Offenbaren.", titel="Messe als Offenbarung"),
             frage("Zerstört die eigene Ausstellung die Neuheit des Designs?", False,
                   ["**Nein!** Eine Offenbarung durch den Entwerfer in den **zwölf Monaten** vor dem Anmeldetag bleibt bei § 2 Abs. 2 und 3 DesignG "
                    "unberücksichtigt (§ 6 S. 1 DesignG). Zwischen April 2025 und Februar 2026 liegen zehn Monate."],
                   merke="Neuheitsschonfrist: zwölf Monate für eigene Offenbarungen.", titel="Eigene Offenbarung"),
             frage("Schadet D der Vertrieb der Nachbauten durch K?", False,
                   ["**Nein!** § 6 S. 1 DesignG erfasst auch Offenbarungen durch einen Dritten „als Folge von Informationen oder Handlungen des "
                    "Entwerfers“. Ks Nachbau beruht auf der Messepräsentation und ist deshalb ebenfalls unschädlich."],
                   abwandlung="K hat die Leuchte nach der Messe nachgebaut und ab Juni 2025 selbst verkauft.",
                   merke="Schonfrist deckt auch Offenbarungen Dritter, die auf den Entwerfer zurückgehen.", titel="Offenbarung durch Dritte", level=2),
             frage("Hilft D die Neuheitsschonfrist noch?", False,
                   ["**Nein!** Die Frist des § 6 DesignG beträgt zwölf Monate ab der Offenbarung und ist im Mai 2026 abgelaufen. Die Ausstellung "
                    "vom April 2025 gehört nun zum Formenschatz und nimmt dem identischen Design die Neuheit (§ 2 Abs. 2 DesignG)."],
                   abwandlung="D meldet nicht im Februar, sondern erst im Mai 2026 an.",
                   merke="Nach zwölf Monaten wird die eigene Offenbarung neuheitsschädlich.", titel="Frist versäumt"),
            ],
            abschnitt="§ 6 DesignG: Neuheitsschonfrist", level=1, concepts=["des_neuheitsschonfrist", "des_offenbarung"], norms=["§ 6 DesignG"],
            step=f"{SF}.4.3"),
        *fallkette("d02n2a2-4", "Das Wandregal",
            "R meldet im Mai ein Wandregal als Design an. Im Januar hatte ein Möbelhaus in seinem Onlineshop ein Regal angeboten, das sich nur in "
            "der Form der Schraubenköpfe und einem zwei Millimeter dickeren Boden unterscheidet.",
            [frage("Ist das Design des R neu?", False,
                   ["**Nein!** Designs gelten als identisch, wenn sich ihre Merkmale nur in **unwesentlichen Einzelheiten** unterscheiden "
                    "(§ 2 Abs. 2 S. 2 DesignG). Schraubenköpfe und eine kaum wahrnehmbare Materialstärke prägen das Erscheinungsbild nicht. Das "
                    "Onlineangebot ist eine Offenbarung (§ 5 DesignG; BGH Ballerinaschuh)."],
                   merke="Nur unwesentlich verschieden heißt identisch.", titel="Unwesentliche Einzelheiten", cases=["des_bgh_ballerinaschuh"]),
             frage("Ist das Design des R dann neu?", True,
                   ["**Ja!** Ein deutlich anders geformter Boden ist keine unwesentliche Einzelheit; die Designs sind nicht identisch. Ob Rs Regal "
                    "auch **Eigenart** hat, ist getrennt nach § 2 Abs. 3 DesignG zu prüfen: Ruft es beim informierten Benutzer einen anderen "
                    "Gesamteindruck hervor?"],
                   abwandlung="Das ältere Regal hat statt gerader Böden deutlich geschwungene Wellenböden.",
                   merke="Neuheit ist eine niedrige Hürde; die eigentliche Prüfung ist die Eigenart.", titel="Wesentlicher Unterschied"),
             frage("Auf welchen Tag kommt es nun für die Neuheit an?", 1,
                   ["**Auf den Prioritätstag.** Wird eine Priorität wirksam in Anspruch genommen, tritt bei der Anwendung der §§ 2 bis 6 DesignG der "
                    "Prioritätstag an die Stelle des Anmeldetages (§ 13 Abs. 2 DesignG). Das Onlineangebot vom Januar liegt danach und schadet nicht."],
                   abwandlung="R hatte das Regal im Dezember zuvor in Japan angemeldet und beansprucht diese Priorität wirksam.",
                   optionen=["Den Anmeldetag beim DPMA im Mai", "Den Prioritätstag im Dezember", "Den Tag der Eintragung", "Den Tag der Bekanntmachung"],
                   merke="Priorität verschiebt den Stichtag für §§ 2 bis 6 DesignG.", titel="Maßgeblicher Tag", level=2,
                   norms=["§ 13 Abs. 2 DesignG", "§ 14 DesignG"], step=f"{SF}.4.1"),
            ],
            abschnitt="Abs. 2 S. 2: Identität und maßgeblicher Tag", level=1, concepts=["des_neuheit", "des_prioritaet"], norms=["§ 2 Abs. 2 DesignG"],
            step=f"{SF}.5"),
    ]),
    # ================================================================== § 2 Abs. 3 DesignG
    dict(id="d02n2a3", titel="§ 2 Abs. 3 DesignG: Eigenart", einheiten=[
        intro("d02n2a3-0", "Unterschiedlichkeit statt Gestaltungshöhe",
              "Ein Design hat **Eigenart**, wenn sich der Gesamteindruck, den es beim informierten Benutzer hervorruft, von dem Gesamteindruck jedes "
              "vor dem Anmeldetag offenbarten Designs unterscheidet; dabei wird der Grad der **Gestaltungsfreiheit** des Entwerfers berücksichtigt "
              "(§ 2 Abs. 3 DesignG, Art. 6 GGV). Prüfung: (1) informierten Benutzer des Sektors bestimmen; (2) Gestaltungsfreiheit und Musterdichte "
              "zum Anmeldetag; (3) Merkmale des Designs und der einzelnen Entgegenhaltung feststellen und gewichten, technisch bedingte Merkmale "
              "treten zurück; (4) Gesamteindrücke im Einzelvergleich gegenüberstellen, keine Kombination mehrerer Vorbilder. Eigenart heißt "
              "Unterschiedlichkeit, nicht Gestaltungshöhe. Derselbe Maßstab bestimmt spiegelbildlich den Schutzumfang (§ 38 Abs. 2 DesignG).",
              norms=["§ 2 Abs. 3 DesignG", "Art. 6 GGV", "§ 38 Abs. 2 DesignG"],
              concepts=["des_eigenart", "des_informierter_benutzer", "des_gestaltungsfreiheit", "des_gesamteindruck"], abschnitt="Überblick"),
        *fallkette("d02n2a3-1", "Die Spielscheiben (PepsiCo)",
            "PepsiCo lässt beim EUIPO ein Muster für runde, leicht gewölbte Spielscheiben eintragen, die Snacktüten beiliegen. Grupo Promer hatte "
            "zuvor ein ähnliches Muster für solche Scheiben angemeldet und beantragt die Nichtigerklärung. Die Scheiben unterscheiden sich vor "
            "allem in Einzelheiten des Profils.",
            [frage("Ist der informierte Benutzer der Durchschnittsverbraucher, der die Scheiben nur beiläufig wahrnimmt?", False,
                   ["**Nein!** Der informierte Benutzer steht zwischen dem Durchschnittsverbraucher des Markenrechts und dem Fachmann: Er kennt "
                    "verschiedene Designs des Sektors, weiß um die üblichen Gestaltungselemente und benutzt die Erzeugnisse mit **vergleichsweise "
                    "großer Aufmerksamkeit** (EuGH PepsiCo). Hier kommen etwa Kinder in Betracht, die mit den Scheiben spielen."],
                   merke="Informierter Benutzer: aufmerksamer als der Verbraucher, kein Fachmann.", titel="Wer vergleicht?"),
             frage("Vergleicht der informierte Benutzer die Designs nach Möglichkeit unmittelbar nebeneinander?", True,
                   ["**Ja!** Der Gesamteindruck ist nach Möglichkeit durch **direkten Vergleich** zu ermitteln; ein Vergleich aus dem unvollkommenen "
                    "Erinnerungsbild ist nur zulässig, wo der direkte Vergleich nicht praktikabel ist (EuGH PepsiCo). Darin liegt ein Unterschied "
                    "zum Markenrecht."],
                   merke="Direkter Vergleich vor Erinnerungsbild.", titel="Direkter Vergleich", level=2),
             frage("Kommt es darauf an, ob ein konkreter Benutzer das ältere Muster tatsächlich gekannt hat?", False,
                   ["**Nein!** Der informierte Benutzer ist eine Maßstabsfigur. Es genügt, dass das ältere Design offenbart ist und den Fachkreisen "
                    "bekannt sein konnte (§ 5 DesignG, Art. 7 GGV); tatsächliche Kenntnis ist nicht erforderlich (EuGH Easy Sanitary)."],
                   merke="Maßstabsfigur, keine reale Kenntnis nötig.", titel="Tatsächliche Kenntnis?", level=2, cases=["des_eugh_easy_sanitary"]),
            ],
            abschnitt="Informierter Benutzer", level=1, concepts=["des_informierter_benutzer", "des_gesamteindruck"],
            norms=["§ 2 Abs. 3 DesignG", "Art. 6 GGV"], cases=["des_eugh_pepsico"], step=f"{SF}.6.1"),
        *fallkette("d02n2a3-2", "Der Filzuntersetzer",
            "U meldet einen runden Getränkeuntersetzer aus Filz mit vier eingestanzten Wellenlinien als Design an. Auf dem Markt gibt es Hunderte "
            "runder Filzuntersetzer, viele mit geometrischen Mustern. Ein Wettbewerber hält Us Untersetzer für banal und deshalb nicht schutzfähig.",
            [frage("Setzt Eigenart eine besondere Gestaltungshöhe voraus?", False,
                   ["**Nein!** Eigenart bedeutet **Unterschiedlichkeit** gegenüber jedem einzelnen vorbekannten Design, nicht Eigentümlichkeit oder "
                    "Gestaltungshöhe wie nach dem alten Geschmacksmusterrecht (BGH Verlängerte Limousinen). Auch ein schlichter Untersetzer kann "
                    "Eigenart haben."],
                   merke="Eigenart = Unterschiedlichkeit, keine Gestaltungshöhe.", titel="Gestaltungshöhe?", cases=["des_bgh_verlaengerte_limousinen"]),
             frage("Genügen bei hoher Musterdichte schon kleinere Unterschiede für einen anderen Gesamteindruck?", True,
                   ["**Ja!** Bei hoher Musterdichte und geringer Gestaltungsfreiheit achtet der informierte Benutzer auf Details; kleinere Unterschiede "
                    "können genügen (§ 2 Abs. 3 S. 2 DesignG; EuGH PepsiCo). Die Kehrseite zeigt sich beim Schutzumfang: Er ist dann eng "
                    "(BGH Untersetzer, § 38 Abs. 2 DesignG)."],
                   merke="Dichter Formenschatz: leichter Eigenart, dafür enger Schutz.", titel="Musterdichte", level=2,
                   cases=["des_eugh_pepsico"]),
             frage("Auf welchen Zeitpunkt kommt es für den Grad der Gestaltungsfreiheit an?", 1,
                   ["**Auf den Anmeldetag.** Gestaltungsfreiheit und Formenschatz werden für den Zeitpunkt der Anmeldung des Designs bestimmt "
                    "(BGH Untersetzer); spätere Designs engen den Spielraum nicht nachträglich ein. Bei Inanspruchnahme einer Priorität tritt der "
                    "Prioritätstag an seine Stelle (§ 13 Abs. 2 DesignG)."],
                   optionen=["Auf den Zeitpunkt der Verletzungshandlung", "Auf den Anmeldetag oder Prioritätstag des Designs",
                             "Auf den Schluss der mündlichen Verhandlung", "Auf den Tag der Eintragung"],
                   merke="Gestaltungsfreiheit wird zum Anmeldetag gemessen.", titel="Stichtag", level=2),
            ],
            abschnitt="Gestaltungsfreiheit und Musterdichte", level=1, concepts=["des_eigenart", "des_gestaltungsfreiheit", "des_formenschatz"],
            norms=["§ 2 Abs. 3 DesignG"], cases=["des_bgh_untersetzer"], step=f"{SF}.6.2"),
        *fallkette("d02n2a3-3", "Die violette Trittleiter",
            "T hat eine Trittleiter mit drei Stufen und gebogenem Haltebügel in Violett als Design eintragen lassen. Eine Leiter mit denselben "
            "prägenden Formmerkmalen war zuvor in Grau im Handel. Ein Wettbewerber beantragt die Feststellung der Nichtigkeit.",
            [frage("Hat Ts Leiter wegen der neuen Farbe Eigenart?", False,
                   ["**Nein!** Unterscheidet sich ein Design mit prägenden Formmerkmalen von einem vorbekannten Design nur in der Farbe, fehlt "
                    "regelmäßig die Eigenart (BPatG Violette Trittleiter). Der Gesamteindruck wird hier von der Form bestimmt."],
                   merke="Nur eine andere Farbe begründet regelmäßig keine Eigenart.", titel="Farbe als Unterschied"),
             frage("Kann eine Farbgestaltung überhaupt Eigenart begründen?", True,
                   ["**Ja**, ausnahmsweise: etwa wenn die Farbgebung ungewöhnlich oder besonders auf die Erfordernisse des Erzeugnisses abgestimmt "
                    "ist (BPatG Violette Trittleiter). Farben gehören zu den Merkmalen der Erscheinungsform (§ 1 Nr. 1 DesignG)."],
                   merke="Farbe: ausnahmsweise, wenn ungewöhnlich oder funktional abgestimmt.", titel="Farbe ausnahmsweise", level=2),
             frage("Darf das DPMA beide älteren Leitern zu einem Vorbild zusammensetzen?", False,
                   ["**Nein!** Eigenart wird im **Einzelvergleich** mit jeweils einem konkreten älteren Design geprüft; eine mosaikartige Kombination "
                    "von Merkmalen aus mehreren Entgegenhaltungen ist unzulässig (EuGH Karen Millen, BGH Meda Gate). Jede ältere Leiter ist für sich "
                    "mit Ts Design zu vergleichen."],
                   abwandlung="Die graue Leiter hatte einen geraden Bügel; einen gebogenen Bügel zeigte nur eine andere, ebenfalls ältere Leiter.",
                   merke="Kein Mosaik: immer ein Vorbild gegen das Design.", titel="Kombination von Vorbildern", level=2,
                   cases=["des_eugh_karen_millen", "des_bgh_meda_gate"]),
            ],
            abschnitt="Gesamteindruck im Einzelvergleich", level=1, concepts=["des_eigenart", "des_gesamteindruck"], norms=["§ 2 Abs. 3 DesignG"],
            cases=["des_bpatg_violette_trittleiter"], step=f"{SF}.6.3"),
    ]),
    # ================================================================== § 3 DesignG
    dict(id="d02n3", titel="§ 3 DesignG: Ausschlüsse vom Designschutz", einheiten=[
        intro("d02n3-0", "Vier Ausschlüsse",
              "§ 3 Abs. 1 DesignG nimmt vier Gruppen vom Schutz aus: (1) Erscheinungsmerkmale, die **ausschließlich durch die technische Funktion** "
              "bedingt sind; (2) **Verbindungselemente**, die in genauer Form und Abmessung nachgebildet werden müssen, damit Erzeugnisse mechanisch "
              "zusammenpassen, mit der Rückausnahme für Bauteilesysteme (Abs. 2); (3) Designs gegen die **öffentliche Ordnung** oder die guten "
              "Sitten; (4) die missbräuchliche Benutzung von Hoheitszeichen nach Art. 6ter PVÜ und sonstigen Abzeichen öffentlichen Interesses. "
              "Nr. 1 und 2 nehmen nur die betroffenen Merkmale aus; nichtig ist das Design erst, wenn keine anderen prägenden Merkmale bleiben. "
              "Nr. 3 und 4 prüft das DPMA schon bei der Anmeldung (§ 18 DesignG); im Übrigen wirkt § 3 DesignG als Nichtigkeitsgrund "
              "(§ 33 Abs. 1 Nr. 3 DesignG). Parallelnorm: Art. 8 GGV.",
              norms=["§ 3 DesignG", "§ 18 DesignG", "§ 33 Abs. 1 DesignG", "Art. 8 GGV"],
              concepts=["des_technisch_bedingt", "des_verbindungselemente", "des_ordre_public"], abschnitt="Überblick"),
        *fallkette("d02n3-1", "Die Zentrierstifte (DOCERAM)",
            "DOCERAM hat Gemeinschaftsgeschmacksmuster für keramische Zentrierstifte, die beim Schweißen Muttern führen. CeramTec bietet gleich "
            "geformte Stifte an und beantragt widerklagend die Nichtigerklärung: Die Form folge allein der Funktion.",
            [frage("Wonach bestimmt sich, ob die Merkmale der Stifte ausschließlich technisch bedingt sind?", 2,
                   ["**Nach dem einzigen bestimmenden Faktor.** Ausgeschlossen sind Merkmale, wenn die technische Funktion der einzige Faktor war, "
                    "der ihre Wahl bestimmt hat, und ästhetische Erwägungen keine Rolle spielten; zu beurteilen objektiv anhand aller Umstände des "
                    "Einzelfalls (EuGH DOCERAM). Alternative Formen schließen den Ausschluss nicht aus, auf einen objektiven Beobachter kommt es nicht an."],
                   optionen=["Danach, ob es alternative Formen mit derselben Funktion gibt", "Nach der Wahrnehmung eines objektiven Beobachters",
                             "Danach, ob die Funktion der einzige Faktor für die Wahl der Merkmale war, objektiv nach allen Umständen",
                             "Danach, ob für das Erzeugnis ein Patent besteht"],
                   merke="DOCERAM: Funktion als einziger Faktor; Mehrheit der Formen ist kein Test.", titel="Maßstab der technischen Bedingtheit", level=2),
             frage("Schließt die Patentanmeldung den Designschutz für die Stifte aus?", False,
                   ["**Nein!** Ein Patent oder eine Patentanmeldung für dasselbe Erzeugnis steht dem Designschutz nicht entgegen. Ansprüche, "
                    "Beschreibung und Zeichnungen gehören aber zu den **objektiven Umständen**, an denen die technische Bedingtheit zu prüfen ist "
                    "(BGH Papierspender)."],
                   abwandlung="DOCERAM hatte für die Stifte zuvor auch ein Patent angemeldet, dessen Ansprüche die Form der Stifte beschreiben.",
                   merke="Patent ist Indiz, kein Ausschlussgrund.", titel="Patent als Indiz", level=2, cases=["des_bgh_papierspender"]),
            ],
            abschnitt="Abs. 1 Nr. 1: Technische Bedingtheit", level=2, concepts=["des_technisch_bedingt"], norms=["§ 3 Abs. 1 DesignG", "Art. 8 GGV"],
            cases=["des_eugh_doceram"], step=f"{SF}.3.1"),
        *fallkette("d02n3-2", "Das Tellerschleifgerät",
            "H hat ein Design für ein Tellerschleifgerät eingetragen. Wettbewerber W greift es an: Schleifteller, Absaugstutzen und Motorblock seien "
            "technisch vorgegeben. Die geschwungene Haube über dem Motor hat H nach den Entwurfsunterlagen auch aus gestalterischen Gründen so geformt.",
            [frage("Ist das Design nichtig, weil viele seiner Merkmale technisch bedingt sind?", False,
                   ["**Nein!** Die technische Bedingtheit ist für jedes den Gesamteindruck **prägende Merkmal** gesondert zu prüfen. Nichtig ist das "
                    "Design nur, wenn alle prägenden Merkmale ausschließlich technisch bedingt sind (BGH Tellerschleifgerät). Die gestaltete Haube "
                    "trägt den Schutz."],
                   merke="Merkmal für Merkmal prüfen; ein freies prägendes Merkmal rettet das Design.", titel="Prüfung je Merkmal"),
             frage("Zählen die technisch bedingten Merkmale bei der Verletzungsprüfung dann noch mit?", True,
                   ["**Ja**, aber mit geringem Gewicht. Sie bleiben Teil des eingetragenen Designs, prägen den Gesamteindruck aber weniger; beim "
                    "Schutzumfang (§ 38 Abs. 2 DesignG) kommt es vor allem auf die gestalterisch freien Merkmale an (BGH Tellerschleifgerät)."],
                   merke="Technisch bedingte Merkmale: im Design, aber schwach gewichtet.", titel="Gewicht im Verletzungsstreit", level=2,
                   norms=["§ 38 Abs. 2 DesignG"]),
            ],
            abschnitt="Abs. 1 Nr. 1: Technische Bedingtheit", level=2, concepts=["des_technisch_bedingt", "des_gesamteindruck"],
            norms=["§ 3 Abs. 1 DesignG"], cases=["des_bgh_tellerschleifgeraet"], step=f"{SF}.3.1"),
        *fallkette("d02n3-3", "Der Klemmbaustein",
            "Lego hat ein Gemeinschaftsgeschmacksmuster für einen Baustein mit Noppen auf der glatten Oberseite und Röhren auf der Unterseite. Ein "
            "Wettbewerber beantragt beim EUIPO die Nichtigerklärung: Noppen und Röhren müssten genau so geformt sein, damit die Steine zusammenpassen.",
            [frage("Sind Merkmale, die exakt passen müssen, damit zwei Erzeugnisse mechanisch verbunden werden können, grundsätzlich vom Schutz "
                   "ausgeschlossen?", True,
                   ["**Ja!** Das ist der Ausschluss der Verbindungselemente nach § 3 Abs. 1 Nr. 2 DesignG und Art. 8 Abs. 2 GGV: Erscheinungsmerkmale, "
                    "die zwangsläufig in genauer Form und Abmessung nachgebildet werden müssen, damit Erzeugnisse zusammengebaut werden und ihre "
                    "Funktion erfüllen können."],
                   merke="Must fit: Passformmerkmale sind ausgeschlossen.", titel="Verbindungselemente"),
             frage("Gilt der Ausschluss auch für die Noppen eines Steckbausteinsystems?", False,
                   ["**Nein!** Merkmale, die den Zusammenbau einer Vielzahl untereinander austauschbarer Teile innerhalb eines **Bauteilesystems** "
                    "ermöglichen, sind nach der Rückausnahme schutzfähig (§ 3 Abs. 2 DesignG, Art. 8 Abs. 3 GGV). Das EUIPO musste diesen Einwand "
                    "prüfen (EuG Lego)."],
                   merke="Modulare Systeme: Rückausnahme des § 3 Abs. 2 DesignG.", titel="Bauteilesystem", level=2),
             frage("Durfte das Amt die glatte Oberseite des Steins bei der Prüfung übergehen?", False,
                   ["**Nein!** Ein Design ist nur dann insgesamt ausgeschlossen, wenn **alle** Erscheinungsmerkmale unter einen Ausschluss fallen. Die "
                    "glatte Oberseite war nicht gewürdigt worden; schon deshalb hob das EuG die Entscheidung auf (EuG Lego)."],
                   merke="Alle Merkmale würdigen, bevor das ganze Design fällt.", titel="Übersehenes Merkmal", level=2),
            ],
            abschnitt="Abs. 1 Nr. 2, Abs. 2: Verbindungselemente", level=2, concepts=["des_verbindungselemente", "des_technisch_bedingt"],
            norms=["§ 3 Abs. 1 DesignG", "§ 3 Abs. 2 DesignG", "Art. 8 GGV"], cases=["des_eug_lego"], step=f"{SF}.3.2"),
        *fallkette("d02n3-4", "Adler auf dem Trikot",
            "F meldet beim DPMA ein Fußballtrikot als Design an, auf dessen Brust ein originalgetreuer Bundesadler prangt. Ein Konkurrent, der "
            "ähnliche Trikots verkauft, will notfalls die Nichtigkeit des Designs beantragen.",
            [frage("Prüft das DPMA schon bei der Anmeldung, ob das Design nach § 3 Abs. 1 Nr. 4 DesignG ausgeschlossen ist?", True,
                   ["**Ja!** Anders als Neuheit und Eigenart prüft das DPMA, ob überhaupt ein Design vorliegt und ob es nach § 3 Abs. 1 Nr. 3 DesignG oder "
                    "§ 3 Abs. 1 Nr. 4 DesignG ausgeschlossen ist; dann weist es die Anmeldung zurück (§ 18 DesignG). Ob die Wiedergabe des Hoheitszeichens "
                    "missbräuchlich ist, ist eine Frage des Einzelfalls."],
                   merke="§ 18 DesignG: Prüfung nur von § 1 Nr. 1 und § 3 Abs. 1 Nr. 3, 4 DesignG.", titel="Prüfung bei der Anmeldung"),
             frage("Kann der Konkurrent einen Nichtigkeitsantrag auf die missbräuchliche Benutzung des Hoheitszeichens stützen?", False,
                   ["**Nein!** Diesen Grund kann nur geltend machen, wer **von der Benutzung betroffen** ist; die zuständige Behörde kann ihn von Amts "
                    "wegen geltend machen (§ 34 S. 3 DesignG). Ein Wettbewerber ist nicht betroffen."],
                   merke="Hoheitszeichen: nur der Betroffene oder die Behörde.", titel="Antragsbefugnis bei Nr. 4", level=2,
                   norms=["§ 34 DesignG"]),
             frage("Kann jedermann diesen Ausschluss im Nichtigkeitsverfahren geltend machen?", True,
                   ["**Ja!** Verstöße gegen die öffentliche Ordnung oder die guten Sitten schließen das Design aus (§ 3 Abs. 1 Nr. 3 DesignG) und sind "
                    "absoluter Nichtigkeitsgrund (§ 33 Abs. 1 Nr. 3 DesignG). Den Antrag kann jedermann stellen (§ 34 S. 1 DesignG); die "
                    "Beschränkung des § 34 S. 3 DesignG gilt nur für Nr. 4."],
                   abwandlung="Statt des Adlers zeigt das Trikot das Kennzeichen einer verbotenen verfassungsfeindlichen Organisation.",
                   merke="Ordre public: Jedermann-Grund.", titel="Öffentliche Ordnung", level=2, norms=["§ 33 Abs. 1 DesignG", "§ 34 DesignG"]),
            ],
            abschnitt="Abs. 1 Nr. 3, 4: Ordnung, Sitten, Hoheitszeichen", level=1, concepts=["des_ordre_public", "des_pruefung_dpma"],
            norms=["§ 3 Abs. 1 DesignG", "§ 18 DesignG"], step=f"{SF}.3.3"),
    ]),
    # ================================================================== §§ 7 bis 10 DesignG
    dict(id="d02n7", titel="§§ 7 bis 10 DesignG: Recht auf das Design und Anspruch gegen den Nichtberechtigten", einheiten=[
        intro("d02n7-0", "Wem das Design gehört",
              "Das Recht auf das eingetragene Design steht dem **Entwerfer** oder seinem Rechtsnachfolger zu, mehreren Entwerfern gemeinschaftlich "
              "(§ 7 Abs. 1 DesignG). Entwirft ein **Arbeitnehmer** in Ausübung seiner Aufgaben oder nach Weisung, gehört das Recht dem Arbeitgeber, "
              "sofern vertraglich nichts anderes vereinbart ist (§ 7 Abs. 2 DesignG). Im Verfahren vor dem DPMA gilt der Anmelder als berechtigt "
              "(§ 8 DesignG); das Amt prüft die Berechtigung nicht, und sie ist kein Nichtigkeitsgrund des § 33 DesignG. Der wahre Berechtigte hilft "
              "sich mit § 9 DesignG: Übertragung, Einwilligung in die Löschung oder Mitinhaberschaft, durch Klage binnen drei Jahren ab "
              "Bekanntmachung, gegen den Bösgläubigen ohne diese Frist. Unabhängig davon hat der Entwerfer das Recht auf Nennung (§ 10 DesignG).",
              norms=["§ 7 DesignG", "§ 8 DesignG", "§ 9 DesignG", "§ 10 DesignG"],
              concepts=["des_entwerfer_recht", "des_arbeitnehmerdesign", "des_vindikation"], abschnitt="Überblick"),
        *fallkette("d02n7-1", "Der Auftragsentwurf (FEIA)",
            "Die Möbelfirma M beauftragt die freie Designerin F, einen Stuhl zu entwerfen, und zahlt das vereinbarte Honorar. Wem die Rechte am "
            "Entwurf zustehen, regelt der Vertrag nicht. M meldet den Stuhl auf ihren Namen als Design an.",
            [frage("Steht das Recht auf das Design nach § 7 Abs. 2 DesignG der M zu?", False,
                   ["**Nein!** § 7 Abs. 2 DesignG weist das Recht nur bei Entwürfen von **Arbeitnehmern** dem Arbeitgeber zu. Für Auftragsentwürfe "
                    "freier Designer gilt die Regel nicht (zur Parallelnorm Art. 14 Abs. 3 GGV: EuGH FEIA)."],
                   merke="Auftrag ist kein Arbeitsverhältnis.", titel="Auftrag statt Arbeitsvertrag"),
             frage("Wem steht das Recht auf das Design dann zu?", 1,
                   ["**F als Entwerferin.** Das Recht steht dem Entwerfer oder seinem Rechtsnachfolger zu (§ 7 Abs. 1 S. 1 DesignG). M wird nur "
                    "Rechtsnachfolgerin, wenn F es ihr vertraglich überträgt (EuGH FEIA); die Honorarzahlung allein genügt nicht. Ob ein Auftrag "
                    "stillschweigend eine Übertragung enthält, ist Auslegungsfrage."],
                   optionen=["M, weil sie das Honorar gezahlt hat", "F als Entwerferin, solange sie es nicht vertraglich überträgt",
                             "M und F gemeinschaftlich", "Niemandem; der Entwurf ist gemeinfrei"],
                   merke="Ohne Übertragung bleibt das Recht beim Entwerfer.", titel="Inhaberin des Rechts", level=2),
             frage("Kann F von M die Übertragung des eingetragenen Designs verlangen?", True,
                   ["**Ja!** Ist ein Design auf den Namen eines nicht nach § 7 DesignG Berechtigten eingetragen, kann der Berechtigte die "
                    "**Übertragung** oder die Einwilligung in die Löschung verlangen (§ 9 Abs. 1 S. 1 DesignG)."],
                   merke="§ 9 Abs. 1 DesignG: Übertragung oder Löschung.", titel="Übertragungsanspruch", norms=["§ 9 DesignG"]),
             frage("Kann F noch Übertragung verlangen?", False,
                   ["**Nein!** Die Ansprüche aus § 9 Abs. 1 DesignG können nur binnen einer **Ausschlussfrist von drei Jahren** ab Bekanntmachung "
                    "durch Klage geltend gemacht werden (§ 9 Abs. 2 S. 1 DesignG). Die Frist gilt nur dann nicht, wenn M bei der Anmeldung "
                    "bösgläubig war (§ 9 Abs. 2 S. 2 DesignG)."],
                   abwandlung="F klagt erst vier Jahre nach der Bekanntmachung; M hielt sich bei der Anmeldung für berechtigt.",
                   merke="Drei Jahre ab Bekanntmachung, außer bei Bösgläubigkeit.", titel="Ausschlussfrist", level=2, norms=["§ 9 DesignG"]),
            ],
            abschnitt="§ 7 Abs. 1 DesignG: Entwerfer und Auftraggeber", level=1, concepts=["des_entwerfer_recht", "des_vindikation"],
            norms=["§ 7 DesignG"], cases=["des_eugh_feia"], step=f"step:des_schema_anmeldung.1"),
        *fallkette("d02n7-2", "Die angestellte Designerin",
            "A ist als Produktdesignerin bei einem Leuchtenhersteller angestellt. Sie entwirft im Büro eine Tischleuchte für die neue Kollektion "
            "und am Wochenende, ohne Bezug zu ihren Aufgaben, einen Fahrradständer. Der Arbeitsvertrag sagt zu Designrechten nichts.",
            [frage("Gehört das Recht an der Tischleuchte dem Arbeitgeber?", True,
                   ["**Ja!** Wird ein Design von einem Arbeitnehmer in Ausübung seiner Aufgaben oder nach den Weisungen seines Arbeitgebers "
                    "entworfen, steht das Recht dem **Arbeitgeber** zu, sofern vertraglich nichts anderes vereinbart ist (§ 7 Abs. 2 DesignG)."],
                   merke="Arbeitnehmerdesign gehört dem Arbeitgeber.", titel="Dienstentwurf"),
             frage("Gehört dem Arbeitgeber auch der Fahrradständer?", False,
                   ["**Nein!** Der Ständer entstand weder in Ausübung der Aufgaben noch auf Weisung. Es bleibt bei der Grundregel: Das Recht steht A "
                    "als Entwerferin zu (§ 7 Abs. 1 S. 1 DesignG)."],
                   merke="Freizeitentwurf ohne Aufgabenbezug bleibt beim Entwerfer.", titel="Freier Entwurf"),
             frage("Kann A verlangen, im Register als Entwerferin der Tischleuchte genannt zu werden?", True,
                   ["**Ja!** Das Recht, im Verfahren vor dem DPMA und im Register als Entwerfer benannt zu werden, hat der Entwerfer gegenüber dem "
                    "Anmelder oder Rechtsinhaber unabhängig davon, wem das Design gehört (§ 10 DesignG)."],
                   merke="Nennung steht dem Entwerfer immer zu.", titel="Entwerferbenennung", norms=["§ 10 DesignG"]),
             frage("Schuldet der Arbeitgeber A für die Leuchte eine gesetzliche Sondervergütung wie für eine Diensterfindung?", False,
                   ["**Nein!** Das DesignG enthält keine Vergütungsregel; das ArbnErfG gilt nur für Erfindungen und technische "
                    "Verbesserungsvorschläge. Eine Vergütung kann sich aber aus dem Vertrag ergeben."],
                   merke="Kein ArbnErfG für Designs.", titel="Vergütung?", level=2),
            ],
            abschnitt="§ 7 Abs. 2 DesignG: Arbeitnehmerdesign", level=1, concepts=["des_arbeitnehmerdesign", "des_entwerfer_recht"],
            norms=["§ 7 DesignG"], step=f"step:des_schema_anmeldung.1"),
        *fallkette("d02n7-3", "Die Vase zu zweit",
            "B und C entwerfen gemeinsam eine Vase. B meldet sie allein auf seinen Namen an und erteilt dem Händler L eine einfache Lizenz; L "
            "vertreibt die Vase seit einem Jahr gutgläubig. C klagt rechtzeitig gegen B.",
            [frage("Kann C von B die Übertragung des ganzen Designs verlangen?", False,
                   ["**Nein!** Haben mehrere ein Design gemeinsam entworfen, steht ihnen das Recht gemeinschaftlich zu (§ 7 Abs. 1 S. 2 DesignG). Wer "
                    "von mehreren Berechtigten nicht eingetragen ist, kann die **Einräumung der Mitinhaberschaft** verlangen (§ 9 Abs. 1 S. 3 DesignG)."],
                   merke="Miterfinder des Designs: Mitinhaberschaft, nicht Alleinrecht.", titel="Gemeinsamer Entwurf"),
             frage("Erlischt damit die Lizenz des L?", True,
                   ["**Ja!** Bei vollständigem Wechsel der Rechtsinhaberschaft nach § 9 Abs. 1 S. 1 DesignG erlöschen mit der Eintragung des "
                    "Berechtigten Lizenzen und sonstige Rechte (§ 9 Abs. 3 S. 1 DesignG)."],
                   abwandlung="C hat die Vase allein entworfen; B hatte sie nur gesehen. C erreicht die Übertragung und wird eingetragen.",
                   merke="Vollständiger Inhaberwechsel lässt Lizenzen erlöschen.", titel="Schicksal der Lizenz", level=2),
             frage("Kann L den Vertrieb fortsetzen, wenn er bei C binnen eines Monats nach dessen Eintragung eine einfache Lizenz beantragt?", True,
                   ["**Ja!** Wer das Design gutgläubig verwertet oder ernsthafte Anstalten dazu getroffen hat, kann die Verwertung fortsetzen, wenn "
                    "er innerhalb eines Monats eine einfache Lizenz beantragt; sie ist für einen angemessenen Zeitraum zu angemessenen Bedingungen zu "
                    "gewähren (§ 9 Abs. 3 S. 2 und 3 DesignG)."],
                   merke="Gutgläubiger Lizenznehmer: binnen eines Monats Lizenz beantragen.", titel="Weiterbenutzung", level=3),
            ],
            abschnitt="§ 9 DesignG: Ansprüche gegen den Nichtberechtigten", level=2, concepts=["des_vindikation", "des_lizenz"],
            norms=["§ 9 DesignG", "§ 7 DesignG"]),
        *fallkette("d02n7-4", "Die Anmeldung durch den Falschen",
            "Händler H hat auf einer Messe den Entwurf der Designerin D gesehen und ihn vor ihr beim DPMA als Design angemeldet. D entdeckt die "
            "Eintragung und überlegt, wie sie vorgehen soll.",
            [frage("Durfte das DPMA das Design für H eintragen, obwohl er nicht der Entwerfer ist?", True,
                   ["**Ja!** Im Verfahren vor dem DPMA gelten Anmelder und Rechtsinhaber als berechtigt und verpflichtet (§ 8 DesignG). Das Amt prüft "
                    "die materielle Berechtigung nicht (§§ 16, 18 DesignG)."],
                   merke="Formelle Berechtigung: Der Anmelder gilt als berechtigt.", titel="Formelle Berechtigung", norms=["§ 8 DesignG"]),
             frage("Kann D gerade wegen der fehlenden Berechtigung des H die Nichtigkeit beim DPMA geltend machen?", False,
                   ["**Nein!** Die Nichtberechtigung ist im DesignG **kein Nichtigkeitsgrund**; § 33 DesignG nennt sie nicht. D muss die Übertragung "
                    "oder die Einwilligung in die Löschung vor dem Landgericht einklagen (§ 9 Abs. 1 DesignG, § 52 DesignG)."],
                   merke="Nichtberechtigung: Klage nach § 9 DesignG, kein Nichtigkeitsantrag.", titel="Kein Nichtigkeitsgrund", level=2,
                   norms=["§ 33 DesignG", "§ 52 DesignG"]),
             frage("Hätte D in diesem Fall einen Nichtigkeitsgrund?", True,
                   ["**Ja!** Ein Unionsgeschmacksmuster kann für nichtig erklärt werden, wenn der Inhaber nach einer Entscheidung des zuständigen "
                    "Gerichts nicht nach Art. 14 GGV berechtigt ist (Art. 25 Abs. 1 lit. c GGV); geltend machen kann das nur der Berechtigte "
                    "(Art. 25 Abs. 3 GGV)."],
                   abwandlung="H hat das Design nicht beim DPMA, sondern beim EUIPO als eingetragenes Unionsgeschmacksmuster angemeldet.",
                   merke="GGV: Nichtberechtigung ist Nichtigkeitsgrund, DesignG: nicht.", titel="Unionsrecht anders", level=3,
                   norms=["Art. 25 GGV", "Art. 14 GGV"]),
            ],
            abschnitt="§ 8 DesignG: Formelle Berechtigung", level=1, concepts=["des_entwerfer_recht", "des_vindikation"],
            norms=["§ 8 DesignG"], step=f"step:des_schema_anmeldung.1"),
    ]),
    # ================================================================== §§ 33, 34 DesignG
    dict(id="d02n33", titel="§§ 33, 34 DesignG: Nichtigkeitsgründe und Antragsbefugnis", einheiten=[
        intro("d02n33-0", "Absolute und relative Gründe",
              "§ 33 DesignG unterscheidet **absolute** Gründe, bei denen die Nichtigkeit festgestellt wird (Abs. 1: kein Design, fehlende Neuheit oder "
              "Eigenart, Ausschluss nach § 3 DesignG), und **relative** Gründe, bei denen sie erklärt wird (Abs. 2: unerlaubte Benutzung eines "
              "urheberrechtlich geschützten Werkes, Kollision mit einem älteren eingetragenen Design, Verwendung eines älteren Zeichens mit "
              "Unterscheidungskraft). Die Feststellung kann **jedermann** beantragen, die Erklärung nur der Inhaber des betroffenen Rechts "
              "(§ 34 DesignG). Entschieden wird vom DPMA oder auf Widerklage vom Designgericht (§ 33 Abs. 3, § 52b DesignG); eine bloße Einrede "
              "genügt nicht (§ 52a DesignG). Die Nichtigkeit wirkt auf den Anfang zurück (§ 33 Abs. 4 DesignG), auch nach Ablauf oder Verzicht "
              "(Abs. 5); dasselbe gilt für die Einwilligung des Inhabers in die Löschung (Abs. 6).",
              norms=["§ 33 DesignG", "§ 34 DesignG", "§ 52a DesignG", "§ 52b DesignG"], concepts=["des_nichtigkeit", "des_widerklage_nichtigkeit"],
              abschnitt="Überblick"),
        *fallkette("d02n33-1", "Die Sportbrille in zwei Kontrasten",
            "S hat ein Design für eine Sportbrille mit Schwarz-Weiß-Fotos angemeldet. Eine Aufnahme zeigt helle Bügel an dunklem Rahmen, eine andere "
            "dunkle Bügel an hellem Rahmen. Wettbewerber W beantragt beim DPMA die Feststellung der Nichtigkeit.",
            [frage("Auf welchen Nichtigkeitsgrund stützt W den Antrag am besten?", 0,
                   ["**§ 33 Abs. 1 Nr. 1 DesignG.** Eine Graustufen-Fotografie macht den Hell-Dunkel-Kontrast zum Schutzgegenstand. Zeigen die "
                    "Aufnahmen den Kontrast einmal so und einmal umgekehrt, geben sie nicht die Erscheinungsform **eines** Erzeugnisses wieder; es fehlt "
                    "ein einheitlicher Schutzgegenstand, das Design ist nichtig (BGH Sportbrille, Sporthelm)."],
                   optionen=["§ 33 Abs. 1 Nr. 1 DesignG: kein Design, weil ein einheitlicher Schutzgegenstand fehlt",
                             "§ 33 Abs. 1 Nr. 3 DesignG: technische Bedingtheit", "§ 33 Abs. 2 Nr. 2 DesignG: älteres Design",
                             "Keiner; Abweichungen zwischen Wiedergaben sind stets unbeachtlich"],
                   merke="Widersprüchliche Wiedergaben: kein einheitlicher Schutzgegenstand.", titel="Passender Nichtigkeitsgrund", level=2,
                   cases=["des_bgh_sporthelm"]),
             frage("Kann W den Antrag stellen, ohne selbst von dem Design betroffen zu sein?", True,
                   ["**Ja!** Die Feststellung der Nichtigkeit nach § 33 Abs. 1 DesignG kann **jedermann** beantragen (§ 34 S. 1 DesignG); eine eigene "
                    "Betroffenheit verlangt das Gesetz nur für Abs. 2 und für Hoheitszeichen."],
                   merke="Absolute Gründe: Popularantrag.", titel="Jedermann", norms=["§ 34 DesignG"]),
             frage("Wird der Antrag damit gegenstandslos?", False,
                   ["**Nein!** Die Nichtigkeit kann auch nach einem Verzicht oder nach Ablauf der Schutzdauer festgestellt werden (§ 33 Abs. 5 DesignG). "
                    "Das hat Gewicht, weil die Feststellung auf den Anfang zurückwirkt (§ 33 Abs. 4 DesignG), etwa für Ansprüche aus der Vergangenheit."],
                   abwandlung="S verzichtet nach Eingang des Antrags auf das Design.",
                   merke="Verzicht beendet das Nichtigkeitsverfahren nicht von selbst.", titel="Verzicht", level=2),
            ],
            abschnitt="Abs. 1: Absolute Gründe", level=2, concepts=["des_nichtigkeit", "des_schutzgegenstand"], norms=["§ 33 Abs. 1 DesignG"],
            cases=["des_bgh_sportbrille"], step=f"{NV}.3.1"),
        *fallkette("d02n33-2", "Die Emblemhalterung",
            "D hat ein Design für eine Emblemhalterung am Kühlergrill eingetragen, deren Umriss die vier Ringe der eingetragenen Marke des "
            "Autoherstellers A nachbildet. Ein Zubehörhändler Z und A wollen gegen das Design vorgehen.",
            [frage("Kann Z die Erklärung der Nichtigkeit wegen der Marke des A beantragen?", False,
                   ["**Nein!** Die Verwendung eines älteren Zeichens mit Unterscheidungskraft ist ein relativer Grund (§ 33 Abs. 2 Nr. 3 DesignG). "
                    "Den Antrag auf Erklärung der Nichtigkeit kann nur der Inhaber des betroffenen Rechts stellen, hier A (§ 34 S. 2 DesignG)."],
                   merke="Relative Gründe: nur der Rechtsinhaber.", titel="Antragsbefugnis bei Abs. 2", norms=["§ 34 DesignG"]),
             frage("Hat A Erfolg, wenn er die Verwendung der Ringe nach Markenrecht untersagen kann?", True,
                   ["**Ja!** § 33 Abs. 2 Nr. 3 DesignG setzt voraus, dass der Zeicheninhaber berechtigt ist, die Verwendung zu untersagen; das richtet "
                    "sich nach dem Markenrecht (§ 14 MarkenG). Dann wird das Design für nichtig erklärt."],
                   merke="Abs. 2 Nr. 3: Maßstab ist das Verbietungsrecht aus der Marke.", titel="Älteres Zeichen", level=2),
             frage("Welche Gründe kann Z als Jedermann geltend machen?", 0,
                   ["**Die absoluten Gründe des § 33 Abs. 1 DesignG.** Die Feststellung der Nichtigkeit kann jedermann beantragen (§ 34 S. 1 DesignG). "
                    "Hatte D die Halterung schon Jahre vor der Anmeldung selbst angeboten, kommt fehlende Neuheit oder Eigenart in Betracht "
                    "(§ 33 Abs. 1 Nr. 2 DesignG)."],
                   optionen=["Nur die Gründe des § 33 Abs. 1 DesignG, etwa fehlende Neuheit oder Eigenart", "Alle Gründe des § 33 DesignG",
                             "Nur die Kollision mit älteren Designs", "Keine, solange D ihn nicht abgemahnt hat"],
                   merke="Jedermann: Abs. 1; Rechtsinhaber: Abs. 2.", titel="Gründe des Jedermann", level=1),
            ],
            abschnitt="Abs. 2: Relative Gründe", level=1, concepts=["des_nichtigkeit"], norms=["§ 33 Abs. 2 DesignG"],
            cases=["des_bpatg_emblemhalterung"], step=f"{NV}.3.2"),
        *fallkette("d02n33-3", "Die Einwilligung in die Löschung",
            "Gegen das Design der I läuft ein Nichtigkeitsverfahren. I erkennt, dass eine ältere Vase dieselbe Gestalt hatte, und erklärt gegenüber "
            "dem DPMA ihre Einwilligung in die Löschung. Zuvor hatte sie den Nachahmer N auf Schadensersatz verklagt.",
            [frage("Gelten die Schutzwirkungen nach der Einwilligung als von Anfang an nicht eingetreten?", True,
                   ["**Ja!** Willigt der Inhaber in den Fällen des § 33 Abs. 1 und 2 DesignG in die Löschung ein, gelten die Schutzwirkungen als **von "
                    "Anfang an nicht eingetreten** (§ 33 Abs. 6 DesignG). Darin liegt der Unterschied zum Verzicht."],
                   merke="Einwilligung in die Löschung wirkt zurück.", titel="Rückwirkung"),
             frage("Kann I gegen N noch Schadensersatz für die Zeit vor der Löschung verlangen?", False,
                   ["**Nein!** Weil das Design als von Anfang an wirkungslos gilt, fehlt auch für die Vergangenheit ein verletztes Recht "
                    "(§ 33 Abs. 6 S. 2 DesignG). Die Klage aus § 42 Abs. 2 DesignG wird unbegründet."],
                   merke="Ohne Recht keine Verletzung, auch rückblickend.", titel="Folgen für den Verletzungsprozess", level=2,
                   norms=["§ 42 Abs. 2 DesignG"]),
             frage("Kann das Design in geänderter Form bestehen bleiben?", True,
                   ["**Ja**, durch Feststellung der Teilnichtigkeit oder Teilverzicht, wenn das Design danach die Schutzvoraussetzungen erfüllt und seine "
                    "**Identität** behält (§ 35 Abs. 1 Nr. 1 DesignG); eine geänderte Wiedergabe ist einzureichen (§ 35 Abs. 2 DesignG)."],
                   abwandlung="I willigt nicht ein: Vorbekannt war nur die Gestalt der Vase, ihre aufgedruckte Ornamentik ist neu und eigenartig.",
                   merke="Teilweise Aufrechterhaltung nur bei gewahrter Identität.", titel="Teilweise Aufrechterhaltung", level=3,
                   norms=["§ 35 DesignG"], step=f"{NV}.3.3"),
            ],
            abschnitt="Abs. 4 bis 6: Wirkung und Einwilligung", level=2, concepts=["des_nichtigkeit", "des_teilweise_aufrechterhaltung"],
            norms=["§ 33 Abs. 4 DesignG", "§ 33 Abs. 6 DesignG"]),
    ]),
    # ================================================================== § 34a DesignG
    dict(id="d02n34a", titel="§ 34a DesignG: Das Nichtigkeitsverfahren vor dem DPMA", einheiten=[
        schema("d02n34a-0", "Prüfungsschema Nichtigkeitsverfahren", "des_schema_nichtigkeitsverfahren",
               "Das Nichtigkeitsverfahren ist ein streitiges Verfahren vor einer Designabteilung des DPMA (§ 23 Abs. 2 DesignG): schriftlicher Antrag "
               "mit Tatsachen und Beweismitteln (§ 34a Abs. 1 DesignG) und Gebühr von 300 € je Design; Zustellung an den Inhaber mit Monatsfrist, "
               "ohne Widerspruch wird die Nichtigkeit ohne Sachprüfung festgestellt oder erklärt (Abs. 2); sonst Vorbereitung, Anhörung auf Antrag "
               "oder bei Sachdienlichkeit, Beweisaufnahme (Abs. 3); Beschluss (Abs. 4) mit Kostenentscheidung nach der ZPO, soweit nicht die "
               "Billigkeit anderes erfordert (Abs. 5), und Gegenstandswert (Abs. 6); Beschwerde zum BPatG (§ 23 Abs. 4 DesignG).",
               abschnitt="Überblick"),
        *fallkette("d02n34a-1", "Die Emblemhalterung: Einwilligung und Kosten",
            "A beantragt beim DPMA ohne Vorwarnung, die Nichtigkeit des Designs der D festzustellen. Drei Wochen nach Zustellung willigt D in die "
            "Löschung ein. Beide erklären das Verfahren für erledigt; streitig sind nur noch die Kosten.",
            [frage("Muss die Designabteilung jetzt noch über die Nichtigkeit entscheiden?", False,
                   ["**Nein!** Erklären die Beteiligten das Verfahren in der Hauptsache für erledigt, wird es durch Beschluss **eingestellt** "
                    "(§ 34a Abs. 2 S. 3 DesignG). Über die Kosten entscheidet das DPMA dann nur auf Antrag (§ 34a Abs. 5 S. 2 DesignG)."],
                   merke="Erledigung: Einstellung, Kosten nur auf Antrag.", titel="Erledigung", step=f"{NV}.2"),
             frage("Trägt D als Unterlegene die Kosten?", False,
                   ["**Nein!** Über § 34a Abs. 5 DesignG und § 84 Abs. 2 PatG gilt der Rechtsgedanke des § 93 ZPO. Die Einwilligung in die Löschung "
                    "binnen der Widerspruchsfrist steht einem **sofortigen Anerkenntnis** gleich. Hat D keinen Anlass zum Antrag gegeben, trägt A die "
                    "Kosten (BPatG Kühlergitter-Emblemhalterung)."],
                   merke="Sofortige Einwilligung ohne Anlass: Kosten beim Antragsteller.", titel="Sofortiges Anerkenntnis", level=2),
             frage("Was hätte A tun müssen, um dieses Kostenrisiko zu vermeiden?", 1,
                   ["**Eine Verzichtsaufforderung.** Anlass zum Antrag gibt der Inhaber grundsätzlich erst, wenn er auf eine Aufforderung mit "
                    "substantiierten Nichtigkeitsgründen und angemessener Frist nicht reagiert hat. Entbehrlich ist sie nur, wenn sie aussichtslos oder "
                    "unzumutbar erscheint (BPatG Kühlergitter-Emblemhalterung)."],
                   optionen=["Nichts; im Nichtigkeitsverfahren trägt stets der Inhaber die Kosten",
                             "D vorher unter Angabe der Gründe und mit Frist zum Verzicht oder zur Einwilligung in die Löschung auffordern",
                             "Den Antrag beim Landgericht statt beim DPMA stellen", "Sofort Beschwerde zum BPatG einlegen"],
                   merke="Erst auffordern, dann beantragen.", titel="Verzichtsaufforderung", level=2),
             frage("Macht das die Aufforderung entbehrlich?", False,
                   ["**Nein!** Wer sich nur in der Antwort auf eine Abmahnung auf sein Design beruft, geht nicht aktiv aus dem Design vor; die "
                    "vorprozessuale Ebene ist nicht verlassen. Anders kann es liegen, wenn der Inhaber selbst Verletzungsklage aus dem Design erhoben "
                    "hat (BPatG Kühlergitter-Emblemhalterung)."],
                   abwandlung="D hatte sich auf eine markenrechtliche Abmahnung des A hin auf ihre Designanmeldung berufen.",
                   merke="Passive Berufung auf das Design ersetzt die Aufforderung nicht.", titel="Berufung auf das Design", level=3),
            ],
            abschnitt="Abs. 2 und 5: Widerspruch, Erledigung, Kosten", level=2, concepts=["des_nichtigkeitsverfahren_dpma"],
            norms=["§ 34a Abs. 2 DesignG", "§ 34a Abs. 5 DesignG", "§ 33 Abs. 6 DesignG"], cases=["des_bpatg_emblemhalterung"], step=f"{NV}.4"),
        *fallkette("d02n34a-2", "Zweiter Anlauf",
            "Wettbewerber W unterlag vor dem Landgericht rechtskräftig mit seiner Widerklage, mit der er die Nichtigkeit des Designs der I wegen "
            "fehlender Eigenart festgestellt haben wollte. Nun stellt W beim DPMA einen Nichtigkeitsantrag mit denselben Entgegenhaltungen.",
            [frage("Ist der Antrag des W zulässig?", False,
                   ["**Nein!** Der Antrag ist unzulässig, soweit über denselben Streitgegenstand zwischen den Parteien durch unanfechtbaren Beschluss "
                    "oder **rechtskräftiges Urteil** entschieden wurde (§ 34a Abs. 1 S. 4 DesignG). Das Urteil über die Widerklage (§ 52b DesignG) "
                    "sperrt den neuen Antrag."],
                   merke="Rechtskraft sperrt zwischen denselben Parteien.", titel="Entgegenstehende Rechtskraft", step=f"{NV}.1.4"),
             frage("Ist der Antrag des K zulässig?", True,
                   ["**Ja!** Die Sperre wirkt nur zwischen den Parteien (§ 34a Abs. 1 S. 4 DesignG). K kann als jedermann die Feststellung der "
                    "Nichtigkeit beantragen (§ 34 S. 1 DesignG), auch gestützt auf dieselben Entgegenhaltungen."],
                   abwandlung="Den Antrag stellt nicht W, sondern sein Konkurrent K, der am Prozess nicht beteiligt war.",
                   merke="Dritte bindet das Urteil nicht.", titel="Antrag eines Dritten", step=f"{NV}.1.4"),
             frage("Was muss K mit dem Antrag einreichen?", 1,
                   ["**Einen schriftlichen Antrag mit Tatsachen und Beweismitteln** (§ 34a Abs. 1 S. 1 und 2 DesignG), dazu die Gebühr von 300 € für "
                    "jedes angegriffene Design (Gebührenverzeichnis zum PatKostG). Wird sie nicht rechtzeitig gezahlt, gilt der Antrag als "
                    "zurückgenommen (§ 6 Abs. 2 PatKostG)."],
                   optionen=["Nur den Antrag; das DPMA ermittelt den Formenschatz von Amts wegen",
                             "Einen schriftlichen Antrag mit Tatsachen und Beweismitteln, dazu 300 € Gebühr je Design",
                             "Die Vollmacht eines Patentanwalts", "Eine Erklärung, dass K selbst vom Design betroffen ist"],
                   merke="Antrag, Begründung, Beweismittel, 300 € je Design.", titel="Form und Gebühr", step=f"{NV}.1.1"),
            ],
            abschnitt="Abs. 1: Antrag", level=1, concepts=["des_nichtigkeitsverfahren_dpma"], norms=["§ 34a Abs. 1 DesignG"]),
        *fallkette("d02n34a-3", "Was ist ein Helmdesign wert?",
            "Nach einem erfolgreichen Nichtigkeitsverfahren gegen das Design für einen Sporthelm beantragt die Antragstellerin, den Gegenstandswert "
            "für die Anwaltsgebühren festzusetzen. Sie hält 250.000 € für angemessen; der Inhaber meint, 10.000 € genügten.",
            [frage("Auf wessen Interesse kommt es für den Gegenstandswert an?", 1,
                   ["**Auf das Interesse des Inhabers.** Der Gegenstandswert wird nach billigem Ermessen bestimmt (§ 34a Abs. 6 DesignG mit § 23 Abs. 3 "
                    "S. 2 RVG); maßgeblich ist das wirtschaftliche Interesse des Designinhabers an der Aufrechterhaltung seines Designs (BGH "
                    "Gegenstandswert Sporthelm)."],
                   optionen=["Auf das Interesse der Antragstellerin an der Beseitigung", "Auf das Interesse des Inhabers an der Aufrechterhaltung",
                             "Auf die Höhe der Amtsgebühr", "Auf den Umsatz aller Anbieter von Helmen"],
                   merke="Gegenstandswert: Interesse des Inhabers.", titel="Maßgebliches Interesse", level=2),
             frage("Ist ohne besondere Anhaltspunkte ein Wert von 50.000 € festzusetzen?", True,
                   ["**Ja!** Im designrechtlichen Nichtigkeitsverfahren entspricht ein Gegenstandswert von **50.000 €** im Regelfall billigem Ermessen "
                    "(BGH Gegenstandswert Sporthelm). Für einen höheren oder niedrigeren Wert braucht es konkrete Anhaltspunkte."],
                   merke="Regelwert 50.000 €.", titel="Regelwert"),
             frage("Werden die Kosten im Nichtigkeitsverfahren ausnahmslos nach dem Unterliegen verteilt?", False,
                   ["**Nein!** § 34a Abs. 5 DesignG verweist auf § 84 Abs. 2 S. 2 PatG: Die Kostenvorschriften der ZPO gelten entsprechend, soweit nicht "
                    "die **Billigkeit** eine andere Entscheidung erfordert. Grundsatz ist das Unterliegensprinzip; Ausnahmen folgen etwa aus dem "
                    "Rechtsgedanken des § 93 ZPO."],
                   merke="Unterliegensprinzip mit Billigkeitsvorbehalt.", titel="Kostengrundsatz", level=2,
                   cases=["des_bpatg_emblemhalterung"]),
            ],
            abschnitt="Abs. 5 und 6: Kosten und Gegenstandswert", level=1, concepts=["des_nichtigkeitsverfahren_dpma"],
            norms=["§ 34a Abs. 5 DesignG", "§ 34a Abs. 6 DesignG"], cases=["des_bgh_gegenstandswert_sporthelm"], step=f"{NV}.4"),
        *fallkette("d02n34a-4", "Anhörung und Beitritt",
            "Gegen das Design des I läuft auf Antrag des W ein Nichtigkeitsverfahren; I hat rechtzeitig widersprochen. W beantragt eine mündliche "
            "Anhörung. Händler H erhält zwei Monate nach Einleitung des Verfahrens eine Abmahnung des I wegen desselben Designs.",
            [frage("Muss die Designabteilung eine Anhörung durchführen?", True,
                   ["**Ja!** Eine Anhörung findet statt, wenn ein Beteiligter sie **beantragt** oder das DPMA sie für sachdienlich hält "
                    "(§ 34a Abs. 3 S. 2 DesignG)."],
                   merke="Anhörung auf Antrag eines Beteiligten.", titel="Anhörung", step=f"{NV}.4"),
             frage("Kann H dem laufenden Verfahren beitreten?", True,
                   ["**Ja!** Wer aufgefordert wurde, eine behauptete Verletzung desselben Designs zu unterlassen, kann dem Nichtigkeitsverfahren binnen "
                    "**drei Monaten** ab Zugang der Aufforderung beitreten, solange keine unanfechtbare Entscheidung vorliegt (§ 34c Abs. 1 DesignG). "
                    "Der Beitritt erfolgt durch eigenen Antrag (§ 34c Abs. 2 DesignG)."],
                   merke="Beitritt des Abgemahnten: drei Monate.", titel="Beitritt", level=2, norms=["§ 34c DesignG"], step=f"{NV}.6.2"),
             frage("Entscheidet über den Antrag ein einzelnes Mitglied der Designstelle?", False,
                   ["**Nein!** Im Nichtigkeitsverfahren beschließt eine **Designabteilung** mit drei rechtskundigen Mitgliedern (§ 23 Abs. 2 DesignG); "
                    "gegen ihren Beschluss findet die Beschwerde zum BPatG statt (§ 23 Abs. 4 DesignG)."],
                   merke="Nichtigkeit: Designabteilung, drei Juristen.", titel="Zuständigkeit im DPMA", norms=["§ 23 DesignG"], step=f"{NV}.5"),
            ],
            abschnitt="Abs. 3 und § 34c DesignG: Anhörung, Beitritt, Zuständigkeit", level=1, concepts=["des_nichtigkeitsverfahren_dpma"],
            norms=["§ 34a Abs. 3 DesignG"]),
    ]),
    # ================================================================== §§ 37, 38 DesignG
    dict(id="d02n37", titel="§§ 37, 38 DesignG: Schutzgegenstand, Rechte und Schutzumfang", einheiten=[
        intro("d02n37-0", "Was geschützt ist und wie weit",
              "§ 37 Abs. 1 DesignG bestimmt den **Schutzgegenstand**: geschützt sind die Merkmale der Erscheinungsform, die in der Anmeldung sichtbar "
              "wiedergegeben sind; mehrere Darstellungen werden ausgelegt, Teile genießen keinen eigenen Schutz. § 38 Abs. 1 DesignG gibt ein "
              "ausschließliches Benutzungs- und Verbietungsrecht; Benutzung ist insbesondere Herstellen, Anbieten, Inverkehrbringen, Einfuhr, "
              "Ausfuhr, Gebrauch und Besitz zu diesen Zwecken. Der **Schutzumfang** erstreckt sich auf jedes Design, das beim informierten Benutzer "
              "keinen anderen Gesamteindruck erweckt, unter Berücksichtigung der Gestaltungsfreiheit (§ 38 Abs. 2 DesignG), spiegelbildlich zur "
              "Eigenart. Das eingetragene Design ist ein Sperrrecht; Nachahmung setzt es nur während der Aufschiebung der Bekanntmachung voraus "
              "(§ 38 Abs. 3 DesignG). Erzeugnisangabe und Warenklasse beschränken den Schutz nicht (§ 11 Abs. 6 DesignG).",
              norms=["§ 37 DesignG", "§ 38 DesignG", "§ 11 Abs. 6 DesignG"], concepts=["des_schutzgegenstand", "des_schutzumfang", "des_benutzung"],
              abschnitt="Überblick"),
        *fallkette("d02n37-1", "Die Weinkaraffe",
            "K hat ein Design für eine Weinkaraffe mit sechs Ansichten eingetragen; Erzeugnisangabe: „Karaffen“. Prägend ist ein eigenwillig "
            "geformter Hals. Wettbewerber W verkauft eine Karaffe mit ganz anderem Körper, aber gleichem Hals.",
            [frage("Bilden die sechs Ansichten sechs Schutzgegenstände?", False,
                   ["**Nein!** Mehrere Darstellungen zeigen ein Design aus verschiedenen Blickwinkeln; sie bilden **einen** Schutzgegenstand, "
                    "Unklarheiten sind durch Auslegung zu klären (BGH Weinkaraffe). Geschützt sind die sichtbar wiedergegebenen Merkmale "
                    "(§ 37 Abs. 1 DesignG)."],
                   merke="Viele Ansichten, ein Schutzgegenstand.", titel="Mehrere Ansichten", step=f"{VL}.2.2"),
             frage("Kann K gegen W allein wegen der Übernahme des Halses vorgehen?", False,
                   ["**Nein!** Teile oder Elemente eines eingetragenen Designs genießen keinen eigenständigen Schutz (BGH Weinkaraffe). Zu vergleichen "
                    "ist der Gesamteindruck des ganzen Designs mit dem der ganzen angegriffenen Karaffe (§ 38 Abs. 2 DesignG)."],
                   merke="Kein Elementeschutz: Verglichen wird das Ganze.", titel="Schutz für Teile?", level=2, step=f"{VL}.4.2"),
             frage("Kann auch eine Vase gleicher Gestalt das Design verletzen, obwohl es nur für „Karaffen“ eingetragen ist?", True,
                   ["**Ja!** Erzeugnisangabe und Warenklasse haben keinen Einfluss auf den Schutzumfang (§ 11 Abs. 6 DesignG). Maßgeblich ist allein, "
                    "ob die Vase beim informierten Benutzer keinen anderen Gesamteindruck erweckt (§ 38 Abs. 2 DesignG)."],
                   merke="Erzeugnisangabe begrenzt den Schutz nicht.", titel="Erzeugnisangabe", norms=["§ 11 Abs. 6 DesignG"]),
            ],
            abschnitt="§ 37 DesignG: Schutzgegenstand", level=1, concepts=["des_schutzgegenstand", "des_wiedergabe", "des_erzeugnisangabe"],
            norms=["§ 37 Abs. 1 DesignG"], cases=["des_bgh_weinkaraffe"]),
        *fallkette("d02n37-2", "Das Schneidebrett",
            "S hat ein Design für ein Schneidebrett mit umlaufender Saftrille eingetragen. Fünf Darstellungen zeigen das Brett allein, eine sechste "
            "zusätzlich eine eingelegte Auffangschale. S geht gegen ein Brett ohne Schale vor.",
            [frage("Ist das Design nichtig, weil die Darstellungen nicht übereinstimmen?", False,
                   ["**Nein**, nicht zwingend. Die Auslegung kann ergeben, dass Abweichungen außer Betracht bleiben und der Schutzgegenstand aus der "
                    "**Schnittmenge** der allen Darstellungen gemeinsamen Merkmale besteht, auch wenn eine Darstellung zusätzliche Elemente zeigt "
                    "(BGH Schneidebrett). Anders liegt es bei widersprüchlichen Ausführungsformen (BGH Sporthelm)."],
                   merke="Zusatzelement in einer Ansicht: Schnittmenge statt Nichtigkeit.", titel="Abweichende Darstellung", level=2,
                   cases=["des_bgh_sporthelm"]),
             frage("Kann das Brett ohne Schale das Design verletzen, obwohl eine Darstellung eine Schale zeigt?", True,
                   ["**Ja!** Besteht der Schutzgegenstand aus der Schnittmenge, gehört die Schale nicht zu den geschützten Merkmalen. Ihr Fehlen am "
                    "angegriffenen Brett steht einer Verletzung nicht entgegen; entscheidend ist der Gesamteindruck der gemeinsamen Merkmale."],
                   merke="Was nicht geschützt ist, muss der Verletzer nicht übernehmen.", titel="Folge für die Verletzung", level=2),
            ],
            abschnitt="§ 37 DesignG: Auslegung der Wiedergabe", level=2, concepts=["des_schutzgegenstand", "des_wiedergabe"],
            norms=["§ 37 Abs. 1 DesignG"], cases=["des_bgh_schneidebrett"], step=f"{VL}.2.2"),
        *fallkette("d02n37-3", "Der Kinderwagen",
            "K hat ein Gemeinschaftsgeschmacksmuster für einen Kinderwagen mit markantem Untergestell. W bringt einen Wagen mit ähnlichem Gestell, "
            "aber deutlich anderen Rädern, Griffen und Bremshebeln auf den Markt. W meint, Räder und Bremsen seien technisch bedingt und daher gleichgültig.",
            [frage("Hängt der Schutzumfang davon ab, wie dicht der Formenschatz bei Kinderwagen ist?", True,
                   ["**Ja!** Der Schutzumfang wird durch die **Musterdichte** und die Ausnutzung des Gestaltungsspielraums bestimmt (§ 38 Abs. 2 "
                    "DesignG, Art. 10 GGV; BGH Kinderwagen II). Je weiter das Design vom Formenschatz abrückt, desto weiter reicht sein Schutz "
                    "(BGH Untersetzer)."],
                   merke="Großer Abstand zum Formenschatz, großer Schutzumfang.", titel="Musterdichte und Schutzumfang", step=f"{VL}.4.1",
                   cases=["des_bgh_untersetzer"]),
             frage("Sind Unterschiede in technisch bedingten Merkmalen für den Gesamteindruck stets unbeachtlich?", False,
                   ["**Nein!** Übereinstimmungen in technisch bedingten Merkmalen misst der informierte Benutzer geringe Bedeutung bei. Daraus folgt "
                    "nicht, dass er **Unterschiede** in solchen Merkmalen ebenso gering gewichtet (BGH Kinderwagen II). Die anderen Räder und Bremsen "
                    "können zu einem anderen Gesamteindruck beitragen."],
                   merke="Technik: Übereinstimmung zählt wenig, Unterschied kann zählen.", titel="Technisch bedingte Unterschiede", level=3),
             frage("Aus welcher Sicht wird der Gesamteindruck verglichen?", 1,
                   ["**Aus der Sicht des informierten Benutzers bei bestimmungsgemäßer Verwendung.** Er nimmt das Erzeugnis so wahr, wie es im "
                    "Gebrauch erscheint; bei einer Armbanduhr also am Handgelenk, nicht die Rückseite. Ergänzend zählt die Präsentation in Werbung "
                    "und Verkauf (BGH Armbanduhr)."],
                   optionen=["Aus der Sicht des flüchtigen Durchschnittsverbrauchers", "Aus der Sicht des informierten Benutzers bei bestimmungsgemäßer Verwendung",
                             "Aus der Sicht eines Konstrukteurs", "Aus der Sicht des Gerichts ohne Bezug zur Benutzung"],
                   merke="Gesamteindruck im Gebrauch, aus Sicht des informierten Benutzers.", titel="Perspektive", level=1,
                   cases=["des_bgh_armbanduhr"], step=f"{VL}.4.2"),
            ],
            abschnitt="§ 38 Abs. 2 DesignG: Schutzumfang", level=2, concepts=["des_schutzumfang", "des_gesamteindruck", "des_technisch_bedingt"],
            norms=["§ 38 Abs. 2 DesignG", "Art. 10 GGV"], cases=["des_bgh_kinderwagen_ii"]),
        *fallkette("d02n37-4", "Die Tasse aus dem Katalog",
            "E hat ein Design für eine Tasse eingetragen und bekannt gemacht. Hersteller H hat danach, ohne das Design der E zu kennen, eine Tasse mit "
            "gleichem Gesamteindruck entworfen, lässt sie in Asien fertigen und bietet sie in seinem Katalog in Deutschland an.",
            [frage("Kann H sich darauf berufen, er habe das Design nicht nachgeahmt?", False,
                   ["**Nein!** Das eingetragene Design ist ein **Sperrrecht**: Es wirkt gegen jedes Design ohne anderen Gesamteindruck, auch gegen eine "
                    "unabhängige Parallelschöpfung (§ 38 Abs. 1 und 2 DesignG). Auf Nachahmung kommt es nur während der Aufschiebung der "
                    "Bekanntmachung an (§ 38 Abs. 3 DesignG)."],
                   merke="Eingetragenes Design: Sperrrecht, keine Nachahmung nötig.", titel="Sperrwirkung"),
             frage("Ist schon das Angebot im Katalog eine Benutzung?", True,
                   ["**Ja!** Benutzung schließt insbesondere das **Anbieten** ein (§ 38 Abs. 1 S. 2 DesignG); ein Verkauf ist nicht nötig. Schon dafür "
                    "kann der Inhaber Schadensersatz nach der Lizenzanalogie verlangen (BGH Catwalk)."],
                   merke="Anbieten ist Benutzung.", titel="Anbieten", step=f"{VL}.3"),
             frage("Kann E gegen H vorgehen?", False,
                   ["**Nein!** Während der Aufschiebung (§ 21 Abs. 1 DesignG) setzt der Schutz voraus, dass das angegriffene Design das Ergebnis einer "
                    "**Nachahmung** ist (§ 38 Abs. 3 DesignG). Hs unabhängiger Entwurf fällt nicht darunter."],
                   abwandlung="E hatte die Aufschiebung der Bekanntmachung beantragt; die Frist von 30 Monaten läuft noch.",
                   merke="Aufgeschobene Bekanntmachung: nur Schutz gegen Nachahmung.", titel="Aufschiebung", level=2,
                   norms=["§ 21 DesignG"]),
            ],
            abschnitt="§ 38 Abs. 1, 3 DesignG: Benutzung und Sperrwirkung", level=1, concepts=["des_benutzung", "des_aufschiebung"],
            norms=["§ 38 Abs. 1 DesignG", "§ 38 Abs. 3 DesignG"], step=f"{VL}.3"),
    ]),
    # ================================================================== §§ 40, 40a DesignG
    dict(id="d02n40", titel="§§ 40, 40a DesignG: Schranken und Reparaturklausel", einheiten=[
        intro("d02n40-0", "Wo das Recht endet",
              "§ 40 DesignG nimmt bestimmte Handlungen von den Rechten aus dem Design aus: (1) Handlungen im privaten Bereich zu nichtgewerblichen "
              "Zwecken, (2) Handlungen zu Versuchszwecken, (3) Wiedergaben zum Zwecke der Zitierung oder der Lehre, wenn sie mit dem redlichen "
              "Geschäftsverkehr vereinbar sind, die normale Verwertung nicht über Gebühr beeinträchtigen und die Quelle angeben, (4) und (5) "
              "Einrichtungen und Reparaturen ausländischer Schiffe und Luftfahrzeuge. Die **Reparaturklausel** des § 40a DesignG nimmt Bauelemente "
              "komplexer Erzeugnisse vom Schutz aus, die allein zur Reparatur verwendet werden, um das ursprüngliche Erscheinungsbild "
              "wiederherzustellen, wenn die Verbraucher über den Ursprung unterrichtet werden. Sie gilt nicht für Designs, die vor dem 2. Dezember "
              "2020 angemeldet wurden (§ 73 Abs. 2 DesignG). Für Unionsgeschmacksmuster gelten Art. 20 und Art. 20a GGV.",
              norms=["§ 40 DesignG", "§ 40a DesignG", "§ 73 DesignG", "Art. 20 GGV", "Art. 20a GGV"],
              concepts=["des_schranken", "des_zitierschranke", "des_reparaturklausel"], abschnitt="Überblick"),
        *fallkette("d02n40-1", "Zubehör für die Spielkonsole (Nintendo)",
            "BigBen verkauft Zubehör für eine Spielkonsole von Nintendo. Auf Verpackung und Website zeigt BigBen sein Zubehör zusammen mit der "
            "Konsole und deren Fernbedienung, die als Gemeinschaftsgeschmacksmuster geschützt sind. Nintendo verlangt Unterlassung.",
            [frage("Kann die Abbildung fremder geschützter Erzeugnisse in der eigenen Werbung eine Wiedergabe zum Zwecke der Zitierung sein?", True,
                   ["**Ja!** Wer rechtmäßig Zubehör vertreibt, darf die Erzeugnisse, für die es bestimmt ist, abbilden, um die gemeinsame Verwendung zu "
                    "erläutern; das ist eine Zitierung im Sinne von Art. 20 Abs. 1 lit. c GGV (EuGH Nintendo). § 40 Nr. 3 DesignG ist gleich gefasst. "
                    "Der Vertriebszweck schließt das Zitat nicht aus."],
                   merke="Zubehörwerbung kann Zitat sein.", titel="Zitat in der Werbung", level=2),
             frage("Muss BigBen dafür auch die Herkunft der abgebildeten Konsole angeben?", True,
                   ["**Ja!** Die Voraussetzungen gelten kumulativ: Vereinbarkeit mit den Gepflogenheiten des redlichen Geschäftsverkehrs, keine "
                    "übermäßige Beeinträchtigung der normalen Verwertung und **Angabe der Quelle** (§ 40 Nr. 3 DesignG, Art. 20 Abs. 2 GGV). Ob sie "
                    "erfüllt sind, prüft das nationale Gericht (EuGH Nintendo)."],
                   merke="Zitat: redlich, keine übermäßige Beeinträchtigung, Quelle.", titel="Quellenangabe", level=2),
             frage("Ist das eine Zitierung?", False,
                   ["**Nein!** Ein Zitat setzt eine **innere Verbindung** zwischen dem wiedergegebenen Design und eigenen Ausführungen voraus; das Design "
                    "muss als Beleg oder Erörterungsgrundlage dienen (BGH ICE). Ein Kalenderbild dient nur der Dekoration."],
                   abwandlung="Ein Verlag druckt das Foto eines als Design geschützten Hochgeschwindigkeitszugs ganzseitig auf einen Wandkalender.",
                   merke="Zitat braucht eigene Gedanken, an die es anknüpft.", titel="Kalenderbild", cases=["des_bgh_ice"]),
            ],
            abschnitt="§ 40 Nr. 3 DesignG: Zitat und Lehre", level=2, concepts=["des_zitierschranke", "des_schranken"],
            norms=["§ 40 DesignG", "Art. 20 GGV"], cases=["des_eugh_nintendo"], step=f"{VL}.5.1"),
        *fallkette("d02n40-2", "Die nachgedruckte Lampe",
            "Student P druckt mit seinem 3D-Drucker eine Lampe nach, deren Design eingetragen ist, und stellt sie in sein Zimmer. Das Labor eines "
            "Leuchtenherstellers baut dieselbe Lampe nach, um ihre Wärmeentwicklung zu messen.",
            [frage("Ist der Nachdruck für das eigene Zimmer von einer Schranke gedeckt?", True,
                   ["**Ja!** Rechte aus dem Design können nicht gegenüber Handlungen geltend gemacht werden, die im **privaten Bereich** zu "
                    "nichtgewerblichen Zwecken vorgenommen werden (§ 40 Nr. 1 DesignG). Beide Voraussetzungen liegen vor."],
                   merke="Privat und nichtgewerblich: frei.", titel="Privatbereich"),
             frage("Darf das Labor die Lampe für seine Messungen nachbauen?", True,
                   ["**Ja!** Handlungen zu **Versuchszwecken** sind ausgenommen (§ 40 Nr. 2 DesignG). Der Nachbau dient der Untersuchung des "
                    "Erzeugnisses, nicht dem Absatz."],
                   merke="Versuche am Erzeugnis sind frei.", titel="Versuchszwecke"),
             frage("Greift die Schranke für P dann noch?", False,
                   ["**Nein!** Der Verkauf verlässt den privaten Bereich und verfolgt gewerbliche Zwecke; § 40 Nr. 1 DesignG ist nicht erfüllt. "
                    "Herstellen und Anbieten sind Benutzung (§ 38 Abs. 1 S. 2 DesignG)."],
                   abwandlung="P verkauft weitere Nachdrucke über eine Onlineplattform.",
                   merke="Wer verkauft, handelt nicht mehr privat.", titel="Verkauf der Nachdrucke", norms=["§ 38 Abs. 1 DesignG"]),
            ],
            abschnitt="§ 40 Nr. 1, 2 DesignG: Privatbereich und Versuch", level=1, concepts=["des_schranken"], norms=["§ 40 DesignG"],
            step=f"{VL}.5.1"),
        *fallkette("d02n40-3", "Die Nachbaufelge",
            "Autohersteller A hat Designs für Leichtmetallfelgen eingetragen. Händler Z verkauft gleich aussehende Nachbaufelgen und weist auf der "
            "Felge und im Shop deutlich darauf hin, dass sie nicht von A stammen und nur zur Reparatur bestimmt sind.",
            [frage("Kann sich Z bei einem 2019 angemeldeten Felgendesign auf § 40a DesignG berufen?", False,
                   ["**Nein!** § 40a DesignG gilt nicht für Rechte aus Designs, die vor dem **2. Dezember 2020** angemeldet wurden (§ 73 Abs. 2 "
                    "DesignG). Für solche Designs bleibt es beim vollen Schutz."],
                   merke="Reparaturklausel nur für Anmeldungen ab 2.12.2020.", titel="Übergangsrecht", level=2, norms=["§ 73 DesignG"]),
             frage("Kann eine Felge, deren Form das Auto nicht vorgibt, unter die Reparaturklausel fallen?", True,
                   ["**Ja!** Eine Formgebundenheit verlangt der Wortlaut des § 40a Abs. 1 DesignG nicht; er erfasst Bauelemente komplexer Erzeugnisse, "
                    "die allein zur Reparatur verwendet werden, um das ursprüngliche Erscheinungsbild wiederherzustellen. Zur ähnlich gefassten früheren "
                    "Unionsregel hat der EuGH auch Felgen erfasst (EuGH Acacia)."],
                   abwandlung="Das Felgendesign wurde 2022 angemeldet.",
                   merke="§ 40a DesignG: keine Formgebundenheit im Wortlaut.", titel="Formungebundenes Teil", level=3,
                   cases=["des_eugh_acacia_audi"]),
             frage("Darf Z die Felgen auch für die Umrüstung unbeschädigter Autos bewerben?", False,
                   ["**Nein!** Die Klausel erfasst nur Bauelemente, die **allein** zur Reparatur verwendet werden; ist der vorrangige Zweck, zu dem das "
                    "Bauelement auf den Markt gebracht wird, ein anderer, gilt sie nicht (§ 40a Abs. 1 S. 2 DesignG). Tuning ist keine Reparatur."],
                   merke="Reparatur ja, Umrüstung nein.", titel="Zweckbindung", level=2),
             frage("Hilft Z die Reparaturklausel?", False,
                   ["**Nein!** Seit dem 1. Mai 2025 gilt Art. 20a GGV. Er erfasst nur Bauelemente, von deren Erscheinungsform das Design des Bauelements "
                    "**abhängt** (formgebundene Teile). Für Felgen, deren Gestalt das Fahrzeug nicht vorgibt, greift die Klausel danach nicht "
                    "(BGH Schlüsselgehäuse)."],
                   abwandlung="A stützt sich stattdessen auf ein Unionsgeschmacksmuster an der Felge; Z verkauft im Jahr 2026.",
                   merke="Art. 20a GGV: nur formgebundene Teile.", titel="Unionsgeschmacksmuster seit 2025", level=3,
                   norms=["Art. 20a GGV"], cases=["des_bgh_schluesselgehaeuse"]),
            ],
            abschnitt="§ 40a DesignG: Reparaturklausel", level=2, concepts=["des_reparaturklausel", "des_bauelement_sichtbarkeit"],
            norms=["§ 40a DesignG"], cases=["des_bgh_kraftfahrzeugfelgen_ii"], step=f"{VL}.5.2"),
    ]),
    # ================================================================== § 42 DesignG
    dict(id="d02n42", titel="§ 42 DesignG: Unterlassung, Beseitigung, Schadensersatz", einheiten=[
        schema("d02n42-0", "Prüfungsschema Designverletzung", "des_schema_designverletzung",
               "§ 42 DesignG ist die Anspruchsgrundlage der Verletzungsklage: Wer entgegen § 38 Abs. 1 S. 1 DesignG ein eingetragenes Design benutzt, "
               "haftet auf **Beseitigung** und bei Wiederholungsgefahr auf **Unterlassung**; droht die Zuwiderhandlung erstmals, genügt "
               "Erstbegehungsgefahr (Abs. 1). Bei Vorsatz oder Fahrlässigkeit schuldet er **Schadensersatz**, berechnet nach dem konkreten Schaden, "
               "dem Verletzergewinn oder einer angemessenen Lizenzgebühr (Abs. 2). Prüfung: Aktivlegitimation (Inhaber, Lizenznehmer nach "
               "§ 31 DesignG), Bestand und Schutzgegenstand, Benutzungshandlung, Schutzumfang, Schranken, Rechtsfolgen. Passivlegitimiert ist jeder "
               "Verletzer; für Arbeitnehmer und Beauftragte haftet der Unternehmensinhaber, außer auf Schadensersatz (§ 44 DesignG).",
               abschnitt="Überblick"),
        *fallkette("d02n42-1", "Kinderwagen aus Fernost",
            "K hat ein eingetragenes Design für einen Kinderwagen. Das Unternehmen W lässt einen nachgebildeten Wagen in China herstellen und bietet "
            "ihn in Deutschland an. K klagt auf Unterlassung, auch des Herstellens.",
            [frage("Begründet das Angebot in Deutschland Wiederholungsgefahr?", True,
                   ["**Ja!** Das Anbieten ist Benutzung (§ 38 Abs. 1 S. 2 DesignG). Eine begangene Verletzung begründet die tatsächliche Vermutung der "
                    "**Wiederholungsgefahr** (§ 42 Abs. 1 S. 1 DesignG)."],
                   merke="Begangene Verletzung: Wiederholungsgefahr wird vermutet.", titel="Wiederholungsgefahr"),
             frage("Kann K auch das Herstellen verbieten lassen, obwohl W bisher nur in China fertigen lässt?", True,
                   ["**Ja!** Für noch nicht begangene Handlungen genügt **Erstbegehungsgefahr** (§ 42 Abs. 1 S. 2 DesignG). Lässt ein produzierendes "
                    "Unternehmen außerhalb der Union herstellen und vertreibt es in der Union, besteht Begehungsgefahr auch für das Herstellen (zum "
                    "Unionsgeschmacksmuster BGH Kinderwagen I)."],
                   merke="Erstbegehungsgefahr trägt den vorbeugenden Unterlassungsanspruch.", titel="Erstbegehungsgefahr", level=2),
             frage("Entfällt die Wiederholungsgefahr, wenn W den Vertrieb einstellt und verspricht, es nicht wieder zu tun?", False,
                   ["**Nein!** Weder die Einstellung des Vertriebs noch ein einfaches Versprechen beseitigt die Wiederholungsgefahr. Nötig ist "
                    "grundsätzlich eine ernsthafte Unterlassungserklärung, die durch ein angemessenes **Vertragsstrafeversprechen** gesichert ist."],
                   merke="Nur die strafbewehrte Unterlassungserklärung beseitigt die Wiederholungsgefahr.", titel="Wegfall der Wiederholungsgefahr"),
            ],
            abschnitt="Abs. 1: Unterlassung und Begehungsgefahr", level=1, concepts=["des_unterlassung"], norms=["§ 42 Abs. 1 DesignG"],
            cases=["des_bgh_kinderwagen_i"], step=f"{VL}.6.1"),
        *fallkette("d02n42-2", "Der Versandhauskatalog",
            "Uhrenherstellerin U hat ein Design für eine Damenuhr eingetragen, die sie für 1.000 € und mehr verkauft. Versandhaus V bietet in seinem "
            "Katalog eine Nachbildung für 20 € an, die es von einem Großhändler bezogen hat, und verkauft 164 Stück. V kannte das Design nicht.",
            [frage("Handelt V schuldhaft, obwohl es das Design nicht kannte?", True,
                   ["**Ja!** Schadensersatz setzt Vorsatz oder Fahrlässigkeit voraus (§ 42 Abs. 2 S. 1 DesignG). An die Sorgfalt gewerblicher Anbieter "
                    "werden strenge Anforderungen gestellt: Wer Erzeugnisse vertreibt, muss sich über bestehende Schutzrechte vergewissern; "
                    "Unkenntnis entlastet in der Regel nicht."],
                   merke="Gewerblicher Händler: Prüfpflicht, Unkenntnis ist meist Fahrlässigkeit.", titel="Verschulden", step=f"{VL}.6.2"),
             frage("Wie kann U ihren Schaden berechnen?", 1,
                   ["**Nach einer von drei Berechnungsarten.** Neben dem konkreten Schaden einschließlich entgangenen Gewinns kann U den "
                    "Verletzergewinn (§ 42 Abs. 2 S. 2 DesignG) oder eine angemessene Lizenzgebühr (§ 42 Abs. 2 S. 3 DesignG) zugrunde legen. Die "
                    "Arten dürfen nicht addiert werden; die Lizenzanalogie setzt nicht voraus, dass U tatsächlich Lizenzen vergibt."],
                   optionen=["Nur als konkreten Schaden", "Konkreter Schaden, Verletzergewinn oder angemessene Lizenzgebühr nach ihrer Wahl",
                             "Nur als Lizenzgebühr, weil U selbst keine Lizenzen vergibt", "Verletzergewinn und Lizenzgebühr nebeneinander"],
                   merke="Drei Berechnungsarten, wahlweise, nicht kumulativ.", titel="Berechnungsarten"),
             frage("Kann U schon für das Anbieten im Katalog Schadensersatz nach der Lizenzanalogie verlangen?", True,
                   ["**Ja!** Der Inhaber kann bereits für das **Anbieten** eines rechtsverletzenden Gegenstands Schadensersatz nach der Lizenzanalogie "
                    "verlangen (BGH Catwalk). Maßstab ist, was vernünftige Parteien als Vergütung vereinbart hätten (§ 42 Abs. 2 S. 3 DesignG); das "
                    "Gericht schätzt sie nach § 287 ZPO."],
                   merke="Lizenzanalogie schon für das Angebot.", titel="Lizenzanalogie", level=2),
             frage("Darf V vom herauszugebenden Gewinn anteilige Gemeinkosten seines Versandhauses abziehen?", False,
                   ["**Nein!** Bei der Herausgabe des Verletzergewinns (§ 42 Abs. 2 S. 2 DesignG) dürfen Gemeinkosten nur abgezogen werden, soweit sie "
                    "den verletzenden Gegenständen **unmittelbar zugerechnet** werden können (BGH Gemeinkostenanteil). Allgemeine Kosten des "
                    "Versandhauses wären auch ohne die Uhr angefallen."],
                   merke="Verletzergewinn: keine pauschalen Gemeinkosten.", titel="Gemeinkosten", level=3, cases=["des_bgh_gemeinkostenanteil"]),
             frage("Ist der Schadensersatz auf die Zeit ab der ersten nachgewiesenen Verletzungshandlung begrenzt?", False,
                   ["**Nein!** Der Schadensersatzanspruch und die Auskunft zu seiner Bezifferung sind zeitlich nicht durch die erste nachgewiesene "
                    "Verletzungshandlung begrenzt (BGH Windsor Estate, zum Markenrecht). U kann Auskunft auch über frühere Verkäufe verlangen."],
                   merke="Keine Begrenzung auf die erste nachgewiesene Verletzung.", titel="Zeitliche Reichweite", level=2,
                   cases=["des_bgh_windsor_estate"]),
            ],
            abschnitt="Abs. 2: Verschulden und Schadensberechnung", level=2, concepts=["des_schadensersatz"], norms=["§ 42 Abs. 2 DesignG"],
            step=f"{VL}.6.2"),
        *fallkette("d02n42-3", "Die Lizenznehmerin klagt",
            "Die G GmbH hat vom Inhaber eines Designs für einen Gartenstuhl eine einfache Lizenz erhalten, die nicht im Register steht. Ein Discounter "
            "verkauft Nachbildungen. G will selbst klagen; der Inhaber reagiert nicht.",
            [frage("Kann G als einfache Lizenznehmerin ohne Zustimmung des Inhabers aus dem eingetragenen Design klagen?", False,
                   ["**Nein!** Der Lizenznehmer kann ein Verletzungsverfahren nur mit **Zustimmung** des Rechtsinhabers anhängig machen (§ 31 Abs. 3 "
                    "S. 1 DesignG). Ohne Zustimmung darf nur der ausschließliche Lizenznehmer klagen, wenn der Inhaber auf Aufforderung binnen "
                    "angemessener Frist nicht selbst klagt (§ 31 Abs. 3 S. 2 DesignG)."],
                   merke="Einfache Lizenz: Klage nur mit Zustimmung.", titel="Klagebefugnis des Lizenznehmers", norms=["§ 31 DesignG"],
                   step=f"{VL}.1"),
             frage("Schadet es G, dass ihre Lizenz nicht im Register eingetragen ist?", False,
                   ["**Nein!** Der Lizenznehmer kann Ansprüche wegen Verletzung eines eingetragenen Unionsgeschmacksmusters geltend machen, auch wenn "
                    "die Lizenz nicht eingetragen ist (Art. 33 Abs. 2 GGV; EuGH Thomas Philipps)."],
                   abwandlung="Der Stuhl ist als eingetragenes Unionsgeschmacksmuster geschützt; der Inhaber stimmt der Klage der G zu.",
                   merke="Registereintragung der Lizenz ist keine Klagevoraussetzung.", titel="Nicht eingetragene Lizenz", level=2,
                   norms=["Art. 33 GGV"], step=f"{UG}.2"),
             frage("Kann G in ihrem eigenen Verfahren Ersatz ihres eigenen Schadens verlangen?", True,
                   ["**Ja!** Der Lizenznehmer kann in einem Verletzungsverfahren, das er nach Art. 32 Abs. 3 GGV selbst anhängig macht, Ersatz seines "
                    "**eigenen** Schadens verlangen (EuGH Thomas Philipps). Im DesignG kann jeder Lizenznehmer der Klage des Inhabers beitreten, um "
                    "seinen Schaden geltend zu machen (§ 31 Abs. 4 DesignG)."],
                   merke="Lizenznehmer: eigener Schaden, eigene Klage oder Beitritt.", titel="Schaden des Lizenznehmers", level=2,
                   norms=["Art. 32 GGV", "§ 31 DesignG"], step=f"{UG}.2"),
            ],
            abschnitt="Aktivlegitimation: Inhaber und Lizenznehmer", level=2, concepts=["des_lizenz", "des_schadensersatz"],
            norms=["§ 42 DesignG"], cases=["des_eugh_thomas_philipps"]),
        *fallkette("d02n42-4", "Der Mitarbeiter im Onlineshop",
            "Im Onlineshop der Firma F stellt ein Mitarbeiter ohne Wissen der Geschäftsführung nachgemachte Vasen ein, die ein eingetragenes Design "
            "verletzen. Die Designinhaberin I verklagt die Inhaberin des Unternehmens.",
            [frage("Haftet die Unternehmensinhaberin auf Unterlassung, obwohl sie von nichts wusste?", True,
                   ["**Ja!** Wird in einem Unternehmen von einem Arbeitnehmer oder Beauftragten ein Design widerrechtlich verletzt, hat der Verletzte "
                    "die Ansprüche aus §§ 42 und 43 DesignG auch gegen den **Inhaber des Unternehmens** (§ 44 DesignG). Eigenes Verschulden ist dafür "
                    "nicht nötig."],
                   merke="§ 44 DesignG: Unternehmensinhaber haftet für seine Leute.", titel="Haftung des Unternehmensinhabers"),
             frage("Haftet sie nach § 44 DesignG auch auf Schadensersatz?", False,
                   ["**Nein!** § 44 DesignG nimmt den Anspruch auf Schadensersatz ausdrücklich aus. Dafür braucht es eigenes Verschulden der "
                    "Inhaberin oder eine Zurechnung nach allgemeinen Vorschriften."],
                   merke="§ 44 DesignG: alles außer Schadensersatz.", titel="Kein Schadensersatz über § 44 DesignG", level=2),
             frage("Ist der Mitarbeiter selbst Verletzer?", True,
                   ["**Ja!** Verletzer ist jeder, der entgegen § 38 Abs. 1 S. 1 DesignG das Design benutzt (§ 42 Abs. 1 S. 1 DesignG), also auch der "
                    "Mitarbeiter, der die Vasen anbietet. § 44 DesignG erweitert die Haftung, ersetzt sie aber nicht."],
                   merke="Wer selbst benutzt, ist selbst Verletzer.", titel="Haftung des Handelnden", level=2),
            ],
            abschnitt="Passivlegitimation: § 44 DesignG", level=1, concepts=["des_unterlassung", "des_schadensersatz"],
            norms=["§ 44 DesignG", "§ 42 DesignG"], step=f"{VL}.6"),
    ]),
    # ================================================================== §§ 43 bis 47 DesignG
    dict(id="d02n43", titel="§§ 43 bis 47 DesignG: Vernichtung, Rückruf, Auskunft, Besichtigung, Bekanntmachung", einheiten=[
        intro("d02n43-0", "Die Folgeansprüche",
              "Neben Unterlassung und Schadensersatz kennt das DesignG Folgeansprüche nach dem Muster der Durchsetzungsrichtlinie: **Vernichtung** "
              "rechtswidriger Erzeugnisse und der Herstellungsvorrichtungen, **Rückruf** und Entfernen aus den Vertriebswegen, wahlweise "
              "**Überlassung** gegen Vergütung (§ 43 DesignG), jeweils unter Verhältnismäßigkeitsvorbehalt. **Auskunft** über Herkunft und "
              "Vertriebsweg schuldet der Verletzer, bei offensichtlicher Verletzung oder erhobener Klage auch ein in gewerblichem Ausmaß beteiligter "
              "Dritter (§ 46 DesignG). Bei hinreichender Wahrscheinlichkeit einer Verletzung gibt es Vorlage und Besichtigung (§ 46a DesignG), zur "
              "Sicherung des Schadensersatzes Bankunterlagen (§ 46b DesignG). Die obsiegende Partei kann die **Urteilsbekanntmachung** erreichen "
              "(§ 47 DesignG). Den schuldlosen Verletzer schützt die Abfindung in Geld (§ 45 DesignG).",
              norms=["§ 43 DesignG", "§ 45 DesignG", "§ 46 DesignG", "§ 46a DesignG", "§ 46b DesignG", "§ 47 DesignG"],
              concepts=["des_vernichtung_rueckruf", "des_auskunft", "des_vorlage_besichtigung"], abschnitt="Überblick"),
        *fallkette("d02n43-1", "Leuchten im Lager",
            "Großhändler G hat 2.000 Nachbildungen einer als Design geschützten Leuchte importiert. 500 lagern bei ihm, 1.500 hat er an Möbelhäuser "
            "geliefert. Die Designinhaberin I hat ein Unterlassungsurteil erstritten und verlangt weitere Maßnahmen.",
            [frage("Kann I die Vernichtung der 500 Leuchten im Lager verlangen?", True,
                   ["**Ja!** Der Verletzte kann die Vernichtung der im Besitz oder Eigentum des Verletzers befindlichen rechtswidrig hergestellten "
                    "oder verbreiteten Erzeugnisse verlangen (§ 43 Abs. 1 S. 1 DesignG), es sei denn, sie ist im Einzelfall unverhältnismäßig "
                    "(§ 43 Abs. 4 DesignG)."],
                   merke="Vernichtung: Regelfall, Ausnahme nur bei Unverhältnismäßigkeit.", titel="Vernichtung"),
             frage("Was kann I statt der Vernichtung verlangen?", 0,
                   ["**Überlassung gegen Vergütung.** Statt der Vernichtung kann der Verletzte verlangen, dass ihm die Erzeugnisse, die im Eigentum des "
                    "Verletzers stehen, gegen eine angemessene Vergütung überlassen werden, die die Herstellungskosten nicht übersteigen darf "
                    "(§ 43 Abs. 3 DesignG)."],
                   optionen=["Überlassung der Leuchten in Gs Eigentum gegen eine Vergütung höchstens in Höhe der Herstellungskosten",
                             "Überlassung ohne jede Gegenleistung", "Zahlung des Ladenpreises der Originale je Leuchte", "Nichts; die Vernichtung ist zwingend"],
                   merke="Überlassung: höchstens Herstellungskosten.", titel="Überlassung", level=2),
             frage("Muss G auch die 1.500 gelieferten Leuchten aus dem Markt holen?", True,
                   ["**Ja!** § 43 Abs. 2 DesignG gibt einen Anspruch auf **Rückruf** der rechtswidrigen Erzeugnisse oder auf ihr endgültiges Entfernen "
                    "aus den Vertriebswegen. G muss die Möbelhäuser ernsthaft zur Rückgabe auffordern."],
                   merke="Rückruf erfasst bereits ausgelieferte Ware.", titel="Rückruf"),
             frage("Durfte G sich darauf beschränken, die Ware im eigenen Lager anzuhalten?", False,
                   ["**Nein!** Ein Unterlassungsgebot gegen einen fortdauernden Störungszustand verpflichtet auch zu möglichen und zumutbaren "
                    "Beseitigungshandlungen. Im Verfügungsverfahren muss der Schuldner nicht zurückrufen, seine Abnehmer aber auffordern, die Ware "
                    "vorläufig nicht weiterzuvertreiben (BGH Produkte zur Wundversorgung, zum Markenrecht)."],
                   abwandlung="I hatte zunächst nur eine einstweilige Verfügung auf Unterlassung erwirkt; G hielt die Ware an, unternahm gegenüber den "
                              "Möbelhäusern aber nichts.",
                   merke="Unterlassen heißt auch: Abnehmer zum Stillhalten auffordern.", titel="Unterlassung und Beseitigung", level=3,
                   cases=["des_bgh_wundversorgung"], norms=["§ 42 Abs. 1 DesignG"]),
            ],
            abschnitt="§ 43 DesignG: Vernichtung, Rückruf, Überlassung", level=1, concepts=["des_vernichtung_rueckruf"], norms=["§ 43 DesignG"],
            step=f"{VL}.6.3"),
        *fallkette("d02n43-2", "Wer hat geliefert?",
            "Händlerin H verkauft über eine Onlineplattform Taschen, die ein eingetragenes Design offensichtlich verletzen. Designinhaberin I will "
            "wissen, von wem H die Taschen bezieht und an wen sie weiterverkauft. Da H unter einem Pseudonym handelt, soll die Plattform Namen und "
            "Anschrift mitteilen.",
            [frage("Muss H Namen und Anschrift ihrer Lieferanten und gewerblichen Abnehmer nennen?", True,
                   ["**Ja!** Der Verletzer schuldet unverzüglich Auskunft über Herkunft und Vertriebsweg (§ 46 Abs. 1 DesignG), insbesondere Namen und "
                    "Anschriften der Hersteller, Lieferanten und gewerblichen Abnehmer sowie Mengen und Preise (§ 46 Abs. 3 DesignG)."],
                   merke="Drittauskunft vom Verletzer: Lieferkette, Mengen, Preise.", titel="Auskunft des Verletzers"),
             frage("Kann I auch von der Plattform Auskunft verlangen?", True,
                   ["**Ja!** Bei offensichtlicher Rechtsverletzung besteht der Anspruch auch gegen Dritte, die in gewerblichem Ausmaß für "
                    "rechtsverletzende Tätigkeiten genutzte **Dienstleistungen erbracht** haben (§ 46 Abs. 2 S. 1 Nr. 3 DesignG). Die Plattform "
                    "stellt der H die Verkaufsinfrastruktur."],
                   merke="Dienstleister haften auf Auskunft bei offensichtlicher Verletzung.", titel="Auskunft vom Dienstleister", level=2),
             frage("Muss dafür auch die Rechtsverletzung der H ein gewerbliches Ausmaß haben?", False,
                   ["**Nein!** Das gewerbliche Ausmaß bezieht sich auf die Tätigkeit des Dritten, nicht auf die Rechtsverletzung (BGH Alles kann besser "
                    "werden, zur wortgleichen Vorschrift des Urheberrechts)."],
                   merke="Gewerbliches Ausmaß: beim Dritten, nicht beim Verletzer.", titel="Gewerbliches Ausmaß", level=3,
                   cases=["des_bgh_alles_kann_besser_werden"]),
             frage("Kann I die Auskunft im Eilverfahren durchsetzen?", True,
                   ["**Ja!** In Fällen offensichtlicher Rechtsverletzung kann die Auskunftspflicht durch **einstweilige Verfügung** angeordnet werden "
                    "(§ 46 Abs. 7 DesignG)."],
                   merke="Offensichtliche Verletzung: Auskunft per einstweiliger Verfügung.", titel="Eilrechtsschutz", level=2),
            ],
            abschnitt="§ 46 DesignG: Auskunft", level=2, concepts=["des_auskunft"], norms=["§ 46 DesignG"], step=f"{VL}.6.4"),
        *fallkette("d02n43-3", "Die Besichtigung",
            "I vermutet, dass Hersteller H in seiner Fabrik Gehäuse nach ihrem eingetragenen Design produziert; ein früherer Mitarbeiter hat ihr "
            "Fotos aus der Halle gegeben. H verweigert jeden Einblick.",
            [frage("Kann I die Besichtigung der Produktion verlangen, obwohl die Verletzung noch nicht feststeht?", True,
                   ["**Ja!** Bei **hinreichender Wahrscheinlichkeit** einer Rechtsverletzung kann der Rechtsinhaber Vorlage einer Urkunde oder "
                    "Besichtigung einer Sache in der Verfügungsgewalt des vermeintlichen Verletzers verlangen, wenn das zur Begründung seiner Ansprüche "
                    "erforderlich ist (§ 46a Abs. 1 DesignG)."],
                   merke="Besichtigung schon bei hinreichender Wahrscheinlichkeit.", titel="Besichtigungsanspruch"),
             frage("Muss H die Besichtigung auch dann dulden, wenn sie im Einzelfall unverhältnismäßig ist?", False,
                   ["**Nein!** Der Anspruch ist ausgeschlossen, wenn die Inanspruchnahme im Einzelfall unverhältnismäßig ist (§ 46a Abs. 2 DesignG). "
                    "Vertrauliche Informationen schützt das Gericht durch geeignete Maßnahmen (§ 46a Abs. 1 S. 3 DesignG)."],
                   merke="Verhältnismäßigkeit und Geheimnisschutz begrenzen die Besichtigung.", titel="Grenzen", level=2),
             frage("Muss I dem H den durch die Besichtigung entstandenen Schaden ersetzen?", True,
                   ["**Ja!** Lag keine Verletzung vor und drohte keine, kann der vermeintliche Verletzer von demjenigen, der die Besichtigung begehrt "
                    "hat, Ersatz des dadurch entstandenen Schadens verlangen (§ 46a Abs. 5 DesignG)."],
                   abwandlung="Die Besichtigung ergibt, dass H ganz andere Gehäuse herstellt.",
                   merke="Fehlgeschlagene Besichtigung: Schadensersatz für den Besichtigten.", titel="Haftung des Antragstellers", level=2),
            ],
            abschnitt="§ 46a DesignG: Vorlage und Besichtigung", level=2, concepts=["des_vorlage_besichtigung"], norms=["§ 46a DesignG"],
            step=f"{VL}.6.4"),
        *fallkette("d02n43-4", "Die Urteilsbekanntmachung",
            "Designinhaberin I hat gegen den Verletzer V ein Urteil auf Auskunft und Feststellung der Schadensersatzpflicht erstritten; die "
            "Unterlassung hatte V schon vorher erklärt. I will das Urteil auf Kosten des V in einer Fachzeitschrift veröffentlichen. Die "
            "Verletzungen liegen fünf Jahre zurück.",
            [frage("Ist die Befugnis zur Urteilsbekanntmachung auf Unterlassungsurteile beschränkt?", False,
                   ["**Nein!** Die Befugnis kann der obsiegenden Partei auch bei Klagen auf Auskunft, Rechnungslegung und Feststellung der "
                    "Schadensersatzpflicht zugesprochen werden (BGH PIERRE CARDIN zu § 19c MarkenG, der § 47 DesignG entspricht)."],
                   merke="Bekanntmachung bei jeder Klage aus dem Gesetz möglich.", titel="Welche Urteile?", level=2),
             frage("Spielt der lange Zeitablauf für das berechtigte Interesse eine Rolle?", True,
                   ["**Ja!** Das berechtigte Interesse (§ 47 S. 1 DesignG) steht unter dem Vorbehalt der **Verhältnismäßigkeit**. Weil die Bekanntmachung "
                    "fortwirkende Störungen beseitigen soll, ist der Zeitablauf seit der Verletzung einzustellen, daneben etwa Marktverwirrung sowie Art "
                    "und Umfang der Verletzung (BGH PIERRE CARDIN)."],
                   merke="Je länger her, desto schwächer das Bekanntmachungsinteresse.", titel="Zeitablauf", level=2),
             frage("Was gilt, wenn I die Befugnis zugesprochen erhält?", 1,
                   ["**Drei Monate ab Rechtskraft.** Die Befugnis erlischt, wenn von ihr nicht binnen drei Monaten nach Eintritt der Rechtskraft "
                    "Gebrauch gemacht wird. Art und Umfang bestimmt das Urteil, die Kosten trägt die unterliegende Partei, und der Ausspruch ist nicht "
                    "vorläufig vollstreckbar (§ 47 DesignG)."],
                   optionen=["I kann sofort aufgrund vorläufiger Vollstreckbarkeit veröffentlichen", "I muss binnen drei Monaten nach Rechtskraft Gebrauch machen, sonst erlischt die Befugnis",
                             "I kann Art und Umfang der Bekanntmachung frei wählen", "I trägt die Kosten der Veröffentlichung selbst"],
                   merke="Bekanntmachung: nach Rechtskraft, binnen drei Monaten.", titel="Frist und Kosten"),
            ],
            abschnitt="§ 47 DesignG: Urteilsbekanntmachung", level=2, concepts=["des_schadensersatz"], norms=["§ 47 DesignG"],
            cases=["des_bgh_pierre_cardin"], step=f"{VL}.6.4"),
    ]),
    # ================================================================== Art. 11, 19, 89 GGV
    dict(id="d02nggv", titel="Art. 11, 19, 89 GGV: Das nicht eingetragene Unionsgeschmacksmuster", einheiten=[
        intro("d02nggv-0", "Schutz ohne Eintragung",
              "Neben dem eingetragenen Design steht das **Unionsgeschmacksmuster**. Es entsteht eingetragen beim EUIPO oder **ohne Eintragung** für "
              "drei Jahre ab dem Tag, an dem es der Öffentlichkeit innerhalb der Union erstmals so zugänglich gemacht wurde, dass die dort tätigen "
              "Fachkreise es kennen konnten (Art. 11 GGV). Das eingetragene Muster ist Sperrrecht; das nicht eingetragene schützt nur gegen "
              "**Nachahmung**, nicht gegen unabhängige Entwürfe (Art. 19 Abs. 4 GGV). Stellt ein Unionsgeschmacksmustergericht die Verletzung fest, "
              "verbietet es die Fortsetzung (Art. 89 Abs. 1 GGV); die Folgeansprüche richten sich nach nationalem Recht, in Deutschland über "
              "§ 62a DesignG nach den §§ 42 bis 47 DesignG. Wer Rechte aus dem nicht eingetragenen Muster geltend macht, muss dessen Entstehung "
              "beweisen und angeben, worin die Eigenart liegt (Art. 85 Abs. 2 GGV).",
              norms=["Art. 11 GGV", "Art. 19 GGV", "Art. 89 GGV", "Art. 85 GGV", "§ 62a DesignG"],
              concepts=["des_ggm_nicht_eingetragen", "des_ggm_anwendbares_recht"], abschnitt="Überblick"),
        *fallkette("d02nggv-1", "Die Gebäckpresse",
            "Herstellerin K ließ ihre elektrische Gebäckpresse 2001 in China als Geschmacksmuster anmelden; das chinesische Amt veröffentlichte es "
            "2002. Ab Juni 2002 lieferte K Pressen an ein britisches Unternehmen. Gegen eine ähnliche Presse, die ein deutscher Filialist ab 2003 "
            "anbietet, beruft sich K auf ein nicht eingetragenes Gemeinschaftsgeschmacksmuster.",
            [frage("Ist durch die Veröffentlichung in China ein nicht eingetragenes Gemeinschaftsgeschmacksmuster entstanden?", False,
                   ["**Nein!** Der Schutz entsteht nur, wenn das Muster der Öffentlichkeit **innerhalb der Union** erstmals zugänglich gemacht wird; eine "
                    "Veröffentlichung außerhalb genügt nicht, selbst wenn die Fachkreise in der Union sie kennen konnten (Art. 11 GGV; BGH Gebäckpresse)."],
                   merke="Entstehung nur durch Offenbarung in der Union.", titel="Offenbarung in China", level=2),
             frage("Entsteht der Schutz dann ohne Weiteres mit den Lieferungen nach Großbritannien?", False,
                   ["**Nein!** Die Lieferungen können den Schutz nur begründen, wenn das Muster zu diesem Zeitpunkt noch neu war und Eigenart hatte. Die "
                    "chinesische Veröffentlichung gehört zum Formenschatz, wenn die in der Union tätigen Fachkreise sie im normalen Geschäftsverlauf "
                    "kennen konnten (Art. 7 GGV; BGH Gebäckpresse). Das musste das Berufungsgericht noch klären."],
                   merke="Eigene Drittstaatsveröffentlichung kann später schaden.", titel="Spätere Offenbarung in der Union", level=3,
                   norms=["Art. 7 GGV"]),
             frage("Wie lange schützt ein nicht eingetragenes Unionsgeschmacksmuster?", 1,
                   ["**Drei Jahre** ab dem Tag, an dem das Muster der Öffentlichkeit in der Union erstmals zugänglich gemacht wurde (Art. 11 Abs. 1 "
                    "GGV). Eine Verlängerung gibt es nicht; längeren Schutz bietet nur die Eintragung."],
                   optionen=["Ein Jahr ab der Offenbarung", "Drei Jahre ab der ersten Offenbarung in der Union",
                             "Fünf Jahre, verlängerbar bis 25 Jahre", "25 Jahre ab dem Entwurf"],
                   merke="Nicht eingetragen: drei Jahre, nicht verlängerbar.", titel="Schutzdauer"),
            ],
            abschnitt="Art. 11 GGV: Entstehung", level=2, concepts=["des_ggm_nicht_eingetragen", "des_offenbarung"], norms=["Art. 11 GGV"],
            cases=["des_bgh_gebaeckpresse"], step=f"{UG}.1.2"),
        *fallkette("d02nggv-2", "Der Gartenpavillon (Gautzsch)",
            "M vertreibt einen Gartenpavillon, dessen Abbildungen sie an Händler in der Union verteilt hat; eingetragen ist er nicht. Großhändler G "
            "bietet einen sehr ähnlichen Pavillon eines Zulieferers an und behauptet, dieser habe ihn unabhängig entworfen. M klagt aus dem nicht "
            "eingetragenen Gemeinschaftsgeschmacksmuster.",
            [frage("Schützt das nicht eingetragene Muster auch gegen einen unabhängig entworfenen Pavillon?", False,
                   ["**Nein!** Der Inhaber kann Benutzungshandlungen nur verbieten, wenn sie das Ergebnis einer **Nachahmung** sind. Keine Nachahmung "
                    "ist die unabhängige Gestaltung eines Entwerfers, von dem berechtigterweise angenommen werden kann, dass er das Muster nicht kannte "
                    "(Art. 19 Abs. 4 GGV)."],
                   merke="Nicht eingetragen: nur Schutz gegen Nachahmung.", titel="Unabhängiger Entwurf"),
             frage("Muss M beweisen, dass der Pavillon des G nachgeahmt ist?", True,
                   ["**Ja!** Der Inhaber muss nachweisen, dass die angegriffene Benutzung das Ergebnis einer Nachahmung ist. Macht diese Beweislast den "
                    "Nachweis praktisch unmöglich oder übermäßig schwer, muss das Gericht die Beweiserleichterungen des nationalen Rechts ausschöpfen "
                    "(EuGH Gautzsch)."],
                   merke="Beweislast für Nachahmung beim Inhaber, mit nationalen Erleichterungen.", titel="Beweislast", level=2),
             frage("Nach welchem Recht richtet sich, ob Ms Unterlassungsanspruch verjährt oder verwirkt ist?", 1,
                   ["**Nach nationalem Recht.** Verjährung und Verwirkung, die einer Klage aus dem Unionsgeschmacksmuster entgegengehalten werden, "
                    "unterliegen dem nationalen Recht unter Beachtung von Äquivalenz und Effektivität (EuGH Gautzsch). In Deutschland gilt über "
                    "§ 62a DesignG die Verjährungsregel des § 49 DesignG."],
                   optionen=["Nach einer eigenen Verjährungsfrist der GGV", "Nach nationalem Recht, angewandt unter Beachtung von Äquivalenz und Effektivität",
                             "Nach dem Recht des Sitzstaats des EUIPO", "Unterlassungsansprüche aus der GGV verjähren nie"],
                   merke="Verjährung und Verwirkung: nationales Recht.", titel="Verjährung und Verwirkung", level=2,
                   norms=["§ 62a DesignG", "§ 49 DesignG"]),
            ],
            abschnitt="Art. 19 Abs. 4 GGV: Nachahmung", level=2, concepts=["des_ggm_nicht_eingetragen", "des_verjaehrung"],
            norms=["Art. 19 GGV"], cases=["des_eugh_gautzsch"], step=f"{UG}.3.3"),
        *fallkette("d02nggv-3", "Felgen aus Italien",
            "Autohersteller B hat ein Gemeinschaftsgeschmacksmuster an einer Felge. Die italienische A bietet Nachbauten auf einer Website an, die sich "
            "gezielt an Kunden in Deutschland richtet, und liefert dorthin. B klagt vor einem deutschen Gericht am Ort der Verletzung auf "
            "Unterlassung, Auskunft und Schadensersatz.",
            [frage("Ergibt sich der Unterlassungsanspruch unmittelbar aus der GGV?", True,
                   ["**Ja!** Stellt ein Unionsgeschmacksmustergericht fest, dass der Beklagte das Muster verletzt hat oder zu verletzen droht, verbietet "
                    "es ihm die Fortsetzung, sofern nicht besondere Gründe entgegenstehen (Art. 89 Abs. 1 GGV)."],
                   merke="Unterlassung: aus der Verordnung selbst.", titel="Unterlassung aus der GGV", step=f"{UG}.5.1"),
             frage("Nach welchem Recht richten sich Auskunft und Schadensersatz?", 1,
                   ["**Nach dem Recht des Staates, in dem die Verletzungshandlungen begangen wurden.** Ein nach Art. 82 Abs. 5 GGV angerufenes Gericht "
                    "prüft die Folgeanträge nach dem Recht dieses Staates, also seinem eigenen (EuGH Acacia/BMW; Art. 88 Abs. 2 GGV, Art. 8 Abs. 2 "
                    "Rom-II-VO). Deutsches Recht heißt: §§ 42 bis 47 DesignG über § 62a DesignG."],
                   optionen=["Stets nach italienischem Recht, weil A dort sitzt", "Nach dem Recht des Staates der Verletzungshandlungen, hier deutschem Recht",
                             "Nach spanischem Recht als Sitzstaat des EUIPO", "Unmittelbar und abschließend nach der GGV"],
                   merke="Folgeansprüche: Recht des Handlungsorts.", titel="Anwendbares Recht", level=3, step=f"{UG}.5.2",
                   cases=["des_eugh_acacia_bmw"]),
             frage("Kann das Gericht A den Vertrieb in der ganzen Union verbieten?", False,
                   ["**Nein!** Ein nach Art. 82 Abs. 5 GGV zuständiges Gericht entscheidet nur über Verletzungshandlungen in dem Mitgliedstaat, in dem "
                    "es seinen Sitz hat (Art. 83 Abs. 2 GGV). Ein unionsweites Verbot gibt es am Wohnsitz oder Sitz des Beklagten (Art. 82 Abs. 1, "
                    "Art. 83 Abs. 1 GGV)."],
                   merke="Gerichtsstand der Verletzung: nur nationale Reichweite.", titel="Reichweite des Verbots", level=2,
                   norms=["Art. 82 GGV", "Art. 83 GGV"], step=f"{UG}.4"),
            ],
            abschnitt="Art. 89 GGV: Sanktionen und anwendbares Recht", level=2, concepts=["des_ggm_anwendbares_recht", "des_ggm_gericht"],
            norms=["Art. 89 GGV", "Art. 88 GGV"], cases=["des_eugh_acacia_bmw"]),
    ]),
]

KURS = dict(
    id="d02", gebiet="designg", kompakt=True,
    titel="DesignG nach Vorschriften",
    untertitel="§§ 1 bis 47 DesignG: jede Vorschrift mit den Fällen von BGH, BPatG und EuGH",
    farbe="#b0562b", icon="register",
    beschreibung="Ein Kapitel je Vorschrift, in der Reihenfolge des Gesetzes: Begriffe und Bauelemente (§§ 1, 4 DesignG), Neuheit und Eigenart "
                 "(§§ 2, 5, 6 DesignG), Ausschlüsse (§ 3 DesignG), Recht auf das Design (§§ 7 bis 10 DesignG), Nichtigkeit und Nichtigkeitsverfahren "
                 "(§§ 33, 34, 34a DesignG), Schutzgegenstand und Schutzumfang (§§ 37, 38 DesignG), Schranken und Reparaturklausel (§§ 40, 40a DesignG), "
                 "die Anspruchsgrundlage der Verletzungsklage (§ 42 DesignG) und die Folgeansprüche (§§ 43 bis 47 DesignG), dazu das Unionsgeschmacksmuster (Art. 11, 19, 89 GGV). Jeder Fall "
                 "ist ein kurzer Sachverhalt nach einer Entscheidung von BGH, BPatG oder EuGH mit mehreren Fragen, Prüfungspunkt für Prüfungspunkt.",
    kapitel=KAPITEL,
)
