import math
def encontra_maximo(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for numero in linha:
            if numero > maior:
                maior = math.fabs(numero)
    return maior
    