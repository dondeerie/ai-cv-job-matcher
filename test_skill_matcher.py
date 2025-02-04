from src.matching.skill_matcher import SkillMatcher

def test_skill_matching():
    print("\nTesting skill matching...")
    
    # Create sample candidate skills
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
        # Initialize matcher
        matcher = SkillMatcher()
        
        # Get match results
        results = matcher.calculate_match(candidate_skills)
        
        # Print results
        print("\nMatch Results:")
        print(f"Total Match Score: {results['total_score']}%")
        
        print("\nCategory Scores:")
        for category, score in results['category_scores'].items():
            print(f"{category}: {score}%")
        
        print("\nMissing Skills:")
        for category, skills in results['missing_skills'].items():
            if skills:
                print(f"\n{category}:")
                for skill in skills:
                    print(f"- {skill}")
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_skill_matching()