import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "precomputed.json")

with open(DATA_PATH) as f:
    data = json.load(f)

def get_top_skills(work_type=None):
    return data["top_skills"], data["total_jobs"]

def get_work_type_distribution():
    return data["work_type_distribution"]
