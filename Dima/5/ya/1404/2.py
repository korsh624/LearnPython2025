def to_base3(n):
    res = ""
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res


def from_base3(s):
    return int(s, 3)


for n in range(3, 1000):
    s = to_base3(n)

    first = int(s[0])
    last = int(s[-1])

    if first == last:
        s += str(first)
    else:
        s += str(max(first, last))

    r = from_base3(s)

    if r > 49:
        print("Ответ:", n)
        break