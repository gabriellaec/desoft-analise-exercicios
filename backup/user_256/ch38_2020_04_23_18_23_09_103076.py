import math
def quantos_uns(n):
    ene = str(n)
    soma=0
    for algarismos in ene:
        if '1' in algarismos:
            soma+=1
    print (soma)
    return soma
        