import os
from PIL import Image

assets_dir = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\assets"
max_size = 600 # 600px is plenty for these cards

for filename in os.listdir(assets_dir):
    if filename.endswith(".png"):
        filepath = os.path.join(assets_dir, filename)
        img = Image.open(filepath)
        
        # Convert to RGBA if not already (for transparency)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        width, height = img.size
        
        if width > max_size or height > max_size:
            if width > height:
                new_width = max_size
                new_height = int(max_size * height / width)
            else:
                new_height = max_size
                new_width = int(max_size * width / height)
            
            print(f"Resizing {filename} from {width}x{height} to {new_width}x{new_height}")
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img.save(filepath, format="PNG", optimize=True)
        else:
            print(f"Optimizing {filename} without resizing")
            img.save(filepath, format="PNG", optimize=True)

print("Optimization complete.")
