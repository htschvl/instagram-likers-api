import aiohttp
import os
from typing import Dict, Any
from utilis.json_handler import save_json, load_json

def load_client_config(filename: str) -> Dict[str, Any]:
    try:
        config: Dict[str, Any] = load_json(filename)
        if not isinstance(config, dict):
            raise ValueError(f"Configuration in file {filename} is not a valid dictionary.")
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file {filename} not found.")
        raise
    except ValueError as value_error:
        print(f"Error: {value_error}")
        raise
    except Exception as load_error:
        print(f"Unknown error loading configuration: {load_error}")
        raise

async def fetch_json(session: aiohttp.ClientSession, url: str, headers: Dict[str, str]) -> Dict[str, Any]:
    try:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientError as client_error:
        print(f"Error accessing {url}: {client_error}")
        try:
            error_response: Dict[str, Any] = await response.json()
            save_json(error_response, 'bad_response.json')
            return {"error": error_response}
        except Exception as process_error:
            print(f"Error processing error response: {process_error}")
        return {"error": str(client_error)}
    except Exception as fetch_error:
        print(f"Unknown error fetching JSON from {url}: {fetch_error}")
        return {"error": str(fetch_error)}

def test_client_configuration() -> None:
    try:
        config_file: str = os.path.join(os.path.dirname(__file__), '../../config/client_config.json')
        client_config: Dict[str, Any] = load_client_config(config_file)
        print("Client configuration loaded successfully.")
    except Exception as config_error:
        print(f"Failed to load client configuration: {config_error}")

if __name__ == "__main__":
    test_client_configuration()
