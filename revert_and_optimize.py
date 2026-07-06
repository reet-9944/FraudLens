import os
import glob
from PIL import Image

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"
assets_dir = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\assets"

# 1. Revert references in dashboard.py
with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(".webp", ".png")
content = content.replace("data:image/webp;base64", "data:image/png;base64")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Resize PNGs to reduce size while preserving alpha channel
for png_path in glob.glob(os.path.join(assets_dir, "*.png")):
    img = Image.open(png_path)
    # Resize to max 400px for massive size savings without losing visual fidelity for a 300px card
    img.thumbnail((400, 400), Image.Resampling.LANCZOS)
    # Save as PNG to perfectly preserve the alpha transparency layer
    img.save(png_path, format="PNG", optimize=True)
    img.close()
    
# 3. Delete broken WebP files
for webp_path in glob.glob(os.path.join(assets_dir, "*.webp")):
    os.remove(webp_path)

print("Reverted to PNGs, resized them to optimize payload, and deleted broken WebPs.")
