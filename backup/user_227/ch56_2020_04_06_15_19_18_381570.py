from math import *
def calcula_norma(dimensão):
    soma=0
    for i in dimensão:
        i*=i
        soma+=i
    return sqrt(soma)