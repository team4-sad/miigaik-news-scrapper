import abc

from src.news_model import NewsModel


class BaseOutput(abc.ABC):
    def save_one(self, news: NewsModel):
        pass

    def save_many(self, news: list[NewsModel]):
        pass
