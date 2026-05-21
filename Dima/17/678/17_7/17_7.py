with open('17 (7).txt') as file:
    lines = file.readlines()
numbers = []
for i in lines:
    numbers.append(int(i.strip()))

# Среднее арифметическое
s = 0
for x in numbers:
    s += x
avg = s / len(numbers)

maxs = -10**9
cnt = 0

for i in range(1, len(numbers)-2):   # ← здесь было ошибка
    p1 = numbers[i] * numbers[i+1]
    p0 = numbers[i-1] * numbers[i]
    p2 = numbers[i+1] * numbers[i+2]
    
    if p1 > p0 and p1 > p2:
        sm = numbers[i] + numbers[i+1]
        if sm > maxs:
            maxs = sm
        if numbers[i] > avg or numbers[i+1] > avg:
            cnt += 1

print(maxs, cnt)