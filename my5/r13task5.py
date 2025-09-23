def func(n):
    n=str(bin(n))[2:]
    n=n+str(n.count('1')%2)
    n = n + str(n.count('1') % 2)
    n=int(n,2)
    return n
d=0
while func(d)<78:
    d+=1
print(d)
