import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean up nested wrappers
# Find instances of <div class="browse-img-wrapper"> followed by another <div class="browse-img-wrapper">
content = re.sub(r'<div class="browse-img-wrapper">\s*<div class="browse-img-wrapper">', r'<div class="browse-img-wrapper">', content)
# And remove the extra closing </div>
# The easiest way to fix this is to strip ALL wrappers and re-add them once.
content = re.sub(r'<div class="browse-img-wrapper">\s*(<img src="data:image/png[^>]+class="browse-img"[^>]*>)\s*</div>(?:\s*</div>)?', r'\1', content)
content = re.sub(r'(<img src="data:image/png[^>]+class="browse-img"[^>]*>)', r'<div class="browse-img-wrapper">\n                    \1\n                </div>', content)

# 2. Remove the light theme override for the wrapper (if it exists)
override_pattern = r'\.browse-img-wrapper\s*{\s*background:\s*#ffffff\s*!important;\s*box-shadow:\s*0 10px 30px rgba\(0,0,0,0\.05\)\s*!important;\s*}'
content = re.sub(override_pattern, '', content)

# 3. Add mobile grid collapse back
# Find the 900px media query and ensure .browse-grid { grid-template-columns: 1fr; } is there.
# Look for .features-section, .browse-section... padding: 5rem 5%;
content = content.replace(
    ".features-section, .browse-section, .how-it-works-section, .newsletter-section {{\n        padding: 5rem 5%;\n    }}",
    ".features-section, .browse-section, .how-it-works-section, .newsletter-section {{\n        padding: 5rem 5%;\n    }}\n    \n    .browse-grid {{\n        grid-template-columns: 1fr;\n    }}"
)

content = content.replace(
    ".features-section, .browse-section, .how-it-works-section, .newsletter-section {{\n        padding: 4rem 5% !important;\n    }}",
    ".features-section, .browse-section, .how-it-works-section, .newsletter-section {{\n        padding: 4rem 5% !important;\n    }}\n    \n    .browse-grid {{ grid-template-columns: 1fr; gap: 1.5rem; }}"
)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed mobile layout and wrappers.")
