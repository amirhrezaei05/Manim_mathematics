"""Reusable derivative visualization primitives."""
from manim import *
from ..graphs import point_on_graph, tangent_at, secant_through
from ..theme import PRIMARY, MOVING

def secant_pair(axes, fn, x0, x1):
    return (
        point_on_graph(axes, fn, x0, PRIMARY),
        point_on_graph(axes, fn, x1, MOVING),
        secant_through(axes, fn, x0, x1, PRIMARY),
    )

def tangent_object(axes, fn, derivative, x0, span=1.0):
    return tangent_at(axes, fn, derivative, x0, span=span, color=PRIMARY)

def difference_quotient_tex():
    return MathTex(
        r"\frac{f(a+h)-f(a)}{h}"
    )
