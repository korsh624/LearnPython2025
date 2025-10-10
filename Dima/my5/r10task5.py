def alg(x):
    return x%2*100+x%3*10+x%5
for i in range(10,100):
     if alg(i)==104:
         print(i)
         break