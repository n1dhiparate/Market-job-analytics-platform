import os
import pandas as pd
from collections import Counter
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample_jobs.csv")

# ✅ Load ONCE
df_global = pd.read_csv(DATA_PATH)

skill_keywords = [
    "python", "sql", "java", "aws", "excel",
    "machine learning", "tableau", "power bi",
    "flask", "react", "node", "docker",
    "kubernetes", "azure", "tensorflow",
    "pandas", "numpy"
]

def get_top_skills(work_type=None):

    df = df_global

    if work_type:
        df = df[df["formatted_work_type"] == work_type]

    descriptions = df["description"].dropna().str.lower()

    skill_counts = Counter()

    for desc in descriptions:
        for skill in skill_keywords:
            if skill in desc:   # simpler than regex
                skill_counts[skill] += 1

    return dict(skill_counts.most_common(10)), len(df)


def get_work_type_distribution():
    return df_global["formatted_work_type"].value_counts().to_dict()
