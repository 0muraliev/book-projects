spam = ['apple', 'bananas', 'tofu', 'cats', 'dogs', 'mothers']


def output(lst):
    lst[-1] = f'and {lst[-1]}'
    print(', '.join(lst))


# def output(lst):
#     spi = ''
#     for i in lst:
#         if i != lst[-1]:
#             spi += f'{i}, '
#         else:
#             spi += f'and {lst[-1]}.'
#
#     print(spi)


output(spam)
