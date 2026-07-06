import os
from PIL import Image

assets_dir = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\assets"
dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

for filename in os.listdir(assets_dir):
    if filename.endswith(".png"):
        png_path = os.path.join(assets_dir, filename)
        webp_filename = filename.replace(".png", ".webp")
        webp_path = os.path.join(assets_dir, webp_filename)
        
        img = Image.open(png_path)
        # Quality 30 is extremely aggressive for massive file size reduction
        img.save(webp_path, format="WEBP", quality=30, method=6)
        
        # Free file handle before removing
        img.close()
        os.remove(png_path)
        print(f"Converted {filename} to WebP.")

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(".png", ".webp")
content = content.replace("data:image/png;base64", "data:image/webp;base64")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Dashboard updated.")
