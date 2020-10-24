def verifica_lista (lista):
    if lista == []:
        return 'misturado'
    i = 0
    par = True
    impar = True
    while i < len(lista):
        if lista[i] == 0 or lista[i] %2 == 0:
            impar = False
        if lista[i] == 1 or lista[i] %2 != 0:
            par = False
        i += 1
    if par == True:
        return 'par'
    elif impar == True:
        return 'ímpar'
    else:
        return 'misturado'