def verifica_lista(lista):
    par = True
    impar = True
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            impar = False
        else:
            par = False
    if len(lista) == 0:
        return 'misturado'
    elif par == False and impar == True:
        return 'ímpar'
    elif par == True and impar == False:
        return 'par'
    else:
        return 'misturado'