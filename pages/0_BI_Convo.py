"""
BI Convo: Governance-First Conversational BI & GraphRAG
5-Layer Semantic Architecture for Small Business AI
CRAIG framework: Context, Role, Action, Impact, Growth
"""

import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dataclasses import dataclass
import time

from components.sidebar_nav import render_sidebar_nav

try:
    import graphviz
    HAS_GRAPHVIZ = True
except ImportError:
    HAS_GRAPHVIZ = False

st.set_page_config(
    page_title="BI Convo | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Custom CSS - CRAIG styling, dark theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
[data-testid="stVerticalBlock"] > div { font-family: 'Inter', -apple-system, sans-serif !important; color: #CCD6F6 !important; }
[data-testid="stMarkdown"] p, span, div { color: #CCD6F6 !important; }
[data-testid="stMarkdown"] h1, h2, h3 { color: #CCD6F6 !important; }
[data-testid="stTabs"] [role="tab"], [data-testid="stTabs"] button { color: #CCD6F6 !important; }
[data-testid="stTabs"] [aria-selected="true"] { color: #CCD6F6 !important; border-bottom-color: #8892B0 !important; }
.craig-header { font-size: 2.2rem; font-weight: bold; color: #CCD6F6; text-align: center; margin-bottom: 1rem; }
.risk-badge { background: rgba(220,53,69,0.2); color: #ff6b6b; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold; display: inline-block; margin: 1rem 0; }
.governance-card { background-color: #112240; border-left: 5px solid #8892B0; padding: 1rem; margin: 1rem 0; border-radius: 0 10px 10px 0; color: #CCD6F6; }
.metric-highlight { background-color: #112240; border: 2px solid #8892B0; padding: 1rem; border-radius: 10px; text-align: center; color: #CCD6F6; }
.rule-box { background-color: rgba(136,146,176,0.15); border: 1px solid #8892B0; padding: 1rem; margin: 0.5rem 0; border-radius: 5px; font-family: monospace; color: #CCD6F6; }
</style>
""", unsafe_allow_html=True)

# ==================== DATA STRUCTURES ====================

@dataclass
class SemanticEntity:
    canonical_name: str
    synonyms: list
    definition: str
    calculation_logic: str
    version: str
    owner: str
    last_updated: str

@dataclass
class GovernanceRule:
    rule_id: str
    rule_type: str
    condition: str
    action: str
    severity: str

def init_knowledge_graph():
    G = nx.DiGraph()
    nodes = [
        ("Customer", "entity", {"def": "Buying entity", "system": "Canonical"}),
        ("Client_QB", "synonym", {"maps_to": "Customer", "system": "QuickBooks"}),
        ("Buyer_Excel", "synonym", {"maps_to": "Customer", "system": "Excel"}),
        ("Prospect_CRM", "synonym", {"maps_to": "Customer", "system": "CRM"}),
        ("Order", "entity", {"def": "Transaction record"}),
        ("Invoice", "entity", {"def": "Billing document"}),
        ("Widget_A", "product", {"category": "Industrial", "sku": "IW-100"}),
        ("Widget_Generic", "synonym", {"maps_to": "Widget_A", "confusion_risk": "high"}),
        ("Net_Profit", "metric", {"formula": "Rev - COGS - Labor - Overhead", "version": "3.0"}),
        ("Gross_Profit", "metric", {"formula": "Rev - COGS", "version": "1.0"}),
        ("QB_Database", "source", {"type": "accrual"}),
        ("Excel_BOM", "source", {"type": "cash_basis"}),
        ("Mike", "user", {"role": "Owner"}),
        ("Susan", "user", {"role": "Bookkeeper"}),
    ]
    for node, ntype, attrs in nodes:
        G.add_node(node, node_type=ntype, **attrs)
    edges = [
        ("Client_QB", "Customer", "synonym_of"), ("Buyer_Excel", "Customer", "synonym_of"),
        ("Prospect_CRM", "Customer", "synonym_of"), ("Customer", "Order", "places"),
        ("Order", "Invoice", "generates"), ("Order", "Widget_A", "contains"),
        ("Widget_Generic", "Widget_A", "ambiguous_synonym"), ("Invoice", "Net_Profit", "contributes_to"),
        ("QB_Database", "Invoice", "stores"), ("Excel_BOM", "Widget_A", "tracks_cost"),
        ("Mike", "Net_Profit", "queries"), ("Susan", "Customer", "validates"),
    ]
    for src, dst, rel in edges:
        G.add_edge(src, dst, relationship=rel)
    return G

def init_semantic_layer():
    return {
        "Customer": SemanticEntity("Customer", ["Client", "Buyer", "Prospect", "Account"],
            "Entity with order or A/R", "SELECT DISTINCT customer_id FROM orders UNION ...",
            "v2.1", "Sales_Ops", "2024-01-15"),
        "Net_Profit": SemanticEntity("Net_Profit", ["Profit", "Bottom Line", "Earnings"],
            "Rev - COGS - Labor - Overhead", "(Revenue - COGS - Labor_Burden - Overhead)",
            "v3.0", "Finance", "2024-03-01"),
        "Active_Customer": SemanticEntity("Active_Customer", ["Active Client", "Current Customer"],
            "Customer with order in last 90 days", "MAX(order_date) >= CURRENT_DATE - INTERVAL 90 DAY",
            "v1.2", "Sales_Ops", "2024-02-01"),
        "Widget_A": SemanticEntity("Widget_A", ["Widget", "Industrial Widget", "Main Product"],
            "Industrial Widget Type 1, SKU IW-100", "SKU LIKE 'IW-100%'",
            "v1.0", "Product", "2024-01-01"),
    }

def init_governance_rules():
    return [
        GovernanceRule("R001", "calculation", "User asks for 'Profit'", "Resolve to Net_Profit v3.0 (not Gross)", "warn"),
        GovernanceRule("R002", "semantic", "Customer entity referenced", "Ask: Active (90d) or All (ever)?", "warn"),
        GovernanceRule("R003", "privacy", "Individual names in aggregate", "Block: Privacy policy prevents", "block"),
        GovernanceRule("R004", "performance", "Query joins >3 sources", "Route to Audit Mode (5-8s)", "log"),
        GovernanceRule("R005", "calculation", "Fiscal quarter referenced", "Use fiscal calendar (Nov-Oct)", "warn"),
        GovernanceRule("R006", "validation", "High-stakes decision", "Trigger Four-Eyes Protocol", "block"),
    ]

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("---")
    st.markdown("**Architecture Layers**")
    st.caption("1. Semantic | 2. Governance | 3. Retrieval | 4. Executive | 5. Change Mgmt")
    st.markdown("---")
    st.markdown("**Key Metrics**")
    st.metric("Retrieval Accuracy", "94%", "+57%")
    st.metric("Decision Variance", "-90%", "↓")
    st.metric("Time to Insight", "30s", "-99%")
    st.markdown("---")
    st.markdown("**Sample Prompts**")
    role_prompt = st.selectbox("Persona", ["Mike (Owner)", "Susan (Bookkeeper)", "Board", "Implementation"], label_visibility="collapsed")
    if "Mike" in role_prompt:
        for p in ["Can I afford to hire 2 shop hands in March?", "Why did profit margin on widgets drop?", "What's my Q2 cash buffer?"]:
            st.code(p, language=None)
    elif "Susan" in role_prompt:
        for p in ["Validate: Lineage for $45K profit", "Flag transactions violating No test data", "Compare Active vs All Customers"]:
            st.code(p, language=None)
    elif "Board" in role_prompt:
        for p in ["Causal impact: AI vs Excel decisions", "Current override rate?", "Generate SBA audit package"]:
            st.code(p, language=None)
    else:
        for p in ["Semantic Contract Template for retail", "Reuse rules for fabrication shop", "Identify lineage gaps"]:
            st.code(p, language=None)
    st.markdown("---")
    st.caption("Target: Burtch Works | Decision Intelligence Architect")

# ==================== HEADER ====================
st.markdown('<div class="craig-header">BI Conversational Agent Architecture</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8892B0;'>A Governance-First Semantic Layer for Small Business Intelligence</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="risk-badge">HIGH RISK: Conversational AI Affects Real Business Decisions</div>', unsafe_allow_html=True)
st.markdown("---")

# ==================== CRAIG TABS ====================
context_tab, role_tab, action_tab, impact_tab, growth_tab = st.tabs([
    "CONTEXT: Mike's Chaos",
    "ROLE: The Architect",
    "ACTION: 5-Layer Architecture",
    "IMPACT: Metrics & Validation",
    "GROWTH: Scaling Strategy",
])

# ==================== CONTEXT TAB ====================
with context_tab:
    st.header("Mike's Manufacturing Chaos")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("The Scenario")
        st.write("Meet Mike. He runs a **$5M custom manufacturing shop** in Milwaukee. Drowning in data, starving for insights:")
        silos = {"QuickBooks": ("Clients", "Invoices"), "Excel": ("Buyers", "Stock"), "CRM": ("Prospects", "Leads"), "Sheets": ("Accounts", "Commissions")}
        for sys, (term, data) in silos.items():
            st.markdown(f"- **{sys}**: `{term}` → {data}")
        st.divider()
        st.subheader("The Disaster")
        st.error("**Mike asks:** \"What was my profit margin on industrial widgets last quarter?\"\n\n**AI Failure:** Semantic conflates Widget A (CRM) vs Industrial Widget (QB). Uses wrong COGS. Answers confidently: **$45K profit** (actual: **$12K loss**). Hiring decision → cash flow crisis.")
    with col2:
        st.subheader("Before vs After")
        st.markdown("<div class='rule-box'>BEFORE: Keyword RAG<br>60% accuracy • No business context • Calculation rules hidden</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-highlight'>AFTER: GraphRAG + Governance<br>94% accuracy • Canonical resolution • Full lineage</div>", unsafe_allow_html=True)
        st.metric("Decision Variance", "$2K → $200", "-90%")
        st.metric("Time to Insight", "4 hrs → 30 sec", "-99%")

# ==================== ROLE TAB ====================
with role_tab:
    st.header("Role: The Semantic Governance Architect")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Decision Intelligence Architect")
        st.write("I architect a **reusable, governable semantic core** that makes AI conversationally competent for small business BI.")
        st.markdown("""
        <div class="governance-card">
        <strong>Why High Risk (MRM)</strong>
        <ul><li>Decision Risk: Wrong profit definition → Real hiring decisions</li>
        <li>Compliance Risk: No lineage → SBA loan failure</li>
        <li>Semantic Drift: Customer definition changes</li></ul>
        </div>
        """, unsafe_allow_html=True)
        philosophy = st.selectbox("Governance Principle", [
            "Semantic Layer as Control Plane", "Calculation as Code",
            "Trust but Verify", "Causal Inference Over Correlation"
        ])
        if "Semantic" in philosophy:
            st.success("Business Dictionary is the API. Client (QB) ≡ Buyer (Excel) ≡ Prospect (CRM) → Customer. GitOps-managed.")
        elif "Calculation" in philosophy:
            st.success("Metrics as contracts: Net_Profit v3.0 = Rev - COGS - Labor - Overhead. Versioned, auditable.")
        elif "Trust" in philosophy:
            st.success("Four-Eyes: AI presents lineage → Susan validates → Mike approves. Target 15-20% override rate.")
        else:
            st.success("Causality: 'If you fire Client X, n=12 similar manufacturers saw +34% profit (90% CI: -12% to +56%).'")
    with col2:
        st.subheader("Principles")
        for p, d in [("Reusable", "Constant frameworks, variable terms"), ("Governable", "Every answer has lineage"), ("Scalable", "Template library"), ("Causal", "Prove impact"), ("Human-Centric", "Susan = AI Supervisor")]:
            with st.expander(p):
                st.caption(d)

# ==================== ACTION TAB ====================
with action_tab:
    st.header("Action: The 5-Layer Governance Architecture")
    layer = st.select_slider("Layer", options=[
        "Layer 1: Semantic", "Layer 2: Governance", "Layer 3: Retrieval",
        "Layer 4: Executive", "Layer 5: Change Mgmt"
    ], value="Layer 3: Retrieval")

    if layer == "Layer 1: Semantic":
        st.subheader("Layer 1: Semantic (Business Dictionary)")
        col1, col2 = st.columns([3, 2])
        with col1:
            user_input = st.text_input("Mike asks:", "Show me my top clients from last quarter")
            st.markdown("""
            <div class="rule-box">
            RESOLUTION: "clients" → Customer (95%)<br>
            "last quarter" → Fiscal vs Calendar (disambiguate)<br>
            "top" → Net_Profit v3.0 (default)
            </div>
            """, unsafe_allow_html=True)
        with col2:
            for name, ent in init_semantic_layer().items():
                with st.expander(f"{name} (v{ent.version})"):
                    st.caption(f"Synonyms: {', '.join(ent.synonyms)}")
                    st.caption(f"Owner: {ent.owner}")
        st.markdown("**Metric as Code**")
        st.code("Net_Profit:\n  formula: Revenue - COGS - Labor - Overhead\n  version: 3.0\n  owner: Finance", language="yaml")

    elif layer == "Layer 2: Governance":
        st.subheader("Layer 2: Governance (Calculation Police)")
        rules = init_governance_rules()
        for r in rules:
            sev = {"block": "BLOCK", "warn": "WARN", "log": "LOG"}[r.severity]
            st.markdown(f"**{r.rule_id}** [{sev}] When: {r.condition} → {r.action}")
        st.markdown("**Rule 4: Calculation Lineage**")
        if HAS_GRAPHVIZ:
            try:
                g = graphviz.Digraph()
                g.attr(rankdir='LR')
                g.node('A', 'QB Invoices')
                g.node('B', 'Transform\n-Discounts')
                g.node('C', 'Excel BOM')
                g.node('D', 'Formula')
                g.node('E', 'Net Profit $12,340')
                g.edges(['AB', 'CB', 'BD', 'DE'])
                st.graphviz_chart(g)
            except Exception:
                st.code("QB Invoices → Transform (-Discounts) → Formula (Rev-COGS-Labor) → Net Profit $12,340")
        else:
            st.code("QB Invoices → Transform (-Discounts) → Formula (Rev-COGS-Labor) → Net Profit $12,340")
        constraints = st.multiselect("Active Constraints", [
            "Exclude @test.com", "Fiscal Calendar (Nov-Oct)", "Redact names", "90-day active"
        ], default=["Exclude @test.com", "Fiscal Calendar (Nov-Oct)"])

    elif layer == "Layer 3: Retrieval":
        st.subheader("Layer 3: Retrieval (GraphRAG)")
        G = init_knowledge_graph()
        pos = nx.spring_layout(G, k=2, iterations=40, seed=42)
        edge_x, edge_y = [], []
        for u, v in G.edges():
            x0, y0 = pos[u]
            x1, y1 = pos[v]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        node_x = [pos[n][0] for n in G.nodes()]
        node_y = [pos[n][1] for n in G.nodes()]
        color_map = {"entity": "#64FFDA", "synonym": "#ff7f0e", "metric": "#2ca02c", "source": "#d62728", "user": "#9467bd", "product": "#8c564b"}
        node_color = [color_map.get(G.nodes[n].get("node_type", "entity"), "#8892B0") for n in G.nodes()]
        fig = go.Figure(data=[
            go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color="#444"), hoverinfo="none", mode="lines"),
            go.Scatter(x=node_x, y=node_y, mode="markers+text", text=list(G.nodes()), textposition="top center",
                marker=dict(size=20, color=node_color, line=dict(width=1, color="#8892B0"))),
        ])
        fig.update_layout(paper_bgcolor="rgba(10,25,47,0)", plot_bgcolor="rgba(17,34,64,0.5)", font=dict(color="#CCD6F6"),
            title="Mike's Manufacturing Knowledge Graph", height=450, showlegend=False, margin=dict(l=20, r=20, t=40, b=20),
            xaxis=dict(visible=False), yaxis=dict(visible=False))
        st.plotly_chart(fig, use_container_width=True)
        query = st.text_input("Test Query", "What was profit on Widget A last quarter?")
        if query:
            with st.spinner("Traversing..."):
                time.sleep(0.8)
                st.success("Path: Widget A (exact) → Net_Profit (95%) → Q4 FY2024 (fiscal) → $12,340")

    elif layer == "Layer 4: Executive":
        st.subheader("Layer 4: Executive (Trade-offs)")
        mode = st.select_slider("Mode", ["Speed (1-2s, 95%)", "Balanced (2-4s, 97%)", "Audit (5-8s, 99%)"], value="Balanced (2-4s, 97%)")
        st.markdown("**Rule 11: Causal vs Correlation**")
        col1, col2 = st.columns(2)
        with col1:
            st.error("Correlation: 'Client X has 8% margin. Terminate.'")
        with col2:
            st.success("Causal: 'Fire X → lose $5K/mo, gain 15hrs. n=12 similar: +34% profit (90% CI: -12% to +56%). Proceed only with pipeline.'")
        exec_df = pd.DataFrame({
            "Metric": ["Decision Velocity", "Override Rate", "Lineage Audit"],
            "Baseline": ["3 days", "0%", "0%"],
            "Target": ["8 min", "15-20%", "100%"],
            "Current": ["6 min", "18%", "100%"],
        })
        st.dataframe(exec_df, use_container_width=True, hide_index=True)

    else:  # Change Mgmt
        st.subheader("Layer 5: Change Management (Susan's Journey)")
        phase = st.selectbox("Adoption Phase", ["Week 1-2: Shadow", "Week 3-4: Co-Create", "Month 2: Validate", "Month 3+: Supervise"])
        if "Shadow" in phase:
            st.write("AI answers, Susan validates 100%. Tacit rules captured.")
            st.metric("Validation Rate", "100%", "Investment")
        elif "Co-Create" in phase:
            st.write("Susan updates glossary. GitOps: v1.3 → v1.4.")
            st.metric("Validation Rate", "50%", "Rules contributed: 12")
        elif "Month 2" in phase:
            st.write("AI handles routine, Susan validates exceptions (5/wk).")
            st.metric("Validation Rate", "20%", "15 hrs/week saved")
        else:
            st.write("Susan = AI Supervisor. Edge cases, training. **+$5K salary bump**.")
            st.metric("Validation Rate", "10%", "Strategic value")
        st.info("Blameless Post-Mortem: Bad data? Bad rules? Bad question? → Schema update, Lunch & Learn, propagate.")

# ==================== IMPACT TAB ====================
with impact_tab:
    st.header("Impact: From Chaos to Conversation")
    c1, c2, c3, c4 = st.columns(4)
    for col, (val, label, sub) in [(c1, ("60%→94%", "Retrieval Accuracy", "GraphRAG")), (c2, ("$2K→$200", "Decision Variance", "Monthly error")), (c3, ("4h→30s", "Time to Insight", "Excel→Convo")), (c4, ("15%→2%", "Hallucination", "Flagged"))]:
        with col:
            st.markdown(f"<div class='metric-highlight'><h3>{val}</h3><p>{label}</p><small>{sub}</small></div>", unsafe_allow_html=True)
    st.divider()
    metrics_df = pd.DataFrame({
        "Category": ["Data Integration", "Calculation", "Audit", "Adoption", "Confidence"],
        "Before": ["5 silos", "60%", "0%", "20%", "Low"],
        "After": ["Unified semantic", "94%", "100%", "85%", "High"],
        "Outcome": ["Single source", "Prevented $45K error", "SBA approved", "Susan promoted", "Validated"],
    })
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)
    st.success("**Q1 Causal Proof:** 15 decisions prevented $127K loss (over-hiring x3, under-priced SKUs x5). Variance: $2K→$200/mo.")
    adoption_data = pd.DataFrame({
        "Month": ["M1", "M2", "M3", "M4", "M5", "M6"],
        "AI_Adoption": [25, 45, 65, 78, 85, 88],
        "Validation_Rate": [100, 60, 35, 20, 15, 10],
        "Accuracy": [70, 82, 88, 91, 93, 94],
    })
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=adoption_data["Month"], y=adoption_data["AI_Adoption"], name="AI %", line=dict(color="#64FFDA")), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Scatter(x=adoption_data["Month"], y=adoption_data["Validation_Rate"], name="Validate %", line=dict(color="#ff7f0e")), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Scatter(x=adoption_data["Month"], y=adoption_data["Accuracy"], name="Accuracy", line=dict(color="#8892B0", dash="dot")), row=1, col=1, secondary_y=True)
    fig.update_layout(paper_bgcolor="rgba(10,25,47,0)", plot_bgcolor="rgba(17,34,64,0.5)", font=dict(color="#CCD6F6"), title="Adoption Curve", height=350)
    fig.update_yaxes(title_text="%", secondary_y=False)
    fig.update_yaxes(title_text="Accuracy", secondary_y=True)
    st.plotly_chart(fig, use_container_width=True)

# ==================== GROWTH TAB ====================
with growth_tab:
    st.header("Growth: Scaling Architecture")
    scale_df = pd.DataFrame({
        "Layer": ["Semantic", "Governance", "Retrieval", "Conversation"],
        "Constant": ["Resolution framework, versioning, GitOps", "Audit trails, workflows, lineage", "Traversal, confidence scoring", "Clarification protocols, confidence UI"],
        "Variable": ["Glossary terms, KPI defs", "Constraints, fiscal calendars", "Graph schema, connectors", "Prompts, compliance"],
        "Mechanism": ["Contract templates", "Policy library", "Schema inheritance", "Prompt library"],
    })
    st.dataframe(scale_df, use_container_width=True, hide_index=True)
    st.subheader("Product Roadmap")
    p1, p2, p3 = st.tabs(["Phase 1: Templates", "Phase 2: Federated", "Phase 3: API"])
    with p1:
        st.write("Vertical templates: Manufacturing (BOM, COGS), Retail (turns, omnichannel), Professional Svcs (utilization). Onboarding: Semantic Contract Template.")
    with p2:
        st.write("Anonymized patterns across SMBs. Privacy-preserving. Auto-suggest rules from peer data.")
    with p3:
        st.write("White-label API for consultants. Embedded in accounting software. Marketplace for semantic packages.")
    st.subheader("Sample Prompts by Persona")
    prompt_cat = st.selectbox("Persona", ["Mike (Owner)", "Susan (Bookkeeper)", "Board", "Implementation"])
    if "Mike" in prompt_cat:
        st.write("- Can I afford to hire 2 shop hands in March?\n- Why did profit margin on widgets drop?\n- Simulate: Drop Client X, reinvest in custom work?")
    elif "Susan" in prompt_cat:
        st.write("- Validate lineage for $45K profit\n- Flag transactions violating No test data\n- Audit prep: SBA loan package")
    elif "Board" in prompt_cat:
        st.write("- Causal impact: AI vs Excel\n- Override rate?\n- ROI proof: $127K retained")
    else:
        st.write("- Semantic Contract for retail\n- Reuse rules for fabrication\n- Migration plan for Four-Eyes")
    st.divider()
    st.markdown("""
    <div style="background-color: #112240; color: #CCD6F6; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <strong>Decision Intelligence = Governance Framework for Safe AI</strong><br>
        Constant: Semantic architecture | Variable: Your business logic
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Skills: GraphRAG | Semantic Layer | Governance-First AI | Causal Inference | Change Management | MRM")

if st.button("Back to Portfolio"):
    st.switch_page("app.py")
