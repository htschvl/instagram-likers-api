import os
from typing import Dict, Any
from dotenv import load_dotenv
from utilis.json_handler import load_json

load_dotenv()

def load_config(config_name: str) -> Dict[str, Any]:
    try:
        config_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../config/{config_name}")
        config: Dict[str, Any] = load_json(config_path)
        
        if not isinstance(config, dict):
            raise ValueError(f"Configuration in file {config_name} is not a valid dictionary.")
        
        csrf_token: str = os.getenv('X_CSRF_TOKEN', '')
        cookie: str = os.getenv('COOKIE', '')
        app_id: str = os.getenv('X_IG_APP_ID', '')
        
        if not csrf_token or not cookie or not app_id:
            raise EnvironmentError("One or more required environment variables are not defined.")
        
        config['headers'].update({
            "X-CSRFToken": csrf_token,
            "Cookie": cookie,
            "X-IG-App-ID": app_id
        })
        
        return config
    
    except FileNotFoundError:
        print(f"Error: Configuration file {config_name} not found.")
        raise
    except ValueError as value_error:
        print(f"Error: {value_error}")
        raise
    except EnvironmentError as env_error:
        print(f"Error: {env_error}")
        raise
    except Exception as load_error:
        print(f"Unknown error loading configuration: {load_error}")
        raise

def test_config_loading() -> None:
    try:
        config: Dict[str, Any] = load_config("media_config.json")
        print("Configuration loaded successfully:")
        print(config)
    except Exception as config_error:
        print(f"Failed to load configuration: {config_error}")

if __name__ == "__main__":
    test_config_loading()
