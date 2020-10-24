def encontra_maximo(matriz):
    maior = matriz[0][0]
    for lista in matriz:
        for numero in lista:
            if numero > maior:
                maior = numero
    return maior