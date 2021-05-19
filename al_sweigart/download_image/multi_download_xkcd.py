import os
import threading

import bs4
import requests

url = 'https://xkcd.com'
# Сохраняет комикс в папке ./xkcd
os.makedirs('xkcd', exist_ok=True)


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Загрузка страницы.
        url_number = f'https://xkcd.com/{url_number}'
        print(f'Загрузка страницы {url_number}...')
        res = requests.get(url_number)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        # Поиск URL-адреса изображения комикса.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Не удалось найти изображение комикса.')
        else:
            comic_url = f"https:{comic_elem[0].get('src')}"
            print(f'Загрузка изображения {comic_url}')
            res = requests.get(comic_url)
            res.raise_for_status()

            # Сохранение изображения в папке ./xkcd под именем значении переменной comic_url.
            image_file = os.path.join('xkcd', os.path.basename(comic_url))
            with open(image_file, 'wb') as f:
                for chunk in res.iter_content(100_000):
                    f.write(chunk)


# Создание и запуск объектов Thread.
download_threads = []
# 14 итераций, создающих 14 потоков.
for i in range(0, 1400, 100):
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()

# Ожидание завершения всех потоков выполнения.
for download_thread in download_threads:
    download_thread.join()

print('Готово.')
