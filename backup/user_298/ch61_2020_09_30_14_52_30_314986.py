def filtra_positivos(lista_reais):
    lista_positivos = []
    t = 0
    while t < len(lista_reais):
        if lista_reais[t] > 0:
            lista_positivos.append(lista_reais[t])
        t += 1
    return lista_positivos