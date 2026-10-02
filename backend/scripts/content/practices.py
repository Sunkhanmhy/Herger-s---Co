"""Content data for the 12 'Practices & Law' sub-menu pages.

Every fact pattern here is grounded in real, named Nigerian legislation. Where the
brief calls for 2007-era alignment, the relevant 2007 Acts are cited explicitly
(Nigerian Minerals and Mining Act 2007, NESREA Act 2007, FIRS Establishment Act 2007,
Fiscal Responsibility Act 2007, Merchant Shipping Act 2007, NIMASA Act 2007,
Investments and Securities Act 2007, Public Procurement Act 2007), alongside the
1999 Constitution and later governing statutes (CAMA 2020, FCCPA 2018, Arbitration
and Mediation Act 2023, etc.) so each page remains legally accurate and current.
"""

def _breadcrumbs(label: str) -> list[dict]:
    return [
        {"label": "Home", "href": "../index.html"},
        {"label": "Practices & Law", "href": "#"},
        {"label": label, "href": "#"},
    ]


PRACTICE_PAGES: dict[str, dict] = {}

# ---------------------------------------------------------------------------
# 1. Mining & Production Law
# ---------------------------------------------------------------------------
PRACTICE_PAGES["mining-production-law"] = {
    "title": "Mining & Production Law",
    "description": "Nigerian mining, mineral titles, extractive-sector production and environmental compliance counsel from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Mining & Production Law",
        "subtitle": "Advising exploration, mining and processing companies through every stage of the mineral title lifecycle under the Nigerian Minerals and Mining Act 2007.",
        "breadcrumbs": _breadcrumbs("Mining & Production Law"),
    },
    "overview": {
        "heading": "Structuring Extractive-Sector Ventures Around Nigeria's Mining Code",
        "image_label": "Mining site inspection — placeholder image",
        "paragraphs": [
            "Nigeria's solid minerals sector operates under one of the most consolidated legal regimes on the continent: the Nigerian Minerals and Mining Act 2007 (Act No. 20 of 2007), together with the Nigerian Minerals and Mining Regulations 2011. The Act vests ownership and control of all mineral resources, wherever situated in Nigeria, in the Government of the Federation, and establishes the Mining Cadastre Office as the sole issuing authority for mineral titles on a 'first come, first served' basis. Herger's & Co. structures every exploration, mining, processing and export mandate against this statutory backbone, ensuring clients hold defensible, registrable title from day one.",
            "Our mining and production team advises junior explorers, mid-tier producers, multinational mining houses, quarry operators and downstream processors on the full title lifecycle: Reconnaissance Permits, Exploration Licences, Small-Scale Mining Leases, Mining Leases, Water Use Permits and Quarry Leases. We conduct cadastral due diligence directly against the Mining Cadastre Office's register to confirm that a concession is free, that pegging and coordinates match survey plans, and that community and surface-rights obligations under the Land Use Act 1978 have been properly discharged before a client commits capital.",
            "Because mineral title in Nigeria is inseparable from environmental and community obligations, we also work closely with the National Environmental Standards and Regulations Enforcement Agency (Establishment) Act 2007 (the NESREA Act), which criminalises breaches of environmental standards in mining and processing operations. Every mine plan we help negotiate incorporates an Environmental Impact Assessment sign-off, a Community Development Agreement compliant with section 116 of the Mining Act, and a resettlement and compensation framework that anticipates host-community claims before they escalate into litigation.",
            "For clients operating at the intersection of solid minerals and petroleum (for example, associated gas, bitumen or coal-to-power projects), we coordinate seamlessly with our Taxation & Policies and Risk & Regulatory Compliance teams so that royalty computations, ministerial consents and multiple-regulator sign-offs (Ministry of Mines and Steel Development, NESREA, and where applicable NUPRC) are sequenced correctly and do not stall bankable feasibility timelines.",
        ],
        "at_a_glance": [
            "Primary statute: Nigerian Minerals and Mining Act 2007 (Act No. 20 of 2007)",
            "Regulator: Mining Cadastre Office & Ministry of Solid Minerals Development",
            "Environmental oversight: NESREA (Establishment) Act 2007",
            "Land access: Land Use Act 1978 (Cap L5, LFN 2004)",
            "Typical mandates: title acquisition, joint ventures, community agreements, export permits",
        ],
    },
    "legislation": {
        "intro": "Our advice is built directly on the primary statutes and regulations governing the extractive sector in Nigeria — not general commentary.",
        "entries": [
            {"act": "Nigerian Minerals and Mining Act 2007", "description": "Vests mineral ownership in the Federal Government, creates the Mining Cadastre Office, and defines the seven categories of mineral title, royalty obligations, and forfeiture/revocation grounds."},
            {"act": "Nigerian Minerals and Mining Regulations 2011", "description": "Operationalises the 2007 Act: pegging and survey standards, environmental protection and rehabilitation fund contributions, and health and safety codes at mine sites."},
            {"act": "NESREA (Establishment) Act 2007", "description": "Empowers the National Environmental Standards and Regulations Enforcement Agency to enforce environmental impact assessments, effluent limits and remediation orders across mining and processing sites."},
            {"act": "Land Use Act 1978", "description": "Governs the acquisition of surface rights, rights of occupancy and compensation payable to host communities whose land is required for mining operations."},
            {"act": "Petroleum Industry Act 2021", "description": "Where a project intersects hydrocarbons, the PIA and the NUPRC/NMDPRA framework governs upstream and midstream production, separate from solid minerals licensing."},
            {"act": "Companies and Allied Matters Act 2020", "description": "Governs the incorporation and corporate structuring of mining special purpose vehicles, joint ventures and farm-in/farm-out arrangements."},
        ],
    },
    "services": {
        "intro": "From first cadastral search to first shipment, our mining lawyers cover the full commercial and regulatory lifecycle.",
        "entries": [
            {"title": "Mineral Title Acquisition & Due Diligence", "description": "Cadastral searches, title verification, pegging disputes and registration of Exploration Licences and Mining Leases with the Mining Cadastre Office."},
            {"title": "Joint Ventures & Farm-In Structuring", "description": "Structuring local-content-compliant joint ventures between foreign investors and Nigerian mining title holders, including shareholder and offtake arrangements."},
            {"title": "Community Development Agreements", "description": "Negotiating statutory Community Development Agreements under section 116 of the Mining Act to secure a durable social licence to operate."},
            {"title": "Environmental & Regulatory Compliance", "description": "Environmental Impact Assessment sign-off, NESREA permitting, mine closure and rehabilitation bonding."},
            {"title": "Royalty, Fees & Fiscal Structuring", "description": "Computing and structuring annual service fees, royalties and surface rents payable to the Federal Government and host states."},
            {"title": "Export, Processing & Offtake Contracts", "description": "Drafting export permits documentation, mineral processing licences and long-term offtake agreements with international buyers."},
            {"title": "Dispute Resolution & Title Litigation", "description": "Representing clients in mineral title revocation appeals, boundary disputes and community compensation claims before the Mines Environmental Compliance Department and the courts."},
            {"title": "Health, Safety & Labour Compliance", "description": "Advising on statutory mine safety obligations and coordinated compliance with the Factories Act and labour legislation applicable to mine workers."},
            {"title": "M&A in the Extractive Sector", "description": "Due diligence and completion mechanics for the acquisition or divestment of mining assets and title-holding companies."},
        ],
    },
    "approach": {
        "intro": "A disciplined, four-stage methodology that keeps extractive projects bankable and regulator-ready.",
        "steps": [
            {"title": "Cadastral & Legal Audit", "description": "We verify title status, boundaries and outstanding obligations directly against the Mining Cadastre Office register before any capital is committed."},
            {"title": "Structuring", "description": "We design the corporate, fiscal and community-engagement structure to match the mine plan, financiers' requirements and local content rules."},
            {"title": "Regulatory Clearance", "description": "We sequence and obtain Ministry, NESREA, host-state and (where relevant) NUPRC approvals in the correct statutory order."},
            {"title": "Operational Support", "description": "We provide ongoing compliance monitoring, royalty reconciliation and dispute-avoidance support once production begins."},
        ],
    },
    "engagements": {
        "intro": "Illustrative, anonymised examples of the type of mandates our mining and production team regularly handles.",
        "entries": [
            {"title": "Gold Exploration Licence Portfolio", "image_label": "Exploration camp — placeholder image", "description": "Advised a mid-tier exploration company on the acquisition and consolidation of a multi-block Exploration Licence portfolio across three states, including cadastral dispute resolution."},
            {"title": "Limestone Quarry Community Agreement", "image_label": "Quarry operations — placeholder image", "description": "Negotiated a Community Development Agreement and resettlement framework for a cement-grade limestone quarry, balancing statutory obligations with production timelines."},
            {"title": "Cross-Border Tin & Tantalite JV", "image_label": "Processing facility — placeholder image", "description": "Structured a joint venture between a foreign strategic investor and a Nigerian title holder for tin and tantalite processing, including offtake and local content commitments."},
        ],
    },
    "stats": [
        {"value": "7", "label": "Mineral title categories navigated"},
        {"value": "20+", "label": "Mining leases perfected"},
        {"value": "3", "label": "Core regulators coordinated"},
        {"value": "100%", "label": "Cadastral audits completed pre-closing"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian mining law",
        "entries": [
            {"q": "Who owns mineral resources in Nigeria?", "a": "Under section 1 of the Nigerian Minerals and Mining Act 2007 and section 44(3) of the 1999 Constitution, ownership and control of all minerals in, under or upon any land in Nigeria is vested exclusively in the Government of the Federation."},
            {"q": "Can a foreign company hold a mining title directly?", "a": "Yes, provided the applicant is incorporated in Nigeria under the Companies and Allied Matters Act 2020 with the Mining Cadastre Office as issuing authority; foreign shareholding is permitted subject to NIPC registration and standard exchange control rules."},
            {"q": "What is a Community Development Agreement?", "a": "A statutory agreement required under section 116 of the Mining Act between a title holder and host communities, setting out social and economic development commitments before mining operations can commence at scale."},
            {"q": "How long does exploration-to-mining conversion take?", "a": "Timelines vary by mineral and location, but a well-prepared application with clean cadastral title, completed feasibility studies and community agreements in place can convert an Exploration Licence to a Mining Lease considerably faster than an incomplete file."},
        ],
    },
    "cta": {
        "title": "Ready to Secure Your Mineral Title?",
        "body": "Speak with our Mining & Production Law team about cadastral due diligence, licensing strategy or community agreements before your next capital commitment.",
    },
}

# ---------------------------------------------------------------------------
# 2. Taxation & Policies
# ---------------------------------------------------------------------------
PRACTICE_PAGES["taxation-and-policies"] = {
    "title": "Taxation & Policies",
    "description": "Corporate tax, fiscal policy and FIRS dispute advisory from Herger's & Co., built on the Federal Inland Revenue Service (Establishment) Act 2007.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Taxation & Policies",
        "subtitle": "Structuring, compliance and dispute resolution across Nigeria's federal and state tax architecture, anchored in the FIRS Establishment Act 2007 and the Fiscal Responsibility Act 2007.",
        "breadcrumbs": _breadcrumbs("Taxation & Policies"),
    },
    "overview": {
        "heading": "Navigating a Multi-Layered Fiscal Regime with Precision",
        "image_label": "Tax advisory session — placeholder image",
        "paragraphs": [
            "Nigeria's tax system operates on three tiers — federal, state and local government — and the Federal Inland Revenue Service (Establishment) Act 2007 is the cornerstone statute conferring autonomy, enforcement powers and self-accounting authority on the FIRS as the primary federal revenue agency. Herger's & Co.'s tax team advises corporates, high-net-worth individuals and public bodies on structuring transactions to be efficient and fully compliant within this framework, rather than merely reactive to assessments.",
            "Our engagements typically begin with a diagnostic review spanning Companies Income Tax, Value Added Tax, Withholding Tax, Petroleum Profits Tax (where applicable), Capital Gains Tax, Stamp Duties and Personal Income Tax exposure, benchmarked against the Finance Act amendments issued in most recent fiscal years. We also advise extensively on the Fiscal Responsibility Act 2007, which imposes budgetary discipline, medium-term expenditure frameworks and transparency obligations on government-linked entities and their private-sector counterparties — an area frequently overlooked by generalist counsel but decisive in public-private partnership and government contracting work.",
            "Where a client faces a disputed assessment, our approach is to first exhaust the FIRS's internal objection and reconciliation process under the Act before escalating to the Tax Appeal Tribunal, and ultimately the Federal High Court, if unresolved. We have successfully negotiated down assessments through documented reconciliation, and where litigation is unavoidable, we build the evidentiary record methodically rather than treating tribunal appearances as a formality.",
            "Beyond compliance, our 'Policies' mandate extends to advising trade associations, multinational subsidiaries and government agencies on the practical implications of new fiscal policy — including changes introduced by annual Finance Acts, the Nigeria Tax Act 2025 reforms, and state-level revenue mobilisation drives — translating legislative text into operational guidance before an audit ever begins.",
        ],
        "at_a_glance": [
            "Primary statute: FIRS (Establishment) Act 2007",
            "Fiscal discipline: Fiscal Responsibility Act 2007",
            "Core taxes: CIT, VAT, WHT, PPT, CGT, Stamp Duties, PIT",
            "Dispute forum: Tax Appeal Tribunal → Federal High Court",
            "Typical mandates: structuring, audits, objections, tribunal litigation",
        ],
    },
    "legislation": {
        "intro": "Every position we advance is anchored to the governing statute, not informal FIRS practice notes alone.",
        "entries": [
            {"act": "FIRS (Establishment) Act 2007", "description": "Establishes the Federal Inland Revenue Service, its Board, autonomy and powers of assessment, audit, distraint and prosecution for tax offences."},
            {"act": "Fiscal Responsibility Act 2007", "description": "Imposes medium-term fiscal frameworks, borrowing limits and transparency obligations on the Federal Government and its agencies, relevant to government contracting and PPP structuring."},
            {"act": "Companies Income Tax Act (as amended)", "description": "Governs the taxation of company profits, capital allowances, minimum tax and the deductibility rules central to corporate structuring advice."},
            {"act": "Value Added Tax Act (as amended)", "description": "Governs VAT registration, exemptions, input-output reconciliation and the reverse-charge rules applicable to non-resident suppliers."},
            {"act": "Petroleum Profits Tax Act / Petroleum Industry Act 2021", "description": "Governs the taxation of upstream and midstream petroleum operations, including hydrocarbon tax and royalty interaction post-PIA."},
            {"act": "Tax Appeal Tribunal (Establishment) Order", "description": "Establishes the specialist tribunal with exclusive first-instance jurisdiction over most federal tax disputes prior to Federal High Court appeal."},
        ],
    },
    "services": {
        "intro": "Full-spectrum tax counsel, from transaction structuring to tribunal advocacy.",
        "entries": [
            {"title": "Corporate Tax Structuring", "description": "Designing group structures, financing arrangements and intercompany pricing to be efficient and defensible under Nigerian transfer pricing regulations."},
            {"title": "Tax Audits & Investigations", "description": "Managing FIRS and state internal revenue service audits from field visit through reconciliation, minimising penalty and interest exposure."},
            {"title": "Tax Appeal Tribunal Litigation", "description": "Representing clients in contested assessments before the Tax Appeal Tribunal and on appeal to the Federal High Court."},
            {"title": "Indirect Tax Advisory (VAT & Customs)", "description": "Advising on VAT treatment of cross-border digital services, exemptions and customs duty classification disputes."},
            {"title": "Transfer Pricing Compliance", "description": "Preparing and defending transfer pricing documentation for multinational groups operating Nigerian subsidiaries."},
            {"title": "Tax Incentives & Pioneer Status", "description": "Applying for Pioneer Status incentives, Export Processing Zone reliefs and other statutory tax holidays available to qualifying investors."},
            {"title": "Fiscal Policy & Government Advisory", "description": "Advising government agencies and their private partners on Fiscal Responsibility Act compliance in PPP and concession structures."},
            {"title": "Personal & Expatriate Tax Planning", "description": "Structuring remuneration and residency positions for executives and expatriate staff to manage Personal Income Tax exposure lawfully."},
        ],
    },
    "approach": {
        "intro": "A methodical, four-step process for every mandate, whether advisory or contentious.",
        "steps": [
            {"title": "Diagnostic Review", "description": "We map the client's full tax footprint across all applicable heads before recommending any structuring change."},
            {"title": "Position Paper", "description": "We document the technical and statutory basis for the recommended position, anticipating likely FIRS challenges."},
            {"title": "Implementation", "description": "We support filing, registration and documentation to ensure the structure is defensible in practice, not just on paper."},
            {"title": "Defence & Resolution", "description": "If challenged, we manage the objection, reconciliation and, where necessary, tribunal process to finality."},
        ],
    },
    "engagements": {
        "intro": "Representative examples of tax mandates our team has handled.",
        "entries": [
            {"title": "Multinational Transfer Pricing Defence", "image_label": "Corporate finance meeting — placeholder image", "description": "Defended a multinational's intercompany pricing arrangements during a comprehensive FIRS transfer pricing audit, achieving a materially reduced final assessment."},
            {"title": "VAT Reverse-Charge Advisory", "image_label": "Digital services team — placeholder image", "description": "Advised a foreign digital services provider on Nigerian VAT reverse-charge obligations and voluntary registration ahead of enforcement."},
            {"title": "Pioneer Status Application", "image_label": "Manufacturing facility — placeholder image", "description": "Secured Pioneer Status tax relief for a manufacturing client under the Industrial Development (Income Tax Relief) framework, saving several fiscal years of Companies Income Tax."},
        ],
    },
    "stats": [
        {"value": "15+", "label": "Years combined tax tribunal experience"},
        {"value": "3", "label": "Tiers of tax jurisdiction covered"},
        {"value": "40+", "label": "Audits successfully reconciled"},
        {"value": "7", "label": "Major tax heads advised on"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian tax law",
        "entries": [
            {"q": "Which law gives FIRS its enforcement powers?", "a": "The Federal Inland Revenue Service (Establishment) Act 2007 grants FIRS autonomy, self-accounting status and powers of assessment, audit, distraint of assets and prosecution for tax offences."},
            {"q": "Where are federal tax disputes first heard?", "a": "Most federal tax disputes are first heard at the Tax Appeal Tribunal, with further appeal on points of law to the Federal High Court."},
            {"q": "What is the Fiscal Responsibility Act 2007 and why does it matter to my company?", "a": "It imposes budgetary discipline and transparency obligations on the Federal Government and its agencies; companies contracting with government bodies or participating in PPPs must structure agreements consistently with it."},
            {"q": "Can tax assessments be negotiated before litigation?", "a": "Yes — the FIRS Act contemplates an internal objection and reconciliation process, which our team pursues diligently before recommending tribunal escalation."},
        ],
    },
    "cta": {
        "title": "Facing an Assessment or Planning a Restructuring?",
        "body": "Talk to our Taxation & Policies team before you file, respond, or restructure — early advice materially changes outcomes.",
    },
}

# ---------------------------------------------------------------------------
# 3. Shipping & International Trade
# ---------------------------------------------------------------------------
PRACTICE_PAGES["shipping-international-trade"] = {
    "title": "Shipping & International Trade",
    "description": "Maritime, cabotage and cross-border trade counsel from Herger's & Co., grounded in the Merchant Shipping Act 2007 and the NIMASA Act 2007.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Shipping & International Trade",
        "subtitle": "Advising shipowners, charterers, terminal operators and traders across Nigeria's maritime and customs frameworks, built on the Merchant Shipping Act 2007.",
        "breadcrumbs": _breadcrumbs("Shipping & International Trade"),
    },
    "overview": {
        "heading": "Counsel for Nigeria's Maritime Gateway to World Trade",
        "image_label": "Container terminal — placeholder image",
        "paragraphs": [
            "Nigeria's ports handle the overwhelming majority of West Africa's containerised trade, and two 2007 statutes form the backbone of the regulatory environment our shipping team operates in daily: the Merchant Shipping Act 2007 (Act No. 8 of 2007), which governs ship registration, seaworthiness, crewing, marine pollution liability and carriage of goods by sea, and the Nigerian Maritime Administration and Safety Agency (Establishment) Act 2007, which created NIMASA as the apex regulator for maritime safety, seafarer certification and cabotage enforcement.",
            "Our advisory work sits alongside the Coastal and Inland Shipping (Cabotage) Act 2003, which restricts the domestic carriage of goods and passengers within Nigerian coastal and inland waters to vessels that are wholly Nigerian-owned, built and crewed, subject to ministerial waivers. We routinely advise foreign shipowners and Nigerian joint-venture partners on structuring vessel acquisition and time-charter arrangements that comply with cabotage restrictions while preserving commercial flexibility, and we prepare and defend waiver applications before the Cabotage Vessel Financing Fund and NIMASA.",
            "On the trade side, we advise importers, exporters and freight forwarders on Nigeria Customs Service classification and valuation disputes, bonded warehousing, temporary importation and the practical application of ECOWAS Trade Liberalisation Scheme certificates and the African Continental Free Trade Area (AfCFTA) preferential tariff regime — an increasingly important source of savings for clients trading across West African borders.",
            "Because maritime disputes frequently combine contractual, tortious and regulatory dimensions — a cargo claim might simultaneously raise bill-of-lading interpretation, NIMASA licensing questions and insurance coverage issues — our team coordinates closely with our Litigation & ADR practice to run admiralty actions before the Federal High Court's Admiralty Jurisdiction, and with our Risk & Regulatory Compliance team on sanctions and anti-money-laundering screening for vessel financing transactions.",
        ],
        "at_a_glance": [
            "Primary statutes: Merchant Shipping Act 2007; NIMASA Act 2007",
            "Cabotage: Coastal and Inland Shipping (Cabotage) Act 2003",
            "Forum: Federal High Court (Admiralty Jurisdiction)",
            "Trade frameworks: ECOWAS ETLS, AfCFTA preferential tariffs",
            "Typical mandates: vessel registration, cabotage waivers, cargo claims, customs disputes",
        ],
    },
    "legislation": {
        "intro": "Nigerian maritime and trade practice draws on a distinct set of statutes that our team applies daily, not occasionally.",
        "entries": [
            {"act": "Merchant Shipping Act 2007", "description": "Governs Nigerian ship registration, seaworthiness certification, seafarer welfare, limitation of liability and carriage of goods by sea."},
            {"act": "NIMASA (Establishment) Act 2007", "description": "Creates the Nigerian Maritime Administration and Safety Agency, responsible for maritime safety enforcement, seafarer certification and cabotage compliance monitoring."},
            {"act": "Coastal and Inland Shipping (Cabotage) Act 2003", "description": "Restricts domestic coastal and inland waterway carriage to Nigerian-owned, built and crewed vessels, subject to statutory waiver applications."},
            {"act": "Nigerian Ports Authority Act", "description": "Governs port operations, terminal concessions and the statutory powers of the Nigerian Ports Authority over port infrastructure."},
            {"act": "Nigeria Customs Service Act 2023", "description": "Governs customs administration, classification, valuation and enforcement, including the modernised penalty and appeal regime."},
            {"act": "AfCFTA Agreement (as domesticated)", "description": "Provides the preferential tariff and rules-of-origin framework for intra-African trade, increasingly relevant to Nigerian exporters and importers."},
        ],
    },
    "services": {
        "intro": "Commercial and regulatory shipping counsel across the full voyage — from vessel acquisition to cargo delivery.",
        "entries": [
            {"title": "Vessel Registration & Financing", "description": "Advising on Nigerian ship registration, mortgage perfection and vessel financing security structures."},
            {"title": "Cabotage Compliance & Waivers", "description": "Structuring joint ventures and preparing waiver applications to navigate the Cabotage Act's local ownership and crewing requirements."},
            {"title": "Charterparty & Bill of Lading Disputes", "description": "Advising on and litigating disputes arising from time charters, voyage charters and bill of lading terms."},
            {"title": "Cargo Claims & Marine Insurance", "description": "Handling cargo damage, short-delivery and general average claims, coordinated with marine insurers and P&I clubs."},
            {"title": "Customs Classification & Valuation", "description": "Challenging Nigeria Customs Service tariff classification and valuation decisions, including post-clearance audits."},
            {"title": "Port & Terminal Concession Advisory", "description": "Advising terminal operators and port service providers on concession agreements with the Nigerian Ports Authority."},
            {"title": "Cross-Border Trade Structuring", "description": "Structuring import/export transactions to take advantage of ECOWAS and AfCFTA preferential tariff treatment."},
            {"title": "Admiralty Litigation", "description": "Representing clients in arrest of vessel proceedings and admiralty actions before the Federal High Court."},
        ],
    },
    "approach": {
        "intro": "Maritime matters move fast — our process is built for time-sensitive, multi-jurisdictional decision-making.",
        "steps": [
            {"title": "Rapid Regulatory Triage", "description": "We immediately identify which regulator(s) — NIMASA, NPA, Customs — govern the issue at hand and the applicable statutory deadlines."},
            {"title": "Commercial Structuring", "description": "We design charter, ownership or trade structures that satisfy cabotage and customs rules without sacrificing commercial terms."},
            {"title": "Documentation & Filing", "description": "We prepare registration, waiver and customs documentation to withstand regulator scrutiny and third-party challenge."},
            {"title": "Dispute Response", "description": "Where a dispute or arrest arises, we mobilise admiralty counsel immediately, given the time-critical nature of vessel detention."},
        ],
    },
    "engagements": {
        "intro": "Representative maritime and trade mandates handled by our team.",
        "entries": [
            {"title": "Cabotage Waiver for LNG Carrier", "image_label": "LNG carrier at port — placeholder image", "description": "Secured a ministerial cabotage waiver enabling a foreign-flagged vessel to operate temporarily on the Nigerian coast pending delivery of a Nigerian-flagged replacement."},
            {"title": "Customs Valuation Appeal", "image_label": "Customs clearance yard — placeholder image", "description": "Successfully appealed a Nigeria Customs Service valuation uplift on imported industrial equipment, restoring the declared transaction value."},
            {"title": "Cargo Short-Delivery Claim", "image_label": "Bulk cargo vessel — placeholder image", "description": "Recovered damages for a commodities trader following a bulk cargo short-delivery, coordinating with P&I club correspondents and surveyors."},
        ],
    },
    "stats": [
        {"value": "2", "label": "Core 2007 maritime statutes applied"},
        {"value": "30+", "label": "Vessel & cargo matters handled"},
        {"value": "2", "label": "Regional trade regimes leveraged (ECOWAS, AfCFTA)"},
        {"value": "24/7", "label": "Emergency admiralty response availability"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian shipping and trade law",
        "entries": [
            {"q": "What is the Cabotage Act and who does it affect?", "a": "The Coastal and Inland Shipping (Cabotage) Act 2003 restricts the carriage of goods and passengers within Nigerian coastal and inland waters to vessels that are Nigerian-owned, built, flagged and crewed, subject to statutory waivers for qualifying foreign vessels."},
            {"q": "Which court hears maritime disputes in Nigeria?", "a": "The Federal High Court has exclusive admiralty jurisdiction over shipping and maritime claims, including vessel arrest applications."},
            {"q": "Can I benefit from AfCFTA tariffs immediately?", "a": "Eligibility depends on rules-of-origin compliance and the trading partner's implementation status; our trade team assesses qualification before shipment to avoid denied preferential treatment at the border."},
            {"q": "What does NIMASA regulate day-to-day?", "a": "NIMASA, established under the NIMASA Act 2007, regulates maritime safety standards, seafarer certification, cabotage enforcement and search-and-rescue coordination."},
        ],
    },
    "cta": {
        "title": "Moving Goods or Vessels Through Nigerian Waters?",
        "body": "Our Shipping & International Trade team can structure your transaction correctly the first time — before customs, NIMASA or a counterparty raises an objection.",
    },
}

# ---------------------------------------------------------------------------
# 4. Risk & Regulatory Compliances
# ---------------------------------------------------------------------------
PRACTICE_PAGES["risk-regulatory-compliance"] = {
    "title": "Risk & Regulatory Compliances",
    "description": "AML/CFT, data protection and financial-sector compliance advisory from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Risk & Regulatory Compliances",
        "subtitle": "Building compliance programmes that satisfy the Money Laundering (Prevention and Prohibition) Act, the Nigeria Data Protection Act 2023, CBN guidelines and SEC rules.",
        "breadcrumbs": _breadcrumbs("Risk & Regulatory Compliances"),
    },
    "overview": {
        "heading": "Turning Regulatory Obligation into Operational Advantage",
        "image_label": "Compliance workshop — placeholder image",
        "paragraphs": [
            "Regulatory risk in Nigeria is layered across multiple overlapping regimes: anti-money-laundering and counter-terrorism financing rules under the Money Laundering (Prevention and Prohibition) Act 2022, data protection obligations under the Nigeria Data Protection Act 2023, prudential requirements set by the Central Bank of Nigeria, market-conduct rules issued by the Securities and Exchange Commission, and sector-specific codes administered by agencies such as NAICOM and the National Pension Commission. Herger's & Co.'s Risk & Regulatory Compliance team designs programmes that satisfy every applicable layer rather than treating each regulator in isolation.",
            "Our starting point is always a gap assessment: mapping a client's existing policies, know-your-customer procedures and reporting lines against statutory requirements, including the Nigerian Financial Intelligence Unit (Establishment) Act 2018's suspicious transaction reporting obligations and the Economic and Financial Crimes Commission (Establishment) Act 2004's broader enforcement powers. We then design board-approved compliance frameworks — AML/CFT policies, data protection impact assessments, whistleblower protocols and sanctions-screening procedures — that are proportionate to the client's actual risk profile rather than generic templates.",
            "We also support clients through direct regulatory engagement: responding to CBN and SEC examination findings, negotiating consent orders, and managing Nigeria Data Protection Commission investigations following a reported breach. Because regulatory risk frequently converts into reputational and criminal exposure, our compliance advisory is coordinated closely with our White Collar Defence practice, ensuring that a compliance gap identified today does not become an enforcement action tomorrow.",
            "For multinational clients, we also advise on the interaction between Nigerian compliance obligations and international regimes such as the UK Bribery Act, the U.S. Foreign Corrupt Practices Act and OFAC sanctions lists, ensuring group-wide compliance policies translate correctly into Nigerian operating entities without creating conflicting obligations.",
        ],
        "at_a_glance": [
            "AML/CFT: Money Laundering (Prevention and Prohibition) Act 2022",
            "Data protection: Nigeria Data Protection Act 2023",
            "Financial intelligence: NFIU (Establishment) Act 2018",
            "Regulators covered: CBN, SEC, NAICOM, NDPC, NFIU, EFCC",
            "Typical mandates: gap assessments, policy design, regulator engagement",
        ],
    },
    "legislation": {
        "intro": "Our compliance frameworks are built directly against the statutes regulators actually enforce.",
        "entries": [
            {"act": "Money Laundering (Prevention and Prohibition) Act 2022", "description": "Sets out customer due diligence, suspicious transaction reporting and record-keeping obligations for designated non-financial businesses and financial institutions."},
            {"act": "Nigeria Data Protection Act 2023", "description": "Establishes the Nigeria Data Protection Commission and imposes data controller/processor obligations, breach notification duties and cross-border transfer restrictions."},
            {"act": "NFIU (Establishment) Act 2018", "description": "Establishes the Nigerian Financial Intelligence Unit as an autonomous agency for receiving and analysing suspicious transaction reports."},
            {"act": "EFCC (Establishment) Act 2004", "description": "Confers investigative and prosecutorial powers on the Economic and Financial Crimes Commission over financial crimes, including compliance failures that facilitate fraud."},
            {"act": "FIRS (Establishment) Act 2007", "description": "Relevant to tax-compliance risk assessments run alongside broader regulatory compliance programmes."},
            {"act": "CBN AML/CFT/CPF Regulations", "description": "Sector-specific prudential and conduct regulations issued by the Central Bank of Nigeria applicable to banks and other financial institutions."},
        ],
    },
    "services": {
        "intro": "Practical, risk-proportionate compliance support — not box-ticking.",
        "entries": [
            {"title": "AML/CFT Programme Design", "description": "Building board-approved AML/CFT policies, customer due diligence procedures and transaction monitoring frameworks."},
            {"title": "Data Protection Compliance", "description": "Conducting data protection impact assessments, drafting privacy policies and registering with the Nigeria Data Protection Commission where required."},
            {"title": "Regulatory Examinations & Consent Orders", "description": "Managing CBN, SEC and NDPC examinations and negotiating consent orders or remediation plans."},
            {"title": "Sanctions & PEP Screening Advisory", "description": "Designing sanctions list screening and politically exposed persons monitoring procedures."},
            {"title": "Whistleblower & Internal Reporting Frameworks", "description": "Establishing confidential whistleblower channels compliant with sector codes and international best practice."},
            {"title": "Compliance Training & Board Reporting", "description": "Delivering board and staff training and preparing compliance reporting packs for audit committees."},
            {"title": "Third-Party & Vendor Risk Assessments", "description": "Screening vendors, agents and distributors for corruption, sanctions and data-handling risk."},
            {"title": "Cross-Border Compliance Alignment", "description": "Reconciling group compliance policies (FCPA, UK Bribery Act, OFAC) with Nigerian statutory requirements."},
        ],
    },
    "approach": {
        "intro": "Our compliance methodology moves from diagnosis to embedded, monitored practice.",
        "steps": [
            {"title": "Risk Mapping", "description": "We identify every regulator and statute applicable to the client's specific business model and customer base."},
            {"title": "Gap Assessment", "description": "We benchmark existing policies and controls against statutory minimums and regulator expectations."},
            {"title": "Framework Design", "description": "We draft or refresh policies, training materials and reporting lines tailored to the client's actual risk exposure."},
            {"title": "Embed & Monitor", "description": "We support implementation, staff training and periodic independent testing to keep the framework audit-ready."},
        ],
    },
    "engagements": {
        "intro": "Representative compliance mandates handled by our team.",
        "entries": [
            {"title": "Fintech AML Framework Build", "image_label": "Fintech operations floor — placeholder image", "description": "Designed a full AML/CFT compliance framework for a licensed payments company ahead of a CBN examination, including transaction monitoring thresholds."},
            {"title": "Data Breach Response", "image_label": "Incident response team — placeholder image", "description": "Managed a data breach notification to the Nigeria Data Protection Commission and affected data subjects within statutory timelines, limiting regulatory penalty exposure."},
            {"title": "Group Sanctions Policy Localisation", "image_label": "Multinational compliance meeting — placeholder image", "description": "Adapted a multinational's global sanctions and PEP screening policy for its Nigerian subsidiary without creating conflicting obligations."},
        ],
    },
    "stats": [
        {"value": "6", "label": "Regulators regularly engaged"},
        {"value": "25+", "label": "Compliance frameworks built"},
        {"value": "100%", "label": "Statutory breach-notification deadlines met"},
        {"value": "0", "label": "Tolerance for template-only advice"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian regulatory compliance",
        "entries": [
            {"q": "Which law governs data protection in Nigeria?", "a": "The Nigeria Data Protection Act 2023 is the primary statute, enforced by the Nigeria Data Protection Commission, replacing the earlier NDPR regulation as the binding legal framework."},
            {"q": "Do all businesses need an AML/CFT programme?", "a": "Financial institutions and designated non-financial businesses (including law firms, real estate agents and dealers in precious metals above certain thresholds) are statutorily required to maintain AML/CFT programmes under the Money Laundering (Prevention and Prohibition) Act 2022."},
            {"q": "What happens if a data breach is not reported in time?", "a": "The Nigeria Data Protection Act imposes specific notification timelines to the Commission and affected individuals; late or absent notification can itself constitute a separate compliance breach attracting penalties."},
            {"q": "How does compliance risk relate to white collar defence?", "a": "A compliance gap that goes unaddressed frequently becomes the evidentiary basis for a later EFCC or regulator enforcement action — our compliance and defence teams work together to close that gap before it is tested."},
        ],
    },
    "cta": {
        "title": "Is Your Compliance Framework Examination-Ready?",
        "body": "Let our Risk & Regulatory Compliance team run a gap assessment before your next CBN, SEC or NDPC examination.",
    },
}

# ---------------------------------------------------------------------------
# 5. White Collar Defence
# ---------------------------------------------------------------------------
PRACTICE_PAGES["white-collar-defence"] = {
    "title": "White Collar Defence",
    "description": "EFCC, ICPC and financial-crime defence representation from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "White Collar Defence",
        "subtitle": "Robust representation before the EFCC, ICPC and the courts in fraud, bribery and financial-crime investigations.",
        "breadcrumbs": _breadcrumbs("White Collar Defence"),
    },
    "overview": {
        "heading": "Protecting Individuals and Institutions Through Investigation and Trial",
        "image_label": "Legal consultation — placeholder image",
        "paragraphs": [
            "White collar investigations in Nigeria are conducted principally by the Economic and Financial Crimes Commission under the EFCC (Establishment) Act 2004 and the Independent Corrupt Practices and Other Related Offences Commission under the ICPC Act 2000, with prosecutions typically proceeding under the Administration of Criminal Justice Act 2015, the Money Laundering (Prevention and Prohibition) Act 2022, the Advance Fee Fraud and Other Fraud Related Offences Act 2006, and the Cybercrimes (Prohibition, Prevention, etc.) Act 2015 as amended. Herger's & Co.'s White Collar Defence team represents directors, executives, financial institutions and corporates from the moment an invitation letter arrives through to trial, appeal or negotiated resolution.",
            "Our approach begins before any formal interview: we advise clients on their rights under section 35 of the 1999 Constitution (personal liberty and the right to be informed of the reason for arrest), prepare them for voluntary statements, and — where a search warrant or asset freezing order is contemplated — challenge overbroad orders promptly rather than after the fact. We have found that early, informed engagement with investigators, rather than reflexive non-cooperation, frequently produces materially better outcomes for clients who are ultimately not the intended target of an investigation.",
            "Where charges are filed, we mount a rigorous defence grounded in the Evidence Act 2011 and the procedural safeguards of the Administration of Criminal Justice Act 2015, including bail applications, no-case submissions and, where appropriate, plea negotiations. For corporate clients, we also advise on parallel civil exposure — asset forfeiture proceedings, regulatory sanctions and shareholder or counterparty litigation — that often runs alongside a criminal investigation and must be managed as a single, coordinated strategy rather than in silos.",
            "Because reputational harm can outpace legal outcome, we work with clients on managing regulatory and public disclosure obligations throughout an investigation, ensuring that statements made to satisfy stock exchange or regulator disclosure rules do not inadvertently prejudice the defence.",
        ],
        "at_a_glance": [
            "Key agencies: EFCC, ICPC, NFIU",
            "Core statutes: EFCC Act 2004, ICPC Act 2000, ACJA 2015",
            "Constitutional protection: Section 35, 1999 Constitution",
            "Typical mandates: investigation defence, bail, trial, asset recovery",
        ],
    },
    "legislation": {
        "intro": "White collar defence in Nigeria requires fluency across criminal, constitutional and financial-crime statutes.",
        "entries": [
            {"act": "EFCC (Establishment) Act 2004", "description": "Confers investigative, asset-freezing and prosecutorial powers on the Economic and Financial Crimes Commission over economic and financial crimes."},
            {"act": "ICPC Act 2000", "description": "Establishes the Independent Corrupt Practices and Other Related Offences Commission and criminalises bribery, gratification and abuse of office."},
            {"act": "Administration of Criminal Justice Act 2015", "description": "Modernises criminal procedure nationwide, including timelines for arraignment, bail conditions and speedy trial obligations."},
            {"act": "Advance Fee Fraud and Other Fraud Related Offences Act 2006", "description": "Criminalises advance fee fraud and related deceptive financial schemes, frequently invoked in commercial fraud prosecutions."},
            {"act": "Cybercrimes (Prohibition, Prevention, etc.) Act 2015 (as amended)", "description": "Criminalises electronic fraud, identity theft and unauthorised access, increasingly central to fintech and digital-fraud prosecutions."},
            {"act": "1999 Constitution, Section 35 & 36", "description": "Guarantees personal liberty and fair hearing rights that frame every stage of a criminal investigation and prosecution."},
        ],
    },
    "services": {
        "intro": "Defence coverage across every stage of a financial-crime matter.",
        "entries": [
            {"title": "Pre-Charge Investigation Defence", "description": "Advising clients invited for questioning, preparing statements and engaging investigators before charges are filed."},
            {"title": "Bail Applications", "description": "Preparing and arguing bail applications before magistrate, high court and appellate courts in economic-crime matters."},
            {"title": "Trial Defence & Advocacy", "description": "Conducting full criminal trial defence, including cross-examination of prosecution witnesses and no-case submissions."},
            {"title": "Asset Freezing & Forfeiture Defence", "description": "Challenging interim and final asset forfeiture orders obtained under the EFCC Act and Money Laundering Act."},
            {"title": "Corporate Internal Investigations", "description": "Conducting privileged internal investigations to establish facts before regulators or law enforcement compel disclosure."},
            {"title": "Regulatory & Disclosure Coordination", "description": "Managing parallel regulatory disclosure obligations to avoid statements that prejudice a client's defence."},
            {"title": "Extradition & Mutual Legal Assistance", "description": "Advising on cross-border enforcement requests and mutual legal assistance treaty processes affecting Nigerian and foreign clients."},
            {"title": "Post-Conviction Appeals", "description": "Representing clients on appeal against conviction or sentence before the Court of Appeal and Supreme Court."},
        ],
    },
    "approach": {
        "intro": "A calm, evidence-first methodology designed to protect clients from the earliest possible stage.",
        "steps": [
            {"title": "Immediate Triage", "description": "We assess the nature of the invitation or allegation and advise on constitutional rights before any statement is made."},
            {"title": "Evidence Mapping", "description": "We independently gather and preserve documentary and digital evidence before it can be characterised unfavourably."},
            {"title": "Strategic Engagement", "description": "We engage investigators and prosecutors from a position of preparation, seeking early resolution where appropriate."},
            {"title": "Trial or Resolution", "description": "We proceed to full trial defence or negotiated resolution, whichever best serves the client's interests."},
        ],
    },
    "engagements": {
        "intro": "Representative white collar mandates handled by our team (details anonymised to protect client confidentiality).",
        "entries": [
            {"title": "Executive Investigation Defence", "image_label": "Boardroom meeting — placeholder image", "description": "Represented a bank executive during an EFCC investigation into alleged internal control failures, achieving discontinuance after evidentiary review."},
            {"title": "Asset Freezing Order Challenge", "image_label": "Courtroom corridor — placeholder image", "description": "Successfully varied an overbroad interim asset freezing order to release funds required for a client's ongoing business operations."},
            {"title": "Corporate Internal Investigation", "image_label": "Internal audit review — placeholder image", "description": "Led a privileged internal investigation into a whistleblower allegation, enabling the client to self-report to regulators on its own terms."},
        ],
    },
    "stats": [
        {"value": "20+", "label": "Investigation-stage mandates handled"},
        {"value": "4", "label": "Core enforcement agencies engaged"},
        {"value": "100%", "label": "Constitutional-rights briefing before statements"},
        {"value": "24/7", "label": "Emergency response line for arrests"},
    ],
    "faqs": {
        "heading": "Common questions on white collar defence in Nigeria",
        "entries": [
            {"q": "What should I do if I receive an EFCC invitation letter?", "a": "Do not ignore it, but do not attend alone. Seek legal advice immediately to understand the scope of the invitation and your rights under section 35 of the 1999 Constitution before making any statement."},
            {"q": "Can the EFCC freeze my company's account without a court order?", "a": "The EFCC can obtain an interim ex parte freezing order from the Federal High Court under the Money Laundering Act, but such orders are time-limited and can be challenged; our team frequently applies to vary or discharge overbroad orders."},
            {"q": "Is cooperation with investigators always advisable?", "a": "Informed cooperation, on legal advice, often produces better outcomes than silence or obstruction, but every statement should be made only after understanding its evidential consequences."},
            {"q": "What is the difference between EFCC and ICPC jurisdiction?", "a": "The EFCC generally handles economic and financial crimes including fraud and money laundering, while the ICPC focuses on corruption and abuse-of-office offences under the ICPC Act 2000; jurisdiction can overlap in practice."},
        ],
    },
    "cta": {
        "title": "Received an Investigative Invitation?",
        "body": "Contact our White Collar Defence team before you respond — early advice at the investigation stage materially changes outcomes.",
    },
}

# ---------------------------------------------------------------------------
# 6. Real Estate & Management
# ---------------------------------------------------------------------------
PRACTICE_PAGES["real-estate-management"] = {
    "title": "Real Estate & Management",
    "description": "Land title, property transactions and estate management advisory from Herger's & Co., grounded in the Land Use Act 1978.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Real Estate & Management",
        "subtitle": "Title verification, property transactions and estate management counsel across Nigeria's Land Use Act framework and state-level property laws.",
        "breadcrumbs": _breadcrumbs("Real Estate & Management"),
    },
    "overview": {
        "heading": "Certainty of Title in a Complex Land Administration System",
        "image_label": "Modern residential development — placeholder image",
        "paragraphs": [
            "All land in each state of Nigeria is vested in the Governor of that state in trust for the people, under the Land Use Act 1978 (Cap L5, Laws of the Federation of Nigeria 2004) — the foundational statute for every real estate transaction our firm handles. Rights of Occupancy, whether statutory or customary, are the operative form of land holding rather than outright freehold, and Herger's & Co.'s real estate team structures every acquisition, lease, mortgage and development around this reality, rather than assuming Western freehold concepts apply unmodified.",
            "Our title due diligence process is deliberately exhaustive: verifying root of title through successive assignments, confirming Governor's Consent has been properly obtained under section 22 of the Land Use Act for any assignment, mortgage or sublease exceeding the statutory threshold, checking for registered encumbrances at the relevant State Lands Registry, and — where applicable — confirming compliance with state-specific instruments such as the Lagos State Land Use Charge Law and the Lagos Tenancy Law 2011 governing rent recovery and eviction procedures.",
            "For institutional and developer clients, our estate management practice extends beyond acquisition to the full property lifecycle: structuring joint development agreements between landowners and developers, negotiating facility management and service charge frameworks for multi-occupant estates, and advising real estate investment schemes on compliance with the Lagos State Real Estate Regulatory Authority (LASRERA) Law 2021 and equivalent regimes emerging in other states.",
            "We also regularly advise on mortgage-backed lending, working with banks and mortgage institutions to perfect security interests correctly — a process notoriously vulnerable to defects where Governor's Consent, stamping and registration are not sequenced correctly — and we represent clients in title disputes, boundary litigation and unlawful-occupation recovery actions before the relevant High Courts.",
        ],
        "at_a_glance": [
            "Primary statute: Land Use Act 1978 (Cap L5, LFN 2004)",
            "Key concept: Right of Occupancy (statutory & customary)",
            "Consent requirement: Governor's Consent under section 22",
            "State overlays: Lagos Tenancy Law 2011, LASRERA Law 2021",
            "Typical mandates: title due diligence, mortgages, estate management, disputes",
        ],
    },
    "legislation": {
        "intro": "Real estate practice in Nigeria is inseparable from a specific set of federal and state instruments.",
        "entries": [
            {"act": "Land Use Act 1978", "description": "Vests all land in the state Governor in trust, establishes Rights of Occupancy as the operative title, and mandates Governor's Consent for most transfers."},
            {"act": "Registered Land Law / Land Instrument Registration Law (state-specific)", "description": "Governs the registration of title instruments at state Lands Registries and the priority effect of registration."},
            {"act": "Lagos State Tenancy Law 2011", "description": "Regulates residential tenancy agreements, notice periods and recovery-of-premises procedures in Lagos State."},
            {"act": "LASRERA Law 2021", "description": "Establishes the Lagos State Real Estate Regulatory Authority to license and regulate real estate agents, developers and transactions in Lagos."},
            {"act": "Mortgage Institutions Act", "description": "Governs the licensing and operation of primary mortgage institutions and mortgage-backed lending structures."},
            {"act": "NESREA (Establishment) Act 2007", "description": "Relevant to environmental compliance for large-scale developments and estate projects."},
        ],
    },
    "services": {
        "intro": "End-to-end real estate counsel for individuals, developers, institutional investors and lenders.",
        "entries": [
            {"title": "Title Due Diligence & Verification", "description": "Root-of-title investigation, encumbrance searches and Governor's Consent status verification before any purchase."},
            {"title": "Sale, Purchase & Lease Transactions", "description": "Drafting and negotiating deeds of assignment, sub-leases and long-term ground leases."},
            {"title": "Mortgage & Security Perfection", "description": "Structuring and perfecting mortgage security for banks and mortgage institutions, including consent and registration sequencing."},
            {"title": "Joint Development Agreements", "description": "Structuring landowner-developer joint ventures, profit-sharing and delivery milestones for estate developments."},
            {"title": "Estate & Facility Management Advisory", "description": "Drafting service charge frameworks, estate rules and facility management agreements for multi-occupant developments."},
            {"title": "Landlord & Tenant Disputes", "description": "Advising on and litigating rent recovery, unlawful occupation and statutory notice-to-quit disputes."},
            {"title": "Real Estate Regulatory Compliance", "description": "Advising developers and agents on LASRERA and equivalent state real estate regulatory compliance."},
            {"title": "Compulsory Acquisition & Compensation", "description": "Representing landowners in compulsory acquisition proceedings and negotiating adequate compensation."},
        ],
    },
    "approach": {
        "intro": "We treat title risk as the single most important variable in any real estate transaction.",
        "steps": [
            {"title": "Title Investigation", "description": "We trace root of title and verify registry records before recommending any commitment of funds."},
            {"title": "Consent & Compliance Sequencing", "description": "We map out the correct order of Governor's Consent, stamping and registration to avoid title defects."},
            {"title": "Transaction Structuring", "description": "We negotiate terms that reflect actual risk allocation between buyer, seller, developer and lender."},
            {"title": "Completion & Post-Closing Support", "description": "We manage registration follow-through and provide ongoing estate management legal support."},
        ],
    },
    "engagements": {
        "intro": "Representative real estate mandates handled by our team.",
        "entries": [
            {"title": "Mixed-Use Development Title Audit", "image_label": "Mixed-use tower — placeholder image", "description": "Conducted a full title and consent audit for a mixed-use development spanning multiple contiguous parcels prior to construction financing drawdown."},
            {"title": "Landowner-Developer Joint Venture", "image_label": "Site handover ceremony — placeholder image", "description": "Structured a joint development agreement between a family landowning group and an institutional developer, including exit and default provisions."},
            {"title": "Mortgage Security Perfection Programme", "image_label": "Bank signing ceremony — placeholder image", "description": "Advised a primary mortgage institution on a portfolio-wide review and correction of defective mortgage security registrations."},
        ],
    },
    "stats": [
        {"value": "500+", "label": "Title due diligence exercises completed"},
        {"value": "1978", "label": "Foundational statute (Land Use Act)"},
        {"value": "3", "label": "States with dedicated regulatory frameworks navigated"},
        {"value": "0", "label": "Shortcuts taken on Governor's Consent"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian real estate law",
        "entries": [
            {"q": "Can I own land outright (freehold) in Nigeria?", "a": "Not in the Western freehold sense. Under the Land Use Act 1978, all land is held by the state Governor in trust; individuals and entities hold Rights of Occupancy, which function similarly to long leaseholds."},
            {"q": "What is Governor's Consent and why is it required?", "a": "Section 22 of the Land Use Act requires the Governor's written consent before a holder of a statutory Right of Occupancy can validly assign, mortgage or sublease the land; a transaction without it is voidable."},
            {"q": "How long does title verification typically take?", "a": "It depends on the state and registry backlog, but a thorough search, root-of-title trace and consent status check should always precede any exchange of funds, regardless of transaction pressure."},
            {"q": "Are service charge disputes common in Nigerian estates?", "a": "Yes — without a clearly drafted estate management or facility management agreement defining scope, billing methodology and dispute resolution, service charge disagreements are one of the most frequent sources of estate litigation."},
        ],
    },
    "cta": {
        "title": "Buying, Developing or Financing Property?",
        "body": "Let our Real Estate & Management team complete title due diligence before you commit funds.",
    },
}

# ---------------------------------------------------------------------------
# 7. Capital Markets & Securities
# ---------------------------------------------------------------------------
PRACTICE_PAGES["capital-markets-securities"] = {
    "title": "Capital Markets & Securities",
    "description": "Public offerings, listings and securities regulation advisory from Herger's & Co., built on the Investments and Securities Act 2007.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Capital Markets & Securities",
        "subtitle": "Advising issuers, underwriters and investors on public offerings, listings and securities compliance under the Investments and Securities Act 2007.",
        "breadcrumbs": _breadcrumbs("Capital Markets & Securities"),
    },
    "overview": {
        "heading": "Bringing Transactions to Market with Regulatory Confidence",
        "image_label": "Stock exchange trading floor — placeholder image",
        "paragraphs": [
            "The Investments and Securities Act 2007 (as subsequently updated) established the Securities and Exchange Commission's apex regulatory authority over Nigeria's capital markets, covering the registration of securities, public offerings, collective investment schemes, and the licensing of capital market operators. Herger's & Co.'s Capital Markets & Securities team advises issuers, sponsors, underwriters, trustees and institutional investors on structuring transactions that satisfy the Commission's rules from prospectus drafting through to admission to trading on the Nigerian Exchange (NGX).",
            "Our work spans initial public offerings, rights issues, bond issuances (both corporate and sub-national), commercial paper programmes and the increasingly active green bond and sukuk markets, each of which carries its own SEC rule set layered on top of the base Investments and Securities Act framework. We coordinate prospectus due diligence with reporting accountants, financial advisers and registrars, and we draft trust deeds, underwriting agreements and vending agreements that correctly allocate liability among transaction parties.",
            "Because many capital markets transactions also engage company law, we work seamlessly with our Mergers & Acquisitions and Corporate Governance teams — for example, ensuring that a rights issue complies with pre-emption provisions in the Companies and Allied Matters Act 2020, or that a listed company's board composition satisfies the SEC Code of Corporate Governance for Public Companies before a transaction proceeds to Commission review.",
            "We also advise on secondary market matters: disclosure obligations for material non-public information, insider dealing risk under the Investments and Securities Act, and the increasingly active enforcement of market conduct rules by both the SEC and NGX Regulation. For asset managers and fund sponsors, we structure and register collective investment schemes, ensuring trustee and custodian arrangements satisfy statutory segregation requirements designed to protect investor funds.",
        ],
        "at_a_glance": [
            "Primary statute: Investments and Securities Act 2007 (as amended)",
            "Regulator: Securities and Exchange Commission",
            "Exchange: Nigerian Exchange Group (NGX)",
            "Typical mandates: IPOs, bonds, rights issues, fund registration",
        ],
    },
    "legislation": {
        "intro": "Capital markets work is rule-dense; our advice tracks both the primary Act and the Commission's subsidiary rules.",
        "entries": [
            {"act": "Investments and Securities Act 2007", "description": "Establishes SEC's regulatory authority over securities registration, public offers, collective investment schemes and capital market operator licensing."},
            {"act": "SEC Rules and Regulations (as amended)", "description": "Detailed subsidiary rules governing prospectus content, book-building, rights issues, bond issuance programmes and sukuk structures."},
            {"act": "Companies and Allied Matters Act 2020", "description": "Governs pre-emption rights, share capital alterations and the corporate mechanics underlying most securities issuances."},
            {"act": "NGX Listing Rules", "description": "Sets admission, continuing disclosure and delisting requirements for companies listed on the Nigerian Exchange."},
            {"act": "SEC Code of Corporate Governance for Public Companies", "description": "Imposes board composition, committee and disclosure standards on public companies raising capital from the market."},
            {"act": "Trustee Investments Act", "description": "Relevant to the powers and duties of trustees appointed under bond trust deeds and collective investment schemes."},
        ],
    },
    "services": {
        "intro": "Full-service capital markets counsel from mandate letter to admission to trading.",
        "entries": [
            {"title": "Initial Public Offerings", "description": "Structuring and executing IPOs, including prospectus drafting, due diligence coordination and SEC registration."},
            {"title": "Bond & Commercial Paper Issuance", "description": "Advising issuers and trustees on corporate bonds, sub-national bonds, commercial paper and green bond programmes."},
            {"title": "Rights Issues & Follow-On Offers", "description": "Structuring rights issues in compliance with CAMA pre-emption rules and SEC procedural requirements."},
            {"title": "Collective Investment Scheme Registration", "description": "Registering mutual funds, REITs and other collective investment schemes with SEC, including trustee and custodian structuring."},
            {"title": "Listings & Continuing Obligations", "description": "Advising on NGX admission requirements and ongoing disclosure and governance obligations post-listing."},
            {"title": "Sukuk & Islamic Finance Structuring", "description": "Structuring Sharia-compliant capital markets instruments consistent with SEC's sukuk framework."},
            {"title": "Market Conduct & Enforcement Defence", "description": "Advising on insider dealing, market manipulation allegations and SEC enforcement proceedings."},
            {"title": "Private Placements", "description": "Structuring exempt private placements of debt and equity securities to qualified institutional investors."},
        ],
    },
    "approach": {
        "intro": "Capital markets transactions demand precision timing across multiple regulators and advisers.",
        "steps": [
            {"title": "Structuring", "description": "We design the instrument and offer structure to match issuer objectives and SEC rule requirements."},
            {"title": "Due Diligence & Documentation", "description": "We coordinate legal due diligence and draft prospectus, trust deed and underwriting documentation."},
            {"title": "Regulatory Clearance", "description": "We manage SEC registration and NGX admission processes, responding to comments efficiently."},
            {"title": "Closing & Post-Issue Compliance", "description": "We support closing mechanics and ongoing continuing disclosure compliance after the transaction completes."},
        ],
    },
    "engagements": {
        "intro": "Representative capital markets mandates handled by our team.",
        "entries": [
            {"title": "Corporate Bond Issuance Programme", "image_label": "Bond signing ceremony — placeholder image", "description": "Advised an issuer on a multi-year corporate bond issuance programme, including trust deed negotiation and SEC shelf registration."},
            {"title": "Rights Issue for Listed Company", "image_label": "Annual general meeting — placeholder image", "description": "Structured and executed a rights issue for a NGX-listed company, ensuring full compliance with pre-emption and disclosure requirements."},
            {"title": "REIT Registration", "image_label": "Commercial property portfolio — placeholder image", "description": "Registered a real estate investment trust with SEC, including trustee appointment and custodial arrangement structuring."},
        ],
    },
    "stats": [
        {"value": "2007", "label": "Foundational Investments & Securities Act"},
        {"value": "15+", "label": "Capital markets transactions advised on"},
        {"value": "3", "label": "Instrument classes covered (equity, debt, funds)"},
        {"value": "1", "label": "Coordinated team across M&A, tax and governance"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian capital markets law",
        "entries": [
            {"q": "Which regulator approves a public offering in Nigeria?", "a": "The Securities and Exchange Commission must register the securities and clear the prospectus before a public offer can proceed, under the Investments and Securities Act 2007 framework."},
            {"q": "Is listing on NGX mandatory after an IPO?", "a": "Not automatically — an issuer can conduct a public offer without listing, but most issuers seeking liquidity and continuing market access proceed to NGX admission under its Listing Rules."},
            {"q": "What is a rights issue and how is it regulated?", "a": "A rights issue offers existing shareholders the opportunity to subscribe for new shares proportionate to their holding; it must comply with CAMA pre-emption provisions and SEC procedural rules."},
            {"q": "Can foreign investors participate in Nigerian capital markets transactions?", "a": "Yes, subject to exchange control and NIPC registration requirements; our team routinely advises foreign institutional investors on Nigerian securities transactions."},
        ],
    },
    "cta": {
        "title": "Planning a Capital Raise or Listing?",
        "body": "Engage our Capital Markets & Securities team early to structure your offering correctly from the outset.",
    },
}

# ---------------------------------------------------------------------------
# 8. Privatization & Venture Capital
# ---------------------------------------------------------------------------
PRACTICE_PAGES["privatization-venture-capital"] = {
    "title": "Privatization & Venture Capital",
    "description": "Privatization transactions, public procurement and venture capital/startup advisory from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Privatization & Venture Capital",
        "subtitle": "Advising on public asset privatization under the Public Enterprises Act and the Public Procurement Act 2007, alongside venture capital and startup investment structuring.",
        "breadcrumbs": _breadcrumbs("Privatization & Venture Capital"),
    },
    "overview": {
        "heading": "From State Divestiture to Startup Financing",
        "image_label": "Infrastructure asset handover — placeholder image",
        "paragraphs": [
            "Nigeria's privatization programme operates under the Public Enterprises (Privatisation and Commercialisation) Act 1999, which established the Bureau of Public Enterprises and the National Council on Privatisation, and — where public procurement processes are engaged in structuring or executing a divestiture — the Public Procurement Act 2007, which mandates open competitive bidding, value-for-money assessment and due process certification for public contracts and asset sales above prescribed thresholds. Herger's & Co. advises both government agencies and private bidders through the full privatization transaction lifecycle.",
            "Our privatization team has advised on transaction structuring for power sector assets, concession arrangements for transport and logistics infrastructure, and the divestiture of government equity stakes in commercial enterprises, always ensuring that due process certificates required under the Public Procurement Act 2007 are properly obtained and that Bureau of Public Enterprises transaction documentation withstands subsequent legislative or judicial scrutiny — a recurring risk given the political sensitivity of major asset sales.",
            "On the venture capital side, we advise Nigerian and diaspora-linked technology startups, angel investors and venture capital funds on seed and growth-stage financing rounds, drawing on the flexible share classes and simplified compliance regime the Companies and Allied Matters Act 2020 introduced for private companies, as well as the Nigeria Startup Act 2022, which creates a formal 'Startup Label' status carrying tax and regulatory incentives for qualifying labelled startups.",
            "We structure convertible instruments (including SAFE-equivalent and convertible loan note structures adapted for Nigerian company law), negotiate term sheets and shareholder agreements that balance founder control with investor protection rights, and advise funds on SEC registration requirements where a vehicle constitutes a collective investment scheme or private equity fund under the Investments and Securities Act 2007 framework.",
        ],
        "at_a_glance": [
            "Privatization statute: Public Enterprises Act 1999",
            "Procurement statute: Public Procurement Act 2007",
            "Startup framework: Nigeria Startup Act 2022",
            "Company law: CAMA 2020 (flexible private company regime)",
            "Typical mandates: asset divestitures, VC rounds, startup structuring",
        ],
    },
    "legislation": {
        "intro": "Privatization and venture capital work draws on distinct but complementary statutory regimes.",
        "entries": [
            {"act": "Public Enterprises (Privatisation and Commercialisation) Act 1999", "description": "Establishes the Bureau of Public Enterprises and National Council on Privatisation and governs the process for divesting government-owned enterprises."},
            {"act": "Public Procurement Act 2007", "description": "Mandates competitive bidding, due process certification and transparency for public contracts and asset sales above statutory thresholds."},
            {"act": "Nigeria Startup Act 2022", "description": "Creates a 'Startup Label' regime offering tax incentives, regulatory sandboxing and access to a dedicated startup investment seed fund for qualifying labelled startups."},
            {"act": "Companies and Allied Matters Act 2020", "description": "Provides the flexible private-company share structuring, single-shareholder companies and simplified compliance startups and investors rely on."},
            {"act": "Nigerian Investment Promotion Commission Act", "description": "Governs foreign investor registration and repatriation guarantees relevant to cross-border venture capital investment."},
            {"act": "Investments and Securities Act 2007", "description": "Relevant where a venture capital or private equity vehicle constitutes a collective investment scheme requiring SEC registration."},
        ],
    },
    "services": {
        "intro": "Counsel spanning state asset divestiture and early-stage private capital formation.",
        "entries": [
            {"title": "Privatization Transaction Advisory", "description": "Advising government agencies and bidders on structuring, bidding and closing privatization transactions."},
            {"title": "Public Procurement Compliance", "description": "Securing due process certification and structuring bids to satisfy Public Procurement Act 2007 requirements."},
            {"title": "Concession & PPP Structuring", "description": "Structuring build-operate-transfer and concession agreements for infrastructure privatization projects."},
            {"title": "Venture Capital Term Sheets & Rounds", "description": "Negotiating seed, Series A and growth-stage term sheets, balancing founder and investor interests."},
            {"title": "Startup Label & Incentive Applications", "description": "Applying for Nigeria Startup Act 'Startup Label' status and related tax and regulatory incentives."},
            {"title": "Convertible Instruments & Cap Table Management", "description": "Drafting convertible notes and advising on cap table structuring across multiple financing rounds."},
            {"title": "Fund Formation & SEC Registration", "description": "Structuring venture capital and private equity funds and managing SEC registration where required."},
            {"title": "Exit & Secondary Sale Structuring", "description": "Advising founders and investors on trade sales, secondary share transfers and IPO exit readiness."},
        ],
    },
    "approach": {
        "intro": "Two distinct transaction rhythms — state divestiture and startup financing — handled with equal rigour.",
        "steps": [
            {"title": "Mandate Scoping", "description": "We clarify whether a transaction sits within public procurement, privatization or private venture financing rules from the outset."},
            {"title": "Structuring", "description": "We design bid, concession or financing structures that satisfy statutory process while meeting commercial objectives."},
            {"title": "Documentation & Negotiation", "description": "We draft and negotiate transaction, term sheet and shareholder documentation to allocate risk appropriately."},
            {"title": "Closing & Post-Completion", "description": "We manage regulatory sign-off, registration and post-completion compliance obligations."},
        ],
    },
    "engagements": {
        "intro": "Representative privatization and venture capital mandates handled by our team.",
        "entries": [
            {"title": "Infrastructure Concession Bid", "image_label": "Toll infrastructure — placeholder image", "description": "Advised a consortium bidder on a transport infrastructure concession, securing Public Procurement Act due process certification."},
            {"title": "Series A Fintech Financing", "image_label": "Startup team meeting — placeholder image", "description": "Structured a Series A round for a Nigerian fintech startup, including convertible bridge notes and a founder-friendly term sheet."},
            {"title": "Startup Label Application", "image_label": "Technology hub workspace — placeholder image", "description": "Secured Nigeria Startup Act 'Startup Label' status for a labelled technology company, unlocking tax and regulatory incentives."},
        ],
    },
    "stats": [
        {"value": "1999", "label": "Foundational Privatisation Act"},
        {"value": "2007", "label": "Public Procurement Act baseline"},
        {"value": "10+", "label": "Venture financing rounds structured"},
        {"value": "2022", "label": "Nigeria Startup Act incentive framework"},
    ],
    "faqs": {
        "heading": "Common questions on privatization and venture capital in Nigeria",
        "entries": [
            {"q": "What is 'due process certification' in a privatization transaction?", "a": "It is a certificate issued under the Public Procurement Act 2007 confirming that a public contract or asset-sale process followed the mandated competitive procurement procedure, a prerequisite for many public transactions to proceed to payment or completion."},
            {"q": "What is Startup Label status under the Nigeria Startup Act?", "a": "It is a formal designation granted to qualifying startups (through the Startup Support and Engagement Portal) that unlocks tax reliefs, regulatory sandbox access and eligibility for the Startup Investment Seed Fund."},
            {"q": "Can foreign venture capital funds invest directly in Nigerian startups?", "a": "Yes, subject to NIPC registration and exchange control certificate of capital importation requirements to guarantee repatriation of returns."},
            {"q": "Do venture capital funds need SEC registration?", "a": "It depends on the fund's structure — vehicles that pool investor capital for collective investment purposes may fall within the Investments and Securities Act 2007 definition of a collective investment scheme, triggering SEC registration."},
        ],
    },
    "cta": {
        "title": "Bidding on a State Asset or Raising a Financing Round?",
        "body": "Our Privatization & Venture Capital team structures both state divestitures and startup financings for durable, enforceable outcomes.",
    },
}

# ---------------------------------------------------------------------------
# 9. Mergers & Acquisition
# ---------------------------------------------------------------------------
PRACTICE_PAGES["mergers-acquisitions"] = {
    "title": "Mergers & Acquisition",
    "description": "M&A structuring, due diligence and FCCPC/SEC merger clearance advisory from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Mergers & Acquisition",
        "subtitle": "Structuring and closing transactions under the Companies and Allied Matters Act 2020 and the Federal Competition and Consumer Protection Act 2018.",
        "breadcrumbs": _breadcrumbs("Mergers & Acquisition"),
    },
    "overview": {
        "heading": "Disciplined Deal Execution from Term Sheet to Closing",
        "image_label": "Deal signing ceremony — placeholder image",
        "paragraphs": [
            "Corporate combinations in Nigeria are governed primarily by Part XII of the Companies and Allied Matters Act 2020, which sets out the statutory scheme of arrangement, merger and takeover procedures, and by the Federal Competition and Consumer Protection Act 2018, which established the Federal Competition and Consumer Protection Commission (FCCPC) as the mandatory merger-review authority for transactions exceeding prescribed thresholds — replacing the Securities and Exchange Commission's former exclusive merger-clearance role for most transactions, though SEC retains parallel oversight for public company and capital-markets-related aspects.",
            "Herger's & Co.'s M&A team runs the full transaction lifecycle: structuring the acquisition vehicle, coordinating legal, financial and tax due diligence, negotiating share purchase or asset purchase agreements (including warranties, indemnities and completion mechanics), and managing the FCCPC merger notification and, where relevant, SEC and sector-regulator approvals — for example, Central Bank of Nigeria approval for banking sector transactions or NCC approval for telecommunications sector deals.",
            "We are equally comfortable on the buy-side and sell-side, and our due diligence methodology is built to surface the issues that most frequently derail Nigerian transactions: unresolved title and Governor's Consent issues on real property assets, unregistered charges and security interests, unresolved tax liabilities, and employment/pension compliance gaps under the Pension Reform Act. We build these findings directly into the risk allocation mechanics of the transaction agreement rather than treating due diligence as a separate, disconnected workstream.",
            "For cross-border transactions, we coordinate with foreign counsel to align Nigerian completion mechanics (share transfer registration, CAC filings, exchange control certificates of capital importation) with the broader multi-jurisdictional signing and closing timetable, ensuring that Nigerian regulatory conditions precedent do not become the critical path item that delays global completion.",
        ],
        "at_a_glance": [
            "Primary statute: CAMA 2020, Part XII (Mergers & Takeovers)",
            "Merger regulator: Federal Competition and Consumer Protection Commission",
            "Parallel regulator: Securities and Exchange Commission (public companies)",
            "Typical mandates: due diligence, SPAs, FCCPC clearance, completion",
        ],
    },
    "legislation": {
        "intro": "M&A transactions engage a layered regulatory framework that must be sequenced correctly to avoid closing delay.",
        "entries": [
            {"act": "Companies and Allied Matters Act 2020, Part XII", "description": "Sets out the statutory procedure for mergers, schemes of arrangement, takeovers and compulsory share acquisitions."},
            {"act": "Federal Competition and Consumer Protection Act 2018", "description": "Establishes the FCCPC as the mandatory merger-review authority for qualifying transactions, with powers to approve, condition or prohibit mergers."},
            {"act": "Investments and Securities Act 2007", "description": "Retains SEC oversight for merger aspects touching public companies and capital markets transactions."},
            {"act": "Pension Reform Act 2014", "description": "Governs employee pension compliance obligations that must be verified and addressed in employment-related due diligence."},
            {"act": "Nigerian Investment Promotion Commission Act", "description": "Governs foreign investor registration requirements relevant to cross-border acquisitions of Nigerian target companies."},
            {"act": "Sector-specific statutes (CBN, NCC, NAICOM regimes)", "description": "Impose additional change-of-control approval requirements for regulated sector targets such as banks, telecoms operators and insurers."},
        ],
    },
    "services": {
        "intro": "Comprehensive transactional support across the deal lifecycle.",
        "entries": [
            {"title": "Legal Due Diligence", "description": "Comprehensive review of corporate, title, tax, employment and litigation risk across target companies."},
            {"title": "Transaction Structuring", "description": "Advising on share versus asset acquisition structures, tax-efficient vehicle design and financing arrangements."},
            {"title": "Share & Asset Purchase Agreements", "description": "Drafting and negotiating warranties, indemnities, price adjustment and completion mechanics."},
            {"title": "FCCPC Merger Notification", "description": "Preparing and managing merger notification filings and responding to FCCPC information requests."},
            {"title": "Sector Regulator Approvals", "description": "Securing CBN, NCC, NAICOM or other sector-specific change-of-control approvals as required."},
            {"title": "Schemes of Arrangement", "description": "Structuring and implementing court-sanctioned schemes of arrangement for complex reorganisations."},
            {"title": "Post-Completion Integration", "description": "Advising on statutory filings, employment harmonisation and governance integration after closing."},
            {"title": "Distressed & Restructuring M&A", "description": "Structuring acquisitions of distressed businesses, including creditor negotiation and asset carve-outs."},
        ],
    },
    "approach": {
        "intro": "A disciplined four-phase process that keeps complex transactions on schedule.",
        "steps": [
            {"title": "Preliminary Structuring", "description": "We agree the optimal acquisition structure and regulatory pathway before due diligence begins."},
            {"title": "Due Diligence", "description": "We investigate the target methodically, flagging risk items for immediate negotiation rather than late surprises."},
            {"title": "Negotiation & Documentation", "description": "We negotiate transaction agreements that reflect due diligence findings and allocate risk appropriately."},
            {"title": "Regulatory Clearance & Closing", "description": "We manage FCCPC, SEC and sector approvals in parallel to keep the transaction on its target closing date."},
        ],
    },
    "engagements": {
        "intro": "Representative M&A mandates handled by our team.",
        "entries": [
            {"title": "Cross-Border Manufacturing Acquisition", "image_label": "Factory floor handshake — placeholder image", "description": "Advised a foreign strategic acquirer on the acquisition of a Nigerian manufacturing business, including FCCPC clearance and Governor's Consent perfection on factory land."},
            {"title": "Fintech Trade Sale", "image_label": "Technology company office — placeholder image", "description": "Represented founders on the sale of a fintech business to a regional financial group, negotiating founder earn-out and warranty caps."},
            {"title": "Banking Sector Scheme of Arrangement", "image_label": "Bank branch exterior — placeholder image", "description": "Advised on a court-sanctioned scheme of arrangement for a banking sector reorganisation, coordinating CBN and court approval processes."},
        ],
    },
    "stats": [
        {"value": "25+", "label": "M&A transactions advised on"},
        {"value": "2018", "label": "FCCPC merger-review framework applied"},
        {"value": "5", "label": "Sector regulators regularly coordinated with"},
        {"value": "2", "label": "Sides equally served — buy and sell"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian M&A law",
        "entries": [
            {"q": "Which transactions require FCCPC merger notification?", "a": "Transactions exceeding thresholds set by the FCCPC's merger review guidelines require mandatory notification and approval before implementation; failure to notify can result in significant penalties and the merger being declared void."},
            {"q": "Is SEC approval still required for M&A transactions?", "a": "SEC retains jurisdiction over merger aspects involving public companies and capital markets matters, operating alongside — not instead of — FCCPC clearance for qualifying transactions."},
            {"q": "What is a scheme of arrangement?", "a": "A court-sanctioned procedure under CAMA 2020 used to implement complex reorganisations, mergers or compromises with creditors or shareholders, requiring court approval after requisite shareholder majorities are obtained."},
            {"q": "How long does a typical Nigerian M&A transaction take to close?", "a": "Timelines vary significantly with regulatory complexity, but well-prepared due diligence and early regulatory engagement materially shorten the path between signing and completion."},
        ],
    },
    "cta": {
        "title": "Structuring a Transaction?",
        "body": "Engage our Mergers & Acquisition team early to align due diligence, structuring and regulatory clearance from the outset.",
    },
}

# ---------------------------------------------------------------------------
# 10. Media & Entertainment Law
# ---------------------------------------------------------------------------
PRACTICE_PAGES["media-entertainment-law"] = {
    "title": "Media & Entertainment Law",
    "description": "Broadcasting, copyright and entertainment industry advisory from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Media & Entertainment Law",
        "subtitle": "Advising broadcasters, producers, artistes and platforms on copyright, broadcasting and advertising regulation across Nigeria's creative economy.",
        "breadcrumbs": _breadcrumbs("Media & Entertainment Law"),
    },
    "overview": {
        "heading": "Legal Counsel for Africa's Fastest-Growing Creative Economy",
        "image_label": "Film production set — placeholder image",
        "paragraphs": [
            "Nigeria's Nollywood film industry, music sector and broadcast media landscape are governed by a distinct regulatory architecture: the Nigerian Copyright Act 2022 (which repealed and modernised the earlier Copyright Act, strengthening enforcement, introducing collective management organisation oversight and updating protection for digital works), the Nigerian Broadcasting Code issued under the National Broadcasting Commission Act, the National Film and Video Censors Board Act governing classification and exhibition of films, and the Advertising Regulatory Council of Nigeria (Establishment) Act 2022 governing advertising content standards.",
            "Herger's & Co.'s media and entertainment team advises production companies, music labels, streaming platforms, broadcasters and individual artistes on rights acquisition and licensing — securing music synchronisation rights, actor and crew engagement agreements, and distribution and streaming licence agreements that correctly allocate territorial and platform-specific rights. We pay particular attention to collective management organisation registration and royalty collection structures under the 2022 Copyright Act, an area where many Nigerian creatives remain under-protected due to informal industry practice.",
            "For broadcasters and platforms, we advise on National Broadcasting Commission licensing, content classification compliance with the National Film and Video Censors Board, and increasingly on the regulatory treatment of video-on-demand and streaming services under evolving NBC guidance. Our advertising and brand practice within this team advises on ARCON compliance, influencer marketing disclosure requirements, and endorsement agreement structuring for talent and brands operating in the Nigerian market.",
            "We also handle entertainment industry disputes — royalty non-payment claims, breach of exclusivity in artiste management agreements, and copyright infringement actions — coordinating with our Litigation & ADR team to pursue both interim injunctive relief and full damages claims where unauthorised use of copyrighted works occurs, whether on traditional broadcast platforms or digital and social media channels.",
        ],
        "at_a_glance": [
            "Primary statute: Nigerian Copyright Act 2022",
            "Broadcast regulator: National Broadcasting Commission",
            "Film classification: National Film and Video Censors Board",
            "Advertising regulator: ARCON (Establishment) Act 2022",
            "Typical mandates: rights licensing, broadcast compliance, royalty disputes",
        ],
    },
    "legislation": {
        "intro": "Media and entertainment practice draws on a modernised, creative-economy-specific statutory framework.",
        "entries": [
            {"act": "Nigerian Copyright Act 2022", "description": "Modernises copyright protection, strengthens enforcement mechanisms and formalises oversight of collective management organisations and royalty collection."},
            {"act": "National Broadcasting Commission Act (as amended)", "description": "Establishes the NBC and the Nigerian Broadcasting Code governing licensing, content standards and broadcast conduct."},
            {"act": "National Film and Video Censors Board Act", "description": "Governs classification, censorship and exhibition licensing for films and video works distributed in Nigeria."},
            {"act": "ARCON (Establishment) Act 2022", "description": "Establishes the Advertising Regulatory Council of Nigeria to regulate advertising content, including influencer and digital marketing disclosure standards."},
            {"act": "Nigerian Communications Act 2003", "description": "Relevant to telecommunications-carried content and platform regulation intersecting with broadcast and streaming services."},
            {"act": "Companies and Allied Matters Act 2020", "description": "Governs the corporate structuring of production companies, labels and joint venture content partnerships."},
        ],
    },
    "services": {
        "intro": "Rights, regulatory and dispute counsel across film, music, broadcast and digital media.",
        "entries": [
            {"title": "Copyright Licensing & Rights Acquisition", "description": "Structuring music synchronisation, distribution and streaming licence agreements across territories and platforms."},
            {"title": "Production & Talent Agreements", "description": "Drafting actor, crew, director and producer engagement agreements for film and television productions."},
            {"title": "Broadcasting Licensing & Compliance", "description": "Advising on National Broadcasting Commission licensing applications and Broadcasting Code compliance."},
            {"title": "Film Classification & Distribution", "description": "Managing National Film and Video Censors Board classification and exhibition licensing processes."},
            {"title": "Advertising & Endorsement Compliance", "description": "Advising brands and talent on ARCON-compliant advertising and influencer endorsement agreements."},
            {"title": "Collective Management & Royalty Structuring", "description": "Advising artistes and rights holders on collective management organisation registration and royalty collection."},
            {"title": "Copyright Enforcement & Litigation", "description": "Pursuing infringement claims and injunctive relief against unauthorised use of copyrighted works."},
            {"title": "Digital & Social Media Content Advisory", "description": "Advising platforms and creators on content moderation, takedown procedures and digital rights management."},
        ],
    },
    "approach": {
        "intro": "We treat every creative work as an asset requiring deliberate rights protection from inception.",
        "steps": [
            {"title": "Rights Mapping", "description": "We identify every category of right embedded in a creative work before any licensing negotiation begins."},
            {"title": "Agreement Structuring", "description": "We draft licensing and talent agreements that clearly allocate territorial, platform and duration-specific rights."},
            {"title": "Regulatory Clearance", "description": "We secure broadcasting, classification and advertising approvals required before content reaches audiences."},
            {"title": "Enforcement", "description": "We act swiftly against infringement, seeking injunctive relief where delay would cause irreversible harm."},
        ],
    },
    "engagements": {
        "intro": "Representative media and entertainment mandates handled by our team.",
        "entries": [
            {"title": "Streaming Distribution Licence", "image_label": "Streaming platform interface — placeholder image", "description": "Negotiated a multi-territory streaming distribution licence for a Nollywood production house, securing minimum guarantee payments and audit rights."},
            {"title": "Artiste Royalty Recovery", "image_label": "Recording studio session — placeholder image", "description": "Recovered unpaid royalties for a recording artiste from a collective management organisation following a documentation dispute."},
            {"title": "Broadcast Licensing Application", "image_label": "Broadcast control room — placeholder image", "description": "Secured National Broadcasting Commission licensing for a new digital terrestrial television channel."},
        ],
    },
    "stats": [
        {"value": "2022", "label": "Modernised Copyright Act applied"},
        {"value": "15+", "label": "Rights and licensing agreements negotiated"},
        {"value": "4", "label": "Regulators navigated (NBC, NFVCB, ARCON, NCC)"},
        {"value": "100%", "label": "Rights clearance verified before release"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian media and entertainment law",
        "entries": [
            {"q": "Who enforces copyright in Nigeria?", "a": "The Nigerian Copyright Commission, empowered under the Nigerian Copyright Act 2022, enforces copyright protection, alongside the courts for civil infringement claims and damages."},
            {"q": "Do I need NBC approval to launch a streaming platform?", "a": "Regulatory treatment of pure video-on-demand services continues to evolve; broadcast-adjacent and terrestrial distribution activities generally require National Broadcasting Commission licensing, and our team advises on current NBC guidance before launch."},
            {"q": "What is a collective management organisation?", "a": "A body registered under the Copyright Act to collectively license and collect royalties on behalf of rights holders such as musicians and composers, subject to Nigerian Copyright Commission oversight."},
            {"q": "Are influencer marketing posts regulated in Nigeria?", "a": "Yes — ARCON's advertising standards extend to influencer and digital marketing content, including disclosure requirements for sponsored posts."},
        ],
    },
    "cta": {
        "title": "Protecting Your Creative Work or Launching a Media Venture?",
        "body": "Our Media & Entertainment Law team secures your rights before your work reaches the market.",
    },
}

# ---------------------------------------------------------------------------
# 11. Litigation & ADR Law
# ---------------------------------------------------------------------------
PRACTICE_PAGES["litigation-adr"] = {
    "title": "Litigation & ADR Law",
    "description": "Commercial litigation, arbitration and mediation advocacy from Herger's & Co., under the Arbitration and Mediation Act 2023.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Litigation & ADR Law",
        "subtitle": "Robust courtroom advocacy and efficient arbitration and mediation representation under the Arbitration and Mediation Act 2023.",
        "breadcrumbs": _breadcrumbs("Litigation & ADR Law"),
    },
    "overview": {
        "heading": "Resolving Disputes Through the Right Forum, Every Time",
        "image_label": "Courtroom interior — placeholder image",
        "paragraphs": [
            "Dispute resolution strategy begins long before a claim is filed. Nigeria's courts derive their jurisdiction from Chapter VII of the 1999 Constitution, with the Federal High Court, State High Courts and the Court of Appeal forming the principal tiers for commercial disputes, applying procedure governed by the Evidence Act 2011 and the respective High Court Civil Procedure Rules. Herger's & Co.'s Litigation & ADR team advises clients not only on how to win a dispute, but on which forum — court, arbitration or mediation — offers the fastest and most enforceable route to resolution.",
            "For arbitration, our advice is grounded in the Arbitration and Mediation Act 2023, which repealed and substantially modernised the former Arbitration and Conciliation Act, introducing emergency arbitrator provisions, third-party funding recognition, consolidation of related arbitrations, and a statutory framework for mediated settlement agreements enforceable in the same manner as arbitral awards. We act as counsel in both domestic and international arbitrations, including proceedings administered by the Lagos Court of Arbitration, the Regional Centre for International Commercial Arbitration, and ICC arbitrations seated in Nigeria or with Nigerian-law-governed contracts.",
            "Our litigation practice covers commercial contract disputes, shareholder and company law disputes, banking and finance litigation, insolvency and winding-up proceedings, and enforcement of foreign judgments and arbitral awards under the Foreign Judgments (Reciprocal Enforcement) Act and the New York Convention as domesticated in Nigerian law. We are equally active before the Lagos Multi-Door Courthouse and equivalent state ADR institutions, which offer court-connected mediation as a faster alternative track for qualifying commercial disputes.",
            "Because litigation outcomes are won substantially through preparation, our team invests heavily in early case assessment — identifying the strongest cause of action, securing evidence before it disappears, and where appropriate pursuing interim injunctive or Mareva-type freezing relief to protect a client's position while the substantive dispute is resolved.",
        ],
        "at_a_glance": [
            "Constitutional basis: Chapter VII, 1999 Constitution",
            "Arbitration statute: Arbitration and Mediation Act 2023",
            "Key institutions: Lagos Court of Arbitration, Multi-Door Courthouse",
            "Typical mandates: commercial litigation, arbitration, mediation, enforcement",
        ],
    },
    "legislation": {
        "intro": "Dispute resolution strategy in Nigeria draws on both constitutional court structure and modernised ADR statute.",
        "entries": [
            {"act": "1999 Constitution, Chapter VII", "description": "Establishes the judicature and the jurisdictional hierarchy of Nigerian courts, including the Federal High Court's exclusive jurisdiction over specified matters."},
            {"act": "Arbitration and Mediation Act 2023", "description": "Modernises Nigerian arbitration law, introducing emergency arbitrator relief, third-party funding recognition and statutory mediation settlement enforcement."},
            {"act": "Evidence Act 2011", "description": "Governs admissibility, burden of proof and the treatment of electronic evidence in Nigerian civil and criminal proceedings."},
            {"act": "Administration of Criminal Justice Act 2015", "description": "Relevant where litigation intersects with parallel criminal proceedings, particularly in fraud-related commercial disputes."},
            {"act": "Companies and Allied Matters Act 2020", "description": "Governs derivative actions, unfair prejudice petitions and shareholder dispute remedies within company law litigation."},
            {"act": "Foreign Judgments (Reciprocal Enforcement) Act", "description": "Governs the recognition and enforcement of foreign court judgments in Nigeria, alongside New York Convention arbitral award enforcement."},
        ],
    },
    "services": {
        "intro": "Advocacy and dispute strategy across every forum and industry sector.",
        "entries": [
            {"title": "Commercial Litigation", "description": "Representing clients in contract, tort and commercial disputes before the Federal and State High Courts."},
            {"title": "Domestic & International Arbitration", "description": "Acting as counsel in institutional and ad hoc arbitrations under the Arbitration and Mediation Act 2023."},
            {"title": "Mediation & Multi-Door Courthouse Advocacy", "description": "Representing parties in court-connected mediation to achieve faster, confidential resolution."},
            {"title": "Company & Shareholder Disputes", "description": "Handling derivative actions, unfair prejudice petitions and boardroom deadlock disputes."},
            {"title": "Banking & Finance Litigation", "description": "Representing lenders and borrowers in loan recovery, security enforcement and guarantee disputes."},
            {"title": "Insolvency & Winding-Up Proceedings", "description": "Advising on corporate insolvency, receivership and winding-up petitions under CAMA 2020."},
            {"title": "Enforcement of Judgments & Awards", "description": "Enforcing domestic judgments, foreign judgments and arbitral awards against Nigerian assets."},
            {"title": "Interim & Injunctive Relief", "description": "Securing urgent interim injunctions and asset-freezing orders to protect a client's position pending trial."},
        ],
    },
    "approach": {
        "intro": "We select forum strategy deliberately, not by default.",
        "steps": [
            {"title": "Early Case Assessment", "description": "We assess merits, evidence and the optimal forum before recommending a dispute resolution strategy."},
            {"title": "Evidence Preservation", "description": "We secure documentary and witness evidence early, including interim relief where evidence is at risk."},
            {"title": "Forum Strategy Execution", "description": "We pursue litigation, arbitration or mediation as appropriate, adapting strategy as the matter develops."},
            {"title": "Enforcement", "description": "We pursue vigorous enforcement of judgments and awards once obtained, including cross-border enforcement where needed."},
        ],
    },
    "engagements": {
        "intro": "Representative litigation and arbitration mandates handled by our team.",
        "entries": [
            {"title": "International Arbitration Defence", "image_label": "Arbitration hearing room — placeholder image", "description": "Defended a Nigerian energy company in an ICC arbitration seated in Lagos, achieving a substantially reduced damages award."},
            {"title": "Shareholder Oppression Petition", "image_label": "Corporate boardroom — placeholder image", "description": "Successfully prosecuted an unfair prejudice petition on behalf of a minority shareholder, securing a share buy-out remedy."},
            {"title": "Cross-Border Judgment Enforcement", "image_label": "Bank asset recovery — placeholder image", "description": "Enforced a foreign court judgment against Nigerian assets, navigating reciprocal enforcement procedure to successful recovery."},
        ],
    },
    "stats": [
        {"value": "2023", "label": "Modernised Arbitration & Mediation Act applied"},
        {"value": "50+", "label": "Litigation and arbitration matters handled"},
        {"value": "3", "label": "Forums covered — courts, arbitration, mediation"},
        {"value": "24/7", "label": "Availability for urgent injunctive relief"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian litigation and ADR",
        "entries": [
            {"q": "Is arbitration faster than litigation in Nigeria?", "a": "Generally yes for commercial disputes, particularly where parties have agreed institutional arbitration rules with defined timelines, though outcomes depend on case complexity and party cooperation."},
            {"q": "What changed under the Arbitration and Mediation Act 2023?", "a": "The Act introduced emergency arbitrator relief, recognised third-party funding, enabled consolidation of related arbitral proceedings, and gave mediated settlement agreements a statutory enforcement mechanism similar to arbitral awards."},
            {"q": "Can a foreign arbitral award be enforced in Nigeria?", "a": "Yes, Nigeria is a New York Convention signatory and foreign arbitral awards are enforceable through Nigerian courts, subject to limited statutory grounds for refusal."},
            {"q": "What is an unfair prejudice petition?", "a": "A statutory remedy under CAMA 2020 allowing a minority shareholder to petition the court where a company's affairs are being conducted in a manner unfairly prejudicial to their interests."},
        ],
    },
    "cta": {
        "title": "Facing a Dispute or Considering Arbitration?",
        "body": "Our Litigation & ADR team will help you choose the right forum and build your case from day one.",
    },
}

# ---------------------------------------------------------------------------
# 12. Corporate Governance
# ---------------------------------------------------------------------------
PRACTICE_PAGES["corporate-governance"] = {
    "title": "Corporate Governance",
    "description": "Board governance, compliance and CAMA 2020 advisory from Herger's & Co.",
    "hero": {
        "eyebrow": "Practices & Law",
        "title": "Corporate Governance",
        "subtitle": "Advising boards and management on governance frameworks under the Companies and Allied Matters Act 2020 and the Nigerian Code of Corporate Governance.",
        "breadcrumbs": _breadcrumbs("Corporate Governance"),
    },
    "overview": {
        "heading": "Governance as a Driver of Value, Not Just Compliance",
        "image_label": "Board meeting — placeholder image",
        "paragraphs": [
            "The Companies and Allied Matters Act 2020 substantially modernised Nigerian company law, introducing single-shareholder companies, simplified statutory declarations, electronic meetings and filings, and a statutory framework for company secretarial compliance that every Nigerian company — public or private — must observe. Herger's & Co.'s Corporate Governance team advises boards, company secretaries and management on building governance structures that satisfy CAMA 2020's minimum requirements while genuinely improving decision-making quality and stakeholder confidence.",
            "For public companies and significant private enterprises, we advise on compliance with the Nigerian Code of Corporate Governance 2018, issued by the Financial Reporting Council of Nigeria under the Financial Reporting Council of Nigeria Act 2011, which sets 'apply and explain' principles on board composition, independence, board committee structures, risk management oversight and remuneration governance. Sector-specific overlays — such as the Central Bank of Nigeria's Code of Corporate Governance for banks and the SEC Code of Corporate Governance for Public Companies — are layered on top of the base framework where applicable, and we ensure clients understand which regime, or combination of regimes, governs their specific entity.",
            "Our governance advisory extends to company secretarial support: preparing board and general meeting documentation, advising on directors' statutory duties (including the codified fiduciary and care duties under CAMA 2020 sections 305-319), managing conflicts of interest and related-party transaction approval processes, and advising on the statutory audit committee and board committee requirements applicable to public companies.",
            "We also advise boards on crisis governance — responding to whistleblower reports, activist shareholder campaigns, and regulatory investigations — ensuring that governance processes function robustly under pressure, not only in routine board cycles. Where governance failures give rise to director liability exposure, we coordinate closely with our Litigation & ADR and White Collar Defence teams to manage the full spectrum of consequences.",
        ],
        "at_a_glance": [
            "Primary statute: Companies and Allied Matters Act 2020",
            "Governance code: Nigerian Code of Corporate Governance 2018 (FRC)",
            "Sector overlays: CBN, SEC, NAICOM governance codes",
            "Typical mandates: board advisory, secretarial compliance, director duties",
        ],
    },
    "legislation": {
        "intro": "Corporate governance advice in Nigeria requires fluency across company law and sector-specific governance codes.",
        "entries": [
            {"act": "Companies and Allied Matters Act 2020", "description": "Governs company incorporation, statutory meetings, director duties, share capital and company secretarial compliance obligations."},
            {"act": "Nigerian Code of Corporate Governance 2018", "description": "Issued by the Financial Reporting Council of Nigeria on an 'apply and explain' basis, covering board composition, independence and risk oversight."},
            {"act": "Financial Reporting Council of Nigeria Act 2011", "description": "Establishes the FRC's authority to issue and enforce corporate governance and financial reporting standards."},
            {"act": "SEC Code of Corporate Governance for Public Companies", "description": "Imposes additional governance requirements specifically on SEC-regulated public companies raising capital from the market."},
            {"act": "CBN Code of Corporate Governance for Banks", "description": "Sets sector-specific governance standards for licensed banks, including board tenure limits and risk committee mandates."},
            {"act": "Public Procurement Act 2007", "description": "Relevant to governance obligations of government-linked entities and their procurement decision processes."},
        ],
    },
    "services": {
        "intro": "Governance counsel for boards, company secretaries and management teams.",
        "entries": [
            {"title": "Board Composition & Effectiveness Advisory", "description": "Advising on board composition, independence assessments and board evaluation processes."},
            {"title": "Company Secretarial Compliance", "description": "Managing statutory filings, board and general meeting documentation and CAC compliance under CAMA 2020."},
            {"title": "Director Duties & Liability Advisory", "description": "Advising directors on statutory fiduciary duties, conflicts of interest and personal liability exposure."},
            {"title": "Governance Code Gap Assessments", "description": "Benchmarking governance practice against the Nigerian Code of Corporate Governance and applicable sector codes."},
            {"title": "Related-Party Transaction Governance", "description": "Designing approval frameworks for related-party transactions to satisfy statutory and code requirements."},
            {"title": "Board & Committee Charters", "description": "Drafting board, audit, risk and remuneration committee charters aligned with governance best practice."},
            {"title": "Crisis & Activist Investor Response", "description": "Advising boards on governance response to whistleblower reports, activist campaigns and regulatory investigations."},
            {"title": "ESG & Sustainability Governance", "description": "Advising on environmental, social and governance disclosure frameworks increasingly expected by investors and regulators."},
        ],
    },
    "approach": {
        "intro": "We treat governance as an operating discipline, reviewed and refreshed continuously.",
        "steps": [
            {"title": "Governance Audit", "description": "We benchmark current board and secretarial practice against CAMA 2020 and applicable governance codes."},
            {"title": "Framework Design", "description": "We design or refresh board charters, committee structures and approval frameworks to close identified gaps."},
            {"title": "Director & Board Training", "description": "We brief directors on statutory duties and emerging governance expectations relevant to their sector."},
            {"title": "Ongoing Secretarial Support", "description": "We provide continuing company secretarial and governance advisory support between formal reviews."},
        ],
    },
    "engagements": {
        "intro": "Representative corporate governance mandates handled by our team.",
        "entries": [
            {"title": "Board Effectiveness Review", "image_label": "Executive board retreat — placeholder image", "description": "Conducted a full board effectiveness review for a mid-cap public company, resulting in revised committee charters and an independence action plan."},
            {"title": "Related-Party Transaction Framework", "image_label": "Finance team review — placeholder image", "description": "Designed a related-party transaction approval framework for a family-controlled group ahead of a planned public listing."},
            {"title": "Governance Crisis Response", "image_label": "Confidential briefing — placeholder image", "description": "Advised a board through an activist shareholder campaign, coordinating governance, litigation and communications strategy."},
        ],
    },
    "stats": [
        {"value": "2020", "label": "Modernised CAMA framework applied"},
        {"value": "30+", "label": "Governance mandates completed"},
        {"value": "4", "label": "Governance codes regularly benchmarked against"},
        {"value": "100%", "label": "Statutory filing deadlines met"},
    ],
    "faqs": {
        "heading": "Common questions on Nigerian corporate governance",
        "entries": [
            {"q": "Is the Nigerian Code of Corporate Governance mandatory?", "a": "It operates on an 'apply and explain' basis for most companies, though sector-specific codes (banking, insurance, public companies) impose binding minimum requirements enforced by the relevant regulator."},
            {"q": "Can a single person own and run a Nigerian company post-CAMA 2020?", "a": "Yes — CAMA 2020 introduced single-shareholder and single-director private companies, simplifying governance requirements for small enterprises while still requiring basic statutory compliance."},
            {"q": "What are a director's core statutory duties under CAMA 2020?", "a": "Sections 305 to 319 codify duties including acting in good faith in the company's best interest, avoiding conflicts of interest, exercising reasonable care and skill, and not making secret profits from the directorship."},
            {"q": "What happens if a company fails its statutory filings?", "a": "Persistent non-compliance can result in Corporate Affairs Commission penalties, striking off the register, and potential personal liability exposure for defaulting directors."},
        ],
    },
    "cta": {
        "title": "Strengthening Your Board's Governance Framework?",
        "body": "Our Corporate Governance team will benchmark your board against CAMA 2020 and applicable governance codes.",
    },
}
