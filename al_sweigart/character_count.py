import pprint

message = 'Давным-давно...в мире, где происходили войны между кланами орков и людьми...' \
          'родился дракон...'
count = {}

for character in message.lower():
    """Подсчитывает кол-во повторений каждого символа, встречающегося в сообщении."""
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
