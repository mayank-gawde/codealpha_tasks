# CodeAlpha Language Translation Tool

A beginner-friendly web app that translates text between supported languages.

## Features
- Source and target language selection
- Translation output in a separate text area
- Handles empty input and common translation errors
- Simple Streamlit interface

## Run on Windows
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
5. Start the app:
   ```powershell
   streamlit run app.py
   ```

The app opens in your browser. An internet connection is required for translation.
