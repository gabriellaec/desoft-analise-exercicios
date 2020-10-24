def verifica_lista (numeros):
    if len(numeros) == 0:
        return 'misturado'
    i = 0
    par = True
    impar = True
    while i < len(numeros):
        a = numeros[i]
        if a%2 == 0:
            impar = False
        if a%2 != 0:
            par = False
        i = i + 1
    if par:
        return 'par'
    elif impar:
        return 'ímpar'
    else:
        return 'misturado'