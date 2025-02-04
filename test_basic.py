from src.parsers.skills_parser import SkillsExtractor
from pathlib import Path

def test_basic_functionality():
    print("Starting test...")
    
    try:
        # Initialize skills extractor
        print("Initializing skills extractor...")
        skills_extractor = SkillsExtractor()
        
        # Print loaded skills data to verify it's there
        print("\nLoaded skills categories:")
        for category, skills in skills_extractor.skills_data.items():
            print(f"{category}: {len(skills)} skills loaded")
        
        # Test text with skills we know should be in our skills_data.json
        test_text = """
        I am a Python developer with 5 years of experience in machine learning and artificial intelligence.
        I have led multiple projects using TensorFlow and PyTorch.
        Strong communication and leadership skills with experience in project management.
        Proficient in SQL, data analysis, and deep learning.
        """
        
        print("\nAnalyzing test text...")
        skills = skills_extractor.extract_skills(test_text)
        
        print("\nExtracted Skills:")
        if not any(skills.values()):
            print("No skills were detected - there might be an issue with the matcher")
        else:
            for category, found_skills in skills.items():
                if found_skills:  # only print categories where skills were found
                    print(f"\n{category}:")
                    for skill in found_skills:
                        print(f"- {skill}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise e  # This will show the full error trace

if __name__ == "__main__":
    print("Running test script...")
    test_basic_functionality()
    print("\nTest complete.")