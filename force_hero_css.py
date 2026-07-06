dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

force_css = """
    /* --- FORCED MOBILE HERO ADJUSTMENTS --- */
    .hero-section {
        padding: 4rem 5% 2rem 5% !important;
        min-height: auto !important;
    }
    .hero-title { font-size: 2.8rem !important; line-height: 1.1 !important; margin-bottom: 1rem !important; }
    .hero-subtitle { font-size: 1rem !important; margin: 0 auto 2rem auto !important; padding: 0 10px !important; }
    
    .hero-buttons {
        flex-direction: column !important;
        gap: 1rem !important;
        margin-bottom: 2rem !important;
        width: 100% !important;
        max-width: 300px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    .btn-primary, .btn-outline { width: 100% !important; text-align: center !important; padding: 14px 0 !important; box-sizing: border-box !important;}
    
    .hero-images {
        height: auto !important;
        width: 100% !important;
        margin-top: 1rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        gap: 20px !important;
        position: relative !important;
    }
    .img-wrapper-1, .img-wrapper-2 {
        position: relative !important;
        top: 0 !important; right: 0 !important; left: 0 !important; bottom: 0 !important;
        transform: none !important;
        margin: 0 !important;
        display: flex !important;
        justify-content: center !important;
    }
    .img-floating-1, .img-floating-2 {
        width: 250px !important;
        height: 250px !important;
        animation: none !important; /* Stop floating animation on mobile to prevent overflow */
    }
    .powered-logos { margin-bottom: 3rem !important; }
"""

# We want to inject this inside the @media (max-width: 900px) block.
# We will find the end of the media query by replacing the very last '}' before '</style>'
# The easiest way is just to append to the end of the style block, but inside a new media query block!
# Yes, a new media query block placed right at the end of the CSS will override everything above it!

new_media_query = f"\n@media (max-width: 900px) {{\n{force_css}\n}}\n</style>"

content = content.replace("</style>\n<div class=\"landing-wrapper\">", new_media_query + "\n<div class=\"landing-wrapper\">")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Forced hero mobile CSS applied.")
