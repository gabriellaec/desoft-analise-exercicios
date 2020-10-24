import math
def calcula_norma(vetor):

    lista = []
    for c in vetor:
        lista.append(c**2)
    return math.sqrt(sum(lista))