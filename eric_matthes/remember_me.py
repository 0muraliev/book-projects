import json


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("Как тебя зовут? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    answer = input(f'Здравствуй, тебя зовут {username}? ')
    if username and answer == 'да':
        print(f"С возвращением, {username}!")
    else:
        username = get_new_username()
        print(f"Мы будем помнить тебя, когда ты вернешься, {username}!")


greet_user()
