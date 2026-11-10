"""Centralized visual identity. Keep semantic color meanings consistent."""
from manim import *

BG = "#10151F"
BG_ALT = "#171F2D"
WHITE = "#F5F7FA"
MUTED = "#AAB4C3"
GRID = "#394454"

# Semantic mathematics palette
PRIMARY = "#58C4DD"       # primary object / fixed reference
MOVING = "#FC6255"        # moving or changing quantity
FUNCTION = "#FFFF00"      # function graph
RESULT = "#83C167"        # final result / verified conclusion
PURPLE = "#9A72AC"        # auxiliary construction
ORANGE = "#FF9F43"        # secondary emphasis

def brand_scene(scene):
    scene.camera.background_color = BG
