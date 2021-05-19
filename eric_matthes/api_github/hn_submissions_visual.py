import requests
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# Обработка информации о каждой статье.
submission_ids = r.json()
submissions_comments, submissions_links = [], []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    response_dict = r.json()

    try:
        submissions_comments.append(response_dict['descendants'])
    except KeyError:
        print(f'Нет комментариев на странице с id: {submission_id}.')
    else:
        submissions_title = response_dict['title']
        submissions_links.append(f'<a href="http://news.ycombinator.com/item?id={submission_id}">'
                                 f'{submissions_title}</a>')

data = [{
    'type': 'bar',
    'x': submissions_links,
    'y': submissions_comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Hacker News Top Stories',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Title',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')
