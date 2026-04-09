import httpx

async def fetch_gists(user: str):
    url = f"https://api.github.com/users/{user}/gists"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            #if response.status_code == 200:
            return response.json()
            #return None
    except Exception as e:
        print(f"Error fetching gists for user {user}: {e}")
        return response.json()