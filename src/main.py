from guardiannews.scraper import GuardianSpider

spider: GuardianSpider = GuardianSpider()

if __name__ == '__main__':
    spider.get_latest_news()