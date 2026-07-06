import re

file_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# The block to move
block_start_marker = r"    /\* --- LIGHT THEME OVERRIDES --- \*/"
block_end_marker = r"    /\* --- END LIGHT THEME OVERRIDES --- \*/"

# Extract the block
match = re.search(f"({block_start_marker}.*?{block_end_marker}\n)", content, flags=re.DOTALL)
if match:
    light_theme_block = match.group(1)
    
    # Remove it from the original location
    content = content.replace(light_theme_block, "")
    
    # We need to insert it right before the FIRST closing </style>
    # Wait, the first closing </style> is at line 354
    # The string is st.markdown("""\n<style>\n...
    # We will split at the first </style>
    parts = content.split("</style>", 1)
    
    if len(parts) == 2:
        # Recombine with the light theme block right before </style>
        new_content = parts[0] + "\n" + light_theme_block + "</style>" + parts[1]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully moved light theme overrides to the end of the global CSS block.")
    else:
        print("Could not find </style>")
else:
    print("Could not find light theme block.")
