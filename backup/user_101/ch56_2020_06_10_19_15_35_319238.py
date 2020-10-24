from math import sqrt
def calcula_norma(vetor):
    norma = 0
    for e in vetor:
        norma += e**2
    return sqrt(norma)