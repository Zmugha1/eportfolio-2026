"""
Reusable skills matrix component for Zubia Mughal E-Portfolio.
Displays Hard Skills and Soft Skills with proficiency indicators.
"""

import streamlit as st


HARD_SKILLS = {
    "Governance & MRM": {
        "skills": [
            ("Model Risk Management", "Expert"),
            ("AI Safety & Evaluation", "Expert"),
            ("Statistical Validation", "Expert"),
            ("Fairness Auditing (4/5ths Rule)", "Expert"),
            ("Bias Detection", "Advanced"),
            ("Early Stopping Protocols", "Advanced"),
        ],
    },
    "Machine Learning": {
        "skills": [
            ("Survival Analysis", "Expert"),
            ("Causal Inference", "Expert"),
            ("GraphRAG", "Advanced"),
            ("Experimental Design", "Expert"),
            ("Retrieval Engineering", "Advanced"),
            ("Agent Orchestration", "Advanced"),
            ("Chi-Square Testing", "Expert"),
            ("Power Analysis", "Expert"),
        ],
    },
    "MLOps & Production": {
        "skills": [
            ("Azure ML", "Advanced"),
            ("MLflow", "Expert"),
            ("Vector DBs", "Advanced"),
            ("Feature Stores", "Advanced"),
            ("Drift Detection", "Expert"),
            ("CI/CD for ML", "Advanced"),
            ("Cost Optimization", "Advanced"),
        ],
    },
    "Data Engineering": {
        "skills": [
            ("Advanced SQL (CTEs, Window Functions)", "Expert"),
            ("Data Contracts", "Advanced"),
            ("Lineage", "Advanced"),
            ("ETL Pipeline Design", "Expert"),
        ],
    },
    "Programming": {
        "skills": [
            ("Python (scikit-learn, TensorFlow, LangChain)", "Expert"),
            ("SQL", "Expert"),
            ("Neo4j", "Advanced"),
            ("Power BI", "Advanced"),
        ],
    },
}

SOFT_SKILLS = {
    "Executive Communication": {
        "skills": [
            ("C-Suite presentation", "Expert"),
            ("Board-level risk reporting", "Expert"),
            ("Technical translation to business value", "Expert"),
        ],
    },
    "Governance Leadership": {
        "skills": [
            ("Cross-functional risk management", "Expert"),
            ("Compliance documentation", "Expert"),
            ("Audit trail creation", "Expert"),
            ("Stakeholder approval workflows", "Advanced"),
        ],
    },
    "Decision Intelligence": {
        "skills": [
            ("Experimental design strategy", "Expert"),
            ("Cost-benefit analysis under uncertainty", "Expert"),
            ("Ethics advocacy", "Expert"),
        ],
    },
    "Production Leadership": {
        "skills": [
            ("Incident response", "Expert"),
            ("Rollback decision-making", "Expert"),
            ("24/7 system reliability", "Advanced"),
            ("Team enablement", "Expert"),
        ],
    },
}


def proficiency_badge_class(level: str) -> str:
    """Map proficiency level to CSS class."""
    return {
        "Expert": "proficiency-expert",
        "Advanced": "proficiency-advanced",
        "Intermediate": "proficiency-intermediate",
    }.get(level, "proficiency-intermediate")


def render_skill_category(category: str, skills_data: dict, icon: str = "fa-cog") -> None:
    """Render a skill category as expandable section."""
    with st.expander(f"**{category}**", expanded=(category == "Governance & MRM")):
        skills_html = []
        for skill_name, proficiency in skills_data["skills"]:
            badge_class = proficiency_badge_class(proficiency)
            skills_html.append(
                f'<span class="skill-pill">{skill_name} '
                f'<span class="proficiency-badge {badge_class}">{proficiency}</span></span>'
            )
        st.markdown(
            f'<div class="skill-category"><div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">'
            + " ".join(skills_html)
            + "</div></div>",
            unsafe_allow_html=True,
        )


def skills_matrix() -> None:
    """Render the full skills matrix with Hard and Soft skills."""
    st.markdown(
        '<h2 style="font-family: \'Playfair Display\', serif; color: #64FFDA; margin-bottom: 1.5rem;">'
        '<i class="fa fa-layer-group" style="margin-right: 0.5rem;"></i>Skills Matrix</h2>',
        unsafe_allow_html=True,
    )
    
    st.markdown(
        '<p style="color: #8892B0; margin-bottom: 2rem;">'
        'Governance-first applied research: technical depth meets production pragmatism.</p>',
        unsafe_allow_html=True,
    )
    
    # Hard Skills
    st.markdown(
        '<h3 style="font-family: \'Playfair Display\', serif; color: #E6F1FF; font-size: 1.25rem; margin-bottom: 1rem;">'
        'Hard Skills (Technical)</h3>',
        unsafe_allow_html=True,
    )
    
    for category, data in HARD_SKILLS.items():
        render_skill_category(category, data)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Soft Skills
    st.markdown(
        '<h3 style="font-family: \'Playfair Display\', serif; color: #E6F1FF; font-size: 1.25rem; margin-bottom: 1rem;">'
        'Soft Skills (Leadership & Communication)</h3>',
        unsafe_allow_html=True,
    )
    
    for category, data in SOFT_SKILLS.items():
        render_skill_category(category, data)
