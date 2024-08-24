import json
import asyncio
import aiohttp
import argparse

async def fetch_json(session, url, headers):
    try:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Erro ao acessar {url}: {e}")
        try:
            error_response = await response.json()
            with open('bad.json', 'w') as bad_file:
                json.dump(error_response, bad_file, indent=4)
            print("Resposta de erro salva em 'bad.json'")
        except:
            pass
        return {}

async def get_likers(session, media_id, headers):
    url = f"https://www.instagram.com/api/v1/media/{media_id}/likers/"
    response = await fetch_json(session, url, headers)
    return response.get('users', [])

async def get_user_info(session, user_id, headers):
    url = f"https://www.instagram.com/api/v1/users/{user_id}/info/"
    response = await fetch_json(session, url, headers)
    user_info = response.get('user', {})
    return user_info.get('full_name', ''), user_info.get('username', '')

async def get_media_id(session, shortcode, headers):
    url = f"https://www.instagram.com/p/{shortcode}/?__a=1&__d=dis"
    response = await fetch_json(session, url, headers)
    items = response.get('items', [])
    if items:
        return items[0].get('pk')  # Obtém o 'pk' que é o media_id
    return None

async def process_shortcode(shortcode, headers):
    async with aiohttp.ClientSession() as session:
        media_id = await get_media_id(session, shortcode, headers)
        if media_id:
            print(f"Media ID encontrado: {media_id}")
            likers = await get_likers(session, media_id, headers)
            user_data = {liker.get('username'): liker.get('full_name') for liker in likers if liker.get('pk')}
            if user_data:
                with open('likers_info.json', 'w') as json_file:
                    json.dump(user_data, json_file)
                print(f"Processo bem-sucedido para {shortcode}.")
            else:
                print(f"Nenhum dado válido encontrado para os likers de {shortcode}.")
        else:
            print(f"Falha ao obter o Media ID para {shortcode}.")

async def main(shortcode=None, test_mode=False):
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    headers = config["headers"]

    if test_mode:
        with open('shortcodes.txt', 'r') as file:
            shortcodes = [line.strip() for line in file.readlines()]
        for sc in shortcodes:
            await process_shortcode(sc, headers)
    else:
        await process_shortcode(shortcode, headers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processa informações de um post do Instagram.')
    parser.add_argument('shortcode', type=str, nargs='?', help='Shortcode da postagem do Instagram')
    parser.add_argument('-t', '--test', action='store_true', help='Executa o script no modo de teste lendo do arquivo shortcodes.txt')
    args = parser.parse_args()

    asyncio.run(main(args.shortcode, test_mode=args.test))
