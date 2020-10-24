from math import *

def calcula_norma(vetor):
    lista2 = []
    for i in vetor:
        lista2.append(i**2)
    return sqrt(sum(lista2))