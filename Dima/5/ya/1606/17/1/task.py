'''
В файле содержится последовательность целых чисел. Её элементы могут принимать целые значения
от -100 000 до 100 000 включительно. Определите количество пар последовательности,
в которых элементы не равны, а абсолютное значение их разности делится на минимальный
положительный элемент последовательности, кратный 35.
Гарантируется, что такой элемент последовательности есть.
В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('17.txt')as f:
    lines=f.readlines()
digits=[]
for line in lines:
    digits.append(int(line))
print(*digits)
minItem35=100000
for digit in digits:
    if digit>0 and digit%35==0:
        minItem35=min(minItem35,digit)
print(minItem35)
count=0
maxsum=-10**9
for i in range(0,len(digits)-1):
    a,b=digits[i],digits[i+1]
    if a!=b and abs(a-b)%minItem35==0:
        count=count+1
        maxsum=max(maxsum,a+b)
print(count, maxsum)