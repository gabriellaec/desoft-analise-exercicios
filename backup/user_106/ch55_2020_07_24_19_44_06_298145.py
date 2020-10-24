import math

def encontra_maximo(lista_matriz):
    maior = abs(lista_matriz[0][0])
    for i in lista_matriz:
        for n in i:
            if abs(n) > maior:
                maior = abs(n)
    return maior