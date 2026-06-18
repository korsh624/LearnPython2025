def f(n):
    nbin=bin(n)[2:]
    if n%2==0:
        nbin='1'+nbin+'0'
    else:
        nbin='11'+nbin+'11'
    return int(nbin,2)
minr=10**9

for i in range(1000):
    r=f(i)
    if r>48:
        minr=min(minr,r)
print(minr)
