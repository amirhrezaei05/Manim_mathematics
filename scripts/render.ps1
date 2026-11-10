param(
    [Parameter(Mandatory=$true, Position=0)]
    [ValidateSet("derivative", "functions", "riemann", "limits", "persian_text_test")]
    [string]$Scene,

    [ValidateSet("l", "m", "h", "k")]
    [string]$Quality = "l",

    [switch]$Portrait
)

$ErrorActionPreference = "Stop"

$sceneFile = Join-Path "scenes" ($Scene + ".py")
if (-not (Test-Path $sceneFile)) {
    throw "Scene file not found: $sceneFile"
}

if (-not (Test-Path ".\.venv\Scripts\manim.exe")) {
    throw "Virtual environment not found. Run .\scripts\setup.ps1 first."
}

$config = if ($Portrait) { "config/portrait.cfg" } else { "config/manim.cfg" }
$qualityFlag = "-pq$Quality"

Write-Host "Rendering $Scene | quality=$Quality | portrait=$Portrait" -ForegroundColor Cyan

& .\.venv\Scripts\manim.exe --config_file $config $qualityFlag $sceneFile $(
    switch ($Scene) {
        "derivative" { "DerivativeIntuition" }
        "functions" { "FunctionTransformations" }
        "riemann" { "RiemannSum" }
        "limits" { "LimitApproach" }
        "persian_text_test" { "PersianTextTest" }
    }
)

if ($LASTEXITCODE -ne 0) {
    throw "Manim render failed. Check the error output above."
}

Write-Host "`nRender completed. Find MP4 files under media/videos/." -ForegroundColor Green
