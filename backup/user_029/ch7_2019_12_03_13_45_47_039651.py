def calcula_norma(lista):
    n  =  0
    for i in lista:
        n += (i**2)
    modulo = n**(1/2)
    return modulo

