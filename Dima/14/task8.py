def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))
bases=[]
for base in range(2, 101):
    res=to_base(27, base)
    if res[-1]=='3':
        bases.append(base)
print(bases)