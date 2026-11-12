"""Reusable unit-circle visualization component for ManimCE."""
from __future__ import annotations

import numpy as np
from manim import Circle, Dot, Line, MathTex, VGroup, ORIGIN, LEFT, RIGHT, UP, DOWN, WHITE, BLUE, RED


class UnitCircle(VGroup):
    """A geometrically scaled unit circle with coordinate helpers.

    `radius` is the displayed radius in Manim scene units. Mathematical
    coordinates remain unit-circle coordinates in [-1, 1].
    """

    def __init__(self, radius: float = 2.0, axis_extension: float = 1.22, **kwargs):
        super().__init__(**kwargs)
        self.radius = float(radius)
        self.circle = Circle(radius=self.radius, color=WHITE, stroke_width=2.6)
        self.x_axis = Line(
            LEFT * self.radius * axis_extension,
            RIGHT * self.radius * axis_extension,
            color=BLUE,
            stroke_width=1.8,
        )
        self.y_axis = Line(
            DOWN * self.radius * axis_extension,
            UP * self.radius * axis_extension,
            color=BLUE,
            stroke_width=1.8,
        )
        self.add(self.x_axis, self.y_axis, self.circle)

    def point_at_angle(self, theta: float) -> np.ndarray:
        center = self.circle.get_center()
        return center + self.radius * np.array([np.cos(theta), np.sin(theta), 0.0])

    def make_point(self, theta: float, color=RED, dot_radius: float = 0.075) -> Dot:
        return Dot(self.point_at_angle(theta), radius=dot_radius, color=color)

    def radius_line(self, theta: float, color=RED, width: float = 3.0) -> Line:
        return Line(self.circle.get_center(), self.point_at_angle(theta), color=color, stroke_width=width)

    def projection_lines(self, theta: float, color=BLUE) -> VGroup:
        p = self.point_at_angle(theta)
        center = self.circle.get_center()
        x_projection = center + np.array([p[0] - center[0], 0.0, 0.0])
        y_projection = center + np.array([0.0, p[1] - center[1], 0.0])
        return VGroup(
            Line(p, x_projection, color=color, stroke_width=2, stroke_opacity=0.9),
            Line(p, y_projection, color=color, stroke_width=2, stroke_opacity=0.9),
        )

    def coordinate_label(self, theta: float, tex: str, direction=UP) -> MathTex:
        return MathTex(tex, color=WHITE).scale(0.48).next_to(
            self.point_at_angle(theta), direction, buff=0.12
        )
