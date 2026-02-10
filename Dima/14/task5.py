def find_base(decimal_num, digits_str):
    """
    Находит основание системы счисления b, при котором
    десятичное число decimal_num записывается как digits_str в системе с основанием b.

    Args:
        decimal_num: целое число в десятичной системе (например, 129)
        digits_str: строка с цифрами числа в неизвестной системе (например, "1004")

    Returns:
        Основание b или None, если не найдено
    """
    # Перебираем основания от 2 до разумного предела (например, 20)
    for b in range(2, 21):
        # Переводим digits_str из системы с основанием b в десятичную
        value = 0
        for digit_char in digits_str:
            digit = int(digit_char)
            value = value * b + digit

        # Если получили искомое десятичное число — возвращаем основание
        if value == decimal_num:
            return b
    return None  # Основание не найдено


# Параметры задачи
decimal_number = 129
digits = "1004"

# Ищем основание
base = find_base(decimal_number, digits)

# Выводим результат
if base is not None:
    print(f"Основание системы счисления: {base}")
else:
    print("Основание не найдено в заданном диапазоне.")
