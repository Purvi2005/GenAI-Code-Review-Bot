import requests
from app.config import get_settings

settings = get_settings()

def post_pr_comment(repo_full_name, pr_number, comment):
    url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {settings['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json"
    }
    payload = {"body": comment}
    requests.post(url, headers=headers, json=payload)
