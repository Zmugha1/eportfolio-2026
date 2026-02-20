# Zubia Mughal E-Portfolio 2026

Professional Streamlit e-portfolio targeting **Senior IC-3/Manager roles** ($160K-$200K). Decision Intelligence Architect, bridging $4.6M business impact with auditable AI.

## Installation

```bash
git clone https://github.com/Zmugha1/eportfolio-2026.git
cd eportfolio-2026
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run main.py
```

Opens at `http://localhost:8501`.

**Streamlit Cloud:** Set `main.py` as the main file in your app settings.

## Project Structure

```
├── main.py                    # Main landing page
├── .streamlit/
│   └── config.toml           # Theme (navy/teal)
├── pages/
│   ├── 01_AB_Testing.py      # AB Testing with MRM
│   ├── 02_Survival.py
│   ├── 03_Classification.py
│   ├── 04_Segmentation.py
│   ├── 05_PCA.py
│   ├── 06_Rules.py
│   ├── 07_Causal.py
│   ├── 08_Knowledge_Graph.py
│   ├── 09_Retrieval.py
│   ├── 10_Governance.py
│   ├── 11_RAG.py
│   └── 12_Agents.py
├── data/
│   ├── ab_test_data.csv      # 12,000 user A/B test dataset
│   └── governance_log.json   # MRM audit trail
├── components/
│   ├── __init__.py
│   ├── skills_matrix.py      # Hard/Soft skills display
│   └── craig_section.py      # Context/Role/Action/Impact/Growth
├── static/
│   └── style.css            # Custom styling
└── requirements.txt
```

## Contact

**zubiamL4L@gmail.com** | [LinkedIn](https://www.linkedin.com/in/zubiamughal) | [GitHub](https://github.com/Zmugha1)

MRM standards aligned with Burtch Works 2026 AI Governance research.
