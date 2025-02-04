from typing import Dict, List

class SkillMatcher:
    def __init__(self):
        self.weights = {
            "technical_skills": 0.5,
            "soft_skills": 0.3,
            "tools": 0.2
        }
        self.required_skills = {
            "technical_skills": ["python", "machine learning", "ai"],
            "soft_skills": ["communication", "leadership", "project management"],
            "tools": ["git", "docker", "tensorflow"]
        }

    def calculate_match(self, candidate_skills: Dict[str, List[str]]) -> Dict:
        scores = {}
        missing_skills = {}
        
        for category in self.required_skills:
            required = set(self.required_skills[category])
            candidate = set(candidate_skills.get(category, []))
            
            matches = required.intersection(candidate)
            missing = required - candidate
            
            scores[category] = len(matches) / len(required) if required else 0
            if missing:
                missing_skills[category] = list(missing)

        total_score = sum(scores[cat] * self.weights[cat] for cat in scores) * 100

        return {
            "total_score": round(total_score, 2),
            "category_scores": {k: round(v * 100, 2) for k, v in scores.items()},
            "missing_skills": missing_skills
        }