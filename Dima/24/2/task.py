'''
Текстовый файл состоит из заглавных букв латинского алфавита.
Определите в прилагаемом файле минимальное количество идущих подряд символов
(длину непрерывной подпоследовательности), среди которых символ E встречается не менее 155 раз.
В ответе запишите число — количество символов в найденной последовательности.
Для выполнения этого задания следует написать программу.
'''
with open('24.txt')as file:
    f=file.readline().strip()
# print(f)
count=0
left=0
mine=float('inf')
for right in range(len(f)):
    if f[right]=='E':
        count+=1
    while count>=155:
        current_length = right - left + 1
        if current_length < mine:
            mine = current_length
        if f[left]=='E':
            count-=1
        left+=1

print(mine)