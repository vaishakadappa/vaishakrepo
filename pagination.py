import re

import requests
from bs4 import BeautifulSoup

root = "https://subslikescript.com"
website = f"{root}/movies"

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")
box = soup.find('article', class_="main-article")

# pagination'
page = soup.find('ul', class_='pagination')
pagination = page.find_all('li', class_='page-item')
last_page = pagination[-2].text
# https://subslikescript.com/movies?page=2

links = []
for pages in range(1, int(last_page) + 1)[:2]:
    website = f"{root}/movies?page={pages}"
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    box = soup.find('article', class_="main-article")

    for link in box.find_all('a', href=True):
        links.append(link['href'])

    print(links)
    for link in links:
        try:
            root = "https://subslikescript.com"
            website = f"{root}/{link}"
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, "lxml")
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            # Remove invalid characters from the title
            clean_title = re.sub(r'[<>:"/\\|?*]', '', title)
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            with open(f"{clean_title}.txt", 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print("---links are not valid ----")
            print(link)
            pass
