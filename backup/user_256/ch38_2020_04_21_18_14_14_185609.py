import math
def quantos_uns(n):
    lista = [n]
    soma=0
    i=0
    while i<n:
        if lista[i]==1:
            soma+=1
            i+=1    
        else:
            i+=1
    return soma
    