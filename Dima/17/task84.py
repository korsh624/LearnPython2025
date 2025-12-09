candidates = []
divisors = [5, 11, 17, 19]
for i in range(10000, 20001):
    count=0
    for j in divisors:
        if i%j==0:
            count+=1
    if count==2:
        candidates.append(i)
print(len(candidates), min(candidates))
