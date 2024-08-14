from bs4 import BeautifulSoup
from .models import NewsScraped


class GuardianSoup(BeautifulSoup):
    def __init__(self, html: bytes, base_url: str = "https://www.theguardian.com"):
        super().__init__(html, "html.parser")
        self.base_url = base_url

    def get_news_by_subcategory(self):
        urls: list[BeautifulSoup] = self.find_all("a", class_="dcr-lv2v9o")
        urls = [f"https://www.theguardian.com{url['href']}" for url in urls]
        return urls

    def get_detail_news(self, url: str):
        title = self.find(
            "h1", attrs={"class": "dcr-u0152o"}
        )  # class_="dcr-tjsa08" == attrs={"class" : "dcr-tjsa08"}
        title = title.get_text()
        print(title)
        tag_news: list[BeautifulSoup] = self.find_all("li", class_="dcr-ncdwh2")
        tag_news = [t.get_text() for t in tag_news]
        print(tag_news)
        # tag_news: list[BeautifulSoup] = tag_news.find_all("span")[-1].get_text()
        paragraphs: list[BeautifulSoup] = self.find_all("p", class_="dcr-1hirwfs")
        if len(paragraphs) > 0:
            paragraphs = [i.get_text() for i in paragraphs]
            paragraphs = "\n".join(paragraphs)
        else:
            paragraphs: list[BeautifulSoup] = self.find_all("p", class_="dcr-uj7d5w")
            paragraphs = [i.get_text() for i in paragraphs]
            paragraphs = "\n".join(paragraphs)
        authors: list[BeautifulSoup] = self.find_all("a", rel="author")
        authors = [i.get_text() for i in authors]
        try:
            published_time = self.find("span", class_="dcr-u0h1qy").get_text()
        except AttributeError:
            published_time = self.find("div", class_="dcr-1pexjb9").get_text()
        output = NewsScraped(
            title=title,
            tag_news=tag_news,
            paragraphs=paragraphs,
            authors=authors,
            published_time=published_time,
            url=url,
        )
        return output

    def get_news_category(self):
        categories: list[BeautifulSoup] = self.find_all("li", class_="dcr-4hq641")
        categories = [f"{self.base_url}{a.find('a')['href']}" for a in categories]
        print(categories)
        return categories
