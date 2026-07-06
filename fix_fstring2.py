import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the forced CSS block we injected
start_marker = "/* --- FORCED MOBILE HERO ADJUSTMENTS --- */"
end_marker = "</style>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Extract the block
    block = content[start_idx:end_idx]
    
    # We must double the braces for f-string escaping
    # First, make sure we aren't doubling already doubled braces
    block = block.replace("{{", "{").replace("}}", "}")
    
    # Now double them
    block = block.replace("{", "{{").replace("}", "}}")
    
    # Replace in content
    new_content = content[:start_idx] + block + content[end_idx:]
    
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed f-string syntax error for the forced CSS block.")
else:
    print("Could not find the block to fix.")
