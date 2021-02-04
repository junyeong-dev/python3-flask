import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&pg=1"

# 마지막 페이지를 가져옴
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pager = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pager)
    last_page = pager[-2].get_text(strip=True)
    return int(last_page)
