"""
Reusable project card component for Zubia Mughal E-Portfolio.
Displays project preview with business impact, skill tags, and risk tier badge.
"""

import streamlit as st


def project_card(
    project_num: int,
    title: str,
    impact_hook: str,
    skill_tags: list[str],
    risk_tier: str,
    page_link: str,
) -> None:
    """
    Render a project card with governance-focused metadata.
    
    Args:
        project_num: Project number (1-12)
        title: Project title
        impact_hook: One-line business impact statement
        skill_tags: List of skill/tech tags (pills)
        risk_tier: "Low", "Medium", or "High"
        page_link: Streamlit page route (e.g., "Project_1")
    """
    risk_class = {
        "Low": "risk-low",
        "Medium": "risk-medium",
        "High": "risk-high",
    }.get(risk_tier, "risk-medium")
    
    with st.container():
        st.markdown(
            f"""
            <div class="project-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
                    <span style="font-family: 'Playfair Display', serif; font-size: 0.9rem; color: #64FFDA;">Project {project_num}</span>
                    <span class="risk-badge {risk_class}">{risk_tier} Risk</span>
                </div>
                <h4 style="font-family: 'Playfair Display', serif; color: #E6F1FF; margin-bottom: 0.5rem;">{title}</h4>
                <p style="font-size: 0.9rem; color: #8892B0; margin-bottom: 1rem; line-height: 1.5;">{impact_hook}</p>
                <div style="margin-bottom: 1rem;">
                    {" ".join([f'<span class="skill-pill">{tag}</span>' for tag in skill_tags])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        if st.button(f"View Case Study →", key=f"project_{project_num}", type="primary"):
            st.switch_page(f"pages/{page_link}.py")
