def quantos_uns(x):
    uns=0
    alg=str(x)
    i=0
    while i<len(alg):
        if alg[i]=='1':
            uns+=1
        i+=1
    return uns