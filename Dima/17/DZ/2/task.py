# Параметры задачи
d = 160  # делитель для проверки остатков
p = 7  # делитель для проверки кратности

with open('17.txt', 'r') as f:
    lines = f.readlines()
numbers=[]
for line in lines:
    numbers.append(int(line))
count_pairs = 0
max_sum = 0

# Перебираем все возможные пары различных элементов
n = len(numbers)
for i in range(n):
    for j in range(i + 1, n):  # j всегда больше i — избегаем дубликатов и пар с одинаковыми индексами
        a, b = numbers[i], numbers[j]

        # Проверяем первое условие: различные остатки от деления на d=160
        remainder_a = a % d
        remainder_b = b % d
        different_remainders = (remainder_a != remainder_b)

        # Проверяем второе условие: хотя бы одно число делится на p=7
        divisible_by_p = (a % p == 0) or (b % p == 0)

        # Если оба условия выполнены
        if different_remainders and divisible_by_p:
            count_pairs += 1
            current_sum = a + b
            if current_sum > max_sum:
                max_sum = current_sum

# Выводим результат: сначала количество пар, затем максимальную сумму
print(count_pairs, max_sum)
