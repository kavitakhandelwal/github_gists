import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_gists_octocat():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/octocat")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "url" in data[0]
    assert "files" in data[0]
