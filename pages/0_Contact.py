"""Contact page - Hire Me / Open to Opportunities."""

import streamlit as st

st.set_page_config(page_title="Contact | Zubia Mughal", layout="wide")
st.title("Open to Opportunities")
st.markdown("**Senior IC (Staff/Principal) or Manager roles** | Milwaukee, WI (Remote preferred)")
st.markdown("📧 **zubiamL4L@gmail.com**")
st.markdown("[LinkedIn](https://www.linkedin.com/in/zubiamughal) | [GitHub](https://github.com/Zmugha1)")
if st.button("← Back to Portfolio"):
    st.switch_page("app.py")
