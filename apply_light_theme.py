import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

light_theme_css = """
    /* --- LIGHT THEME OVERRIDES --- */
    @media (prefers-color-scheme: light) {
        /* Global App */
        .stApp {
            background: linear-gradient(-45deg, #f8f9fa, #e9ecef, #fdfbfb, #ffffff) !important;
            background-size: 400% 400% !important;
            color: #2b1154 !important;
        }
        
        /* Modals and Cards */
        .glass-card, .glass-modal-content {
            background: rgba(255, 255, 255, 0.7) !important;
            border: 1px solid rgba(0, 0, 0, 0.05) !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05) !important;
        }
        .glass-card:hover {
            box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.1) !important;
        }
        
        /* Text Colors */
        .metric-value, .hero-title, .hiw-title, .hiw-step-title, .browse-title, .newsletter-title, 
        .modal-title-text, .stRadio div[role="radiogroup"] > label {
            color: #2b1154 !important;
        }
        .metric-label, .hero-subtitle, .hiw-step-desc, .modal-desc-text, .footer-col p {
            color: #4a4a4a !important;
        }
        
        /* Specific Component Backgrounds */
        .hero-section {
            background: linear-gradient(-45deg, #f8f9fa, #e9ecef, #fdfbfb, #ffffff) !important;
        }
        .how-it-works-section, .newsletter-section {
            background-color: #f1f3f5 !important;
            color: #2b1154 !important;
        }
        .browse-section {
            background-color: #ffffff !important;
        }
        .newsletter-card {
            background: #ffffff !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
        }
        .browse-img-wrapper {
            background: #ffffff !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background: rgba(248, 249, 250, 0.8) !important;
            border-right: 1px solid rgba(0, 0, 0, 0.05) !important;
        }
        
        /* Radio Buttons */
        .stRadio div[role="radiogroup"] > label:hover {
            background: rgba(0,0,0,0.05) !important;
            color: #2b1154 !important;
        }
        .stRadio div[role="radiogroup"] > label:has(input:checked) {
            background: rgba(116, 50, 255, 0.1) !important;
            color: #2b1154 !important;
        }
        
        /* Buttons */
        .btn-outline {
            border-color: #5a22d5 !important;
            color: #5a22d5 !important;
        }
        .btn-outline:hover {
            background: #5a22d5 !important;
            color: white !important;
        }
        
        /* Code Blocks */
        code {
            color: #5a22d5 !important;
            background-color: rgba(0, 0, 0, 0.05) !important;
        }
        
        /* Blobs */
        .blob-1 { background: rgba(255, 0, 122, 0.15) !important; }
        .blob-2 { background: rgba(0, 210, 255, 0.15) !important; }
        .blob-3 { background: rgba(116, 50, 255, 0.15) !important; }
    }
    /* --- END LIGHT THEME OVERRIDES --- */
"""

# Insert the light theme CSS right after the first <style> tag
if "/* --- LIGHT THEME OVERRIDES --- */" not in content:
    content = content.replace("<style>", f"<style>\n{light_theme_css}", 1)
    
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Light theme overrides applied.")
else:
    print("Overrides already applied.")
