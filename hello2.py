import requests

url = "https://api.artic.edu/api/v1/artworks"
params = {
    "page": 1,
    "limit": 1,
    "fields": "id,title,artist_display,date_display"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    artwork = response.json()["data"][0]
    print(f"🎨 {artwork['title']} by {artwork['artist_display']} ({artwork['date_display']})")
else:
    print("Error:", response.status_code)
