import requests
from bs4 import BeautifulSoup


URL_CURRENCY_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE&aqs=chrome.1.69i57j0i67i131i433i650j0i67i131i433i457i650j0i67i131i433i650j0i67i650l2j0i402i650l2j0i433i512j0i67i650.3058j1j7&sourceid=chrome&ie=UTF-8"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


class Currency:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    def get_price(self):
        page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        result = soup.find_all("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
        price = result[0].text
        return price.replace(",", ".")
