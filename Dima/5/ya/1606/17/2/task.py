'''
В файле содержится последовательность целых чисел. Её элементы могут принимать целые значения
от -100 000 до 100 000 включительно. Определите количество пар последовательности,
в которых только один из элементов является пятизначным числом, a квадрат суммы элементов пары
превышает квадрат максимального пятизначного элемента последовательности, оканчивающегося на 37.
В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('17 .txt')as f:
    lines=f.readlines()
digits=[]
for line in lines:
    digits.append(int(line))
print(*digits)
max_37 = None
for num in digits:
    abs_num = abs(num)
    if 10000 <= abs_num <= 99999 and abs_num % 100 == 37:
        if max_37 is None or abs_num > max_37:
                max_37 = abs_num
print(max_37)
count=0
maxsum=0
for i in range(0,len(digits)-1):
    a,b=digits[i],digits[i+1]
    cond1=(a+b)**2>max_37**2
    cond2=len(str(a))!=len(str(b))
    cond3=len(str(a))==5 or len(str(b))==5
    if cond1 and cond2 and cond3:
        count+=1
        maxsum=max(maxsum,digits[i]+digits[i+1])
print(count,maxsum)