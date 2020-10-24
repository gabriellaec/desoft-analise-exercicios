from math import sqrt
def calcula_norma(vetor):
    soma=0
    for comprimento in vetor:
        soma=soma+comprimento**2
    return sqrt(soma)