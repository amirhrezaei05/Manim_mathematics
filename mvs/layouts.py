"""Reusable scene composition helpers."""
from manim import *
from .theme import WHITE, MUTED

def top_title(tex, color=WHITE, scale=0.82):
    return MathTex(tex, color=color).scale(scale).to_edge(UP, buff=0.3)

def bottom_formula(tex, color=WHITE, scale=0.78):
    return MathTex(tex, color=color).scale(scale).to_edge(DOWN, buff=0.28)

def corner_tag(text, color=MUTED):
    tag = Text(text, font_size=22, color=color)
    tag.to_corner(UL, buff=0.3)
    return tag

def side_by_side(left, right, gap=1.0):
    group = VGroup(left, right).arrange(RIGHT, buff=gap)
    return group
