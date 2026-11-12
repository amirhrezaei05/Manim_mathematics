"""Geometric measurement annotations."""
from manim import Line, MathTex, VGroup, WHITE, GREEN, DOWN, UP, LEFT, RIGHT


def measured_segment(point_a, point_b, label_tex, color=GREEN, label_direction=None):
    """Return a highlighted segment and its length label."""
    a = point_a.get_center() if hasattr(point_a, "get_center") else point_a
    b = point_b.get_center() if hasattr(point_b, "get_center") else point_b
    segment = Line(a, b, color=color, stroke_width=5)
    if label_direction is None:
        midpoint = (a + b) / 2
        # Pick a side of the segment that is generally away from the origin.
        label_direction = DOWN if midpoint[1] < -0.1 else UP
    label = MathTex(label_tex, color=WHITE).scale(0.62)
    label.next_to(segment, label_direction, buff=0.16)
    return VGroup(segment, label)
