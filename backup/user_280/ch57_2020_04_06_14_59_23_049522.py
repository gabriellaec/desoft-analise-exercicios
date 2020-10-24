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
    if verifica_pa(lista) == True and verifica_pg(lista) == True:
        return 'AG'
    if verifica_pa(lista) == True and verifica_pg(lista) == False:
        return 'PA'
    if verifica_pa(lista) == False and verifica_pg(lista) == True:
        return 'PG'
    if verifica_pa(lista) == False and verifica_pg(lista) == False:
        return 'NA'
