with open('17.txt') as f:
    a = [int(x) for x in f]

# 🔹 1. минимальное трёхзначное, оканчивается на 8
m = min(x for x in a if 100 <= abs(x) <= 999 and abs(x) % 10 == 8)
print(m)
limit = m * m

count = 0
max_sum = -10 ** 20

# 🔹 2. перебор троек
for i in range(len(a) - 2):
    x, y, z = a[i], a[i + 1], a[i + 2]

    # условие 1: ровно 2 числа
    cond1 = sum(v * v > limit for v in (x, y, z)) == 2

    # условие 2: хотя бы одно трёхзначное
    cond2 = any(100 <= abs(v) <= 999 for v in (x, y, z))

    if cond1 and cond2:
        count += 1
        max_sum = max(max_sum, x + y + z)

print(count, max_sum)