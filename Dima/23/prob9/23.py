'''
Исполнитель Август21 преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
За какое минимальное количество команд можно получить из числа 3 число 89?
'''
def findMin(start, stop):
    if start == stop:
        return 0
    if start > stop:
        return float('inf')
    dey1=findMin(start+1,stop)
    dey2=findMin(start*2,stop)
    dey3=findMin(start*3,stop)
    result = 1 + min(dey1,dey2,dey3)
    return result
minsteps=findMin(3,89)
print(minsteps)