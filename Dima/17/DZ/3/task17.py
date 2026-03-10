'''
В файле содержится последовательность из 10000 целых положительных чисел.
 Каждое число не превышает 10000. Определите и запишите в ответе сначала
 количество пар элементов последовательности, разность которых четна
 и хотя бы одно из чисел делится на 31, затем максимальную из
 сумм элементов таких пар. В данной задаче под парой подразумевается
 два различных элемента последовательности.
 Порядок элементов в паре не важен.
'''
from itertools import count

with open('17.txt', 'r') as f:
    lines = f.readlines()
decimal=[]
for line in lines:
    decimal.append(int(line))
count=0
maxsumm=0

# Перебираем все возможные пары различных элементов
n = len(decimal)
for i in range(n):
    for j in range(i + 1, n):  # j всегда больше i, чтобы избежать дубликатов и пар с одинаковыми индексами
        a, b = decimal[i], decimal[j]

        # Вычисляем разность и проверяем, чётная ли она
        difference = abs(a - b)
        is_difference_even = (difference % 2 == 0)

        # Проверяем, делится ли хотя бы одно число на 31
        divisible_by_31 = (a % 31 == 0) or (b % 31 == 0)

        # Если оба условия выполнены
        if is_difference_even and divisible_by_31:
            count += 1
            current_sum = a + b
            if current_sum > maxsumm:
                maxsumm = current_sum

# Выводим результат: сначала количество пар, затем максимальную сумму
print(count, maxsumm)
