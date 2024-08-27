import requests
import re
import json

def get_media_id(shortcode):
    url = f"https://www.instagram.com/p/{shortcode}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
        
        html = response.text
        media_id_match = re.search(r'"media_id":"(\d+)"', html)
        
        if media_id_match:
            return media_id_match.group(1)
        else:
            return None
    except requests.exceptions.RequestException as e:

        return None