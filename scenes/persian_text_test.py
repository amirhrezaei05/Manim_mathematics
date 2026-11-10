from manim import *
from mvs.theme import BG

class PersianTextTest(Scene):
    """Test local Persian font shaping and right-to-left display."""
    def construct(self):
        self.camera.background_color = BG
        # Install a Persian-capable font (e.g. Vazirmatn) and change font name below.
        sample = Text(
            "آزمایش نمایش متن فارسی",
            font="Vazirmatn",
            font_size=44
        )
        self.play(Write(sample))
        self.wait(2)
