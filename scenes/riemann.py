from manim import *
from mvs.theme import BG, FUNCTION, PRIMARY, RESULT
from mvs.graphs import make_axes, plot_function
from mvs.calculus.integrals import riemann_rectangles
from mvs.layouts import top_title

class RiemannSum(Scene):
    """Compare left-endpoint Riemann sums with the area under x^2."""

    def construct(self):
        self.camera.background_color = BG
        axes = make_axes(
            x_range=[0, 3, 1], y_range=[0, 9, 3],
            x_length=7.0, y_length=4.6
        ).shift(DOWN * 0.15)
        fn = lambda x: x**2
        graph = plot_function(axes, fn, [0, 2.7], color=FUNCTION)
        title = top_title(r"\text{Approximating area with rectangles}")

        self.play(Write(title), Create(axes), Create(graph))
        for n in [4, 10, 24]:
            rects = riemann_rectangles(
                axes, graph, [0, 2.5], dx=2.5/n,
                color=PRIMARY, input_sample_type="left"
            )
            self.play(FadeIn(rects), run_time=1.1)
            self.wait(0.5)
            if n != 24:
                self.play(FadeOut(rects), run_time=0.5)
        integral = MathTex(
            r"\int_0^{2.5}x^2\,dx",
            color=RESULT
        ).scale(0.9).to_edge(DOWN)
        self.play(Write(integral))
        self.wait(2)
