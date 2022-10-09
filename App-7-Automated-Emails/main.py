# api key - f450b62759394d49a40a076cd24f1406
import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass

url = "https://newsapi.org/v2/everything?" \
      "q=andrewtate&" \
      "from=2022-09-10&" \
      "language=en" \
      "&apiKey=f450b62759394d49a40a076cd24f1406"
response = requests.get(url)
content = response.json()
x = content['articles'][1]['title']
pprint(content)
