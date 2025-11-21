import json, re
from pathlib import Path

SKILLS = json.loads(Path("data/skills_dict.json").read_text())

def extract_skills(text):
    text_low = (text or "").lower()
    found = set()
    
    for skill, keywords in SKILLS.items():
        for kw in keywords:
            if re.search(rf"\b{re.escape(kw)}\b", text_low):
                found.add(skill)
                break
    return list(found)
