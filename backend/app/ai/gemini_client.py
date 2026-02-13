from google import genai
from app.config import get_settings
import time

settings = get_settings()

client = genai.Client(api_key=settings["GEMINI_API_KEY"])

def generate_response(prompt):
    for _ in range(3):
        try:
            response = client.models.generate_content(
                model="models/gemini-1.5-flash",
                contents=prompt
            )
            return response.text
        except Exception:
            time.sleep(2)
    return "AI review temporarily unavailable due to rate limits."
