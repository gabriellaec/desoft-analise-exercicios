from math import sqrt
def calcula_norma(lista):
    teste = []
    for i in range(len(lista)):
        teste.append(lista[i]**2)
    return abs(sum((teste)))