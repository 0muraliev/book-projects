import cProfile


def calc_prod():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


cProfile.run('calc_prod()')
