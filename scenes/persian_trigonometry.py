
from manim import *
import numpy as np


class PersianTrigonometry(Scene):
    def construct(self):

        # Background
        self.camera.background_color = "#10141F"

        # Title
        title = Text(
            "مقدمه‌ای بر مثلثات",
            font="Vazirmatn",
            font_size=40,
            color=WHITE,
        )

        title.to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        # Coordinate system
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={
                "color": GREY_B,
                "include_numbers": False,
            },
        )

        self.play(Create(axes))

        # Unit circle
        circle = Circle(
            radius=2,
            color=BLUE,
            stroke_width=3,
        )

        self.play(Create(circle))

        # Angle
        theta = ValueTracker(0.3)

        # Moving point
        point = always_redraw(
            lambda: Dot(
                axes.c2p(
                    np.cos(theta.get_value()),
                    np.sin(theta.get_value()),
                ),
                color=YELLOW,
                radius=0.08,
            )
        )

        # Radius vector
        radius = always_redraw(
            lambda: Line(
                axes.c2p(0, 0),
                axes.c2p(
                    np.cos(theta.get_value()),
                    np.sin(theta.get_value()),
                ),
                color=YELLOW,
                stroke_width=4,
            )
        )

        self.play(
            FadeIn(point),
            Create(radius),
        )

        # Equation
        equation = MathTex(
            r"P(\theta)=(\cos\theta,\sin\theta)"
        )

        equation.to_edge(DOWN)

        self.play(Write(equation))

        # Rotation
        self.play(
            theta.animate.set_value(2 * PI),
            run_time=6,
            rate_func=linear,
        )

        self.wait(2)
