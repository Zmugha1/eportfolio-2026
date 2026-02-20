"""
Project 5: Feature Store with PCA Compression
Dimensionality reduction for real-time ML with governance
"""

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from components.craig_section import _key_terms_box
from components.sidebar_nav import render_sidebar_nav

st.set_page_config(
    page_title="Feature Compression | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_nav()

# Paths
BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "data"
CSV_PATH = DATA_DIR / "pca_sample_data.csv"
JSON_PATH = DATA_DIR / "pca_governance_log.json"

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

# Fallback values when JSON/CSV fail to load
FALLBACK_GOV = {
    "risk_tier": "Medium",
    "approval": "Data Platform Lead + Model Risk Committee",
    "compression": {
        "original_features": 200,
        "compressed_features": 15,
        "compression_ratio": "15/200",
        "retained_variance": 0.95,
    },
    "performance": {
        "baseline_accuracy": 0.842,
        "compressed_accuracy": 0.856,
        "accuracy_change": "+1.4%",
        "training_speedup": "60x",
        "latency_improvement": "111x",
    },
    "financial": {
        "annual_storage_savings": 462000,
        "compute_savings": 400000,
        "fraud_prevention_value": 2000000,
        "total_annual_value": 2862000,
    },
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
            with open("data/pca_governance_log.json") as f:
                gov = json.load(f)
        except Exception:
            pass
    return df, gov


with st.spinner("Loading PCA governance and sample data..."):
    df, gov = load_data()

if gov is None:
    gov = FALLBACK_GOV

# Header
st.title("Project 5: Feature Store with PCA Compression")
st.markdown("*Dimensionality reduction for real-time ML with governance*")
st.markdown("---")

# Metrics - use fallbacks when loaded values are missing
comp = gov.get("compression") or {}
perf = gov.get("performance") or {}
fin = gov.get("financial") or {}
comp_ratio = comp.get("compression_ratio") or "15/200"
retained = comp.get("retained_variance") or 0.95
speedup = perf.get("training_speedup") or "60x"
total_val = fin.get("total_annual_value") if (fin.get("total_annual_value") or 0) > 0 else 2862000

c1, c2, c3, c4 = st.columns(4)
c1.metric("Risk Tier", gov.get("risk_tier", "Medium"))
c1.caption("Platform Risk")
c2.metric("Compression", comp_ratio)
c2.caption(f"Variance: {retained:.0%}")
c3.metric("Speed Gain", speedup)
c4.metric("Annual Value", f"${total_val/1000000:.1f}M")

st.markdown("---")

# CRAIG Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

with tab1:
    st.subheader("The Feature Avalanche")
    st.write("""
    FinanceCorp had 1,100 features per customer (transaction patterns, demographics, credit scores).
    Models took 18 hours to train, predictions took 5 seconds (too slow for fraud detection),
    and storage cost $50K/month.

    **The Curse of Dimensionality:** With 1,100 dimensions, every customer looked "far away"
    from others. The fraud model thought everyone was an outlier, missing actual fraud.

    **The Breaking Point:** Mobile app needed real-time fraud scores (50ms), but current
    latency was 5 seconds—100x too slow.
    """)

    st.markdown(
        """
        <div style='background-color: #112240; padding: 20px; border-radius: 8px; border-left: 4px solid #8892B0; margin: 20px 0;'>
            <p style='color: #CCD6F6; font-weight: 500; margin: 0;'>Why This Matters: More features ≠ better models. Correlated features waste space, noise drowns signal, and high dimensionality breaks distance-based algorithms.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _key_terms_box("""<b>Dimensionality:</b> Number of variables describing each customer. Like using 1,100 adjectives instead of 10.<br><br>
<b>Curse of Dimensionality:</b> As features increase, data becomes sparse. Models can't find patterns because everything looks unique.<br><br>
<b>Multicollinearity:</b> When features are correlated (e.g., "income" and "spending"), duplicating information.""")

with tab2:
    st.subheader("The Feature Compression Architect")
    st.write("""
    I architected a Feature Store with PCA (Principal Component Analysis)—compressing 200 features
    into 15 "super-features" that capture 95% of the signal, reusable across 12 teams.

    **Why Medium Risk:**
    - Information Loss Risk: Compress too much = miss fraud signals (costly false negatives)
    - Interpretability Crisis: Regulators can't understand "Component_1" vs "income"
    - Pipeline Complexity: 12 teams depend on these features; changes break downstream models

    **Governance Responsibilities:**
    - Prove 95% variance retention (information preservation)
    - Document feature lineage (map compressed features back to originals for audits)
    - Version control (features_v1.2 vs v1.3) to prevent breaking changes
    - Storage SLAs: Reduce costs while maintaining performance
    """)

with tab3:
    st.subheader("Mathematical Magic: Keeping Signal, Removing Noise")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**The Approach**")
        st.write("""
        **Step 1: Correlation Audit** - Found 400 features were highly correlated (99.9% overlap).
        "Income", "Income_lag_0", and "Combo_0" were the same signal repeated.

        **Step 2: PCA Compression** - Like converting 3D object to 2D shadow but keeping outline sharp.
        Found 15 principal components explaining 95% of variance.

        **Step 3: Feature Store** - Centralized repository serving compressed features to 12 teams.
        """)

        st.write("**Redundancy Detected:**")
        st.write("- income ↔ income_lag_0: 99.9% correlated")
        st.write("- income ↔ combo_0: 100% correlated")
        st.write("- Transaction aggregates: 98% correlated")

    with col2:
        st.markdown("**Governance Controls**")
        st.write(f"""
        - **Risk Tier:** {gov.get('risk_tier', 'N/A')}
        - **Approval:** {gov.get('approval', 'N/A')}
        - **Variance Retention:** {retained:.0%} (Threshold: 95%)
        - **Original Features:** {comp.get('original_features', 'N/A')}
        - **Compressed:** {comp.get('compressed_features', 'N/A')}
        """)

        st.write("**Lineage Example (PC1):**")
        st.write("- income: 0.62 weight")
        st.write("- debt_ratio: 0.31 weight")
        st.write("- geographic_risk: 0.18 weight")

    st.markdown("---")
    st.markdown("**Feature Store Architecture**")
    st.code("""
Raw Data Lake (200 features)
    ↓ [PCA Compression]
Feature Store (15 components)
    ↓ [Serving Layer]
Fraud Detection (real-time)
Credit Risk (batch)
Mobile API (50ms latency)
    """)

    _key_terms_box("""<b>PCA:</b> Finds "orthogonal directions" where data varies most. Like rotating a camera to find the best angle showing most detail.<br><br>
<b>Eigenvalue:</b> "Importance score" of each direction. We keep directions with eigenvalues > 1.0.<br><br>
<b>Feature Store:</b> Centralized repository where teams share features (library vs everyone keeping books at home).""")

with tab4:
    st.subheader("From 18 Hours to 18 Minutes")

    m1, m2, m3 = st.columns(3)
    m1.metric("Training Speed", perf.get("training_speedup", "60x"), "faster")
    m2.metric("Latency", perf.get("latency_improvement", "111x"), "faster")
    m3.metric("Accuracy", perf.get("accuracy_change", "+1.4%"), "improved")

    st.write("""
    **Technical Wins:**
    - Training: 18 hours → 18 minutes (60x faster)
    - Prediction: 5 seconds → 45 milliseconds (111x faster)
    - Storage: $50K/month → $8K/month (84% reduction)
    - Accuracy: Actually improved 1.4% (removing noise helped)

    **Business Wins:**
    - Real-time fraud detection now possible in mobile app
    - 12 teams share consistent features (no duplication)
    - Compliance cost down 70% (automated lineage tracking)

    **Governance Win:** When auditors asked "How does Component_12 affect loans?" we showed exact
    mathematical weights mapping back to original features (income: 0.6, debt: 0.3). Full transparency.
    """)

    storage_k = (fin.get("annual_storage_savings") or 462000) / 1000
    compute_k = (fin.get("compute_savings") or 400000) / 1000
    fraud_m = (fin.get("fraud_prevention_value") or 2000000) / 1000000
    st.markdown(
        f"""
        <div style='background-color: #112240; padding: 20px; border-radius: 8px; border-left: 4px solid #8892B0; margin: 20px 0;'>
            <p style='color: #CCD6F6; font-weight: 500; margin: 0;'>ROI: ${total_val/1000000:.1f}M annual value (${storage_k:.0f}K storage + ${compute_k:.0f}K compute + ${fraud_m:.1f}M fraud prevention)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with tab5:
    st.subheader("From Compression to Intelligence")
    st.write("""
    **Current State:** 15 compressed features serving 12 models with full lineage.

    **Next Phase:** Auto-ML Feature Engineering—AI discovers optimal compression.

    **Phase 2 Roadmap:**

    1. **Deep Autoencoders:** Neural networks for non-linear compression (better than PCA for images/text)
    2. **Real-time Computation:** Calculate features on-the-fly via stream processing
    3. **Federated Feature Stores:** Share features across banks without sharing raw data
    4. **Causal Selection:** Compress based on "what causes outcomes" not just correlation

    **The Vision:** A "Feature Cloud" where compression, storage, and serving are automated.
    Data scientists just specify "I need fraud signals" and the system serves optimal features in milliseconds.
    """)

st.markdown("---")
st.caption("Skills: PCA • Dimensionality Reduction • Feature Stores • Eigenvalue Analysis • Data Lineage • MLOps")

if df is not None and len(df) > 0:
    st.subheader("Sample Feature Data")
    st.dataframe(df.head(15), use_container_width=True)

st.markdown("---")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
