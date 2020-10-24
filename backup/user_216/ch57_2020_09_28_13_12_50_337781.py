def verifica_progressao(lista):
    razaoA = [0] * (len(lista) - 1)
    razaoG = [0] * (len(lista) - 1)
    PA = True
    PG = True
    Teste = True

    for e in range(0,len(lista)):
        if lista[e] != lista[e-1]:
            break
        return "AG"


    for e in range(1,len(lista)):
        razaoA[e - 1] = lista[e] - lista[e-1]
    for e in range(0, len(razaoA)):
        if razaoA[e] != razaoA[0]:
            PA = False

    for e in range(0,len(lista)):
        if lista[e] == 0:
            PG = False
            Teste = False
            break

    
    if Teste:
        for e in range(1,len(lista)):
            razaoG[e-1] = lista[e] / lista[e-1]
        for e in range(0, len(razaoG)):
            if razaoG[e] != razaoG[0]:
                PG = False


    if PA and PG:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG:
        return 'PG'
    else:
        return 'NA'