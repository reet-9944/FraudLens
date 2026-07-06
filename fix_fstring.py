import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the responsive CSS block we injected
start_marker = "/* --- RESPONSIVE MOBILE ADJUSTMENTS --- */"
end_marker = "</style>\n<div class=\"landing-wrapper\">"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Extract the block
    block = content[start_idx:end_idx]
    
    # We must double the braces for f-string escaping
    # Since it might already have some mixed up ones or we just need to replace single braces
    # But wait, we injected it with single braces. 
    # Let's just safely replace { with {{ and } with }}
    
    # First, make sure we aren't doubling already doubled braces
    block = block.replace("{{", "{").replace("}}", "}")
    
    # Now double them
    block = block.replace("{", "{{").replace("}", "}}")
    
    # Replace in content
    new_content = content[:start_idx] + block + content[end_idx:]
    
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed f-string syntax error.")
else:
    print("Could not find the block to fix.")
