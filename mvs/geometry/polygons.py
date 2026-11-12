"""Polygon construction helpers."""
from manim import Polygon, GREEN


def polygon_from_vertices(vertices, color=GREEN, fill_opacity=0.16, stroke_width=3.5):
    """Build a polygon from Manim-space points or Mobjects."""
    points = [
        vertex.get_center() if hasattr(vertex, "get_center") else vertex
        for vertex in vertices
    ]
    polygon = Polygon(*points, color=color, stroke_width=stroke_width)
    polygon.set_fill(color, opacity=fill_opacity)
    return polygon
