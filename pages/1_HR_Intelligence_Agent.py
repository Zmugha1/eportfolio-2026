"""
HR Intelligence Agent: 60K Hours Saved
Impact Networking (Impact My Biz) - Agentic RAG with GraphRAG, Azure ML
CRAIG framework: Context, Role, Action, Impact, Growth
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from components.sidebar_nav import render_sidebar_nav

try:
    import graphviz
    HAS_GRAPHVIZ = True
except ImportError:
    HAS_GRAPHVIZ = False

st.set_page_config(
    page_title="HR Intelligence Agent | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Custom CSS - dark theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
[data-testid="stVerticalBlock"] > div { font-family: 'Inter', -apple-system, sans-serif !important; color: #CCD6F6 !important; }
[data-testid="stMarkdown"] p, span, div { color: #CCD6F6 !important; }
[data-testid="stMarkdown"] h1, h2, h3 { color: #CCD6F6 !important; }
[data-testid="stTabs"] [role="tab"], [data-testid="stTabs"] button { color: #CCD6F6 !important; }
[data-testid="stTabs"] [aria-selected="true"] { color: #CCD6F6 !important; border-bottom-color: #8892B0 !important; }
.metric-card { background-color: #112240; border: 2px solid #8892B0; padding: 1.2rem; border-radius: 10px; text-align: center; color: #CCD6F6; margin: 0.5rem 0; }
.governance-rule { background-color: rgba(136,146,176,0.15); border-left: 4px solid #8892B0; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0; color: #CCD6F6; }
.tech-stack { display: inline-block; background: rgba(136,146,176,0.2); padding: 4px 10px; margin: 2px; border-radius: 6px; font-size: 0.85em; color: #CCD6F6; }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.title("HR Intelligence Agent: 60K Hours Saved")
st.markdown("*Impact Networking (Impact My Biz) | Agentic RAG with GraphRAG, Azure ML*")
st.markdown('<span style="background: rgba(220,53,69,0.2); color: #ff6b6b; padding: 6px 12px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">HIGH RISK: HR data (ERISA, HIPAA, salary)</span>', unsafe_allow_html=True)
st.markdown("---")

# ==================== CRAIG TABS ====================
context_tab, role_tab, action_tab, impact_tab, growth_tab = st.tabs([
    "CONTEXT: The Crisis",
    "ROLE: The Architect",
    "ACTION: 5-Month Build",
    "IMPACT: 60K Hours",
    "GROWTH: Scaling",
])

# ==================== CONTEXT TAB ====================
with context_tab:
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("The Crisis at Impact Networking")
        st.write("""
        The HR department received **200-300 emails/day** (500-person company). **80%** asked the same repetitive questions:
        - "How many PTO days do I have left?"
        - "When is the next enrollment period?"
        - "What's my salary vs. my pay rate?" (synonym confusion)
        - "How do I apply for parental leave?"

        **The Cost:** 1-2 hours daily per HR person on repetitive responses. At $60/hr fully loaded × 5 HR staff = **$18K/month**. Annual: **$216K in manual email handling**.
        """)
        st.error("""
        **Compliance Risk:**
        - Wrong benefits answer = ERISA violation
        - Sharing other employees' info = HIPAA/privacy breach
        - Inconsistent policy = discrimination liability
        """)
    with col2:
        st.subheader("Before Metrics")
        st.metric("Daily Repetitive Emails", "250+", "↑")
        st.metric("Response Time", "4-6 hours", "")
        st.metric("HR Satisfaction", "32%", "↓")
        st.metric("Cost per Inquiry", "$12.50", "")
        st.markdown('<div style="background-color: #112240; padding: 1rem; border-radius: 8px; border-left: 4px solid #ff6b6b;">"I emailed HR 3 days ago about my PTO and still haven\'t heard back..."</div>', unsafe_allow_html=True)

# ==================== ROLE TAB ====================
with role_tab:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Founding Member: AI as a Service Unit")
        st.write("""
        I didn't just build a chatbot—I architected an **agentic system** that behaves like a senior HR generalist with institutional memory and compliance guardrails.

        **Dual Mandate:**
        1. **Technical:** RAG pipeline, vector embeddings, confidence scoring (migrating from Flux Prompt)
        2. **Governance:** "HR Brain"—rules for what AI can/cannot say, security protocols, synonym resolution (salary = pay = compensation)

        **Constraint:** Prove ROI in 4 months or lose budget.
        """)
        st.info("**Recruiter Insight:** 70% hands-on coding (Python, Azure ML, vector DBs) + 30% strategic (governance with C-suite).")
    with col2:
        st.subheader("Tech Stack")
        for tech in ["Python 3.9", "Azure ML Studio", "GraphRAG", "Vector DB (Pinecone)", "OpenAI Embeddings", "MS Teams API", "SharePoint Crawler", "VADER (Sentiment)"]:
            st.markdown(f'<span class="tech-stack">{tech}</span>', unsafe_allow_html=True)
        st.divider()
        st.write("**Team:** Chief AI Officer, 2 ML Engineers, 1 Data Engineer, 1 PM, HR SMEs")

# ==================== ACTION TAB ====================
with action_tab:
    phase = st.select_slider(
        "Build Phase:",
        options=["Month 1: Foundation", "Month 2: Semantic Layer", "Month 3: Intelligence", "Month 4: Reinforcement", "Month 5: Production"],
        value="Month 3: Intelligence",
    )

    if phase == "Month 1: Foundation":
        st.subheader("Month 1: Knowledge Base & Governance Foundation")
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write("""
            **Challenge:** 10,000+ HR documents across SharePoint—policy PDFs, benefits guides. Raw ChatGPT would hallucinate.

            **Solution:**
            1. **Document Ingestion:** Python crawler for PDFs, Word, email archives
            2. **Hierarchical Chunking:** Parent-child so sub-policy retains context
            3. **Security Tags:** Public | Restricted (salary bands) | Confidential (medical)
            """)
        with col2:
            st.metric("Documents Processed", "10,000+")
            st.metric("Avg. Chunk Size", "512 tokens")
            st.metric("Security Tags", "100%")
            st.markdown("""
            <div class="governance-rule">
            <strong>Governance Rule #1:</strong><br>
            If query contains "salary" or "pay" → Verify SSO before retrieving Restricted docs.
            </div>
            """, unsafe_allow_html=True)

    elif phase == "Month 2: Semantic Layer":
        st.subheader("Month 2: Semantic Layer (Synonym Resolution)")
        st.write("Employees ask the same question 20 ways: 'salary' vs 'pay' vs 'compensation'; 'PTO' vs 'vacation' vs 'leave'.")
        col1, col2 = st.columns(2)
        with col1:
            user_query = st.text_input("Test Query:", "How many vacation days do I have left?")
            if user_query:
                st.success("""
                **Resolution:** "vacation days" → PTO_Balance | "I" → Current user (SSO) | Confidence: 98%
                """)
        with col2:
            for canonical, terms in [("Salary", "pay, compensation, wages"), ("PTO", "vacation, time off, leave"), ("Benefits", "insurance, 401k, retirement"), ("Enrollment", "sign up, register, apply")]:
                with st.expander(canonical):
                    st.caption(f"Synonyms: {terms}")

    elif phase == "Month 3: Intelligence":
        st.subheader("Month 3: Vector Embeddings & Confidence Scoring")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.code("""
# Tier 1: Exact semantic match
if exact_matches[0].score > 0.95:
    return exact_matches, confidence=0.98, tier=1

# Tier 2: Synonym expansion
expanded_query = expand_synonyms(query)
if synonym_matches[0].score > 0.85:
    return synonym_matches, confidence=0.85, tier=2

# Tier 3: Vector fallback
return similar, confidence=0.65, tier=3, warning=True
            """, language="python")
            st.info("**Breakthrough:** Confidence calibration—if Tier 1 contradicted history, downgrade to Tier 2 with human verification.")
        with col2:
            fig = go.Figure(go.Bar(x=["Tier 1 (Exact)", "Tier 2 (Synonym)", "Tier 3 (Vector)"], y=[98, 85, 65], marker_color=["#2ecc71", "#f39c12", "#e74c3c"]))
            fig.update_layout(paper_bgcolor="rgba(10,25,47,0)", plot_bgcolor="rgba(17,34,64,0.5)", font=dict(color="#CCD6F6"), title="Confidence by Tier", height=280)
            st.plotly_chart(fig, use_container_width=True)

    elif phase == "Month 4: Reinforcement":
        st.subheader("Month 4: Human-in-the-Loop & RLHF")
        st.write("Thumbs up/down wasn't just logging—**reinforcement learning** adjusted vector weights.")
        st.code("""
# Boost alternatives when user thumbs down
alternatives = find_semantic_neighbors(feedback.query, exclude=feedback.chunks)
for alt in alternatives:
    alt.weight *= 1.2

# Sentiment on free-text
if sentiment < -0.5:
    alert_hr_team(feedback)
        """, language="python")
        st.metric("Thumbs Down Rate", "3.2%", "↓ from 15% in Month 3")
        st.metric("Sentiment Score", "+0.72", "Positive")

    else:  # Production
        st.subheader("Month 5: Production & Security Hardening")
        st.write("""
        **Four-Eyes Protocol:** Salary → manager approval | Medical leave → HR partner | PIP employee asking termination → flag.

        **Anti-Hallucination:** Confidence < 70% → "Let me connect you with HR" | Other employees → "I cannot discuss" | Policy conflict → "HR will contact you."
        """)
        if HAS_GRAPHVIZ:
            try:
                arch = graphviz.Digraph()
                arch.attr(rankdir='TB')
                arch.node('A', 'Employee Query', shape='oval')
                arch.node('B', 'Semantic Layer', shape='diamond')
                arch.node('C', 'Governance Engine', shape='hexagon')
                arch.node('D', 'Vector DB (GraphRAG)', shape='cylinder')
                arch.node('E', 'Confidence Scorer', shape='box')
                arch.node('F', 'HR SME Validation', shape='house')
                arch.node('G', 'Response + Lineage', shape='ellipse')
                arch.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'])
                st.graphviz_chart(arch)
            except Exception:
                st.code("Query → Semantic → Governance → Vector DB → Confidence → HR Validation → Response")
        else:
            st.code("Query → Semantic → Governance → Vector DB → Confidence → HR Validation → Response")

# ==================== IMPACT TAB ====================
with impact_tab:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h2>60,000</h2><p>Hours Saved Annually</p><small>Across 500 employees</small></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h2>$216K</h2><p>Cost Avoidance</p><small>$60/hr × 1.5 hrs/day × 5 HR</small></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h2>94%</h2><p>Accuracy Rate</p><small>Up from 68% (Month 2)</small></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h2>4.2★</h2><p>Employee Satisfaction</p><small>Up from 2.1★</small></div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("ROI Breakdown")
    roi_data = pd.DataFrame({
        "Metric": ["Pre-Implementation Labor", "Post-Implementation Labor", "System Maintenance", "Net Savings"],
        "Annual_Cost": [216000, 28800, 14400, 172800],
    })
    fig = px.bar(roi_data, x="Metric", y="Annual_Cost", title="Annual Cost: Manual vs. AI-Assisted HR",
        color="Metric", color_discrete_map={"Pre-Implementation Labor": "#e74c3c", "Post-Implementation Labor": "#3498db", "System Maintenance": "#f39c12", "Net Savings": "#2ecc71"})
    fig.update_layout(paper_bgcolor="rgba(10,25,47,0)", plot_bgcolor="rgba(17,34,64,0.5)", font=dict(color="#CCD6F6"), height=350)
    st.plotly_chart(fig, use_container_width=True)

    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown("**HR Transformation**")
        st.write("Response: 4 hrs → 30 sec | First-call resolution: 89%")
    with i2:
        st.markdown("**Compliance**")
        st.write("Zero privacy breaches | 100% audit trail | 50-state consistency")
    with i3:
        st.markdown("**Demand Gen**")
        st.write("3 additional AI agent requests in 6 months | Proved AI-as-a-Service")

# ==================== GROWTH TAB ====================
with growth_tab:
    st.write("**Scaling Strategy:** Core architecture cloned for other departments by swapping semantic layer and governance rules.")
    st.subheader("6-Month Scaling Roadmap")
    timeline = pd.DataFrame({
        "Project": ["HR Agent", "L&D Assistant", "IT Assessment", "Sales Enablement", "External Pilot"],
        "Reuse_%": [0, 70, 75, 80, 85],
        "New_Dev_%": [100, 30, 25, 20, 15],
    })
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Reused", x=timeline["Project"], y=timeline["Reuse_%"], marker_color="#2ecc71"))
    fig.add_trace(go.Bar(name="New Dev", x=timeline["Project"], y=timeline["New_Dev_%"], marker_color="#3498db"))
    fig.update_layout(barmode="stack", paper_bgcolor="rgba(10,25,47,0)", plot_bgcolor="rgba(17,34,64,0.5)", font=dict(color="#CCD6F6"), title="Architecture Reuse Across Agents", height=350)
    st.plotly_chart(fig, use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("**Retrieval Engine**")
        st.caption("Vector DB, GraphRAG, confidence scoring. Reused across all agents.")
    with c2:
        st.markdown("**Governance Framework**")
        st.caption("Security classification, human-in-loop, audit logging.")
    with c3:
        st.markdown("**Semantic Layer**")
        st.caption("Synonym resolution, canonical mapping. Custom per department.")
    with c4:
        st.markdown("**Domain Logic**")
        st.caption("Business rules, workflows, APIs. Fully custom.")

    st.subheader("Next Iterations")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**L&D Assistant (ILI)**")
        st.write("Cloned for Impact Leadership Institute: training design, course recommendations, learning paths.")
    with col2:
        st.markdown("**IT Assessment Agent**")
        st.write("Multi-file upload, objection handling from bids, proposal generation. Bid turnaround: weeks → hours.")

st.markdown("---")
st.caption("Skills: GraphRAG | Azure ML | Vector DB | RLHF | Governance | Python | Impact Networking")

if st.button("Back to Portfolio"):
    st.switch_page("app.py")
