def verifica_lista(lista):
    impar = False 
    par = False
    for num in lista:
        if num % 2 == 0:
            par = True
        else:
            impar = True
    if impar and par:
        return 'misturado'
    elif par:
        return 'par'
    elif impar:
        return 'ímpar'
    else:
        return 'misturado'