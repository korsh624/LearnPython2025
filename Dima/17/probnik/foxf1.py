'''
В файле содержится последовательность целых чисел.
Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
Определите количество пар последовательности, в которых только одно число оканчивается на 7,
а квадрат суммы элементов пары не меньше квадрата минимального элемента последовательности,
оканчивающегося на 7. В ответе запишите два числа через пробел:
сначала количество найденных пар, затем максимальный из квадратов сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('fox1.txt', 'r') as file:
    lines = file.readlines()
numbers = []
for line in lines:
    numbers.append(int(line))

min_end7=None
for number in numbers:
    if abs(number)%10==7:
        if min_end7 is None or number < min_end7:
            min_end7 = number

if min_end7==None:
    print('0 0')
    exit()
min_square=min_end7*min_end7
counter=0
max_sum_square=0

for i in range(len(numbers)-1):
    a,b=numbers[i],numbers[i+1]
    a_end7=abs(a)%10==7
    b_end7=abs(b)%10==7
    if a_end7!=b_end7:
        squaresum=(a+b)**2
        if squaresum>min_square:
            counter+=1
            if squaresum>max_sum_square:
                max_sum_square=squaresum
print(counter , max_sum_square)




