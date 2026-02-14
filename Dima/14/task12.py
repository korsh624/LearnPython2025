'''12)	Укажите, сколько всего раз встречается  цифра 3 в записи чисел 19, 20, 21, …, 33 в системе счисления с основанием 6.'''
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))
finishstring=''
for i in range(19, 34):
    result = to_base(i, 6)
    finishstring += result
print(finishstring.count('3'))
