'''
Текстовый файл состоит из заглавных букв латинского алфавита
A,B,C,D,E и F.
Определите в прилагаемом файле максимальное количество идущих подряд символов,
среди которых пара символов
BC (в указанном порядке) встречается ровно 190 раз.
В ответе запишите число — количество символов в найденной последовательности.
Для выполнения этого задания следует написать программу.
'''
with open('24.txt')as f:
    l=f.readline().strip()
left=0
count=0
maxlen=0
for right in range(len(l)):
    if right>0 and  l[right-1]=='B' and l[right]=='C':
        count+=1
    while count>190:
        if l[left]=='B' and (l[left+1]=='C' and left + 1 < len(l)):
            count-=1
        left+=1
    maxlen=max(maxlen,right-left+1)
print(maxlen)
