def calcula_norma(listavetor):
    n=0
    for i in listavetor:
        n=((i**2+n)**0.5)
    return n