'''
Задание 23
Исполнитель преобразует число на экране.
У исполнителя есть три команды, которые обозначены латинскими буквами:
A. Прибавить 1
B. Прибавить 2
C. Умножить на 2
Программа для исполнителя – это последовательность команд.
Сколько существует программ, для которых при исходном числе 3 результатом является число 18, при этом траектория
вычислений содержит число 14 и не содержит 8?


'''
def count_programs(start, end):
    # Если превысили конечное число — путь неверный
    if start > end:
        return 0

    # Если попали на запрещённое число 8 — путь неверный
    if start == 8:
        return 0

    # Если достигли конечного числа — нашли одну программу
    if start == end:
        return 1

    # Рекурсивно считаем количество программ для каждого действия
    count_a = count_programs(start + 1, end)  # Команда A: +1
    count_b = count_programs(start + 2, end)  # Команда B: +2
    count_c = count_programs(start * 2, end)     # Команда C: ×2

    # Суммируем количество программ для всех вариантов
    return count_a + count_b + count_c

# Параметры задачи
start_number = 3
intermediate_number = 14
target_number = 18

# Этап 1: от 3 до 14 без прохождения через 8
paths_1 = count_programs(start_number, intermediate_number)

# Этап 2: от 14 до 18 (все числа > 14, поэтому 8 не встретится)
paths_2 = count_programs(intermediate_number, target_number)

# Общее количество программ
total_paths = paths_1 * paths_2

print(f"Количество программ от {start_number} до {intermediate_number}: {paths_1}")
print(f"Количество программ от {intermediate_number} до {target_number}: {paths_2}")
print(f"Общее количество программ: {total_paths}")
