def zera_negativos(valores):
    for i in valores:
        if i<0:
            valores[i] = 0
    return (valores)