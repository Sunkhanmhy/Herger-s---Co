"""Content data for the Contact Us page — hosts the Contact, Schedule Free Consultation
and Paid Consultation forms (Newsletter form lives sitewide in the footer)."""

CONTEXT = {
    "title": "Contact Us",
    "description": "Contact Herger's & Co., schedule a free consultation, or request a paid consultation with hourly-rate estimation.",
    "calendly_url": "https://calendly.com/hergerandco/free-consultation",
    "hero": {
        "eyebrow": "Get in Touch",
        "title": "Contact Us",
        "subtitle": "Reach our team directly, schedule a complimentary consultation, or request a paid consultation with an instant fee estimate.",
        "breadcrumbs": [
            {"label": "Home", "href": "../index.html"},
            {"label": "Contact Us", "href": "#"},
        ],
    },
    "office": {
        "heading": "Our Office",
        "entries": [
            {"title": "Address", "value": "16A Ahmadu Bello Way, Victoria Island, Lagos, Nigeria"},
            {"title": "Phone", "value": "+234 (0) 1 234 5678"},
            {"title": "Email", "value": "info@hergerandco.com"},
            {"title": "Office Hours", "value": "Monday – Friday, 8:00am – 6:00pm WAT"},
        ],
    },
    "contact_form": {
        "heading": "Send Us a Message",
        "subtitle": "General enquiries are typically answered within one business day.",
    },
    "consultation_form": {
        "heading": "Schedule a Free Consultation",
        "subtitle": "Tell us about your matter and pick a convenient time on our live calendar — your first consultation is complimentary.",
        "practice_areas": [
            "General Enquiry", "Mining & Production Law", "Taxation & Policies",
            "Shipping & International Trade", "Risk & Regulatory Compliances", "White Collar Defence",
            "Real Estate & Management", "Capital Markets & Securities", "Privatization & Venture Capital",
            "Mergers & Acquisition", "Media & Entertainment Law", "Litigation & ADR Law", "Corporate Governance",
        ],
    },
    "paid_consultation_form": {
        "heading": "Request a Paid Consultation",
        "subtitle": "Use the calculator below for an instant estimate based on session type, duration and urgency. Final billing is always confirmed in writing before your session.",
        "urgency_options": [
            {"value": "standard", "label": "Standard (within 5 business days)"},
            {"value": "priority", "label": "Priority (within 2 business days) — +25%"},
            {"value": "same_day", "label": "Same-Day (subject to availability) — +60%"},
        ],
    },
    "faqs": {
        "heading": "Consultation FAQs",
        "entries": [
            {"q": "Is the first consultation really free?", "a": "Yes — our Schedule Free Consultation form and Calendly booking are entirely complimentary and carry no obligation to retain the firm afterward."},
            {"q": "How accurate is the paid consultation fee estimate?", "a": "The calculator provides a good-faith estimate based on standard hourly rates by practice area; our billing team confirms the final scope and fee in writing before any session is scheduled or invoiced."},
            {"q": "Can I request a specific partner?", "a": "Yes — mention the partner or practice group in the notes field of either consultation form and we will do our best to accommodate your preference."},
            {"q": "How quickly will I hear back after submitting the contact form?", "a": "We aim to respond to all general enquiries within one business day."},
        ],
    },
}
