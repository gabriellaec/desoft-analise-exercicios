def verifica_lista(lista):
    par = True
    impar = True
    for valor in lista:
        if valor%2 == 0:
            impar = False
        else:
            par = False
            
    if par and not impar:
        return "par"
    if impar and not par:
        return "ímpar"
    return "misturado"