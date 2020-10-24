from math import sqrt

def calcula_norma(vetor):
    return sqrt(sum([x**2 for x in vetor]))