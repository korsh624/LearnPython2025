def alg(n):
    c = bin(n)[2:]
    newstr = ''
    for char in c:
        if char == '1':
            newstr += '0'
        else:
            newstr += '1'
    newsrt = newstr.lstrip('0')
    res = int(newstr, 2)
    return res

for i in range(100):
    print(alg(i))
