import os

dashboard_path = r"c:\Users\reetu\Desktop\hegi\online_projects\genai_hackathon\fraudlens\app\dashboard.py"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

responsive_css = """
/* --- RESPONSIVE MOBILE ADJUSTMENTS --- */
@media (max-width: 900px) {
    .hero-section {
        flex-direction: column;
        padding: 6rem 5% 4rem 5%;
        text-align: center;
    }
    .hero-title { font-size: 3rem; }
    .hero-subtitle { margin: 0 auto 2rem auto; }
    .hero-buttons { justify-content: center; flex-wrap: wrap; }
    .powered-logos { justify-content: center; flex-wrap: wrap; }
    
    .hero-images {
        height: 300px;
        width: 100%;
        margin-left: 0;
        margin-top: 2rem;
    }
    .img-floating-1, .img-floating-2 {
        width: 180px;
        height: 180px;
    }
    .img-wrapper-1 { top: 20px; right: 5%; }
    .img-wrapper-2 { bottom: 0px; right: auto; left: 5%; }
    
    .features-section, .browse-section, .how-it-works-section, .newsletter-section {
        padding: 5rem 5%;
    }
    
    .hiw-step {
        flex-direction: column !important;
        gap: 2rem;
        text-align: center;
    }
    .hiw-badge { margin: 0 auto 1rem auto; }
    .hiw-img { width: 100%; }
    
    .browse-grid {
        grid-template-columns: 1fr;
    }
    
    .newsletter-card {
        padding: 3rem 5%;
        text-align: center;
    }
    .newsletter-title { font-size: 2rem; }
    .newsletter-input-group {
        flex-direction: column;
        margin: 0 auto;
    }
    .footer-content {
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }
}
</style>
<div class="landing-wrapper">"""

content = content.replace('</style>\n\n<div class="landing-wrapper">', responsive_css)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Responsive CSS added.")
