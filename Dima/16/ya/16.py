import sys

sys.setrecursionlimit(1000000)
from functools import lru_cache
def G(n):
    if n >= 250000:
        return n // 20 + 45
    # сколько шагов нужно до >= 250000
    k = (250000 - n + 8) // 9
    m = n + 9 * k
    return m // 20 + 45 - 2 * k

@lru_cache(None)
def F(n):
    if n >= 25:
        return F(n - 6) + 4137
    return 7 * (G(n - 9) - 40)


print(F(680))