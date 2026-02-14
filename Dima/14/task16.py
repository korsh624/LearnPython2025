'''16)	Десятичное число, переведенное в восьмеричную и в девятеричную систему, в обоих случаях заканчивается на цифру 0.
Какое минимальное натуральное число удовлетворяет этому условию?'''
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))
for n in range(1, 1000):

    to9=to_base(n, 9)
    to8=to_base(n, 8)
    print(n, to9,to8)
    if to9[-1]==to8[-1]=='0':
        print(n)
        break