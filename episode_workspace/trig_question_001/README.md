# Trigonometry Question 001

## Add to the existing repository

Copy the contents of this patch into the root of `Manim_mathematics`, preserving the directory structure. These files add two reusable geometry/trigonometry modules, one portrait scene, the complete solution, storyboard, narration, and a PowerShell render helper.

## Render

From PowerShell at the repository root:

```powershell
.\scripts\render_trig_question_001.ps1 -Quality l
```

Use `m` for a medium render and `h` for the final 1080x1920 render:

```powershell
.\scripts\render_trig_question_001.ps1 -Quality h
```

Equivalent direct command:

```powershell
.\.venv\Scripts\python.exe -m manim --config_file config/portrait.cfg -pqh scenes/trigonometry/question_001.py TrigQuestion001
```

Requirements: the repository's existing ManimCE 0.19.0 environment, FFmpeg, and a working LaTeX installation for MathTex.

## Notes

- The scene uses the existing `mvs.theme` palette.
- It deliberately avoids Persian text inside Manim because the repository README correctly warns that RTL shaping must be tested locally. Use the supplied Persian narration and add Persian captions in your editor.
- The identity is `cos(2x) = 1 - 2 sin²(x)`. Omitting the coefficient 2 would make the solution incorrect.
- The solution angles are listed in one complete revolution, `0 <= x < 2π`.
