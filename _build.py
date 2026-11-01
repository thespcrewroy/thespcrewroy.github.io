# Generates the static HTML pages from one shared template.
# Run:  python3 _build.py   (edit content below, then re-run)
import pathlib

ROOT = pathlib.Path(__file__).parent

LINKEDIN = "https://www.linkedin.com/in/swapnil-roy"
GITHUB = "https://github.com/thespcrewroy"
EMAIL = "royswapnil07@gmail.com"
MEDIUM_LIST = "https://medium.com/@sr42946/list/new-media-case-study-collection-0e82a201ecae"
MEDIUM_PROFILE = "https://medium.com/@sr42946"
NMIX_REPO = "https://github.com/thespcrewroy/NMIX4030-NativeAppDev"
SWE_REPO = "https://github.com/thespcrewroy/SoftwareEngineeringTutorials"

# ---------- sticker icons (original SVGs) ----------
ICONS = {
"about": """<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="12" y="6" width="40" height="52" rx="5" fill="#fffdf4" stroke="#1a1a1a" stroke-width="3"/><path d="M20 20h24M20 29h24M20 38h24M20 47h14" stroke="#1fa2e6" stroke-width="3" stroke-linecap="round"/><rect x="24" y="2" width="16" height="9" rx="3" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/></svg>""",
"projects": """<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M6 16a4 4 0 0 1 4-4h14l6 6h24a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H10a4 4 0 0 1-4-4z" fill="#ffa62b" stroke="#1a1a1a" stroke-width="3"/><path d="M6 26h52" stroke="#1a1a1a" stroke-width="3"/><path d="M24 36l-5 5 5 5M40 36l5 5-5 5M34 34l-4 14" fill="none" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/></svg>""",
"resume": """<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M14 4h26l12 12v42a3 3 0 0 1-3 3H14a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3z" fill="#fffdf4" stroke="#1a1a1a" stroke-width="3"/><path d="M40 4v12h12" fill="#cfe3f2" stroke="#1a1a1a" stroke-width="3"/><path d="M19 26h26M19 33h26M19 40h18" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/><rect x="6" y="44" width="30" height="14" rx="4" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><text x="21" y="55" font-family="monospace" font-weight="700" font-size="10" text-anchor="middle" fill="#fff">PDF</text></svg>""",
"cases": """<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="8" y="40" width="48" height="12" rx="3" fill="#20b8b0" stroke="#1a1a1a" stroke-width="3"/><rect x="12" y="28" width="42" height="12" rx="3" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><rect x="10" y="16" width="44" height="12" rx="3" fill="#1fa2e6" stroke="#1a1a1a" stroke-width="3"/><path d="M42 16v-10l4 3 4-3v10" fill="#ffd21f" stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round"/></svg>""",
"contact": """<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="6" y="14" width="52" height="36" rx="5" fill="#fffdf4" stroke="#1a1a1a" stroke-width="3"/><path d="M8 17l24 18 24-18" fill="none" stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round"/><circle cx="50" cy="16" r="8" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><text x="50" y="20" font-family="sans-serif" font-weight="900" font-size="11" text-anchor="middle" fill="#fff">!</text></svg>""",
"github": """<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="6" y="10" width="52" height="44" rx="6" fill="#1a1a1a" stroke="#1a1a1a" stroke-width="3"/><rect x="6" y="10" width="52" height="10" rx="4" fill="#fffdf4" stroke="#1a1a1a" stroke-width="3"/><path d="M16 32l7 5-7 5" fill="none" stroke="#ffd21f" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M28 43h14" stroke="#20b8b0" stroke-width="3.5" stroke-linecap="round"/></svg>""",
# decorative stickers
"belt": """<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="4" y="18" width="56" height="11" rx="3" fill="#1a1a1a" stroke="#1a1a1a" stroke-width="2"/><path d="M27 28 L18 54 L25 56 L31 31 Z M37 28 L46 54 L39 56 L33 31 Z" fill="#1a1a1a" stroke="#1a1a1a" stroke-width="2" stroke-linejoin="round"/><rect x="25" y="14" width="14" height="19" rx="4" fill="#1a1a1a" stroke="#fffdf4" stroke-width="2.5"/><path d="M19 49l6 2M45 49l-6 2" stroke="#ffd21f" stroke-width="2.5"/></svg>""",
"coffee": """<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M12 24h34v18a12 12 0 0 1-12 12H24a12 12 0 0 1-12-12z" fill="#fffdf4" stroke="#1a1a1a" stroke-width="3"/><path d="M46 28h4a7 7 0 0 1 0 14h-4" fill="none" stroke="#1a1a1a" stroke-width="3"/><rect x="12" y="30" width="34" height="8" fill="#ee4057"/><path d="M22 8c-3 4 3 6 0 10M32 8c-3 4 3 6 0 10" fill="none" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/></svg>""",
"shield": """<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M32 4l22 8v16c0 15-10 25-22 31C20 53 10 43 10 28V12z" fill="#20b8b0" stroke="#1a1a1a" stroke-width="3"/><path d="M22 31l7 7 13-14" fill="none" stroke="#fffdf4" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>""",
"coin": """<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="24" fill="#ffd21f" stroke="#1a1a1a" stroke-width="3"/><circle cx="32" cy="32" r="17" fill="none" stroke="#f5b800" stroke-width="3"/><text x="32" y="41" font-family="sans-serif" font-weight="900" font-size="24" text-anchor="middle" fill="#1a1a1a">$</text></svg>""",
"paw": """<svg viewBox="0 0 64 64" aria-hidden="true"><ellipse cx="32" cy="42" rx="14" ry="12" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><circle cx="16" cy="26" r="6" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><circle cx="26" cy="16" r="6" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><circle cx="38" cy="16" r="6" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/><circle cx="48" cy="26" r="6" fill="#ee4057" stroke="#1a1a1a" stroke-width="3"/></svg>""",
}

NAV = [
    ("/", "home", None),
    ("/about/", "about.txt", "about"),
    ("/projects/", "projects/", "projects"),
    ("/resume/", "resume.pdf", "resume"),
    ("/contact/", "contact.exe", "contact"),
]

def page(path, title, description, body, extra_head="", extra_scripts=""):
    active = path
    nav_links = []
    for href, label, _ in NAV[1:]:
        cur = ' aria-current="page"' if href == active else ""
        nav_links.append(f'<a href="{href}"{cur}>{label}</a>')
    nav_links.append(f'<a href="{MEDIUM_LIST}" target="_blank" rel="noopener">case-studies.md</a>')
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="/assets/img/swapnil-roy.jpg">
  <link rel="icon" href="/assets/img/logo.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Lilita+One&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="/assets/css/style.css">{extra_head}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <main id="main" class="wrap">
{body}
    <footer class="site-foot">
      <p>&copy; <span id="year">2026</span> Swapnil Roy &middot; hand-coded with HTML, CSS, JavaScript &amp; Three.js</p>
    </footer>
  </main>

  <nav class="taskbar" aria-label="Main">
    <a class="start" href="/"><img src="/assets/img/logo.svg" alt="">Swapnil Roy</a>
    {' '.join(nav_links)}
    <span class="clock" id="clock" aria-hidden="true"></span>
  </nav>
  <script src="/assets/js/main.js"></script>{extra_scripts}
</body>
</html>
"""
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

def window(title, inner, close=True, cls=""):
    x = '<a class="window__close" href="/" aria-label="Close and go home">✕</a>' if close else ""
    return f"""<section class="paper window {cls}">
      <div class="window__bar"><span class="window__dots" aria-hidden="true"><span></span><span></span><span></span></span><span class="window__title">{title}</span>{x}</div>
      <div class="window__body">
{inner}
      </div>
    </section>"""

# ======================= HOME =======================
icons = [
    ("/about/", "about.txt", "about", ""),
    ("/projects/", "projects/", "projects", ""),
    ("/resume/", "resume.pdf", "resume", ""),
    (MEDIUM_LIST, "case-studies.md", "cases", ' target="_blank" rel="noopener"'),
    ("/contact/", "contact.exe", "contact", ""),
    (GITHUB, "github.sh", "github", ' target="_blank" rel="noopener"'),
]
icon_html = "\n".join(
    f'        <a class="icon" href="{h}"{ext}>{ICONS[k]}<span>{label}</span></a>' for h, label, k, ext in icons
)
stickers = [
    ("belt", "1st Dan black belt"), ("shield", "Security+ certified"), ("coin", "fintech nerd"),
    ("coffee", "runs on coffee"), ("paw", "Go Dawgs"),
]
sticker_html = "\n".join(f'        <div class="sticker">{ICONS[k]}<span>{t}</span></div>' for k, t in stickers)

home_body = f"""    <div class="hero">
      {window("hello.exe", f'''        <p class="hero__lead">click on the icons below to find out more!</p>
        <h1>hi, i'm <span class="name-pill">Swapnil</span></h1>
        <p class="tagline">Securing the systems that move money.</p>
        <div class="stage" id="stage">
          <div class="stage__fallback"><img src="/assets/img/logo.svg" alt="Cartoon padlock mascot with eyes"></div>
          <button class="unlock-btn" id="unlock-btn" type="button" aria-pressed="false">🔒 click to unlock</button>
        </div>''', close=False)}
      <aside class="paper note tape" aria-labelledby="about-me">
        <figure class="photo"><img src="/assets/img/swapnil-roy.jpg" alt="Headshot of Swapnil Roy in a suit and tie" width="640" height="640"></figure>
        <h2 id="about-me">About me</h2>
        <p>I'm a Computer Science senior at the University of Georgia working where <strong>cybersecurity</strong>, <strong>software engineering</strong> and <strong>fintech</strong> meet.</p>
        <ul class="facts">
          <li>Cybersecurity risk analyst intern, CyberArch</li>
          <li>SOC analyst intern, UGA EITS</li>
          <li>President, UGA Society for Cyber Security</li>
          <li>Graduating May 2027 &middot; Cumming, GA</li>
        </ul>
      </aside>
    </div>

    <section class="desktop" aria-labelledby="desktop-title">
      <h2 id="desktop-title" class="desktop__hint">C:\\Users\\swapnil\\Desktop&gt; dir</h2>
      <div class="icons">
{icon_html}
      </div>
    </section>

    <section class="stickers" aria-label="A few things about me">
{sticker_html}
    </section>"""

page("/", "Swapnil Roy | Cybersecurity, Software & FinTech",
     "Portfolio of Swapnil Roy, a UGA Computer Science senior working at the intersection of cybersecurity, software engineering and fintech.",
     home_body,
     extra_head="""
  <script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>""",
     extra_scripts='\n  <script type="module" src="/assets/js/hero.js"></script>')

# ======================= ABOUT =======================
about_inner = f"""        <div class="about-grid">
          <figure class="polaroid"><img src="/assets/img/swapnil-roy.jpg" alt="Headshot of Swapnil Roy" width="640" height="640"><figcaption>that's me!</figcaption></figure>
          <div>
            <h1>about.txt</h1>
            <p>Hi! I'm Swapnil, a Computer Science senior at the University of Georgia (May 2027), with minors in FinTech and Informatics and the New Media Certificate.</p>
            <p>I like work that sits between the technical and the human side of security. At <strong>CyberArch</strong>, I help Georgia local governments, schools and businesses assess their security against the CIS Controls and the NIST Cybersecurity Framework, then turn the findings into reports leaders can act on. In UGA's <strong>Security Operations Center</strong>, I investigate reported phishing emails. Before that, I built an internal web app on Microsoft Azure as a <strong>Software Engineering Intern at Voya Financial</strong>.</p>
            <p>My goal is a career securing the systems that move money, where cybersecurity, software engineering and fintech overlap.</p>
            <h2>Outside of work</h2>
            <p>I lead the UGA Society for Cyber Security as president, keep the books for The Hack Pack (our competitive CTF club), co-founded a startup called Tabula Rasa and write on Medium. Off the keyboard, I'm a Kukkiwon 1st Dan black belt in Taekwondo, I'm learning software-defined radio, and I'll never skip a Bon Jovi song.</p>
            <h2>Honors &amp; certifications</h2>
            <p>
              <span class="chip chip--red">Phi Beta Kappa</span><span class="chip chip--red">Omicron Delta Kappa</span><span class="chip chip--red">CURO Research Award</span>
              <span class="chip chip--teal">CompTIA Security+</span><span class="chip chip--teal">Google Cybersecurity</span><span class="chip chip--teal">MIT Cybersecurity for Critical Urban Infrastructure</span><span class="chip chip--teal">CCSMM</span>
            </p>
          </div>
        </div>"""
page("/about/", "About | Swapnil Roy", "About Swapnil Roy: UGA Computer Science senior, cybersecurity risk analyst intern and president of the UGA Society for Cyber Security.",
     window("about.txt — notepad", about_inner))

# ======================= PROJECTS =======================
projects = [
    ("Cybersecurity Risk Assessments", "CyberArch, Carl Vinson Institute of Government &middot; 2026–present",
     "Guide Georgia local governments, schools and businesses through risk reviews against the CIS Controls and NIST CSF, testing 100+ Implementation Group 1 safeguards and writing reports that tell leaders which gaps to fix first.",
     ["GRC", "NIST CSF", "CIS Controls", "Excel"], []),
    ("AI Change-Risk Agent", "Mastercard capstone, Terry FinTech Certificate &middot; Fall 2026",
     "With a five-person cross-functional team, researched where AI can safely cut manual approvals in technology operations, and built a demo agent that scores the risk of IT change requests using synthetic data.",
     ["AI governance", "Risk", "FinTech"], []),
    ("Email Campaign Tracker", "Voya Financial &middot; Summer 2025",
     "Built an internal web app on Azure Functions and SQL Server that tracks email campaign responses automatically, then presented its design and testing results to senior leadership.",
     ["Azure Functions", "C# / .NET", "SQL Server", "Azure DevOps"], []),
    ("Jukebox iOS App", "NMIX 4030: Native App Development &middot; Spring 2024",
     "A one-tap SwiftUI jukebox with reusable song cards, play/pause controls and a live progress slider powered by AVFoundation.",
     ["Swift", "SwiftUI", "AVFoundation"],
     [("Case study", MEDIUM_LIST), ("Code", f"{NMIX_REPO}/tree/main/Projects/03.%20Jukebox")]),
    ("Random Trivia iOS App", "NMIX 4030: Native App Development &middot; Spring 2024",
     "A SwiftUI quiz app that pulls live questions from a public API, decodes JSON with Codable and keeps score across questions.",
     ["Swift", "SwiftUI", "REST API", "Codable"],
     [("Case study", MEDIUM_LIST), ("Code", f"{NMIX_REPO}/tree/main/Projects/02.%20RandomtTrivia")]),
    ("Software Engineering Tutorials", "Open-source knowledge base &middot; ongoing",
     "A curated, categorized guide to hundreds of software engineering tools, from frontend frameworks to DevOps, that I maintain for students learning the field.",
     ["Open source", "Documentation", "GitHub"], [("Repo", SWE_REPO)]),
]
cards = []
for name, meta, desc, tags, links in projects:
    tag_html = "".join(f'<span class="chip">{t}</span>' for t in tags)
    link_html = "".join(f'<a class="btn" href="{u}" target="_blank" rel="noopener">{l} <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a>' for l, u in links)
    cards.append(f"""          <article class="card">
            <h3>{name}</h3>
            <p class="meta">{meta}</p>
            <p>{desc}</p>
            <p>{tag_html}</p>
            {f'<div class="links">{link_html}</div>' if links else ''}
          </article>""")
projects_inner = f"""        <div class="page-head"><h1>projects/</h1><span class="chip chip--orange">{len(projects)} items</span></div>
        <div class="grid-3">
{chr(10).join(cards)}
        </div>
        <p style="margin-top:28px">Want the full write-ups? Read my <a href="{MEDIUM_LIST}" target="_blank" rel="noopener">New Media case studies on Medium</a>.</p>"""
page("/projects/", "Projects | Swapnil Roy", "Featured projects by Swapnil Roy: cybersecurity risk assessments, an AI change-risk agent, an Azure web app and SwiftUI iOS apps.",
     window("C:\\Users\\swapnil\\projects", projects_inner))

# ======================= RESUME =======================
resume_inner = """        <div class="page-head"><h1>resume.pdf</h1>
          <a class="btn btn--red" href="/assets/Swapnil-Roy-Resume.pdf" download><i class="fa-solid fa-download" aria-hidden="true"></i> Download PDF</a>
        </div>
        <div class="grid-2">
          <div>
            <h2>Experience</h2>
            <ol class="timeline">
              <li><strong>Cybersecurity Risk Analyst Intern</strong> CyberArch, UGA Carl Vinson Institute of Government<br><span>Jan 2026 – present</span></li>
              <li><strong>Security Operations Center Analyst Intern</strong> UGA Enterprise Information Technology Services<br><span>Jun 2026 – present</span></li>
              <li><strong>Software Engineering Intern</strong> Voya Financial<br><span>Jun 2025 – Aug 2025</span></li>
              <li><strong>President</strong> UGA Society for Cyber Security<br><span>Apr 2025 – present</span></li>
            </ol>
          </div>
          <div>
            <h2>Education</h2>
            <p><strong>University of Georgia</strong><br>B.S. Computer Science, May 2027<br>Minors: FinTech, Informatics &middot; New Media Certificate</p>
            <h2>Skills</h2>
            <p>
              <span class="chip chip--teal">NIST CSF</span><span class="chip chip--teal">CIS Controls</span><span class="chip chip--teal">CMMC</span><span class="chip chip--teal">Risk Assessments</span>
              <span class="chip chip--blue">Python</span><span class="chip chip--blue">SQL</span><span class="chip chip--blue">C# / .NET</span><span class="chip chip--blue">Swift</span><span class="chip chip--blue">Microsoft Azure</span>
              <span class="chip chip--red">Microsoft Defender</span><span class="chip chip--red">Entra ID</span><span class="chip chip--red">Microsoft 365</span>
            </p>
            <div class="terminal" aria-label="Certifications"><span class="prompt">$</span> cat certs.txt<br>CompTIA Security+<br>Google Cybersecurity Certificate<br>MIT Cybersecurity for Critical Urban Infrastructure<br>Community Cyber Security Maturity Model (CCSMM)</div>
          </div>
        </div>"""
page("/resume/", "Resume | Swapnil Roy", "Resume of Swapnil Roy: cybersecurity, GRC and software engineering experience at CyberArch, UGA EITS and Voya Financial.",
     window("resume.pdf — viewer", resume_inner))

# ======================= CONTACT =======================
contact_inner = f"""        <div class="grid-2">
          <div>
            <h1>contact.exe</h1>
            <p>I'm looking for cybersecurity, GRC and fintech roles starting in 2027, and I'm always happy to talk about speaking at the UGA Society for Cyber Security. Say hi!</p>
            <ul class="contact-list">
              <li><a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i>{EMAIL}</a></li>
              <li><a href="{LINKEDIN}" target="_blank" rel="noopener"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i>LinkedIn</a></li>
              <li><a href="{GITHUB}" target="_blank" rel="noopener"><i class="fa-brands fa-github" aria-hidden="true"></i>GitHub</a></li>
              <li><a href="{MEDIUM_PROFILE}" target="_blank" rel="noopener"><i class="fa-brands fa-medium" aria-hidden="true"></i>Medium</a></li>
            </ul>
          </div>
          <div class="terminal" aria-hidden="true">
            <span class="prompt">swapnil@uga:~$</span> ./contact.exe<br>
            &gt; establishing secure connection...<br>
            &gt; handshake complete ✔<br>
            &gt; status: <span class="prompt">open to opportunities</span><br>
            &gt; response time: ~24 hours<br>
            <span class="prompt">swapnil@uga:~$</span> _
          </div>
        </div>"""
page("/contact/", "Contact | Swapnil Roy", "Contact Swapnil Roy by email, LinkedIn, GitHub or Medium.",
     window("contact.exe", contact_inner))

print("built")
