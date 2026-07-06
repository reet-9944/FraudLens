import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

old_footer_html = """    <div class="main-footer" style="display: flex; flex-direction: column; background:#1c1726; color:#a3a7b8; padding: 4rem 10%; font-family:'Outfit', sans-serif;">
        <div style="display:flex; justify-content:flex-start; align-items:center; gap: 2rem; margin-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 1.5rem;" class="footer-top-row">
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

new_footer_html = """    <div class="main-footer" style="display: flex; flex-direction: column; background:#1c1726; color:#a3a7b8; padding: 4rem 10%; font-family:'Outfit', sans-serif;">
        <div style="display:flex; justify-content:flex-start; align-items:center; gap: 2rem; margin-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 1.5rem;" class="footer-top-row">
            <h4 style="color:white; margin:0; letter-spacing:1px; font-weight:700;">FOLLOW US</h4>
            <div style="display:flex; gap:15px; transform: translateY(-4px);">
                <a href="https://facebook.com" target="_blank" style="text-decoration:none; transition: transform 0.2s;"><div style="width:35px; height:35px; border-radius:50%; background:#4267B2; display:flex; justify-content:center; align-items:center; color:white; font-weight:bold; cursor:pointer;">f</div></a>
                <a href="https://linkedin.com" target="_blank" style="text-decoration:none; transition: transform 0.2s;"><div style="width:35px; height:35px; border-radius:50%; background:linear-gradient(45deg, #f09433, #dc2743, #bc1888); display:flex; justify-content:center; align-items:center; color:white; font-weight:bold; cursor:pointer;">in</div></a>
                <a href="https://youtube.com" target="_blank" style="text-decoration:none; transition: transform 0.2s;"><div style="width:35px; height:35px; border-radius:50%; background:#FF0000; display:flex; justify-content:center; align-items:center; color:white; font-weight:bold; cursor:pointer;">&#9654;</div></a>
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
                <a href="mailto:support@fraudlens.io" style="color:#a3a7b8; text-decoration:none; font-size:0.9rem;">support@fraudlens.io</a>
            </div>
            <div class="footer-col" style="flex: 1;">
                <h4 style="color:white; margin-bottom:1.5rem; letter-spacing:1px; font-weight:700;">NAVIGATE</h4>
                <a href="#" style="color:#a3a7b8; text-decoration:none; display:block; margin-bottom:1rem; font-size:0.9rem; transition:color 0.2s;">Home</a>
                <a href="#" style="color:#a3a7b8; text-decoration:none; display:block; margin-bottom:1rem; font-size:0.9rem; transition:color 0.2s;">About</a>
                <a href="#" style="color:#a3a7b8; text-decoration:none; display:block; margin-bottom:1rem; font-size:0.9rem; transition:color 0.2s;">Products</a>
                <a href="#" style="color:#a3a7b8; text-decoration:none; display:block; margin-bottom:1rem; font-size:0.9rem; transition:color 0.2s;">Locations</a>
                <a href="#" style="color:#a3a7b8; text-decoration:none; display:block; margin-bottom:1rem; font-size:0.9rem; transition:color 0.2s;">Contact</a>
            </div>
        </div>
    </div>"""

if old_footer_html in content:
    content = content.replace(old_footer_html, new_footer_html)
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Links made functional and icons nudged up!")
else:
    print("Warning: old footer html not found exactly.")
