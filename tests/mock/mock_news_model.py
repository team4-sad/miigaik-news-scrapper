from src.news_model import NewsModel


class MockNewsModel(NewsModel):
    def __init__(self):
        super().__init__(
            cover_url="mock_cover_url",
            title="Mock News Model",
            description="mock_news_title",
            url="mock_url",
            date="mock_date",
            content_html="<h1>mock_content_html</h1>"
        )
