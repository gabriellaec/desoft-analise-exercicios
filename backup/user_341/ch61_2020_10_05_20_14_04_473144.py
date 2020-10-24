def filtra_positivos(lista):
    liss = []
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            liss.append(lista[i])
            i = i + 1
        else:
            i = i + 1
          