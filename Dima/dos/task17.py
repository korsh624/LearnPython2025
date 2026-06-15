with open('17.txt') as f:
    lines = f.readlines()
digits=[]
for line in lines:
    digits.append(int(line))
print(*digits)
minel=10**9
for digit in digits:
    if digit%23==0 and digit<minel:
        minel=digit
print(minel)
count=0
maxsum=0
for i in range(0,len(digits)-1):
    a=digits[i]
    b=digits[i+1]
    if a%minel==0 or b%minel==0:
        count+=1
        maxsum=max(maxsum,a+b)
print(count, maxsum)



