from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Создание кубиков D8.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)


# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.sides + die_2.sides + die_3.sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling a D6 and a D10 50000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
