import math
def quantos_uns(n):
    soma=0
    i=0
    for algarismos in n:
        if 1 in algarismos:
            soma+=1
    return soma
        