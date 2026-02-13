import requests
from app.config import get_settings

settings = get_settings()

def fetch_pr_diff(diff_url):
    headers = {
        "Authorization": f"Bearer {settings['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3.diff"
    }
    response = requests.get(diff_url, headers=headers)
    return response.text
