import math
def verifica_pa(lista):
    for i in range(1, len(lista) - 2):
        if lista[i] == (lista[i-1] +lista[i+1])/2:
            return True
        else:
            return False

def verifica_pg(lista):
    for i in range(1, len(lista) - 2):
        if lista[i] == math.sqrt(lista[i-1]*lista[i+1]):
            return True
        else:
            return False

def verifica_progressao(lista):
    if verifica_pa(lista):
        if verifica_pg(lista):
            return 'AG'
        else:
            return 'PA'
    else:
        if verifica_pg(lista):
            return 'PG'
        else:
            return 'NA'