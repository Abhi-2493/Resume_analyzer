import pandas as pd

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_PATH = os.path.join(BASE_DIR, "data", "skills.csv")

skills = pd.read_csv(SKILL_PATH)["skill"].tolist()


def extract_skills(text):
    found = []
    for skill in skills:
        if skill.lower() in text:
            found.append(skill)
    return list(set(found))
