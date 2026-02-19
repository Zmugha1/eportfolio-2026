"""Case Study: Survival Analysis for Churn."""

import streamlit as st

st.set_page_config(page_title="Survival Analysis | Zubia Mughal", layout="wide")
st.title("Survival Analysis for Churn")
st.markdown("*Time-to-Event, Censored Data, Cox PH*")
st.info("Case study content coming soon. 22% improvement in retention prediction.")
if st.button("← Back to Portfolio"):
    st.switch_page("app.py")
