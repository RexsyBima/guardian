from guardiannews.models import NewsScraped
import pandas as pd
from guardiannews.requests_custom import CustomRequests
from guardiannews.soup import GuardianSoup
import datetime


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
        for url in news_url[0:2]:
            print(url)
            try:
                html = custom_requests.get_html(url)
                soup = GuardianSoup(html)
                data = soup.get_detail_news(url)
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
    main()
    # debug_per_news_url()
