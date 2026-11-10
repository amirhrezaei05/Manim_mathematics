"""Riemann-sum helpers."""
from manim import *
from ..theme import PRIMARY

def riemann_rectangles(axes, graph, x_range, dx, color=PRIMARY,
                       input_sample_type="left", fill_opacity=0.55):
    return axes.get_riemann_rectangles(
        graph,
        x_range=x_range,
        dx=dx,
        input_sample_type=input_sample_type,
        color=color,
        fill_opacity=fill_opacity,
        stroke_width=0.7,
    )
