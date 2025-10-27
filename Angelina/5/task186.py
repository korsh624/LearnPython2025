'''186)	Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N.
2) Инвертируются все разряды исходного числа, кроме последней единицы и стоящих за ней нулей (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Чему равен результат работы алгоритма для N = 211?
'''
def func(n):
    n=bin(n)[2:].zfill(0)
    # 01011000
    pointlastone=None
    for i in range(8):
        if n[i]=='1':
            pointlastone=i
    toinvert=n[:pointlastone]
    noinvert=n[pointlastone:]
    invert=''
    for char in toinvert:
        if char=='1':
            invert+='0'
        else:
            invert+='1'
    res=invert+noinvert
    return int(res,2)
print(func(211))


