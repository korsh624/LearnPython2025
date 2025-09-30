for i in range(256):
    r=bin(i)[2:].zfill(8)
    ri=''
    for char in r:
        if char == "0":
            ri+='1'
        else:
            ri+='0'
    if int(ri,2) - i ==113:
        print(i)