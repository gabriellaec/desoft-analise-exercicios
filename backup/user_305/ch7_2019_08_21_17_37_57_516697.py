def calcula_norma(lista):
    s = 0
    for i in lista:
        s += i**2
    y = s**(1/2)
    return y