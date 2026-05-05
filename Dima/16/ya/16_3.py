import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n<10:
        return n
    else:
        return 3*n+f(n-3)
res=(f(650)+2*f(6244))/f(6238)
print(res)