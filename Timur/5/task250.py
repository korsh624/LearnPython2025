def get_R(N):
    binary = bin(N)[2:]  # двоичная запись без '0b'

    for _ in range(3):
        count_0 = binary.count('0')
        count_1 = binary.count('1')

        if count_0 == count_1:
            # добавляем последнюю цифру
            binary += binary[-1]
        else:
            # добавляем цифру, которая встречается реже
            if count_0 < count_1:
                binary += '0'
            else:
                binary += '1'

    return int(binary, 2)  # переводим в десятичную систему


# Ищем наименьшее N > 60
N = 61
while True:
    R = get_R(N)
    if R % 2 == 0 and R % 4 != 0:  # чётное, но не делится на 4
        print(N)
        break
    N += 1
