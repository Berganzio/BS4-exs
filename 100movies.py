from bs4 import BeautifulSoup
import requests


response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
html_text = response.text

soup = BeautifulSoup(html_text, 'html.parser')
print(soup.prettify())
title = soup.find_all(name='h3', class_='title')
movies_names = [name.getText() for name in title]
reversed_names = movies_names[::-1]
with open('movies_names.txt', encoding='utf-8', mode='w') as file:
    for name in reversed_names:
        file.write(f"{name}\n")
