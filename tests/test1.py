from olivattam import *
result = analyze_image("img_path", num_colors=9,rgb=True)
for color in result:
    print(color)
    print(rgb_to_hex(color))
    print(rgb_to_hsl(color))
print(type(result))