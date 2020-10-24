def verifica_lista(lista):
    par = True
    impar = True
    for valor in lista:
        if valor%2 == 0:
            impar = False
        else:
            par = False
    if par not in impar:
        return "par"
    if impar not in par:
        teturn "ímpar"
    return "misturado"