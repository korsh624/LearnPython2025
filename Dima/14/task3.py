def find_bases(number, last_digit):
    # Находим все делители числа (number - last_digit)
    diff = number - last_digit
    bases = []
    for b in range(1, diff + 1):
        if diff % b == 0 and b > last_digit:
            bases.append(b)
    return sorted(bases)

# Параметры задачи
number = 39
last_digit = 3

# Получаем результат
result = find_bases(number, last_digit)
print(", ".join(map(str, result)))