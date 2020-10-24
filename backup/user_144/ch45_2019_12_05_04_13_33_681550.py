def zera_negativos(valores):
    valores_pos=[]
    i = 0
    n = len(valores)
    while i < n:
        if valores[i] < 0.0:
            valores[i] = 0.0
            valores_pos.append(valores[i])
            i += 1
    return valores_pos