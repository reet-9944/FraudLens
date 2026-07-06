import os

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove Emojis from sidebar strings
replacements = {
    "🏠 Home / Overview": "Home / Overview",
    "🔴 Live Triage & Alerting": "Live Triage & Alerting",
    "🚀 Live Accelerator Benchmark": "Live Accelerator Benchmark",
    "🔬 Transaction Risk Simulator": "Transaction Risk Simulator",
    "💬 Gemini Fraud Copilot": "Gemini Fraud Copilot",
    "☁️ GCP Enterprise Architecture": "GCP Enterprise Architecture"
}

for old, new in replacements.items():
    content = content.replace(old, new)

# 2. Add stunning background CSS and glassmorphism sidebar
new_css = """
    /* Premium Sidebar Styling - Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(15, 18, 30, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Add stunning glowing animated background orbs to the entire dashboard */
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
    }
"""

# Replace the old sidebar styling with the new premium one and add animations
old_sidebar_css = """    /* --- Premium Sidebar Styling --- */
    [data-testid="stSidebar"] {
        background-color: #232236 !important;
        border-right: none !important;
    }"""

if old_sidebar_css in content:
    content = content.replace(old_sidebar_css, new_css)
else:
    print("WARNING: Could not find old sidebar CSS to replace!")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Dashboard styled successfully.")
