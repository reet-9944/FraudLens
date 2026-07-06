import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the media query definition bracket
content = content.replace("@media (max-width: 900px) {", "@media (max-width: 900px) {{")

# Fix the closing bracket before </style>
# We can find the exact block:
#     .powered-logos {{ margin-bottom: 3rem !important; }}
# 
# }
# </style>
content = content.replace("    .powered-logos {{ margin-bottom: 3rem !important; }}\n\n}\n</style>", "    .powered-logos {{ margin-bottom: 3rem !important; }}\n\n}}\n</style>")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Final f-string brackets fixed!")
