import streamlit as st


def project_card(title, description, skills, risk_tier, impact, page_file):
    """Display a project card with risk tier badge"""

    # Risk tier colors
    risk_colors = {
        "Low": "#28a745",
        "Medium": "#ffc107",
        "High": "#dc3545",
    }

    with st.container():
        st.markdown(f"### {title}")
        st.write(description)

        # Risk badge
        color = risk_colors.get(risk_tier, "#6c757d")
        st.markdown(
            f'<span style="background-color: {color}; color: white; padding: 4px 8px; '
            f'border-radius: 12px; font-size: 0.8em;">{risk_tier} Risk</span>',
            unsafe_allow_html=True,
        )

        st.caption(f"**Impact:** {impact}")
        st.caption(f"**Skills:** {skills}")

        if st.button(f"View Case Study", key=title):
            st.switch_page(f"pages/{page_file}")

        st.markdown("---")
