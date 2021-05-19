import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    station_name = next(reader)[header_row.index('NAME')]

    # Получение дат, температурных минимумов и максимумов, а также их индексы.
    date_i = header_row.index('DATE')
    tmax_i = header_row.index('TMAX')
    tmin_i = header_row.index('TMIN')

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_i], '%Y-%m-%d')
        try:
            high = int(row[tmax_i])
            low = int(row[tmin_i])
        except ValueError:
            print(f'Отсутствуют данные за {current_date}.')

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Форматирование диаграммы.
title = f'Daily high and low temperatures - 2018\n{station_name}'
plt.title(title, fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
