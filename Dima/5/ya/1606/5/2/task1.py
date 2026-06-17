def f(n):
    nbin=bin(n)[2:]
    sumbin=nbin.count('1')
    if sumbin%2==0:
        nbin='10'+nbin[2:]+'0'
    else:
        nbin = '11' + nbin[2:] + '1'
    return int(nbin,2)
maxn=0
for i in range(1000):
    r=f(i)
    if r<=19:
        maxn=i
print(maxn)

