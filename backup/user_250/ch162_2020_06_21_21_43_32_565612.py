def verifica_lista(lista):
    par = True
    impar = True
    for i in lista:
        if i%2 == 0:
            impar = False
        if i%2 != 0:
            par = False
    if par == True and impar == False:
        return 'par'
    if par == False and impar == True:
        return 'ímpar'
    else:
        return 'misturado'