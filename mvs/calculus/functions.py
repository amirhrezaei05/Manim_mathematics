"""Function transformations and graph helpers."""
from manim import *
from ..graphs import plot_function
from ..theme import FUNCTION, PRIMARY

def transformed_function(axes, fn, x_range, color=FUNCTION):
    return plot_function(axes, fn, x_range, color=color)

def function_family(axes, functions, x_range, colors=None):
    """Create a VGroup of curves from a list of callables."""
    colors = colors or [FUNCTION, PRIMARY, RED, GREEN]
    curves = [
        plot_function(axes, fn, x_range, color=colors[i % len(colors)])
        for i, fn in enumerate(functions)
    ]
    return VGroup(*curves)
