from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RESUMES_DIR = DATA_DIR / "resumes"
OUTPUT_DIR = DATA_DIR / "output"

# Ensure directories exist
RESUMES_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# File settings
ALLOWED_RESUME_EXTENSIONS = {'.pdf', '.docx'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Job titles and their weights
JOBS = {
    "ai_implementation_specialist": {
        "title": "AI Implementation Specialist",
        "soft_skills_weight": 0.5,
        "hard_skills_weight": 0.5
    }
}