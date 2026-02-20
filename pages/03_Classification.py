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
st.title("Smart Targeting with Classification")
st.markdown("*Random Forest lead scoring, Precision-Recall optimization, drift detection*")
st.markdown("---")

# Metrics from governance
mp = gov["model_performance"]
bi = gov["business_impact"]

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Risk Tier", gov["risk_tier"])
with c2:
    st.metric("AUC", f"{mp['auc']:.2f}")
with c3:
    st.metric("Precision (75% threshold)", f"{mp['precision_at_threshold']:.0%}")
with c4:
    st.metric("Annual Cost Savings", f"${bi['cost_savings_annual']/1000000:.1f}M")

st.markdown("---")

# CRAIG Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

with tab1:
    st.subheader("The $2M Cold Calling Disaster")
    st.write("""Imagine you run a sales team at TechSolutions Inc. Your reps are making 1,000 cold calls per day. They hate it. Customers hate it. And 95% of those calls go nowhere, wasting $80 per call in rep time and phone costs.

The old approach? "Spray and pray." Call everyone on the list and hope someone bites. It's like fishing with dynamite, expensive, annoying, and you scare away all the fish.

Meanwhile, buried in your CRM data were clear signals:
- Some prospects downloaded white papers (interested)
- Some visited pricing pages (very interested)
- Some opened 5 emails but never clicked (not ready)
- Some were enterprise size with budget authority (high value)

The Problem: Sales reps couldn't see these patterns. They were calling "John from Accounting" who accidentally clicked an ad, while ignoring "Sarah the CTO" who was actively researching solutions.

The Cost: $2M annually in wasted sales effort, plus burned bridges with annoyed prospects who now block your number.""")
    st.info("Why This Matters: In B2B sales, calling the wrong person doesn't just waste money, it destroys brand reputation. You get one chance to make a first impression. Don't waste it on someone who will never buy.")
    _key_terms_box("""Classification Model: A system that sorts people into "Likely to Buy" vs "Not Ready" categories, like a spam filter for your sales pipeline.<br><br>
Precision vs Recall: Precision means "when we say they'll buy, we're usually right" (quality). Recall means "we caught most of the actual buyers" (quantity). You need balance, calling only perfect leads means missing good ones; calling everyone means wasting money.<br><br>
False Positives: Predicting someone will buy, but they don't. Expensive mistake (wasted sales call).<br><br>
False Negatives: Predicting someone won't buy, but they would have. Missed opportunity (competitor gets them).""")

with tab2:
    st.subheader("The Lead Scoring Architect")
    st.write("""As Senior Applied Data Scientist, I didn't just build a "lead scoring algorithm", I built a Smart Targeting System that tells sales reps exactly which 100 prospects to call today (out of 10,000), ranked by likelihood to convert and deal size.

Why This Was High Stakes: This is Medium-High Risk in our MRM framework because:
- Revenue Impact: If the model is wrong, we miss quarterly targets (sales reps waste time on bad leads)
- Fairness Risk: We had to ensure we weren't discriminating against certain industries or company sizes (legal compliance)
- Drift Risk: Prospect behavior changes (e.g., during economic downturns), but the model keeps using old assumptions, like using a 2019 map in 2024

My Governance Responsibilities:
- Pre-deployment: Validate that the model works equally well for Enterprise vs SMB prospects (no bias)
- Monitoring: Set up "drift detection", automatic alerts when prospect behavior changes and the model gets stale
- Threshold Setting: Determine the "call score" cutoff (75/100) balancing sales team capacity vs opportunity cost
- Documentation: Create "Model Cards" showing exactly how the model makes decisions (transparency for sales leadership)

The Human Element: I didn't just hand sales a black box algorithm. I built a dashboard showing why each lead scored high ("Downloaded security whitepaper + visited pricing page + VP title"), so reps could have intelligent conversations, not robotic pitches.""")

with tab3:
    st.subheader("Teaching the Machine to Recognize Buying Signals")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Step 1: The Data Detective Work**")
        st.write(f"""We analyzed 2 years of historical sales data, {mp['sample_size']:,} prospects, tracking {mp['n_features']} signals:
- Digital body language (email opens, webpage visits, content downloads)
- Firmographic data (company size, industry, budget authority)
- Engagement velocity (how fast they moved through the funnel)""")

        st.markdown("**Step 2: Building the Classifier**")
        st.write("""We used a Random Forest algorithm (think of it as asking 100 different "expert trees" for their opinion, then voting on the answer). Why not simple rules? Because buying signals interact in complex ways:
- "Downloaded whitepaper" alone = 5% conversion
- "Downloaded whitepaper + Pricing page + VP title" = 65% conversion

The model learned these combinations automatically.""")

    with col2:
        st.markdown("**Step 3: The Governance Layer**")
        st.write(f"""Before deploying, we ran three critical checks:

Bias Audit: Does the model favor certain industries? We tested accuracy across Healthcare, Finance, and Tech sectors. Result: 94% precision across all groups (passes fairness).

Drift Detection Baseline: We measured the "normal" distribution of lead characteristics (company size, engagement rates) to create a "fingerprint." If future leads look different (e.g., suddenly more small businesses), the model alerts us, it might be outdated.

Threshold Optimization: We plotted the Precision-Recall Curve to find the sweet spot:
- At 90% confidence: Only call 50 leads/week, but 90% convert (too conservative, miss opportunities)
- At 50% confidence: Call 500 leads/week, but only 20% convert (too expensive)
- Sweet Spot (75%): Call 200 leads/week, 75% convert (optimal ROI)""")

    st.markdown("**Step 4: Production MLOps**")
    st.write("""- Model Registry: Version-controlled deployment (v1.2.3) with rollback capability
- A/B Testing: 50% of reps used old method, 50% used AI recommendations for 30 days to prove value
- Real-time Scoring: New leads scored within 5 minutes of web activity (API integration)""")

    _key_terms_box("""Random Forest: An algorithm that builds 100+ "decision trees" and lets them vote. More accurate than a single tree, less likely to overfit.<br><br>
Feature Engineering: Creating smart inputs for the model, like "days since last website visit" or "email engagement score" (0-100).<br><br>
Drift Detection: Monitoring if new data looks different from training data. Like realizing your GPS is using old maps because the roads changed.<br><br>
Precision-Recall Tradeoff: The tension between "only high-quality leads" (high precision) vs "don't miss any buyers" (high recall).<br><br>
Model Registry: A library that tracks which version of the model is running in production, who approved it, and when to rollback.""")

with tab4:
    st.subheader("The 3x Sales Efficiency Breakthrough")

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Calls Before", f"{bi['calls_before_per_week']:,}/week")
    with m2:
        st.metric("Calls After", f"{bi['calls_after_per_week']:,}/week")
    with m3:
        st.metric("Conversion", f"{bi['conversion_after_pct']:.0%}")
    with m4:
        st.metric("Efficiency Gain", f"{bi['efficiency_lift']:.0f}x")

    st.write("""The Numbers:
- Before: 1,000 calls/week, 50 deals (5% conversion), $200K revenue
- After: 200 calls/week, 150 deals (75% conversion), $600K revenue
- Efficiency Gain: 3x more deals with 80% fewer calls
- Cost Savings: $1.6M annually in reduced sales effort
- Rep Satisfaction: Up 40% (they're closing deals, not being hung up on)

The "Soft" Benefits:
- Brand Reputation: Stopped annoying unqualified prospects
- Sales Confidence: Reps trust the AI because they see the "why" (explanations)
- Pipeline Velocity: Average deal closes 12 days faster (targeting ready buyers, not tire-kickers)

Governance Win: Zero bias incidents. Model monitored weekly for drift. When COVID-19 hit and buying patterns shifted (suddenly everyone wanted remote-work solutions), drift detection triggered within 14 days. We retrained the model with new data rather than letting it make bad recommendations for months.""")

    st.success(f"ROI Breakdown: Model development cost ${bi['model_dev_cost']/1000:.0f}K. Annual savings ${bi['cost_savings_annual']/1000:.0f}K. {bi['roi_year1']}x return in Year 1.")

with tab5:
    st.subheader("From Lead Scoring to Opportunity Intelligence")
    st.write("""**Current State:** We identify "who to call today."

**Next Phase:** We identify "what to say" and "when to say it."

**Phase 2 Roadmap:**

1. Next-Best-Action Engine: Instead of just scoring, recommend the specific action:
   - "Send case study on security compliance" (if they downloaded security content)
   - "Offer ROI calculator" (if they visited pricing twice)
   - "Introduce technical architect" (if they have technical questions)

2. Causal Uplift Modeling: Don't just predict who will buy, predict who needs the call to buy. Some people buy anyway (don't waste time on them). Some never buy (don't waste time on them). Focus on the "persuadables", people who buy ONLY if contacted.

3. Dynamic Pricing Integration: Combine lead score with optimal pricing. High-score lead + tight budget = standard pricing. High-score lead + loose budget = premium pricing (they'll pay for value).

**The Vision:** A fully autonomous "Sales Intelligence" system that not only ranks leads but orchestrates the entire outreach strategy, timing, channel (email vs call vs LinkedIn), message, and pricing, personalized per prospect.""")

st.markdown("---")

# Bias audit table
if "bias_audit" in gov:
    st.subheader("Bias Audit by Industry Segment")
    ba = gov["bias_audit"]
    ba_data = []
    for ind, v in ba.items():
        ba_data.append({"Industry": ind.title(), "Precision": f"{v['precision']:.0%}", "Support": v["support"]})
    st.dataframe(pd.DataFrame(ba_data), use_container_width=True)

# Sample data preview
if df is not None and len(df) > 0:
    st.subheader("Sample Lead Data")
    st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
