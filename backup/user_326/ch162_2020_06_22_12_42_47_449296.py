def verifica_lista(lista):
    par = False
    impar = False
    for num in lista:
        if num % 2 == 0:
            par = True
        else:
            impar = True
    if par and not impar:
        return 'par'
    elif impar and not par:
        return 'ímpar'
    else:
        return 'misturado'