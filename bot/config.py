import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not DISCORD_TOKEN:
    print("WARNING: DISCORD_TOKEN is not set in environment variables.")

if not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY is not set in environment variables.")
