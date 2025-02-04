from pathlib import Path
from typing import Union
import os
from config.settings import ALLOWED_RESUME_EXTENSIONS, MAX_FILE_SIZE

def validate_file(file_path: Union[str, Path]) -> bool:
    """
    Validate if the file is acceptable for processing
    Returns True if valid, False otherwise
    """
    file_path = Path(file_path)
    
    # Check if file exists
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check extension
    if file_path.suffix.lower() not in ALLOWED_RESUME_EXTENSIONS:
        raise ValueError(f"Invalid file type. Allowed types: {ALLOWED_RESUME_EXTENSIONS}")
    
    # Check file size
    if os.path.getsize(file_path) > MAX_FILE_SIZE:
        raise ValueError(f"File too large. Maximum size: {MAX_FILE_SIZE/1024/1024}MB")
    
    return True

def ensure_directory(directory: Union[str, Path]) -> Path:
    """
    Ensure a directory exists and create it if it doesn't
    Returns Path object
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    return directory