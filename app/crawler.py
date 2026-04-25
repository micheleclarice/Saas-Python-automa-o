import requests
from bs4 import BeautifulSoup


def crawl(url: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    texts = [p.get_text() for p in soup.find_all("p")]
    return "\n".join(texts)