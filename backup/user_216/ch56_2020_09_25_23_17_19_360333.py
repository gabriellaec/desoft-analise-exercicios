def calcula_norma(lista):
    modulo = 0
    for e in lista:
        modulo += e

    if modulo < 0:
        modulo = -modulo
    return modulo