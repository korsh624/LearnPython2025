def f(n):
    nbin=bin(n)[2:]
    for i in range(2):
        nbin+=str(nbin.count('1')%2)
    return int(nbin,2)
for i in range(100):
    res=f(i)
    if res>253:
        print(i)
        break