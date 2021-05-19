import os

import bs4
import requests

url = 'https://xkcd.com'
# Сохраняем комикс в папке ./xkcd
os.makedirs('../xkcd', exist_ok=True)

while not url.endswith('#'):
    # Загрузка страницы.
    print(f'Загрузка страницы {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # Поиск URL-адреса изображения комикса.
    comic_elem = soup.select('#comic img')
    if not comic_elem:
        print('Не удалось найти изображение комикса.')
    else:
        print(comic_elem)
        comic_url = f"https:{comic_elem[0].get('src')}"

        print(f'Загрузка изображения {comic_url}')
        res = requests.get(comic_url)
        res.raise_for_status()

        # Сохранение изображения в папке ./xkcd под именем значении переменной comic_url.
        image_file = os.path.join('../xkcd', os.path.basename(comic_url))
        with open(image_file, 'wb') as f:
            for chunk in res.iter_content(100_000):
                f.write(chunk)

    # Получение URL-адреса кнопки Prev.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print('Готово.')
