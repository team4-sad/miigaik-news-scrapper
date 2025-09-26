from src.base_output import BaseOutput
from src.news_model import NewsModel


class MockOutput(BaseOutput):
    def __init__(self):
        self.data = []

    def save_one(self, news: NewsModel):
        self.data.append(news)

    def save_many(self, news: list[NewsModel]):
        self.data.extend(news)