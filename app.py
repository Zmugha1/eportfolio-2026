import streamlit as st

# Page config
st.set_page_config(
    page_title="Zubia Mughal | Decision Intelligence Architect",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# PREMIUM DARK THEME CSS (Fixes legibility)
st.markdown(
    """
    <style>
    /* Main text colors */
    .main-header {
        font-family: 'Georgia', serif;
        color: #E6F1FF;
        font-size: 3.2em;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 0.2em;
    }
    .sub-header {
        color: #64FFDA;
        font-size: 1.4em;
        font-weight: 300;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 1em;
    }
    .tagline {
        color: #8892B0;
        font-size: 1.1em;
        font-style: italic;
        line-height: 1.6;
    }

    /* Metric Cards - Dark background with teal accent */
    .metric-container {
        background-color: #112240;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #233554;
        border-left: 5px solid #64FFDA;
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-container:hover {
        transform: translateY(-2px);
        border-color: #64FFDA;
    }
    .metric-number {
        color: #64FFDA;
        font-size: 2.5em;
        font-weight: 700;
        margin: 0;
    }
    .metric-label {
        color: #8892B0;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-top: 8px;
    }

    /* Skills section */
    .skills-container {
        background-color: #112240;
        border-radius: 12px;
        padding: 25px;
        margin: 10px 0;
        border: 1px solid #233554;
    }
    .skills-header {
        color: #64FFDA;
        font-size: 1.2em;
        font-weight: 600;
        margin-bottom: 15px;
        border-bottom: 2px solid #233554;
        padding-bottom: 10px;
    }
    .skill-item {
        color: #CCD6F6;
        padding: 5px 0;
        font-size: 0.95em;
    }

    /* Project cards */
    .project-card {
        background-color: #112240;
        border-radius: 12px;
        padding: 30px;
        border: 1px solid #233554;
        margin-bottom: 20px;
        transition: all 0.3s;
    }
    .project-card:hover {
        border-color: #64FFDA;
        box-shadow: 0 10px 30px -15px rgba(2, 12, 27, 0.7);
    }
    .project-title {
        color: #E6F1FF;
        font-size: 1.5em;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .project-impact {
        color: #64FFDA;
        font-size: 2em;
        font-weight: 700;
    }
    .risk-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .risk-low { background-color: rgba(100, 255, 218, 0.1); color: #64FFDA; border: 1px solid #64FFDA; }
    .risk-medium { background-color: rgba(255, 193, 7, 0.1); color: #ffc107; border: 1px solid #ffc107; }
    .risk-high { background-color: rgba(220, 53, 69, 0.1); color: #ff6b6b; border: 1px solid #ff6b6b; }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #0A192F;
    }
    .stSidebar [data-testid="stSidebarNav"] {
        background-color: #0A192F;
        padding-top: 20px;
    }
    .stSidebar [data-testid="stSidebarNav"] a {
        color: #CCD6F6 !important;
        font-size: 0.9em;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 2px 10px;
        transition: all 0.2s;
    }
    .stSidebar [data-testid="stSidebarNav"] a:hover {
        background-color: #112240;
        color: #64FFDA !important;
    }
    .stSidebar [data-testid="stSidebarNav"] a:active {
        background-color: #64FFDA;
        color: #0A192F !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# SIDEBAR - HIRING-FOCUSED NAVIGATION (Not file names!)
with st.sidebar:
    st.markdown("### 🎯 Impact Areas")
    st.caption("Select a case study to view governance framework & ROI")

    # Navigation buttons that sound like business outcomes
    if st.button("📧 Campaign Optimization", use_container_width=True, type="primary"):
        st.switch_page("pages/01_project_ab_testing.py")

    st.markdown("**Coming Soon:**")

    st.button("⏱️ Churn Prevention", use_container_width=True, disabled=True)
    st.button("🎯 Targeting Accuracy", use_container_width=True, disabled=True)
    st.button("👥 Customer Intelligence", use_container_width=True, disabled=True)
    st.button("📉 Dimensionality Mgmt", use_container_width=True, disabled=True)
    st.button("🛒 Cross-sell Engine", use_container_width=True, disabled=True)
    st.button("📊 Causal ROI Analysis", use_container_width=True, disabled=True)
    st.button("📄 Document AI", use_container_width=True, disabled=True)
    st.button("🔍 Enterprise Search", use_container_width=True, disabled=True)
    st.button("⚡ Real-time Monitoring", use_container_width=True, disabled=True)
    st.button("🤖 Safe RAG Systems", use_container_width=True, disabled=True)
    st.button("🎛️ Agent Orchestration", use_container_width=True, disabled=True)

    st.markdown("---")
    st.markdown("**Contact**")
    st.markdown("📧 zubiamL4L@gmail.com")
    st.markdown("🔗 [LinkedIn](https://linkedin.com/in/zubiamughal)")
    st.markdown("💻 [GitHub](https://github.com/zmugha1)")

# MAIN CONTENT
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<p class="main-header">Zubia Mughal, Ed.D.</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Decision Intelligence Architect</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="tagline">Governance-first AI systems that executives trust. Bridging rigorous statistical methodology with $4.6M+ business impact.</p>',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        '<div style="background-color: #112240; padding: 20px; border-radius: 12px; border: 1px solid #64FFDA; text-align: center;">',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="color: #8892B0; font-size: 0.9em; margin: 0;">Portfolio Status</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="color: #64FFDA; font-size: 2em; font-weight: 700; margin: 0;">1/12</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="color: #E6F1FF; font-size: 0.8em; margin: 0;">Projects Live</p>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# METRICS ROW - High Contrast Dark Cards
st.markdown("### 📊 Enterprise Impact Metrics")
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        """
    <div class="metric-container">
        <p class="metric-number">23</p>
        <p class="metric-label">Years Experience</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        """
    <div class="metric-container">
        <p class="metric-number">$4.6M</p>
        <p class="metric-label">Revenue Impact</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        """
    <div class="metric-container">
        <p class="metric-number">92K+</p>
        <p class="metric-label">Hours Automated</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with m4:
    st.markdown(
        """
    <div class="metric-container">
        <p class="metric-number">100%</p>
        <p class="metric-label">Audit Compliance</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# SKILLS MATRIX
st.markdown("---")
st.markdown("### 🛡️ Governance-First Capabilities")

tab1, tab2 = st.tabs(["🔧 Technical Architecture", "💼 Strategic Leadership"])

with tab1:
    c1, c2 = st.columns(2)

    with c1:
        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Model Risk Management (MRM)</p>
                <p class="skill-item">• Risk tier classification & approval workflows</p>
                <p class="skill-item">• Statistical validation (power analysis, significance)</p>
                <p class="skill-item">• Fairness auditing (4/5ths rule, disparate impact)</p>
                <p class="skill-item">• Early stopping & harm detection protocols</p>
                <p class="skill-item">• Audit trail documentation (SOX, GDPR compliant)</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Experimental Design</p>
                <p class="skill-item">• A/B/n testing with Chi-Square & Bayesian methods</p>
                <p class="skill-item">• Survival analysis (time-to-event, censored data)</p>
                <p class="skill-item">• Causal inference (synthetic controls, diff-in-diff)</p>
                <p class="skill-item">• Cost-optimized sampling strategies</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with c2:
        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Production MLOps</p>
                <p class="skill-item">• Azure ML & MLflow model registry</p>
                <p class="skill-item">• Drift detection & automated retraining</p>
                <p class="skill-item">• Vector DBs (Pinecone/Chroma) & GraphRAG</p>
                <p class="skill-item">• Feature stores & data contracts</p>
                <p class="skill-item">• Cost-aware LLM orchestration</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Advanced Analytics</p>
                <p class="skill-item">• SQL optimization (CTEs, window functions)</p>
                <p class="skill-item">• Segmentation (K-means, hierarchical)</p>
                <p class="skill-item">• Association rules & recommendation engines</p>
                <p class="skill-item">• Real-time operational dashboards</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

with tab2:
    c1, c2 = st.columns(2)

    with c1:
        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Executive Communication</p>
                <p class="skill-item">• Board-level risk reporting</p>
                <p class="skill-item">• C-Suite technical translation</p>
                <p class="skill-item">• Go/no-go decision frameworks</p>
                <p class="skill-item">• Business case development ($ impact)</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Governance Leadership</p>
                <p class="skill-item">• Cross-functional risk management</p>
                <p class="skill-item">• Compliance documentation</p>
                <p class="skill-item">• Incident response protocols</p>
                <p class="skill-item">• Ethics & fairness advocacy</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with c2:
        with st.container():
            st.markdown(
                """
            <div class="skills-container">
                <p class="skills-header">Decision Intelligence</p>
                <p class="skill-item">• Cost-benefit under uncertainty</p>
                <p class="skill-item">• Multi-stakeholder alignment</p>
                <p class="skill-item">• Production reliability strategy</p>
                <p class="skill-item">• Team enablement & mentoring</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

# FEATURED PROJECT (The Hiring Hook)
st.markdown("---")
st.markdown("### 🎨 Featured Case Study")

with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(
            '<p class="project-title">📧 Campaign Optimization with MRM</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <p style="color: #8892B0; font-size: 1.1em; line-height: 1.6;">
        Production-grade A/B testing framework with Model Risk Management governance.
        Eliminated $480K in wasteful spend while generating $387K risk-adjusted revenue
        through statistical validation and fairness auditing.
        </p>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <span class="risk-badge risk-medium">Medium Risk Tier</span>
        <span style="margin-left: 10px; color: #64FFDA; font-size: 0.9em;">
        • Chi-Square • SQL Window Functions • 4/5ths Fairness Rule • 95% Power
        </span>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            '<p style="color: #8892B0; font-size: 0.9em; margin: 0;">Risk-Adjusted Revenue</p>',
            unsafe_allow_html=True,
        )
        st.markdown('<p class="project-impact">$387K</p>', unsafe_allow_html=True)
        st.markdown(
            '<p style="color: #64FFDA; font-size: 1.2em; font-weight: 600; margin: 0;">+17.9% Lift</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color: #8892B0; font-size: 0.8em; margin-top: 5px;">P &lt; 0.001</p>',
            unsafe_allow_html=True,
        )

        if st.button("View Full Case Study →", type="primary", use_container_width=True):
            st.switch_page("pages/01_project_ab_testing.py")

    st.markdown("</div>", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("---")
st.markdown("### 👩‍💼 About")

col1, col2 = st.columns([2, 1])
with col1:
    st.write(
        """
    **Doctorate-trained Applied Data Scientist** with 23 years of enterprise systems architecture
    and 6 years applied ML research.

    I specialize in **Decision Intelligence**—architecting governance-first ML systems that
    executives trust and teams actually use. My background bridges rigorous statistical methodology
    (survival analysis, causal inference, experimental design) with production MLOps at scale.

    **Current Focus:** Model Risk Management (MRM) for AI systems, ensuring statistical validity,
    fairness compliance, and auditable decision-making for regulated industries.
    """
    )

with col2:
    st.markdown("**Hiring Status**")
    st.markdown("🟢 **Open to Opportunities**")
    st.markdown("**Target Roles:**")
    st.markdown("• Senior Applied Data Scientist (IC-3/4)")
    st.markdown("• Decision Intelligence Lead")
    st.markdown("• AI Governance & Risk Manager")
    st.markdown("**Location:** Milwaukee, WI (Remote)")
    st.markdown("**Contact:** zubiamL4L@gmail.com")

# FOOTER
st.markdown("---")
st.caption(
    """
*This portfolio demonstrates Model Risk Management (MRM) principles aligned with
Burtch Works 2026 AI Governance standards and production ML interview requirements.*
"""
)
