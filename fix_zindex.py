dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the z-index so the pseudo-elements render in front of the global background
content = content.replace("z-index: -1;", "z-index: 0;")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Z-index fixed.")
