board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def draw_board(b):
    """Вырисовывает доску для игры в крестики-нолики."""
    print(f"{b['top-L']}|{b['top-M']}|{b['top-R']}")
    print('-+-+-')
    print(f"{b['mid-L']}|{b['mid-M']}|{b['mid-R']}")
    print('-+-+-')
    print(f"{b['low-L']}|{b['low-M']}|{b['low-R']}")


turn = 'X'
for i in range(9):
    draw_board(board)
    print(f'Turn for {turn}. Move on which space?')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

draw_board(board)
