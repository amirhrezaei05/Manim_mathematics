"""Typography helpers. MathTex is recommended for formulas."""
from manim import *
from .theme import WHITE, MUTED

def formula(tex, color=WHITE, scale=1.0):
    return MathTex(tex, color=color).scale(scale)

def title(tex, color=WHITE, scale=0.85):
    return MathTex(tex, color=color).scale(scale).to_edge(UP, buff=0.35)

def caption(text, color=WHITE, font_size=30):
    """Latin text helper. For Persian, validate RTL shaping locally first."""
    return Text(text, color=color, font_size=font_size)
