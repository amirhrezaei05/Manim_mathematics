# Persian portrait Manim scene — Trigonometry Question 001

## Design
- Portrait 9:16 composition (1080 × 1920, 30 fps)
- Cinematic dark navy background with a subtle scientific grid
- Persian prose uses Vazirmatn and is laid out RTL by Pango
- Mathematical expressions are separate `MathTex` objects and retain standard notation
- Diagram and coordinate panel are positioned inside the portrait safe area

## Requirements
- Python 3.10–3.12 recommended
- Manim Community Edition
- LaTeX installation supported by Manim
- Vazirmatn font installed on the operating system

Install:
```powershell
python -m pip install manim
```

Install Vazirmatn:
- Download the Vazirmatn font family from its official GitHub repository.
- Install the font in Windows (right-click the `.ttf` files → Install).
- Restart the terminal/editor after installation.

## Render
From this folder:
```powershell
manim -pql scenes/trigonometry/question_001.py TrigQuestion001FA
```
For a high-quality render:
```powershell
manim -pqh scenes/trigonometry/question_001.py TrigQuestion001FA
```

The scene sets portrait camera dimensions itself. If Persian letters appear disconnected,
check that Vazirmatn is installed and that Manim's Pango text renderer is available.

## RTL rule
Do not reverse Persian strings manually. Pango performs bidirectional layout and glyph
shaping. Keep Persian prose in `Text`; keep equations and symbols in `MathTex`.
Mixing Persian prose and equations in a single text object is intentionally avoided.


## Automatic PowerShell render (Windows)

From the project root:
```powershell
.\\render.ps1
```
This uses high quality (`-Quality h`) and opens the rendered video when complete.

Quick low-quality preview:
```powershell
.\\render.ps1 -Quality l
```

Render without automatically opening the video:
```powershell
.\\render.ps1 -Quality h -NoPreview
```

Open the output folder after rendering:
```powershell
.\\render.ps1 -Quality h -NoPreview -OpenFolder
```

You can also call the script directly:
```powershell
.\\scripts\\render.ps1 -Quality h
```
