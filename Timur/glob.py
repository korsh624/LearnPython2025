count=0
def f(n):
    global count
    print("*"*n)
    count+=10

def func(n):
    global count
    print("**"*n)
    count+=20

f(10)
func(10)
f(10)
func(10)
f(10)
func(10)
print(count)