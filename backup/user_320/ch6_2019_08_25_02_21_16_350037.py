def encontrar_maximo(matriz):
    max = -999999
    for linha in matriz:
        for elemento in linha:
            if elemento > max:
                max = elemento
    return max