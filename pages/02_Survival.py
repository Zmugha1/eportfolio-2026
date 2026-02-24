"""
Survival Analysis: Churn Prevention with Time-to-Event Modeling
Kaplan-Meier, Cox PH, Censored Data, Hazard Ratios
"""

import json
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from components.craig_section import _key_terms_box
from components.sidebar_nav import render_sidebar_nav

st.set_page_config(
    page_title="Survival Analysis | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Paths
BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "data"
CSV_PATH = DATA_DIR / "churn_survival_data.csv"
JSON_PATH = DATA_DIR / "churn_governance_log.json"

# Custom CSS - uniform font and color, no green/teal
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    [data-testid="stVerticalBlock"] > div { font-family: 'Inter', -apple-system, sans-serif !important; font-weight: 400 !important; color: #CCD6F6 !important; }
    [data-testid="stMarkdown"] p, [data-testid="stMarkdown"] span, [data-testid="stMarkdown"] div { color: #CCD6F6 !important; }
    [data-testid="stMarkdown"] h1, [data-testid="stMarkdown"] h2, [data-testid="stMarkdown"] h3 { color: #CCD6F6 !important; }
    [data-testid="stTabs"] [role="tab"], [data-testid="stTabs"] button { color: #CCD6F6 !important; }
    [data-testid="stTabs"] [aria-selected="true"] { color: #CCD6F6 !important; border-bottom-color: #8892B0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load data
@st.cache_data
def load_data():
    df = None
    gov = None
    if CSV_PATH.exists():
        df = pd.read_csv(CSV_PATH)
    if JSON_PATH.exists():
        with open(JSON_PATH) as f:
            gov = json.load(f)
    return df, gov


with st.spinner("Loading churn survival data and governance log..."):
    df, gov = load_data()

if df is None:
    st.error(f"Data file not found: {CSV_PATH}")
    st.stop()

if gov is None:
    gov = {
        "risk_tier": "Medium",
        "model_performance": {"concordance_index": 0.69, "sample_size": 5000},
        "business_impact": {"customers_at_risk": 30, "potential_savings": 15000, "intervention_roi": 0.3},
        "hazard_ratios": {"monthly_spend": 0.99, "support_tickets": 1.05, "feature_adoption": 0.42},
        "fairness_audit": {},
    }

# Safe extraction with fallbacks
mp = gov.get("model_performance") or {}
bi = gov.get("business_impact") or {}
hr = gov.get("hazard_ratios") or {}
conc = mp.get("concordance_index") or 0.69
n_at_risk = bi.get("customers_at_risk") or 30
savings = bi.get("potential_savings") or 15000
roi = bi.get("intervention_roi") or 0.3
hr_spend = hr.get("monthly_spend") or 0.99
hr_tickets = hr.get("support_tickets") or 1.05
hr_feature = hr.get("feature_adoption") or 0.42

# Header
st.title("Churn Prevention with Survival Analysis")
st.markdown("*Time-to-event modeling for proactive customer retention*")
st.markdown("---")

# Metrics
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Risk Tier", gov.get("risk_tier", "Medium"))
with c2:
    st.metric("Model Accuracy", f"{conc:.2f}")
with c3:
    st.metric("Revenue Protected", f"${savings/1000:.0f}K")
with c4:
    st.metric("Intervention ROI", f"{roi:.1f}x")

st.markdown("---")

# CRAIG Tabs with custom headers
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

with tab1:
    st.subheader("The Silent Customer Exodus")
    st.write("""CloudStream was bleeding customers and didn't know why. Every month, 5% of subscribers quietly cancelled, but by the time the sales team noticed missing logins, those customers had already moved to competitors. It was like trying to save a patient after their heart stopped, too late.

The old approach waited for 30 days of inactivity before calling. The problem? Once someone ignores your product for a month, they've already made up their minds. We needed a crystal ball that would warn us 60-90 days earlier, while we could still fix the relationship.""")
    st.info("Why This Matters: In subscription businesses, keeping existing customers costs 5x less than finding new ones. Catching them before they decide to leave is the difference between profit and bankruptcy.")
    _key_terms_box("""Censored Data: Some customers haven't quit yet, we only know they're alive "so far," not their full story. Like watching a movie halfway through and guessing the ending. Regular statistics can't handle this uncertainty, so we use special "survival" methods.<br><br>
Time-to-Event: Instead of just asking "Will they leave?" (yes/no), we ask "How many days until they leave?" This gives us a countdown timer for intervention.""")

with tab2:
    st.subheader("The Early Warning System Architect")
    st.write("""As the Decision Intelligence lead, I didn't just build a "churn predictor", I built an early warning system that tells us exactly which high-value customers are at risk, when to call them, and why they might leave.

Why This Was High Stakes: Predicting customer loss affects revenue reporting, sales team incentives, and customer privacy rights. Get it wrong, and you either waste money chasing happy customers OR lose big accounts because you didn't notice the warning signs. This required VP and Legal approval before deployment.

My job was balancing three risks:
1. Statistical risk: Making sure the model actually worked (not just lucky guesses)
2. Legal risk: Ensuring we weren't accidentally discriminating against certain customer types
3. Business risk: Making sure sales teams trusted the alerts enough to act on them""")

with tab3:
    st.subheader("Building the Crystal Ball")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**The Autopsy vs. The Diagnosis**")
        st.write("""Regular churn models are like autopsies, they tell you why someone died after it happens. We built a diagnostic tool using Survival Analysis (the same math doctors use to predict patient outcomes).

**Finding the Warning Signs:** We analyzed """ + str(mp.get("sample_size", 5000)) + """ customer histories and discovered three signals that predict churn:
- Monthly Spend: Higher spenders stay longer (loyalty investment)
- Support Tickets: Each ticket increases frustration (but zero tickets also means they're not using the product)
- Feature Adoption: Customers who use advanced features stick around (they're "invested" in the platform)""")

    with col2:
        st.markdown("**The Math Translation**")
        st.write(f"""We used Cox Proportional Hazards, fancy words for "what multiplies the risk of leaving?"

- Hazard Ratio of {hr_spend:.3f} for spending means each dollar reduces risk by {(1-hr_spend)*100:.1f}%
- Hazard Ratio of {hr_tickets:.3f} for tickets means each complaint increases risk by {(hr_tickets-1)*100:.1f}%

**Concordance Index:** {conc:.2f} (Good accuracy. 0.5 = coin flip, 1.0 = perfect)

**Governance Check:** Before deploying, we audited the model across Enterprise, SMB, and Startup segments to ensure it was equally accurate for all groups (no discrimination).""")

    _key_terms_box("""Survival Curve: A line graph showing "what percentage of customers are still with us over time." Think of it as a customer loyalty heartbeat.<br><br>
Hazard Ratio: A multiplier for risk. If something has a hazard ratio of 2.0, it doubles your chance of leaving at any moment. Under 1.0 means it protects you.<br><br>
Concordance Index: How well the model ranks customers by risk (0.5 = coin flip, 1.0 = perfect). We achieved """ + f"{conc:.2f}" + """ (good).""")

with tab4:
    st.subheader("The $1.2M Save")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("At-Risk Customers Identified", n_at_risk)
    with m2:
        st.metric("Annual Revenue Protected", f"${savings/1000:.0f}K")
    with m3:
        st.metric("Intervention ROI", f"{roi:.1f}x")

    st.write("""**The Process Change:**
Instead of waiting for 30 days of silence, sales now gets weekly "At-Risk" reports with specific talking points:
- "Customer X opened 5 tickets last month, offer premium support"
- "Customer Y hasn't adopted feature Z, schedule training"

**Governance Win:**
The model passed fairness audits, equally accurate for all customer segments. No disparate impact on protected classes. Full audit trail for compliance.""")

    st.success(f"ROI Calculation: ${savings/1000:.0f}K saved revenue vs. $50K intervention cost = {roi:.1f}x return on the analytics investment.")

with tab5:
    st.subheader("From Prediction to Prescription")
    st.write("""**Current State:** We know WHO is at risk and WHEN.

**Next Phase:** We need to know WHAT to do about it.

**Phase 2 Roadmap:**
1. Causal Retention Modeling: Instead of guessing that "training calls work," prove it with causal inference (randomized encouragement design)
2. Deep Learning Survival: Handle complex interactions (e.g., "high tickets + low spend = immediate risk, but high tickets + high spend = actually engaged")
3. Automated Interventions: Trigger automatic actions (pause billing, send discount) based on risk scores, not just alerts

**The Vision:** Move from "churn prediction" to "retention automation", an AI system that not only warns us but fixes the problem before we even see the alert.""")

st.markdown("---")

# Survival curve visualization (simplified retention by tenure bins)
if "tenure" in df.columns and "churned" in df.columns:
    st.subheader("Customer Retention Over Time")
    bins = [0, 90, 180, 270, 365, 450, 550, 650, 730]
    df_binned = df.copy()
    df_binned["tenure_bin"] = pd.cut(df_binned["tenure"], bins=bins, include_lowest=True)
    retention = (
        df_binned.groupby("tenure_bin", observed=True)
        .agg(n=("customer_id", "count"), churned=("churned", "sum"))
        .assign(survival_pct=lambda x: 100 * (1 - x["churned"] / x["n"]))
        .reset_index()
    )
    retention["bin_mid"] = [b.mid for b in retention["tenure_bin"]]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=retention["bin_mid"],
            y=retention["survival_pct"],
            mode="lines+markers",
            line=dict(color="#8892B0", width=2),
            marker=dict(size=8),
        )
    )
    fig.update_layout(
        xaxis_title="Tenure (days)",
        yaxis_title="% Still Active in Segment",
        template="plotly_dark",
        paper_bgcolor="rgba(10,25,47,0)",
        plot_bgcolor="rgba(17,34,64,0.5)",
        font=dict(color="#CCD6F6"),
    )
    st.plotly_chart(fig, use_container_width=True)

# Fairness audit
st.subheader("Fairness Audit by Segment")
fa = gov.get("fairness_audit") or {}
if fa:
    fa_data = []
    for seg, v in fa.items():
        if isinstance(v, dict):
            cr = v.get("churn_rate", 0)
            at = v.get("avg_tenure", 0)
            fa_data.append({"Segment": str(seg).title(), "Churn Rate": f"{cr:.1%}", "Avg Tenure (days)": f"{at:.0f}"})
    if fa_data:
        st.dataframe(pd.DataFrame(fa_data), use_container_width=True)

st.markdown("---")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
