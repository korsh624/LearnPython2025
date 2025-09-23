def alg(n):
    if n%2==0:
        n=str(bin(n))[2:]+'01'
    else:
        n=str(bin(n))[2:]+'10'
    return int(n,2)
target = 62
ans = None
for N in range(1, 1000):
    R = alg(N)
    if R > target:
        ans = R
        break

print(ans)  # выведет 65
