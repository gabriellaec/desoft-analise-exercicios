def quantos_uns(x):
    i=0
    soma=0
    while i<len(str(x)):
        if x[i]==1:
            soma+=1
    return soma
    
