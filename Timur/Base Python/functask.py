def F(x):
    return x**2

def myfunc(i):
    s=str(i)
    n=s.count('0')
    i=i*n
    return i, n

x,y=myfunc(500)
print(x,y)
print(myfunc(1000))