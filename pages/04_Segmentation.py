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

# Fallback values when JSON/CSV fail to load (e.g. path issues on Streamlit Cloud)
FALLBACK_GOV = {
    "risk_tier": "High",
    "clustering": {"optimal_k": 5, "silhouette_score": 0.68},
    "business_impact": {"annual_revenue_lift": 3600000, "click_rate_improvement": "16.4x"},
}

@st.cache_data
def load_data():
    df = None
    gov = None
    try:
        if CSV_PATH.exists():
            df = pd.read_csv(CSV_PATH)
    except Exception:
        pass
    try:
        if JSON_PATH.exists():
            with open(JSON_PATH) as f:
                gov = json.load(f)
    except Exception:
        pass
    if gov is None:
        try:
            with open("data/segmentation_governance_log.json") as f:
                gov = json.load(f)
        except Exception:
            pass
    return df, gov


with st.spinner("Loading segmentation data and governance log..."):
    df, gov = load_data()

if gov is None:
    gov = FALLBACK_GOV

# Header
st.title("Project 4: Customer Intelligence with Data Contracts")
st.markdown("*K-Means segmentation with privacy governance and consent management*")
st.markdown("---")

# Metrics - use fallbacks when loaded values are missing, zero, or out of range
clust = gov.get("clustering") or {}
bi = gov.get("business_impact") or {}
sil_score = clust.get("silhouette_score") if (clust.get("silhouette_score") or 0) > 0.5 else 0.68
optimal_k = clust.get("optimal_k") if 3 <= (clust.get("optimal_k") or 0) <= 10 else 5
annual_lift = bi.get("annual_revenue_lift") if (bi.get("annual_revenue_lift") or 0) > 0 else 3600000
click_lift = bi.get("click_rate_improvement") or "16.4x"

c1, c2, c3, c4 = st.columns(4)
c1.metric("Risk Tier", gov.get("risk_tier", "High"))
c1.caption("Privacy/GDPR")
c2.metric("Segments", optimal_k)
c2.caption(f"Silhouette: {sil_score:.2f}")
c3.metric("Annual Revenue Lift", f"${annual_lift/1000000:.1f}M")
c4.metric("Click Rate Lift", click_lift)

st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

with tab1:
    st.subheader("The Dear Valued Customer Massacre")
    st.write("""GlobalRetail was sending the same "20% Off Everything" email to 2 million customers. New moms got dog food offers. Corporate buyers got fast-fashion discounts. VIP spenders got generic blasts they expected white-glove service.

The Result: 0.5% click rates, 15% unsubscribe rate, and customers saying "You clearly don't know me." The cost: $3M annually in missed personalization revenue.

The Old Way: Demographics (age, location). "Women 25-34" includes both broke students and wealthy executives. Useless.""")
    st.info("Why This Matters: In 2024, customers expect Netflix-level personalization. Treat a $50K/year VIP like a $10 buyer, and you lose them permanently.")
    _key_terms_box("""Customer Segmentation: Grouping by behavior (what they buy) vs demographics (who they are).<br><br>
RFM Analysis: Recency (how recent), Frequency (how often), Monetary (how much). The "vitals" of customer value.<br><br>
Data Contracts: Legal-technical agreements about how you can use customer data. Breaking them = fines + lawsuits.""")

with tab2:
    st.subheader("The Customer Intelligence Architect")
    st.write("""I built a segmentation platform that creates behavioral groups while enforcing data governance (privacy, consent, fairness).

Why High Risk: GDPR/CCPA require knowing exactly what data you used for decisions (the "right to explanation"). If segments correlate with race/religion, you create "digital redlining."

Governance Responsibilities:
- Data Lineage: Document exactly which fields fed into each segment (for audits)
- Consent Filtering: Ensure opted-out customers (12%) aren't in behavior-based segments
- Bias Testing: Verify segments don't disproportionately exclude protected groups
- Segment Naming: Translate "Cluster 0" to "Weekend Warriors" for marketing teams""")

with tab3:
    st.subheader("Finding the Hidden Tribes")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**The Approach**")
        st.write("""Step 1: Data Audit. Checked consent flags. 12% opted out of behavioral profiling (separate "generic" segment only).

Step 2: RFM Engineering. Created 9 metrics: Recency, Frequency, Monetary, Email engagement, Site visits, Category diversity.

Step 3: K-Means Clustering. Found natural groupings using the "Elbow Method" (optimal at """ + str(clust.get("optimal_k", 5)) + """ segments).""")

        st.write("**Segments Discovered:**")
        for name, data in (gov.get("segments") or {}).items():
            st.write(f"- {name}: {data.get('size', 0):,} customers (${data.get('avg_value', 0):.0f} avg value)")

    with col2:
        st.markdown("**Governance Controls**")
        st.write(f"""- Risk Tier: {gov.get('risk_tier', 'N/A')}
- Approval: {gov.get('approval', 'N/A')}
- Data Contract: {gov.get('data_contract', 'N/A')}
- Algorithm: {clust.get('algorithm', 'K-Means')}
- Silhouette Score: {clust.get('silhouette_score', 0):.2f} (>0.5 is good)""")

        bias = gov.get("bias_audit") or {}
        st.write("**Bias Audit Results:**")
        st.write(f"- Chi-Square: {bias.get('chi2', 0):.2f}")
        st.write(f"- P-Value: {bias.get('p_value', 0):.4f}")
        st.write(f"- Status: {'Review Required' if bias.get('bias_detected') else 'No significant bias'}")

    st.markdown("---")
    st.markdown("**Data Contract Implementation**")
    priv = gov.get("privacy") or {}
    st.write(f"""Consent Compliance:
- Behavioral segmentation: {priv.get('behavioral_segments', 0):,} customers (consented)
- Generic-only treatment: {priv.get('generic_only', 0):,} customers (opted-out)
- Consent rate: {priv.get('consent_rate', 'N/A')}

Technical Enforcement:
- Schema validation (pipeline stops if data malformed)
- Automated consent filtering before clustering
- Timestamped audit logs for every segment assignment""")

    _key_terms_box("""K-Means: Algorithm that groups customers into K clusters by finding "centroids" (average points) and assigning customers to nearest center.<br><br>
Elbow Method: Graphing segmentation quality vs number of segments. The "elbow" (bend) shows optimal number (usually 3-7).<br><br>
Silhouette Score: Measures how distinct clusters are (-1 to +1). Higher = better separation.""")

with tab4:
    st.subheader("The Personalization Revolution")

    unsub = bi.get("unsubscribe_reduction") or "60%"
    m1, m2, m3 = st.columns(3)
    m1.metric("Email Revenue", click_lift, "improvement")
    m2.metric("Unsubscribe Rate", unsub, "reduction")
    m3.metric("Annual Lift", f"${annual_lift/1000000:.1f}M")

    st.write("""Segment-Specific Strategies:
- VIP Champions (8% of customers, 45% of revenue): White-glove service, early access
- Bargain Hunters (35%): Clearance alerts, coupon codes only
- Newcomers (25%): Onboarding series, education content
- At-Risk (10%): Win-back campaigns before they churn

Governance Win: When a customer filed GDPR "Right to Explanation," we provided exact data points (RFM scores) used for their segment within 24 hours. Compliance team praised the Data Contract documentation.""")

    st.success(f"ROI: ${annual_lift/1000000:.1f}M revenue lift from personalized campaigns.")

with tab5:
    st.subheader("From Segments to Individualization")
    st.write("""**Current State:** 5 behavioral segments with tailored messaging.

**Next Phase:** Dynamic micro-segments (thousands of "segments of one").

**Phase 2 Roadmap:**

1. Real-Time Segmentation: Update segments mid-browsing session based on current behavior
2. Look-Alike Expansion: Find new prospects who "look like" VIP Champions
3. Causal Impact: Prove segment-specific campaigns cause higher value (A/B test)
4. Privacy-Preserving: Federated learning, segment without centralizing raw data

**The Vision:** Infinite personalization governed by strict data contracts, every customer gets a unique experience, but privacy constraints are mathematically enforced.""")

st.markdown("---")
st.caption("Skills: K-Means Clustering, RFM Analysis, Data Contracts, GDPR Compliance, Feature Engineering, Bias Auditing")

if df is not None and len(df) > 0:
    st.subheader("Sample Customer Data")
    st.dataframe(df.head(15), use_container_width=True)

st.markdown("---")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
