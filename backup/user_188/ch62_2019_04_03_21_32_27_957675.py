def filtra_positivos(reais):
    positivos = []
    contador = 0
    while contador < len(reais):
        if reais[contador] > 0:
            positivos.append(reais[contador])
        contador += 1
    return positivos