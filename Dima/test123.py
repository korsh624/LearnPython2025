def convert_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(n % base)
        n = n // base
    # Преобразуем цифры > 9 в буквы для наглядности, но для проверки просто выводим числа
    digit_symbols = [str(d) if d < 10 else f"[{d}]" for d in reversed(digits)]
    print(digit_symbols)
    return ''.join(digit_symbols)

# Проверяем основания 5, 30 и 40
for base in [5, 30, 40]:
    num_in_base = convert_to_base(63, base)
    ends_with_23 = num_in_base.endswith("23")
    print(f"Основание {base}: {num_in_base} -> оканчивается на '23': {ends_with_23}")
