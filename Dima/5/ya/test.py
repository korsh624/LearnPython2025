def to_decimal(s, base):
    return int(s, base)


for x in range(29):
    num1 = f"463{x}7921"
    num2 = f"8241{x}153"

    val = int(num1, 29) + int(num2, 29)

    if val % 28 == 0:
        print("x =", x)
        print("Ответ:", val // 28)
        break
