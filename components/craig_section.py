"""
Reusable CRAIG (Context/Role/Action/Impact/Growth) display component.
Executive consulting-style expandable tabs or cards.
"""

import streamlit as st


def craig_section(
    context: str,
    role: str,
    action: str,
    impact: str,
    growth: str,
) -> None:
    """
    Render a CRAIG-style section with expandable tabs.
    
    Args:
        context: Business/situation context
        role: Role played
        action: Actions taken
        impact: Business impact delivered
        growth: Learning/growth outcome
    """
    st.markdown(
        '<h4 style="font-family: \'Playfair Display\', serif; color: #64FFDA; margin-bottom: 1rem;">'
        '<i class="fa fa-layer-group" style="margin-right: 0.5rem;"></i>CRAIG Framework</h4>',
        unsafe_allow_html=True,
    )
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Context", "Role", "Action", "Impact", "Growth"]
    )
    
    with tab1:
        st.markdown(f"**Context**")
        st.markdown(context)
    
    with tab2:
        st.markdown(f"**Role**")
        st.markdown(role)
    
    with tab3:
        st.markdown(f"**Action**")
        st.markdown(action)
    
    with tab4:
        st.markdown(f"**Impact**")
        st.markdown(impact)
    
    with tab5:
        st.markdown(f"**Growth**")
        st.markdown(growth)
