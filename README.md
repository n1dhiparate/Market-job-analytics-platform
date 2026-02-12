## 🔗 Live Demo

👉 https://market-job-analytics-platform.onrender.com/dashboard


🚀 Market Job Analytics Platform

A full-stack data analytics platform for extracting, analyzing, and visualizing job market intelligence using real-world datasets.

📌 Project Vision

The Market Job Analytics Platform is a modular, production-structured analytics system that transforms raw job listing datasets into actionable labor market insights.

It identifies:

# High-demand skills
Technology trends over time
Skill co-occurrence relationships
City & sector-based hiring patterns
Funding-stage hiring correlations

# This project demonstrates practical application of:
Data engineering
Text mining
Exploratory Data Analysis (EDA)
Backend architecture design
Visualization engineering
Modular Flask development

🔎 Core Capabilities

1️⃣ Skill Extraction Engine

Regex-based extraction pipeline
Keyword normalization
Token cleaning
Custom skill dictionary mapping
Case-insensitive parsing
Duplicate elimination

2️⃣ Trend Analysis Module

Frequency aggregation
Time-based grouping
Sector-based filtering
Funding-stage segmentation
Demand ranking system

3️⃣ Skill Co-occurrence Network

Pairwise skill mapping
Graph-based relationship modeling
Weighted edge scoring
Network centrality detection
NetworkX visualization

4️⃣ Interactive Dashboard

Multi-view analytics pages
Visual insights rendering
Modular route-based architecture
Clean Jinja2 templating
Static asset separation

🏗 Architecture Overview

This project follows a modular Flask blueprint pattern with clean separation of concerns.

Market-job-analytics-platform/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   │
│   ├── services/
│   │   ├── skill_extraction.py
│   │   ├── trend_analysis.py
│   │   └── cooccurrence.py
│   │
│   ├── utils/
│   │   ├── data_cleaning.py
│   │   └── helpers.py
│   │
│   ├── templates/
│   └── static/
│
├── data/
├── migrations/
├── run.py
├── requirements.txt
└── README.md

⚙️ Tech Stack

🖥 Backend

Python 3.10+
Flask
Jinja2

📊 Data Processing

Pandas
NumPy
Regex (re module)
Scikit-learn (text utilities)

📈 Visualization

Matplotlib
Seaborn
Plotly
NetworkX

🗄 Database

SQLite (development)

PostgreSQL-ready architecture

🔄 Data Pipeline Flow
Raw CSV Dataset
        ↓
Data Cleaning Module
        ↓
Skill Extraction Engine
        ↓
Aggregation & Trend Computation
        ↓
Co-occurrence Network Builder
        ↓
Visualization Layer
        ↓
Flask Dashboard Rendering

🚀 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/Market-job-analytics-platform.git
cd Market-job-analytics-platform

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
python run.py


Application runs at:

http://127.0.0.1:5000

📊 Analytical Questions This Platform Answers

What are the top 20 in-demand skills this year?
Which technologies dominate fintech vs robotics sectors?
What skills frequently appear together?
Which cities show rising AI demand?
Does funding stage impact tech hiring patterns?

🔮 Future Roadmap

Real-time job scraping integration
Machine learning-based demand prediction
REST API endpoints
Authentication system
Docker containerization
Cloud deployment
CI/CD pipeline integration

👩‍💻 Author

Nidhi Parate
B.Tech Information Technology
Focused on Frontend, Backend Development & Data Analytics

📜 License

This project is built for academic, research, and portfolio purposes.