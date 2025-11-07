count=0
def F( n ):
    global count
    print('*')
    count+=1
    if n >= 1:
        print('*')
        count+=1
        F(n - 1)
        F(n - 2)

F(12)
print(count)
