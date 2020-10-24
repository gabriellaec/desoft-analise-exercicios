def quantos_uns(x):
    x=str(x)
    i=0
    soma=0
    while i<(len(x)-1):
        if x[i]==1:
            soma+=1
        i+=1
    return soma