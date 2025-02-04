# Error Messages and Maintenance Guide

## Common Error Messages and Solutions

### Backend Errors

1. "ModuleNotFoundError: No module named 'src'"
```bash
# Issue: Python can't find the src module
# Solution: Add __init__.py files
touch src/__init__.py
touch src/api/__init__.py
touch src/parsers/__init__.py
touch src/matching/__init__.py
```

2. "Error: Address already in use"
```bash
# Check processes using port
lsof -i :8001

# Kill specific process
kill -9 <PID>
```

3. "Error processing file: Unsupported file format"
```bash
# Verify file extension is .pdf or .docx
# Check file isn't corrupted
# Ensure temp file has correct extension
```

### Frontend Errors

1. "Error: Can't resolve 'web-vitals'"
```bash
cd frontend
npm install web-vitals
```

2. "Failed to compile: Module not found"
```bash
# Reinstall dependencies
rm -rf node_modules
npm install
```

3. "CORS policy: No 'Access-Control-Allow-Origin' header"
```bash
# Verify backend CORS settings include correct port
# Clear browser cache
# Check frontend fetch URL matches backend port
```

4. Tailwind CSS Error
```bash
# Reinstall Tailwind
npm uninstall tailwindcss postcss autoprefixer
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
npx tailwindcss init -p
```

## Maintenance Tasks

### Regular Cleanup

1. Python Cleanup
```bash
# Remove cache files
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Remove temporary files
find . -type f -name "temp*" -delete
find . -type f -name "*.tmp" -delete
```

2. Node/Frontend Cleanup
```bash
# Clean npm cache
npm cache clean --force

# Remove build files
rm -rf frontend/build
rm -rf frontend/node_modules/.cache
```

### Security Updates

1. Backend Updates
```bash
# Check outdated packages
pip list --outdated

# Update all packages
pip install -r requirements.txt --upgrade
```

2. Frontend Updates
```bash
# Check for vulnerabilities
npm audit

# Fix security issues
npm audit fix

# Update packages
npm update
```

### Performance Optimization

1. Backend Profiling
```bash
# Install profiler
pip install memory_profiler

# Profile code
python -m memory_profiler src/api/server.py
```

2. Frontend Optimization
```bash
# Build optimization
npm run build

# Analyze bundle
npm run build -- --stats
```

### Backup Procedures

1. Configuration Backup
```bash
# Backup config files
cp .env .env.backup
cp requirements.txt requirements.backup.txt
cp package.json package.backup.json
```

2. Project Backup
```bash
# Create dated backup
tar -czf ../resume_matcher_backup_$(date +%Y%m%d).tar.gz .
```

### Development Workflow

1. Code Quality
```bash
# Format Python code
pip install black
black src/

# Lint JavaScript
cd frontend
npm run lint
```

2. Testing
```bash
# Python tests
pytest tests/

# React tests
cd frontend
npm test
```

### Recovery Procedures

1. Complete Reset
```bash
# Backend reset
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend reset
cd frontend
rm -rf node_modules
rm package-lock.json
npm install
```

## Best Practices

1. Regular Maintenance Schedule
- Run cleanup scripts weekly
- Check for updates monthly
- Create backups before major changes
- Test both PDF and DOCX uploads regularly

2. Error Monitoring
- Keep terminal outputs for debugging
- Monitor browser console (F12)
- Check server logs regularly
- Document new error patterns

3. Version Control
- Commit changes regularly
- Use meaningful commit messages
- Create feature branches for changes
- Test before merging

4. Performance Monitoring
- Monitor memory usage
- Check response times
- Profile code regularly
- Track file processing times