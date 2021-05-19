players = ['charles', 'martina', 'alfa', 'bravo', 'omega', 'florence', 'lucifer', 'drago', 'relt']
# print(players[1:-1:2])

print('Позвольте представить свою команду:')
my_players = [print(f'\t- {player.upper()}') for player in players[:]]

print('Команда соперников:')
friend_players = players[:]
print(players)
