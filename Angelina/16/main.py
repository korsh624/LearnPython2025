def factorial(n):
    if n==0 or n==1:  # тот случай когда рекурсия не вызывается
        return 1
    else:
        return n*factorial(n-1) # тот случай когда функция вызывает сама ссебя

print(factorial(10000000000))