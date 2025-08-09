from PIL import Image
from collections import Counter

def extract_colors(image_path, num_colors=5):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((100, 100))  # Resize for faster processing
    pixels = list(image.getdata())
    most_common = Counter(pixels).most_common(num_colors)
    return [color for color, _ in most_common]