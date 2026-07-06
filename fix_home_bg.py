dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

home_style = """    st.markdown('''<style>
.stApp::before { content: ''; position: fixed; top: -10%; left: -10%; width: 50vw; height: 50vw; background: radial-gradient(circle, rgba(116, 50, 255, 0.12) 0%, rgba(0,0,0,0) 70%); border-radius: 50%; z-index: 0; animation: driftBg1 20s infinite alternate ease-in-out; pointer-events: none; }
.stApp::after { content: ''; position: fixed; bottom: -20%; right: -10%; width: 60vw; height: 60vw; background: radial-gradient(circle, rgba(0, 230, 118, 0.08) 0%, rgba(0,0,0,0) 70%); border-radius: 50%; z-index: 0; animation: driftBg2 25s infinite alternate-reverse ease-in-out; pointer-events: none; }
@keyframes driftBg1 { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(10vw, 10vh) scale(1.2); } }
@keyframes driftBg2 { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(-10vw, -10vh) scale(1.1); } }
</style>''', unsafe_allow_html=True)
"""

if 'if page == "Home / Overview":' in content and 'driftBg1' not in content.split('if page == "Home / Overview":')[1][:500]:
    content = content.replace('if page == "Home / Overview":', 'if page == "Home / Overview":\n' + home_style)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Home background fixed.")
