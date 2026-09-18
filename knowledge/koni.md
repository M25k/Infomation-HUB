# Koni Trainer

Kanonisch. Stand Quellenlauf **18.09.2026** (Asana, Gmail `joachim@northdocks.com`, Drive). Keine FreeAgent-Rechnung — Forschung, kein Verkauf.

**Koni = Konisation (LLETZ), nicht Koniotomie.** Zervix, Kolposkop, Elektroschlinge. Soft-Tissue-Cutting für operative Gynäkologie. Meditrain-Pipeline / Coming Soon, **kein Katalogmodul**, nicht als ausgeliefert behaupten.

## Was es ist

Akademischer VR-Trainer der **Hochschule Darmstadt (h_da, nicht TU Darmstadt)** und der **Frauenklinik UKW**. Northdocks hat den Unity-PCVR-Stand ab 10/2025 nach Unreal / Meditrain-CI auf **Pico 4 Ultra** (Mobile, ohne Login) portiert. Produktziel intern: Soft-Tissue-Cutting auf Edge-Devices, OpenXR, Local-Only, passive Haptik statt Force-Feedback-Roboter.

RC1 seit **26.11.2025**. Danach keine Entwicklung. Offen und ohne Assignee: **Mesh Cutting** (das eigentliche Schneiden) und **Auswertung/Statistik**.

## Partner

| Wer | Rolle |
|---|---|
| Northdocks GmbH | Port, Meditrain-CI, Koordinator KMU-innovativ-Skizze. Intern: Joachim (Antrag), Patrick (Anstoß), Marcel Timm (Unreal), Renke (Assets), Silas (CC) |
| Prof. Dr. Ute Trapp | h_da / EUT+, Fachbereich Informatik (UX). GitLab-Quelle. HAW-Skizze 05.08.2026 allein eingereicht |
| PD Dr. med. Matthias Kiesel | Oberarzt Frauenklinik und Poliklinik, Uniklinikum Würzburg. Klinische Validierung / Studienpfad |
| Prof. Dr. Christine Wulff | Nur auf einem UKW-Entwurf (30.04.), nicht als Verbundpartner der eingereichten Skizze |

Arbeitsteilung ab **18.06.2026** (Joachim an Trapp): ND liefert höchstens Textbausteine. **Keine zweite KMU-innovativ-Federführung.** Einreichung künftig Hochschule/Klinik.

## Förderung

| Vorgang | Stand | Kern |
|---|---|---|
| **KMU-innovativ Medizintechnik**, 30. Runde, Akronym **VR-Koni-Edge**, Skizzen-ID **100771908** | **Abgelehnt 10.07.2026** (VDI TZ an Joachim; 139 Skizzen, keine Priorität). Partner informiert **13.07.2026** | easy-Online **15.04.2026 08:20**. Titel: *Strategische Neuausrichtung des VR-Koni-Trainers: Hardware-agnostische Soft-Tissue-Cutting-Engine auf Edge-Devices*. Verbund ND (Koordinator) + UKW + h_da. Gesamt **1.310.000 €**, beantragt ca. **1.079.000 €**, 36 Monate. Asana-Task „KMU Innovativ Antrag“ liegt noch in *Eingereicht* — Status dort veraltet |
| Zweiter BMFTR-Anlauf (Trapp-Entwurf *Koni-AntragBFTR-MT4W*) | **Nicht eingereicht** | Frist **30.04.2026 13:00**. Kiesel um Aufschub gebeten, Frist verpasst |
| **HAW-ForschungsSchub** | Mini-Skizze **05.08.2026** durch Trapp allein, **200.000 €**. Losverfahren bis 60 HAW; Call 1 **15.09.2026**. Los-Ausgang hier **nicht** belegt | Fördermittel **nur** an die HAW. ND und UKW höchstens assoziiert, ohne Zuwendung. Finanziert h_da-Weiterentwicklung, **nicht** ND-Produktisierung. Stufe-1-Aufwand für ND null; Entscheidung erst bei Los + Partnerzusage im Vollantrag |
| Innovationsfonds G-BA (Versorgungsforschung, themenoffen 19.06.2026) | Idee Trapp 14.07., Kiesel teilt Einschätzung 16.07. | Federführung Kiesel, Fokus Behandlungsqualität/Patientensicherheit bei der Konisation. 36 Monate, nur **75.000 €**, aus Trapp-Sicht aufwändig. Kapazität Trapp SS 2027 |
| Forschungszulage | Vorschlag Trapp 14.07. an ND | [bescheinigung-forschungszulage.de](https://www.bescheinigung-forschungszulage.de/) — intern offen, kein Antrag hier |
| VLP Plus | Nur in früher Task-Notiz | Validierung, Antrag von UKW; nicht als laufend behandeln |

Ablehnung nennt außer fehlender Priorität **keinen** fachlichen Grund. Kiesel bat 16.07. um das Begründungsschreiben — **unbeantwortet**. Entweder so mitteilen oder vorher VDI TZ anrufen (`kmu-innovativ-medizintechnik@vdi.de`).

## Entwicklung (Asana-Projekt *Koni Trainer*)

Team Interne Projekte. Board 38 Tasks, **30 erledigt / 8 offen**. Due des Projekts war 17.10.2025. Mitglieder: Joachim, Patrick, Marcel, Renke.

Erledigt (Auswahl): Repo/Projekt aufsetzen, Assets (Gynostuhl, Colposkop, OP-Tisch, TV, Hocker), Elektroschlinge grabbar, Colposkop-Kamera, Tutorial, Settings, Savegame, RC1. Offen in Documentation/Backlog: Doku, Meetings, Repo-Infos (`MTVR-Koni`), Logos (UKW Frauenklinik, UKW, h_da), **R+D Mesh Cutting**, **Auswertung/Statistik** (jeweils als Dublette Task + R+D).

Marcel 17.10.2025: Unity-Stand ist PCVR mit Hub/Login; Einschätzung ~10 Tage ohne Login, plus 3–5 Tage Assets, plus 4–5 Tage falls Auth. Joachim: Ziel **Mobile Q3 / Pico 4 Ultra**, Login weglassen, CI analog Strahlenschutz unter Meditrain.

## Code und Drive

| Ort | Inhalt |
|---|---|
| GitLab h_da `vr-koni-trainer` | Ursprung Unity. Release-Job in der Asana-Projektbeschreibung |
| GitLab h_da `accuracy-evaluation` | Controller-Genauigkeit (Patrick 18.02.2026) |
| Intern `MTVR-Koni` | ND-Unreal-Repo (Asana *Repo Infos*) |
| Drive-Zip `vr-koni-trainer-main.zip` | Unity-Export 16.10.2025, ~1 GB |
| Shared Drive `Projects_Koni` | Assets (Colposcop, Gynochair) |
| Drive-Ordner *Koni Trainer* | Hülle 28.08.2026, leer |
| Skizze eingereicht | `VR-Koni-Edge-projektskizze-kmu-innovativ-medizintechnik-02-2026.docx` (14.04.2026) |
| Patrick-Entwurf | *Förderantrag: Koni Trainer VR Stand 20.02.2026* |
| Joachim-Umbau 13.03. | *Koni Projektskizze: KMU-innovativ: Medizintechnik* (MDR raus, Innovation statt Skalierung) |
| LoI-Vorlage | assoziierte Lehrkrankenhäuser, unverbindlich |
| Trapp 30.04. | *Koni-AntragBFTR-MT4W* (nicht eingereicht) |

Patrick-Statusmemo 06.08.2026 (Asana *Koni Trainer* + intern MediTrain VR `02_Kontext/2026-08-06_koni_trainer_status.md`).

## Claims

Erlaubt intern: Partnerschaft h_da + UKW in der **Antragsgeschichte**; akademischer Unity-Prototyp; ND-RC1 Mobile ohne Mesh-Cutting; Ablehnung VR-Koni-Edge dokumentiert.

Nicht: Koni als ausgeliefertes Meditrain-Modul; Soft-Tissue-Engine live; „klinisch validiert an Würzburg“ (steht fälschlich auf Fresenius/Helios-Decks); TU Darmstadt; Koniotomie; Volumen 1,31 Mio. € als bewilligt; HAW-200 k€ als ND-Mittel.

Bielefeld-Kinderchirurgie nutzt Softbody — das ist ein **anderes** Los, nicht Koni/OP.

## Offene Punkte

1. HAW-Los nach Call 1 (15.09.2026) — Ausgang unbelegt.
2. Kiesel-Bitte um Ablehnungsgründe — unbeantwortet.
3. Mesh Cutting / Statistik — unbesetzt, seit RC1 stehen.
4. Forschungszulage und G-BA-Innovationsfonds — nur Idee.
5. Asana-Folge: [Koni Trainer — Weiterführung Meditrain / Folgepfade](https://app.asana.com/1/8864272155433/project/1200346071931886/task/1218626781608081) in *Sammlung* (18.09.2026). Alte Antrags-Tasks geschlossen und nach *Abgelehnt* gezogen. Technisches Board bleibt offen.
