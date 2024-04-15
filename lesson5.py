import requests
from bs4 import BeautifulSoup as BS
url = 'https://mignews.com/mobile'
page = requests.get(url)
# print(page.status_code)
filtered_news = []
all_news = []
soup = BS(page.text, 'html.parser')
# print(soup)
all_news = soup.find_all('article', class_ = 'post mb-2')
# print(all_news)
for data in all_news:
    if data.find('div', class_ = 'text-color-dark'):
        filtered_news.append(data.text)
for data in filtered_news:
    for i in range(1,len(data)):
        if data[i] == '/n':
            data.pop(i)
    print(data)
