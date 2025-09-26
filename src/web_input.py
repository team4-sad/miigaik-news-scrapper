import requests

from src.base_input import BaseInput


class WebInput(BaseInput):
    def __init__(self, base_url):
        self._page = 1
        self._base_url = base_url
        self._page_id = None

    @property
    def page(self):
        return self._page

    @property
    def base_url(self):
        return self._base_url

    @property
    def url_item_news(self):
        if self._page_id is None:
            raise ValueError("Page id is None")
        return f"{self.base_url}/{self._page_id}"

    @property
    def url(self):
        return f'{self.base_url}?PAGEN_2={self._page}'

    def next_page(self):
        self._page += 1

    def set_page_id(self, page_id):
        self._page_id = page_id

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def fetch_page(self):
        response = requests.get(self.url_item_news)
        response.raise_for_status()
        return response.text
