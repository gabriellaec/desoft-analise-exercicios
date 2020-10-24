def encontra_maximo(matriz):
    valor_max = 0
    for elemento in matriz:
        for e in elemento:
            if e > valor_max:
                valor_max = e
    return valor_max