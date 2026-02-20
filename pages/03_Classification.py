"""
Smart Targeting: Random Forest Classification for Lead Scoring
Precision-Recall optimization, Drift Detection, Bias Audit
"""

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from components.craig_section import _key_terms_box

st.set_page_config(
    page_title="Smart Targeting | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Paths
BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "data"
CSV_PATH = DATA_DIR / "targeting_classification_data.csv"
JSON_PATH = DATA_DIR / "targeting_governance_log.json"

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


with st.spinner("Loading targeting data and governance log..."):
    df, gov = load_data()

if gov is None:
    st.error(f"Governance log not found: {JSON_PATH}")
    st.stop()

# Header
st.title("Project 3: Smart Targeting with Drift Detection")
st.markdown("*Classification model for sales efficiency with MLOps governance*")
st.markdown("---")

# Metrics - support both performance (Colab) and model_performance (placeholder) structures
perf = gov.get("performance") or gov.get("model_performance") or {}
auc_val = perf.get("auc_roc") or perf.get("auc") or perf.get("concordance_index", 0)
bi = gov.get("business_impact") or {}
c1, c2, c3, c4 = st.columns(4)
c1.metric("Risk Tier", gov.get("risk_tier", "N/A"))
c2.metric("Model AUC", f"{auc_val:.2f}")
c3.metric("Annual Savings", f"${bi.get('cost_savings_annual', 0)/1000000:.1f}M")
c4.metric("Efficiency Lift", bi.get("efficiency_gain", "N/A"))

st.markdown("---")

# CRAIG Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

with tab1:
    st.subheader("The $2M Cold Calling Disaster")
    st.write("""TechSolutions was making 1,000 cold calls per day with a 5% success rate. Sales reps hated it, prospects hated it, and the company was burning $2M annually on "spray and pray" outreach.

The problem? Buried in the data were clear signals, some prospects downloaded white papers (interested), visited pricing pages (very interested), while others were just accidental clicks. Sales couldn't see these patterns, so they called "John from Accounting" while ignoring "Sarah the CTO" who was actively researching solutions.""")
    st.info("Why This Matters: In B2B sales, calling the wrong person destroys brand reputation. You get one chance at a first impression, don't waste it on someone who will never buy.")
    _key_terms_box("""Classification Model: A system sorting prospects into "Likely to Buy" vs "Not Ready" categories, like a spam filter for your sales pipeline.<br><br>
False Positives: Predicting someone will buy, but they don't. Expensive mistake (wasted sales call).<br><br>
False Negatives: Predicting someone won't buy, but they would have. Missed opportunity (competitor gets them).""")

with tab2:
    st.subheader("The Lead Scoring Architect")
    st.write("""I built a Smart Targeting System that tells sales exactly which 100 prospects to call today (out of 10,000), ranked by likelihood to convert and deal size.

Why High Stakes: This is Medium-High Risk because it affects quarterly revenue targets and requires fairness compliance (we can't discriminate against certain industries). It required VP Sales + Legal approval.

Governance Responsibilities:
- Bias audit: Validate model works equally for Enterprise vs SMB (no discrimination)
- Drift detection: Alert when prospect behavior changes (e.g., economic downturns)
- Threshold setting: Balance "call quality" vs "don't miss opportunities"
- Transparency: Show sales reps WHY each lead scored high (not a black box)""")

with tab3:
    st.subheader("Teaching the Machine to Read Buying Signals")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**The Approach**")
        st.write("""Analyzed 20,000 prospects across 50 signals (email opens, webpage visits, downloads).

Used Random Forest algorithm, 100 "expert trees" voting on the answer. Why? Because buying signals interact: "Downloaded whitepaper" alone = 5% conversion, but "Downloaded whitepaper + Pricing page + VP title" = 65% conversion.""")

        st.write("**Top Buying Signals:**")
        for feat in (gov.get("feature_importance") or [])[:3]:
            st.write(f"- {feat['feature']}: {feat['importance']:.1%} importance")

    with col2:
        st.markdown("**Governance Controls**")
        perf = gov.get("performance") or gov.get("model_performance") or {}
        st.write(f"""- Risk Tier: {gov.get('risk_tier', 'N/A')}
- Approval: {gov.get('approval', 'N/A')}
- Optimal Threshold: {perf.get('optimal_threshold', 0.5):.0%} probability
- Precision: {perf.get('precision_at_threshold', 0):.0%} (when we say they'll buy, we're right)
- Recall: {perf.get('recall_at_threshold', 0):.0%} (we catch most actual buyers)
- Drift Monitoring: Weekly KS tests for data distribution changes""")

    st.markdown("---")
    st.markdown("**Fairness and Bias Audit**")
    st.write("Model accuracy by protected segment (ensuring no discrimination):")
    for group, metrics in (gov.get("fairness_audit") or {}).items():
        st.write(f"- {group}: {metrics['precision']:.1%} accuracy (n={metrics['sample_size']})")

    dm = gov.get("drift_monitoring") or {}
    st.markdown("**Drift Detection Results**")
    st.write(f"Method: {dm.get('method', 'N/A')}")
    st.write(f"Status: {'Drift Detected' if dm.get('drift_detected') else 'No Significant Drift'}")
    st.write(f"Features monitored: {dm.get('features_monitored', 0)}")
    st.write(f"Features drifted: {dm.get('features_drifted', 0)}")

    _key_terms_box("""Random Forest: 100+ decision trees voting on the answer. More accurate than one tree, less likely to overfit.<br><br>
Kolmogorov-Smirnov (KS) Test: A statistical test that checks if two samples (training data vs new data) come from the same distribution. If p-value < 0.05, the data has "drifted" and the model may be outdated.<br><br>
Precision-Recall Tradeoff: The tension between "only high-quality leads" (precision) vs "don't miss any buyers" (recall).""")

with tab4:
    st.subheader("The 3x Sales Efficiency Breakthrough")

    m1, m2, m3 = st.columns(3)
    m1.metric("Weekly Calls", f"{bi.get('calls_reduced_weekly', 0):,} fewer")
    m2.metric("Conversion Lift", bi.get("conversion_lift", "N/A"))
    m3.metric("Annual Savings", f"${bi.get('cost_savings_annual', 0)/1000000:.1f}M")

    st.write("""The Transformation:
- Before: 1,000 calls/week, 50 deals (5% conversion)
- After: 200 calls/week, 150 deals (75% conversion)

Governance Win: When COVID-19 shifted buying patterns, drift detection triggered within 14 days. We retrained the model rather than letting it make bad recommendations for months. Zero bias incidents.

Soft Benefits: Sales rep satisfaction up 40% (they're closing deals, not being hung up on). Brand reputation improved (stopped annoying unqualified prospects).""")

    st.success(f"ROI: ${bi.get('cost_savings_annual', 0)/1000000:.1f}M savings vs $80K development cost = 20x return in Year 1.")

with tab5:
    st.subheader("From Lead Scoring to Opportunity Intelligence")
    st.write("""**Current State:** We identify "who to call today."

**Next Phase:** We identify "what to say" and "when to say it."

**Phase 2 Roadmap:**

1. Next-Best-Action Engine: Recommend specific actions:
   - "Send security case study" (if they downloaded security content)
   - "Offer ROI calculator" (if they visited pricing twice)

2. Causal Uplift Modeling: Focus on the "persuadables", people who buy ONLY if contacted, not those who buy anyway (don't waste time) or never buy (don't waste time).

3. Dynamic Pricing: Combine lead score with optimal pricing. High-score + loose budget = premium pricing.

**The Vision:** Fully autonomous "Sales Intelligence" that orchestrates timing, channel, message, and pricing, personalized per prospect.""")

st.markdown("---")
st.caption("Skills: Random Forest, Classification, Precision-Recall, Drift Detection, Feature Engineering, Bias Auditing")

if df is not None and len(df) > 0:
    st.subheader("Sample Lead Data")
    st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
