import math

def calcula_norma(vetor):
    x = vetor[0] - vetor[2]
    y = vetor[1] - vetor[3]
    return math.sqrt((x**2)+(y**2))