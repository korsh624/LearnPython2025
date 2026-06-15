n=2*2187**567+729**566-2*243**565+81**564-2*27**563-6561
count=0
while n>0:
    digit=n%27
    if digit%2==0 and digit>9:
        count+=1
    n=n//27
print(count)
