import csv

from plotly import offline
from plotly.graph_objs import Layout

# Изучение структуры данных.
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lat_i = header_row.index('latitude')
    lon_i = header_row.index('longitude')
    bright_i = header_row.index('bright_ti4')

    lats, lons, brights = [], [], []
    for row in reader:
        try:
            lat = row[lat_i]
            lon = row[lon_i]
            bright = float(row[bright_i])

        except ValueError:
            print(f'Отсутствуют данные в строке: {row}')

        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Нанесение данных на карту.
data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'text': brights,
    'marker': {
        'size': [bri/40 for bri in brights],
        'color': brights,
        'colorscale': 'YlOrRd',
        'colorbar': {'title': 'Brightness (F)'},
    },
}]

my_layout = Layout(title='Global Fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
