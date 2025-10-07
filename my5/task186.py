def alg(N):
    nbit=bin(N)[2:].zfill(8)
    poinlasttone=None
    for i in range(len(nbit)):
        if nbit[i] == '1':
            pointlastone = i

    toinvert=nbit[:pointlastone]
    noinvert=nbit[pointlastone:]
    invert=''
    for char in toinvert:
        if char == '1':
            invert+='0'
        else:
            invert+='1'
    res=invert+noinvert
    res=int(res,2)
    return res
print(alg(211))

