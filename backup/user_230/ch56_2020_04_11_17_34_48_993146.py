def calcula_norma(lista):
    norma=0
    for i in lista:
        norma+=i**2
    return norma**(1/2)