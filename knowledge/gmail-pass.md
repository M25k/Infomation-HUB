# Gmail-Tiefenpass (laufend)

Ziel: Mailbox `joachim@northdocks.com` vollständig gegen die KB aufarbeiten. Kein Skim. Keine Secrets (Passwörter, AVPQ, Portal-Logins, Kundentelefone, private Mobilnummern) ins Git.

Stand Mailbox 28.08.2026: Inbox ~76.6k Threads / ~39k ungelesen; Sent ~9.6k; Starred 22; Label `Northdocks Rechnungen` (Label_9) 34 Threads — Plugin-Suche nach `label:Label_9` lieferte bisher leere Treffer, Slice Rechnungen offen.

## Filter

Immer ausschließen: `from:asana.com`, Vergabe-Newsletter, Promotions, WordPress-Spam (`[Radiation Protection VR] Bitte moderiere`), Linode-Alerts außer Team-Hinweisen, Booking/Apple/Google-Promo.

`get_thread` mit `PLAIN_TEXT`. Drafts sind keine Fakten.

## Coverage

| Slice | Status | Pass |
|---|---|---|
| 2026 Kunden/Förder-Oberfläche | erledigt | 20 |
| TMA / State of Emergency / Omnicom 2024–2026 | Kern gelesen (V4 signed, FY26 25k USD, Consolidation, MOS/ArborXR) | 21 |
| Bayer 2026 Pipeline (Mais, Vials, Gewächshaus) | erledigt | 21 |
| Currenta Absender (Lieferant 37966, POs, Befliegung) | Inventar, keine Volumensumme | 21 |
| RWE PO | nur Kontaktformular 03/2021 Probeanmeldung; keine PO | 23 |
| Henkel Absender (Tablet 2.0, VeSACh, Sprinkler, Ariba) | POs belegt (SoftwareOne DEC-PO-442523/526042, PSG 4503615550, Ariba 4577279489). **Kein** neues Volumen; Eignung bleibt ca. 80.000 € | 28 |
| UKK Rechnungen 2023 (Meilensteine II/IV) | gelesen; plus MS III Instabiler Patient `20230731-01`, MS II auch `20220822-02`, Start `20220307-01`. Zuschlag **28.12.2021** | 21, 27 |
| EIC NKS 04.08.2026 | gelesen; **Anlauf auf 2027 verschoben** (GF 28.08., Asana-Kommentar) | 21–22 |
| Stadt Köln GIS / Dom 09.2025 | gelesen | 21 |
| TEMA Grant-ID / ENG MinIO / ATOS-Amendment | Grant 101093003; Amendment ATOS→BULL eingereicht 26.06.2026; M36-Deliverables akzeptiert; RP2 verzögert | 28 |
| Spot-KI GEOMAR Benavides | belegt | 21 |
| Starred 22 | gesichtet; Noise (WP-Spam, Asana, Linode) übersprungen | 21 |
| Crane Currency, XFEL Fusion, Dräger 2024 Angebot | gelesen | 21 |
| Rechnungen-Label 34 Threads | Plugin `in:Label_9` weiter leer. Fallback: UKFFM **20241028-01** 11.566,80 € (ARiNeP); Henkel-PSG 12-Monatsbestellung endete 01/2022 | 26 |
| Kosovo Playground Mail | gelesen: Kognita → Interadria, Rechnung 20241220-03, 10 Quest | 23 |
| Feuerwehr Berlin / VITA-GUARD Belege | Berlin **2026-199** = Berliner Feuerwehr Hardware-Zuschlag. VITA-GUARD 10 Setups intern (Asana + Mail Tomczak) | 24 |
| Historisches Asana-Archiv (105 Boards) + Merck/Actemium/Framatome/THW/Spot-KI | Inventar in history.md; Merck-POs und Spot-KI-Erstattungen gelesen | 22 |
| FlowAR / feir / EPIC Mega Grant Originalzusage | FlowAR IN-NX-2-013c + Bescheid 23.05.2025; EPIC **45.000 USD** 10.06.2020 | 23 |
| Sent-Angebote 2024–2025, Quassum/Fulldome 2009–2018 | Intel IFA 2014/15; **Quassum-Kern**: Einstellung 24.05.2018 JacPer UG i.L.; Support ab 2011. Keine 2009-Gründungsmail | 26 |
| UKK Station / Pulse / ARiNeP volle Historie | Pulse-Eval 06.12.2021, Zuschlag 28.12.2021, drei Szenarien inkl. Station. ARiNeP-Rechnung UKFFM. Station-Produktseite weiter Frontiers | 27 |

Nächster Tick: Rechnungen-Label (Plugin weiter leer) oder ältere UKK-Rechnungen vor 2022. Henkel-POs und TEMA-Amendment-Kern geschlossen — Volumen Henkel unverändert 80 k€.

## Schreibregel

Widerspruch zu kanonischen Claims → `open-questions.md`, nicht still überschreiben. TMA-Dokumenttitel „on behalf of US Army“ bleibt Vertragssprache von Omnicom, nicht der Claim „Kunde US Army“.
