"""Shared navigation/site data used by every page's Jinja2 context."""
from datetime import date

from content.footer import FOOTER

# ---------------------------------------------------------------------------
# Image resolution: maps every `image_label`/`image_label` placeholder string
# used across scripts/content/*.py to a real, downloaded, royalty-free stock
# photo under assets/images/shared/ (see assets/images/shared for licenses —
# all sourced from Pixabay's Content License, free for commercial use, no
# attribution required). Matching is keyword-based so new content labels are
# automatically routed to a sensible category without code changes; images
# rotate round-robin within a category so repeated labels aren't identical.
# ---------------------------------------------------------------------------
_IMAGE_POOL = {
    "portrait": [f"assets/images/shared/portrait-{i:02d}.jpg" for i in (3, 5, 8)],
    "mining": [f"assets/images/shared/mining-{i:02d}.jpg" for i in range(1, 4)],
    "shipping": ["assets/images/shared/shipping-02.jpg"],
    "courtroom": [f"assets/images/shared/courtroom-{i:02d}.jpg" for i in range(1, 5)],
    "office": [f"assets/images/shared/office-{i:02d}.jpg" for i in range(1, 4)],
}

_KEYWORD_CATEGORIES = [
    (("portrait", "team", "partner", "associate", "attorney", "member", "leadership",
      "secretary", "counsel", "managing"), "portrait"),
    (("mining", "mine", "quarry", "exploration", "tin", "tantalite", "limestone",
      "processing facility", "manufacturing"), "mining"),
    (("ship", "vessel", "cargo", "port", "container", "maritime", "customs", "lng",
      "logistics", "trade"), "shipping"),
    (("court", "hearing", "litigation", "arbitration", "tribunal", "judgment",
      "investigation", "consultation", "audit", "legal"), "courtroom"),
]
_DEFAULT_CATEGORY = "office"

_category_counters: dict[str, int] = {}


def image_for(label: str) -> str:
    """Resolve a content image_label string to a local asset path (see above)."""
    text = (label or "").lower()
    category = _DEFAULT_CATEGORY
    for keywords, cat in _KEYWORD_CATEGORIES:
        if any(keyword in text for keyword in keywords):
            category = cat
            break
    pool = _IMAGE_POOL[category]
    index = _category_counters.get(category, 0)
    _category_counters[category] = index + 1
    return pool[index % len(pool)]


PRACTICES = [
    {"slug": "mining-production-law", "label": "Mining & Production Law",
     "short_label": "Mining & Production Law"},
    {"slug": "taxation-and-policies", "label": "Taxation & Policies",
     "short_label": "Taxation & Policies"},
    {"slug": "shipping-international-trade", "label": "Shipping & International Trade",
     "short_label": "Shipping & Int'l Trade"},
    {"slug": "risk-regulatory-compliance", "label": "Risk & Regulatory Compliances",
     "short_label": "Risk & Compliance"},
    {"slug": "white-collar-defence", "label": "White Collar Defence",
     "short_label": "White Collar Defence"},
    {"slug": "real-estate-management", "label": "Real Estate & Management",
     "short_label": "Real Estate & Mgmt"},
    {"slug": "capital-markets-securities", "label": "Capital Markets & Securities",
     "short_label": "Capital Markets"},
    {"slug": "privatization-venture-capital", "label": "Privatization & Venture Capital",
     "short_label": "Privatization & VC"},
    {"slug": "mergers-acquisitions", "label": "Mergers & Acquisition",
     "short_label": "Mergers & Acquisition"},
    {"slug": "media-entertainment-law", "label": "Media & Entertainment Law",
     "short_label": "Media & Entertainment"},
    {"slug": "litigation-adr", "label": "Litigation & ADR Law",
     "short_label": "Litigation & ADR"},
    {"slug": "corporate-governance", "label": "Corporate Governance",
     "short_label": "Corporate Governance"},
]


def build_nav(base: str, active: str = "") -> list[dict]:
    return [
        {"label": "Home", "href": f"{base}index.html", "active": active == "home"},
        {
            "label": "Company",
            "active": active == "company",
            "children": [
                {"label": "About Herger's & Co.", "href": f"{base}company/about.html"},
                {"label": "Our Partners", "href": f"{base}company/partners.html"},
                {"label": "Our Clients", "href": f"{base}company/clients.html"},
                {"label": "Careers & Positions", "href": f"{base}company/careers.html"},
            ],
        },
        {
            "label": "Practices & Law",
            "active": active == "practices",
            "children": [
                {"label": p["label"], "href": f"{base}practices/{p['slug']}.html"}
                for p in PRACTICES
            ],
        },
        {"label": "News & Events", "href": f"{base}news-events.html", "active": active == "news"},
        {"label": "Publications", "href": f"{base}publications.html", "active": active == "publications"},
        {"label": "Contact Us", "href": f"{base}contact.html", "active": active == "contact"},
    ]


def base_context(base: str, active: str = "") -> dict:
    return {
        "base": base,
        "nav": build_nav(base, active),
        "practices": PRACTICES,
        "footer": FOOTER,
        "year": date.today().year,
    }
