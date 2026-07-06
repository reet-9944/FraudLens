import re

file_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the sidebar background to make it a transparent whitish cremish glass in light mode
content = content.replace(
    """    /* Premium Sidebar Styling - Glassmorphism */
    [data-testid="stSidebar"] {
        background: var(--secondary-background-color) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(128, 128, 128, 0.2) !important;
    }""",
    """    /* Premium Sidebar Styling - Glassmorphism */
    [data-testid="stSidebar"] {
        background: color-mix(in srgb, var(--secondary-background-color) 40%, rgba(255, 253, 248, 0.7)) !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        border-right: 1px solid color-mix(in srgb, var(--text-color) 10%, transparent) !important;
    }"""
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated sidebar to be transparent whitish cremish!")
