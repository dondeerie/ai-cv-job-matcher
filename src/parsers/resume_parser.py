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

    def parse(self) -> Dict:
        self.text = self.extract_text().lower()  # Convert to lowercase for better matching
        
        print("Extracted text, looking for skills...")
        
        # Define some basic skills to look for
        skill_patterns = {
            "technical_skills": [
                "python", "machine learning", "ai", "artificial intelligence",
                "data analysis", "deep learning", "sql", "programming"
            ],
            "soft_skills": [
                "leadership", "communication", "project management",
                "team", "training", "presentation"
            ],
            "tools": [
                "tensorflow", "pytorch", "git", "docker", "github",
                "jira", "kubernetes"
            ]
        }
        
        # Look for skills in the text
        for category, skills in skill_patterns.items():
            for skill in skills:
                if skill in self.text:
                    self.parsed_data["skills"][category].append(skill)
                    print(f"Found {category}: {skill}")
        
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