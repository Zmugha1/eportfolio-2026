"""Governance Dashboards, Coming soon."""
import streamlit as st

from components.sidebar_nav import render_sidebar_nav

st.set_page_config(page_title="Governance | Zubia Mughal", layout="wide")
render_sidebar_nav()
st.title("Governance Dashboards")
st.info("Case study coming soon.")
if st.button("Back to Portfolio"):
    st.switch_page("app.py")
