def encontra_maximo(matriz):
    valor_max = 0
    for elemento in matriz:
        i = 0
        while i <= 3:
            if elemento[i] > valor_max:
                valor_max = elemento[i]
            else:
                i += 1
    return valor_max