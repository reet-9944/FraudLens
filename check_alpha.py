from PIL import Image
import os

img_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\assets\hero_collage_2.webp"
if os.path.exists(img_path):
    img = Image.open(img_path)
    print(f"Mode: {img.mode}")
    print(f"Has alpha: {'A' in img.mode or (img.info.get('transparency', None) is not None)}")
else:
    print("File not found.")
