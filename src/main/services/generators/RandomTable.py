import random


def get_table(size):
    random.seed()
    result = [random.randint(1, 100) for _ in range(size)]
    return result
