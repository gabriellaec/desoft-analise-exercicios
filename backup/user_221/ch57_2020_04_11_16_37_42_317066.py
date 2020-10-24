import math
def verifica_progressao(lista):
    for i in range(len(lista)):
        if lista [i-1] == lista[i]:
            return 'AG'
        elif lista[i-1] == (lista[i] + lista[i-2])/2:
            return 'PA'
        elif lista[i-1] == math.sqrt(lista[i]*lista[i-2]):
            return 'PG'
        else:
            return 'NA'