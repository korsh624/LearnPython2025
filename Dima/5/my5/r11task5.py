def alg(x):
  s = bin(x)[2:]
  return x - int( s[1:], 2 )

res=[]
for i in range(500,5001):
    res.append(alg(i))
# print(len(res))
res=set(res)
print(len(res))
