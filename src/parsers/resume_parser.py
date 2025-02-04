from pathlib import Path
import PyPDF2
import docx
from typing import Dict, Union

class ResumeParser:
    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)
        self.text = ""
        self.parsed_data = {
            "skills": {
                "technical_skills": [],
                "soft_skills": [],
                "tools": []
            }
        }
        # Move skill_patterns to be a class attribute
        self.skill_patterns = {
            "technical_skills": [
                # AI Implementation Skills
                "python", "machine learning", "ai", "artificial intelligence",
                "data analysis", "deep learning", "sql", "programming",
                # Project Manager Skills
                "project planning", "reporting", "process improvement",
                "risk management", "agile", "analytics", "scrum",
                "project delivery", "budget management"
            ],
            "soft_skills": [
                # Common Skills
                "leadership", "communication", "project management",
                # Project Manager Specific
                "stakeholder management", "team management",
                "problem solving", "mentoring", "team leadership",
                "agile methodologies", "cross-functional"
            ],
            "tools": [
                # AI Tools
                "tensorflow", "pytorch", "git", "docker", "github",
                # PM Tools
                "jira", "ms project", "excel", "powerpoint",
                "confluence", "slack", "microsoft project"
            ]
        }

    def parse(self) -> Dict:
        self.text = self.extract_text().lower()  # Convert to lowercase for better matching
        
        print("\n=== Parsed Text Sample ===")
        print(self.text[:200])
        
        print("\n=== Looking for Skills ===")
        print("Searching for these skills:")
        for category, skills in self.skill_patterns.items():
            print(f"{category}: {skills}")
        
        # Look for skills in the text
        for category, skills in self.skill_patterns.items():
            for skill in skills:
                if skill in self.text:
                    self.parsed_data["skills"][category].append(skill)
                    print(f"Found {category}: {skill}")
        
        print("\n=== Skills Found Summary ===")
        for category, skills in self.parsed_data["skills"].items():
            print(f"{category}: {skills}")
        
        return self.parsed_data

    def extract_text(self) -> str:
        print(f"Extracting text from file: {self.file_path}")
        print(f"File suffix: {self.file_path.suffix.lower()}")
        print(f"File exists: {self.file_path.exists()}")
        
        if self.file_path.suffix.lower() == '.pdf':
            print("Detected PDF file, attempting to extract...")
            return self._extract_from_pdf()
        elif self.file_path.suffix.lower() == '.docx':
            print("Detected DOCX file, attempting to extract...")
            return self._extract_from_docx()
        
        raise ValueError(f"Unsupported file format: {self.file_path.suffix}. Please provide PDF or DOCX file.")

    def _extract_from_pdf(self) -> str:
        try:
            print(f"Opening PDF file: {self.file_path}")
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = []
                for page in reader.pages:
                    # Extract and clean text from each page
                    page_text = page.extract_text()
                    # Remove extra whitespace and normalize
                    page_text = ' '.join(page_text.split())
                    text.append(page_text)
                    
                full_text = ' '.join(text)
                print("Successfully extracted text from PDF")
                print(f"Extracted {len(full_text)} characters")
                return full_text
        except Exception as e:
            print(f"Error reading PDF: {str(e)}")
            raise

    def _extract_from_docx(self) -> str:
        doc = docx.Document(self.file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text