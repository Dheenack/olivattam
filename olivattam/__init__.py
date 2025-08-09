from .extractor import extract_colors
from .utils import format_color_output
from .converter import *

def analyze_image(image_path, num_colors=5,all_fmt=False,rgb=False):
    colors = extract_colors(image_path, num_colors)
    if all_fmt==True:
        return [format_color_output(c) for c in colors]
    elif rgb==True:
        return colors
    else:
        return [rgb_to_hex(c) for c in colors]
    
