import os
from dotenv import load_dotenv

load_dotenv()

def get_settings():
    return {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")
    }
