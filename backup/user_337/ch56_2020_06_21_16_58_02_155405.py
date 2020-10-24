from math import * 
def calcula_norma(lista):
    a = 0
    for i in lista:
        a += i**2
    norma = sqrt(a)
    return norma