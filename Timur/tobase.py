def tobase(n, base):
    res=''
    if n==0:
        return '0'
    while n>0:
        r=n%base
        res=str(r)+res
        n=n//base
    return res
print(bin(143)[2:])
print(tobase(143,2))