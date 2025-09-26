import dataclasses


@dataclasses.dataclass
class NewsModel:
    cover_url: str
    title: str
    description: str
    date: str
    url: str
    content_html: str
