import requests
import json

try:
    with open("./config.json") as rawJson:
        config = json.loads(rawJson.read())
except:
    print("Unable to read config json")
    exit()

quote = requests.get("https://api.quotable.io/random").json()

try:
    requests.patch(
        "https://discord.com/api/v9/users/@me/settings", json={
            'custom_status': {'text': f'"{quote["content"]}" - {quote["author"]}'}
        }, headers={'authorization': config["token"]})
except Exception as error:
    print(error)
finally:
    print("Done")
