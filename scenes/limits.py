from manim import *
from mvs.theme import BG, FUNCTION, PRIMARY, MOVING, RESULT
from mvs.graphs import make_axes, plot_function
from mvs.calculus.limits import approaching_point
from mvs.layouts import top_title

class LimitApproach(Scene):
    """A point on y=x^2 approaches x=2."""

    def construct(self):
        self.camera.background_color = BG
        axes = make_axes(
            x_range=[0, 4, 1], y_range=[0, 17, 4],
            x_length=7.0, y_length=4.6
        )
        fn = lambda x: x**2
        graph = plot_function(axes, fn, [0, 4], color=FUNCTION)
        x = ValueTracker(0.5)
        dot = approaching_point(axes, fn, x)
        limit_line = DashedLine(
            axes.c2p(2, 0), axes.c2p(2, 4),
            color=RESULT, stroke_width=2
        )
        title = top_title(r"\text{Approaching a limit}")

        self.play(Write(title), Create(axes), Create(graph))
        self.play(FadeIn(dot), Create(limit_line))
        self.play(x.animate.set_value(1.98), run_time=4, rate_func=smooth)
        answer = MathTex(r"\lim_{x\to 2}x^2=4", color=RESULT).to_edge(DOWN)
        self.play(Write(answer))
        self.wait(2)
