import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Restore CSS
old_img_css = """.browse-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 1.5rem;
    background: white;
    transition: transform 0.5s ease;
}
.browse-card:hover .browse-img {
    transform: scale(1.05); /* Subtle zoom effect on hover */
}"""

new_img_css = """.browse-img-wrapper {
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
}
.browse-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: scale(1.25); /* Zoom in to eliminate baked-in borders */
    transition: transform 0.5s ease;
}
.browse-card:hover .browse-img {
    transform: scale(1.35); /* Subtle zoom effect on hover */
}"""

if old_img_css in content:
    content = content.replace(old_img_css, new_img_css)

# 2. Restore HTML wrappers
# We need to find all instances of <label for="modal-toggle-X" class="browse-card"> (or similar)
# and wrap the <img ... class="browse-img" ...> inside <div class="browse-img-wrapper"> ... </div>

# Regular expression to wrap the img tags inside .browse-card or .browse-card.extra-card
# Pattern looks for <img src="..." class="browse-img" onerror="...">
content = re.sub(r'(<img src="data:image/png[^>]+class="browse-img"[^>]*>)', r'<div class="browse-img-wrapper">\n                    \1\n                </div>', content)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored browse-img-wrapper.")
