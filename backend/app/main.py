from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.github.webhook import router as github_router
from app.services.pr_summary import LATEST_REVIEW

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(github_router)

@app.get("/latest-review")
def latest_review():
    if not LATEST_REVIEW:
        return {
            "repo": "No PR reviewed yet",
            "summary": "Trigger a GitHub PR to see review",
            "issues": [],
            "time_saved": 0
        }
    return LATEST_REVIEW
