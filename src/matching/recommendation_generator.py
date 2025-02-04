from typing import Dict

class RecommendationGenerator:
   def __init__(self):
       self.priority_mapping = {
           "technical_skills": "High",
           "soft_skills": "High", 
           "tools": "Medium"
       }
       
       self.learning_paths = {
           "technical_skills": "Consider online courses or certifications",
           "soft_skills": "Look for practical experience or workshops",
           "tools": "Try hands-on tutorials and documentation"
       }

   def generate_recommendations(self, matching_results: Dict) -> Dict:
       recommendations = {
           "priority_skills": [],
           "strengths": []
       }

       missing_skills = matching_results.get("missing_skills", {})
       
       for category, skills in missing_skills.items():
           priority = self.priority_mapping.get(category, "Medium")
           for skill in skills:
               recommendations["priority_skills"].append({
                   "skill": skill,
                   "category": category,
                   "priority": priority,
                   "learning_path": self.learning_paths[category]
               })
       
       recommendations["priority_skills"].sort(
           key=lambda x: 0 if x["priority"] == "High" else 1
       )

       category_scores = matching_results.get("category_scores", {})
       for category, score in category_scores.items():
           if score >= 75:
               recommendations["strengths"].append({
                   "category": category,
                   "score": score
               })
               
       return recommendations