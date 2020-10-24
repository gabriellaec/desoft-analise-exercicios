def soma_impares(x):
    soma=0
    i=0
    while i<len(x):
        if x[i]/2 is float:
            i+=1
        else:
            soma+=x[i]
            i+=1
    return soma 
            