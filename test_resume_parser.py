from src.parsers.resume_parser import ResumeParser
from src.parsers.skills_parser import SkillsExtractor
from pathlib import Path
import pytest

def test_skills_extraction():
    """Test the skills extraction directly without file parsing"""
    print("\nTesting skills extraction from resume text...")
    
    # Test with sample text
    test_text = """
    JOHN DOE
    Python Developer
    
    EXPERIENCE
    Senior Developer | TechCorp
    - Led machine learning projects using TensorFlow
    - Implemented deep learning solutions
    - Managed team of 5 developers
    
    SKILLS
    - Python, SQL, Machine Learning
    - Project Management
    - Team Leadership
    """
    
    # Use skills extractor directly
    try:
        skills_extractor = SkillsExtractor()
        skills = skills_extractor.extract_skills(test_text)
        
        # Print results
        print("\nExtracted Skills:")
        for category, found_skills in skills.items():
            if found_skills:
                print(f"\n{category}:")
                for skill in found_skills:
                    print(f"- {skill}")
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_skills_extraction()