from fastapi import FastAPI, HTTPException
from services.github_api import fetch_gists

app = FastAPI(title="GitHub Gists API")

@app.get("/{user}")
async def get_gists(user: str):
    gists = await fetch_gists(user)
    if gists is None:
        raise HTTPException(status_code=500, detail="Unable to fetch gists")
    return gists