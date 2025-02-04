from src.resume_analyzer import ResumeAnalyzer
from pathlib import Path
import os

def test_integrated_analysis():
    print("\nTesting complete resume analysis with sample resumes...")
    
    # Define paths
    BASE_DIR = Path(__file__).parent
    PDF_DIR = BASE_DIR / "data" / "sample_resumes" / "pdf"
    DOCX_DIR = BASE_DIR / "data" / "sample_resumes" / "docx"
    
    try:
        # Test PDF resumes
        print("\nTesting PDF resumes:")
        for pdf_file in PDF_DIR.glob("*.pdf"):
            analyze_resume(pdf_file)
            
        # Test DOCX resumes
        print("\nTesting DOCX resumes:")
        for docx_file in DOCX_DIR.glob("*.docx"):
            analyze_resume(docx_file)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def analyze_resume(file_path: Path):
    """Analyze a single resume file"""
    print(f"\nAnalyzing: {file_path.name}")
    
    try:
        analyzer = ResumeAnalyzer()
        results = analyzer.analyze_resume(file_path)
        
        if "error" in results:
            print(f"Error analyzing {file_path.name}: {results['error']}")
            return
            
        # Print analysis results
        print("\nSkills Found:")
        for category, skills in results["parsed_skills"].items():
            if skills:
                print(f"\n{category}:")
                for skill in skills:
                    print(f"- {skill}")
        
        print(f"\nMatch Score: {results['match_results']['total_score']}%")
        
        print("\nRecommendations:")
        for skill_info in results["recommendations"]["priority_skills"]:
            print(f"\n- {skill_info['skill']} ({skill_info['category']}):")
            print(f"  Priority: {skill_info['priority']}")
            print(f"  Suggestion: {skill_info['learning_path']}")
            
    except Exception as e:
        print(f"Error processing {file_path.name}: {str(e)}")

if __name__ == "__main__":
    test_integrated_analysis()