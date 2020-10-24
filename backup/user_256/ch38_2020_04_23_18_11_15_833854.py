import math
def quantos_uns(n):
    soma=0
    i=0
    for algarismos in n:
        if algarismos[i]==1:
            soma+=1
            i+=1    
        else:
            i+=1
    return soma
    