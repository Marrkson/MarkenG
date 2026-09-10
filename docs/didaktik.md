# Didaktisches Konzept von IPelico

IPelico ist der Fallkurs zum Markenrecht. Die Falldidaktik folgt dem Vorbild von Jurafuchs (öffentliche
Beschreibungen und Nutzung der App); die Umsetzung ist eigenständig. Fünf Prinzipien tragen das Format:

| Prinzip | Vorbild | Umsetzung in IPelico |
|---|---|---|
| **Atomisierung** | Der Stoff wird in die kleinsten sinnvollen Einheiten zerlegt. Eine Einheit behandelt genau ein Rechtsproblem, meist einen Prüfungspunkt. | Jede Einheit ist an einen Prüfungspunkt des Wissensgraphen gekoppelt (`step`-Referenz), z.B. „markenmäßige Benutzung“ oder „Bekanntheit zum Prioritätstag“. |
| **Falldidaktik** | Rechtswissen wird ausschließlich über konkrete Lebenssachverhalte vermittelt, wenige Sätze lang, mit Namen und Alltagsbezug, häufig an echte BGH-Fälle angelehnt. | 88 Mini-Fälle, viele nach Leitentscheidungen (Opel-Blitz, ORTLIEB, Goldbären, Ritter Sport, Tork). Sachverhalt in eigener Box, dann die Frage. |
| **Aktives Abrufen mit sofortigem Feedback** | Ja/Nein- oder Auswahlfrage, direkte Rückmeldung „Richtig“ / „Falsch“, dann die ausführliche Lösung. Der Lernende committet sich, bevor er die Antwort sieht (Testing-Effekt). | Ja/Nein bei Fällen, Multiple Choice bei Wissensfragen; Feedbackbanner, Lösung im Gutachtenstil (Definition, Subsumtion, Ergebnis), Merksatz. |
| **Aufeinander aufbauende Einheiten** | Ein Kapitel beginnt mit einem Grundfall nahe am Normtext, führt das Prüfungsschema ein, steigert dann die Schwierigkeit (Basics, Fortgeschritten, Examen). | Jedes Kapitel startet mit Einführung oder Prüfungsschema, danach folgen die Fälle in Prüfungsreihenfolge; drei Schwierigkeitsstufen werden angezeigt. |
| **Gamification und Wiederholung** | Fortschrittsbalken pro Kurs, Streak, Punkte, Wiederholungsmodus für falsch beantwortete Aufgaben, Spaced Repetition. | Fortschritt pro Kurs und Kapitel, Streak, XP, Wiederholungsmodus mit wachsenden Intervallen (1, 3, 7, 14, 30, 60 Tage), alles per Cookie gespeichert. |

Weitere Merkmale, die übernommen wurden:

- **Sprache**: Du-Anrede, kurze Sätze, fett gesetzte Kernaussage, Normzitate in Klammern,
  typische Antwortsätze („Ja, in der Tat!“, „Nein!“).
- **Vernetzung**: Definitionen, Schemata und Entscheidungen sind aus jeder Lösung heraus
  aufrufbar, statt sie in getrennten Listen zu verstecken.
- **Kapitelabschluss** mit Ergebnis und Liste der Fehler, die direkt erneut geöffnet werden können.

Was bewusst anders ist: keine Illustrationen je Fall. IPelico setzt auf ein ruhiges, seriöses Design
(`DESIGN.md`): Glas-Oberflächen in Rhein-IP-Blau, Wissensboxen (Sachverhalt, Merke, Richtig, Falsch),
Kursnummern statt Farbkacheln, ein eigenes Icon-Set in der Sprache des Zeichens. Lückentexte und
Gruppierungsaufgaben wurden nicht nachgebaut.

## Kursaufbau

| Kurs | Kapitel | Einheiten |
|---|---|---|
| 1 Grundlagen des Markenrechts | Schutzgegenstände und Funktionen · Entstehung und Priorität | 11 |
| 2 Schutzfähigkeit und absolute Schutzhindernisse | [§ 3](https://www.gesetze-im-internet.de/markeng/__3.html) · Unterscheidungskraft · Freihaltebedürfnis, Bösgläubigkeit, Verkehrsdurchsetzung | 17 |
| 3 Markenverletzung I | Aufbau · Markenmäßige Benutzung · Doppelidentität und Keyword-Advertising | 15 |
| 4 Markenverletzung II: Verwechslungsgefahr | Faktoren und Wechselwirkung · Zeichenähnlichkeit · Arten | 14 |
| 5 Markenverletzung III: Bekanntheitsschutz | Bekanntheit und Verknüpfung · Vier Eingriffe · [§ 9 Abs. 1 Nr. 3](https://www.gesetze-im-internet.de/markeng/__9.html) | 12 |
| 6 Schranken | [§ 23](https://www.gesetze-im-internet.de/markeng/__23.html) · [§ 24](https://www.gesetze-im-internet.de/markeng/__24.html) · Verwirkung, Verjährung, [§ 22](https://www.gesetze-im-internet.de/markeng/__22.html) | 15 |
| 7 Benutzungszwang, Widerspruch, Löschung | [§ 26](https://www.gesetze-im-internet.de/markeng/__26.html) · §§ [49](https://www.gesetze-im-internet.de/markeng/__49.html)–[52](https://www.gesetze-im-internet.de/markeng/__52.html) · §§ [42](https://www.gesetze-im-internet.de/markeng/__42.html), [43](https://www.gesetze-im-internet.de/markeng/__43.html) | 13 |
| 8 Geschäftliche Bezeichnungen und Domains | Unternehmenskennzeichen · Werktitel | 8 |
| 9 Rechtsfolgen und Durchsetzung | Unterlassung und Schadensersatz · Täter, Teilnehmer, Störer | 7 |
| 10 Unionsmarke und IR-Marke | Unionsmarke · IR-Marke | 11 |
| 11 Die Markenrechtsrichtlinie (EU) 2015/2436 | Struktur, Harmonisierung, Auslegung · Materielles Recht: Art. 3 bis 18 · Verfahren und Umsetzung im MaMoG | 20 |
| 12 Die Durchsetzungsrichtlinie 2004/48/EG | Zwei Richtlinien, ein Muster in sieben Gesetzen · Aufklärung: Auskunft, Vorlage, Sicherung (Art. 6 bis 9) · Eilrechtsschutz, Sanktionen, Mittelspersonen, Kosten (Art. 9 bis 15) | 30 |
| 13 Klausurtraining NS | Widerspruch: Zulässigkeit, Frist, Gebühr · Beschwerde: Form, Frist, Gebühr, Wiedereinsetzung · Nichtbenutzungseinrede und Glaubhaftmachung · Verwechslungsgefahr in der Klausur · Unternehmenskennzeichen, Bösgläubigkeit, ältere Rechte · Verfall, Schutzentziehung, Herkunftsangaben | 56 |
| 14 Wirksamkeit und Zulässigkeit | Die drei Ebenen · Die vier Fähigkeiten · Wirksamkeit: Gebühren und Zahlungstag · Zulässigkeit des Widerspruchs · Erinnerung, Beschwerde, Rechtsbeschwerde · Wiedereinsetzung und Weiterbehandlung · Klagen vor dem ordentlichen Gericht · Tenor formulieren | 59 |
| 15 Das Einheitliche Patentgericht: Aufbau, Rechtsquellen, Übergangszeit | Gericht, Kammern, Spruchkörper · Rechtsquellen und Vorrang des Unionsrechts · Übergangszeit, Opt-out, Altfälle und Verfahrensgrundsätze | 12 |
| 16 Zuständigkeit und Kammerwahl | Ob und wo: internationale, sachliche und Kammerzuständigkeit · Die Rüge: Einspruch nach R. 19 bis 21 VerfO | 12 |
| 17 Die Verletzungsklage: vom Schriftsatz zur Entscheidung | Klageschrift, Zustellung, Fristen · Sprache, Berichterstatter, Zwischenverfahren, mündliche Verhandlung · Änderung, Rücknahme, Streithilfe und rechtliches Gehör | 12 |
| 18 Verletzung und Auslegung vor dem EPG | Schutzbereich: Auslegung des Patentanspruchs · Benutzungshandlungen: unmittelbar, mittelbar, äquivalent · Einwendungen und Haftung: Art. 27 bis 29, 63 EPGÜ, FRAND | 12 |
| 19 Einstweilige Maßnahmen, Beweissicherung, Vertraulichkeit | Antrag auf einstweilige Maßnahmen (Art. 62 EPGÜ, R. 205 bis 213 VerfO) · Beweissicherung, Beweisvorlage und Ex-parte-Anordnungen · Vertraulichkeit und Akteneinsicht (Art. 58 EPGÜ, R. 262, 262A VerfO) | 12 |
| 20 Nichtigkeit, Widerklage und Änderung des Patents | Nichtigkeitsklage und Widerklage: Zulässigkeit und Verfahren · Nichtigkeitsgründe (Art. 65 Abs. 2 EPGÜ, Art. 138 EPÜ) · Verteidigung: Änderung des Patents und Erwiderung | 12 |
| 21 Rechtsfolgen, Zwangsgeld und Vollstreckung | Die Anordnungen nach Art. 63, 64, 67 und 80 EPGÜ · Schadensersatz (Art. 68 EPGÜ) und das Festsetzungsverfahren · Vollstreckung und Zwangsgeld (Art. 82 EPGÜ, R. 354 VerfO) | 13 |
| 22 Kosten, Gebühren und Prozesskostensicherheit | Gerichtsgebühren und Streitwert (R. 370 VerfO) · Kostengrundentscheidung und Kostenfestsetzung (Art. 69 EPGÜ, R. 150 bis 157 VerfO) · Prozesskostensicherheit (Art. 69 Abs. 4 EPGÜ, R. 158 VerfO) | 13 |
| 23 Berufung und Rechtsbehelfe | Statthaftigkeit und Frist (Art. 73 EPGÜ, R. 220 bis 224 VerfO) · Beschwer, Anschlussberufung, bedingte Berufung, Streithelfer · Aufschiebende Wirkung, neues Vorbringen, Entscheidung, Wiederaufnahme | 13 |
| 24 EPGÜ und Durchsetzungsrichtlinie: eine Richtlinie, drei Gesetze | Die Entsprechungen: Richtlinie, EPGÜ, PatG, MarkenG · Schadensersatz, Kosten und Veröffentlichung (Art. 68, 69, 80 EPGÜ ↔ Art. 13, 14, 15 RL) | 8 |


Stand September 2026: 24 Kurse, 74 Kapitel, 409 Einheiten: 261 Fälle (Ja/Nein), 81 Wissensfragen (Auswahl),
23 Prüfungsschemata, 14 Einführungen. Zu den Kursen 1 bis 10 kamen Kurs 11 (Markenrechtsrichtlinie), Kurs 12
(Klausurtraining NS nach den Klausuren der Patentanwaltsprüfung), Kurs 13 (Wirksamkeit und Zulässigkeit)
und Kurs 14 (Durchsetzungsrichtlinie).

## Speicherung des Fortschritts

Zwei Cookies (`mgk_p` Einheiten mit Ergebnis, Tag und Wiederholungszähler; `mgk_m` Streak,
Punkte, letzte Einheit, Hinweis bestätigt), Laufzeit ein Jahr, `SameSite=Lax`, keine
Übermittlung an einen Server. Wird die Seite als lokale Datei geöffnet, akzeptiert der Browser
keine Cookies; dann weicht die App automatisch auf `localStorage` aus und sagt das im Profil.

## Kurs 11: Die Markenrechtsrichtlinie (EU) 2015/2436

Der Kurs folgt demselben Format, behandelt aber die Ebene über dem MarkenG: Aufbau der Richtlinie, richtlinienkonforme Auslegung und Vorlage an den EuGH, dann die Artikel 3 bis 18 und die Verfahrensvorschriften mit ihren Umsetzungen im MaMoG 2019 (Transit, Vorbereitungshandlungen, Namensschranke, Schonfrist, Cooling-off, Amtsverfahren, Gewährleistungsmarke). Zusätzlich verweisen zehn bestehende Fälle der Kurse 1 bis 7 nun auf den jeweils zugrunde liegenden Richtlinienartikel.

## Nachschlagen: Lernkarten, Suche und Lernradar (Vorbild AMBOSS)

Neben der Falldidaktik (Vorbild Jurafuchs) übernimmt IPelico seit September 2026 drei Prinzipien der
Medizin-Plattform AMBOSS, die Lernen und Nachschlagen in einer Wissensbasis verbindet:

| Prinzip | Vorbild | Umsetzung in IPelico |
|---|---|---|
| **Suche über alles** | Eine Suche über Kapitel, Fragen und Begriffe mit gruppierten Treffern. | Such-Kugel in der Tableiste (Taste `/`). Treffer gruppiert nach Begriffen, Prüfungspunkten, Schemata, Gesetz, Richtlinien, Entscheidungen, Abgrenzungen und Fällen; zuletzt Gesuchtes und Stöbern-Kacheln, wenn das Feld leer ist. |
| **Lernkarten mit festem Schema** | Jedes Kapitel ist gleich gegliedert, damit man beim Nachschlagen sofort weiß, wo etwas steht; über 200.000 Verlinkungen mit Kurzdefinitionen. | Jeder Knoten des Wissensgraphen hat eine Lernkarte in fester Reihenfolge: Definition oder Kern, Norm, Prüfung, Rechtsprechung, Abgrenzung, Verwandtes, Fälle dazu. Chips öffnen Kurzkarten inline, jede Kurzkarte verlinkt zur Lernkarte, jede Lernkarte zu den Fällen. |
| **Lernradar** | Fakten, zu denen eine Frage falsch beantwortet wurde, bleiben in der Lernkarte rot unterstrichen, bis die Frage richtig beantwortet ist. | Falsch beantwortete Fälle markieren ihre Begriffe, Prüfungspunkte, Entscheidungen und Abgrenzungen rot in Chips, Schemata, Lernkarten, Suche und im Tab Wiederholen. Die Markierung verschwindet mit der nächsten richtigen Antwort; abschaltbar im Profil. |

Noch nicht übernommen: Relevanz-Markierung nach Klausurhäufigkeit, ein eigener Nachschlage-Modus ohne
Lernelemente und vorgefertigte Lernsitzungen.
