import math
def coun_divisors_in_range(n,low,high):
    count=0
    divisors=set()
    for i in range(1, int(math.sqrt(n)+1)):
        if n%i==0:
            divisors.add(i)
            divisors.add(n//i)
    for i in divisors:
        if low<=i<=high:
            count+=1