import pandas as pd
from collections import Counter
import re

def get_work_type_distribution():
    df = pd.read_csv("data/sample_jobs.csv")
    return df["formatted_work_type"].value_counts().to_dict()

def get_top_skills(work_type=None):

    df = pd.read_csv("data/sample_jobs.csv")

    if work_type:
        df = df[df["formatted_work_type"] == work_type]

    descriptions = df["description"].dropna().str.lower()

    skill_keywords = [
        "python", "sql", "java", "aws", "excel",
        "machine learning", "tableau", "power bi",
        "flask", "react", "node", "docker",
        "kubernetes", "azure", "tensorflow",
        "pandas", "numpy"
    ]

    skill_counts = Counter()

    for desc in descriptions:
        for skill in skill_keywords:
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, desc):
                skill_counts[skill] += 1

    return dict(skill_counts.most_common(10)), len(df)
