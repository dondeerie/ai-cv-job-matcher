from src.parsers.resume_parser import ResumeParser
from src.parsers.skills_parser import SkillsExtractor
from pathlib import Path

def test_pdf_extraction():
    print("\nTesting enhanced PDF parsing...")
    
    # Define path to the PDF resume
    pdf_path = Path("data/sample_resumes/pdf/alex_taylor_resume.pdf")
    
    try:
        # Parse PDF
        parser = ResumeParser(pdf_path)
        extracted_text = parser.extract_text()
        
        # Extract skills from cleaned text
        skills_extractor = SkillsExtractor()
        skills = skills_extractor.extract_skills(extracted_text)
        
        # Print results
        print("\nExtracted Skills from PDF:")
        for category, found_skills in skills.items():
            if found_skills:
                print(f"\n{category}:")
                for skill in found_skills:
                    print(f"- {skill}")
        
        # Print sample of extracted text for verification
        print("\nSample of extracted text:")
        print(extracted_text[:500] + "...")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_pdf_extraction()