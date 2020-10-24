encontra_maximo(lista):
    x = 0
    for n in lista:
        if n>x:
            n = x
    return n