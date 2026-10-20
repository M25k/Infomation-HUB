# Logo-Intros, Transitions und Logo-Animationen (Video)

Stand: 19.10.2026. Alle Dateien nur lesend aus dem Drive geladen (Northdocks-Intros per Drive-Connector, Submarken-Animationen aus `Verticals-Logos.zip` per rclone auf dem GPU-PC). Technische Werte per ffprobe gemessen. Kontaktbögen liegen bei Northdocks Video (nicht im Repo).

**Katalog und Freigabe (Wissen, 19.10.2026):** Alle Dateien stehen in [../assets/assets.csv](../assets/assets.csv), Katalog-ID in Klammern hinter dem Link, alle „nur intern“ (Regel 13). Stumme Tonspur der Intros A/B, der Transition und von Komp 1 von Wissen nachgemessen (−91 dB, keine Musik). PREVIEW_Transitions hat durchgehend Ton (mittel −16,5 dB, nachgemessen); Musik und Quelle sind ungeklärt, daher nie ins Angebot (Regel 6/11).

**Kernaussage:** Keine einzige Datei hat einen Alpha-Kanal. Alle sind H.264 MP4, yuv420p. Northdocks-Intros haben eine stumme AAC-Spur (−91 dB). Die Submarken-Animationen haben keinen Ton. Alles ist 16:9 (bzw. 2:1 equirectangular für VR), für 9:16-Reels also neu zu komponieren. Da alle Hintergründe einfarbig sind, geht das per Center-Crop bzw. Einbetten auf eine Fläche in Hintergrundfarbe.

## Northdocks (Dachmarke)

| Datei | Drive-ID | Ordner | Datum | Format | Auflösung | fps | Dauer | Alpha | Inhalt |
|---|---|---|---|---|---|---|---|---|---|
| INTRO_varinatA_soild.mp4 | [18SJADO5pM0CbUTW9aSRKlxohou1R75Zi](https://drive.google.com/open?id=18SJADO5pM0CbUTW9aSRKlxohou1R75Zi) (ND-0003) | ND_WEB_VIDEO_INTRO / V002 ([1L9wrMRWmNP_XphWo435n9vHxIRaYvv0f](https://drive.google.com/open?id=1L9wrMRWmNP_XphWo435n9vHxIRaYvv0f)), Kopie in _ND_Resources / Streaming & Video Editing / Transitions & Intros ([1s75iL70aNY76baF8n8wucF4JBZsetrSP](https://drive.google.com/open?id=1s75iL70aNY76baF8n8wucF4JBZsetrSP)) | 31.03.2020 (Kopie 01.12.2020) | MP4 H.264 | 1920x1080 | 30 | 3,0 s | nein | Weißer Schrägbalken-Wipe, Bildmarke fliegt ein, Logo quer (Bildmarke + NORTHDOCKS) weiß auf #505050, Ausblendung. Logo-Box x 525–1356 |
| INTRO_varinatB_soild.mp4 | [1GeiP6BP5lOqNS1R7brxMqWL_wj1bSA5v](https://drive.google.com/open?id=1GeiP6BP5lOqNS1R7brxMqWL_wj1bSA5v) (ND-0004) | dto. | 31.03.2020 (Kopie 01.12.2020) | MP4 H.264 | 1920x1080 | 30 | 3,0 s | nein | Wie A, aber Logo hoch (Bildmarke über Wortmarke), x 712–1159 |
| LgogTransition2x.mp4 | [1h0DEo_AZswDwrBidWQLV0hqm4pH3ibFY](https://drive.google.com/open?id=1h0DEo_AZswDwrBidWQLV0hqm4pH3ibFY) (ND-0493) | _ND_Resources / Streaming & Video Editing / Transitions & Intros | 03.11.2020 | MP4 H.264 | 1920x1080 | 30,65 | 1,56 s | nein | Doppelt schnelle Fassung von Variante B, endet stehend auf Logo hoch |
| INTRO_varinatA/B_soild.mp4 (Kopien in Transitions & Intros) | exakte Duplikate, nicht verlinkt | _ND_Resources / Streaming & Video Editing / Transitions & Intros | 01.12.2020 | | | | | | md5-identisch mit ND-0003/ND-0004, keine eigene Katalog-ID ([../assets/aufraeumen.md](../assets/aufraeumen.md)) |
| ND_InOut_v002_clean.aep | [16yT4GizGemVtzUpFFS-QvtIkWPiazlCW](https://drive.google.com/open?id=16yT4GizGemVtzUpFFS-QvtIkWPiazlCW) (ND-0005) | ND_WEB_VIDEO_INTRO / V002 | 31.03.2020 | After-Effects-Projekt | | | | (renderbar) | Kompositionen INTRO_varinatA/B, INTRO_varinatA/B_soild, OUTRO_varinatA/B. Logo als Shape-Layer (ND_Sym_FILL, ND_TYPO_FILL), also vektoriell. Die Nicht-solid-Comps und die Outros sind nicht als Render im Drive; aus dem AEP ließen sich Fassungen mit Alpha (ProRes 4444 / PNG-Sequenz) und 9:16 rendern |
| previw_varA.mp4 (V001) | [1Z6Sk-DIY36Cd2ErYNBYOJBJ5OOO0Xs9x](https://drive.google.com/open?id=1Z6Sk-DIY36Cd2ErYNBYOJBJ5OOO0Xs9x) (ND-0001) | ND_WEB_VIDEO_INTRO / V001 | 31.03.2020 | MP4 H.264 | 1920x1080 | 30 | 10,03 s | nein | Vorschau-Schnitt: Intro A auf Schwarz, Kölner-Dom-Rendering, Outro mit großer Bildmarke, Logo quer auf Schwarz |
| previw_varB.mp4 (V001) | [18x_EH5gxFE7wh_EU2KPOjIADn1IN-YQi](https://drive.google.com/open?id=18x_EH5gxFE7wh_EU2KPOjIADn1IN-YQi) (ND-0002) | dto. | 31.03.2020 | MP4 H.264 | 1920x1080 | 30 | 10,03 s | nein | Wie oben mit Logo hoch auf Schwarz |
| preview_v002_varA.mp4 | [19bD6sBfY55ulyldqb5Fzs3-SCq7XnPPo](https://drive.google.com/open?id=19bD6sBfY55ulyldqb5Fzs3-SCq7XnPPo) (ND-0006) | ND_WEB_VIDEO_INTRO / V002 | 31.03.2020 | MP4 H.264 | 1920x1080 | 30 | 10,03 s | nein | Wie V001 A, Hintergrund #505050 statt Schwarz |
| preview_v002_varB.mp4 | [1WTsXDHuQNjrMzYgerzazUcPeN3h0DH7_](https://drive.google.com/open?id=1WTsXDHuQNjrMzYgerzazUcPeN3h0DH7_) (ND-0007) | dto. | 31.03.2020 | MP4 H.264 | 1920x1080 | 30 | 10,03 s | nein | Wie V001 B auf #505050 |
| preview_v002_varB_solid.mp4 | [1y9W7NCh-ObT5qiMqrTgLINrUwbNdRjUi](https://drive.google.com/open?id=1y9W7NCh-ObT5qiMqrTgLINrUwbNdRjUi) (ND-0008) | dto. | 31.03.2020 | MP4 H.264 | 1920x1080 | 30 | 10,03 s | nein | Laut Name Solid-Fassung von v002 B, im Kontaktbogen optisch wie v002 B |
| preview_v002_varA/B.mp4 (Kopien) | exakte Duplikate, nicht verlinkt | 00 Brands / Northdocks / ND Website & CI Progress ([1MSx9J46aSdw9HtYA0Q3EBLyKgMyD-pF6](https://drive.google.com/open?id=1MSx9J46aSdw9HtYA0Q3EBLyKgMyD-pF6)) | 01.04.2020 | | | | | | Gleiche Größe wie ND-0006/ND-0007, keine eigene Katalog-ID |
| PREVIEW_Transitions.mp4 | [10_mjKVwbdgoxm5kjNo8MUxU73Pq_dmee](https://drive.google.com/open?id=10_mjKVwbdgoxm5kjNo8MUxU73Pq_dmee) (ND-0490) | ND Website & CI Progress | 06.05.2020 | MP4 H.264 | 1920x1080 | 30 | 13,33 s | nein | Demo der Logo-Transition zwischen Clips (Kölner Dom, Streaming-Szene), mit Ton (Musik ungeklärt: nie im Angebot, Regel 6/11) |
| Komp 1.mp4 | [10ZHKACrY4Sbh9jTci5MtixZxiY3FfNBi](https://drive.google.com/open?id=10ZHKACrY4Sbh9jTci5MtixZxiY3FfNBi) (ND-0542) | ND Website & CI Progress | 08.04.2020 | MP4 H.264 | 1920x1080 | 30 | 40,0 s | nein | Kein Intro: Website-Mockup-Animation 2020 (NORTHDOCKS / DIGITAL TWIN in Oswald, Orange-Brücke) |

Farben in den Intros (gemessen): Hintergrund #505050 (Solid-Fassungen und v002) oder #000000 (V001), Logo und Wipe #FFFFFF. Kein Orange in den Intros.

Nicht Northdocks-Intros (in der Assets-Liste als Logo-Animation geführt): `CorporateDesignShowcase.mp4` ([1iLjjJMKQVdUVzfGboiir6iTnV0EQ-d4A](https://drive.google.com/open?id=1iLjjJMKQVdUVzfGboiir6iTnV0EQ-d4A) (ND-0492), 1920x1080, 60 fps, 156 s) und `CorporateDesignPresetDesigner.mp4` ([1k-Iw5gN3jVBLg8JAeUMQZgVFrWrlFzGr](https://drive.google.com/open?id=1k-Iw5gN3jVBLg8JAeUMQZgVFrWrlFzGr) (ND-0491), 1920x1052, 25 fps, 167 s), beide 2024. Das sind Unreal-Bildschirmaufnahmen eines CI-Preset-Werkzeugs für Kunden-CIs (Farben/Logos in der VR-Szene), keine Northdocks-CI.

## Submarken (Logo-Animationen 2023)

Quelle: `Verticals-Logos.zip` / „4 Erscheinungsbilder / <Marke> / Animationen“. Dieselben Dateinamen und Größen liegen im Drive unter 00 Brands / <Marke> / Animationen (08.01.2024) und als Dubletten unter Messe-Material / Bilder / Logos (27.03.2024).

| Datei | Drive-ID (00 Brands) | Marke | Auflösung | fps | Dauer | Alpha | Ton | Inhalt |
|---|---|---|---|---|---|---|---|---|
| meditrain_screen.mp4 | [1rfSzJGkxBxA0mqRiY65PvlHgc8ost4W9](https://drive.google.com/open?id=1rfSzJGkxBxA0mqRiY65PvlHgc8ost4W9) (MED-0037) | MediTrain VR | 1920x1080 | 30 | 6,87 s | nein | nein | Bildmarke baut sich auf, Logo weiß auf #63B1E5 (Styleguide-Primär). Logo-Box x 378–1542, 1164 px breit, passt nicht in einen 1080er Center-Crop |
| meditrain_vr_360.mp4 | [1rdNpgBaxcfxWdtSDykpH7o1amdr6kYvh](https://drive.google.com/open?id=1rdNpgBaxcfxWdtSDykpH7o1amdr6kYvh) (MED-0038) | MediTrain VR | 4096x2048 | 30 | 6,0 s | nein | nein | 360°-Fassung (equirectangular), Logo klein mittig auf Schwarz, für VR-Brillen |
| nextfactory_screen.mp4 | [1rrMsVXyfDiBkf1-LDRPjWPIr6KaQPGfK](https://drive.google.com/open?id=1rrMsVXyfDiBkf1-LDRPjWPIr6KaQPGfK) (NFVR-0025) | Next Factory VR | 1920x1080 | 30 | 7,97 s | nein | nein | Rauten-Animation, Logo weiß auf #EBE945 (gemessen #E9E844) |
| nextfactory_vr_360.mp4 | [1rqfY0rX2Ftgxi1xLWFnV0PfApC4Sshj3](https://drive.google.com/open?id=1rqfY0rX2Ftgxi1xLWFnV0PfApC4Sshj3) (NFVR-0026) | Next Factory VR | 4096x2048 | 30 | 5,13 s | nein | nein | 360°-Fassung |
| spearhead_screen.mp4 | [1sYlQdIjCCImunIdCvxV4WT2frZeaMf4G](https://drive.google.com/open?id=1sYlQdIjCCImunIdCvxV4WT2frZeaMf4G) (SPVR-0036) | Spearhead VR | 1920x1080 | 30 | 4,0 s | nein | nein | 3D-Bildmarke (silbern) + „SPEARHEAD VR“ hoch, auf #ABBDCA |
| spearhead_2D_screen.mp4 | [1sZVUAPW2NHOpxrDLGHi7UJxNRxi4Luy1](https://drive.google.com/open?id=1sZVUAPW2NHOpxrDLGHi7UJxNRxi4Luy1) (SPVR-0035) | Spearhead VR | 1920x1080 | 30 | 4,0 s | nein | nein | Flache Bildmarke weiß, hoch, auf #ABBDCA |
| spearhead_vr_360.mp4 | [1sYE5_CoZGOH_GlfNPigxmVff3yPdMhhM](https://drive.google.com/open?id=1sYE5_CoZGOH_GlfNPigxmVff3yPdMhhM) (SPVR-0037) | Spearhead VR | 4096x2048 | 30 | 4,0 s | nein | nein | 360°-Fassung |
| storywalx_screen.mp4 | [1ulpuZ-jN0Xnnn5-rgn0Od0QCJJ3lxwdA](https://drive.google.com/open?id=1ulpuZ-jN0Xnnn5-rgn0Od0QCJJ3lxwdA) (SW-0023) | storywalx | 1920x1080 | 30 | 3,93 s | nein | nein | Schriftzug schreibt sich entlang gestrichelter Linie, weiß auf #7771B2 |
| storywalx_vr_360.mp4 | [1ujtNg3-AGtS1qEgVaoTBimWjJG-aJuiD](https://drive.google.com/open?id=1ujtNg3-AGtS1qEgVaoTBimWjJG-aJuiD) (SW-0024) | storywalx | 4096x2048 | 30 | 6,0 s | nein | nein | 360°-Fassung |
| impsolutions_screen.mp4 / _VR_360.mp4 | [1r_1rchjfcTXJMyEj8Nvy10uSlxXzK1p-](https://drive.google.com/open?id=1r_1rchjfcTXJMyEj8Nvy10uSlxXzK1p-) (IMP-0022) / [1raiO6SU7qTd0tJFR9ZKxTvCyTDJSWeVH](https://drive.google.com/open?id=1raiO6SU7qTd0tJFR9ZKxTvCyTDJSWeVH) (IMP-0021) | IMP Solutions (nicht beauftragt) | 1920x1080 / 4096x2048 | 30 | 4,0 / 6,0 s | nein | nein | Schwarz auf Grün #09EF09 |

Die Hintergrundfarben der Animationen entsprechen den Styleguide-Primärfarben (#63B1E5, #EBE945, #ABBDCA, #7771B2), nicht den abweichenden Farben einzelner Logo-SVGs.

## Keine Intros gefunden für

FirefighterVR, StrahlenschutzVR / RadiationProtectionVR, GodView, BMA Trainer, Meta-dom. Für FirefighterVR gibt es nur den Splash-Screen `FFVRSplash.png` ([1yokbwtpV21PitUf5f-IM5vYSfDwgG8z0](https://drive.google.com/open?id=1yokbwtpV21PitUf5f-IM5vYSfDwgG8z0) (FFVR-0248), 600x200, Logo weiß/rot #E1001A auf #505050, Asset-Library / Logos & Splash Screens).

## Hinweise für den Einsatz in Reels (9:16)

- Northdocks Intro A/B und LgogTransition2x: Center-Crop 1080 px breit (x 420–1500) enthält das Logo vollständig. Danach auf 1080x1920 mit #505050 auffüllen. Der weiße Schräg-Wipe wird dabei angeschnitten.
- Submarken-Screens: Bei Next Factory, Spearhead und storywalx reicht ein Center-Crop. Bei MediTrain VR (1164 px) und IMP (1254 px) besser skalieren (etwa 0,9) und auf Fläche in Hintergrundfarbe setzen.
- Für Overlays mit Transparenz fehlen Alpha-Renderings. Für Northdocks ist das AEP vorhanden. Für die Submarken gibt es keine Projektdatei im Drive.
