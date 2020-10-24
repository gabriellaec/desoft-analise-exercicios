from math import sqrt

def calcula_norma(lista):
    norma = 0
    l = []
    i = 0
    while i<len(lista):
        l.append(lista[i]**2)
        i+=1
    soma = sum(l)
    norma = sqrt(soma)
    return norma