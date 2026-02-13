from app.ai.gemini_client import generate_response

def rank_feedback(security_report, style_report):
    prompt = f"""
    You are an AI review prioritization engine.

    Rank the following findings by:
    1. Severity
    2. Impact
    3. Fix urgency

    Remove low-value noise.
    Return only the top 3 issues with brief explanations.

    Security Findings:
    {security_report}

    Style & Performance Findings:
    {style_report}
    """
    return generate_response(prompt)
