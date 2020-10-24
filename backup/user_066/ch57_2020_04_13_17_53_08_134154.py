def verifica_progressao(lista):
    constanteA1 = lista[3] - lista[2]
    constanteA2 = lista[2] - lista[1]
    constanteG1 = lista[3]/lista[2]
    constanteG2 = lista[2]/lista[1]
    if constanteA1 == constanteA2:
        PA = True
    else:
        PA = False
    if constanteG1 == constanteG2:
        PG = True
    else:
        PG = False
    if PA and PG:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG:
        return 'PG'
    else:
        return 'NA'