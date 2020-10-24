def verifica_progressao(lista_numeros):
    if len(lista_numeros) < 2:
        return 'NA'
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i + 1] - lista_numeros[i] == lista_numeros[i - 1] - lista_numeros[i - 2]:
            PA = True
        else:
            PA = False
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i + 1] / lista_numeros[i] == lista_numeros[i - 1] / lista_numeros[i - 2]:
            PG = True
        if lista_numeros[i] == 0:
            PG = False
        else:
            PG = False
    if PA == True and PG == True:
        return 'AG'
    if PA == True:
        return 'PA'
    if PG == True:
        return 'PG'
    else:
        return 'NA'