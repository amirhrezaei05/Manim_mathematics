[CmdletBinding()]
param(
    [ValidateSet("l", "m", "h", "k")]
    [string]$Quality = "h",

    [switch]$NoPreview,

    [switch]$OpenFolder
)

$ErrorActionPreference = "Stop"

# Resolve the project root from this script, so it works from any current directory.
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$SceneFile = Join-Path $ProjectRoot "scenes\trigonometry\question_001.py"
$SceneName = "TrigQuestion001FA"
$MediaDir = Join-Path $ProjectRoot "media"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " Persian Trigonometry — Manim Render" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "Project : $ProjectRoot"
Write-Host "Scene   : $SceneName"
Write-Host "Quality : $Quality"
Write-Host ""

if (-not (Test-Path $SceneFile)) {
    throw "Scene file not found: $SceneFile"
}

# Prefer the project's virtual environment; otherwise use Python on PATH.
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (Test-Path $VenvPython) {
    $Python = $VenvPython
    Write-Host "[OK] Using project virtual environment." -ForegroundColor Green
}
else {
    $PythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $PythonCommand) {
        throw "Python was not found. Install Python 3.10–3.12 or create .venv in the project root."
    }
    $Python = $PythonCommand.Source
    Write-Host "[INFO] Using Python from PATH." -ForegroundColor Yellow
}

# Check Manim before starting a potentially long render.
& $Python -c "import manim; print('Manim', manim.__version__)"
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Manim is missing from this Python environment." -ForegroundColor Yellow
    Write-Host "Install it with:" -ForegroundColor Yellow
    Write-Host "  & `"$Python`" -m pip install manim" -ForegroundColor White
    exit 1
}

# Confirm the Persian font is available to Windows/Pango.
$FontCheck = @'
from manim import Text
try:
    t = Text("آزمون قلم فارسی", font="Vazirmatn")
    print("Vazirmatn font: available")
except Exception as e:
    print("Vazirmatn font: NOT AVAILABLE")
    print(e)
'@
& $Python -c $FontCheck
if ($LASTEXITCODE -ne 0) {
    Write-Warning "Could not verify Vazirmatn. Install the font before rendering for correct Persian text."
}

# Render from project root so media output has a predictable location.
Push-Location $ProjectRoot
try {
    $ManimArgs = @(
        "-m", "manim",
        "--media_dir", $MediaDir,
        "-q", $Quality
    )

    if (-not $NoPreview) {
        $ManimArgs += "-p"
    }

    $ManimArgs += @(
        $SceneFile,
        $SceneName
    )

    Write-Host ""
    Write-Host "[RENDER] Starting Manim..." -ForegroundColor Cyan
    & $Python @ManimArgs

    if ($LASTEXITCODE -ne 0) {
        throw "Manim render failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

# Locate the newest MP4 generated for this scene.
$VideoRoot = Join-Path $MediaDir "videos"
$RenderedVideo = Get-ChildItem -Path $VideoRoot -Filter "$SceneName.mp4" -Recurse -File -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($RenderedVideo) {
    Write-Host ""
    Write-Host "[SUCCESS] Render completed." -ForegroundColor Green
    Write-Host "Video: $($RenderedVideo.FullName)"
    if ($OpenFolder) {
        Invoke-Item $RenderedVideo.DirectoryName
    }
}
else {
    Write-Warning "Manim finished, but the MP4 was not found under $VideoRoot."
    Write-Host "Check Manim's output above for the saved file location."
}
