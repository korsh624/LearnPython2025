"""195)  (П. Волгин) В файле 17-9.txt содержится последовательность целых чисел. Элементы последовательности могут принимать значения
 от 0 до 1100 включительно. Определите сначала количество троек элементов последовательности, в которых хотя бы два числа в двоичной 
 системе счисления имеют не менее 3 единиц и эти же два числа в двоичной системе счисления имеют как минимум один ноль, а 
 затем максимальное число среди максимальных чисел в подходящих тройках. Под тройкой подразумевается три идущих подряд элемента 
 последовательности.
"""

def check30(N):
    N=bin(N)[2:]
    count1=N.count("1")
    count0=N.count("0")
    if count1>=3 and count0>=1:
        return True

    

with open("files/17-9.txt") as f:
    lines=f.readlines()

numbers=[]
for i in lines:
    numbers.append(int(i.strip()))

print(numbers)
count=0
maxnum=0
for i in range(len(numbers)-2):
    three=numbers[i:i+3]
    #[145, 687, 344]
    countvalid=0
    for num in three:
        if check30(num):
            countvalid+=1
    if countvalid>=2:
        count+=1
        if max(three)>maxnum:
            maxnum=max(three)
print(count, maxnum)