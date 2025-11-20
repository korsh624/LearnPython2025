'''
7)	Рассматривается множество целых чисел, принадлежащих отрезку [200; 9120], которые делятся на 8 и не делятся на 7, 11, 17 и 19.
Найдите количество таких чисел и минимальное из них. В ответе запишите два числа через пробел: сначала количество, затем минимальное число.
'''
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

valid=[]
for i in range(200,9121):
    if i%8==0 and i%7==0 and i%11!=0 and i%17!=0 and i%19!=0:
        valid.append(i)

print(len(valid), min(valid))

