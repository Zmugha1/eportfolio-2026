"""
Project 1: Governed A/B Testing with MRM
Chi-Square validation, Fairness Auditing, Model Risk Management
"""

import json
from pathlib import Path

import pandas as pd
import streamlit as st
from scipy import stats

from components.craig_section import craig_section

st.set_page_config(
    page_title="Governed A/B Testing | Zubia Mughal",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Paths
BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "data"
CSV_PATH = DATA_DIR / "ab_test_data.csv"
JSON_PATH = DATA_DIR / "governance_log.json"

# Custom CSS
st.markdown(
    """
    <style>
    .metric-card { background: rgba(100, 255, 218, 0.08); border: 1px solid rgba(100, 255, 218, 0.2); 
                  border-radius: 12px; padding: 1rem; margin: 0.5rem 0; }
    .governance-event { border-left: 4px solid #64FFDA; padding-left: 1rem; margin: 0.5rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">',
    unsafe_allow_html=True,
)

# Load data with error handling
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


with st.spinner("Loading A/B test data and governance log..."):
    df, governance = load_data()

if df is None:
    st.error(f"Data file not found: {CSV_PATH}. Please add ab_test_data.csv from Colab.")
    st.stop()

# Header
st.title("Governed A/B Testing with MRM")
st.markdown("*$387K Risk-Adjusted Revenue | Chi-Square | Fairness Auditing | Model Risk Management*")
st.markdown("---")

# CRAIG Section
craig_section(
    context="E-commerce platform needed to validate a new checkout flow (Variant B) before full rollout. "
    "Stakeholders required statistical rigor, fairness checks across segments, and auditable MRM documentation.",
    role="Senior Applied Data Scientist leading experimental design, statistical validation, and governance documentation.",
    action="Designed A/B test with power analysis (0.80), ran Chi-Square tests, applied 4/5ths rule for segment fairness, "
    "created governance log for Model Risk Committee approval.",
    impact="$387K risk-adjusted revenue impact. Zero adverse fairness findings. Full audit trail for compliance.",
    growth="Productionized MRM workflow for future experiments. Template adopted by 3 other product teams.",
)

st.markdown("---")

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Users", f"{len(df):,}")
with col2:
    conv_a = df[df["variant"] == "A"]["conversion"].mean() * 100
    st.metric("Variant A Conv %", f"{conv_a:.2f}%")
with col3:
    conv_b = df[df["variant"] == "B"]["conversion"].mean() * 100
    st.metric("Variant B Conv %", f"{conv_b:.2f}%")
with col4:
    rev_b = df[df["variant"] == "B"]["revenue"].sum()
    st.metric("Variant B Revenue", f"${rev_b:,.0f}")

# Chi-Square Test
st.subheader("Statistical Validation (Chi-Square)")
contingency = pd.crosstab(df["variant"], df["conversion"])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
st.markdown(f"**Chi-Square** = {chi2:.2f} | **p-value** = {p_value:.4f} | **df** = {dof}")
if p_value < 0.05:
    st.success("Statistically significant at α=0.05. Variant B shows significant lift.")
else:
    st.warning("Not statistically significant at α=0.05.")

# Segment fairness (4/5ths rule)
st.subheader("Fairness Audit (4/5ths Rule)")
segment_conv = df.groupby(["segment", "variant"])["conversion"].mean().unstack(fill_value=0)
st.dataframe(segment_conv.style.format("{:.2%}"))

# Governance Log
if governance:
    st.subheader("Model Risk Management Audit Trail")
    for event in governance.get("audit_trail", []):
        st.markdown(
            f"""
            <div class="governance-event">
                <strong>{event['event']}</strong> — {event['actor']}<br>
                <small style="color: #8892B0;">{event['timestamp'][:10]}</small><br>
                {event['details']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Back to portfolio
st.markdown("---")
if st.button("← Back to Portfolio"):
    st.switch_page("app.py")
