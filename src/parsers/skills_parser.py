import spacy
from typing import List, Dict, Set
from pathlib import Path
import json
from collections import defaultdict

class SkillsExtractor:
    """Extract and analyze skills from resume text"""
    
    def __init__(self):
        # Load spaCy model
        self.nlp = spacy.load("en_core_web_sm")
        self.skills_data = self._load_skills_data()
        
        # Create phrase matcher for multi-word skills
        self.matcher = spacy.matcher.PhraseMatcher(self.nlp.vocab)
        self._setup_skill_patterns()
    
    def _setup_skill_patterns(self):
        """Set up patterns for skill matching"""
        for category, skills in self.skills_data.items():
            patterns = [self.nlp.make_doc(text) for text in skills]
            self.matcher.add(category, patterns)
    
    def _load_skills_data(self) -> Dict:
        """Load and prepare skills data"""
        try:
            skills_path = Path(__file__).parent.parent.parent / "data" / "lookups" / "skills_data.json"
            with open(skills_path) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Skills data file not found. Using empty default.")
            return {
                "technical_skills": [],
                "soft_skills": [],
                "tools": []
            }
    
    def extract_skills(self, text: str) -> Dict[str, List[str]]:
        """
        Extract skills from text using NLP
        Returns categorized skills with context
        """
        doc = self.nlp(text.lower())
        found_skills = defaultdict(set)
        
        # Use phrase matcher for skill identification
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            category = self.nlp.vocab.strings[match_id]
            skill = doc[start:end].text
            found_skills[category].add(skill)
        
        # Convert sets to sorted lists for output
        return {
            category: sorted(list(skills))
            for category, skills in found_skills.items()
        }
    
    def get_skill_context(self, text: str, skill: str, window: int = 10) -> List[str]:
        """
        Extract context around mentioned skills
        Helps understand skill level and experience
        """
        doc = self.nlp(text.lower())
        contexts = []
        
        for token_idx, token in enumerate(doc):
            if token.text in skill.lower():
                start = max(0, token_idx - window)
                end = min(len(doc), token_idx + window)
                context = doc[start:end].text
                contexts.append(context)
                
        return contexts