from manim import *
from mvs.theme import BG, PRIMARY, MOVING, FUNCTION, RESULT, WHITE
from mvs.graphs import make_axes, plot_function
from mvs.calculus.derivatives import secant_pair
from mvs.layouts import top_title, bottom_formula

class DerivativeIntuition(Scene):
    """Secant line approaches tangent line for f(x)=x^2 at x=1."""

    def construct(self):
        self.camera.background_color = BG
        axes = make_axes(
            x_range=[0, 3, 1], y_range=[0, 8, 2],
            x_length=7.2, y_length=4.4
        ).shift(DOWN * 0.12)
        curve = plot_function(axes, lambda x: x**2, [0, 2.75])

        a = 1.0
        h = ValueTracker(1.15)
        fixed_dot = Dot(axes.c2p(a, a**2), color=PRIMARY, radius=0.09)

        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(a + h.get_value(), (a + h.get_value())**2),
                color=MOVING, radius=0.09
            )
        )
        secant = always_redraw(
            lambda: axes.plot(
                lambda x: 1 + (2 + h.get_value()) * (x - 1),
                x_range=[0.15, 2.75],
                color=PRIMARY,
                stroke_width=3.5
            )
        )

        heading = top_title(r"\text{From secant to tangent}")
        quotient = MathTex(
            r"m_{\mathrm{secant}}="
            r"\frac{f(1+h)-f(1)}{h}=2+h"
        ).scale(0.78).to_edge(DOWN, buff=0.3)

        self.play(Write(heading))
        self.play(Create(axes), run_time=1.2)
        self.play(Create(curve), run_time=1.4)
        self.play(FadeIn(fixed_dot), FadeIn(moving_dot))
        self.play(Create(secant), Write(quotient))
        self.wait(0.8)
        self.play(h.animate.set_value(0.035), run_time=4.5, rate_func=smooth)

        result = MathTex(
            r"f'(1)=\lim_{h\to 0}(2+h)=2",
            color=RESULT
        ).scale(0.9).to_edge(DOWN, buff=0.3)
        self.play(Transform(quotient, result))
        self.wait(2)
