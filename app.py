import streamlit as st
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="Zubia Mughal | Decision Intelligence Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for branding
st.markdown(
    """
    <style>
    .main-header {
        font-family: 'Serif', Georgia;
        color: #0A192F;
        font-size: 3em;
        font-weight: bold;
    }
    .sub-header {
        color: #2E86AB;
        font-size: 1.5em;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border-left: 5px solid #64FFDA;
    }
    .skills-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# HERO SECTION
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<p class="main-header">Zubia Mughal, Ed.D.</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Senior Applied Data Scientist | Decision Intelligence & AI Governance</p>',
        unsafe_allow_html=True,
    )
    st.write(
        "*Translating complex research into $4.6M+ business impact. Bridging rigorous statistical methodology with production-safe AI systems.*"
    )

with col2:
    st.metric("Portfolio Status", "1/12 Complete", "Project 1 Live")

# STATS ROW
st.markdown("---")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(
        '<div class="metric-card"><h3>23 Years</h3><p>Experience</p></div>',
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        '<div class="metric-card"><h3>$4.6M</h3><p>Revenue Impact</p></div>',
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        '<div class="metric-card"><h3>92K+</h3><p>Hours Saved</p></div>',
        unsafe_allow_html=True,
    )
with c4:
    st.markdown(
        '<div class="metric-card"><h3>100%</h3><p>Audit Compliance</p></div>',
        unsafe_allow_html=True,
    )

# SKILLS MATRIX (Inline to avoid import issues)
st.markdown("---")
st.header("🎯 Technical Skills & Governance Expertise")

with st.expander("🔧 Hard Skills (Click to Expand)", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Governance & MRM")
        st.markdown("""
        - Model Risk Management (MRM)
        - AI Safety & Evaluation
        - Statistical Validation (Chi-Square, Power Analysis)
        - Fairness Auditing (4/5ths Rule)
        - Bias Detection & Mitigation
        - Early Stopping Protocols
        """)

        st.subheader("Machine Learning")
        st.markdown("""
        - Survival Analysis & Censored Data
        - Causal Inference & Synthetic Controls
        - GraphRAG & Vector Search
        - Experimental Design (A/B Testing)
        - Retrieval Engineering
        - Agent Orchestration
        """)

    with col2:
        st.subheader("MLOps & Production")
        st.markdown("""
        - Azure ML & MLflow
        - Vector DBs (Pinecone/Chroma)
        - Feature Stores & Data Contracts
        - Drift Detection & Monitoring
        - CI/CD for ML Pipelines
        - Cost Optimization & Token Budgeting
        """)

        st.subheader("Data Engineering")
        st.markdown("""
        - Advanced SQL (CTEs, Window Functions)
        - Data Contracts & Lineage
        - ETL Pipeline Design
        - Neo4j Graph DB
        - Power BI & Executive Dashboards
        """)

with st.expander("💼 Soft Skills & Leadership", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Executive Communication")
        st.markdown("""
        - C-Suite & Board presentations
        - Risk reporting & governance boards
        - Technical translation to business value
        - Cross-functional stakeholder management
        """)

        st.subheader("Governance Leadership")
        st.markdown("""
        - Model Risk Tier classification
        - Compliance documentation (SOX, GDPR)
        - Audit trail creation
        - Approval workflow design
        """)

    with col2:
        st.subheader("Decision Intelligence")
        st.markdown("""
        - Experimental design strategy
        - Cost-benefit analysis under uncertainty
        - Ethics & fairness advocacy
        - Production go/no-go decisions
        """)

        st.subheader("System Reliability")
        st.markdown("""
        - Incident response protocols
        - Rollback decision-making
        - 24/7 system reliability
        - Team enablement & mentoring
        """)

# PROJECT GALLERY
st.markdown("---")
st.header("🎨 Production ML Case Studies")

st.info(
    "🚧 **Portfolio in Progress:** Currently showing Project 1 (Governed A/B Testing). Projects 2-12 coming soon."
)

# Project 1 Card
with st.container():
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("🛡️ Project 1: Governed A/B Testing with MRM")
        st.write(
            "Production-grade experimental design with Model Risk Management framework. Statistical validation with 95% power and 4/5ths fairness compliance."
        )

        st.markdown(
            """
        **Key Skills:** Chi-Square Testing • SQL Window Functions • Statistical Power • Fairness Auditing • Risk-Adjusted ROI
        """
        )

        st.markdown(
            '<span style="background-color: #ffc107; color: black; padding: 4px 8px; border-radius: 12px; font-size: 0.8em;">Medium Risk</span>',
            unsafe_allow_html=True,
        )

    with col2:
        st.metric("Lift", "+17.9%")
        st.metric("Revenue", "$387K")
        st.metric("P-Value", "<0.001")

        if st.button("View Full Case Study", key="p1"):
            st.switch_page("pages/01_project_ab_testing.py")

# Placeholder for future projects
st.markdown("---")
st.caption(
    "**Coming Soon:** Survival Analysis • Causal Impact • Retrieval Engineering • RAG Safety • Agent Orchestration"
)

# ABOUT & CONTACT
st.markdown("---")
st.header("👩‍💼 About")

col1, col2 = st.columns([2, 1])
with col1:
    st.write(
        """
    **Doctorate-trained Applied Data Scientist** with 23 years of enterprise systems architecture and 6 years applied ML research.

    I specialize in **Decision Intelligence**—architecting governance-first ML systems that executives trust and teams actually use. My background bridges rigorous statistical methodology (survival analysis, causal inference, experimental design) with production MLOps.

    **Current Focus:** Model Risk Management (MRM) for AI systems, ensuring statistical validity, fairness compliance, and auditable decision-making at scale.
    """
    )

with col2:
    st.subheader("Contact")
    st.write("📧 zubiamL4L@gmail.com")
    st.write("🔗 LinkedIn: /in/zubiamughal")
    st.write("💻 GitHub: /zmugha1")
    st.write("📍 Milwaukee, WI (Remote)")

# FOOTER
st.markdown("---")
st.caption(
    "*This portfolio demonstrates Model Risk Management (MRM) principles aligned with Burtch Works 2026 AI Governance standards.*"
)
