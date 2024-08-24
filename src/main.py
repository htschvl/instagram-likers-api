from typing import Dict, Any, Optional, List
import aiohttp
import asyncio
from utilis.config_loader import load_config
from utilis.media_id_fetcher import fetch_media_id_by_shortcode
from utilis.instagram_api_read import get_likers
from utilis.json_handler import save_json

async def fetch_and_process_likers(shortcode: str) -> None:
    try:
        config: Dict[str, Any] = load_config("media_config.json")
        async with aiohttp.ClientSession() as session:
            media_id: Optional[str] = await fetch_media_id_by_shortcode(session, shortcode)
            if not media_id:
                print("Failed to obtain Media ID.")
                return
            
            likers: List[Dict[str, Any]] = await get_likers(session, media_id, config['headers'])
            if not likers:
                print("No likers found for the media.")
                return
            
            # Formatar os dados dos likers
            formatted_data: Dict[int, Dict[str, str]] = {}
            sorted_likers = sorted(likers, key=lambda liker: liker['username'])
            for index, liker in enumerate(sorted_likers, start=1):
                username = liker.get('username', 'unknown')
                full_name = liker.get('full_name', 'unknown')
                formatted_data[index] = {username: full_name}
            
            # Salvar os dados formatados usando o JSON handler
            save_json(formatted_data, 'likers_info.json')
            print("Likers info saved successfully.")
    
    except Exception as process_error:
        print(f"Error in processing likers: {process_error}")

def run_main_flow() -> None:
    shortcode: str = "C4RIDmqxC4X"  # Exemplo de shortcode
    asyncio.run(fetch_and_process_likers(shortcode))

if __name__ == "__main__":
    run_main_flow()
