with open('17.txt') as f:
    a = [int(x) for x in f]

# 🔹 1. ищем M
M = max(x for x in a if 10000 <= x <= 99999 and x % 100 == 17)
print(M)

count = 0
min_sum = 10 ** 20  # большое число

# 🔹 2. перебор троек
for i in range(len(a) - 2):
    x, y, z = a[i], a[i + 1], a[i + 2]

    # условие 1
    cond1 = (x % 100 == 17) or (y % 100 == 17) or (z % 100 == 17)

    # условие 2
    cond2 = abs(x) + abs(y) + abs(z) <= M

    if cond1 and cond2:
        count += 1
        min_sum = min(min_sum, x + y + z)

print(count, min_sum)