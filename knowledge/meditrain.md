# Meditrain VR — Medizinlinie

Canonical: https://meditrainvr.com/  
Marke der Northdocks GmbH. Telefon auf der Site: +49 2173 9996714. Mail: kontakt@northdocks.com.

Strategie: [strategy.md](strategy.md) — FFVR-Betriebsmodell auf Klinik übertragen.

## Pain Points (Klinik-Sprache, intern abgestimmt)

Fachkräftemangel, Zeitmangel, Patientengefährdung beim Realtraining, fehlendes Arzt–Pflege-Teamtraining, teure raumgebundene Simulatoren, harte Klinik-IT (kein Cloud-Zwang).

Lösungssatz: Standalone-VR, Local-Only, interprofessionell, Physiologie statt Skript, passive Haptik statt Millionen-Roboter.

## Module

| Modul | Partner / Beleg | Stand | FFVR-Analog |
|---|---|---|---|
| **Schockraum VR** (interner Projektname bleibt; außen **ERVR** / **Emergency Room VR**) | UKK, PD Dr. Rabi Raj Datta; cABCDE; Multiplayer; Physiologie; Debriefing; Sprach-NPCs | Referenzprojekt, FA **328.403 €** Paid + KI 40 k€ zugesagt (noch nicht in FA, Rechnung ab 01.01.2027); AMBOSS 2026; Voice „Hey Lisa“ Kickoff 01.07. Zielhardware **Pico Project Swan**, Mobile-Ports laufen. Emergency **Response** nicht. | Innenangriff / Team / Debriefing |
| **Station VR** | UKK; Ursprungsszenario **Instabiler Patient auf Normalstation**. Produkt: 9 randomisierte Notfälle, Zwei-Spieler Arzt & Pflege. Frontiers 2026 DOI 10.3389/frvir.2026.1737515 = **Delphi-Lernziele**, Hardware Paper **PCVR Pimax**, nicht Pico-Koffer-Wirksamkeit. Rechnung MS III `20230731-01` | Produktseite live | Szenarien-Katalog |
| **Strahlenschutz VR** | BfS, evaluiert UKK und UKSH; **Präsenz ECR 2024** (Wien). Award nur Deck. Site https://strahlenschutzvr.de/ | Am nächsten an FFVR-Produkt: Miete ab 499 €/Woche, Kauf ab 3.499 €; § 63 StrlSchV / ALARA | Koffer + Pflichtunterweisung |
| **CPR VR** | Björn-Steiger-Stiftung; Puppe, Drucktiefe/Frequenz, Röntgenblick | Auch FirefighterVR-Paket CPR. Schulableger **Hand aufs Herz** (handaufsherz-vr.de): Pilot OHG Monheim öffentlich nennbar; bis Aug. 2026 vier Kurse, Feedback intern nach 31.08. Stiftung-Gespräch intern offen. Offline, keine Schülerdaten. Vertical-Mail nicht als Firmenstandard | Identische Haptik-Linie |
| **Koni / OP (Coming Soon)** | Soft-Tissue-Cutting auf Edge-Devices; h_da / Uniklinik Würzburg in Antragsgeschichte | Forschung, nicht Katalog | Neues Fachmodul |
| **Flashlight / UKSH** | Interreg, acht Lagen, Rettung, Eye-Tracking | Angebot/Vergabe 2026 | Planspiel + Medizin-Lagen |
| **Triage / MANV (Pipeline)** | Spezifikation UKFFM 28.08.2026; fachlich UKK/CeMIT | Innerklinische Sichtung, 20 Patienten, Scan Anfahrt. Kein Auftrag, eigene Vergabe UKFFM. ARiNeP nicht als Beleg. TEAM-X 2024 nicht als Produkt | Neu-Modul, nicht Katalog |
| **ARiNeP** | Uniklinik Frankfurt Neurologie, Eye-Tracking CSV | Referenz Eye-Tracking, nicht Meditrain-Katalog | Blicksteuerung Storywalx-Linie |

Erste Hilfe Actemium (Pitch 2023) ist Industrie-Erste-Hilfe, näher an Next Factory / FFVR als an Klinik-Meditrain.

## Partner und Köpfe

| Wer | Rolle |
|---|---|
| Uniklinikum Köln / CeMIT | Schockraum, Station, Lehre, AMBOSS 2026 |
| PD Dr. Rabi Raj Datta | Lehrkoordinator, Testimonial. Pitch-2024-Wort „Gründungsteam“ nicht mehr verwenden |
| Dr. Jana Adams | Fachpartnerin Station VR, Frontiers-Paper 2026. Nicht als Startup-Gründerin führen |
| Niels-Benjamin Adams | UKK, CC auf Meditrain-Terminen ab 21.07.2026 — intern, nicht als Website-Zeuge |
| AMBOSS SE | LiSA / AMBOSS AI Mode. Kontakt Lina Glaser (Product); Hackathon Juni 2026; LoI intern offen. **Nicht** behaupten, Meditrain liefere AMBOSS-Wissen als fertiges Produkt |
| BfS | Strahlenschutz VR |
| UKSH | Strahlenschutz-Historie, Flashlight 2026 |
| Björn-Steiger-Stiftung | CPR |
| Medizin-Studierende UKK | Pulse Engine (Asana Status UKK-VR) |

## Technik, die aus FFVR kommt

- Unreal / OpenXR / Standalone (Pico/Quest). Schockraum: Mobile-Ports für **Pico Project Swan** laufen; Auslieferung dort wahrscheinlich, noch nicht als live behaupten.
- Multiuser online und offline
- Haptische reale Objekte im Tracking
- Local-Only für regulierte Netze
- Debriefing / Logs (CSV/JSON analog UKSH)
- GodView nur als Leitung/Debrief (Typ B), nicht als Headset-App

Medizinspezifisch dazu: physiologische Echtzeit-Engine (Pulse), Sprachsteuerung NPCs, cABCDE, Dosimetrie-Simulation. GitHub `ND-Strahlensimulation` ist Unreal **4.27** (`NDRaySimulation`) — historischer Beleg, nicht der 5.7-Produktionsstand. UKK KI/Voice: **ein Topf** 40.000 € aus UKK-Mitteln (Datta) ab 01.01.2027, nicht in FA. Kickoff 01.07.2026: Voice Control („Hey Lisa“). Stack **unabhängig von AMBOSS**. LoI AMBOSS separat, kein zweites 40 k€. Medizinische ASR-Modelle intern in Test — nicht als ausgelieferte Standardfunktion. Paper-NPC-Spracherkennung (Frontiers Delphi) nicht mit Pico-Lisa vermischen. Frankfurt-Klinik: Spezifikation „Modul Triage“ 28.08.2026 da (MANV/Sichtung UKFFM). Vergabe noch nicht veröffentlicht; Angebotsfähigkeit intern offen. AR-Anamnese separat, Förderidee, nicht Liefergegenstand.

## Sites und Repos

| URL / Repo | Inhalt |
|---|---|
| meditrainvr.com | Dachmarke, Module |
| strahlenschutzvr.de | Pflichtunterweisung Katheterlabor, Preise |
| handaufsherz-vr.de | Schul-CPR, Launch 2026, Pilot OHG Monheim |
| `WWW-meditrain-vr` | Website |
| `www-strahlenschutzvr` | Landing + Ads |
| `www-handaufsherz` | Schulprodukt, nutzt FFVR-CPR-Fotos |
| Asana `UKK - VR` | laufende Klinikentwicklung |
| Asana `MediTrain VR - Plattform` | archiviert, 4 offene Tasks |

## Claims — vorsichtig

Erlaubt: UKK-Partnerschaft, BfS, Präsenz ECR 2024, AMBOSS 2026, Frontiers-Paper Station **als Delphi**, Strahlenschutz-Preismodell der öffentlichen Site, 97/94/91 % aus Strahlenschutz-Evaluation **als Studien-/Deck-Zahlen mit Quelle**, Schockraum-Volumen intern **328.403 €**.

Nicht: SaaS-Abo-Prognosen aus Drive-Kalkulator; „komplettes Klinik-Ökosystem schon ausgeliefert“; Meditrain als eigenes Startup oder Ausgründung (Pitch 2024, verworfen); Vodafone (gehört nicht hierher).

## Produktmodell (kanonisch)

Marke der Northdocks GmbH. Ziel: **Koffer / Hardware+Software-Komplettpaket** wie FirefighterVR (auspacken, lokal trainieren, Katalog inklusive). Pitch-2024-Ausgründung ist tot. In EIC/Investorentexten: Produktlinie der GmbH, nicht neue Gesellschaft.
