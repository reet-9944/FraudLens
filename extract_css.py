import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"
with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if match:
    css = match.group(1)
    with open("current_css.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("CSS extracted.")
else:
    print("CSS not found.")
