from PIL import Image
import os

img_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\assets\feature_ai.png"
if os.path.exists(img_path):
    img = Image.open(img_path).convert("RGBA")
    print(f"Size: {img.size}")
    corners = [(0,0), (img.width-1, 0), (0, img.height-1), (img.width-1, img.height-1)]
    for idx, c in enumerate(corners):
        print(f"Corner {idx} color: {img.getpixel(c)}")
else:
    print("Not found")
