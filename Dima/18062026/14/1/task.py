digits = '0123456789ABCDEFGHI'
xmax = 0
rxmax = 0
for i in range(19):
    x_char = digits[i]
    n1 = f'98897{x_char}21'
    n2 = f'2{x_char}923'
    r = int(n1, 19) + int(n2, 19)
    if r % 18 == 0:
        xmax = i
        rxmax = r

print(rxmax // 18)
