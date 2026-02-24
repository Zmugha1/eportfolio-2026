"""
BI Convo: Governance-First Conversational BI & GraphRAG
5-Layer Semantic Architecture for Small Business AI
Hero project for Burtch Works Conversational BI & GraphRAG role
"""

import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go

from components.sidebar_nav import render_sidebar_nav
from components.craig_section import _key_terms_box

st.set_page_config(
    page_title="BI Convo | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Custom CSS - navy/gold accents, dark theme
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    [data-testid="stVerticalBlock"] > div { font-family: 'Inter', -apple-system, sans-serif !important; color: #CCD6F6 !important; }
    [data-testid="stMarkdown"] p, [data-testid="stMarkdown"] span, [data-testid="stMarkdown"] div { color: #CCD6F6 !important; }
    [data-testid="stMarkdown"] h1, [data-testid="stMarkdown"] h2, [data-testid="stMarkdown"] h3 { color: #CCD6F6 !important; }
    [data-testid="stTabs"] [role="tab"], [data-testid="stTabs"] button { color: #CCD6F6 !important; }
    [data-testid="stTabs"] [aria-selected="true"] { color: #CCD6F6 !important; border-bottom-color: #8892B0 !important; }
    .bi-card { background-color: #112240; padding: 20px; border-radius: 12px; border-left: 4px solid #8892B0; margin: 12px 0; }
    .mrm-badge { display: inline-block; background: rgba(220, 53, 69, 0.2); color: #ff6b6b; padding: 6px 12px; border-radius: 20px; font-size: 0.75em; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============ SAMPLE PROMPTS SIDEBAR ============
with st.sidebar:
    st.markdown("---")
    st.markdown("**Sample Prompts for Adoption**")
    st.caption("Copy-paste into BI Convo")
    role_prompt = st.selectbox(
        "Role",
        ["Mike (Owner)", "Susan (Bookkeeper)", "Board (Executive)"],
        label_visibility="collapsed",
    )
    if role_prompt == "Mike (Owner)":
        prompts = [
            "Can I afford to hire 2 new shop hands in March?",
            "Why did my profit margin on industrial widgets drop last month?",
            "What's my cash buffer for Q2?",
        ]
    elif role_prompt == "Susan (Bookkeeper)":
        prompts = [
            "Validate: Show me the lineage for the $45K profit calculation",
            "Flag any transactions in the last 30 days that violate the 'No test data' rule",
            "Compare: Active Customers (90 days) vs All Customers (ever)",
        ]
    else:
        prompts = [
            "Show me the causal impact: AI-assisted decisions vs baseline Excel decisions",
            "What's our current override rate? Are we trusting the AI too much or too little?",
            "Generate SBA loan audit package: Full lineage for all Q4 profit calculations",
        ]
    for p in prompts:
        st.code(p, language=None)
    st.markdown("---")

# ============ HERO HEADER ============
st.title("BI Convo: From Tower of Babel to Single Source of Truth")
st.markdown("*5-Layer Governance-First Semantic Architecture for Small Business AI*")
st.markdown('<span class="mrm-badge">High Risk - Conversational AI affects real-world decisions</span>', unsafe_allow_html=True)
st.markdown("---")

# ============ SECTION 1: CONTEXT ============
st.header("Mike's Manufacturing Chaos")
col_before, col_after = st.columns(2)
with col_before:
    st.markdown("**BEFORE: Data Chaos**")
    st.markdown(
        """
        - QuickBooks (Clients) | Excel (Buyers) | CRM (Prospects) | Sheets (Accounts)
        - "Widget A" means different things across systems
        - AI calculates profit using wrong COGS → **$45K phantom profit** vs **$12K actual loss**
        - Bad hire decision → cash flow crisis
        """
    )
with col_after:
    st.markdown("**AFTER: Governed AI**")
    st.markdown(
        """
        - Canonical entities: Client (QB) ≡ Buyer (Excel) ≡ Prospect (CRM) → **Customer**
        - Metric definitions as code: Net_Profit v3.0 (Revenue - COGS - Labor - Overhead)
        - Full lineage: every calculation traceable to source
        - Four-eyes protocol for high-stakes decisions
        """
    )

st.markdown(
    """
    **The Disaster:** Mike's $5M custom manufacturing shop in Milwaukee. Data silos caused AI to confuse "Widget A" across systems, 
    miscalculate profit (phantom $45K vs actual $12K loss), leading to a bad hiring decision and cash flow crisis.
    """
)
_key_terms_box("""<b>Semantic Layer:</b> Business glossary that resolves synonyms (Client = Buyer = Prospect → Customer) and defines metrics as code.<br><br>
<b>GraphRAG:</b> Retrieval that traverses a knowledge graph (entities + relationships) instead of keyword search.<br><br>
<b>Calculation Lineage:</b> Audit trail showing exactly which sources and formulas produced each number.""")

st.markdown("---")

# ============ SECTION 2: ROLE ============
st.header("The Semantic Governance Architect")
st.markdown("**Building a Decision Intelligence Layer, Not Just Another Chatbot**")
st.write(
    """
    I architected a reusable, governable semantic core that makes AI conversationally competent for small business BI.
    **MRM Tier:** High Risk—Conversational AI affects real-world decisions (hiring, firing, pricing).
    **Value Proposition:** 5-layer architecture (Semantic → Governance → Retrieval → Executive → Human) with explicit constant-vs-variable rules for multi-tenancy scaling.
    """
)
st.markdown("---")

# ============ SECTION 3: ACTION - 5-LAYER ARCHITECTURE TABS ============
st.header("The 5-Layer Architecture")
arch_tabs = st.tabs([
    "Layer 1: Semantic", "Layer 2: Governance", "Layer 3: Retrieval (GraphRAG)",
    "Layer 4: Executive", "Layer 5: Change Management"
])

with arch_tabs[0]:
    st.subheader("Semantic Layer (Business Dictionary)")
    st.markdown("**Rule 1: Canonical Entity Resolution**")
    st.code("Client (QB) ≡ Buyer (Excel) ≡ Prospect (CRM) → Customer (Canonical)\nVersion: v1.2 → v1.3 (90-day to 120-day active threshold)", language=None)
    st.markdown("**Rule 2: Metric Definitions as Code**")
    st.code("""Net_Profit:
  formula: Revenue - COGS - Labor - Overhead
  revenue_definition: SUM(Invoices.Total) WHERE Status='Paid'
  version: 3.0
  owner: Finance""", language="yaml")
    st.markdown("**Rule 3: Contextual Disambiguation**")
    quarter_choice = st.selectbox('"Last Quarter" means:', ["Fiscal (Nov–Oct)", "Calendar (Jan–Dec)"])
    st.caption(f"Selected: {quarter_choice}")

with arch_tabs[1]:
    st.subheader("Governance Layer (Calculation Police)")
    st.markdown("**Rule 4: Calculation Lineage Enforcement**")
    st.code("Profit = $12K [Source: QB #1001-1050, Transformed: -Discounts, Formula: Sum - COGS from Excel/BOM_v2.1]", language=None)
    st.markdown("**Rule 5: Four-Eyes Protocol**")
    st.info("High-stakes questions (e.g., 'Can I afford to hire?') trigger human-in-the-loop approval workflow.")
    st.markdown("**Rule 6: Constraint Injection**")
    st.code("Exclude: Email contains @test.com\nFiscal: Q4 2024 = Nov 1 2024 - Jan 31 2025", language=None)

with arch_tabs[2]:
    st.subheader("Retrieval Layer (GraphRAG)")
    G = nx.DiGraph()
    G.add_edge("Customer", "Order", label="PLACES_ORDER")
    G.add_edge("Order", "Invoice", label="GENERATES")
    G.add_edge("Invoice", "Product", label="CONTAINS")
    G.add_edge("Product", "Widget_A", label="ISA")
    pos = nx.spring_layout(G, seed=42)
    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]
    fig = go.Figure()
    for u, v, d in G.edges(data=True):
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        label = d.get("label", "")
        fig.add_trace(go.Scatter(
            x=[x0, (x0 + x1) / 2, x1], y=[y0, (y0 + y1) / 2, y1],
            mode="lines+text", text=["", label, ""], textposition="top center",
            line=dict(color="#8892B0", width=2),
        ))
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y, mode="markers+text",
        text=list(G.nodes()), textposition="top center",
        marker=dict(size=24, color="#64FFDA", line=dict(width=2, color="#8892B0")),
    ))
    fig.update_layout(
        title="Knowledge Graph: Customer → Order → Invoice → Product → Widget_A",
        paper_bgcolor="rgba(10,25,47,0)", plot_bgcolor="rgba(10,25,47,0)",
        font=dict(color="#CCD6F6"), showlegend=False, height=350,
        margin=dict(l=20, r=20, t=40, b=20), xaxis=dict(visible=False), yaxis=dict(visible=False),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Query 'Profit on widgets' traverses Semantic → Logical → Physical layers")
    st.markdown("**Confidence Tiers:** Exact (100%) → Synonym (85%) → Vector (60% + warning)")

with arch_tabs[3]:
    st.subheader("Executive Adoption (Causal Layer)")
    st.markdown("**Rule 11: Decision Quality A/B Testing**")
    st.dataframe(pd.DataFrame({
        "Method": ["Control (Excel)", "Treatment (AI + Human)"],
        "Error Rate": ["15%", "3%"],
    }), use_container_width=True, hide_index=True)
    st.markdown("**Rule 12: Trade-off Transparency Protocol**")
    mode = st.radio("Mode", ["Speed Mode (1–2s, 95% accuracy)", "Audit Mode (5–8s, 99% accuracy)"], horizontal=True)
    st.caption("$10K decision → Speed | $100K hire → Audit")

with arch_tabs[4]:
    st.subheader("Change Management (Human Layer)")
    st.markdown("**Susan's Story: From Excel Hunter to AI Supervisor**")
    st.write("""
    - **Weeks 1–4:** Shadow mode—AI answers, Susan validates 100%. Tacit rules → Data Contracts.
    - **Month 2–3:** Validation drops to 20%. Susan manages exceptions.
    - **Outcome:** Handles 50 weekly lookups, validates 5, **+$5K salary bump**. Passes "Bus Test."
    """)
    st.info("Susan's '10% waste rule' became Data Contract v1.4.")

st.markdown("---")

# ============ INTERACTIVE: SEMANTIC RESOLUTION DEMO ============
st.header("Semantic Resolution Demo")
user_query = st.text_input("Ask Mike's question:", "What was my profit on widgets last quarter?", key="bi_query")
st.markdown("**Real-time resolution:**")
resolutions = [
    "profit → Net_Profit (v3.0)",
    "widgets → Widget_A (Industrial, SKU IW-100)",
    "last quarter → Q4 FY2024 (Nov 2024 - Jan 2025)",
]
for r in resolutions:
    st.code(r, language=None)
st.markdown("---")

# ============ GOVERNANCE RULE ENGINE ============
st.header("Governance Rule Engine")
rules = {
    "R001": "Resolve Profit to Net (not Gross)",
    "R002": "Disambiguate Active vs All Customers",
    "R003": "Block individual names in aggregates",
    "R004": "Route multi-source joins to Audit Mode",
    "R005": "Enforce fiscal calendar (Nov–Oct)",
}
rules_fired = ["R001", "R002", "R005"]
for rid, desc in rules.items():
    badge = " [FIRED]" if rid in rules_fired else ""
    st.markdown(f"- **{rid}**{badge}: {desc}")
st.caption("Rules that fired for current query: R001, R002, R005")

# ============ TRADE-OFF TRANSPARENCY SLIDER ============
st.subheader("Trade-off Transparency: Speed vs Audit Mode")
speed_val = st.slider("Speed (left) vs Audit (right)", 0, 100, 25, key="speed_slider")
st.caption("Speed Mode: 1–2s, 95% accuracy | Audit Mode: 5–8s, 99% accuracy, full lineage")

# ============ CONFIDENCE CALCULATOR ============
st.subheader("Confidence Scoring")
match_type = st.radio("Match type for query", ["Exact match", "Synonym match", "Vector fallback"], horizontal=True)
conf = 100 if "Exact" in match_type else (85 if "Synonym" in match_type else 60)
st.metric("Confidence", f"{conf}%", "Warning: verify sources" if conf < 100 else "High confidence")
st.markdown("---")

# ============ SECTION 4: IMPACT ============
st.header("Impact: Metrics & Validation")
impact_df = pd.DataFrame({
    "Metric": ["Retrieval Accuracy", "Decision Variance", "Time to Insight", "Hallucination Rate", "Audit Readiness"],
    "Before (Chaos)": ["60% (keyword)", "$2K/month error", "4 hours (Excel)", "15%", "0% lineage"],
    "After (Governed)": ["94% (GraphRAG)", "$200/month error", "30 seconds", "2% (flagged)", "100% traceable"],
    "Improvement": ["+57%", "-90%", "99.8% faster", "-87%", "Full SBA compliance"],
})
st.dataframe(impact_df, use_container_width=True, hide_index=True)
st.markdown(
    """**Causal Proof Point:** $127K retained profit in Q1 through 15 specific decisions 
    (prevented over-hiring x3, identified under-priced SKUs x5)."""
)
st.markdown("---")

# ============ SECTION 5: GROWTH ============
st.header("Scaling Architecture")
scale_df = pd.DataFrame({
    "Layer": ["Semantic", "Governance", "Retrieval", "Conversation"],
    "Constant (Reusable)": [
        "Resolution framework, versioning, synonym handling",
        "Audit trails, approval workflows, constraint syntax",
        "Graph traversal patterns, confidence scoring",
        "Clarification protocols, confidence display",
    ],
    "Variable (Client-Specific)": [
        "Business glossary terms, KPI definitions",
        "Specific constraints (fiscal calendars, exclusion rules)",
        "Graph schema (BOM vs Inventory vs Project hierarchy)",
        "Industry-specific prompts, compliance requirements",
    ],
})
st.dataframe(scale_df, use_container_width=True, hide_index=True)
st.markdown("**Phase Roadmap:** Phase 1: Template Library (Manufacturing, Retail, Professional Services) | Phase 2: Federated Learning | Phase 3: Decision Intelligence API")
st.markdown("---")

# ============ EXECUTIVE DEEP DIVE ============
with st.expander("Executive Deep Dive: Trade-offs & Causal Inference"):
    st.subheader("The Three Tensions")
    st.write("""
    1. **Speed vs. Precision:** Speed Mode (1–2s, 95%) vs Audit Mode (5–8s, 99%). Context-aware toggling.
    2. **Automation vs. Oversight:** Target 15–20% override rate. <10% = blind trust | >30% = AI not learning.
    3. **Standardization vs. Customization:** Bank reporting uses standard Net Profit; Mike uses custom "Shop Floor Profit" (excl. overhead).
    """)
    st.subheader("Counterfactual Engine")
    st.write("""
    **Query:** 'Should I fire Client X?'
    - Intervention: Fire Client X → lose $5K/month revenue, gain 15 hours shop time
    - Mechanism: Similar manufacturers (n=12) who reinvested saw 34% profit increase
    - Uncertainty: 2 of 12 saw revenue drops due to unfilled capacity
    - 90% CI: [-12%, +34%] profit change
    """)
    st.markdown("**Decision Quality:** Pre-Dr. Data: $2K/month variance | Post-Dr. Data: $200/month | Causal Attribution: $127K retained profit")

st.markdown("---")
st.caption("Skills: GraphRAG | Semantic Layer | Governance-First AI | Causal Inference | Change Management | MRM")

if st.button("Back to Portfolio"):
    st.switch_page("app.py")
