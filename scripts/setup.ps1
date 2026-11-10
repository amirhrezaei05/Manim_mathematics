$ErrorActionPreference = "Stop"

Write-Host "=== Manim Mathematical Studio setup ===" -ForegroundColor Cyan

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    throw "Python Launcher 'py' not found. Install Python 3.12 (64-bit) and enable the launcher."
}

py -3.12 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host "`nChecking Manim installation..." -ForegroundColor Cyan
& .\.venv\Scripts\manim.exe checkhealth

Write-Host "`nSetup complete. Activate with: .\.venv\Scripts\Activate.ps1" -ForegroundColor Green
Write-Host "Then render: .\scripts\render.ps1 derivative"
