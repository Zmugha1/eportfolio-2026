"""Case Study: Governed A/B Testing with MRM."""

import streamlit as st

st.set_page_config(page_title="Governed A/B Testing | Zubia Mughal", layout="wide")
st.title("Governed A/B Testing with MRM")
st.markdown("*Chi-Square validation, Fairness Auditing, Model Risk Management*")
st.info("Case study content coming soon. $180K incremental revenue impact.")
if st.button("← Back to Portfolio"):
    st.switch_page("app.py")
