def filtra_positivos(lista):
    nova_l =[]
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            nova_l.append(lista[i])
        i += 1
    return nova_l