from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Prevent CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Google Apps Script URL
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzbYX-duK81hsoQ3Xfsdj0X8u76a6SeyBbW2V2mToVq99axSf9UT2hxqV35HIe8w3OQjQ/exec"

@app.get("/api/data")
async def get_website_content():
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(GOOGLE_SCRIPT_URL)
        return response.json()
