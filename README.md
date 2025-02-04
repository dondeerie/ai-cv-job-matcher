# AI CV Job Matcher

An AI-powered CV analysis tool that matches CVs against job descriptions, focusing on AI Implementation Specialist roles. Built with Python (FastAPI) for backend and React for frontend.

## Features
- CV Analysis (PDF & DOCX support)
- Skill Extraction & Matching
- Job Role Matching
- Match Score Generation
- Personalized Recommendations
- Modern Web Interface

## Tech Stack

### Backend
- Python with FastAPI
- spaCy for Natural Language Processing
- PyPDF2 and python-docx for file processing

### Frontend
- React
- Tailwind CSS
- Modern JavaScript

## Prerequisites
- Python 3.x
- Node.js and npm
- Git

## Setup and Installation

### Backend Setup

1. Clone repository and create virtual environment:
```bash
git clone https://github.com/dondeerie/ai-cv-job-matcher.git
cd ai-cv-job-matcher
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install fastapi uvicorn python-multipart python-docx PyPDF2 spacy
python -m spacy download en_core_web_sm
```

3. Start backend server:
```bash
uvicorn src.api.server:app --reload --port 8001
```

### Frontend Setup

1. Navigate to frontend directory and install dependencies:
```bash
cd frontend
npm install
```

2. Start frontend development server:
```bash
npm start
```

## Usage

1. Ensure both servers are running:
   - Backend: http://localhost:8001
   - Frontend: http://localhost:3000
2. Open web interface at http://localhost:3000
3. Upload CV in PDF or DOCX format
4. View match score, skills analysis, and recommendations

## Common Issues & Solutions

### Backend Issues
- Port 8001 already in use: Choose different port using `--port` flag
- Missing dependencies: Rerun pip install commands
- Virtual environment not active: Remember to activate using source command

### Frontend Issues
- Port 3000 in use: React will suggest alternative port
- Node modules missing: Run `npm install`
- Build errors: Check console for specific error messages

## Project Structure
```
ai-cv-job-matcher/
├── src/                # Backend source code
│   ├── api/           # FastAPI server
│   ├── parsers/       # CV parsing logic
│   └── matching/      # Matching algorithms
├── frontend/          # React frontend
│   ├── src/          # Frontend source
│   └── public/       # Static files
└── data/             # Sample data & resources
```

## Notes
- PDF and DOCX files may show slight variations in results
- Both servers must be running for full functionality
- Recommended file size: < 5MB
- Current version focuses on AI Implementation Specialist role

## Contributing
1. Fork repository
2. Create feature branch
3. Submit pull request

## License
MIT License - feel free to use and modify for your purposes!