def format_color_output(rgb):
    from .converter import rgb_to_hex, rgb_to_hsl, rgb_to_rgba
    return {
        'rgb': rgb,
        'hex': rgb_to_hex(rgb),
        'hsl': rgb_to_hsl(rgb),
        'rgba': rgb_to_rgba(rgb)
    }
