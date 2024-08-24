from typing import Dict, Any, List
import aiohttp
import asyncio
from utilis.instagram_api_read import get_likers

async def process_likers_data(media_id: str, headers: Dict[str, str]) -> Dict[str, str]:
    async with aiohttp.ClientSession() as session:
        try:
            likers: List[Dict[str, Any]] = await get_likers(session, media_id, headers)
            processed_data: Dict[str, str] = {liker['username']: liker['full_name'] for liker in likers if 'username' in liker and 'full_name' in liker}
            
            if not processed_data:
                raise ValueError(f"No valid user data found for media_id: {media_id}")
            
            return processed_data
        except Exception as process_error:
            print(f"Error processing likers data for media_id {media_id}: {process_error}")
            return {}

def run_user_processor() -> None:
    test_media_id: str = "1234567890"
    test_headers: Dict[str, str] = {"Authorization": "Bearer token"}
    
    asyncio.run(process_and_display_likers_data(test_media_id, test_headers))

async def process_and_display_likers_data(media_id: str, headers: Dict[str, str]) -> None:
    processed_data: Dict[str, str] = await process_likers_data(media_id, headers)
    print(f"Processed Likers Data: {processed_data}")

if __name__ == "__main__":
    run_user_processor()
