import glob
from PIL import Image

for f in glob.glob(r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\assets\*.png"):
    try:
        img = Image.open(f).convert("RGBA")
        c = img.getpixel((0,0))
        print(f"{f.split('\\')[-1]}: {c}")
    except Exception as e:
        print(f"{f}: {e}")
