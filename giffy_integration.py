import requests
import random

def get_gif(giffy_token, giffy_phrase):

    headers = {}
    url_string = "http://api.giphy.com/v1/gifs/search?q=" + giffy_phrase + "&api_key=" + giffy_token
    resp = requests.get(url_string, headers=headers, verify=False)
    resp = resp.json()
    max = len(resp["data"])
    min = 0
    random_number = random.randint(min, max+1)
    return resp["data"][random_number]["images"]["downsized"]["url"];
