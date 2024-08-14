from pydantic import BaseModel


class NewsScraped(BaseModel):
    title: str
    tag_news: list[str]
    paragraphs: str
    authors: list
    published_time: str
    url: str
