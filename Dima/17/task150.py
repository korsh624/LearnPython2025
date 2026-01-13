# Открываем файл и считываем числа
with open('files/17-1.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

count = 0  # счётчик подходящих пар
min_sum = None  # минимальная сумма (изначально не определена)

# Проходим по всем соседним парам
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]

    # Проверяем условие задачи
    if (a % 7 == 0 and b % 17 != 0) or (b % 7 == 0 and a % 17 != 0):
        count += 1
        current_sum = a + b
        if min_sum is None or current_sum < min_sum:
            min_sum = current_sum

# Выводим результат
print(count, min_sum)