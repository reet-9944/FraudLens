import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the mobile override that collapses browse-grid to 1 column
content = re.sub(r'\.browse-grid\s*{\s*grid-template-columns:\s*1fr;\s*}', '', content)
content = content.replace('.browse-grid { grid-template-columns: 1fr; gap: 1.5rem; }', '')

# Restore background: white; to .browse-img if it's missing (just to be exactly like feec8b8b2c^)
old_img_css = """.browse-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 1.5rem;
    transition: transform 0.5s ease;
}"""
new_img_css = """.browse-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 1.5rem;
    background: white;
    transition: transform 0.5s ease;
}"""
content = content.replace(old_img_css, new_img_css)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed browse grid.")
