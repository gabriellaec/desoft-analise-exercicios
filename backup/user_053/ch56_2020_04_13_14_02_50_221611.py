import math

def calcula_norma(vetor):
    soma_quadrados = 0
    for elemento in vetor:
        elemento_quadrado = elemento**2
        soma_quadrados += elemento_quadrado
    raiz = math.sqrt(soma_quadrados)
    return raiz