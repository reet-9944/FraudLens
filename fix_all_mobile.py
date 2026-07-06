import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to find where the current media query starts and ends.
# It starts at "@media (max-width: 900px) {{"
# and ends right before "</style>"

start_marker = "@media (max-width: 900px) {{"
end_marker = "</style>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

full_mobile_css = """@media (max-width: 900px) {{
    .hero-section {{
        flex-direction: column !important;
        padding: 4rem 5% 2rem 5% !important;
        text-align: center;
        min-height: auto !important;
    }}
    .hero-title {{ font-size: 2.8rem !important; line-height: 1.1 !important; margin-bottom: 1rem !important; }}
    .hero-subtitle {{ font-size: 1rem !important; margin: 0 auto 2rem auto !important; padding: 0 10px !important; }}
    
    .hero-buttons {{
        flex-direction: column !important;
        gap: 1rem !important;
        margin-bottom: 2rem !important;
        width: 100% !important;
        max-width: 300px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }}
    .btn-primary, .btn-outline {{ width: 100% !important; text-align: center !important; padding: 14px 0 !important; box-sizing: border-box !important;}}
    
    .hero-images {{
        height: auto !important;
        width: 100% !important;
        margin-top: 1rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        gap: 20px !important;
        position: relative !important;
    }}
    .img-wrapper-1, .img-wrapper-2 {{
        position: relative !important;
        top: 0 !important; right: 0 !important; left: 0 !important; bottom: 0 !important;
        transform: none !important;
        margin: 0 !important;
        display: flex !important;
        justify-content: center !important;
    }}
    .img-floating-1, .img-floating-2 {{
        width: 250px !important;
        height: 250px !important;
        animation: none !important;
    }}
    .powered-logos {{ margin-bottom: 3rem !important; justify-content: center !important; flex-wrap: wrap !important; }}
    
    .features-section, .browse-section, .how-it-works-section, .newsletter-section {{
        padding: 4rem 5% !important;
    }}
    
    .hiw-step {{
        flex-direction: column !important;
        gap: 2rem;
        text-align: center;
    }}
    .hiw-badge {{ margin: 0 auto 1rem auto; }}
    .hiw-img {{ width: 100%; }}
    
    .browse-grid {{ grid-template-columns: 1fr; gap: 1.5rem; }}
    
    .newsletter-card {{ padding: 3rem 5%; text-align: center; }}
    .newsletter-title {{ font-size: 1.8rem; }}
    .newsletter-input-group {{ flex-direction: column; margin: 0 auto; }}
    
    .main-footer {{ padding: 3rem 5% !important; flex-direction: column !important; display: flex !important; width: 100% !important; box-sizing: border-box !important; }}
    .footer-top-row {{ flex-direction: row !important; gap: 1rem !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; justify-content: flex-start !important; flex-wrap: wrap !important;}}
    .footer-grid {{ flex-direction: row !important; gap: 1rem !important; text-align: left !important; width: 100% !important; box-sizing: border-box !important; }}
    .footer-col {{ flex: 1 !important; min-width: 0 !important; overflow-wrap: break-word !important; word-wrap: break-word !important; }}
}}
"""

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + full_mobile_css + content[end_idx:]
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("All mobile CSS restored perfectly!")
else:
    print("Could not find the target block.")
