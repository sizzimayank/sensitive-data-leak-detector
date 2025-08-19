
import re
from pathlib import Path

AADHAAR_RE = re.compile(r"(?:^|\D)(\d{4}\s?\d{4}\s?\d{4})(?:\D|$)")
PAN_RE = re.compile(r"\b([A-Z]{5}[0-9]{4}[A-Z])\b")
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PASSWORD_PHRASE_RE = re.compile(r"\b(password|pwd|passcode)\b\s*[:=]?", re.IGNORECASE)

def extract_text(path: Path) -> str:
    p = Path(path)
    if p.suffix.lower() in {".txt", ""}:
        try:
            return p.read_text(errors="ignore")
        except Exception:
            return ""
    # Placeholder for PDF/DOCX extension in future
    return ""

def detect(text: str):
    aadhaar = AADHAAR_RE.findall(text)
    pan = PAN_RE.findall(text)
    emails = EMAIL_RE.findall(text)
    pwd_hint = bool(PASSWORD_PHRASE_RE.search(text))
    return {
        "aadhaar": aadhaar,
        "pan": pan,
        "emails": emails,
        "password_phrase": pwd_hint,
    }

def severity(findings) -> str:
    if findings["aadhaar"] or findings["pan"]:
        return "Critical"
    if findings["password_phrase"] or len(findings["emails"]) >= 3:
        return "Medium"
    if findings["emails"]:
        return "Low"
    return "None"
