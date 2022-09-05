from selectorlib import Extractor
import requests


class Temperature:


  base_url = 'https://www.timeanddate.com/weather/'
  yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        url = url.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers = self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content



    def get(self):
        pass