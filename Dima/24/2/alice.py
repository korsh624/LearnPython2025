with open('24.txt', 'r') as f:
    s = f.readline().strip()

left = 0
count_E = 0
min_length = float('inf')  # Изначально устанавливаем очень большое значение

# Проходим по строке правой границей окна
for right in range(len(s)):
    # Если текущий символ — 'E', увеличиваем счётчик
    if s[right] == 'E':
        count_E += 1

    # Пока в окне достаточно 'E', пытаемся сузить его слева
    while count_E >= 155:
        # Обновляем минимальную длину, если текущая меньше
        current_length = right - left + 1
        if current_length < min_length:
            min_length = current_length

        # Сдвигаем левую границу вправо
        if s[left] == 'E':
            count_E -= 1
        left += 1

# Если min_length не обновилось, подходящих подпоследовательностей нет
if min_length == float('inf'):
    print(0)
else:
    print(min_length)
