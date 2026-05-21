"""
В файле содержится последовательность целых чисел. 
Элементы последовательности могут принимать целые значения 
от -100000 до 100000 включительно. 

Определите количество троек элементов последовательности, 
в которых хотя бы один из трёх элементов оканчивается на 17, 
а сумма модулей элементов тройки не больше максимального 
положительного элемента последовательности, оканчивающегося на 17.

В ответе запишите количество найденных троек, затем 
минимальную из сумм элементов таких троек.
Под тройкой подразумеваются три идущих подряд элемента.
"""

with open('17 (6).txt') as file:
    lines = file.readlines()

numbers = []
for i in lines:
    numbers.append(int(i.strip()))

max_elem=0
for x in numbers:
    if x>0 and x%100==17:
        if x>max_elem:
            max_elem=x
print(max_elem)
count=0
minsum=None

for i in range(len(numbers)-2):
    a = numbers[i]
    b = numbers[i+1]
    c = numbers[i+2]
    
    if (abs(a) % 100 == 17) or (abs(b) % 100 == 17) or (abs(c) % 100 == 17):
        if abs(a) + abs(b) + abs(c)<=max_elem:
            count+=1
            s=a+b+c
            if minsum is None or s<minsum : # небыло проверки  на минимальность
                minsum=s

print(count, minsum)