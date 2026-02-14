''' Укажите через запятую в порядке возрастания все основания систем счисления,
в которых запись числа 22 оканчивается на 4'''
def find_bases(number, last_digit):
    diff=number-last_digit
    bases=[]
    for i in range(1,diff+1):
        if diff%i==0 and i > last_digit:
            bases.append(i)
    return sorted(bases)

number=22
last_digit=4
result=find_bases(number,last_digit)
print(result)
print(', '.join(map(str,result)))