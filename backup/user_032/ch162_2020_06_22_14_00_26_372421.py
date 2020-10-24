def verifica_lista(lista):
    par = False
    impar = False
    for x in lista:
        if x %2 == 0:
            par = True
        else:
            impar = True
    if par and not impar:
        return 'par'
    elif impar and not par:
        return 'impar'
    else:
        return 'misturado'