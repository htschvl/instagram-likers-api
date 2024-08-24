import requests

r = requests.get("https://www.instagram.com/p/CxURF0aL-i2/?__a=1&__d=dis", headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)"})
if r.ok: open('response.html', 'w').write(r.text); print(r.json()['graphql']['shortcode_media']['id'])
