import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Restore CSS for wrappers
old_img_css = """.browse-img {{
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 1.5rem;
    background: white;
    transition: transform 0.5s ease;
}}
.browse-card:hover .browse-img {{
    transform: scale(1.05); /* Subtle zoom effect on hover */
}}"""

new_img_css = """.browse-img-wrapper {{
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
    transform: scale(1.25); /* Zoom in to eliminate baked-in borders */
    transition: transform 0.5s ease;
}}
.browse-card:hover .browse-img {{
    transform: scale(1.35); /* Subtle zoom effect on hover */
}}"""

if old_img_css in content:
    content = content.replace(old_img_css, new_img_css)

# 2. Add responsive grid collapse to mobile media queries
# Find the first @media query for .newsletter-card and insert .browse-grid before it
content = content.replace(
    "    .newsletter-card {{",
    "    .browse-grid {{\n        grid-template-columns: 1fr;\n    }}\n    \n    .newsletter-card {{"
)

# Replace the specific one in the second media query
content = content.replace(
    "    .newsletter-card {{ padding: 3rem 5%; text-align: center; }}",
    "    .browse-grid {{ grid-template-columns: 1fr; gap: 1.5rem; }}\n    \n    .newsletter-card {{ padding: 3rem 5%; text-align: center; }}"
)

# 3. Add HTML wrappers
content = re.sub(r'(<img src="data:image/png[^>]+class="browse-img"[^>]*>)', r'<div class="browse-img-wrapper">\n                    \1\n                </div>', content)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored wrapper and responsive grid!")
