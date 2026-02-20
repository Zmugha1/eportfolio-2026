"""
Customer Intelligence: Segmentation with Data Contracts
K-Means, RFM Analysis, Privacy-by-design, GDPR compliance
"""

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from components.craig_section import _key_terms_box
from components.sidebar_nav import render_sidebar_nav

st.set_page_config(
    page_title="Customer Intelligence | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Paths
BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "data"
CSV_PATH = DATA_DIR / "segmentation_customer_data.csv"
JSON_PATH = DATA_DIR / "segmentation_governance_log.json"

# Custom CSS - uniform font and color
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    [data-testid="stVerticalBlock"] > div { font-family: 'Inter', -apple-system, sans-serif !important; color: #CCD6F6 !important; }
    [data-testid="stMarkdown"] p, [data-testid="stMarkdown"] span, [data-testid="stMarkdown"] div { color: #CCD6F6 !important; }
    [data-testid="stMarkdown"] h1, [data-testid="stMarkdown"] h2, [data-testid="stMarkdown"] h3 { color: #CCD6F6 !important; }
    [data-testid="stTabs"] [role="tab"], [data-testid="stTabs"] button { color: #CCD6F6 !important; }
    [data-testid="stTabs"] [aria-selected="true"] { color: #CCD6F6 !important; border-bottom-color: #8892B0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

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


with st.spinner("Loading segmentation data and governance log..."):
    df, gov = load_data()

if gov is None:
    st.error(f"Governance log not found: {JSON_PATH}")
    st.stop()

# Header
st.title("Project 4: Customer Intelligence (Segmentation with Data Contracts)")
st.markdown("*Stop treating everyone the same, know your clusters, respect their boundaries.*")
st.markdown("---")

# Metrics
mp = gov.get("model_performance") or {}
bi = gov.get("business_impact") or {}
c1, c2, c3, c4 = st.columns(4)
c1.metric("Risk Tier", gov.get("risk_tier", "N/A"))
c2.metric("Silhouette Score", f"{mp.get('silhouette_score', 0):.2f}")
c3.metric("Segments", mp.get("n_segments", 5))
c4.metric("Annual Revenue Lift", f"${bi.get('annual_revenue_lift', 0)/1000000:.1f}M")

st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

with tab1:
    st.subheader("The Dear Valued Customer Massacre")
    st.write("""Imagine you run GlobalRetail, an online store with 2 million customers. Your marketing team sends the same "20% Off Everything" email to everyone.

The Problem:
- New moms get dog food offers (they don't have dogs)
- Corporate buyers get fast-fashion discounts (they need business attire)
- Bargain hunters get luxury product alerts (they can't afford them)
- VIP spenders get generic blasts (they expect white-glove service)

The Result: 0.5% click-through rates, 15% unsubscribe rate, and customers complaining "You clearly don't know me."

The Old Way: Demographics (age, location, gender). Lazy and often wrong. "Women 25-34" includes both broke college students and wealthy executives. "Midwest Region" includes both rural farmers and Chicago tech workers.

The Cost: $3M annually in missed personalization revenue, plus customer churn from irrelevant messaging.""")
    st.info("Why This Matters: In 2024, customers expect Netflix-level personalization. If you treat a $50K/year VIP the same as a one-time $10 buyer, you lose the VIP. Permanently.")
    _key_terms_box("""Customer Segmentation: Grouping customers by behavior (what they buy, when, how often) instead of just demographics (who they are).<br><br>
Clustering: Using math to find "natural groupings" in data, like sorting rocks by size without knowing the sizes beforehand.<br><br>
RFM Analysis: Recency (how recently bought), Frequency (how often), Monetary (how much spent). The "vitals" of customer value.<br><br>
Data Contracts: Legal agreements about how you can use customer data. Breaking them = fines + lawsuits.""")

with tab2:
    st.subheader("The Customer Intelligence Architect")
    st.write("""As Senior Applied Data Scientist, I didn't just "run a clustering algorithm." I built a Customer Intelligence Platform that creates behavioral segments while enforcing data governance (privacy, consent, and fairness).

Why This Was High Risk (Data Governance):
- Privacy Law: GDPR/CCPA require knowing exactly what data you used to make decisions about people (the "right to explanation")
- Discrimination Risk: If segments accidentally correlate with protected classes (race, religion), you create "digital redlining"
- Consent Management: Some customers opted out of "profiling", we had to segment them separately using only permitted data

My Governance Responsibilities:
- Data Lineage: Document exactly which data fields fed into each segment (for audits)
- Consent Filtering: Ensure opted-out customers aren't in behavior-based segments
- Bias Testing: Verify segments don't disproportionately exclude protected groups
- Segment Validation: Ensure clusters are "stable" (real patterns, not random noise)

The Human Element: I worked with marketing to name segments meaningfully:
- Not "Cluster 0" but "Weekend Warriors" (high Fri-Sun activity)
- Not "Cluster 1" but "Bargain Hunters" (only buy on sale)
- Not "Cluster 2" but "VIP Champions" (high value, frequent buyers)

This made segments actionable for non-technical teams.""")

with tab3:
    st.subheader("Finding the Hidden Tribes")

    st.markdown("**Step 1: The Data Audit (Governance First)**")
    dg = gov.get("data_governance") or {}
    opt_out = dg.get("opted_out_pct", 0.12)
    st.write(f"""Before touching the algorithm, we audited data permissions:
- Permitted for segmentation: Purchase history, browsing behavior, email engagement
- Restricted: Demographic inferences (ethnicity, religion, health status)
- Consent status: {opt_out*100:.0f}% opted out of behavioral profiling (separate "generic" segment only)""")

    st.markdown("**Step 2: RFM Engineering (The Behavior DNA)**")
    st.write("""We created 9 core metrics for each customer:
- Recency: Days since last purchase (0-100 scale)
- Frequency: Orders per year (1-50 scale)
- Monetary: Average order value ($10-$1000 scale)
- Engagement: Email click rate, site visits, cart abandonment
- Category Affinity: Preference for electronics vs apparel vs home goods""")

    st.markdown("**Step 3: The Clustering Algorithm (K-Means)**")
    st.write(f"""We used K-Means clustering (imagine throwing darts at a board and grouping customers by who stands closest together).

The "Elbow Method": We tested 2, 3, 4, 5... up to 10 segments. At {mp.get('n_segments', 5)} clusters, adding more didn't improve grouping quality (the "elbow" bend in the graph).

Validation Checks:
- Silhouette Score: {mp.get('silhouette_score', 0.68):.2f} (measures how "distinct" clusters are; >0.5 is good)
- Stability: Ran algorithm {mp.get('stability_runs', 10)} times, got same clusters each time (not random noise)
- Size Balance: No segment smaller than {mp.get('min_segment_pct', 5)}% or larger than {mp.get('max_segment_pct', 40)}%""")

    st.markdown("**Step 4: The Data Contract Implementation**")
    st.write("""We created "Data Contracts", technical documentation that travels with the data:
- Schema validation: If new data arrives with missing fields, pipeline stops (prevents bad segments)
- Consent flags: Automated filtering of opted-out users before segmentation
- Audit logs: Every segment assignment timestamped with data version used
- Governance Control: Before deploying segments to marketing, Legal reviewed for disparate impact. Result: No correlation with protected classes.""")

    _key_terms_box("""K-Means: Algorithm that groups data into K clusters by finding "centroids" (average points) and assigning customers to nearest center.<br><br>
Elbow Method: Graphing segmentation quality vs number of segments. The "elbow" (bend) shows optimal number (usually 3-7).<br><br>
Silhouette Score: Measures how similar a customer is to their own segment vs other segments (-1 to +1, higher is better).<br><br>
Data Contract: Technical agreement specifying what data can be used, how it must be validated, and who can access it (like a legal contract, but enforced by code).<br><br>
Feature Store: Centralized repository for customer features (RFM scores) used across multiple models (segmentation, churn, targeting).""")

with tab4:
    st.subheader("The Personalization Revolution")

    segs = gov.get("segments") or {}
    if segs:
        st.markdown("**The Segments Discovered:**")
        for name, v in segs.items():
            st.write(f"- {name} ({v.get('pct', 0)}% of customers, {v.get('revenue_share', 0)}% of revenue)")

    st.write(f"""The Numbers:
- Email Revenue: Up {bi.get('email_revenue_lift_pct', 340)}% (from $200K to $880K/month)
- Generic blasts: 0.5% click rate | Segmented campaigns: 8.2% click rate
- Customer Lifetime Value: Up {bi.get('clv_lift_pct', 28)}%
- Unsubscribe Rate: Down {bi.get('unsubscribe_reduction_pct', 60)}%
- Data Governance: Zero privacy violations, full audit trail for GDPR requests

The "Soft" Win: Marketing team stopped guessing. Instead of "Let's blast everyone," they ask "What's the Weekend Warriors campaign this week?" The segments became organizational vocabulary.

Governance Win: When a customer filed a GDPR "Right to Explanation" request ("Why am I getting these ads?"), we provided the exact data points used for their segment assignment (RFM scores, purchase categories) within 24 hours. Compliance team praised the "Data Contract" documentation.""")

with tab5:
    st.subheader("From Segments to Individualization")
    st.write("""**Current State:** 5 segments with tailored messaging.

**Next Phase:** Dynamic micro-segments (thousands of "segments of one").

**Phase 2 Roadmap:**

1. Real-Time Segmentation: Currently updated weekly. Move to real-time (customer changes segment mid-browsing session based on current behavior).

2. Look-Alike Expansion: Use segmentation to find "new customers who look like VIP Champions" in prospect databases.

3. Causal Segment Impact: Prove that segment-specific campaigns cause higher value (not just correlation). A/B test: Does treating a "Bargain Hunter" like a "VIP" backfire?

4. Privacy-Preserving Clustering: Implement federated learning, segment customers without centralizing their raw data (encryption during computation).

**The Vision:** Move from "5 buckets" to "infinite personalization", where every customer gets a unique experience, but governed by strict data contracts and privacy constraints.""")

st.markdown("---")

if df is not None and len(df) > 0:
    st.subheader("Sample Customer Data")
    st.dataframe(df.head(15), use_container_width=True)

st.markdown("---")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
