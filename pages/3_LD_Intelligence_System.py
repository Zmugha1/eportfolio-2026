"""
L&D Intelligence System (ILI Assistant)
Multi-Agent Workflow Automation for Impact Leadership Institute
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
    page_title="L&D Intelligence System | Dr. Data",
    page_icon="🎓",
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
.domain-badge { background-color: rgba(155, 89, 182, 0.4); color: #CCD6F6; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; display: inline-block; margin: 0.25rem; border: 1px solid #9b59b6; }
.workflow-box { background-color: #112240; border-left: 5px solid #9b59b6; padding: 1rem; margin: 0.5rem 0; border-radius: 0 10px 10px 0; color: #CCD6F6; }
.agent-card { background-color: #112240; border: 2px solid #8892B0; border-radius: 10px; padding: 1rem; margin: 0.5rem 0; text-align: center; color: #CCD6F6; }
.sme-gate { background-color: rgba(255, 193, 7, 0.15); border: 2px dashed #ffc107; padding: 1rem; border-radius: 10px; margin: 1rem 0; color: #CCD6F6; }
</style>
""", unsafe_allow_html=True)

st.title("🎓 L&D Intelligence System (ILI Assistant)")
st.subheader("Multi-Agent Workflow Automation: From Weeks to Hours")
st.caption("Impact Leadership Institute | Impact Networking | Multi-Agent Architecture with Human-in-the-Loop")

st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
    <strong>🎯 Domain Expertise Advantage:</strong> I built this for my former department.
    Having been a technical trainer and OD consultant, I knew exactly where the bottlenecks were
    in the training development lifecycle. This wasn't just coding—it was systems design informed by
    6+ years in workforce development.
</div>
""", unsafe_allow_html=True)

context_tab, role_tab, action_tab, impact_tab, growth_tab = st.tabs([
    "📖 CONTEXT: Slow Lifecycle", "🎯 ROLE: The Systems Architect", "⚡ ACTION: Multi-Agent Build",
    "📊 IMPACT: Weeks → Hours", "🚀 GROWTH: IT Assessment Clone"
])

with context_tab:
    st.header("The Training Bottleneck: 6-Week Program Development")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.write("""
        **The Pain Point at Impact Leadership Institute:**
        Creating a custom corporate training program followed an archaic waterfall process:
        1. **Needs Analysis** (Week 1-2): Consultant interviews stakeholders, documents gaps
        2. **Content Design** (Week 3-4): Instructional designers build curriculum, wait for SME reviews
        3. **Material Creation** (Week 5): PowerPoints, handouts, assessments created manually
        4. **Review Cycles** (Week 6): Back-and-forth with SMEs via email, version control nightmares
        **Total Time: 6-8 weeks per program**
        **The Cost:** High-potential employees waited months for critical leadership training.
        """)
        st.error("**The Breaking Point:** A manufacturing client needed emergency safety training after an OSHA incident. The traditional process would take 6 weeks. They needed it in 48 hours. ILI couldn't deliver—until we built the AI system.")
    with col2:
        st.subheader("Legacy Process")
        for step, duration, method in [("Needs Analysis","2 weeks","Manual"),("Design","2 weeks","Static"),("Development","1 week","Manual"),("SME Review","2 weeks","Email"),("Delivery","1 week","Scheduling")]:
            st.markdown(f"<div style='background-color: rgba(255,107,107,0.15); padding: 0.5rem; margin: 0.25rem 0; border-radius: 5px; color: #CCD6F6;'><strong>{step}</strong><br><small>{duration} • {method}</small></div>", unsafe_allow_html=True)
        st.metric("Avg. Time to Delivery", "6-8 weeks", "Unacceptable")
        st.metric("SME Revision Cycles", "4.2 avg", "Bottleneck")
        st.metric("Cost per Program", "$15K-$25K", "High")

with role_tab:
    st.header("Role: Systems Architect & Domain Expert")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **My Unique Position:** I WAS the SME for this project. I had spent years as a technical trainer and workforce development consultant. I knew the tacit rules, failure modes, and stakeholders.
        **Dual Role:** 1) Systems Designer: Lucidchart/Mermaid architecture diagrams. 2) Technical Lead: Multi-agent Python system with SME gates.
        **Architecture Philosophy:** I reimagined it as a **human-AI collaborative workflow** where AI handles routine synthesis and humans handle strategic decisions.
        """)
        st.info("**Recruiter Note:** This demonstrates I can operate at the intersection of **Technical Architecture** (multi-agent systems) and **Organizational Development** (training workflows)—a rare combination for Staff+ roles.")
    with col2:
        st.subheader("Domain Expertise Stack")
        for domain in ["Instructional Design", "Andragogy", "Workforce Dev", "OD Theory", "Competency Mapping", "SME Management"]:
            st.markdown(f"<span class='domain-badge'>{domain}</span>", unsafe_allow_html=True)
        st.divider()
        st.subheader("Multi-Agent Architecture")
        st.write("1. Intake Agent (NLP) | 2. Design Agent (Content) | 3. Review Agent (Quality) | 4. Delivery Agent (Logistics)")

with action_tab:
    st.header("Action: Building the 4-Agent Ecosystem")
    agent = st.selectbox("Select Agent:", ["Agent 1: Intake & Analysis", "Agent 2: Curriculum Design", "Agent 3: SME Review Gateway", "Agent 4: Delivery Orchestration"])
    if agent == "Agent 1: Intake & Analysis":
        st.subheader("Agent 1: Needs Analysis & Intake")
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write("**Problem:** 2 weeks of stakeholder interviews. **Solution:** AI agent conducts structured intake via chat/Teams. Extracts: target audience, competency gaps, compliance, time constraints. Output: structured needs analysis + modality recommendation.")
            st.code("""
# Competency Extraction Logic
def extract_competency_gap(conversation_transcript):
    gaps = []
    for sentence in conversation_transcript:
        if "struggling with" in sentence or "need to learn" in sentence:
            skill = extract_skill_entity(sentence)
            proficiency = assess_current_level(skill)
            target = determine_target_level(skill)
            gaps.append({
                "competency": skill,
                "current": proficiency,
                "target": target,
                "gap_size": target - proficiency
            })
    return prioritize_gaps(gaps, business_context)
            """, language="python")
        with col2:
            st.markdown("""
            <div class='agent-card'>
                <h3>🎤 Intake Agent</h3>
                <p><strong>Input:</strong> Stakeholder chat</p>
                <p><strong>Process:</strong> NLP extraction</p>
                <p><strong>Output:</strong> Structured analysis</p>
                <hr>
                <p><strong>Time Saved:</strong> 10 days → 2 hours</p>
            </div>
            """, unsafe_allow_html=True)
            st.chat_message("user").write("We need leadership training for new managers. They're struggling with difficult conversations.")
            st.chat_message("assistant").write("""
            **Analysis Complete:**
            - Target: New managers (0-2 years exp)
            - Competency Gap: Conflict Management (Current: L2, Target: L4)
            - Modality Recommendation: Blended (workshop + simulation)
            - Compliance: None required
            - Urgency: Medium (next quarter)
            - **Next Step**: Routing to Design Agent...
            """)
    elif agent == "Agent 2: Curriculum Design":
        st.subheader("Agent 2: Automated Curriculum Design")
        st.write("**Problem:** Days creating outlines. **Solution:** Agent generates first-draft from competency gaps + 50+ templates. Template matching, modality selection, assessment builder.")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Before:** Blank PPT, 3 days, generic cases")
        with col2:
            st.write("**After:** Template-based, 30 min, contextual scenarios")
        st.code("def generate_curriculum(gap, profile):\n    template = match_template(gap.domain, profile.seniority)\n    content = { 'module_1': generate_intro(gap), 'module_2': generate_theory(gap), 'assessment': generate_assessment(gap.objectives) }\n    return apply_andragogy(content, profile)", language="python")
    elif agent == "Agent 3: SME Review Gateway":
        st.subheader("Agent 3: The SME Gate (Human-in-the-Loop)")
        st.write("**Rules:** Auto-Approve: soft skills. SME Required: technical, compliance, safety. Legal Required: harassment, medical, financial.")
        st.markdown("<div class='sme-gate'><h4>🚦 SME Gate Logic</h4><p><strong>IF</strong> content_type==compliance OR risk>medium → Route to SME → AI pre-flags → SME approves/modifies → Feedback trains AI</p></div>", unsafe_allow_html=True)
        for step, time, detail in [("AI generates draft","2 hrs","OSHA templates"),("AI flags for SME","Auto","Fall Protection→safety engineer"),("SME Review","24 hrs","Teams integration"),("AI incorporates feedback","30 min","Auto revisions"),("Final Approval","1 hr","Legal sign-off")]:
            c1, c2, c3 = st.columns([2, 1, 3])
            c1.write(f"**{step}**")
            c2.write(time)
            c3.write(detail)
    else:
        st.subheader("Agent 4: Delivery & Logistics")
        st.write("**Problem:** Manual scheduling, forgotten learners. **Solution:** Smart scheduling, prerequisite checks, nudge engine, real-time completion tracking.")
        c1, c2, c3 = st.columns(3)
        c1.metric("Scheduling", "2 hrs → 5 min", "-95%")
        c2.metric("No-Show", "25% → 8%", "-68%")
        c3.metric("Tracking", "Manual → Real-time", "Auto")
    st.divider()
    st.subheader("Multi-Agent System Architecture")
    if HAS_GRAPHVIZ:
        arch = graphviz.Digraph()
        arch.attr(rankdir='TB')
        arch.node('A', 'Intake Agent\n(NLP)', shape='box', style='filled', fillcolor='#e3f2fd')
        arch.node('B', 'Design Agent\n(Content)', shape='box', style='filled', fillcolor='#f3e5f5')
        arch.node('C', 'SME Gate\n(Human-in-Loop)', shape='diamond', style='filled', fillcolor='#fff3cd')
        arch.node('D', 'Delivery Agent\n(Logistics)', shape='box', style='filled', fillcolor='#e8f5e9')
        arch.node('E', 'Competency DB', shape='cylinder')
        arch.node('F', 'Template Library', shape='cylinder')
        arch.node('G', 'SME Queue', shape='folder')
        arch.edges(['AB', 'BC', 'CD'])
        arch.edge('B', 'E', label='Queries')
        arch.edge('B', 'F', label='Uses')
        arch.edge('C', 'G', label='Routes to')
        arch.edge('G', 'C', label='Feedback')
        st.graphviz_chart(arch)
    else:
        st.info("Architecture: Intake → Design → SME Gate → Delivery (graphviz not installed)")

with impact_tab:
    st.header("Impact: From 6 Weeks to 48 Hours")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div style='background: rgba(46,204,113,0.2); padding: 2rem; border-radius: 10px; text-align: center; border: 2px solid #2ecc71;'><h1 style='color:#2ecc71'>6 weeks → 48 hours</h1><p style='color:#CCD6F6'>For urgent compliance training</p></div>", unsafe_allow_html=True)
    with col2:
        st.metric("Standard Programs", "6 wks → 5 days", "-88%")
        st.metric("SME Time", "20 hrs → 4 hrs", "-80%")
        st.metric("Revision Cycles", "4.2 → 1.3", "-69%")
    with col3:
        st.metric("Programs/Year", "12 → 34", "+183%")
        st.metric("Satisfaction", "3.2 → 4.6★", "+44%")
        st.metric("Cost/Program", "$18K → $12K", "-33%")
    st.divider()
    st.subheader("Case Study: Emergency OSHA Compliance")
    st.write("**Crisis:** Manufacturing client, safety incident, OSHA retraining in 7 days for 200 workers. **AI Solution:** H0-2 Intake; H2-6 Design; H6-24 SME Gate; H24-30 Delivery; H30-48 Training delivered. **Result:** 5 days ahead of deadline. $150K annual contract.")
    df = pd.DataFrame({'Phase':['Intake','Design','Review','Delivery','Total'],'Traditional_Days':[10,14,10,5,39],'AI_Assisted_Days':[0.5,1,1.5,0.5,3.5]})
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Traditional (Days)', x=df['Phase'], y=df['Traditional_Days'], marker_color='#e74c3c'))
    fig.add_trace(go.Bar(name='AI-Assisted (Days)', x=df['Phase'], y=df['AI_Assisted_Days'], marker_color='#2ecc71'))
    fig.update_layout(
        title='Training Development Timeline: Traditional vs. AI-Assisted',
        barmode='group',
        yaxis_title='Days',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#CCD6F6')
    )
    st.plotly_chart(fig, use_container_width=True)

with growth_tab:
    st.header("Growth: Cloning the Architecture (IT Assessment Agent)")
    st.write("**70% Reuse:** 4-Agent pattern, SME Gate, Lucidchart, Python/Azure, Teams. **30% Custom:** Competency DB→IT Skills, templates→IT Assessment, SMEs→Solutions Architects.")
    df_reuse = pd.DataFrame({'Component':['Intake','Design','SME Gate','Delivery','Integrations'],'Reuse_%':[85,75,95,90,100]})
    fig = px.bar(df_reuse, x='Component', y='Reuse_%', title='Architecture Reuse: L&D → IT Assessment', color='Reuse_%', color_continuous_scale='Greens', range_y=[0,100])
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#CCD6F6'))
    st.plotly_chart(fig, use_container_width=True)
    st.info("**Recruiter Insight:** I build **platforms**, not one-off projects. Reuse % increased 70%→85% with each iteration.")
    st.subheader("IT Assessment Clone: Bid Response Automation")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**L&D:** Input=Training needs, Output=Curriculum, SME=Instructional Designer")
    with c2:
        st.write("**IT:** Input=RFP, Output=Bid proposal, SME=Solutions Architect, Urgency=48hr")
    st.subheader("Innovation: Objection Intelligence")
    st.write("Agent analyzed 5 years of bids, extracted objection patterns, auto-generated Objection Handling Guides. **Impact:** Bid turnaround 3 wks→3 days, Win rate +23%, 15 hrs/bid saved.")
    st.subheader("Roadmap: From 2 Agents to Ecosystem")
    roadmap_cols = st.columns(4)
    with roadmap_cols[0]:
        st.markdown("**Month 1-2**"); st.write("✅ HR Agent (Single)"); st.write("Foundation built")
    with roadmap_cols[1]:
        st.markdown("**Month 3-4**"); st.write("✅ L&D System (Multi)"); st.write("SME gates added")
    with roadmap_cols[2]:
        st.markdown("**Month 5-6**"); st.write("✅ IT Assessment"); st.write("Clone & customize")
    with roadmap_cols[3]:
        st.markdown("**Month 7+**"); st.write("🔄 Sales Enablement"); st.write("External clients")

with st.sidebar:
    st.markdown("---")
    st.subheader("🎓 L&D System")
    st.metric("Time Reduction", "6 wks → 48 hrs", "-88%")
    st.metric("Architecture Reuse", "70%", "Platform")
    st.metric("SME Time Saved", "80%", "")
    st.metric("Programs/Year", "+183%", "")
    st.info("**Recruiter:** 'I design multi-agent orchestration with human governance gates.'")
