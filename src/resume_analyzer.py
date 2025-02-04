from pathlib import Path
from typing import Dict, Union

from .parsers.resume_parser import ResumeParser
from .matching.skill_matcher import SkillMatcher
from .matching.recommendation_generator import RecommendationGenerator

class ResumeAnalyzer:
    """Main class to coordinate resume analysis process"""
    
    def __init__(self):
        self.matcher = SkillMatcher()
        self.recommender = RecommendationGenerator()
    
    def analyze_resume(self, file_path: Union[str, Path]) -> Dict:
        """
        Analyze resume and provide complete results
        """
        try:
            # Parse resume
            parser = ResumeParser(file_path)
            parsed_data = parser.parse()
            
            # Match skills
            match_results = self.matcher.calculate_match(parsed_data["skills"])
            
            # Generate recommendations
            recommendations = self.recommender.generate_recommendations(match_results)
            
            # Combine results
            analysis_results = {
                "parsed_skills": parsed_data["skills"],
                "match_results": match_results,
                "recommendations": recommendations
            }
            
            return analysis_results
            
        except Exception as e:
            return {
                "error": str(e),
                "status": "failed"
            }