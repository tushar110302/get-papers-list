from typing import Optional
import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = [
        "university", "college", "institute", "school", "faculty", "department", "hospital", "center", "labs"
    ]
    return not any(keyword in affiliation.lower() for keyword in academic_keywords)

def is_pharma_or_biotech(affiliation: str) -> bool:
    pharma_keywords = [
        "pharma", "biotech", "therapeutics", "laboratories", "inc", "ltd", "llc", "gmbh", "corp", "company"
    ]
    return any(keyword in affiliation.lower() for keyword in pharma_keywords)

def extract_email(text: str) -> Optional[str]:
    match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
    return match.group(0) if match else None

def clean_affiliation(text):
    # Remove entire "Electronic address: <email>" or "Electronic address <email>" sections
    cleaned = re.sub(r'Electronic address[:\s]*\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b[.;]?', '', text)

    # Also remove any standalone emails elsewhere in the text
    cleaned = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '', cleaned)

    # Remove extra whitespace, semicolons, periods, and clean up the result
    cleaned = re.sub(r'\s+', ' ', cleaned).strip().strip('.;')

    return cleaned


