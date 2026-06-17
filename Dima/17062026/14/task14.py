for x in range(3000, 0, -1):  # Перебираем от 3000 вниз
    n = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    count_zeros = 0

    while n > 0:
        if n % 11 == 0:  # Если последняя цифра 0
            count_zeros += 1
        n //= 11  # Отбрасываем последнюю цифру

    if count_zeros == 60:
        print(x)
        break
