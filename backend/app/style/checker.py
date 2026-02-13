from app.style.rules import STYLE_PATTERNS
from app.ai.gemini_client import generate_response

def check_style(diff_text):
    issues = []

    for issue, patterns in STYLE_PATTERNS.items():
        for pattern in patterns:
            if pattern in diff_text:
                issues.append(issue)

    if not issues:
        return []

    prompt = f"""
    Analyze the following code style and performance issues.
    Provide improvement suggestions in bullet points.

    Issues: {issues}
    """
    return generate_response(prompt)
