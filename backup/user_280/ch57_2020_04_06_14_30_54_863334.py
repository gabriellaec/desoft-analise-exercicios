import math
def verifica_progressao(lista):
    str(len(lista)) = l
    for i in range(l - 1):
        PG = False
        PA = False
        AG = False
        NA = False
        if lista[i] == math.sqrt(lista[i-1]*lista[i+1]) and lista[i] == (lista[i-1] +lista[i+1])/2:
            AG = True
            y = AG
        if lista[i] == math.sqrt(lista[i-1]*lista[i+1]) and lista[i] != (lista[i-1] +lista[i+1])/2:
            PG = True
            y = PG
        if lista[i] != math.sqrt(lista[i-1]*lista[i+1]) and lista[i] == (lista[i-1] +lista[i+1])/2:
            PA = True
            y = PA
        if lista[i] != math.sqrt(lista[i-1]*lista[i+1]) and lista[i] != (lista[i-1] +lista[i+1])/2:
            NA = True
            y = NA
    return y
 
 
