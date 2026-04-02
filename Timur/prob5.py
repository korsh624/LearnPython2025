def f(n):
    s = bin(n)[2:]
    cnt = s.count('1')
    if cnt % 2 == 0:
        ans = '10' + s
        ans = ans[:len(ans) - 1] + '1'
    else:
        ans = '1' + s
        ans = ans[:len(ans) - 2] + '11'
    return int(ans, 2)


n = 1
while f(n) <= 62:
    n += 1
print(n, f(n))