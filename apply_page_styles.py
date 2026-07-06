import os
import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove emojis from st.title
emojis_to_remove = ["🔴 ", "🚀 ", "🔬 ", "☁️ "]
for emoji in emojis_to_remove:
    content = content.replace(f'st.title("{emoji}', 'st.title("')

# 2. Remove the old global stApp before/after pseudo elements added in previous step
old_global_animations = """    /* Add stunning glowing animated background orbs to the entire dashboard */
    .stApp::before {
        content: '';
        position: fixed;
        top: -10%;
        left: -10%;
        width: 50vw;
        height: 50vw;
        background: radial-gradient(circle, rgba(116, 50, 255, 0.12) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        z-index: -1;
        animation: driftBg1 20s infinite alternate ease-in-out;
        pointer-events: none;
    }
    
    .stApp::after {
        content: '';
        position: fixed;
        bottom: -20%;
        right: -10%;
        width: 60vw;
        height: 60vw;
        background: radial-gradient(circle, rgba(0, 230, 118, 0.08) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        z-index: -1;
        animation: driftBg2 25s infinite alternate-reverse ease-in-out;
        pointer-events: none;
    }
    
    @keyframes driftBg1 {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(10vw, 10vh) scale(1.2); }
    }
    @keyframes driftBg2 {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(-10vw, -10vh) scale(1.1); }
    }"""

content = content.replace(old_global_animations, "")

# 3. Inject unique styles per page
triage_style = """st.markdown('''<style>
.stApp::before { content: ''; position: fixed; top: 0; left: 0; width: 100vw; height: 100vw; background: radial-gradient(circle at 80% 20%, rgba(255, 61, 0, 0.15) 0%, transparent 40%); z-index: -1; animation: pulseAlert 4s infinite alternate; pointer-events: none; }
.stApp::after { content: ''; position: fixed; bottom: 0; left: 10%; width: 60vw; height: 60vw; background: radial-gradient(circle, rgba(116, 50, 255, 0.1) 0%, transparent 50%); z-index: -1; animation: driftBg1 15s infinite alternate ease-in-out; pointer-events: none; }
@keyframes pulseAlert { 0% { opacity: 0.5; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1.1); } }
@keyframes driftBg1 { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(10vw, 10vh) scale(1.2); } }
</style>''', unsafe_allow_html=True)
"""
content = content.replace('st.title("Real-Time Triage & Alerts")', 'st.title("Real-Time Triage & Alerts")\n    ' + triage_style)

benchmark_style = """st.markdown('''<style>
.stApp::before { content: ''; position: fixed; top: -20%; left: -10%; width: 50vw; height: 50vw; background: radial-gradient(circle, rgba(0, 230, 118, 0.15) 0%, transparent 60%); z-index: -1; animation: speedFloat 8s infinite alternate ease-in-out; pointer-events: none; }
.stApp::after { content: ''; position: fixed; bottom: -10%; right: -20%; width: 70vw; height: 70vw; background: radial-gradient(circle, rgba(0, 210, 255, 0.1) 0%, transparent 50%); z-index: -1; animation: speedFloat 6s infinite alternate-reverse ease-in-out; pointer-events: none; }
@keyframes speedFloat { 0% { transform: translateY(0) skewX(-10deg); } 100% { transform: translateY(-50px) skewX(10deg); } }
</style>''', unsafe_allow_html=True)
"""
content = content.replace('st.title("NVIDIA GPU Acceleration Benchmark")', 'st.title("NVIDIA GPU Acceleration Benchmark")\n    ' + benchmark_style)

simulator_style = """st.markdown('''<style>
.stApp::before { content: ''; position: fixed; top: 30%; right: 10%; width: 40vw; height: 40vw; background: radial-gradient(circle, rgba(255, 145, 0, 0.12) 0%, transparent 60%); z-index: -1; animation: rotateGlow 20s linear infinite; pointer-events: none; }
.stApp::after { content: ''; position: fixed; bottom: 10%; left: -10%; width: 50vw; height: 50vw; background: radial-gradient(circle, rgba(75, 54, 124, 0.2) 0%, transparent 60%); z-index: -1; animation: driftBg2 15s infinite alternate ease-in-out; pointer-events: none; }
@keyframes rotateGlow { 0% { transform: rotate(0deg) scale(1); } 50% { transform: rotate(180deg) scale(1.2); } 100% { transform: rotate(360deg) scale(1); } }
@keyframes driftBg2 { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(-10vw, -10vh) scale(1.1); } }
</style>''', unsafe_allow_html=True)
"""
content = content.replace('st.title("Real-Time Risk Simulator")', 'st.title("Real-Time Risk Simulator")\n    ' + simulator_style)

copilot_style = """st.markdown('''<style>
.stApp::before { content: ''; position: fixed; top: -10%; left: 20%; width: 60vw; height: 60vw; background: radial-gradient(circle, rgba(66, 133, 244, 0.12) 0%, transparent 50%); z-index: -1; animation: morphAI 15s infinite alternate ease-in-out; pointer-events: none; }
.stApp::after { content: ''; position: fixed; bottom: -20%; right: 10%; width: 70vw; height: 70vw; background: radial-gradient(circle, rgba(234, 67, 53, 0.08) 0%, transparent 50%); z-index: -1; animation: morphAI2 18s infinite alternate-reverse ease-in-out; pointer-events: none; }
@keyframes morphAI { 0% { transform: scale(1) translate(0,0); border-radius: 50%; } 100% { transform: scale(1.2) translate(5vw, 5vh); border-radius: 40% 60% 70% 30%; } }
@keyframes morphAI2 { 0% { transform: scale(1) translate(0,0); border-radius: 50%; } 100% { transform: scale(1.3) translate(-5vw, -5vh); border-radius: 60% 40% 30% 70%; } }
</style>''', unsafe_allow_html=True)
"""
content = content.replace('st.title("Gemini Fraud Copilot Agent")', 'st.title("Gemini Fraud Copilot Agent")\n    ' + copilot_style)

gcp_style = """st.markdown('''<style>
.stApp::before { content: ''; position: fixed; top: 10%; left: -20%; width: 140vw; height: 30vh; background: radial-gradient(ellipse, rgba(142, 197, 252, 0.08) 0%, transparent 70%); z-index: -1; animation: cloudDrift 30s infinite linear; pointer-events: none; }
.stApp::after { content: ''; position: fixed; bottom: 20%; right: -20%; width: 120vw; height: 40vh; background: radial-gradient(ellipse, rgba(224, 195, 252, 0.06) 0%, transparent 60%); z-index: -1; animation: cloudDrift2 40s infinite linear reverse; pointer-events: none; }
@keyframes cloudDrift { 0% { transform: translateX(0); } 100% { transform: translateX(5vw); } }
@keyframes cloudDrift2 { 0% { transform: translateX(0); } 100% { transform: translateX(-5vw); } }
</style>''', unsafe_allow_html=True)
"""
content = content.replace('st.title("Google Cloud Data & Application Stack")', 'st.title("Google Cloud Data & Application Stack")\n    ' + gcp_style)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Unique page styles applied successfully.")
