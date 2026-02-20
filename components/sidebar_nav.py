"""Shared sidebar navigation. Use on all pages for consistent Main/AB Testing/etc labels."""
import streamlit as st


def render_sidebar_nav():
    """Render the consistent navigation sidebar with Main (not app), AB Testing, Survival, etc."""
    with st.sidebar:
        st.markdown("### Navigation")
        st.caption("Select a case study to view governance framework & ROI")

        st.page_link("app.py", label="Main")
        st.page_link("pages/01_AB_Testing.py", label="AB Testing")
        st.page_link("pages/02_Survival.py", label="Survival")
        st.page_link("pages/03_Classification.py", label="Classification")
        st.page_link("pages/04_Segmentation.py", label="Segmentation")
        st.page_link("pages/05_PCA.py", label="Feature Compression")
        st.page_link("pages/06_Rules.py", label="Rules")
        st.page_link("pages/07_Causal.py", label="Causal")
        st.page_link("pages/08_Knowledge_Graph.py", label="Knowledge Graph")
        st.page_link("pages/09_Retrieval.py", label="Retrieval")
        st.page_link("pages/10_Governance.py", label="Governance")
        st.page_link("pages/11_RAG.py", label="RAG")
        st.page_link("pages/12_Agents.py", label="Agents")

        st.markdown("---")
        st.markdown("**Contact**")
        st.markdown("zubiamL4L@gmail.com")
        st.markdown("[LinkedIn](https://linkedin.com/in/zubiamughal)")
        st.markdown("[GitHub](https://github.com/zmugha1)")
