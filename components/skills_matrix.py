import streamlit as st


def skills_matrix():
    """Display hard and soft skills in organized sections"""

    st.header("🎯 Technical Skills & Governance Expertise")

    # Hard Skills
    with st.expander("🔧 Hard Skills (Click to Expand)", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Governance & MRM")
            st.markdown("""
            - Model Risk Management (MRM)
            - AI Safety & Evaluation
            - Statistical Validation
            - Fairness Auditing (4/5ths Rule)
            - Bias Detection
            - Early Stopping Protocols
            """)

            st.subheader("Machine Learning")
            st.markdown("""
            - Survival Analysis
            - Causal Inference
            - GraphRAG & Vector Search
            - Experimental Design (A/B Testing)
            - Retrieval Engineering
            - Agent Orchestration
            """)

        with col2:
            st.subheader("MLOps & Production")
            st.markdown("""
            - Azure ML & MLflow
            - Vector DBs (Pinecone/Chroma)
            - Feature Stores
            - Drift Detection
            - CI/CD for ML
            - Cost Optimization
            """)

            st.subheader("Data Engineering")
            st.markdown("""
            - Advanced SQL (CTEs, Windows)
            - Data Contracts & Lineage
            - ETL Pipeline Design
            - Neo4j Graph DB
            - Power BI
            """)

    # Soft Skills
    with st.expander("💼 Soft Skills & Leadership", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Executive Communication")
            st.markdown("""
            - C-Suite presentations
            - Board-level risk reporting
            - Technical translation to business value
            - Stakeholder management
            """)

            st.subheader("Governance Leadership")
            st.markdown("""
            - Cross-functional risk management
            - Compliance documentation
            - Audit trail creation
            - Approval workflow design
            """)

        with col2:
            st.subheader("Decision Intelligence")
            st.markdown("""
            - Experimental design strategy
            - Cost-benefit analysis
            - Ethics & fairness advocacy
            - Production decision-making
            """)

            st.subheader("System Leadership")
            st.markdown("""
            - Incident response
            - Rollback decision-making
            - 24/7 system reliability
            - Team enablement
            """)
