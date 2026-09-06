# Didaktische Analyse: Jurafuchs-Format und Übertragung auf das MarkenG

## Wie Jurafuchs Kapitel aufbereitet

Die Analyse stützt sich auf die öffentlichen Beschreibungen von Jurafuchs (Website, FAQ,
Interviews mit den Gründern bei iurratio, Erfahrungsberichte aus der Lehre) und auf die
Nutzung der App selbst. Fünf Prinzipien tragen das Format:

| Prinzip | Was Jurafuchs macht | Übertragung im Markenrecht Fallkurs |
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

Was bewusst anders ist: Jurafuchs nutzt Illustrationen für jeden Fall; hier stehen stattdessen
Kursfarben und Icons. Lückentexte und Gruppierungsaufgaben wurden nicht nachgebaut.

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

Insgesamt 125 Einheiten: 88 Fälle (Ja/Nein), 20 Wissensfragen (Auswahl), 14 Prüfungsschemata,
3 Einführungen.

## Speicherung des Fortschritts

Zwei Cookies (`mgk_p` Einheiten mit Ergebnis, Tag und Wiederholungszähler; `mgk_m` Streak,
Punkte, letzte Einheit, Hinweis bestätigt), Laufzeit ein Jahr, `SameSite=Lax`, keine
Übermittlung an einen Server. Wird die Seite als lokale Datei geöffnet, akzeptiert der Browser
keine Cookies; dann weicht die App automatisch auf `localStorage` aus und sagt das im Profil.
