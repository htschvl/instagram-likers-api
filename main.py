import requests
import re
import json

# Função para obter o media_id a partir do shortcode
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
            print("Media ID não encontrado na fonte da página.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o Media ID: {e}")
        return None

# Função para obter a lista de likers
def get_likers(media_id, headers):
    url = f"https://www.instagram.com/api/v1/media/{media_id}/likers/"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        likers = response.json()
        return likers.get('users', [])
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter a lista de likers: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar a resposta JSON: {e}")
        return []

# Função para obter informações de um usuário a partir do user_id
def get_user_info(user_id, headers):
    url = f"https://www.instagram.com/api/v1/users/{user_id}/info/"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        user_info = response.json().get('user', {})
        return user_info.get('full_name', ''), user_info.get('username', '')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter informações do usuário {user_id}: {e}")
        return '', ''
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar a resposta JSON para o usuário {user_id}: {e}")
        return '', ''

# Função principal para coordenar as operações
def main():
    shortcode = input("Digite o shortcode da postagem no Instagram: ")
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-IG-App-ID": "936619743392459",
        "X-CSRFToken": "your_csrf_token_here",  # Substitua com seu CSRF token
        "Cookie": "your_cookie_here"  # Substitua com seus cookies de sessão
    }
    # Passo 2: Obter media_id
    media_id = get_media_id(shortcode)
    
    if media_id:
        print(f"Media ID: {media_id}")
        
        # Passo 3: Obter lista de likers
        likers = get_likers(media_id, headers)
        
        if not likers:
            print("Nenhum liker encontrado ou houve um erro ao obter os likers.")
            return
        
        # Preparar dicionário para armazenar os dados
        user_data = {}
        
        # Passo 4: Obter informações de cada liker
        for liker in likers:
            user_id = liker.get('pk')
            if user_id:
                full_name, username = get_user_info(user_id, headers)
                if full_name and username:
                    user_data[username] = full_name
        
        if user_data:
            # Passo 5: Salvar dados em um arquivo JSON
            with open('likers_info.json', 'w') as json_file:
                json.dump(user_data, json_file, indent=4)
            print("Dados salvos em 'likers_info.json'")
        else:
            print("Não foram obtidas informações válidas dos usuários.")
    else:
        print("Falha ao obter o Media ID.")

if __name__ == "__main__":
    main()
