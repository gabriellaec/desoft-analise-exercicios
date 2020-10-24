def verifica_lista(lista):
    par = True
    impar = True
    if len(lista) == 0:
        return 'misturado'
    for numero in lista:
        if numero%2 == 0:
            impar = False
        else:
            par = False
    if par == True  and impar == False:
        return 'par'
    elif impar == True:
        return 'impar'
    else:
        return 'misturado'