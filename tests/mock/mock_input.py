from src.base_input import BaseInput


class MockInput(BaseInput):
    def __init__(self):
        self._page_id = None
        with open("./tests/mock/res/news.html", mode="r", encoding="utf-8") as file:
            self.mock_content = file.read()
        with open("./tests/mock/res/news_last.html", mode="r", encoding="utf-8") as file:
            self.mock_last_content = file.read()
        with open("./tests/mock/res/news_item.html", mode="r", encoding="utf-8") as file:
            self.mock_item_content = file.read()
        self._page = 1

    def fetch(self):
        if self._page == 1:
            return self.mock_content
        return self.mock_last_content

    def fetch_page(self):
        return self.mock_item_content

    def next_page(self):
        self._page += 1

    def set_page_id(self, page_id):
        self._page_id = page_id

    @property
    def page(self):
        return self._page



