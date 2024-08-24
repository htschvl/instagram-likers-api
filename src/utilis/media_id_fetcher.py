from typing import Optional, Dict, Any
import aiohttp
import asyncio
from utilis.http_client import fetch_json
from utilis.json_handler import save_json
from utilis.config_loader import load_config

async def fetch_media_id_by_shortcode(session: aiohttp.ClientSession, shortcode: str) -> Optional[str]:
    try:
        config: Dict[str, Any] = load_config("media_config.json")
        url: str = config['url'].format(shortcode=shortcode)
        headers: Dict[str, str] = config['headers']

        response: Dict[str, Any] = await fetch_json(session, url, headers)

        if "error" in response:
            save_json(response["error"], 'bad_media_id.json')
            raise ValueError(f"Error response received for shortcode {shortcode}, saved to 'bad_media_id.json'.")

        items: Optional[Any] = response.get('items', [])
        if items and isinstance(items, list) and items:
            media_id: Optional[str] = items[0].get('pk')
            if media_id:
                return media_id
        
        raise ValueError(f"'items' not found or invalid in response for shortcode {shortcode}.")

    except (ValueError, KeyError) as specific_error:
        print(f"Specific error: {specific_error}")
        return None
    except Exception as fetch_error:
        print(f"Unexpected error fetching media_id: {fetch_error}")
        return None

def run_fetch_media_id_test() -> None:
    try:
        shortcode: str = "Cxr0F0aL-z0"
        asyncio.run(test_fetch_media_id(shortcode))
    except Exception as test_error:
        print(f"Error during test execution: {test_error}")

async def test_fetch_media_id(shortcode: str) -> None:
    async with aiohttp.ClientSession() as session:
        media_id: Optional[str] = await fetch_media_id_by_shortcode(session, shortcode)
        if media_id:
            print(f"Media ID: {media_id}")
        else:
            print("Failed to obtain Media ID.")

if __name__ == "__main__":
    run_fetch_media_id_test()
