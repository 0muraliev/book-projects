import threading
import time

print('Начало программы.')


def nap():
    time.sleep(5)
    print('Проснись!')


thread_obj = threading.Thread(target=nap)
thread_obj.start()

print('Конец программы.')
