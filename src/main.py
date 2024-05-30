from guardiannews.runner import Run
from guardiannews.models import NewsScraped
from guardiannews.scraper import GuardianSpider
import pandas as pd
runner = Run()

def save_xlsx(input_ : list[NewsScraped]):
    input_ = [i.model_dump() for i in input_]
    df = pd.DataFrame(input_)
    df.to_excel("output.xlsx")


if __name__ == '__main__':
    #runner.scrape_category()
    scraper = GuardianSpider()
    urls = scraper.get_news_by_subcategory("https://www.theguardian.com/uk-news")
    output = []
    print(len(urls))

    for url in urls[0:5]:
        try:
            item = scraper.get_detail_news(url)
            output.append(item)
        except AttributeError:
            print(f"{url} cant be scraped, may have different html structure ")
    save_xlsx(output)
    
    
    """
    while True:
        url = input("url : ")
    #url = "https://www.theguardian.com/world/article/2024/may/30/all-eyes-on-rafah-how-ai-generated-image-spread-across-social-media"
        output = scraper.get_detail_news(url)
        print(output)
        """
        
    