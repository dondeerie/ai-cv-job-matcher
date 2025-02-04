from src.matching.skill_matcher import SkillMatcher
from src.matching.recommendation_generator import RecommendationGenerator

def test_recommendations():
    print("\nTesting recommendation generation...")
    
    # Sample candidate skills (using our previous test data)
    candidate_skills = {
        "technical_skills": [
            "python",
            "machine learning",
            "data analysis"
        ],
        "soft_skills": [
            "communication",
            "leadership",
            "project management"
        ],
        "tools": [
            "git",
            "tensorflow"
        ]
    }
    
    try:
        # Get match results
        matcher = SkillMatcher()
        match_results = matcher.calculate_match(candidate_skills)
        
        # Generate recommendations
        recommender = RecommendationGenerator()
        recommendations = recommender.generate_recommendations(match_results)
        
        # Print recommendations
        print("\nRecommendations:")
        print("\nPriority Skills to Develop:")
        for skill_info in recommendations["priority_skills"]:
            print(f"\n- {skill_info['skill']} ({skill_info['category']}):")
            print(f"  Priority: {skill_info['priority']}")
            print(f"  Suggestion: {skill_info['learning_path']}")
        
        print("\nStrengths:")
        for strength in recommendations["strengths"]:
            print(f"- Strong in {strength['category']}: {strength['score']}%")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_recommendations()