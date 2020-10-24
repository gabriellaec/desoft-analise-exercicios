valores = [2, 3, 7, -8, 1, -9]
def zera_negativos(valores):
    print(valores)
    i = 0
    while i < len(valores):
        if valores[i] < 0:
            valores[i] = 0
            i+=1