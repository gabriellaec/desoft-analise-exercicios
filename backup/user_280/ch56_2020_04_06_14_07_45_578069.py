import math

def calcula_norma(vetor):
    maracatu = 0
    for i in range(len(vetor)):
        maracatu += vetor[i]**2
    modulo = math.sqrt(maracatu)
    return modulo