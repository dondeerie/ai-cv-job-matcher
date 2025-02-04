from src.parsers.resume_parser import ResumeParser
from pathlib import Path
import pytest

def test_text_extraction():
    """Test the basic text extraction functionality"""
    print("\nTesting resume parsing...")
    
    # Test with sample text first
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
    
    # Initialize parser
    try:
        parser = ResumeParser("dummy_path")
        # Temporarily set the text directly for testing
        parser.text = test_text
        
        # Parse the text
        result = parser.parse()
        
        # Print results
        print("\nExtracted Skills:")
        for category, skills in result["skills"].items():
            if skills:
                print(f"\n{category}:")
                for skill in skills:
                    print(f"- {skill}")
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_text_extraction()