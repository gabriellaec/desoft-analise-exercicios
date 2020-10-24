def zera_negativos(valores):
    i = 0
    while i < len(valores):
        if valores[i] < 0:
            valores[i] = 0
        i += 1
    return valores
print(zera_negativos([-4,0,3,4]))