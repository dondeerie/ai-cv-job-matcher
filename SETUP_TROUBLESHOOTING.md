# Setup and Troubleshooting Guide

## Starting the Application

### 1. Start Backend Server
```bash
# Navigate to project directory
cd /path/to/resume_matcher

# Activate virtual environment
source venv/bin/activate

# Start backend server
uvicorn src.api.server:app --reload --port 8001
```

### 2. Start Frontend Server
```bash
# In a new terminal
cd /path/to/resume_matcher/frontend

# Start frontend
npm start
```

## Verification Steps

### 1. Backend Health Check
```bash
# Using curl in terminal
curl http://localhost:8001/health

# Expected response:
{"status":"healthy"}
```

### 2. Frontend Verification
- Open browser to http://localhost:3000 or http://localhost:3001
- Verify:
  - Role selection dropdown appears
  - File upload section is visible
  - UI styling is applied correctly

### 3. Full System Check
1. Upload test resume
2. Check backend terminal for parsing logs
3. Verify results display
4. Test both PDF and DOCX formats

## Common Issues and Solutions

### 1. Port and Server Issues

#### Port Already in Use
```bash
# Check what's using the port
lsof -i :8001

# Kill process(es) using the port (replace XXXX with PID number)
kill -9 XXXX

# If multiple processes, can kill all at once
kill -9 PID1 PID2
```

#### Server Won't Start
```bash
# Check if Python environment is active
which python

# Should show path to your venv Python
# If not, activate virtual environment
source venv/bin/activate
```

### 2. File Upload Issues

#### File Upload Fails
1. Check file size (should be < 5MB)
2. Verify file extension (.pdf or .docx)
3. Check backend logs for parsing errors
4. Verify temp directory has write permissions

#### Parse Errors
1. Check file is not corrupted
2. Try converting PDF to DOCX or vice versa
3. Check backend logs for specific error messages

### 3. Frontend Issues

#### npm Start Fails
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules
rm package-lock.json
npm install
```

#### UI Rendering Issues
1. Clear browser cache
2. Check console for CSS/JS errors
3. Verify Tailwind installation:
```bash
# Reinstall Tailwind
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

#### CORS Issues
1. Verify backend CORS settings
2. Check frontend fetch URL matches backend port
3. Clear browser cache and cookies
4. Try incognito/private browsing mode

### 4. Backend Issues

#### spaCy Model Issues
```bash
# Reinstall spaCy and download model
pip uninstall spacy
pip install spacy
python -m spacy download en_core_web_sm
```

#### PDF/DOCX Processing Issues
```bash
# Reinstall processing libraries
pip uninstall PyPDF2 python-docx
pip install PyPDF2 python-docx
```

## Environment Setup Issues

### 1. Virtual Environment Problems
```bash
# Remove and recreate virtual environment
deactivate  # if active
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Node Version Issues
```bash
# Check Node version
node --version

# Should be v14+ for React
# If using nvm, switch version:
nvm use 14  # or higher
```

## Debugging Steps

### 1. Backend Debugging
1. Check logs in backend terminal
2. Verify file paths and permissions
3. Test endpoints with curl:
```bash
# Health check
curl http://localhost:8001/health

# File upload (replace path)
curl -X POST -F "file=@/path/to/test.pdf" http://localhost:8001/analyze-resume
```

### 2. Frontend Debugging
1. Open browser dev tools (F12)
2. Check:
   - Console for JavaScript errors
   - Network tab for API calls
   - React DevTools for component state

### 3. Full System Debug
1. Clear all cached data:
```bash
# Frontend
npm cache clean --force
rm -rf node_modules/.cache

# Backend
rm -rf __pycache__
```

2. Restart everything:
   - Close all terminals
   - Kill all Python processes
   - Clear browser cache
   - Start fresh

## Maintenance Tasks

### Regular Updates
```bash
# Update Python packages
pip freeze > requirements.txt
pip install -r requirements.txt --upgrade

# Update npm packages
npm update
```

### System Cleanup
```bash
# Clean Python cache
find . -type d -name "__pycache__" -exec rm -r {} +

# Clean npm cache
npm cache clean --force
```

## Notes
- Keep terminal outputs for debugging
- Document any new issues and solutions
- Update requirements.txt after adding packages
- Test with multiple file formats regularly