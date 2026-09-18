# nextfactoryvr.com

Canonical: https://nextfactoryvr.com/  
Repo: `C:\Githup\WWW-next-factory-vr`

Rolle: Industrie-/Anlagentraining auf Scan/Twin (Technikum, Chemiepark, Instandhaltung). **Custom-Projekte**, kein FirefighterVR-Katalog. Infinity ist der Actemium-/VINCI-Workspace-Name, nicht die Northdocks-Produktmarke.

## Ist-Struktur (Live 17.09.2026)

SvelteKit, DE/EN auf derselben URL. Nav: Leistungen / Projekte / Kontakt (Anker auf der Startseite). Eigenständige Case-URLs:

| URL | Case |
|---|---|
| `/` | Hero, Logos, Features, Workflow, zwei Featured Cases, Referenzkarten, Security, Zitate, Kontakt |
| `/project/merck/` | Merck Chemikanten / Technikum |
| `/project/actemium/` | Actemium Rollenförderer / Infinity |
| `/project/currenta/` | Currenta Technikum Explorer |
| `/project/bayer/` | Sprinklerwartung Hi-Fog Bayer/Henkel |
| `/imprint/` | Impressum |
| `/privacy/` | Datenschutz |

`/projects` ist **404** — Projekte liegen als Anker `#projekte` plus die vier Case-Seiten.

Öffentliche Kundenleiste live: Bayer, Merck, BASF, Evonik, Henkel, Infraserv, Actemium. In [claims.md](../claims.md) zusätzlich **Currenta** und **Vinci** — die fehlen im Ticker.

Security-Text nennt **RWE** und **Framatome**. Intern: FirefighterVR-Paket **Feuerlöscher**. RWE: nur Probeanmeldung 03/2021, **keine PO**. Framatome: Lieferantenanlage 09/2024. Factory nur als Randfall (z. B. Sprinklerwartung), kein Twin-Vollprojekt.

Kontakt live: Mail **kontakt@northdocks.com** (richtig). Telefon **+49 (0) 2173 9996713** (FirefighterVR — falsch für diese Domain). Impressum: USt-IdNr. **DE 305 886 984** (falsch; kanonisch **DE298519758**). Erreichbarkeit 9:00–13:00 fehlt. CTA „Antwort in 24 Stunden“ nicht in der KB belegt.

Hero-Headset trägt das **Infinity**-Logo (Kunde Actemium). Copy spricht von einem „training catalog“ und platziert 4× / 75 % / 0 / 100 % als Plattform-KPIs.

## Soll bei Anpassungen

1. **Marke:** Lead ist Next Factory VR = Headset-Training an der gescannten Kundenanlage. Infinity nur auf dem Actemium-Case. Kein zweites öffentliches Produkt.
2. **Nachbarn klar trennen:** GodView = Browser-Twin (Link [godview.solutions](https://godview.solutions/)), nicht die Trainingsapp. FirefighterVR = Werkfeuer / Feuerlöscher-Katalog (Link [firefightervr.de](https://firefightervr.de/)). Sprinkler Bayer/Henkel darf als industrieller Brandschutz-Case bleiben, ist aber nicht das Leitversprechen.
3. **RWE/Framatome** nicht als Twin-Referenz. Streichen oder eine Zeile Brandschutz/Feuerlöscher mit Verweis auf FirefighterVR.
4. **Currenta:** Explorer-Case behalten. Kein FA-Gesamt, kein einzelnes Los, keine Vermischung mit Planspiel/GodView Bürrig als „das Currenta-Projekt“.
5. **Claims:** „4× Knowledge Transfer, 75 % Retention 72h“ nur am **Merck-Case**, als Case-Angabe, nicht als Meta-Studie und nicht als Home-KPI. Keine „0 %“ / „100 %“ / „unprecedented“ / „revolutionize“.
6. **Technik öffentlich:** Offline im Schulungsbetrieb, Pico Device Manager, Standalone (Pico), Fallback PC/Tablet/Mobile, Unreal Engine 5 / OpenXR, Laserscan → interaktives Anlagenmodell. Nicht: Unity als Leit-Engine, ElevenVoice, Plugin-Listen, Hosting intern.
7. **Kontakt:** kontakt@northdocks.com, Telefon Hub **+49 (0) 2173 9996715**, Mo.–Fr. 9:00–13:00. Nicht 6713. 24-h-Antwort nur, wenn der Vertrieb das ausdrücklich hält.
8. **Recht:** Impressum wie [_shared.md](_shared.md) — USt-IdNr. **DE298519758**, HRB 76844 Düsseldorf, GF Joachim Perschbacher und Patrick D. Reschke.
9. **DE/EN:** Voll spiegeln. Footer-Reste („HOME“, „Ready for VR?“) auf DE-Seiten entfernen.
10. **Logo-Leiste:** Currenta und Vinci ergänzen (schon öffentlich). Keine neuen Case-Seiten für BASF/Evonik/Infraserv nur wegen des Tickers.

## Öffentlich sagbar

- Kundenleiste: Bayer, Merck, BASF, Evonik, Henkel, Currenta, Infraserv, Vinci, Actemium
- Cases: Merck Technikum, Actemium Infinity / Förderband, Currenta Technikum Explorer, Sprinkler Bayer/Henkel
- Offline, Pico MDM, Standalone, Fallback PC/Tablet
- Kundenstimmen, die zum Case passen (Actemium Breiner, VINCI Bäcker nur auf Actemium/VINCI, Henkel Thein auf Sprinkler)

## Nicht auf diese Site

- Spearhead/Defense-Zahlen, TMA, Kosovo
- FFVR-Katalog (23 Module, Kofferpreise) als Factory-Standard
- Interne Currenta-/Merck-/Henkel-Volumina
- RWE oder Framatome als Digital-Twin-Vollprojekt
- Craftsmen, Philips, ElevenVoice
- Holcim, APG, BIT Gendorf als neue öffentliche Cases ohne extra Freigabe
- Self-Testimonials („Northdocks VR-Team“)

## Briefing

Live-Abgleich 17.09.2026: Canvas `nextfactory-site-briefing.canvas.tsx` (Diagnose, Soll-IA, Cases, Copy, Rollout).
