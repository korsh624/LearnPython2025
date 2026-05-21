# считываем числа из файла
with open("17 (7).txt") as f:
    nums = [int(x) for x in f]

# среднее арифметическое всех чисел
avg = sum(nums) / len(nums)

max_sum = -10**20
count = 0

# перебираем пары
# первая и последняя пары не рассматриваются
for i in range(1, len(nums) - 2):

    pair_prod = nums[i] * nums[i + 1]

    # произведения соседних пар
    prev_prod = nums[i - 1] * nums[i]
    next_prod = nums[i + 1] * nums[i + 2]

    # условие задачи
    if pair_prod > prev_prod and pair_prod > next_prod:

        # максимальная сумма пары
        pair_sum = nums[i] + nums[i + 1]
        max_sum = max(max_sum, pair_sum)

        # хотя бы одно число больше среднего
        if nums[i] > avg or nums[i + 1] > avg:
            count += 1

print(max_sum, count)