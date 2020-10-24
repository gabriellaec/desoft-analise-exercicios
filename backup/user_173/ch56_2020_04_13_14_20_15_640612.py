from math import *
def calcula_norma (lista1):
    lista2 = []
    for i in lista1:
        lista2.appemd(i**2)
    return sqrt(sum(lista2))