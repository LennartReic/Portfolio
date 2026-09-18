#!/usr/bin/env python3
"""Builds the static portfolio pages from _build/content.py.

Run from the repository root:  python3 _build/build.py
Output: index.html, work/*.html, research/*.html (plus redirect pages for old URLs).
"""
import html
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_build"))
import content as C  # noqa: E402

FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
)


def img_src(base, name, sizes):
    """Return src + srcset for an image saved as assets/img/<name>-<w>.jpg"""
    sizes = sorted(sizes)
    srcset = ", ".join(f"{base}assets/img/{name}-{w}.jpg {w}w" for w in sizes)
    src = f"{base}assets/img/{name}-{sizes[-1]}.jpg"
    return src, srcset


def picture(base, name, sizes, alt, sizes_attr="100vw", cls="", loading="lazy", extra=""):
    src, srcset = img_src(base, name, sizes)
    cls_attr = f' class="{cls}"' if cls else ""
    return (f'<img{cls_attr} src="{src}" srcset="{srcset}" sizes="{sizes_attr}" '
            f'alt="{html.escape(alt, quote=True)}" loading="{loading}" decoding="async"{extra}>')


def head(base, title, description, og_image=None):
    og = f'{base}assets/img/las/dancefloor-2026-1920.jpg' if og_image is None else og_image
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(description, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{og}">
<meta name="theme-color" content="#F6F3EE">
<link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
{FONT_LINK}
<link rel="stylesheet" href="{base}assets/css/style.css">
<noscript><style>.reveal{{opacity:1;transform:none}}</style></noscript>
</head>"""


def nav(base, current=None):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    home = f"{base}index.html"
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<nav class="site-nav" aria-label="Main">
  <a class="nav-brand" href="{home}">{C.SITE['name']}</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links">Menu</button>
  <ul class="nav-links" id="nav-links">
    {link(home + '#work', 'Work', 'work')}
    {link(home + '#research', 'Research', 'research')}
    {link(home + '#about', 'About', 'about')}
    {link(home + '#contact', 'Contact', 'contact')}
  </ul>
</nav>"""


def footer(base):
    s = C.SITE
    return f"""<footer class="site-footer">
  <span>© 2026 {s['name']} · Copenhagen</span>
  <span><a href="mailto:{s['email']}">{s['email']}</a> · <a href="{s['linkedin']}" rel="me noopener" target="_blank">LinkedIn</a></span>
</footer>
<script src="{base}assets/js/main.js" defer></script>
</body>
</html>"""


# ---------------------------------------------------------------- home page

def build_index():
    base = ""
    s = C.SITE
    tiles = []
    for w in C.WORK:
        tiles.append(f"""
      <a class="work-card reveal" href="work/{w['slug']}.html">
        <div class="work-card__media">{picture(base, w['image'], w['sizes'], w['title'].replace('&amp;', '&'), sizes_attr="(max-width: 760px) 100vw, 50vw")}</div>
        <p class="eyebrow">{w['eyebrow']}</p>
        <h3 class="work-card__title">{w['title']}</h3>
        <p class="work-card__desc">{w['tile']}</p>
      </a>""")
    rows = []
    for i, r in enumerate(C.RESEARCH, 1):
        rows.append(f"""
      <a class="research-row reveal" href="research/{r['slug']}.html">
        <span class="research-row__num">0{i}</span>
        <span>
          <span class="research-row__title">{r['title']}</span>
          <p class="research-row__q">{r['question']}</p>
        </span>
        <span class="research-row__meta">{r['meta']}</span>
        <span class="research-row__arrow" aria-hidden="true">→</span>
      </a>""")
    facts = "".join(f"<div><dt class=\"eyebrow\">{k}</dt><dd>{v}</dd></div>" for k, v in C.ABOUT["facts"])
    about_ps = "".join(f"<p>{p}</p>" for p in C.ABOUT["paragraphs"])
    poster = "assets/img/las/dancefloor-2026-1920.jpg"

    return f"""{head(base, f"{s['name']} · Urban Planner", s['description'])}
<body class="has-hero">
{nav(base)}
<main id="main">
  <header class="hero">
    <img class="hero-poster" src="{poster}" alt="" aria-hidden="true">
    <video class="hero-video" muted loop playsinline preload="metadata" poster="{poster}"
      data-src-large="assets/video/hero-loop-1600.mp4" data-src-small="assets/video/hero-loop-540.mp4" aria-hidden="true"></video>
    <div class="hero-shade"></div>
    <div class="hero-content">
      <div>
        <h1 class="hero-name">Lennart<br>Reichow</h1>
        <p class="hero-tagline">{s['tagline']}</p>
        <p class="hero-meta">{s['meta_line']}</p>
      </div>
      <blockquote class="hero-quote">
        <p>{s['quote']}</p>
        <cite>{s['quote_by']}</cite>
      </blockquote>
    </div>
  </header>

  <section class="section" id="work">
    <div class="section-head reveal">
      <h2 class="section-title">Selected work</h2>
      <span class="eyebrow">04 projects</span>
    </div>
    <div class="work-grid">{''.join(tiles)}
    </div>
  </section>

  <section class="section" id="research">
    <div class="section-head reveal">
      <h2 class="section-title">Research</h2>
      <span class="eyebrow">04 studies</span>
    </div>
    <div class="research-list">{''.join(rows)}
    </div>
  </section>

  <section class="section" id="about">
    <div class="section-head reveal">
      <h2 class="section-title">About</h2>
      <span class="eyebrow">Lennart Reichow</span>
    </div>
    <div class="about reveal">
      <img class="about-portrait" src="assets/img/about/portrait-1200.jpg" alt="Portrait of Lennart Reichow" loading="lazy" width="886" height="886">
      <div class="about-text">
        {about_ps}
        <dl class="about-facts">{facts}</dl>
        <div class="about-links">
          <a href="assets/cv-lennart-reichow.pdf" target="_blank" rel="noopener">Download CV (PDF) ↗</a>
          <a href="{s['linkedin']}" target="_blank" rel="me noopener">LinkedIn ↗</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="contact">
    <div class="section-head reveal">
      <h2 class="section-title">Contact</h2>
      <span class="eyebrow">Get in touch</span>
    </div>
    <div class="reveal">
      <p class="contact-lead">Interested in my work? I'm happy to hear from you.</p>
      <a class="contact-email" href="mailto:{s['email']}">{s['email']}</a>
      <div class="contact-links">
        <a href="{s['linkedin']}" target="_blank" rel="me noopener">LinkedIn ↗</a>
        <span>Copenhagen, Denmark</span>
      </div>
    </div>
  </section>
</main>
{footer(base)}"""


# ------------------------------------------------------------ project pages

def figure_html(base, f, cover=False):
    cls = "figure" + (" figure--framed" if f.get("framed") else "") + (" figure--max" if f.get("max") else "")
    style = f' style="max-width:{f["max"]}px"' if f.get("max") else ""
    img = picture(base, f["src"], f["sizes"], f.get("alt", ""), sizes_attr="(max-width: 900px) 100vw, 1000px")
    cap = f"<figcaption>{f['caption']}</figcaption>" if f.get("caption") else ""
    return f'<figure class="{cls}"{style}>{img}{cap}</figure>'


WIDE = {"figure", "figgrid", "video", "youtube"}


def inner_html(base, block):
    """HTML of one block without its grid wrapper."""
    kind, data = block
    if kind == "h2":
        return f'<h2>{data}</h2>'
    if kind == "p":
        return f'<p>{data}</p>'
    if kind == "ul":
        return '<ul>' + "".join(f"<li>{i}</li>" for i in data) + '</ul>'
    if kind == "cta":
        return (f'<div class="cta"><p>{data}</p>'
                f'<a class="cta-link" href="mailto:{C.SITE["email"]}">Write me: {C.SITE["email"]}</a></div>')
    if kind == "figure":
        return figure_html(base, data)
    if kind == "figgrid":
        cls = "fig-grid" + (" fig-grid--cover" if data.get("cover") else " fig-grid--natural")
        return f'<div class="{cls}">' + "".join(figure_html(base, f) for f in data["items"]) + '</div>'
    if kind == "video":
        cap = f"<figcaption>{data['caption']}</figcaption>" if data.get("caption") else ""
        return (f'<figure class="video-wrap"><video class="inline-video" muted loop playsinline preload="metadata" '
                f'poster="{base}assets/img/{data["poster"]}.jpg" src="{base}{data["src"]}"></video>{cap}</figure>')
    if kind == "youtube":
        src, srcset = img_src(base, data["poster"], data["sizes"])
        cap = f"<figcaption>{data['caption']}</figcaption>" if data.get("caption") else ""
        return (f'<figure class="figure"><div class="yt" data-id="{data["id"]}" data-title="{html.escape(data["title"], quote=True)}">'
                f'<img src="{src}" srcset="{srcset}" sizes="(max-width: 900px) 100vw, 1000px" alt="" loading="lazy">'
                f'<button type="button" aria-label="Play video: {html.escape(data["title"], quote=True)}">'
                f'<span class="play"></span><span class="label">Play video</span></button></div>{cap}</figure>')
    raise ValueError(kind)


def blocks_html(base, blocks):
    """Group consecutive text blocks into one column segment; wide blocks get their own full-width row."""
    out, seg = [], []

    def flush():
        if seg:
            out.append('<div class="block reveal">' + "".join(seg) + '</div>')
            seg.clear()

    for b in blocks:
        if b[0] in WIDE:
            flush()
            out.append('<div class="block block--wide reveal">' + inner_html(base, b) + '</div>')
        else:
            seg.append(inner_html(base, b))
    flush()
    return "".join(out)


def build_page(slug):
    p = C.PAGES[slug]
    base = "../"
    section = p["section"]
    current = "work" if section == "work" else "research"
    hero = ""
    og = None
    if p.get("hero"):
        h = p["hero"]
        cls = "page-hero" + (" page-hero--contain" if h.get("contain") else "")
        hero_img = picture(base, h["src"], h["sizes"], h["alt"], loading="eager", extra=' fetchpriority="high"')
        hero = f'<figure class="{cls}">{hero_img}</figure>'
        og = f"../assets/img/{h['src']}-{max(h['sizes'])}.jpg"
    meta = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in p["meta"])
    blocks = blocks_html(base, p["blocks"])

    # next project
    order = C.ORDER
    nxt_slug = order[(order.index(slug) + 1) % len(order)]
    nxt = C.PAGES[nxt_slug]
    nxt_href = f"../{nxt['section']}/{nxt_slug}.html"
    nxt_label = "Next project" if nxt["section"] == "work" else "Next research project"

    plain_title = html.unescape(p["title"])
    return f"""{head(base, f"{plain_title} · {C.SITE['name']}", p['description'], og)}
<body class="subpage">
{nav(base, current)}
<main id="main">
  {hero}
  <header class="page-head">
    <p class="eyebrow">{p['eyebrow']}</p>
    <h1 class="page-title">{p['title']}</h1>
    <p class="page-lead">{p['subtitle']}</p>
  </header>
  <div class="page-body">
    <aside class="page-aside">
      <dl class="meta">{meta}</dl>
    </aside>
    {blocks}
  </div>
  <nav class="next" aria-label="Next project">
    <p class="eyebrow">{nxt_label}</p>
    <a href="{nxt_href}"><span>{nxt['title']}</span><span class="arrow" aria-hidden="true">→</span></a>
  </nav>
</main>
{footer(base)}"""


def redirect_page(target, title):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">
</head><body><p>This page has moved to <a href="{target}">{target}</a>.</p></body></html>
"""


def main():
    os.chdir(ROOT)
    os.makedirs("work", exist_ok=True)
    os.makedirs("research", exist_ok=True)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(build_index())
    for slug, p in C.PAGES.items():
        path = f"{p['section']}/{slug}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_page(slug))
    # redirects for the URLs of the previous version of the site
    old = {
        "student-study.html": "work/student-study.html",
        "lyngten-bazar.html": "work/lygten-bazar.html",
        "lost-sound.html": "work/lost-and-sound.html",
        "city-apps.html": "research/city-apps.html",
        "strategic-partnerships.html": "research/strategic-partnerships.html",
        "adult-play.html": "research/adult-play.html",
        "helsinki-tallinn.html": "research/helsinki-tallinn.html",
    }
    for src, target in old.items():
        with open(src, "w", encoding="utf-8") as f:
            f.write(redirect_page(target, "Moved"))
    print("built index.html,", len(C.PAGES), "pages,", len(old), "redirects")


if __name__ == "__main__":
    main()
