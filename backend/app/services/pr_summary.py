from app.scaledown.pipeline import scaledown_diff
from app.security.scanner import scan_diff
from app.style.checker import check_style
from app.ranker.ranker import rank_feedback
from app.ai.gemini_client import generate_response

LATEST_REVIEW = {}

def summarize_pr(diff_text, repo=None):
    reduced_diff = scaledown_diff(diff_text)
    security_report = scan_diff(diff_text)
    style_report = check_style(diff_text)
    ranked_feedback = rank_feedback(security_report, style_report)

    prompt = f"""
    You are a senior software engineer.
    Provide a concise pull request review.

    Compressed Diff:
    {reduced_diff}

    Priority Feedback:
    {ranked_feedback}
    """

    summary = generate_response(prompt)

    if repo:
        LATEST_REVIEW["repo"] = repo
        LATEST_REVIEW["summary"] = summary
        LATEST_REVIEW["issues"] = ranked_feedback.split("\n")[:3]
        LATEST_REVIEW["time_saved"] = 70

    return summary
