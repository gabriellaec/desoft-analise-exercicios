import math as m 
def verifica_progressao(lista):
    for i in lista:
        if lista[i+1] == (lista[i] + lista[i+2])/2 and lista[i+1] == m.sqrt(lista[i]*lista[i+2]):
            return 'AG'
        if lista[i+1] == (lista[i] + lista[i+2])/2:
            return 'PA'
        if lista[i+1] == m.sqrt(lista[i]*lista[i+2]):
            return 'PG'
        else:
            return 'NA'