# считываем данные из файла
with open("17 (6).txt") as f:
    nums = [int(x) for x in f]

# максимальный положительный элемент, оканчивающийся на 17
max17 = max(x for x in nums if x > 0 and x % 100 == 17)
print(max17)
count = 0
min_sum = 10**20

# перебираем тройки подряд идущих элементов
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]

    # проверка: хотя бы одно число оканчивается на 17
    has17 = any(abs(x) % 100 == 17 for x in triple)

    # сумма модулей
    sum_abs = sum(abs(x) for x in triple)

    if has17 and sum_abs <= max17:
        count += 1

        s = sum(triple)
        min_sum = min(min_sum, s)

print(count, min_sum)