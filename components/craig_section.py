import streamlit as st


def _key_terms_box(html_content: str) -> None:
    """Render Key Terms callout with dark theme, uniform font and color."""
    st.markdown(
        f"""
        <div style='background-color: #112240; padding: 20px; border-radius: 8px; border-left: 4px solid #8892B0; margin: 20px 0; font-family: Inter, -apple-system, sans-serif;'>
            <p style='color: #CCD6F6; font-weight: 500; margin-bottom: 10px; font-size: 0.9em; text-transform: uppercase; letter-spacing: 0.1em;'>Key Terms Explained</p>
            <div style='color: #CCD6F6; font-size: 0.95em; line-height: 1.6; font-weight: 400;'>
                {html_content}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_craig(context, role, action, impact, growth, key_terms=None, action_code=None):
    """Display CRAIG framework with narrative storytelling and Key Terms callouts.
    key_terms: dict mapping tab names to HTML content for Key Terms boxes
    action_code: optional SQL/code block for Action tab
    """
    st.markdown(
        """
        <style>
        .stTabs [data-baseweb="tab"] { color: #CCD6F6 !important; }
        .stTabs [aria-selected="true"] { color: #CCD6F6 !important; border-color: #8892B0 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context", "Role", "Action", "Impact", "Growth"])

    with tab1:
        st.subheader("The Business Problem")
        st.write(context)
        if key_terms and "context" in key_terms:
            _key_terms_box(key_terms["context"])

    with tab2:
        st.subheader("Decision Intelligence Architect")
        st.write(role)
        if key_terms and "role" in key_terms:
            _key_terms_box(key_terms["role"])

    with tab3:
        st.subheader("Technical Implementation & Governance Controls")
        st.write(action)
        if action_code:
            st.code(action_code, language="sql")
        if key_terms and "action" in key_terms:
            _key_terms_box(key_terms["action"])

    with tab4:
        st.subheader("Business Outcomes & Risk Mitigation")
        st.write(impact)
        if key_terms and "impact" in key_terms:
            _key_terms_box(key_terms["impact"])

    with tab5:
        st.subheader("Next Iteration: Bayesian Optimization")
        st.write(growth)
        if key_terms and "growth" in key_terms:
            _key_terms_box(key_terms["growth"])


def craig_section(context, role, action, impact, growth, key_terms=None, action_code=None):
    """CRAIG framework display with Key Terms callout boxes."""
    show_craig(context, role, action, impact, growth, key_terms, action_code)
