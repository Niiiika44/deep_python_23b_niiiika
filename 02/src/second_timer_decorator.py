from collections import deque
from time import time


def mean(k: int):
    if not isinstance(k, int):
        raise TypeError("k should be int")
    if k <= 0:
        raise ValueError("k should be greater than 0")

    times = deque([], k)

    def inner(func):
        def wrapper(*args, **kwargs):
            start = time()
            res = func(*args, **kwargs)
            end = time() - start

            times.append(end)

            print(f'The average execution time for {k}',
                  f'recent calls is {sum(times)/len(times)} seconds.')

            return res
        return wrapper
    return inner
