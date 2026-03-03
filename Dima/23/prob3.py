def f(start, stop):
    if start<stop:
        return 0
    if start==stop:
        return 1
    if start>stop:
        return f(start-4,stop)+f(start//2, stop)
print(f(74,10)*f(10,2))