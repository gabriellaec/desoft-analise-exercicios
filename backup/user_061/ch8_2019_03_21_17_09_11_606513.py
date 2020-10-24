import math

def verifica_pa(PA):
    i = 1
    while i<(len(PA)-1):
        if PA[i] == (PA[i+1] + PA[i-1])/2:
            i+=1
        else:
            return False
    return True

def verifica_pg(PG):
    i = 1
    while i<(len(PG)-1):
        if PG[i] == math.sqrt(PG[i+1]*PG[i-1]):
            i+=1
        else:
            return False
    return True

def verifica_progressao(lista):
    if (verifica_pa(lista) == True) and (verifica_pg(lista) == True):
        return "AG"
    elif (verifica_pa(lista) == True) and (verifica_pg(lista) == False):
        return "PA"
    elif (verifica_pa(lista) == False) and (verifica_pg(lista) == True):
        return "PG"
    else:
        return "NA"