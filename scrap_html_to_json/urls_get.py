import requests
from bs4 import BeautifulSoup


# url_short, url_pages - ввести актуальные urls
from url_info import url_short, url_pages

# сбор ссылок на страницы, получаем urls страниц
# количество страниц
pages = 2
for i in range(1, pages+1):
    # при изменении url, проверить формат строки
    url = f'{url_pages}{i}'

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    q = requests.get(url, headers=headers)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')

    with open('urls_new.txt', 'a') as f:
        for tag in soup.findAll('a'):
            url_new = tag.get('href')
            url_new = url_short + url_new

            f.writelines(url_new + '\n')