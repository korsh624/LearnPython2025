'''18)	Укажите наименьшее основание системы счисления, в которой запись числа 70 трехзначна. '''
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))
for i in range(2,21):
    res=to_base(70, i)
    if len(res)==3:
        print(i)
        break