def to_base(n, base):
    if n == 0:
        return '0'
    digits=[]
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))