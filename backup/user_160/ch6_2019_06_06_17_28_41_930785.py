def encontra_maximo(matriz):
    maior = abs(matriz[0][0])
    for linha in matriz:
        for numero in linha:
            if abs(numero) > abs(maior):
                maior = abs(numero)
    return maior
