# читаем файл
with open("17.txt") as f:
    nums = [int(x) for x in f]


# функция проверки "трехзначное и оканчивается на 9"
def is_special(x):
    return (100 <= abs(x) <= 999) and (abs(x) % 10 == 9)


# находим максимальный элемент, оканчивающийся на 42
max_42 = max(x for x in nums if abs(x) % 100 == 42)

count = 0
max_sum = -10 ** 18

# перебор троек
for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]

    special_count = sum(is_special(x) for x in (a, b, c))

    if special_count == 1:
        s = a + b + c
        if s > max_42:
            count += 1
            max_sum = max(max_sum, s)

print(count, max_sum)