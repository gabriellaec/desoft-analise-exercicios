def verifica_progressao(lista):
    r = lista[1] - lista[0]
    PA = True
    PG = True

    for i in range(len(lista)-1):
        rn = (lista[i+1]) - (lista[i])
        if rn != r:
            PA = False

    if 0 not in lista:
        q = lista[1]/lista[0]
        for i in range(len(lista)-1):
            qn = lista[i+1]/lista[i]
            if qn != q:
                PG = False
    else:
        PG = False

    if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    else:
        return "NA"