# Gemeinsame Website-Regeln

Gilt für alle Northdocks-Domains, solange die Site-Datei nichts Engeres festlegt.

## Rechtsträger (Impressum / Footer)

| Feld | Wert |
|---|---|
| Firma | Northdocks GmbH |
| Sitz | Niederstraße 18, 40789 Monheim am Rhein |
| Register | HRB 76844, Amtsgericht Düsseldorf |
| USt-IdNr. | DE298519758 |
| Geschäftsführer | Joachim Perschbacher, Patrick D. Reschke |
| Telefon | +49 (0) 2173 9996713 |
| Mail (kanonisch) | **kontakt@northdocks.com** |

Kiel, Schauenburgerstraße 116, nur wo der Standort inhaltlich vorkommt (nicht als Rechtssitz).

Marken (FirefighterVR, MeditrainVR, …) sind Marken der GmbH. Footer: „powered by Northdocks“ / „a brand of Northdocks GmbH“, Vertragspartnerin immer die GmbH.

## Was auf Websites darf

Nur Claims der Stufe **öffentlich** in [claims.md](../claims.md). Beispiele die **nicht** auf die Site, außer GF gibt sie frei:

- >100 Kunden FirefighterVR (Eignung ja, Website nein)
- ca. 1 Mio. € Umsatz
- AVPQ-Nummer und Zugangscodes
- TMA / Omnicom / National Guard als Vertragstext
- Kosovo-Playground als öffentliche Referenz ohne Freigabe
- Schockraum-Volumen intern **328.403 €** Paid (Mappe 380 k€ tot); KI 40 k€ (ein Topf Voice/Lisa, nicht auf die Site)
- Linode / On-Prem-Hosting intern
- Pitch 2024 Meditrain-Ausgründung
- ElevenVoice / intern TTS-Pipeline

## Was nie vermischt werden darf

1. GodView (Browser-Twin) ist nicht die Unreal-Headset-App.
2. BMA Trainer ist nicht ein FirefighterVR-Headset-Modul.
3. RWE/Framatome nicht als Next-Factory-Vollprojekt (FFVR-Feuerlöscher).
4. DFV nicht als Mitgliedschaft (nur WFVD, vfdb, DRZ, DIBT).
5. Sieben Vertikale, nicht „five Verticals“ aus dem Deck.

## Verlinkung der Vertikale

Canonical-URLs:

| Marke | URL |
|---|---|
| Meditrain VR | https://meditrainvr.com/ |
| Firefighter VR | https://firefightervr.de/ (EN: https://www.firefightervr.de/en/) |
| Next Factory VR | https://nextfactoryvr.com/ |
| SpearheadVR | https://spearheadvr.de/ |
| Storywalx | https://storywalx.com/ |
| Meta-dom | https://meta-dom.de/ |
| GodView | https://godview.solutions/ |

Satelliten (keine der sieben Hub-Kacheln):

| Marke | URL |
|---|---|
| StrahlenschutzVR | https://strahlenschutzvr.de/ |
| Hand aufs Herz | https://handaufsherz-vr.de/ |
| BMA Trainer | https://bmatraining.de/ — derzeit **keine Vermarktung** |

`firefightervrmobile.de` ist Alias, kein Canonical. Neue Links immer auf firefightervr.de.

## Ton

Sachlich, produktbezogen. Keine Superlative ohne Beleg („Pioniere“, „radikal“, „nie dagewesen“, „100 %“). Keine erfundenen Kundenzahlen. Deutsch und Englisch getrennt pflegen, wo die Site zweisprachig ist — Inhalte spiegeln, nicht maschinell halb übersetzen.

## Technik öffentlich sagbar

- Unreal Engine 5, OpenXR, Standalone (Pico/Quest) für Trainingsprodukte
- GodView: Browser, Cesium, 3D Tiles, Hosting Deutschland / DSGVO (Site-Aussage)
- Photogrammetrie / Punktwolke / Digital Twin wo das Produkt das leistet
- Nicht: Unity als Leit-Engine, Eye-Tracking als NDFramework-Häkchen, Plugin-Listen aus `.uproject`

## Secrets

Keine Passwörter, AVPQ-Codes, Portal-Logins, Kundentelefone in HTML, Git oder Chats.
