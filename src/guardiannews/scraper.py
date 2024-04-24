import requests
import  os

from datetime import datetime
from bs4 import BeautifulSoup
from typing import Optional, Any


# url = "https://www.theguardian.com/ |artanddesign |/2024/apr/24/|  claudette-johnson-art-cotton-capital-nominated-for-turner-prize"


class GuardianSpider(object):
    def __init__(self, category: Optional[str] = None, subcategory: Optional[str] = None):
        self.base_url: str = "https://www.theguardian.com"
        self.category: Optional[str] = category
        self.date: str = datetime.now().strftime("/%Y/%b/%d/")
        self.subcategory: Optional[str] = subcategory

    def get_latest_news(self):
        headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        res = requests.get(os.path.join(self.base_url, "international"), headers=headers)
        print("Site Status Code: ", res.status_code)

        #  response checking
        f = open("response.html", 'w+')
        f.write(res.text)
        f.close()

        # scrape process
        soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

        contents = soup.find("div", attrs={"id": "container-headlines"}).find_all("li")
        for content in contents:
            title: str = content.find("span", attrs={"class": "show-underline"}).text.strip()
            print(title)

    def get_spesific_news(self):
        pass

    def get_news_by_category(self):
        pass

    def get_news_by_subcategory(self):
        pass
