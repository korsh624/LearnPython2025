def solve_task(filename):
    # Шаг 1: Читаем последовательность из файла
    with open(filename, 'r') as file:
        numbers = list(map(int, file.readlines()))

    # Шаг 2: Находим максимальный четырёхзначный элемент, заканчивающийся на 86
    max_four_digit_86 = -1  # Инициализируем значением, заведомо меньшим любого возможного

    for num in numbers:
        # Проверяем, что число четырёхзначное и заканчивается на 86
        if 1000 <= num <= 9999 and num % 100 == 86:
            if num > max_four_digit_86:
                max_four_digit_86 = num

    # Гарантируется, что такой элемент есть, поэтому проверка на отсутствие не требуется

    # Шаг 3: Ищем пары подряд идущих элементов, удовлетворяющие условиям
    print(max_four_digit_86)
    count_pairs = 0
    min_sum = float('inf')  # Инициализируем бесконечностью, чтобы первая подходящая сумма стала минимумом

    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]
        current_sum = a + b

        # Проверяем условия:
        # 1. Хотя бы один элемент чётный
        # 2. Сумма меньше максимального четырёхзначного числа, заканчивающегося на 86
        if (a % 2 == 0 or b % 2 == 0) and current_sum < max_four_digit_86:
            count_pairs += 1
            if current_sum < min_sum:
                min_sum = current_sum

    # Шаг 4: Возвращаем результат: количество пар и минимальная сумма
    return count_pairs, min_sum


# Пример использования:
# Замените 'numbers.txt' на путь к вашему файлу с данными
result = solve_task('17.txt')
print(f"{result[0]} {result[1]}")
