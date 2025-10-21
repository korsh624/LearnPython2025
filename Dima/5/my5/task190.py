def alg(n):
    n=bin(n)[2:]
    count1=n.count('1')
    count0=n.count('0')
    if count1>count0:
        n=n+'1'
    else:
        n=n+'0'
    res=int(n,2)
    return res
for i in range(100):
    res=alg(i)
    if res>36:
        print(res)
        break
