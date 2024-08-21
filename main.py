from src.models import NewsScraped
import pandas as pd
from src.requests_custom import CustomRequests
from src.soup import GuardianSoup
import datetime
from src.utils import insert_to_db, check_news_exist, insert_to_db2, check_news_exist2


def save_xlsx(input_: list[NewsScraped], filename: str = "output.xlsx"):
    input_ = [i.model_dump() for i in input_]
    time = datetime.datetime.now().strftime("%d-%B-%Y-%H-%M")
    df = pd.DataFrame(input_)
    df.to_excel(f"{time}-{filename}")
    # "14agustus2024-output.xlsx"


def main():
    output = []
    custom_requests = CustomRequests()
    url = "https://www.theguardian.com/international"
    news_categories = GuardianSoup(custom_requests.get_html(url)).get_news_category()
    for category in news_categories:
        news_url = GuardianSoup(
            custom_requests.get_html(category)
        ).get_news_by_subcategory()
        for url in news_url[0:10]:
            print(f"accessing : {url}")
            if check_news_exist(url):
                print(f"url {url} already scraped, skipping")
            else:
                try:
                    html = custom_requests.get_html(url)
                    soup = GuardianSoup(html)
                    data = soup.get_detail_news(url)
                    insert_to_db(data)
                    output.append(data)
                except AttributeError:
                    print(f"error accessing {url}, HTML structure may be different")
                    pass
    save_xlsx(output)


def main2():
    output = []
    custom_requests = CustomRequests()
    url = "https://www.theguardian.com/international"
    news_categories = GuardianSoup(custom_requests.get_html(url)).get_news_category()
    for category in news_categories:
        news_url = GuardianSoup(
            custom_requests.get_html(category)
        ).get_news_by_subcategory()
        for url in news_url[0:10]:
            print(f"accessing : {url}")
            if check_news_exist2(url):
                print(f"url {url} already scraped, skipping")
            else:
                try:
                    html = custom_requests.get_html(url)
                    soup = GuardianSoup(html)
                    data = soup.get_detail_news(url)
                    insert_to_db2(data)
                    output.append(data)
                except AttributeError:
                    print(f"error accessing {url}, HTML structure may be different")
                    pass
    save_xlsx(output)


def debug_per_news_url():
    custom_requests = CustomRequests()
    url = "https://www.theguardian.com/technology/2024/aug/12/susan-wojcicki-obituary"
    soup = GuardianSoup(custom_requests.get_html(url, True)).get_detail_news(url)
    print(soup)


if __name__ == "__main__":
    # print(
    #    check_news_exist(
    #        "https://www.theguardian.com/world/article/2024/aug/20/police-in-kenya-say-serial-killer-suspect-has-escaped-from-custodyasdasdwasd"
    #    )
    # )
    # main()
    main2()
    # debug_per_news_url()
