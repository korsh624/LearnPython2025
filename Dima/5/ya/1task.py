'''
Строится четверичная запись числа N.
Далее эта запись обрабатывается по следующему правилу:
a) если число N делится на 4, то к этой записи справа дописываются
две последние четверичные цифры
б) если число N на 4 не делится, то вычисляется сумма цифр
полученной четверичной записи, эта сумма умножается на 4,
переводится в четверичную систему счисления и дописывается
в конец числа Полученная таким образом запись является
четверичной записью искомого числа R.
Результат переводится в десятичную систему и выводится на экран.
'''
def to_base(n,base) -> str:
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

def f(n):
    n_qw=to_base(n,4)
    if n%4==0:
        if len(n_qw) >= 2:
            n_qw += n_qw[-2:]
        else:
            n_qw += n_qw
    else:
        sumdigit=0
        for char in n_qw:
            sumdigit+=int(char)
        sumdigit=to_base(sumdigit*4,4)
        n_qw +=sumdigit
    return int(n_qw,4)
for i in range(212,1000):
    r=f(i)
    if r>211 and r%3==0 and r%2==0:
        print(r)
        break
R = 212
found=False
while True:
    if R % 2 == 0 and R % 3 == 0:  # четное и кратно 3
        for N in range(1, 1000):  # проверяем возможные N
            if f(N) == R:
                print(R)
                found = True
                break
        if found:
            break
    R += 2  # идем к следующему четному числу