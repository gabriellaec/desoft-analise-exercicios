def quantos_uns(x):
    i=0
    soma=0
    while i<len(str(x)):
        if x[i]==1:
            soma+=x[i]
            i+=1
        return soma
        
        
