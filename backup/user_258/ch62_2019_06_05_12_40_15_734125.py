def filtra_positivos(lista_reais):
    lista_positivos = []
    for k in lista_reais:
        if k > 0:
            lista_positivos.append(k)
    return lista_positivos