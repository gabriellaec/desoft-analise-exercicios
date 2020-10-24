def zera_negativos(valores):
    valores_pos=[]
    for i in valores:
        if i < 0.0:
            i = 0.0
            valores_pos.append(i)
    return valores_pos