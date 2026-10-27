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


CASES = [
    ev("upc_coa_netgear_huawei_r333", "Netgear/Huawei (Überprüfung von Anordnungen des Berichterstatters)", BG, "2024-03-21", "APL_595643/2023",
       "Verfahrensleitende Entscheidungen des Berichterstatters oder des Vorsitzenden sind, soweit nichts anderes bestimmt ist, nicht unmittelbar mit der Berufung anfechtbar; statthaft ist der Antrag auf Überprüfung durch den Spruchkörper nach R. 333.1 VerfO, über dessen Zulässigkeit der Spruchkörper entscheidet. Die Mitteilung, der Einspruch werde im Hauptverfahren behandelt (R. 20.2 VerfO), ist eine solche verfahrensleitende Entscheidung. Weist der Berichterstatter den Einspruch zurück und lässt er die Berufung zu, kann die Partei wählen, ob sie Berufung einlegt oder die Überprüfung nach R. 333.1 VerfO beantragt; lässt er sie nicht zu, ist zunächst die Überprüfung durch den Spruchkörper zu beantragen.",
       norms=["R. 333 VerfO", "R. 20 VerfO", "R. 21 VerfO", "R. 220 VerfO"], concepts=["upc_berichterstatter", "upc_einspruch_r19", "upc_ermessensueberpruefung"],
       tags=["Einspruch", "Berichterstatter"]),
    ev("upc_coa_huawei_quinn_akteneinsicht_r333", "Huawei/Quinn Emanuel (Akteneinsicht: Überprüfung nach R. 333 VerfO)", BG, "2026-06-29", "UPC-COA-52/2026",
       "Entscheidungen des Berichterstatters über die Akteneinsicht Dritter nach R. 262.1(b) VerfO können nach R. 333 VerfO vom Spruchkörper überprüft werden; gegen dessen Entscheidung ist die Berufung nach R. 220.2 und 220.3 VerfO gegeben. Die Entscheidung des Berichterstatters ist weder Endentscheidung (R. 220.1(a) VerfO) noch eine das Verfahren nur für eine Partei beendende Entscheidung (R. 220.1(b) VerfO); die abweichende Auffassung der Lokalkammer München ist überholt.",
       norms=["R. 333 VerfO", "R. 262.1 VerfO", "R. 220 VerfO"], concepts=["upc_berichterstatter", "upc_akteneinsicht", "upc_ermessensueberpruefung"],
       tags=["Fallmanagement", "Akteneinsicht"]),
    ev("upc_coa_avago_tesla_ruecknahme", "Avago/Tesla (Klagerücknahme im Berufungsverfahren)", BG, "2025-01-15", "App_66724/2024",
       "Ein Antrag auf Rücknahme der Klage nach R. 265 VerfO kann auch im Berufungsverfahren gestellt werden; erst nach Rechtskraft der Endentscheidung ist er unzulässig. Über die Rücknahme entscheidet dann das Berufungsgericht. Die Rücknahme der Nichtigkeitswiderklage macht die Anträge auf Änderung des Patents gegenstandslos.",
       norms=["R. 265 VerfO", "R. 370 VerfO"], concepts=["upc_ruecknahme", "upc_aenderung_patent", "upc_gerichtsgebuehren"],
       tags=["Rücknahme", "Berufung"]),
    ev("upc_coa_supponor_aim_klageaenderung", "Supponor/AIM Sport (Klageänderung und Parteierweiterung)", BG, "2025-04-11", "APL_9191/2025",
       "Bei R. 263 und R. 305 VerfO hat das Gericht erster Instanz Ermessen; das Berufungsgericht prüft nur, ob es dessen Grenzen überschritten hat. Der Antrag nach R. 263 VerfO muss selbst begründen, weshalb die Änderung nicht im ursprünglichen Schriftsatz stand; der genaue Wortlaut darf in Anlagen stehen, etwa einer geänderten Klageschrift mit und ohne Änderungsmarkierungen. Beim Hinzufügen einer Partei (R. 305 VerfO) zählen u.a. frühere Kenntnis des Klägers, Beteiligung der übrigen Parteien, Auswirkungen auf sie und der Verfahrensstand.",
       norms=["R. 263 VerfO", "R. 305 VerfO"], concepts=["upc_klageaenderung", "upc_front_loaded"],
       tags=["Klageänderung"]),
    ev("upc_coa_sharkninja_seb_frist", "SharkNinja/SEB (Signatur, rückwirkende Fristverlängerung, Vertraulichkeit)", BG, "2026-05-22", "UPC-CoA-61/2026",
       "Der Schriftsatz selbst muss elektronisch signiert sein (R. 4.1 VerfO); die Bestätigung des Uploads im CMS genügt nicht. R. 9.3 lit. a VerfO erlaubt ausdrücklich die rückwirkende Fristverlängerung, auch auf einen erst nach Fristablauf gestellten Antrag. Von Dritten gegen Entgelt bezogene Marktdaten können vertrauliche Informationen im Sinne von Art. 58 EPGÜ, R. 262A VerfO sein.",
       norms=["R. 4 VerfO", "R. 9.3 VerfO", "R. 262A VerfO", "Art. 58 EPGÜ"], concepts=["upc_fristen", "upc_vertraulichkeit"],
       tags=["Fristen", "Vertraulichkeit"]),
]
