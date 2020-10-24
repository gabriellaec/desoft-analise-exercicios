def verifica_lista(lista):
    if len(lista) == 0:
        return "misturado"
    par = False
    impar = False
    for l in lista:
        if l%2 == 0:
            par = True
        if l%2 != 0:
            impar = True
    if par == True and impar == True:
        return "misturado"
    elif par == True:
        return "par"
    elif impar == True:
        return "ímpar"