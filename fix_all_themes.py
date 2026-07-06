import re

file_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the entire LIGHT THEME OVERRIDES block, since it relies on OS preference and causes bugs
light_theme_pattern = r"\s*/\* --- LIGHT THEME OVERRIDES --- \*/.*?/\* --- END LIGHT THEME OVERRIDES --- \*/"
content = re.sub(light_theme_pattern, "", content, flags=re.DOTALL)

# 2. Fix .stApp background to dynamically mix with Streamlit's theme
content = re.sub(
    r"\.stApp\s*\{\s*background:\s*linear-gradient\(-45deg,\s*#0b0d12,\s*#1a1f2e,\s*#0f1626,\s*#050811\);\s*background-size:\s*400%\s*400%;\s*animation:\s*gradientBG\s*15s\s*ease\s*infinite;\s*\}",
    """.stApp {
        background: color-mix(in srgb, var(--background-color) 85%, #1a1f2e) !important;
    }""",
    content
)

# 3. Fix .hero-section background
content = re.sub(
    r"\.hero-section\s*\{\s*background:\s*linear-gradient\(135deg,\s*#1d3354\s*0%,\s*#3d1c5a\s*50%,\s*#201335\s*100%\);",
    """.hero-section {
        background: color-mix(in srgb, var(--background-color) 80%, #3d1c5a) !important;""",
    content
)

# 4. Fix [data-testid="stSidebar"] to be heavily opaque in light mode (to hide stApp) and beautifully milky
content = re.sub(
    r"\[data-testid=\"stSidebar\"\]\s*\{\s*background:\s*color-mix\(in\s*srgb,\s*var\(--secondary-background-color\)\s*40%,\s*rgba\(255,\s*253,\s*248,\s*0\.7\)\)\s*!important;",
    """[data-testid="stSidebar"] {
        background: color-mix(in srgb, var(--background-color) 85%, rgba(255, 253, 248, 0.9)) !important;""",
    content
)

# Fix any stray old sidebar CSS if it didn't match the regex
content = re.sub(
    r"\[data-testid=\"stSidebar\"\]\s*\{\s*background:\s*rgba\(15,\s*18,\s*30,\s*0\.6\)\s*!important;",
    """[data-testid="stSidebar"] {
        background: color-mix(in srgb, var(--background-color) 85%, rgba(255, 253, 248, 0.9)) !important;""",
    content
)

# 5. Fix .landing-wrapper background
content = re.sub(
    r"\.landing-wrapper\s*\{\s*width:\s*100%;\s*margin:\s*0;\s*padding:\s*0;\s*font-family:\s*'Outfit',\s*sans-serif;\s*background:\s*#2a1b4e;\s*color:\s*white;\s*\}",
    """.landing-wrapper {
        width: 100%;
        margin: 0;
        padding: 0;
        font-family: 'Outfit', sans-serif;
        background: color-mix(in srgb, var(--background-color) 85%, #2a1b4e) !important;
        color: var(--text-color);
    }""",
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated all backgrounds to dynamically sync with Streamlit's theme using color-mix!")
