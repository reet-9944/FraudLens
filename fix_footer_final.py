import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix global .main-footer CSS
old_main_footer_css = """/* Main Footer */
.main-footer {
    background: linear-gradient(-45deg, #fdfbfb, #ebedee, #f3e7e9, #e3eeff);
    background-size: 400% 400%;
    animation: soothingGradient 15s ease infinite;
    padding: 4rem 10%;
    display: flex;
    justify-content: space-between;
    color: #2b1154;
    border-top: 1px solid rgba(0,0,0,0.03);
}"""

new_main_footer_css = """/* Main Footer */
.main-footer {
    display: flex;
    flex-direction: column;
    width: 100%;
}"""

content = content.replace(old_main_footer_css, new_main_footer_css)

# 2. Fix the HTML of the footer slightly to ensure it stacks perfectly without relying on old CSS
old_footer_html_start = """<div class="main-footer" style="background:#1c1726; color:#a3a7b8; padding: 4rem 10%; font-family:'Outfit', sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 1.5rem;" class="footer-top-row">"""

new_footer_html_start = """<div class="main-footer" style="display: flex; flex-direction: column; background:#1c1726; color:#a3a7b8; padding: 4rem 10%; font-family:'Outfit', sans-serif;">
        <div style="display:flex; justify-content:flex-start; align-items:center; gap: 2rem; margin-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 1.5rem;" class="footer-top-row">"""

content = content.replace(old_footer_html_start, new_footer_html_start)

# 3. Update the mobile responsive CSS for the footer
old_mobile_footer = """    .footer-top-row { flex-direction: column; gap: 1.5rem; border-bottom: none !important; }
    .footer-grid { flex-direction: row !important; gap: 1rem !important; text-align: left; }
    .main-footer { padding: 3rem 5% !important; }"""

new_mobile_footer = """    .main-footer { padding: 3rem 5% !important; flex-direction: column !important; display: flex !important; width: 100% !important; box-sizing: border-box !important; }
    .footer-top-row { flex-direction: row !important; gap: 1rem !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; justify-content: flex-start !important; flex-wrap: wrap !important;}
    .footer-grid { flex-direction: row !important; gap: 1rem !important; text-align: left !important; width: 100% !important; box-sizing: border-box !important; }
    .footer-col { flex: 1 !important; min-width: 0 !important; overflow-wrap: break-word !important; word-wrap: break-word !important; }"""

content = content.replace(old_mobile_footer, new_mobile_footer)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Footer completely fixed.")
