# api key - f450b62759394d49a40a076cd24f1406
import requests
from pprint import pprint


class NewsFeed:


    base_url = "https://newsapi.org/v2/everything?"
    api_key = "f450b62759394d49a40a076cd24f1406"


    def __init__(self, interest, from_date, to_date, language='en'):

        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"q={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}" \
              f"&apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='Biden', from_date='2022-10-18', to_date='2022-10-19', language='en')
    print(news_feed.get())


