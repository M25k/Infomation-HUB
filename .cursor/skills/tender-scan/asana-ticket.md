# Asana-Ticket: Bid/No-Bid

Sobald eine Ausschreibung den Kompetenzfilter besteht, **sofort** ein Task anlegen. Das Ticket ist die Entscheidungsakte, kein Stub.

Projekt: `1200346071931886` (Anträge & Ausschreibungen)  
Spalte: **Sammlung** `1200346071931887`  
Name: `Ausschreibung: {Kurz-Titel}, Frist {YYYY-MM-DD}`  
Due date = Angebotsfrist. Assignee `me`, außer der User nennt jemand anderen. Patrick (`732711459534815`) als Follower, wenn er nicht Assignee ist.

Kein Task, wenn derselbe Vorgang schon im Board liegt — dann die bestehende Beschreibung auf dieses Raster **auffüllen**.

Keine Portal-Passwörter, keine AVPQ-Zugangscodes in die Notes.

**Ticket und Paket (Joachim 25.10.2026, übermittelt von One bzw. Förderung):**
- Eine Ausschreibung bekommt **ein** Asana-Ticket mit grobem Status. Unteraufgaben nur für Dinge, die andere Personen tun müssen.
- Details stehen als `.md` im Drive-Ordner der Ausschreibung (inkl. Checkliste; eine Checkliste wird nie als Asana-Unteraufgaben angelegt). Die Ticketbeschreibung ist sauber gegliedert; Referenz: [UKSH-Ticket](https://app.asana.com/1/8864272155433/project/1200346071931886/task/1217328350929037).
- So schnell wie möglich bearbeiten. Joachim bekommt einen kompletten Vorschlag in **einem** Paket: Eignung/Referenzen, Umsetzungskonzept (falls gefordert) und Kalkulation.
- Theoretische Punkte wie Konflikte bei den Mitarbeiterressourcen fallen ganz weg.
- **Keine Bieterfragen**, weil sie Wettbewerber aufmerksam machen. Ist eine Ausschreibung uneindeutig, gilt die für Northdocks günstigere Auslegung.
- **Preise so ansetzen, dass wir gewinnen:** ein fester Tagessatz nach außen; die interne Kalkulation (Puffer, Wiederverwendung, Marge) bleibt intern.

**Inhaltsregel (Joachim 25.10.2026, 17:26, übermittelt von One):** Leasing war nur für eine bestimmte UKSH-Ausschreibung gedacht und gehört nicht in normale Northdocks-Inhalte (Angebote, Tickets, Dokumente), auch nicht als Abgrenzung. Allgemein keine Negativ-Abgrenzungen nach dem Muster „das ist nicht X“: Wir beschreiben nur, was wir anbieten.

## Pflichtblöcke

Jedes Feld ausfüllen. Unbekannt = `offen` (nicht weglassen). Bekanntmachung/XML/PDF lesen, bevor der Task gespeichert wird.

**Quellenrang für Eignung, Wertung, Fristen, Budget:**

1. Auftragsbekanntmachung (Portal-PDF / TED-XML / bund.de-HTML der Vergabestelle)
2. Leistungsbeschreibung, Preisblatt, Bewerbungsbedingungen
3. BKMS/TED-Rohfelder (Titel, CPV, Frist), wenn 1. noch fehlt

Nicht als Quelle: Bidfix, Tender Impulse, dtad, „KI-Kriterien-Analyse“, Such-Snippets. Die dürfen nur den **Fund** (URL) liefern. Kriterien daraus nicht ins Ticket, auch nicht als „zu prüfen“. Bis das amtliche PDF gelesen ist, bleibt das Feld `offen`.

```
ENTSCHEIDUNG
Teilnahme: offen
Empfehlung Scan: einreichen / nicht einreichen / nur mit Partner / klären
Begründung (max. 5 Sätze, Strategie + Machbarkeit + Formalia)
Was fehlt noch, um zu entscheiden:

ECKDATEN
Titel:
Vergabestelle:
Kontakt (Mail/Tel, wenn in der Bekanntmachung):
Verfahren (VgV / UVgO / VOL / VOF; offen / nicht offen):
Art (Dienst / Liefer / Bau):
CPV:
Veröffentlicht:
Angebotsfrist (Datum, Uhrzeit):
Fragenfrist / Bieterfragen bis (nur Info, wir stellen keine Bieterfragen):
Bindefrist:
TED-Nr. / bund.de / Unterlagen-URL:
Erfüllungsort:
Lose (welches Los, andere Lose ignorieren?):
Geschätzter Wert / Budgetdeckel:

GEGENSTAND
Was genau geliefert/entwickelt wird:
Hardware (Stückzahl, Typ) ja/nein:
Software: Katalog / Custom / beides:
Zielgruppe (Profi-Feuerwehr, Klinik, Schule, …):
Laufzeit und Meilensteine:
Offline / Local-Only / Hosting-DE verlangt?:
Sprache der Unterlagen und der Lieferung:

PASSUNG (Kompetenz + Strategie)
Cluster (XR / Meditrain / FFVR / Factory / GodView A / GodView B / Spearhead):
Koffer-Komplettpaket möglich? ja / teilweise / nein:
Was wir schon haben vs. neu bauen:
Produktanker (FirefighterVR, Meditrain, StrahlenschutzVR, GodView, …):
Strategie-Fit (Meditrain-Koffer und FFVR zuerst): hoch / mittel / niedrig

EIGNUNG / FORMALIA
AVPQ verlangt? (Zertifikatnummer intern bekannt, Code nicht ins Ticket)
Referenzen, die wir nennen dürfen:
Bietergemeinschaft / Unterauftrag / Eignungsleihe: erlaubt / verboten / offen
Nebenangebote: erlaubt / unzulässig / offen
Lieferort vs. Kiel:

RISIKEN
Preis/Budget (zu eng wie UniBw 300 k€?):
Custom-Falle (einmalig, kein Katalog):
Spezialhardware / Eye-Tracking:
Sonstiges:

NÄCHSTER SCHRITT
Unterlagen gezogen: ja/nein
Wer entscheidet Teilnahme (Datum):
Wenn ja: Eignung vs. Zuschlag trennen, Claims nur aus claims.md
```

In Asana Task-**Beschreibung** (`html_notes`) mit denselben Überschriften (`h2`) und Listen. Links als `<a href="...">`.

**Kommentare** (`add_comment`): nur Klartext-Feld `text`, keine HTML-Tags. Sonst erscheint der Quelltext im Feed.
