"""
Elevate Multi-Agent Assessment System
Enterprise Bid Intelligence & IT Assessment Automation
CRAIG framework: Context, Role, Action, Impact, Growth
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from components.sidebar_nav import render_sidebar_nav

try:
    import graphviz
    HAS_GRAPHVIZ = True
except ImportError:
    HAS_GRAPHVIZ = False

st.set_page_config(
    page_title="Elevate Assessment System | Dr. Data",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Custom CSS - dark theme aligned with eportfolio
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
[data-testid="stVerticalBlock"] > div { font-family: 'Inter', -apple-system, sans-serif !important; color: #CCD6F6 !important; }
[data-testid="stMarkdown"] p, span, div { color: #CCD6F6 !important; }
[data-testid="stMarkdown"] h1, h2, h3 { color: #CCD6F6 !important; }
[data-testid="stTabs"] [role="tab"], [data-testid="stTabs"] button { color: #CCD6F6 !important; }
[data-testid="stTabs"] [aria-selected="true"] { color: #CCD6F6 !important; border-bottom-color: #8892B0 !important; }
.enterprise-header { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem; }
.agent-box { background-color: #112240; border: 2px solid #8892B0; border-radius: 10px; padding: 1rem; margin: 0.5rem 0; border-left: 5px solid #2a5298; color: #CCD6F6; }
.governance-alert { background-color: rgba(255, 193, 7, 0.15); border: 1px solid #ffc107; padding: 1rem; border-radius: 5px; margin: 1rem 0; color: #CCD6F6; }
.roi-metric { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; padding: 1.5rem; border-radius: 10px; text-align: center; margin: 0.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown("""
<div class="enterprise-header">
    <h1 style="margin:0;">Elevate Multi-Agent Assessment System</h1>
    <h3 style="margin:0; font-weight: normal;">Enterprise Bid Intelligence & IT Assessment Automation</h3>
    <p style="margin-top: 1rem; opacity: 0.9;">
        A governance-first, 9-agent orchestration platform for scalable enterprise decision intelligence.<br>
        <em>Not a chatbot. A deterministic + agentic hybrid with 7-layer governance architecture.</em>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: rgba(46, 204, 113, 0.2); border-left: 5px solid #28a745; padding: 1rem; margin: 1rem 0; border-radius: 0 10px 10px 0; color: #CCD6F6;">
    <strong>Architecture Scaling:</strong> This system clones the L&D Multi-Agent architecture with 75% reuse,
    proving domain-agnostic platform capability. Same 9-agent backbone, different domain ontology (IT Services vs. Training).
</div>
""", unsafe_allow_html=True)

# ==================== CRAIG TABS ====================
context_tab, role_tab, action_tab, impact_tab, growth_tab = st.tabs([
    "CONTEXT: Bid Chaos",
    "ROLE: Systems Architect",
    "ACTION: 9-Agent Engine",
    "IMPACT: 3 Weeks to 3 Days",
    "GROWTH: Platform Play"
])

# ==================== CONTEXT TAB ====================
with context_tab:
    st.header("The Bid Response Crisis: Losing Deals to Speed")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.write("""
        **The Problem at Managed Services Inc (IT Division):**

        Competitive bids for enterprise IT contracts required rapid turnaround of complex technical assessments:
        - **Current State Analysis**: Document client's existing infrastructure (servers, cloud, security posture)
        - **Gap Assessment**: Identify vulnerabilities and optimization opportunities
        - **Solution Design**: Propose specific services (migration, security, managed support)
        - **Pricing Strategy**: Competitive yet profitable pricing
        - **Risk Mitigation**: Address potential objections proactively

        **The Traditional Process (3 Weeks):**
        1. **Week 1**: Solutions Architect visits client, takes notes, returns to office
        2. **Week 1-2**: Manual document review (Teams call transcripts, email threads, CSV exports)
        3. **Week 2**: Due diligence on similar past bids (searching file shares for "similar deal")
        4. **Week 2-3**: Write proposal, legal review, pricing approval
        5. **Week 3**: Submit bid (often missing deadline or rushed)

        **The Cost:**
        - 15-20 hours per Solutions Architect per bid
        - 40% bid loss rate due to slow turnaround
        - $2M+ in lost annual revenue from missed deadlines
        """)
        st.error("""
        **The Breaking Point:** A $500K manufacturing client RFP required response in 72 hours.
        Traditional process would take 3 weeks. Competitor won because they responded in 5 days.
        We needed **Elevate** to compress 3 weeks into 3 days without sacrificing quality.
        """)
    with col2:
        st.subheader("Pre-Elevate Metrics")
        st.metric("Avg. Bid Turnaround", "21 days", "")
        st.metric("Win Rate", "58%", "")
        st.metric("Architect Hours/Bid", "18 hours", "")
        st.metric("Due Diligence Success", "60%", "")
        st.metric("Annual Lost Revenue", "$2.1M", "")
        st.markdown("""
        <div style="background-color: rgba(255,107,107,0.15); padding: 1rem; border-radius: 5px; margin-top: 1rem; color: #CCD6F6;">
            <strong>Sales Engineer Quote:</strong><br>
            <em>"I spend more time searching old SharePoint files for similar bids than actually
            strategizing. And half the time I miss critical objections that killed us last time."</em>
        </div>
        """, unsafe_allow_html=True)

# ==================== ROLE TAB ====================
with role_tab:
    st.header("Role: Multi-Agent Systems Architect")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **The Challenge:** Build a system that doesn't just speed up document reading—it **reasons**
        across unstructured data (call transcripts, emails, CSVs) and **synthesizes** competitive
        intelligence from historical bids while maintaining **enterprise governance** (no data leakage,
        full audit trails).

        **My Architecture Strategy:**
        1. **Hybrid Intelligence**: Local ML for deterministic structure (PII detection, rule validation)
           + LLM agents for reasoning (objection anticipation, strategy synthesis)
        2. **Governance-First**: Every agent output logged, confidence scored, and SME-overridable.
           No black-box decisions on $500K bids.
        3. **Domain Portability**: Same 9-agent backbone as L&D system, swappable JSON-LD ontology
           (IT skills vs. Training competencies)

        **The Technical Lead Role:**
        - Designed 7-layer architecture (Interface → Processing → Governance → Knowledge → Agents)
        - Built the 9-agent orchestration layer in Python (Azure ML Studio)
        - Implemented the GraphRAG knowledge layer for cross-bid reasoning
        - Created the SME "Gate" system for high-stakes decisions
        """)
        st.info("""
        **Recruiter Note:** This answers your question about "hands-on vs. strategic." I was **70% hands-on**
        (coding the agent orchestration, vector embeddings, governance rules) and **30% strategic**
        (designing the ontology schema with Solutions Architects).
        """)
    with col2:
        st.subheader("Enterprise Tech Stack")
        stack = {
            "Orchestration": ["FastAPI", "Azure ML", "Python 3.9"],
            "AI/ML": ["Azure OpenAI", "FAISS", "sklearn", "LayoutLM"],
            "Data": ["PostgreSQL", "JSON-LD", "Qdrant Vector DB"],
            "Governance": ["PII Detector", "Audit Logger", "Policy Engine"],
            "Interface": ["Streamlit", "MS Teams API", "SharePoint"]
        }
        for category, tools in stack.items():
            with st.expander(category):
                for tool in tools:
                    st.write(f"- {tool}")
        st.divider()
        st.write("**Team Context:** 2 ML Engineers, 1 Solutions Architect, 1 Product Manager, + 3 Sales Engineers (feedback)")

# ==================== ACTION TAB ====================
with action_tab:
    st.header("Action: The 9-Agent Orchestration Engine")
    st.write("**Core Innovation:** Elevate operates as a **council of specialized agents**, each with specific governance constraints, passing structured data through a deterministic pipeline.")
    agent_options = [
        "1. Ingestion Agent", "2. Labeling Agent", "3. Governance Agent", "4. Ontology Agent",
        "5. Retrieval Agent", "6. Assessment Agent", "7. Synthesis Agent", "8. Confidence Agent", "9. Feedback Agent"
    ]
    selected_agent = st.selectbox("Select Agent for Deep Dive:", agent_options)

    if "Ingestion" in selected_agent:
        st.subheader("Agent 1: Ingestion Agent (Local ML)")
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write("""
            **Function:** Document normalization and structural parsing before AI sees data.
            **Technical:** LayoutLM for structure, PII Scanner for masking, multi-modal input (PDFs, CSV, Teams transcripts).
            **Governance:** All documents sanitized and tagged before entering the agent pipeline.
            """)
            st.code("""
class IngestionAgent:
    def process_document(self, file_path, source_type):
        doc_structure = layoutlm_extractor.parse(file_path)
        pii_scan = self.pii_detector.scan(doc_structure.text)
        if pii_scan.risk_score > 0.7:
            doc_structure.mask_pii(pii_scan.entities)
            self.governance_log.log_pii_action(file_path, pii_scan)
        doc_structure.metadata = {"source": source_type, "timestamp": datetime.now(), "trace_id": generate_uuid()}
        return doc_structure
            """, language="python")
        with col2:
            st.metric("Documents Processed", "500+/month"); st.metric("PII Incidents Blocked", "100%"); st.metric("Processing Time", "<2 min/doc")
            st.markdown("<div class='governance-alert'><strong>Governance:</strong> All documents PII-scanned before LLM. Audit trail immutable.</div>", unsafe_allow_html=True)

    elif "Labeling" in selected_agent:
        st.subheader("Agent 2: Labeling Agent (LLM + Local ML Validation)")
        st.write("""
        **Function:** Semantic tagging with consistency validation. LLM extracts labels; Local ML validates against historical patterns; flags ambiguity for SME.
        **Example:** "cloud-hesitant" → [Cloud_Migration_Risk: High, Security_Concern: Historical]
        """)
        st.code("""
def label_document(self, doc):
    llm_labels = self.llm.extract_entities(doc.text)
    validation = self.consistency_checker.validate(llm_labels, self.knowledge_graph.get_label_distribution())
    if validation.anomaly_score > 0.8:
        self.sme_queue.flag_for_review(doc, llm_labels, validation)
        confidence = "low"
    else:
        confidence = "high"
    return LabelSet(entities=llm_labels, confidence=confidence)
        """, language="python")

    elif "Governance" in selected_agent:
        st.subheader("Agent 3: Governance Agent (The Enterprise Gatekeeper)")
        st.write("""
        **Enforcement:** Policy compliance, bias detection, threshold routing to SMEs, immutable audit trace.
        **Enterprise Safety:** Azure OpenAI (no client data training), data isolation per client, role-based access.
        """)
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Block vendor mentions under NDA", value=True)
            st.checkbox("Require legal review for >$100K bids", value=True)
            st.checkbox("Mask competitor pricing from LLM", value=True)
        with col2:
            st.metric("Policy Violations Blocked", "23/month"); st.metric("Avg. Audit Time", "<50ms"); st.metric("Compliance Score", "100%")

    elif "Ontology" in selected_agent:
        st.subheader("Agent 4: Ontology Agent (Graph Builder)")
        st.write("**Function:** Maintains JSON-LD semantic layer. Same agent works for L&D (skills) and IT (tech stack) by swapping schema.")
        st.code('{"@type": "ITAssessment", "clientProfile": {"industry": "Manufacturing", "cloudReadiness": 0.3}, "competencyGaps": [{"skill": "Azure Migration", "currentLevel": 0, "targetLevel": 3}]}', language="json")

    elif "Retrieval" in selected_agent:
        st.subheader("Agent 5: Retrieval Agent (GraphRAG)")
        st.write("**Function:** Cross-document reasoning via vector similarity + knowledge graph. Finds relationships between current bid and historical bids.")
        st.markdown("**Tiers:** Tier 1 (98%): Exact match. Tier 2 (85%): Similar tech. Tier 3 (65%): Vector only + manual review.")

    elif "Assessment" in selected_agent:
        st.subheader("Agent 6: Assessment Agent (Core Intelligence)")
        st.write("**Function:** Multi-criteria scoring (technical fit, financial viability, strategic alignment, risk). Deterministic rubric + LLM narrative.")
        st.code("""
composite = (technical_fit*0.3 + financial_viability*0.4 + strategic_alignment*0.2 + (1-risk_level)*0.1)
explanation = self.llm.synthesize_assessment(scores, retrieved_cases)
return Assessment(score=composite, narrative=explanation, confidence=...)
        """, language="python")

    elif "Synthesis" in selected_agent:
        st.subheader("Agent 7: Synthesis Agent (Output Generator)")
        st.write("**Output:** Executive Summary, Technical Assessment, Risk Analysis, Pricing Strategy, Objection Handling, Source Attribution. No hallucinated case studies.")

    elif "Confidence" in selected_agent:
        st.subheader("Agent 8: Confidence Agent (Uncertainty Quantification)")
        st.write("**Formula:** Retrieval×0.4 + Policy×0.3 + Data Coverage×0.2 + Historical×0.1. **Thresholds:** >90% auto-approve; 70-90% SME review; <70% deep analysis.")
        conf_df = pd.DataFrame({'Dimension': ['Retrieval', 'Policy', 'Data Coverage', 'Historical'], 'Weight': [40, 30, 20, 10], 'Score': [92, 88, 95, 85]})
        fig = px.bar(conf_df, x='Dimension', y='Score', color='Weight', title='Confidence Breakdown')
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#CCD6F6'))
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.subheader("Agent 9: Feedback Agent (Reinforcement Learning)")
        st.write("**Loop:** SME overrides → Feedback logs → Ontology updates → Future bids improve. No unsupervised drift.")

    st.divider()
    st.subheader("7-Layer Architecture Visualization")
    if HAS_GRAPHVIZ:
        arch = graphviz.Digraph()
        arch.attr(rankdir='TB')
        layers = [("L1","Client Interface"),("L2","Input Processing"),("L3","Governance"),("L4","Knowledge"),("L5","9 Agents"),("L6","Assessment Engine"),("L7","Output & Feedback")]
        for node, label in layers:
            arch.node(node, label, shape='box', style='filled', fillcolor='#e3f2fd' if node != 'L5' else '#fff3cd')
        for i in range(len(layers)-1):
            arch.edge(layers[i][0], layers[i+1][0])
        arch.edge("L7", "L4", label="Feedback", style='dashed', color='red')
        st.graphviz_chart(arch)
    else:
        st.info("L1 Interface → L2 Processing → L3 Governance → L4 Knowledge → L5 Agents → L6 Assessment → L7 Output (Feedback to L4)")

# ==================== IMPACT TAB ====================
with impact_tab:
    st.header("Impact: $2.1M Revenue Protection + 75% Time Savings")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='roi-metric'><h2>3 Weeks → 3 Days</h2><small>86% faster</small></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='roi-metric'><h2>+23%</h2><p>Win Rate</p><small>58% → 81%</small></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='roi-metric'><h2>$2.1M</h2><p>Revenue Protected</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='roi-metric'><h2>15 → 4 hrs</h2><p>Hours/Bid</p><small>73% reduction</small></div>", unsafe_allow_html=True)
    st.divider()
    st.subheader("ROI Breakdown")
    roi_calc = pd.DataFrame({
        'Metric': ['Annual Bids', 'Win Rate', 'Avg Deal', 'Additional Wins', 'Revenue Impact', 'Labor Savings'],
        'Before': ['120', '58%', '$75K', '-', '$5.2M', '2,160 hrs'],
        'After': ['120', '81%', '$75K', '+28', '$7.3M', '480 hrs'],
        'Delta': ['-', '+23%', '-', '+28', '+$2.1M', '-1,680 hrs']
    })
    st.dataframe(roi_calc, use_container_width=True, hide_index=True)
    st.subheader("Innovation: Objection Intelligence")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Secret Weapon:** Analyzed 5 years of bids to extract objection patterns. Example: 'Your cost is 20% higher' → AI recommends TCO analysis from 2023 Manufacturing case.")
        st.metric("Objection Prediction Accuracy", "89%"); st.metric("Preparedness Score", "4.2/5.0", "Up from 2.8")
    with col2:
        scenarios = ['Pricing', 'Technical', 'Timeline', 'Security']
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Before', x=scenarios, y=[45, 52, 38, 61], marker_color='#e74c3c'))
        fig.add_trace(go.Bar(name='With Elevate', x=scenarios, y=[92, 88, 85, 94], marker_color='#2ecc71'))
        fig.update_layout(title='Preparedness by Scenario (%)', barmode='group', template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#CCD6F6'))
        st.plotly_chart(fig, use_container_width=True)
    st.subheader("Enterprise Value: Audit Trail")
    st.write("Every agent action logged with Trace ID. SME overrides captured. Full traceability for legal/compliance.")

# ==================== GROWTH TAB ====================
with growth_tab:
    st.header("Growth: From Point Solution to Platform")
    st.write("**Platform Strategy:** Domain-agnostic assessment engine. Same 9-agent backbone, swappable JSON-LD ontology.")
    st.subheader("Architecture Reuse: L&D → IT → Future")
    reuse_data = {
        'Component': ['Ingestion', 'Labeling', 'Governance', 'Ontology', 'Retrieval', 'Assessment', 'Synthesis', 'Confidence', 'Feedback'],
        'L&D': [100, 100, 100, 100, 100, 100, 100, 100, 100],
        'IT_Clone': [85, 75, 95, 60, 90, 80, 85, 95, 90],
        'Sales': [85, 80, 95, 50, 90, 75, 85, 95, 90],
    }
    df_reuse = pd.DataFrame(reuse_data).set_index('Component')
    fig = px.imshow(df_reuse, color_continuous_scale='Greens', aspect='auto',
        labels=dict(x='System', y='Component', color='Reuse %'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#CCD6F6'))
    st.plotly_chart(fig, use_container_width=True)
    st.info("**Key Insight:** Dark green = core platform. Lighter = domain customization. Proves 'build once, deploy many'.")
    st.subheader("12-Month Roadmap")
    r1, r2, r3, r4 = st.columns(4)
    with r1: st.markdown("**Q1**"); st.write("IT Assessment (Internal)"); st.write("Sales Enablement Agent"); st.progress(0.75)
    with r2: st.markdown("**Q2**"); st.write("Compliance Audit Agent"); st.write("HR Performance Assessment"); st.progress(0.3)
    with r3: st.markdown("**Q3**"); st.write("Client-facing portal"); st.write("White-label offering"); st.progress(0)
    with r4: st.markdown("**Q4**"); st.write("Multi-tenant SaaS"); st.write("Ontology marketplace"); st.progress(0)
    st.subheader("Why This Signals Staff+ Capability")
    for p in [
        "**Multi-Agent Architecture**: Orchestrated specialist agents, not single LLM prompt",
        "**Governance-First**: Security, audit, compliance built-in",
        "**Hybrid Intelligence**: Local ML + LLM (hallucination mitigation)",
        "**Domain Portability**: JSON-LD ontologies = platform, not point solution",
        "**Enterprise Integration**: Azure ML, Teams, SharePoint",
        "**Uncertainty Quantification**: Confidence scores route to humans appropriately"
    ]:
        st.markdown(f"- {p}")

# Sidebar
with st.sidebar:
    st.markdown("---")
    st.subheader("Elevate System")
    st.caption("Multi-Agent Assessment Platform")
    st.metric("Agents", "9", "Modular")
    st.metric("Layers", "7", "Governance-first")
    st.metric("Reuse from L&D", "75%", "Platform proof")
    st.metric("Confidence Tiers", "3", "Risk-based")
    st.info("**Recruiter:** 'I architect enterprise AI with 9-agent orchestration, full audit trails, and domain scalability.'")
    st.markdown("**Architecture Series:**")
    st.write("1. BI Convo | 2. HR Agent | 3. L&D System | 4. **Elevate IT**")
