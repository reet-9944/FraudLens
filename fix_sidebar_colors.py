import re

file_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Premium Sidebar Styling
content = content.replace(
    """    /* Premium Sidebar Styling - Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(15, 18, 30, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }""",
    """    /* Premium Sidebar Styling - Glassmorphism */
    [data-testid="stSidebar"] {
        background: var(--secondary-background-color) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(128, 128, 128, 0.2) !important;
    }"""
)

# 2. Radio Buttons Styling
content = content.replace(
    """    /* Style the radio label container */
    .stRadio div[role="radiogroup"] > label {
        background: transparent;
        padding: 12px 20px;
        border-radius: 12px;
        margin-bottom: 8px;
        color: #8E9AA8;
        font-weight: 600;
        transition: all 0.3s ease;
        cursor: pointer;
    }""",
    """    /* Style the radio label container */
    .stRadio div[role="radiogroup"] > label {
        background: transparent;
        padding: 12px 20px;
        border-radius: 12px;
        margin-bottom: 8px;
        color: var(--text-color);
        opacity: 0.8;
        font-weight: 600;
        transition: all 0.3s ease;
        cursor: pointer;
    }"""
)

content = content.replace(
    """    /* Hover state */
    .stRadio div[role="radiogroup"] > label:hover {
        background: rgba(255,255,255,0.05);
        color: #ffffff;
    }""",
    """    /* Hover state */
    .stRadio div[role="radiogroup"] > label:hover {
        background: rgba(128, 128, 128, 0.1);
        color: var(--text-color);
        opacity: 1.0;
    }"""
)

# 3. Sidebar HTML Markdown (Logo and User Profile)
content = content.replace(
    """<h3 style="margin:0; color: white; font-weight: 800; font-size: 1.4rem;">FraudLens</h3>""",
    """<h3 style="margin:0; color: var(--text-color); font-weight: 800; font-size: 1.4rem;">FraudLens</h3>"""
)

content = content.replace(
    """<div style="text-align: center; margin-bottom: 35px; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px;">""",
    """<div style="text-align: center; margin-bottom: 35px; background: rgba(128,128,128,0.05); padding: 20px; border-radius: 16px;">"""
)

content = content.replace(
    """<h3 style="margin: 0; color: white; font-size: 1.1rem; font-weight: 700;">Saira Karim</h3>""",
    """<h3 style="margin: 0; color: var(--text-color); font-size: 1.1rem; font-weight: 700;">Saira Karim</h3>"""
)

content = content.replace(
    """<p style="margin: 0; color: #8E9AA8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Risk Analyst</p>""",
    """<p style="margin: 0; color: var(--text-color); opacity: 0.7; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Risk Analyst</p>"""
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated sidebar colors successfully.")
