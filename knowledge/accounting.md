# Buchhaltung (FreeAgent)

Live-Quelle: [FreeAgent](https://www.freeagent.com/) für **Northdocks GmbH**. Git nur destillierte Fakten.

**FreeAgent-Zahlen zählen und sind richtig** (Verkauf, Rechnungen, Angebote). Weicht Mail, Deck oder eine ältere KB-Zahl ab → FreeAgent gilt. **Ausnahme: abgerufene Fördermittel sind nicht in FA** (TEMA, feir, Spot-KI, FlowAR → [grants.md](grants.md)). FA-Umsatz und Zuschüsse nicht addieren.

MCP: `freeagent-mcp-server` in `C:\Users\joach\.cursor\mcp.json` (nicht in diesem Repo). Tokens: `~\.freeagent-mcp\tokens.json`.

Stand 30.08.2026: API lesbar (OAuth). Tax-Timeline-Endpunkt 403, ignoriert. Nur list/get/report.

## Schreibregel

Widerspruch zu [claims.md](claims.md) → [open-questions.md](open-questions.md), nicht still überschreiben. Website bleibt ohne Umsatz ([websites/_shared.md](websites/_shared.md)).

**Reschke Productions GmbH** in FA = **interne Verrechnung** (GF 30.08.2026). Nicht als Kundenreferenz, nicht in Eignung, nicht zu Umsatz-Narrativen addieren. Betrag intern merken, nicht zitieren.

**Großkunden** (Currenta, Merck, Actemium, Dom, …): FA-Kontakt-**Gesamtsumme darf** (GF 30.08.2026). Es sind oft **getrennte Projekte**, andere Ansprechpartner, andere POs. Summe = Beziehung zum Rechtsträger, nicht „ein Auftrag“. Ein Los nur mit seiner eigenen Zahl nennen. Henkel-POs SoftwareONE 442523/526042 und PSG 4503615550 zugeordnet; restliche Kanal-Zeilen nicht addieren.

## Nie ins Git

- OAuth-Client-Secret, Access-/Refresh-Tokens
- IBANs, Kontonummern, Bankumsätze
- Lohn/Gehaltszeilen, private Spesen
- Komplette Rechnungs- oder Kontaktlisten
- Private Telefone oder Privatmails aus Kontakten

## Firma (FreeAgent `GET /company`)

| Feld | FreeAgent | Hub |
|---|---|---|
| Name | Northdocks GmbH | [company.md](company.md) |
| Register | HRB 76844 Düsseldorf | gleich |
| USt-IdNr. | DE298519758, VAT Registered | gleich |
| Sitz | Niederstr. 18, 40789 Monheim, Germany | gleich |
| Währung | EUR | — |
| GJ | Kalenderjahr (Perioden 01.01.–31.12.; erstes GJ 30.01.2015–31.12.2015) | Gründung **2009** bleibt; 2015 = FreeAgent-/GmbH-Buchstart, nicht Firmenalter |
| FA-Kontaktmail | `accounts@northdocks.com` | kein öffentlicher Standard; kanonisch `kontakt@northdocks.com` |

## Geschäftsjahr / Umsatz (ohne Fördermittel)

P&L `income` = Rechnungsumsatz netto. Keine Kosten- oder Gewinnzahlen hier (Expense-Zeilen im Summary wirken unvollständig, nicht zitieren).

| GJ | Income netto (FA) | Quelle | Abgleich Claims |
|---|---|---|---|
| 2023 | 1.314.505 € | P&L 01.01.–31.12.2023 | >200 k€ ja; nahe der vagen 1-Mio-Orientierung |
| 2024 | 796.554 € | P&L 01.01.–31.12.2024 | >200 k€ ja |
| 2025 | 580.274 € | P&L 01.01.–31.12.2025 | >200 k€ ja; unter „ca. 1 Mio. € p.a.“ |

Eignungsschwelle **> 200.000 €** VR/Simulation in mind. einem der letzten drei GJ: auf FreeAgent-Verkauf **in allen drei Jahren** erfüllt. Fördermittel extra, nicht in dieser Tabelle.

„ca. 1 Mio. € p.a.“ bleibt **vage Orientierung** (GF), keine exakte GJ-Zahl, nicht auf die Website. 2025-Verkauf allein nicht als 1 Mio. zitieren. Siehe [open-questions.md](open-questions.md).

## Kontakt ↔ Projekt (Organisationen, keine Privatadressen)

| Organisation | Hub-Zeile | FreeAgent-Kontakt |
|---|---|---|
| Universitätsklinikum Köln | Schockraum / ERVR | `12855700` |
| Universitätsklinikum Frankfurt | ARiNeP | `16759258` |
| Currenta GmbH & Co. OHG | Chempark / Kits | `7087550` (weitere Currenta-Kontakte existieren) |
| Henkel AG & Co. KGaA | FFVR Werkfeuer | `17084405` / `7212980`; Standort Schoenbach `23013685` |
| Kognita sp. z o.o | Playground Kosovo | `18059335` |
| Holcim (Deutschland) GmbH | Höver GodView | `17534459` |
| Coloplast GmbH | Atos Medical-Rechnung `20250113-01` | `18494793` (daneben Kontakt Atos Medical GmbH `18124521`) |
| Ainavio GmbH | Avatar-Support | `17481156` |
| 1KOMMA5° GmbH | Showroom | `12836354` |
| Sony Music Entertainment Germany GmbH | DDF / Salztote | `14468906` — Mail-Betreff `20250304-01` = FA `20250307-02` |
| The Marketing Arm | State of Emergency | `15095952`; zusätzlich FUSE / Omnicom Media Group DE `5612457` |

## Rechnungsindex (nur schon in der KB genannte Belege)

Netto = FreeAgent `net_value`. Status 30.08.2026. Keine neuen Eignungsvolumina aus diesen Zeilen zusammenzählen.

| Ref | Kontext in der KB | FreeAgent |
|---|---|---|
| `20220307-01` | UKK Schockraum Start | 30.000 € netto, Paid, 07.03.2022, UKK |
| `20220822-02` | UKK MS II Schockraum | 60.000 € netto, Paid, 22.08.2022, UKK |
| `20230622-01` | UKK MS II Schockraum | 60.000 € netto, Paid, 22.06.2023, UKK |
| `20230731-01` | UKK MS III Instabiler Patient / Station | 90.000 € netto, Paid, 31.07.2023, UKK |
| `20230802-01` | UKK MS IV Fahrstuhl | 60.000 € netto, Paid, 02.08.2023, UKK |
| `20240226-01` | Currenta, PO 2960335518 | 1.920 € netto, Paid, 26.02.2024 — **ein** Custom-Los, nicht die Currenta-Gesamtsumme |
| `20241008-02` | Ainavio | 540 € netto, Paid, 08.10.2024 |
| `20241028-01` | ARiNeP UKFFM; KB 11.566,80 € | 9.720 € netto, Paid, 28.10.2024 — 9.720 × 1,19 = 11.566,80 (KB = brutto) |
| `20241106-01` | Ainavio | 2.970 € netto, Paid, 06.11.2024 |
| `20241202-01` | 1Komma5 | 840 € netto, Paid, 02.12.2024 |
| `20241202-02` | Ainavio | 810 € netto, Paid, 02.12.2024 |
| `20241220-03` | Kognita / Kosovo, 10 Quest | 18.160 € netto, Paid, 20.12.2024 — kein Eignungsslot |
| `20250113-01` | Atos Medical | 4.400 € netto, Paid, 13.01.2025, Kontakt **Coloplast GmbH** |
| `20250120-01` | Holcim Höver Abo Jahr 1 | 1.600 € netto, Paid, 20.01.2025 — GodView Unlimited, PO 4502769747 |
| `20250203-01` | Ainavio | 1.350 € netto, Paid, 03.02.2025 |
| `20250304-01` | DDF / Sony Salztote (Mail-Betreff Simona 04.03.2025) | FA-Nummer **`20250307-02`** 7.560 € Paid — nicht als fehlend behandeln |
| `20250305-01` | 1Komma5 | 1.200 € netto, Paid, 05.03.2025 |
| `202507-01` | 1Komma5 Mahnung 4.712,40 € | 3.960 € netto, Paid, 01.07.2025 — 3.960 × 1,19 = 4.712,40 (KB = brutto, eine Rechnung) |

UKK acht Rechnungen **328.403 €** Paid (gilt). KI 40 k€ nicht in FA. Henkel-Eignungsslice 80 k€ bleibt Mappe. Belegte Henkel-POs: SoftwareONE DEC-PO-442523 / 526042, PSG 4503615550. Restliche PSG/SoftwareONE-Zeilen nicht ungeprüft dazuaddieren.

## Pass Positionen 30.08.2026

854 Rechnungen + 991 Angebote (Estimates) gelesen; Positionen nur bei Abgleich-Belegen. Kontakt-**Gesamtsumme** bei Großkunden **erlaubt** (Kundenbeziehung). Status-Mix (Draft/Refund) vorher bereinigen. Ein Los nur mit seiner Zahl. Ohne Fördermittel.

### Kontakt-Summen (Hub-relevant, intern)

| FA-Organisation | Rechnungen | Netto-Summe | vs. KB |
|---|---|---|---|
| Metropolitankapitel Hohe Domkirche Köln | 46 | ca. 770 k€ | Meta-dom ohne Volumen; historisch Photogrammetrie |
| The Marketing Arm | 17 | ca. 726 k€ | KB nannte vor allem FY26-Slice 25 k; SOE+Philips viel größer |
| Currenta GmbH & Co. OHG | 61 | ca. **685 k€** | Gesamtsumme erlaubt (Kundenbeziehung). Mehrere Workstreams (Kits, Custom, Arena, Technikum, Bürrig). UKSH-Mappe 20 k€ nicht umschreiben |
| Merck KGaA | 15 | ca. **401 k€** | Gesamtsumme erlaubt; Technikum + Ausbildung können getrennte Lose sein |
| Universitätsklinikum Köln | 8 | 328.403 € | gilt; KI 40 k€ extra, nicht in FA |
| PSG Procurement + SoftwareONE + Henkel direkt | 56+5+14 | nicht addieren | Einkaufskanäle; Eignung **ca. 80 k€** bleibt |
| sonnen GmbH | 50 | ca. 276 k€ | KB nur „Videos“, unterschätzt |
| 1KOMMA5° | 22 | ca. 214 k€ | 2022 Aufbau (u. a. 40.470+28.451+34.870+7.100) + 2023 Tage + 2024+ Stunden; nicht ein Los |
| Actemium Cegelec West | 14 | ca. 210 k€ | Infinity/ACHEMA-Linie |
| Bundesamt für Strahlenschutz | 4+ | ca. 204 k€ | AP2 `20221114-01` 123.550 €; AP3 `20230913-01` 34.454 € — intern, nicht neues Eignungsvolumen |
| Dräger Safety Rechnungsstelle | 16 | ca. 200 k€ | KB „kein Volumen“; intern belegt, nicht Website |
| amatik Designagentur | 40 | ca. 193 k€ | Wilhelmshaven/Hannover oft über amatik, nicht über die Stadt |
| Stadtverwaltung Trier | 3 | 142.920 € Paid | gilt; Mappe 80 k€ verworfen |
| Austrian Power Grid | 8 | ca. 119 k€ | POs 4500320239 / 4500320883 bestätigt |
| InfraServ Gendorf | 1 Paid | 80.000 € `20221215-01` | Angebotszahl 47.880 € und Rejected-Estimate 142.190 € sind **andere** Papiere |
| Technische Universität Hamburg | 4 | ca. 70 k€ netto nach Gutschrift | Campus Lab 2025–26 fakturiert |
| VITA-GUARD Tomczak | 4 | ca. 34 k€ + Approved-Angebot 30.490 € | 10 Setups bestätigt |

### Positionen vs. KB

**UKK Schockraum.** Positionen: MS I Pulse/Planung 30 k€; MS II Schockraum 120 k€ in zwei Rechnungen à 60 k€; MS III Instabiler Patient 90 k€; MS IV Fahrstuhl 60 k€. Zusätzlich 2024: Überarbeitung Schockraum 10 k€ (`20240603-06`), Fahrstuhl 10 k€ (`20240603-05`), Updates Nov. 8.403 € (`20241203-01`). KI 40 k€ nicht in FA (Rechnung ab 01.01.2027). Fakturiert **328.403 €** (gilt). Mappe 380 k€ verworfen.

**TMA / SOE.** Zwei Rechnungen à 160 k€ (`20231009-01`, `20231102-01`) mit denselben sechs Szenarien: Helicopter Search & Rescue, Hazmat, River Crossing, Field Clinic, Air Traffic Control, **Urban Tank Mission**. Philips-SOW zwei Mal 65 k€ (`20231102-04`, `20240214-01`). MOS-Kit 40 k€. 2025: Visual Patient Avatar / Sound-Escape-Integration 70 k€ (`20250124-01 COR`, PO über TBWA NEBOKO); Szenario-Updates 39.150 €. `20260326-03` **25.000 € Overdue**: Unified App, 20 × 1.250 € (gilt; Mail-USD verworfen).

**Kognita / Kosovo.** `20241220-03`: **18.160 €** = 20 × 800 € + 2 PT (gilt). Mail „10 Quest“ ist nicht der Betrag.

**Currenta PO 2960335518.** `20230731-02` 5.760 € (3 POIs, Partner, Packaging, PM à 960 €) + `20240226-01` 1.920 € (20 %-Puffer, 2 × 960 €) = 7.680 €. Puffer später `20240405-02` **storniert** (−1.920 €). Slice-Arbeit damit eher **5.760 € netto** nach Storno.

**InfraServ Gendorf.** Paid 80.000 € Chemiesystem-Tage (840 €/PT, Template 7.300 €, Lizenzen 1.000 €, Rabatt −1.380 €). Rejected-Angebot `20210223-BIT-Technikum-02` 142.190 € und Kommentar 47.880 € sind nicht der Paid-Betrag.

**ARiNeP.** Positionen 9 × 1.080 €-Tage: Schmetterling, Eyetracking, Raum, Rohdaten Gehrig, Mobile, 20 %-Puffer, PM. Passt zur KB (brutto 11.566,80 €).

**Atos / Coloplast.** Zwei Rechnungen an Coloplast GmbH: `20241115-01` **6.650 €** + `20250113-01` **4.400 €** = **11.050 €**. Operativ Atos Medical Troisdorf. Nicht TEMA-ATOS. Kein Telefon ins Git.

**Sony.** Mail `20250304-01` = FA `20250307-02` 7.560 €. Weiter `20250806-01` 7.560 €, `20251022-01` 13.440 € (Wolfsburg-4K). `20221219-01` 1.240 € = ???-Rendering, anderes Los.

**Holcim.** Drive Twin+Abo **50.362 €** ≈ FA ~50 k€. Twin: `20240603-08` 10.800 + `20240627-01` 12.602 + `20240807-01` 23.760. Abo 1.600 €/Jahr: `20250120-01` + `20250829-02`. PO-Abo 4502769747; Twin-POs 4502571109 / 4502630049. LoI AI-Inspect nur Entwurf.

**BfS.** Ausschreibung **3621S42350**, Vertrag 08/2021 (Meister). Summe ca. 204 k€ intern, Produktlinie StrahlenschutzVR.

**TikTok / Bytedance.** Zwei Legal, zwei Rechnungen. UK Ltd `20250217-02` **18.261,70 €** (PO25030300594, 5 Kits London/Dubai) ≈ FA ~18 k€. Dublin `20250606-01` **14.801,36 €** (PO25051300070, 4 Kits NY, Paid 10.07.2025) **nicht** zur 18-k€-Zeile addieren. Kein Eignungsslot.

**VITA-GUARD.** Approved-Angebot `20260805-03`: 10 × FirefighterVR-Kit 2.750 €, 10 × Feuerlöscher 449 €, ohne ÜbungsLöscher −150 €/Stück, **10 Monatsraten à 3.049 €**. Lieferung aller 10 nach Anzahlung. Rechnung `20260820-42` 27.441 €.

**IMS / 20260807-02.** KB: IMS Services Angebot FirefighterVR-Kauf. FA: Estimate `20260807-02 FIREFIGHTER VR KAUF` **Invoiced** an **mekontor GmbH & Co. KG** (2.789 €), nicht IMS. IMS hat eigene Reseller-Rechnungen 10/2025–01/2026.

**Berliner Feuerwehr.** Nicht mehr volumenlos: `20251002-01` 2.916 €, `20260701-01` 4.302 € (Ausschreibung), Offer Verlängerung Support offen.

**Bodenheim.** Open-Estimate `20260824-02` FirefighterVR Kauf 3.942 € an VG-Verwaltung Bodenheim (Smart-PSA-Pfad).

**Trier.** Zwei Paid-Positionen „5W/22 Digitale Erlebniswelt VR-Stadtführung“ 84.034 € + 58.886 €. Claim 80 k€ nicht überschreiben.

**Hannover 2026.** Große amatik-Rechnungen `20260305-01` 15.000 € und `20260811-01` 25.600 € — Richtung Claim 55 k€, noch nicht Summe.

### Offene / genehmigte Angebote (kein Auftrag)

Nur merken, nicht als Referenz: Currenta CP Arena 2.0 106.920 € Open; HELIOS FFVR-Kauf 49.668 € Open; VR Synergy zwei FFVR-Offers ~74/60 k€; Actemium Merlin/Alton Towers 60.820 €; VITA-GUARD 30.490 € Approved (s. o.); THW-VR-01 11.740 €; John Deere Manheim 9.000 €; AKH Wien StrahlenschutzVR Mobile; Fresenius/Michelin/Kaufland FFVR-Kauf. Estimates: 403 Invoiced, 398 Rejected, 171 Open, 3 Approved, 16 Draft.

### Rejected / Absagen (kein Volumen)

FA-Liste der **398** Rejected-Estimates in diesem Pass **nicht** lesbar (keine Tokens). Kein Dump erfinden.

Bereits kanonisch: InfraServ `20210223-BIT-Technikum-02` **142.190 €** Rejected ≠ Paid 80.000 €. BASF EMPL-Custom Asana **Rejected**. Kepler/XFEL anderer Anbieter. Dräger Mobile `20240429` ~2.965 € = Angebot, kein Zuschlag. John Deere 9.000 € bleibt **Open**, nicht Rejected.

Mail-Absagen 2024 (Hardware-Vergabe, nicht Eignung, keine FA-Nummer hier): Landkreis **Wunsiedel** `24-L-0077-LRA` VR-Brillen (09.04.2024); Landratsamt **Eichstätt** `LRA-2024-MZ-1` VR-Equipment (15.03.2024).

## Pass Historie 30.08.2026 (FA gilt)

Ohne Fördermittel. Paid/Refund, Drafts raus.

**Currenta** Rechnungen ab **2016**. Große Paid-Jahre u. a. 2018–21 (Arena/Technikum/Wasserwerk). 2020 Gutschrift −42.820 € zu `20201126-01`. 2026: `20260415-01` **14.748 €** Paid. Kontakt-Summe ca. **685 k€** = erlaubte Gesamtsumme, **mehrere** Lose/Ansprechpartner.

**Dom / Metropolitankapitel** (Paid-Nähe nach Jahr): 2019 14 k€; 2020 164 k€; 2021 174 k€; 2022 39 k€; 2023 13 k€; 2024 78 k€; 2025 177 k€; 2026 81 k€. Läuft weiter, nicht nur „Coming Soon“.

**Merck** 12 Paid 2019–25 = **401.150 €**.

**Dräger Safety Rechnungsstelle** Custom 2020–22 (Gaming-Welt/Brandcontainer/Katalog) plus kleine 2024/25-Zeilen — intern ca. 200 k€ Kontakt, nicht Website.

**sonnen** durchgehend 2015–23 (nicht nur ein Video 2023).

**Actemium/VINCI/PC Mechatronics** 2021–24. INFINITY Imagefilm **15.000 €** (`20221018-01a`; `20221017-01` gleiche Summe, nicht addieren). Controlmatic Mitte `20240408-01` **42.369 €**. Axians Office 9.980 € separat. Lose nicht addieren.

**Dom Innenraum:** Angebot 68.400 €, belegt 50 % `20221018-01` **34.200 €**. Zweite Hälfte offen. Extra `20230417-01` 12.720 + 2026 `20260203-01` 10.060 + `20260302-01` 9.600 — andere Lose, nicht als 68.400-Rest setzen.

**amatik** 2018–26; 2026 bereits **40.600 €** (Hannover-Nähe). Wilhelmshaven: AG **WTF GmbH**, ND Nachunternehmer von amatik — keine Stadt-Rechnung. Mappe ca. 70 k€ bleibt Mappe.

**Rheinkalk/Lhoist:** drei Drive-Rechnungen **26.400 €** netto (`20191008-07`, `20200408-02`, `20200827-03`). Steinbruch-Visualisierung, nicht Factory.

**Bayer Hi-Fog:** `20230629-01` **33.336 €** netto (PO 2150948372). Ordner „3336“ falsch. Reaktivierung 15–25 k€ nur Angebot.

**1Komma5 2022–23:** Aufbau 2022 Angebot 51.520 € **vollständig** in drei Abschlägen (`20220223-01` 12.880, `20220607-03` 25.760, `20220807-04` 12.880) plus Videos `20220502-02` 40.470 €; 2023 `20230926-01` 9.538 € und `20231207-01` 9.600 €. Kontakt ~214 k€ bleibt Beziehung, nicht ein Los.

**Schwarz IT / XM Cyber:** eine Rechnung `20230321-01` **51.400 €** netto (PO 2000456014 Plan 41.520,17 €; Ist inkl. Extra). FA ~51 k€ = diese Zeile. AG seit 01.03.2026 **Schwarz Digits IT KG**. Fulldome, kein Eignungsslot.

**THW:** `20230906-01` **21.000 €** netto Paid (LV BEBBST, 2 Kits + Lizenzen). FA ~21 k€ = diese Rechnung. `THW-VR-01` 11.740 € bleibt Open.

**Evonik 2019:** `20190828-01` 14.400 + `20190926-01` 4.320 = **18.720 €** netto (Ausgangsbuch brutto 17.136 + 5.140,80). FA ~19 k€. T&I GmbH / GIS-3D Marl.

**Omexom 2026:** `20260415-02` **17.900 €** netto Paid (PO 941828791, A270). FA ~18 k€ = diese Rechnung. 2022 FR `20221124-01` 8.640 € ist anderes Legal.

**DLR 2021:** eine PO **X/369/67300871** Campus Dieburg **24.040 €** netto (`20210922-02` 8.013,33 Paid 22.10. + `20211118-01` 16.026,67). FA ~24 k€ = diese Zeile. Nicht TEMA, nicht Lampoldshausen.

**Feishu China 2026:** eine Rechnung `20260619-03` **28.358 €** (0 % USt, Quote `20260112-01`). FA ~28 k€ = diese Zeile. Outdoor-Lab Shanghai / TUHH-Template, nicht Lark-Office.

**Planetarien (getrennt):** Berlin Maus Armstrong Produktion **94.920 €** (I 23.730 + II 14.238 + III 28.476 + IV 28.476). Kombi `20220106-02` 56.952 nicht extra. Korrekturen `20230123-01` **13.440 €** separat. Bochum 39.840; Hamburg 24.192. Nicht addieren, nicht Eignung.

**Craftsmen:** `20230616-01` 42.250 € + `20230713-01` 17.472,30 USD. FA ~60 k€ bleibt Kontakt, nicht eine EUR-Summe erfinden.

**Extreme E:** `20231122-01` **5.000 €** (Sardinia-Spesen, Vodafone recharge). **Pico Immersive:** `20230612-01` **2.880 €** (Re-Cut). Nicht Eignung.

**PE HENRICH Kiew:** Vertrag 0502/23. Annex 12.597,48 € + `20231025-01` 19.500 € Paid = **32.097,48 €** Drohnen, kein XR.

**KIWI / Strandort:** Angebot 25.02.2022 **32.540 €**. Belegt `20220822-01` + `20231115-01` je **10.846,66 €** (je 1/3). `20240506-01` = dritte Teilrechnung (Betrag in der Drive-Kopie nicht OCR-lesbar; Rest **10.846,68 €** nur arithmetisch). Nicht Eignung.

**hhpberlin:** `20230803-01` **810 €** netto (Pico 4 Enterprise + Versand), Paid 07.09.2023. Hardware, kein Projektvolumen.

**EG Westholstein:** Angebot 18./08.08.2022 **20.490 €** Video-FFB; belegt nur 1/3 `20220822-03` **6.830 €** plus Flyer `20221103-02` **557 €** Paid. Restliche 2/3 nicht belegt.

**Schiffshebewerk LWL:** `20211124-03` **37.250,30 €** (nicht plus `20210928-01` 32.930,30 — gleiche Gruppen). Nachtrag `20220805-02` **500 €**. Belegt **37.750,30 €**.

**APG Wien:** sechs Drive-Rechnungen **86.350 €** (2×33.000 PoC/Real + 2×4.800 + Pico 1.000 + 2026 9.750). Teil-2-Option 66 k€ aus 2022 **nicht** beauftragt. Nicht Eignung.

**Axians Office:** `20240221-03` **9.980 €** an Actemium Cegelec West (PO 941230778). Nicht Infinity.

**Kindswater AG:** Katalog 20.830 €, belegt 1/3 `20210927-01` **6.943,33 €**. Kit `20250703-03` **2.965,34 €**. Rest Katalog offen.

**Ainavio:** Rahmen 04.06.2024, Jan-Ole Legal-Assistant. Auslesbar **13.700,99 €** (Juni–Feb inkl. `20240701-02` 6.926,99). `20240902-04` ohne OCR-Betrag. Nicht Eignung.

**Weitere FA-Blöcke intern:** Rhein-Kreis Neuss **61.416 €** netto; BASF 58 k€ (14 Rechnungen) — keine neuen Eignungsslots.

**Reschke Productions GmbH:** FA-Kontakt intern ca. 137 k€. **Interne Verrechnung**, kein Kunde. Nicht in `projects.md`, nicht in Eignung, nicht als Referenz.
