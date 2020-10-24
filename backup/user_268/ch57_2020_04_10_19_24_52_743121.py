def verifica_progressao(lista):
    a = len(lista)
    for i in range(1, (a)):
        if (lista[i] ** 2) == lista[i - 1] * lista[i+1]:
            PG = True
        elif lista[i] == (lista[i - 1] + lista[i+1])/2:
            PA = True
        else:
            PA = False
            PG = False
            
    if PA and PG:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG :
        return 'PG'
    else:
        return 'NA'