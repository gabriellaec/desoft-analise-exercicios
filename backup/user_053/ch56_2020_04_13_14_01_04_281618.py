import math

def calcula_norma(vetor):
    soma_quadrados = (vetor[0])**2 + (vetor[1])**2 + (vetor[2])**2
    raiz = math.sqrt(soma_quadrados)
    return raiz