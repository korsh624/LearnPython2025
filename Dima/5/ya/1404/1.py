def to_base8(n):
    return oct(n)[2:]

def from_base8(s):
    return int(s, 8)

max_n = 0

for n in range(8, 1000):  # запас с головой
    s = to_base8(n)

    if n % 2 == 0:
        s = s + s[-1]
    else:
        if len(s) > 1:
            s = s[-1] + s[1:-1] + s[0]
        # если одна цифра — ничего не меняется

    r = from_base8(s)

    if r < 254:
        max_n = n

print("Ответ:", max_n)