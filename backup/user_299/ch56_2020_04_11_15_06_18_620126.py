import math
def calcula_norma(lista):
    lista_quadrados = []
    soma = 0
    for e in lista:
        lista_quadrados.append(e**2)
        soma = soma + lista_quadrados[-1]
    norma = math.sqrt(soma)
    return norma