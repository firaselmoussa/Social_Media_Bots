import requests
import json


def getQuote():
    url = "https://zenquotes.io/api/quotes/"

    response = requests.request("GET", url)
    response = json.loads(response.text)

    quote = response[0]['q']
    author = response[0]['a']

    return quote, author
