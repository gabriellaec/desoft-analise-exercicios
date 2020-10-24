def verifica_lista (numeros):
    par = True
    impar = True
    if len(numeros) == 0:
        return 'misturado'
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 != 0:
            par == False
        if numeros[i] % 2 == 0:
            impar = False
        i += 1
    if par:
        return 'par'
    elif impar:
        return 'impar'
    else:
        return 'misturado'