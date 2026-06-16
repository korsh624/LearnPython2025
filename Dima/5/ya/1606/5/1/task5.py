def f(n):
    nbin=bin(n)[2:]
    if n%2==0:
        nbin='11'+nbin[2:]+'0'
    else:
        nbin+=str(nbin.count('1')%2)
    return int(nbin,2)
for i in range(21,10000):
    r=f(i)
    if r>154:
        print(i)
        break