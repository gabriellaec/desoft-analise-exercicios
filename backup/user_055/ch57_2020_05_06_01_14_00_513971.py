def verifica_progressao(lista_numeros):
    PA = True
    PG = True
    if len(lista_numeros) < 3:
        return 'NA'
    if lista_numeros[0] == 0:
        PG = False
    r = (lista_numeros[1] - lista_numeros[0])
    q = (lista_numeros[1] / lista_numeros[0])
    for i in range(len(lista_numeros) - 1):
        if r != (lista_numeros[i + 1] - lista_numeros[i]):
            PA = False
        if q != (lista_numeros[i + 1] / lista_numeros[i]):
            PG = False
    if PA == True and PG == True:
        return 'AG'
    if PA == True and PG == False:
        return 'PA'
    if PA == False and PG == True:
        return 'PG'