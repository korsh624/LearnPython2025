valid=[]
for i in range(1234567, 7654322):
    ml_r=i%100
    st_r=i//100000
    try:
        if i%(st_r-ml_r)==0:
            valid.append(i)
    except Exception as e:
        pass
print(len(valid), max(valid))


