'''17)	В системе счисления с некоторым основанием десятичное число 49 записывается в виде 100. Укажите это основание.'''
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))

for i in range(2,20):
    print(i)
    res=to_base(49,i)
    print(i, res)
    if res == "100":
        print(i)
        break