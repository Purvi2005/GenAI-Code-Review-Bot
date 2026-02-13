from app.security.rules import SECURITY_PATTERNS
from app.ai.gemini_client import generate_response

def scan_diff(diff_text):
    findings = []

    for issue, patterns in SECURITY_PATTERNS.items():
        for pattern in patterns:
            if pattern in diff_text:
                findings.append(issue)

    if not findings:
        return []

    prompt = f"""
    Classify the severity and impact of the following security findings.
    Output JSON with issue, severity, and explanation.

    Findings: {findings}
    """
    response = generate_response(prompt)
    return response
