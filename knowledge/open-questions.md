# Offene Fragen und Widersprüche

Geklärte Punkte bleiben kurz dokumentiert. Nur offene Punkte blockieren Formulierungen.

## Geklärt 2026-08-26

| Thema | Entscheidung |
|---|---|
| Vertikale | Sieben wie northdocks.com. Deck mit fünf ist veraltet. |
| FFVR-URL | Canonical https://firefightervr.de/ |
| >100 Kunden | In Eignung erlaubt |
| Firmenalter | 2009 CAU Kiel, vier Studierende, Joachim verbliebener Gründer. Patrick über Intel, nicht Gründer. Erstprodukt Quassum (tot). VR über Fulldome/Planetarium zum Kern. Nicht „17 Jahre FirefighterVR“. |
| Dom-Erfassung | 100.000+ Fotos **und** 1.000 Laserscans zitierfähig. 30.000 aus 2020 verwerfen. |
| Spot-KI | Nur KI-Transfer-Hub SH / EU+Land. Keine Vodafone, keine UKK. |
| GodView | Zwei Kundentypen auf einer Plattform: Bauinspektion vs. Einsatz/Playground. Nicht Headset-Trainingsapp. |
| Repos | C:\Githup-Checkouts als Cursor-Codebase-Referenz nutzen (siehe repos.md). |
| Meditrain-Rechtsform | Bleibt Vertical der Northdocks GmbH. Pitch 2024 (Ausgründung/Startup) ist tot. Produktziel: Koffer + Hardware/Software-Komplettpaket analog FirefighterVR. |
| Spearhead / TMA | **The Marketing Arm (TMA)**, Teil von Omnicom, ist Auftraggeber der National-Guard-Trainings. Lieferung intern **State of Emergency**. Zweitens: Playground-Sonderversion Kosovo. Site-/Deck-Zahlen nicht verwenden. |
| RWE / Framatome | Nutzen das FirefighterVR-Paket **Feuerlöscher**. Auf nextfactoryvr.com, weil es Factory-Randfälle gibt (z. B. Sprinklerwartung) — nicht als Full-Custom-Next-Factory-Twins führen. |
| Kontakt | Kanonisch **kontakt@northdocks.com** (+49 2173 9996713). Andere Adressen auf Vertical-Sites nicht als Firmenstandard. |
| BMA Trainer | Eigenes Produkt, perspektivisch Funnel für FirefighterVR (z. B. WebXR). Derzeit **keine Vermarktung**. |
| Umsatz | Intern vage **ca. 1 Mio. € p.a.** (GF). In Eignung die Schwelle >200.000 € VR/Simulation in mind. einem der letzten drei GJ. Keine präzise GJ-2026-Zahl nach außen. |
| Alte FFVR-Plattform | PCVR mit PC-Launcher (Steam-ähnlich). Eingestellt, weil Kunden PCVR als zu teuer und kompliziert rückmeldeten → Wechsel auf die Koffer-/Standalone-Lösung. Nicht „gescheitert“ nach außen. |
| Currenta | Viele Jahre, **mehrere** Vorhaben. Immer trennen: Custom-Aufträge vs. FirefighterVR-Kits. Keine einzelne Summe als „das“ Currenta-Volumen. UKSH-Eignungstext mit **ca. 20.000 €** so lassen (GF 2026-08-26) — das ist der Eignungsslice in der Mappe, nicht das Gesamtvolumen. |
| DFV vs. WFVD | Öffentliche Mitgliedschaften nur wie auf firefightervr.de: WFVD, vfdb, DRZ, DIBT. Deck-Phrase „German Fire Brigade Association“ nicht als DFV-Partnerschaft. |
| ElevenVoice | Intern **kanonisch**: ElevenVoice für die **meiste** Sprachausgabe (TTS) in den XR-Produkten. Ausnahmen: diverse **Fulldome-Shows** und die **VR-Stadttouren** (Storywalx). Plugin-Dateien fehlen im `NDVRActemium`-Checkout — Nutzung trotzdem intern Standard, nicht als Website-Marketingclaim. |

## Noch offen

### Website-Link firefightervrmobile.de

Canonical bleibt https://firefightervr.de/. In `www-northdocks` stehen noch Mobile-Links in `index.html`, `index-en.html`, `virtual-reality-training.html`, `virtual-reality-training-en.html`, `online_index.html`. Fix gehört in jenes Repo, nicht in diese KB.

### Content-Repos

FFVR-Szenen: Drive `ND-AssetReferenz` (`NDAssetReferenz.uproject`), nicht unter `C:\Githup`. National-Guard **State of Emergency**: Asana-Repo-Karte, Checkout nicht lokal gefunden.

### Kepler-Fulldome-Profil (Drive, 07.07.2026)

Dokument „Unternehmensprofil & Referenzen - Northdocks GmbH - KEPLER Fulldome“ ist eine **Antragsfassung**, nicht kanonisch. Widerspricht der KB u. a. bei Dom-Erfassung (dort 200.000 Fotos / 25 Mrd. Polygone / 1 mm — kanonisch bleiben 100.000+ Fotos **und** 1.000 Laserscans, öffentlich 2B+). Renderfarm (40 Server, 90 TB), ESA/ESO/MPI-Netzwerk und „Cross-Platform SciVis-Pipeline“ daraus **nicht** ungeprüft übernehmen. XM Cyber (2023–24) und Intel IFA 360 (2016) stehen nur in diesem Entwurf — intern notieren, nicht als Website-/Eignungsstandard.

### FFVR-Modulzahl 22 vs. 23

Internes Didaktik-Dokument v47 (März 2026) spricht von **22** Modulen. Öffentliche Site und diese KB führen **23** namentlich aus `trainingslist.html` (u. a. Firesaber). Bis zur Abstimmung: nach außen **23** laut Website, v47 nicht als Modulzähler zitieren.

### FlowAR iOS vs. Android

Öffentlich bleibt EFRE-AR-Kunst. Intern ist der Prototyp Android (Mapbox/OpenGL). iOS braucht Mac + Apple-Developer-Account (Asana offen, 19.08.2026). Nicht „native iOS-App live“ schreiben.

### Meißen zweite Eignungsreferenz

Henkel/Kornetzky **freigegeben** (GF 26.08.2026). Hannover VR **nicht** als Slot 2. Slot 2 soll in der FirefighterVR-Linie bleiben: **Hand aufs Herz** (Bildung, Schule, offline; Volumen in der KB nicht als Euro) oder zweites Werkfeuer (**Currenta**, Slice benennen). Formblatt braucht zwei Kundenprojekte, nicht die Marke allein.
