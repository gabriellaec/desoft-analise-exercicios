def zera_negativos(valores):
    for i in valores:
        if i < 0:
            i = 0
    return valores