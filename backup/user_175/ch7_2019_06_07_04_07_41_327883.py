from math import sqrt
def calcula_norma(vetor):
    soma = 0
    for valor in vetor:
        soma += (valor**2)
    resultado = sqrt(soma)
    return resultado