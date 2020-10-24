def zera_negativos(valores):
    for i in range(len(valores)):
        if valores[i] < 0.0:
            valores[i] = 0.0
    return valores
