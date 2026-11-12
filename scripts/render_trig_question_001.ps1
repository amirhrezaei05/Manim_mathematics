param(
    [ValidateSet("l", "m", "h")]
    [string]$Quality = "h"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    throw "Project venv not found. Run .\scripts\setup.ps1 first."
}

$SceneFile = "scenes/trigonometry/question_001.py"
$ConfigFile = "config/portrait.cfg"
$SceneName = "TrigQuestion001"

& $Python -m manim --config_file $ConfigFile "-q$Quality" $SceneFile $SceneName
if ($LASTEXITCODE -ne 0) {
    throw "Manim render failed with exit code $LASTEXITCODE"
}

$Video = Get-ChildItem "media\videos\question_001" -Recurse -Filter "*.mp4" |
    Where-Object { $_.Name -match "TrigQuestion001" } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if (-not $Video) {
    # Manim's default directory is based on the scene filename.
    $Video = Get-ChildItem "media\videos" -Recurse -Filter "*.mp4" |
        Where-Object { $_.FullName -match "question_001" } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
}

if (-not $Video) {
    throw "Render completed but the MP4 could not be located."
}

$ExportDir = Join-Path $ProjectRoot "media\exports"
New-Item -ItemType Directory -Force -Path $ExportDir | Out-Null
$Destination = Join-Path $ExportDir "trig_question_001_portrait.mp4"
Copy-Item $Video.FullName $Destination -Force
Write-Host "Exported: $Destination"
