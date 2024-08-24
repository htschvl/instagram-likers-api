from typing import Dict, Any, List, Optional
import aiohttp
import asyncio
from utilis.http_client import fetch_json

async def get_likers(session: aiohttp.ClientSession, media_id: str, headers: Dict[str, str]) -> List[Dict[str, Any]]:
    try:
        url: str = f"https://www.instagram.com/api/v1/media/{media_id}/likers/"
        response: Dict[str, Any] = await fetch_json(session, url, headers)
        users: Optional[List[Dict[str, Any]]] = response.get('users', [])

        if not users:
            raise ValueError(f"No users found for media_id: {media_id}")
        
        return users
    except Exception as get_likers_error:
        print(f"Error retrieving likers: {get_likers_error}")
        return []

async def test_get_likers() -> None:
    async with aiohttp.ClientSession() as session:
        media_id: str = "1234567890"
        headers: Dict[str, str] = {"Authorization": "Bearer token"}
        likers: List[Dict[str, Any]] = await get_likers(session, media_id, headers)
        print(f"Likers: {likers}")

if __name__ == "__main__":
    asyncio.run(test_get_likers())
