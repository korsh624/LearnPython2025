# Открываем файл и читаем строку
with open('24.txt', 'r') as f:
    s = f.readline().strip()

# Список для хранения индексов начала каждой подстроки 'BC'
bc_positions = []

# Находим все вхождения 'BC' и сохраняем их начальные индексы
for i in range(len(s) - 1):
    if s[i] == 'B' and s[i + 1] == 'C':
        bc_positions.append(i)

# Добавляем фиктивные границы: -1 в начало и len(s) в конец
bc_positions = [-1] + bc_positions + [len(s)]

# Если в строке меньше 190 вхождений 'BC', ответ — 0
if len(bc_positions) - 2 < 190:
    print(0)
else:
    max_length = 0
    # Перебираем все возможные наборы из 190 подряд идущих 'BC'
    for i in range(1, len(bc_positions) - 190):
        # Начало отрезка — позиция после предыдущего 'BC' (или начало строки)
        start = bc_positions[i] + 2  # +2, чтобы пропустить саму 'BC'
        # Конец отрезка — позиция перед следующим 'BC' после 190‑го (или конец строки)
        end = bc_positions[i + 190]
        # Длина отрезка
        length = end - start + 2
        if length > max_length:
            max_length = length
    print(max_length)
