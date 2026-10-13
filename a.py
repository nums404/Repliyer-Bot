import requests

API_KEY = "GbwSgda0fn-iN3ok5sRhVMZOSsYXCeJO8"
GUILD_ID = "1349906583668396072"
headers = {
    "Authorization": API_KEY
}

offset = 0
user_ids = set()

while True:
    r = requests.get(
        f"https://api.tatsu.gg/v1/guilds/{GUILD_ID}/rankings/all",
        params={"offset": offset},
        headers=headers,
        timeout=15,
    )

    print(r.status_code, r.url)

    if r.status_code != 200:
        print(r.text)
        break

    data = r.json()
    rankings = data.get("rankings", [])

    if not rankings:
        break

    for entry in rankings:
        user_ids.add(entry["user_id"])

    offset += len(rankings)

user_ids = [f"<@{uid}>" for uid in user_ids]

print(user_ids[:10])