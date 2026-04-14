max_zeros = -1
best_x = None

for x in range(1, 3501):
    # позиции единиц
    p1 = 457
    p2 = 48 - x

    # если степень отрицательная — пропускаем
    if p2 < 0:
        continue

    # создаём массив цифр (как столбик сложения)
    length = p1 + 2
    digits = [0] * length

    digits[p1] += 1
    digits[p2] += 1

    # делаем переносы по основанию 12
    for i in range(length):
        if digits[i] >= 12:
            carry = digits[i] // 12
            digits[i] %= 12
            digits[i + 1] += carry

    zeros = digits.count(0)

    if zeros > max_zeros:
        max_zeros = zeros
        best_x = x

print("Ответ:", best_x)