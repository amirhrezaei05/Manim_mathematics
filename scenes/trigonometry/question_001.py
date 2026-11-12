"""Persian, portrait, cinematic solution for trigonometry question 001.

Persian prose is rendered with Pango via Manim Text (automatic bidirectional
layout and character shaping). Mathematical expressions remain separate MathTex
objects so their conventional left-to-right notation is never reversed.
"""
from __future__ import annotations

import numpy as np
from manim import *

# Explicit portrait canvas: 9:16 composition.
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30

BG = "#07111F"
WHITE = "#F2F6FC"
MUTED = "#A8B7C9"
CYAN = "#55D6E8"
GOLD = "#FFC857"
CORAL = "#FF7A90"
GREEN = "#8BE0B0"
PANEL = "#101F31"
GRID = "#20354B"

FONT_FA = "Vazirmatn"


def fa(text: str, size=30, color=WHITE, weight=NORMAL, width=7.5):
    """Persian text. Do not reverse the string: Pango handles RTL shaping."""
    mob = Text(
        text,
        font=FONT_FA,
        font_size=size,
        color=color,
        weight=weight,
        alignment="right",
        line_spacing=0.9,
    )
    if mob.width > width:
        mob.scale_to_fit_width(width)
    return mob


def formula(tex: str, size=0.9, color=WHITE, max_width=7.7):
    mob = MathTex(tex, color=color).scale(size)
    if mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    return mob


class TrigQuestion001FA(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add_background_design()
        self.opening()
        self.algebra()
        self.roots_and_angles()
        self.unit_circle_and_triangle()
        self.compare_sides()
        self.final_answer()

    def add_background_design(self):
        # Subtle scientific grid, safely behind all foreground content.
        lines = VGroup()
        for x in np.arange(-4.0, 4.01, 0.5):
            lines.add(Line([x, -8, 0], [x, 8, 0], stroke_color=GRID, stroke_width=0.45, stroke_opacity=0.34))
        for y in np.arange(-7.5, 7.51, 0.5):
            lines.add(Line([-4.5, y, 0], [4.5, y, 0], stroke_color=GRID, stroke_width=0.45, stroke_opacity=0.34))
        glow = Circle(radius=3.7, stroke_color=CYAN, stroke_opacity=0.07, stroke_width=18)
        glow.move_to(DOWN * 1.2)
        self.add(lines, glow)

    def section_header(self, number, title):
        num = Text(number, font=FONT_FA, font_size=25, color=CYAN, weight=BOLD)
        title_mob = fa(title, size=31, color=WHITE, weight=BOLD, width=6.4)
        title_mob.next_to(num, RIGHT, buff=0.22)
        group = VGroup(num, title_mob).arrange(RIGHT, buff=0.22)
        group.to_edge(UP, buff=0.68)
        # Small accent rule
        rule = Line(LEFT * 3.65, RIGHT * 3.65, color=CYAN, stroke_width=1.2, stroke_opacity=0.55)
        rule.next_to(group, DOWN, buff=0.24)
        return VGroup(group, rule)

    def show_persian_caption(self, text, y, color=MUTED, size=29):
        caption = fa(text, size=size, color=color, width=7.7)
        caption.move_to([0, y, 0])
        self.play(FadeIn(caption, shift=UP * 0.12), run_time=0.55)
        return caption

    def opening(self):
        eyebrow = fa("ریاضی • مثلثات • حل تشریحی", size=27, color=CYAN, width=7.6)
        eyebrow.move_to([0, 6.25, 0])
        title = fa("طول بزرگ‌ترین ضلع را بیابید", size=43, color=WHITE, weight=BOLD)
        title.move_to([0, 4.85, 0])
        prompt = fa(
            "رأس‌های یک چندضلعی روی دایرهٔ مثلثاتی قرار دارند و جواب‌های معادلهٔ زیر، زاویه‌های متناظر با آن‌ها هستند:",
            size=27, color=MUTED, width=7.7
        )
        prompt.move_to([0, 2.95, 0])
        eq = formula(r"\cos(2x)=2+3\sin x", size=1.05, color=GOLD)
        eq.move_to([0, 1.55, 0])
        condition = fa("در بازهٔ ۰ تا ۲π", size=27, color=CYAN)
        condition.move_to([0, 0.25, 0])
        options = formula(r"1\qquad \sqrt{2}\qquad \sqrt{3}\qquad 2", size=0.78, color=WHITE)
        options.move_to([0, -1.25, 0])
        options_label = fa("گزینه‌ها", size=23, color=MUTED)
        options_label.next_to(options, DOWN, buff=0.32)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(prompt), run_time=0.8)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(condition), FadeIn(options), FadeIn(options_label), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(VGroup(eyebrow, title, prompt, eq, condition, options, options_label)), run_time=0.6)

    def algebra(self):
        header = self.section_header("۰۱", "حل جبری معادله")
        self.play(FadeIn(header))
        caption = self.show_persian_caption("ابتدا از اتحاد زاویهٔ دوبرابر استفاده می‌کنیم:", 4.35)
        steps = [
            (r"\cos(2x)=1-2\sin^2x", "اتحاد کسینوس زاویهٔ دوبرابر", CYAN),
            (r"1-2\sin^2x=2+3\sin x", "جای‌گذاری در معادلهٔ اصلی", WHITE),
            (r"2\sin^2x+3\sin x+1=0", "انتقال همهٔ جمله‌ها به یک طرف", GOLD),
            (r"(2\sin x+1)(\sin x+1)=0", "تجزیهٔ عبارت درجهٔ دوم", GREEN),
        ]
        current = None
        y_positions = [2.75, 1.25, -0.25, -1.75]
        for tex, note, color in steps:
            note_mob = fa(note, size=24, color=MUTED)
            note_mob.move_to([0, y_positions[0] + 0.43, 0])
            eq = formula(tex, size=0.85, color=color, max_width=7.6)
            eq.move_to([0, y_positions[0] - 0.25, 0])
            if current is None:
                self.play(FadeIn(note_mob), Write(eq), run_time=1.25)
            else:
                self.play(FadeOut(current[0]), FadeOut(current[1]), run_time=0.25)
                self.play(FadeIn(note_mob), Write(eq), run_time=1.0)
            current = (note_mob, eq)
            self.wait(1.05)
            y_positions.pop(0)
        self.wait(1.0)
        self.play(FadeOut(header), FadeOut(caption), FadeOut(current[0]), FadeOut(current[1]), run_time=0.6)

    def roots_and_angles(self):
        header = self.section_header("۰۲", "به‌دست‌آوردن زاویه‌ها")
        self.play(FadeIn(header))
        cap = self.show_persian_caption("هر یک از عامل‌ها را برابر صفر قرار می‌دهیم:", 4.25)
        label1 = self.show_persian_caption("حالت اول:", 3.15, size=25)
        r1 = formula(r"\sin x=-\frac{1}{2}", size=1.0, color=CYAN)
        r1.move_to([0, 2.35, 0])
        self.play(Write(r1), run_time=0.8)
        label2 = self.show_persian_caption("حالت دوم:", 1.35, size=25)
        r2 = formula(r"\sin x=-1", size=1.0, color=GOLD)
        r2.move_to([0, 0.55, 0])
        self.play(Write(r2), run_time=0.8)
        interval_label = self.show_persian_caption("در بازهٔ خواسته‌شده:", -0.55, size=25)
        interval = formula(r"0\leq x<2\pi", size=0.78, color=MUTED)
        interval.move_to([0, -1.25, 0])
        self.play(FadeIn(interval), run_time=0.6)
        angles1 = formula(r"x=\frac{7\pi}{6},\quad \frac{11\pi}{6}", size=0.85, color=CYAN)
        angles2 = formula(r"x=\frac{3\pi}{2}", size=0.9, color=GOLD)
        angles1.move_to([0, -2.55, 0])
        angles2.move_to([0, -3.55, 0])
        self.play(Write(angles1), run_time=1.0)
        self.play(Write(angles2), run_time=0.8)
        conclusion = self.show_persian_caption("پس سه زاویهٔ متناظر به‌دست می‌آید.", -4.75, color=GREEN, size=26)
        self.wait(1.5)
        self.wait(1.0)
        self.play(FadeOut(VGroup(header, cap, label1, label2, interval_label, r1, r2, interval, angles1, angles2, conclusion)), run_time=0.6)

    def unit_circle_and_triangle(self):
        header = self.section_header("۰۳", "نمایش هندسی روی دایرهٔ مثلثاتی")
        self.play(FadeIn(header))
        cap = self.show_persian_caption("این سه زاویه را روی دایرهٔ واحد مشخص می‌کنیم:", 4.45, size=27)

        radius = 2.15
        center = np.array([0.0, -0.25, 0.0])
        circle = Circle(radius=radius, color=WHITE, stroke_width=2.6).move_to(center)
        x_axis = Line(center + LEFT * 2.65, center + RIGHT * 2.65, color=MUTED, stroke_width=1.4)
        y_axis = Line(center + DOWN * 2.65, center + UP * 2.65, color=MUTED, stroke_width=1.4)
        self.play(Create(x_axis), Create(y_axis), Create(circle), run_time=1.4)

        angles = [7 * PI / 6, 3 * PI / 2, 11 * PI / 6]
        pts = [center + radius * np.array([np.cos(a), np.sin(a), 0]) for a in angles]
        colors = [CYAN, GOLD, CYAN]
        dots = [Dot(p, radius=0.085, color=c) for p, c in zip(pts, colors)]
        radii = [Line(center, p, color=c, stroke_width=2.8) for p, c in zip(pts, colors)]
        self.play(LaggedStart(*[AnimationGroup(Create(rad), FadeIn(dot)) for rad, dot in zip(radii, dots)], lag_ratio=0.28), run_time=2.0)
        triangle = Polygon(*pts, color=GREEN, stroke_width=3.5, fill_color=GREEN, fill_opacity=0.10)
        self.play(Create(triangle), run_time=1.0)

        # Coordinate labels are placed in a separate, fixed panel below the circle.
        panel = RoundedRectangle(width=7.5, height=2.15, corner_radius=0.18, stroke_color=GRID, fill_color=PANEL, fill_opacity=0.95)
        panel.move_to([0, -4.55, 0])
        coords = VGroup(
            formula(r"P_1\left(-\frac{\sqrt3}{2},-\frac12\right)", size=0.54, color=CYAN, max_width=7.0),
            formula(r"P_2(0,-1)", size=0.58, color=GOLD),
            formula(r"P_3\left(\frac{\sqrt3}{2},-\frac12\right)", size=0.54, color=CYAN, max_width=7.0),
        ).arrange(DOWN, buff=0.18)
        coords.move_to(panel.get_center())
        self.play(FadeIn(panel), FadeIn(coords), run_time=0.9)
        self.wait(2.0)

        self.circle_objects = VGroup(circle, x_axis, y_axis, *radii, *dots, triangle, panel, coords)
        self.play(FadeOut(VGroup(header, cap)), run_time=0.4)

    def compare_sides(self):
        header = self.section_header("۰۴", "مقایسهٔ طول ضلع‌ها")
        self.play(FadeIn(header))
        cap = self.show_persian_caption("در دایرهٔ واحد، فاصلهٔ مرکز تا هر رأس برابر ۱ است.", 4.45, size=26)

        # Retain diagram, scale it slightly and move it upward to reserve space.
        diagram = self.circle_objects.copy()
        diagram.scale(0.83)
        diagram.shift(UP * 0.55)
        self.play(Transform(self.circle_objects, diagram), run_time=0.8)

        f1 = formula(r"P_1P_2=1", size=0.8, color=GOLD)
        f2 = formula(r"P_2P_3=1", size=0.8, color=GOLD)
        f3 = formula(r"P_1P_3=\sqrt3", size=0.9, color=GREEN)
        equations = VGroup(f1, f2, f3).arrange(DOWN, buff=0.45).move_to([0, -5.0, 0])
        self.play(Write(f1), run_time=0.7)
        self.play(Write(f2), run_time=0.7)
        self.play(Write(f3), run_time=0.8)
        self.show_persian_caption("چون رادیکال ۳ از ۱ بزرگ‌تر است، این ضلع بزرگ‌ترین ضلع است.", -6.75, size=23)
        self.wait(1.5)
        self.play(FadeOut(VGroup(header, cap, self.circle_objects, equations)), run_time=0.7)

    def final_answer(self):
        eyebrow = fa("نتیجهٔ نهایی", size=30, color=CYAN, weight=BOLD)
        eyebrow.move_to([0, 3.1, 0])
        sentence = fa("بزرگ‌ترین طول ضلع برابر است با:", size=30, color=WHITE)
        sentence.move_to([0, 1.6, 0])
        answer = formula(r"\boxed{\sqrt3}", size=2.0, color=GREEN)
        answer.move_to([0, -0.1, 0])
        option = fa("گزینهٔ ۳", size=36, color=GOLD, weight=BOLD)
        option.move_to([0, -2.0, 0])
        self.play(FadeIn(eyebrow), run_time=0.6)
        self.play(FadeIn(sentence), run_time=0.6)
        self.play(Write(answer), run_time=1.1)
        self.play(FadeIn(option, shift=UP * 0.15), run_time=0.7)
        self.wait(3.0)
