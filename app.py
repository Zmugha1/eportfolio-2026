"""
Zubia Mughal E-Portfolio - Main Landing Page
Senior Applied Data Scientist | Decision Intelligence & AI Governance
Target: Senior IC-3/Manager roles ($160K-$200K)
"""

import streamlit as st
from pathlib import Path

from components.skills_matrix import skills_matrix
from components.project_card import project_card

# Page config - SEO and UX
st.set_page_config(
    page_title="Zubia Mughal, Ed.D. | Senior Applied Data Scientist | AI Governance & Decision Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS
css_path = Path(__file__).parent / "static" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# FontAwesome for icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">',
    unsafe_allow_html=True,
)

# Meta description for SEO
st.markdown(
    '<meta name="description" content="Zubia Mughal, Ed.D. - Senior Applied Data Scientist specializing in '
    'Decision Intelligence, AI Governance, and Model Risk Management. $4.6M+ business impact. '
    '23 years enterprise systems + applied ML research.">',
    unsafe_allow_html=True,
)

# =============================================================================
# SECTION 1: HERO HEADER
# =============================================================================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        <div class="hero-container">
            <h1 class="hero-headline">Zubia Mughal, Ed.D.</h1>
            <p class="hero-subhead">Senior Applied Data Scientist | Decision Intelligence & AI Governance</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="hero-container">
            <p class="hero-tagline">
                Translating complex research into <strong style="color: #64FFDA;">$4.6M+</strong> business impact. 
                23 years enterprise systems architecture + applied ML research.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Hire Me CTA - Above the fold
st.markdown(
    '<div style="margin: 1rem 0 2rem 0;">',
    unsafe_allow_html=True,
)
if st.button("Hire Me | Open to Opportunities", type="primary", use_container_width=False):
    st.switch_page("pages/0_Contact.py")
st.markdown("</div>", unsafe_allow_html=True)

# Stats Row
st.markdown(
    """
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-value">23 Years</div>
            <div class="stat-label">Experience (17 Enterprise + 6 ML)</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">$4.6M</div>
            <div class="stat-label">Revenue Impact Delivered</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">92,000+</div>
            <div class="stat-label">Labor Hours Saved</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">12</div>
            <div class="stat-label">Production ML Systems</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Portfolio completion indicator
st.markdown(
    '<div style="margin: 2rem 0;"><span class="completion-badge">Portfolio Completion: 12/12 Projects</span></div>',
    unsafe_allow_html=True,
)

# =============================================================================
# SECTION 2: SKILLS MATRIX (CRITICAL - PROMINENT)
# =============================================================================
st.markdown("---")
skills_matrix()

# =============================================================================
# SECTION 3: PROJECT GALLERY (12 Projects)
# =============================================================================
st.markdown("---")
st.markdown(
    '<h2 style="font-family: \'Playfair Display\', serif; color: #64FFDA; margin-bottom: 1.5rem;">'
    '<i class="fa fa-folder-open" style="margin-right: 0.5rem;"></i>Project Gallery</h2>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color: #8892B0; margin-bottom: 2rem;">Production ML systems with Model Risk Management (MRM) standards.</p>',
    unsafe_allow_html=True,
)

PROJECTS = [
    {
        "num": 1,
        "title": "Governed A/B Testing with MRM",
        "impact": "Reduced rollout risk with Chi-Square validation and fairness auditing—$180K incremental revenue.",
        "tags": ["Chi-Square", "Fairness Auditing", "MRM"],
        "risk": "High",
        "page": "1_Governed_AB_Testing",
    },
    {
        "num": 2,
        "title": "Survival Analysis for Churn",
        "impact": "Time-to-event modeling with censored data—22% improvement in retention prediction.",
        "tags": ["Time-to-Event", "Censored Data", "Cox PH"],
        "risk": "Medium",
        "page": "2_Survival_Analysis",
    },
    {
        "num": 3,
        "title": "Production Classification",
        "impact": "Drift detection and model registry—99.2% uptime, zero uncaught degradations.",
        "tags": ["Drift Detection", "Model Registry", "MLflow"],
        "risk": "High",
        "page": "3_Production_Classification",
    },
    {
        "num": 4,
        "title": "Customer Segmentation",
        "impact": "K-Means clustering with data contracts—$420K campaign efficiency gain.",
        "tags": ["K-Means", "Data Contracts", "Clustering"],
        "risk": "Low",
        "page": "4_Customer_Segmentation",
    },
    {
        "num": 5,
        "title": "Dimensionality Reduction",
        "impact": "PCA + Feature Store integration—40% faster model training, auditable lineage.",
        "tags": ["PCA", "Feature Store", "Lineage"],
        "risk": "Low",
        "page": "5_Dimensionality_Reduction",
    },
    {
        "num": 6,
        "title": "Association Rules Engine",
        "impact": "Apriori-based real-time scoring—$95K incremental cross-sell revenue.",
        "tags": ["Apriori", "Real-time Scoring", "Rules"],
        "risk": "Medium",
        "page": "6_Association_Rules",
    },
    {
        "num": 7,
        "title": "Causal Impact Analysis",
        "impact": "Synthetic controls + Bayesian inference—validated $310K policy impact.",
        "tags": ["Synthetic Controls", "Bayesian", "Causal Inference"],
        "risk": "High",
        "page": "7_Causal_Impact",
    },
    {
        "num": 8,
        "title": "Document Intelligence",
        "impact": "OCR + PII detection—85% reduction in manual document review hours.",
        "tags": ["OCR", "PII Detection", "NLP"],
        "risk": "Medium",
        "page": "8_Document_Intelligence",
    },
    {
        "num": 9,
        "title": "Retrieval Engineering",
        "impact": "Vector search, reranking, cost optimization—35% latency reduction.",
        "tags": ["Vector Search", "Reranking", "Cost Optimization"],
        "risk": "Medium",
        "page": "9_Retrieval_Engineering",
    },
    {
        "num": 10,
        "title": "Operational Dashboards",
        "impact": "Streaming + alerting—real-time visibility, 2hr MTTR improvement.",
        "tags": ["Streaming", "Alerting", "Dashboards"],
        "risk": "Low",
        "page": "10_Operational_Dashboards",
    },
    {
        "num": 11,
        "title": "RAG Safety & Evaluation",
        "impact": "RAGAS, hallucination detection, guardrails—production-safe RAG deployment.",
        "tags": ["RAGAS", "Hallucination Detection", "Guardrails"],
        "risk": "High",
        "page": "11_RAG_Safety",
    },
    {
        "num": 12,
        "title": "Agent Orchestration",
        "impact": "Tool-use, cost-aware routing, SQL agents—$78K operational savings.",
        "tags": ["Tool-use", "Cost-aware Routing", "SQL Agents"],
        "risk": "High",
        "page": "12_Agent_Orchestration",
    },
]

# 3-column grid
for i in range(0, 12, 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(PROJECTS):
            p = PROJECTS[idx]
            with col:
                project_card(
                    project_num=p["num"],
                    title=p["title"],
                    impact_hook=p["impact"],
                    skill_tags=p["tags"],
                    risk_tier=p["risk"],
                    page_link=p["page"],
                )

# =============================================================================
# SECTION 4: ABOUT SNIPPET
# =============================================================================
st.markdown("---")
st.markdown(
    """
    <div class="about-section">
        <h2 style="font-family: 'Playfair Display', serif; color: #64FFDA; margin-bottom: 1rem;">
            <i class="fa fa-user" style="margin-right: 0.5rem;"></i>About</h2>
        <p style="color: #E6F1FF; line-height: 1.8;">
            <strong>Doctorate in Workforce Development Leadership</strong> (Quantitative Research Focus). 
            Rare combination: <strong>17 years enterprise architecture</strong> + <strong>6 years applied ML</strong>. 
            Specialization in <strong>Decision Intelligence</strong>—systems that executives trust for high-stakes decisions.
        </p>
        <p style="color: #8892B0; margin-top: 1rem;">
            Open to <strong>Senior IC (Staff/Principal)</strong> or <strong>Manager</strong> roles. 
            Location: Milwaukee, WI (Remote preferred). 
            Contact: <a href="mailto:zubiamL4L@gmail.com" style="color: #64FFDA;">zubiamL4L@gmail.com</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================================================
# SECTION 5: FOOTER
# =============================================================================
st.markdown("---")
st.markdown(
    """
    <div class="footer-section">
        <p>
            <a href="https://www.linkedin.com/in/zubiamughal" target="_blank" class="footer-link">
                <i class="fa-brands fa-linkedin"></i> LinkedIn
            </a>
            <a href="https://github.com/Zmugha1" target="_blank" class="footer-link">
                <i class="fa-brands fa-github"></i> GitHub
            </a>
            <a href="mailto:zubiamL4L@gmail.com" class="footer-link">
                <i class="fa fa-envelope"></i> Email
            </a>
        </p>
        <p style="margin-top: 1rem;">
            <a href="#" class="footer-link" style="border: 1px solid #64FFDA; padding: 0.5rem 1rem; border-radius: 8px;">
                <i class="fa fa-download"></i> Download Resume PDF
            </a>
        </p>
        <p class="disclaimer">
            Portfolio demonstrates Model Risk Management (MRM) standards aligned with Burtch Works 2026 AI Governance research.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
