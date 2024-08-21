from requests import Session


class CustomRequests(Session):
    def __init__(self) -> None:
        super().__init__()

    def get_html(self, url: str, savemode: bool = False) -> bytes:
        html = self.get(url).content
        if savemode:
            with open("output.html", "wb") as f:
                f.write(html)
        return html

    def get_status_code(self, url: str) -> int:
        return self.get(url).status_code
