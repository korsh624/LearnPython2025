with open('17.txt')as file:
    lines=file.readlines()
# print(lines)
# print(type(lines[0]))
numbers=[]
for line in lines:
    numbers.append(int(line))
print(numbers)
count=0
maxsumm=0
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        if i==j:
            continue
        s=numbers[i]+numbers[j]
        if s%120==0:
            count+=1
            maxsumm=max(maxsumm,s)
print(count//2, maxsumm)