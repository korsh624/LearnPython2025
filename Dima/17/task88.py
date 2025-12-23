"""
88) (Е. Джобс) Рассматривается множество целых чисел, принадлежащих числовому отрезку [54123; 75321],
которые имеют ровно 5 делителей в диапазоне [10;20]. Найдите количество таких чисел и максимальное из них.
"""
import math
def coun_divisors_in_range(n,low,high):
    count=0
    divisors=set()
    for i in range(1, int(math.sqrt(n)+1)):
        # print(i)
        if n%i==0:
            divisors.add(i)
            divisors.add(n//i)
    for i in divisors:
        if low<=i<=high:
            count+=1
    if count==5:
        return True
    else:
        return False

valid=[]
for i in range(54123,75322):
    if coun_divisors_in_range(i,10,20):
        valid.append(i)
print(len(valid), max(valid))

