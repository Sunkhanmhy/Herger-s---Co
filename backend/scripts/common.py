"""Shared navigation/site data used by every page's Jinja2 context."""
from datetime import date

from content.footer import FOOTER

def image_for(label: str) -> str:
    """Every image across the site is enforced to this single asset (per explicit spec)."""
    return "assets/images/shared/office-01.jpg"


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


def build_nav(base: str, active: str = "", active_item: str = "") -> list[dict]:
    return [
        {"label": "Home", "href": f"{base}index.html", "active": active == "home"},
        {
            "label": "Company",
            "active": active == "company",
            "children": [
                {"label": "About Herger's & Co.", "href": f"{base}company/about.html",
                 "active": active_item == "about"},
                {"label": "Our Partners", "href": f"{base}company/partners.html",
                 "active": active_item == "partners"},
                {"label": "Our Clients", "href": f"{base}company/clients.html",
                 "active": active_item == "clients"},
                {"label": "Careers & Positions", "href": f"{base}company/careers.html",
                 "active": active_item == "careers"},
            ],
        },
        {
            "label": "Practices & Law",
            "active": active == "practices",
            "children": [
                {"label": p["label"], "href": f"{base}practices/{p['slug']}.html",
                 "active": active_item == p["slug"]}
                for p in PRACTICES
            ],
        },
        {"label": "News & Events", "href": f"{base}news-events.html", "active": active == "news"},
        {"label": "Publications", "href": f"{base}publications.html", "active": active == "publications"},
        {"label": "Contact Us", "href": f"{base}contact.html", "active": active == "contact"},
    ]


def base_context(base: str, active: str = "", active_item: str = "") -> dict:
    return {
        "base": base,
        "nav": build_nav(base, active, active_item),
        "practices": PRACTICES,
        "footer": FOOTER,
        "year": date.today().year,
    }
