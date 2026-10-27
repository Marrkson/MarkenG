# -*- coding: utf-8 -*-
"""Weitere Leitentscheidungen für die überarbeiteten EPG-Kurse; Aktenzeichen und Datum werden gegen data/upc_decisions.json geprüft
(Helfer `ev`, URL aus dem Korpus). IDs mit Präfix `upc_`."""
from .cases import e, BG  # noqa: F401
from . import entscheidungen as _k


def ev(id, name, court, date, az, kern, norms=(), concepts=(), tags=()):
    rec = _k.by_docket(az, date)
    if rec is None:
        raise ValueError(f"Entscheidung {az} vom {date} ({name}) nicht im Korpus data/upc_decisions.json")
    return e(id, name, court, date, az, kern, norms=norms, concepts=concepts, tags=tags, url=rec["url"], patent=rec.get("patent", ""))


# Kurse u06 bis u10; `kern` fasst den Leitsatz der Entscheidung (Tabelle UpcDecision) in eigenen Worten zusammen.
CASES = [
    ev("upc_coa_belkin_philips_auskunft", "Belkin/Philips (Auskunftsfrist, Zwangsgeld trotz verspäteter Erfüllung)", BG, "2025-05-30", "APL_68523/2024",
       "Der Antrag auf Auskunft nach Art. 67 Abs. 1 EPGÜ soll eine Frist für die Auskunftserteilung enthalten, die ab der Mitteilung nach R. 118.8 VerfO (im Eilverfahren ab Zustellung der Anordnung) läuft; fehlt sie in der Entscheidung, setzt der Kläger sie mit der Mitteilung der Vollstreckungsabsicht. Weil das Zwangsgeld nicht nur Beuge-, sondern auch Strafcharakter hat, kann es auch verhängt werden, wenn der Beklagte die Auskunft inzwischen, aber verspätet erteilt hat. Die Erfüllung hat der Beklagte darzulegen und zu beweisen. Art. 67 Abs. 1 lit. b EPGÜ umfasst auch die vom Verletzer gezahlten Einkaufspreise; ist keine Form vorgeschrieben, darf die Auskunft schriftlich oder elektronisch erteilt werden.",
       norms=["Art. 67 Abs. 1 EPGÜ", "R. 118.8 VerfO", "R. 354 VerfO", "Art. 82 Abs. 4 EPGÜ"], concepts=["upc_auskunft", "upc_zwangsgeld", "upc_vollstreckung"],
       tags=["Auskunft", "Zwangsgeld", "Vollstreckung"]),
    ev("upc_coa_philips_belkin_aufschiebend", "Philips/Belkin (aufschiebende Wirkung, Geschäftsführer keine Mittelsperson)", BG, "2024-10-29", "App_53031/2024",
       "Der Antrag auf aufschiebende Wirkung muss nach R. 223.2 VerfO aus sich heraus verständlich sein, sodass der Gegner erwidern und das Berufungsgericht entscheiden kann; Verweise auf erstinstanzliche Schriftsätze sind nur mit konkret bezeichneten Textstellen zulässig. Aufschiebende Wirkung kommt in Betracht, wenn die angefochtene Entscheidung evident fehlerhaft ist, weil ihre tragenden Feststellungen oder Erwägungen schon bei summarischer Prüfung nicht halten. Ein Geschäftsführer vertritt das verletzende Unternehmen; dieses ist ihm gegenüber nicht „Dritter“ im Sinne von Art. 63 EPGÜ und Art. 11 DurchsetzungsRL, sodass er nicht allein wegen seiner Funktion als Mittelsperson haftet. Sicherheit nach R. 352.1 VerfO ist mit Erlass der Entscheidung anzuordnen.",
       norms=["Art. 74 Abs. 1 EPGÜ", "R. 223 VerfO", "Art. 63 Abs. 1 EPGÜ", "Art. 11 DurchsetzungsRL", "R. 352 VerfO"],
       concepts=["upc_aufschiebende_wirkung", "upc_verletzer", "upc_unterlassungsanordnung"], tags=["Berufung", "aufschiebende Wirkung", "Mittelsperson"]),
    ev("upc_coa_meril_edwards_obsiegende_partei", "Meril/Edwards (obsiegende Partei nach Unterlassungserklärung)", BG, "2024-10-04", "APL_83/2024",
       "Wer nach Abgabe einer Unterlassungs- und Verpflichtungserklärung durch den Beklagten obsiegende Partei im Sinne von Art. 69 Abs. 1 EPGÜ ist, bestimmt sich nach den Anträgen und dem Inhalt der Erklärung. Verpflichtet sich der Beklagte nach Einleitung des Verfahrens, den Anträgen des Klägers nachzukommen, sind Zulässigkeit und Begründetheit im Zeitpunkt der Erklärung in der Regel nicht zu prüfen; die Erklärung zeigt, dass die Anträge erfüllt wurden, und der Kläger ist in der Regel obsiegende Partei.",
       norms=["Art. 69 Abs. 1 EPGÜ", "R. 360 VerfO"], concepts=["upc_kostenerstattung", "upc_einstweilige_massnahmen"], tags=["Kosten", "Erledigung"]),
    ev("upc_coa_meril_edwards_rechtsargument", "Meril/Edwards (neue Rechtsargumente, Aussetzung bei EPA-Einspruch)", BG, "2024-11-21", "APL_50205/2024",
       "R. 222.2 VerfO erfasst nur Anträge, Tatsachen und Beweismittel, nicht rechtliche Ausführungen; ein neues Rechtsargument auf Grundlage der erstinstanzlichen Tatsachen und Beweise ist in der Berufung zulässig. Art. 33 Abs. 10 EPGÜ ist in R. 295 lit. a VerfO (vor Entscheidungsreife) und R. 295 lit. g VerfO i.V.m. R. 118 VerfO umgesetzt. Für die Aussetzung genügt, dass die Einspruchsabteilung rasch entscheiden wird, auch wenn wahrscheinlich Beschwerde folgt; eine rasche rechtskräftige Entscheidung des EPA ist nicht erforderlich. Die Aussetzung soll Widersprüche zwischen Verletzungsentscheidung und Widerruf im Einspruch vermeiden.",
       norms=["R. 222 VerfO", "Art. 33 Abs. 10 EPGÜ", "R. 295 VerfO", "R. 118 VerfO"], concepts=["upc_neues_vorbringen_berufung", "upc_aussetzung"],
       tags=["Berufung", "neues Vorbringen", "Aussetzung"]),
    ev("upc_coa_icpillar_arm_neues_vorbringen", "ICPillar/Arm (R. 222.2 VerfO von Amts wegen)", BG, "2024-09-16", "APL_33746/2024",
       "Das Berufungsgericht prüft von Amts wegen, wie es sein Ermessen nach R. 222.2 VerfO ausübt; es kann verspätete Anträge, Tatsachen und Beweismittel auch dann außer Acht lassen, wenn die Gegenseite nicht widerspricht. Aus R. 172.1 VerfO folgt die Pflicht, verfügbare Beweismittel vorzulegen; Beweisanordnungen nach R. 172.2 VerfO stehen im Ermessen des Gerichts. Die Bürgschaft einer in den USA zugelassenen Bank ist keine angemessene Sicherheit nach R. 158 VerfO.",
       norms=["R. 222 VerfO", "R. 172 VerfO", "R. 158 VerfO"], concepts=["upc_neues_vorbringen_berufung", "upc_beweismittel_beweislast", "upc_prozesskostensicherheit"],
       tags=["Berufung", "neues Vorbringen"]),
    ev("upc_coa_hurom_nuc_auskunft", "Hurom/NUC (Auskunft und aufschiebende Wirkung)", BG, "2025-06-06", "App_23407/2025",
       "Art. 67 EPGÜ spiegelt Art. 8 DurchsetzungsRL, der ein hohes Schutzniveau und genaue Informationen über Herkunft, Vertriebswege und beteiligte Dritte sichern soll. Die Auskunft gehört daher zu den Maßnahmen, deren Vollstreckung nur unter außergewöhnlichen Umständen nach R. 223 VerfO ausgesetzt werden kann. Dass die Auskunft vor der Berufungsentscheidung den Zweck der Berufung teilweise unterläuft, genügt nicht, solange der Berufungskläger nicht zeigt, dass die Berufung ohne aufschiebende Wirkung gegenstandslos würde und sein Geheimhaltungsinteresse das Interesse des Klägers an sofortiger Information überwiegt.",
       norms=["Art. 67 EPGÜ", "Art. 8 DurchsetzungsRL", "R. 223 VerfO", "Art. 74 Abs. 1 EPGÜ"], concepts=["upc_auskunft", "upc_aufschiebende_wirkung", "upc_durchsetzungsrl_bezug"],
       tags=["Auskunft", "aufschiebende Wirkung", "Durchsetzungsrichtlinie"]),
    ev("upc_coa_bruker_10x_buecher", "Bruker/10x Genomics (Offenlegung der Bücher, Gebühren)", BG, "2025-10-01", "UPC_CoA_681/2025",
       "Der Antrag auf Offenlegung der Bücher ist Teil des Verfahrens zur Festsetzung von Schadensersatz und Entschädigung (R. 131.1 lit. c, R. 141 bis 144 VerfO). Wer ihn stellt, schuldet die Festgebühr und die streitwertabhängige Gebühr für die Festsetzung des Schadensersatzes.",
       norms=["R. 131 VerfO", "R. 141 VerfO", "R. 370 VerfO"], concepts=["upc_schadensersatz", "upc_gerichtsgebuehren"], tags=["Schadensersatz", "Gebühren"]),
    ev("upc_coa_hanshow_ses_kostenfrist", "Hanshow/SES-imagotag (Frist für die Kostenfestsetzung)", BG, "2025-06-06", "APL_57918/2024",
       "Die Monatsfrist für den Antrag auf Kostenfestsetzung nach R. 151 VerfO beginnt mit Zustellung der Sachentscheidung, nicht einer Anordnung über einstweilige Maßnahmen. Wird kein Hauptsacheverfahren eingeleitet, etwa weil der Eilantrag erfolglos war, und ist der Antragsteller zur Kostentragung verurteilt, gelten R. 150 und 151 VerfO entsprechend; die Frist läuft dann ab Zustellung der Eilanordnung. Eine versäumte Frist kann nur durch Wiedereinsetzung (R. 320 VerfO) geheilt werden. Die eigenen Kosten des Kostenfestsetzungsverfahrens trägt jede Partei selbst, mit Ausnahme der Gerichtsgebühr.",
       norms=["R. 150 VerfO", "R. 151 VerfO", "R. 320 VerfO"], concepts=["upc_kostenerstattung", "upc_fristen"], tags=["Kosten", "Fristen"]),
    ev("upc_coa_hybridgenerator_infotech_zwangsgeld", "Hybridgenerator/Infotech (Zwangsgeld durch den Spruchkörper)", BG, "2025-06-04", "APL_13146/2025",
       "Über einen Antrag auf Festsetzung von Zwangsgeld nach R. 354.4 VerfO entscheidet der Spruchkörper, nicht ein Einzelrichter.",
       norms=["R. 354 VerfO"], concepts=["upc_zwangsgeld", "upc_spruchkoerper"], tags=["Zwangsgeld", "Vollstreckung"]),
]
