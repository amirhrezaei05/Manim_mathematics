"""Limit visualization primitives."""
from manim import *
from ..theme import PRIMARY, MOVING, RESULT

def approaching_point(axes, fn, tracker, color=MOVING):
    return always_redraw(
        lambda: Dot(
            axes.c2p(tracker.get_value(), fn(tracker.get_value())),
            color=color,
            radius=0.085,
        )
    )

def horizontal_limit_line(axes, y, color=RESULT):
    return DashedLine(
        axes.c2p(axes.x_range[0], y),
        axes.c2p(axes.x_range[1], y),
        color=color,
        stroke_width=2,
    )
