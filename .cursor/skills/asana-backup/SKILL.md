---
name: asana-backup
description: Monthly full Asana workspace JSON backup for Northdocks. Exports every project (active and archived) plus comments via the REST API. Use when the user asks for an Asana backup, JSON export, monthly Asana dump, or to register the scheduled backup.
---

# Asana backup

Complete workspace dump. Not the UI “Export → JSON” permalink (login-gated, no comments). Not Asana’s official graph / organization export — those need **Enterprise**; this workspace is below Business (portfolios already 402).

## What it writes

Each run creates `Documents/Northdocks-Backups/asana/YYYY-MM-DD/`:

- `manifest.json` — counts, failures, API-call total
- `workspace.json`, `teams.json`, `users.json`, `tags.json`
- `projects/{gid}-{name}.json` — project, sections, tasks, subtasks, stories (comments), attachment **metadata**

Attachment **files** are not downloaded (URLs expire). HR/FiBu notes and customer phones stay in these files — **never Git, never a shared Drive folder**.

Keep the last **12** dated folders. Token never in the repo.

## Token (once)

1. Asana → profile photo → **Settings → Apps → Personal access tokens → Create token**.
2. Save the token only to `%USERPROFILE%\.config\northdocks\asana-pat.txt` (one line) or user-level env `ASANA_PAT`.
3. Do not paste the token into chat, Git, or Asana comments.

## Commands

Test one project first (Anträge & Ausschreibungen):

```text
py -3 .cursor/skills/asana-backup/scripts/export_asana.py --project 1200346071931886
```

Full workspace (75+ active, 100+ archived; tens of minutes):

```text
py -3 .cursor/skills/asana-backup/scripts/export_asana.py
```

Register the monthly Windows task (1st of month, 03:00, logged-on user):

```text
powershell -ExecutionPolicy Bypass -File .cursor/skills/asana-backup/scripts/register-monthly-task.ps1
```

## Rules

- Default output is under the user Documents folder, not this repo.
- Do not commit backup JSON. Do not put dumps in `knowledge/`.
- If a run fails partway, `manifest.json` lists `failures`; re-run is safe (overwrites that date).
- Cursor MCP is the wrong tool for this dump (pagination + comments + unattended schedule).
