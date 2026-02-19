import streamlit as st


def show_craig(context, role, action, impact, growth):
    """Display CRAIG framework (Context, Role, Action, Impact, Growth)"""

    tabs = st.tabs(["🎯 Context", "👤 Role", "⚡ Action", "💰 Impact", "📈 Growth"])

    with tabs[0]:
        st.markdown("### The Business Problem")
        st.write(context)

    with tabs[1]:
        st.markdown("### My Role")
        st.write(role)

    with tabs[2]:
        st.markdown("### Technical Implementation")
        st.write(action)

    with tabs[3]:
        st.markdown("### Measurable Results")
        st.write(impact)

    with tabs[4]:
        st.markdown("### Next Iteration")
        st.write(growth)


# Alias for backward compatibility with 01_project_ab_testing.py
def craig_section(context, role, action, impact, growth):
    """Alias for show_craig - CRAIG framework display"""
    show_craig(context, role, action, impact, growth)
