# Register a monthly full Asana JSON backup (Windows Task Scheduler).
# Token stays in %USERPROFILE%\.config\northdocks\asana-pat.txt — never in the task XML.

$ErrorActionPreference = "Stop"

$taskName = "Northdocks Asana Backup"
$repo = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$script = Join-Path $PSScriptRoot "export_asana.py"
$tokenFile = Join-Path $env:USERPROFILE ".config\northdocks\asana-pat.txt"
$outDir = Join-Path $env:USERPROFILE "Documents\Northdocks-Backups\asana"
$logDir = Join-Path $outDir "logs"

if (-not (Test-Path $script)) {
    throw "Exporter missing: $script"
}
if (-not (Test-Path $tokenFile)) {
    throw "Create a Personal Access Token and save it to $tokenFile first."
}

New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$pyCmd = Get-Command py -ErrorAction SilentlyContinue
$pyArgs = @("-3")
if (-not $pyCmd) {
    $pyCmd = Get-Command python -ErrorAction SilentlyContinue
    $pyArgs = @()
}
if (-not $pyCmd) {
    throw "Python launcher not found (py or python)."
}

$pyArgLine = if ($pyArgs) { ($pyArgs -join " ") + " " } else { "" }
$wrapper = @"
`$log = Join-Path '$logDir' ('asana-backup-' + (Get-Date -Format 'yyyy-MM-dd') + '.log')
`$env:PYTHONIOENCODING = 'utf-8'
& '$($pyCmd.Source)' $pyArgLine'$script' --out '$outDir' *>&1 | Tee-Object -FilePath `$log
exit `$LASTEXITCODE
"@
$wrapperPath = Join-Path $logDir "run-asana-backup.ps1"
Set-Content -Path $wrapperPath -Value $wrapper -Encoding UTF8

# New-ScheduledTaskTrigger has no -Monthly on this Windows build; schtasks does.
$tr = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File `"$wrapperPath`""
$create = schtasks /Create /TN $taskName /SC MONTHLY /D 1 /ST 03:00 /TR $tr /F /RL LIMITED
if ($LASTEXITCODE -ne 0) {
    throw "schtasks failed: $create"
}

Write-Host "Scheduled '$taskName' monthly on the 1st at 03:00."
Write-Host "Output: $outDir"
Write-Host "Logs:   $logDir"
