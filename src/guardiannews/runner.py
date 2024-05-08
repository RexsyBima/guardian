# use for run program
import os

from .scraper import GuardianSpider

class Run(object):
    def __init__(self):
        self.spider: GuardianSpider = GuardianSpider()

    def scrape_category(self):
        soup = self.spider.get_response(os.path.join(self.spider.base_url, "international"))
        categories = self.spider.get_category(soup)
        print(categories)

