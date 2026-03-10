'''
Файл содержит последовательность неотрицательных целых чисел, не превышающих
 10000. Назовём парой два идущих подряд элемента последовательности.
 Определите количество пар, в которых хотя бы один из двух элементов делится
  на 5 и хотя бы один из двух элементов меньше среднего арифметического
  всех элементов последовательности, значение которых нечетно.
  В ответе запишите два числа: сначала количество найденных пар,
  а затем — максимальную сумму элементов таких пар.
'''
with open('17.txt', 'r') as f:
    lines = f.readlines()
decimal=[]
for line in lines:
    decimal.append(int(line))
print(decimal)
nechet=[]
for dec in decimal:
    if dec%2==0:
        nechet.append(dec)
avg=sum(nechet)/len(nechet)
count=0
maxsumm=0

for i in range(len(decimal)-1):
    a,b=decimal[i],decimal[i+1]
    cond1= a%5==0 or b%5==0
    cond2=a<avg or b<avg
    if cond1 and cond2:
        count+=1
        if maxsumm<a+b:
            maxsumm=a+b
print(count, maxsumm)