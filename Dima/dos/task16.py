from sys import setrecursionlimit
setrecursionlimit(10**9)
def f(n):
    if n<10:
        return 3
    else:
        return (n+4)*f(n-5)
res=(f(257487)//683+f(257477)//67)//f(257472)
print(res)