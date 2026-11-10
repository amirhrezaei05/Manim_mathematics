from manim import *
from mvs.theme import BG, FUNCTION, PRIMARY, MOVING, WHITE
from mvs.graphs import make_axes, plot_function
from mvs.layouts import top_title

class FunctionTransformations(Scene):
    """Show how vertical translation changes y=x^2 into y=x^2+k."""

    def construct(self):
        self.camera.background_color = BG
        axes = make_axes(
            x_range=[-3, 3, 1], y_range=[-1, 9, 2],
            x_length=7.3, y_length=4.8
        )
        tracker = ValueTracker(0)
        base = plot_function(axes, lambda x: x**2, [-2.7, 2.7], color=FUNCTION)

        shifted = always_redraw(
            lambda: axes.plot(
                lambda x: x**2 + tracker.get_value(),
                x_range=[-2.7, 2.7],
                color=MOVING,
                stroke_width=4
            )
        )
        formula = always_redraw(
            lambda: MathTex(
                rf"y=x^2+{tracker.get_value():.1f}",
                color=MOVING
            ).scale(0.85).to_edge(DOWN)
        )
        heading = top_title(r"\text{Vertical transformations}")

        self.play(Write(heading), Create(axes))
        self.play(Create(base))
        self.play(Create(shifted), Write(formula))
        self.play(tracker.animate.set_value(3), run_time=3)
        self.play(tracker.animate.set_value(-1), run_time=3)
        self.wait(1)
