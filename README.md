# Sensitive Data Leak Detector for Cloud Storage

Detects sensitive information (Aadhaar, PAN, emails, and password disclosures) in uploaded files and assigns a severity level (Low/Medium/Critical). Includes a simple CLI, sample test files, and auto-generated reports/screenshots for your presentation.

## Features
- Regex-based detection for **Aadhaar**, **PAN**, **Email**, **Password leak phrases**.
- Per-file findings with **severity classification**.
- Auto-generates a **CSV report** and **JSON report**.
- Creates a **severity chart** and **sample results table** image for your slides.
- Ready for extension to PDFs/DOCX and a Flask UI.

## Quick Start
```bash
# 1) Create & activate virtual environment (optional)
python3 -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install requirements
pip install -r requirements.txt

# 3) Run the scanner on the bundled sample data
python app.py --input data --outdir screenshots
```

## How It Works
1. Load files from `--input` folder.
2. Extract text (TXT supported by default).
3. Run regex patterns to detect Aadhaar, PAN, emails, and password phrases.
4. Compute severity:
   - **Critical**: Contains Aadhaar or PAN.
   - **Medium**: Password phrases found or >= 3 emails.
   - **Low**: Anything else with any detection; **None** if no findings.
5. Save `results.csv`, `results.json`, and charts to `--outdir`.

## Extend
- Add PDF/DOCX parsing by installing `pypdf2` / `python-docx` and updating `utils.py:extract_text()`.
- Wrap the CLI in Flask for a simple web UI.

## Project Structure
```
sensitive-data-leak-detector/
├── README.md
├── requirements.txt
├── app.py
├── utils.py
├── data/
│   ├── sample_leak_1.txt
│   ├── sample_leak_2.txt
│   └── sample_clean.txt
└── screenshots/  # auto-generated charts and images
```

## License
MIT
