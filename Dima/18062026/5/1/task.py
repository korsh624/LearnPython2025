def f(n):
    binn = bin(n)[2:]
    if n % 3 == 0:
        binn += binn[-3:]
    else:
        binn += bin((n % 3) * 3)[2:]
    return int(binn, 2)
for i in range(100, 0, -1):
    r = f(i)
    if r < 76:
        print(i)
        break
