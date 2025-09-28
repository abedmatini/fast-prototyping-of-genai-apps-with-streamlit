# Quick MVP Setup Guide

To start a Minimum Viable Product (MVP) quickly, make sure you have these files and directories:


## Required Files & Directories
- `app.py` — Main application file
- `requirements.txt` — List your Python dependencies
- `.env` — Store environment variables (API keys, secrets, etc.)
- `data/` — Directory for your data files

## Quick File/Directory Creation Commands
Run these in your project folder:

```bash
mkdir data
touch app.py requirements.txt .env
echo "streamlit" > requirements.txt
```

## Recommended Setup Steps
1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate your virtual environment:
   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your code to `app.py` and data to `data/` as needed.

---
This setup helps you start building and testing your MVP right away.