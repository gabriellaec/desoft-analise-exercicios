import math
def quantos_uns(n):
    num = str(n)
    soma=0
    i=0
    while i<num:
        if num[i]==1:
            soma+=1
            i+=1    
        else:
            i+=1
    return soma
    