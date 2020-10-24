def verifica_lista(numeros):
    if numeros == []:
        return 'misturado'
    impar = True
    par = True
    i = 1
    while i < len(numeros):
        if numeros[i] % 2 != 0:
            par = False
        if numeros[i] % 2 == 0:
            impar = False
        i += 1
    if par:
        return 'par'
    elif impar:
        return 'ímpar'
    else:
        return 'misturado'