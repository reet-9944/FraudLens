import re

file_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix footer background
content = content.replace(
    """<div class="main-footer" style="display: flex; flex-direction: column; background:#1c1726; color:#a3a7b8; padding: 4rem 10%; font-family:'Outfit', sans-serif;">""",
    """<div class="main-footer" style="display: flex; flex-direction: column; background: color-mix(in srgb, var(--background-color) 85%, #1c1726) !important; color:var(--text-color); padding: 4rem 10%; font-family:'Outfit', sans-serif;">"""
)

# Fix footer headers
content = content.replace(
    """<h4 style="color:white; margin:0; letter-spacing:1px; font-weight:700;">FOLLOW US</h4>""",
    """<h4 style="color:var(--text-color); margin:0; letter-spacing:1px; font-weight:700;">FOLLOW US</h4>"""
)
content = content.replace(
    """<h4 style="color:white; margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">CONTACT US</h4>""",
    """<h4 style="color:var(--text-color); margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">CONTACT US</h4>"""
)
content = content.replace(
    """<h4 style="color:white; margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">NAVIGATE</h4>""",
    """<h4 style="color:var(--text-color); margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">NAVIGATE</h4>"""
)

# Fix footer bold text
content = content.replace(
    """<strong style="color:white; font-weight:600;">Address:</strong>""",
    """<strong style="color:var(--text-color); font-weight:600;">Address:</strong>"""
)
content = content.replace(
    """<strong style="color:white; font-weight:600;">Contact:</strong>""",
    """<strong style="color:var(--text-color); font-weight:600;">Contact:</strong>"""
)
content = content.replace(
    """<strong style="color:white; font-weight:600;">E-mail:</strong>""",
    """<strong style="color:var(--text-color); font-weight:600;">E-mail:</strong>"""
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated footer colors!")
