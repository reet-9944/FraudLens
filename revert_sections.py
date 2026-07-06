import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Restore .hiw-step CSS
if ".hiw-step {" not in content and ".hiw-step {{" not in content:
    hiw_step_css = """
.hiw-step {{
    display: flex;
    align-items: center;
    gap: 4rem;
    margin-bottom: 5rem;
}}
.hiw-step.reverse {"""
    content = content.replace(".hiw-step.reverse {", hiw_step_css)

# 2. Fix .browse-img CSS
old_img_css = """.browse-img-wrapper {{
    width: 100%;
    height: 300px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    margin-bottom: 1.5rem;
    background: #080312; /* Deep dark background to blend with tech images */
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}}
.browse-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: scale(1.25); /* Zoom in to eliminate baked-in white borders */
    transition: transform 0.5s ease;
}}
.browse-card:hover .browse-img {{
    transform: scale(1.35); /* Subtle zoom effect on hover */
}}"""

new_img_css = """.browse-img {{
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 1.5rem;
    transition: transform 0.5s ease;
}}
.browse-card:hover .browse-img {{
    transform: scale(1.05); /* Subtle zoom effect on hover */
}}"""
content = content.replace(old_img_css, new_img_css)

# 3. Strip the wrapper divs from the HTML
content = re.sub(r'<div class="browse-img-wrapper">\s*<img([^>]+)>\s*</div>', r'<img\1>', content)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Reverted sections.")
