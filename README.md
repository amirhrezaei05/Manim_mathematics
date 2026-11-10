# Manim Mathematical Studio

A reusable Manim Community Edition project for producing polished mathematical teaching videos.
Designed for Windows 11, Persian narration, a presenter + digital-board + Manim workflow, and a colorful mathematical-visualization aesthetic.

## 1. What is included

- Central visual theme and semantic colors.
- Reusable graph, point, secant, tangent, formula and annotation helpers.
- Reusable modules for functions, derivatives, limits and integrals.
- Four ready-to-render demonstration scenes.
- Landscape (16:9) and portrait (9:16) configurations.
- PowerShell setup and rendering scripts.
- A Persian storyboard and narration outline for the first derivative episode.

## 2. Requirements

Recommended:
- Windows 10/11, 64-bit
- Python 3.12 (64-bit)
- FFmpeg
- MiKTeX (LaTeX distribution)
- Manim Community Edition 0.19.0

Install FFmpeg and MiKTeX separately. During MiKTeX setup, enable automatic installation of missing packages. Reopen PowerShell after installing them.

## 3. Install

Extract this folder somewhere convenient, for example `D:\Projects\Manim_Mathematical_Studio`.

Open PowerShell in the project folder:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\setup.ps1
```

Or manually:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
manim checkhealth
```

If `py -3.12` is not found, install Python 3.12 from python.org and enable the Python Launcher.

## 4. Render your first scene

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Fast preview:

```powershell
.\scripts\render.ps1 derivative
```

High-quality landscape render:

```powershell
.\scripts\render.ps1 derivative -Quality h
```

Portrait preview:

```powershell
.\scripts\render.ps1 derivative -Portrait
```

Other scene names:
- `functions`
- `riemann`
- `limits`

You can also call Manim directly:

```powershell
manim --config_file config/manim.cfg -pql scenes/derivative.py DerivativeIntuition
```

Manim quality options:
- `-ql`: low quality preview
- `-qm`: medium
- `-qh`: high quality
- `-qk`: 4K (slow; use only when needed)

## 5. Project structure

```text
Manim_Mathematical_Studio/
├── config/
│   ├── manim.cfg
│   └── portrait.cfg
├── mvs/
│   ├── theme.py
│   ├── typography.py
│   ├── layouts.py
│   ├── graphs.py
│   └── calculus/
│       ├── functions.py
│       ├── derivatives.py
│       ├── limits.py
│       └── integrals.py
├── scenes/
│   ├── derivative.py
│   ├── functions.py
│   ├── riemann.py
│   └── limits.py
├── scripts/
│   ├── setup.ps1
│   └── render.ps1
├── episode_workspace/
│   └── episode_01_derivative/
│       ├── storyboard_fa.md
│       └── narration_fa.md
├── media/
│   ├── audio/
│   ├── images/
│   └── exports/
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. How to create a new episode

1. Copy the closest scene from `scenes/`.
2. Rename the class and file.
3. Import reusable objects from `mvs`.
4. Keep the mathematical logic in the scene, and reusable visual logic in `mvs`.
5. Put Persian narration in `episode_workspace/` and record it separately.
6. Render Manim clips and assemble them with camera footage and digital-board recording in your editor.

Example:

```python
from manim import *
from mvs.theme import *
from mvs.graphs import make_axes, plot_function

class MyNewLesson(Scene):
    def construct(self):
        self.camera.background_color = BG
        axes = make_axes(x_range=[-3, 3, 1], y_range=[-2, 8, 2])
        graph = plot_function(axes, lambda x: x**2, [-2.5, 2.5])
        self.play(Create(axes), Create(graph))
        self.wait()
```

## 7. Persian text and equations

Use `MathTex` for equations and mathematical notation. Persian text rendering can depend on font shaping and right-to-left support in the local rendering stack. For dependable production:
- Record Persian narration separately.
- Add Persian captions, titles and lower-thirds in DaVinci Resolve.
- If you want Persian text inside Manim, test the included `persian_text_test.py` scene after installing a Persian font such as Vazirmatn. Verify letter joining, RTL ordering and punctuation on your computer.

Do not build a whole episode around Persian text rendering until that test passes.

## 8. Landscape and portrait

- Landscape: 1920×1080, 16:9.
- Portrait: 1080×1920, 9:16.

Portrait is a separate composition, not just a crop. Reposition graphs and equations for vertical safe areas. Use the portrait render script as a starting point and adjust the scene's layout where necessary.

## 9. Rendering and exports

Manim stores generated files in `media/videos/`. The render script copies the selected MP4 to `media/exports/` for convenient access.

Keep your source scenes and assets; do not edit the rendered MP4 as your only copy.

## 10. Framework design rules

- Colors have consistent mathematical meaning.
- Mathematical functions and parameters should be configurable.
- Keep reusable visual objects in `mvs/`.
- Keep episode-specific storytelling in `scenes/`.
- Use low quality while developing; high quality only for final output.
- Keep narration, camera footage and digital-board recording separate from Manim.
