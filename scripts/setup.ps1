
$ErrorActionPreference = "Stop"

# Always work from the project root
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

$Python = ".\.venv\Scripts\python.exe"

Write-Host "=== Manim Mathematical Studio Setup ===" -ForegroundColor Cyan

# Verify Python 3.12
if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    throw "Python Launcher not found."
}

py -3.12 --version
if ($LASTEXITCODE -ne 0) {
    throw "Python 3.12 is not installed."
}

# Create environment if needed
if (-not (Test-Path $Python)) {
    py -3.12 -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to create virtual environment."
    }
}

# Install dependencies
& $Python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    throw "Pip upgrade failed."
}

& $Python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    throw "Dependency installation failed."
}

# Verify Manim
Write-Host "`nChecking Manim installation..." -ForegroundColor Cyan

& $Python -m manim checkhealth
if ($LASTEXITCODE -ne 0) {
    throw "Manim health check failed."
}

Write-Host "`nSetup completed successfully!" -ForegroundColor Green
Write-Host "Activate: .\.venv\Scripts\Activate.ps1"
Write-Host "Render: .\scripts\render.ps1 derivative"
