"""Content data for the Publications page."""

CONTEXT = {
    "title": "Publications",
    "description": "Legal insights, guides and regulatory analysis published by Herger's & Co.",
    "hero": {
        "eyebrow": "Insights",
        "title": "Publications",
        "subtitle": "In-depth legal analysis from our twelve practice groups, written for general counsel, executives and fellow practitioners.",
        "breadcrumbs": [
            {"label": "Home", "href": "../index.html"},
            {"label": "Publications", "href": "#"},
        ],
    },
    "intro": {
        "heading": "Practical Analysis, Not Just Commentary",
        "paragraphs": [
            "Every publication on this page is authored or reviewed by the partner leading the relevant practice group, and each is written to be directly usable by the reader — a general counsel deciding whether a transaction requires FCCPC notification, a compliance officer preparing for a CBN examination, or an entrepreneur weighing Startup Label eligibility.",
            "Our publications draw exclusively on named, current Nigerian statutes and regulator guidance, cross-referenced against the Constitution of the Federal Republic of Nigeria 1999 where constitutional questions arise. Where a topic touches an area we have covered elsewhere on this site, we cross-reference the relevant Practices & Law page for deeper context.",
        ],
    },
    "categories": ["All", "Mining & Energy", "Tax & Fiscal Policy", "Capital Markets", "Compliance", "Dispute Resolution", "Corporate Governance"],
    "featured": {
        "heading": "Featured Publications",
        "entries": [
            {"title": "Understanding the FCCPC Merger Review Thresholds", "category": "Capital Markets", "image_label": "Regulatory analysis document — placeholder image", "excerpt": "A practical walkthrough of when a Nigerian transaction requires mandatory FCCPC notification, and how to prepare a clean filing.", "practice_slug": "mergers-acquisitions"},
            {"title": "Nigeria Data Protection Act: A Board-Level Briefing", "category": "Compliance", "image_label": "Data governance briefing — placeholder image", "excerpt": "What directors need to know about breach notification timelines, cross-border transfer restrictions and enforcement risk.", "practice_slug": "risk-regulatory-compliance"},
            {"title": "Mineral Title Due Diligence: A Practical Checklist", "category": "Mining & Energy", "image_label": "Mining checklist document — placeholder image", "excerpt": "The cadastral, environmental and community-agreement checks every investor should complete before committing capital to a mining title.", "practice_slug": "mining-production-law"},
        ],
    },
    "articles": {
        "heading": "All Publications",
        "entries": [
            {"title": "Transfer Pricing Documentation: Lessons from Recent FIRS Audits", "category": "Tax & Fiscal Policy", "practice_slug": "taxation-and-policies"},
            {"title": "Cabotage Waivers: When and How to Apply", "category": "Dispute Resolution", "practice_slug": "shipping-international-trade"},
            {"title": "The Arbitration and Mediation Act 2023: What Changed", "category": "Dispute Resolution", "practice_slug": "litigation-adr"},
            {"title": "Structuring a Compliant Rights Issue Under CAMA 2020", "category": "Capital Markets", "practice_slug": "capital-markets-securities"},
            {"title": "Governor's Consent: Avoiding the Most Common Title Defect", "category": "Corporate Governance", "practice_slug": "real-estate-management"},
            {"title": "Startup Label Status: Is Your Company Eligible?", "category": "Corporate Governance", "practice_slug": "privatization-venture-capital"},
            {"title": "EFCC Investigations: Your Rights at the Invitation Stage", "category": "Dispute Resolution", "practice_slug": "white-collar-defence"},
            {"title": "Copyright Enforcement in the Streaming Era", "category": "Corporate Governance", "practice_slug": "media-entertainment-law"},
            {"title": "Board Composition Under the Nigerian Code of Corporate Governance", "category": "Corporate Governance", "practice_slug": "corporate-governance"},
        ],
    },
    "cta": {
        "title": "Have a Question on One of These Topics?",
        "body": "Schedule a free consultation with the practice group behind any publication above.",
    },
}
