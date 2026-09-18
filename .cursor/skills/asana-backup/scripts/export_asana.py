#!/usr/bin/env python3
"""Monthly full-workspace Asana backup for Northdocks.

Walks every project (active + archived) via the REST API and writes JSON
outside Git. Official graph / organization exports need Enterprise and are
not available on this workspace.

Token (never print, never commit):
  1. env ASANA_PAT or ASANA_ACCESS_TOKEN
  2. %USERPROFILE%\\.config\\northdocks\\asana-pat.txt

No third-party packages.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

API = "https://app.asana.com/api/1.0"
WORKSPACE = "8864272155433"
TOKEN_FILE = Path.home() / ".config" / "northdocks" / "asana-pat.txt"
DEFAULT_OUT = Path.home() / "Documents" / "Northdocks-Backups" / "asana"

PROJECT_FIELDS = ",".join(
    [
        "name",
        "notes",
        "html_notes",
        "archived",
        "color",
        "created_at",
        "modified_at",
        "due_on",
        "start_on",
        "completed",
        "completed_at",
        "owner.name",
        "team.name",
        "permalink_url",
        "privacy_setting",
        "default_view",
        "icon",
        "members.name",
        "custom_field_settings.custom_field.name",
        "custom_field_settings.custom_field.resource_subtype",
        "current_status.title",
        "current_status.color",
        "current_status.text",
    ]
)

TASK_FIELDS = ",".join(
    [
        "name",
        "notes",
        "html_notes",
        "completed",
        "completed_at",
        "completed_by.name",
        "assignee.name",
        "assignee.email",
        "due_on",
        "due_at",
        "start_on",
        "start_at",
        "created_at",
        "modified_at",
        "permalink_url",
        "resource_subtype",
        "parent.gid",
        "parent.name",
        "memberships.section.name",
        "memberships.project.gid",
        "custom_fields.name",
        "custom_fields.display_value",
        "custom_fields.type",
        "custom_fields.enum_value.name",
        "tags.name",
        "followers.name",
        "dependencies.gid",
        "dependents.gid",
        "attachments.gid",
        "attachments.name",
        "attachments.created_at",
        "attachments.host",
        "num_subtasks",
    ]
)

STORY_FIELDS = ",".join(
    [
        "created_at",
        "created_by.name",
        "type",
        "resource_subtype",
        "text",
        "html_text",
    ]
)

USER_FIELDS = "name,email,resource_type"
TAG_FIELDS = "name,color,permalink_url"


def load_token() -> str:
    for key in ("ASANA_PAT", "ASANA_ACCESS_TOKEN"):
        value = (os.environ.get(key) or "").strip()
        if value:
            return value
    if TOKEN_FILE.is_file():
        value = TOKEN_FILE.read_text(encoding="utf-8").strip()
        if value:
            return value
    raise SystemExit(
        "No Asana token. Create a Personal Access Token in Asana -> Settings -> "
        "Apps, then save it to "
        f"{TOKEN_FILE} or set ASANA_PAT."
    )


def slug(name: str, gid: str) -> str:
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", (name or "project").strip())
    base = re.sub(r"-{2,}", "-", base).strip("-")[:80] or "project"
    return f"{gid}-{base}"


class Asana:
    def __init__(self, token: str, pause: float = 0.12) -> None:
        self.token = token
        self.pause = pause
        self.calls = 0

    def get(self, path: str, params: dict | None = None) -> dict:
        query = urllib.parse.urlencode(params or {}, doseq=True)
        url = f"{API}{path}"
        if query:
            url = f"{url}?{query}"
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
                "Asana-Enable": "new_project_templates,new_goal_memberships",
            },
        )
        for attempt in range(8):
            try:
                if self.pause:
                    time.sleep(self.pause)
                with urllib.request.urlopen(req, timeout=120) as resp:
                    self.calls += 1
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")
                if exc.code == 429 or exc.code >= 500:
                    wait = 10 * (attempt + 1)
                    retry_after = exc.headers.get("Retry-After")
                    if retry_after:
                        try:
                            wait = max(wait, int(float(retry_after)))
                        except ValueError:
                            pass
                    time.sleep(wait)
                    continue
                raise SystemExit(f"Asana {exc.code} {path}: {body[:400]}") from exc
            except urllib.error.URLError as exc:
                if attempt == 7:
                    raise SystemExit(f"Asana network error {path}: {exc}") from exc
                time.sleep(5 * (attempt + 1))
        raise SystemExit(f"Asana gave up on {path}")

    def pages(self, path: str, params: dict | None = None) -> list:
        rows: list = []
        query = dict(params or {})
        query.setdefault("limit", 100)
        while True:
            payload = self.get(path, query)
            rows.extend(payload.get("data") or [])
            nxt = payload.get("next_page") or {}
            offset = nxt.get("offset")
            if not offset:
                return rows
            query["offset"] = offset


def dump_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def list_projects(api: Asana, workspace: str, include_archived: bool) -> list[dict]:
    seen: dict[str, dict] = {}
    flags = [False]
    if include_archived:
        flags.append(True)
    for archived in flags:
        rows = api.pages(
            "/projects",
            {
                "workspace": workspace,
                "archived": "true" if archived else "false",
                "opt_fields": "name,archived,modified_at,team.name,permalink_url",
            },
        )
        for row in rows:
            seen[row["gid"]] = row
    return list(seen.values())


def export_task_tree(
    api: Asana,
    task: dict,
    include_stories: bool,
    cache: dict[str, dict],
) -> dict:
    gid = task["gid"]
    if gid in cache:
        return cache[gid]
    row = dict(task)
    if include_stories:
        row["stories"] = api.pages(
            f"/tasks/{gid}/stories",
            {"opt_fields": STORY_FIELDS},
        )
    subtasks = []
    if int(task.get("num_subtasks") or 0) > 0:
        children = api.pages(
            f"/tasks/{gid}/subtasks",
            {"opt_fields": TASK_FIELDS},
        )
        subtasks = [
            export_task_tree(api, child, include_stories, cache) for child in children
        ]
    row["subtasks"] = subtasks
    cache[gid] = row
    return row


def export_project(
    api: Asana,
    project: dict,
    include_stories: bool,
) -> dict:
    gid = project["gid"]
    detail = api.get(
        f"/projects/{gid}",
        {"opt_fields": PROJECT_FIELDS},
    )["data"]
    sections = api.pages(
        f"/projects/{gid}/sections",
        {"opt_fields": "name,created_at"},
    )
    tasks = api.pages(
        f"/tasks",
        {"project": gid, "opt_fields": TASK_FIELDS},
    )
    cache: dict[str, dict] = {}
    tree = [export_task_tree(api, task, include_stories, cache) for task in tasks]
    return {
        "project": detail,
        "sections": sections,
        "tasks": tree,
        "task_count": len(tree),
        "object_count": len(cache),
    }


def prune_old_runs(root: Path, keep: int) -> list[str]:
    if keep <= 0 or not root.is_dir():
        return []
    runs = sorted(
        [p for p in root.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name)],
        reverse=True,
    )
    removed = []
    for stale in runs[keep:]:
        for child in sorted(stale.rglob("*"), reverse=True):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                child.rmdir()
        stale.rmdir()
        removed.append(stale.name)
    return removed


def main() -> int:
    parser = argparse.ArgumentParser(description="Export all Asana projects as JSON.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Backup root")
    parser.add_argument("--workspace", default=WORKSPACE)
    parser.add_argument("--project", action="append", default=[], help="Limit to project GID(s)")
    parser.add_argument("--no-archived", action="store_true")
    parser.add_argument("--no-stories", action="store_true")
    parser.add_argument("--keep", type=int, default=12, help="Dated run folders to keep")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    token = load_token()
    api = Asana(token)
    run_dir = args.out / args.date
    projects_dir = run_dir / "projects"
    started = datetime.now(timezone.utc)

    print(f"Backup root: {run_dir}", flush=True)
    if args.project:
        projects = [{"gid": gid, "name": gid} for gid in args.project]
    else:
        print("Listing projects...", flush=True)
        projects = list_projects(api, args.workspace, include_archived=not args.no_archived)
        print(f"Found {len(projects)} projects", flush=True)

    workspace = api.get(f"/workspaces/{args.workspace}", {"opt_fields": "name,is_organization"})["data"]
    teams = api.pages(
        f"/workspaces/{args.workspace}/teams",
        {"opt_fields": "name"},
    )
    users = api.pages(
        f"/users",
        {"workspace": args.workspace, "opt_fields": USER_FIELDS},
    )
    tags = api.pages(
        f"/tags",
        {"workspace": args.workspace, "opt_fields": TAG_FIELDS},
    )
    dump_json(run_dir / "workspace.json", workspace)
    dump_json(run_dir / "teams.json", teams)
    dump_json(run_dir / "users.json", users)
    dump_json(run_dir / "tags.json", tags)

    failures: list[dict] = []
    index: list[dict] = []
    for i, project in enumerate(projects, start=1):
        gid = project["gid"]
        name = project.get("name") or gid
        print(f"[{i}/{len(projects)}] {name}", flush=True)
        try:
            payload = export_project(api, project, include_stories=not args.no_stories)
            exported_name = payload["project"].get("name") or name
            path = projects_dir / f"{slug(exported_name, gid)}.json"
            dump_json(path, payload)
            index.append(
                {
                    "gid": gid,
                    "name": exported_name,
                    "archived": payload["project"].get("archived"),
                    "team": (payload["project"].get("team") or {}).get("name"),
                    "task_count": payload["task_count"],
                    "object_count": payload["object_count"],
                    "file": str(path.relative_to(run_dir)).replace("\\", "/"),
                }
            )
        except SystemExit as exc:
            failures.append({"gid": gid, "name": name, "error": str(exc)})
            print(f"  FAILED: {exc}", flush=True)

    finished = datetime.now(timezone.utc)
    manifest = {
        "exported_at": started.isoformat(),
        "finished_at": finished.isoformat(),
        "workspace": workspace,
        "project_count": len(index),
        "failed_count": len(failures),
        "api_calls": api.calls,
        "include_archived": not args.no_archived,
        "include_stories": not args.no_stories,
        "projects": index,
        "failures": failures,
    }
    dump_json(run_dir / "manifest.json", manifest)
    removed = prune_old_runs(args.out, args.keep)
    if removed:
        print(f"Pruned old runs: {', '.join(removed)}", flush=True)
    print(
        f"Done. {len(index)} projects, {len(failures)} failed, {api.calls} API calls -> {run_dir}",
        flush=True,
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
