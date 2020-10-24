def verifica_progressao(lista):
    PA = False
    PG = False
    for i in lista:
        if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:
            PA = True
        elif lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            PG = True
    if lista[i+1]-lista[i]==lista[i+2]-lista[i+1] and lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
        return 'AG'

    elif PA and PG:
        return 'NA'
    elif PA:
        return 'PA'
    else:
        return 'PG'