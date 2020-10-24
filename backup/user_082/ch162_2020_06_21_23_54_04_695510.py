def verifica_lista(lista):
    par = False
    impar = False

    for i in lista:
        if i % 2 == 0:
            par = True
        if i % 2 != 0:
            impar = True

    if par and impar:
        return('misturado')
    elif par:
        return('par')
    elif impar:
        return('ímpar')