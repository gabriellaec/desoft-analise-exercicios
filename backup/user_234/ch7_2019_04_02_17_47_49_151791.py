import math
def calcula_norma(lista):
    soma_quad=0
    for comprimento in lista:
        soma_quad += comprimento**2
    modulo = math.sqrt(soma_quad)
    return modulo