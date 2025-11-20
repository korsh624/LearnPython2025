'''
38)	(Д.Ф. Муфаззалов, г. Уфа) Определите количество различных значений n таких, что n и m – натуральные числа,
а значение F(n, m) равно числу 30
'''
def F(n,m):
 if m == 0:
  d = 0
 else:
  d = n+F(n, m-1)
 return d

count=0
for n in range(1, 31):
    for m in range(1, 31):
        if F(n, m) == 30:
            count+=1
print(count)

