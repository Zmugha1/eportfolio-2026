"""
Zubia Mughal E-Portfolio - Main Landing Page
Decision Intelligence Architect | Senior IC-3/Manager ($160K-$200K)
"""

import streamlit as st
from pathlib import Path

from components.skills_matrix import skills_matrix
from components.project_card import project_card

# Page config
st.set_page_config(
    page_title="Zubia Mughal, Ed.D. | Decision Intelligence & AI Governance",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar: Project links + progress tracker
with st.sidebar:
    st.markdown("### Portfolio Progress")
    st.markdown("**1/12 Projects Complete**")
    st.markdown("---")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/01_project_ab_testing.py", label="1. Governed A/B Testing", icon="📊")
    st.markdown("---")
    st.markdown("*2–12: Coming soon*")

# Inject custom CSS
css_path = Path(__file__).parent / "static" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">',
    unsafe_allow_html=True,
)

# =============================================================================
# HERO
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
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Stats
st.markdown(
    """
    <div class="stats-row">
        <div class="stat-card"><div class="stat-value">23 Years</div><div class="stat-label">Experience</div></div>
        <div class="stat-card"><div class="stat-value">$4.6M</div><div class="stat-label">Revenue Impact</div></div>
        <div class="stat-card"><div class="stat-value">92K+</div><div class="stat-label">Hours Saved</div></div>
        <div class="stat-card"><div class="stat-value">12</div><div class="stat-label">Production Systems</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div style="margin: 2rem 0;"><span class="completion-badge">Portfolio: 1/12 Projects</span></div>', unsafe_allow_html=True)

# =============================================================================
# SKILLS MATRIX (PROMINENT)
# =============================================================================
st.markdown("---")
skills_matrix()

# =============================================================================
# PROJECT GALLERY
# =============================================================================
st.markdown("---")
st.markdown(
    '<h2 style="font-family: \'Playfair Display\', serif; color: #64FFDA;">'
    '<i class="fa fa-folder-open" style="margin-right: 0.5rem;"></i>Project Gallery</h2>',
    unsafe_allow_html=True,
)

PROJECTS = [
    (1, "Governed A/B Testing", "$387K Risk-Adjusted Revenue", ["MRM", "Chi-Square", "Fairness"], "Medium", "01_project_ab_testing"),
    (2, "Survival Analysis for Churn", "Time-to-Event, Censored Data", ["Time-to-Event", "Cox PH"], "Low", "02_project_survival"),
    (3, "Production Classification", "Drift Detection, Model Registry", ["Drift Detection", "MLflow"], "Medium", "03_project_classification"),
    (4, "Customer Segmentation", "K-Means, Data Contracts", ["K-Means", "Data Contracts"], "Low", "04_project_segmentation"),
    (5, "Dimensionality Reduction", "PCA, Feature Store", ["PCA", "Feature Store"], "Low", "05_project_pca"),
    (6, "Association Rules Engine", "Apriori, Real-time", ["Apriori", "Real-time"], "Medium", "06_project_rules"),
    (7, "Causal Impact Analysis", "Synthetic Controls", ["Synthetic Controls", "Bayesian"], "High", "07_project_causal"),
    (8, "Document Intelligence", "OCR, PII Detection", ["OCR", "PII"], "Medium", "08_project_document"),
    (9, "Retrieval Engineering", "Vector Search, Cost Optimization", ["Vector Search", "RAG"], "High", "09_project_retrieval"),
    (10, "Operational Dashboards", "Streaming, Alerting", ["Streaming", "Alerting"], "Low", "10_project_dashboards"),
    (11, "RAG Safety & Evaluation", "RAGAS, Guardrails", ["RAGAS", "Guardrails"], "High", "11_project_rag"),
    (12, "Agent Orchestration", "Tool-use, Cost-aware", ["Tool-use", "Agents"], "High", "12_project_agents"),
]

for i in range(0, 12, 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(PROJECTS):
            num, title, impact, tags, risk, page = PROJECTS[idx]
            with col:
                project_card(num, title, impact, tags, risk, page)

# =============================================================================
# ABOUT
# =============================================================================
st.markdown("---")
st.markdown(
    """
    <div class="about-section">
        <h2 style="font-family: 'Playfair Display', serif; color: #64FFDA;">
            <i class="fa fa-user" style="margin-right: 0.5rem;"></i>About</h2>
        <p style="color: #E6F1FF; line-height: 1.8;">
            <strong>Doctorate in Workforce Development Leadership</strong> (Quantitative Research). 
            17 years enterprise architecture + 6 years applied ML. 
            Specialization: <strong>Decision Intelligence</strong>—systems executives trust.
        </p>
        <p style="color: #8892B0; margin-top: 1rem;">
            Milwaukee, WI (Remote) | <a href="mailto:zubiamL4L@gmail.com" style="color: #64FFDA;">zubiamL4L@gmail.com</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("---")
st.markdown(
    """
    <div class="footer-section">
        <p>
            <a href="https://www.linkedin.com/in/zubiamughal" target="_blank" class="footer-link"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
            <a href="https://github.com/Zmugha1" target="_blank" class="footer-link"><i class="fa-brands fa-github"></i> GitHub</a>
            <a href="mailto:zubiamL4L@gmail.com" class="footer-link"><i class="fa fa-envelope"></i> Email</a>
        </p>
        <p style="margin-top: 1rem;">
            <a href="#" class="footer-link" style="border: 1px solid #64FFDA; padding: 0.5rem 1rem; border-radius: 8px;">
                <i class="fa fa-download"></i> Download Resume PDF
            </a>
        </p>
        <p class="disclaimer">MRM standards aligned with Burtch Works 2026 AI Governance research.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
