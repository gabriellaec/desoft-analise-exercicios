def quantos_uns(x):
    i=0
    soma=0
    y=str(x)
    while i<len(y):
        if y[i]==1:
            soma+=1
        i+=1
    return soma
    
