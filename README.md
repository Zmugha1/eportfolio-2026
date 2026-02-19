# Zubia Mughal E-Portfolio 2026

Professional multi-page Streamlit e-portfolio targeting **Senior IC-3/Manager roles** ($160K-$200K). Showcases Decision Intelligence expertise with emphasis on **AI Governance** and **Model Risk Management (MRM)**.

## Differentiator

> *"I bridge $4.6M business impact with auditable, production-safe AI systems."*

## Setup

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Zmugha1/eportfolio-2026.git
cd eportfolio-2026

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Project Structure

```
eportfolio-2026/
├── app.py                 # Main landing page
├── components/
│   ├── skills_matrix.py   # Skills visualization (Hard + Soft)
│   └── project_card.py   # Project preview component
├── pages/
│   ├── 0_Contact.py      # Hire Me / Contact
│   └── 1_*.py ... 12_*.py  # Project case studies
├── static/
│   └── style.css        # Custom premium styling
├── requirements.txt
└── README.md
```

## Brand Specifications

- **Colors**: Deep Navy (#0A192F), Teal Accent (#64FFDA), White Text (#E6F1FF), Light Gray (#F8F9FA)
- **Typography**: Inter (body), Playfair Display (headers)
- **Tone**: Governance-first Applied Researcher

## Sections

1. **Hero** – Headline, tagline, stats (23 years, $4.6M, 92K hours, 12 systems)
2. **Skills Matrix** – Hard skills (Governance & MRM, ML, MLOps, Data Eng, Programming) + Soft skills (Executive Comms, Governance Leadership, Decision Intelligence, Production Leadership)
3. **Project Gallery** – 12 projects with business impact, skill tags, risk tier badges
4. **About** – Bio, location, contact
5. **Footer** – LinkedIn, GitHub, Email, Resume, MRM disclaimer

## Deployment

- **Streamlit Community Cloud**: Connect this repo for one-click deploy
- **Docker**: Use `streamlit run app.py` as the entrypoint

## License

Portfolio content © Zubia Mughal. Demonstrates MRM standards aligned with Burtch Works 2026 AI Governance research.
