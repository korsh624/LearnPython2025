'''
В файле содержится последовательность целых чисел. Её элементы могут принимать целые значения от –100 000 до 100 000 включительно.

Определите количество пар последовательности, в которых сумма элементов меньше минимального положительного элемента последовательности,
кратного 123. Гарантируется, что такой элемент в последовательности есть.

В ответе запишите количество найденных пар, затем абсолютное значение максимальной из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
from numpy.ma.core import masked_print_option

with open('17.txt')as file:
    lines=file.readlines()
# print(lines)
# print(type(lines[0]))
numbers=[]
for line in lines:
    numbers.append(int(line))
minitem=101000
for number in numbers:
    if number<minitem and number>0 and number%123==0:
        minitem=number
count=0
maxsum=0
for i in range(len(numbers)-1):
    a,b=numbers[i],numbers[i+1]
    s=a+b
    if s<minitem:
        count+=1
        if s>maxsum:
            maxsum=s
print(count, abs(maxsum))

