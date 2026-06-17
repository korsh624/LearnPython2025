from sys import setrecursionlimit
setrecursionlimit(1000000)
def G(n):
    if n>25:
        return G(n-4)+n
    else:
        return 2*(n+1)
def F(n):
    return G(n-1)-G(n-5)
print(F(150774))