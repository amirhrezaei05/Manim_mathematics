"""Reusable coordinate systems and graph helpers."""
from manim import *
from .theme import MUTED, GRID, FUNCTION

def make_axes(
    x_range=(-3, 3, 1),
    y_range=(-2, 6, 1),
    x_length=7.2,
    y_length=4.6,
    numbers=True,
):
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        axis_config={
            "color": MUTED,
            "stroke_width": 2,
            "include_numbers": numbers,
            "font_size": 22,
        },
        tips=True,
    )
    return axes

def plot_function(axes, fn, x_range, color=FUNCTION, stroke_width=4):
    return axes.plot(
        fn,
        x_range=x_range,
        color=color,
        stroke_width=stroke_width,
    )

def point_on_graph(axes, fn, x, color, radius=0.085):
    return Dot(axes.c2p(x, fn(x)), color=color, radius=radius)

def secant_through(axes, fn, x0, x1, color, stroke_width=3):
    """Line segment joining two points on a graph."""
    return Line(
        axes.c2p(x0, fn(x0)),
        axes.c2p(x1, fn(x1)),
        color=color,
        stroke_width=stroke_width,
    )

def tangent_at(axes, fn, derivative, x0, span=1.0, color=None, stroke_width=3):
    """Draw a local tangent segment using the supplied derivative."""
    from .theme import PRIMARY
    slope = derivative(x0)
    y0 = fn(x0)
    return axes.plot(
        lambda x: y0 + slope * (x - x0),
        x_range=[x0 - span, x0 + span],
        color=color or PRIMARY,
        stroke_width=stroke_width,
    )
