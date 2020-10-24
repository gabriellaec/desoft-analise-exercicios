def filtra_positivos(valores):
    valores_pos = []
    for i in range(len(valores)):
        if valores[i] > 0.0:
            valores_pos.append(valores[i])
    return valores_pos
