from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from src.parsers.resume_parser import ResumeParser
from src.matching.skill_matcher import SkillMatcher
from src.matching.recommendation_generator import RecommendationGenerator
import tempfile
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        print("=== Debug Info ===")
        print(f"Filename: {file.filename}")
        print(f"Content type: {file.content_type}")
        
        # Get the file extension from original filename
        file_extension = Path(file.filename).suffix
        
        # Create temporary file with the correct extension
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            content = await file.read()
            print(f"File size: {len(content)} bytes")
            temp_file.write(content)
            temp_file_path = temp_file.name
            
        print(f"Temp file created at: {temp_file_path}")

        try:
            # Parse resume
            parser = ResumeParser(temp_file_path)
            parsed_data = parser.parse()

            # Match skills
            matcher = SkillMatcher()
            match_results = matcher.calculate_match(parsed_data["skills"])

            # Generate recommendations
            recommender = RecommendationGenerator()
            recommendations = recommender.generate_recommendations(match_results)

            return {
                "success": True,
                "data": {
                    "parsed_skills": parsed_data["skills"],
                    "match_results": match_results,
                    "recommendations": recommendations
                }
            }
        finally:
            # Clean up temp file
            os.unlink(temp_file_path)
            
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return {"success": False, "error": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}