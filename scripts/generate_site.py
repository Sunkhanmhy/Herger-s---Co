"""Static site generator: renders every page from Jinja2 templates + content data.

Run with: python3 scripts/generate_site.py  (see package.json "build:site").
"""
from __future__ import annotations

import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import base_context, PRACTICES, image_for  # noqa: E402

env = Environment(
    loader=FileSystemLoader(str(ROOT / "scripts" / "templates")),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
)
env.globals["image_for"] = image_for


def render_page(template_name: str, output_path: Path, context: dict) -> None:
    template = env.get_template(template_name)
    html = template.render(**context)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    word_count = len(html.split())
    print(f"  wrote {output_path.relative_to(ROOT)}  (~{word_count} words incl. markup)")


def main() -> None:
    from content import home, about, partners, clients, careers
    from content import news_events, publications, contact as contact_content
    from content.practices import PRACTICE_PAGES

    print("Building Herger & Co. static site...")

    render_page("pages/home.html", ROOT / "index.html", {
        **base_context("", "home"), **home.CONTEXT,
    })

    render_page("pages/about.html", ROOT / "company" / "about.html", {
        **base_context("../", "company"), **about.CONTEXT,
    })
    render_page("pages/partners.html", ROOT / "company" / "partners.html", {
        **base_context("../", "company"), **partners.CONTEXT,
    })
    render_page("pages/clients.html", ROOT / "company" / "clients.html", {
        **base_context("../", "company"), **clients.CONTEXT,
    })
    render_page("pages/careers.html", ROOT / "company" / "careers.html", {
        **base_context("../", "company"), **careers.CONTEXT,
    })

    for index, practice in enumerate(PRACTICES):
        slug = practice["slug"]
        page_ctx = dict(PRACTICE_PAGES[slug])
        others = PRACTICES[:index] + PRACTICES[index + 1:]
        page_ctx["related_practices"] = others[:4]
        render_page("pages/practice.html", ROOT / "practices" / f"{slug}.html", {
            **base_context("../", "practices"), **page_ctx,
        })

    render_page("pages/news_events.html", ROOT / "news-events.html", {
        **base_context("", "news"), **news_events.CONTEXT,
    })
    render_page("pages/publications.html", ROOT / "publications.html", {
        **base_context("", "publications"), **publications.CONTEXT,
    })
    render_page("pages/contact.html", ROOT / "contact.html", {
        **base_context("", "contact"), **contact_content.CONTEXT,
    })

    print("Done.")


if __name__ == "__main__":
    main()
