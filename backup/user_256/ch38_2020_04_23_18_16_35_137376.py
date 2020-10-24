import math
def quantos_uns(n):
    p = str(n)
    soma=0
    i=0
    for algarismos in p:
        if algarismos[i]==1:
            soma+=1
        i+=1    
    return soma