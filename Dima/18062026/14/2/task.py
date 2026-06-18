n=2*2401**525+3*343**524-4*49**523+5*49**522-6*7**521-35
count=0
while n>0:
    r=n%49
    if r<=9:
        count+=1
    n=n//49
print(count)