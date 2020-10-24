import math
def verifica_progressao(lista):
    l = int(len(lista))
    for i in range(1, l):
        if lista[i] == math.sqrt(lista[i-1]*lista[i+1]) and lista[i] == (lista[i-1] +lista[i+1])/2:
            y = AG
        if lista[i] == math.sqrt(lista[i-1]*lista[i+1]) and lista[i] != (lista[i-1] +lista[i+1])/2:
            y = PG
        if lista[i] != math.sqrt(lista[i-1]*lista[i+1]) and lista[i] == (lista[i-1] +lista[i+1])/2:
            y = PA
        if lista[i] != math.sqrt(lista[i-1]*lista[i+1]) and lista[i] != (lista[i-1] +lista[i+1])/2:
            y = NA
    return y