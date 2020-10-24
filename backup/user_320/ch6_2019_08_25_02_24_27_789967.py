def encontra_maximo(matriz):
    max = -999999
    for linha in matriz:
        for elemento in linha:
            if abs(elemento) > max:
                max = abs(elemento)
    return max