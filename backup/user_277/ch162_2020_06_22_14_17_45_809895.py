def verifica_lista(lista):
    par = True
    impar = True
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            impar = False
        else:
            par = True
    if len(lista) == 0:
        return 'misturado'
    elif impar:
        return 'par'
    elif par:
        return 'impar'
    else:
        return 'misturado'