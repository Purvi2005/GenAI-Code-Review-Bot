from fastapi import APIRouter, Body
from app.github.utils import fetch_pr_diff
from app.github.commenter import post_pr_comment
from app.services.pr_summary import summarize_pr

router = APIRouter()

@router.post("/webhook")
async def github_webhook(payload: dict = Body(...)):
    if "pull_request" not in payload:
        return {"status": "ignored"}

    pr = payload["pull_request"]
    diff_url = pr["diff_url"]
    repo = payload["repository"]["full_name"]
    pr_number = pr["number"]

    diff_text = fetch_pr_diff(diff_url)
    summary = summarize_pr(diff_text, repo)


    post_pr_comment(repo, pr_number, summary)

    return {
        "status": "commented",
        "repo": repo,
        "pr": pr_number
    }
