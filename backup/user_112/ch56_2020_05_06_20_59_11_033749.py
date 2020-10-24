import math

def calcula_norma(vetor):
    for n in vetor:
        norma = math.sqrt(vetor[n] ** 2 + vetor[n] ** 2)
        return norma
        
        