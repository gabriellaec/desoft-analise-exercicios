def filtra_positivos(n):
    lista_positivos = []
    i = 0
    while i < len(n):
        if n[i] > 0:
            lista_positivos.append(n[i])
        i += 1
    return lista_positivos    