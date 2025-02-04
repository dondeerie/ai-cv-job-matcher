from typing import Dict, List

class SkillMatcher:
    def __init__(self):
        self.roles = {
            "ai_implementation": {
                "weights": {
                    "technical_skills": 0.5,
                    "soft_skills": 0.3,
                    "tools": 0.2
                },
                "required_skills": {
                    "technical_skills": ["python", "machine learning", "ai", "data analysis"],
                    "soft_skills": ["communication", "project management", "training", "leadership"],
                    "tools": ["git", "sql", "tensorflow", "pytorch"]
                }
            },
            "project_manager": {
                "weights": {
                    "technical_skills": 0.3,
                    "soft_skills": 0.5,
                    "tools": 0.2
                },
                "required_skills": {
                    "technical_skills": [
                        "project planning",
                        "reporting",
                        "process improvement",
                        "risk management",
                        "agile",
                        "analytics"
                    ],
                    "soft_skills": [
                        "leadership",
                        "stakeholder management",
                        "team management",
                        "communication",
                        "problem solving"
                    ],
                    "tools": [
                        "jira",
                        "ms project",
                        "excel",
                        "powerpoint",
                        "confluence"
                    ]
                }
            }
        }

    def calculate_match(self, candidate_skills: Dict[str, List[str]], role: str = "ai_implementation") -> Dict:
        """Calculate match percentage and identify gaps"""
        if role not in self.roles:
            raise ValueError(f"Invalid role: {role}. Available roles: {list(self.roles.keys())}")
            
        role_config = self.roles[role]

        print(f"\n=== Match Calculation Debug ===")
        print(f"Checking skills for role: {role}")
        print(f"Required skills: {role_config['required_skills']}")
        print(f"Candidate skills: {candidate_skills}")

        scores = {}
        missing_skills = {}
        
        # Calculate score for each category
        for category in role_config["required_skills"]:
            required = set(role_config["required_skills"][category])
            candidate = set(candidate_skills.get(category, []))
            
            # Find matching and missing skills
            matches = required.intersection(candidate)
            missing = required - candidate
            
            # Calculate category score
            category_score = len(matches) / len(required) if required else 0
            scores[category] = category_score
            
            # Track missing skills
            if missing:
                missing_skills[category] = list(missing)
        
        # Calculate weighted total score
        total_score = sum(
            scores[category] * role_config["weights"][category]
            for category in scores
        ) * 100
        
        return {
            "role": role,
            "total_score": round(total_score, 2),
            "category_scores": {k: round(v * 100, 2) for k, v in scores.items()},
            "missing_skills": missing_skills
        }