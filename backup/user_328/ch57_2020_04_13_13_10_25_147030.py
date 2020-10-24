def verifica_progressao(lista1):
    PG = True
    PA = True
    if len(lista1) < 2:
        return 'NA'
    elif len(lista1) == 2:
        return 'AG'
    elif lista1[0] == 0 and lista1[1] == 0:
        PG = False
    if PA:
        PArazao = lista1[1] - lista1[0]
    if PG:
        PGrazao = lista1[1]/lista1[0]
    while PA:
        for i in range(0,len(lista1)-1):
            if lista1[i+1]-lista1[i] != PArazao:
                PA = False
                break
        break
    while PG:
        for i in range(0,len(lista1)-1):
            if lista1[i+1]/lista1[i] != PGrazao:
                PG = False
                break
        break
    if PG and PA:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG:
        return 'PG'
    else:
        return 'NA'
            