import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Re-write the responsive CSS block completely
old_responsive_css = """/* --- RESPONSIVE MOBILE ADJUSTMENTS --- */
@media (max-width: 900px) {{
    .hero-section {{
        flex-direction: column;
        padding: 6rem 5% 4rem 5%;
        text-align: center;
    }}
    .hero-title {{ font-size: 3rem; }}
    .hero-subtitle {{ margin: 0 auto 2rem auto; }}
    .hero-buttons {{ justify-content: center; flex-wrap: wrap; }}
    .powered-logos {{ justify-content: center; flex-wrap: wrap; }}
    
    .hero-images {{
        height: 300px;
        width: 100%;
        margin-left: 0;
        margin-top: 2rem;
    }}
    .img-floating-1, .img-floating-2 {{
        width: 180px;
        height: 180px;
    }}
    .img-wrapper-1 {{ top: 20px; right: 5%; }}
    .img-wrapper-2 {{ bottom: 0px; right: auto; left: 5%; }}
    
    .features-section, .browse-section, .how-it-works-section, .newsletter-section {{
        padding: 5rem 5%;
    }}
    
    .hiw-step {{
        flex-direction: column !important;
        gap: 2rem;
        text-align: center;
    }}
    .hiw-badge {{ margin: 0 auto 1rem auto; }}
    .hiw-img {{ width: 100%; }}
    
    .browse-grid {{
        grid-template-columns: 1fr;
    }}
    
    .newsletter-card {{
        padding: 3rem 5%;
        text-align: center;
    }}
    .newsletter-title {{ font-size: 2rem; }}
    .newsletter-input-group {{
        flex-direction: column;
        margin: 0 auto;
    }}
    .footer-content {{
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }}
    
    .main-footer {{
        flex-direction: column;
        gap: 3rem;
        text-align: center;
        align-items: center;
    }}
    .main-footer > div:nth-child(2) {{
        flex-direction: column;
        gap: 2rem !important;
    }}
}}"""

new_responsive_css = """/* --- RESPONSIVE MOBILE ADJUSTMENTS --- */
@media (max-width: 900px) {{
    .hero-section {{
        flex-direction: column;
        padding: 4rem 5% 2rem 5%;
        text-align: center;
        min-height: auto;
    }}
    .hero-title {{ font-size: 2.8rem; line-height: 1.1; margin-bottom: 1rem; }}
    .hero-subtitle {{ font-size: 1rem; margin: 0 auto 2rem auto; padding: 0 10px; }}
    
    .hero-buttons {{
        flex-direction: column;
        gap: 1rem;
        margin-bottom: 2rem;
        width: 100%;
        max-width: 300px;
        margin-left: auto;
        margin-right: auto;
    }}
    .btn-primary, .btn-outline {{ width: 100%; text-align: center; padding: 14px 0; }}
    
    .hero-images {{
        height: auto;
        width: 100%;
        margin-top: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        position: relative;
    }}
    .img-wrapper-1, .img-wrapper-2 {{
        position: relative;
        top: 0; right: 0; left: 0; bottom: 0;
        animation: none; /* Disable complex floating on mobile to prevent overflow */
    }}
    .img-floating-1, .img-floating-2 {{
        width: 250px;
        height: 250px;
    }}
    
    .powered-logos {{ justify-content: center; flex-wrap: wrap; margin-bottom: 3rem; }}
    
    .features-section, .browse-section, .how-it-works-section, .newsletter-section {{
        padding: 4rem 5%;
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
    
    .footer-top-row {{ flex-direction: column; gap: 1.5rem; border-bottom: none !important; }}
    .footer-grid {{ flex-direction: row !important; gap: 1rem !important; text-align: left; }}
    .main-footer {{ padding: 3rem 5% !important; }}
}}"""

content = content.replace(old_responsive_css, new_responsive_css)

# 2. Re-write the HTML footer
old_footer_html = """    <div class="main-footer">
        <div class="footer-col" style="max-width: 300px;">
            <h3 style="font-weight: 800; font-size: 1.5rem; margin-bottom: 1rem;">FraudLens</h3>
            <p>Accelerated Risk Intelligence powered by NVIDIA and GCP. We stop fraud before it happens.</p>
        </div>
        <div style="display: flex; gap: 4rem;">
            <div class="footer-col">
                <h4>Sitemap</h4>
                <p>Home</p>
                <p>Live Triage</p>
                <p>Simulator</p>
                <p>Copilot</p>
            </div>
            <div class="footer-col">
                <h4>Company</h4>
                <p>About Us</p>
                <p>Core Team</p>
                <p>Studio</p>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <p>support@fraudlens.io</p>
                <p>28 Cambridge Avenue<br>San Francisco 94126</p>
                <p>(700) 555-0199</p>
            </div>
        </div>
    </div>"""

new_footer_html = """    <div class="main-footer" style="background:#1c1726; color:#a3a7b8; padding: 4rem 10%; font-family:'Outfit', sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 1.5rem;" class="footer-top-row">
            <h4 style="color:white; margin:0; letter-spacing:1px; font-weight:700;">FOLLOW US</h4>
            <div style="display:flex; gap:15px;">
                <div style="width:35px; height:35px; border-radius:50%; background:#4267B2; display:flex; justify-content:center; align-items:center; color:white; font-weight:bold; cursor:pointer;">f</div>
                <div style="width:35px; height:35px; border-radius:50%; background:linear-gradient(45deg, #f09433, #dc2743, #bc1888); display:flex; justify-content:center; align-items:center; color:white; font-weight:bold; cursor:pointer;">in</div>
                <div style="width:35px; height:35px; border-radius:50%; background:#FF0000; display:flex; justify-content:center; align-items:center; color:white; font-weight:bold; cursor:pointer;">&#9654;</div>
            </div>
        </div>
        
        <div style="display:flex; justify-content:space-between; gap: 2rem;" class="footer-grid">
            <div class="footer-col" style="flex: 1;">
                <h4 style="color:white; margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">CONTACT US</h4>
                <p style="margin-bottom:0.3rem;"><strong style="color:white; font-weight:600;">Address:</strong></p>
                <p style="margin-top:0; margin-bottom:1rem; line-height:1.5; font-size:0.9rem;">28 Cambridge Avenue<br>FraudLens HQ,<br>San Francisco 94126</p>
                <p style="margin-bottom:0.3rem;"><strong style="color:white; font-weight:600;">Contact:</strong></p>
                <p style="margin-top:0; margin-bottom:1rem; font-size:0.9rem;">(700) 555-0199</p>
                <p style="margin-bottom:0.3rem;"><strong style="color:white; font-weight:600;">E-mail:</strong></p>
                <p style="margin-top:0; font-size:0.9rem;">support@fraudlens.io</p>
            </div>
            <div class="footer-col" style="flex: 1;">
                <h4 style="color:white; margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">NAVIGATE</h4>
                <p style="margin-bottom:1rem; cursor:pointer; transition:color 0.2s; font-size:0.9rem;">Home</p>
                <p style="margin-bottom:1rem; cursor:pointer; transition:color 0.2s; font-size:0.9rem;">About</p>
                <p style="margin-bottom:1rem; cursor:pointer; transition:color 0.2s; font-size:0.9rem;">Products</p>
                <p style="margin-bottom:1rem; cursor:pointer; transition:color 0.2s; font-size:0.9rem;">Locations</p>
                <p style="margin-bottom:1rem; cursor:pointer; transition:color 0.2s; font-size:0.9rem;">Contact</p>
            </div>
        </div>
    </div>"""

if old_footer_html in content:
    content = content.replace(old_footer_html, new_footer_html)
else:
    print("Warning: old footer html not found exactly.")
    # Fallback regex replace if indentation changed
    # We will just write it if we can find the old footer text
    
with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Mobile layout and footer rebuilt.")
