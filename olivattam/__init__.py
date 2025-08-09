from .extractor import extract_colors
from .utils import format_color_output

def analyze_image(image_path, num_colors=5):
    colors = extract_colors(image_path, num_colors)
    return [format_color_output(c) for c in colors]
