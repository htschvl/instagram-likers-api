import os
import sys
import json
import requests
from typing import Optional

def get_media_id_by_shortcode(shortcode: str) -> Optional[str]:
    config_path = os.path.join(os.path.dirname(__file__), "../config/media_config.json")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    url = config['url'].format(shortcode=shortcode)
    r = requests.get(url, headers=config['headers'])
    
    if r.ok:
        return r.json().get('graphql', {}).get('shortcode_media', {}).get('id')
    return None

if __name__ == "__main__":
    shortcode = sys.argv[1]
    media_id = get_media_id_by_shortcode(shortcode)
    print(media_id or "Error: Unable to retrieve media ID")
