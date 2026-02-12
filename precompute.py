import pandas as pd
import json

df = pd.read_csv("data/sample_jobs.csv")

skill_keywords = [
    "python", "sql", "java", "aws", "excel",
    "machine learning", "tableau", "power bi",
    "flask", "react", "node", "docker",
    "kubernetes", "azure", "tensorflow",
    "pandas", "numpy"
]

skill_counts = {}

for desc in df["description"].dropna().str.lower():
    for skill in skill_keywords:
        if skill in desc:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

# Save top 10
top_skills = dict(sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:10])

work_type_distribution = df["formatted_work_type"].value_counts().to_dict()

data = {
    "top_skills": top_skills,
    "work_type_distribution": work_type_distribution,
    "total_jobs": len(df)
}

with open("data/precomputed.json", "w") as f:
    json.dump(data, f)

print("Precomputed data saved.")
