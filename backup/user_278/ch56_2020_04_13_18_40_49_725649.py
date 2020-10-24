import math
def calcula_norma (vetor):
    norma = []
    for i in vetor:
        norma.append(i**2)
    return math.sqrt(sum(norma))