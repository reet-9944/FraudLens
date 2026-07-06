dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "/* --- RESPONSIVE MOBILE ADJUSTMENTS --- */" in line:
        skip = True
        continue
    if skip and line.strip() == "}}":
        # Check if the NEXT line (or after empty lines) is the forced one
        # To be safe, we'll just stop skipping here
        skip = False
        continue
    if not skip:
        new_lines.append(line)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Old CSS block removed, syntax error solved!")
