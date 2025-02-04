from typing import Dict

class RecommendationGenerator:
    """Generate personalized recommendations based on skill gaps"""
    
    def __init__(self):
        # Role-specific priority mappings
        self.role_priorities = {
            "ai_implementation": {
                "technical_skills": "High",
                "soft_skills": "High",
                "tools": "Medium"
            },
            "project_manager": {
                "technical_skills": "Medium",
                "soft_skills": "High",
                "tools": "Medium"
            }
        }
        
        # Role-specific learning paths
        self.role_learning_paths = {
            "ai_implementation": {
                "technical_skills": "Consider AI/ML courses or certifications",
                "soft_skills": "Look for implementation and training opportunities",
                "tools": "Practice with AI/ML frameworks and tools"
            },
            "project_manager": {
                "technical_skills": "Take project management certification courses",
                "soft_skills": "Focus on leadership and stakeholder management training",
                "tools": "Get hands-on experience with PM tools and methodologies"
            }
        }

    def generate_recommendations(self, matching_results: Dict) -> Dict:
        """Generate role-specific recommendations"""
        role = matching_results.get("role", "ai_implementation")
        
        recommendations = {
            "priority_skills": [],
            "strengths": [],
            "role_specific_advice": []
        }
        
        # Get role-specific configurations
        priorities = self.role_priorities.get(role, self.role_priorities["ai_implementation"])
        learning_paths = self.role_learning_paths.get(role, self.role_learning_paths["ai_implementation"])
        
        # Generate priority skills
        missing_skills = matching_results.get("missing_skills", {})
        for category, skills in missing_skills.items():
            priority = priorities.get(category, "Medium")
            for skill in skills:
                recommendations["priority_skills"].append({
                    "skill": skill,
                    "category": category,
                    "priority": priority,
                    "learning_path": learning_paths[category]
                })
        
        # Sort by priority
        recommendations["priority_skills"].sort(
            key=lambda x: 0 if x["priority"] == "High" else 1
        )
        
        # Identify strengths
        category_scores = matching_results.get("category_scores", {})
        for category, score in category_scores.items():
            if score >= 75:
                recommendations["strengths"].append({
                    "category": category,
                    "score": score
                })
        
        # Add role-specific advice
        if role == "project_manager":
            recommendations["role_specific_advice"].append(
                "Focus on demonstrating concrete project outcomes and metrics"
            )
        elif role == "ai_implementation":
            recommendations["role_specific_advice"].append(
                "Highlight hands-on experience with AI/ML implementations"
            )
        
        return recommendations