def encontra_maximo(matriz):
    maior = abs(matriz[0][0])
    for lista in matriz:
        for numero in lista:
            if abs(numero) > maior:
                maior = abs(numero)
    return maior