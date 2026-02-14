'''2)	В системе счисления с некоторым основанием число 12 записывается в виде 110. Укажите это основание.'''
def convert_from_base(digits, base):
    result=0
    for digit in digits:
        result = result * base + digit
    return result

digits=[1,1,0]
target_dec=12
for i in range(2,21):
    dec_value=convert_from_base(digits, i)
    if dec_value==target_dec:
        print(i)
        break
