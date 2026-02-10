def convert_from_base(digits, base):
    """Переводит число (в виде списка цифр) из системы с основанием `base` в десятичную."""
    result = 0
    for digit in digits:
        result = result * base + digit
    return result

# Заданное число в виде цифр: 110
digits = [1, 1, 0]
target_decimal = 12

# Перебираем основания от 2 до некоторого разумного предела (например, 20)
for b in range(2, 21):
    decimal_value = convert_from_base(digits, b)
    if decimal_value == target_decimal:
        print(f"Основание системы счисления: {b}")
        break
else:
    print("Основание не найдено в заданном диапазоне.")
