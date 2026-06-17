def solve(filename):
    with open(filename, 'r') as f:
        data = list(map(int, f.read().split()))

    # Шаг 1: Находим максимальное пятизначное число, оканчивающееся на 37
    max_37 = None
    for num in data:
        abs_num = abs(num)
        if 10000 <= abs_num <= 99999 and abs_num % 100 == 37:
            if max_37 is None or abs_num > max_37:
                max_37 = abs_num

    if max_37 is None:
        print("В последовательности нет пятизначных чисел, оканчивающихся на 37")
        return
    print(max_37)
    max_square = max_37 ** 2
    count = 0
    max_sum = float('-inf')

    # Шаг 2: Проходим по парам (соседним элементам)
    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]

        # Проверяем условие на пятизначность (только один элемент пятизначный)
        is_a_five = 10000 <= abs(a) <= 99999
        is_b_five = 10000 <= abs(b) <= 99999

        if is_a_five != is_b_five:  # XOR: только один истинен
            pair_sum = a + b
            if pair_sum ** 2 > max_square:
                count += 1
                if pair_sum > max_sum:
                    max_sum = pair_sum

    print(count, max_sum)


# Вызов функции (замените 'input.txt' на имя вашего файла)
solve('17 .txt')
