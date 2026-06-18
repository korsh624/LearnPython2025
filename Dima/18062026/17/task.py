with open('17.txt') as f:
    lines=f.readlines()
digits=[]
for line in lines:
    digits.append(int(line))
print(digits)
min2el=1000
for digit in digits:
    if digit < min2el and 9<digit<100:
        min2el=digit
print(min2el)
count=0
maxsum=0
for i in range(len(digits)-1):
    a,b=digits[i],digits[i+1]
    if ((len(str(a))==2 and len(str(b))!=2) or (len(str(a))!=2 and len(str(b))==2)) and (a+b)%min2el==0:
        count+=1
        maxsum=max(maxsum,a+b)
print(count, maxsum)