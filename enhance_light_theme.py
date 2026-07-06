import re

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Additional light theme CSS to append right before the closing } of the media query
additional_css = """
        /* Metric Values for Light Theme */
        .metric-value-green {
            color: #008a47 !important; /* Darker green */
            text-shadow: none !important;
        }
        .metric-value-red {
            color: #d12f00 !important; /* Darker red */
            text-shadow: none !important;
        }
        .metric-value-orange {
            color: #c97200 !important; /* Darker orange */
            text-shadow: none !important;
        }
        
        /* Table / DataFrame Overrides */
        [data-testid="stDataFrame"] {
            background-color: rgba(255,255,255,0.7) !important;
        }
        
        /* Chat UI Overrides */
        [data-testid="stChatMessage"] {
            background-color: rgba(255,255,255,0.8) !important;
            color: #2b1154 !important;
        }
        
        /* Headers globally */
        h1, h2, h3, h4, h5, h6 {
            color: #2b1154 !important;
        }
        
        /* Remove the borders from transparent elements so they don't look muddy */
        .glass-card-border-green {
            border-left: 5px solid #008a47 !important;
        }
        .glass-card-border-red {
            border-left: 5px solid #d12f00 !important;
        }
        .glass-card-border-orange {
            border-left: 5px solid #c97200 !important;
        }
"""

if "/* Metric Values for Light Theme */" not in content:
    # Find the end of the light theme block
    # It ends with:
    #         .blob-3 { background: rgba(116, 50, 255, 0.15) !important; }
    #     }
    #     /* --- END LIGHT THEME OVERRIDES --- */
    
    target_string = "        .blob-3 { background: rgba(116, 50, 255, 0.15) !important; }\n    }"
    replacement = f"        .blob-3 {{ background: rgba(116, 50, 255, 0.15) !important; }}\n{additional_css}\n    }}"
    
    content = content.replace(target_string, replacement)
    
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Enhanced light theme overrides applied.")
else:
    print("Enhanced overrides already applied.")
