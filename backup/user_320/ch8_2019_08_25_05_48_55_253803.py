def verifica_PA(lista):
    dif = lista[1] - lista[0]
    for i in range(2, len(lista)):
        dif2 = lista[i] - lista[i - 1]
        if dif2 != dif:
            return False
    return True

def verifica_PG(lista):
    if lista[0] == 0:
        return False
    dif = (lista[1] / lista[0]) ** (1/(2 - 1))
    for i in range(2  , len(lista)):
        dif2 = (lista[i] / lista[0]) ** (1/i) 
        if ads(dif2) != abs(dif):
            return False
    return True

def verifica_progressao(lista):
    if verifica_PA(lista):
        return 'PA'
    elif verifica_PG(lista):
        return 'PG'
    return 'NA'
