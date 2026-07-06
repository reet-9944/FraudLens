dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# We want to add responsive styles for .main-footer inside the @media (max-width: 900px) block.
# We can find the end of the media query by looking for:
#     .footer-content {
#         flex-direction: column;
#         text-align: center;
#         gap: 2rem;
#     }
# }
# </style>

replacement_css = """    .footer-content {
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }
    
    .main-footer {
        flex-direction: column;
        gap: 3rem;
        text-align: center;
        align-items: center;
    }
    .main-footer > div:nth-child(2) {
        flex-direction: column;
        gap: 2rem !important;
    }
}
"""

content = content.replace("    .footer-content {\n        flex-direction: column;\n        text-align: center;\n        gap: 2rem;\n    }\n}", replacement_css)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Footer responsive CSS added.")
