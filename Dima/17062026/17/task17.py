'''
В файле содержится последовательность целых чисел. Её элементы могут принимать целые значения от –100 000 до 100 000 включительно.
Определите количество троек последовательности, в которых все числа одного знака, при этом произведение минимального и максимального
элементов тройки больше квадрата минимального элемента последовательности, который оканчивается на 15 и является трёхзначным числом.
В ответе запишите количество найденных троек чисел, затем минимальное из произведений максимального и минимального элементов таких троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
with open('17.txt')as file:
    lines=file.readlines()
digits=[]
for line in lines:
    digits.append(int(line))
print(digits)
minel15=float('inf')
for digit in digits:
    if digit < minel15 and abs(digit)%100==15 and 99<abs(digit)<1000:
        minel15=digit
print(minel15)
print(minel15**2)
minel15=minel15**2
count=0
minmaxmin=10**9
for i in range(len(digits)-2):
    a,b,c=digits[i],digits[i+1],digits[i+2]
    if (a>0 and b>0 and c>0) or (a<0 and b<0 and c<0):
        if min(a,b,c)*max(a,b,c)>minel15:
            count+=1
            minmaxmin=min(minmaxmin,min(a,b,c)*max(a,b,c))
print(count,minmaxmin)

