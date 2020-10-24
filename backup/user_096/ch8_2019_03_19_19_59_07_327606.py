import math
def verifica_progressao(lista):
    i=0
    while i<len(lista):
        if (lista[i-1]+lista[i+1])/2==lista[i]:
            return"PA"
        elif (math.sqrt(lista[i-1]+lista[i+1]))==lista[i]:
            return"PG"
        elif (lista[i-1]+lista[i+1])/2==lista[i] and (math.sqrt(lista[i]+lista[i+2]))==lista[i+1]:
            return"AG"
        else:
            return"NA"