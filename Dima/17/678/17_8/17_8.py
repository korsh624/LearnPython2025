with open('17 (8).txt') as f:
    lines = f.readlines()
n = []
for i in lines:
    n.append(int(i.strip()))

m = 10000
for x in n:
    if 100 <= abs(x) <= 999 and x % 10 == 8:
        if x < m:
            m = x
t = m * m
c = 0
ms = -10**9
for i in range(len(n)-2):
    a,b,c = n[i], n[i+1], n[i+2]
    
    if not (100<=abs(a)<=999 or 100<=abs(b)<=999 or 100<=abs(c)<=999):
        k = 0
    if a*a>t:
        k+=1
    if b*b>t:
        k+=1
    if c*c>t:
        k+=1
    
    if k==2:
        s=a+b+c
        c+=1
        if s>ms:
            ms=s
print(c, ms)