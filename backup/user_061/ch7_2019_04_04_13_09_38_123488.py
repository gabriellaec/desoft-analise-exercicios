import math

def calcula_norma(vetor):
    norma = 0
    for i in range(len(vetor)):
        norma += vetor[i]**2
    return math.sqrt(norma)