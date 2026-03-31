def to_base4(n):
    """Перевод числа n в четвертичную систему, возвращает строку"""
    if n == 0:
        return '0'
    digits = ''
    while n > 0:
        digits = str(n % 4) + digits
        n //= 4
    return digits

def from_base4(s):
    """Перевод строки s из четверичной системы в десятичную"""
    return int(s, 4)

def generate_r(n):
    """Применяем алгоритм Хадачи"""
    base4 = to_base4(n)
    if base4[-1] == '0':  # последняя цифра в base4
        if len(base4) >= 2:
            base4 += base4[-2:]
        else:
            base4 += base4
    else:
        digit_sum = sum(int(d) for d in base4)
        add = to_base4(digit_sum * 4)
        base4 += add
    return from_base4(base4)

# ищем минимальное R > 211, которое четное и кратно 3
R = 212  # минимальное четное > 211

while True:
    if R % 2 == 0 and R % 3 == 0:  # четное и кратно 3
        for N in range(1, 1000):  # проверяем возможные N
            if generate_r(N) == R:
                print(R)
                found = True
                break
        if found:
            break
    R += 2  # идем к следующему четному числу